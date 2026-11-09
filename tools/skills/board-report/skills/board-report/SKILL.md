---
name: board-report
description: Draft the quarterly Apache Incubator board report for the VP Incubator. Use this skill when the user asks to draft, write, or produce the quarterly board report, the Incubator report for the ASF board, or the VP Incubator report. The report covers the Apache Incubator ONLY — not any education or learning programme. There are no enrolment or learner metrics. Triggers on phrases like "draft board report", "quarterly incubator report", "board report for this quarter", "VP Incubator report", or "write the incubator report".
allowed-tools:
  - Bash
  - Read
  - Write
---

# Quarterly Board Report Drafter

Produce the VP Incubator's quarterly report to the ASF board. The report covers
the **Apache Incubator** — the programme through which new projects enter the
ASF as podlings. It has four sections:

1. **Podling Statistics** — aggregate counts of current, graduated, and retired
   podlings, plus new podlings started and completions this quarter.
2. **Graduations and Retirements** — individual podlings that graduated or
   retired during the current quarter, with brief descriptions.
3. **Reporting Cohort Summary** — the cohort of podlings that reported to the
   board this quarter, pulled from the most recent cached Incubator board report.
4. **Items Requiring Board Attention** — podlings flagged by the IPMC watchlist
   as needing intervention, with severity and recommended action.

Run this skill when the VP Incubator (or a delegate) needs to draft the report
ahead of the next ASF board meeting.

---

## Server locations

Use these absolute paths. The harness invokes server functions directly via
Python imports — never call MCP tool endpoints over stdio.

| Role | Path |
|------|------|
| Podling roster and lifecycle data | `~/PodlingsMCP` |
| IPMC oversight and watchlist | `~/IncubatorMCP` |
| Incubator board report cache | `~/ReportMCP` |

Health report Markdown files (input to IncubatorMCP):
`~/incubator/tools/health/reports`

Report cache directory:
`~/ReportMCP/.cache/incubator-reports`

Set the Python path at the start of every Bash session:

```bash
export PYTHONPATH=~/PodlingsMCP:\
~/IncubatorMCP:\
~/ReportMCP/src
```

---

## Step 1 — Determine the current quarter

Calculate the current quarter from today's date. This governs which podlings
count as graduating or retiring "this quarter".

```python
import sys, json
from datetime import date

today = date.today()
year  = today.year
month = today.month
q     = (month - 1) // 3 + 1          # 1..4

quarter_start = date(year, (q - 1) * 3 + 1, 1)
quarter_end_month = q * 3
quarter_end = date(
    year if quarter_end_month <= 12 else year + 1,
    quarter_end_month if quarter_end_month <= 12 else quarter_end_month - 12,
    1,
)

CURRENT_QUARTER = f"Q{q} {year}"
QUARTER_START   = str(quarter_start)   # YYYY-MM-DD
QUARTER_END     = str(quarter_end)     # YYYY-MM-DD (exclusive — first day of next quarter)

print(f"Quarter: {CURRENT_QUARTER}  ({QUARTER_START} to {QUARTER_END}, exclusive)")
```

---

## Step 2 — Podling statistics (`podling_stats`)

Call `tool_podling_stats` to retrieve all-time aggregate counts, then call
`started_podlings_by_year` and `completed_podlings_in_range` to get the
year-to-date activity for the current calendar year.

```python
sys.path.insert(0, '~/PodlingsMCP')
from podlings.tools import (
    tool_podling_stats,
    tool_started_podlings_by_year,
    tool_completed_podlings_in_range,
)

# All-time aggregate counts
stats = tool_podling_stats({})

current_count   = stats["status_counts"].get("current",   0)
graduated_count = stats["status_counts"].get("graduated", 0)
retired_count   = stats["status_counts"].get("retired",   0)
total_ever      = stats["total_podlings"]

print(f"All-time: {total_ever} total  "
      f"({current_count} current, {graduated_count} graduated, {retired_count} retired)")

# Year-to-date started in current year
started_ytd = tool_started_podlings_by_year({"year": today.year})
started_names = started_ytd["started"]

# Year-to-date completed in current year
completed_ytd = tool_completed_podlings_in_range({
    "start_year": today.year,
    "end_year":   today.year,
})
graduated_ytd = completed_ytd["graduated"]
retired_ytd   = completed_ytd["retired"]

print(f"YTD {today.year}: started={started_ytd['started_count']}, "
      f"graduated={len(graduated_ytd)}, retired={len(retired_ytd)}")
```

---

## Step 3 — Graduations and retirements this quarter

Retrieve individual podling records for every podling that completed in the
current calendar year and filter down to those whose `enddate` falls within the
current quarter.

