# Apache Incubator — Podling Health Script

This script generates **health summaries** for Apache Incubator podlings by comparing activity across three rolling windows: **3 months, 6 months, and 12 months**.  
It is intended to provide mentors, PPMCs, and the IPMC with quick indicators of project momentum and trends over time.

It highlights **relative changes** across short-, medium-, and long-term windows.

---

## What it produces

- Markdown or CSV reports with podling health data
- For each podling, typical fields include:
  - Release count and cadence across 3m / 6m / 12m
  - Mailing list traffic (dev@, general@) and unique posters
  - Median merge/review times
  - GitHub activity (contributors, PRs, issues)
  - Diversity indicators (reviewer spread, PR authorship)
  - Trend arrows (↗, ↘, →) comparing windows

---

## Requirements

- **Python 3.10+**
- Packages: `requests`, `python-dateutil`, `tabulate`
- Optional: GitHub token (`GITHUB_TOKEN`) to raise API rate limits

Install dependencies:

    pip install -U requests python-dateutil tabulate

---

## Usage

    ./incubator_health.py --podling <podling> --minutes-dir <archived board agendas>

### Common flags

- `--out DIR`  
  Output directory for CSV/JSON/MD files (default: `./out`).

- `--md FILE`  
  Write Markdown health report.

- `--window-days N`  
  Override default window length. The script runs **3m, 6m, 12m** comparisons automatically; this sets the base window used for certain calculations.

- `--repos "org1/repo1,org2/repo2"`  
  Restrict GitHub analysis to given repos. If omitted, repos are discovered automatically.

- `--no-auto-repos`  
  Skip repo auto-discovery (useful when you only want curated repos).

- `--emit-repo-map FILE.json`  
  Export discovered repo mapping for inspection or reuse.

- `--debug`  
  Verbose logging.

---

## Output

### Typical data fields
- Release thread count per window  
- Median days between releases  
- Mailing list posts and unique posters  
- GitHub merges / reviews / open vs closed PRs and issues  
- Diversity indicators (reviewers, PR authors)

---

## How to use these results

The outputs are meant to **support podling reporting and mentor guidance**, not replace them.

- **Do not include the raw numbers in podling reports.**  
  Instead, provide **commentary** that explains what the data shows:
  - Why activity has increased, decreased, or stayed the same.  
  - Whether changes are due to planned pauses (holidays, conferences) or organic growth/decline.  
  - Any context mentors or the IPMC should be aware of.

- **Remember:** these indicators are heavily **developer-focused** (releases, PRs, commits, reviews).  
  Podling reports should also highlight **non-code contributions**:
  - Documentation and website improvements  
  - User support on mailing lists or chats  
  - Community events, talks, blog posts, outreach, etc.  
  - Broader ecosystem adoption or integrations

- **In podling reports**, aim to tell the **story of the community**, not just the activity metrics.  
  Use these results as a **cross-check** to help identify trends and prompt reflection.

For guidance on what podling reports should contain, see the [ASF Incubator reporting guide](https://cwiki.apache.org/confluence/display/INCUBATOR/Reporting+Guide).

## Interpreting results

- **Use trend arrows** to compare short (3m) vs medium (6m) vs long (12m) windows and spot growth or decline.  
- **Look for balance:** regular releases, sustained community activity, and diverse PR reviews are healthier signals. 
- **Check anomalies:** sudden drop-offs or spikes may warrant mentor follow-up.  
- **Consider proportionality:** raw numbers are less important than whether activity is steady and sustainable relative to project size.  
- **Watch diversity trends:** if contributions or reviews are concentrated in one individual or company, that is a risk even if numbers look strong.  
- **Look beyond developers:** mailing list traffic, discussions, and community participation are as important as GitHub stats.  
- **Cross-check signals:** consistent releases with declining discussions may indicate the project is becoming vendor-driven; high list activity with no releases may show process blockers.  
- **Use as a conversation starter:** results should guide mentoring discussions, not serve as a pass/fail score.  

> This script is **descriptive, not prescriptive** — it highlights relative trends and raw data. Human interpretation is essential. Reports should not copy these numbers directly; instead, provide commentary on *why* things have changed (or not changed), and balance the developer-focused metrics with observations on community health, inclusiveness, and broader participation.

---
