---
name: retirement-shepherd
description: Shepherd the retirement of a stalled Apache Incubator podling. Use this skill whenever a user asks to retire a podling, assess whether a podling should be retired, check for stalled evidence, draft a retirement announcement email, or produce a project shutdown checklist. Triggers on phrases like "retire podling", "retirement shepherd", "stalled podling", "shut down project", "retirement email", "shutdown checklist", "podling is inactive", or "move to Attic". This skill is the counterpart to the graduation-packet-builder — it handles podlings leaving the Incubator through retirement rather than graduation.
allowed-tools:
  - Bash
  - Read
  - Write
---

# Retirement Shepherd

Produce a complete retirement dossier for one Apache Incubator podling:
stalled-evidence assessment, retirement announcement email, and a step-by-step
shutdown checklist.

Run this skill when a podling's mentors, the IPMC chair, or a shepherd
believe a podling has stalled and should be retired rather than graduated.

## Server locations

All server code lives here — use these absolute paths; never assume relative
paths:

| Role | Path |
|------|------|
| IPMC oversight tools | `~/IncubatorMCP` |
| Per-podling health metrics | `~/HealthMCP` |
| Podling roster & schedule | `~/PodlingsMCP` |
| Report cache | `~/ReportMCP` |

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

- A mentor or IPMC member reports that a podling has had no meaningful commits,
  releases, or community activity for an extended period.
- `tool_stalled_podlings` or `tool_ipmc_watchlist` returns a podling with
  severity `"high"` and the recommended action involves retirement.
- The IPMC chair asks for a retirement dossier ahead of a board meeting.
- A user asks whether a specific podling should be retired.

The podling name is **required**. If the user has not supplied one, ask.
If the user asks to find stalled podlings first, run Step 1 across all current
podlings before targeting a specific one.

---

## Workflow

Work through these five steps in order. Each step writes a file under `scratch/`
(create the directory first if it does not exist: `mkdir -p scratch`). Later
steps depend on earlier ones, so do not skip ahead.

### Step 1 — Stalled evidence assessment

Collect objective evidence that the podling has stalled. The goal is to replace
subjective impressions with specific, sourced metrics that can be cited in the
retirement discussion.

#### 1a — Configure inactivity windows and thresholds

All three inactivity signals — commits, mailing-list posts, and releases —
are checked against configurable windows. Adjust these before running if the
podling is in an unusual situation (e.g., very new, recently donated large
codebase, seasonal project).

```python
import sys, json
sys.path.insert(0, '~/IncubatorMCP')
sys.path.insert(0, '~/HealthMCP/src')
sys.path.insert(0, '~/PodlingsMCP')
sys.path.insert(0, '~/ReportMCP/src')

PODLING     = '<podling-name>'   # replace with the target podling
REPORTS_DIR = '~/incubator/reports'

# --- Configurable inactivity detection ---
# Each signal has:
#   window   : health-report window to read from ("3m", "6m", "12m")
#   threshold: value at-or-below which the signal is FLAGGED
#   metric   : field name in the health report window
#   label    : human-readable name for reporting
INACTIVITY_CONFIG = {
    "commits": {
        "window":    "3m",   # short window — catches recent freeze quickly
        "metric":    "commits",
        "threshold": 5,       # ≤ 5 commits in 3 months = effectively inactive
        "label":     "Commits (3m)",
        "rationale": "Fewer than 5 commits in the past 3 months indicates"
                     " the codebase is not being actively developed.",
    },
    "mail_posts": {
        "window":    "6m",   # longer window — mailing lists can be quiet seasonally
        "metric":    "dev_messages",
        "threshold": 5,       # ≤ 5 messages in 6 months = community is silent
        "label":     "dev@ messages (6m)",
        "rationale": "Fewer than 5 messages on dev@ in 6 months indicates"
                     " the community is no longer actively discussing the project.",
    },
    "releases": {
        "window":    "12m",  # annual window — one release per year is the minimum
        "metric":    "releases",
        "threshold": 0,       # 0 releases in 12 months = no Apache release made
        "label":     "Releases (12m)",
        "rationale": "Zero releases in the past 12 months means the podling has"
                     " not produced any Apache-branded software deliverable.",
    },
}
# Optional overrides — uncomment and adjust as needed:
# INACTIVITY_CONFIG["commits"]["window"]    = "6m"   # use 6m if 3m data is noisy
# INACTIVITY_CONFIG["commits"]["threshold"] = 10      # stricter for large repos
# INACTIVITY_CONFIG["mail_posts"]["threshold"] = 10   # stricter for active domains
# INACTIVITY_CONFIG["releases"]["window"]  = "6m"    # tighter for older podlings
```

