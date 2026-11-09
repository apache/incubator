<!-- Reference for the podling-onboarding skill. -->

# Phase 3 — ICLA Coverage

Every person who will have commit access — initial PPMC members, committers,
and mentors — must have a signed Individual Contributor Licence Agreement (ICLA)
on file with the ASF Secretary before their LDAP account is created. Existing
ASF committers already have ICLAs; new-to-ASF contributors must submit one.

Start this phase immediately after acceptance — ICLA processing can take days
to weeks. Do not wait until infrastructure is being requested.

#### 3a — Build the complete roster

```python
# Combine mentors (from Phase 1) and initial committers (from Phase 1 step 1d)
# into a single de-duplicated roster for ICLA tracking.

phase1_committers = proposal_review.get("initial_committers", {}).get("committers", [])
mentor_usernames  = proposal_review.get("mentor_list", {}).get("usernames", [])

# Normalise committers to a common dict shape
roster = {}

# Add mentors first (they are always existing ASF committers — they must be
# IPMC members, which requires an existing ASF account and therefore an ICLA)
for username in mentor_usernames:
    roster[username] = {
        "name":            username,           # update with full name if known
        "apache_id":       username,
        "is_existing_asf": True,               # mentors are IPMC members → existing
        "email":           None,
        "employer":        None,               # for CCLA determination
        "role":            "mentor",
        # ICLA tracking fields — filled in step 3b:
        "icla_status":     "assumed_confirmed", # existing ASF committer
        "icla_date":       None,
        "ccla_needed":     None,
        "ccla_status":     None,
        "ldap_exists":     None,
        "whimsy_url":      f"https://whimsy.apache.org/roster/committer/{username}",
    }

# Add initial committers from Phase 1
for c in phase1_committers:
    apache_id = c.get("apache_id") or c.get("username")
    key       = apache_id or c["name"].lower().replace(" ", "_")
    is_asf    = c.get("is_existing_asf", False)
    roster[key] = {
        "name":            c.get("name", key),
        "apache_id":       apache_id,
        "is_existing_asf": is_asf,
        "email":           c.get("email"),
        "employer":        c.get("employer"),
        "role":            "ppmc" if c.get("is_ppmc") else "committer",
        "icla_status":     "assumed_confirmed" if is_asf else "unknown",
        "icla_date":       None,
        "ccla_needed":     None,
        "ccla_status":     None,
        "ldap_exists":     is_asf,   # existing ASF people already have LDAP
        "whimsy_url":      (f"https://whimsy.apache.org/roster/committer/{apache_id}"
                            if apache_id else None),
    }

existing_asf = [k for k, v in roster.items() if v["is_existing_asf"]]
new_to_asf   = [k for k, v in roster.items() if not v["is_existing_asf"]]

print(f"\nRoster: {len(roster)} people total")
print(f"  Existing ASF committers: {len(existing_asf)} (ICLAs assumed on file)")
print(f"  New to ASF:              {len(new_to_asf)} (ICLAs required)")
```

---

#### 3b — Verify existing ASF committers via Whimsy

Existing ASF committers have ICLAs on file by definition (they signed when
originally added to any ASF project). Verify via Whimsy that the Apache ID
is valid and the account is active.

```python
# For each existing ASF committer, check:
#   https://whimsy.apache.org/roster/committer/<apache_id>
# A valid page confirms the account exists. An HTTP 404 means the ID is wrong.

for key in existing_asf:
    person = roster[key]
    apache_id = person.get("apache_id")
    if not apache_id:
        person["icla_status"] = "cannot_verify"
        person["notes"] = "No Apache ID — cannot look up on Whimsy"
        continue

    # Manual verification required — automated Whimsy access is not available
    # Set these after opening each Whimsy URL:
    person["ldap_exists"]    = None   # True after confirming Whimsy page loads
    person["icla_status"]    = "assumed_confirmed"   # update to "confirmed" after check
    # person["icla_status"]  = "confirmed"  # set after manually confirming

print("\nExisting ASF committers (verify each Whimsy URL):")
for key in existing_asf:
    p = roster[key]
    print(f"  {p['apache_id']:<20} {p['name']:<30} {p['whimsy_url']}")
```

