"""
trademark_branding_check: check a podling's homepage and inferred GitHub repo
against the ASF branding compliance ruleset defined in rules.json.
"""

import json
import re
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

RULES_PATH = Path(__file__).parent / "rules.json"
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
TIMEOUT = 5          # homepage fetch
GITHUB_TIMEOUT = 3   # per GitHub raw probe


def _load_rules():
    with open(RULES_PATH) as f:
        return json.load(f)


def _fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ASF-BrandingChecker/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception:
        return None


def _short_name(podling_name):
    # "Apache Foo Bar" -> "foo-bar"
    return podling_name.removeprefix("Apache ").strip().lower().replace(" ", "-")


def _probe_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ASF-BrandingChecker/1.0"})
        with urllib.request.urlopen(req, timeout=GITHUB_TIMEOUT) as resp:
            return resp.status == 200
    except Exception:
        return False


def _github_file_exists(short_name, filename):
    candidates = [
        f"https://raw.githubusercontent.com/apache/{short_name}-incubating/main/{filename}",
        f"https://raw.githubusercontent.com/apache/{short_name}-incubating/master/{filename}",
        f"https://raw.githubusercontent.com/apache/{short_name}/main/{filename}",
        f"https://raw.githubusercontent.com/apache/{short_name}/master/{filename}",
    ]
    with ThreadPoolExecutor(max_workers=len(candidates)) as pool:
        return any(pool.map(_probe_url, candidates))


def _check_text_contains(html, rule, podling_name):
    short = _short_name(podling_name)
    flags = re.IGNORECASE if rule["check"].get("case_insensitive") else 0
    for pattern in rule["check"]["patterns"]:
        expanded = pattern.replace("{name}", re.escape(short))
        if re.search(expanded, html, flags):
            return None  # pass
    return {
        "rule_id": rule["id"],
        "severity": rule["severity"],
        "detail": (
            f"None of the required patterns found on homepage. "
            f"Expected one of: {rule['check']['patterns']}"
        ),
    }


def _check_text_absent(html, rule, podling_name):
    flags = re.IGNORECASE if rule["check"].get("case_insensitive") else 0
    for pattern in rule["check"]["patterns"]:
        if re.search(pattern, html, flags):
            return {
                "rule_id": rule["id"],
                "severity": rule["severity"],
                "detail": f"Prohibited pattern found on homepage: '{pattern}'",
            }
    return None  # pass


def _check_link_exists(html, rule):
    required_urls = rule["check"].get("urls", [])
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    for required in required_urls:
        if any(href.startswith(required) for href in hrefs):
            return None  # pass
    return {
        "rule_id": rule["id"],
        "severity": rule["severity"],
        "detail": f"No link to any of {required_urls} found on homepage",
    }


def _check_file_exists(podling_name, rule):
    short = _short_name(podling_name)
    filenames = rule["check"].get("filenames", [])
    for filename in filenames:
        if _github_file_exists(short, filename):
            return None  # pass
    return {
        "rule_id": rule["id"],
        "severity": rule["severity"],
        "detail": (
            f"Could not find {' or '.join(filenames)} in common GitHub repo locations "
            f"(apache/{short}-incubating, apache/{short}). Verify manually."
        ),
    }


def trademark_branding_check(podling_name, podling_url):
    """
    Check a podling's homepage against the ASF branding ruleset.

    Returns a list of violation dicts, each with keys:
      rule_id  – identifier from rules.json
      severity – 'critical' | 'high' | 'medium' | 'low'
      detail   – human-readable description of the specific failure
    Sorted by severity (critical first).
    """
    rules = _load_rules()
    html = _fetch(podling_url)
    if not html:
        return [
            {
                "rule_id": "_fetch_error",
                "severity": "critical",
                "detail": f"Could not fetch homepage: {podling_url}",
            }
        ]

    violations = []
    for rule in rules:
        check_type = rule["check"]["type"]
        targets = rule["check"].get("targets", [])
        homepage_targeted = any(
            t in ("homepage", "homepage_title", "homepage_footer", "about_page")
            for t in targets
        )
        file_targeted = any(
            t in ("release_archive_root", "source_repo_root")
            for t in targets
        )

        result = None
        if check_type == "text_contains" and homepage_targeted:
            result = _check_text_contains(html, rule, podling_name)
        elif check_type == "text_absent" and homepage_targeted:
            result = _check_text_absent(html, rule, podling_name)
        elif check_type == "link_exists" and homepage_targeted:
            result = _check_link_exists(html, rule)
        elif check_type == "file_exists" and file_targeted:
            result = _check_file_exists(podling_name, rule)

        if result:
            violations.append(result)

    violations.sort(key=lambda v: SEVERITY_ORDER.get(v["severity"], 99))
    return violations


if __name__ == "__main__":
    import sys

    # --test: run against example.com, which carries no ASF branding and is
    # guaranteed to produce violations for every homepage-targeted rule.
    if len(sys.argv) == 2 and sys.argv[1] == "--test":
        _TEST_NAME = "Apache TestPodling"
        _TEST_URL = "https://example.com"
        results = trademark_branding_check(_TEST_NAME, _TEST_URL)
        assert results, "Expected at least one violation from the test fixture but got none"
        print(json.dumps(results, indent=2))
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Usage: checker.py <podling_name> <homepage_url>")
        print("       checker.py --test")
        sys.exit(1)

    name, url = sys.argv[1], sys.argv[2]
    results = trademark_branding_check(name, url)
    if results:
        print(f"\n{len(results)} violation(s) for '{name}':")
        for v in results:
            print(f"  [{v['severity'].upper()}] {v['rule_id']}: {v['detail']}")
    else:
        print(f"No violations found for '{name}'.")