```python
from podlings.tools import tool_get_podling

def in_current_quarter(enddate_str: str | None) -> bool:
    """Return True if enddate falls within [quarter_start, quarter_end)."""
    if not enddate_str:
        return False
    try:
        d = date.fromisoformat(enddate_str)
    except ValueError:
        return False
    return quarter_start <= d < quarter_end

all_completed_ytd = graduated_ytd + retired_ytd
quarter_graduations = []
quarter_retirements = []

for name in all_completed_ytd:
    record = tool_get_podling({"name": name})
    podling = record.get("podling", {})
    enddate = podling.get("enddate")
    status  = (podling.get("status") or "").lower()
    if in_current_quarter(enddate):
        entry = {
            "name":        podling.get("name", name),
            "status":      status,
            "startdate":   podling.get("startdate"),
            "enddate":     enddate,
            "description": podling.get("description", ""),
        }
        if status == "graduated":
            quarter_graduations.append(entry)
        elif status == "retired":
            quarter_retirements.append(entry)

print(f"{CURRENT_QUARTER} graduations: {[p['name'] for p in quarter_graduations]}")
print(f"{CURRENT_QUARTER} retirements: {[p['name'] for p in quarter_retirements]}")
```

---

## Step 4 — Reporting cohort summary (`incubator-reports`)

The incubator-reports server has no tool literally named `cohort-summary`.
The cohort summary is obtained in two calls:

1. `incubator_reports_overview` — lists all cached report IDs. Pick the most
   recent one (last entry in `report_ids`).
2. `get_report_summary` — returns the parsed podling list for that report.

```python
sys.path.insert(0, '~/ReportMCP/src')
from apache_incubator_reports_mcp.tools import (
    incubator_reports_overview,
    get_report_summary,
)

REPORT_CACHE = '~/ReportMCP/.cache/incubator-reports'

overview = incubator_reports_overview(cache_dir=REPORT_CACHE)

# Most recent cached report
latest_report_id = overview["report_ids"][-1]    # e.g. "board-minutes-2026-06-17"
latest_period    = overview["report_periods"][-1] # e.g. "2026-06"

cohort = get_report_summary(latest_report_id, cache_dir=REPORT_CACHE)

cohort_podlings = cohort["podlings"]    # list of per-podling dicts
cohort_count    = cohort["podling_count"]
cohort_title    = cohort.get("title", latest_report_id)

print(f"Cohort report: {cohort_title}  ({cohort_count} podlings in reporting cohort)")
```

Key fields in each `cohort_podlings` entry:

| Field | Meaning |
|-------|---------|
| `podling` | Podling name |
| `incubating_since` | Entry date into the Incubator |
| `issue_count` | Number of open issues noted in the report |
| `last_release` | Date string of the podling's last Apache release |
| `observed_mentor_signoff_count` | Number of mentor sign-offs observed |
| `signed_off_by` | List of mentor names who signed off |

Do **not** compute sign-off fractions or apply red/orange/green traffic-light
colouring to `observed_mentor_signoff_count`. Full mentor sign-off is not
required; these are informational counts only.

---

## Step 5 — Items requiring board attention (`ipmc_watchlist`)

Call `tool_ipmc_watchlist` from the IPMC server. The default `limit` is 10
and returns podlings ordered from highest to lowest severity.

```python
sys.path.insert(0, '~/IncubatorMCP')
from ipmc.tools import tool_ipmc_watchlist

HEALTH_SOURCE = '~/incubator/tools/health/reports'

watchlist = tool_ipmc_watchlist({
    "health_source": HEALTH_SOURCE,
    "limit":         20,              # increase to capture medium-severity items
})

watchlist_items = watchlist.get("items", [])

# For the board report, include only medium-severity and above
board_items = [
    item for item in watchlist_items
    if item["severity"] in ("high", "critical", "medium")
]

print(f"Watchlist: {len(watchlist_items)} total, "
      f"{len(board_items)} at medium+ severity for board attention")
for item in board_items:
    print(f"  {item['podling']:20s}  {item['severity']:8s}  {item.get('watch_reasons')}")
```

Key fields in each watchlist item:

| Field | Meaning |
|-------|---------|
| `podling` | Podling name |
| `severity` | `critical`, `high`, `medium`, or `low` |
| `trend` | `improving`, `stable`, `declining`, or `unknown` |
| `watch_reasons` | List of reason codes (e.g. `missing_reports`, `low_community_activity`) |
| `summary` | One-sentence description of the primary concern |
| `recommended_ipmc_action` | What the IPMC should do |
| `confidence` | Evidence confidence: `high`, `medium`, or `low` |

---

## Step 6 — Assemble the board report

Combine the data from Steps 1–5 into the standard board report format.
Write the finished report to `scratch/board-report-draft.txt` (create
`scratch/` first if it does not exist).