#### 1b — Collect health metrics across all windows

```python
from apache_health_mcp.tools import get_report_summary

try:
    health = get_report_summary(PODLING, REPORTS_DIR)
    all_windows = health.get("latest_metrics", {})
    # Keep all windows for context; flag signals use only the configured window
    activity_by_window = {}
    for w, m in all_windows.items():
        if m is None:
            continue
        activity_by_window[w] = {
            "date_range":        m.get("date_range"),
            "commits":           m.get("commits"),
            "unique_committers": m.get("unique_committers"),
            "unique_authors":    m.get("unique_authors"),
            "releases":          m.get("releases"),
            "new_contributors":  m.get("new_contributors"),
            "dev_messages":      m.get("dev_messages"),
            "dev_unique_posters":m.get("dev_unique_posters"),
            "bus50":             m.get("bus50"),
            "avg_mentor_signoffs": m.get("avg_mentor_signoffs"),
        }
except FileNotFoundError:
    health = None
    activity_by_window = {}
```

#### 1c — Evaluate inactivity signals against configured thresholds

```python
inactivity_flags = {}   # signal_name -> flag dict

for signal_name, cfg in INACTIVITY_CONFIG.items():
    window_key = cfg["window"]
    metric     = cfg["metric"]
    threshold  = cfg["threshold"]

    window_data = activity_by_window.get(window_key)
    if window_data is None:
        # Window not present in health report — treat as unknown, not flagged
        inactivity_flags[signal_name] = {
            "flagged":    None,       # None = data not available
            "window":     window_key,
            "metric":     metric,
            "observed":   None,
            "threshold":  threshold,
            "label":      cfg["label"],
            "rationale":  cfg["rationale"],
            "note":       f"Window '{window_key}' not available in health report.",
        }
        continue

    observed = window_data.get(metric)
    if observed is None:
        flagged = None   # metric absent — cannot evaluate
    else:
        flagged = observed <= threshold

    inactivity_flags[signal_name] = {
        "flagged":   flagged,    # True = stalled signal triggered
        "window":    window_key,
        "metric":    metric,
        "observed":  observed,
        "threshold": threshold,
        "label":     cfg["label"],
        "rationale": cfg["rationale"],
        "note":      None,
    }

# Count confirmed flags (True) vs unknown (None) vs passing (False)
confirmed_flags = [k for k, v in inactivity_flags.items() if v["flagged"] is True]
unknown_flags   = [k for k, v in inactivity_flags.items() if v["flagged"] is None]
passing_signals = [k for k, v in inactivity_flags.items() if v["flagged"] is False]
```

Print a detection table immediately after evaluation so the shepherd can
review the signals before proceeding:

```python
print(f"\n=== Inactivity Detection: Apache {PODLING} ===\n")
print(f"{'Signal':<15} {'Window':<6} {'Observed':>10}  {'Threshold':>10}  {'Flagged'}")
print("-" * 60)
for name, f in inactivity_flags.items():
    obs = str(f["observed"]) if f["observed"] is not None else "N/A"
    thr = str(f["threshold"])
    flag_str = "*** YES ***" if f["flagged"] else ("UNKNOWN" if f["flagged"] is None else "no")
    print(f"  {f['label']:<13} {f['window']:<6} {obs:>10}  {thr:>10}  {flag_str}")
print()
print(f"Confirmed flags: {len(confirmed_flags)} / {len(INACTIVITY_CONFIG)}"
      f" ({', '.join(confirmed_flags) or 'none'})")
```

#### 1d — IPMC stalled-podling and watchlist signals

