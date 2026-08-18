<!-- Reference for the podling-onboarding skill. -->

# Phase 2 — SGA Receipt

Confirm whether a Software Grant Agreement is needed for the donated code and,
if so, that it has been filed with and acknowledged by the Apache Secretary.
The SGA is distinct from ICLAs: it transfers ownership of the existing codebase
to the ASF; ICLAs (Phase 3) cover ongoing contributions.

**Ordering rule (from the Mentor Onboarding guide):** Do NOT request source
repositories before the SGA is filed when the donated code was not already
Apache-licensed. Violating this ordering means unlicensed code could enter ASF
infrastructure before the grant is recorded.

#### 2a — Determine SGA requirement

```python
# Pull the IP clearance result from Phase 1 (already populated in proposal_review)
ip = proposal_review.get("ip_clearance", {})
incoming_licence        = ip.get("incoming_licence")          # e.g. "Apache-2.0"
licence_is_apache_cat_a = ip.get("licence_is_apache_or_cat_a")  # True / False / None

# An SGA is required when the incoming code is NOT already Apache-licensed
# or Category A. If Phase 1 was not yet run, determine here.
if licence_is_apache_cat_a is None:
    # Phase 1 not yet complete — ask the mentor directly
    sga_required = None   # fill in: True if licence is not Apache-2.0 / Cat-A
elif licence_is_apache_cat_a is True:
    sga_required = False  # already Apache-licensed; no SGA needed
else:
    sga_required = True   # non-Apache licence — SGA mandatory

print(f"Incoming licence: {incoming_licence or 'UNKNOWN'}")
print(f"SGA required:     {sga_required}")
```

Manual check:

- [ ] If `incoming_licence` is `None`, read the proposal and enter it in Phase 1 first
- [ ] Confirm `sga_required` with the donating organisation's legal team if the licence is ambiguous
- [ ] If `sga_required = False`, skip to step 2c (IP Clearance file still needed)

---

#### 2b — SGA submission and acknowledgment

```python
# The SGA is submitted to secretary@apache.org by the donating organisation.
# The Secretary logs receipt; check the ASF Received Grants list:
#   https://www.apache.org/licenses/contributor-agreements.html
# and the INCUBATOR JIRA ticket for this podling (filed during proposal acceptance).

sga = {
    "required":           sga_required,
    # Submission details — fill after consulting the donating org:
    "submitter_name":     None,   # legal name of the signing officer
    "submitter_org":      None,   # organisation name (must match the entity donating)
    "submitted_date":     None,   # ISO date, e.g. "2026-08-01"
    "submission_method":  None,   # "email" | "post" | "electronic"
    # Secretary acknowledgment — fill after Secretary confirms:
    "secretary_ack":      None,   # True / False
    "secretary_ack_date": None,   # ISO date the Secretary confirmed receipt
    "grants_list_url":    None,   # URL of the entry on the ASF received-grants page
    "incubator_jira_url": None,   # INCUBATOR JIRA where SGA status is tracked
    "notes":              "",
}

# Gate: repositories may only be provisioned once this condition is met
repos_gate_open = (sga_required is False) or (
    sga_required is True
    and sga["secretary_ack"] is True
)

sga_failures = []
if sga_required is True:
    if not sga["submitted_date"]:
        sga_failures.append("SGA not yet submitted — donating org must send to secretary@apache.org")
    if not sga["secretary_ack"]:
        sga_failures.append("Secretary has not yet acknowledged SGA receipt")
    if not sga["grants_list_url"]:
        sga_failures.append("SGA not yet visible on ASF received-grants list")
if sga_required is None:
    sga_failures.append("SGA requirement undetermined — complete Phase 1 ip_clearance first")

print(f"\nSGA status:")
print(f"  Required:       {sga_required}")
print(f"  Submitted:      {sga.get('submitted_date') or 'NO'}")
print(f"  Secretary ack:  {sga.get('secretary_ack')}")
print(f"  Repos gate:     {'OPEN' if repos_gate_open else 'BLOCKED'}")
if sga_failures:
    print("  Failures:")
    for f in sga_failures:
        print(f"    - {f}")
```

Manual checks:

- [ ] Contact the donating organisation's legal representative and confirm they will sign the SGA
- [ ] Provide the SGA template: `https://www.apache.org/licenses/software-grant-template.pdf`
- [ ] Donating org returns the signed SGA to `secretary@apache.org`
- [ ] Follow up with the ASF Secretary via `secretary@apache.org` to confirm receipt; note `secretary_ack_date`
- [ ] Verify the podling appears on `https://www.apache.org/licenses/contributor-agreements.html`; paste URL into `grants_list_url`
- [ ] Update the INCUBATOR JIRA issue with SGA received status

---

#### 2c — IP Clearance file

Whether or not an SGA is required, a formal IP Clearance must be opened in the
Incubator SVN to record provenance and dependency audit results. This is
separate from the SGA and must be completed before the first release.

```python
# IP Clearance lives in the Incubator SVN:
#   https://svn.apache.org/repos/asf/incubator/public/trunk/ip-clearance/
# File naming convention: <resource>-ip-clearance.xml

ip_clearance_file = {
    "svn_path":       f"incubator/public/trunk/ip-clearance/{resource}-ip-clearance.xml",
    "filed":          None,   # True / False
    "filed_date":     None,   # ISO date
    "review_complete": None,  # True / False — IPMC has reviewed the file
    "svn_revision":   None,   # SVN revision number when filed
}

if not ip_clearance_file["filed"]:
    sga_failures.append(
        f"IP Clearance file not yet created at "
        f"{ip_clearance_file['svn_path']}"
    )
```

Manual checks:

- [ ] Check out or browse the Incubator SVN at `https://svn.apache.org/repos/asf/incubator/public/trunk/ip-clearance/`
- [ ] Copy an existing IP clearance file as a template (e.g., `seata-ip-clearance.xml`)
- [ ] Fill in: podling name, donating organisation, incoming licence, dependency audit summary
- [ ] Commit the file and record `svn_revision`
- [ ] Post the file to `general@incubator.apache.org` for IPMC review

---

#### Phase 2 — Write results

```python
sga["failures"]        = sga_failures
sga["repos_gate_open"] = repos_gate_open
sga["ip_clearance_file"] = ip_clearance_file
phase2_pass = len(sga_failures) == 0

print(f"\nPhase 2 — SGA Receipt: {'PASS' if phase2_pass else 'INCOMPLETE'}")

with open(OUTPUT, "a") as fh:
    fh.write("## Phase 2 — SGA Receipt\n\n")
    fh.write(f"SGA required: {sga_required}\n")
    fh.write(f"Submitted:    {sga.get('submitted_date') or 'NO'}\n")
    fh.write(f"Secretary ack: {sga.get('secretary_ack')}\n")
    fh.write(f"Repos gate:   {'OPEN' if repos_gate_open else 'BLOCKED — do not provision repos yet'}\n")
    fh.write(f"IP Clearance file filed: {ip_clearance_file.get('filed')}\n")
    if sga_failures:
        fh.write("\n**Failures:**\n")
        for f in sga_failures:
            fh.write(f"- {f}\n")
    fh.write(f"\nOverall: {'PASS' if phase2_pass else 'INCOMPLETE'}\n\n")
```

---

