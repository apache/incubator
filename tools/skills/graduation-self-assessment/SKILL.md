---
name: graduation-self-assessment
description: >
  Checks an Apache Incubator podling's graduation readiness against what the
  podling itself says in its Incubator reports: the "three most important
  unfinished issues to address before graduating", the self-assessed maturity
  checkboxes, the "issues the IPMC or Board need to be aware of" answer, mentor
  comments and IPMC/shepherd notes. Use it whenever someone asks if a podling
  is ready to graduate, asks for a graduation readiness check or review, is
  preparing or reviewing a graduation vote or resolution, asks what is
  stopping a podling from graduating, or gets a graduation_readiness result
  from the ipmc MCP and wants it sanity checked. The ipmc graduation_readiness
  tool scores metrics only and ignores the podling's own view, so always run
  this skill alongside it rather than reporting that tool's verdict alone.
---

# Graduation self-assessment

`ipmc:graduation_readiness` scores health metrics, sign-offs and releases. It
does not read what the podling says is stopping it from graduating. This skill
puts the two side by side. A podling that says it has unfinished graduation
work is not ready, whatever the metrics say, until that work is shown to be
done.

Keep source facts (what the report says, what the metrics show) separate from
your judgement. Quote report text briefly; do not paraphrase it into
something stronger or weaker than the podling wrote.

## 1. Gather

**Status first.** Call `podlings:get_podling`. If the podling has graduated
or retired, say so with the end date and stop.

Then call in parallel:

```text
ipmc:graduation_readiness(podling="<name>", include_evidence=true)
incubator-reports:get_podling_reports(podling="<name>")
incubator-mail:podling_release_vote_history(podling="<name>", timespan="lte=12M")
incubator-mail:search_incubator_general_mail(query="<name> graduation", timespan="lte=12M")
```

Board minutes are published about a month after the meeting, so the latest
report is often missing from the cache. If `podlings:reporting_schedule`
shows a report was due since the latest cached one, read that month's page
in the INCUBATOR cwiki space (`cwiki:cwiki_get_page`, for example
`September2026`) with `format="storage"`, which keeps the `[X]` marks, and
date it by that month's board meeting. No page yet means the report is not
filed: say it is due. Use `refresh=true` only for minutes that should be
published; if it fails, carry on with the cache and its `refresh_warning`.

If neither the cache (retry with the lowercase name) nor cwiki has a report,
say there is no report history. For a podling that started in the last few
months that is expected: report what the proposal, acceptance vote and dev@
show, and give no combined view. Otherwise stop at the metric verdict,
flagged as unverified against the podling's own view.

If `graduation_readiness` returns an error, say so and carry on with the
podling's own evidence; give the combined view without a metric verdict.

If the metric result shows general-list mail as `"available": false`, say the
metric verdict was built without general@ evidence. The mail calls in this
skill go to the live archive, so they fill that gap.

**Freshness.** `report_period` is the board meeting month, and the date is
in `report_id` (`board-minutes-YYYY-MM-DD`). Reports are written one to
three weeks before that date. Evidence dated after the meeting is after the
report. Evidence in the weeks before it may or may not be: check whether
the report text mentions it. Note how old the latest report is and say so if
it is more than about three months.

Take the latest four reports, or all of them if there are fewer. Use older
reports only to date when an item first appeared. For each report read:

- **Unfinished issues**: read the "Three most important unfinished issues
  to address before graduating" section of `body` and check the parsed
  `issues` list against it. If the podling answers "None" or leaves it
  blank, say so, and take the blockers from the report narrative, mentor
  comments and IPMC notes instead. Ignore a blank numbered slot.
- **Maturity**: the boxes under "How would you assess the podling's
  maturity?" and any commentary. `[X]` is ticked; `[ ]` and `[]` are not.
  Count `[-]`, `[~]`, `[o]` or a note on an unticked box ("<== here",
  "current status") as partly there, and quote it. Commentary such as "not
  yet nearing graduation" counts as an unticked box.
- **Aware of**: the answer to "Are there any issues that the IPMC or ASF
  Board need to be aware of?"
- **New committers and PPMC members**: the answer to "When were the last committers or PPMC
  members elected?"
- **Mentors**: the answer to "Have your mentors been helpful and
  responsive?" and mentor comments in the sign-off block.
- **Last release**: `last_release`.
- **IPMC/Shepherd notes.**

