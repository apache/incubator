<!--
  Retirement announcement email template.
  Send AFTER a successful [VOTE] thread closes on general@incubator.apache.org.
  Fill every {{placeholder}} from scratch/stalled_evidence.json,
  scratch/consultation.json, and scratch/vote_result.txt before sending.

  Distribution:
    To:  dev@{{resource}}.apache.org
    CC:  general@incubator.apache.org
    BCC: announce@apache.org

  Note: announce@apache.org is a moderated broadcast list — the message will be
  held for VP of Infrastructure approval. Keep the body factual and concise;
  do not include opinions or editorialising.

  Send a separate copy to user@{{resource}}.apache.org if that list is active.
-->

To: dev@{{resource}}.apache.org
CC: general@incubator.apache.org
BCC: announce@apache.org
Subject: Apache {{PODLING}} (incubating) has been retired

Dear Apache {{PODLING}} community,

The Apache Incubator PMC has voted to retire Apache {{PODLING}} (incubating)
and move the project to the Apache Attic. This email is the official
announcement of that decision.

== Vote Result ==

A [VOTE] thread was held on general@incubator.apache.org from
{{vote_start_date}} to {{vote_close_date}}. The result was:

  Binding +1:  {{binding_plus1}}
  Binding  0:  {{binding_zero}}
  Binding -1:  {{binding_minus1}}

The vote passed with {{binding_plus1}} binding +1 vote(s) and no unresolved
binding -1 votes. The vote thread is archived at:
  {{vote_thread_url}}

== Reason for Retirement ==

Apache {{PODLING}} entered the Apache Incubator on {{start_date}} and has
been incubating for approximately {{months_incubating}} months. The decision
to retire was based on the following evidence of sustained inactivity:

  Commits ({{commits_window}}):        {{observed_commits}} (threshold: ≤ {{threshold_commits}})
  dev@ messages ({{mail_window}}):     {{observed_mail}} (threshold: ≤ {{threshold_mail}})
  Releases ({{releases_window}}):      {{observed_releases}} (threshold: {{threshold_releases}})

<!-- Include any additional stalled signals flagged in stalled_evidence.json:
  Additional IPMC signals: {{stalled_signal.definition_matched}}
-->

<!-- Include chronic issues if present:
  Chronic unresolved issues that recurred across multiple board reports:
    - {{chronic_issue_1}}
-->

The project did not produce a release on Apache distribution infrastructure
during the incubation period, and community activity fell below the level
required to sustain a healthy open-source project.

== What Happens Next ==

The project source code, mailing list archives, and issue tracker history
are being preserved in the Apache Attic:
  https://attic.apache.org/projects/{{resource}}.html

  Source code (read-only archive):
    https://gitbox.apache.org/repos/asf/{{resource}}.git

  Mailing list archives:
    dev@:     https://lists.apache.org/list.html?dev@{{resource}}.apache.org
    commits@: https://lists.apache.org/list.html?commits@{{resource}}.apache.org

The following infrastructure will be closed or made read-only:
  - Mailing lists: dev@, commits@, user@ (if active)
  - Issue tracker: {{issue_tracker_url}}
  - Website: {{website_url}} (redirected to the Attic project page)

== Thank You ==

We sincerely thank everyone who contributed to Apache {{PODLING}} during its
time in the Incubator — committers, contributors, mentors, and users. The
code and discussions remain available through the Attic for future reference.

If you have questions about the retirement process or the Attic, please
contact general@incubator.apache.org.

{{SHEPHERD_NAME}}
Apache Incubator PMC
