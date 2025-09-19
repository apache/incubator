#!/usr/bin/env python3
# podling_6mo_values.py
# Generate <=6mo podling metrics (CSV/MD).
#
# Note that this code is mostly AI generated.
#

import argparse
import csv
import os
import sys
import time
import re
import glob
import email
from email.parser import BytesParser
from email.policy import default as EMAIL_DEFAULT
from datetime import datetime, timezone, timedelta
from dateutil import parser as dtp
from typing import Dict, Any, Optional, Tuple, List, Set
from urllib.parse import urlparse, parse_qs

import requests
from tabulate import tabulate

# ---------------- Constants ----------------

W_PUBLIC = "https://whimsy.apache.org/public"
URL_PODLINGS = f"{W_PUBLIC}/public_podlings.json"
URL_PODLING_STATUS = f"{W_PUBLIC}/public_podling_status.json"
URL_LDAP_PROJECTS = f"{W_PUBLIC}/public_ldap_projects.json"

TODAY = datetime.now(timezone.utc).date()

# Stable mailing list API (mbox)
LAA_MBOX = "https://lists.apache.org/api/mbox.lua"

# Subjects
RELEASE_VOTE_SUBJECT = re.compile(r"\[(?:VOTE)\].*\b(RELEASE|INCUBATING)\b", re.I)
SUBJ_PREFIX_RE = re.compile(r'^\s*(re|fwd|fw)\s*:\s*', re.I)

# Growth heuristics on general@incubator
PPMC_VOTE_SUBJECT = re.compile(r"\[(?:VOTE|RESULT)\].*(PPMC|PMC).*(member|add|appoint)", re.I)
COMMITTER_VOTE_SUBJECT = re.compile(r"\[(?:VOTE|RESULT)\].*committer", re.I)

# GitHub
GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Repo discovery filters (avoid websites/docs-only)
EXCLUDE_SUFFIXES = (
    "-site", "-website", "-site-pub", "-asf-site", "-asf-site-src",
    "-images", "-logos", "-branding", "-docs", "-documentation", "-examples"
)

# ---------------- HTTP helpers ----------------

def http_json(url: str, params: Optional[Dict[str, Any]] = None,
              headers: Optional[Dict[str, str]] = None,
              retries: int = 3, backoff: float = 1.5) -> Any:
    last = None
    for i in range(retries):
        try:
            h = {"Accept": "application/json"}
            if url.startswith(GITHUB_API):
                h["Accept"] = "application/vnd.github+json"
                if GITHUB_TOKEN:
                    h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
            if headers:
                h.update(headers)
            r = requests.get(url, params=params, headers=h, timeout=45)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            last = e
            if i < retries - 1:
                time.sleep(backoff ** (i + 1))
    raise last

def http_text(url: str, params: Optional[Dict[str, Any]] = None,
              headers: Optional[Dict[str, str]] = None,
              retries: int = 3, backoff: float = 1.5) -> str:
    last = None
    for i in range(retries):
        try:
            h = {"Accept": "text/plain"}
            if headers:
                h.update(headers)
            r = requests.get(url, params=params, headers=h, timeout=60)
            r.raise_for_status()
            r.encoding = r.encoding or "utf-8"
            return r.text
        except Exception as e:
            last = e
            if i < retries - 1:
                time.sleep(backoff ** (i + 1))
    raise last

def http_json_paginated(url: str, params: Dict[str, Any], item_key: Optional[str] = None) -> List[Any]:
    out = []
    page = 1
    while True:
        p = dict(params or {})
        p.setdefault("per_page", 100)
        p["page"] = page
        data = http_json(url, params=p)
        if isinstance(data, list):
            chunk = data
        elif isinstance(data, dict) and item_key and item_key in data:
            chunk = data[item_key]
        else:
            chunk = []
        out.extend(chunk)
        if len(chunk) < p.get("per_page", 30):
            break
        page += 1
    return out

# ---------------- Utilities ----------------

