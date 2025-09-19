#!/usr/bin/env python3
# podling_6mo_inject_from_csv.py
# Minimal injector: read rows from a CSV and produce:
#  - CSV summary (--out)
#  - Markdown table (--md)
#  - Per-podling review cards (--gen-cards)
#
# Note that this code is mostly AI generated.
#
# No web/API calls. Uses the field names listed in TEMPLATE_FIELDS below.
#

import argparse
import csv
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List
from tabulate import tabulate

TODAY = datetime.now(timezone.utc).date()

# Columns expected in input and emitted in outputs
TEMPLATE_FIELDS = [
    # Identity & core
    "podling","id","start_date","age_months","ppmc_count","committer_count",

    # Mentor metrics
    "mentors_count","reports_count","mentor_signoffs",

    # Mailing list activity
    "unique_posters","dev_emails",
    "dev_release_vote_threads","general_release_vote_threads","total_release_vote_threads",

    # GitHub metrics
    "github_contributors","github_open_issues","github_closed_issues",
    "github_open_prs","github_closed_prs","github_repos",

    # Growth
    "new_ppmc","new_committers",
]

def to_int(x, default=0):
    try:
        return int(x)
    except Exception:
        try:
            return int(float(x))
        except Exception:
            return default

def clamp02(x):
    return max(0, min(2, x))

def safe_div(n, d):
    n = float(n or 0)
    d = float(d or 0)
    return (n / d) if d else 0.0

def fmt_pct(x: float) -> str:
    try:
        return f"{(x*100):.0f}%"
    except Exception:
        return "0%"

def truthy_ratio_ok(site_checks_ok: str) -> bool:
    if not site_checks_ok:
        return False
    try:
        a, b = [int(s.strip()) for s in str(site_checks_ok).split("/", 1)]
        return b > 0 and (a / b) >= 0.6
    except Exception:
        return False

# --------- Suggested scoring (heuristic; human review required) ---------
def suggested_scores(row: Dict[str, Any]) -> Dict[str, int]:
    scores = {"community": 0, "governance": 0, "releases": 0, "mentors": 0, "risk": 0}

    # Core signals 
    up            = to_int(row.get("unique_posters"))
    dev_emails    = to_int(row.get("dev_emails"))
    committers    = to_int(row.get("committer_count"))
    ppmc          = to_int(row.get("ppmc_count"))
    age_mo        = to_int(row.get("age_months"))

    # Release votes
    dev_rel       = to_int(row.get("dev_release_vote_threads"))
    gen_rel       = to_int(row.get("general_release_vote_threads"))
    rel_total     = to_int(row.get("total_release_vote_threads"))

    # GitHub
    gh_contribs   = to_int(row.get("github_contributors"))
    gh_open_i     = to_int(row.get("github_open_issues"))
    gh_closed_i   = to_int(row.get("github_closed_issues"))
    gh_open_p     = to_int(row.get("github_open_prs"))
    gh_closed_p   = to_int(row.get("github_closed_prs"))
    gh_total      = gh_open_i + gh_closed_i + gh_open_p + gh_closed_p

    # Growth
    new_ppmc       = to_int(row.get("new_ppmc"))
    new_committers = to_int(row.get("new_committers"))
    new_core       = new_ppmc + new_committers

    # Mentors (all reports)
    mentors_count  = to_int(row.get("mentors_count"))
    reports_count  = to_int(row.get("reports_count"))
    signoffs_total = to_int(row.get("mentor_signoffs"))
    avg_signoffs   = safe_div(signoffs_total, reports_count)
    row["_avg_signoffs_per_report"] = f"{avg_signoffs:.2f}" if reports_count > 0 else ""

    # -------- Community Growth / Activity (tightened thresholds) --------
    # Evidence of broad engagement (posters/emails/GH) or concrete growth (new core)
    if (up >= 10) or (dev_emails >= 120) or (gh_contribs >= 15) or (new_core >= 3):
        scores["community"] = 2
    elif (up >= 10) or (dev_emails >= 40) or (gh_contribs >= 5) or (new_core >= 1):
        scores["community"] = 1
    else:
        scores["community"] = 0

    # -------- Governance & Culture (evidence-based) --------
    # Governance evidence = reports filed + mentor sign-offs; new PPMC as concrete action.
    if (reports_count >= 3 and avg_signoffs >= 2.0) or (new_ppmc >= 2):
        scores["governance"] = 2
    elif (reports_count >= 2 and avg_signoffs >= 1.0) or (new_ppmc >= 1):
        scores["governance"] = 1
    else:
        scores["governance"] = 0

    # -------- Releases & ASF Process (evidence-based) --------
    # 2 = dev@ release vote held; 1 = general@ mention OR process readiness (reports+sign-offs)
    if dev_rel >= 2:
        scores["releases"] = 2
    elif gen_rel >= 1 or (reports_count >= 3 and avg_signoffs >= 1.5):
        scores["releases"] = 1
    else:
        scores["releases"] = 0

    # -------- Mentor Engagement (0–2 by avg sign-offs per report) --------
    if reports_count > 3 and avg_signoffs >= 3.0:
        scores["mentors"] = 2
    elif reports_count > 3 and avg_signoffs >= 1.0:
        scores["mentors"] = 1
    else:
        scores["mentors"] = 0

    # -------- Risk (reverse: 0 = high risk, 2 = low risk) --------
    risk = 2

    # Growth: lack of new core members is a red flag (more penal as time passes)
    if age_mo >= 2 and new_core == 0:
        risk -= 1
    if age_mo >= 4 and new_core == 0:
        risk -= 1

    # Mentor coverage: penalise weak sign-offs only if there are reports to sign
    if reports_count >= 2 and avg_signoffs < 1.0:
        risk -= 1
    if reports_count >= 4 and avg_signoffs < 1.5:
        risk -= 1

    # Mailing lists: low participation
    if up < 3 and dev_emails < 40:
        risk -= 1
    if up == 0 and dev_emails < 10:
        risk -= 1

    # GitHub: very small footprint
    if gh_contribs < 3 and gh_total < 10:
        risk -= 1
    if gh_contribs == 0 and gh_total < 5:
        risk -= 1

    # Positive offsets
    if rel_total >= 1:
        risk += 1     # release vote is a strong positive
    if new_core >= 3:
        risk += 1     # strong growth

    scores["risk"] = clamp02(risk)
    return scores

