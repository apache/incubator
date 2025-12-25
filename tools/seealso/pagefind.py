#!/usr/bin/env python3
"""
Generate search pages from YAML file
"""
import argparse
import html
import re
from pathlib import Path

import yaml  # pip install pyyaml


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def safe_filename_from_id(rid: str) -> str:
    rid = (rid or "").strip().lower()
    rid = re.sub(r"[^a-z0-9._-]+", "-", rid).strip("-")
    return (rid or "item") + ".html"


TYPE_ICONS = {
    "guide": "📘",
    "slides": "🖥️",
    "video": "🎞️",
    "quiz": "🧩",
    "scenario": "🧠",
    "interactive": "🎮",
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("yaml_path", help="Path to resources.yml")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--items-dir", default="_pagefind_items")
    args = ap.parse_args()

    yaml_path = Path(args.yaml_path).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    resources = data.get("resources", [])
    if not isinstance(resources, list):
        raise SystemExit("ERROR: resources.yml must contain top-level 'resources:' list")

    items_dir = out_dir / args.items_dir
    items_dir.mkdir(parents=True, exist_ok=True)

    for p in items_dir.glob("*.html"):
        p.unlink()

    for r in resources:
        rid = str(r.get("id", "")).strip()
        title = str(r.get("title", "")).strip()
        rtype = str(r.get("type", "")).strip().lower()
        url = str(r.get("url", "")).strip()
        desc_raw = str(r.get("description", "")).strip()

        if not rid or not title or not rtype or not url:
            raise SystemExit(f"ERROR: resource missing id/title/type/url: {r}")

        desc = desc_raw
        if desc.startswith(title):
            desc = desc[len(title):].lstrip(" .:-—")

        themes = [str(x).strip() for x in (r.get("themes") or []) if str(x).strip()]
        topics = [str(x).strip() for x in (r.get("topics") or []) if str(x).strip()]

        icon = TYPE_ICONS.get(rtype, "")
        display_title = f"{icon} {title}".strip() if icon else title

        html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="robots" content="noindex" />
  <title>{esc(title)}</title>
</head>
<body>

  <main data-pagefind-body>
    <h1 hidden aria-hidden="true">{esc(title)}</h1>
    <p>{esc(desc)}</p>
  </main>

  <div hidden aria-hidden="true">
    <span data-pagefind-meta="url">{esc(url)}</span>
    <span data-pagefind-meta="title">{esc(display_title)}</span>

    <span data-pagefind-filter="type">{esc(rtype)}</span>
    {''.join(f'<span data-pagefind-filter="theme">{esc(t)}</span>' for t in themes)}
    {''.join(f'<span data-pagefind-filter="topic">{esc(t)}</span>' for t in topics)}
  </div>

</body>
</html>
"""
        (items_dir / safe_filename_from_id(rid)).write_text(html_doc, encoding="utf-8")

    print(f"Wrote Pagefind items to {items_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())