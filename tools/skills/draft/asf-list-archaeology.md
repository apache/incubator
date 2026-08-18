---
name: asf-list-archaeology
description: Answers "why does the ASF do it this way?" questions by reading the mailing list archives directly — the rationale behind a policy, when a rule changed and who argued which way, whether a topic has come up before, what happened to an old proposal. Use this whenever someone asks about the history, origin, or reasoning behind an ASF or Incubator practice, or asks to find an old discussion, even if they don't mention mailing lists. Ranked keyword search over lists.apache.org answers these badly — the decisive thread is usually old, and its subject line rarely contains the words people search for. Requires the incubator-mail MCP.
---

# ASF list archaeology

## What this is for

Questions like "why must podling releases carry a DISCLAIMER?", "when did we
start requiring three IPMC votes?", "has anyone proposed dropping the monthly
report?" have answers in the archives, but ordinary search does not find them.

Search ranks by term match and recency, so it returns messages where a rule is
*applied* — recent release votes, recent report threads. The message where the
rule was *argued* is fifteen years old and its subject line says something like
"Corporations and the incubator". No amount of query tuning surfaces it.

What works instead: cut the corpus down by list and date range using a cheap
term filter, then actually read what comes back. The filter needs recall, not
precision — 200 messages is a comfortable read, and the reasoning is visible on
the page once you have them.

## Procedure

**1. Expand the question into term variants.**

Take the question's central concept and list the words the mailing list would
have used for it, including the ones that have gone out of fashion. Old threads
use old vocabulary: what is now a "podling" was once an "incubating project";
"DISCLAIMER" may appear as "disclaimer", "incubating notice", or "branding".
Aim for three to six variants covering the distinct ways people would phrase it.

This step is what determines whether the whole thing works. Spend real thought
on it.

**2. Pick the window.**

Guess where the discussion happened and go wide around it. Policy is usually
argued years before it settles into the documentation, so if a rule is in
today's policy, look at when the practice was young. A three-year window is
cheap: 36 months of one list on a reasonably specific term is typically a few
hundred messages and under a minute.

If you have no idea when, sweep in three-year blocks from the list's start
rather than trying to pick one window cleverly.

**3. Cache the mboxes.**

Use the incubator-mail MCP's mbox caching tools — `cache_incubator_general_mboxes`
for general@incubator, `cache_podling_mboxes` for a podling list — with
`start_month`, `end_month` and `header_body` set to one term variant. Run it once
per variant and take the union.

The response gives you `cache_dir` and a per-month message count. Use the
returned path rather than assuming one.

**4. Thread and read.**

Run `scripts/thread_mbox.py` against the cache directory to group messages into
threads and print them oldest first. Then read them — this is the part that
cannot be delegated to a filter.

Threads with `[VOTE]`, `[RESULT]` or `[REPORT]` subjects are usually the rule
being applied, not decided. Skim them and spend your attention on ordinary
prose subjects, which is where arguments happen.

**5. Cite properly.**

Every claim needs a permalink. To get one, call `search_incubator_general_mail`
with `timespan` set to the message's month (`YYYY-MM`) and the thread subject as
the query — month-scoped search is precise once you already know what you are
looking for. Take the `permalink` field.

Quote people directly and briefly. The value of this work is that it shows what
was actually said, so paraphrase loses most of it.

## Reporting the answer

Give the finding, the evidence, and the shape of the disagreement — most
policies exist because somebody objected and somebody else prevailed, and the
objection is usually the interesting part.

State the search that produced it: lists, window, terms, message count. Someone
should be able to repeat or contradict your work.

## The failure mode worth naming

If the term variants miss the vocabulary the discussion actually used, the
filter returns nothing and you have no way to tell that from a topic that was
never discussed. An empty result is not evidence of absence.

When you come up dry, say so explicitly, list the terms you tried, and treat it
as unresolved rather than answered. Then widen — more variants, longer window,
a different list — before concluding anything. Where a discussion probably
happened on a list you haven't checked (board@, legal-discuss@, a project's own
dev@), say which one and why.

Recall here is unmeasured and probably imperfect. Anyone relying on this should
know that they are seeing what the filter caught, not everything that exists.

## Cost

A three-year window on one term is roughly 200 messages, 1 MB, under a minute,
and no infrastructure beyond the MCP. Widening is cheap, so widen freely rather
than agonising over the perfect first query.