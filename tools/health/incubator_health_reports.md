# Sample Incubator Health Report (Illustrative)

This report shows how automated health script outputs can be turned into clear, ready-to-use assessments for the Incubator PMC. The aim is to provide mentors and the IPMC with additional information to support podling self-reports. These reports highlight trends in releases, contributions, community activity, and diversity, enabling early detection of strengths and risks. They are meant to start conversations, not to judge or rank podlings.

**⚠️ Important:** These indicators are **descriptive, not prescriptive**. They do not provide the full picture of a podling’s health. More context from within the community is always needed to interpret results, refine potential actions, or identify underlying issues such as vendor dominance, off-list decision-making, or community conflicts.  

---

# How to Read This Report

- The **summary table** provides a quick snapshot of relative health.  
- Each **podling write-up** offers more detail and suggests possible actions.  
- The **glossary** appendix explains key metrics used in the analysis.  
- The **appendices** (placeholders here) contain raw data for transparency.  

---

# Podling Summary Table

| Podling | Status          | Very Short Summary                                   |
|---------|-----------------|------------------------------------------------------|
| A       | Healthy         | Balanced: steady releases, active code + community.  |
| B       | Stalled         | Very low activity, no releases, minimal engagement.  |
| C       | Slowing         | Still active, but fewer new contributors, backlog.   |
| D       | Community-light | Strong code velocity, but weak mailing list activity |

---

### Category Definitions

- **Healthy** → balanced code and community activity, with sustained releases and broad participation.  
- **Stalled** → little or no visible progress in releases, contributions, or discussions.  
- **Slowing** → activity continues but at a reduced pace, with fewer new contributors and backlog risks.  
- **Community-light** → technically strong but with weak mailing list engagement, raising transparency concerns.  

---

## Podling A

See **Appendix A** for raw script output.

**Report**  

The project is progressing well, with a steady release cadence, a growing contributor and committer base, and high development activity. Pull requests are merged quickly, and participation on the mailing list is broad, indicating a healthy balance between technical output and community engagement.  

Areas to watch include diversity and bus factor (signs of contribution concentration), as well as an emerging gap between issues opened and closed. These do not currently pose a threat to overall health, but they merit monitoring.

**Possible Actions**  

Encourage wider review and merge participation; consider **voting in new committers** to spread responsibility; share ownership of issue triage; highlight non-code contributions to reinforce balance and sustain participation.

---

## Podling B

See **Appendix B** for raw script output.

**Report**  

Activity has been very limited, with no recent releases, minimal code contributions, and a small number of active committers and reviewers. Mailing list participation is sparse, and merged pull requests have taken a considerable amount of time, suggesting low responsiveness. Required Incubator reports are being filed with mentor sign-offs; however, overall momentum appears to be stalled.

**Possible Actions**  

Re-energize participation by inviting previous contributors back, recruiting new participants, and publishing a concrete release plan. Improve responsiveness to PRs and issues. If momentum cannot be regained, mentors and the community may need to **consider whether to continue incubation or retire the podling**.

---

## Podling C

See **Appendix C** for raw script output.

**Report**  

The project remains active, with a recent release, and ongoing contribution, and visible mailing list discussions. Compared to earlier periods, activity has slowed: there are fewer new contributors, fewer commits, and issues are opening faster than they are closing, which risks backlog growth. The trend suggests momentum may be softening rather than failing.

**Possible Actions**  

Invest in onboarding (better documentation, mentoring newcomers), schedule regular issue triage to balance the backlog, and distribute responsibilities more evenly across committers to avoid bottlenecks and maintain motivation.

---

## Podling D

See **Appendix D** for raw script output.

**Report**  

Technical momentum is strong, driven by high PR throughput and extremely fast turnaround on contributions. The contributor and committer numbers are solid, and the bus factor appears stable. The key weakness is community visibility. Mailing list activity is very low relative to the code volume, suggesting that collaboration may be occurring elsewhere, which raises concerns about transparency.

**Possible Actions**  

Encourage **moving architectural and design discussions onto the dev@ list** and summarizing decisions there. Invite wider participation in list discussions to strengthen community health. While releases have occurred recently, cadence remains limited.

---

## Glossary of Metrics