```python
import os
os.makedirs("scratch", exist_ok=True)

def _podling_list(entries: list[dict], bullet: str = "  - ") -> str:
    if not entries:
        return f"{bullet}(none this quarter)"
    lines = []
    for p in entries:
        desc = (p.get("description") or "").strip()
        desc_snippet = (desc[:120] + "…") if len(desc) > 120 else desc
        lines.append(f"{bullet}{p['name']} (ended {p.get('enddate', '?')})")
        if desc_snippet:
            lines.append(f"    {desc_snippet}")
    return "\n".join(lines)

def _cohort_table(podlings: list[dict]) -> str:
    if not podlings:
        return "  (no cohort data available)"
    lines = [f"  {'Podling':<22} {'Since':<12} {'Last release':<25} Sign-offs"]
    lines.append("  " + "-" * 72)
    for p in podlings:
        release = (p.get("last_release") or "—")
        if release.startswith("###") or release.startswith("n/a") or release == "XXXX-XX-XX":
            release = "—"
        lines.append(
            f"  {p['podling']:<22} "
            f"{p.get('incubating_since', '?'):<12} "
            f"{release:<25} "
            f"{p.get('observed_mentor_signoff_count', 0)}"
        )
    return "\n".join(lines)

def _watchlist_section(items: list[dict]) -> str:
    if not items:
        return "  No podlings currently require specific board attention."
    lines = []
    for item in items:
        reasons = ", ".join(item.get("watch_reasons") or []) or "see summary"
        lines.append(
            f"  {item['podling']} [{item['severity'].upper()}]\n"
            f"    Reason: {reasons}\n"
            f"    Summary: {item.get('summary', '')}\n"
            f"    Recommended action: {item.get('recommended_ipmc_action', '')}"
        )
    return "\n\n".join(lines)

report = f"""\
Apache Incubator Report — {CURRENT_QUARTER}
{'=' * 60}

Report period: {QUARTER_START} to {today}
Prepared: {today}

== 1. Podling Statistics ==

Total podlings ever accepted into the Incubator: {total_ever}

Current status (all-time):
  Current (in incubation): {current_count}
  Graduated:               {graduated_count}
  Retired:                 {retired_count}

Activity this calendar year ({today.year}):
  New podlings started:    {len(started_names)}
    {', '.join(started_names) if started_names else '(none)'}
  Graduated:               {len(graduated_ytd)}
  Retired:                 {len(retired_ytd)}

Activity this quarter ({CURRENT_QUARTER}):
  Graduated:               {len(quarter_graduations)}
  Retired:                 {len(quarter_retirements)}


== 2. Graduations and Retirements This Quarter ==

Graduations ({len(quarter_graduations)}):
{_podling_list(quarter_graduations)}

Retirements ({len(quarter_retirements)}):
{_podling_list(quarter_retirements)}


== 3. Reporting Cohort Summary ==

Source: {cohort_title}
Reporting period: {latest_period}
Podlings in cohort: {cohort_count}

{_cohort_table(cohort_podlings)}

Note: "Sign-offs" is the observed count of mentors who checked a sign-off box
in the report text. Full mentor sign-off is not required; this is informational.


== 4. Items Requiring Board Attention ==

The IPMC watchlist flags podlings with significant oversight concerns.
The following podlings at medium or higher severity are highlighted for
board awareness:

{_watchlist_section(board_items)}
"""

output_path = "scratch/board-report-draft.txt"
with open(output_path, "w") as f:
    f.write(report)

print(f"\nDraft written to: {output_path}")
print(f"Sections: Statistics | {len(quarter_graduations)} grad / "
      f"{len(quarter_retirements)} ret | {cohort_count} cohort | "
      f"{len(board_items)} board items")
```

---

## Output

The finished draft is at `scratch/board-report-draft.txt`. Present its full
contents to the user and offer to:

- Add specific notes about individual high-severity watchlist podlings
- Expand the cohort table with issue details from `issue_count`
- Adjust the quarter range if the user wants data for a different period

---

## Common issues

**`incubator_reports_overview` shows no 2026-Q3 report** — the cache only
contains approved board minutes, not in-progress reports. The most recent entry
is the correct one to use; note its period in the report header.

**`tool_completed_podlings_in_range` uses calendar year, not quarter** — the
tool only filters by year. Filter by `enddate` within `quarter_start` /
`quarter_end` after fetching the records (Step 3 does this automatically).

**`get_report_summary` needs the exact `report_id`** — use `report_ids[-1]`
from `incubator_reports_overview` to get the latest. Do not guess IDs.

**`tool_ipmc_watchlist` `report_source` defaults to a non-existent path** —
the server falls back gracefully; the health data is sufficient for the
watchlist. Pass `health_source` explicitly; omit `report_source` unless a
local ReportMCP cache is needed.

**Podling description is blank for new podlings** — if `description` is empty
or None, omit the description line from Section 2 rather than printing a blank.

**`observed_mentor_signoff_count` must not be rendered as a completion
fraction** — never divide by mentor count or apply traffic-light colouring.
Display only the raw count as shown in `_cohort_table`.

**PYTHONPATH must be set in every Bash subprocess** — if running code across
multiple Bash tool calls, re-export PYTHONPATH or use `sys.path.insert` at the
top of each script.
