---
name: release-vote-reviewer
description: Review an Apache Incubator release vote and draft the +1 or -1 response. Use this skill whenever a user asks to review a release vote, check a release candidate, verify signatures/checksums/DISCLAIMER on an incubating release, tally vote maths on a general@ VOTE thread, or decide how to vote on a podling release. Triggers on phrases like "review this release vote", "check the RC", "should I +1", "verify the release artifacts", "vote thread", "release candidate for <podling>", or "walk the release checks".
---

# Release Vote Reviewer

## Purpose

Given an Apache Incubator release vote thread on general@, perform a complete
release review and draft a binding or non-binding vote response (+1 or -1)
with explicit reasons for each check.

## Checks performed

1. **Artifacts** — verify all expected release artifacts (source, binaries, checksums, signatures) are present on the staging repository.
2. **Signatures and checksums** — validate GPG signatures against the project KEYS file and verify SHA checksums match the published artifacts.
3. **DISCLAIMER** — confirm the DISCLAIMER (or DISCLAIMER-WIP) file is present in the source release and contains the correct incubator wording.
4. **Incubating in the name** — confirm the release artifact names and version strings include "incubating" as required by Incubator policy.
5. **Vote maths** — tally binding vs. non-binding votes, check whether the minimum threshold (3 binding +1s, more +1s than -1s) has been met.

## Artifact fetch and incubating filename check

Use the **incubator-releases** MCP server to perform the following steps:

1. **Retrieve the staging index** — fetch the directory listing at the staging
   URL given in the vote email (e.g.
   `https://dist.apache.org/repos/dist/dev/<podling>/<version>/`).

2. **List all filenames** — collect every filename in the listing, including
   source tarballs, binary archives, checksums (`.sha512`), and signatures
   (`.asc`).

3. **Check each filename for "incubating"** — for every file, assert that the
   filename contains the substring `incubating` (case-insensitive). Record
   each filename that fails this check.

4. **Download each artifact** — fetch the full content of each non-metadata
   file (source tarballs, binary archives) via the MCP server so that
   subsequent checks (checksums, signatures, DISCLAIMER) can operate on the
   actual bytes.

5. **Report results** — produce a per-file table:

   | Filename | Contains "incubating" | Downloaded |
   |----------|----------------------|------------|
   | `<name>` | PASS / **FAIL**      | yes / no   |

   If any file fails the incubating-name check, mark this section **-1** and
   include the offending filenames in the final vote reply.

## Checksum verification

Use the **incubator-releases** MCP server to perform the following steps:

1. **Enumerate checksum sidecar files** — from the staged artifact list,
   identify every file with a `.sha256` or `.sha512` extension. Each sidecar
   file contains the expected digest for the artifact that shares its base
   name (e.g. `foo-1.0-incubating-src.tar.gz.sha512` covers
   `foo-1.0-incubating-src.tar.gz`).

2. **Read the published digest** — fetch the contents of each sidecar file and
   extract the hex digest string, ignoring any trailing filename annotation
   that some tools append.

3. **Compute the actual digest** — using the artifact bytes downloaded in the
   artifact fetch step, compute the matching digest:
   - SHA-256 for `.sha256` sidecars
   - SHA-512 for `.sha512` sidecars

4. **Compare digests** — perform a constant-time string comparison between the
   published digest and the computed digest. They must match exactly
   (case-insensitive hex).

5. **Flag missing sidecars** — if an artifact has no corresponding `.sha256`
   or `.sha512` sidecar, record it as a failure; ASF policy requires at least
   one checksum file per artifact.

6. **Report results** — produce a per-artifact table:

   | Artifact | Sidecar | Algorithm | Published digest (truncated) | Computed digest (truncated) | Match |
   |----------|---------|-----------|-----------------------------|-----------------------------|-------|
   | `<name>` | `<name>.sha512` | SHA-512 | `abc123…` | `abc123…` | PASS / **FAIL** |

   If any digest does not match, or if any artifact is missing a checksum
   sidecar, mark this section **-1** and include details in the final vote
   reply.

## DISCLAIMER file check

Use the **incubator-releases** MCP server and the **asf-policy** server to
perform the following steps:

1. **Identify the source artifact** — from the staged file list, select the
   source release tarball (typically named `*-src.tar.gz` or `*-source*.zip`).
   Use the artifact bytes downloaded in the artifact fetch step.

2. **Unpack the archive** — extract the top-level directory of the tarball or
   zip in memory (or a temporary location) far enough to list its root-level
   files without unpacking the entire tree.

3. **Locate the DISCLAIMER file** — check for a file named exactly
   `DISCLAIMER` or `DISCLAIMER-WIP` at the root of the unpacked source tree.
   - `DISCLAIMER` is required for podlings that have not yet resolved their
     IP clearance.
   - `DISCLAIMER-WIP` is the alternative accepted during the incubation period
     when the disclaimer text differs slightly.
   - If neither file is present, this check fails immediately.

4. **Read the required text** — use the **asf-policy** server to retrieve the
   current canonical DISCLAIMER text mandated by the Apache Incubator. This
   avoids hardcoding text that may change over time.

5. **Verify the file contents** — compare the content of the located
   DISCLAIMER (or DISCLAIMER-WIP) file against the canonical text:
   - The file must contain all required lines from the canonical template.
   - Minor whitespace differences are acceptable; missing or altered sentences
     are not.
   - Record any lines that are absent or materially different.

6. **Report results**:

   | Check | Result | Notes |
   |-------|--------|-------|
   | DISCLAIMER or DISCLAIMER-WIP present | PASS / **FAIL** | |
   | File contents match canonical text | PASS / **FAIL** | list deviations |

   If the file is absent or its content does not match the required wording,
   mark this section **-1** and quote the missing or incorrect text in the
   final vote reply.

## GPG signature verification

Use the **incubator-releases** MCP server to perform the following steps:

1. **Fetch the KEYS file** — download the project KEYS file from the canonical
   location (typically
   `https://dist.apache.org/repos/dist/dev/<podling>/KEYS` or the URL stated
   in the vote email). Import all public keys it contains into a temporary GPG
   keyring.

2. **Enumerate signature files** — from the staged artifact list collected in
   the previous section, identify every file with a `.asc` extension. Each
   `.asc` file is a detached GPG signature for the artifact that shares its
   base name (e.g. `foo-1.0-incubating-src.tar.gz.asc` signs
   `foo-1.0-incubating-src.tar.gz`).

3. **Verify each signature** — for each `.asc` / artifact pair:
   - Confirm the paired artifact was successfully downloaded in the artifact
     fetch step.
   - Run GPG detached-signature verification of the `.asc` file against the
     artifact bytes using the imported keyring.
   - Record the signing key fingerprint, the key owner's UID, and whether
     that key is present in the project KEYS file.

4. **Check signer identity** — warn if a signature was made by a key that is
   not listed in the project KEYS file, as this may indicate a key not yet
   published by the release manager.

5. **Report results** — produce a per-artifact table:

   | Artifact | Signature file | GPG result | Key in KEYS |
   |----------|---------------|------------|-------------|
   | `<name>` | `<name>.asc`  | PASS / **FAIL** | yes / **no** |

   If any artifact fails signature verification, or if no `.asc` file exists
   for an artifact, mark this section **-1** and include details in the final
   vote reply.

## Vote tally and pass/fail determination

Use the **incubator-mail** MCP server to perform the following steps:

1. **Fetch the full vote thread** — retrieve all messages in the vote thread
   from general@incubator.apache.org using the message-id or URL supplied by
   the user. Include replies so that vote responses, clarifications, and
   vote changes are all visible.

2. **Identify voters** — for each reply, extract the sender's email address
   and the vote they cast. Accepted vote tokens are `+1`, `0`, and `-1`
   (with or without surrounding text). If a voter posts more than once, use
   only their most recent vote.