def format_review_card(row: Dict[str, Any], sc: Dict[str, int], window_days: int) -> str:
    total = sum(sc.values())
    if total >= 10:
        cat = "On Track"
    elif total >= 6:
        cat = "Making Progress"
    else:
        cat = "At Risk"

    return f"""# Apache Incubator 6-Month Progress Review

**Podling:** {row.get('podling')}  
**Review Date:** {TODAY.isoformat()}  
**Reviewers:** [Mentors + 1–2 IPMC]  

---

## Scoring Guidance

Each category is scored **0–2**.  
- **0 = Not yet visible / needs support**  
- **1 = Emerging / developing**  
- **2 = Established / healthy**  

⚠️ **Note:** These scores are auto-suggested based on available data. They are **not definitive** and must be discussed and confirmed by mentors and IPMC reviewers.  

### Overall Rating
- **10–12 points** → **On Track** — Podling shows strong signals of community health and ASF alignment. Maintain the current pace and begin planning toward graduation milestones.  
- **6–9 points** → **Making Progress** — Podling is moving forward, but a few areas need extra attention. Work with mentors to set one to two clear goals for the next quarter.  
- **0–5 points** → **At Risk** — Key signals are missing or weak. Collaborate with mentors and the IPMC to agree on a short-term recovery plan. If challenges persist, re-evaluate the podling’s path.  

---

## Auto-filled Metrics (last {window_days} days)
- **Start Date:** {row.get('start_date')}  |  **Age:** {row.get('age_months')} months  
- **PPMC / Committers:** {row.get('ppmc_count')} / {row.get('committer_count')}  
- **New PPMC / Committers:** {row.get('new_ppmc', 0)} / {row.get('new_committers', 0)}  
- **Mentors / Reports / Sign-offs:** {row.get('mentors_count')} / {row.get('reports_count')} / {row.get('mentor_signoffs')}  
- **Unique Posters (dev@):** {row.get('unique_posters')}  
- **dev@ emails:** {row.get('dev_emails')}  
- **Release Votes:** dev@ {row.get('dev_release_vote_threads')} · general@incubator {row.get('general_release_vote_threads')} · **Total {row.get('total_release_vote_threads')}**  
- **GitHub:** contributors {row.get('github_contributors')} · issues open {row.get('github_open_issues')}, closed {row.get('github_closed_issues')} · PRs open {row.get('github_open_prs')}, closed {row.get('github_closed_prs')}  

---

## 1. Community Building (0–2)

**Suggested Score:** {sc['community']}  

**How to Score:**  
- **0** = Mostly proposers active  
- **1** = Some new contributors starting to join  
- **2** = Multiple new contributors and more than one org involved  

**Notes:**  

---

## 2. Decision-Making & Culture (0–2)

**Suggested Score:** {sc['governance']}  

**How to Score:**  
- **0** = Decisions mainly off-list or mentor/vendor-driven  
- **1** = Consensus emerging; participation uneven  
- **2** = Podling shows clear ASF-style decision making  

**Notes:**  

---

## 3. Releases & Process Alignment (0–2)

**Suggested Score:** {sc['releases']}  

**How to Score:**  
- **0** = No release yet  
- **1** = Preparing or in progress for first release  
- **2** = One or more incubating releases completed  

**Notes:**  

---

## 4. Mentor Support & Guidance (0–2)

**Suggested Score:** {sc['mentors']}  

**How to Score:**  
- **0** = Mentors not visibly engaged  
- **1** = Some mentor activity but inconsistent  
- **2** = Mentors active and supportive  

**Notes:**  

---

## 5. Sustainability & Risks (0–2, reverse scored)

**Suggested Score:** {sc['risk']}  

**How to Score:**  
- **0** = Clear risks (single vendor, very low activity)  
- **1** = Some concerns or uneven participation  
- **2** = No major risks identified  

**Notes:**  

---

## Final Score
- **Total:** {total} / 12  
- **Category:** {cat}  

### Summary Recommendation

Reviewers should:  
- Highlight the podling’s **key strengths and recent progress**  
- Identify **1–2 improvement areas** to focus on in the next 3–6 months  
- Confirm whether the suggested scores reflect the podling’s reality  

[Reviewer’s overall recommendation and suggested next steps]  

---

ℹ️ This review is a **mentoring tool**, not a pass/fail test.  

"""


