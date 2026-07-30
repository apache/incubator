# Routing Reference

Contents:

1. Source inventory — what each server is for, and its limits
2. Lane-by-lane routing with concrete calls
3. Name resolution
4. Freshness and cache handling
5. Common misroutes
6. Ambiguous tool names — read before calling these

---

## 1. Source inventory

Names below are logical. Actual tool prefixes vary (`ipmc`, `IPMC_MCP`,
`mcp__remote-devices__ipmc__…`). Match the logical name, but see §6 first for
the tool names that collide across servers.

Schemas are frequently deferred. Load a lane's tools in one `ToolSearch` call
with the comma-separated select form rather than one call each.

### `asf-policy` — the rulebook
Cached ASF policy documents with canonical URLs. `list_policies()` shows
everything by section; `search_policies(query)` returns ranked excerpts;
`get_policy(key)` returns a full document — the parameter is `key`, not `id`.
`force_refresh=true` re-fetches a single document.

Policy IDs that come up constantly: `incubator` (podling policy),
`incubator_ip_clearance`, `podling_branding`, `release_policy`, `voting`,
`release_distribution`, `release_download_pages`, `pmc`, `licenses`,
`resolved_licenses` (Category A/B/X), `source_headers`, `crypto_policy`,
`branding`, `trademark_policy`, `generative_tooling`, `security`.

Limits: it is a cache of published policy, and cached copies can be months old.
Search only covers documents already cached, and the cache does not know your
project's situation. For anything with a legal or release-blocking edge, give
the canonical URL so the reader sees the live text, and pass `force_refresh=true`
if the answer turns on a recent policy change.

### `cwiki` — Incubator Confluence space
`cwiki_search_pages(query, title_only=)`, `cwiki_get_page`,
`cwiki_get_children`, `cwiki_list_pages`. Where working notes, checklists, and
IPMC procedural pages live.

Limits: wiki pages are not policy. When the wiki and `asf-policy` disagree,
policy wins and the discrepancy is worth mentioning.

### `podlings` — lifecycle ground truth
Reads `podlings.xml`. `list_podlings(search=)`, `get_podling(name)`,
`list_current_podlings()`, `list_graduated_podlings()`,
`list_retired_podlings()`, `reporting_schedule()`, `mentor_count_stats()`,
`podling_stats()`, and the `*_over_time` / `*_by_year` family for history
(`graduation_rate_over_time`, `time_to_retirement_over_time`,
`podlings_started_over_time`, `completion_rate_over_time`, …).

This is the most reliable source and needs no local caches. Start here for
identity, status, dates, and mentor lists.

Two quirks in `reporting_schedule`:

- `due_this_month=true` rolls forward once the current cycle's due date has
  passed, so late in a month it returns *next* month's cohort. When someone says
  "this month", pin it explicitly with `report_month="YYYY-MM"` or `as_of_date`
  rather than trusting the default, and state which month you answered for.
- `total_matching` counts podlings evaluated, not matches truncated. Seeing
  `returned: 10, total_matching: 25` does not mean 15 results were dropped — it
  means 25 podlings were checked and 10 matched. Do not hedge about missing data
  on the strength of that gap. (This tool has no `limit` parameter; the
  filters are `name`, `report_month`, `as_of_date`, `due_this_month`,
  `sponsor_type`, `source`.)

### `incubator-reports` — Incubator report record
`get_report_due_dates()` and `get_report_due_dates_ical()` for cadence,
`get_podling_reports(podling)` for a podling's history,
`get_report_summary` / `get_report_markdown` for a specific report,
`search_reports(query)` across text, `incubator_reports_overview()`.

Limits: cached. A missing report may mean the cache lacks it. Report text is
what the podling *said*, which is narrative evidence, not measurement.

### `apache-health` — community health metrics
`health_overview()`, `list_podlings()`, `search_podlings`,
`get_window_metrics`, `compare_windows`, `query_metric_rankings`,
`list_metrics`, `get_report_summary` / `get_report_markdown`.

Windows run `3m`, `6m`, `12m`, `to-date`; prefer the freshest available in that
order. Check `health_overview()` for `latest_generated_on` before leaning on it.

Limits: derived from generated reports, so coverage is partial and can lag.
A podling missing from health data is a coverage gap, not a healthy podling and
not a broken tool.

### `incubator-releases` — release artifact evidence
`podling_releases(podling)` — artifacts, signatures, checksums, cadence,
Incubator naming and DISCLAIMER hints, download-page checks.

