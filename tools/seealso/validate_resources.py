#!/usr/bin/env python3
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Validate resources.yml.

Checks that every resource is well formed and that every theme and topic it
claims is actually defined at the top of the file. An entry tagged with an
undefined theme or topic is silently dropped from the generated browse pages,
which is easy to introduce and hard to notice.

Note that a word may legitimately be both a theme and a topic, as 'branding'
and 'stewardship' are. That is a deliberate cross-listing, not an error. What
matters is only that whatever an entry claims is defined somewhere.

Usage:
    python3 validate_resources.py [path/to/resources.yml] [--strict]

Exit codes:
    0  no errors
    1  errors found, or warnings found when --strict is given
    2  the file could not be read or parsed
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

REQUIRED_FIELDS = ("id", "title", "type", "themes", "topics", "description", "url")
DEFAULT_PATH = pathlib.Path(__file__).with_name("resources.yml")


def load(path: pathlib.Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        sys.exit(f"cannot read {path}: {exc}")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        sys.exit(f"cannot parse {path}: {exc}")
    if not isinstance(data, dict):
        sys.exit(f"{path}: expected a mapping at the top level")
    for key in ("themes", "topics", "resources"):
        if key not in data:
            sys.exit(f"{path}: missing top-level '{key}'")
    return data


def check(data: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    themes = set(data["themes"])
    topics = set(data["topics"])
    resources = data["resources"]

    if not isinstance(resources, list):
        return ["'resources' must be a list"], []

    seen_ids: collections.Counter = collections.Counter()
    seen_urls: collections.Counter = collections.Counter()
    used_themes: set[str] = set()
    used_topics: set[str] = set()

    for position, resource in enumerate(resources, start=1):
        if not isinstance(resource, dict):
            errors.append(f"resource #{position}: expected a mapping")
            continue

        name = resource.get("id") or f"#{position} ({resource.get('title', 'untitled')})"

        for field in REQUIRED_FIELDS:
            if field not in resource:
                errors.append(f"{name}: missing '{field}'")
            elif resource[field] in (None, "", [], {}):
                errors.append(f"{name}: '{field}' is empty")

        if "id" in resource:
            seen_ids[resource["id"]] += 1

        url = resource.get("url", "")
        if url:
            seen_urls[url] += 1
            if not url.startswith(("http://", "https://")):
                errors.append(f"{name}: url is not absolute: {url}")

        for theme in resource.get("themes") or []:
            used_themes.add(theme)
            if theme not in themes:
                errors.append(f"{name}: undefined theme '{theme}'")
        for topic in resource.get("topics") or []:
            used_topics.add(topic)
            if topic not in topics:
                errors.append(f"{name}: undefined topic '{topic}'")

    for value, count in seen_ids.items():
        if count > 1:
            errors.append(f"duplicate id '{value}' used {count} times")
    for value, count in seen_urls.items():
        if count > 1:
            errors.append(f"duplicate url '{value}' used {count} times")

    for theme in sorted(themes - used_themes):
        warnings.append(f"theme '{theme}' is defined but no resource uses it")
    for topic in sorted(topics - used_topics):
        warnings.append(f"topic '{topic}' is defined but no resource uses it")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "path", nargs="?", type=pathlib.Path, default=DEFAULT_PATH,
        help="path to resources.yml (defaults to the one beside this script)",
    )
    parser.add_argument(
        "--strict", action="store_true", help="treat warnings as errors",
    )
    args = parser.parse_args()

    data = load(args.path)
    errors, warnings = check(data)

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    counts = (
        f"{len(data['resources'])} resources, "
        f"{len(data['themes'])} themes, "
        f"{len(data['topics'])} topics"
    )

    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s). {counts}")
        return 1
    if warnings and args.strict:
        print(f"\nFAILED under --strict: {len(warnings)} warning(s). {counts}")
        return 1
    print(f"OK: {counts}, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
