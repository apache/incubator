#!/usr/bin/env python3
# podling_6mo_values.py
# Generate <=6mo podling metrics (CSV/MD).

import argparse, csv, os, sys, re, glob, email, json
from email.parser import BytesParser
from email.policy import default as EMAIL_DEFAULT
from datetime import datetime, timezone, timedelta, date
from dateutil import parser as dtp
from typing import Dict, Any, Optional, Tuple, List, Set
from urllib.parse import urlparse, parse_qs
import xml.etree.ElementTree as ET

import requests
from tabulate import tabulate

# ---------------- Constants ----------------

INCUBATOR_ROOT = "https://incubator.apache.org"
URL_PODLINGS_XML = f"{INCUBATOR_ROOT}/podlings.xml"

W_PUBLIC = "https://whimsy.apache.org/public"
URL_LDAP_PROJECTS = f"{W_PUBLIC}/public_ldap_projects.json"

TODAY = datetime.now(timezone.utc).date()

LAA_MBOX = "https://lists.apache.org/api/mbox.lua"

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
EXCLUDE_SUFFIXES = ("-site","-website","-site-pub","-asf-site","-asf-site-src",
                    "-images","-logos","-branding","-docs","-documentation","-examples")

RELEASE_VOTE_SUBJECT = re.compile(r"\[(?:VOTE)\].*\b(RELEASE|INCUBATING)\b", re.I)
SUBJ_PREFIX_RE = re.compile(r'^\s*(re|fwd|fw)\s*:\s*', re.I)
PPMC_VOTE_SUBJECT = re.compile(r"\[(?:VOTE|RESULT)\].*(PPMC|PMC).*(member|add|appoint)", re.I)
COMMITTER_VOTE_SUBJECT = re.compile(r"\[(?:VOTE|RESULT)\].*committer", re.I)

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

def parse_iso_dt(s: Optional[str]) -> Optional[datetime]:
    if not s:
        return None
    try:
        return dtp.parse(s)
    except Exception:
        return None

# ---------------- podlings.xml parsing ----------------

def load_podlings_xml(url: str = URL_PODLINGS_XML) -> Dict[str, Dict[str, Any]]:
    xml_text = http_text(url)
    root = ET.fromstring(xml_text)
    podlings: Dict[str, Dict[str, Any]] = {}
    for p in root.findall("podling"):
        resource = (p.get("resource") or "").strip()
        name = (p.get("name") or resource or "").strip()
        status = (p.get("status") or "").strip()
        startdate = (p.get("startdate") or p.get("start_date") or "").strip()
        enddate = (p.get("enddate") or "").strip()

        mentors: List[Dict[str, str]] = []
        for m in p.findall("./mentors/mentor"):
            mentors.append({
                "name": (m.text or "").strip() or (m.get("name") or "").strip(),
                "username": (m.get("username") or m.get("availid") or "").strip(),
                "role": (m.get("role") or "").strip(),
            })

        # aliases
        aliases: List[str] = []
        for ra in p.findall("resourceAlias"):
            val = (ra.get("name") or (ra.text or "")).strip()
            if val:
                aliases.append(val)

        if not resource:
            continue
        podlings[resource] = {
            "id": resource,
            "name": name,
            "status": status,
            "startdate": startdate,
            "enddate": enddate,
            "mentors": mentors,
            "aliases": aliases,
        }
    return podlings

# ---------------- Public lists (ancillary signals) ----------------

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
            # TODO: this does not handle header wrapping
            for line in headers.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    msg[k.strip()] = v.strip()
            yield msg

def infer_dev_list_domain(pod_id: str) -> str:
    return f"{pod_id}.apache.org"

def lists_activity_dev(dev_domain: str, days: int, debug: bool=False) -> Tuple[int, int, int, List[str]]:
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

HDR_RE = re.compile(r'(?m)^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$')
SIGNED_OFF_RE = re.compile(r'(?mi)^\s*###\s+Signed-off-by:\s*$')   # exact label; case-insensitive
NEXT_H3_RE = re.compile(r'(?m)^\s*###\s+')
CHECKED_BULLET_RE = re.compile(r'(?m)^\s*-\s*\[\s*[xX]\s*\]')      # "- [X]" lines only

AGENDA_DATE_RE = re.compile(r'^board_agenda_(\d{4})_(\d{2})_(\d{2})\.txt$')

