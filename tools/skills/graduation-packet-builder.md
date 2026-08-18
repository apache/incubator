---
name: graduation-packet-builder
description: Build a graduation packet for an Apache Incubator podling. Use this skill whenever a user asks to prepare a graduation packet, assess graduation readiness, draft a graduation DISCUSS email, draft a board graduation resolution, or produce a summary of a podling's maturity evidence, name search status, community health, or release history for graduation. Triggers on phrases like "graduation packet", "graduate <podling>", "draft graduation resolution", "graduation DISCUSS email", "graduation readiness report", "prepare graduation", or "maturity evidence for graduation".
allowed-tools:
  - Bash
  - Read
  - Write
---

# Graduation Packet Builder

Produce a complete graduation packet for one Apache Incubator podling: maturity
evidence, name search status, community and release history, a ready-to-post
DISCUSS email, and a ready-to-submit board resolution.

Run this skill when a podling's mentors or IPMC chair believe the project is
approaching graduation and want a consolidated evidence dossier.

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

- A podling mentor, PPMC member, or IPMC member requests a graduation packet or
  DISCUSS email for a named podling.
- The IPMC chair asks for a graduation readiness dossier ahead of a board meeting.
- A user asks whether a specific podling is ready to graduate.

The podling name is **required**. If the user has not supplied one, ask before
proceeding.

---

## Workflow

Work through these six steps in order. Each step writes a file under `scratch/`;
later steps depend on earlier ones, so do not skip ahead.

### Step 1 — Graduation readiness assessment

Call `tool_graduation_readiness` from IncubatorMCP with `include_evidence=True`
to retrieve the overall readiness assessment and supporting evidence.

```python
import sys, json
sys.path.insert(0, '~/IncubatorMCP')
sys.path.insert(0, '~/HealthMCP/src')
sys.path.insert(0, '~/PodlingsMCP')
sys.path.insert(0, '~/ReportMCP/src')

from ipmc.tools import tool_graduation_readiness

PODLING = '<podling-name>'   # replace with the target podling

readiness = tool_graduation_readiness({
    "podling": PODLING,
    "include_evidence": True,
    "strict_mode": False,
})
```

Key output fields to capture:

| Field | Meaning |
|-------|---------|
| `assessment` | `"ready"`, `"near_ready"`, or `"not_yet_ready"` |
| `confidence` | Evidence confidence: `"high"`, `"medium"`, or `"low"` |
| `summary` | One-paragraph readiness narrative |
| `strengths` | List of positive signals (each has `dimension`, `statement`) |
| `blockers` | List of graduation blockers (each has `dimension`, `statement`) |
| `missing_evidence` | Data gaps that reduce confidence |
| `dimension_scores` | Per-dimension score map (commits, diversity, releases, mentoring, reporting) |
| `evidence` | Detailed evidence statements with sources |
| `recommended_next_steps` | Ordered list of actions before a graduation vote |

If `assessment` is `"not_yet_ready"` and `blockers` is non-empty, list every
blocker explicitly in the packet and in the DISCUSS email. Do not suppress them.

Write to `scratch/readiness.json`.

### Step 2 — Name search status

Run the automated trademark naming check. This covers reserved marks, Native
American name check, ASF project-list conflicts, and (with `include_external_search`)
live GitHub, PyPI, and npm searches — the same evidence that appears in a
PODLINGNAMESEARCH JIRA ticket.

```python
from ipmc.tools import tool_trademark_naming_check

name_check = tool_trademark_naming_check({
    "proposed_name": PODLING,       # without the "Apache " prefix
    "include_external_search": True,
})
```

Key output fields:

| Field | Meaning |
|-------|---------|
| `verdict` | `"PASS"`, `"WARN"`, `"FAIL"`, or `"SKIP"` |
| `apache_form` | Full proposed name: `"Apache <Podling>"` |
| `blocking_issues` | Hard stops that must be resolved before graduation |
| `warnings` | Advisory items for trademarks@apache.org review |
| `asf_name_conflicts` | Exact matches with existing ASF project names |
| `fuzzy_asf_results` | Near-matches to check for confusion risk |
| `external_search` | GitHub/PyPI/npm results (populated when `include_external_search=True`) |
| `summary` | Human-readable verdict summary |
| `recommended_ipmc_action` | What the IPMC should do next |

Note in the packet whether a PODLINGNAMESEARCH JIRA ticket has been filed and
whether VP, Brand Management has approved. Automated checks passing does **not**
replace the JIRA process — record this caveat explicitly.

Write to `scratch/name_check.json`.

### Step 3 — Community history

Collect community health metrics and report history to document that a
self-sustaining community exists independently of the founding company.

#### 3a — Health metrics

