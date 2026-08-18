<!-- Reference for the podling-onboarding skill. -->

# Phase 5 — First Board Report Date

Determine exactly when the first board report is due, build the full reporting
schedule for the first year, verify that `podlings.xml` records it correctly,
and explain how to submit via Whimsy.

**Background:** The ASF Board meets monthly, traditionally on the **third
Wednesday** of each month. Incubator podlings file a report at every board
meeting for the first three months after acceptance, then switch to quarterly
reporting. The Incubator shepherd (mentor) must sign off on each report before
it is included in the board agenda.

---

#### 5a — Derive the first report month

```python
from datetime import date, timedelta
import calendar as cal_mod

if not start_date:
    raise ValueError(
        "start_date is None — podlings.xml entry (Phase 4a) must be complete "
        "before Phase 5 can run"
    )

start = date.fromisoformat(start_date)

# The first report is due at the board meeting in the month AFTER acceptance.
# Example: accepted 2026-08-05 → first report due at the September board meeting.
if start.month == 12:
    first_report_year  = start.year + 1
    first_report_month = 1
else:
    first_report_year  = start.year
    first_report_month = start.month + 1

print(f"Podling accepted: {start_date}  (start month: {start.strftime('%B %Y')})")
print(f"First report due: {cal_mod.month_name[first_report_month]} {first_report_year}")
```

---

#### 5b — Calculate board meeting dates (third Wednesday)

The ASF Board meets on the third Wednesday of each month. Reports must be
submitted to the board agenda **at least one week before** the board meeting.
The typical deadline is the Wednesday one week prior to the board meeting.

```python
def third_wednesday(year: int, month: int) -> date:
    """Return the date of the third Wednesday in the given year/month."""
    # Find the first day of the month and advance to the first Wednesday (weekday 2)
    first = date(year, month, 1)
    days_to_wed = (2 - first.weekday()) % 7   # 0 if already Wednesday
    first_wed   = first + timedelta(days=days_to_wed)
    return first_wed + timedelta(weeks=2)      # third Wednesday

def report_deadline(board_meeting: date) -> date:
    """Report submission deadline: one week before the board meeting."""
    return board_meeting - timedelta(weeks=1)

# Build the schedule: 3 monthly reports, then quarterly
GROUP_MONTHS = {
    "1": [1, 4, 7, 10],
    "2": [2, 5, 8, 11],
    "3": [3, 6, 9, 12],
}

if reporting_group not in ("1", "2", "3"):
    print(f"WARNING: reporting_group='{reporting_group}' is invalid or unset. "
          "Fix podlings.xml (Phase 4a) before trusting the schedule below.")

quarterly_months = GROUP_MONTHS.get(str(reporting_group), [])

# Generate monthly schedule for reports 1–3
monthly_schedule = []
y, m = first_report_year, first_report_month
for report_num in range(1, 4):
    meeting  = third_wednesday(y, m)
    deadline = report_deadline(meeting)
    monthly_schedule.append({
        "report_num":    report_num,
        "type":          "monthly",
        "report_month":  f"{cal_mod.month_name[m]} {y}",
        "board_meeting": meeting.isoformat(),
        "deadline":      deadline.isoformat(),
        "note":          ("Remove monthly=\"True\" from podlings.xml after filing"
                          if report_num == 3 else ""),
    })
    m += 1
    if m > 12:
        m, y = 1, y + 1

# Generate the first four quarterly reports that come after the third monthly
# (use the reporting group to find the right months in the calendar year)
quarterly_schedule = []
# Start looking from the month after the third monthly report
after_monthly_y = y
after_monthly_m = m   # already incremented above

for _ in range(4):   # next 4 quarterly slots
    # Advance until we hit a quarter month for this group
    # and that month is after the end of the monthly phase
    found = False
    scan_y, scan_m = after_monthly_y, after_monthly_m
    for __ in range(12):   # scan up to 12 months ahead
        if scan_m in quarterly_months:
            meeting  = third_wednesday(scan_y, scan_m)
            deadline = report_deadline(meeting)
            quarterly_schedule.append({
                "type":          "quarterly",
                "report_month":  f"{cal_mod.month_name[scan_m]} {scan_y}",
                "board_meeting": meeting.isoformat(),
                "deadline":      deadline.isoformat(),
                "note":          f"Group {reporting_group} quarterly",
            })
            # Advance past this entry for the next iteration
            after_monthly_m = scan_m + 1
            if after_monthly_m > 12:
                after_monthly_m, after_monthly_y = 1, scan_y + 1
            else:
                after_monthly_y = scan_y
            found = True
            break
        scan_m += 1
        if scan_m > 12:
            scan_m, scan_y = 1, scan_y + 1
    if not found:
        break

full_schedule = monthly_schedule + quarterly_schedule
first_report_date = date.fromisoformat(monthly_schedule[0]["board_meeting"])

# Print the schedule
print(f"\nReporting group: {reporting_group}  "
      f"Quarterly months: {[cal_mod.month_name[m] for m in quarterly_months]}\n")
print(f"{'#':<4} {'Type':<10} {'Report month':<20} {'Board meeting':<16} "
      f"{'Deadline':<16} Notes")
print("-" * 88)
for i, s in enumerate(full_schedule, 1):
    rtype = s["type"]
    print(f"{i:<4} {rtype:<10} {s['report_month']:<20} {s['board_meeting']:<16} "
          f"{s['deadline']:<16} {s.get('note', '')}")
```

