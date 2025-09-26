#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Incubator Podling Health — Reports + GitHub + Mailing Lists + Diversity + Summary

- Windows: 3m, 6m, 12m (strict by age) or single "to-date" if <3m old
- Release threads: from dev@ & incubator-general@ [VOTE]/[RESULT]
- GitHub: commits, contributors, issues, PRs; PR median merge time via statistically significant sample
- Bus factor proxy: contributors needed to reach 50% / 75% of commits (higher = better)
- Mentor sign-offs: simple working parser on 'Signed-off-by' lines
- Mailing lists: header-only parsing (Date/Subject/From) for speed
- Trend arrows compare **per-month rates** with guards (≥28d window AND ≥5 events), else “—”
- “--all” writes per-podling MD files + SUMMARY.md
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
import os
import time
import random
import re
import statistics
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, UTC
from requests.exceptions import RequestException

import requests
import xml.etree.ElementTree as ET

# ---------------- Constants ----------------

ISO = "%Y-%m-%dT%H:%M:%SZ"
URL_PODLINGS_XML = "https://incubator.apache.org/podlings.xml"
MOD_MBOX_BASE = "http://mail-archives.apache.org/mod_mbox"

AVG_DAYS_PER_MONTH = 30.44  # for rate normalization

# Trend guards
MIN_DAYS_FOR_WINDOW = 28
MIN_EVENTS_FOR_TREND = 5

CACHE_DIR = ".mbox_cache"
os.makedirs(CACHE_DIR, exist_ok=True)
CACHE_TTL_SECONDS_CURRENT_MONTH = 24 * 60 * 60  # 24 hours

# ---------------- CLI ----------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Trend-based health indicators for Incubator podlings (reports + GitHub + mailing lists)."
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--podling", help="Single podling name as appears in board agendas.")
    g.add_argument("--all", action="store_true", help="Process all current podlings from podlings.xml.")

    p.add_argument("--minutes-dir", required=True, help="Path to ASF board archived agendas (txt files).")
    p.add_argument("--repos", nargs="*", default=[], help="GitHub repos (owner/name). Default guess is apache/<slug>.")
    p.add_argument("--today", default=None, help="Override today YYYY-MM-DD.")

    # Output
    p.add_argument("--out-csv", default=None, help="CSV path for aggregated rows.")
    p.add_argument("--out-md", default=None, help="Markdown for single-podling mode.")
    p.add_argument("--out-md-dir", default=None, help="Directory for per-podling Markdown in --all mode.")

    # Podlings registry
    p.add_argument("--podlings-xml", default=None, help="Optional local podlings.xml.")

    p.add_argument("--debug", action="store_true", help="Verbose progress output.")
    return p.parse_args()

# ---------------- Utils ----------------

def log(msg: str, debug: bool):
    if debug:
        print(msg, file=sys.stderr)

def parse_today(s: Optional[str]) -> dt.date:
    return dt.date.today() if not s else dt.date.fromisoformat(s)

def months_ago(d: dt.date, months: int) -> dt.date:
    y = d.year + (d.month - months - 1) // 12
    m = (d.month - months - 1) % 12 + 1
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m-1])
    return dt.date(y, m, day)

def to_iso_date(d: dt.datetime) -> str:
    return d.date().isoformat()

def to_naive_utc(d: dt.datetime) -> dt.datetime:
    if d.tzinfo is None:
        return d.replace(tzinfo=dt.timezone.utc).astimezone(dt.timezone.utc).replace(tzinfo=None)
    return d.astimezone(dt.timezone.utc).replace(tzinfo=None)

def months_in_window(start: dt.datetime, end: dt.datetime) -> float:
    days = (end - start).days + 1
    return max(days / AVG_DAYS_PER_MONTH, 1e-9)

def rate_per_month(value: Optional[float], start: dt.datetime, end: dt.datetime) -> Optional[float]:
    if value is None:
        return None
    return float(value) / months_in_window(start, end)

def window_days(start: dt.datetime, end: dt.datetime) -> int:
    return max(1, (end - start).days + 1)

def canonical_repo(repo: str) -> str:
    def probe(r: str) -> str:
        url = f"https://api.github.com/repos/{r}"
        try:
            resp = requests.get(url, headers=gh_headers(), timeout=20)
        except RequestException:
            return ""  # network issue → no change
        if resp.status_code == 200:
            return resp.json().get("full_name", r)
        return ""  # 404/403/etc.

    # 1) try as-is
    hit = probe(repo)
    if hit:
        return hit

    # 2) toggle "incubator-" once
    try:
        owner, name = repo.split("/", 1)
    except ValueError:
        return repo  # malformed; give up

    if name.startswith("incubator-"):
        alt = f"{owner}/{name[len('incubator-'):]}"
    else:
        alt = f"{owner}/incubator-{name}"

    hit = probe(alt)
    return hit or repo


# ---------------- Trend arrows & scoring ----------------

def trend_score(curr: Optional[float], prev: Optional[float], *, lower_is_better: bool, flat_tol: float = 0.10) -> int:
    """
    Integer score in [-3..+3].
    lower_is_better flips the sense (so decreases become positive improvements).
    Thresholds: flat ±10% => 0; small 10–25% => ±1; medium 25–100% => ±2; large ≥100% => ±3.
    """
    if curr is None or prev is None:
        return 0
    try:
        pv = float(prev); cv = float(curr)
    except (TypeError, ValueError):
        return 0

    if lower_is_better:
        pv, cv = cv, pv

    if pv == 0:
        return 3 if cv > 0 else 0

    delta = (cv - pv) / abs(pv)
    if -flat_tol < delta < flat_tol:
        return 0

    mag = abs(delta)
    if mag < 0.25:
        n = 1
    elif mag < 1.0:
        n = 2
    else:
        n = 3
    return n if delta > 0 else -n

def arrows_from_score(score: int) -> str:
    if score == 0:
        return "→"
    arrow = "↗" if score > 0 else "↘"
    return arrow * min(3, abs(score))

def trend_arrows(curr: Optional[float], prev: Optional[float], flat_tol: float = 0.10) -> str:
    return arrows_from_score(trend_score(curr, prev, lower_is_better=False, flat_tol=flat_tol))

# ---------------- GitHub ----------------