def months_between(start_date, end_date):
    m = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    if end_date.day < start_date.day:
        m -= 1
    return max(0, m)

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", (s or "").strip().lower()).strip("-")

def canon_subject(s: str) -> str:
    if not s:
        return ""
    prev = None
    out = s.strip()
    while prev != out:
        prev = out
        out = SUBJ_PREFIX_RE.sub("", out).strip()
    return re.sub(r"\s+", " ", out).lower()

def months_covering_last_days(days: int, today_dt: Optional[datetime] = None) -> List[Tuple[int, int]]:
    if not today_dt:
        today_dt = datetime.now(timezone.utc)
    start = today_dt - timedelta(days=days)
    y, m = start.year, start.month
    res: List[Tuple[int, int]] = []
    while (y, m) <= (today_dt.year, today_dt.month):
        res.append((y, m))
        if m == 12:
            y, m = y + 1, 1
        else:
            m += 1
    return res

def to_int(x, default=0):
    try:
        return int(x)
    except Exception:
        try:
            return int(float(x))
        except Exception:
            return default

# ---------------- Mailing lists (mbox) ----------------

def fetch_month_mbox(domain: str, listname: str, year: int, month: int, debug: bool=False) -> str:
    dval = f"{year:04d}-{month:02d}"
    params = {"list": listname, "domain": domain, "d": dval}
    try:
        return http_text(LAA_MBOX, params=params)
    except Exception as e:
        if debug:
            print(f"    · no mbox for {listname}@{domain} {dval} ({e})")
        return ""

def iter_mbox_messages(mbox_text: str):
    chunks = re.split(r'(?m)^From [^\n]*\n', mbox_text)
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            yield BytesParser(policy=EMAIL_DEFAULT).parsebytes(chunk.encode('utf-8', errors='ignore'))
        except Exception:
            headers, _, _ = chunk.partition("\n\n")
            msg = email.message.EmailMessage()
            for line in headers.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    msg[k.strip()] = v.strip()
            yield msg

def infer_dev_list_domain(pod_id: str, meta: Dict[str, Any]) -> str:
    return f"{pod_id}.apache.org"

def lists_activity_dev(dev_domain: str, days: int, debug: bool=False) -> Tuple[int, int, int, List[str]]:
    """
    Returns: (unique_posters, release_vote_threads, total_emails, sample_senders)
    """
    unique_senders: Set[str] = set()
    vote_threads: Set[str] = set()
    sample_senders: List[str] = []
    email_count = 0

    for (y, m) in months_covering_last_days(days):
        mbox = fetch_month_mbox(dev_domain, "dev", y, m, debug)
        if not mbox:
            continue
        for msg in iter_mbox_messages(mbox):
            email_count += 1
            subj = str(msg.get("Subject", "") or "")
            frm  = str(msg.get("From", "") or msg.get("Sender", "") or "")
            addr = email.utils.parseaddr(frm)[1].strip().lower() if frm else ""
            if addr:
                if addr not in unique_senders and len(sample_senders) < 25:
                    sample_senders.append(addr)
                unique_senders.add(addr)
            if RELEASE_VOTE_SUBJECT.search(subj or ""):
                vote_threads.add(canon_subject(subj))

    return (len(unique_senders), len(vote_threads), email_count, sample_senders)

def lists_release_votes_general(pod_id: str, pod_name: str, days: int, debug: bool=False) -> int:
    name_pat = re.compile(re.escape(pod_name), re.I)
    id_pat   = re.compile(rf"\b{re.escape(pod_id)}\b", re.I)
    seen_threads: Set[str] = set()

    for (y, m) in months_covering_last_days(days):
        mbox = fetch_month_mbox("incubator.apache.org", "general", y, m, debug)
        if not mbox:
            continue
        for msg in iter_mbox_messages(mbox):
            subj = str(msg.get("Subject", "") or "")
            if subj and RELEASE_VOTE_SUBJECT.search(subj) and (name_pat.search(subj) or id_pat.search(subj)):
                seen_threads.add(canon_subject(subj))

    return len(seen_threads)

