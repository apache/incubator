#!/usr/bin/env python3
"""
Incubator Training Navigation Generator
"""

import yaml
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_YAML = SCRIPT_DIR / "resources.yml"

OUTPUT_DIR = SCRIPT_DIR.parents[1] / "pages" / "training"
THEMES_DIR = OUTPUT_DIR / "themes"
TOPICS_DIR = OUTPUT_DIR / "topics"

TYPE_ICONS = {
    "guide": "📘",
    "slides": "🖥️",
    "video": "🎞️",
    "quiz": "🧩",
    "scenario": "🧠",
}

ALLOWED_TYPES = set(TYPE_ICONS.keys())

ICON_LEGEND = (
    "Resource Types: "
    "📘 Guide  "
    "🖥️ Slide Deck  "
    "🎞️ Video  "
    "🧩 Quiz  "
    "🧠 Practice / Scenario\n"
)

LARGE_PAGE_THRESHOLD = 10
MIN_TOPIC_CLUSTER_SIZE = 3
MIN_CLUSTER_COVERAGE = 0.7

def load_yaml(path):
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def ensure_dirs():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

def make_header(title):
    return (
        f"= {title}\n"
        ":jbake-type: guide\n"
        ":jbake-status: published\n"
        "\n"
    )

def humanize_slug(slug):
    SPECIAL_CASES = {
        "clas": "CLAs",
    }

    if slug in SPECIAL_CASES:
        return SPECIAL_CASES[slug]

    ACRONYMS = {"ipmc", "pmc", "asf", "tlp", "ci", "api"}

    words = slug.split("-")
    out = []

    for word in words:
        if word.lower() in ACRONYMS:
            out.append(word.upper())
        else:
            out.append(word.capitalize())

    return " ".join(out)

def item_line(item):
    raw_type = item.get("type", "").lower()

    if raw_type and raw_type not in ALLOWED_TYPES:
        raise ValueError(
            f"Unknown resource type '{raw_type}' in resource '{item.get('title')}'"
        )

    icon = TYPE_ICONS.get(raw_type, "")
    icon_prefix = f"{icon} " if icon else ""

    return f"- {icon_prefix}link:{item['url']}[{item['title']}] - {item['description']}"

def write_page(path, title, description, items):
    content = make_header(title)
    content += ICON_LEGEND + "\n"

    if description:
        content += f"{description}\n\n"

    if len(items) <= LARGE_PAGE_THRESHOLD:
        for item in sorted(items, key=lambda x: x["title"].lower()):
            content += item_line(item) + "\n"
        content += "\n"
        path.write_text(content, encoding="utf-8")
        return

    grouped = defaultdict(list)
    for item in items:
        grouped[item.get("type", "")].append(item)

    section_order = ["guide", "slides", "video", "quiz", "scenario"]
    section_titles = {
        "guide": "Guides",
        "slides": "Slide Decks",
        "video": "Videos",
        "quiz": "Quizzes",
        "scenario": "Practice / Scenarios",
    }

    for key in section_order:
        if key not in grouped:
            continue

        section_items = sorted(grouped[key], key=lambda x: x["title"].lower())
        content += f"== {section_titles[key]}\n\n"

        if key != "guide" or len(section_items) <= LARGE_PAGE_THRESHOLD:
            for item in section_items:
                content += item_line(item) + "\n"
            content += "\n"
            continue

        topic_groups = defaultdict(list)
        for item in section_items:
            topics = item.get("topics", [])
            dominant = topics[0] if topics else "other"
            topic_groups[dominant].append(item)

        major_groups = {
            k: v for k, v in topic_groups.items()
            if len(v) >= MIN_TOPIC_CLUSTER_SIZE
        }

        total_guides = len(section_items)
        covered_by_major = sum(len(v) for v in major_groups.values())

        if len(major_groups) < 2 or covered_by_major < int(total_guides * MIN_CLUSTER_COVERAGE):
            for item in section_items:
                content += item_line(item) + "\n"
            content += "\n"
            continue

        used = set()

        for topic_id in sorted(major_groups.keys()):
            content += f"=== {humanize_slug(topic_id)}\n\n"
            for item in major_groups[topic_id]:
                used.add(id(item))
                content += item_line(item) + "\n"
            content += "\n"

        remaining = [i for i in section_items if id(i) not in used]
        if remaining:
            content += "=== Additional Guides\n\n"
            for item in remaining:
                content += item_line(item) + "\n"
            content += "\n"

    path.write_text(content, encoding="utf-8")

def write_themes_index(path, themes_map, theme_descriptions):
    lines = [make_header("Themes")]
    lines.append(ICON_LEGEND)
    lines.append("\nNavigation by theme.\n")

    for theme in sorted(themes_map.keys()):
        display = humanize_slug(theme)
        desc = theme_descriptions.get(theme, "")
        if desc:
            lines.append(f"- link:{theme}.html[{display}] - {desc}")
        else:
            lines.append(f"- link:{theme}.html[{display}]")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")

def write_topics_index(path, topics_map, topic_descriptions):
    lines = [make_header("Topics")]
    lines.append(ICON_LEGEND)
    lines.append("\nNavigation by topic.\n")

    for topic in sorted(topics_map.keys()):
        display = humanize_slug(topic)
        desc = topic_descriptions.get(topic, "")
        if desc:
            lines.append(f"- link:{topic}.html[{display}] - {desc}")
        else:
            lines.append(f"- link:{topic}.html[{display}]")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")

def main():
    data = load_yaml(INPUT_YAML)
    ensure_dirs()

    theme_descriptions = data.get("themes", {})
    topic_descriptions = data.get("topics", {})
    resources = data.get("resources", data)

    by_theme = defaultdict(list)
    by_topic = defaultdict(list)

    for item in resources:
        for theme in item.get("themes", []):
            by_theme[theme].append(item)
        for topic in item.get("topics", []):
            by_topic[topic].append(item)

    for theme in sorted(by_theme.keys()):
        filename = THEMES_DIR / f"{theme}.adoc"
        write_page(
            filename,
            f"Theme: {theme}",
            theme_descriptions.get(theme, ""),
            by_theme[theme],
        )

    for topic in sorted(by_topic.keys()):
        filename = TOPICS_DIR / f"{topic}.adoc"
        write_page(
            filename,
            f"Topic: {topic}",
            topic_descriptions.get(topic, ""),
            by_topic[topic],
        )

    write_themes_index(THEMES_DIR / "index.adoc", by_theme, theme_descriptions)
    write_topics_index(TOPICS_DIR / "index.adoc", by_topic, topic_descriptions)

    print("Navigation pages generated successfully")

if __name__ == "__main__":
    main()