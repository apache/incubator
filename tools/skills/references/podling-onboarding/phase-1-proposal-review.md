<!-- Reference for the podling-onboarding skill. -->

# Phase 1 — Proposal Review

Verify that the accepted proposal meets all IPMC entry criteria before
bootstrap work begins. Work through sub-steps 1a–1e in order; each sub-step
populates one key of `proposal_review` and records any failures. The phase
writes its findings to `OUTPUT` under `## Phase 1 — Proposal Review`.

```python
from podlings.tools import tool_get_podling
import xml.etree.ElementTree as ET

# Load from PodlingsMCP (authoritative for current metadata)
podling_meta = tool_get_podling({"name": PODLING})
p            = podling_meta["podling"]

name        = p.get("name")
resource    = p.get("resource", PODLING.lower())
start_date  = p.get("startdate")
sponsor     = p.get("sponsor")
champion    = p.get("champion") or {}   # dict with "availid" and text name
mentors     = p.get("mentors", [])      # list of dicts with "username" and name
description = p.get("description", "")

# Also parse podlings.xml directly for fields not exposed by the tool
tree    = ET.parse(PODLINGS_XML)
root    = tree.getroot()
xml_pod = next(
    (x for x in root.findall("podling")
     if x.get("name", "").lower() == PODLING.lower()),
    None,
)

# Accumulate all failures; any non-empty list means the phase is incomplete
proposal_failures = []
proposal_review   = {}
```

#### 1a — Board Resolution

The IPMC vote that accepted the podling must have produced a formal resolution:
at least 3 binding +1 votes, more +1s than -1s, and no unresolved blocking
objections. The vote is conducted on `general@incubator.apache.org` and
archived there; the result is also logged in the INCUBATOR JIRA project.

```python
# Board resolution cannot be fetched automatically.
# The mentor must supply these values after reading the vote thread:

board_resolution = {
    "vote_thread_url":   None,   # URL of the [VOTE] thread on lists.apache.org
    "binding_plus1":     None,   # int — number of binding +1 votes
    "binding_minus1":    None,   # int — number of binding -1 votes (must be 0 or resolved)
    "unresolved_minus1": None,   # bool — True if any -1 was never resolved
    "incubator_jira":    None,   # e.g. "https://issues.apache.org/jira/browse/INCUBATOR-NNN"
    "acceptance_email_sent": None,  # bool — announcement posted to general@
}

# Evaluate:
res_ok = (
    board_resolution["binding_plus1"] is not None
    and board_resolution["binding_plus1"] >= 3
    and not board_resolution["unresolved_minus1"]
)
if not res_ok:
    proposal_failures.append(
        "1a board_resolution: vote not confirmed or has unresolved -1"
    )
proposal_review["board_resolution"] = {**board_resolution, "pass": res_ok}
```

Manual checks:

- [ ] Locate the `[VOTE]` thread on `general@incubator.apache.org` and paste URL into `vote_thread_url`
- [ ] Count binding +1 votes (IPMC members only); enter in `binding_plus1`
- [ ] Confirm no unresolved -1 votes; set `unresolved_minus1 = False`
- [ ] Find the INCUBATOR JIRA issue (search `https://issues.apache.org/jira/projects/INCUBATOR`); paste URL
- [ ] Confirm acceptance announcement was sent to `general@incubator.apache.org`

Threshold: **binding_plus1 ≥ 3 and unresolved_minus1 = False**.

---

#### 1b — Champion

Every podling proposal must name a Champion who is an existing IPMC member.
The Champion steers the proposal through discussion and the IPMC vote; they
need not become a Mentor, but they must be on the IPMC at the time of
acceptance.