def lists_growth_general(pod_id: str, pod_name: str, days: int, debug: bool=False) -> Tuple[int, int]:
    name_pat = re.compile(re.escape(pod_name), re.I)
    id_pat   = re.compile(rf"\b{re.escape(pod_id)}\b", re.I)
    ppmc_threads: Set[str] = set()
    comm_threads: Set[str] = set()

    for (y, m) in months_covering_last_days(days):
        mbox = fetch_month_mbox("incubator.apache.org", "general", y, m, debug)
        if not mbox:
            continue
        for msg in iter_mbox_messages(mbox):
            subj = str(msg.get("Subject", "") or "")
            if not subj:
                continue
            norm_s = canon_subject(subj)
            if (name_pat.search(subj) or id_pat.search(subj)):
                if PPMC_VOTE_SUBJECT.search(subj):
                    ppmc_threads.add(norm_s)
                if COMMITTER_VOTE_SUBJECT.search(subj):
                    comm_threads.add(norm_s)

    return len(ppmc_threads), len(comm_threads)

# ---------------- Mentor reports/sign-offs (board agendas) ----------------

H2_THIS_POD_RE = lambda pod_id, pod_name: re.compile(
    rf'(?mi)^\s*##\s+(?:{re.escape(pod_id)}|{re.escape(pod_name)})\s*$'
)
SIGNED_OFF_RE   = re.compile(r'(?mi)^\s*#+\s*Signed[- ]off[- ]by\s*:\s*$')
BLOCK_END_RE    = re.compile(r'(?m)^(?:##\s+|###\s+|-{5,}\s*$)')   # next H2/H3 or dashed rule
CHECKBOX_RE     = re.compile(r'\[(?:x|X)\]')

def count_reports_and_signoffs(pod_id: str, pod_name: str, minutes_dir: str, debug: bool=False) -> Tuple[int, int]:
    """
    reports_count: +1 per agenda file that contains an H2 header '## <pod_id|pod_name>'
    mentor_signoffs: number of [X]/[x] checkboxes inside the pod's section, within any
                     'Signed-off-by:' block(s), up to the next '##'/'###' or dashed rule.
    """
    if not minutes_dir:
        return 0, 0

    reports = 0
    total_signoffs = 0
    for path in sorted(glob.glob(os.path.join(minutes_dir, "board_agenda_*.txt"))):
        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                txt = f.read()
        except Exception as e:
            if debug:
                print(f"! error reading {path}: {e}", file=sys.stderr)
            continue

        section_re = H2_THIS_POD_RE(pod_id, pod_name)
        sec_match = section_re.search(txt)
        if not sec_match:
            if debug:
                print(f"{os.path.basename(path)}: no section for {pod_id}")
            continue

        reports += 1
        sec_start = sec_match.end()
        next_h2 = re.search(r'(?m)^\s*##\s+', txt[sec_start:])
        sec_end = sec_start + (next_h2.start() if next_h2 else 0) if next_h2 else len(txt)
        section = txt[sec_start:sec_end]

        local_signoffs = 0
        for sm in SIGNED_OFF_RE.finditer(section):
            bstart = sm.end()
            bend_m = BLOCK_END_RE.search(section, bstart)
            bend = bend_m.start() if bend_m else len(section)
            block = section[bstart:bend]
            local_signoffs += len(CHECKBOX_RE.findall(block))

        total_signoffs += local_signoffs
        if debug:
            print(f"{os.path.basename(path)}: report=1, signoffs+={local_signoffs}")

    return reports, total_signoffs

# --------- Audit mode (show exactly what’s counted) ---------

