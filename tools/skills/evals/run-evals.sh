#!/bin/bash
# Run all skill evals via REAL claude invocations.
#
# Each case runs `claude -p` from the skills directory with a realistic user
# prompt that references a fixture file. The skills are discovered the same way
# they would be in real use, so this tests triggering AND judgment - nothing is
# pasted into the prompt.
#
# Usage: bash evals/run-evals.sh
# Exit status = number of failed cases (0 = all 8 passed).
set -u
cd "$(dirname "$0")/.."

TAIL='Work ONLY from that file - treat it as the complete evidence; make no
live server calls and no network requests. End your reply with a single last
line reading exactly "OUTCOME: APPROVE" or "OUTCOME: FLAG" - APPROVE if it
passes / is healthy / is ready / should not be retired, FLAG if you found
blocking problems, a mismatch, unreadiness, or grounds to retire.'

run_case() {
  skill=$1; fixture=$2; expect=$3; prompt=$4
  out="evals/$skill/output/$fixture.txt"
  mkdir -p "evals/$skill/output"
  echo "running $skill/$fixture ..." >&2
  claude -p --dangerously-skip-permissions "$prompt

$TAIL" > "$out" 2>"$out.err"
  verdict=$(grep -Eo "OUTCOME: (APPROVE|FLAG)" "$out" | tail -1)
  if [ "$verdict" = "OUTCOME: $expect" ]; then
    echo "PASS  $skill/$fixture"
  else
    echo "FAIL  $skill/$fixture  (expected OUTCOME: $expect, got: ${verdict:-nothing})"
    fails=$((fails + 1))
  fi
}

fails=0

run_case release-vote-reviewer passing-vote APPROVE \
  "There's an incubator release vote I need to review. The full thread and artifact evidence are in evals/release-vote-reviewer/passing-vote.txt. Walk the checks and tell me whether I should vote +1 or -1."

run_case release-vote-reviewer failing-vote FLAG \
  "There's an incubator release vote I need to review. The full thread and artifact evidence are in evals/release-vote-reviewer/failing-vote.txt. Walk the checks and tell me whether I should vote +1 or -1."

run_case monthly-report-review clean-cohort APPROVE \
  "Do the monthly Incubator report review. The cohort, filed reports, and health data are all in evals/monthly-report-review/clean-cohort.txt - use that as the only data source. Flag anything that needs a shepherd comment."

run_case monthly-report-review mismatch-cohort FLAG \
  "Do the monthly Incubator report review. The cohort, filed reports, and health data are all in evals/monthly-report-review/mismatch-cohort.txt - use that as the only data source. Flag anything that needs a shepherd comment."

run_case graduation-packet-builder ready-podling APPROVE \
  "Is the podling described in evals/graduation-packet-builder/ready-podling.txt ready to graduate? Assess the maturity evidence and give me your call."

run_case graduation-packet-builder not-ready-podling FLAG \
  "Is the podling described in evals/graduation-packet-builder/not-ready-podling.txt ready to graduate? Assess the maturity evidence and give me your call."

run_case retirement-shepherd active-podling APPROVE \
  "Should we start a retirement discussion for the podling described in evals/retirement-shepherd/active-podling.txt? Review the evidence and advise."

run_case retirement-shepherd stalled-podling FLAG \
  "Should we start a retirement discussion for the podling described in evals/retirement-shepherd/stalled-podling.txt? Review the evidence and advise."

echo
if [ "$fails" -eq 0 ]; then
  echo "All 8 eval cases passed."
else
  echo "$fails eval case(s) FAILED - read the output file(s) named above."
fi
exit "$fails"