```python
from ipmc.tools import tool_stalled_podlings, tool_ipmc_watchlist, tool_podling_brief

stalled_all = tool_stalled_podlings({"health_source": REPORTS_DIR})
stalled_entry = next(
    (item for item in stalled_all.get("items", [])
     if item["podling"].lower() == PODLING.lower()),
    None,
)
# stalled_entry fields when present:
#   severity: "high" / "medium" / "low"
#   definition_matched: list of signals matched by the IPMC strict definition
#   observed: {commits, unique_committers, dev_messages, releases_12m}
#   summary, recommended_ipmc_action

watchlist = tool_ipmc_watchlist({
    "health_source": REPORTS_DIR,
    "severity_at_least": "medium",
})
watchlist_entry = next(
    (item for item in watchlist.get("items", [])
     if item.get("podling", "").lower() == PODLING.lower()),
    None,
)

brief = tool_podling_brief({
    "podling": PODLING,
    "health_source": REPORTS_DIR,
    "focus": ["status", "health", "risk"],
    "brief_format": "detailed",
})
```

The IPMC strict stalled definition (from `tool_stalled_podlings`) requires
*all* of low commits, low committers, and no releases to fire together. The
configurable flags above are *independent* — each can fire alone. Both
perspectives appear in the final evidence record.

#### 1e — Podling lifecycle and incubation duration

```python
from podlings.tools import tool_get_podling
from datetime import date

podling_meta      = tool_get_podling({"name": PODLING})
p                 = podling_meta["podling"]
mentors           = p.get("mentors", [])
start_date        = p.get("startdate")
resource          = p.get("resource", PODLING.lower())
months_incubating = None
if start_date:
    start             = date.fromisoformat(start_date)
    today             = date.today()
    months_incubating = (today.year - start.year) * 12 + (today.month - start.month)

# A podling incubating > 24 months with all three signals flagged is a strong
# retirement candidate regardless of the IPMC strict stalled definition.
long_incubation = months_incubating is not None and months_incubating > 24
```

#### 1f — Report history: missed reports and chronic issues

```python
from apache_incubator_reports_mcp.tools import get_podling_reports

CACHE_DIR = '~/ReportMCP/.cache/agenda-incubator-reports'
try:
    report_history = get_podling_reports(podling=PODLING, cache_dir=CACHE_DIR)
    all_reports    = report_history.get("reports", [])   # newest-first
    total_reports  = len(all_reports)
    report_periods = [r["report_period"] for r in all_reports]

    # Tally issues across all reports; chronic = appears in ≥ 3 reports
    issue_counts = {}
    for r in all_reports:
        for issue in (r.get("issues") or []):
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
    chronic_issues = [i for i, cnt in issue_counts.items() if cnt >= 3]
except Exception:
    total_reports, report_periods, chronic_issues = 0, [], []
```

Chronic issues (in 3+ reports unresolved) corroborate the inactivity flags
and should be quoted in the retirement email.

#### 1g — Write the stalled-evidence record

```python
import os
os.makedirs("scratch", exist_ok=True)

# Overall retirement case strength:
# "strong"   — all three configurable flags triggered, or IPMC stalled signal at high severity
# "moderate" — one or two flags triggered, or watchlist entry present
# "weak"     — no flags triggered and not on watchlist
all_three_flagged = len(confirmed_flags) == 3
ipmc_high         = stalled_entry and stalled_entry.get("severity") == "high"

if all_three_flagged or ipmc_high:
    retirement_case_strength = "strong"
elif confirmed_flags or stalled_entry or watchlist_entry:
    retirement_case_strength = "moderate"
else:
    retirement_case_strength = "weak"

stalled_evidence = {
    "podling":                  PODLING,
    "resource":                 resource,
    "mentors":                  mentors,
    "start_date":               start_date,
    "months_incubating":        months_incubating,
    "long_incubation":          long_incubation,

    # Configurable inactivity detection results
    "inactivity_config":        INACTIVITY_CONFIG,
    "inactivity_flags":         inactivity_flags,
    "confirmed_flags":          confirmed_flags,    # signals that fired
    "unknown_flags":            unknown_flags,      # signals with missing data
    "passing_signals":          passing_signals,    # signals that did NOT fire

    # IPMC tool signals
    "stalled_signal":           stalled_entry,
    "watchlist_entry":          watchlist_entry,
    "brief_summary":            brief.get("status_summary"),
    "active_concerns":          brief.get("active_concerns", []),
    "outlook":                  brief.get("outlook"),

    # Raw health data for all windows
    "activity_by_window":       activity_by_window,

    # Board report history
    "report_history": {
        "total_reports_filed":  total_reports,
        "report_periods":       report_periods,
        "chronic_issues":       chronic_issues,
    },

    "retirement_case_strength": retirement_case_strength,
}

with open("scratch/stalled_evidence.json", "w") as f:
    json.dump(stalled_evidence, f, indent=2, default=str)

print(f"\nRetirement case strength: {retirement_case_strength.upper()}")
print(f"Confirmed inactivity flags: {confirmed_flags}")
if unknown_flags:
    print(f"Flags with missing data:   {unknown_flags}")
```

