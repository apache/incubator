# Roadmap

Planned lessons for the Incubator AI tutors, and the state of each. See
[README.md](README.md) for what these are and how to run one, and
[PLAN.md](PLAN.md) for how one gets built.

Twenty-six lessons across eight tracks, covering the Incubator guides listed in
[`tools/seealso/resources.yml`](../seealso/resources.yml), which is the
maintained index of Incubator training material and the source of truth for what
exists.

Lessons are grouped by track rather than run as one sequence, so they line up
with the role paths already on the training site (mentor, IPMC, PPMC,
committer). Track A is the prerequisite for everything else; the rest can be
taken in any order.

## Status

| Status | Meaning |
|---|---|
| Done | Written, reviewed and in this directory |
| Next | Agreed as the next to build |
| Planned | Scoped, sources identified, not written |

## Track A: Foundations

For everyone, and the prerequisite for the other tracks. Assumes no knowledge of
the ASF at all.

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 1 | What the Incubator is, and whether you want it | Joining the Incubator, Podling Orientation Guide, Incubation Readiness, Common Myths, Glossary of Incubator Terms, Who Does What | **Done** |
| 2 | The Apache Way, in practice | Practicing The Apache Way, Governance in Practice, Why Governance Matters | **Done** |
| 3 | Working in public: lists, tone, culture, time zones | Communication in Apache Projects, International and Cultural Awareness, and the [ASF Code of Conduct](https://www.apache.org/foundation/policies/conduct) | **Done** |

Lesson 2 took a wider slice of Practicing The Apache Way than first scoped,
using twelve of its scenarios. No source moved, since that guide was only ever
lesson 2's, but two later lessons can now start deeper rather than introduce
from scratch:

- **Lesson 3** assumed public disagreement had been introduced, including why it
  is expected and what it costs when a thread turns personal. As written it
  opens at how a message lands wrong, then silence, then time zones, and reaches
  the Code of Conduct near the end, which suits a learner who arrives with a
  tone or time zone problem of their own.
- **Lesson 6** can assume the learner knows discussion builds consensus and a
  vote records it, and knows roughly what lazy consensus is. It should start at
  mechanics: which votes bind, who is eligible, what a veto is and when it
  applies.

## Track B: Podling startup and PPMC

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 4 | From proposal to podling | Proposal Discussions, Community Proposals, Initial Committer Selection | **Done** |
| 5 | Getting set up with Infra | Interacting with ASF Infra | **Done** |
| 6 | How decisions get made: lazy consensus, votes, vetoes | Voting and Consensus in Practice | **Done** |
| 7 | Growing committers and the PPMC | Podling Committer Onboarding, Podling PPMC Onboarding, Community Governance | **Done** |
| 8 | Writing a report the IPMC can use | Reporting Guide | **Done** |

Lesson 4 read the proposal template alongside its three guides, since the
template's Known Risks headings are the same concerns the guides describe from
the reviewers' side. It touches naming, licensing and IP only as far as a
proposal has to disclose them, so Lessons 9 and 10 keep their sources.

Lesson 6's wiki guide covers consensus and the podling vote types but says
nothing about vetoes, so the veto material, the vote values and the approval
definitions come from the ASF voting process page and the release policy. Those
are Foundation policy rather than Incubator practice, and the lesson says which
is which. Note for anyone revising it: the Incubator's PPMC guide and the
incubation policy word the binding-vote question differently, and incubation
policy governs, since it states that it takes precedence where other documents
differ.

Lesson 7's three wiki pages describe practice, and incubation policy says almost
nothing on the subject: one line about adding PPMC members, which is a pointer
to the Incubator's PPMC guide, and nothing at all about adding committers. So
the lesson is cross-checked against that guide and teaches the whole sequence as
what podlings do rather than as what they must do. Two things for anyone
revising it. The public acceptance on `dev@` comes from the wiki alone, not from
the guide or policy, so it is taught as strong practice rather than as a rule.
And "majority approval" is a defined ASF term meaning at least three binding
`+1` votes, while the voting page also calls procedural votes simple majority,
so the threshold for a vote on a person is genuinely unsettled and the lesson
says so instead of picking one.

Lesson 8 has a constraint no other lesson has. The Reporting Guide requires
reports to be written by humans and names AI-generated text as something to
leave out, so the tutor is told several times that it must not draft, polish or
ghostwrite any part of a real report, and its exercises use invented podlings
for that reason. It also draws on the live monthly report page as well as the
guide, because the guide's list of sections and the page's actual headings are
related but not the same, and the page carries the formatting rules and the real
dates.

Lesson 5 has only one wiki guide behind it, so it also draws on the
Infrastructure team's own pages for the setup sequence and on the incubation
policy for what a podling may set up. It is the lesson most exposed to things
moving, so it teaches the routing question and the etiquette rather than portal
menus, and points at `infra.apache.org` and `selfserve.apache.org` for anything
current. Committer onboarding, reporting, releases and the disclaimer wording
are named but handed on to Lessons 7, 8, 10 and Track D.

## Track C: Legal, branding and IP

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 9 | Legal basics: licences, ICLAs, provenance | Legal Basics, Licensing and Provenance | **Done** |
| 10 | Names, trademarks and branding | Naming and Trademarks, Naming and Branding, Third-Party Branding and Incubating Projects, Graduation Identity | **Done** |
| 11 | Privacy and data handling | Privacy and Data Handling | **Done** |

Track C draws more on Foundation documents than on Incubator guides, because the
rules here are ASF-wide. Lesson 9 works from ASF Legal's third-party licensing
policy, the contributor agreements page, the IP clearance pages and the release
policy; Lesson 10 from the trademark policy, the project branding requirements
and the naming process; Lesson 11 from the privacy policy for project websites
and the committers' privacy FAQ. Incubation policy is silent on most of Lesson
9's subject, which the lesson says rather than leaving a learner to look for a
rule that is not there.

Track D follows.

## Track D: Releases

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 12 | Anatomy of a podling release | Releases | **Done** |
| 13 | Running a release vote | Release Votes, Release Vote Insights, Release Review Issues | **Done** |
| 14 | Announcing and distributing | Release Announcements | **Done** |

Track D also leans on Foundation and Infrastructure documents rather than
Incubator guides, because the release rules are ASF-wide. Lesson 12 works from
the release policy, the release distribution policy and Infra's signing and
publishing pages; Lesson 13 from the ASF voting process page, the release policy
and the Incubator cookbook; Lesson 14 from the release download pages policy,
the distribution policy and the Incubator publicity guide. Incubation policy
supplies everything podling-specific in all three, and each lesson says where a
Foundation page and an Incubator guide pull in different directions rather than
picking one quietly.

The next lesson is 15, which begins Track E.

## Track E: Mentoring

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 15 | What a mentor actually does | Incubator Mentor Quick Start Guide, Mentor Onboarding, Mentor Handbook | **Done** |
| 16 | Reading the signals | Common Red Flags, Measuring Podling Health, Mentor Engagement Patterns, Best Practices for Mentors | **Done** |
| 17 | Difficult conversations | Mentors Tough Conversation Guide | **Done** |
| 18 | Mentor lifecycle: selection, replacement, offboarding | Select Your Mentors, Mentor Replacement, Mentor Offboarding | **Done** |

Track E is the first track written for mentors rather than podling members,
which changes the hard rule in every lesson: the tutor teaches the judgement and
refuses to exercise it. Lesson 15 works from the mentor quick start, onboarding
and handbook pages; Lesson 16 from the red flags sheet, the health and
engagement analyses and Best Practices; Lesson 17 from the Tough Conversation
Guide; Lesson 18 from Select Your Mentors, Mentor Replacement and Mentor
Offboarding, with the PPMC and Mentors' guides for the mechanics the wiki pages
do not carry.

## Track F: IPMC oversight

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 19 | The IPMC's job | Incubator PMC Onboarding, IPMC Governance, IPMC Reflection and Oversight | Planned |
| 20 | Vendor neutrality | Vendor Neutrality, Neutrality In Practice | Planned |
| 21 | Edge cases and judgement calls | Edge Cases, Incubator Case Studies, An Incubator Learns | Planned |

## Track G: Graduation and exit

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 22 | Graduation criteria and readiness | Graduation Criteria, Graduation Readiness | Planned |
| 23 | The graduation vote and the initial PMC | Graduation Votes, Selecting a PMC Chair, Selecting the Initial PMC at Graduation | Planned |
| 24 | Life after, and the other exit | Graduation and Beyond, Retiring Podlings | Planned |

## Track H: Data and trends

Optional, and better suited to IPMC members and experienced mentors than to
newcomers.

| # | Lesson | Source pages | Status |
|---|---|---|---|
| 25 | Ten years of the Incubator | 10 years of the Incubator, 10 Years Summary, Governance Patterns, Podling Governance Patterns, Community and Governance Growth, Incubator Discussion Trends, Mentor Trends, Incubator Health | Planned |
| 26 | Using emerging technology | Using Emerging Technology | Planned |

## Coverage

Every guide a lesson draws on is used by exactly one lesson, with none used
twice. Not every guide in `resources.yml` feeds a lesson.

[SOURCES.md](SOURCES.md) has the mapping the other way round, source by source,
with themes and links.

## Open questions

- **Lesson 25 wraps eight data guides** and is closer to a seminar than a
  lesson. It may be worth splitting, or leaving as a reading list rather than a
  tutored lesson.
- **Lesson 24 can assume retirement is known.** Lesson 1 introduces retirement
  as a normal outcome, so 24 can go straight to how it works.

## Licence

Licensed under the Apache License, Version 2.0.
<https://www.apache.org/licenses/LICENSE-2.0>