def audit_minutes_for_pod(pod_id: str, pod_name: str, minutes_dir: str) -> None:
    """
    Prints an audit trail: for each board_agenda_*.txt
      - whether ## <pod> section found
      - each Signed-off-by block within that section
      - each [X] line counted
    """
    if not minutes_dir:
        print("No minutes_dir provided.")
        return

    H2_RE = H2_THIS_POD_RE(pod_id, pod_name)

    for path in sorted(glob.glob(os.path.join(minutes_dir, "board_agenda_*.txt"))):
        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                txt = f.read()
        except Exception as e:
            print(f"{os.path.basename(path)}: ! read error: {e}")
            continue

        sec = H2_RE.search(txt)
        if not sec:
            print(f"{os.path.basename(path)}: section: NO")
            continue

        sec_start = sec.end()
        next_h2 = re.search(r'(?m)^\s*##\s+', txt[sec_start:])
        sec_end = sec_start + (next_h2.start() if next_h2 else 0) if next_h2 else len(txt)
        section = txt[sec_start:sec_end]
        print(f"{os.path.basename(path)}: section: YES (bytes {sec_start}-{sec_end})")

        total_block = 0
        for sm in SIGNED_OFF_RE.finditer(section):
            bstart = sm.end()
            bend_m = BLOCK_END_RE.search(section, bstart)
            bend = bend_m.start() if bend_m else len(section)
            block = section[bstart:bend]
            lines = [ln.rstrip() for ln in block.splitlines() if CHECKBOX_RE.search(ln)]
            total_block += len(lines)
            print("  Signed-off-by block:")
            for ln in lines:
                print(f"    COUNTED: {ln}")
        print(f"  => mentor_signoffs in file: {total_block}")

# ---------------- GitHub helpers ----------------

class Github422(Exception):
    pass

def gh_repo_exists_full(full: str) -> bool:
    try:
        http_json(f"{GITHUB_API}/repos/{full}")
        return True
    except Exception:
        return False

def gh_repo_info(owner_repo: str) -> Dict[str, Any]:
    """Fetch repository metadata (used to respect has_issues)."""
    return http_json(f"{GITHUB_API}/repos/{owner_repo}")

def gh_count_via_link_header(url: str, params: Dict[str, Any]) -> int:
    """
    Count items using per_page=1 + Link rel=last heuristic (works for /pulls).
    Returns 0 on 422 or if the endpoint doesn’t support paging.
    """
    p = dict(params or {})
    p.setdefault("per_page", 1)
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    r = requests.get(url, params=p, headers=headers, timeout=45)
    if r.status_code == 422:
        return 0
    r.raise_for_status()

    link = r.headers.get("Link", "")
    if not link:
        try:
            data = r.json()
            return len(data) if isinstance(data, list) else 0
        except Exception:
            return 0

    last_page = 1
    for part in link.split(","):
        if 'rel="last"' in part:
            m = re.search(r'<([^>]+)>', part)
            if not m:
                continue
            last_url = m.group(1)
            q = parse_qs(urlparse(last_url).query)
            try:
                last_page = int((q.get("page") or ["1"])[0])
            except Exception:
                last_page = 1
            break
    return last_page

def gh_search_count_safe(query: str) -> int:
    """
    Use GitHub search API for counts; on errors return 0 instead of raising.
    """
    try:
        url = f"{GITHUB_API}/search/issues"
        data = http_json(url, params={"q": query})
        return int(data.get("total_count", 0))
    except Exception:
        return 0

def gh_repo_contributors(owner_repo: str) -> Set[str]:
    owner_repo = owner_repo.strip()
    print(f"    · GitHub: contributors for {owner_repo} ...")
    url = f"{GITHUB_API}/repos/{owner_repo}/contributors"
    params = {"anon": "1", "per_page": 100}
    people = http_json_paginated(url, params, item_key=None)
    ids: Set[str] = set()
    for p in people:
        login = p.get("login")
        if login:
            ids.add(login.lower())
        else:
            name = (p.get("name") or "").strip().lower()
            if name:
                ids.add(f"anon:{name}")
    return ids

