---
name: maturity-model-assessment
description: >
  Builds an evidence pack for assessing an Apache Incubator podling against
  the Apache Project Maturity Model: the 38
  items in Code, Licenses and Copyright, Releases, Quality, Community,
  Consensus Building, Independence and Trademark and Branding. For each
  item it gathers what the ASF MCP servers, GitHub and the mailing list
  archives can show, marks it evidenced, proxy or human, and writes the
  question the PPMC still has to answer. Use it whenever someone asks to
  assess, evaluate or score a project against the maturity model, asks
  "how mature is Apache Foo (incubating)", wants a maturity self-assessment
  drafted for graduation or a PPMC review, asks which maturity items a podling
  falls short on, or asks what the model says about a specific item ID
  such as CS50 or TB30. It produces evidence and questions for the PPMC to
  finish, never a maturity verdict or score, because the model has no
  levels and is a guide rather than a requirements document.
---

# Maturity model assessment

Gather evidence; a person judges. The model says of itself that it is a
guide, not a requirements document, that there are no partial compliance
levels, and that it is used for self-assessment. So the output is a
half-filled self-assessment: facts where tools can reach them, and a
pointed question where they cannot. Never write a score, a percentage, a
pass or fail, or "the project is mature".

Keep facts and judgement apart. A fact carries its source and date. A
proxy signal is reported as the signal ("one person merged 24 of 30 PRs"),
not as the conclusion it hints at.

## Setup

Confirm the podling with `podlings:get_podling`; it gives the slug, start
date, mentors and homepage. If the name is a graduated project rather than
a current podling, say so and stop: this skill reads Incubator sources.

Check the model version. Fetch
https://community.apache.org/apache-way/apache-project-maturity-model.html
and read the version history line. `references/items.md` is written for
v1.4. If the page has moved on, re-read it and update `items.md` before
assessing, and say so in the report.

Read the policy pages the items lean on from the Policy MCP each run,
since policy changes: `resolved_licenses`, `voting`, `project_independence`,
`branding`, `security_committers`, `release_policy`. Cite each page's own
URL, not the MCP.

A shell with `gh` and network access is needed for the repository items
(CD30, CD40, CD50, QU30, QU50, CO20, CO60). Without one, do the rest and
list those items under Not checked.

## 1. Identity and rosters

In parallel: `apache-projects-mcp:get_project_people(<slug>)` for the PPMC
and committer rosters, `get_repositories` for the repository names, and
the podling status page at `incubator.apache.org/projects/<slug>.html` for
the roster history. Note committer and PPMC counts. This feeds LC40, CS10,
CO40 and the vote counts in RE20.

## 2. Repository facts

For the main repository, with `gh` (`references/tools.md` has the calls):
public flag and default branch; tags; SECURITY.md, CONTRIBUTING.md and
the community profile; the last 30 merged pull requests with author and
merger; the 20 oldest open issues. One pass of calls covers CD10, CD20,
CD40, CD50, QU30, QU50, CO20, CO60.

For CD50 read five merge commits whose author is not the merger and
check the author identity survived the merge.

## 3. Releases

Run `ipmc:release_artifact_evidence(podling, include_platforms=true,
release_page_url="auto")`. It lists every release on downloads.apache.org
and archive.apache.org, pairs the sidecars, checks the download page and
looks up the registries, in under ten seconds. If a source's `error` says
the listing may be incomplete, list that directory with curl
(`references/tools.md`). Match each release to a tag (CD40), check sidecars
(RE30), source archive present (RE10), download page wording (RE40).

For LC10 and LC50 inspect the latest source release's LICENSE, NOTICE and
headers. The podling-release-check skill's `scripts/check_rc.py` does this
for any release directory; use it where it is installed.

For LC20 and LC30 enumerate direct dependencies from the build descriptor
and classify against `resolved_licenses`. The magpie-repo-health
dependency-license-audit skill does this where installed. Report Category
X and Category B items individually.

## 4. Mailing lists

`incubator-mail:podling_release_vote_history(podling, timespan="lte=36M")`
gives the general@ vote and result threads for RE20 and RE50 (distinct
release managers); add `list_name="dev"` with the podling's domain for the
PPMC votes. `search_podling_mail` on dev@ for `[DISCUSS]`, `[VOTE]`,
`veto`, and for off-list markers (`slack`, `wechat`, `meeting`, `offline`)
in the last 12 months for CS20, CS40, CS50.

Say which list and timespan were searched. An empty result is "none
found in <list> over <span>", not "none".

Read the hits for CS40 and CS50 in context before recording anything;
a search count on its own is not evidence for those items.

## 5. Health and reports

`apache-health:get_window_metrics(podling, "12m")` and
`compare_windows(podling, ["3m","12m"])` for the metrics mapped in
`references/tools.md`. `incubator-reports:get_podling_reports(podling)`
for new committers and PPMC members by quarter (CO40) and mentor or
shepherd comments about off-list decisions (CS50).

If the question is graduation, also run the graduation-self-assessment
skill; it reads what the podling itself says is unfinished, which this
skill does not.

## 6. Branding

`asf-trademark:check_project_website(homepage, stage="podling",
project_name)` for CO10, QU30, TB10, TB20; the `ipmc` wrapper of the same check skips when
its trademark dependency is missing. `whois` any non-apache.org domain the site presents as its own
(TB20). `asf-policy:get_policy trademark_list` and
`asf-trademark:validate_name` for TB30; ask for the PODLINGNAMESEARCH
ticket key for a podling, since no tool reaches JIRA.

## 7. Assess each item

Work through `references/items.md` in order. For each item set the state:

- **Evidenced** when the listed tool facts were obtained and settle it.
- **Proxy** when signals were obtained; write the signal, not a verdict.
- **Human** when the item is marked Human, or when the tools for an
  Evidenced or Proxy item failed or the sample was too small. Downgrade
  freely; never upgrade a Human item because the proxies look good.

Write the PPMC question from `items.md`, adapted to what was found. Where
a fact contradicts the item (release with no vote, Category X dependency,
no Security link, one merger for most PRs), record the fact under
Evidence and put the gap as a question under For the PPMC. Keep the
model's own wording: no "fails", no "non-compliant".

## 8. Report

Follow `references/report-template.md`: opening paragraph with scope and
the guide-not-requirements sentence, per-section summary lines, one table
per section, the gaps list, the not-checked list. For a mailing list
post, drop the headings and bold and link the tables.

The evidenced / proxy / human split comes out within one item of 13 / 16
/ 9 for every podling, because it measures what the model's items let
tools reach, not the project. Never compare podlings on those counts; the
gaps list is where the differences are.

## Several podlings

For a cohort, run one subagent per podling with the podling name, the
path to this skill and the output file path, and have each reply with
its section counts, its five most consequential gaps, what it did not
check and any tool that misbehaved. Then write one comparison: a table of
recurring patterns (off-list discussion, merge concentration, single
release manager, PPMC growth, stale roster, security page, branding,
release hygiene, licensing, originating company) with one cell per
podling, and fold the tool lessons back into `references/tools.md`. Six
runs took 17 to 26 minutes and 250 to 380 thousand tokens each.

When an item turns out to be checkable by a tool this skill did not use,
add the call to `references/items.md` and `references/tools.md`. When a
PPMC answers a Human question in a way that suggests a proxy, add the
proxy, but leave the state as Human.
