# Incubator AI Tutors

Interactive tutor prompts for the Apache Incubator training material, one file
per lesson. Each file turns a capable chat model into a tutor for a single
lesson: it teaches the material one idea at a time, runs the exercises, and
grades the learner's answers against the lesson's answer keys.

These are built from the Incubator guides on the [Incubator
wiki](https://cwiki.apache.org/confluence/display/INCUBATOR/). The wiki pages
remain the reference; a tutor adds structure on top of them, so a learner can
work through a topic with someone to answer back rather than only reading.

## How to use one

Each file has two parts, split by a `---` line:

- Everything **above** the line is notes to you: what the lesson covers and how
  it was built. It is not sent to the model.
- Everything **below** the line is the tutor. Send it as the system prompt.

So the one rule is: **paste everything below the `---` into a model as the
system prompt, then chat normally.** The learner answers the tutor's opening
questions and it takes over from there.

Where the system prompt goes, by tool:

Times in the table below are for a full run, covering the teaching, the
exercises and the self-check. They assume someone new to the ASF; anyone who
already knows the material will be quicker, and the tutors are told to speed up
rather than pad when a learner is answering well.

| Tool | Where to put it |
|---|---|
| claude.ai, ChatGPT | Paste it as your first message in a new chat. Not a true system prompt, but it behaves the same for one session. |
| claude.ai Projects | Paste it into the Project's custom instructions. Every chat in that Project is then the tutor, and learners never see the prompt. |
| Open WebUI | Workspace > Models > new model, pick a base, paste it into the System Prompt field, save. It appears in the model dropdown with the prompt already loaded and out of the learner's reach. |
| API | Pass it as the `system` parameter; the learner's turns are `messages`. |

## Lessons

| Lesson | Track | Covers | Time |
|---|---|---|---|
| [1. What the Incubator is, and whether you want it](lesson-01-what-the-incubator-is.md) | A, Foundations | What a podling is, stewardship rather than sponsorship, who does what, when a project is not ready, the common misconceptions, and what happens if a podling does not make it. | ~30 min |
| [2. The Apache Way, in practice](lesson-02-the-apache-way-in-practice.md) | A, Foundations | Why a foundation with no managers needs governance, the four values in practice, how a decision gets built by discussion and recorded by a vote, the bureaucracy objection, and the patterns that quietly erode all of it. | ~35 min |
| [3. Working in public: lists, tone, culture, time zones](lesson-03-working-in-public.md) | A, Foundations | Why messages land wrong when nobody meant them to, what silence does and does not tell you, English as the working language, deciding across time zones, which channel for what, and what the code of conduct asks. | ~35 min |
| [4. From proposal to podling](lesson-04-from-proposal-to-podling.md) | B, Podling startup and PPMC | What goes in a proposal, describing a community truthfully, what makes an initial committer list credible, writing Known Risks honestly, what reviewers ask, and what "not yet" means. | ~40 min |
| [5. Getting set up with Infra](lesson-05-getting-set-up-with-infra.md) | B, Podling startup and PPMC | What ASF Infrastructure does and what the project does, choosing between self-serve, a ticket, the roster tools and a private security address, writing a request that works, and what a mentor should hand over. | ~30 min |
| [6. How decisions get made: lazy consensus, votes, vetoes](lesson-06-how-decisions-get-made.md) | B, Podling startup and PPMC | When a decision needs no vote, a discussion, or a formal vote; who casts binding votes and where; the two-stage podling release vote; what a veto is and is not; and how to run and close a vote. | ~35 min |
| [7. Growing committers and the PPMC](lesson-07-growing-committers-and-the-ppmc.md) | B, Podling startup and PPMC | What separates a committer from a PPMC member, how to decide who to invite and how to tell when a bar has drifted, both addition processes and where each step happens, the awkward cases, and why committer growth is what graduation reads. | ~30 min |
| [8. Writing a report the IPMC can use](lesson-08-writing-a-report-the-ipmc-can-use.md) | B, Podling startup and PPMC | Who reads a podling report and what they look for, what belongs in each section, facts that mean something versus statistics that do not, reporting a bad month honestly, the submission mechanics, and what happens when a report is late or missed. | ~30 min |

Twenty-six lessons are planned across eight tracks: Foundations, podling startup
and PPMC, legal and branding, releases, mentoring, IPMC oversight, graduation
and exit, and data and trends. See [ROADMAP.md](ROADMAP.md) for the full list
and what is built so far, and [SOURCES.md](SOURCES.md) to go the other way, from
an Incubator guide to the lesson that teaches it.

## Writing a new one

[PLAN.md](PLAN.md) covers how a lesson gets built: which sources to trust for
what, the traps that produced wrong statements in the first draft of Lesson 1,
and the writing rules the prompts follow.

## Notes

- **Model choice matters.** These prompts ask the model to hold a multi-step
  teaching flow, withhold answers until the learner attempts them, and grade.
  Hosted models follow that reliably. Small local models are fine for testing
  but less dependable with real learners.
- **Self-contained.** Each prompt embeds the teaching content it needs, so it
  requires no web access and refers to no external paths. The wiki guides behind
  them change slowly, so this needs little upkeep. If one is substantially
  rewritten, update the lesson that draws on it.

## Licence

Licensed under the Apache License, Version 2.0.
<https://www.apache.org/licenses/LICENSE-2.0>