def gh_repo_issue_pr_breakdown(owner_repo: str, debug: bool=False) -> Tuple[int, int, int, int]:
    """
    Returns (open_issues, closed_issues, open_prs, closed_prs).
    - PRs counted via /pulls and Link rel=last.
    - Issues counted via search/issues; if search fails or has_issues=False → 0/0.
    """
    # PR counts
    try:
        open_prs = gh_count_via_link_header(f"{GITHUB_API}/repos/{owner_repo}/pulls", {"state": "open"})
    except Exception as e:
        if debug:
            print(f"      · PR open count fallback error for {owner_repo}: {e}", file=sys.stderr)
        open_prs = 0

    try:
        closed_prs = gh_count_via_link_header(f"{GITHUB_API}/repos/{owner_repo}/pulls", {"state": "closed"})
    except Exception as e:
        if debug:
            print(f"      · PR closed count fallback error for {owner_repo}: {e}", file=sys.stderr)
        closed_prs = 0

    # Issue counts
    open_issues = closed_issues = 0
    try:
        info = gh_repo_info(owner_repo)
        if not info.get("has_issues", True):
            if debug:
                print(f"      · issues disabled for {owner_repo}; setting issue counts to 0")
        else:
            open_issues   = gh_search_count_safe(f"repo:{owner_repo} is:issue is:open")
            closed_issues = gh_search_count_safe(f"repo:{owner_repo} is:issue is:closed")
    except Exception as e:
        if debug:
            print(f"      · issue count error for {owner_repo}: {e}", file=sys.stderr)
        # leave zeros

    return open_issues, closed_issues, open_prs, closed_prs

def gh_search_repos(query: str, per_page: int = 50) -> List[Dict[str, Any]]:
    url = f"{GITHUB_API}/search/repositories"
    data = http_json(url, params={"q": query, "per_page": per_page})
    return data.get("items", []) if isinstance(data, dict) else []