Limits: it observes dist/archive contents. A missing signature is a review item
for a human to confirm, not a proven policy violation.

Payload warning: this tool has no summary mode and lists every artifact
including each `.asc` and `.sha512`, which for an active podling is thousands of
tokens. `include_platforms` defaults to false and `max_depth` to 1 — leave them
there unless the question needs more. When you only want to show a podling its
own release precedent, summarise from the response rather than quoting it.

### `incubator-mail` — discussion evidence
General list: `recent_incubator_general_mail`, `search_incubator_general_mail`,
`get_incubator_general_email`, `incubator_general_mail_overview`, plus the
cached variants. Podling lists: `resolve_podling_mail_domain`,
`search_podling_mail`, `recent_podling_mail`, `podling_mail_overview`.
Votes: `find_release_vote_threads`, `find_release_result_threads`,
`summarize_release_vote_thread`, `podling_release_vote_history`.

`resolve_podling_mail_domain` requires `list_name`, constrained to `dev`,
`users`, or `commits` — `dev` is almost always the one you want.

Limits: search is lexical. Threads that used different wording will not match.
Absence of a hit is never evidence of absence — say "no matching thread found".

### `asf-trademark` — naming and branding
`validate_name(proposed_name, technical_description)` checks reserved marks,
format, Native American names, and the live committees+podlings list.
`perform_name_search`, `check_project_website`, `check_third_party_use`,
`get_naming_policy`, `get_branding_checklist`, `get_policy_guidance`,
`search_asf_projects`.

Pass names *without* the `Apache` prefix. Limits: these are automated
pre-checks, not a trademark clearance opinion. Contested cases go to
`trademarks@apache.org`.

### `ipmc` — oversight synthesis
`podling_brief`, `graduation_readiness`, `ipmc_watchlist`,
`mentoring_attention_needed`, `stalled_podlings`, `reporting_gaps`,
`reporting_reliability`, `reporting_cohort`, `report_narrative_signals`,
`cross_source_mismatches`, `release_visibility`, `release_vote_evidence`,
`release_artifact_evidence`, `community_health_summary`, `recent_changes`,
`significant_changes`, `current_podlings_overview`, `reporting_schedule`,
`configure_sources`, and on some builds `trademark_naming_check`,
`trademark_branding_check`, `trademark_third_party_check`,
`refresh_trademark_cache`. Refreshers live here, not on the source servers:
`refresh_report_cache`, `refresh_mail_cache`.

These compose the sources above and add opinions. Use them for oversight
questions; do not use them as a shortcut for single facts. If the `ipmc` skill
is available, hand oversight work to it.

**Read the availability block in every response.** Results carry `report_source`
and `mail_source` blocks with `available` flags. These tools will return
`confidence: high` on a finding while a source is `available: false` — meaning
the finding rests on health data alone, with no Incubator report text or mail
evidence behind it.

Check the `reason` before caveating, because `available: false` has two very
different meanings:

- *"Default ReportMCP cache directory does not exist"* / a missing or empty cache
  → a genuine coverage gap. Say so in the answer, and check the per-finding
  `missing:` list.
- *"General-list mail evidence was not needed for this tool call"* → the tool
  simply did not require it. No caveat needed; mentioning it implies a gap that
  is not there.

Look at `report_count` too — zero reports alongside a confident finding is the
clearest signal that the read is health-only.

**When two `ipmc` variants are both connected** — e.g. `ipmc` and `IPMC_MCP` —
they are not necessarily the same build. Prefer whichever exposes more tools
(the trademark checks above are the usual difference) and stay on it for the
whole answer rather than mixing.

Do not pass `*_source` parameters on routine calls — they are one-off
overrides. If a session needs custom paths, call `configure_sources` once.

`ipmc_watchlist` responses repeat a large `explainability` block per signal and
again per item, so an unbounded call across all podlings runs to tens of
thousands of tokens. Pass `limit`.

### `apache-projects` — the whole ASF
(may be connected as `apache-projects-mcp`)
`search_projects`, `get_project_overview`, `list_podlings`, `list_committees`,
`get_committee`, `get_project_people`, `get_releases`, `get_repositories`,
`get_person`, `find_projects_by_person`, `project_stats`, `search_people`.

Use it to settle podling-vs-TLP, and for people, repos, and releases across the
foundation.

---

## 2. Lane-by-lane routing

### "What's the rule for X?"
`asf-policy:search_policies(query="X")` → `get_policy(key="…")` for the full text.
Add `cwiki_search_pages` when the question is about Incubator procedure rather
than foundation policy. Always return the canonical URL.