```python
champion_availid = champion.get("availid") if isinstance(champion, dict) else None
champion_name    = (champion.get("#text") or champion.get("name")
                    if isinstance(champion, dict) else str(champion))

# Automated check: champion field must be non-empty in podlings.xml
champion_listed = bool(champion_availid or champion_name)

# IPMC membership must be verified manually via Whimsy:
#   https://whimsy.apache.org/roster/committee/incubator
champion_is_ipmc = None   # True / False — fill after Whimsy check

champ_ok = champion_listed and (champion_is_ipmc is not False)
if not champion_listed:
    proposal_failures.append("1b champion: no champion recorded in podlings.xml")
if champion_is_ipmc is False:
    proposal_failures.append(
        f"1b champion: {champion_availid} is NOT an IPMC member"
    )

proposal_review["champion"] = {
    "availid":       champion_availid,
    "name":          champion_name,
    "listed":        champion_listed,
    "is_ipmc_member": champion_is_ipmc,
    "pass":          champ_ok,
}

print(f"Champion: {champion_name} ({champion_availid})")
print(f"  Listed in podlings.xml: {champion_listed}")
print(f"  IPMC member (manual): {champion_is_ipmc}")
```

Manual checks:

- [ ] Open `https://whimsy.apache.org/roster/committee/incubator`
- [ ] Confirm `{champion_availid}` appears in the IPMC roster
- [ ] Set `champion_is_ipmc = True` (or `False` if absent — escalate to IPMC chair)
- [ ] If champion is not on IPMC, they must request election before the podling proceeds

Threshold: champion field non-empty **and** champion confirmed as IPMC member.

---

#### 1c — Mentor List

Each podling requires 2–3 Mentors who are IPMC members. Mentors are distinct
from the Champion (though one person can hold both roles). They guide the
PPMC through incubation, sign off on board reports, and vote on releases.

```python
mentor_usernames = [
    (m.get("username") or m.get("availid") or str(m))
    for m in mentors
]
mentor_names_text = [
    (m.get("#text") or m.get("name") or str(m))
    for m in mentors
]

mentor_count     = len(mentor_usernames)
meets_minimum    = mentor_count >= 2   # 2 minimum; 3 recommended

# IPMC membership for each mentor must be verified on Whimsy:
#   https://whimsy.apache.org/roster/committee/incubator
# Fill this dict after checking each username:
mentor_ipmc_status = {u: None for u in mentor_usernames}
# e.g. mentor_ipmc_status["jmclean"] = True

all_mentors_ipmc = all(v is True for v in mentor_ipmc_status.values())
any_mentor_not_ipmc = any(v is False for v in mentor_ipmc_status.values())

if not meets_minimum:
    proposal_failures.append(
        f"1c mentor_list: only {mentor_count} mentor(s); minimum is 2"
    )
if any_mentor_not_ipmc:
    non_members = [u for u, v in mentor_ipmc_status.items() if v is False]
    proposal_failures.append(
        f"1c mentor_list: non-IPMC mentor(s): {non_members} — "
        "each must request IPMC election before incubation begins"
    )

proposal_review["mentor_list"] = {
    "count":             mentor_count,
    "usernames":         mentor_usernames,
    "meets_minimum":     meets_minimum,
    "ipmc_status":       mentor_ipmc_status,
    "all_ipmc_members":  all_mentors_ipmc,
    "pass":              meets_minimum and not any_mentor_not_ipmc,
}

print(f"\nMentors ({mentor_count}):")
for u, name in zip(mentor_usernames, mentor_names_text):
    status = mentor_ipmc_status.get(u)
    flag   = "OK" if status is True else ("NOT IPMC" if status is False else "?")
    print(f"  {u:<20} {name:<30} [{flag}]")
```

Manual checks (one row per mentor):

- [ ] Open `https://whimsy.apache.org/roster/committee/incubator`
- [ ] For each username in `mentor_usernames`, confirm presence on IPMC; set `mentor_ipmc_status[username] = True`
- [ ] Any absent mentor must request election via email to `private@incubator.apache.org` — note expected timeline (typically a few days)
- [ ] Confirm at least one mentor has already subscribed to `general@incubator.apache.org` and `private@incubator.apache.org`
- [ ] Confirm mentors are aware they must subscribe to the podling's `dev@` and `private@` lists (Phase 4)

Threshold: **mentor_count ≥ 2 and all mentors confirmed as IPMC members**.

---

#### 1d — Initial Committers

The accepted proposal must list the initial set of committers and PPMC members.
These are the people who will bootstrap the project; every one of them requires
an ICLA before ASF LDAP accounts are created (verified fully in Phase 3).
This step confirms the list exists and is non-trivial.

