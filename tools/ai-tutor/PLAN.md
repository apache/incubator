# Plan

How a lesson in this directory gets made, and which sources to trust for what.

[README.md](README.md) covers what these are and how to run one.
[ROADMAP.md](ROADMAP.md) lists the lessons and their state.

## Sources

Six sources feed this material and they are not interchangeable. Most of the
mistakes made while writing Lesson 1 came from asking the wrong one.

| Source | Good for | Do not use it for |
|---|---|---|
| [`tools/seealso/resources.yml`](../seealso/resources.yml) | Finding out what teaching material exists. 91 resources, 63 of them Incubator wiki guides, tagged by theme and topic. | Nothing much. This is the index, start here. |
| [Incubator wiki guides](https://cwiki.apache.org/confluence/display/INCUBATOR/) | The teaching content itself: explanations, examples, patterns drawn from real discussions. | Settling a question of what is required. These pages summarise practice and say so. |
| [Incubation Policy](https://incubator.apache.org/policy/incubation.html) | What is actually required, where it covers a topic: reporting, disclaimers, releases, podling constraints, termination. | Anything it does not mention. It has no section on mentors at all, so silence there means "look in a guide", not "no rule exists". |
| Incubator guides: [roles and responsibilities](https://incubator.apache.org/guides/roles_and_responsibilities.html), [mentor](https://incubator.apache.org/guides/mentor.html), [graduation](https://incubator.apache.org/guides/graduation.html), [ppmc](https://incubator.apache.org/guides/ppmc.html), [release management](https://incubator.apache.org/guides/releasemanagement.html) | Roles, who votes on what, process detail. | Assuming a guide is policy. Cite it as a guide. |
| [ASF Legal](https://www.apache.org/legal/resolved.html) | Anything about licences and what may be distributed. | Nothing else. |
| `podlings.xml`, via the podlings MCP | What has actually happened: how long podlings took, how many graduated, mentor counts. | Working out what is normal or healthy. See the trap below. |

Beyond all of those sits the IPMC, and Incubator practice that is real but
unwritten. When a question is about what the Incubator expects rather than what
a document says, ask a person. That is not a fallback, it is the correct source.

## Traps

Each of these produced a wrong statement in the first draft of Lesson 1.

**Data answers "what happened", not "what is healthy".** The median time to
graduation across podlings since 2015 is about 20 months, but that distribution
is dragged out by podlings that struggled. A healthy incubation runs about a
year. The numbers describe community health, not a timetable, and reading them
as a timetable produced three wrong answers in a row.

**Absence from policy does not mean a claim is wrong.** Much of how the
Incubator works is expectation rather than rule. Three mentors is a good number
with no policy behind it. A first release within roughly six months of entry is
a genuine expectation with no policy behind it. Neither is an error in the
material that states it.

**Checking a claim against a source only catches errors the source does not
share.** The first draft said incubation cannot fix a licensing problem, which
survived a full fact-check because the wiki says something similar. It is wrong:
authors can be asked to relicense, and incompatible parts can be removed or
swapped, and podlings do this during incubation with mentors helping.

**Three strengths of claim, and they are not interchangeable.** Policy is
written and enforced, so say "must". An expectation is what the Incubator looks
for and acts on, so say "expected" and say nothing automatic follows from
missing it. Good practice is what tends to work, so say "usually" or "a good
number". Deciding which one you are looking at is most of the work.

## Building a lesson

1. **Scope it.** Take the lesson and its source pages from
   [ROADMAP.md](ROADMAP.md), and check [SOURCES.md](SOURCES.md) for anything
   else that touches the same ground. Read all of them in full before writing
   anything. If you add a source that is not in `resources.yml`, record it in
   SOURCES.md and be sure it belongs: an unchecked addition is what made the
   dropped "who does what" lesson incoherent.
2. **Decide the level, and write it down first.** Who is this for, what do they
   already know, and which of the detail belongs to a later lesson? This becomes
   the `Pitch` section at the top of the prompt, and everything else follows
   from it.
3. **Draft the teaching text**, then the exercises, then the answer keys. The
   exercises are the part that decides whether the lesson is any good, so give
   them the most thought.
4. **Fact-check** the draft against the policy and guides above, and against ASF
   Legal for anything touching licences. An adversarial pass here found a wrong
   answer key in Lesson 1 that nothing else would have caught.
5. **Re-read the whole thing against the audience.** This step is not optional.
   Fact-checking pushes a draft toward precision, and precision at the wrong
   level is its own failure. Lesson 1 drifted from an introduction into IPMC
   reference material exactly this way, one defensible correction at a time.
6. **Test it** by running the prompt against a few learner types: someone
   expecting the ASF to promote their project, someone certain their prototype
   is ready, someone who just wants the rules. Watch whether it holds the level
   under pressure.

## Writing rules

- **Pitch to the audience and say so in the prompt.** Every lesson opens with a
  `Pitch` section telling the model what level to teach at and what to leave to
  later lessons. Foundations lessons assume no knowledge of the ASF at all.
- **Answer direct questions, but do not build the lesson around rules.** A
  learner who asks how many votes a release needs should get a straight answer
  and then be brought back to the lesson. Each prompt carries a short
  `Reference, for direct questions only` section for this, marked
  do-not-teach-from. Refusing to answer is worse than a brief digression.
- **Do not turn good practice into rules.** Keep the hedges. Tell the model to
  say when it is unsure rather than inventing a threshold, and not to leave a
  learner holding a number.
- **Check questions must use the idea.** Ask the learner to apply it to their
  own situation or someone else's. Do not ask them to spot the odd one out,
  group things into categories, or work out which two are in tension. Those test
  how the material was organised rather than the subject, and a learner can only
  answer by guessing what the author had in mind. If a question would still make
  sense with the Incubator swapped for any other subject, it is the wrong
  question.
- **Do not read lists out.** After a list-shaped section, tell the model to take
  the two or three items most relevant to whoever is in front of it.
- **One file per lesson**, self-contained, carrying its own teaching text,
  exercises and answer keys. Nothing to keep in step with anything else.
- **No em dashes.** Commas, colons and full stops.

## Licence

Licensed under the Apache License, Version 2.0.
<https://www.apache.org/licenses/LICENSE-2.0>