def load_repo_map(path: str) -> Dict[str, List[str]]:
    mapping: Dict[str, List[str]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            pid = (row.get("podling") or "").strip().lower()
            repo = (row.get("repo") or "").strip()
            if not pid or not repo:
                continue
            mapping.setdefault(pid, []).append(repo)
    return mapping

def name_candidates(pod_id: str, meta: Dict[str, Any]) -> List[str]:
    cands = {norm(pod_id)}
    res = meta.get("resource") or meta.get("podling") or ""
    if res:
        cands.add(norm(res))
    for alias in (meta.get("resourceAliases") or []) + (meta.get("aliases") or []):
        if alias:
            cands.add(norm(alias))
    cands = {re.sub(r"^apache-", "", x) for x in cands}
    return sorted(cands)

def discover_apache_repos(pod_id: str, meta: Dict[str, Any], debug: bool=False) -> List[str]:
    cands = name_candidates(pod_id, meta)
    if debug:
        print(f"    · repo name candidates: {', '.join(cands)}")
    found: List[str] = []
    checked: Set[str] = set()

    for base in cands:
        for pat in (base, f"incubator-{base}"):
            full = f"apache/{pat}"
            if full in checked:
                continue
            checked.add(full)
            if gh_repo_exists_full(full):
                found.append(full)

    if found:
        return sorted(set(found))

    search_items: List[Dict[str, Any]] = []
    for base in cands:
        for q in (f"org:apache in:name {base}", f"org:apache in:name incubator-{base}"):
            try:
                items = gh_search_repos(q, per_page=50)
                search_items.extend(items or [])
            except Exception as e:
                if debug:
                    print(f"      ! repo search failed for '{q}': {e}", file=sys.stderr)
                continue

    def keep(n: str) -> bool:
        n = n.lower()
        if any(n.endswith(suf) for suf in EXCLUDE_SUFFIXES):
            return False
        return any(n == x or n.startswith(f"{x}-") or n == f"incubator-{x}" or n.startswith(f"incubator-{x}-")
                   for x in cands)

    for it in search_items:
        name = it.get("name", "")
        full = it.get("full_name", "")
        if not full.startswith("apache/"):
            continue
        if keep(name):
            found.append(full)

    # Dedup preserve order
    seen: Set[str] = set()
    rv: List[str] = []
    for f in found:
        if f not in seen:
            seen.add(f)
            rv.append(f)

    if debug and not rv:
        print("    · no candidate repos found in apache/", file=sys.stderr)
    return rv

# ---------------- Main ----------------

def main():
    parser = argparse.ArgumentParser(description="Generate <=6mo podling metrics CSV/MD (no template/scoring).")
    parser.add_argument("--out", default="podlings_under6mo.csv", help="CSV output path")
    parser.add_argument("--md", default="podlings_under6mo.md", help="Markdown table output path")
    parser.add_argument("--lists-activity", type=int, default=180, help="Days window for lists activity [default: 180]")
    parser.add_argument("--repos", default="", help="CSV mapping podling->repo (columns: podling,repo)")
    parser.add_argument("--emit-repo-map", default="", help="Write discovered/mapped repos to CSV")
    parser.add_argument("--minutes-dir", default="", help="Path to board agenda text files (for mentor sign-offs & reports)")
    parser.add_argument("--no-auto-repos", dest="auto_repos", action="store_false",
                        help="Disable auto-discovering GitHub repos under github.com/apache")
    parser.set_defaults(auto_repos=True)
    parser.add_argument("--debug", action="store_true", help="Verbose debug logging")
    parser.add_argument("--audit-pod", default="", help="Audit board_agenda matches for this pod (id or name) and exit")

    args = parser.parse_args()

    if (args.repos or args.auto_repos) and not GITHUB_TOKEN:
        print("WARN: GitHub access without GITHUB_TOKEN may hit rate limits.", file=sys.stderr)

    print("Fetching podling metadata from Whimsy...")
    podlings = http_json(URL_PODLINGS).get("podling", {})
    pstatus = http_json(URL_PODLING_STATUS).get("podling", {})
    ldapproj = http_json(URL_LDAP_PROJECTS).get("projects", {})

    # If auditing, run once and exit
    if args.audit_pod:
        pid = None; pname = None
        for k, meta in podlings.items():
            if k.lower() == args.audit_pod.lower():
                pid = k; pname = meta.get("name", k); break
        if not pid:
            for k, meta in podlings.items():
                if str(meta.get("name","")).lower() == args.audit_pod.lower():
                    pid = k; pname = meta.get("name", k); break
        if not pid:
            pid = args.audit_pod; pname = args.audit_pod
        print(f"Auditing pod: id='{pid}' name='{pname}' in {args.minutes_dir or '(no minutes_dir)'}")
        audit_minutes_for_pod(pid, pname, args.minutes_dir)
        return

    # Optional explicit repo mappings
    repo_map: Dict[str, List[str]] = {}
    if args.repos:
        print(f"Loading repo mapping from {args.repos} ...")
        repo_map = load_repo_map(args.repos)

    rows: List[Dict[str, Any]] = []
    per_pod_repos: Dict[str, List[str]] = {}

    for pod_id, meta in podlings.items():
        if pstatus.get(pod_id) != "current":
            continue
        start = meta.get("startdate") or meta.get("start_date")
        if not start:
            continue
        try:
            sdate = dtp.parse(start).date()
        except Exception:
            continue

        age_mo = months_between(sdate, TODAY)
        if age_mo > 6:
            continue
        if age_mo < 5:
            continue

        pod_name = meta.get("name", pod_id)
        print(f"\nProcessing podling: {pod_name} (age {age_mo} months)")

        proj = ldapproj.get(pod_id, {})
        owners = proj.get("owners", [])
        members = proj.get("members", [])
        ppmc = len(owners)
        committers = len(members)

        # Mentors
        mentors_field = meta.get("mentors") or meta.get("mentorsNames") or []
        if isinstance(mentors_field, dict):
            mentors_count = len(mentors_field)
        elif isinstance(mentors_field, list):
            mentors_count = len([m for m in mentors_field if m])
        else:
            mentors_count = 0

        # Mailing lists signals
        dev_unique, dev_release_votes, dev_emails, _ = lists_activity_dev(
            infer_dev_list_domain(pod_id, meta), args.lists_activity, args.debug
        )
        gen_release_votes = lists_release_votes_general(
            pod_id, pod_name, args.lists_activity, args.debug
        )
        new_ppmc_count, new_committers_count = lists_growth_general(
            pod_id, pod_name, args.lists_activity, args.debug
        )

        # Reports & mentor sign-offs from board agendas
        reports_count = mentor_signoffs = 0
        if args.minutes_dir:
            try:
                reports_count, mentor_signoffs = count_reports_and_signoffs(pod_id, pod_name, args.minutes_dir, args.debug)
            except Exception as e:
                print(f"    ! agenda parse error for {pod_id}: {e}", file=sys.stderr)

        # GitHub repos
        repos: List[str] = []
        if pod_id.lower() in repo_map:
            repos = repo_map[pod_id.lower()]
            print(f"  - Using mapped repos: {', '.join(repos)}")
        elif args.auto_repos:
            print("  - Auto-discovering GitHub repos under apache/ ...")
            try:
                repos = discover_apache_repos(pod_id, meta, args.debug)
            except Exception as e:
                print(f"    ! auto-discovery error: {e}", file=sys.stderr)
            if repos:
                print(f"    · found: {', '.join(repos)}")
            else:
                print("    · none found (you can provide --repos to override)")
        else:
            print("  - Auto-discovery disabled and no explicit mapping provided.")

        per_pod_repos[pod_id] = repos[:]

        # GitHub metrics
        gh_contribs_set: Set[str] = set()
        gh_open_prs = gh_closed_prs = gh_open_issues = gh_closed_issues = 0
        if repos:
            for repo in repos:
                try:
                    gh_contribs_set |= gh_repo_contributors(repo)
                except Exception as e:
                    print(f"    ! contributors error for {repo}: {e}", file=sys.stderr)
                try:
                    o_i, c_i, o_p, c_p = gh_repo_issue_pr_breakdown(repo, args.debug)
                    gh_open_issues  += o_i
                    gh_closed_issues+= c_i
                    gh_open_prs     += o_p
                    gh_closed_prs   += c_p
                except Exception as e:
                    print(f"    ! issue/PR count error for {repo}: {e}", file=sys.stderr)
        else:
            print("  - No GitHub repos mapped for this podling.")

        # Assemble output row
        row = {
            "podling": pod_name,
            "id": pod_id,
            "start_date": sdate.isoformat(),
            "age_months": age_mo,
            "ppmc_count": ppmc,
            "committer_count": committers,

            # Mentor block
            "mentors_count": mentors_count,
            "reports_count": reports_count,
            "mentor_signoffs": mentor_signoffs,

            # Lists activity
            "unique_posters": dev_unique,
            "dev_emails": dev_emails,
            "dev_release_vote_threads": dev_release_votes,
            "general_release_vote_threads": gen_release_votes,
            "total_release_vote_threads": dev_release_votes + gen_release_votes,

            # GitHub
            "github_contributors": len(gh_contribs_set) if repos else "",
            "github_open_issues": gh_open_issues if repos else "",
            "github_closed_issues": gh_closed_issues if repos else "",
            "github_open_prs": gh_open_prs if repos else "",
            "github_closed_prs": gh_closed_prs if repos else "",
            "github_repos": ", ".join(repos) if repos else "",

            # Growth
            "new_ppmc": new_ppmc_count,
            "new_committers": new_committers_count,
        }
        rows.append(row)

    if not rows:
        print("\nNo podlings ≤ 6 months found.")
        return

    rows.sort(key=lambda r: (r["age_months"], r["start_date"], r["podling"]))

    print("\nWriting summary outputs...")
    fieldnames = list(rows[0].keys())
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    if args.md:
        md = tabulate([[r[k] for k in fieldnames] for r in rows],
                      headers=fieldnames, tablefmt="github")
        with open(args.md, "w", encoding="utf-8") as f:
            f.write(md + "\n")

    print(f"Wrote {len(rows)} podlings to {args.out}" + (f" and {args.md}" if args.md else ""))
    print("\nDone.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
