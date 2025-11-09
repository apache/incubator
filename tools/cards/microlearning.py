#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
microlearning.py
Convert ASF scenario cards JSON (cards.json) into a Harlowe (.twee) micro-course.

Explorable single-course edition with consistent navigation:
- Intro slide (concise) with soft styling; Story start = "Introduction"
- StoryMenu: Home | All Groups | Explore All Scenarios | Finish (gated)
- Explore All Scenarios (A–Z index, macro-free; A–E / F–J / K–O / P–T / U–Z)
- Breadcrumbs via Header
- Group pages:
  - Estimated time (configurable, shown as ranges)
  - Progress with strict completion (Discuss + Tips)
  - “Module Complete” banner at 100%
  - Mini-intro line
  - Thematic accent color per group
- Home page lists groups with estimated time, resume to first INCOMPLETE scenario
- Scenario pages: consistent nav styling, Discuss → All Tips link, prev/next within group, Back links use ◀

Usage:
  python3 microlearning.py --in cards.json --out apache_way_harlowe.twee --images-dir images
"""

import argparse
import json
import math
import re
import unicodedata
from pathlib import Path
from datetime import datetime
from collections import OrderedDict

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "scenario"

def esc(s: str) -> str:
    """Escape Twine link brackets and a few risky characters for passage/link safety."""
    if not s:
        return ""
    s = s.replace("[[", "&#91;&#91;").replace("]]", "&#93;&#93;")
    s = s.replace("|", "&#124;")            # avoid [[text|target]]
    s = s.replace("{", "&#123;").replace("}", "&#125;")  # avoid hooks
    return s.strip()

def find_image_file(images_dir: Path, slug: str):
    if not images_dir:
        return None
    for ext in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        cand = images_dir / f"{slug}{ext}"
        if cand.exists():
            return cand
    return None

def make_passage(name: str, body: str, tags=None, pos=None, size=None):
    """Emit a Twee passage with optional tags and visual editor metadata."""
    tag_brackets = f" [{' '.join(tags)}]" if tags else ""
    meta_parts = []
    if pos:
        meta_parts.append(f'"position":"{pos}"')
    if size:
        meta_parts.append(f'"size":"{size}"')
    meta_json = f" {{{','.join(meta_parts)}}}" if meta_parts else ""
    return f":: {name}{tag_brackets}{meta_json}\n{body.rstrip()}\n\n"

# ---------- Improved time estimation ----------
WORD_RE = re.compile(r"\b[\w’'-]+\b", re.UNICODE)

def _word_count(text: str) -> int:
    return len(WORD_RE.findall(text or ""))

def estimate_minutes_for_scenario(c: dict, *, mode: str, wpm: int,
                                  base_min: float, per_q: float, per_tip: float) -> float:
    """
    Returns a float minutes estimate for a single scenario.
    Priority: explicit override in JSON > selected mode.
    JSON override keys supported: 'estimate_min', 'estimateMinutes'
    """
    for key in ("estimate_min", "estimateMinutes"):
        if isinstance(c.get(key), (int, float)) and c[key] > 0:
            return float(c[key])

    summary = c.get("summary") or ""
    questions = [q for q in (c.get("questions") or []) if (q or "").strip()]
    path = [p for p in (c.get("path") or []) if (p or "").strip()]

    if mode == "off":
        return 0.0

    if mode == "simple":
        return max(base_min, base_min + per_q*len(questions) + per_tip*len(path))

    # mode == "word" (default)
    total_words = _word_count(summary) \
                  + sum(_word_count(q) for q in questions) \
                  + sum(_word_count(p) for p in path)
    read_min = total_words / max(60, wpm)  # clamp WPM floor
    interact_min = 0.25 * (len(questions) + len(path))
    return max(base_min, read_min + interact_min)

def _round5(n: float) -> int:
    return int(round(n / 5.0) * 5) if n >= 2.5 else max(1, int(round(n)))

# ---------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", required=True, help="cards.json input")
    ap.add_argument("--out", dest="outfile", default="apache_way_harlowe.twee", help="Twee output file")
    ap.add_argument("--title", dest="story_title", default="Practicing The Apache Way", help="StoryTitle text")
    ap.add_argument("--start", dest="start_passage", default="The Apache Way", help="Home passage name (kept)")
    ap.add_argument("--tag", dest="story_tag", default="TheApacheWay", help="Story tag for stylesheet demo")
    ap.add_argument("--images-dir", dest="images_dir", default="", help="Directory where images are stored (optional)")
    ap.add_argument("--harlowe-version", default="3.3.5", help="Harlowe story format version")

    # Time estimation controls
    ap.add_argument("--time-mode", choices=["off", "simple", "word"], default="word",
                    help="How to estimate time hints: off | simple | word (default: word)")
    ap.add_argument("--wpm", type=int, default=180,
                    help="Reading speed (words per minute) for --time-mode=word (default: 180)")
    ap.add_argument("--base-min", type=float, default=1.5,
                    help="Baseline minutes per scenario (simple mode and as a floor in word mode)")
    ap.add_argument("--per-question", type=float, default=0.75,
                    help="Extra minutes per question in simple mode (default: 0.75)")
    ap.add_argument("--per-tip", type=float, default=0.5,
                    help="Extra minutes per tip in simple mode (default: 0.5)")
    args = ap.parse_args()

    data = json.loads(Path(args.infile).read_text(encoding="utf-8"))
    scenarios = [c for c in data if (c.get("title") or "").strip()]
    if not scenarios:
        raise SystemExit("No scenarios in JSON. Expect 'title','summary','questions','path' and optional 'group'.")

    images_dir = Path(args.images_dir) if args.images_dir else None

    # Normalize groups (preserve input order)
    def norm_group(c):
        g = (c.get("group") or "").strip()
        return g if g else "Ungrouped"

    grouped = OrderedDict()
    for c in scenarios:
        g = norm_group(c)
        grouped.setdefault(g, [])
        grouped[g].append(c)

    # Prev/Next within each group
    group_prev, group_next = {}, {}
    for g, scen_list in grouped.items():
        titles = [(c.get("title") or "Untitled").strip() for c in scen_list]
        for idx, t in enumerate(titles):
            group_prev[t] = titles[idx-1] if idx > 0 else ""
            group_next[t] = titles[idx+1] if idx+1 < len(titles) else ""

    # Completion requires BOTH subpages visited
    def complete_expr_for_title(title_esc: str) -> str:
        return f'(visited: "Discuss: {title_esc}") and (visited: "Tips: {title_esc}")'

    # Titles (escaped) and visited-all expression
    all_titles = [esc((c.get("title") or "Untitled").strip()) for c in scenarios]
    visited_all_expr = " and ".join(complete_expr_for_title(t) for t in all_titles) if all_titles else "true"
    titles_array_literal = ", ".join(f'"{t}"' for t in all_titles)

    # Estimated minutes (group totals + ranges)
    group_minutes = {}         # float totals
    group_minutes_range = {}   # (lo, hi) rounded to ~5 min
    for g, scen_list in grouped.items():
        vals = [
            estimate_minutes_for_scenario(
                c,
                mode=args.time_mode,
                wpm=args.wpm,
                base_min=args.base_min,
                per_q=args.per_question,
                per_tip=args.per_tip
            )
            for c in scen_list
        ]
        total = sum(vals)
        group_minutes[g] = total
        if args.time_mode == "off":
            group_minutes_range[g] = (0, 0)
        else:
            lo = _round5(total * 0.8)
            hi = _round5(total * 1.2)
            lo = max(1, min(lo, hi)) if hi > 0 else 0
            group_minutes_range[g] = (lo, max(hi, lo))

    # A–Z buckets for index
    def bucket_label(ch: str) -> str:
        ch = (ch[:1] or "#").upper()
        if "A" <= ch <= "E": return "A–E"
        if "F" <= ch <= "J": return "F–J"
        if "K" <= ch <= "O": return "K–O"
        if "P" <= ch <= "T": return "P–T"
        return "U–Z"

    buckets = {"A–E": [], "F–J": [], "K–O": [], "P–T": [], "U–Z": []}
    for t in all_titles:
        buckets[bucket_label(t)].append(t)

    # Light thematic accent colors (cycled)
    accents = ["#e8f4ff", "#e8fff3", "#fff5e8", "#f3e8ff", "#ffe8f0", "#eef6ff", "#f6ffee"]
    group_accent = {}
    for i, g in enumerate(grouped.keys()):
        group_accent[g] = accents[i % len(accents)]

    # IFID
    now_ifid = "E54A9B5E-" + slugify(args.story_title + '-' + datetime.utcnow().isoformat())[:18].upper()

    parts = []

    # StoryTitle
    parts.append(f":: StoryTitle\n{args.story_title}\n\n")

    # StoryData (start at Introduction)
    story_start = "Introduction"
    storydata = {
        "ifid": now_ifid,
        "format": "Harlowe",
        "format-version": args.harlowe_version,
        "start": story_start,
        "zoom": 1
    }
    parts.append(":: StoryData\n" + json.dumps(storydata, ensure_ascii=False, indent=2) + "\n\n")

    # StoryMenu + Header
    parts.append(f":: StoryMenu\n[[Home|{esc(args.start_passage)}]] | [[All Groups|{esc(args.start_passage)}]] | [[Explore All Scenarios]] | (if: {visited_all_expr})[[Finish->End]]\n\n")
    parts.append(""":: Header
{
  (if: $crumbs is not set)[(set: $crumbs to (a:))]
  (if: $here is a string and ($crumbs's last is not $here))[(set: $crumbs to it + (a: $here))]
}
''You are here:'' (join: " › ", $crumbs)
\n\n""")

    # Stylesheet (readability + intro styling + group accents)
    css_lines = [f""":: StoryStylesheet [stylesheet]
tw-story[tags="{args.story_tag}"] {{
  background-image: url("open.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}}
tw-story[tags="End"] {{
  background-image: url("fireworks.gif");
  background-repeat: no-repeat;
  background-size: cover;
}}
tw-passage {{
  max-width: 68ch;
  margin: 0 auto;
  line-height: 1.5;
}}
tw-link {{
  padding: .2em .45em;
  border-radius: .25em;
}}
tw-link:hover {{ text-decoration: underline; }}
tw-passage img {{
  display: block;
  margin: 0 auto;
  max-width: 100%;
  max-height: 100%;
}}
/* Intro slide styling (no logo) */
tw-passage[aria-label="Introduction"] {{
  background: linear-gradient(to bottom right, #f9fafc 0%, #ffffff 100%);
  text-align: center;
  padding-top: 3em;
}}
tw-passage[aria-label="Introduction"] tw-link {{
  display: inline-block;
  margin-top: 2em;
  padding: 0.6em 1.2em;
  border-radius: 0.3em;
  background: #eaeef9;
  color: #002a5c;
  font-weight: 600;
}}
tw-passage[aria-label="Introduction"] tw-link:hover {{ background: #dde5f7; }}
"""]

    for g, color in group_accent.items():
        safe_g = esc(g)
        css_lines.append(f"""
/* Accent for Group: {safe_g} */
tw-passage[aria-label="Group: {safe_g}"] {{
  border-top: 4px solid {color};
  background-image: linear-gradient(to bottom, {color} 0%, rgba(255,255,255,0) 180px);
  background-repeat: no-repeat;
}}
""")
    parts.append("".join(css_lines) + "\n")

    # Explore All Scenarios (index)
    index_lines = [
        '(set: $here to "Explore All Scenarios")',
        "''Explore All Scenarios''",
        "//Tip: press Ctrl/Cmd + F to find by title.//",
        ""
    ]
    for label in ("A–E", "F–J", "K–O", "P–T", "U–Z"):
        index_lines.append("{" + label + "}")
        if buckets[label]:
            for t in buckets[label]:
                index_lines.append(f"* [[{t}->{t}]]")
        else:
            index_lines.append("_(none)_")
        index_lines.append("")
    parts.append(":: Explore All Scenarios\n" + "\n".join(index_lines) + "\n\n")

    # Introduction
    intro_body = """(set: $here to "Introduction")

(size:1.8)[Practicing The Apache Way]

Discover how Apache communities learn to govern themselves through collaboration, consensus, and transparency.  
These short scenarios show how podlings apply ASF culture in everyday decisions, from voting and branding to mentoring and community growth.

[[Start Learning->The Apache Way]]
"""
    parts.append(make_passage("Introduction", intro_body, pos="600,150", size="120,120"))

    # Home (Explorer hub)
    first_title = esc(scenarios[0].get("title", "Start"))
    start_lines = [
        "(set: $here to \"Home\")",
        "(size:1.8)[Understanding the Apache Way]",
        "",
        "Explore by topic area:",
        ""
    ]
    for g in grouped.keys():
        safe_g = esc(g)
        mins_lo, mins_hi = group_minutes_range.get(g, (0, 0))
        if mins_hi == 0:
            time_str = ""
        elif mins_lo == mins_hi:
            time_str = f" (~{mins_hi} min)"
        else:
            time_str = f" (~{mins_lo}–{mins_hi} min)"
        start_lines.append(f"* [[{safe_g}->Group: {safe_g}]]{time_str}")
    start_lines.append("* [[Explore All Scenarios]]")
    # Resume to FIRST INCOMPLETE (missing either Discuss or Tips)
    start_lines += [
        "",
        "(set: _cont to \"\")",
        f"(set: _order to (a: {titles_array_literal}))",
        "(for: each _t, ..._order)[(if: _cont is \"\")[ (if: not ((visited: \"Discuss: \" + _t) and (visited: \"Tips: \" + _t)))[ (set: _cont to _t) ]]]",
        "{(if: _cont is not \"\")[ (link-goto: \"Continue where I left off\", _cont) ](else:)[ [[Begin again->" + first_title + "]] ]}",
        "",
        f"(if: {visited_all_expr})[[Finish->End]]"
    ]
    parts.append(make_passage(args.start_passage, "\n".join(start_lines), tags=[args.story_tag], pos="600,250", size="120,130"))

    # Group pages
    for g, scen_list in grouped.items():
        safe_g = esc(g)
        titles = [esc((c.get("title") or "Untitled").strip()) for c in scen_list]
        titles_array = ", ".join(f'"{t}"' for t in titles)
        group_total = len(titles)
        mins_lo, mins_hi = group_minutes_range.get(g, (0, 0))

        glines = [
            f"(set: $here to \"Group: {safe_g}\")",
            f"(size:1.6)[{safe_g}]",
            "",
            f"//Scenarios in this theme help you practice {safe_g.lower()} in everyday ASF decision-making.//",
            "",
            (f"''Estimated time:'': ~{mins_lo}–{mins_hi} min" if mins_hi > 0 else "''Estimated time:'' —"),
            "",
            f"[[◀ Back to All Groups|{esc(args.start_passage)}]]",
            "",
            f"(set: _g to (a: {titles_array}))",
            "(set: _done to 0)",
            "(for: each _t, ..._g)[(if: (visited: \"Discuss: \" + _t) and (visited: \"Tips: \" + _t))[ (set: _done to _done + 1) ]]",
            f'(print: "Progress: " + (str: _done) + " / " + (str: {group_total}))',
            '(if: _done is ' + str(group_total) + ')[\n ✅ \'\'Module complete.\'\' You\'ve finished this theme.\n]',
            ""
        ]
        for t in titles:
            glines.append(f"* (if: (visited: \"Discuss: {t}\") and (visited: \"Tips: {t}\"))[✅] (else:)[◻] [[{t}->{t}]]")
        group_gate = " and ".join(complete_expr_for_title(t) for t in titles) if titles else "true"
        glines += ["", f"(if: {group_gate})[[Finish->End]]"]
        parts.append(make_passage(f"Group: {safe_g}", "\n".join(glines)))

    # Scenario pages + subpages
    base_x, base_y, dy = 600, 425, 125

    for i, c in enumerate(scenarios):
        title = (c.get("title") or "Untitled").strip()
        safe_title = esc(title)
        slug = slugify(title)
        group_name = norm_group(c)
        safe_group = esc(group_name)
        summary = esc((c.get("summary") or "").strip())
        questions = [esc(q) for q in (c.get("questions") or []) if q and q.strip()]
        path = [esc(p) for p in (c.get("path") or []) if p and p.strip()]
        img_path = find_image_file(images_dir, slug) if images_dir else None
        prev_in_group = esc(group_prev.get(title, "") or "")
        next_in_group = esc(group_next.get(title, "") or "")

        # Scenario main
        body_lines = [
            f"(set: $here to \"{safe_title}\")",
            f"(size:1.5)[{safe_title}]",
            f"''Group:'' {safe_group}",
            ""
        ]
        if img_path:
            body_lines += [f'<img src="{img_path.name}" alt="Illustration for {safe_title}">', ""]
        if summary:
            body_lines += [summary, ""]
        # Action links (no arrows)
        body_lines.append(f"[[Explore What You Would Do->Discuss: {safe_title}]]")
        body_lines.append(f"[[See Possible Mentor Approaches->Tips: {safe_title}]]")
        # Directional links (arrows)
        body_lines.append(f"[[◀ Back to {safe_group}|Group: {safe_group}]]")
        if prev_in_group:
            body_lines.append(f"[[◀ Previous in {safe_group}|{prev_in_group}]]")
        if next_in_group:
            body_lines.append(f"[[Next in {safe_group} ▶|{next_in_group}]]")
        body_lines.append(f"(if: {visited_all_expr})[[Finish->End]]")
        parts.append(make_passage(safe_title, "\n".join(body_lines), pos=f"{base_x},{base_y + i*dy}", size="100,100"))

        # Discuss
        d_lines = [
            f"(set: $here to \"Discuss — {safe_title}\")",
            f"(size:1.5)[Discuss — {safe_title}]",
            f"''Group:'' {safe_group}",
            "",
            "//Use these questions in a short thread; aim for lazy consensus then record the conclusion.//",
            ""
        ]
        if questions:
            for q in questions:
                d_lines.append(f"* {q}")
        else:
            d_lines.append("//No reflection questions available.//")
        # Action link (no arrow), then directional backs
        d_lines += [
            "",
            f"''Next:'' [[See Possible Mentor Approaches->Tips: {safe_title}]]",
            "",
            f"[[◀ Back to {safe_title}|{safe_title}]]",
            f"[[◀ Back to {safe_group}|Group: {safe_group}]]",
            f"(if: {visited_all_expr})[[Finish->End]]"
        ]
        parts.append(make_passage(f"Discuss: {safe_title}", "\n".join(d_lines)))

        # Tips
        t_lines = [
            f"(set: $here to \"All Tips — {safe_title}\")",
            f"(size:1.5)[All Tips — {safe_title}]",
            f"''Group:'' {safe_group}",
            "",
            "//These aren’t rules; pick the smallest next step that fits your context.//",
            ""
        ]
        if path:
            for step in path:
                t_lines.append(f"* {step}")
        else:
            t_lines.append("//No path-forward items available.//")
        t_lines += [
            "",
            f"[[◀ Back to {safe_title}|{safe_title}]]",
            f"[[◀ Back to {safe_group}|Group: {safe_group}]]",
            f"(if: {visited_all_expr})[[Finish->End]]"
        ]
        parts.append(make_passage(f"Tips: {safe_title}", "\n".join(t_lines)))

    # End
    end_body = """(set: $here to "End")
Congrats on completing this micro-course on the Apache Way!

For more on the Apache Way see (link: "The Apache Way")[(goto-url: "https://www.apache.org/theapacheway/")]."""
    parts.append(make_passage("End", end_body, tags=["End"], pos="600,900", size="100,100"))

    Path(args.outfile).write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {args.outfile} with {len(scenarios)} scenarios in {len(grouped)} groups.")

if __name__ == "__main__":
    main()