---

#### 5c — Verify and update podlings.xml

The `<reporting>` element in `podlings.xml` must be present and correct for
the podling to appear in the Whimsy board agenda tool. Two attributes matter:

| Attribute | Meaning | Required |
|-----------|---------|---------|
| `group`   | `"1"`, `"2"`, or `"3"` — quarterly reporting slot | Always |
| `monthly` | `"True"` — podling reports every month | First 3 months only |

```python
# Re-read podlings.xml to check current state (may have changed since Phase 4a)
tree    = ET.parse(PODLINGS_XML)
root    = tree.getroot()
xml_pod = next(
    (x for x in root.findall("podling")
     if x.get("name", "").lower() == PODLING.lower()),
    None,
)

phase5_failures = []

if xml_pod is None:
    phase5_failures.append(
        "podling entry missing from podlings.xml — complete Phase 4a first"
    )
else:
    r_el = xml_pod.find("reporting")
    if r_el is None:
        phase5_failures.append(
            "<reporting> element missing from podlings.xml entry — "
            "add <reporting group=\"N\" monthly=\"True\" />"
        )
    else:
        actual_group   = r_el.get("group")
        actual_monthly = r_el.get("monthly", "").lower() == "true"

        if actual_group not in ("1", "2", "3"):
            phase5_failures.append(
                f"reporting group='{actual_group}' is invalid; "
                "must be '1', '2', or '3' — coordinate with IPMC Secretary"
            )

        # Should monthly still be True?  Only if fewer than 3 reports have been filed.
        # We detect this by checking the ReportMCP cache if available, otherwise
        # trust the current value and flag if it looks wrong.
        try:
            from apache_incubator_reports_mcp.tools import get_podling_reports
            CACHE_DIR    = '~/ReportMCP/.cache/agenda-incubator-reports'
            report_hist  = get_podling_reports(podling=PODLING, cache_dir=CACHE_DIR)
            reports_filed = len(report_hist.get("reports", []))
        except Exception:
            reports_filed = None   # cache not available

        if reports_filed is not None:
            if reports_filed >= 3 and actual_monthly:
                phase5_failures.append(
                    f"{reports_filed} reports filed but monthly=\"True\" still set — "
                    "remove the monthly attribute from podlings.xml"
                )
            if reports_filed < 3 and not actual_monthly:
                phase5_failures.append(
                    f"only {reports_filed} reports filed but monthly attribute is absent — "
                    "add monthly=\"True\" to <reporting> until 3 reports are filed"
                )
        else:
            # Cannot auto-detect report count; rely on mentor to check
            if not actual_monthly:
                print("  NOTE: monthly attribute is not set — confirm ≥ 3 reports "
                      "have been filed, or add monthly=\"True\" if still in monthly phase")

        print(f"\n  podlings.xml <reporting>:")
        print(f"    group={actual_group}  monthly={actual_monthly}")
        if reports_filed is not None:
            print(f"    reports filed so far: {reports_filed}")
```

The required XML changes to make after the third report:

```xml
<!-- BEFORE (first 3 months): -->
<reporting group="2" monthly="True" />

<!-- AFTER (quarterly from month 4 onward): -->
<reporting group="2" />
```

Manual checks:

- [ ] Confirm `<reporting group="N" monthly="True" />` is present and correct in the SVN copy of `podlings.xml`
- [ ] Coordinate with the IPMC Secretary if the group number needs to change (e.g., to balance report load across groups)
- [ ] After the **third** monthly report is filed, remove `monthly="True"` from the element in `podlings.xml` and commit
- [ ] Verify the podling appears in the correct quarter on the board agenda at `https://whimsy.apache.org/board/agenda/`