def gh_headers() -> Dict[str, str]:
    h = {"Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h

def gh_get(url: str, params: Dict[str, str] | None = None) -> requests.Response:
    r = requests.get(url, headers=gh_headers(), params=params or {}, timeout=30)
    r.raise_for_status()
    return r

def gh_paginate(url: str, params: Dict[str, str]) -> List[dict]:
    out: List[dict] = []
    sess = requests.Session()
    while True:
        r = sess.get(url, params=params, headers=gh_headers(), timeout=30)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):
            chunk = data
        elif isinstance(data, dict) and "items" in data:
            chunk = data["items"]
        else:
            chunk = [data] if isinstance(data, dict) else []
        out.extend(chunk)
        ln = r.headers.get("Link", "")
        nxt = None
        for part in ln.split(","):
            if 'rel="next"' in part:
                nxt = part[part.find("<")+1:part.find(">")]
                break
        if not nxt:
            break
        url = nxt
        params = {}
    return out

def gh_search_issues(q: str) -> int:
    r = gh_get("https://api.github.com/search/issues", {"q": q, "per_page": "1"})
    j = r.json()
    return int(j.get("total_count", 0))

def gh_search_issue_items(q: str, per_page: int = 100) -> List[dict]:
    return gh_paginate("https://api.github.com/search/issues", {"q": q, "per_page": str(per_page)})

def gh_get_pr(repo: str, number: int) -> dict:
    r = gh_get(f"https://api.github.com/repos/{repo}/pulls/{number}")
    return r.json()

def gh_list_commits(repo: str, since: dt.datetime, until: dt.datetime) -> List[dict]:
    url = f"https://api.github.com/repos/{repo}/commits"
    return gh_paginate(url, {"since": since.strftime(ISO), "until": until.strftime(ISO), "per_page": "100"})

def median_days_between(dts: List[dt.datetime]) -> Optional[float]:
    if len(dts) < 2:
        return None
    dts_sorted = sorted(dts)
    deltas = [(b - a).days for a, b in zip(dts_sorted, dts_sorted[1:])]
    return statistics.median(deltas) if deltas else None

# ---------------- Board reports (mentor sign-offs) ----------------

INCUBATOR_ATTACHMENT_HDR = re.compile(r"^\s*Attachment\s+[A-Z0-9]+:\s.*Incubator", re.I | re.M)
NEXT_ATTACHMENT_HDR      = re.compile(r"^\s*Attachment\s+[A-Z0-9]+:", re.I | re.M)

def _pod_hdr_re(name: str) -> re.Pattern:
    return re.compile(rf"^\s*##\s*(?:Apache\s+)?{re.escape(name)}\b", re.I)

CHECKED_BOX = re.compile(r"^\s*\[\s*[xX✓]\s*\]\s*")
SIGNED_BY_HDR = re.compile(r"^\s*###\s*Signed[- ]off[- ]by\s*:?\s*$", re.I)
SIGNOFF_LINE_RE = re.compile(r"^\s*-\s*\[\s*[xX]\s*\]\s*(.+?)\s*$")

def _extract_incubator_block(file_text: str) -> str:
    m = INCUBATOR_ATTACHMENT_HDR.search(file_text)
    if not m:
        return ""
    m2 = NEXT_ATTACHMENT_HDR.search(file_text, m.end())
    end = m2.start() if m2 else len(file_text)
    return file_text[m.start():end]

def _clean_mentor_line(raw: str) -> str | None:
    s = raw.strip()
    if not s or NO_SIGNOFF_LINE.search(s):
        return None
    s = BULLET_RE.sub("", s)
    s = CHECKED_BOX.sub("", s)
    s = re.sub(r"^\((?:[a-z0-9][a-z0-9._\- ]{1,30})\)\s*", "", s, flags=re.I)
    s = re.sub(r"<[^>]*>", "", s)
    s = re.split(r"\bComments?\s*:\s*", s, maxsplit=1, flags=re.I)[0].strip()
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s).strip()
    return s if re.search(r"[A-Za-z]", s) else None