### "Is Foo still incubating / when did it graduate?"
`podlings:get_podling(name)`. If unsure of the name,
`podlings:list_podlings(search=)` first, then `apache-projects:search_projects`
if it is not a podling at all.

### "When is our report due?"

**Confirm the project is a current podling first.**
`podlings:list_podlings(search="<name>")` and check `status`. Nothing in the
report tooling will catch this for you: `get_report_due_dates()` takes no
podling argument at all, so it returns valid Incubator cycle dates for a
graduated project, a retired one, or a name that was never in the Incubator.
Answering from it without the status check is how you tell a TLP maintainer their
Incubator report is due next month.

Once confirmed current:

- `podlings:reporting_schedule(name="<podling>")` — this is the podling-specific
  answer: their cadence and next expected reporting period.
- `incubator-reports:get_report_due_dates()` — the Incubator-wide cycle dates,
  useful as context, not as the answer.
- `get_report_due_dates_ical()` when someone wants it in a calendar.

If the project graduated or retired, say so with the date and explain what
replaced the obligation — graduated projects report to the board through their
own PMC; retired ones have no reporting obligation.

### "What did we say in our last report?"
`incubator-reports:get_podling_reports(podling)` → `get_report_markdown` for
the one they mean.

### "How do we cut a release?" (contributor)

If they are asking what is *different* for a podling, `get_policy("incubator")`
is the only policy you need — it contains all the podling-specific requirements.
`release_policy` and `voting` contain nothing podling-specific, so pull them only
when the question is about ASF release mechanics generally, or when the asker has
clearly never done an ASF release at all.

