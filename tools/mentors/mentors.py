#!/usr/bin/env python3
"""
Generate a Markdown mentor roster from ASF Incubator podlings.xml.

Splits the roster into:
- Active mentors this year (last activity year == current year)
- Previous mentors (no current podlings; sorted by last year desc, then name)

Features:
- Current podlings listed first (and excluded from past list)
- Bold mentors with >= N current podlings (default 4; --highlight)
- Optional capacity view from historical max concurrent podlings (--show-capacity)
- Optional truncation of long lists (--max-list N)
- Optional hide of Previous mentors (--only-current)
- Collation by Apache ID to handle name variations

Notes:
- Source is podlings.xml only.
- Mentors can leave a project and be removed from podlings.xml so some mentor entries may be incorrect.
"""

import argparse
import sys
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from urllib.parse import urlparse
from collections import defaultdict
from datetime import datetime, date, UTC
import re
import unicodedata

DEFAULT_URL = "https://incubator.apache.org/podlings.xml"

START_KEYS = ["start", "startdate", "startDate", "sdate", "entered", "creationdate", "created"]
END_KEYS = [
    "end", "enddate", "endDate", "edate", "graduated", "retired",
    "resolutiondate", "resolutionDate", "attic", "exit", "graduation"
]
DATE_FORMATS = ["%Y-%m-%d", "%Y-%m", "%Y"]

NAME_BRACKETS = re.compile(r"\s*[<(\[].*?[>)\]]\s*")
MULTISPACE = re.compile(r"\s+")

def clean_name(name: str) -> str:
    s = NAME_BRACKETS.sub(" ", name or "")
    s = MULTISPACE.sub(" ", s).strip()
    return s

def norm_name_for_sort(s: str) -> str:
    if not s:
        return ""
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii").strip().lower()

def parse_date_str(s: str):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None

def get_first_date(elem: ET.Element, keys):
    for k in keys:
        d = parse_date_str(elem.get(k) or "")
        if d:
            return d
    return None

def get_last_date(elem: ET.Element, keys):
    for k in keys:
        d = parse_date_str(elem.get(k) or "")
        if d:
            return d
    return None

def load_xml(source: str) -> ET.Element:
    try:
        parsed = urlparse(source)
        if parsed.scheme in ("http", "https"):
            with urlopen(source) as resp:
                data = resp.read()
            root = ET.fromstring(data)
        else:
            root = ET.parse(source).getroot()
        return root
    except Exception as e:
        print(f"Error loading XML from {source}: {e}", file=sys.stderr)
        sys.exit(1)

def text_or_attr(elem: ET.Element, attr: str) -> str:
    txt = (elem.text or "").strip()
    if txt:
        return txt
    return (elem.get(attr) or "").strip()

def mentor_uid(elem: ET.Element) -> str:
    # Prefer Apache UID; used for de-duplication and (optionally) links
    for key in ("username", "id", "apacheId"):
        val = (elem.get(key) or "").strip()
        if val:
            return val
    return ""

def collect_mentor_stats(root: ET.Element, status_filter: set | None = None):
    """
    Returns mentor_info keyed by Apache UID when available (else cleaned name, lowercased):
        {
          "name": display_name,
          "uid": uid_or_empty,
          "podlings": set[str],
          "current_podlings": set[str],
          "first_date": date|None,
          "last_date": date|None,
          "intervals": list[(date,date)]
        }
    """
    mentor_info = {}

    def key_for(name: str, uid: str) -> str:
        return uid if uid else clean_name(name).lower()

    def ensure_entry(name: str, uid: str):
        k = key_for(name, uid)
        if k not in mentor_info:
            mentor_info[k] = {
                "name": clean_name(name) if name else (uid or "Unknown"),
                "uid": uid,
                "podlings": set(),
                "current_podlings": set(),
                "first_date": None,
                "last_date": None,
                "intervals": []
            }
        else:
            if name and mentor_info[k]["name"] != clean_name(name):
                mentor_info[k]["name"] = clean_name(name)
            if uid and not mentor_info[k]["uid"]:
                mentor_info[k]["uid"] = uid
        return k

    for pod in root.findall(".//podling"):
        # Only include projects sponsored by the Incubator
        sponsor_attr = (pod.get("sponsor") or "").strip().lower()
        if "incubator" not in sponsor_attr:
            continue

        status = (pod.get("status") or "").strip().lower()
        if status_filter and status not in status_filter:
            continue

        pod_name = (pod.get("name") or "").strip() or (pod.text or "").strip()
        if not pod_name:
            continue

        pod_start = get_first_date(pod, START_KEYS)
        pod_end = get_last_date(pod, END_KEYS)

        is_current = (status == "current")
        if is_current:
            pod_end = date.today()

        mentors_parent = pod.find("./mentors")
        mentor_elems = mentors_parent.findall("./mentor") if mentors_parent is not None else pod.findall("./mentor")

        for m in mentor_elems:
            raw_name = text_or_attr(m, "name")
            uid = mentor_uid(m)
            display_name = raw_name or uid
            if not display_name and not uid:
                continue

            k = ensure_entry(display_name, uid)
            info = mentor_info[k]

            info["podlings"].add(pod_name)
            if is_current:
                info["current_podlings"].add(pod_name)

            if pod_start and (info["first_date"] is None or pod_start < info["first_date"]):
                info["first_date"] = pod_start
            if pod_end and (info["last_date"] is None or pod_end > info["last_date"]):
                info["last_date"] = pod_end
            if info["last_date"] is None and pod_start:
                info["last_date"] = pod_start
            if pod_start and pod_end:
                info["intervals"].append((pod_start, pod_end))

    return mentor_info

