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
MIN_CLUSTER_COVERAGE = 0.7  # 70%

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

    # Small page → flat list
    if len(items) <= LARGE_PAGE_THRESHOLD:
        items_sorted = sorted(items, key=lambda x: x["title"].lower())
        for item in items_sorted:
            content += item_line(item) + "\n"

        content += "\n"
        path.write_text(content, encoding="utf-8")
        return

    # Large page → split by TYPE
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
        title = section_titles[key]

        content += f"== {title}\n\n"

        # Only Guides are eligible for topic clustering
        if key != "guide" or len(section_items) <= LARGE_PAGE_THRESHOLD:
            for item in section_items:
                content += item_line(item) + "\n"
            content += "\n"
            continue

        # --- STRICT OPTION A GATING ---

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

        # ❌ Abort topic splitting unless it truly consolidates
        if len(major_groups) < 2 or covered_by_major < int(total_guides * MIN_CLUSTER_COVERAGE):
            for item in section_items:
                content += item_line(item) + "\n"
            content += "\n"
            continue

        # ✅ Perform consolidated topic split
        used_items = set()

        for topic_id in sorted(major_groups.keys()):
            topic_title = topic_id.replace("-", " ").title()
            content += f"=== {topic_title}\n\n"

            for item in major_groups[topic_id]:
                used_items.add(id(item))
                content += item_line(item) + "\n"

            content += "\n"

        remaining_items = [i for i in section_items if id(i) not in used_items]

        if remaining_items:
            content += "=== Additional Guides\n\n"
            for item in remaining_items:
                content += item_line(item) + "\n"
            content += "\n"

    path.write_text(content, encoding="utf-8")

def write_themes_index(path, themes_map, theme_descriptions):
    lines = [make_header("Themes")]
    lines.append(ICON_LEGEND)
    lines.append("\nNavigation by theme.\n")

    for theme in sorted(themes_map.keys()):
        desc = theme_descriptions.get(theme, "")
        if desc:
            lines.append(f"- link:{theme}.html[{theme}] - {desc}")
        else:
            lines.append(f"- link:{theme}.html[{theme}]")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")

def write_topics_index(path, topics_map, topic_descriptions):
    lines = [make_header("Topics")]
    lines.append(ICON_LEGEND)
    lines.append("\nNavigation by topic.\n")

    for topic in sorted(topics_map.keys()):
        desc = topic_descriptions.get(topic, "")
        if desc:
            lines.append(f"- link:{topic}.html[{topic}] - {desc}")
        else:
            lines.append(f"- link:{topic}.html[{topic}]")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")

def main():
    print("Loading YAML from:", INPUT_YAML.resolve())
    print("Output directory:", OUTPUT_DIR.resolve())

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
        items = by_theme[theme]
        filename = THEMES_DIR / f"{theme}.adoc"
        description = theme_descriptions.get(theme, "")
        write_page(filename, f"Theme: {theme}", description, items)

    for topic in sorted(by_topic.keys()):
        items = by_topic[topic]
        filename = TOPICS_DIR / f"{topic}.adoc"
        description = topic_descriptions.get(topic, "")
        write_page(filename, f"Topic: {topic}", description, items)

    write_themes_index(THEMES_DIR / "index.adoc", by_theme, theme_descriptions)
    write_topics_index(TOPICS_DIR / "index.adoc", by_topic, topic_descriptions)

    print("Navigation pages generated successfully")

if __name__ == "__main__":
    main()