```python
sys.path.insert(0, '~/HealthMCP/src')
from apache_health_mcp.tools import get_report_summary

REPORTS_DIR = '~/incubator/reports'

try:
    health = get_report_summary(PODLING, REPORTS_DIR)
    # health['windows'] is a dict keyed by window: '3m', '6m', '12m', 'to-date'
    # Each window contains:
    #   commits, unique_committers, releases, bus50, bus75,
    #   dev_messages, prs_merged, avg_mentor_signoffs, new_contributors
except FileNotFoundError:
    health = None  # podling has no health report yet
```

Capture for all available windows:

| Metric | Graduation signal |
|--------|-------------------|
| `unique_committers` | ≥ 3 in 3m; ≥ 5 to-date indicates growing community |
| `bus50` | ≥ 3 — at least three people hold 50% of commits |
| `releases` (12m) | ≥ 1 recent release; ideally 3+ total since entry |
| `avg_mentor_signoffs` | ≥ 2 consistent mentor engagement |
| `new_contributors` | Positive trend signals open community |
| `dev_messages` | Sustained list traffic shows public discussion |

#### 3b — Incubator report history

```python
sys.path.insert(0, '~/ReportMCP/src')
from apache_incubator_reports_mcp.tools import get_podling_reports

CACHE_DIR = '~/ReportMCP/.cache/agenda-incubator-reports'

reports = get_podling_reports(
    podling=PODLING,
    cache_dir=CACHE_DIR,
    limit=12,   # last 12 months of reports
)
# reports['reports'] is a list sorted newest-first
# Each entry has: report_period, issues, mentor_names, observed_mentor_signoff_count, narrative_excerpt
```

Note: total number of reports filed, any gaps (missed months), recurring issues
reported, and whether mentor sign-offs appear consistently.

#### 3c — Cross-source mismatches

```python
from ipmc.tools import tool_cross_source_mismatches

mismatches = tool_cross_source_mismatches({"podling": PODLING})
# Returns list of mismatches; each has: signal, severity, reason
# High/medium mismatches should be resolved before a graduation vote.
```

Write combined community data to `scratch/community.json`.

### Step 4 — Release history

Document that releases have been made correctly on Apache infrastructure with
proper naming and IP clearance.

#### 4a — Artifact evidence

```python
from ipmc.tools import tool_release_artifact_evidence

artifacts = tool_release_artifact_evidence({
    "podling": PODLING,
    "include_platforms": True,  # also checks GitHub, PyPI, npm, Maven
})
# Key fields:
#   artifacts: list of release files with naming and sidecar metadata
#   cadence: release interval summary
#   incubator_naming: whether filenames include "incubating"
#   platform_hints: GitHub/PyPI/Maven distribution evidence
```

Capture:
- Total number of releases on Apache dist infrastructure
- Whether all release artifact names include `incubating`
- Release cadence (first release date, most recent, interval)
- Platform distribution hints (GitHub tags/releases, PyPI versions, Maven Central)

#### 4b — Release vote evidence

```python
from ipmc.tools import tool_release_vote_evidence

votes = tool_release_vote_evidence({"podling": PODLING})
# Key fields:
#   observed.vote_count    — VOTE threads found on general@
#   observed.result_count  — RESULT threads found on general@
#   votes: list of vote thread summaries
#   results: list of result thread summaries
#   release_visibility_signals: IPMC-level signals about release governance
```

Flag any `release_visibility_signals` with severity `"medium"` or `"high"` in
the packet. All release votes must have passed on general@incubator.apache.org,
not only on the podling dev@ list.

Write combined release data to `scratch/releases.json`.

### Step 5 — Draft the DISCUSS email

Compose a ready-to-post email to general@incubator.apache.org proposing the
graduation discussion. Follow the ASF Incubator convention for DISCUSS threads.

```
Subject: [DISCUSS] Graduate Apache <Podling> (incubating)

To: general@incubator.apache.org

Hi all,

We would like to propose that Apache <Podling> (incubating) graduate to a
Top-Level Project.

== About Apache <Podling> ==

<One-paragraph description of what the podling does.>

== Maturity Assessment ==

The podling's IPMC maturity model assessment is "<assessment>" with
<confidence> confidence.

Strengths:
<bullet per strength from readiness['strengths']>

<If blockers present:>
Open items to resolve before a vote:
<bullet per blocker from readiness['blockers']>

== Community ==

- Unique committers (3m): <value>
- Unique committers (to-date): <value>
- Bus factor 50% (to-date): <value> people hold 50% of commits
- Avg mentor sign-offs per report: <value>
- Total Incubator board reports filed: <count>

== Releases ==

- Total releases on Apache infrastructure: <count>
- Most recent release: <version>, <date>
- All release artifact names include "incubating": <yes/no>
- Release votes passed on general@: <count>

== Name Clearance ==

Automated trademark check verdict: <verdict>
<If WARN/FAIL: list blocking_issues and warnings>
PODLINGNAMESEARCH JIRA: <link if available, otherwise "not yet filed">
VP, Brand Management approval: <approved/pending>

== Maturity Model Checklist ==

Please review the podling's self-assessment in the Incubator wiki:
<link to podling's maturity model page on cwiki>

== Proposed Initial PMC ==

<List of proposed PMC members — confirm with PPMC and mentors>

== Proposed Initial PMC Chair ==

<Name> (<Apache ID>)

We welcome feedback from the community and mentors. If there are no
unresolved objections after 72 hours, we will move to a [VOTE] thread.

Thanks,
<Shepherd name>
```