def _agenda_file_date(path: str) -> Optional[date]:
    m = AGENDA_DATE_RE.match(os.path.basename(path))
    if not m:
        return None
    try:
        y, mth, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return date(y, mth, d)
    except Exception:
        return None

def _section_end_for_level(text: str, start: int, level: int) -> int:
    for m in HDR_RE.finditer(text, start):
        next_level = len(m.group('hashes'))
        if next_level <= level:
            return m.start()
    return len(text)

def _match_pod_title(title: str, pod_id: str, pod_name: str) -> bool:
    t = title.strip().lower()
    pid = re.escape(pod_id.strip().lower())
    pname = re.escape(pod_name.strip().lower())
    return bool(re.search(rf'\b({pid}|{pname})\b', t))

def count_reports_and_signoffs(pod_id: str, pod_name: str, minutes_dir: str,
                               window_days: int = 180, debug: bool=False) -> Tuple[int, int]:
    if not minutes_dir:
        return 0, 0
    reports = 0
    total_signoffs = 0

    for path in sorted(glob.glob(os.path.join(minutes_dir, "board_agenda_*.txt"))):
        fdt = _agenda_file_date(path)
        if fdt and (TODAY - fdt) > timedelta(days=window_days):
            continue

        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                txt = f.read()
        except Exception as e:
            if debug:
                print(f"! error reading {path}: {e}", file=sys.stderr)
            continue

        # Find the podling header (any level), then slice its section.
        pod_hdr = None
        for m in HDR_RE.finditer(txt):
            if _match_pod_title(m.group('title'), pod_id, pod_name):
                pod_hdr = m
                break

        if not pod_hdr:
            if debug:
                print(f"{os.path.basename(path)}: podling header: NO")
            continue

        reports += 1

        level = len(pod_hdr.group('hashes'))
        sec_start = pod_hdr.end()
        sec_end = _section_end_for_level(txt, sec_start, level)
        pod_section = txt[sec_start:sec_end]

        local_signoffs = 0
        for sm in SIGNED_OFF_RE.finditer(pod_section):
            block = pod_section[sm.end():]
            m_next = NEXT_H3_RE.search(block)
            if m_next:
                block = block[:m_next.start()]
            local_signoffs += len(CHECKED_BULLET_RE.findall(block))

            if debug:
                hdr_end = pod_section.find("\n", sm.start())
                hdr_line = pod_section[sm.start(): hdr_end if hdr_end != -1 else len(pod_section)]
                print(f"  Found header: {hdr_line.rstrip()}")
                for ln in block.splitlines():
                    if CHECKED_BULLET_RE.search(ln):
                        print(f"    COUNTED: {ln.rstrip()}")

        if debug:
            print(f"{os.path.basename(path)}: report=1, signoffs+={local_signoffs}")

        total_signoffs += local_signoffs

    return reports, total_signoffs

def audit_minutes_for_pod(pod_id: str, pod_name: str, minutes_dir: str,
                          window_days: int = 180) -> None:
    if not minutes_dir:
        print("No minutes_dir provided.")
        return

    for path in sorted(glob.glob(os.path.join(minutes_dir, "board_agenda_*.txt"))):
        fdt = _agenda_file_date(path)
        if fdt and (TODAY - fdt) > timedelta(days=window_days):
            continue

        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                txt = f.read()
        except Exception as e:
            print(f"{os.path.basename(path)}: ! read error: {e}")
            continue

        pod_hdr = None
        for m in HDR_RE.finditer(txt):
            if _match_pod_title(m.group('title'), pod_id, pod_name):
                pod_hdr = m
                break

        if not pod_hdr:
            print(f"{os.path.basename(path)}: podling header: NO")
            continue

        level = len(pod_hdr.group('hashes'))
        sec_start = pod_hdr.end()
        sec_end = _section_end_for_level(txt, sec_start, level)
        pod_section = txt[sec_start:sec_end]
        print(f"{os.path.basename(path)}: podling subsection: YES (bytes {sec_start}-{sec_end})")

        total_block = 0
        for sm in SIGNED_OFF_RE.finditer(pod_section):
            block = pod_section[sm.end():]
            m_next = NEXT_H3_RE.search(block)
            if m_next:
                block = block[:m_next.start()]
            lines = [ln.rstrip() for ln in block.splitlines() if CHECKED_BULLET_RE.search(ln)]
            total_block += len(lines)
            print("  Signed-off-by block:")
            for ln in lines:
                print(f"    COUNTED: {ln}")
        print(f"  => mentor_signoffs in file: {total_block}")

