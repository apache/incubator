"""
ranker.py: read raw-results.json, score each podling by severity-weighted
violation count, and return a ranked fix list (worst first).

Severity weights
  critical -> 10   (blocks graduation)
  high     ->  5   (major branding gap)
  medium   ->  1   (minor / advisory)
  low      ->  1
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
RAW_RESULTS_PATH = BASE_DIR / "raw-results.json"

WEIGHTS = {
    "critical": 10,
    "high": 5,
    "medium": 1,
    "low": 1,
}


def _score(violations):
    return sum(WEIGHTS.get(v.get("severity", "low"), 1) for v in violations)


def rank(raw_results):
    """
    Accept the list loaded from raw-results.json and return a new list of dicts,
    each containing the original podling fields plus:
      score           – total weighted severity score
      critical_count  – number of critical violations
      high_count      – number of high violations
      medium_count    – number of medium/low violations
    Sorted descending by score, then descending by critical_count as tiebreaker.
    """
    ranked = []
    for entry in raw_results:
        violations = entry.get("violations", [])
        severities = [v.get("severity", "low") for v in violations]
        ranked.append(
            {
                **entry,
                "score": _score(violations),
                "critical_count": severities.count("critical"),
                "high_count": severities.count("high"),
                "medium_count": sum(1 for s in severities if s in ("medium", "low")),
            }
        )
    ranked.sort(key=lambda r: (-r["score"], -r["critical_count"]))
    return ranked


def load_and_rank(path=RAW_RESULTS_PATH):
    with open(path) as f:
        raw = json.load(f)
    return rank(raw)


OUTPUT_PATH = BASE_DIR / "ranked-fix-list.json"

if __name__ == "__main__":
    import sys

    path = Path(sys.argv[1]) if len(sys.argv) > 1 else RAW_RESULTS_PATH
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    ranked = load_and_rank(path)

    # Write the ranked fix list — each entry: name, score, violations
    fix_list = [
        {
            "name": r["name"],
            "score": r["score"],
            "critical_count": r["critical_count"],
            "high_count": r["high_count"],
            "medium_count": r["medium_count"],
            "violations": r["violations"],
        }
        for r in ranked
    ]
    with open(OUTPUT_PATH, "w") as f:
        json.dump(fix_list, f, indent=2)

    print(f"{'Rank':<5} {'Score':>5}  {'C':>3} {'H':>3} {'M':>3}  {'Podling'}")
    print("-" * 60)
    for i, r in enumerate(ranked, 1):
        print(
            f"{i:<5} {r['score']:>5}  "
            f"{r['critical_count']:>3} {r['high_count']:>3} {r['medium_count']:>3}  "
            f"{r['name']}"
        )
    print(f"\nTotal podlings ranked: {len(ranked)}")
    print("C=critical(×10)  H=high(×5)  M=medium/low(×1)")
    print(f"\nFix list written to {OUTPUT_PATH}")