Substitute all `<…>` placeholders from the data collected in Steps 1–4.
If a value is unavailable, state "data not available" rather than omitting
the line.

Write the finished email to `scratch/discuss_email.txt`.

### Step 6 — Draft the board resolution

Compose the formal resolution text for the ASF board agenda. Use the standard
graduation resolution template. The PMC name and description come from the
podling's proposal; the initial PMC and chair come from the PPMC roster and
mentors' recommendation.

```
WHEREAS, the Board of Directors deems it to be in the best
interests of the Foundation and consistent with the
Foundation's purpose to establish an Apache <Podling> Project
Management Committee charged with the creation and maintenance
of open-source software, for distribution at no charge to the
public, related to <one-sentence description of the project>.

NOW, THEREFORE, BE IT RESOLVED, that a Project Management
Committee (PMC), to be known as the "Apache <Podling> Project",
be and hereby is established pursuant to Bylaws of the
Foundation; and be it further

RESOLVED, that the following individuals listed as "Proposed
PMC Members" are appointed to serve as the initial members of
the Apache <Podling> PMC:

  Proposed PMC Members:
  <First Last> (<Apache ID>)
  <First Last> (<Apache ID>)
  …

and be it further

RESOLVED, that <First Last> be appointed to the position of
initial PMC Chair for Apache <Podling>, to serve in accordance
with the Bylaws of the Foundation; and be it further

RESOLVED, that the initial Apache <Podling> PMC is requested
to establish a home page at https://apache.org/; and be it
further

RESOLVED, that the Apache <Podling> PMC is requested to
provide the Board of Directors with a quarterly report
beginning with the <Month YYYY> board meeting; and be it
further

RESOLVED, that all responsibilities pertaining to the Apache
<Podling> Podling currently assigned to the Incubator PMC are
henceforth assigned to the newly-established Apache <Podling>
Project Management Committee; and be it further

RESOLVED, that the Incubator PMC is requested to provide the
Board of Directors with a final report on the Apache <Podling>
Podling within three months of graduation.
```

Populate `<Podling>`, `<one-sentence description>`, the PMC list, and the
initial chair from:
- The readiness output (`readiness['recommended_next_steps']` often names the chair)
- The PodlingsMCP roster (mentor list, PPMC members)
- Confirmation from the user if any field is ambiguous

Write the finished resolution to `scratch/board_resolution.txt`.

---

## Output checklist

Before declaring the packet complete, confirm all six files exist and are
non-empty:

- [ ] `scratch/readiness.json` — graduation readiness assessment with evidence
- [ ] `scratch/name_check.json` — trademark name check verdict and details
- [ ] `scratch/community.json` — health metrics, report history, mismatches
- [ ] `scratch/releases.json` — artifact evidence and vote history
- [ ] `scratch/discuss_email.txt` — ready-to-post DISCUSS email
- [ ] `scratch/board_resolution.txt` — ready-to-submit board resolution

Report the overall readiness assessment, any blockers, the name check verdict,
and the total release count as a summary to the user before presenting the
draft emails.

---

## Common issues

**Podling has no health report** — `get_report_summary` raises `FileNotFoundError`
for very new or renamed podlings. Catch it, set `health = None`, and note in
the packet that health metrics are unavailable.

**Name check returns `SKIP`** — the apache-trademark-mcp dependency is not
installed or its cache is missing. Note the skip, and remind the user that a
manual PODLINGNAMESEARCH JIRA ticket is required regardless.

**Release vote evidence shows 0 results** — either the MailMCP cache has not
been refreshed or the votes were cast only on dev@ and not on general@. Flag
this as a governance gap; IPMC release votes on general@ are mandatory.

**`assessment` is `"not_yet_ready"` with blockers** — do not suppress the
blockers or draft a DISCUSS email that glosses over them. List them in the
packet and in the email. The packet's purpose is accurate evidence, not advocacy.

**PYTHONPATH must include all four repos** in the same Python process. If you
use multiple `subprocess` calls, re-export `PYTHONPATH` in each shell invocation
or inline it with `sys.path.insert` in every script.

**PMC list is not auto-populated** — the packet builder can suggest the PPMC
roster from PodlingsMCP as a starting point, but the final PMC list must be
confirmed by the mentors and PPMC chair before posting the VOTE or submitting
the resolution.