Write to `scratch/stalled_evidence.json`.

If `retirement_case_strength == "weak"`, report this to the user and ask
whether to continue — retiring a healthy podling is a serious, irreversible
action. The configurable thresholds can be tightened (lower values) to
produce a stricter assessment, or loosened if the project has a known
slow period.

---

### Step 2 — Mentor consultation record

Before posting a retirement discussion, the shepherding mentor must have
attempted to re-engage the PPMC and documented the outcome. Record this
manually:

```python
consultation = {
    "podling": PODLING,
    "contact_attempts": [
        # Each entry: date, method (email/IRC/call), summary of response
        # e.g. {"date": "2026-07-01", "method": "email to dev@",
        #        "response": "no reply after 14 days"}
    ],
    "ppmc_willing_to_continue": None,  # True / False / None (no response)
    "mentor_recommendation":    None,  # "retire" / "continue" / "defer"
    "notes": "",
}

with open("scratch/consultation.json", "w") as f:
    json.dump(consultation, f, indent=2, default=str)
```

The shepherd must fill `contact_attempts`, `ppmc_willing_to_continue`, and
`mentor_recommendation` before drafting the retirement email. If there has been
no contact attempt, make one and wait at least 14 days for a response before
proceeding.

Write to `scratch/consultation.json`.

---

### Step 3 — Draft the retirement emails

This step produces **two** emails that are sent at different points in the
retirement process:

| File | Template | When to send | To |
|------|----------|-------------|-----|
| `scratch/retire_discuss.txt` | `templates/retire-email.md` | Before the vote | `general@incubator.apache.org` |
| `scratch/retire_announce.txt` | `templates/announce-email.md` | After vote passes | `dev@`, `announce@`, CC `general@` |

Draft both now; send only the DISCUSS email immediately. Keep the announcement
draft until the vote closes successfully.

#### 3a — Load shared data

```python
import os, json

def _load(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

evidence     = _load("scratch/stalled_evidence.json")
consultation = _load("scratch/consultation.json")

mentors       = evidence.get("mentors", [])
months        = evidence.get("months_incubating", "?")
stalled_sig   = evidence.get("stalled_signal") or {}
concerns      = evidence.get("active_concerns", [])
chronic       = evidence.get("report_history", {}).get("chronic_issues", [])
resource      = evidence.get("resource", PODLING.lower())
iflags        = evidence.get("inactivity_flags", {})
confirmed     = evidence.get("confirmed_flags", [])

SHEPHERD_NAME = "<Your Name>"   # set before rendering

def _flag_row(signal_name):
    """Format one inactivity signal as a table row."""
    f = iflags.get(signal_name, {})
    obs = f.get("observed")
    obs_str = str(obs) if obs is not None else "N/A"
    flag_str = "YES" if f.get("flagged") else ("unknown" if f.get("flagged") is None else "no")
    return (f"  {f.get('label', signal_name):<28}"
            f"observed={obs_str:<6} threshold≤{f.get('threshold','?'):<4} flagged={flag_str}")

def _flag_detail(signal_name):
    """Format a signal for the announcement email (concise, factual)."""
    f = iflags.get(signal_name, {})
    obs = f.get("observed")
    return (f"  {f.get('label', signal_name):<28}"
            f"{str(obs) if obs is not None else 'N/A':>6}  "
            f"(threshold: ≤ {f.get('threshold', '?')})")
```

#### 3b — DISCUSS email (send before vote)

