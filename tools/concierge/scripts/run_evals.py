#!/usr/bin/env python3
"""Run the Incubator Concierge eval suites through the Claude Code CLI.

    python3 scripts/run_evals.py --suite all
    python3 scripts/run_evals.py --suite behaviour --filter status-gate
    python3 scripts/run_evals.py --suite content        # no model, no cost

Suites:

  content     Static assertions over the skill files. No model, instant, free.
              This is the one to wire into CI.
  behaviour   Real prompts through `claude -p`, graded deterministically and
              (unless --no-judge) by a judge model.
  triggering  Does the skill fire on real phrasings and stay quiet on
              near-misses. Grades the description, not the body.

Exit status is 1 if any deterministic check fails, or if a judged criterion
fails and --judge-fatal is set. Judged failures are advisory by default because
judges are less reproducible than regexes, and a flaky red build gets ignored.

The CLI invocation is deliberately configurable: flag names and permission
defaults vary between Claude Code versions, so pass --claude-arg as needed
rather than editing this file.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (  # noqa: E402
    CaseResult,
    Check,
    build_judge_prompt,
    detect_skill_use,
    extract_json,
    grade_assertions,
    grade_judge_reply,
    load_suite,
    render_report,
    select_cases,
    summarise,
)

SKILL_NAME = "incubator-concierge"
ROOT = Path(__file__).resolve().parent.parent
EVALS_DIR = ROOT / "evals"


# --------------------------------------------------------------------------- #
# CLI invocation
# --------------------------------------------------------------------------- #


class ClaudeRunner:
    def __init__(
        self,
        binary: str,
        model: str | None,
        timeout: int,
        extra_args: list[str],
        cwd: Path,
    ) -> None:
        self.binary = binary
        self.model = model
        self.timeout = timeout
        self.extra_args = extra_args
        self.cwd = cwd

    def _base_cmd(self, prompt: str, output_format: str) -> list[str]:
        cmd = [self.binary, "-p", prompt, "--output-format", output_format]
        if self.model:
            cmd += ["--model", self.model]
        if output_format == "stream-json":
            cmd.append("--verbose")
        return cmd + self.extra_args

    def run(self, prompt: str, output_format: str = "json") -> tuple[str, str]:
        """Return (raw stdout, extracted answer text)."""

        cmd = self._base_cmd(prompt, output_format)
        proc = subprocess.run(
            cmd,
            cwd=str(self.cwd),
            capture_output=True,
            text=True,
            timeout=self.timeout,
        )
        raw = proc.stdout
        if proc.returncode != 0 and not raw.strip():
            raise RuntimeError(f"claude exited {proc.returncode}: {proc.stderr.strip()[:400]}")
        return raw, extract_answer(raw)


def extract_answer(raw: str) -> str:
    """Pull the final assistant text out of json or stream-json output."""

    # stream-json: last event carrying a result field wins.
    answer = ""
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and isinstance(event.get("result"), str):
            answer = event["result"]
    if answer:
        return answer

    parsed = extract_json(raw)
    if isinstance(parsed, dict) and isinstance(parsed.get("result"), str):
        return parsed["result"]

    return raw.strip()


# --------------------------------------------------------------------------- #
# Suites
# --------------------------------------------------------------------------- #


def run_content_suite(filters: list[str] | None) -> list[CaseResult]:
    suite = load_suite(EVALS_DIR / "content.json")
    results: list[CaseResult] = []

    for case in select_cases(suite["cases"], filters):
        target = ROOT / case["file"]
        result = CaseResult(case_id=case["id"], prompt=f"static check on {case['file']}", tags=case.get("tags", []))
        if not target.is_file():
            result.error = f"{case['file']} does not exist"
            results.append(result)
            continue
        text = target.read_text(encoding="utf-8")
        result.checks = grade_assertions(text, case.get("assertions", {}))
        if case.get("why"):
            result.tags = [*result.tags, "why:" + case["why"]]
        results.append(result)

    return results


def run_behaviour_suite(
    runner: ClaudeRunner,
    filters: list[str] | None,
    use_judge: bool,
    jobs: int,
    force_skill: bool,
) -> list[CaseResult]:
    suite = load_suite(EVALS_DIR / "behaviour.json")
    cases = select_cases(suite["cases"], filters)

    def one(case: dict) -> CaseResult:
        result = CaseResult(case_id=case["id"], prompt=case["prompt"], tags=case.get("tags", []))
        started = time.time()
        prompt = case["prompt"]
        if force_skill:
            prompt = f"Use the {SKILL_NAME} skill for this.\n\n{prompt}"
        try:
            _, answer = runner.run(prompt)
            result.answer = answer
            result.checks = grade_assertions(answer, case.get("assertions", {}))

            criteria = case.get("judge", [])
            if use_judge and criteria:
                judge_prompt = build_judge_prompt(case["prompt"], answer, criteria)
                _, reply = runner.run(judge_prompt)
                if extract_json(reply) is None:
                    # A judge that answers in prose fails every criterion, which
                    # reads as a broken answer rather than a broken grader. Give
                    # it exactly one stricter retry before believing the verdict.
                    _, reply = runner.run(
                        judge_prompt
                        + "\n\nYour previous reply could not be parsed. Reply with ONLY the JSON "
                        "object described above: no prose before or after it, no code fence."
                    )
                result.checks += grade_judge_reply(reply, criteria)
            elif criteria:
                result.checks += [
                    Check(name=f"judge:{c['id']}", passed=True, detail="skipped (--no-judge)", judged=True)
                    for c in criteria
                ]
        except Exception as exc:  # noqa: BLE001 - surfaced in the report
            result.error = f"{type(exc).__name__}: {exc}"
        result.duration_s = time.time() - started
        return result

    return _map(one, cases, jobs)


def run_triggering_suite(runner: ClaudeRunner, filters: list[str] | None, jobs: int) -> list[CaseResult]:
    suite = load_suite(EVALS_DIR / "triggering.json")
    cases = select_cases(suite["cases"], filters)

    def one(case: dict) -> CaseResult:
        expected = bool(case["should_trigger"])
        result = CaseResult(
            case_id=case["id"],
            prompt=case["prompt"],
            tags=[*case.get("tags", []), "expect:" + ("trigger" if expected else "no-trigger")],
        )
        started = time.time()
        try:
            raw, answer = runner.run(case["prompt"], output_format="stream-json")
            result.answer = answer
            fired = detect_skill_use(raw, SKILL_NAME)
            result.checks = [
                Check(
                    name=("skill fires" if expected else "skill stays quiet"),
                    passed=(fired == expected),
                    detail=f"skill {'was' if fired else 'was not'} consulted",
                )
            ]
        except Exception as exc:  # noqa: BLE001
            result.error = f"{type(exc).__name__}: {exc}"
        result.duration_s = time.time() - started
        return result

    return _map(one, cases, jobs)


def _map(fn, cases: list[dict], jobs: int) -> list[CaseResult]:
    if jobs <= 1:
        out = []
        for case in cases:
            print(f"  running {case['id']} …", flush=True)
            out.append(fn(case))
        return out
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = {pool.submit(fn, c): c for c in cases}
        out = []
        for future in concurrent.futures.as_completed(futures):
            case = futures[future]
            print(f"  done {case['id']}", flush=True)
            out.append(future.result())
    order = {c["id"]: i for i, c in enumerate(cases)}
    return sorted(out, key=lambda r: order.get(r.case_id, 0))


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--suite", default="content", choices=["content", "behaviour", "triggering", "all"])
    parser.add_argument("--filter", action="append", dest="filters", help="regex on case id or tag; repeatable")
    parser.add_argument("--claude-bin", default="claude")
    parser.add_argument("--model", default=None, help="model id passed to claude --model")
    parser.add_argument("--timeout", type=int, default=300, help="per-call timeout in seconds")
    parser.add_argument("--jobs", type=int, default=3, help="parallel cases (1 = serial, readable output)")
    parser.add_argument("--no-judge", action="store_true", help="skip LLM-judged criteria")
    parser.add_argument("--judge-fatal", action="store_true", help="judged failures also fail the run")
    parser.add_argument("--force-skill", action="store_true", help="prepend an instruction to use the skill")
    parser.add_argument(
        "--claude-arg",
        action="append",
        default=[],
        dest="claude_args",
        help="extra arg passed through to claude, e.g. --claude-arg=--permission-mode "
        "--claude-arg=bypassPermissions; repeatable",
    )
    parser.add_argument(
        "--cwd",
        default=None,
        help="directory to launch claude from. Defaults to this repo. Set it if your MCP servers "
        "are project-scoped elsewhere — the behaviour suite is meaningless without them.",
    )
    parser.add_argument("--out", default=str(ROOT / "evals" / "results"), help="output directory")
    args = parser.parse_args(argv[1:])

    suites = ["content", "behaviour", "triggering"] if args.suite == "all" else [args.suite]
    needs_model = any(s in {"behaviour", "triggering"} for s in suites)

    runner = None
    if needs_model:
        if not shutil.which(args.claude_bin):
            print(f"error: '{args.claude_bin}' not found on PATH.", file=sys.stderr)
            print("       The content suite runs without it: --suite content", file=sys.stderr)
            return 2
        launch_dir = Path(args.cwd).expanduser().resolve() if args.cwd else ROOT
        if not launch_dir.is_dir():
            print(f"error: --cwd {launch_dir} is not a directory", file=sys.stderr)
            return 2
        print(f"launching claude from {launch_dir}")
        runner = ClaudeRunner(args.claude_bin, args.model, args.timeout, args.claude_args, launch_dir)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    exit_code = 0

    for suite_name in suites:
        print(f"\n=== {suite_name} ===")
        if suite_name == "content":
            results = run_content_suite(args.filters)
        elif suite_name == "behaviour":
            assert runner is not None
            results = run_behaviour_suite(runner, args.filters, not args.no_judge, args.jobs, args.force_skill)
        else:
            assert runner is not None
            results = run_triggering_suite(runner, args.filters, args.jobs)

        if not results:
            print("  no cases matched the filter")
            continue

        stats = summarise(results)
        (out_dir / f"{suite_name}.json").write_text(
            json.dumps({"suite": suite_name, "summary": stats, "results": [r.to_dict() for r in results]}, indent=2),
            encoding="utf-8",
        )
        (out_dir / f"{suite_name}.md").write_text(render_report(suite_name, results), encoding="utf-8")

        for result in results:
            if result.error:
                mark = "ERROR"
            elif result.hard_failed:
                mark = "FAIL"
            elif result.judged_failed:
                mark = "FAIL(judge)"
            else:
                mark = "pass"
            print(f"  {mark:12} {result.case_id}")
            for check in result.checks:
                if not check.passed:
                    print(f"               ↳ {check.name} — {check.detail}")

        print(
            f"  deterministic {stats['hard_passed']}/{stats['hard_checks']}"
            + (f", judged {stats['judged_passed']}/{stats['judged_checks']}" if stats["judged_checks"] else "")
        )
        print(f"  report: {out_dir / (suite_name + '.md')}")

        if stats["cases_failed_hard"] or stats["errors"]:
            exit_code = 1
        if args.judge_fatal and stats["cases_failed_judge_only"]:
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