From the graduation search, open any [DISCUSS] or [VOTE] graduation thread
and read it. Questions and concerns raised there count as concerns (step 2).
The search matches any message that names the podling, so check each hit is
about this podling. Also search general@ for the podling's name alone and
open any thread about its status or retirement: an open retirement
discussion changes the combined view (step 3). Do not rely on a "retire"
search; these threads are often titled "Discuss the status of Apache <name>"
and the replies say "retiring" or "retirement".

When two reports contradict each other, or a report contradicts the mail,
note it as a finding and go by the mail. Answers sometimes sit under the
wrong heading, for example the mentors answer under the new committers question; read the
answer for what it says, not where it is.

**Few reports.** With fewer than four reports, apply the checks that need a
run of reports (persistence, "Nearing graduation" four times, a mentor who
signed none of the last four, dropped items) only over the reports there
are, and say how many that is. One unsigned report is not yet worth noting.

## 2. Compare

Work through each check. Note each mismatch as a finding.

**Maturity vs verdict.**
- Metric verdict `ready` or `near_ready` but "Nearing graduation" not
  ticked: the podling does not think it is ready. This is a hard cap.
- "Nearing graduation" ticked but the verdict is `not_yet_ready` or
  `at_risk`: the podling may be overestimating, or the metrics are missing
  something. Say which dimensions disagree.
- "Nearing graduation" ticked for four or more reports in a row with no
  graduation thread found: likely stalled near the line. Graduation
  discussions often start on dev@, so search `list_name="dev"` on the
  podling's domain for "graduation" as well, and report a dev@-only thread
  as such. Zero hits from
  search is weak evidence, so say "no thread found", not "no discussion".

**Each unfinished issue.** Classify it. An issue can have more than one
kind; list all of them and use the most serious. Two issues of the same kind
that are steps of one task (trademark verification and a name search) count
as one.

| Kind | Examples | Blocking until |
|---|---|---|
| Release | first release, more releases, release cadence | a release passes |
| Release capability | more release managers, PPMC can release without help | someone outside the initial PPMC has run a release |
| Community | grow or diversify community, more committers or PPMC | committers and at least one PPMC member added from outside the initial roster and founding organisation |
| Governance | private list issues, voting, decisions off list | the podling shows it is resolved |
| Legal / brand / security | licensing, IP or grant coverage, trademarks, domain transfer, security handling | the podling shows it is resolved |
| Infrastructure | website, repo or docs transfer to ASF | ASF requirements are met |
| Graduation process | start graduation discussion, maturity model, draft resolution | not blocking; signals intent |
| Product work | features, roadmap, performance, docs polish | not blocking |

For each blocking issue, check whether the metric result already reflects it
(a matching weak `dimension_scores` entry, blocker or `missing_evidence`). A
blocking issue the metrics score as `strong` or ignore is the key finding of
this skill: report it explicitly.

**Persistence.** Match items by meaning, not wording, since podlings reword
every report. But a recurring goal with a new instance each time is not
stuck: "release 0.8", then "release 0.9", both shipped, is progress. An item
is stuck when the same unmet need appears in three or more reports.

Decide each blocking issue on evidence:

- **Release**: vote history marks each vote's `result` by `source`:
  `result_thread`, `reply_in_vote_thread`, `cancelled` or
  `cancelled_in_vote_thread`, and labels each result `ipmc` or `ppmc`. A
  cancelled vote has not passed. Read the IPMC result with
  `incubator-mail:get_incubator_general_email` rather than trusting a count,
  and note binding -1 or 0 votes and what they raised. Vote history covers
  general@ only, so also search the podling's dev@
  (`incubator-mail:search_podling_mail`, `list_name="dev"`, query `VOTE`)
  for a release still at the PPMC stage or a PPMC vote that failed.
- **Release capability**: the release managers across recent votes.
  When a podling releases several sub-products (core, adapters, SDKs),
  count release managers across all of them and judge each sub-product's
  votes on their own. One person running every sub-product's releases is
  still one release manager.
- **Community**: the new committers answer. Initial-roster dates only, or nobody
  added for six months or more, means not shown. Do not call these additions
  elections, even though the report template says "elected".
  `apache-projects-mcp:get_project_people` gives the current PPMC and
  committers; compare it with the initial roster in the podling's proposal
  or status page to see who joined later.
  Affiliations are rarely recorded: if you cannot show someone is from
  outside the founding organisations (there may be several), label the issue
  partly addressed and ask.
- **Others**: report text, mail, or ask.

Label each blocking issue:

