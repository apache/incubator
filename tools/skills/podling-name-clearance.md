---
name: podling-name-clearance
description: Clear a proposed Apache Incubator podling name and produce the PODLINGNAMESEARCH writeup. Use this skill whenever a user asks to run a name search, clear the name, check a podling name for trademark conflicts, or file/prepare a PODLINGNAMESEARCH JIRA ticket. Triggers on phrases like "name search", "PODLINGNAMESEARCH", "clear the name", "check this podling name", "is <name> available", or "name clearance for <podling>".
allowed-tools:
  - Bash
  - Read
  - Write
---

# Podling Name Clearance

Run the ASF Incubator's automated name-clearance checks for a proposed podling
name and produce a writeup in the same shape as a PODLINGNAMESEARCH JIRA
ticket: a validation verdict, a trademark search, a web search, an ASF
namespace check, and a summary.

Run this skill when a mentor, IPMC member, or podling proposer wants a
proposed name checked before filing (or while drafting) a
`PODLINGNAMESEARCH` JIRA ticket at
https://issues.apache.org/jira/projects/PODLINGNAMESEARCH.

The proposed name is **required**. If the user has not supplied one, ask
before proceeding.

## Server location

The real checks live in the asf-trademark MCP server source. Use this
absolute path; never assume a relative path:

| Role | Path |
|------|------|
| Trademark/name-search tools | `~/TrademarkMCP` |

The harness has no MCP transport — invoke the server's Python functions
directly via `Bash` with that path's `src/` directory on `PYTHONPATH`. Never
call MCP tool endpoints over stdio.

```bash
export PYTHONPATH=~/TrademarkMCP/src
```

A helper script, `scripts/podling_name_clearance.py` (in this
skill directory), shows a minimal reference implementation of the same two
function names and the target writeup format (see `format_clearance_report`
in that file) — use it as a formatting template if useful, but call the real
`validate_name`/`perform_name_search` below for the actual verdicts and
search results; do not rely on the helper's own simplified logic for the
final report.

---

## Workflow

Work through these steps in order.

### Step 1 — Validate the name

Call `validate_name` from the TrademarkMCP source. This runs the reserved-name
check, the Native American tribal/cultural name check, format checks, and an
ASF project-namespace conflict check, and returns a structured verdict.

```bash
PYTHONPATH=~/TrademarkMCP/src python3 -c "
import sys, json
sys.path.insert(0, '~/TrademarkMCP/src')
from apache_trademark_mcp.tools import validate_name

result = validate_name(proposed_name='<Name>', technical_description='<one-sentence technical description>')
print(json.dumps(result, indent=2))
"
```

Key fields on the returned dict:

| Field | Meaning |
|-------|---------|
| `verdict` | `"PASS"`, `"WARN"`, or `"FAIL"` |
| `apache_form` | Full proposed name: `"Apache <Name>"` |
| `blocking_issues` | Hard stops (reserved word, Native American name, exact/near-exact ASF conflict, format violation) |
| `warnings` | Advisory items, non-blocking |
| `asf_name_conflicts` | Exact or near-exact matches against existing ASF project names — this is the **Apache Namespace** evidence |
| `nearby_asf_names` | String-similar ASF names listed for awareness only (not a policy violation) |
| `podlingnamesearch_process` | The required PODLINGNAMESEARCH steps and approvals |

If `verdict` is `"FAIL"`, do not treat the name as cleared — report the
`blocking_issues` prominently regardless of what Step 2 finds.

### Step 2 — Search for conflicts

Call `perform_name_search` from the same module. This runs live GitHub, PyPI,
and npm searches, assesses the findings, and assembles trademark-search URLs
and a JIRA ticket template.

```bash
PYTHONPATH=~/TrademarkMCP/src python3 -c "
import sys, json
sys.path.insert(0, '~/TrademarkMCP/src')
from apache_trademark_mcp.tools import perform_name_search

result = perform_name_search(proposed_name='<Name>', technical_description='<one-sentence technical description>')
print(json.dumps(result, indent=2))
"
```

