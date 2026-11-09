---
name: monthly-report-review
description: Run the IPMC monthly Incubator report review. Use this skill whenever a user asks to review this month's Incubator reports, check who has filed, flag missing reports, cross-check report narratives against health data, or draft shepherd comments for podlings. Triggers on phrases like "monthly report review", "check Incubator reports", "who hasn't filed", "draft shepherd comments", or "report cohort".
allowed-tools:
  - Bash
  - Read
  - Write
---

# Monthly Report Review

Heaviest recurring IPMC chore. Each month a cohort of podlings has reports due
before the board meeting. This skill pulls that cohort, flags who hasn't filed,
cross-checks each narrative against health and cross-source data, and drafts
shepherd comments ready to post to the incubator general@ list.

Run this skill at the start of each reporting window (typically the first week
of the month) and again after the report deadline to catch stragglers.

## Server locations

All server code lives here — use these absolute paths; never assume relative
paths like `../incubator-reports`:

| Role | Path |
|------|------|
| Report cache & due dates | `~/ReportMCP` |
| IPMC oversight tools | `~/IncubatorMCP` |
| Per-podling health metrics | `~/HealthMCP` |
| Podling roster & schedule | `~/PodlingsMCP` |

Health report Markdown files (input to HealthMCP): `~/incubator/reports`

The harness has no MCP transport — invoke server Python functions directly via
`Bash` with the PYTHONPATH below. Never call MCP tool endpoints over stdio.

```bash
export PYTHONPATH=~/IncubatorMCP:\
~/HealthMCP/src:\
~/PodlingsMCP:\
~/ReportMCP/src
```

---

## Trigger conditions

Run this workflow when:

- It is within the reporting window for the current month (reports typically
  due the first Wednesday, mentor sign-off the following Wednesday, board
  meeting the third Wednesday).
- A user asks who has or hasn't filed, wants shepherd comments drafted, or
  needs a narrative vs. health cross-check for any cohort podling.
- The IPMC chair requests a cohort summary ahead of the board meeting.

---

## Workflow

Work through these five steps in order. Each step produces a JSON or Markdown
artifact; later steps depend on earlier ones, so do not skip ahead.

### Step 1 — Pull the reporting cohort from ReportMCP

Identify which podlings are due this month and retrieve the key deadlines.

```python
import sys, json
sys.path.insert(0, '~/ReportMCP/src')
sys.path.insert(0, '~/PodlingsMCP')

from apache_incubator_reports_mcp.schedule import report_due_dates, current_year_month
from podlings.tools import tool_reporting_schedule, tool_list_current_podlings

year, month = current_year_month()
due = report_due_dates(year, month)          # reports_due, mentor_signoff_due, board_meeting

cohort_raw = tool_reporting_schedule(due_this_month=True)   # list of this month's podlings
all_podlings = tool_list_current_podlings()                  # full roster for enrichment
```

Key output fields: `report_period` (YYYY-MM), `reports_due`, `mentor_signoff_due`,
`board_meeting`, and a list of cohort podlings with `name`, `mentors`,
`startdate`, `months_in_incubation`.

Write to `scratch/cohort.json`.

### Step 2 — Check filing status via IncubatorMCP roster diff

For each cohort podling, retrieve the most recent cached report and determine
whether it has been filed for the current period.

```python
import sys, json
sys.path.insert(0, '~/ReportMCP/src')
from apache_incubator_reports_mcp.tools import get_podling_reports

CACHE_DIR = '~/ReportMCP/.cache/agenda-incubator-reports'

for podling in cohort:
    result = get_podling_reports(
        podling=podling['name'],
        cache_dir=CACHE_DIR,
        limit=3,
    )
    # result['reports'] is a list sorted newest-first
    # Compare result['reports'][0]['report_period'] against the current period
    # to determine filed_this_period (bool)
```

Also call `tool_current_podlings_overview({})` from IncubatorMCP for the
canonical mentor list if it differs from the PodlingsMCP roster.

```python
sys.path.insert(0, '~/IncubatorMCP')
from ipmc.tools import tool_current_podlings_overview
overview = tool_current_podlings_overview({})
```

Flag any podling whose latest cached `report_period` does not match the current
period as **unfiled**. Note the last cached period so shepherd comments can
reference it precisely.

Write to `scratch/filed_reports.json`.

### Step 3 — Cross-ref narratives against health data via HealthMCP

For each cohort podling, retrieve the parsed health snapshot and compare it
against the latest cached narrative.

