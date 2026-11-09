<!-- Reference for the podling-onboarding skill. -->

# Phase 4 — Infrastructure Provisioning

Request and verify all ASF infrastructure resources in dependency order.
Two hard gates from earlier phases apply:

- **Repos gate** (from Phase 2): source repositories must not be provisioned
  before the SGA is filed when the donated code is not already Apache-licensed.
- **LDAP gate** (from Phase 3): LDAP accounts must not be created before every
  committer's ICLA is confirmed.

```python
import xml.etree.ElementTree as ET

# Carry gate states forward from earlier phases
repos_gate_open = sga.get("repos_gate_open", False)   # set in Phase 2
ldap_gate_open  = all_iclas_confirmed                  # set in Phase 3

# Convenience: resource slug used in all URL patterns
resource_lc = resource.lower()

# Master infra state dict — each key updated as the step completes
infra = {
    "podlings_xml":     {"done": None, "notes": ""},
    "status_page":      {"done": None, "notes": ""},
    "mailing_lists":    {"done": None, "notes": ""},
    "git_repos":        {"done": None, "notes": ""},
    "issue_tracker":    {"done": None, "notes": ""},
    "cwiki_space":      {"done": None, "notes": ""},
    "ldap_accounts":    {"done": None, "notes": ""},
    "website":          {"done": None, "notes": ""},
}

infra_failures = []

def _flag(key, reason):
    infra_failures.append(f"4 {key}: {reason}")
    infra[key]["done"] = False

print(f"\nPhase 4 — Infrastructure Provisioning")
print(f"  Repos gate:  {'OPEN' if repos_gate_open else 'BLOCKED (SGA not confirmed)'}")
print(f"  LDAP gate:   {'OPEN' if ldap_gate_open else 'BLOCKED (ICLAs pending)'}")
```

---

#### 4a — Podling metadata in podlings.xml

The podling entry in `content/podlings.xml` (Incubator SVN) must be added
immediately after acceptance — it drives the reporting schedule and the
incubator website podlings list. This is the mentor's first action.

```python
# Parse the local copy of podlings.xml to check current state
tree    = ET.parse(PODLINGS_XML)
root    = tree.getroot()
xml_pod = next(
    (x for x in root.findall("podling")
     if x.get("name", "").lower() == PODLING.lower()),
    None,
)

if xml_pod is None:
    _flag("podlings_xml",
          "podling entry missing from podlings.xml — add it immediately after acceptance")
    reporting_group = None
    monthly_active  = False
else:
    r_el = xml_pod.find("reporting")
    reporting_group = r_el.get("group") if r_el is not None else None
    monthly_active  = (r_el.get("monthly", "").lower() == "true"
                       if r_el is not None else False)
    status_attr     = xml_pod.get("status")
    start_attr      = xml_pod.get("startdate")

    if status_attr != "current":
        _flag("podlings_xml", f"status='{status_attr}' — should be 'current'")
    if not start_attr:
        _flag("podlings_xml", "startdate missing")
    if reporting_group not in ("1", "2", "3"):
        _flag("podlings_xml",
              f"reporting group='{reporting_group}' is invalid; must be 1, 2, or 3")
    if not monthly_active:
        # Check if three reports have already been filed (legitimate)
        pass  # will re-evaluate in Phase 5

    if not infra_failures or not any("podlings_xml" in f for f in infra_failures):
        infra["podlings_xml"]["done"] = True

print(f"\n  podlings.xml entry: {'found' if xml_pod is not None else 'MISSING'}")
if xml_pod is not None:
    print(f"    status={xml_pod.get('status')}  startdate={xml_pod.get('startdate')}")
    print(f"    reporting group={reporting_group}  monthly={monthly_active}")
```

The required SVN entry shape:

```xml
<podling name="ExampleProject" status="current" resource="exampleproject"
    sponsor="Incubator" startdate="YYYY-MM-DD">
    <description>One-sentence description.</description>
    <reporting group="2" monthly="True" />
    <champion availid="championid">Champion Full Name</champion>
    <mentors>
        <mentor username="mentorid1">Mentor One</mentor>
        <mentor username="mentorid2">Mentor Two</mentor>
    </mentors>
</podling>
```

Manual checks:

- [ ] Checkout or edit `https://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings.xml`
- [ ] Add the podling entry (copy an existing `status="current"` entry as a template)
- [ ] Set `status="current"`, `startdate` to the IPMC vote result date, and assign `resource` slug
- [ ] Set `<reporting group="N" monthly="True" />` — group is assigned by the IPMC Secretary
- [ ] Commit and verify the entry appears on `https://incubator.apache.org/projects/`
- [ ] Podling status page auto-generated; confirm it loads at `https://incubator.apache.org/projects/<resource>.html`

---

#### 4b — Mailing lists

Mailing lists are the primary communication channel for all Apache projects.
They must use the `incubator.apache.org` domain (not the podling's own domain)
and must be created before the source repositories (commits notifications go
to `commits@`). At least one moderator is required before selfserve will create
a list; three moderators are recommended.

```python
lists_config = {
    # Required lists:
    "dev": {
        "address":     f"dev@{resource_lc}.apache.org",
        "description": "Public development discussion",
        "required":    True,
        "created":     None,      # True / False
        "moderators":  [],        # list of email addresses (≥ 1 required)
        "archive_url": f"https://lists.apache.org/list.html?dev@{resource_lc}.apache.org",
    },
    "commits": {
        "address":     f"commits@{resource_lc}.apache.org",
        "description": "Automated commit and CI notifications",
        "required":    True,
        "created":     None,
        "moderators":  [],
        "archive_url": f"https://lists.apache.org/list.html?commits@{resource_lc}.apache.org",
    },
    "private": {
        "address":     f"private@{resource_lc}.apache.org",
        "description": "PPMC-only private discussion",
        "required":    True,
        "created":     None,
        "moderators":  [],
        "archive_url": None,  # private lists are not publicly archived
    },
    # Optional:
    "user": {
        "address":     f"user@{resource_lc}.apache.org",
        "description": "Public user support (create only if PPMC requests it)",
        "required":    False,
        "created":     None,
        "moderators":  [],
        "archive_url": f"https://lists.apache.org/list.html?user@{resource_lc}.apache.org",
    },
}

# Subscription tracking
subscriptions = {
    "ppmc_on_private":   None,   # True when all PPMC members subscribed to private@
    "mentors_on_dev":    None,   # True when all mentors subscribed to dev@
    "mentors_on_private": None,  # True when all mentors subscribed to private@
    "announcement_sent": None,   # True when introduction email sent to dev@
}

# Check required lists
for list_key, cfg in lists_config.items():
    if cfg["required"] and not cfg["created"]:
        _flag("mailing_lists",
              f"{cfg['address']} not yet created")
    if cfg["required"] and cfg["created"] and not cfg["moderators"]:
        _flag("mailing_lists",
              f"{cfg['address']} has no moderator recorded")

if not any("mailing_lists" in f for f in infra_failures):
    infra["mailing_lists"]["done"] = True

print(f"\n  Mailing lists:")
for k, cfg in lists_config.items():
    req  = "required" if cfg["required"] else "optional"
    done = cfg["created"]
    print(f"    {cfg['address']:<45} [{req}]  created={done}")
```

Manual checks:

- [ ] Identify at least **one** moderator per list (recommended: **three** to distribute workload); all moderators should be PPMC members or mentors
- [ ] Open `https://selfserve.apache.org/mail.html` (ASF member login required)
- [ ] Create `dev@{resource_lc}.apache.org` — set the domain to `incubator.apache.org`, **not** the podling's own domain
- [ ] Create `commits@{resource_lc}.apache.org` with the same domain
- [ ] Create `private@{resource_lc}.apache.org` — mark as private/members-only
- [ ] Optionally create `user@{resource_lc}.apache.org` if the PPMC requests it
- [ ] Verify archives appear at `https://lists.apache.org/list.html?dev@{resource_lc}.apache.org` (may take minutes after creation)
- [ ] All PPMC members subscribe to `private@`
- [ ] All mentors subscribe to `dev@` and `private@`
- [ ] Mentor sends an introduction email to `dev@` explaining their role
- [ ] If the project had an existing external mailing list: notify subscribers to join the new list (external subscribers do not transfer automatically)

> **Domain note:** Lists must be `@<resource>.apache.org`, not `@incubator.apache.org`. The Incubator owns the namespace `<resource>.apache.org` during incubation.

---

#### 4c — Source repository

Source repositories must not be provisioned until the SGA repos gate is open
(Phase 2). All ASF code is hosted on Apache infrastructure — either on
`gitbox.apache.org` (canonical) mirrored to `github.com/apache/`, or migrated
from an existing external repository via an INFRA Jira ticket.

```python
if not repos_gate_open:
    _flag("git_repos",
          "SGA repos gate is BLOCKED — do not provision repos until SGA is confirmed")
else:
    git_repos_config = {
        # Typically one repo matching the resource slug; add more if needed
        f"apache/{resource_lc}": {
            "gitbox_url":  f"https://gitbox.apache.org/repos/asf/{resource_lc}.git",
            "github_url":  f"https://github.com/apache/{resource_lc}",
            "selfserve_url": "https://selfserve.apache.org/repos.html",
            "created":     None,        # True / False
            "is_migration": None,       # True if migrating from external repo
            "migration_source": None,   # URL of the source repo (if migration)
            "infra_jira_ticket": None,  # INFRA-NNNNN (for migrations)
            "gitbox_ticket": None,      # GitBox Integration ticket (if write-back needed)
            "default_branch": "main",   # confirm with PPMC
        },
    }

    for repo, cfg in git_repos_config.items():
        if not cfg["created"]:
            _flag("git_repos", f"repo {repo} not yet created")

    if not any("git_repos" in f for f in infra_failures):
        infra["git_repos"]["done"] = True

    print(f"\n  Git repositories (repos gate OPEN):")
    for repo, cfg in git_repos_config.items():
        print(f"    {repo}: created={cfg['created']}  migration={cfg['is_migration']}")
```

Manual checks:

- [ ] Confirm SGA repos gate is open (Phase 2) before proceeding
- [ ] Decide repository name(s) with the PPMC — typically `apache/<resource>` matching the podling slug
- [ ] **New repo:** Open `https://selfserve.apache.org/repos.html` → "Git Repositories" → create `<resource>`
- [ ] **Migration from GitHub/GitLab/etc.:** File an INFRA Jira ticket at `https://issues.apache.org/jira/projects/INFRA`:
  - Summary: `Migrate <source-url> to Apache GitHub organization as apache/<resource>`
  - Include: source URL, target name, whether to preserve history
- [ ] **Gitbox write-back** (if PPMC wants GitHub as primary write surface): file a "GitBox Integration" ticket via INFRA Jira; then manage the repo at `https://gitbox.apache.org/`
- [ ] Verify canonical repo appears at `https://gitbox.apache.org/repos/asf/<resource>.git`
- [ ] Verify GitHub mirror appears at `https://github.com/apache/<resource>`
- [ ] Set branch protection on default branch (recommended: require PR reviews, status checks)
- [ ] Add `commits@<resource>.apache.org` as a notification email for push events (via INFRA or Gitbox settings)

---

#### 4d — Issue tracker

The PPMC chooses whether to use ASF Jira or GitHub Issues. Both are supported;
the decision should be made early and recorded so contributors know where to
file bugs.

```python
issue_tracker_config = {
    "choice":       None,   # "jira" | "github_issues" | "other"
    # If Jira:
    "jira_project_key":   None,   # e.g. "EXAMPLEPROJECT"
    "jira_url":           None,   # https://issues.apache.org/jira/projects/<KEY>
    "jira_created":       None,   # True / False
    # If GitHub Issues:
    "github_issues_enabled": None,  # True / False (enabled on the github.com/apache/<resource> repo)
    "github_issues_url":     f"https://github.com/apache/{resource_lc}/issues",
    # Either way:
    "tracker_announced":  None,   # True — mentioned in first dev@ introduction email
}

if issue_tracker_config["choice"] is None:
    _flag("issue_tracker", "tracker choice not made — PPMC must decide: Jira or GitHub Issues")
elif issue_tracker_config["choice"] == "jira" and not issue_tracker_config["jira_created"]:
    _flag("issue_tracker", "Jira project not yet created via selfserve")
elif issue_tracker_config["choice"] == "github_issues" \
        and not issue_tracker_config["github_issues_enabled"]:
    _flag("issue_tracker", "GitHub Issues not yet enabled on the repo")

if not any("issue_tracker" in f for f in infra_failures):
    infra["issue_tracker"]["done"] = True

print(f"\n  Issue tracker: choice={issue_tracker_config['choice']}")
```

Manual checks:

- [ ] PPMC votes on mailing list to choose Jira or GitHub Issues (lazy consensus is fine)
- [ ] **If Jira:** open `https://selfserve.apache.org/jira.html`
  - Create project; choose a short uppercase key (e.g., `EXAMPLEPROJECT`)
  - Confirm the project appears at `https://issues.apache.org/jira/projects/<KEY>`
- [ ] **If GitHub Issues:** ensure the repo exists (step 4c), then:
  - Go to `https://github.com/apache/<resource>/settings` → Features → enable Issues
  - No selfserve ticket needed
- [ ] Whichever tracker is chosen: mention it in the introduction email on `dev@` so contributors know where to file bugs
- [ ] Optionally add issue templates (`ISSUE_TEMPLATE/`) to the repository

---

#### 4e — Confluence wiki space (cwiki)

A Confluence wiki space under the `INCUBATOR` space (or a standalone space)
gives the podling a place for documentation, meeting notes, and the incubation
status page. It is optional but strongly recommended.

```python
cwiki_config = {
    "requested":      None,   # True if PPMC wants a wiki space
    "space_key":      None,   # e.g. "EXAMPLEPROJECT" (uppercase, short)
    "space_url":      None,   # https://cwiki.apache.org/confluence/display/<KEY>
    "created":        None,   # True / False
    "selfserve_ticket": None, # selfserve request ID or INFRA ticket
    # Home page set up:
    "home_page_created": None,
    "status_page_linked": None,  # True if linked from Incubator status page
}

if cwiki_config["requested"] is True and not cwiki_config["created"]:
    _flag("cwiki_space",
          "wiki space requested but not yet created — open selfserve or INFRA Jira")
elif cwiki_config["requested"] is None:
    # Not a hard failure — wiki is optional
    infra["cwiki_space"]["notes"] = "PPMC has not decided whether to use cwiki"

if cwiki_config["created"] is True:
    infra["cwiki_space"]["done"] = True
elif cwiki_config["requested"] is False:
    infra["cwiki_space"]["done"] = True   # opted out — not a failure
    infra["cwiki_space"]["notes"] = "PPMC opted out of cwiki space"

print(f"\n  Cwiki space: requested={cwiki_config['requested']}  "
      f"created={cwiki_config['created']}")
if cwiki_config["space_url"]:
    print(f"    URL: {cwiki_config['space_url']}")
```

Manual checks:

- [ ] PPMC decides whether to use Confluence wiki (optional but common)
- [ ] If yes: open `https://selfserve.apache.org/confluence.html`
  - Choose a space key (uppercase, ≤ 10 chars, unique — check existing spaces first)
  - Set space name: "Apache ExampleProject (Incubating)"
- [ ] Alternatively file an INFRA Jira ticket: `https://issues.apache.org/jira/projects/INFRA`
  - Summary: `Create Confluence wiki space for Apache <Podling> (incubating)`
- [ ] After creation, verify at `https://cwiki.apache.org/confluence/display/<KEY>`
- [ ] Create a home page with: description, links to mailing lists, issue tracker, and GitHub
- [ ] Link the wiki space from the Incubator status page

---

#### 4f — LDAP accounts and commit access

LDAP accounts are gated on ICLA confirmation (Phase 3). New-to-ASF committers
receive an account creation email from the Secretary once their ICLA is
processed. Existing ASF committers already have accounts — only commit access
to the new repository needs granting.

```python
if not ldap_gate_open:
    _flag("ldap_accounts",
          "LDAP gate BLOCKED — do not request accounts until all ICLAs confirmed")
else:
    ldap_status = {}
    for key, person in roster.items():
        if person["is_existing_asf"]:
            # Existing committer: account already exists, just needs repo access
            ldap_status[key] = {
                "account_exists":  True,
                "repo_access_granted": None,   # True once added to Apache GitHub org
            }
        else:
            # New committer: account created by Secretary after ICLA is confirmed
            ldap_status[key] = {
                "account_exists":  person["ldap_exists"],  # True once Secretary confirms
                "repo_access_granted": None,
            }

    accounts_complete = all(
        v["account_exists"] is True and v["repo_access_granted"] is True
        for v in ldap_status.values()
    )

    if not accounts_complete:
        pending = [k for k, v in ldap_status.items()
                   if not (v["account_exists"] and v["repo_access_granted"])]
        _flag("ldap_accounts",
              f"accounts/access not yet complete for: {pending}")
    else:
        infra["ldap_accounts"]["done"] = True

    print(f"\n  LDAP accounts (gate OPEN):")
    for key, s in ldap_status.items():
        print(f"    {key:<20} exists={s['account_exists']}  "
              f"repo_access={s['repo_access_granted']}")
```

Manual checks:

- [ ] Confirm LDAP gate is open (all ICLAs confirmed in Phase 3)
- [ ] New-to-ASF committers: wait for Secretary confirmation email (subject: "Account created")
- [ ] Once account exists, add each committer to the Apache GitHub org:
  - Go to `https://gitbox.apache.org/` → manage team for the podling repo
  - Or use Whimsy: `https://whimsy.apache.org/roster/ppmc/<resource>` to add members
- [ ] Verify each person can push to the repository (ask them to test with a small commit or check GitHub team membership)
- [ ] Add all PPMC members and committers to the Incubator roster at `https://whimsy.apache.org/roster/ppmc/<resource>`

---

#### 4g — Website

The podling website must be established at `<resource>.apache.org` and must
display the mandatory incubation disclaimer on every page.

```python
website_config = {
    "url":                f"https://{resource_lc}.apache.org",
    "live":               None,   # True / False
    "disclaimer_present": None,   # True / False
    "hosting_method":     None,   # "github_pages" | "svnpubsub" | "cms" | "other"
    "redirect_from_incubator": None,  # True if incubator.apache.org/<resource> redirects
}

DISCLAIMER_TEXT = (
    f"Apache {PODLING} is an effort undergoing incubation at The Apache "
    "Software Foundation (ASF), sponsored by the Apache Incubator. "
    "Incubation is required of all newly accepted projects until a further "
    "review indicates that the infrastructure, communications, and decision "
    "making process have stabilized in a manner consistent with other "
    "successful ASF projects. While incubation status is not necessarily a "
    "reflection of the completeness or stability of the code, it does "
    "indicate that the project has yet to be fully endorsed by the ASF."
)

if not website_config["live"]:
    _flag("website", "website not yet live")
if not website_config["disclaimer_present"]:
    _flag("website", "incubation disclaimer missing from website")

if not any("website" in f for f in infra_failures):
    infra["website"]["done"] = True

print(f"\n  Website: {website_config['url']}")
print(f"    live={website_config['live']}  disclaimer={website_config['disclaimer_present']}")
```

Manual checks:

- [ ] PPMC decides hosting method:
  - **GitHub Pages:** add a `gh-pages` branch to the Apache GitHub repo; INFRA enables `<resource>.apache.org` pointing to it
  - **svnpubsub:** commit static files to `https://svn.apache.org/repos/asf/incubator/<resource>/site/`
  - Request DNS via INFRA Jira: `https://issues.apache.org/jira/projects/INFRA` — "Create Apache subdomain for <resource>.apache.org"
- [ ] Verify website loads at `https://{resource_lc}.apache.org`
- [ ] Confirm incubation disclaimer appears on every page (exact wording from the Incubator policy — see `DISCLAIMER_TEXT` above)
- [ ] Add links to: mailing lists (`https://lists.apache.org`), source repository, issue tracker, wiki
- [ ] Check that `https://incubator.apache.org/projects/{resource_lc}.html` links to the website

---

#### Phase 4 — Write results

```python
# Overall phase pass: all required items done; cwiki is optional
required_keys = ["podlings_xml", "status_page", "mailing_lists",
                 "git_repos", "issue_tracker", "ldap_accounts", "website"]
phase4_pass = all(infra[k]["done"] is True for k in required_keys)

print(f"\n{'='*60}")
print(f"Phase 4 — Infrastructure Provisioning: "
      f"{'PASS' if phase4_pass else 'INCOMPLETE'}")
print(f"{'='*60}")
for k, v in infra.items():
    status = "PASS" if v["done"] is True else ("OPT-OUT" if v["done"] == "opted_out" else "PENDING")
    note   = f"  ({v['notes']})" if v.get("notes") else ""
    print(f"  {k:<25} {status}{note}")
if infra_failures:
    print("\nItems to resolve:")
    for f in infra_failures:
        print(f"  - {f}")

with open(OUTPUT, "a") as fh:
    fh.write("## Phase 4 — Infrastructure Provisioning\n\n")
    fh.write("| Resource | Status | Notes |\n")
    fh.write("|----------|--------|-------|\n")
    for k, v in infra.items():
        status = "done" if v["done"] is True else "pending"
        fh.write(f"| {k} | {status} | {v.get('notes', '')} |\n")
    if infra_failures:
        fh.write("\n**Failures:**\n")
        for f in infra_failures:
            fh.write(f"- {f}\n")
    fh.write(f"\nOverall: {'PASS' if phase4_pass else 'INCOMPLETE'}\n\n")
```

---