```python
# The initial committer list comes from the proposal page (wiki or cwiki),
# not from podlings.xml. The mentor must supply it here.
# Format: list of dicts with "name" and "apache_id" (if existing ASF committer)
# or "email" (if new to ASF).

initial_committers = [
    # {"name": "Alice Example", "apache_id": "aexample", "is_existing_asf": True},
    # {"name": "Bob Sample",    "apache_id": None,        "is_existing_asf": False,
    #  "email": "bob@example.com"},
]

committer_count         = len(initial_committers)
existing_asf_committers = [c for c in initial_committers if c.get("is_existing_asf")]
new_to_asf              = [c for c in initial_committers if not c.get("is_existing_asf")]

# Minimum: at least one committer must be listed (usually several)
has_committer_list = committer_count > 0

if not has_committer_list:
    proposal_failures.append(
        "1d initial_committers: list is empty — populate from the accepted proposal"
    )

proposal_review["initial_committers"] = {
    "count":                committer_count,
    "existing_asf_count":   len(existing_asf_committers),
    "new_to_asf_count":     len(new_to_asf),
    "committers":           initial_committers,
    "pass":                 has_committer_list,
}

print(f"\nInitial committers: {committer_count}")
print(f"  Existing ASF committers: {len(existing_asf_committers)}")
print(f"  New to ASF (need ICLA):  {len(new_to_asf)}")
if new_to_asf:
    print("  New-to-ASF names:")
    for c in new_to_asf:
        print(f"    {c['name']} <{c.get('email', 'no email')}>")
```

Manual checks:

- [ ] Copy the committer list from the accepted proposal wiki page into `initial_committers`
- [ ] Mark each person `is_existing_asf = True` if they already have an Apache ID (check `https://whimsy.apache.org/roster/committer/`)
- [ ] For each `is_existing_asf = True` person: confirm their ICLA is already on file (it is — existing committers signed when first added to any ASF project)
- [ ] For each `is_existing_asf = False` person: flag for ICLA collection in Phase 3
- [ ] Confirm the list includes PPMC members (not just code contributors) — PPMC members must also be on this list or added to it

Threshold: **at least one committer listed**; ICLAs verified in Phase 3.

---

#### 1e — IP Clearance

Before infrastructure is provisioned, the provenance and licence of all donated
code must be established. This step records what is known from the proposal; the
SGA and formal IP clearance process are tracked in Phase 2.

```python
# These values come from reading the proposal; the mentor fills them in.

ip_clearance = {
    # Incoming code licence — must be Apache 2.0 or Category A to proceed
    # without an SGA. Any other licence requires an SGA before repo creation.
    "incoming_licence":         None,   # e.g. "Apache-2.0", "MIT", "GPL-2.0"
    "licence_is_apache_or_cat_a": None, # True / False / None

    # Third-party dependencies — Category B or C may require special handling
    "dependencies_listed":      None,   # True / False — proposal lists them
    "has_category_b_deps":      None,   # True / False / None
    "has_category_c_deps":      None,   # True / False / None (C = incompatible, blocked)

    # Cryptography — ASF export control policy applies
    "has_crypto":               None,   # True / False / None
    "crypto_noted_in_proposal": None,   # True / False (must be if has_crypto=True)

    # Name / trademark
    "podlingnamesearch_filed":  None,   # True / False
    "podlingnamesearch_jira":   None,   # URL e.g. "https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-NNN"
}

# Derive whether an SGA will be required (feeds into Phase 2)
sga_required_by_ip = (
    ip_clearance["licence_is_apache_or_cat_a"] is False
)

ip_issues = []
if ip_clearance["incoming_licence"] is None:
    ip_issues.append("incoming_licence not recorded — read proposal and fill in")
if ip_clearance["licence_is_apache_or_cat_a"] is False:
    ip_issues.append(
        f"incoming licence ({ip_clearance['incoming_licence']}) requires SGA — "
        "do not provision repos until SGA is filed (Phase 2)"
    )
if ip_clearance["has_category_c_deps"] is True:
    ip_issues.append(
        "Category C (GPL-incompatible) dependencies found — "
        "these must be removed or resolved before acceptance is valid"
    )
if ip_clearance["has_crypto"] is True and not ip_clearance["crypto_noted_in_proposal"]:
    ip_issues.append(
        "project includes cryptography but proposal does not note it — "
        "add crypto export-control notice to the proposal"
    )
if not ip_clearance["podlingnamesearch_filed"]:
    ip_issues.append(
        "PODLINGNAMESEARCH JIRA not yet filed — "
        "file at https://issues.apache.org/jira/projects/PODLINGNAMESEARCH"
    )

for issue in ip_issues:
    proposal_failures.append(f"1e ip_clearance: {issue}")

proposal_review["ip_clearance"] = {
    **ip_clearance,
    "sga_required": sga_required_by_ip,
    "issues":       ip_issues,
    "pass":         len(ip_issues) == 0,
}

print(f"\nIP Clearance:")
print(f"  Incoming licence:         {ip_clearance['incoming_licence'] or 'UNKNOWN'}")
print(f"  Apache/Cat-A licence:     {ip_clearance['licence_is_apache_or_cat_a']}")
print(f"  SGA required:             {sga_required_by_ip}")
print(f"  Dependencies listed:      {ip_clearance['dependencies_listed']}")
print(f"  Category C deps:          {ip_clearance['has_category_c_deps']}")
print(f"  Cryptography noted:       {ip_clearance['crypto_noted_in_proposal']}")
print(f"  PODLINGNAMESEARCH filed:  {ip_clearance['podlingnamesearch_filed']}")
if ip_issues:
    print("  Issues:")
    for i in ip_issues:
        print(f"    - {i}")
```

