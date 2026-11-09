<!--
  Retirement DISCUSS email template.
  Fill every {{placeholder}} from scratch/stalled_evidence.json and
  scratch/consultation.json before posting.
-->

To: general@incubator.apache.org
Subject: [DISCUSS] Retire Apache {{PODLING}} (incubating)

Hi all,

After reviewing the evidence below, I would like to propose that we retire
Apache {{PODLING}} (incubating) and move it to the Apache Attic.

== Background ==

Apache {{PODLING}} has been in incubation since {{start_date}}
({{months_incubating}} months). Despite mentoring efforts, the project has
not demonstrated the sustained activity or release cadence needed to graduate.

== Stalled Evidence ==

Activity ({{best_window.date_range}}):
  Commits:             {{activity.commits}}  (threshold for concern: ≤ 5)
  Unique committers:   {{activity.unique_committers}}  (threshold: ≤ 1)
  Releases (12m):      {{activity.releases}}  (threshold: 0)
  dev@ unique posters: {{activity.dev_unique_posters}}

IPMC stalled signal: {{stalled_signal.summary}}
Signals matched: {{stalled_signal.definition_matched}}

IPMC active concerns:
  - {{concern_1}}
  - {{concern_2}}

<!-- If chronic issues exist:
Chronic unresolved issues (3+ consecutive reports):
  - {{chronic_issue_1}}
-->

== Community Engagement ==

Mentor contact attempts: {{consultation.contact_attempts_count}}
PPMC willing to continue: {{consultation.ppmc_willing_to_continue}}
Mentor recommendation: {{consultation.mentor_recommendation}}

Mentor list: {{mentors}}

== Proposed Action ==

We propose to retire Apache {{PODLING}} and move the project to the Apache
Attic (https://attic.apache.org). This involves:

  1. A [DISCUSS] thread on this list (this email) — 72-hour open window.
  2. A [VOTE] thread on this list requiring 3 binding +1s and no unresolved -1s.
  3. Archival steps (mailing lists, git repo, website, roster update).

If the PPMC wishes to continue instead, please respond in this thread within
72 hours with a concrete plan and a committed timeline.

== Call for Feedback ==

We invite all community members, mentors, and IPMC members to share their views:

  - Do you agree this podling meets the criteria for retirement?
  - Is there evidence of activity or plans we have not considered?
  - Do you support moving to a [VOTE] thread?

Thanks,
{{SHEPHERD_NAME}}
