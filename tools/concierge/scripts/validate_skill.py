#!/usr/bin/env python3
"""Validate the Incubator Concierge skill before packaging.

The checks here exist because each one has already caused a real problem:

* A description over 1024 characters is rejected at install time, and the limit
  applies to the *folded* YAML value, not the raw source lines.
* A reference file named in SKILL.md but missing from the tree fails silently at
  runtime — the model simply never gets the routing table.
* Some sources are deliberately excluded (see EXCLUDED_SOURCES). Re-adding one
  by accident is a disclosure problem, not a style problem, so it fails the build.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_DESCRIPTION_CHARS = 1024
REQUIRED_FRONTMATTER = ("name", "description")

# Sources that must not appear in a shipped skill, with the reason shown on failure.
EXCLUDED_SOURCES = {
    "book": "the book MCP is not public; route concept questions to asf-policy and cwiki instead",
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def fold_scalar(raw: str) -> str:
    """Collapse a YAML folded block scalar the way a YAML parser would."""

    return " ".join(line.strip() for line in raw.strip().splitlines() if line.strip())


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md does not start with a --- frontmatter block")

    block = match.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []

    for line in block.splitlines():
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if key_match and not line.startswith((" ", "\t")):
            if current is not None:
                fields[current] = fold_scalar("\n".join(buffer))
            current = key_match.group(1)
            value = key_match.group(2).strip()
            buffer = [] if value in {">", "|", ">-", "|-", ""} else [value]
        elif current is not None:
            buffer.append(line)

    if current is not None:
        fields[current] = fold_scalar("\n".join(buffer))
    return fields


def check(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return [f"{skill_md} not found"]

    text = skill_md.read_text(encoding="utf-8")

    try:
        fields = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    for key in REQUIRED_FRONTMATTER:
        if not fields.get(key):
            errors.append(f"frontmatter is missing a non-empty '{key}'")

    description = fields.get("description", "")
    if description:
        length = len(description)
        if length > MAX_DESCRIPTION_CHARS:
            errors.append(
                f"description is {length} characters; the limit is {MAX_DESCRIPTION_CHARS} "
                f"({length - MAX_DESCRIPTION_CHARS} over)"
            )
        else:
            print(f"  description: {length}/{MAX_DESCRIPTION_CHARS} characters")

    name = fields.get("name", "")
    if name and name != skill_dir.resolve().name:
        print(f"  note: frontmatter name '{name}' differs from directory '{skill_dir.resolve().name}'")

    # Every references/<file>.md mentioned in SKILL.md must exist.
    referenced = sorted(set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text)))
    for filename in referenced:
        target = skill_dir / "references" / filename
        if target.is_file():
            print(f"  reference ok: references/{filename}")
        else:
            errors.append(f"SKILL.md refers to references/{filename}, which does not exist")
    if not referenced:
        print("  note: SKILL.md names no reference files")

    # Excluded sources must not be routed to anywhere in the skill.
    all_files = [skill_md, *sorted((skill_dir / "references").glob("*.md"))]
    for source, reason in EXCLUDED_SOURCES.items():
        pattern = re.compile(rf"`{re.escape(source)}[:`]|^\s*###\s+`?{re.escape(source)}`?\b", re.MULTILINE)
        for path in all_files:
            if pattern.search(path.read_text(encoding="utf-8")):
                rel = path.relative_to(skill_dir)
                errors.append(f"{rel} routes to the excluded source '{source}' — {reason}")

    return errors


def main(argv: list[str]) -> int:
    skill_dir = Path(argv[1] if len(argv) > 1 else ".")
    print(f"Validating skill in {skill_dir.resolve()}")
    errors = check(skill_dir)

    if errors:
        print("\nFAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nOK: skill is ready to package")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