3. **Classify binding vs. non-binding votes** — use the **asf-policy** server
   to obtain the current PPMC (podling PMC) and IPMC (Incubator PMC) member
   lists for the podling in question:
   - **Binding**: votes cast by IPMC members (mentors and general IPMC
     members). PPMC member votes are non-binding on the Incubator general@
     vote (they are binding on the podling's own dev@ vote, not here).
   - **Non-binding**: all other voters, including PPMC members who are not
     also IPMC members.
   - Note any voters whose binding status cannot be determined and flag them
     as "unknown".

4. **Tally the votes** — count separately:
   - Binding +1s
   - Binding 0s
   - Binding -1s
   - Non-binding +1s / 0s / -1s

5. **Apply the pass criteria** — the vote passes only when **all** of the
   following conditions are met:
   - At least **3 binding +1s**.
   - More binding +1s than binding -1s.
   - No unresolved binding -1s (a -1 is resolved only if the voter
     explicitly withdraws it or changes their vote to +1 or 0 in a later
     message in the thread).

6. **Report results**:

   | Voter | Email | Binding | Vote |
   |-------|-------|---------|------|
   | Alice | alice@… | yes (IPMC) | +1 |
   | Bob   | bob@…   | no (PPMC only) | +1 |

   **Summary**

   | | Binding | Non-binding |
   |-|---------|-------------|
   | +1 | N | N |
   | 0  | N | N |
   | -1 | N | N |

   **Outcome**: PASS — 3 or more binding +1s and no unresolved binding -1s.
   *or*
   **Outcome**: **FAIL** — fewer than 3 binding +1s / unresolved binding -1 from
   `<voter>` (`<reason given>`).

   Include the outcome in the final vote reply.

## Draft vote response

After all checks are complete, compose a ready-to-send email reply to the
vote thread. Follow these rules:

### Determine the overall vote

- Cast **+1** only if every check in the sections above passed:
  - All artifact filenames contain "incubating"
  - All GPG signatures verified against keys in the KEYS file
  - All checksums match the downloaded artifacts
  - DISCLAIMER (or DISCLAIMER-WIP) is present and contains the required text
  - Vote tally meets pass criteria (≥3 binding +1s, no unresolved binding -1s)
- Cast **-1** if any single check failed. A -1 blocks the release.

### Email format

```
Subject: Re: [VOTE] Release Apache <Podling> <version> (incubating)

+1 (binding)        ← or -1 (binding) — adjust as appropriate

I have reviewed this release and checked the following:

[ ] Artifacts
    All filenames contain "incubating": PASS
    <list each artifact>

[ ] GPG signatures
    KEYS file fetched from: <url>
    <artifact>: signed by <Key ID> (<UID>) — PASS / FAIL: <reason>

[ ] Checksums
    <artifact>.sha512: PASS / FAIL: <reason>

[ ] DISCLAIMER
    File present: PASS / FAIL
    Contents match canonical Incubator text: PASS / FAIL: <reason>

[ ] Vote tally (informational — not a blocker for my individual vote)
    Binding +1s: N  (need ≥3)
    Binding -1s: N  (need 0 unresolved)
    Outcome: PASS / FAIL

Overall: +1 / -1

<if -1, summarise each blocking issue here, one bullet per failed check>

<Your Name>
```

### Guidance on reasons

- For each **PASS**, include a one-line confirmation (e.g. the signing key
  fingerprint, the digest algorithm used, the exact DISCLAIMER filename found).
- For each **FAIL**, quote the specific discrepancy: the offending filename,
  the mismatched digest values (truncated to 16 hex chars is sufficient), the
  missing DISCLAIMER line, or the unresolved -1 voter's name and stated
  objection.
- Do not omit any check from the email even if it passed — reviewers rely on
  seeing the full list to trust the review.
- Mark the vote `(binding)` if the agent is acting on behalf of an IPMC
  member; otherwise use `(non-binding)`.

## Required MCP servers

- **incubator-releases** — access to the Apache Incubator staging and release repositories to fetch and inspect artifacts, checksums, and signatures.
- **incubator-mail** — access to Apache mailing list archives to retrieve the vote thread from general@incubator.apache.org and any follow-up messages.
- **asf-policy** — access to ASF and Incubator policy documents to verify compliance requirements (naming, DISCLAIMER wording, release process rules).

## Usage

Invoke this skill with the URL or message-id of the vote thread on general@.
The skill will run all checks above and output a ready-to-send vote reply.