The podling-specific deltas, quoting Incubation Policy §Releases
(https://incubator.apache.org/policy/incubation.html) — all four verified
against the policy text, so they can be stated as requirements rather than
hedged:

1. **Two votes, not one.** The podling votes on its own public dev list, where
   "at least three +1 PPMC votes are required … and more +1 votes than -1
   votes". If it passes, the podling sends a summary to general@incubator and
   requests IPMC approval, where "three +1 Incubator PMC votes are required to
   approve a release". Note the second condition on the podling vote — three +1s
   is not sufficient on its own if there are three or more -1s.
2. **`incubating` in the filename.** "The release archive(s) MUST include the
   word 'incubating' in the filename."
3. **A disclaimer in the archive.** The archive MUST contain a disclaimer, which
   SHOULD sit in a `DISCLAIMER` or `DISCLAIMER-WIP` file alongside NOTICE and
   LICENSE. `DISCLAIMER-WIP` is the choice for podlings whose releases may not
   yet be fully ASF-policy-compliant, and it requires listing the known issues.
   A different disclaimer text needs IPMC approval first. The disclaimer
   obligation is broader than releases: policy requires it on the website and in
   all documentation and release announcements too.
4. **Distribution through the Incubator dist area.** "Releases for the Podling
   MUST be distributed through http://www.apache.org/dist/incubator/<Podling>".
   A podling MAY additionally distribute through other channels by following the
   release-distribution guidelines — so "we also publish to Maven Central / npm"
   is fine, but it does not replace the Incubator dist location.

Signing and checksums are *not* a podling-specific extra — those are general ASF
release policy, identical for TLPs. Listing them as podling requirements
misleads, and it crowds out the four above.

Note also that podlings MAY make **non-ASF releases** while incubating, as long
as they are moving toward ASF releases. Contributors sometimes assume every
artifact needs the full vote; it depends on whether they are calling it an ASF
release.

Then `incubator-releases:podling_releases(podling)` to show what their own
previous releases looked like, which is usually more convincing than policy
prose — but summarise it rather than quoting the artifact listing.

### "Did our release vote pass?" / "why was it challenged?"
`incubator-mail:find_release_vote_threads` then `find_release_result_threads`,
`summarize_release_vote_thread` for the detail. Cross-check artifacts with
`incubator-releases:podling_releases`. For the governance read,
`ipmc:release_vote_evidence(podling=)`.

### "Are we ready to graduate?"
Normative bar from `asf-policy:get_policy("incubator")` and the Incubator
graduation guide via `cwiki`. Evidence from
`ipmc:graduation_readiness(podling=, include_evidence=true)`. Present the bar,
then the evidence against it, then note that the IPMC and board decide.
Use `strict_mode=true` when they want the conservative read.

### "Which podlings need attention?" (IPMC)
Hand to the `ipmc` skill. Failing that: `ipmc:ipmc_watchlist` (with `limit`),
`mentoring_attention_needed`, `stalled_podlings`, `reporting_gaps`,
`community_health_summary`.

When the question is scoped to a reporting month, establish the cohort from
`podlings:reporting_schedule(report_month="YYYY-MM", due_this_month=true)` and
intersect it with the concern signals. `ipmc:reporting_cohort()` sounds like the
cohort tool but is not — it buckets all health-covered current podlings by
concern type and has no month parameter, so podlings it surfaces may not be due
this month at all.

### "Can we call it Apache Foo?"
`asf-trademark:validate_name(proposed_name="Foo", technical_description=...)`,
then `perform_name_search` for depth, then
`asf-policy:get_policy("podling_branding")` for what the podling must do once
named. Contested → `trademarks@apache.org`.

### "Our website / branding — are we compliant?"
`asf-trademark:check_project_website(...)` and `get_branding_checklist()`, with
`asf-policy:get_policy("podling_branding")` as the authority.

### "Someone else is using our name"
`asf-trademark:check_third_party_use(...)` +
`asf-policy:get_policy("downstream_distribution")` / `trademark_policy`.
Route the decision to `trademarks@apache.org` and the PMC.

### "How do I become a committer here?"
`asf-policy:get_policy("pmc")` for the mechanics, then the podling's own
practice: `incubator-mail:search_podling_mail(query="committer")`. Podlings vary
in how they run this, so describe the general shape and point at their dev list.

### "What is IP clearance / do I need an ICLA?"
`asf-policy:get_policy("incubator_ip_clearance")` and `get_policy("licenses")` /
`cla_faq`.

### "Can we depend on <library with licence L>?"
`asf-policy:get_policy("resolved_licenses")` for Category A/B/X. State the
category and its condition; send genuinely unclear cases to
`legal-discuss@apache.org`.

### "How does the Incubator work?" (newcomer)
Concept from `asf-policy:get_policy(key="incubator")` and the Incubator guides
via `cwiki` — the incubation policy's own framing is the safest source for "why
does the ASF do it this way", since it states the requirements the process
exists to test. Then
one live number from `podlings:list_current_podlings()` to make it concrete.
No tables.

### "Has incubation gotten slower / how many graduate?"
`podlings:graduation_rate_over_time`, `graduation_time_over_time`,
`completion_rate_over_time`, `time_to_retirement_over_time`,
`podlings_started_over_time`.

Interpretation trap: a spike in average time-to-graduate usually means several
long-stalled podlings were finally resolved that year, not that the process
slowed for healthy projects. Say so.

---

## 3. Name resolution

Order of attempts:

1. `podlings:list_podlings(search="<what they said>")` — covers current,
   graduated, and retired.

   **`search` matches descriptions as well as names**, which cuts both ways.
   Triage the hits in this order:

   | What you see | What it means |
   | --- | --- |
   | A hit whose `name` matches | Your project. Check `status`. |
   | No name match, but a description says "entered Incubation as X", "formerly X", or "renamed" | A **rename**. That hit is your answer — name it in the reply. |
   | A hit whose description merely mentions your term in passing | False positive. Keep looking. |
   | Nothing at all | Not a podling under that name — go to step 2. |

   Both error directions are real and have both been observed. Searching
   "Iceberg" returns Amoro first, because Amoro's description mentions Iceberg,
   and Amoro is *current* — so a careless status check passes on the wrong
   record. Searching "Hunter" returns only Otava, whose description reads "Otava
   entered Incubation as Hunter" — so a strict name-match rule discards the one
   correct hit and reports that no such podling exists.

   The question that separates them: does the description say the project **was**
   your term, or merely **uses** it? Confirm with
   `podlings:get_podling(name="…")`.

   Never conclude "there is no such podling" from a single search, and never
   offer a similar-sounding name as a substitute — suggesting "Hamilton" for
   "Hunter" looks like an answer but is coincidence. Say it is unknown instead.
2. `apache-projects:search_projects(query=...)` — settles TLP vs podling and
   catches projects that were never in the Incubator.
3. `asf-trademark:search_asf_projects(...)` — useful for near-miss names.
4. `incubator-mail:resolve_podling_mail_domain(...)` — before any podling
   mail search.

If two candidates are plausible, name both and ask which. Guessing wrong and
producing a confident answer about the wrong project is the worst outcome here.

Watch for: proposal names that changed before entry, projects that graduated
long ago and no longer have podling obligations, retired podlings the asker
believes are active, and names that collide with unrelated software.

---

## 4. Freshness and cache handling

- `podlings` reads live lifecycle data — trust it.
- `apache-health` is generated; check `latest_generated_on` and flag anything
  older than ~4 weeks.
- `incubator-reports` caches reports; refresh with its own `cache_all_reports`
  or `cache_report`.
- `incubator-mail` caches mail; refresh with `cache_incubator_general_mail`,
  `cache_incubator_general_mbox(es)`, `cache_podling_mail`,
  `cache_podling_mbox(es)`.
- `refresh_report_cache` and `refresh_mail_cache` live on **`ipmc`**, not on the
  reports or mail servers. Looking for them on the source server wastes a round
  trip.
- `asf-policy` shows cache age per document and takes `force_refresh` per call.
  Cached policy can be months old. For anything with a legal or
  release-blocking edge, give the canonical URL so the reader sees the live text.
- `asf-trademark` has `refresh_project_cache`.

Refresh when the question turns on recency and the cache is clearly behind;
otherwise say what window the cache covers.

Refreshing can be slow. When it is not needed for the answer, describe the
window covered rather than blocking on a refresh.

---

## 5. Common misroutes

| Symptom | Fix |
| --- | --- |
| Answering "what does graduation require" with graduation statistics | The question was normative — get the policy |
| Answering a report-due question without checking `status` | Graduated and retired projects get confident, wrong due dates |
| Running `ipmc:podling_brief` to find a report due date | Use `podlings:reporting_schedule(name=)` |
| Reporting an `ipmc` finding without checking `report_source` / `mail_source` availability | `confidence: high` can sit on health data alone |
| Calling `get_policy(id=...)` | The parameter is `key` |
| Listing signing/checksums as podling-specific release requirements | General ASF policy; the podling extras are filename, DISCLAIMER, two votes, Incubator dist area |
| Telling a contributor their podling is on a "watchlist" | Oversight vocabulary; translate to plain, actionable terms |
| Applying TLP release rules to a podling | Podlings need DISCLAIMER, `-incubating`, and an IPMC vote |
| Reporting an empty mail search as "no discussion happened" | Say "no matching thread found" |
| Treating a podling absent from health data as healthy | It is a coverage gap |
| Adjudicating a trademark dispute | Give policy plus `trademarks@apache.org` |
| Presenting `confidence: low` results as firm | Say the health report is missing and the read is lifecycle-only |
| Reporting `trend: unknown` as stable | It means trend evidence is unavailable |
| Calling a colliding tool name on whichever server appears first | See §6 — same name, different data |

---

## 6. Ambiguous tool names

Several servers export identical tool names that return different things.
"Match on the logical name" is unsafe for these — decide deliberately.

### `list_podlings` — four servers
- `podlings:list_podlings` — **lifecycle ground truth** from `podlings.xml`,
  with `status`, dates, mentors. Takes `search`. This is the one you want for
  identity and status questions.
- `apache-projects:list_podlings` — the ASF-wide project registry's view.
- `apache-health:list_podlings` — only podlings with **health-report coverage**.
  A podling missing here is a coverage gap, not a non-podling.
- `incubator-reports:list_podlings` — only podlings present in the **report
  cache**. Same caveat.

Answering "is Foo a podling?" from the health or reports variant produces false
negatives.

### `reporting_schedule` — two servers, not equivalent
- `podlings:reporting_schedule` — **use this one.** Source-of-truth cadence,
  takes `name`, `report_month`, `as_of_date`, `due_this_month`, `sponsor_type`.
- `ipmc:reporting_schedule` — a delegating wrapper whose parameter is `podling`,
  not `name`, and which fails outright on builds where the installed PodlingsMCP
  does not expose the underlying call (`"Installed PodlingsMCP does not provide
  reporting_schedule"`). Do not treat it as a drop-in alternative. If you land on
  it and it errors, go to `podlings:reporting_schedule`.

Either way, treat the output as source fact, separate from IPMC judgments about
reporting reliability.

### `get_report_summary` / `get_report_markdown` — two servers, different documents
- `apache-health:*` — a generated **community-health report**, i.e. metrics.
- `incubator-reports:*` — the podling's **Incubator report narrative**, i.e.
  what the podling wrote.

These are not interchangeable in either direction. Quoting a health report as
"what the podling reported" misattributes generated metrics to the podling's own
words, and vice versa.

### `search_asf_projects` / `search_projects`
- `asf-trademark:search_asf_projects` — for name-collision checking.
- `apache-projects:search_projects` — for settling podling vs TLP and finding
  project metadata.