Key fields on the returned dict:

| Field | Meaning |
|-------|---------|
| `suitability_assessment` | Overall automated assessment of the name's availability |
| `automated_search_results` | `github`, `pypi`, `npm` — each a list of matching projects/packages found |
| `trademark_search_urls` | Direct USPTO (and related) search URLs to run manually — record results in the writeup |
| `manual_searches_still_required` | Reminders: USPTO is required; Google and SourceForge should also be checked |
| `jira_ticket_template` | Pre-filled body text for the PODLINGNAMESEARCH JIRA ticket |
| `jira_url` | https://issues.apache.org/jira/projects/PODLINGNAMESEARCH |
| `next_step` | What to do after this automated pass (file JIRA, email trademarks@apache.org, await VP Brand Management approval) |

USPTO and Google are **not** searched automatically — `trademark_search_urls`
and `manual_searches_still_required` exist precisely because those two
searches must be run by hand. Open the USPTO URL, run the query, and record
what you find (or "No conflicts found." if nothing relevant turns up) in the
writeup's Trademark Search section. Do the same web-search check for the
Web Search section.

### Step 3 — Produce the PODLINGNAMESEARCH-format writeup

Combine the Step 1 and Step 2 results into a single Markdown writeup with
this exact section structure (mirrors `dragonfly_name_clearance.md`, the
sample output in the parent directory):

```markdown
# Podling Name Clearance: <Name>

**Name valid:** <YES if verdict is PASS or WARN, NO if verdict is FAIL>

## Trademark Search (USPTO)

<"No conflicts found." if the manual USPTO search (Step 2's trademark_search_urls) turned up nothing, otherwise list each conflict as "- <name>: <url>">

## Web Search (Google)

<"No conflicts found." if the manual web search turned up nothing relevant, otherwise list each conflict as "- <name>: <url>">

## Apache Namespace

<"No conflicts found." if asf_name_conflicts is empty, otherwise list each conflict as "- <name>: <url>">

## Summary

<"CLEARED: No conflicts found. Name appears available for use." if verdict is PASS and no conflicts were found in any section, otherwise "FURTHER REVIEW REQUIRED: <N> conflict(s) found." or, if verdict is FAIL, restate the blocking_issues>
```

If Step 1's `verdict` is `"WARN"` or there are entries in `nearby_asf_names`,
add a short note under the Apache Namespace section listing them for
awareness (they are not conflicts, but reviewers should see them).

Write the finished writeup to `<name.lower()>_name_clearance.md` in the
current working directory, matching the helper script's original naming
convention.

---

## Output checklist

Before declaring the name clearance complete, confirm the writeup:

- [ ] Has the `# Podling Name Clearance: <Name>` title
- [ ] States `**Name valid:**` YES or NO
- [ ] Has `## Trademark Search (USPTO)`, `## Web Search (Google)`, and
      `## Apache Namespace` sections, each with a conflict list or
      "No conflicts found."
- [ ] Has a `## Summary` section with a CLEARED or FURTHER REVIEW REQUIRED
      verdict
- [ ] Notes whether a `PODLINGNAMESEARCH` JIRA ticket still needs to be filed
      and that VP, Brand Management approval is mandatory — automated checks
      passing does **not** replace that process

## Common issues

**`validate_name` returns `FAIL`** — do not soften this in the writeup.
State the exact `blocking_issues` text; a reserved name, Native American
name, or exact ASF conflict cannot be cleared by a favorable Step 2 result.

**Live GitHub/PyPI/npm searches fail or time out** — note the failure in the
relevant section rather than silently reporting "No conflicts found."

**USPTO/Google searches are not automated** — never claim "No conflicts
found." for these two sections without actually opening the URLs from
`trademark_search_urls` and checking; if you cannot browse the web in this
session, say so explicitly instead of fabricating a clean result.