# ---------------- GitHub helpers (unchanged; optional) ----------------

def gh_repo_exists_full(full: str) -> bool:
    try:
        http_json(f"{GITHUB_API}/repos/{full}")
        return True
    except Exception:
        return False

def gh_repo_info(owner_repo: str) -> Dict[str, Any]:
    return http_json(f"{GITHUB_API}/repos/{owner_repo}")

def gh_count_via_link_header(url: str, params: Dict[str, Any]) -> int:
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
    try:
        open_prs = gh_count_via_link_header(f"{GITHUB_API}/repos/{owner_repo}/pulls", {"state": "open"})
    except Exception:
        open_prs = 0
    try:
        closed_prs = gh_count_via_link_header(f"{GITHUB_API}/repos/{owner_repo}/pulls", {"state": "closed"})
    except Exception:
        closed_prs = 0
    open_issues = closed_issues = 0
    try:
        info = gh_repo_info(owner_repo)
        if info.get("has_issues", True):
            open_issues   = gh_search_count_safe(f"repo:{owner_repo} is:issue is:open")
            closed_issues = gh_search_count_safe(f"repo:{owner_repo} is:issue is:closed")
    except Exception:
        pass
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

def name_candidates_from_xml(meta: Dict[str, Any]) -> List[str]:
    cands = {norm(meta.get("id") or ""), norm(meta.get("name") or "")}
    for a in meta.get("aliases", []) or []:
        if a:
            cands.add(norm(a))
    cands.discard("")
    return sorted({re.sub(r"^apache-", "", x) for x in cands})

def discover_apache_repos_from_xml(meta: Dict[str, Any], debug: bool=False) -> List[str]:
    cands = name_candidates_from_xml(meta)
    found: List[str] = []
    checked: Set[str] = set()
    for base in cands:
        for pat in (base, f"incubator-{base}"):
            full = f"apache/{pat}"
            if full in checked:
                continue
            checked.add(full)
            try:
                http_json(f"{GITHUB_API}/repos/{full}")
                found.append(full)
            except Exception:
                pass
    return sorted(set(found))

# ---------------- Main ----------------

