from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st


# ============================
# Git helpers (robust from any subdir/worktree)
# ============================

def git_toplevel(start: Path) -> Path:
    p = subprocess.run(
        ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or f"Not a git repo: {start}")
    return Path(p.stdout.strip())


def run_git(repo_dir: Path, args: list[str]) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo_dir), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "git command failed")
    return p.stdout


def git_show_file(repo_dir: Path, commit: str, path: str) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo_dir), "show", f"{commit}:{path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "git show failed")
    return p.stdout


def list_report_files(repo_dir: Path, reports_dir: str) -> list[str]:
    out = run_git(repo_dir, ["ls-tree", "-r", "--name-only", "HEAD", reports_dir])
    return [x.strip() for x in out.splitlines() if x.strip()]


def file_commits(repo_dir: Path, path: str, max_commits: int) -> list[str]:
    out = run_git(repo_dir, ["log", f"--max-count={max_commits}", "--pretty=format:%H", "--", path])
    return [x.strip() for x in out.splitlines() if x.strip()]


# ============================
# Parsing (based on actual report format)
# ============================

RE_GENERATED_ON = re.compile(r"_Generated on\s+(\d{4}-\d{2}-\d{2})_", re.IGNORECASE)
RE_WINDOW_HEADER = re.compile(r"^###\s+(3m|6m|12m)\b", re.MULTILINE)


def _to_int(s: Optional[str]) -> Optional[int]:
    if s is None:
        return None
    try:
        return int(s)
    except Exception:
        return None


def _to_float(s: Optional[str]) -> Optional[float]:
    if s is None:
        return None
    try:
        return float(s)
    except Exception:
        return None


def parse_window_block(lines: list[str]) -> dict:
    """
    Parses the Window Details bullet lines for one window.
    Designed explicitly for the format you pasted (Amoro/Polaris).
    """
    row: dict = {}

    for line in lines:
        line = line.strip()

        # Releases + median gap (gap may be —)
        if "Releases (from list votes/results)" in line:
            m = re.search(r"Releases .*?:\*\*\s*(\d+)", line)
            row["releases"] = _to_int(m.group(1)) if m else None

            m = re.search(r"Median gap \(days\):\*\*\s*([0-9.]+)", line)
            row["median_gap_days"] = _to_float(m.group(1)) if m else None

        # New contributors / unique committers / commits
        elif "New contributors" in line:
            row["new_contributors"] = _to_int(re.search(r"New contributors:\*\*\s*(\d+)", line).group(1))
            row["unique_committers"] = _to_int(re.search(r"Unique committers:\*\*\s*(\d+)", line).group(1))
            row["commits"] = _to_int(re.search(r"Commits:\*\*\s*(\d+)", line).group(1))

        # Issues: opened X / closed Y
        elif line.startswith("- **Issues:**"):
            m = re.search(r"opened\s*(\d+)\s*/\s*closed\s*(\d+)", line)
            row["issues_opened"] = _to_int(m.group(1)) if m else None
            row["issues_closed"] = _to_int(m.group(2)) if m else None

        # PRs + median merge time
        elif line.startswith("- **PRs:**"):
            m = re.search(r"opened\s*(\d+)\s*/\s*merged\s*(\d+)", line)
            row["prs_opened"] = _to_int(m.group(1)) if m else None
            row["prs_merged"] = _to_int(m.group(2)) if m else None

            m = re.search(r"Median merge time \(days\):\*\*\s*([0-9.]+)", line)
            row["median_merge_days"] = _to_float(m.group(1)) if m else None

        # Reviews (sampled): multiple fields in one line
        elif "Reviews (sampled)" in line:
            m = re.search(r"median reviewers/PR\s*\*\*([0-9.]+)\*\*", line)
            row["median_reviewers_per_pr"] = _to_float(m.group(1)) if m else None

            m = re.search(r"reviewer diversity \(eff\.#\)\s*\*\*([0-9.]+)\*\*", line)
            row["reviewer_div_eff"] = _to_float(m.group(1)) if m else None

            m = re.search(r"PR author diversity \(eff\.#\)\s*\*\*([0-9.]+)\*\*", line)
            row["pr_author_div_eff"] = _to_float(m.group(1)) if m else None

            m = re.search(r"unique reviewers\s*\*\*(\d+)\*\*", line)
            row["unique_reviewers"] = _to_int(m.group(1)) if m else None

            m = re.search(r"unique authors\s*\*\*(\d+)\*\*", line)
            row["unique_authors"] = _to_int(m.group(1)) if m else None

        # Bus factor proxy
        elif "Bus factor proxy (50% / 75%)" in line:
            m = re.search(r"\*\*:\*\*\s*(\d+)\s*/\s*(\d+)", line)
            row["bus50"] = _to_int(m.group(1)) if m else None
            row["bus75"] = _to_int(m.group(2)) if m else None

        # Incubator reports + avg mentor sign-offs (sign-offs may be —)
        elif "Incubator reports" in line:
            m = re.search(r"Incubator reports:\*\*\s*(\d+)", line)
            row["reports_count"] = _to_int(m.group(1)) if m else None

            m = re.search(r"Avg mentor sign-offs:\*\*\s*([0-9.]+)", line)
            row["avg_mentor_signoffs"] = _to_float(m.group(1)) if m else None

        # Mailing lists: dev messages **X**, dev unique posters **Y**
        elif "Mailing lists:" in line:
            m = re.search(r"dev messages\s*\*\*(\d+)\*\*", line)
            row["dev_msgs"] = _to_int(m.group(1)) if m else None

            m = re.search(r"dev unique posters\s*\*\*(\d+)\*\*", line)
            row["dev_unique_posters"] = _to_int(m.group(1)) if m else None

    return row


