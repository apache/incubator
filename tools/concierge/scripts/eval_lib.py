"""Shared machinery for the Incubator Concierge eval suites.

Everything here is pure and model-free so it can be exercised without spending
tokens — see `self_test_evals.py`. The model invocation lives in `run_evals.py`.

Assertion vocabulary (all optional, all case-insensitive unless noted):

    contains        list[str]   every string must appear
    not_contains    list[str]   no string may appear
    matches         list[str]   every regex must match
    not_matches     list[str]   no regex may match
    contains_any    list[list]  for each group, at least one member must appear

`contains_any` exists because a correct answer often has several acceptable
phrasings ("graduated", "is now a top-level project"), and asserting one exact
wording tests the phrasing rather than the behaviour.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #


@dataclass
class Check:
    """One graded expectation and whether the answer met it."""

    name: str
    passed: bool
    detail: str = ""
    judged: bool = False


@dataclass
class CaseResult:
    case_id: str
    prompt: str
    tags: list[str] = field(default_factory=list)
    answer: str = ""
    checks: list[Check] = field(default_factory=list)
    error: str | None = None
    duration_s: float = 0.0

    @property
    def hard_checks(self) -> list[Check]:
        return [c for c in self.checks if not c.judged]

    @property
    def judged_checks(self) -> list[Check]:
        return [c for c in self.checks if c.judged]

    @property
    def hard_failed(self) -> bool:
        return self.error is not None or any(not c.passed for c in self.hard_checks)

    @property
    def judged_failed(self) -> bool:
        return any(not c.passed for c in self.judged_checks)

    def to_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "prompt": self.prompt,
            "tags": self.tags,
            "answer": self.answer,
            "error": self.error,
            "duration_s": round(self.duration_s, 2),
            "checks": [
                {"name": c.name, "passed": c.passed, "detail": c.detail, "judged": c.judged} for c in self.checks
            ],
        }


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #


def load_suite(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "cases" not in data or not isinstance(data["cases"], list):
        raise ValueError(f"{path} has no 'cases' list")
    seen: set[str] = set()
    for case in data["cases"]:
        cid = case.get("id")
        if not cid:
            raise ValueError(f"{path} has a case with no 'id'")
        if cid in seen:
            raise ValueError(f"{path} has duplicate case id '{cid}'")
        seen.add(cid)
    return data


def select_cases(cases: list[dict[str, Any]], patterns: list[str] | None) -> list[dict[str, Any]]:
    if not patterns:
        return cases
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    return [c for c in cases if any(p.search(c["id"]) or p.search(" ".join(c.get("tags", []))) for p in compiled)]


# --------------------------------------------------------------------------- #
# Deterministic grading
# --------------------------------------------------------------------------- #


def _norm(text: str) -> str:
    """Fold whitespace so assertions survive line wrapping in the answer."""

    return re.sub(r"\s+", " ", text)


def _excerpt(text: str, needle: str, width: int = 60) -> str:
    idx = _norm(text).lower().find(needle.lower())
    if idx < 0:
        return ""
    body = _norm(text)
    start = max(0, idx - width // 2)
    return "…" + body[start : start + width] + "…"


def grade_assertions(answer: str, assertions: dict[str, Any]) -> list[Check]:
    """Apply the deterministic assertion vocabulary to one answer."""

    checks: list[Check] = []
    folded = _norm(answer)

    for needle in assertions.get("contains", []):
        hit = needle.lower() in folded.lower()
        checks.append(
            Check(
                name=f"contains {needle!r}",
                passed=hit,
                detail=_excerpt(answer, needle) if hit else "not found",
            )
        )

    for needle in assertions.get("not_contains", []):
        hit = needle.lower() in folded.lower()
        checks.append(
            Check(
                name=f"does not contain {needle!r}",
                passed=not hit,
                detail=_excerpt(answer, needle) if hit else "absent as required",
            )
        )

    for group in assertions.get("contains_any", []):
        found = [n for n in group if n.lower() in folded.lower()]
        checks.append(
            Check(
                name=f"contains any of {group!r}",
                passed=bool(found),
                detail=f"matched {found!r}" if found else "none of the alternatives appeared",
            )
        )

    for pattern in assertions.get("matches", []):
        match = re.search(pattern, folded, re.IGNORECASE)
        checks.append(
            Check(
                name=f"matches /{pattern}/",
                passed=match is not None,
                detail=f"matched {match.group(0)!r}" if match else "no match",
            )
        )

    for pattern in assertions.get("not_matches", []):
        match = re.search(pattern, folded, re.IGNORECASE)
        checks.append(
            Check(
                name=f"does not match /{pattern}/",
                passed=match is None,
                detail=f"matched {match.group(0)!r}" if match else "absent as required",
            )
        )

    return checks


# --------------------------------------------------------------------------- #
# LLM judging
# --------------------------------------------------------------------------- #

JUDGE_INSTRUCTIONS = """You are grading one answer produced by an Apache Incubator assistant.

Grade ONLY the criteria listed. Judge what the answer actually says, not what a
good answer might have said. If a criterion is not clearly met, mark it failed —
default to failing when uncertain, because a lenient judge makes the eval useless.

