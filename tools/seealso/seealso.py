#!/usr/bin/env python3
"""
Generate related resource links from resources.yml in Markdown format.

Grouped output example:

    [Vendor Neutrality](https://cwiki.apache.org/confluence/display/INCUBATOR/Vendor+Neutrality) - Guidance on ensuring balanced, community-led governance without single-vendor dominance. [Slide Deck](https://training.apache.org/presentations/apache/incubator/VendorNeutrality/index.html) [Video](https://youtu.be/WmmZYl3ZNr0)
    [Governance in Practice](https://cwiki.apache.org/confluence/display/INCUBATOR/Governance+in+Practice) - Shows how ASF values translate into day-to-day community decisions. [Slide Deck](https://training.apache.org/presentations/apache/incubator/Governance/index.html)

Usage:

    python seealso.py resources.yml CURRENT_RESOURCE_ID

    # Limit to 8 lines (8 grouped headings)
    python seealso.py resources.yml neutrality-in-practice --max 8

Expected YAML structure (one entry per resource):

- id: vendor-neutrality
  title: Vendor Neutrality
  type: guide              # one of: guide | slide | video | quiz | scenario
  themes: [neutrality, governance]
  topics: [vendor-neutrality, independence]
  description: "Ensures Apache projects are community-controlled..."
  url: https://cwiki.apache.org/...

The script:
- finds the resource with id == CURRENT_RESOURCE_ID
- uses its topics (and themes) as the "about" set
- excludes that resource from the output
- filters by positive relevance score
- sorts by score / type / title
- groups by exact title
- applies --max as a limit on the number of *lines* (groups)
- prints grouped Markdown lines
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: This script requires PyYAML. Install with: pip install pyyaml\n")
    sys.exit(1)


# Lower value = higher priority
TYPE_PRIORITY = {
    "guide": 0,
    "scenario": 1,
    "slide": 2,
    "video": 3,
    "quiz": 4,
}

TYPE_LABELS = {
    "guide": "Guide",
    "scenario": "Scenario",
    "slide": "Slide Deck",
    "video": "Video",
    "quiz": "Quiz",
}


def load_resources(path: Path):
    """Load resources from a YAML file."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, list):
        raise ValueError("resources.yml must contain a top-level list of resources")

    # Normalise some fields
    for r in data:
        r.setdefault("themes", [])
        r.setdefault("topics", [])
        r.setdefault("description", "")
        r.setdefault("type", "guide")
        r.setdefault("url", "")
        r.setdefault("id", "")
        r.setdefault("title", "")
    return data


def find_resource_by_id(resources, resource_id):
    """Return the resource dict with the given id, or None."""
    for r in resources:
        if r.get("id") == resource_id:
            return r
    return None


def compute_score(resource, about_topics, about_themes):
    """
    Compute a relevance score between a resource and the current guide's topics/themes.

    - topic overlap is weighted more heavily than theme overlap.
    """
    topics = set(resource.get("topics", []) or [])
    themes = set(resource.get("themes", []) or [])

    topic_overlap = len(topics & about_topics)
    theme_overlap = len(themes & about_themes)

    score = topic_overlap * 3 + theme_overlap * 1
    return score, topic_overlap, theme_overlap


def sort_resources(candidates, about_topics, about_themes):
    """Sort resources by score and type preference."""
    def sort_key(r):
        score, topic_overlap, theme_overlap = compute_score(r, about_topics, about_themes)
        type_priority = TYPE_PRIORITY.get(r.get("type", "guide"), 99)
        title = r.get("title", "")
        # Negative scores for descending order
        return (-score, -topic_overlap, -theme_overlap, type_priority, title.lower())

    return sorted(candidates, key=sort_key)


