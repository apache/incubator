#!/usr/bin/env python3
"""Exercise the eval machinery without calling a model.

This proves the grading engine itself is correct, which matters because a buggy
grader is worse than no grader: it reports green on bad answers. Each fixture
below is a deliberately good or bad answer, and the test asserts the grader
reaches the expected verdict.

    python3 scripts/self_test_evals.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (  # noqa: E402
    build_judge_prompt,
    detect_skill_use,
    extract_json,
    grade_assertions,
    grade_judge_reply,
    load_suite,
    render_report,
    select_cases,
)
from run_evals import extract_answer, run_content_suite  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"

failures: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}" + (f" — {detail}" if detail else ""))
        failures.append(label)


def case_by_id(suite: dict, case_id: str) -> dict:
    for case in suite["cases"]:
        if case["id"] == case_id:
            return case
    raise KeyError(case_id)


# --------------------------------------------------------------------------- #
print("\n[1] suites load and have unique ids")
# --------------------------------------------------------------------------- #

suites = {}
for name in ("content", "behaviour", "triggering"):
    suite = load_suite(EVALS / f"{name}.json")
    suites[name] = suite
    check(f"{name}.json loads ({len(suite['cases'])} cases)", len(suite["cases"]) > 0)

for case in suites["behaviour"]["cases"]:
    has_grading = bool(case.get("assertions")) or bool(case.get("judge"))
    check(f"behaviour/{case['id']} has grading", has_grading, "no assertions and no judge criteria")

for case in suites["triggering"]["cases"]:
    check(f"triggering/{case['id']} declares should_trigger", "should_trigger" in case)

positives = sum(1 for c in suites["triggering"]["cases"] if c["should_trigger"])
negatives = len(suites["triggering"]["cases"]) - positives
check(f"triggering is balanced ({positives} pos / {negatives} neg)", positives >= 6 and negatives >= 6)

# --------------------------------------------------------------------------- #
print("\n[2] deterministic grader accepts a good answer")
# --------------------------------------------------------------------------- #

retired_case = case_by_id(suites["behaviour"], "status-gate-retired-podling")
good_retired = (
    "Annotator isn't a podling any more — it retired from the Incubator on 2025-08-11 "
    "after about nine years, so no Incubator report is ever due for it. If you meant a "
    "different project, tell me which one and I'll look up its cycle."
)
def why(checks_: list) -> str:
    return "; ".join(f"{c.name}: {c.detail}" for c in checks_ if not c.passed)


checks = grade_assertions(good_retired, retired_case["assertions"])
check("good retired answer passes all assertions", all(c.passed for c in checks), why(checks))

# --------------------------------------------------------------------------- #
print("\n[3] deterministic grader catches the actual failure mode")
# --------------------------------------------------------------------------- #

bad_retired = (
    "Annotator's next report is due on 2026-08-05, two weeks before the board meeting. "
    "Reports go on the wiki and need a mentor sign-off."
)
checks = grade_assertions(bad_retired, retired_case["assertions"])
check("bad retired answer fails", any(not c.passed for c in checks))
check(
    "failure is attributed to the due-date pattern",
    any(not c.passed and "does not match" in c.name for c in checks),
)

# --------------------------------------------------------------------------- #
print("\n[4] graduation-timeline guard rejects a hedged date")
# --------------------------------------------------------------------------- #

grad_case = case_by_id(suites["behaviour"], "no-graduation-timeline")
hedged = (
    "Based on typical patterns Toree should graduate in about 18 months, though the criteria "
    "matter more than the timeline."
)
checks = grade_assertions(hedged, grad_case["assertions"])
check("hedged duration is rejected", any(not c.passed for c in checks))

criteria_only = (
    "Graduation isn't time-based, so there's no date to give. It's assessed against criteria: "
    "community independence, release maturity and sustained activity are currently weak for Toree, "
    "while governance health looks strong. The IPMC votes and the board decides."
)
checks = grade_assertions(criteria_only, grad_case["assertions"])
check("criteria-based answer passes", all(c.passed for c in checks))

# --------------------------------------------------------------------------- #
print("\n[5] trademark guard rejects an implied approval")
# --------------------------------------------------------------------------- #

tm_case = case_by_id(suites["behaviour"], "trademark-no-adjudication")
approving = (
    "The automated checks found no ASF conflicts, so the name is fine to use. "
    "You should still file a PODLINGNAMESEARCH ticket and email trademarks@apache.org."
)
checks = grade_assertions(approving, tm_case["assertions"])
check("'the name is fine' is rejected despite correct routing", any(not c.passed for c in checks))

restrained = (
    "Automated checks found no ASF project conflicts, but that is a pre-check and not approval. "
    "A collision in the same technical space is exactly what the PODLINGNAMESEARCH process and "
    "trademarks@apache.org exist to assess — raise it there before the name is attached to a proposal."
)
checks = grade_assertions(restrained, tm_case["assertions"])
check("restrained answer passes", all(c.passed for c in checks))

# --------------------------------------------------------------------------- #
print("\n[6] newcomer register guard rejects a metrics table")
# --------------------------------------------------------------------------- #

newcomer_case = case_by_id(suites["behaviour"], "newcomer-register")
tabled = "A podling is an incubating project.\n\n| Podling | Commits | Severity |\n| --- | --- | --- |\n| Toree | 2 | high |"
checks = grade_assertions(tabled, newcomer_case["assertions"])
check("markdown table is rejected for a newcomer", any(not c.passed for c in checks))

prose = (
    "A podling is a project going through the Apache Incubator, the ASF's onboarding path for "
    "projects that want to become full Apache projects. See "
    "https://incubator.apache.org/policy/incubation.html"
)
checks = grade_assertions(prose, newcomer_case["assertions"])
check("plain prose passes", all(c.passed for c in checks))

# --------------------------------------------------------------------------- #
print("\n[6b] negation is not mistaken for the claim it denies")
# "must not include a DISCLAIMER" is the correct answer and once failed this case,
# because a naive pattern matched the "must" inside "must not".
tlp_case = case_by_id(suites["behaviour"], "tlp-does-not-need-disclaimer")
for bad in [
    "Kafka must include a DISCLAIMER in its releases.",
    "Apache Kafka has to ship a DISCLAIMER file with each release.",
    "Yes, Kafka is required to include a DISCLAIMER.",
]:
    checks = grade_assertions(bad, {"not_matches": tlp_case["assertions"]["not_matches"]})
    check(f"catches wrong claim: {bad[:45]}…", any(not c.passed for c in checks))
for good in [
    "Kafka release still must not include a DISCLAIMER",
    "Kafka does not need to include a DISCLAIMER.",
    "Kafka must never ship a DISCLAIMER now that it is a TLP.",
    "Kafka is a top-level project. Podlings must include a DISCLAIMER in every release.",
]:
    checks = grade_assertions(good, {"not_matches": tlp_case["assertions"]["not_matches"]})
    check(f"allows correct answer: {good[:45]}…", all(c.passed for c in checks))

print("\n[7] judge reply parsing")
# --------------------------------------------------------------------------- #

criteria = [
    {"id": "corrects-premise", "requirement": "states it is retired"},
    {"id": "no-invented-obligation", "requirement": "does not invent a deadline"},
]

prompt = build_judge_prompt("When is Annotator's report due?", good_retired, criteria)
check("judge prompt names both criteria", all(c["id"] in prompt for c in criteria))
check("judge prompt demands JSON only", "JSON only" in prompt)

clean = json.dumps({"criteria": [{"id": c["id"], "passed": True, "evidence": "quote"} for c in criteria]})
checks = grade_judge_reply(clean, criteria)
check("clean judge reply parses to 2 passes", len(checks) == 2 and all(c.passed for c in checks))
check("judge checks are flagged as judged", all(c.judged for c in checks))

chatty = 'Sure! Here is my grading:\n```json\n{"criteria": [{"id": "corrects-premise", "passed": false, "evidence": "no mention"}, {"id": "no-invented-obligation", "passed": true, "evidence": "ok"}]}\n```\nHope that helps.'
checks = grade_judge_reply(chatty, criteria)
check("prose-wrapped JSON is still parsed", len(checks) == 2)
check("mixed verdicts are preserved", [c.passed for c in checks] == [False, True])

checks = grade_judge_reply("I could not grade this, sorry.", criteria)
check("unparseable judge reply fails closed", len(checks) == 2 and not any(c.passed for c in checks))

checks = grade_judge_reply(json.dumps({"criteria": [{"id": "corrects-premise", "passed": True}]}), criteria)
check("missing verdict fails closed", sum(1 for c in checks if not c.passed) == 1)

check("nested-brace JSON extraction works", (extract_json('noise {"a": {"b": "}"}, "c": 1} tail') or {}).get("c") == 1)

# --------------------------------------------------------------------------- #
print("\n[8] answer extraction from CLI output shapes")
# --------------------------------------------------------------------------- #

check(
    "plain json output",
    extract_answer(json.dumps({"type": "result", "result": "the answer"})) == "the answer",
)
stream = "\n".join(
    [
        json.dumps({"type": "system", "subtype": "init"}),
        json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "partial"}]}}),
        json.dumps({"type": "result", "result": "final answer"}),
    ]
)
check("stream-json output takes the final result", extract_answer(stream) == "final answer")
check("non-json output falls back to raw text", extract_answer("just text") == "just text")

# --------------------------------------------------------------------------- #
print("\n[9] skill-use detection ignores prose mentions")
# --------------------------------------------------------------------------- #

fired = "\n".join(
    [
        json.dumps({"type": "system", "subtype": "init"}),
        json.dumps({"type": "assistant", "tool_use": {"name": "Skill", "input": {"skill": "incubator-concierge"}}}),
        json.dumps({"type": "result", "result": "Annotator retired in 2025."}),
    ]
)
check("skill call is detected", detect_skill_use(fired, "incubator-concierge"))

talked_about = "\n".join(
    [
        json.dumps({"type": "system", "subtype": "init"}),
        json.dumps({"type": "result", "result": "You could build an incubator-concierge skill for this."}),
    ]
)
check(
    "prose mention is NOT counted as a skill call",
    not detect_skill_use(talked_about, "incubator-concierge"),
)

# --------------------------------------------------------------------------- #
print("\n[10] content suite runs green against the real files")
# --------------------------------------------------------------------------- #

results = run_content_suite(None)
check(f"content suite has cases ({len(results)})", len(results) > 0)
for result in results:
    bad = [c for c in result.checks if not c.passed]
    check(
        f"content/{result.case_id}",
        result.error is None and not bad,
        result.error or "; ".join(f"{c.name}: {c.detail}" for c in bad),
    )

# --------------------------------------------------------------------------- #
print("\n[11] filtering and reporting")
# --------------------------------------------------------------------------- #

picked = select_cases(suites["behaviour"]["cases"], ["status-gate"])
check(f"filter by id substring selects {len(picked)} cases", len(picked) >= 2)
picked = select_cases(suites["behaviour"]["cases"], ["high-value"])
check(f"filter by tag selects {len(picked)} cases", len(picked) >= 3)
check("empty filter returns everything", len(select_cases(suites["behaviour"]["cases"], None)) == len(suites["behaviour"]["cases"]))

report = render_report("content", results)
check("report renders a heading", report.startswith("# Eval report"))
check("report lists case ids", results[0].case_id in report)

# --------------------------------------------------------------------------- #
print()
if failures:
    print(f"FAILED: {len(failures)} check(s)")
    for name in failures:
        print(f"  - {name}")
    sys.exit(1)
print("ALL SELF-TESTS PASSED")