---

#### 5d — Report submission process

Reports are collected via the **Whimsy Board Agenda** tool and then assembled
by the Incubator PMC shepherd into the monthly Incubator board report. The
PPMC drafts the report; the Mentor reviews and signs off; the Incubator PMC
secretary adds it to the agenda.

```python
# Report submission state — the mentor fills these in for each report period
report_log = []
for s in monthly_schedule:
    report_log.append({
        "period":          s["report_month"],
        "type":            "monthly",
        "deadline":        s["deadline"],
        "board_meeting":   s["board_meeting"],
        "draft_started":   None,   # True / False
        "mentor_signoff":  None,   # True / False — required before submission
        "submitted":       None,   # True / False
        "note":            s.get("note", ""),
    })

# Whimsy tool for report submission:
WHIMSY_REPORT_URL  = "https://whimsy.apache.org/board/agenda/"
INCUBATOR_REPORT_PAGE = "https://incubator.apache.org/guides/mentor.html#monthly_reports"

print(f"\nReport submission workflow:")
print(f"  1. PPMC drafts report on dev@ or private@")
print(f"  2. Mentor reviews and signs off ({INCUBATOR_REPORT_PAGE})")
print(f"  3. Report submitted via: {WHIMSY_REPORT_URL}")
print(f"  4. Incubator PMC shepherd adds to agenda before board meeting")
print()
print(f"  Deadline for first report: {monthly_schedule[0]['deadline']}")
print(f"  Board meeting date:        {monthly_schedule[0]['board_meeting']}")
```

What a good first report must include (from the Mentor Onboarding guide):

- Community growth (new contributors, committer nominations)
- Infrastructure status (lists created, repos provisioned)
- Release plans or first release timeline
- Any open issues or blockers
- Mentor sign-off that the report is accurate

What to avoid (from the Mentor Onboarding guide — warning signs):

- "Everything is fine" with no detail
- Copy-pasted boilerplate with no updates
- Optimistic tone that ignores real blockers
- Missing mentor sign-off (report will not be submitted without it)

Manual checks for each report period:

- [ ] PPMC assigned a report lead (rotating is recommended)
- [ ] Draft posted to `private@<resource>.apache.org` at least 2 weeks before the deadline
- [ ] Mentor reviewed the draft and confirmed accuracy
- [ ] Mentor sign-off recorded (email reply on the private list suffices)
- [ ] Report submitted to Whimsy before the deadline (`{monthly_schedule[0]['deadline']}` for report 1)
- [ ] After third report: `monthly="True"` removed from `podlings.xml`

---

#### Phase 5 — Write results

```python
phase5_pass = len(phase5_failures) == 0

# Format schedule as a Markdown table for the output file
schedule_md = (
    "| # | Type | Report month | Board meeting | Submission deadline | Notes |\n"
    "|---|------|--------------|---------------|---------------------|-------|\n"
)
for i, s in enumerate(full_schedule, 1):
    schedule_md += (
        f"| {i} | {s['type']} | {s['report_month']} | {s['board_meeting']} "
        f"| {s['deadline']} | {s.get('note', '')} |\n"
    )

# Current podlings.xml state
if xml_pod is not None and r_el is not None:
    xml_state = (f"group={r_el.get('group')}  "
                 f"monthly={r_el.get('monthly', 'not set')}")
else:
    xml_state = "MISSING"

with open(OUTPUT, "a") as fh:
    fh.write("## Phase 5 — First Board Report Date\n\n")
    fh.write(f"Acceptance date:     {start_date}\n")
    fh.write(f"First report due:    {monthly_schedule[0]['board_meeting']} "
             f"(deadline: {monthly_schedule[0]['deadline']})\n")
    fh.write(f"Reporting group:     {reporting_group or 'UNSET'}\n")
    fh.write(f"podlings.xml state:  {xml_state}\n")
    fh.write(f"Reports filed:       {reports_filed if reports_filed is not None else 'unknown'}\n\n")
    fh.write("### Reporting schedule\n\n")
    fh.write(schedule_md)
    fh.write(f"\nWhimsy agenda tool: {WHIMSY_REPORT_URL}\n")
    if phase5_failures:
        fh.write("\n**Failures:**\n")
        for f in phase5_failures:
            fh.write(f"- {f}\n")
    fh.write(f"\nOverall: {'PASS' if phase5_pass else 'INCOMPLETE'}\n\n")

print(f"\nPhase 5 — First Board Report Date: "
      f"{'PASS' if phase5_pass else 'INCOMPLETE'}")
```

---

