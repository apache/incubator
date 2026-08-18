#!/usr/bin/env python3
"""Compile skill directories into distributable .skill files.

A .skill file is a zip archive whose entries live under the skill's folder
name (skill-name/SKILL.md, skill-name/templates/..., ...) — the format the
Claude apps accept for installing a skill.

Works with both layouts:
  - a flat single-file skill: <skill-name>.md, with any supporting files in
    sibling shared directories keyed by skill name --
        scripts/<skill-name>/...      -> <skill-name>/scripts/... in the package
        templates/<skill-name>/...    -> <skill-name>/templates/...
        references/<skill-name>/...   -> <skill-name>/references/...
  - a skill DIRECTORY containing SKILL.md plus its own templates/scripts

Usage:
    python3 package-skills.py <skill-dir-or-md> [more...]
    python3 package-skills.py --all [SOURCE-DIR]

--all scans SOURCE-DIR (default: this script's directory) for every
*/SKILL.md directory and every top-level flat skill *.md, and compiles each
one. Output always lands in dist/ next to this script, so you can keep the
compiled packages in one place and the sources somewhere else:

    python3 package-skills.py --all ~/path/to/skill-sources

Output: dist/<skill-name>.skill next to this script. Exit status is the
number of skills that failed to package (0 = all good).

Excluded from packages: __pycache__/, *.pyc, .DS_Store, node_modules/, and a
skill's root-level evals/ or output/ directories — evals live in the repo,
not in the shipped skill.
"""

import fnmatch
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
EXCLUDE_DIRS = {"__pycache__", "node_modules"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store"}
ROOT_EXCLUDE_DIRS = {"evals", "output"}


def validate(md: Path) -> str | None:
    """Return an error string, or None if the skill markdown looks valid."""
    if not md.is_file():
        return "no SKILL.md"
    text = md.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"\s*---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return "SKILL.md has no YAML frontmatter"
    front = m.group(1)
    for field in ("name:", "description:"):
        if not re.search(rf"^{field}", front, re.MULTILINE):
            return f"frontmatter missing {field.rstrip(':')}"
    return None


def should_exclude(arcname: Path) -> bool:
    parts = arcname.parts
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if len(parts) > 1 and parts[1] in ROOT_EXCLUDE_DIRS:
        return True
    if arcname.name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(arcname.name, pat) for pat in EXCLUDE_GLOBS)


def package(target: Path) -> bool:
    target = target.resolve()
    if target.is_dir():
        name = target.name
        md = target / "SKILL.md"
    else:
        name = target.stem
        md = target
    err = validate(md)
    if err:
        print(f"FAIL  {name}: {err}")
        return False
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{name}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        if target.is_dir():
            for f in sorted(target.rglob("*")):
                if not f.is_file():
                    continue
                arcname = f.relative_to(target.parent)
                if should_exclude(arcname):
                    continue
                zf.write(f, arcname)
        else:
            zf.write(target, Path(name) / "SKILL.md")
            # Pull in this skill's supporting files from the shared directories
            # beside it, so a single-file skill can still ship templates,
            # scripts or reference pages.
            for kind in ("scripts", "templates", "references"):
                shared = target.parent / kind / name
                if not shared.is_dir():
                    continue
                for f in sorted(shared.rglob("*")):
                    if not f.is_file():
                        continue
                    rel = f.relative_to(shared)
                    if should_exclude(Path(name) / kind / rel):
                        continue
                    zf.write(f, Path(name) / kind / rel)
    size_kb = out.stat().st_size / 1024
    print(f"OK    {out.relative_to(ROOT)}  ({size_kb:.0f} KB)")
    return True


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args and args[0] == "--all":
        if len(args) > 2:
            print("--all takes at most one source directory.")
            return 1
        src = Path(args[1]).expanduser().resolve() if len(args) == 2 else ROOT
        if not src.is_dir():
            print(f"Not a directory: {src}")
            return 1
        dirs = sorted(p.parent for p in src.glob("*/SKILL.md"))
        # A top-level .md counts as a flat skill only if it actually carries
        # skill frontmatter — otherwise it's a README, a todo list, or some
        # other stray document that would report as a spurious failure.
        flat = sorted(
            p for p in src.glob("*.md")
            if p.name.lower() != "readme.md"
            and p.parent.name != "draft"
            and validate(p) is None
        )
        dirs = dirs + flat
        if not dirs:
            built = len(list(src.glob("*.skill")))
            print(f"No skill sources found in {src}")
            if built:
                print(
                    f"  ({built} compiled .skill package(s) are here, but nothing to\n"
                    f"   compile FROM — sources are <skill-name>/SKILL.md directories.)"
                )
            print("  Point --all at the directory holding the skill sources, e.g.:")
            print("    python3 package-skills.py --all ~/path/to/skill-sources")
            return 1
    else:
        dirs = [Path(a) for a in args]
    failures = sum(0 if package(d) else 1 for d in dirs)
    print(f"\n{len(dirs) - failures}/{len(dirs)} packaged into {DIST.relative_to(ROOT)}/")
    return failures


if __name__ == "__main__":
    sys.exit(main())
