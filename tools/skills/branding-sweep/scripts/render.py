"""
render.py: read ranked-fix-list.json and write fix-list.md grouped by severity tier.
"""

import json
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_PATH  = BASE_DIR / "ranked-fix-list.json"
OUTPUT_PATH = BASE_DIR / "fix-list.md"


def render(data):
    buckets = {"critical": [], "major": [], "minor": []}
    for entry in data:
        if entry["critical_count"] > 0:
            buckets["critical"].append(entry)
        elif entry["high_count"] > 0:
            buckets["major"].append(entry)
        else:
            buckets["minor"].append(entry)

    lines = [
        "# Apache Incubator Branding Compliance — Ranked Fix List",
        "",
        f"Generated: {date.today()}  ",
        f"Podlings checked: {len(data)}  ",
        "Scoring: critical=10 · high=5 · medium/low=1",
        "",
        "---",
        "",
    ]

    TIERS = [
        ("critical", "## Critical",
         "Must-fix before graduation. Violations in this tier block IPMC approval."),
        ("major",    "## Major",
         "Significant branding gaps. Should be resolved promptly."),
        ("minor",    "## Minor",
         "Advisory items. Low urgency but should be addressed before graduation."),
    ]

    for key, heading, blurb in TIERS:
        entries = buckets[key]
        if not entries:
            continue
        lines += [heading, "", blurb, ""]
        for i, e in enumerate(entries, 1):
            top    = e["violations"][0] if e["violations"] else {}
            rule_id = top.get("rule_id", "—")
            detail  = top.get("detail", "—")
            if len(detail) > 120:
                detail = detail[:117] + "…"
            lines.append(
                f"{i}. **{e['name']}** (score {e['score']}, "
                f"{e['critical_count']}C/{e['high_count']}H/{e['medium_count']}M)  "
            )
            lines.append(f"   `{rule_id}` — {detail}")
            lines.append("")

    lines += [
        "---",
        "",
        "_Scores: each critical violation ×10, each high ×5, each medium/low ×1._",
    ]
    return "\n".join(lines)


def main():
    with open(INPUT_PATH) as f:
        data = json.load(f)
    md = render(data)
    with open(OUTPUT_PATH, "w") as f:
        f.write(md)
    print(f"Rendered {len(data)} podlings → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
