# Worked Examples

Eight examples chosen to show the judgment calls, not just the tool calls. The
value is in what each one *declines* to do.

Examples 7 and 8 are the ones to read first if you are short on time. They are
the two halves of name resolution — a name that is no longer a podling, and a
podling that is no longer under that name — and between them they cover the
failure mode that fires most often.

---

## 1. Newcomer, conceptual

**Asked:** "I keep seeing 'podling' on Apache mailing lists. What is that?"

**Route:** `asf-policy:get_policy("incubator")` for the definition,
`podlings:list_current_podlings()` for one live number.

**Answer:**

> A podling is a project going through the Apache Incubator — the ASF's
> onboarding path for projects that want to become full Apache projects. The
> Incubator exists to check that a project can govern itself the Apache way:
> decisions made in public on mailing lists, a community that does not depend on
> a single company, clean intellectual property, and releases that follow ASF
> policy. Podlings get assigned mentors from the Incubator PMC, report on their
> progress regularly, and either graduate to become a top-level project or
> retire if it does not work out. There are about **[current count from
> `list_current_podlings()`]** in the Incubator at the moment.
>
> The Incubator's own guide is the best next read:
> https://incubator.apache.org/policy/incubation.html

The count is a placeholder on purpose — fetch it. Podling numbers move every
month, and a number carried over from an example is exactly the kind of stale
fact that gets repeated on a mailing list.

**What it declines to do:** no table of the 30 podlings, no metrics, no mention
of which servers were queried. They asked what a word means.

---

## 2. Contributor, actionable

**Asked:** "We're a podling and want to do our first release. What do we
actually have to do differently from a normal Apache project?"

**Route:** `asf-policy:get_policy(key="incubator")` — which contains all the
podling-specific requirements on its own — then
`incubator-releases:podling_releases(podling)` if the podling is identified.
`release_policy` and `voting` are only worth pulling if they also need the
general ASF release mechanics.

**Answer shape:** the four podling-specific deltas stated plainly and in order:

1. Two votes — at least 3 +1 PPMC votes on the podling dev list *and* more +1s
   than -1s, then 3 +1 IPMC votes on general@incubator.
2. `incubating` in the release filename.
3. A disclaimer in the archive, in a `DISCLAIMER` or `DISCLAIMER-WIP` file.
4. Distribution through `www.apache.org/dist/incubator/<Podling>`; other
   channels are allowed in addition, not instead.

Quote the policy for each rather than paraphrasing from memory — a contributor
is going to act on this, and the vote thresholds are the part people get wrong.

Then, if the podling is known, what their previous releases did, because a
concrete precedent from their own project lands better than policy prose. Close
by pointing at their mentors as the people to sanity-check the first one.

**What it declines to do:** it does not restate general ASF release policy at
length. They asked what is *different*, and burying the four deltas inside a
full release tutorial is how people miss the DISCLAIMER. It also does not list
signing and checksums among the deltas — those apply identically to TLPs, and
including them both misleads and pushes a real requirement off the list.

**Note:** if the podling was not named, ask — the precedent half of this answer
needs it, and their mentors' names are worth including.

---

## 3. The question that looks empirical but is normative

**Asked:** "How long until we can graduate?"

This sounds like a request for a date. It is not answerable as one, and giving a
number would be actively misleading.

**Route:** `asf-policy:get_policy("incubator")` and the Incubator graduation
guide for the actual criteria; `ipmc:graduation_readiness(podling=,
include_evidence=true)` for where they stand;
`podlings:graduation_time_over_time` only as context, and only with its caveat.

**Answer shape:** lead by reframing — graduation is not time-based, it is
criteria-based, so the honest answer is which criteria are met and which are
not. Then the assessment against each. Then, if they want the statistical
context, the typical range with the explicit note that it describes other
projects and predicts nothing about theirs. Close with who decides: the IPMC
votes, then the board.

**What it declines to do:** it does not produce an estimated date, even a hedged
one. Contributors quote these back to their communities as commitments.

---

## 4. IPMC oversight

**Asked:** "Anything I should look at before this month's Incubator report?"

**Route:** hand to the `ipmc` skill if available. Otherwise:

1. `podlings:reporting_schedule(report_month="YYYY-MM", due_this_month=true)` —
   this is what establishes who actually owes a report in the month you mean.
   Pin `report_month` rather than relying on the `due_this_month` default, which
   rolls forward once the current cycle's date has passed.
2. `ipmc:ipmc_watchlist(severity_at_least="medium", limit=5)` and
   `ipmc:reporting_gaps()` for the concern signals.
3. `ipmc:significant_changes()` for what moved since last month.

Note that `ipmc:reporting_cohort()` is **not** a "who is due this month" tool
despite the name — it buckets all current podlings with health coverage into
concern groups and takes no month parameter. Answering from it alone names
podlings that are not in this month's cohort at all.

**Answer shape:** grouped by what action is needed rather than by severity
score — podlings that owe a report, podlings whose report will need a mentor to
chase it, and anything that changed since last month. One sentence of evidence
per podling. The genuinely useful finding is usually the *overlap*: a podling
that is both in this month's cohort and carrying a high signal. Two or three
recommended actions at the end, not fifteen.

**Check the availability blocks before writing any of it.** If `report_source`
and `mail_source` come back `available: false`, every finding is health-derived
only, and the answer needs a line saying so — something like "note that report
and mail evidence weren't available for this pass, so these are health signals
only." The tools will still say `confidence: high`; that refers to the health
data, not to the completeness of the evidence base.

