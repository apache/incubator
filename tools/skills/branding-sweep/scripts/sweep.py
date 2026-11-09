"""
sweep.py: run trademark_branding_check across all current podlings and write
per-podling results to raw-results.json.

Homepage URLs are derived from the podling name using the standard Apache
subdomain pattern (https://<short-name>.apache.org/). Network errors for any
individual podling are caught and recorded without aborting the sweep.
"""

import json
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from checker import trademark_branding_check

BASE_DIR = Path(__file__).parent
PODLINGS_PATH = BASE_DIR / "podlings.json"
OUTPUT_PATH = BASE_DIR / "raw-results.json"
MAX_WORKERS = 8
TIMEOUT = 15


def _short_name(podling_name):
    # "Apache Foo Bar" -> "foo-bar"
    return podling_name.removeprefix("Apache ").strip().lower().replace(" ", "-")


def _resolve_url(podling_name):
    """Try the canonical apache.org subdomain; return it regardless (checker handles 404)."""
    short = _short_name(podling_name)
    return f"https://{short}.apache.org/"


def _check_one(podling):
    name = podling["name"]
    url = podling.get("homepage_url") or _resolve_url(name)
    try:
        violations = trademark_branding_check(name, url)
    except Exception as exc:
        violations = [
            {
                "rule_id": "_sweep_error",
                "severity": "critical",
                "detail": f"Unhandled exception during check: {exc}",
            }
        ]
    return {
        "name": name,
        "status": podling.get("status", "incubating"),
        "started": podling.get("started"),
        "homepage_url": url,
        "violation_count": len(violations),
        "violations": violations,
    }


def run_sweep(podlings):
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_check_one, p): p["name"] for p in podlings}
        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {
                    "name": name,
                    "status": "unknown",
                    "started": None,
                    "homepage_url": None,
                    "violation_count": 1,
                    "violations": [
                        {
                            "rule_id": "_sweep_error",
                            "severity": "critical",
                            "detail": f"Future raised: {exc}",
                        }
                    ],
                }
            results.append(result)
            total = result["violation_count"]
            print(f"  {'OK' if total == 0 else f'{total} violation(s)':>15}  {name}")

    # Sort by descending violation count so worst offenders surface first
    results.sort(key=lambda r: -r["violation_count"])
    return results


def main():
    with open(PODLINGS_PATH) as f:
        podlings = json.load(f)

    print(f"Sweeping {len(podlings)} podling(s)…\n")
    results = run_sweep(podlings)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    total_violations = sum(r["violation_count"] for r in results)
    print(f"\nDone. {total_violations} total violation(s) across {len(results)} podling(s).")
    print(f"Results written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
