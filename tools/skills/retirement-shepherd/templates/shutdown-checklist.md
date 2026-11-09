# Shutdown Checklist — Apache {{PODLING}} (incubating)

<!--
  Standalone shutdown checklist template for Apache Incubator podling retirement.
  Rendered by skills/retirement-shepherd.md Step 4 into scratch/shutdown_checklist.md.
  Replace every {{placeholder}} with podling-specific values before use.

  References:
    Apache Attic:   https://attic.apache.org
    ASF Infra JIRA: https://issues.apache.org/jira/projects/INFRA
    Attic JIRA:     https://issues.apache.org/jira/projects/ATTIC
    Incubator PMC:  general@incubator.apache.org
-->

Generated for: {{PODLING}}
Resource slug: {{resource}}
Mentors: {{mentors}}
Retirement vote passed: {{vote_close_date}}
Vote thread: {{vote_thread_url}}

Complete each item in order. Tick the checkbox when done.

---

## Phase 1 — Vote and announcement (before archival)

- [ ] Post `[DISCUSS]` thread on `general@incubator.apache.org` and wait 72 hours.
- [ ] Post `[VOTE]` thread on `general@incubator.apache.org`; requires ≥ 3 binding +1s,
      more +1s than -1s, and no unresolved -1s.
- [ ] Record vote result in `scratch/vote_result.txt` (binding counts, thread URL, dates).
- [ ] Post a `[RESULT][VOTE]` reply on `general@incubator.apache.org` citing the final tally.
- [ ] Send retirement announcement to `dev@{{resource}}.apache.org`
      (CC `general@incubator.apache.org`, BCC `announce@apache.org`).
      Use template: `templates/retirement/retirement-email.md`
- [ ] Send a separate copy to `user@{{resource}}.apache.org` if that list is active.

---

## Phase 2 — Repository archival

- [ ] Open an INFRA JIRA ticket requesting the git repository be made read-only:
      `https://gitbox.apache.org/repos/asf/{{resource}}.git`
      Subject: "Archive (read-only) Apache {{PODLING}} git repository"
- [ ] Confirm all commits and tags are pushed to the canonical ASF repository
      before archival is applied.
- [ ] Remove or disable active CI/build pipelines (GitHub Actions, Jenkins, etc.)
      attached to the repository.
- [ ] Verify the archived repository is accessible at:
      `https://gitbox.apache.org/repos/asf/{{resource}}.git`

---

## Phase 3 — Website redirect to the Attic

- [ ] Open an Attic JIRA ticket at `https://issues.apache.org/jira/projects/ATTIC`
      Subject: "Move Apache {{PODLING}} to the Apache Attic"
      Include: mailing list names, git repo URL, current website URL,
               JIRA project key, vote thread URL.
- [ ] Coordinate with the Attic PMC to create an Attic project page at:
      `https://attic.apache.org/projects/{{resource}}.html`
- [ ] Once the Attic page is live, redirect `{{website_url}}` to the Attic page
      via an INFRA JIRA ticket (DNS/httpd redirect).
      Subject: "Redirect {{resource}}.apache.org to attic.apache.org/projects/{{resource}}.html"
- [ ] Verify the redirect works in a browser.
- [ ] Remove or archive the website source from the CMS / git-based site repo
      if it is no longer maintained.

---

## Phase 4 — Mailing-list closure

- [ ] Open an INFRA JIRA ticket to close or archive all podling mailing lists:
      - `dev@{{resource}}.apache.org`
      - `commits@{{resource}}.apache.org`
      - `user@{{resource}}.apache.org` (if active)
      Subject: "Archive mailing lists for Apache {{PODLING}}"
- [ ] Confirm that list archives remain publicly accessible at:
      - `https://lists.apache.org/list.html?dev@{{resource}}.apache.org`
      - `https://lists.apache.org/list.html?commits@{{resource}}.apache.org`
- [ ] Remove any mailing-list subscription references from the project website
      (already being archived/redirected in Phase 3, but confirm no dangling links).

---

## Phase 5 — Issue-tracker decommissioning

- [ ] Open an INFRA JIRA ticket to set the issue tracker to read-only:
      - ASF JIRA project: `https://issues.apache.org/jira/projects/{{PODLING_UPPER}}`
      - GitHub Issues: `https://github.com/apache/{{resource}}/issues` (if used)
      Subject: "Set issue tracker read-only for Apache {{PODLING}}"
- [ ] Add a banner or description note to the issue tracker pointing to the Attic page.
- [ ] Remove any issue-tracker webhook integrations from the git repository.
- [ ] Confirm no open release-critical or security issues remain unresolved
      (if any, transfer to the Attic JIRA ticket for tracking).

---

## Phase 6 — Roster and metadata cleanup

- [ ] Update `podlings.xml` in the Incubator repository:
      - Set `status="retired"`
      - Set `enddate={{retirement_date}}`
      Commit message: "Retire Apache {{PODLING}}"
- [ ] Remove `{{PODLING}}` from the active reporting schedule in the Incubator
      board report template for the next board meeting.
- [ ] Update the Incubator website active-podlings page if it caches podling lists.
- [ ] Verify `{{PODLING}}` no longer appears in the active podlings dashboard.

---

## Phase 7 — Final board report

- [ ] The Incubator PMC includes a retirement note in the next board report:
      > "Apache {{PODLING}} was retired on {{retirement_date}} following a vote on
      > general@incubator.apache.org ({{vote_thread_url}})."
- [ ] The podling's mentors are formally released from mentoring duties.

---

## Contacts

| Role | Contact |
|------|---------|
| ASF Infrastructure | `https://issues.apache.org/jira/projects/INFRA` |
| Apache Attic PMC | `https://issues.apache.org/jira/projects/ATTIC` / `dev@attic.apache.org` |
| Incubator PMC | `general@incubator.apache.org` |
| Podling dev list | `dev@{{resource}}.apache.org` (read-only after closure) |

---

## Notes

_(Add any podling-specific notes here — custom infrastructure, active downstream
users, donated IP that requires special handling, trademark registrations, etc.)_