Reply with JSON only, no prose, in exactly this shape:
{"criteria": [{"id": "<criterion id>", "passed": true, "evidence": "<short quote or reason>"}]}
"""


def build_judge_prompt(question: str, answer: str, criteria: list[dict[str, str]]) -> str:
    listed = "\n".join(f"- id: {c['id']}\n  requirement: {c['requirement']}" for c in criteria)
    return (
        f"{JUDGE_INSTRUCTIONS}\n"
        f"## Question asked\n{question}\n\n"
        f"## Answer to grade\n{answer}\n\n"
        f"## Criteria\n{listed}\n"
    )


def extract_json(text: str) -> dict[str, Any] | None:
    """Pull the first balanced JSON object out of a model reply."""

    start = text.find("{")
    while start != -1:
        depth = 0
        in_string = False
        escaped = False
        for idx in range(start, len(text)):
            char = text[idx]
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_string = False
                continue
            if char == '"':
                in_string = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    try:
                        parsed = json.loads(text[start : idx + 1])
                    except json.JSONDecodeError:
                        break
                    if isinstance(parsed, dict):
                        return parsed
                    break
        start = text.find("{", start + 1)
    return None


def grade_judge_reply(reply: str, criteria: list[dict[str, str]]) -> list[Check]:
    parsed = extract_json(reply)
    if parsed is None or not isinstance(parsed.get("criteria"), list):
        return [
            Check(
                name=f"judge:{c['id']}",
                passed=False,
                detail="judge reply was not parseable JSON",
                judged=True,
            )
            for c in criteria
        ]

    verdicts = {str(v.get("id")): v for v in parsed["criteria"] if isinstance(v, dict)}
    checks: list[Check] = []
    for criterion in criteria:
        verdict = verdicts.get(criterion["id"])
        if verdict is None:
            checks.append(
                Check(
                    name=f"judge:{criterion['id']}",
                    passed=False,
                    detail="judge did not return a verdict for this criterion",
                    judged=True,
                )
            )
            continue
        checks.append(
            Check(
                name=f"judge:{criterion['id']}",
                passed=bool(verdict.get("passed")),
                detail=str(verdict.get("evidence", ""))[:300],
                judged=True,
            )
        )
    return checks


# --------------------------------------------------------------------------- #
# Triggering detection
# --------------------------------------------------------------------------- #


def detect_skill_use(raw_output: str, skill_name: str) -> bool:
    """Decide whether a transcript shows the skill being consulted.

    The answer text itself is excluded from the search: a reply that merely says
    the words "incubator concierge" is not evidence the skill loaded. Only
    structural mentions — a Skill tool call, a loaded-skill event — count.
    """

    events: list[str] = []
    for line in raw_output.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        events.append(json.dumps(_strip_result_text(parsed)))

    if not events:
        # Not stream-json; fall back to the whole payload minus the result field.
        parsed = extract_json(raw_output)
        if parsed is not None:
            events.append(json.dumps(_strip_result_text(parsed)))
        else:
            return False

    needle = skill_name.lower()
    return any(needle in event.lower() for event in events)


def _strip_result_text(payload: Any) -> Any:
    """Remove assistant prose so only structural fields are searched."""

    if isinstance(payload, dict):
        return {k: _strip_result_text(v) for k, v in payload.items() if k not in {"result", "text", "content"}}
    if isinstance(payload, list):
        return [_strip_result_text(v) for v in payload]
    return payload


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #


def summarise(results: list[CaseResult]) -> dict[str, Any]:
    hard_total = sum(len(r.hard_checks) for r in results)
    hard_passed = sum(1 for r in results for c in r.hard_checks if c.passed)
    judged_total = sum(len(r.judged_checks) for r in results)
    judged_passed = sum(1 for r in results for c in r.judged_checks if c.passed)
    return {
        "cases": len(results),
        "cases_failed_hard": sum(1 for r in results if r.hard_failed),
        "cases_failed_judge_only": sum(1 for r in results if r.judged_failed and not r.hard_failed),
        "errors": sum(1 for r in results if r.error),
        "hard_checks": hard_total,
        "hard_passed": hard_passed,
        "judged_checks": judged_total,
        "judged_passed": judged_passed,
    }


def render_report(suite_name: str, results: list[CaseResult]) -> str:
    stats = summarise(results)
    lines = [
        f"# Eval report — {suite_name}",
        "",
        f"- Cases: **{stats['cases']}**",
        f"- Deterministic checks: **{stats['hard_passed']}/{stats['hard_checks']}**",
    ]
    if stats["judged_checks"]:
        lines.append(f"- Judged criteria: **{stats['judged_passed']}/{stats['judged_checks']}**")
    lines += [
        f"- Cases failing a deterministic check: **{stats['cases_failed_hard']}**",
        f"- Cases failing only a judged criterion: **{stats['cases_failed_judge_only']}**",
        f"- Runner errors: **{stats['errors']}**",
        "",
    ]

    for result in results:
        if result.error:
            status = "ERROR"
        elif result.hard_failed:
            status = "FAIL"
        elif result.judged_failed:
            status = "FAIL (judge)"
        else:
            status = "PASS"

        lines.append(f"## {status} — `{result.case_id}`")
        if result.tags:
            lines.append(f"tags: {', '.join(result.tags)}")
        lines.append("")
        lines.append(f"**Prompt:** {result.prompt}")
        lines.append("")
        if result.error:
            lines += [f"**Runner error:** {result.error}", ""]
        for check in result.checks:
            mark = "x" if check.passed else " "
            lines.append(f"- [{mark}] {check.name}" + (f" — {check.detail}" if check.detail else ""))
        lines.append("")
        if result.answer:
            excerpt = result.answer if len(result.answer) < 1500 else result.answer[:1500] + "\n…[truncated]"
            lines += ["<details><summary>Answer</summary>", "", "```", excerpt, "```", "", "</details>", ""]

    return "\n".join(lines)
