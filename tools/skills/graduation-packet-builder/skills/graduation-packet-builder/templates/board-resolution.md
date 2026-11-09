<!--
  ASF Board graduation resolution template for Apache Incubator podlings.
  Fill every {{placeholder}} from scratch/ before submitting to the board secretary.
  Required files: scratch/maturity.json, scratch/readiness.json,
                  scratch/community.json, scratch/releases.json
  Do NOT submit if release_count < 3 or name clearance_status == "conflicted".
-->

Establish the Apache {{PODLING}} Project

    WHEREAS, the Apache {{PODLING}} podling has been incubating under the
    Apache Software Foundation Incubator since {{incubating_since}}, a period
    of approximately {{months_in_incubation}} months; and

    WHEREAS, the podling has demonstrated maturity across the required dimensions:

      Releases: {{releases.release_count}} releases have been made on Apache
      distribution infrastructure, all with artifact names conforming to the
      Incubator naming policy (including the "incubating" identifier); the most
      recent release was {{releases.last_release_date}}; and

      Community diversity: the project has {{ppmc_diversity.unique_committers_12m}}
      unique committers over the past 12 months, a bus-factor-50% of
      {{ppmc_diversity.bus50}} committers, and {{ppmc_diversity.new_contributors}}
      new contributors; the PPMC draws from multiple independent organisations
      (multi-org verified: {{ppmc_diversity.multi_org_verified}}); and

      Community health: the project has filed {{report_history.total_reports_filed}}
      Incubator board reports, maintains active mailing lists at
      dev@{{resource}}.apache.org, and has sustained a dev@ poster count of
      {{ppmc_diversity.dev_unique_posters}} unique participants over the past
      12 months; and

      IP clearance: a Software Grant Agreement has been filed
      ({{ip_clearance.sga_filed}}), ICLAs are on file for all committers
      ({{ip_clearance.iclas_complete}}), and a Category A/B dependency audit
      has been completed ({{ip_clearance.category_audit_done}}), with no
      unresolved IP issues remaining; and

      Apache Infrastructure: the project uses ASF-hosted mailing lists
      ({{infrastructure.mailing_lists}}), source repository
      ({{infrastructure.source_repository}}), issue tracker
      ({{infrastructure.issue_tracker}}), website
      ({{infrastructure.website}}), and release distribution
      ({{infrastructure.distribution}}); and

      Name clearance: the proposed name "Apache {{PODLING}}" has been reviewed
      through the PODLINGNAMESEARCH process
      (JIRA: {{name_check.jira_ticket_url}}); VP Brand Management approval
      status: {{name_check.vp_brand_approved}}; and

    WHEREAS, the IPMC maturity assessment for Apache {{PODLING}} is
    "{{readiness.assessment}}" (confidence: {{readiness.confidence}}),
    with no unresolved graduation blockers; and

    WHEREAS, the podling's mentors have reviewed the graduation packet and
    recommend graduation (see mentor sign-offs below);

    NOW, THEREFORE, BE IT RESOLVED, that a Project Management Committee
    (PMC), to be known as the "Apache {{PODLING}} Project", be and hereby
    is established pursuant to the Bylaws of the Foundation, charged with
    the creation and maintenance of open-source software, for distribution
    at no charge to the public, related to {{PODLING_ONE_LINE_DESCRIPTION}};
    and be it further

    RESOLVED, that the following individuals are appointed to serve as the
    initial members of the Apache {{PODLING}} PMC:

      <!-- List each proposed PMC member on its own line. -->
      <!-- Confirm this list with mentors and PPMC before submitting. -->
      {{PMC_MEMBER_1_FULL_NAME}} ({{PMC_MEMBER_1_APACHE_ID}})
      {{PMC_MEMBER_2_FULL_NAME}} ({{PMC_MEMBER_2_APACHE_ID}})
      <!-- ... add all members ... -->

    and be it further

    RESOLVED, that {{PMC_CHAIR_FULL_NAME}} ({{PMC_CHAIR_APACHE_ID}}) be
    appointed to the position of initial Vice President and Chair of the
    Apache {{PODLING}} PMC, to serve in accordance with the Bylaws of the
    Foundation; and be it further

    RESOLVED, that the Apache {{PODLING}} PMC is requested to establish a
    project home page at https://{{resource}}.apache.org/; and be it further

    RESOLVED, that the Apache {{PODLING}} PMC is requested to provide the
    Board of Directors with a quarterly report beginning with the
    {{FIRST_REPORT_MONTH_YEAR}} board meeting; and be it further

    RESOLVED, that all responsibilities pertaining to the Apache {{PODLING}}
    podling currently held by the Apache Incubator PMC are henceforth
    assigned to the newly-established Apache {{PODLING}} Project Management
    Committee; and be it further

    RESOLVED, that the Apache Incubator PMC is requested to provide the
    Board of Directors with a final report on the Apache {{PODLING}} podling
    within three months of this graduation.

---
<!-- Mentor sign-offs — each sponsoring mentor must review and approve
     the graduation packet before the resolution is submitted.        -->

Mentor sign-offs for Apache {{PODLING}} graduation:

  [ ] {{MENTOR_1_NAME}} ({{MENTOR_1_APACHE_ID}})
      Date reviewed: ___________
      Comments: ___________

  [ ] {{MENTOR_2_NAME}} ({{MENTOR_2_APACHE_ID}})
      Date reviewed: ___________
      Comments: ___________

  <!-- Add one block per mentor listed in podlings.xml for this podling. -->

<!-- Shepherd confirmation -->
Graduation packet assembled by: {{SHEPHERD_NAME}} ({{SHEPHERD_APACHE_ID}})
Packet assembly date: {{PACKET_DATE}}
DISCUSS thread: https://lists.apache.org/thread/{{DISCUSS_THREAD_ID}}
VOTE thread:    https://lists.apache.org/thread/{{VOTE_THREAD_ID}}