Manual checks for each existing ASF committer:

- [ ] Open each `whimsy_url`; confirm the page loads (200 OK = account exists)
- [ ] Set `ldap_exists = True` for each confirmed account
- [ ] Set `icla_status = "confirmed"` for each confirmed account
- [ ] If Whimsy returns 404: the Apache ID is wrong — check the proposal or ask the person directly

---

#### 3c — ICLA submission for new-to-ASF contributors

New-to-ASF contributors must sign and submit an ICLA before they can receive
an ASF LDAP account. The ICLA is submitted directly to `secretary@apache.org`.

```python
# ICLA submission tracking for each new-to-ASF person:
for key in new_to_asf:
    person = roster[key]
    # Shepherd fills these fields after contacting each person:
    person["icla_status"]      = "unknown"  # "unknown" | "notified" | "submitted" | "confirmed"
    person["icla_notified_date"] = None     # ISO date — when the mentor told them to submit
    person["icla_submitted_date"] = None    # ISO date — when they sent it to Secretary
    person["icla_date"]          = None     # ISO date — when Secretary confirmed receipt
    # Whimsy URL will only resolve once account is created; keep None until then
    person["whimsy_url"]         = None

# Status meanings:
# "unknown"   — not yet contacted; mentor must reach out
# "notified"  — mentor sent instructions; waiting for person to submit
# "submitted" — person confirms they emailed the ICLA; waiting for Secretary
# "confirmed" — Secretary acknowledged and Whimsy account now exists

# ICLA instructions to send to each new contributor:
ICLA_INSTRUCTIONS = f"""\
To contribute to Apache {PODLING} (incubating) as a committer, you must
sign and submit an Individual Contributor Licence Agreement (ICLA) to the
Apache Software Foundation.

Steps:
1. Download the ICLA form: https://www.apache.org/licenses/icla.pdf
2. Fill in your full legal name, preferred Apache ID, and contact email.
   Choose an Apache ID that is not already taken:
   https://whimsy.apache.org/committers/listids (search before choosing)
3. Sign the form (electronic signature accepted).
4. Email the signed PDF to: secretary@apache.org
   Subject: "ICLA for Apache {PODLING}"
5. Reply to this message with the date you submitted it.

Processing typically takes several days to a few weeks. You will receive
a confirmation email from the Secretary when your account is created.
"""

print(f"\nNew-to-ASF contributors needing ICLAs ({len(new_to_asf)}):")
for key in new_to_asf:
    p = roster[key]
    print(f"  {p['name']:<35} email={p.get('email') or 'UNKNOWN'}  "
          f"status={p['icla_status']}")
```

Manual checks for each new-to-ASF contributor:

- [ ] Send ICLA instructions (above) to each person's email address
- [ ] Record `icla_notified_date` for each person
- [ ] Ask each person to confirm when they have submitted their ICLA; record `icla_submitted_date`
- [ ] Follow up with `secretary@apache.org` if no confirmation arrives within 2 weeks
- [ ] Once the Secretary confirms, set `icla_status = "confirmed"` and `icla_date`
- [ ] Verify the new Apache ID appears at `https://whimsy.apache.org/roster/committer/<id>`

---

#### 3d — CCLA handling

A Corporate Contributor Licence Agreement (CCLA) is needed when a contributor
is making contributions as part of their employment (i.e., the employer holds
the copyright to the work). Not every contributor needs one — only those
whose employer could claim ownership of the donated code.

```python
# Determine which roster members may need a CCLA:
possible_ccla = []
for key, person in roster.items():
    employer = person.get("employer")
    # If employer is known and not "self" / "individual", flag for CCLA review
    if employer and employer.lower() not in ("self", "individual", "none", ""):
        person["ccla_needed"]    = None   # True / False — confirm with person
        person["ccla_org"]       = employer
        person["ccla_status"]    = "unknown"  # "unknown" | "filed" | "confirmed"
        possible_ccla.append(key)
    else:
        person["ccla_needed"] = False   # no employer or self-employed

# CCLA is submitted by the employer (not the individual) to secretary@apache.org
# Template: https://www.apache.org/licenses/cla-corporate.txt
# A company that already has a CCLA on file does not need to submit again —
# check https://www.apache.org/licenses/contributor-agreements.html

if possible_ccla:
    print(f"\nPossible CCLA required for ({len(possible_ccla)}):")
    for key in possible_ccla:
        p = roster[key]
        print(f"  {p['name']:<30} employer={p.get('ccla_org')}")
else:
    print("\nNo CCLA candidates identified (confirm employer status for each person).")
```