Manual checks:

- [ ] Read the accepted proposal and record `incoming_licence` (the SPDX identifier of the donated code's licence)
- [ ] Verify the licence is Apache-2.0 or [Category A](https://www.apache.org/legal/resolved.html#category-a); set `licence_is_apache_or_cat_a`
- [ ] List all third-party dependencies in the proposal; note any [Category B](https://www.apache.org/legal/resolved.html#category-b) (allowed with conditions) or Category C (incompatible — blocked)
- [ ] Note whether the code includes cryptography; if so, ensure the proposal includes the required export-control statement
- [ ] File a `PODLINGNAMESEARCH` JIRA issue if not already done: `https://issues.apache.org/jira/projects/PODLINGNAMESEARCH`
- [ ] Confirm no Category C dependencies are present (hard blocker — proposal is invalid if they are)

Threshold: **incoming licence confirmed, no Category C deps, crypto noted if present, PODLINGNAMESEARCH filed**.

---

#### Phase 1 — Write results

```python
# Phase 1 overall pass/fail
phase1_pass = len(proposal_failures) == 0

proposal_review["overall"] = {
    "pass":     phase1_pass,
    "failures": proposal_failures,
}

# Pretty-print Phase 1 summary
print(f"\n{'='*60}")
print(f"Phase 1 — Proposal Review: {'PASS' if phase1_pass else 'INCOMPLETE'}")
print(f"{'='*60}")
criteria = ["board_resolution", "champion", "mentor_list",
            "initial_committers", "ip_clearance"]
for c in criteria:
    status = "PASS" if proposal_review.get(c, {}).get("pass") else "PENDING"
    print(f"  {c:<25} {status}")
if proposal_failures:
    print("\nItems to resolve:")
    for f in proposal_failures:
        print(f"  - {f}")

# Append Phase 1 section to the output file
with open(OUTPUT, "a") as fh:
    fh.write("## Phase 1 — Proposal Review\n\n")
    fh.write(f"Overall: {'PASS' if phase1_pass else 'INCOMPLETE'}\n\n")
    fh.write("| Criterion | Pass? |\n|-----------|-------|\n")
    for c in criteria:
        ok = proposal_review.get(c, {}).get("pass")
        fh.write(f"| {c} | {'yes' if ok else 'NO — see failures'} |\n")
    if proposal_failures:
        fh.write("\n**Failures:**\n")
        for f in proposal_failures:
            fh.write(f"- {f}\n")
    fh.write("\n")
```

---

