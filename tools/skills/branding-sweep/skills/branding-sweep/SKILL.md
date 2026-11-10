---
name: branding-sweep
description: Batch ASF trademark and branding compliance sweep across all current Apache Incubator podlings, producing a ranked fix list for IPMC review. Use this skill whenever a user asks to check podling branding, run a trademark compliance sweep, audit podling websites for branding issues, or produce a branding fix list. Triggers on phrases like "branding sweep", "trademark check the podlings", "branding compliance", "check podling websites", "ranked fix list", or "which podlings have branding problems". Suited to a periodic (e.g. weekly) run.
---

# Skill: branding-sweep

(Recommended cadence if scheduled via a todo item: `@every=7d`.)

## Description

Batch ASF trademark and branding compliance sweep across all current Apache
Incubator podlings. Fetches each podling's homepage, checks it against the
ruleset in `scripts/rules.json`, scores violations by severity, and
produces a ranked fix list suitable for IPMC review.

## Required capabilities

- Outbound HTTP (fetches podling homepages and GitHub raw URLs)
- Read/write access to this skill directory
- Python 3.9+ in PATH (`python3`)

## Steps performed

1. **Refresh podling roster** — fetch the current list from
   `https://projects.apache.org/json/foundation/podlings.json` and overwrite
   `output/podlings.json`.
2. **Run sweep** — `python3 scripts/sweep.py`  
   Checks every podling in parallel (8 workers). Writes raw per-podling results
   to `output/raw-results.json`.
3. **Rank results** — `python3 scripts/ranker.py`  
   Scores each podling (critical×10, high×5, medium/low×1), sorts descending,
   writes `output/ranked-fix-list.json`.
4. **Render report** — inline Python that reads `ranked-fix-list.json` and
   writes `output/fix-list.md` with a `## Critical / ## Major / ## Minor`
   section per severity tier and one line per podling showing its top violation.

## Example invocation

```
/branding-sweep
```

Or to re-run just the ranking and report after a manual sweep:

```
python3 scripts/ranker.py
```

## Output files

| File | Description |
|------|-------------|
| `output/podlings.json` | Current podling roster (name, status, started) |
| `scripts/rules.json` | Branding ruleset (edit to add/tune rules) |
| `output/raw-results.json` | Per-podling violation arrays, unranked |
| `output/ranked-fix-list.json` | Scored and sorted fix list (JSON) |
| `output/fix-list.md` | Human-readable ranked report by severity tier |

## Rules checked (scripts/rules.json)

| ID | Severity | What is checked |
|----|----------|-----------------|
| `incubating-disclaimer` | critical | Homepage contains the standard ASF incubating disclaimer text |
| `apache-name-prefix` | critical | Page title uses "Apache \<Name\> (Incubating)" |
| `disclaimer-file-present` | critical | DISCLAIMER or DISCLAIMER-WIP exists in GitHub repo root |
| `notice-file-present` | critical | NOTICE file exists in GitHub repo root |
| `license-file-present` | critical | LICENSE file exists in GitHub repo root |
| `homepage-asf-branding` | high | Homepage links to apache.org |
| `homepage-incubator-branding` | high | Homepage links to incubator.apache.org |
| `no-graduated-claim` | high | Page does not falsely claim TLP / graduation status |
| `trademark-attribution` | medium | Footer includes ASF trademark attribution statement |

## Severity weights

| Severity | Weight | Meaning |
|----------|--------|---------|
| critical | 10 | Blocks graduation; must be fixed before IPMC vote |
| high | 5 | Significant branding gap; fix promptly |
| medium/low | 1 | Advisory; fix before graduation |

## Periodic scheduling

The `@every=7d` directive at the top of this file schedules the skill to run
automatically once per week. Results accumulate in the output files above;
`fix-list.md` is overwritten each run with the latest state.

To disable periodic runs, remove or comment out the `@every=` line.
