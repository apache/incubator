---
name: podling-onboarding
description: Run the new-podling onboarding workflow for an Apache Incubator podling. Use this skill whenever a user asks to onboard a new podling, review a podling proposal against the acceptance checklist, track SGA or ICLA receipt, verify infrastructure setup, or determine a podling's first board report date. Triggers on phrases like "onboard podling", "new podling checklist", "proposal review", "check SGA status", "ICLA coverage", "set up podling infra", "first report date", "bootstrap <podling>", or "what still needs to be done for <podling>".
allowed-tools:
  - Bash
  - Read
  - Write
---

# Podling Onboarding

Review a new Apache Incubator podling against the five-phase onboarding
checklist — proposal criteria, SGA receipt, ICLA coverage, infrastructure
provisioning, and first board report date — and produce a status report that
tells a mentor or IPMC member exactly what has been completed and what remains
to be done.

Run this skill immediately after a podling is accepted into the Incubator, and
again at any point when a mentor wants a snapshot of bootstrap progress.

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

Reference data fetched from cwiki and podlings.xml:

| Source | Local path |
|--------|-----------|
| Onboarding checklist | `docs/onboarding-checklist.md` |
| cwiki guidelines | `sources/cwiki-incubator-guidelines.html` |
| Podlings status XML | `sources/podlings-status.xml` |

---

## Trigger conditions

Run this workflow when:

- A mentor or IPMC member asks to onboard or bootstrap a named podling.
- A proposal has just been accepted and someone needs to know what to do next.
- A user asks whether SGA, ICLAs, infrastructure, or the first report date have
  been handled for a specific podling.
- A podling is new (entered the Incubator within the last 90 days) and a status
  check is requested.

The podling name is **required**. If the user has not supplied one, ask before
proceeding.

---

## Workflow

Work through these five phases in order. Each phase writes a section to
`scratch/onboarding-<podling>.md` (create `scratch/` first if needed:
`mkdir -p scratch`). Later phases depend on earlier ones; do not skip ahead.

```python
import sys, json, os
sys.path.insert(0, '~/IncubatorMCP')
sys.path.insert(0, '~/HealthMCP/src')
sys.path.insert(0, '~/PodlingsMCP')
sys.path.insert(0, '~/ReportMCP/src')

PODLING     = '<podling-name>'   # replace with the target podling name
REPORTS_DIR = '~/incubator/reports'
PODLINGS_XML = 'sources/podlings-status.xml'

os.makedirs('scratch', exist_ok=True)
OUTPUT      = f'scratch/onboarding-{PODLING.lower()}.md'
```

---


Each phase is a separate reference file. Read the phase file you are on,
complete it, then move to the next — they run in order and later phases
consume values the earlier ones establish. Do not load them all at once.

| Phase | Read | Covers |
|---|---|---|
| 1 | `references/phase-1-proposal-review.md` | board resolution, champion, mentor list, initial committers, IP clearance |
| 2 | `references/phase-2-sga-receipt.md` | whether an SGA is required, submission and acknowledgment, IP clearance file |
| 3 | `references/phase-3-icla-coverage.md` | roster build, Whimsy checks, ICLA submission, CCLA handling, the LDAP gate |
| 4 | `references/phase-4-infrastructure.md` | podlings.xml metadata, mailing lists, repo, issue tracker, cwiki, LDAP, website |
| 5 | `references/phase-5-first-report-date.md` | derive first report month, board meeting dates, podlings.xml update, submission |

---

## Output

After all five phases, write a summary block at the top of `OUTPUT`:

```python
phases_complete = {
    "proposal_review":    None,              # True if all manual checks confirmed
    "sga_receipt":        repos_may_proceed,
    "icla_coverage":      all_iclas_confirmed,
    "infrastructure":     infra_complete,
    "first_report_date":  phase5_pass,
}

ready_to_operate = all(v is True for v in phases_complete.values())

summary = f"""# Onboarding Status: Apache {PODLING} (incubating)

Accepted: {start_date or "unknown"}
Reporting group: {reporting_group or "unknown"}  Monthly phase: {"active" if monthly_active else "completed"}
First report due: {first_report_date or "unknown"}

| Phase | Status |
|-------|--------|
| 1 Proposal review     | {"DONE" if phases_complete["proposal_review"] else "PENDING"} |
| 2 SGA receipt         | {"DONE" if phases_complete["sga_receipt"] else "PENDING"} |
| 3 ICLA coverage       | {"DONE" if phases_complete["icla_coverage"] else "PENDING"} |
| 4 Infrastructure      | {"DONE" if phases_complete["infrastructure"] else "PENDING"} |
| 5 First report date   | {"DONE" if phases_complete["first_report_date"] else "PENDING"} |

Overall: {"READY TO OPERATE" if ready_to_operate else "BOOTSTRAP IN PROGRESS"}
"""

# Prepend summary to the per-phase content already written to OUTPUT
with open(OUTPUT) as f:
    existing = f.read()
with open(OUTPUT, "w") as f:
    f.write(summary + "\n---\n\n" + existing)

print(f"Onboarding status written to: {OUTPUT}")
print(f"Overall: {'READY TO OPERATE' if ready_to_operate else 'BOOTSTRAP IN PROGRESS'}")
```

---

## Output checklist

Before presenting results to the user, confirm `scratch/onboarding-<podling>.md`
is non-empty and contains all five phase sections:

- [ ] `## Phase 1 — Proposal Review` with criteria table and manual check results
- [ ] `## Phase 2 — SGA Receipt` with `sga_required`, `sga_filed`, `sga_ack` status
- [ ] `## Phase 3 — ICLA Coverage` with per-person ICLA record
- [ ] `## Phase 4 — Infrastructure Provisioning` with per-step status
- [ ] `## Phase 5 — First Board Report Date` with calculated date and cadence table
- [ ] Summary block at the top with overall `READY TO OPERATE` / `BOOTSTRAP IN PROGRESS` verdict

---

## Common issues

**SGA is required but repos have already been requested** — flag this to the
mentor immediately. Repositories should not contain donated code under a
non-Apache licence until the SGA is on file. If repos already exist, confirm
with the ASF Secretary and INFRA whether the content must be withheld until
the SGA clears.

**Mentor is not yet an IPMC member** — a prospective mentor must request
election to the IPMC via `private@incubator.apache.org` before incubation
formally begins. This process may take a few days. Do not assign IPMC-only
responsibilities to a non-member mentor.

**ICLA processing is slow** — ICLAs are processed by the ASF Secretary manually
and may take days to weeks. Start the process immediately after acceptance; do
not block infrastructure provisioning on ICLAs for existing ASF committers (they
already have accounts and ICLAs on file — check Whimsy first).

**`podling_xml` is None** — the podling entry has not yet been added to
`podlings.xml`. Phase 4 Step 4a is incomplete. Add the entry and re-run.

**Reporting group not set** — if `reporting_group` is None, the `<reporting>`
element is missing from `podlings.xml`. The mentor must add it. Without a
group, the podling will not appear in the quarterly reporting schedule.

**`monthly` attribute not removed after third report** — after three monthly
reports the `monthly="True"` attribute must be removed from the `<reporting>`
element in `podlings.xml`. If it remains, the podling will continue to be
scheduled for monthly reports indefinitely. Check the `monthly_active` value
and flag if three reports have already been filed.

**`tool_get_podling` raises KeyError** — the podling name may not match the
`name` attribute in `podlings.xml` exactly (case-sensitive). Try the resource
slug or check the XML directly:
`grep -i '<podling name=' sources/podlings-status.xml | grep -i <term>`

**Infrastructure items partially done** — partial infrastructure (e.g., lists
created but LDAP accounts pending) is normal in the first days after acceptance.
Record each item's state truthfully in `infra_status`; do not mark items as
`True` until they are verified.