def format_grouped_line(title, resources_in_group):
    """
    Format a group of resources that share the same title into a single Markdown line:

        [Title](primary-url) - Description. [Slide Deck](...) [Video](...) [Quiz](...)

    Primary is usually the guide; extras become [Type] links.
    """
    if not resources_in_group:
        return ""

    # Pick primary resource (typically the guide) based on type priority, then title
    primary = sorted(
        resources_in_group,
        key=lambda r: (
            TYPE_PRIORITY.get(r.get("type", "guide"), 99),
            (r.get("title") or "").lower()
        )
    )[0]

    primary_url = (primary.get("url") or "").strip()
    desc = (primary.get("description") or "").strip()

    # If primary has no description, fall back to the first non-empty one in the group
    if not desc:
        for r in resources_in_group:
            d = (r.get("description") or "").strip()
            if d:
                desc = d
                break

    clean_title = (title or "").strip() or "Untitled"

    # First part: main link
    if primary_url:
        line = f"[{clean_title}]({primary_url})"
    else:
        line = clean_title

    if desc:
        line = f"{line} - {desc}"

    # Extra links for the rest of the group
    extras = [r for r in resources_in_group if r is not primary]

    if extras:
        extras_sorted = sorted(
            extras,
            key=lambda r: (
                TYPE_PRIORITY.get(r.get("type", "guide"), 99),
                (r.get("title") or "").lower()
            )
        )
        extra_parts = []
        for r in extras_sorted:
            r_type = (r.get("type") or "guide").lower()
            label = TYPE_LABELS.get(r_type, r_type.capitalize())
            url = (r.get("url") or "").strip()
            if url:
                extra_parts.append(f"[{label}]({url})")
            else:
                extra_parts.append(label)
        if extra_parts:
            line = f"{line} " + " ".join(extra_parts)

    return line


def generate_related_links(resources, current_id, max_items=8):
    """
    Generate Markdown link lines of related resources for the guide with current_id.

    Behaviour:
    - group by exact title
    - output one line per title
    - --max limits number of LINES (groups), not number of underlying resources
    """
    current = find_resource_by_id(resources, current_id)
    if current is None:
        raise ValueError(f"Resource id '{current_id}' not found in resources.yml")

    about_topics = set(current.get("topics", []) or [])
    about_themes = set(current.get("themes", []) or [])

    if not about_topics and not about_themes:
        # If nothing is tagged, we can't infer related items meaningfully
        return []

    # Exclude the current resource
    candidates = [r for r in resources if r.get("id") != current_id]

    # Filter by positive score only
    scored = []
    for r in candidates:
        score, _, _ = compute_score(r, about_topics, about_themes)
        if score > 0:
            scored.append(r)

    if not scored:
        return []

    sorted_resources = sort_resources(scored, about_topics, about_themes)

    # Group by title, preserving order of first appearance in sorted_resources
    groups = {}      # title -> list[resource]
    group_order = [] # list of titles

    for r in sorted_resources:
        title = (r.get("title") or "").strip() or "Untitled"
        if title not in groups:
            groups[title] = []
            group_order.append(title)
        groups[title].append(r)

    # Now produce lines, stopping after max_items groups
    lines = []
    for title in group_order[:max_items]:
        line = format_grouped_line(title, groups[title])
        if line:
            lines.append(line)

    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Generate related resource Markdown links from resources.yml."
    )
    parser.add_argument(
        "resources_file",
        help="Path to resources.yml"
    )
    parser.add_argument(
        "current_id",
        help="id of the current guide/resource (as listed in resources.yml)"
    )
    parser.add_argument(
        "--max",
        type=int,
        default=8,
        help="Maximum number of related resource lines to list (default: 8)"
    )

    args = parser.parse_args()

    resources_path = Path(args.resources_file)
    if not resources_path.is_file():
        sys.stderr.write(f"ERROR: resources file not found: {resources_path}\n")
        sys.exit(1)

    try:
        resources = load_resources(resources_path)
    except Exception as e:
        sys.stderr.write(f"ERROR: failed to load resources: {e}\n")
        sys.exit(1)

    try:
        lines = generate_related_links(
            resources=resources,
            current_id=args.current_id,
            max_items=args.max,
        )
    except Exception as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

    if not lines:
        sys.stderr.write("No related resources found for the given id/topics.\n")
        return

    # Print just the Markdown link lines
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
