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

`contains_any` exists because a correct answer often has several acceptable
phrasings — "graduated", "is now a top-level project" — and pinning one exact
wording tests phrasing rather than behaviour.

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