def whole_years(a, b):
    if not a or not b:
        return None
    years = b.year - a.year
    if (b.month, b.day) < (a.month, a.day):
        years -= 1
    return max(0, years)

def maybe_truncate(names, max_list):
    if max_list is None or max_list <= 0:
        return ", ".join(names) if names else "None"
    if len(names) <= max_list:
        return ", ".join(names) if names else "None"
    shown = ", ".join(names[:max_list])
    return f"{shown} (+{len(names) - max_list} more)"

def mentor_label_plain(info: dict, bold: bool) -> str:
    label = info["name"] or info["uid"] or "Unknown"
    return f"**{label}**" if bold else label

def max_concurrent(intervals):
    """Compute peak overlap of [start, end] date intervals (inclusive)."""
    if not intervals:
        return 0
    events = []
    for s, e in intervals:
        if not s or not e:
            continue
        events.append((s.toordinal(), +1))
        events.append((e.toordinal() + 1, -1))  # inclusive end
    if not events:
        return 0
    events.sort()
    cur = peak = 0
    for _, d in events:
        cur += d
        if cur > peak:
            peak = cur
    return peak

def capacity_badge(current_cnt: int, max_hist: int) -> str:
    """Return short, neutral capacity labels with emoji."""
    if max_hist <= 0:
        return "NA"
    # OK if comfortably below historical peak
    if current_cnt < max_hist * 0.8:
        return "🟢 OK"
    # High when approaching historical peak
    if current_cnt < max_hist:
        return "🟡 High"
    # Full when at historical peak
    if current_cnt == max_hist:
        return "🟠 Full"
    # Above past max (rare)
    return "🔴 Above"

def table_rows_active(mentor_info, highlight_threshold: int, max_list: int | None, show_capacity: bool):
    # Sort by total podlings (current + past) desc, then current count desc, then name
    items = list(mentor_info.items())

    def sort_key(kv):
        k, v = kv
        total = len(v["podlings"])
        current = len(v["current_podlings"])
        return (-total, -current, norm_name_for_sort(v["name"]), v["uid"] or k)

    items.sort(key=sort_key)

    rows = []
    for k, info in items:
        pods_current = sorted(info["current_podlings"], key=str.lower)
        pods_past = sorted(info["podlings"] - info["current_podlings"], key=str.lower)
        yrs = whole_years(info["first_date"], info["last_date"])
        yrs_str = f"{yrs}" if yrs is not None else "NA"
        # bold = len(pods_current) >= highlight_threshold if highlight_threshold else False
        label = mentor_label_plain(info, False)
        podlist_current = maybe_truncate(pods_current, max_list)
        podlist_past = maybe_truncate(pods_past, max_list)

        if show_capacity:
            max_hist = info.get("max_concurrent", 0)
            cap = capacity_badge(len(pods_current), max_hist)
            rows.append(
                f"| {label} | {podlist_current} | {len(pods_current)} | {podlist_past} | {len(pods_past)} | {yrs_str} | {max_hist} | {cap} |"
            )
        else:
            rows.append(
                f"| {label} | {podlist_current} | {len(pods_current)} | {podlist_past} | {len(pods_past)} | {yrs_str} |"
            )
    return rows

def table_rows_previous(mentor_info, max_list: int | None):
    # Sort by last activity year desc, then normalized name asc
    sorted_items = sorted(
        mentor_info.items(),
        key=lambda kv: (
            kv[1]["last_date"].year if kv[1]["last_date"] else 0,
            norm_name_for_sort(kv[1]["name"])
        ),
        reverse=True
    )
    rows = []
    for _, info in sorted_items:
        pods_past = sorted(info["podlings"], key=str.lower)
        yrs = whole_years(info["first_date"], info["last_date"])
        yrs_str = f"{yrs}" if yrs is not None else "NA"
        last_year_str = f"{info['last_date'].year}" if info["last_date"] else "NA"
        label = mentor_label_plain(info, False)
        podlist_past = maybe_truncate(pods_past, max_list)
        rows.append(
            f"| {label} | {podlist_past} | {len(pods_past)} | {yrs_str} | {last_year_str} |"
        )
    return rows