def parse_report(text: str, podling: str) -> list[dict]:
    """
    Returns one dict per window (3m/6m/12m) for a single report snapshot.
    """
    m = RE_GENERATED_ON.search(text)
    if not m:
        return []
    snapshot_date = m.group(1)

    # Only parse Window Details section (ignore Trends)
    wd_idx = text.find("## Window Details")
    if wd_idx == -1:
        return []
    wd = text[wd_idx:]

    # Find each window header and gather bullet lines until next header
    matches = list(RE_WINDOW_HEADER.finditer(wd))
    out: list[dict] = []

    for i, mm in enumerate(matches):
        window = mm.group(1)
        start = mm.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(wd)
        block = wd[start:end]

        # Collect only bullet lines that begin with "- "
        lines = [ln for ln in block.splitlines() if ln.strip().startswith("- ")]

        metrics = parse_window_block(lines)
        out.append({
            "podling": podling,
            "snapshot_date": snapshot_date,
            "window": window,
            **metrics
        })

    return out


# ============================
# Dataset build
# ============================

@st.cache_data(show_spinner=True)
def build_dataset(repo_root: str, reports_dir: str, max_commits: int) -> pd.DataFrame:
    repo_dir = Path(repo_root)
    rows: list[dict] = []

    files = list_report_files(repo_dir, reports_dir)
    for path in files:
        podling = Path(path).stem
        commits = file_commits(repo_dir, path, max_commits=max_commits)

        for commit in commits:
            try:
                text = git_show_file(repo_dir, commit, path)
            except Exception:
                continue

            for r in parse_report(text, podling):
                r["commit"] = commit
                r["path"] = path
                rows.append(r)

    df = pd.DataFrame(rows)
    if df.empty:
        return df

    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"], errors="coerce")
    df = df.dropna(subset=["snapshot_date"])

    # Keep 1 row per podling+window+snapshot_date (later commits may be formatting-only)
    df = df.sort_values(["podling", "window", "snapshot_date", "commit"])
    df = df.drop_duplicates(["podling", "window", "snapshot_date"], keep="last")
    return df.reset_index(drop=True)


# ============================
# Scoring (NaN-safe)
# ============================

def latest_and_previous(dfw: pd.DataFrame) -> pd.DataFrame:
    d = dfw.sort_values(["podling", "snapshot_date"])
    g = d.groupby("podling", as_index=False)
    latest = g.tail(1).set_index("podling")
    prev = g.tail(2).groupby("podling").head(1).set_index("podling")  # second-to-last
    return latest.add_prefix("latest_").join(prev.add_prefix("prev_"), how="left").reset_index()


def _num(row: pd.Series, key: str) -> Optional[float]:
    v = row.get(key)
    if v is None:
        return None
    if isinstance(v, float) and pd.isna(v):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    return None


def score_row(row: pd.Series, window: str) -> tuple[float, str]:
    score = 0.0
    reasons: list[str] = []

    releases = _num(row, "latest_releases")
    posters = _num(row, "latest_dev_unique_posters")
    bus50 = _num(row, "latest_bus50")
    merge = _num(row, "latest_median_merge_days")
    signoffs = _num(row, "latest_avg_mentor_signoffs")

    # Only treat "no releases" as a risk on longer windows
    if window in ("6m", "12m") and releases is not None and releases == 0:
        score += 3
        reasons.append("No releases")

    if posters is not None and posters <= 3:
        score += 2
        reasons.append("Low dev posters")

    if bus50 is not None and bus50 <= 2:
        score += 2
        reasons.append("Bus factor risk")

    if merge is not None and merge >= 30:
        score += 2
        reasons.append("Slow PR merges")

    if signoffs is not None and signoffs < 1:
        score += 1
        reasons.append("Low mentor sign-off")

    prev_posters = _num(row, "prev_dev_unique_posters")
    if posters is not None and prev_posters is not None and posters < prev_posters:
        score += 1
        reasons.append("Posters declining")

    return score, ", ".join(reasons)


