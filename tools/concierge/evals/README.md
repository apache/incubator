# Evals

Three suites, in increasing cost:

| Suite | Model? | What it grades |
| --- | --- | --- |
| `content` | no | Static assertions over the skill files |
| `triggering` | yes | Whether the skill fires on real phrasings and stays quiet on near-misses |
| `behaviour` | yes | Whether answers route correctly, avoid the traps, and match the register |

```bash
make evals-self-test    # prove the grader works — no model, no cost
make evals-content      # static regressions — no model, no cost
make evals              # behaviour, needs `claude` on PATH
make evals-trigger      # triggering
make evals-all
```

Filter to one area while iterating:

```bash
python3 scripts/run_evals.py --suite behaviour --filter status-gate --jobs 1
python3 scripts/run_evals.py --suite behaviour --filter high-value --no-judge
```

Reports land in `evals/results/<suite>.md` and `.json` (gitignored).

## The suites

**`content.json`** is the one to wire into CI. Every case corresponds to a defect
that was actually found while building the skill, so a failure means a known-bad
state has come back — the `get_policy(id=)` parameter error, the missing status
gate, a stale hardcoded podling count, the excluded `book` source reappearing.
It is free and instant, so there is no reason not to run it on every change.

**`triggering.json`** grades the `description` frontmatter, not the skill body.
The negatives are deliberately near-misses that share vocabulary with the skill
but need something else: a lab incubator that won't hold temperature, booking a
call with a mentor, turning a podling report into a Word document. An obviously
irrelevant negative tests nothing. Note that Claude consults skills for
substantive work and often handles trivial one-step asks directly, so the
positives are written with realistic detail rather than as bare keywords.

**`behaviour.json`** is where the real defects have been. The highest-value cases
are the traps: a retired podling, a graduated project, an old proposal name, a
question that looks like it wants a date. Tagged `high-value` — run those first
when short on time.

## Grading

Deterministic assertions handle facts. The vocabulary is `contains`,
`not_contains`, `contains_any`, `matches`, `not_matches`; all are
case-insensitive and whitespace-folded so they survive line wrapping.

**Which layer gets which job.** Deterministic assertions are for things with a
canonical form: a project name, an email address, a filename, a path, a term of
art, a number. Plus every `not_matches` trap, which encodes a specific wrong
claim and stays stable because wrong claims have a shape.

Everything semantic belongs to the judge. "Did it ask which podling", "did it
correct the premise", "did it decline to adjudicate" have unlimited valid
phrasings, and matching strings against free prose tests wording rather than
behaviour.

The warning sign is extending a `contains_any` list because a good answer used a
phrasing you had not listed. That means the assertion is in the wrong layer.
Delete it and write a judge criterion — do not add the phrasing. A suite tuned
that way converges on whatever the model said last, stops failing, and therefore
stops catching anything.

`contains_any` still has a narrow use: several canonical tokens where any one
would do, such as an identifier that might appear qualified or bare.

**Watch for negation.** A `not_matches` pattern looking for "Kafka must …
DISCLAIMER" happily matches "Kafka must **not** include a DISCLAIMER", which is
the correct answer. The patterns here use tempered repetition — `(?:(?!\bnot\b|n't)[^.]){0,60}` — so no negation can sit between the subject and the
claim. If you add a pattern asserting someone said something wrong, always test
it against the correctly-negated form too.

The `not_matches` patterns are the sharp end: they encode the specific wrong
answer, not the absence of a right one. `no-graduation-timeline` fails on
"should graduate in about 18 months" and on "expect graduation by mid-2027", but
passes "Toree has been incubating for 127 months, and graduation is assessed
against criteria" — a sentence that pairs a month count with the word graduation
yet is entirely correct. Getting that boundary right is why the grader has its
own tests.

An **LLM judge** covers what regexes cannot: whether the register suited the
audience, whether the answer showed restraint, whether it declined to adjudicate.
Judged criteria are advisory by default — judges vary run to run, and a flaky red
build gets ignored. Pass `--judge-fatal` to make them binding, or `--no-judge` to
skip them.

The judge is told to **default to failing when uncertain**, because a lenient
judge is worse than no judge: it reports green on bad answers.

**Never quote the passing answer into the criterion.** When a good answer fails,
the tempting fix is to add "phrasing X satisfies this" — but a judge handed the
winning wording is pattern-matching, not judging, and the criterion stops
generalising to answers phrased any other way. State the principle and the
reason it matters instead. Naming what *failure* looks like is safer than naming
what success looks like: rejecting vagueness generalises, blessing one sentence
does not.

## Adding a case

Add to the relevant JSON file, then run `make evals-self-test` — it checks every
case has grading attached, ids are unique, and the triggering set stays balanced.

Write assertions against the *behaviour*, not the wording. Before adding a
`not_matches` pattern, write down the bad answer you are trying to catch and the
good answer that must still pass, then check both. `self_test_evals.py` has
fixtures for exactly this; extending it when you add a tricky pattern is cheap
insurance against a guard that silently never fires.

## Limitations

- Triggering detection scans the transcript for a structural skill invocation and
  deliberately ignores the answer prose, so a reply that merely mentions the
  skill name is not counted. It depends on the CLI's event shape, so verify it
  reports sensibly after a Claude Code upgrade.
- The behaviour suite talks to live MCP servers. Cases assert on lifecycle facts
  (Annotator retired, Iceberg graduated, Hunter renamed to Otava) that are stable
  history, but a case asserting on current health data would go stale.
- Runs are not deterministic. A single failure is worth re-running before
  treating it as a regression.