- **Releases** → number of release vote thread recorded on mailing lists.  
- **Median days between releases** → indicator of release cadence.  
- **New contributors** → people contributing for the first time in the window. 
- **Unique committers** → distinct individuals with commit rights making contributions.  
- **Commits** → total commits recorded on GitHub during the window.  
- **Issues opened/closed** → activity on GitHub issues.  
- **PRs opened/merged** → pull request activity.  
- **Median PR time-to-merge** → average speed of processing contributions.  
- **Bus factor proxy (50% / 75%)** → number of contributors needed to account for half or three-quarters of commits; lower values = higher risk of concentration.  
- **Reviewer diversity (eff.#)** → effective number of reviewers (statistical diversity measure).  
- **PR author diversity (eff.#)** → effective number of distinct PR authors.  
- **Mailing list msgs / unique posters** → community engagement on dev@ lists.  
---

# Intended Use

These health reports are intended as inputs for **mentoring conversations and IPMC oversight**. They should not be treated as pass/fail scores. Possible uses include:  
- Informing review of podling reports.  
- Identifying where mentor attention may be useful.  
- Spotting broader trends across the Incubator.  

Ultimately, **mentor and community context** is essential to interpret the data and decide on appropriate actions.  

---

# Appendices

## Appendix A — Podling A Results (placeholder)

```markdown

## Trends (short vs medium)

- **Releases (from list votes/results):** 3 (—)
- **Median days between releases:** 32.5 (↗↗)
- **New contributors:** 21 (→)
- **Unique committers:** 41 (↗↗)
- **Commits:** 532 (→)
- **Issues opened/closed:** 88/54 (→/↘)
- **PRs opened/merged:** 647/537 (→/→)
- **Median PR time-to-merge (days):** 0.6 (↗↗)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 3 / 7 (↘↘/↘)
- **Mailing list msgs (dev@):** 690 (→)
- **Unique posters (dev@):** 49 (↗↗)
- **Reviewer diversity (eff.#, sampled):** 5.65 (↘↘)
- **PR author diversity (eff.#, sampled):** 8.33 (↘↘)
- **Unique reviewers (sampled):** 20 (↗↗)
- **Unique PR authors (sampled):** 22 (↗↗)

## Trends (short vs long)

- **Releases (from list votes/results):** 3 (—)
- **Median days between releases:** 32.5 (↗↗)
- **New contributors:** 21 (↗↗)
- **Unique committers:** 41 (↗↗↗)
- **Commits:** 532 (↗↗)
- **Issues opened/closed:** 88/54 (→/→)
- **PRs opened/merged:** 647/537 (↗↗/↗↗↗)
- **Median PR time-to-merge (days):** 0.6 (↘)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 3 / 7 (↘↘/↘)
- **Mailing list msgs (dev@):** 690 (↗)
- **Unique posters (dev@):** 49 (↗↗↗)
- **Reviewer diversity (eff.#, sampled):** 5.65 (↘↘)
- **PR author diversity (eff.#, sampled):** 8.33 (↘↘)
- **Unique reviewers (sampled):** 20 (↗↗↗)
- **Unique PR authors (sampled):** 22 (↗↗↗)

## Window Details
### 3m  (2025-06-27 → 2025-09-27)
- **Releases (from list votes/results):** 3  |  **Median gap (days):** 32.5
- **New contributors:** 21  |  **Unique committers:** 41  |  **Commits:** 532
- **Issues:** opened 88 / closed 54
- **PRs:** opened 647 / merged 537  |  **Median merge time (days):** 0.6
- **Reviews (sampled):** median reviewers/PR **1.0**  |  reviewer diversity (eff.#) **5.65**  |  PR author diversity (eff.#) **8.33**  |  unique reviewers **20**, unique authors **22**
- **Bus factor proxy (50% / 75%):** 3 / 7
- **Incubator reports:** 0  |  **Avg mentor sign-offs:** —
- **Mailing lists:** dev messages **690**, dev unique posters **49**

### 6m  (2025-03-27 → 2025-09-27)
- **Releases (from list votes/results):** 4  |  **Median gap (days):** 42
- **New contributors:** 38  |  **Unique committers:** 60  |  **Commits:** 990
- **Issues:** opened 184 / closed 123
- **PRs:** opened 1242 / merged 998  |  **Median merge time (days):** 0.9
- **Reviews (sampled):** median reviewers/PR **1**  |  reviewer diversity (eff.#) **8.82**  |  PR author diversity (eff.#) **12.91**  |  unique reviewers **27**, unique authors **32**
- **Bus factor proxy (50% / 75%):** 4 / 9
- **Incubator reports:** 1  |  **Avg mentor sign-offs:** 2.0
- **Mailing lists:** dev messages **1494**, dev unique posters **65**

### 12m  (2024-09-27 → 2025-09-27)
- **Releases (from list votes/results):** 5  |  **Median gap (days):** 51.0
- **New contributors:** 63  |  **Unique committers:** 79  |  **Commits:** 1628
- **Issues:** opened 359 / closed 213
- **PRs:** opened 1998 / merged 1000  |  **Median merge time (days):** 0.5
- **Reviews (sampled):** median reviewers/PR **1.0**  |  reviewer diversity (eff.#) **9.38**  |  PR author diversity (eff.#) **13.19**  |  unique reviewers **27**, unique authors **28**
- **Bus factor proxy (50% / 75%):** 4 / 8
- **Incubator reports:** 4  |  **Avg mentor sign-offs:** 2.0
- **Mailing lists:** dev messages **2265**, dev unique posters **79**

```

## Appendix B — Podling B Results (placeholder)

```markdown

## Trends (short vs medium)

- **Releases (from list votes/results):** 0 (—)
- **Median days between releases:** — (—)
- **New contributors:** 0 (—)
- **Unique committers:** 2 (—)
- **Commits:** 2 (—)
- **Issues opened/closed:** 2/0 (—/—)
- **PRs opened/merged:** 3/2 (—/—)
- **Median PR time-to-merge (days):** 132.3 (—)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 1 / 2 (↘↘/↘↘)
- **Mailing list msgs (dev@):** 2 (—)
- **Unique posters (dev@):** 2 (—)
- **Reviewer diversity (eff.#, sampled):** 2.0 (—)
- **PR author diversity (eff.#, sampled):** 2.0 (—)
- **Unique reviewers (sampled):** 2 (—)
- **Unique PR authors (sampled):** 2 (—)

## Trends (short vs long)

- **Releases (from list votes/results):** 0 (—)
- **Median days between releases:** — (—)
- **New contributors:** 0 (—)
- **Unique committers:** 2 (—)
- **Commits:** 2 (—)
- **Issues opened/closed:** 2/0 (—/—)
- **PRs opened/merged:** 3/2 (—/—)
- **Median PR time-to-merge (days):** 132.3 (—)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 1 / 2 (↘↘/↘↘)
- **Mailing list msgs (dev@):** 2 (—)
- **Unique posters (dev@):** 2 (—)
- **Reviewer diversity (eff.#, sampled):** 2.0 (—)
- **PR author diversity (eff.#, sampled):** 2.0 (—)
- **Unique reviewers (sampled):** 2 (—)
- **Unique PR authors (sampled):** 2 (—)

## Window Details
### 3m  (2025-06-27 → 2025-09-27)
- **Releases (from list votes/results):** 0  |  **Median gap (days):** —
- **New contributors:** 0  |  **Unique committers:** 2  |  **Commits:** 2
- **Issues:** opened 2 / closed 0
- **PRs:** opened 3 / merged 2  |  **Median merge time (days):** 132.3
- **Reviews (sampled):** median reviewers/PR **1.0**  |  reviewer diversity (eff.#) **2.0**  |  PR author diversity (eff.#) **2.0**  |  unique reviewers **2**, unique authors **2**
- **Bus factor proxy (50% / 75%):** 1 / 2
- **Incubator reports:** 1  |  **Avg mentor sign-offs:** 3.0
- **Mailing lists:** dev messages **2**, dev unique posters **2**

### 6m  (2025-03-27 → 2025-09-27)
- **Releases (from list votes/results):** 0  |  **Median gap (days):** —
- **New contributors:** 5  |  **Unique committers:** 5  |  **Commits:** 7
- **Issues:** opened 3 / closed 0
- **PRs:** opened 9 / merged 7  |  **Median merge time (days):** 206.3
- **Reviews (sampled):** median reviewers/PR **1**  |  reviewer diversity (eff.#) **1.81**  |  PR author diversity (eff.#) **4.45**  |  unique reviewers **3**, unique authors **5**
- **Bus factor proxy (50% / 75%):** 2 / 4
- **Incubator reports:** 2  |  **Avg mentor sign-offs:** 3.0
- **Mailing lists:** dev messages **3**, dev unique posters **3**

### 12m  (2024-09-27 → 2025-09-27)
- **Releases (from list votes/results):** 0  |  **Median gap (days):** —
- **New contributors:** 6  |  **Unique committers:** 6  |  **Commits:** 8
- **Issues:** opened 8 / closed 2
- **PRs:** opened 18 / merged 8  |  **Median merge time (days):** 210.2
- **Reviews (sampled):** median reviewers/PR **1.0**  |  reviewer diversity (eff.#) **1.81**  |  PR author diversity (eff.#) **5.33**  |  unique reviewers **3**, unique authors **6**
- **Bus factor proxy (50% / 75%):** 2 / 4
- **Incubator reports:** 2  |  **Avg mentor sign-offs:** 3.0
- **Mailing lists:** dev messages **7**, dev unique posters **4**

```

## Appendix C — Podling C Results (placeholder)

```markdown

## Trends (short vs medium)

- **Releases (from list votes/results):** 1 (—)
- **Median days between releases:** — (—)
- **New contributors:** 5 (↘↘)
- **Unique committers:** 30 (↗)
- **Commits:** 135 (↘↘)
- **Issues opened/closed:** 47/29 (↗/↗↗)
- **PRs opened/merged:** 114/100 (↘/→)
- **Median PR time-to-merge (days):** 6.0 (↘↘)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 4 / 9 (↗↗/↗↗)
- **Mailing list msgs (dev@):** 202 (↘)
- **Unique posters (dev@):** 22 (↗↗)
- **Reviewer diversity (eff.#, sampled):** 6.03 (→)
- **PR author diversity (eff.#, sampled):** 8.82 (→)
- **Unique reviewers (sampled):** 19 (↗↗)
- **Unique PR authors (sampled):** 21 (↗↗↗)

## Trends (short vs long)

- **Releases (from list votes/results):** 1 (—)
- **Median days between releases:** — (—)
- **New contributors:** 5 (↘↘)
- **Unique committers:** 30 (↗)
- **Commits:** 135 (↘↘)
- **Issues opened/closed:** 47/29 (↗/↗↗)
- **PRs opened/merged:** 114/100 (↘/→)
- **Median PR time-to-merge (days):** 6.0 (↘↘)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 4 / 9 (↗↗/↗↗)
- **Mailing list msgs (dev@):** 202 (↘)
- **Unique posters (dev@):** 22 (↗↗)
- **Reviewer diversity (eff.#, sampled):** 6.03 (→)
- **PR author diversity (eff.#, sampled):** 8.82 (→)
- **Unique reviewers (sampled):** 19 (↗↗)
- **Unique PR authors (sampled):** 21 (↗↗↗)

## Window Details
### 3m  (2025-06-27 → 2025-09-27)
- **Releases (from list votes/results):** 1  |  **Median gap (days):** —
- **New contributors:** 5  |  **Unique committers:** 30  |  **Commits:** 135
- **Issues:** opened 47 / closed 29
- **PRs:** opened 114 / merged 100  |  **Median merge time (days):** 6.0
- **Reviews (sampled):** median reviewers/PR **2.0**  |  reviewer diversity (eff.#) **6.03**  |  PR author diversity (eff.#) **8.82**  |  unique reviewers **19**, unique authors **21**
- **Bus factor proxy (50% / 75%):** 4 / 9
- **Incubator reports:** 0  |  **Avg mentor sign-offs:** —
- **Mailing lists:** dev messages **202**, dev unique posters **22**

### 6m  (2025-03-27 → 2025-09-27)
- **Releases (from list votes/results):** 1  |  **Median gap (days):** —
- **New contributors:** 14  |  **Unique committers:** 49  |  **Commits:** 627
- **Issues:** opened 75 / closed 45
- **PRs:** opened 253 / merged 204  |  **Median merge time (days):** 4.5
- **Reviews (sampled):** median reviewers/PR **2.0**  |  reviewer diversity (eff.#) **6.27**  |  PR author diversity (eff.#) **8.62**  |  unique reviewers **19**, unique authors **17**
- **Bus factor proxy (50% / 75%):** 3 / 6
- **Incubator reports:** 2  |  **Avg mentor sign-offs:** 1.0
- **Mailing lists:** dev messages **450**, dev unique posters **32**

```

## Appendix D — Podling D Results (placeholder)

```markdown

# Iggy — Incubator Health (Reports + GitHub + Mailing Lists)
_Generated on 2025-09-27_

**Windows:** 3m, 6m

## Trends (short vs medium)

- **Releases (from list votes/results):** 1 (—)
- **Median days between releases:** — (—)
- **New contributors:** 10 (↘)
- **Unique committers:** 22 (↗↗)
- **Commits:** 110 (→)
- **Issues opened/closed:** 51/48 (↘↘/↘↘)
- **PRs opened/merged:** 234/189 (↗/↗↗)
- **Median PR time-to-merge (days):** 0.1 (↗↗↗)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 3 / 7 (→/→)
- **Mailing list msgs (dev@):** 84 (→)
- **Unique posters (dev@):** 3 (—)
- **Reviewer diversity (eff.#, sampled):** 3.35 (→)
- **PR author diversity (eff.#, sampled):** 5.46 (↘)
- **Unique reviewers (sampled):** 8 (↗↗)
- **Unique PR authors (sampled):** 20 (↗↗↗)

## Trends (short vs long)

- **Releases (from list votes/results):** 1 (—)
- **Median days between releases:** — (—)
- **New contributors:** 10 (↘)
- **Unique committers:** 22 (↗↗)
- **Commits:** 110 (→)
- **Issues opened/closed:** 51/48 (↘↘/↘↘)
- **PRs opened/merged:** 234/189 (↗/↗↗)
- **Median PR time-to-merge (days):** 0.1 (↗↗↗)
- **Bus factor proxy (contributors to reach 50% / 75% of commits):** 3 / 7 (→/→)
- **Mailing list msgs (dev@):** 84 (→)
- **Unique posters (dev@):** 3 (—)
- **Reviewer diversity (eff.#, sampled):** 3.35 (→)
- **PR author diversity (eff.#, sampled):** 5.46 (↘)
- **Unique reviewers (sampled):** 8 (↗↗)
- **Unique PR authors (sampled):** 20 (↗↗↗)

## Window Details
### 3m  (2025-06-27 → 2025-09-27)
- **Releases (from list votes/results):** 1  |  **Median gap (days):** —
- **New contributors:** 10  |  **Unique committers:** 22  |  **Commits:** 110
- **Issues:** opened 51 / closed 48
- **PRs:** opened 234 / merged 189  |  **Median merge time (days):** 0.1
- **Reviews (sampled):** median reviewers/PR **2.0**  |  reviewer diversity (eff.#) **3.35**  |  PR author diversity (eff.#) **5.46**  |  unique reviewers **8**, unique authors **20**
- **Bus factor proxy (50% / 75%):** 3 / 7
- **Incubator reports:** 1  |  **Avg mentor sign-offs:** 3.0
- **Mailing lists:** dev messages **84**, dev unique posters **3**

### 6m  (2025-03-27 → 2025-09-27)
- **Releases (from list votes/results):** 2  |  **Median gap (days):** 114
- **New contributors:** 24  |  **Unique committers:** 31  |  **Commits:** 212
- **Issues:** opened 158 / closed 163
- **PRs:** opened 378 / merged 293  |  **Median merge time (days):** 0.2
- **Reviews (sampled):** median reviewers/PR **2.0**  |  reviewer diversity (eff.#) **3.45**  |  PR author diversity (eff.#) **7.19**  |  unique reviewers **9**, unique authors **19**
- **Bus factor proxy (50% / 75%):** 3 / 7
- **Incubator reports:** 4  |  **Avg mentor sign-offs:** 3.0
- **Mailing lists:** dev messages **172**, dev unique posters **7**

```

---