```python
subject_discuss = f"[DISCUSS] Retire Apache {PODLING} (incubating)"

discuss_body = f"""\
To: general@incubator.apache.org
Subject: {subject_discuss}

Hi all,

After reviewing the evidence below, I would like to propose that we retire
Apache {PODLING} (incubating) and move it to the Apache Attic.

== Background ==

Apache {PODLING} has been in incubation since {evidence.get("start_date", "unknown")}
({months} months). Despite mentoring efforts, the project has not demonstrated
the sustained activity or release cadence needed to graduate as a Top-Level
Project.

== Stalled Evidence ==

Inactivity signals (each checked against its own configurable window):
{_flag_row("commits")}
{_flag_row("mail_posts")}
{_flag_row("releases")}

Signals flagged: {len(confirmed)} / 3  ({", ".join(confirmed) if confirmed else "none"})

IPMC stalled signal: {"YES — " + stalled_sig.get("summary", "") if stalled_sig else "not triggered (see concerns below)"}

IPMC concerns:
{"".join("  - " + c + chr(10) for c in concerns) or "  (see stalled_evidence.json)"}

{"Chronic unresolved issues (3+ consecutive reports):" + chr(10) + "".join("  - " + i + chr(10) for i in chronic) if chronic else ""}

== Community Engagement ==

Mentor contact attempts: {len(consultation.get("contact_attempts", []))}
PPMC willing to continue: {consultation.get("ppmc_willing_to_continue", "unknown")}
Mentor recommendation: {consultation.get("mentor_recommendation", "pending")}

Mentor list: {", ".join(mentors) if mentors else "see podlings.xml"}

== Proposed Action ==

We propose to retire Apache {PODLING} and move the project to the Apache Attic
(https://attic.apache.org). This involves:

  1. A [DISCUSS] thread on this list (this email) — 72-hour open window.
  2. A [VOTE] thread on this list requiring 3 binding +1s and no unresolved -1s.
  3. Archival steps listed in the shutdown checklist (see scratch/shutdown_checklist.md).

If the PPMC wishes to continue instead, please respond in this thread within
72 hours with a concrete plan and a committed timeline.

We invite all community members, mentors, and IPMC members to share their views:

  - Do you agree this podling meets the criteria for retirement?
  - Is there evidence of activity or plans we have not considered?
  - Do you support moving to a [VOTE] thread?

Thanks,
{SHEPHERD_NAME}
"""

with open("scratch/retire_discuss.txt", "w") as f:
    f.write(discuss_body)
print(f"DISCUSS email written to: scratch/retire_discuss.txt")
```

#### 3c — Retirement announcement email (send after vote passes)

Based on `templates/announce-email.md`. This email goes to the
podling's own `dev@` list, the ASF-wide `announce@apache.org` (moderated),
and CCs `general@incubator.apache.org`.

```python
# vote_result is filled in after the vote closes; leave as placeholders for now
VOTE_START    = "<YYYY-MM-DD>"
VOTE_CLOSE    = "<YYYY-MM-DD>"
VOTE_PLUS1    = "<N>"
VOTE_ZERO     = "<N>"
VOTE_MINUS1   = "<N>"
VOTE_THREAD   = "<https://lists.apache.org/thread/...>"
ISSUE_TRACKER = f"https://issues.apache.org/jira/projects/{PODLING.upper()}"
WEBSITE_URL   = f"https://{resource}.apache.org"

subject_announce = f"Apache {PODLING} (incubating) has been retired"

announce_body = f"""\
To: dev@{resource}.apache.org
CC: general@incubator.apache.org
BCC: announce@apache.org
Subject: {subject_announce}

Dear Apache {PODLING} community,

The Apache Incubator PMC has voted to retire Apache {PODLING} (incubating)
and move the project to the Apache Attic. This email is the official
announcement of that decision.

== Vote Result ==

A [VOTE] thread was held on general@incubator.apache.org from
{VOTE_START} to {VOTE_CLOSE}. The result was:

  Binding +1:  {VOTE_PLUS1}
  Binding  0:  {VOTE_ZERO}
  Binding -1:  {VOTE_MINUS1}

The vote thread is archived at: {VOTE_THREAD}

== Reason for Retirement ==

Apache {PODLING} entered the Apache Incubator on {evidence.get("start_date", "unknown")}
and has been incubating for approximately {months} months. The retirement was
based on the following evidence of sustained inactivity:

{_flag_detail("commits")}
{_flag_detail("mail_posts")}
{_flag_detail("releases")}

{"Chronic unresolved issues (3+ board reports):" + chr(10) + "".join("  - " + i + chr(10) for i in chronic) if chronic else ""}

== What Happens Next ==

Project resources are being preserved in the Apache Attic:
  https://attic.apache.org/projects/{resource}.html

  Source code (read-only):  https://gitbox.apache.org/repos/asf/{resource}.git
  dev@ archive:             https://lists.apache.org/list.html?dev@{resource}.apache.org
  commits@ archive:         https://lists.apache.org/list.html?commits@{resource}.apache.org
  Issue tracker:            {ISSUE_TRACKER}
  Website:                  {WEBSITE_URL} (redirected to the Attic project page)

The mailing lists, issue tracker, and website will be closed or made
read-only as part of the shutdown checklist in scratch/shutdown_checklist.md.

== Thank You ==

We sincerely thank everyone who contributed to Apache {PODLING} — committers,
contributors, mentors, and users. All code and discussions remain available
through the Attic for future reference.

Questions? Contact general@incubator.apache.org.

{SHEPHERD_NAME}
Apache Incubator PMC
"""

with open("scratch/retire_announce.txt", "w") as f:
    f.write(announce_body)
print(f"Announcement email written to: scratch/retire_announce.txt")
print()
print("Next steps:")
print("  1. Review and send scratch/retire_discuss.txt to general@incubator.apache.org")
print("  2. After 72h, post a [VOTE] thread")
print("  3. After vote passes, fill in vote placeholders in scratch/retire_announce.txt")
print("  4. Send retire_announce.txt to dev@, announce@, CC general@")
```

