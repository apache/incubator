"""Podling name clearance tool for Apache Software Foundation incubator proposals."""

import json
import re
import urllib.error
import urllib.parse
import urllib.request


def validate_name(name: str) -> bool:
    """Validate that a proposed podling name meets basic ASF naming requirements.

    Returns True if the name is valid (non-empty, starts with a letter,
    contains only letters/digits/hyphens), False otherwise.
    """
    if not name:
        return False
    if not name[0].isalpha():
        return False
    if not re.fullmatch(r"[A-Za-z0-9-]+", name):
        return False
    return True


def perform_name_search(name: str) -> dict:
    """Search for conflicts with the proposed podling name across relevant namespaces.

    Returns a dict with keys 'apache', 'uspto', and 'google'. Each value is a
    list of conflict dicts, where every entry has at least 'name' and 'url'.
    An empty list means no conflicts were found (or the search failed silently).
    """
    return {
        "apache": _search_apache(name).get("conflicts", []),
        "uspto": _search_uspto(name).get("conflicts", []),
        "google": _search_web(name).get("conflicts", []),
    }


def _fetch_json(url: str, timeout: int = 12) -> object:
    req = urllib.request.Request(
        url, headers={"User-Agent": "PodlingNameClearance/1.0 (ASF incubator check)"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _make_result(conflicts=None, warnings=None, error=None):
    return {"conflicts": conflicts or [], "warnings": warnings or [], "error": error}


def _search_apache(name: str) -> dict:
    url = "https://projects.apache.org/json/foundation/projects.json"
    try:
        projects = _fetch_json(url)
        name_lower = name.lower()
        conflicts = []
        for key, proj in projects.items():
            proj_name = proj.get("name", "")
            if name_lower in (key.lower(), proj_name.lower()):
                conflicts.append(
                    {
                        "name": proj_name or key,
                        "url": proj.get(
                            "homepage",
                            f"https://projects.apache.org/project/{key}.html",
                        ),
                    }
                )
        return _make_result(conflicts=conflicts)
    except Exception as exc:
        return _make_result(error=str(exc))


def _search_uspto(name: str) -> dict:
    encoded = urllib.parse.quote(name)
    url = (
        "https://tmsearch.uspto.gov/api/search"
        f"?searchInput={encoded}&searchType=all&rows=5&start=0"
    )
    try:
        data = _fetch_json(url, timeout=15)
        hits = (data.get("hits") or {}).get("hits") or []
        conflicts = []
        for hit in hits:
            src = hit.get("_source", hit)
            mark = src.get("markVerbalElementText") or src.get("name") or ""
            serial = src.get("serialNumber") or src.get("id") or ""
            if mark and name.lower() in mark.lower():
                conflicts.append(
                    {
                        "name": mark,
                        "url": (
                            f"https://tsdrapi.uspto.gov/ts/cd/casestatus/sn{serial}"
                            if serial
                            else "https://tmsearch.uspto.gov/"
                        ),
                    }
                )
        return _make_result(conflicts=conflicts)
    except Exception as exc:
        return _make_result(error=str(exc))


def _search_web(name: str) -> dict:
    query = urllib.parse.quote(f"Apache {name} open source project")
    url = (
        f"https://api.duckduckgo.com/?q={query}"
        "&format=json&t=PodlingNameClearance&no_redirect=1&no_html=1"
    )
    try:
        data = _fetch_json(url)
        warnings = []
        abstract = data.get("AbstractText", "")
        abstract_url = data.get("AbstractURL", "")
        if abstract and name.lower() in abstract.lower():
            warnings.append(
                f"Web search returned a notable result for '{name}': "
                + (abstract_url or abstract[:120])
            )
        for topic in (data.get("RelatedTopics") or [])[:5]:
            text = topic.get("Text", "")
            href = topic.get("FirstURL", "")
            if text and name.lower() in text.lower():
                warnings.append(f"Web result: {text[:120]} — {href}")
        return _make_result(warnings=warnings)
    except Exception as exc:
        return _make_result(error=str(exc))


def format_clearance_report(name: str, search_results: dict) -> str:
    """Format the name clearance findings into the standard ASF writeup.

    Returns a string in the format expected for the PODLINGNAMESEARCH section
    of an Apache incubator proposal, with Trademark, Web Search, and Apache
    Namespace sections.

    search_results keys: 'uspto', 'google', 'apache'. Each value may be a list
    of conflict dicts (legacy) or a sub-dict with 'conflicts'/'warnings'/'error'.
    """
    lines = [
        f"== Podling Name Clearance: {name} ==",
        "",
    ]

    def _section(heading: str, data) -> None:
        lines.append(f"=== {heading} ===")
        if isinstance(data, list):
            conflicts, warnings, error = data, [], None
        else:
            conflicts = data.get("conflicts", [])
            warnings = data.get("warnings", [])
            error = data.get("error")
        if error:
            lines.append(f"Search failed: {error}")
        elif conflicts:
            lines.append(f"CONFLICTS FOUND ({len(conflicts)}):")
            for c in conflicts:
                if isinstance(c, dict):
                    lines.append(f"  - {c.get('name','?')}: {c.get('url','')}")
                else:
                    lines.append(f"  - {c}")
        else:
            lines.append("No conflicts found.")
        for w in warnings:
            lines.append(f"  NOTE: {w}")
        lines.append("")

    _section("Trademark Search (USPTO)", search_results.get("uspto", {}))
    _section("Web Search (Google)", search_results.get("google", {}))
    _section("Apache Namespace", search_results.get("apache", {}))

    def _conflicts(key):
        d = search_results.get(key, {})
        return d if isinstance(d, list) else d.get("conflicts", [])

    all_conflicts = _conflicts("uspto") + _conflicts("google") + _conflicts("apache")
    lines.append("=== Summary ===")
    if all_conflicts:
        lines.append(
            f"FURTHER REVIEW REQUIRED: {len(all_conflicts)} conflict(s) found."
        )
    else:
        lines.append("CLEARED: No conflicts found. Name appears available for use.")

    return "\n".join(lines)


def PODLINGNAMESEARCH(name: str) -> str:
    """Run the full podling name clearance workflow end to end.

    Raises ValueError for names that fail validate_name so callers and the
    CLI can surface a non-zero exit. On success, writes
    '<name.lower()>_name_clearance.md' and returns the report string.
    """
    if not validate_name(name):
        raise ValueError(
            f"Invalid podling name {name!r}: must be non-empty, start with a "
            "letter, and contain only letters, digits, and hyphens."
        )

    search_results = perform_name_search(name)
    report = format_clearance_report(name, search_results)
    report = f"Name valid: YES\n\n" + report

    filename = f"{name.lower()}_name_clearance.md"
    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(report)

    return report


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <candidate-name>", file=sys.stderr)
        sys.exit(2)
    try:
        print(PODLINGNAMESEARCH(sys.argv[1]))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