# --------- Input & output ---------

def read_rows(inp: str) -> List[Dict[str, Any]]:
    rows = []
    with open(inp, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for raw in reader:
            # Ensure all expected fields exist (fill blanks for missing)
            row = {k: (raw.get(k, "") if raw.get(k, "") is not None else "") for k in TEMPLATE_FIELDS}
            # Sorting helper
            try:
                row["_age_sort"] = int(float(row.get("age_months") or 0))
            except Exception:
                row["_age_sort"] = 0
            rows.append(row)
    return rows

def main():
    ap = argparse.ArgumentParser(description="Inject <=6mo podling data from CSV into template outputs (no web calls).")
    ap.add_argument("--in", dest="inp", required=True, help="Input CSV with columns matching TEMPLATE_FIELDS.")
    ap.add_argument("--out", default="podlings_under6mo.csv", help="CSV output path")
    ap.add_argument("--md", default="podlings_under6mo.md", help="Markdown table output path")
    ap.add_argument("--gen-cards", default="", help="Directory to write per-podling Markdown review cards")
    ap.add_argument("--lists-activity", type=int, default=90, help="Label for the 'last Nd days' window printed on cards")
    args = ap.parse_args()

    rows = read_rows(args.inp)
    if not rows:
        print("No rows in input CSV.")
        return

    rows.sort(key=lambda r: (r["_age_sort"], r.get("start_date",""), r.get("podling","")))

    # Write normalized CSV (only the fields the template uses)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TEMPLATE_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in TEMPLATE_FIELDS})

    # Markdown table
    md_table = tabulate([[r.get(k, "") for k in TEMPLATE_FIELDS] for r in rows],
                        headers=TEMPLATE_FIELDS, tablefmt="github")
    with open(args.md, "w", encoding="utf-8") as f:
        f.write(md_table + "\n")

    print(f"Wrote {len(rows)} podlings → {args.out} and {args.md}")

    # Optional cards
    if args.gen_cards:
        outdir = Path(args.gen_cards)
        outdir.mkdir(parents=True, exist_ok=True)
        index_lines = ["# 6-Month Review Cards\n\n"]
        for r in rows:
            sc = suggested_scores(r)
            card_md = format_review_card(r, sc, args.lists_activity)
            fname = f"{r['id']}_6mo_review.md"
            (outdir / fname).write_text(card_md, encoding="utf-8")
            total = sum(sc.values())
            index_lines.append(f"- [{r['podling']}]({fname}) — suggested total: {total} / 12\n")
        (outdir / "index.md").write_text("".join(index_lines), encoding="utf-8")
        print(f"Review cards in: {outdir}/")

if __name__ == "__main__":
    main()
