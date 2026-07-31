# Incubator Concierge

An AI skill that acts as a front door for questions about the Apache
Incubator, for anyone asking: podling contributors, mentors, IPMC members, ASF
newcomers, and people just curious how incubation works.

It is a routing layer, not a data source. The evidence comes from the Incubator
MCP servers; this skill decides which one answers a given question, and pitches
the answer at whoever is asking.

## Layout

```
concierge/
├── SKILL.md                   Skill body: question triage, audience, answer rules
├── references/
│   ├── routing.md             Lane-by-lane routing, tool names, parameters, limits
│   └── examples.md            Worked answers across audiences, incl. the traps
├── evals/
│   ├── content.json           Static regression assertions (no model)
│   ├── behaviour.json         Routing, traps and register, through real prompts
│   ├── triggering.json        Does the skill fire on the right prompts
│   └── README.md              How the suites and grading work
├── scripts/
│   ├── validate_skill.py      Pre-package checks
│   ├── eval_lib.py            Grading engine (pure, model-free)
│   ├── run_evals.py           Suite runner via the claude CLI
│   └── self_test_evals.py     Tests for the grader itself
└── Makefile
```

## Build

```bash
make validate   # frontmatter, description length, references, excluded sources
make package    # -> build/incubator-concierge.skill
```

The resulting `.skill` file is a zip containing a single top-level
`incubator-concierge/` directory. Deliver it to a AI session to install it.

## Test

```bash
make check          # validate + grader self-test + static regressions. No model, free.
make evals          # behaviour suite (routing, traps, register) — needs `claude` on PATH
make evals-trigger  # triggering suite
make evals-all
```

`make check` is the pre-commit gate: it needs no model, costs nothing, and every
case in the static suite corresponds to a defect that was actually found while
building the skill. `make evals` is the one that catches behavioural regressions
but costs tokens and takes a few minutes.

See `evals/README.md` for how grading works and how to add cases.

## Design notes

**Normative vs empirical.** The skill's central rule is to decide whether a
question is about the rules ("what must a DISCLAIMER say") or about current state
("is Foo still incubating"), because answering one with the other is the most
common way to be confidently wrong. Most real questions are a mix, and are
handled by getting the rule first, then the evidence, then stating how they line
up.

**Audience shapes register, not facts.** The same fact is delivered differently
to a newcomer, a contributor, and an IPMC member. Sending oversight vocabulary
("watchlist", "risk severity") to a first-time contributor reads as a complaint
being filed about their project.

**Status gating.** Any podling-scoped question resolves the project's name and
`status` before answering. Several tools will happily answer about a project that
graduated or retired years ago — `get_report_due_dates()` takes no podling
argument at all, so it returns valid Incubator cycle dates for a top-level
project.

**Handoff to `ipmc`.** Sustained oversight work belongs to the `ipmc` skill,
which encodes calibration this one does not. The concierge hands off rather than
reimplementing it.

## Relationship to other tooling

- The `ipmc` skill and the IPMC MCP server remain the oversight specialists.
- This skill deliberately does **not** route to the `book` MCP; that source is
  not public, and `make validate` fails if it is reintroduced.
- Anything with a legal edge — trademark disputes, licence calls, individual CLA
  problems — gets the policy plus the right ASF contact address, never an
  adjudication.

## Maintenance

The routing reference records tool quirks found by testing against the live
servers, including several cases where two servers export the same tool name and
return different data. When a source MCP changes a tool name, parameter, or
output shape, update `references/routing.md` in the same change — a stale routing
table sends the skill to a plausible answer built on the wrong data.

When you fix a real defect, add a case for it. The static suite is cheap enough
that there is no reason to rely on remembering. Guard rails added this way so far
cover the `get_policy` parameter name, the podling status gate, the complete set
of release deltas, and the excluded source.
