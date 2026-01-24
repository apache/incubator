from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st
import altair as alt

# ============================
# Git helpers (use THIS repo)
# ============================

def run_git(repo_dir: Path, args: list[str]) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo_dir), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        env={**dict(os.environ), "GIT_TERMINAL_PROMPT": "0"},
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "git command failed")
    return p.stdout


def resolve_repo_root() -> Path:
    """
    Use the dashboard repo itself as the git root.
    This works locally and on Streamlit Community Cloud.
    """
    cwd = Path.cwd().resolve()
    try:
        p = subprocess.run(
            ["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return Path(p.stdout.strip())
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            "This app must be run from a git checkout.\n"
            f"cwd={cwd}\n{e.stderr}"
        )


_RE_LS_TREE_BLOB = re.compile(r"^\d+\s+blob\s+([0-9a-f]{40})\t(.+)$")


def report_set_commits(repo_dir: Path, reports_dir: str, max_sets: int) -> list[str]:
    out = run_git(repo_dir, ["log", f"--max-count={max_sets}", "--pretty=format:%H", "--", reports_dir])
    return [x.strip() for x in out.splitlines() if x.strip()]


def report_blobs_at_commit(repo_dir: Path, commit: str, reports_dir: str) -> list[tuple[str, str]]:
    out = run_git(repo_dir, ["ls-tree", "-r", commit, reports_dir])
    pairs: list[tuple[str, str]] = []
    for line in out.splitlines():
        m = _RE_LS_TREE_BLOB.match(line.strip())
        if not m:
            continue
        oid, path = m.group(1), m.group(2)
        if path.endswith(".md"):
            pairs.append((path, oid))
    return pairs


def cat_blobs(repo_dir: Path, oids: list[str]) -> dict[str, str]:
    if not oids:
        return {}

    proc = subprocess.Popen(
        ["git", "-C", str(repo_dir), "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.stdin and proc.stdout

    proc.stdin.write(("\n".join(oids) + "\n").encode("utf-8"))
    proc.stdin.flush()

    out: dict[str, str] = {}

    for _ in oids:
        header_b = proc.stdout.readline()
        if not header_b:
            break
        header = header_b.decode("utf-8", errors="replace").strip()
        parts = header.split()
        if len(parts) < 3:
            continue

        got_oid, typ, size_s = parts[0], parts[1], parts[2]
        size = int(size_s) if size_s.isdigit() else 0
        content = proc.stdout.read(size)
        proc.stdout.read(1)  # trailing newline

        if typ == "blob":
            out[got_oid] = content.decode("utf-8", errors="replace")

    proc.stdin.close()
    proc.wait(timeout=120)
    return out


# ============================
# Parsing (based on actual report format)
# ============================

RE_GENERATED_ON = re.compile(r"_Generated on\s+(\d{4}-\d{2}-\d{2})_", re.IGNORECASE)
RE_WINDOW_HEADER = re.compile(r"^###\s+(3m|6m|12m)\b", re.MULTILINE)

RE_RELEASES = re.compile(r"Releases .*?:\s*(\d+)\s*\|\s*Median gap \(days\):\s*([0-9.]+|—)")
RE_CONTRIB = re.compile(r"New contributors:\s*(\d+)\s*\|\s*Unique committers:\s*(\d+)\s*\|\s*Commits:\s*(\d+)")
RE_ISSUES = re.compile(r"Issues:\s*opened\s*(\d+)\s*/\s*closed\s*(\d+)")
RE_PRS = re.compile(r"PRs:\s*opened\s*(\d+)\s*/\s*merged\s*(\d+)\s*\|\s*Median merge time \(days\):\s*([0-9.]+|—)")
RE_REVIEWS = re.compile(
    r"Reviews \(sampled\):.*?median reviewers/PR\s*([0-9.]+|—).*?"
    r"reviewer diversity \(eff\.\#\)\s*([0-9.]+|—).*?"
    r"PR author diversity \(eff\.\#\)\s*([0-9.]+|—).*?"
    r"unique reviewers\s*(\d+|—),\s*unique authors\s*(\d+|—)"
)
RE_BUS = re.compile(r"Bus factor proxy \(50%\s*/\s*75%\):\s*(\d+|—)\s*/\s*(\d+|—)")
RE_REPORTS = re.compile(r"Incubator reports:\s*(\d+|—)\s*\|\s*Avg mentor sign-offs:\s*([0-9.]+|—)")
RE_MAIL = re.compile(r"Mailing lists:\s*dev messages\s*(\d+|—),\s*dev unique posters\s*(\d+|—)")


def _to_int(s: Optional[str]) -> Optional[int]:
    if s is None or s == "—":
        return None
    return int(s)


def _to_float(s: Optional[str]) -> Optional[float]:
    if s is None or s == "—":
        return None
    return float(s)


def strip_md(line: str) -> str:
    return line.replace("**", "").strip()


def parse_window_details_block(bullet_lines: list[str]) -> dict:
    row: dict = {}
    for raw in bullet_lines:
        line = strip_md(raw)
        line = line[2:].strip() if line.startswith("- ") else line

        if line.startswith("Releases "):
            m = RE_RELEASES.search(line)
            if m:
                row["releases"] = _to_int(m.group(1))
                row["median_gap_days"] = _to_float(m.group(2))

        elif line.startswith("New contributors:"):
            m = RE_CONTRIB.search(line)
            if m:
                row["new_contributors"] = _to_int(m.group(1))
                row["unique_committers"] = _to_int(m.group(2))
                row["commits"] = _to_int(m.group(3))

        elif line.startswith("Issues:"):
            m = RE_ISSUES.search(line)
            if m:
                row["issues_opened"] = _to_int(m.group(1))
                row["issues_closed"] = _to_int(m.group(2))

        elif line.startswith("PRs:"):
            m = RE_PRS.search(line)
            if m:
                row["prs_opened"] = _to_int(m.group(1))
                row["prs_merged"] = _to_int(m.group(2))
                row["median_merge_days"] = _to_float(m.group(3))

        elif line.startswith("Reviews (sampled):"):
            m = RE_REVIEWS.search(line)
            if m:
                row["median_reviewers_per_pr"] = _to_float(m.group(1))
                row["reviewer_div_eff"] = _to_float(m.group(2))
                row["pr_author_div_eff"] = _to_float(m.group(3))
                row["unique_reviewers"] = _to_int(m.group(4))
                row["unique_authors"] = _to_int(m.group(5))

        elif line.startswith("Bus factor proxy"):
            m = RE_BUS.search(line)
            if m:
                row["bus50"] = _to_int(m.group(1))
                row["bus75"] = _to_int(m.group(2))

        elif line.startswith("Incubator reports:"):
            m = RE_REPORTS.search(line)
            if m:
                row["reports_count"] = _to_int(m.group(1))
                row["avg_mentor_signoffs"] = _to_float(m.group(2))

        elif line.startswith("Mailing lists:"):
            m = RE_MAIL.search(line)
            if m:
                row["dev_msgs"] = _to_int(m.group(1))
                row["dev_unique_posters"] = _to_int(m.group(2))

    return row


def parse_report(text: str, podling_stem: str) -> list[dict]:
    m = RE_GENERATED_ON.search(text)
    if not m:
        return []
    snapshot_date = m.group(1)

    wd_idx = text.find("## Window Details")
    if wd_idx == -1:
        return []
    wd = text[wd_idx:]

    matches = list(RE_WINDOW_HEADER.finditer(wd))
    out: list[dict] = []

    for i, mm in enumerate(matches):
        window = mm.group(1)
        start = mm.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(wd)
        block = wd[start:end]

        bullet_lines = [ln for ln in block.splitlines() if ln.strip().startswith("- ")]
        metrics = parse_window_details_block(bullet_lines)

        out.append(
            {
                "podling_key": podling_stem.casefold(),  # merge Hamalton/hamalton/etc
                "podling_display": podling_stem,         # keep original for display; latest wins
                "snapshot_date": snapshot_date,
                "window": window,
                **metrics,
            }
        )

    return out


# ============================
# Dataset build (git history)
# ============================

@st.cache_data(show_spinner=True)
def build_dataset(repo_root: str, reports_dir: str, max_commits: int) -> pd.DataFrame:
    repo_dir = Path(repo_root)
    rows: list[dict] = []

    commits = report_set_commits(repo_dir, reports_dir, max_sets=max_commits)
    for commit in commits:
        pairs = report_blobs_at_commit(repo_dir, commit, reports_dir)
        if not pairs:
            continue

        oids = [oid for (_path, oid) in pairs]
        blob_text = cat_blobs(repo_dir, oids)

        for path, oid in pairs:
            text = blob_text.get(oid)
            if not text:
                continue

            podling_stem = Path(path).stem
            for r in parse_report(text, podling_stem):
                r["commit"] = commit
                r["path"] = path
                rows.append(r)

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"], errors="coerce")
    df = df.dropna(subset=["snapshot_date"])

    # de-dupe
    df = df.sort_values(["podling_key", "window", "snapshot_date", "commit"])
    df = df.drop_duplicates(["podling_key", "window", "snapshot_date"], keep="last")

    # ensure one display name per key: latest snapshot wins
    latest_name = (
        df.sort_values(["podling_key", "snapshot_date", "commit"])
        .groupby("podling_key", as_index=False)
        .tail(1)[["podling_key", "podling_display"]]
    )
    df = df.drop(columns=["podling_display"]).merge(latest_name, on="podling_key", how="left")

    return df.reset_index(drop=True)


# ============================
# Latest-only combined snapshot (STRICT)
# - availability and signals come ONLY from the latest snapshot per podling_key
# - windows count ONLY if present in that latest snapshot (no inference)
# ============================

def latest_combo(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    # latest snapshot_date per podling_key
    latest_dates = df.groupby("podling_key", as_index=False)["snapshot_date"].max()
    latest = df.merge(latest_dates, on=["podling_key", "snapshot_date"], how="inner")

    # if multiple commits same day, keep latest commit row per (key, window)
    latest = latest.sort_values(["podling_key", "window", "snapshot_date", "commit"]).groupby(
        ["podling_key", "window"], as_index=False
    ).tail(1)

    keep = ["podling_key", "podling_display", "window", "snapshot_date"]
    metrics = [c for c in latest.columns if c not in (keep + ["commit", "path"])]

    wide = latest.pivot(index="podling_key", columns="window", values=metrics)
    wide.columns = [f"{m}_{w}" for (m, w) in wide.columns]
    wide = wide.reset_index()

    dates = latest.pivot(index="podling_key", columns="window", values="snapshot_date")
    dates.columns = [f"snapshot_date_{w}" for w in dates.columns]
    dates = dates.reset_index()

    names = latest.groupby("podling_key", as_index=False).tail(1)[["podling_key", "podling_display"]]
    out = wide.merge(dates, on="podling_key", how="left").merge(names, on="podling_key", how="left")

    # add single "latest_snapshot_date" (for info / debugging if needed)
    out["latest_snapshot_date"] = latest.groupby("podling_key")["snapshot_date"].max().reindex(out["podling_key"]).values
    return out


# ============================
# Signals + commentary (STRICT latest-only windows)
# ============================

PRIMARY = "primary"
SECONDARY = "secondary"
FYI = "fyi"


def _val(row: pd.Series, key: str) -> Optional[float]:
    v = row.get(key)
    if v is None:
        return None
    if isinstance(v, float) and pd.isna(v):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    return None


def _has_window(row: pd.Series, w: str) -> bool:
    d = row.get(f"snapshot_date_{w}")
    return d is not None and not pd.isna(d)


def window_availability_messages(row: pd.Series) -> list[str]:
    # STRICT: only based on latest snapshot (presence of ### window section in that latest file)
    msgs: list[str] = []
    for w in ["12m", "6m", "3m"]:
        msgs.append(f"- **{w}**: {'available' if _has_window(row, w) else 'not available'}")
    return msgs


def build_signals_latest_only(row: pd.Series) -> list[dict]:
    sig: list[dict] = []

    def add(level: str, text: str):
        sig.append({"level": level, "text": text})

    has3 = _has_window(row, "3m")
    has6 = _has_window(row, "6m")
    has12 = _has_window(row, "12m")

    # pull values ONLY if the window exists
    r6 = _val(row, "releases_6m") if has6 else None
    r12 = _val(row, "releases_12m") if has12 else None

    p3 = _val(row, "dev_unique_posters_3m") if has3 else None
    p12 = _val(row, "dev_unique_posters_12m") if has12 else None

    m3 = _val(row, "dev_msgs_3m") if has3 else None
    m12 = _val(row, "dev_msgs_12m") if has12 else None

    bus3 = _val(row, "bus50_3m") if has3 else None
    committers12 = _val(row, "unique_committers_12m") if has12 else None

    merge3 = _val(row, "median_merge_days_3m") if has3 else None
    merge12 = _val(row, "median_merge_days_12m") if has12 else None

    prs3 = _val(row, "prs_merged_3m") if has3 else None
    revdiv3 = _val(row, "reviewer_div_eff_3m") if has3 else None
    authdiv3 = _val(row, "pr_author_div_eff_3m") if has3 else None

    commits3 = _val(row, "commits_3m") if has3 else None

    # Releases checks: only when the relevant windows exist in the LATEST report
    if has12 and r12 is not None and r12 == 0:
        add(PRIMARY, "No releases in 12m — likely needs mentor/IPMC attention (blockers/ownership/process).")
    elif has6 and has12 and r6 is not None and r6 == 0 and (r12 is not None and r12 > 0):
        add(SECONDARY, "No releases in 6m but releases exist in 12m — check-in: planned pause or emerging blockers?")

    # Participation vs baseline: only compare if BOTH windows exist in the LATEST report
    if has3 and has12 and p3 is not None and p12 is not None and p12 > 0:
        ratio = p3 / p12
        if p12 >= 15 and p3 <= 6 and ratio <= 0.25:
            add(
                SECONDARY,
                "Recent dev@ participation (3m) is materially lower than the 12m baseline — confirm whether discussion moved channels or participation narrowed."
            )

    if has3 and has12 and m3 is not None and m12 is not None and m12 > 0:
        drop = (m12 - m3) / m12
        if m3 <= 20 and drop >= 0.50:
            add(
                FYI,
                "Recent dev@ message volume (3m) is lower than the 12m baseline — interpret alongside other indicators (releases/review activity)."
            )

    # Bus factor: needs 3m and 12m in the LATEST report
    if has3 and has12 and bus3 is not None and bus3 <= 2 and committers12 is not None and committers12 <= 10:
        add(SECONDARY, "Contribution concentration signal (bus50 ≤ 2) with small 12m committer base — check dominance risk.")

    # PR throughput concentration: only needs 3m
    if has3 and prs3 is not None and prs3 >= 50:
        if revdiv3 is not None and revdiv3 <= 3.0:
            add(SECONDARY, "High PR throughput but low reviewer diversity (3m) — are reviews concentrated?")
        if authdiv3 is not None and authdiv3 <= 3.0:
            add(SECONDARY, "Activity concentrated among few PR authors (3m) — is funnel broadening?")

    # Merge time baseline comparison: only if BOTH windows exist in the LATEST report
    if has3 and has12 and merge3 is not None and merge12 is not None and merge12 > 0:
        ch = (merge3 - merge12) / merge12
        if ch >= 0.50 and merge3 >= 7:
            add(SECONDARY, "3m PR merge time much slower than 12m baseline — backlog/review capacity/process change?")
        elif ch >= 0.25 and merge3 >= 7:
            add(FYI, "3m PR merge time trending slower than 12m baseline — FYI (watch next snapshot).")

    # Commit activity vs participation: only needs 3m
    if has3 and commits3 is not None and commits3 >= 100 and (p3 is not None and p3 <= 5):
        add(FYI, "High commit activity with low dev@ participation (3m) — FYI: check on-list socialisation norms.")

    return sig


def signals_summary(sig: list[dict]) -> str:
    if not sig:
        return "—"
    order = {PRIMARY: 0, SECONDARY: 1, FYI: 2}
    sig = sorted(sig, key=lambda x: order.get(x["level"], 9))
    return " • ".join([f"[{s['level']}] {s['text']}" for s in sig])


def draft_commentary_from_latest(pod_display: str, row: pd.Series) -> str:
    sigs = row.get("signals") or []
    order = {PRIMARY: 0, SECONDARY: 1, FYI: 2}
    sigs = sorted(sigs, key=lambda x: order.get(x["level"], 9))

    primary = [s for s in sigs if s["level"] == PRIMARY]
    secondary = [s for s in sigs if s["level"] == SECONDARY]
    fyi = [s for s in sigs if s["level"] == FYI]

    lines: list[str] = []
    lines.append(f"### {pod_display} — health cross-check summary")
    lines.append("")
    lines.append("**Data availability:**")
    lines.extend(window_availability_messages(row))
    lines.append("")
    lines.append("**Indicators:**")

    if not (primary or secondary or fyi):
        lines.append("- —")
        return "\n".join(lines)

    if primary:
        lines.append("- **Primary:**")
        for s in primary:
            lines.append(f"  - {s['text']}")
    if secondary:
        lines.append("- **Secondary:**")
        for s in secondary:
            lines.append(f"  - {s['text']}")
    if fyi:
        lines.append("- **FYI:**")
        for s in fyi:
            lines.append(f"  - {s['text']}")

    return "\n".join(lines)


# ============================
# Charts
# ============================

def altair_metric_chart(pod_df: pd.DataFrame, metric: str, title: str):
    if metric not in pod_df.columns:
        return

    d = pod_df[["snapshot_date", "window", metric]].dropna().copy()
    if d.empty:
        return

    c = (
        alt.Chart(d)
        .mark_line(point=True)
        .encode(
            x=alt.X("snapshot_date:T", title="Snapshot date"),
            y=alt.Y(f"{metric}:Q", title=metric),
            color=alt.Color(
                "window:N",
                title=None,
                legend=alt.Legend(orient="bottom", direction="horizontal"),
            ),
            tooltip=[
                alt.Tooltip("snapshot_date:T", title="Snapshot"),
                alt.Tooltip("window:N", title="Window"),
                alt.Tooltip(f"{metric}:Q", title=metric),
            ],
        )
        .properties(title=title)
    )
    st.altair_chart(c, use_container_width=True)


def charts_panel(pod_df: pd.DataFrame):
    c1, c2, c3 = st.columns(3)
    with c1:
        altair_metric_chart(pod_df, "commits", "Commits (3m/6m/12m)")
    with c2:
        altair_metric_chart(pod_df, "prs_merged", "PRs merged (3m/6m/12m)")
    with c3:
        altair_metric_chart(pod_df, "dev_unique_posters", "Dev unique posters (3m/6m/12m)")

    c4, c5, c6 = st.columns(3)
    with c4:
        altair_metric_chart(pod_df, "releases", "Releases (3m/6m/12m)")
    with c5:
        altair_metric_chart(pod_df, "median_merge_days", "Median PR merge time (days) (3m/6m/12m)")
    with c6:
        altair_metric_chart(pod_df, "bus50", "Bus factor proxy 50% (3m/6m/12m)")

    c7, c8, c9 = st.columns(3)
    with c7:
        altair_metric_chart(pod_df, "issues_opened", "Issues opened (3m/6m/12m)")
    with c8:
        altair_metric_chart(pod_df, "issues_closed", "Issues closed (3m/6m/12m)")
    with c9:
        altair_metric_chart(pod_df, "dev_msgs", "Dev messages (3m/6m/12m)")


# ============================
# UI (same layout)
# ============================

st.set_page_config(layout="wide")
st.title("Incubator Health — combined view (3m/6m/12m)")

if "selected_podling_key" not in st.session_state:
    st.session_state["selected_podling_key"] = None

with st.sidebar:
    reports_dir = st.text_input("Reports directory", "reports")
    max_commits = st.slider("Max report runs (commits touching reports/)", 10, 300, 120, 10)
    rebuild = st.button("Rebuild dataset (clear cache)")

try:
    repo_root = resolve_repo_root()
except RuntimeError as e:
    st.error(str(e))
    st.stop()

if rebuild:
    build_dataset.clear()

st.caption(f"Repo: {repo_root}")

df = build_dataset(str(repo_root), reports_dir, max_commits)

if df.empty:
    st.warning("No data parsed. Check reports_dir.")
    try:
        st.write("cwd:", str(Path.cwd().resolve()))
        st.write("repo_root:", str(repo_root))
        st.write("reports_dir:", reports_dir)
        st.write("reports_dir exists on disk:", (Path(repo_root) / reports_dir).exists())
        out = run_git(repo_root, ["ls-tree", "-r", "--name-only", "HEAD", reports_dir])
        st.write("git ls-tree (first 20 lines):", out.splitlines()[:20])
    except Exception as e:
        st.error(f"Debug: {e}")
    st.stop()

# STRICT latest-only combo for indicators/availability
combo = latest_combo(df)
combo["signals"] = combo.apply(build_signals_latest_only, axis=1)
combo["primary_count"] = combo["signals"].apply(lambda xs: sum(1 for x in xs if x["level"] == PRIMARY))
combo["secondary_count"] = combo["signals"].apply(lambda xs: sum(1 for x in xs if x["level"] == SECONDARY))
combo["fyi_count"] = combo["signals"].apply(lambda xs: sum(1 for x in xs if x["level"] == FYI))
combo["signal_summary"] = combo["signals"].apply(signals_summary)

tabs = st.tabs(["📋 Podling queue", "📈 Charts", "📝 Commentary builder"])

with tabs[0]:
    st.subheader("Podling queue (latest report per podling)")

    c1, c2, c3 = st.columns(3)
    with c1:
        show_level = st.selectbox(
            "Show",
            ["Primary only", "Primary + Secondary", "All (incl FYI)"],
            index=1,
        )
    with c2:
        contains = st.text_input("Filter signals containing (optional)", value="")
    with c3:
        sort_by = st.selectbox("Sort by", ["Most primary", "Most secondary", "Podling name"], index=0)

    q = combo.copy()

    if show_level == "Primary only":
        q = q[q["primary_count"] >= 1]
    elif show_level == "Primary + Secondary":
        q = q[(q["primary_count"] + q["secondary_count"]) >= 1]
    else:
        # All projects (no filtering-out by default would also be fine, but keep your UI)
        q = q.copy()

    if contains.strip():
        needle = contains.strip().lower()
        q = q[q["signal_summary"].str.lower().str.contains(needle, na=False)]

    if sort_by == "Most primary":
        q = q.sort_values(["primary_count", "secondary_count", "podling_display"], ascending=[False, False, True])
    elif sort_by == "Most secondary":
        q = q.sort_values(["secondary_count", "primary_count", "podling_display"], ascending=[False, False, True])
    else:
        q = q.sort_values(["podling_display"], ascending=[True])

    cols = [
        "podling_display",
        "primary_count",
        "secondary_count",
        "fyi_count",
        "signal_summary",
        "releases_3m", "releases_6m", "releases_12m",
        "commits_3m", "commits_6m", "commits_12m",
        "prs_merged_3m", "prs_merged_6m", "prs_merged_12m",
        "dev_unique_posters_3m", "dev_unique_posters_6m", "dev_unique_posters_12m",
        "dev_msgs_3m", "dev_msgs_6m", "dev_msgs_12m",
        "median_merge_days_3m", "median_merge_days_6m", "median_merge_days_12m",
        "bus50_3m", "bus50_6m", "bus50_12m",
    ]
    present = [c for c in cols if c in q.columns]

    try:
        event = st.dataframe(
            q[present],
            use_container_width=True,
            height=520,
            selection_mode="single-row",
            on_select="rerun",
        )
        sel_rows = event.selection.rows
        if sel_rows:
            # map selected display back to key deterministically via the selected row in q
            st.session_state["selected_podling_key"] = q.iloc[sel_rows[0]]["podling_key"]
    except Exception:
        st.info(
            "Row selection isn’t available in this Streamlit version. "
            "Use the dropdown below."
        )
        # fallback list: ALL projects
        pods_all = (
            combo[["podling_key", "podling_display"]]
            .drop_duplicates()
            .sort_values("podling_display")
            .reset_index(drop=True)
        )
        display = pods_all["podling_display"].tolist()
        # no extra widgets elsewhere; only used when dataframe selection is unavailable
        chosen_display = st.selectbox("Select podling", display, key="fallback_pod_select")
        chosen_key = pods_all[pods_all["podling_display"] == chosen_display].iloc[0]["podling_key"]
        st.session_state["selected_podling_key"] = chosen_key

with tabs[1]:
    st.subheader("Charts")

    pods_all = (
        combo[["podling_key", "podling_display"]]
        .drop_duplicates()
        .sort_values("podling_display")
        .reset_index(drop=True)
    )
    options = pods_all["podling_key"].tolist()
    fmt = dict(zip(pods_all["podling_key"], pods_all["podling_display"]))

    sel_key = st.session_state.get("selected_podling_key")
    if sel_key is None and options:
        sel_key = options[0]
        st.session_state["selected_podling_key"] = sel_key

    # keep the charts selectbox in sync WITHOUT warnings: set session_state value, do not pass index
    if "charts_pod_key" not in st.session_state:
        st.session_state["charts_pod_key"] = sel_key
    elif sel_key is not None and st.session_state["charts_pod_key"] != sel_key and sel_key in options:
        st.session_state["charts_pod_key"] = sel_key

    chosen_key = st.selectbox(
        "Podling",
        options,
        format_func=lambda k: fmt.get(k, k),
        key="charts_pod_key",
    )
    st.session_state["selected_podling_key"] = chosen_key

    pod_df = df[df["podling_key"] == chosen_key].sort_values("snapshot_date")
    charts_panel(pod_df)

with tabs[2]:
    st.subheader("Commentary builder (copyable)")

    pods_all = (
        combo[["podling_key", "podling_display"]]
        .drop_duplicates()
        .sort_values("podling_display")
        .reset_index(drop=True)
    )
    options = pods_all["podling_key"].tolist()
    fmt = dict(zip(pods_all["podling_key"], pods_all["podling_display"]))

    sel_key = st.session_state.get("selected_podling_key")
    if sel_key is None and options:
        sel_key = options[0]
        st.session_state["selected_podling_key"] = sel_key

    if "commentary_pod_key" not in st.session_state:
        st.session_state["commentary_pod_key"] = sel_key
    elif sel_key is not None and st.session_state["commentary_pod_key"] != sel_key and sel_key in options:
        st.session_state["commentary_pod_key"] = sel_key

    chosen_key = st.selectbox(
        "Podling",
        options,
        format_func=lambda k: fmt.get(k, k),
        key="commentary_pod_key",
    )
    st.session_state["selected_podling_key"] = chosen_key

    row = combo[combo["podling_key"] == chosen_key].iloc[0]
    pod_display = fmt.get(chosen_key, chosen_key)
    st.code(draft_commentary_from_latest(pod_display, row), language="markdown")