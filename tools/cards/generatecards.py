#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASF Incubator Scenario Card Generator

This script converts an HTML page containing multiple scenario sections into
a printable two-sided (2-up duplex) PDF card set with an introductory overview,
grouped indexes, and front/back layouts for each scenario.

Each scenario is expected to follow a consistent structure in the HTML:
  - Headings labeled "Scenario: <title>"
  - Optional "Reflection questions" and "Possible path forward" subsections

Features:
  • Parses HTML headings and lists using BeautifulSoup
  • Extracts scenario summaries, reflection questions, and possible paths
  • Groups scenarios by the nearest preceding section heading
  • Outputs optional JSON data for verification or reuse
  • Generates a fully formatted ReportLab PDF with:
      - Introductory section
      - Per-group and full index pages
      - Duplex-ready two-sided scenario cards

Intended use:
  This tool supports ASF Incubator training and mentoring resources,
  creating printable cards for scenario-based learning (e.g., "Mentoring in Practice").

Example usage:
  python3 generatecards.py --infile scenarios.html --out cards.pdf --dump-json cards.json
"""


import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path
from bs4 import BeautifulSoup

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, FrameBreak,
    PageBreak, NextPageTemplate, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm

# ----------------------------
# Extraction (HTML)
# ----------------------------
SCEN_RE   = re.compile(r'^\s*Scenario\s*[:\-–]\s*(.+)$', re.I)
QUEST_RE  = re.compile(r'^\s*Reflection questions\b', re.I)
PATH_RE   = re.compile(r'^\s*Possible path forward\b', re.I)

def slugify(s: str) -> str:
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'[^a-zA-Z0-9\-]+', '', s)
    s = re.sub(r'-{2,}', '-', s)
    return s.strip('-').lower() or 'section'

def extract_from_html(html_file: Path):
    soup = BeautifulSoup(html_file.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    cards = []
    current_group = None  # track nearest preceding non-scenario heading

    for h in soup.find_all(re.compile(r'^h[1-6]$')):
        title_text = h.get_text(strip=True)
        if QUEST_RE.match(title_text) or PATH_RE.match(title_text):
            continue

        m = SCEN_RE.match(title_text)
        if not m:
            # treat as section/group heading
            current_group = title_text or None
            continue

        title = (m.group(1) or "").strip()
        current = {"title": title, "group": current_group, "summary": "", "questions": [], "path": []}
        node = h.find_next_sibling()
        mode = "summary"

        while node and not re.match(r'^h[1-6]$', (node.name or ''), re.I):
            text = node.get_text(" ", strip=True) if hasattr(node, "get_text") else ""
            if text:
                if QUEST_RE.search(text):
                    mode = "questions"
                elif PATH_RE.search(text):
                    mode = "path"
                else:
                    if mode == "summary":
                        if node.name in ("p", "div"):
                            if current["summary"]:
                                current["summary"] += " "
                            current["summary"] += text
                    elif mode == "questions":
                        if node.name in ("ul", "ol"):
                            for li in node.find_all("li", recursive=False):
                                t = li.get_text(" ", strip=True)
                                if t:
                                    current["questions"].append(t)
                    elif mode == "path":
                        if node.name in ("ul", "ol"):
                            for li in node.find_all("li", recursive=False):
                                t = li.get_text(" ", strip=True)
                                if t:
                                    current["path"].append(t)
            node = node.find_next_sibling()
        cards.append(current)
    return cards


# ----------------------------
# PDF builder with indexes and intro
# ----------------------------
def build_pdf(cards, out_pdf: Path):
    page_size = landscape(A4)
    doc = BaseDocTemplate(
        str(out_pdf), pagesize=page_size,
        leftMargin=15*mm, rightMargin=15*mm,
        topMargin=12*mm, bottomMargin=12*mm
    )

    gap = 10*mm
    frame_w = (page_size[0] - doc.leftMargin - doc.rightMargin - gap) / 2.0
    frame_h = page_size[1] - doc.topMargin - doc.bottomMargin

    left  = Frame(doc.leftMargin, doc.bottomMargin, frame_w, frame_h, id="left")
    right = Frame(doc.leftMargin + frame_w + gap, doc.bottomMargin, frame_w, frame_h, id="right")
    right_first = Frame(doc.leftMargin + frame_w + gap, doc.bottomMargin, frame_w, frame_h, id="right_first")
    left_second = Frame(doc.leftMargin, doc.bottomMargin, frame_w, frame_h, id="left_second")

    front = PageTemplate(id="front", frames=[left, right])
    back  = PageTemplate(id="back",  frames=[right_first, left_second])
    doc.addPageTemplates([front, back])

    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CardTitle",
        parent=styles["Heading2"],
        fontSize=15, leading=18,
        spaceAfter=2,
        textColor=colors.HexColor("#222222"),
    )
    group_label_style = ParagraphStyle(
        "GroupLabel",
        parent=styles["BodyText"],
        fontSize=8.7, leading=11,
        textColor=colors.HexColor("#666666"),
        backColor=colors.whitesmoke,
        leftIndent=0,
        rightIndent=0,
        borderPadding=(2, 4, 2, 4),
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "CardBody",
        parent=styles["BodyText"],
        fontSize=10.5, leading=13,
    )
    subhead_style = ParagraphStyle(
        "CardSubhead",
        parent=styles["Heading4"],
        fontSize=11, leading=14,
        textColor=colors.HexColor("#0F62FE"),
        spaceBefore=4, spaceAfter=2,
    )

    intro_title_style = ParagraphStyle(
        "IntroTitle",
        parent=styles["Heading1"],
        fontSize=18,
        leading=22,
        spaceAfter=10,
        textColor=colors.HexColor("#111111"),
    )
    intro_body_style = ParagraphStyle(
        "IntroBody",
        parent=styles["BodyText"],
        fontSize=11.5,
        leading=15,
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "IntroBullet",
        parent=styles["BodyText"],
        fontSize=11.5,
        leading=15,
        leftIndent=16,
        bulletIndent=6,
    )
    index_group_style = ParagraphStyle(
        "IndexGroup",
        parent=styles["Heading3"],
        fontSize=14,
        leading=18,
        spaceBefore=6,
        spaceAfter=4,
        textColor=colors.HexColor("#0F62FE"),
    )
    index_item_style = ParagraphStyle(
        "IndexItem",
        parent=styles["BodyText"],
        fontSize=11,
        leading=14,
        leftIndent=14,
    )

    # Assign anchors and groups
    def group_key(c): return c.get("group") or "Ungrouped"
    groups = OrderedDict()
    for i, c in enumerate(cards):
        c["_anchor"] = f"scen-{i+1:03d}"
        gname = group_key(c)
        groups.setdefault(gname, []).append(c)
    group_anchors = {g: f"group-{slugify(g)}" for g in groups.keys()}

    # --- Cards ---
    def front_card(c):
        flow = [
            Paragraph(f'<a name="{c["_anchor"]}"/>{c["title"]}', title_style),
            Paragraph(group_key(c), group_label_style),
            Paragraph((c["summary"] or "").strip() or "—", body_style),
            Spacer(1, 6),
            Paragraph("Discuss", subhead_style),
        ]
        if c["questions"]:
            for q in c["questions"]:
                flow.append(Paragraph(q, body_style, bulletText="•"))
        else:
            flow.append(Paragraph("—", body_style))
        return KeepTogether(flow)

    def back_card(c):
        flow = [
            Paragraph(c["title"], title_style),
            Paragraph(group_key(c), group_label_style),
            Paragraph("Possible path forward", subhead_style),
        ]
        if c["path"]:
            for step in c["path"]:
                flow.append(Paragraph(step, body_style, bulletText="•"))
        else:
            flow.append(Paragraph("—", body_style))
        return KeepTogether(flow)

    story = []

    # --- Introductory Page ---
    story.append(Paragraph("How Apache Communities Learn to Govern Themselves", intro_title_style))
    intro_paragraphs = [
        "At the Apache Software Foundation, governance emerges from collaboration, not authority. Projects thrive when contributors make decisions together, in public, and with respect for different perspectives. This is the culture that enables hundreds of Apache projects to evolve independently while sharing a common foundation: The Apache Way.",
        "In the Incubator, podlings learn to apply these principles in everyday practice. Mentors guide communities as they move from informal decisions to open discussion, from individual effort to shared ownership, and ultimately toward the self-governance expected of an Apache Project Management Committee (PMC).",
        "This guide shows how ASF culture is applied in practice. It covers how projects:"
    ]
    for p in intro_paragraphs:
        story.append(Paragraph(p, intro_body_style))
    bullet_items = [
        "build and record consensus through discussion and voting;",
        "develop trust through contribution and transparency (“trust through contribution”);",
        "handle conflict constructively and inclusively;",
        "balance independence with accountability; and",
        "protect user trust through privacy, branding, and policy awareness."
    ]
    for b in bullet_items:
        story.append(Paragraph(b, bullet_style, bulletText="•"))
    story.append(Paragraph(
        "The examples and scenarios are anonymized composites based on more than a decade of real ASF experiences drawn from public mailing lists. They illustrate what works, what doesn’t, and how communities learn by doing, from unclear votes to mentor disengagement to cultural misunderstandings.",
        intro_body_style))
    story.append(Paragraph(
        "Who this is for: Mentors, PPMC members, podling contributors, and future PMC members who seek practical guidance rooted in ASF norms.",
        intro_body_style))
    story.append(Paragraph(
        "What this is not: A policy manual. Official ASF policies are published elsewhere; this guide focuses on how to apply them in everyday project work.",
        intro_body_style))
    story.append(Paragraph(
        "Each discussion, vote, and release presents an opportunity to practice these values, build trust through contribution, and help a project evolve into a sustainable Apache community.",
        intro_body_style))
    story.append(PageBreak())

    # --- Index: All Groups ---
    story.append(Paragraph("Scenarios — All Groups", intro_title_style))
    for g in groups.keys():
        ga = group_anchors[g]
        story.append(Paragraph(f'• <a href="#{ga}">{g}</a>', index_item_style))
    story.append(PageBreak())

    # --- Per-group indexes ---
    for g, scen_list in groups.items():
        ga = group_anchors[g]
        story.append(Paragraph(f'<a name="{ga}"/>{g}', index_group_style))
        for c in scen_list:
            story.append(Paragraph(f'• <a href="#{c["_anchor"]}">{c["title"]}</a>', index_item_style))
        story.append(PageBreak())

    # --- Cards (2-up duplex) ---
    story.append(NextPageTemplate("front"))
    for i in range(0, len(cards), 2):
        pair = cards[i:i+2]

        # FRONT (left/right)
        if len(pair) >= 1:
            story.append(front_card(pair[0]))
        if len(pair) == 2:
            story.append(FrameBreak())
            story.append(front_card(pair[1]))

        # BACK
        story.append(NextPageTemplate("back"))
        story.append(PageBreak())
        if len(pair) >= 1:
            story.append(back_card(pair[0]))
        if len(pair) == 2:
            story.append(FrameBreak())
            story.append(back_card(pair[1]))

        # next
        story.append(NextPageTemplate("front"))
        story.append(PageBreak())

    if story and isinstance(story[-1], PageBreak):
        story.pop()

    doc.handle_nextPageTemplate("front")
    doc.build(story)
    print(f"Wrote {out_pdf} ({len(cards)} cards)")

# ----------------------------
# CLI
# ----------------------------
def main():
    ap = argparse.ArgumentParser(description="Generate 2-up duplex scenario cards with intro and group indexes.")
    ap.add_argument("--infile", required=True, help="Input HTML file")
    ap.add_argument("--out", default="scenario_cards.pdf", help="Output PDF")
    ap.add_argument("--dump-json", help="Also write extracted data to this JSON file")
    ap.add_argument("--no-pdf", action="store_true", help="Only dump JSON (skip PDF generation)")
    args = ap.parse_args()

    html_path = Path(args.infile).expanduser()
    if not html_path.exists():
        raise SystemExit(f"Input not found: {html_path}")

    cards = extract_from_html(html_path)
    if not cards:
        raise SystemExit("No scenarios found. Check headings like 'Scenario:', 'Reflection questions', 'Possible path forward'.")

    # JSON
    if args.dump_json:
        json_path = Path(args.dump_json)
        json_path.write_text(json.dumps(cards, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote JSON: {json_path} ({len(cards)} scenarios)")

    # PDF
    if not args.no_pdf:
        build_pdf(cards, Path(args.out))

if __name__ == "__main__":
    main()