def main():
    parser = argparse.ArgumentParser(description="Generate 6mo podling metrics CSV/MD.")
    parser.add_argument("--out", default="podlings_under6mo.csv", help="CSV output path")
    parser.add_argument("--md", default="podlings_under6mo.md", help="Markdown table output path")
    parser.add_argument("--lists-activity", type=int, default=180, help="Days window for lists/GitHub activity [default: 180]")
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

    if not args.minutes_dir:
        print("NOTE: --minutes-dir not provided → report/sign-off columns will be 0.", file=sys.stderr)
    else:
        print(f"Using minutes_dir: {args.minutes_dir}")

    print("Fetching podlings from podlings.xml...")
    podlings_xml = load_podlings_xml(URL_PODLINGS_XML)

    print("Fetching LDAP project membership (owners/members) from Whimsy...")
    ldapproj = http_json(URL_LDAP_PROJECTS).get("projects", {})

    # If auditing, run once and exit
    if args.audit_pod:
        lower = args.audit_pod.lower()
        pid = None; pname = None
        for rid, meta in podlings_xml.items():
            if rid.lower() == lower or meta.get("name","").lower() == lower:
                pid = rid; pname = meta.get("name", rid); break
        if not pid:
            pid = args.audit_pod; pname = args.audit_pod
        print(f"Auditing pod: id='{pid}' name='{pname}' in {args.minutes_dir or '(no minutes_dir)'}")
        audit_minutes_for_pod(pid, pname, args.minutes_dir, args.lists_activity)
        return

    rows: List[Dict[str, Any]] = []

    since_dt = datetime.now(timezone.utc) - timedelta(days=args.lists_activity)
    until_dt = datetime.now(timezone.utc)

    for rid, meta in podlings_xml.items():
        if (meta.get("status") or "").lower() != "current":
            continue
        start = meta.get("startdate") or meta.get("start_date")
        if not start:
            continue
        try:
            sdate = dtp.parse(start).date()
        except Exception:
            continue
        age_mo = months_between(sdate, TODAY)
        if age_mo != 6:
            continue

        pod_id = rid
        pod_name = meta.get("name", pod_id)
        print(f"\nProcessing podling: {pod_name} (age {age_mo} months)")

        proj = ldapproj.get(pod_id, {})
        owners = proj.get("owners", []) or []
        members = proj.get("members", []) or []
        ppmc = len(owners)
        committers = len(members)

        mentors_count = len({
            (m.get("username") or "").strip().lower() or (m.get("name") or "").strip().lower()
            for m in (meta.get("mentors") or [])
            if (m.get("name") or m.get("username"))
        })

        dev_domain = infer_dev_list_domain(pod_id)
        dev_unique, dev_release_votes, dev_emails, _ = lists_activity_dev(dev_domain, args.lists_activity, args.debug)
        gen_release_votes = lists_release_votes_general(pod_id, pod_name, args.lists_activity, args.debug)
        new_ppmc_vote_threads, new_committer_vote_threads = lists_growth_general(pod_id, pod_name, args.lists_activity, args.debug)

        reports_count = mentor_signoffs = 0
        if args.minutes_dir:
            try:
                reports_count, mentor_signoffs = count_reports_and_signoffs(
                    pod_id, pod_name, args.minutes_dir, args.lists_activity, args.debug
                )
            except Exception as e:
                print(f"    ! agenda parse error for {pod_id}: {e}", file=sys.stderr)

        if args.debug:
            print(f"  SUMMARY for {pod_name}: mentors={mentors_count}, reports={reports_count}, signoffs={mentor_signoffs}")

        repos: List[str] = []
        if args.auto_repos:
            try:
                repos = discover_apache_repos_from_xml(meta, args.debug)
            except Exception:
                repos = []

        gh_contribs_set: Set[str] = set()
        gh_open_prs = gh_closed_prs = gh_open_issues = gh_closed_issues = 0
        if repos:
            for repo in repos:
                try:
                    # very lightweight; safe to skip on errors
                    data = http_json(f"{GITHUB_API}/repos/{repo}/contributors", params={"anon": "1", "per_page": 100})
                    for p in (data or []):
                        if p.get("login"):
                            gh_contribs_set.add(p["login"].lower())
                except Exception:
                    pass
                try:
                    o_i = gh_search_count_safe(f"repo:{repo} is:issue is:open")
                    c_i = gh_search_count_safe(f"repo:{repo} is:issue is:closed")
                    o_p = gh_count_via_link_header(f"{GITHUB_API}/repos/{repo}/pulls", {"state": "open"})
                    c_p = gh_count_via_link_header(f"{GITHUB_API}/repos/{repo}/pulls", {"state": "closed"})
                    gh_open_issues  += o_i
                    gh_closed_issues+= c_i
                    gh_open_prs     += o_p
                    gh_closed_prs   += c_p
                except Exception:
                    pass

        pr_merged_count = 0
        if repos:
            merged_since = since_dt.strftime("%Y-%m-%d")
            merged_until = until_dt.strftime("%Y-%m-%d")
            for repo in repos:
                q = f'repo:{repo} is:pr is:merged merged:{merged_since}..{merged_until}'
                try:
                    page = 1
                    while True:
                        data = http_json(f"{GITHUB_API}/search/issues", params={"q": q, "per_page": 100, "page": page})
                        items = (data or {}).get("items", [])
                        if not items:
                            break
                        pr_merged_count += len(items)
                        if len(items) < 100:
                            break
                        page += 1
                except Exception:
                    pass

        # Assemble output row
        row = {
            "podling": pod_name,
            "id": pod_id,
            "start_date": sdate.isoformat(),
            "age_months": age_mo,
            "ppmc_count": ppmc,
            "committer_count": committers,

            "mentors_count": mentors_count,
            "reports_count": reports_count,
            "mentor_signoffs": mentor_signoffs,

            "unique_posters": dev_unique,
            "dev_emails": dev_emails,
            "dev_release_vote_threads": dev_release_votes,
            "general_release_vote_threads": gen_release_votes,
            "total_release_vote_threads": dev_release_votes + gen_release_votes,

            "github_contributors": len(gh_contribs_set) if repos else "",
            "github_open_issues": gh_open_issues if repos else "",
            "github_closed_issues": gh_closed_issues if repos else "",
            "github_open_prs": gh_open_prs if repos else "",
            "github_closed_prs": gh_closed_prs if repos else "",
            "github_repos": ", ".join(repos) if repos else "",

            "new_ppmc_vote_threads": new_ppmc_vote_threads,
            "new_committer_vote_threads": new_committer_vote_threads,

            "pr_merged_count": pr_merged_count if repos else "",
            "merger_diversity": "",
            "reviewer_diversity": "",
        }
        rows.append(row)

    if not rows:
        print("\nNo podlings 6 months old found.")
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