**What it declines to do:** it does not dump every signal for every podling.
An oversight answer that requires the same triage work the tool was supposed to
do has not helped.

---

## 5. Naming, with a legal edge

**Asked:** "Can we name our project Apache Quill? There's a commercial product
called Quill."

**Route:** `asf-trademark:validate_name(proposed_name="Quill",
technical_description=...)`, then `perform_name_search`, then
`asf-policy:get_policy("podling_branding")`.

**Answer shape:** report what the automated checks found — reserved-mark
status, format, existing ASF collisions, and the external hits with a note on
whether they look relevant to the same technical field. State clearly that this
is a pre-check, not clearance. Then: name conflicts in the same field are
exactly what `trademarks@apache.org` exists to assess, and they should raise it
there before the name gets attached to a proposal, a domain, and a repo.

**What it declines to do:** it does not say the name is fine, and it does not
say it is a problem. Neither call is this skill's to make, and a wrong
reassurance here costs a rename later.

---

## 6. When the data cannot answer it

**Asked:** "Is our community healthy? We feel like things have gone quiet."

**Route:** `apache-health:health_overview()` first to check coverage,
`get_window_metrics` / `compare_windows` if the podling is covered,
`incubator-mail:podling_mail_overview` for list volume,
`incubator-releases:podling_releases` for cadence.

**Answer shape:** what the signals show, separated by source, with the window
each covers. Then the honest limit: these measure list traffic, commits,
releases, and reports. They do not measure whether the people involved are
losing interest, whether a key contributor is about to leave, or whether the
quiet is a normal lull after a release. Their own read of the room is data the
tools do not have — and if the numbers look fine but it feels quiet, that gap is
worth raising with their mentors rather than dismissing.

If the podling is absent from health data, say that plainly and answer from
lifecycle, mail, and release evidence only.

**What it declines to do:** it does not answer "yes" or "no". It does not
reassure them because the metrics look acceptable, and it does not alarm them
because one window dipped.

---

## 7. The name that is not a podling

**Asked:** "When is Iceberg's next Incubator report due?"

The premise is false — Iceberg graduated in May 2020 — and the report tooling
will not tell you that. `get_report_due_dates()` takes no podling argument, so it
returns the real upcoming Incubator cycle dates regardless of who you asked
about. Answer straight from it and you have just told a top-level project's
maintainer that they owe the Incubator a report.

**Route:** `podlings:list_podlings(search="Iceberg")` first — it returns the
record with `status: graduated` and an end date. `apache-projects:search_projects`
confirms it is now a TLP.

**Answer:**

> Iceberg isn't a podling any more — it graduated from the Incubator on
> 2020-05-20 and is now a top-level Apache project, so no Incubator report is
> ever due. As a TLP it reports to the ASF board on the board's quarterly
> schedule, through its own PMC rather than through the IPMC.
>
> If you were after the current Incubator reporting dates for a different
> project, tell me which one and I'll look it up.

**What it declines to do:** it does not answer the question as asked. Correcting
the premise *is* the answer here, and the offer at the end keeps it helpful
rather than pedantic.

**Generalise this.** The same trap applies to any podling-scoped question about a
graduated, retired, or never-incubated project: DISCLAIMER requirements, mentor
lists, `-incubating` naming, IPMC votes. Checking `status` costs one call and
prevents a whole class of confidently wrong answers.

---

## 8. The name that has changed

**Asked:** "How is Hunter doing these days?"

There is no podling called Hunter, and stopping there is wrong. Otava entered
incubation under that name, and the only trace is in its description: "Otava
entered Incubation as Hunter". So `list_podlings(search="Hunter")` returns
exactly one hit whose *name* does not match — which is precisely the shape a
strict name-match rule throws away.

**Route:** `podlings:list_podlings(search="Hunter")`, then read the description
of the hit rather than only its name. `get_podling(name="Otava")` to confirm.

**Answer shape:** lead with the rename, because that is the thing the asker does
not know — "Hunter is now Otava; it was renamed during incubation." Then the
status they actually asked for. Naming the change explicitly matters: someone
searching their own memory for "Hunter" needs to learn the current name, not just
receive facts under a label they will not recognise.

**What it declines to do:** it does not report that no such podling exists, and
it does not offer a similar-sounding current podling as a guess. "Did you mean
Hamilton?" reads as helpfulness but is coincidence — the names merely share a
letter or two, and answering about the wrong project confidently is worse than
admitting the search came up empty.

**Why this case exists.** An earlier version of this skill said to use "the hit
whose name actually matches", added to stop the Amoro/Iceberg false positive.
That rule broke this case: it discarded the one correct hit and produced a
confident "there is no Hunter podling". Both failure directions are live, so
triage the hits rather than applying a single rule — see `routing.md` §3.

---

## Register, side by side

The same fact, pitched three ways:

- **Newcomer:** "Podlings send in a progress report every three months, and
  their mentors sign off on it."
- **Contributor:** "Your report is due in the March cycle — the report itself is
  due two weeks before the board meeting, and mentor sign-off closes about a week
  after that. Check the current dates rather than trusting either from memory."
- **IPMC:** "Foo is in the March cohort. Two of the last four reports were
  missed and the latest observed mentor sign-off is below its rolling average,
  so this one likely needs chasing."

All three are accurate. Sending the third one to a first-time contributor reads
as a complaint being filed about them.