Write to `scratch/retire_discuss.txt` and `scratch/retire_announce.txt`.

---

### Step 4 — Shutdown checklist

Produce a step-by-step checklist of every action required to shut down the
podling cleanly. The shepherd works through this list after a successful
retirement vote.

```python
resource = evidence.get("resource", PODLING.lower())

checklist = f"""# Shutdown Checklist — Apache {PODLING} (incubating)

Generated for: {PODLING}
Resource slug: {resource}
Mentors: {", ".join(evidence.get("mentors", []))}

Complete each item in order. Tick when done.

## Phase 1 — Vote and announcement (before archival)

  [ ] Post [DISCUSS] thread on general@incubator.apache.org and wait 72 h.
  [ ] Post [VOTE] thread on general@incubator.apache.org; requires ≥ 3 binding
      +1s and more +1s than -1s, with no unresolved -1s.
  [ ] Record vote result in scratch/vote_result.txt (vote count, thread URL).
  [ ] Notify dev@{resource}.apache.org and any user@ list of the retirement
      decision, including where archived code can be found.
  [ ] Post a [RESULT][VOTE] message on general@incubator.apache.org.

## Phase 2 — Apache Attic transfer

  [ ] Open an Attic JIRA ticket at https://issues.apache.org/jira/projects/ATTIC
      with subject "Move Apache {PODLING} to Attic".
      Include: mailing list names, git repo URL, website URL, JIRA project key.
  [ ] Coordinate with the Attic PMC to transfer or archive the project website.
  [ ] Redirect {resource}.apache.org (or {resource}.incubator.apache.org) to
      the Attic project page once the Attic entry is live.

## Phase 3 — Infrastructure retirement

  [ ] Close or archive mailing lists:
        dev@{resource}.apache.org
        commits@{resource}.apache.org
        user@{resource}.apache.org  (if active)
      Coordinate with ASF Infra (https://issues.apache.org/jira/projects/INFRA).
  [ ] Archive the source repository:
        https://gitbox.apache.org/repos/asf/{resource}.git
      Request read-only archival via INFRA JIRA.
  [ ] Close or archive the issue tracker:
        JIRA project: https://issues.apache.org/jira/projects/{PODLING.upper()}
        OR GitHub Issues: https://github.com/apache/{resource}
  [ ] Remove active CI/build pipelines (GitHub Actions, Jenkins) from the repo.
  [ ] Remove any release artifacts from dist.apache.org/repos/dist/release
      that must not remain available; confirm with the Attic PMC first.

## Phase 4 — Roster and metadata

  [ ] Update podlings.xml: set status="retired" and enddate=<YYYY-MM-DD>.
      The podlings.xml change is made by the Incubator PMC secretary.
  [ ] Remove the podling from the active reporting schedule in the Incubator
      board report for the next board meeting.
  [ ] Update the Incubator website podlings page if it caches active podlings.

## Phase 5 — Final board report

  [ ] The Incubator PMC includes a final retirement note in the next board
      report, citing the vote thread URL and the retirement date.
  [ ] The podling's mentors are released from mentoring duties.

## Contacts

  ASF Infra JIRA:  https://issues.apache.org/jira/projects/INFRA
  Apache Attic:    https://attic.apache.org / https://issues.apache.org/jira/projects/ATTIC
  Incubator PMC:   general@incubator.apache.org

## Notes

(add any podling-specific notes here — custom infra, active downstream users,
 donated IP that needs special handling, etc.)
"""

with open("scratch/shutdown_checklist.md", "w") as f:
    f.write(checklist)

print("Written to: scratch/shutdown_checklist.md")
```