def render_markdown(mentor_info: dict, total_podlings: int, highlight_threshold: int, max_list: int | None, only_current: bool, show_capacity: bool) -> str:
    now = datetime.now(UTC)
    generated = now.strftime("%Y-%m-%d")
    current_year = now.year

    total_mentors = len(mentor_info)
    current_mentors = sum(1 for v in mentor_info.values() if len(v["current_podlings"]) > 0)

    active_this_year = {k: v for k, v in mentor_info.items() if v["last_date"] and v["last_date"].year == current_year}
    previous_mentors = {k: v for k, v in mentor_info.items() if k not in active_this_year}

    # If showing capacity, precompute per-mentor historical peak concurrency
    if show_capacity:
        for v in active_this_year.values():
            v["max_concurrent"] = max_concurrent(v.get("intervals", []))

    total_podlings = len({p for v in mentor_info.values() for p in v["podlings"]})

    lines = []
    lines.append("# ASF Incubator Mentor Roster")
    lines.append("")
    lines.append(f"_Generated on: {generated}_")
    lines.append("")
    # Short, neutral disclaimer sits high to survive copy/paste/screenshots
    lines.append("**Generated from public `podlings.xml`. Figures are historical, may be incomplete, and are not an evaluation of any individual.**")
    lines.append("")
    lines.append(f"- Total podlings: {total_podlings}")
    lines.append(f"- Total mentors: {total_mentors}")
    lines.append(f"- Total mentors for current podlings: {current_mentors}")
    lines.append(f"- Active mentors this year: {len(active_this_year)}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Source is podlings.xml only.")
    lines.append("- Years active is based on podlings start and end dates and may be inaccurate.")
    lines.append("- Mentors can leave a project and be removed from podlings.xml so some mentor entries may be missing podlings they mentored.")
    if show_capacity:
        lines.append("- Capacity = historical workload estimate (OK / High / Full) is based on past mentoring counts only and may not reflect current availability.")
    lines.append("- Corrections welcome")
    lines.append("")

    # Active mentors table
    lines.append("## Mentors with entries in the past year")
    lines.append("")
    if show_capacity:
        lines.append("| Mentor | Current podlings | Current count | Past podlings | Past count | Years mentoring | Max concurrent | Capacity |")
        lines.append("|---|---|---:|---|---:|---:|---:|---|")
    else:
        lines.append("| Mentor | Current podlings | Current count | Past podlings | Past count | Years mentoring |")
        lines.append("|---|---|---:|---|---:|---:|")
    lines.extend(table_rows_active(active_this_year, highlight_threshold, max_list, show_capacity))
    lines.append("")

    # Previous mentors table
    if not only_current:
        lines.append("## Previous mentors")
        lines.append("")
        lines.append("| Mentor | Past podlings | Past count | Years mentoring | Last seen |")
        lines.append("|---|---|---:|---:|---:|")
        lines.extend(table_rows_previous(previous_mentors, max_list))
        lines.append("")

    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Create a Markdown mentor roster from podlings.xml (sponsor='Incubator').")
    parser.add_argument("--source", default=DEFAULT_URL, help="URL or path to podlings.xml")
    parser.add_argument("--status", choices=["current", "graduated", "retired", "all"], default="all",
                        help="Filter by podling status")
    parser.add_argument("--highlight", type=int, default=4,
                        help="Bold mentors in the Active table with at least this many current podlings (default 4)")
    parser.add_argument("--max-list", type=int, default=0,
                        help="Maximum items to show in podling lists before truncating (0 = no limit)")
    parser.add_argument("--only-current", action="store_true",
                        help="Show only the Active mentors section (hide Previous mentors)")
    parser.add_argument("--show-capacity", action="store_true",
                        help="Show historical max concurrent and capacity badge in the Active table")
    parser.add_argument("--output", help="Write Markdown to this file instead of stdout")
    args = parser.parse_args()

    status_filter = None
    if args.status != "all":
        status_filter = {args.status}

    root = load_xml(args.source)
    podlings = {p.get("name") for p in root.findall(".//podling") if (p.get("sponsor") or "").lower().find("incubator") != -1}
    total_podlings = len(podlings)
    mentor_info = collect_mentor_stats(root, status_filter=status_filter)
    md = render_markdown(
        mentor_info,
        total_podlings,
        highlight_threshold=args.highlight,
        max_list=args.max_list if args.max_list > 0 else None,
        only_current=args.only_current,
        show_capacity=args.show_capacity
    )

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(md)
        except Exception as e:
            print(f"Error writing to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(md, end="")

if __name__ == "__main__":
    main()