def parse_podling_reports_from_agenda(path: str, podling_name: str) -> Optional[dict]:
    """
    Return {'path','text','signoffs': [...]} for this agenda if the podling is present.
    Strictly counts only lines of the form '- [x] Name' (or '- [X] Name') after the
    '### Signed-off-by' header in the podling's section.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            full = f.read()
    except Exception:
        return None

    inc = _extract_incubator_block(full) 
    if not inc:
        return None

    lines = inc.splitlines()

    # find the podling section bounds
    start = None
    pod_hdr = _pod_hdr_re(podling_name) 
    for i, ln in enumerate(lines):
        if pod_hdr.match(ln):
            start = i
            break
    if start is None:
        return None

    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^\s*##\s+", lines[j]):  # next podling header
            end = j
            break

    # find the "### Signed-off-by" header inside this podling section
    sign_idx = None
    for k in range(start + 1, end):
        if SIGNED_BY_HDR.match(lines[k]):
            sign_idx = k
            break

    # if no explicit Signed-off-by header, treat as zero sign-offs for this report
    if sign_idx is None:
        return {"path": path, "text": "\n".join(lines[start:end]), "signoffs": []}

    # collect only checked-box bullets until the next header
    names = set()
    for t in range(sign_idx + 1, end):
        ln = lines[t].rstrip()
        if ln.startswith("###") or ln.startswith("##"):
            break
        m = SIGNOFF_LINE_RE.match(ln)
        if m:
            name = m.group(1).strip()
            if name:
                names.add(name)

    return {
        "path": path,
        "text": "\n".join(lines[start:end]),
        "signoffs": sorted(names, key=str.lower),
    }

AGENDA_RE = re.compile(r"board_agenda_(\d{4})_(\d{2})_(\d{2})\.txt$", re.I)

def list_agenda_files(minutes_dir: str | os.PathLike) -> list[str]:
    files = []
    for name in os.listdir(minutes_dir):
        m = AGENDA_RE.match(name)
        if not m:
            continue
        path = os.path.join(minutes_dir, name)
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        files.append(((y, mo, d), path))
    files.sort(key=lambda t: t[0])
    return [p for _, p in files]

def collect_reports(minutes_dir: str, podling_name: str, since: dt.datetime, until: dt.datetime) -> List[dict]:
    items: List[dict] = []
    for p in list_agenda_files(minutes_dir):
        m = re.search(r"(\d{4})_(\d{2})_(\d{2})", os.path.basename(p))
        if not m:
            continue
        d = dt.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if d < since or d > until:
            continue
        meta = parse_podling_reports_from_agenda(p, podling_name)
        if meta:
            meta["date"] = d
            items.append(meta)
    return sorted(items, key=lambda x: x["date"])

# ---------------- Podlings registry (with start date) ----------------

def load_podlings_root(xml_path: Optional[str], debug: bool=False) -> ET.Element:
    try:
        if xml_path and os.path.exists(xml_path):
            log(f"[podlings] using local {xml_path}", debug)
            tree = ET.parse(xml_path); root = tree.getroot()
        else:
            log(f"[podlings] fetching {URL_PODLINGS_XML}", debug)
            r = requests.get(URL_PODLINGS_XML, timeout=30); r.raise_for_status()
            root = ET.fromstring(r.text)
    except Exception as e:
        sys.exit(f"[error] unable to load podlings.xml: {e}")
    return root

def fetch_podlings(root: ET.Element) -> List[str]:
    names = [p.attrib.get("name","").strip() for p in root.findall(".//podling[@status='current']")]
    return [n for n in names if n]

def get_podling_start_date(root: ET.Element, name: str) -> Optional[dt.date]:
    target = name.lower()
    for el in root.findall(".//podling[@status='current']"):
        if el.attrib.get("name", "").lower() == target:
            startdate = (el.attrib.get("startdate") or "").strip()
            if startdate:
                return dt.date.fromisoformat(startdate[:10])
    return None

# ---------------- Mailing lists (release detection + activity) ----------------

EMAIL_RE = re.compile(r"<([^>]+)>")

def podling_to_dev_list_slug(podling: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", podling.lower()).strip("-")
    return f"{slug}-dev"

def month_iter(start_date: dt.date, end_date: dt.date):
    y, m = start_date.year, start_date.month
    while (y < end_date.year) or (y == end_date.year and m <= end_date.month):
        yield y, m
        m += 1
        if m == 13:
            m = 1; y += 1

def fetch_month_mbox(list_slug: str, y: int, m: int, debug: bool=False) -> Optional[bytes]:
    mm = f"{y}{m:02d}.mbox"
    url = f"{MOD_MBOX_BASE}/{list_slug}/{mm}"
    cache_path = os.path.join(CACHE_DIR, f"{list_slug.replace('/', '_')}-{mm}")

    now = datetime.now(UTC)
    is_current = (y == now.year and m == now.month)

    # Use cache if available:
    if os.path.exists(cache_path):
        if not is_current:
            log(f"[lists] cached {cache_path}", debug)
            with open(cache_path, "rb") as f:
                return f.read()
        else:
            age = time.time() - os.path.getmtime(cache_path)
            if age <= CACHE_TTL_SECONDS_CURRENT_MONTH:
                log(f"[lists] cached (fresh) {cache_path}", debug)
                with open(cache_path, "rb") as f:
                    return f.read()

    log(f"[lists] fetch {url}", debug)
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        data = r.content
        # Cache both current and past months (current month valid for 24h)
        try:
            with open(cache_path, "wb") as f:
                f.write(data)
        except Exception as e:
            log(f"[lists] cache write fail {cache_path}: {e}", debug)
        return data
    except Exception as e:
        log(f"[lists] fetch fail {url}: {e}", debug)
        # Fallback to any existing (even stale) cache if fetch failed
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "rb") as f:
                    return f.read()
            except Exception:
                pass
        return None

def fast_scan_mbox_headers(mbox_bytes: bytes):
    def ensure_str(b):
        if isinstance(b, bytes):
            try:
                return b.decode("utf-8", "ignore")
            except Exception:
                return ""
        return b

    headers = {}
    in_headers = False
    for raw in mbox_bytes.splitlines(keepends=False):
        line = ensure_str(raw)
        if line.startswith("From "):
            if headers:
                yield headers
            headers = {}
            in_headers = True
            continue
        if in_headers:
            if line.strip() == "":
                in_headers = False
                continue
            if line.startswith((" ", "\t")):
                for k in ("Date", "Subject", "From"):
                    if k in headers:
                        headers[k] = (headers[k] + " " + line.strip()).strip()
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip(); v = v.strip()
                if k in ("Date", "Subject", "From"):
                    headers[k] = (headers.get(k, "") + " " + v).strip()
    if headers:
        yield headers

def extract_email(addr: str) -> str:
    if not addr:
        return ""
    m = EMAIL_RE.search(addr)
    return (m.group(1) if m else addr).strip().lower()

def _to_naive_utc(d: dt.datetime) -> dt.datetime:
    if d.tzinfo is None:
        return d.replace(tzinfo=dt.timezone.utc).astimezone(dt.timezone.utc).replace(tzinfo=None)
    return d.astimezone(dt.timezone.utc).replace(tzinfo=None)

VOTE_RE = re.compile(r"\[VOTE[^\]]*\].*RELEASE", re.I)
RESULT_RE = re.compile(r"\[RESULT[^\]]*\].*RELEASE", re.I)

VERSION_TOKEN_RE = re.compile(r"\b[vV]?(\d+(?:\.\d+){1,3}(?:-[A-Za-z0-9_.-]+)?)\b")
NAME_NORMALIZE_RE = re.compile(r"[^a-z0-9]+")

def _tokens(s: str) -> set[str]:
    return set(t for t in re.split(r"[^a-z0-9]+", s.lower()) if t)

def _subject_mentions_podling(subj: str, podling: str) -> bool:
    subj_tokens = _tokens(subj)
    pod_tokens = [t for t in _tokens(podling) if t not in {"apache", "incubator"}]
    return any(t in subj_tokens for t in pod_tokens)

def _extract_release_version(subj: str) -> Optional[str]:
    m = VERSION_TOKEN_RE.search(subj)
    if not m:
        return None
    v = m.group(1)
    v = re.sub(r"^[vV]", "", v)
    v = re.sub(r"(?i)[\-\._]incubat(?:or|ing)(?:[\-\._][A-Za-z0-9_.-]+)?", "", v)
    v = re.sub(r"(?i)(?:[\-._]?rc\d+)$", "", v)
    v = re.sub(r"[\-._]+$", "", v)
    v = v.strip()
    return v or None

def scan_lists_for_window(podling: str, start: dt.datetime, end: dt.datetime, debug: bool=False) -> Dict[str, int | List[dt.datetime]]:
    from email.utils import parsedate_to_datetime

    dev_slug = podling_to_dev_list_slug(podling)
    gen_slug = "incubator-general"

    dev_msgs = 0
    dev_posters = set()
    by_version: Dict[str, Dict[str, List[dt.datetime]]] = {}

    def handle_header(hdr: dict, track_dev: bool):
        nonlocal dev_msgs
        try:
            d = parsedate_to_datetime(hdr.get("Date"))
            if d is None:
                return
            d = _to_naive_utc(d)
        except Exception:
            return
        if not (start <= d <= end):
            return

        subj = (hdr.get("Subject") or "").strip()
        frm = extract_email(hdr.get("From") or "")

        if track_dev:
            dev_msgs += 1
            if frm:
                dev_posters.add(frm)

        up = subj.upper()
        is_release_thread = ("RELEASE" in up) and ("[VOTE" in up or "[RESULT" in up)
        if not is_release_thread:
            return

        if (not track_dev) and (not _subject_mentions_podling(subj, podling)):
            return

        ver = _extract_release_version(subj)
        if not ver:
            if debug:
                log(f"      [lists] skip release thread w/o version: {subj}", debug)
            return

        if RESULT_RE.search(subj):
            by_version.setdefault(ver, {}).setdefault("result", []).append(d)
        elif VOTE_RE.search(subj):
            by_version.setdefault(ver, {}).setdefault("vote", []).append(d)

    for slug, track_dev in [(dev_slug, True), (gen_slug, False)]:
        for y, m in month_iter(start.date(), end.date()):
            blob = fetch_month_mbox(slug, y, m, debug=debug)
            if not blob:
                continue
            for hdr in fast_scan_mbox_headers(blob):
                handle_header(hdr, track_dev)

    release_event_dates: List[dt.datetime] = []
    for ver, payload in by_version.items():
        result_dates = sorted(payload.get("result", []))
        vote_dates = sorted(payload.get("vote", []))
        event_dt = result_dates[0] if result_dates else (vote_dates[0] if vote_dates else None)
        if event_dt:
            release_event_dates.append(event_dt)

    return {
        "dev_messages": dev_msgs,
        "dev_unique_posters": len(dev_posters),
        "release_event_dates": sorted(release_event_dates),
    }

# ---------------- Diversity helpers ----------------

def is_bot_login(login: Optional[str]) -> bool:
    if not login:
        return False
    l = login.lower()
    return l.endswith("[bot]") or l.endswith("-bot") or l.endswith("_bot") or l in {"dependabot", "renovate"}

def effective_diversity(counts: Dict[str, int]) -> Optional[float]:
    total = sum(counts.values())
    if total <= 0:
        return None
    hhi = sum((c/total)**2 for c in counts.values())
    return None if hhi <= 0 else round(1.0 / hhi, 2)

# ---------------- Metrics ----------------

@dataclass
class WindowMetrics:
    window: str
    start: dt.datetime
    end: dt.datetime

    # Releases (from mailing lists)
    release_count: int = 0
    release_median_days_between: Optional[float] = None

    # GitHub
    commits: int = 0
    unique_committers: int = 0
    new_contributors: int = 0
    issues_opened: int = 0
    issues_closed: int = 0
    prs_opened: int = 0
    prs_merged: int = 0
    pr_median_merge_days: Optional[float] = None
    bus_factor_50: Optional[int] = None
    bus_factor_75: Optional[int] = None

    # Diversity (from sampled merged PRs)
    median_reviewers_per_pr: Optional[float] = None
    reviewer_diversity_effective: Optional[float] = None
    pr_author_diversity_effective: Optional[float] = None
    reviewer_unique_sampled: int = 0
    pr_author_unique_sampled: int = 0

    # Reports
    reports_count: int = 0
    avg_mentor_signoffs: Optional[float] = None

    # Mailing lists
    dev_messages: int = 0
    dev_unique_posters: int = 0

# --- statistically significant sample size ---

def sample_size(total_points: int) -> int:
    return max(100, min(300, int(total_points * 0.25)))

# --- GitHub aggregation (incl. Bus factor + Diversity) ---

def compute_bus_factor_proxies(by_ident_counts: Dict[str, int], total: int) -> Tuple[Optional[int], Optional[int]]:
    if total <= 0 or not by_ident_counts:
        return None, None
    target50 = 0.50 * total
    target75 = 0.75 * total
    running = 0; k50 = None; k75 = None
    for i, c in enumerate(sorted(by_ident_counts.values(), reverse=True), start=1):
        running += c
        if k50 is None and running >= target50:
            k50 = i
        if k75 is None and running >= target75:
            k75 = i
            break
    return k50, k75

def compute_github_metrics(repos: List[str], start: dt.datetime, end: dt.datetime, debug: bool=False) -> Dict[str, any]:
    commit_authors_window: set = set()
    commit_authors_prior: set = set()
    total_commits = 0
    by_ident_counts: Dict[str, int] = {}
    horizon_start = start - dt.timedelta(days=365 * 5)

    repos = [canonical_repo(r) for r in repos]
    for r in repos:
        r = canonical_repo(r)
        try:
            commits = gh_list_commits(r, start, end)
            total_commits += len(commits)
            for c in commits:
                a = c.get("author") or {}
                login = a.get("login")
                name = (c.get("commit") or {}).get("author", {}).get("name")
                ident = (login or name or "").strip()
                if ident:
                    commit_authors_window.add((r, ident))
                    by_ident_counts[ident] = by_ident_counts.get(ident, 0) + 1

            prior = gh_list_commits(r, horizon_start, start - dt.timedelta(seconds=1))
            for c in prior:
                a = c.get("author") or {}
                login = a.get("login")
                name = (c.get("commit") or {}).get("author", {}).get("name")
                ident = (login or name or "").strip()
                if ident:
                    commit_authors_prior.add((r, ident))
        except Exception as e:
            log(f"[gh] commits {r}: {e}", debug)

    window_idents = {ident for (_, ident) in commit_authors_window}
    prior_idents = {ident for (_, ident) in commit_authors_prior}

    bus50, bus75 = compute_bus_factor_proxies(by_ident_counts, total_commits)

    def dr(a: dt.datetime, b: dt.datetime) -> str:
        return f"{a.date().isoformat()}..{b.date().isoformat()}"

    issues_opened = issues_closed = prs_opened = prs_merged = 0
    pr_merge_deltas_days: List[float] = []
    reviewers_per_pr: List[int] = []
    reviewer_counts: Dict[str, int] = {}
    author_counts: Dict[str, int] = {}

    for r in repos:
        try:
            issues_opened += gh_search_issues(f"repo:{r} is:issue created:{dr(start,end)}")
            issues_closed += gh_search_issues(f"repo:{r} is:issue closed:{dr(start,end)}")
            prs_opened += gh_search_issues(f"repo:{r} is:pr created:{dr(start,end)}")
            merged_items = gh_search_issue_items(f"repo:{r} is:pr is:merged merged:{dr(start,end)}")
            prs_merged += len(merged_items)
        except Exception as e:
            log(f"[gh] search {r}: {e}", debug)
            merged_items = []

        N_total = len(merged_items)
        if N_total > 0:
            required_n = sample_size(N_total)
            items_for_detail = merged_items if N_total <= required_n else random.sample(merged_items, required_n)
            if N_total <= required_n:
                log(f"[gh] PRs {r}: using all {N_total} merged", debug)
            else:
                log(f"[gh] PRs {r}: sampled {required_n}/{N_total}", debug)

            def _fetch_pr_metrics(item):
                number = item.get("number")
                if number is None:
                    mnum = re.search(r"/pull/(\d+)", item.get("html_url",""))
                    if not mnum:
                        return None
                    number = int(mnum.group(1))
                try:
                    pr = gh_get(f"https://api.github.com/repos/{r}/pulls/{int(number)}").json()
                    created = dt.datetime.fromisoformat(pr["created_at"].replace("Z","+00:00"))
                    merged_at = pr.get("merged_at")

                    author_login = ((pr.get("user") or {}).get("login") or "").strip()
                    delta_days = None
                    if merged_at:
                        merged = dt.datetime.fromisoformat(merged_at.replace("Z","+00:00"))
                        merged = to_naive_utc(merged)
                        if start <= merged <= end:
                            delta_days = (merged - to_naive_utc(created)).total_seconds() / 86400.0

                    try:
                        revs = gh_paginate(
                            f"https://api.github.com/repos/{r}/pulls/{int(number)}/reviews",
                            {"per_page": "100"}
                        )
                    except Exception:
                        revs = []

                    reviewers = set()
                    for rv in revs:
                        login = ((rv.get("user") or {}).get("login") or "").strip()
                        if login and not is_bot_login(login) and login != author_login:
                            reviewers.add(login)

                    return {
                        "delta_days": delta_days,
                        "author_login": author_login,
                        "reviewers": list(reviewers),
                    }
                except Exception as e:
                    log(f"[gh] get PR {r}#{number}: {e}", debug)
                    return None

            with ThreadPoolExecutor(max_workers=min(16, max(4, len(items_for_detail)//10))) as ex:
                futures = [ex.submit(_fetch_pr_metrics, it) for it in items_for_detail]
                for fut in as_completed(futures):
                    res = fut.result()
                    if not res:
                        continue
                    if res.get("delta_days") is not None:
                        pr_merge_deltas_days.append(res["delta_days"])
                    a = res.get("author_login")
                    if a and not is_bot_login(a):
                        author_counts[a] = author_counts.get(a, 0) + 1
                    revs = res.get("reviewers") or []
                    reviewers_per_pr.append(len(revs))
                    for u in revs:
                        reviewer_counts[u] = reviewer_counts.get(u, 0) + 1

    return {
        "commits": total_commits,
        "unique_committers": len(window_idents),
        "new_contributors": len(window_idents - prior_idents),
        "issues_opened": issues_opened,
        "issues_closed": issues_closed,
        "prs_opened": prs_opened,
        "prs_merged": prs_merged,
        "pr_median_merge_days": round(statistics.median(pr_merge_deltas_days), 1) if pr_merge_deltas_days else None,
        "bus_factor_50": bus50,
        "bus_factor_75": bus75,
        "median_reviewers_per_pr": round(statistics.median(reviewers_per_pr), 1) if reviewers_per_pr else None,
        "reviewer_diversity_effective": effective_diversity(reviewer_counts),
        "pr_author_diversity_effective": effective_diversity(author_counts),
        "reviewer_unique_sampled": len(reviewer_counts),
        "pr_author_unique_sampled": len(author_counts),
    }

# ---------------- Window selection (STRICT by age) ----------------

def select_windows_strict(today: dt.date, start_date: Optional[dt.date]) -> List[Tuple[str, dt.datetime, dt.datetime]]:
    """
    - If age < 3m: single 'to-date' window.
    - If 3m ≤ age < 6m: 3m only.
    - If 6m ≤ age < 12m: 3m and 6m.
    - If ≥12m: 3m, 6m, 12m.
    """
    if start_date is None:
        # If we can't find the start date, default to full set.
        return [
            ("3m", dt.datetime.combine(months_ago(today, 3), dt.time.min), dt.datetime.combine(today, dt.time.max)),
            ("6m", dt.datetime.combine(months_ago(today, 6), dt.time.min), dt.datetime.combine(today, dt.time.max)),
            ("12m", dt.datetime.combine(months_ago(today, 12), dt.time.min), dt.datetime.combine(today, dt.time.max)),
        ]

    age_days = (today - start_date).days
    if age_days < 90:
        return [("to-date", dt.datetime.combine(start_date, dt.time.min), dt.datetime.combine(today, dt.time.max))]
    wins: List[Tuple[str, dt.datetime, dt.datetime]] = []
    if age_days >= 90:
        wins.append(("3m", dt.datetime.combine(months_ago(today, 3), dt.time.min), dt.datetime.combine(today, dt.time.max)))
    if age_days >= 180:
        wins.append(("6m", dt.datetime.combine(months_ago(today, 6), dt.time.min), dt.datetime.combine(today, dt.time.max)))
    if age_days >= 365:
        wins.append(("12m", dt.datetime.combine(months_ago(today, 12), dt.time.min), dt.datetime.combine(today, dt.time.max)))
    return wins

# ---------------- Markdown (per-podling) ----------------

def render_md(podling: str, today: dt.date, windows: List["WindowMetrics"]) -> str:
    md: List[str] = []
    md.append(f"# {podling} — Incubator Health (Reports + GitHub + Mailing Lists)")
    md.append(f"_Generated on {today.isoformat()}_")
    md.append("")
    md.append("**Windows:** " + ", ".join([wm.window for wm in windows]))
    md.append("")

    if not windows:
        return "\n".join(md)

    # window refs
    short = windows[0]
    medium = windows[1] if len(windows) >= 2 else None
    longw = windows[2] if len(windows) >= 3 else (windows[-1] if len(windows) > 1 else None)

    # --- helpers (LOCAL to render_md) ---

    def guarded_rate(count: Optional[int], w: "WindowMetrics") -> Optional[float]:
        """Return per-month rate or None if window too short (<28d) or events too few (<5)."""
        if count is None:
            return None
        d = window_days(w.start, w.end)
        if d < MIN_DAYS_FOR_WINDOW or count < MIN_EVENTS_FOR_TREND:
            return None
        return rate_per_month(count, w.start, w.end)

    def comp_up_rate(curr_val, curr_w, prev_val, prev_w):
        """Compare counts as per-month rates with guards."""
        c = guarded_rate(curr_val, curr_w)
        p = guarded_rate(prev_val, prev_w)
        return "—" if (c is None or p is None) else trend_arrows(c, p, flat_tol=0.10)

    def comp_up(c, p):
        """Compare scalar metrics where higher is better (no rate/guard)."""
        return trend_arrows(c, p, flat_tol=0.10)

    def comp_improve(c, p):
        """Compare scalar metrics where LOWER is better (latencies)."""
        return arrows_from_score(trend_score(c, p, lower_is_better=True, flat_tol=0.10))

    def comp_improve_guarded_latency(curr_latency, curr_count, prev_latency, prev_count):
        """
        For latency derived from event samples (e.g., PR median merge days).
        Require >= MIN_EVENTS_FOR_TREND events in BOTH windows, else '—'.
        """
        if (curr_count or 0) < MIN_EVENTS_FOR_TREND or (prev_count or 0) < MIN_EVENTS_FOR_TREND:
            return "—"
        if curr_latency is None or prev_latency is None:
            return "—"
        return comp_improve(curr_latency, prev_latency)

    def comp_improve_guarded_release_gap(curr_gap_days, curr_release_count, prev_gap_days, prev_release_count):
        """
        'Median days between releases' requires at least 2 releases in EACH window.
        Otherwise there is no cadence to compare → '—'.
        """
        if (curr_release_count or 0) < 2 or (prev_release_count or 0) < 2:
            return "—"
        if curr_gap_days is None or prev_gap_days is None:
            return "—"
        return comp_improve(curr_gap_days, prev_gap_days)

    def comp_up_diversity_guarded(curr_eff, curr_sample_n, prev_eff, prev_sample_n):
        """
        Diversity indices (effective #) based on sampled PRs.
        Require at least MIN_EVENTS_FOR_TREND unique samples in BOTH windows, else '—'.
        """
        if (curr_sample_n or 0) < MIN_EVENTS_FOR_TREND or (prev_sample_n or 0) < MIN_EVENTS_FOR_TREND:
            return "—"
        if curr_eff is None or prev_eff is None:
            return "—"
        return comp_up(curr_eff, prev_eff)

    # --- Trends sections ---

    if medium:
        md.append("## Trends (short vs medium)")
        md.append("")
        md.append(f"- **Releases (from list votes/results):** {short.release_count} ({comp_up_rate(short.release_count, short, medium.release_count, medium)})")
        md.append(f"- **Median days between releases:** {short.release_median_days_between or '—'} ({comp_improve_guarded_release_gap(short.release_median_days_between, short.release_count, medium.release_median_days_between, medium.release_count)})")
        md.append(f"- **New contributors:** {short.new_contributors} ({comp_up_rate(short.new_contributors, short, medium.new_contributors, medium)})")
        md.append(f"- **Unique committers:** {short.unique_committers} ({comp_up_rate(short.unique_committers, short, medium.unique_committers, medium)})")
        md.append(f"- **Commits:** {short.commits} ({comp_up_rate(short.commits, short, medium.commits, medium)})")
        md.append(f"- **Issues opened/closed:** {short.issues_opened}/{short.issues_closed} ({comp_up_rate(short.issues_opened, short, medium.issues_opened, medium)}/{comp_up_rate(short.issues_closed, short, medium.issues_closed, medium)})")
        md.append(f"- **PRs opened/merged:** {short.prs_opened}/{short.prs_merged} ({comp_up_rate(short.prs_opened, short, medium.prs_opened, medium)}/{comp_up_rate(short.prs_merged, short, medium.prs_merged, medium)})")
        md.append(f"- **Median PR time-to-merge (days):** {short.pr_median_merge_days or '—'} ({comp_improve_guarded_latency(short.pr_median_merge_days, short.prs_merged, medium.pr_median_merge_days, medium.prs_merged)})")
        md.append(f"- **Bus factor proxy (contributors to reach 50% / 75% of commits):** {short.bus_factor_50 or '—'} / {short.bus_factor_75 or '—'} ({comp_up(short.bus_factor_50 or 0, medium.bus_factor_50 or 0)}/{comp_up(short.bus_factor_75 or 0, medium.bus_factor_75 or 0)})")
        md.append(f"- **Mailing list msgs (dev@):** {short.dev_messages} ({comp_up_rate(short.dev_messages, short, medium.dev_messages, medium)})")
        md.append(f"- **Unique posters (dev@):** {short.dev_unique_posters} ({comp_up_rate(short.dev_unique_posters, short, medium.dev_unique_posters, medium)})")
        md.append(f"- **Reviewer diversity (eff.#, sampled):** {short.reviewer_diversity_effective or '—'} ({comp_up_diversity_guarded(short.reviewer_diversity_effective, short.reviewer_unique_sampled, medium.reviewer_diversity_effective, medium.reviewer_unique_sampled)})")
        md.append(f"- **PR author diversity (eff.#, sampled):** {short.pr_author_diversity_effective or '—'} ({comp_up_diversity_guarded(short.pr_author_diversity_effective, short.pr_author_unique_sampled, medium.pr_author_diversity_effective, medium.pr_author_unique_sampled)})")
        md.append(f"- **Unique reviewers (sampled):** {short.reviewer_unique_sampled} ({comp_up_rate(short.reviewer_unique_sampled, short, medium.reviewer_unique_sampled, medium)})")
        md.append(f"- **Unique PR authors (sampled):** {short.pr_author_unique_sampled} ({comp_up_rate(short.pr_author_unique_sampled, short, medium.pr_author_unique_sampled, medium)})")
        md.append("")

    if longw and longw is not short:
        md.append("## Trends (short vs long)")
        md.append("")
        md.append(f"- **Releases (from list votes/results):** {short.release_count} ({comp_up_rate(short.release_count, short, longw.release_count, longw)})")
        md.append(f"- **Median days between releases:** {short.release_median_days_between or '—'} ({comp_improve_guarded_release_gap(short.release_median_days_between, short.release_count, longw.release_median_days_between, longw.release_count)})")
        md.append(f"- **New contributors:** {short.new_contributors} ({comp_up_rate(short.new_contributors, short, longw.new_contributors, longw)})")
        md.append(f"- **Unique committers:** {short.unique_committers} ({comp_up_rate(short.unique_committers, short, longw.unique_committers, longw)})")
        md.append(f"- **Commits:** {short.commits} ({comp_up_rate(short.commits, short, longw.commits, longw)})")
        md.append(f"- **Issues opened/closed:** {short.issues_opened}/{short.issues_closed} ({comp_up_rate(short.issues_opened, short, longw.issues_opened, longw)}/{comp_up_rate(short.issues_closed, short, longw.issues_closed, longw)})")
        md.append(f"- **PRs opened/merged:** {short.prs_opened}/{short.prs_merged} ({comp_up_rate(short.prs_opened, short, longw.prs_opened, longw)}/{comp_up_rate(short.prs_merged, short, longw.prs_merged, longw)})")
        md.append(f"- **Median PR time-to-merge (days):** {short.pr_median_merge_days or '—'} ({comp_improve_guarded_latency(short.pr_median_merge_days, short.prs_merged, longw.pr_median_merge_days, longw.prs_merged)})")
        md.append(f"- **Bus factor proxy (contributors to reach 50% / 75% of commits):** {short.bus_factor_50 or '—'} / {short.bus_factor_75 or '—'} ({comp_up(short.bus_factor_50 or 0, longw.bus_factor_50 or 0)}/{comp_up(short.bus_factor_75 or 0, longw.bus_factor_75 or 0)})")
        md.append(f"- **Mailing list msgs (dev@):** {short.dev_messages} ({comp_up_rate(short.dev_messages, short, longw.dev_messages, longw)})")
        md.append(f"- **Unique posters (dev@):** {short.dev_unique_posters} ({comp_up_rate(short.dev_unique_posters, short, longw.dev_unique_posters, longw)})")
        md.append(f"- **Reviewer diversity (eff.#, sampled):** {short.reviewer_diversity_effective or '—'} ({comp_up_diversity_guarded(short.reviewer_diversity_effective, short.reviewer_unique_sampled, longw.reviewer_diversity_effective, longw.reviewer_unique_sampled)})")
        md.append(f"- **PR author diversity (eff.#, sampled):** {short.pr_author_diversity_effective or '—'} ({comp_up_diversity_guarded(short.pr_author_diversity_effective, short.pr_author_unique_sampled, longw.pr_author_diversity_effective, longw.pr_author_unique_sampled)})")
        md.append(f"- **Unique reviewers (sampled):** {short.reviewer_unique_sampled} ({comp_up_rate(short.reviewer_unique_sampled, short, longw.reviewer_unique_sampled, longw)})")
        md.append(f"- **Unique PR authors (sampled):** {short.pr_author_unique_sampled} ({comp_up_rate(short.pr_author_unique_sampled, short, longw.pr_author_unique_sampled, longw)})")
        md.append("")

    # --- Details and legend ---

    md.append("## Window Details")
    for m in windows:
        md.append(f"### {m.window}  ({m.start.date()} → {m.end.date()})")
        md.append("- **Releases (from list votes/results):** {}  |  **Median gap (days):** {}".format(
            m.release_count, m.release_median_days_between if m.release_median_days_between is not None else "—"))
        md.append("- **New contributors:** {}  |  **Unique committers:** {}  |  **Commits:** {}".format(
            m.new_contributors, m.unique_committers, m.commits))
        md.append("- **Issues:** opened {} / closed {}".format(m.issues_opened, m.issues_closed))
        md.append("- **PRs:** opened {} / merged {}  |  **Median merge time (days):** {}".format(
            m.prs_opened, m.prs_merged, m.pr_median_merge_days if m.pr_median_merge_days is not None else "—"))
        md.append("- **Reviews (sampled):** median reviewers/PR **{}**  |  reviewer diversity (eff.#) **{}**  |  PR author diversity (eff.#) **{}**  |  unique reviewers **{}**, unique authors **{}**".format(
            m.median_reviewers_per_pr if m.median_reviewers_per_pr is not None else "—",
            m.reviewer_diversity_effective if m.reviewer_diversity_effective is not None else "—",
            m.pr_author_diversity_effective if m.pr_author_diversity_effective is not None else "—",
            m.reviewer_unique_sampled, m.pr_author_unique_sampled
        ))
        md.append("- **Bus factor proxy (50% / 75%):** {} / {}".format(
            m.bus_factor_50 if m.bus_factor_50 is not None else "—",
            m.bus_factor_75 if m.bus_factor_75 is not None else "—"))
        md.append("- **Incubator reports:** {}  |  **Avg mentor sign-offs:** {}".format(
            m.reports_count, m.avg_mentor_signoffs if m.avg_mentor_signoffs is not None else "—"))
        md.append("- **Mailing lists:** dev messages **{}**, dev unique posters **{}**".format(
            m.dev_messages, m.dev_unique_posters))
        md.append("")
    md.append(
        "## Reading the Indicators\n"
        "- **Use trend arrows** to compare available windows; when a window lacks ≥28 days or ≥5 events, trends show **—**.\n"
        "- **Look for balance:** steady releases, active community discussions, and a mix of reviewers signal healthier progress.\n"
        "- **Check anomalies:** sudden drop-offs or spikes may need mentor follow-up.\n"
        "- **Consider proportionality:** absolute numbers matter less than whether activity is sustainable for the project’s size.\n"
        "- **Watch diversity trends:** concentration in one person or company is a risk, even if raw activity looks strong.\n"
        "- **Look beyond developers:** list traffic and wider participation matter as much as GitHub stats.\n"
        "- **Treat results as conversation starters:** these outputs inform mentoring; they aren’t pass/fail scores.\n"
        "\n"
        "#### Trend Arrows Legend\n"
        "- →  = change within ±10% (flat)\n"
        "- ↗ / ↘ = 10–25% increase / decrease (small)\n"
        "- ↗↗ / ↘↘ = 25–100% increase / decrease (medium)\n"
        "- ↗↗↗ / ↘↘↘ = ≥100% increase / decrease (large)\n"
    )
    return "\n".join(md)

# ---------------- Main ----------------

def main():
    args = parse_args()
    today = parse_today(args.today)

    # Load podlings.xml once so we can get start dates
    root = load_podlings_root(args.podlings_xml, debug=args.debug)

    # Podling set
    if args.all:
        podlings = fetch_podlings(root)
        if not podlings:
            sys.exit("[error] No current podlings found in podlings.xml")
        if not args.out_md_dir:
            sys.exit("[error] --all requires --out-md-dir for per-podling Markdown.")
        os.makedirs(args.out_md_dir, exist_ok=True)
        log(f"[start] processing ALL current podlings: {len(podlings)}", args.debug)
    else:
        podlings = [args.podling.strip()]
        log(f"[start] processing podling: {podlings[0]}", args.debug)

    # CSV writer
    csv_writer = None
    csv_file = None
    if args.out_csv:
        csv_file = open(args.out_csv, "w", newline="", encoding="utf-8")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            "podling","window","start","end",
            "release_count","release_median_days_between",
            "commits","unique_committers","new_contributors",
            "issues_opened","issues_closed",
            "prs_opened","prs_merged","pr_median_merge_days",
            "median_reviewers_per_pr","reviewer_diversity_effective","pr_author_diversity_effective",
            "reviewer_unique_sampled","pr_author_unique_sampled",
            "bus_factor_50","bus_factor_75",
            "reports_count","avg_mentor_signoffs",
            "dev_messages","dev_unique_posters"
        ])
        log(f"[write] CSV header -> {args.out_csv}", args.debug)

    total = len(podlings)
    summary_rows: List[Tuple[str, int]] = []

    for idx, podling in enumerate(podlings, 1):
        log(f"[{idx}/{total}] {podling}", args.debug)

        # Repo guess if not provided — prefer apache/<slug> only
        if args.repos:
            repos = args.repos[:]
        else:
            slug = re.sub(r"[^a-z0-9]+", "-", podling.lower())
            repos = [f"apache/{slug}"]
        log(f"  [repos] {', '.join(repos)}", args.debug)

        # Strict window selection by podling age
        pod_start = get_podling_start_date(root, podling)
        if pod_start:
            log(f"  [age] start {pod_start.isoformat()} (age {(today - pod_start).days} days)", args.debug)
        else:
            log(f"  [age] start UNKNOWN — defaulting to full 3m/6m/12m", args.debug)

        win_specs = select_windows_strict(today, pod_start)

        windows: List[WindowMetrics] = []
        for label, start, end in win_specs:
            log(f"  [win {label}] {to_iso_date(start)} → {to_iso_date(end)}", args.debug)

            wm = WindowMetrics(window=label, start=start, end=end)

            # Reports (mentor sign-offs)
            log("    [reports] agendas …", args.debug)
            rep = collect_reports(args.minutes_dir, podling, start, end)
            wm.reports_count = len(rep)
            if wm.reports_count:
                signoff_counts = [len(set(r.get("signoffs") or [])) for r in rep]
                wm.avg_mentor_signoffs = round(sum(signoff_counts) / len(signoff_counts), 2) if signoff_counts else None

            # Mailing lists (activity + official releases)
            log("    [lists] dev@ + incubator-general …", args.debug)
            ml = scan_lists_for_window(podling, start, end, debug=args.debug)
            wm.dev_messages = ml["dev_messages"]
            wm.dev_unique_posters = ml["dev_unique_posters"]

            release_dates = ml.get("release_event_dates", [])
            wm.release_count = len(release_dates)
            wm.release_median_days_between = median_days_between(release_dates) if release_dates else None
            log(f"    [lists] releases found: {wm.release_count}", args.debug)
            if args.debug and release_dates[:3]:
                samp = ", ".join(d.date().isoformat() for d in release_dates[:3])
                log(f"      sample release dates: {samp}{' …' if len(release_dates)>3 else ''}", args.debug)

            # GitHub metrics (incl. bus factor + diversity)
            log("    [gh] commits/issues/prs/diversity …", args.debug)
            gh = compute_github_metrics(repos, start, end, debug=args.debug)
            for k, v in gh.items():
                setattr(wm, k, v)

            windows.append(wm)

            # CSV row
            if csv_writer:
                csv_writer.writerow([
                    podling, wm.window, wm.start.date(), wm.end.date(),
                    wm.release_count, wm.release_median_days_between if wm.release_median_days_between is not None else "",
                    wm.commits, wm.unique_committers, wm.new_contributors,
                    wm.issues_opened, wm.issues_closed,
                    wm.prs_opened, wm.prs_merged, wm.pr_median_merge_days if wm.pr_median_merge_days is not None else "",
                    wm.median_reviewers_per_pr if wm.median_reviewers_per_pr is not None else "",
                    wm.reviewer_diversity_effective if wm.reviewer_diversity_effective is not None else "",
                    wm.pr_author_diversity_effective if wm.pr_author_diversity_effective is not None else "",
                    wm.reviewer_unique_sampled, wm.pr_author_unique_sampled,
                    wm.bus_factor_50 if wm.bus_factor_50 is not None else "",
                    wm.bus_factor_75 if wm.bus_factor_75 is not None else "",
                    wm.reports_count, wm.avg_mentor_signoffs if wm.avg_mentor_signoffs is not None else "",
                    wm.dev_messages, wm.dev_unique_posters
                ])

        # Markdown per podling
        if args.all:
            out_path = os.path.join(args.out_md_dir, f"{re.sub(r'[^A-Za-z0-9_-]+','_', podling)}.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(render_md(podling, today, windows))
            log(f"  [write] {out_path}", args.debug)
        else:
            if args.out_md:
                with open(args.out_md, "w", encoding="utf-8") as f:
                    f.write(render_md(podling, today, windows))
                log(f"  [write] {args.out_md}", args.debug)
            else:
                print(render_md(podling, today, windows))

    if csv_file:
        csv_file.close()
        log(f"[write] CSV -> {args.out_csv}", args.debug)

    print(f"[done] processed podlings: {len(podlings)}")

if __name__ == "__main__":
    main()