# ============================
# Streamlit UI
# ============================

st.set_page_config(layout="wide")
st.title("Incubator Health Dashboard")

with st.sidebar:
    repo_input = st.text_input("Any path inside the incubator repo", value=str(Path.cwd()))
    reports_dir = st.text_input("Reports directory", "tools/health/reports")
    window = st.selectbox("Window", ["3m", "6m", "12m"], index=0)
    max_commits = st.slider("Max commits per file", 10, 200, 120, 10)
    rebuild = st.button("Rebuild dataset (clear cache)")
    show_debug = st.checkbox("Show debug panel", value=False)

try:
    repo_root = git_toplevel(Path(repo_input))
except RuntimeError as e:
    st.error(str(e))
    st.stop()

if rebuild:
    build_dataset.clear()

df = build_dataset(str(repo_root), reports_dir, max_commits)

st.caption(f"Repo: {repo_root}")

if df.empty:
    st.warning("No data parsed — check reports_dir or parser assumptions.")
    st.stop()

dfw = df[df["window"] == window].copy()
if dfw.empty:
    st.warning(f"No rows for window {window}.")
    st.stop()

snap = latest_and_previous(dfw)

scores = snap.apply(lambda r: score_row(r, window), axis=1, result_type="expand")
snap["risk"] = scores[0]
snap["reasons"] = scores[1]

latest_date = pd.to_datetime(snap["latest_snapshot_date"]).max()
st.caption(
    f"{snap.shape[0]} podlings • snapshots {df['snapshot_date'].min().date()} → {df['snapshot_date'].max().date()} • "
    f"latest snapshot {latest_date.date()}"
)

# Follow-up queue
st.subheader("Follow-up queue")
queue = snap.sort_values(["risk", "latest_dev_unique_posters"], ascending=[False, True])

cols = [
    "podling",
    "risk",
    "reasons",
    "latest_snapshot_date",
    "latest_releases",
    "latest_commits",
    "latest_prs_merged",
    "latest_dev_unique_posters",
    "latest_bus50",
    "latest_median_merge_days",
    "latest_reviewer_div_eff",
    "latest_pr_author_div_eff",
    "latest_unique_reviewers",
    "latest_unique_authors",
    "latest_reports_count",
    "latest_avg_mentor_signoffs",
    "latest_dev_msgs",
]
present = [c for c in cols if c in queue.columns]
st.dataframe(queue[present], use_container_width=True, height=650)

# Podling drill-down
st.subheader("Podling drill-down")
podling = st.selectbox("Podling", sorted(dfw["podling"].unique()))
d = dfw[dfw["podling"] == podling].sort_values("snapshot_date").copy()

c1, c2, c3 = st.columns(3)
with c1:
    st.write("Commits")
    if "commits" in d.columns:
        st.line_chart(d.set_index("snapshot_date")["commits"])
with c2:
    st.write("PRs merged")
    if "prs_merged" in d.columns:
        st.line_chart(d.set_index("snapshot_date")["prs_merged"])
with c3:
    st.write("Dev unique posters")
    if "dev_unique_posters" in d.columns:
        st.line_chart(d.set_index("snapshot_date")["dev_unique_posters"])

c4, c5, c6 = st.columns(3)
with c4:
    st.write("Median merge time (days)")
    if "median_merge_days" in d.columns:
        st.line_chart(d.set_index("snapshot_date")["median_merge_days"])
with c5:
    st.write("Bus factor (50% / 75%)")
    if "bus50" in d.columns and "bus75" in d.columns:
        st.line_chart(d.set_index("snapshot_date")[["bus50", "bus75"]])
with c6:
    st.write("Mailing list messages (dev@)")
    if "dev_msgs" in d.columns:
        st.line_chart(d.set_index("snapshot_date")["dev_msgs"])

if show_debug:
    st.divider()
    st.subheader("Debug")
    st.write("Parsed dataframe columns:", list(df.columns))
    st.write("Non-null counts (key metrics):")
    key = ["commits", "prs_merged", "dev_unique_posters", "bus50", "dev_msgs", "reviewer_div_eff"]
    key = [k for k in key if k in df.columns]
    st.write(df[key].notna().sum())
    st.write("Sample rows:")
    st.dataframe(df.head(30), use_container_width=True)