Write to `scratch/shutdown_checklist.md`.

---

### Step 5 — Summary report

Print a one-page summary for the shepherd before they post anything.

```python
strength = evidence.get("retirement_case_strength", "unknown")
mentor_rec = consultation.get("mentor_recommendation", "pending")

print(f"""
=== Retirement Dossier: Apache {PODLING} ===

Incubating since: {evidence.get("start_date", "?")} ({months} months)
Retirement case:  {strength.upper()}
Mentor recommendation: {mentor_rec}

Key stalled signals:
{"".join("  - " + s + chr(10) for s in (stalled_sig.get("definition_matched") or concerns[:3]))}

Next actions:
  1. Fill in SHEPHERD_NAME in scratch/retire_discuss.txt and scratch/retire_announce.txt.
  2. Complete consultation.json if mentor contact is not yet done.
  3. Post [DISCUSS] email (scratch/retire_discuss.txt) to general@incubator.apache.org.
  4. After 72 h, post [VOTE] thread.
  5. After vote passes, fill vote placeholders in scratch/retire_announce.txt and send.
  6. Work through scratch/shutdown_checklist.md after a successful vote.

Scratch files written:
  scratch/stalled_evidence.json
  scratch/consultation.json
  scratch/retire_discuss.txt
  scratch/retire_announce.txt
  scratch/shutdown_checklist.md
""")
```

---

## Output checklist

Before declaring the dossier complete, confirm all five files exist and are
non-empty:

- [ ] `scratch/stalled_evidence.json` — stalled signals, health metrics, lifecycle data
- [ ] `scratch/consultation.json` — mentor contact attempts and recommendation
- [ ] `scratch/retire_discuss.txt` — ready-to-post [DISCUSS] email to `general@incubator.apache.org`
- [ ] `scratch/retire_announce.txt` — post-vote announcement to `dev@`, CC `general@`, BCC `announce@`
- [ ] `scratch/shutdown_checklist.md` — ordered shutdown steps with checkboxes

---

## Common issues

**Adjusting the configurable windows** — the defaults (commits 3m ≤ 5,
mail_posts 6m ≤ 5, releases 12m = 0) are calibrated for a typical active
podling. For projects with known seasonal patterns or a single large initial
commit, raise the commit threshold or widen the window. For fast-moving
ecosystems where one release per year is genuinely insufficient, lower the
releases threshold to check 6m. Always record any override in the
`INACTIVITY_CONFIG` comment so the rationale is visible in the evidence record.

**`flagged = None` means data is missing, not that the signal is clear** —
if a health report window is absent, that signal is recorded as `unknown`.
Count `unknown_flags` separately from `confirmed_flags` in the email; do not
treat a missing window as evidence the project is healthy.

**`stalled_entry` is None but the podling seems inactive** — the IPMC strict
stalled definition requires low commits, low committers, AND no 12-month
releases simultaneously. A podling with mailing-list traffic but no commits may
not trigger it. Independent inactivity flags (from `INACTIVITY_CONFIG`) can
still fire on individual signals; use them and `watchlist_entry` as
supplementary evidence in the retirement email.

**PPMC responds and commits to a revival plan** — do not proceed to a vote.
Update `consultation.json` with the response, close the dossier, and schedule a
follow-up check in 90 days (use the monthly report review skill to monitor).

**`get_podling_reports` has no `limit` parameter** — it returns all cached
reports. Sort by `report_period` descending after retrieval; do not pass a
`limit` keyword argument.

**Podling has no health report** — `get_report_summary` raises `FileNotFoundError`.
Set `activity_by_window = {}` and note in the retirement email that health data
is unavailable; rely on `stalled_entry` and report-history evidence instead.

**PYTHONPATH must include all four repos** in the same Python process. Re-export
`PYTHONPATH` in every `subprocess` call or use `sys.path.insert` at the top of
each script.
