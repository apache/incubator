<!--
  Graduation DISCUSS email template.
  Fill every {{placeholder}} from the data in scratch/ before posting.
  Do NOT post if release_count < 3 or name clearance_status == "conflicted".
-->

To: general@incubator.apache.org
Subject: [DISCUSS] Graduate Apache {{PODLING}} (incubating)

Hi all,

We would like to propose that Apache {{PODLING}} (incubating) graduate to a
Top-Level Project (TLP).

== About Apache {{PODLING}} ==

{{PODLING_DESCRIPTION}}

== Maturity Evidence ==

--- PPMC Diversity ---
  Unique committers (12m):        {{ppmc_diversity.unique_committers_12m}}
  Bus factor 50% (12m):           {{ppmc_diversity.bus50}} (threshold ≥ 3)
  Bus factor 75% (12m):           {{ppmc_diversity.bus75}} (threshold ≥ 5)
  New contributors (12m):         {{ppmc_diversity.new_contributors}}
  PR-author diversity index:      {{ppmc_diversity.pr_author_div_eff}}
  Unique dev@ posters (12m):      {{ppmc_diversity.dev_unique_posters}}
  Multi-organisation PPMC:        {{ppmc_diversity.multi_org_verified}}
  Listed mentors:                 {{ppmc_diversity.mentor_count}}

  <!-- If diversity concerns exist, list them:
  Diversity concerns:
    - {{diversity_concern_1}}
  -->

--- IP Clearance ---
  SGA filed:                      {{ip_clearance.sga_filed}}
  ICLAs complete for all committers: {{ip_clearance.iclas_complete}}
  Category A/B audit done:        {{ip_clearance.category_audit_done}}
  Unresolved IP issues:           {{ip_clearance.unresolved_ip_issues}}

--- Releases on Apache Infrastructure ---
  Total releases:                 {{releases.release_count}} (minimum required: 3)
  All artifact names include "incubating": {{releases.naming_ok}}
  Most recent release:            {{releases.last_release_date}}
  Cadence:                        {{releases.cadence}}

  <!-- If naming violations exist, list them:
  Naming violations:
    - {{naming_violation_1}}
  -->

--- Apache Infrastructure ---
  Mailing lists (listserv.apache.org):         {{infrastructure.mailing_lists}}
  Source repository (gitbox / apache/ GitHub): {{infrastructure.source_repository}}
  Issue tracker (ASF JIRA or GitHub):          {{infrastructure.issue_tracker}}
  Website ({{PODLING_LOWER}}.apache.org):      {{infrastructure.website}}
  Distribution (dist.apache.org):              {{infrastructure.distribution}}

== Maturity Assessment ==

IPMC assessment: {{readiness.assessment}} (confidence: {{readiness.confidence}})

Strengths:
  - {{strength_1}}
  - {{strength_2}}

<!-- If blockers exist:
Open items to resolve before a vote:
  - {{blocker_1}}
-->

<!-- If recommended next steps exist:
Recommended next steps:
  - {{next_step_1}}
-->

== Community ==

Mailing list archives:
  dev@:              {{mail_archives.dev}}
  General Incubator: {{mail_archives.general_incubator}}

Board reports filed: {{report_history.total_reports_filed}}

<!-- If recurring issues exist:
Recurring open issues:
  - {{recurring_issue_1}}
-->

== Release History ==

Chronological releases ({{releases.release_count}} total, oldest first):

  #   Version                     Date          Incubating name?
  --- --------------------------- ------------- ----------------
  {{release_row_1}}
  {{release_row_2}}
  {{release_row_3}}
  <!-- add rows for each release from scratch/releases.json -->

Release votes on general@incubator: {{vote_evidence.vote_threads_found}} vote
thread(s), {{vote_evidence.result_threads_found}} result thread(s).

<!-- If release governance concerns exist:
Release governance concerns:
  - {{governance_concern_1}}
-->

== Name Clearance ==

  Status:                  {{name_check.clearance_status}}
  Automated check verdict: {{name_check.automated_verdict}}
  PODLINGNAMESEARCH JIRA:  {{name_check.jira_ticket_url}}
  VP Brand Management:     {{name_check.vp_brand_approved}}

  <!-- If status is "pending", add:
  Name clearance is pending; a [VOTE] will not be called until status is CLEARED.
  -->

== Maturity Model Checklist ==

Please review the podling's self-assessment on the Incubator wiki:
  https://cwiki.apache.org/confluence/display/INCUBATOR/{{PODLING_WIKI}}+Graduation+Status

== Proposed Initial PMC ==

  {{pmc_member_1}} (<Apache ID>)
  {{pmc_member_2}} (<Apache ID>)
  <!-- list all proposed PMC members; confirm with PPMC and mentors before posting -->

== Proposed Initial PMC Chair ==

  {{PROPOSED_CHAIR}} (<Apache ID>)

== Call for Feedback ==

We invite all community members, mentors, and IPMC members to review the
evidence above and share their thoughts:

  - Does the project meet the graduation criteria?
  - Are there any unresolved issues that should be addressed first?
  - Do you support moving to a [VOTE] thread on this list?

Please reply to this thread with your feedback. If there are no unresolved
objections after 72 hours, we will open a [VOTE] thread.

Thanks,
{{SHEPHERD_NAME}}