- **open**: no evidence of progress.
- **partly addressed**: some evidence, not enough to meet the table.
- **met**: the table's test is met, before or after the report, even if the
  podling still lists it. Podlings often keep "grow the community" on the
  list until graduation; that alone is not a gap.
- **dropped without evidence**: gone from the list, nothing shows it was
  done. It counts toward the caps like open; a dropped item with some
  evidence is partly addressed and counts the same way.

**Aware of.** A plain "no", "none" or "N/A" is not a finding. A blank answer
is a gap; note it. Anything else is a finding, including an answer that
starts with "No" and then names ongoing work.

**Concerns.** A concern is a point about this podling raised by a mentor,
shepherd or IPMC member, in a report or on a graduation, release or general@
thread. General advice ("still needs some guidance") is not a concern, nor
is a routine IPMC note that raises no problem with the podling (sent a
reminder, CI or infra admin). These also count:

- A binding 0 or -1 asking for fixes, until a later release shows them
  fixed. If the voter said the fixes do not block ("not essential", "fix
  in the next release"), or voted +1 while listing fixes, it is a note; it
  becomes a concern if the next release ships without them.
- A missed report in the last twelve months, or two or more reports the
  IPMC had to chase. A graduated project reports to the board unprompted.
- An IPMC or shepherd note naming an issue without detail ("issues on
  private@"). Do not guess what it means: it is open unless a later note
  or mail shows it settled, and it becomes a follow-up question.

Label each concern **open** (unanswered, or answered without fixing it) or
**resolved** (fixed, or answered and the person raising it accepted the
answer, for example by voting +1 afterwards). A fix the podling reports with
evidence (a commit, a ticket, a release) is resolved unless the person who
raised it disputes it. This does not apply to a binding 0 or -1 on a release:
that stays open until a later release passes with the fixes. Acceptance on condition ("fine as long as the PPMC
deals with them") is resolved; carry the condition as a follow-up.
Concerns outweigh a positive
metric score in the same area.

**Mentoring.** Gaps in mentoring are the IPMC's to fix, not the podling's,
so they never cap the verdict. Note them separately:

- A mentor who signed none of the last four reports, or none since joining,
  and whether they cast binding votes on recent releases. Partial sign-off
  is not worth noting.
- A report with no mentor sign-off.
- A mentors answer that is blank, "No answer", "None", "Not applicable" or
  negative.
- A release vote that waited for binding votes.

A specific problem with the podling that a mentor raises is still a concern.

**Last release.** If the podling's stated last release is older than about
twelve months and vote history shows nothing newer, note it against
`release_maturity`. The metric tool checks this too; if it still scores a
release older than twelve months `strong`, say so.

## 3. Combined view

The order, best to worst, is `ready`, `near_ready`, `not_yet_ready`,
`at_risk`. Start from the metric verdict and apply every cap that fits; the
lowest wins.

- No "Nearing graduation" tick, any blocking issue open or partly addressed,
  or any open concern: at most `near_ready`.
- Two or more blocking issues open or partly addressed, or an open
  governance or legal concern that names a specific unresolved problem: at
  most `not_yet_ready`.
- An open retirement discussion, raised by the IPMC, a mentor or the PPMC:
  `at_risk`. Lead the report with it.
- Met issues and resolved concerns do not count toward a cap. If they were
  met after the latest report, say the podling has not yet reported them.
- Never raise the metric verdict on the strength of the podling's own
  optimism alone.

If one label decides between two levels, give both and say what would
settle it.

## 4. Report

Keep it short:

1. **Verdicts.** Metric verdict and confidence; podling self-assessment
   (latest maturity boxes and report period, with its age); combined view.
2. **What the podling says is stopping it.** The latest issues, each with
   kind, label, since when, and whether the metrics reflect it.
3. **Disagreements and concerns.** Each mismatch and concern from step 2,
   with its label, most serious first, and where it comes from.
4. **Mentoring.** The mentoring notes, for the IPMC. Omit if there are none.
5. **Follow-up.** Concrete questions for mentors or the PPMC, for example
   "Has the security issue listed since 2026-01 been resolved?" Phrase these
   as questions, not conclusions, unless the evidence is conclusive.

For a cohort question ("which podlings are close to graduating"), run
`ipmc:current_podlings_overview` first, then this skill for each podling
whose metric verdict is `ready` or `near_ready` or whose latest report ticks
"Nearing graduation", and give one line per podling with both verdicts.