Manual checks:

- [ ] For each roster member, ask: "Are your contributions made as part of your employment?"
- [ ] If yes: ask which company; set `employer` and `ccla_needed = True`
- [ ] Check `https://www.apache.org/licenses/contributor-agreements.html` to see if that company already has a CCLA
- [ ] If no existing CCLA: ask the employer's legal team to submit one to `secretary@apache.org` using `https://www.apache.org/licenses/cla-corporate.txt`
- [ ] Record `ccla_status = "confirmed"` once the Secretary acknowledges

---

#### 3e — ICLA gate: block LDAP account creation until confirmed

```python
icla_failures = []
confirmed_statuses = {"confirmed", "assumed_confirmed"}

for key, person in roster.items():
    if person["icla_status"] not in confirmed_statuses:
        icla_failures.append(
            f"{person['name']} ({key}): icla_status={person['icla_status']} "
            f"— do not create LDAP account until confirmed"
        )

# CCLA failures: if ccla_needed=True but not confirmed, flag (warning, not hard block)
ccla_warnings = []
for key, person in roster.items():
    if person.get("ccla_needed") is True and person.get("ccla_status") != "confirmed":
        ccla_warnings.append(
            f"{person['name']} ({key}): CCLA needed for employer "
            f"'{person.get('ccla_org')}' — status={person.get('ccla_status')}"
        )

all_iclas_confirmed = len(icla_failures) == 0
ldap_gate_open      = all_iclas_confirmed

print(f"\nICLA gate: {'OPEN — all ICLAs confirmed' if ldap_gate_open else 'BLOCKED'}")
if icla_failures:
    print("  Pending ICLAs:")
    for f in icla_failures:
        print(f"    - {f}")
if ccla_warnings:
    print("  CCLA warnings (not a hard block but must be resolved):")
    for w in ccla_warnings:
        print(f"    - {w}")
```

---

#### Phase 3 — Write results

```python
phase3_pass = all_iclas_confirmed   # CCLAs are warnings, not hard failures

# Summary table for output file
rows = []
for key, p in roster.items():
    rows.append(
        f"| {p['name']:<30} | {p.get('apache_id') or 'TBD':<18} "
        f"| {p['role']:<10} | {'existing' if p['is_existing_asf'] else 'new':<8} "
        f"| {p['icla_status']:<20} | {p.get('ccla_needed', 'N/A')} |"
    )

with open(OUTPUT, "a") as fh:
    fh.write("## Phase 3 — ICLA Coverage\n\n")
    fh.write(f"Roster size: {len(roster)} "
             f"({len(existing_asf)} existing ASF, {len(new_to_asf)} new)\n\n")
    fh.write("| Name | Apache ID | Role | ASF status | ICLA status | CCLA needed |\n")
    fh.write("|------|-----------|------|------------|-------------|-------------|\n")
    for row in rows:
        fh.write(row + "\n")
    fh.write(f"\nLDAP gate: {'OPEN' if ldap_gate_open else 'BLOCKED — see pending ICLAs below'}\n")
    if icla_failures:
        fh.write("\n**Pending ICLAs (LDAP blocked):**\n")
        for f in icla_failures:
            fh.write(f"- {f}\n")
    if ccla_warnings:
        fh.write("\n**CCLA warnings:**\n")
        for w in ccla_warnings:
            fh.write(f"- {w}\n")
    fh.write(f"\nOverall: {'PASS' if phase3_pass else 'INCOMPLETE'}\n\n")

print(f"\nPhase 3 — ICLA Coverage: {'PASS' if phase3_pass else 'INCOMPLETE'}")
```

---