```python
import sys
sys.path.insert(0, '~/HealthMCP/src')
from apache_health_mcp.tools import get_report_summary

REPORTS_DIR = '~/incubator/reports'

for podling in cohort:
    try:
        health = get_report_summary(podling['name'], REPORTS_DIR)
        # health['latest_metrics'] contains windows: '3m', '6m', '12m', 'to-date'
        # Each window has: commits, unique_committers, releases, bus50, bus75,
        #   dev_messages, prs_merged, avg_mentor_signoffs, new_contributors, ...
    except Exception:
        health = None   # Casbin and other new podlings may have no health report yet
```

Narrative vs. health discrepancies to flag:

| Signal | Threshold |
|--------|-----------|
| Commits (3m) | < 5 — very low; 5–14 — low |
| Unique committers (3m) | ≤ 2 — bus factor critical; ≤ 4 — modest |
| Bus factor 50% (3m) | ≤ 2 — highly concentrated |
| Releases (12m) | 0 — no releases in 12 months |
| Release in narrative but 0 in 3m health | Possible dist-tree visibility issue |

Write to `scratch/health_data.json`.

### Step 4 — Review cross_source_mismatches and narrative signals

For each cohort podling, call the two IncubatorMCP analysis tools.

```python
sys.path.insert(0, '~/IncubatorMCP')
from ipmc.tools import tool_cross_source_mismatches, tool_report_narrative_signals

# Both tools accept a dict of optional source-path overrides; pass {} for defaults
mismatches = tool_cross_source_mismatches({})   # returns per-podling mismatch list
signals    = tool_report_narrative_signals({})  # returns per-podling signal list
```

`cross_source_mismatches` detects discrepancies between cached report narratives
and current health/release evidence (e.g. `report_release_visibility_mismatch`).
Severity levels: `high`, `medium`, `low`.

`report_narrative_signals` detects:
- `possible_report_copy_forward` — text nearly identical to a prior period
- `recurring_reported_issue` — same open issue appears across multiple reports
- `low_mentor_signoff_count` — fewer than the expected number of mentor signs
- `release_without_evidence` — narrative claims a release with no dist evidence

Append results into `scratch/filed_reports.json` under each podling's entry.

### Step 5 — Draft shepherd comments

For each podling in the cohort (sorted alphabetically), draft a shepherd comment
that covers, in this order:

1. **Filing status** — if unfiled, a clear request to file with the deadline
   and a pointer to the last cached period.
2. **Open issues from the cached narrative** — list them and ask for a status
   update.
3. **Health discrepancies** — call out any signals from Step 3 with specific
   numbers from the health snapshot.
4. **Cross-source mismatches** — for any medium/high mismatch, quote the signal
   name, severity, and reason; ask the podling to reconcile.
5. **Narrative signals** — flag copy-forward or recurring issues; ask for a
   fresh narrative update.
6. **Mentor reminder** — remind mentors of the sign-off deadline if the report
   is filed or nearly due.

Format output as Markdown. **The file must begin with the first podling's
level-2 header** (e.g. `## Burr`) so the file passes automated checks that
anchor to the start of the file. Do not add a document-level `#` title above
the first `## PodlingName` header. Metadata (report period, deadlines) may
appear at the end of the file or in an HTML comment.

```markdown
## PodlingName
**Status:** NOT filed for 2026-08 (last cached: 2025-11)
**Started:** 2025-05-24

### Draft Shepherd Comment
Your Incubator report for **2026-08** was due on 2026-08-05 ...
```

Write to `scratch/shepherd_comments.md`.

---

## Output checklist

Before declaring the review complete, confirm:

- [ ] `scratch/cohort.json` — cohort list with deadlines
- [ ] `scratch/filed_reports.json` — filing status, mismatches, narrative signals per podling
- [ ] `scratch/health_data.json` — health metrics per podling
- [ ] `scratch/shepherd_comments.md` — one `## PodlingName` section per cohort podling

Post the shepherd comments to `general@incubator.apache.org` with subject
`[REPORT REVIEW] YYYY-MM Incubator reports — shepherd comments` after IPMC
chair review.

---

## Common issues

**Casbin (and very new podlings) have no health report** — `get_report_summary`
raises `FileNotFoundError`. Catch it, set health to `None`, and note in the
shepherd comment that no health snapshot is available.

**All cohort podlings show as unfiled early in the month** — the report cache
(`~/ReportMCP/.cache/agenda-incubator-reports`) is only as
fresh as the last `cache_all_reports` run. If the due date has not yet passed,
"unfiled" is expected; if it has passed, check whether the cache needs a
refresh.

**`cross_source_mismatches` lives in IncubatorMCP**, not ReportMCP. Import it
from `ipmc.tools`, not `apache_incubator_reports_mcp.tools`.

**PYTHONPATH must include all four repos** in the same Python process. If you
use multiple `subprocess` calls, re-export PYTHONPATH in each shell invocation
or inline it with `sys.path.insert` in every script.
