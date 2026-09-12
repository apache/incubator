---
name: podling-release-check
description: >
  Checks an Apache Incubator podling release candidate before or during its
  vote: signatures, checksums, naming, DISCLAIMER, LICENSE and NOTICE, headers,
  bundled third-party code, binaries, and whether issues raised on the
  podling's earlier votes have been fixed. Uses the ASF Policy MCP for the
  current rules and the Incubator mail and release MCPs for the podling's
  history. Use it whenever someone asks to check, review, verify or validate a
  podling release or RC, asks "is our release ready to vote on", is about to
  call a PPMC or IPMC release vote, is voting on a [VOTE] Release thread on
  general@incubator, or wants to know why an earlier RC was voted down. It
  produces findings for a person to review, never a vote.
---

# Podling release check

Find things for a person to check. Never vote and never say a release
passes. Never report a script candidate as a finding until it has been
looked at.

## Setup

Get the podling, RC, tag and dist/dev URL from the vote email. If only a name
is given, confirm it's a current podling with `podlings:get_podling`.

Step 4 needs a shell with network access. Without one, do the other steps and
say the archive contents were not checked.

No MCP server is required. If one is missing, fetch the same source over HTTP
(`references/tools.md` lists the endpoint for each), say so in the report,
and still do the step.

## 1. Current rules

Read these from the Policy MCP each run, since policy changes:
`incubator`, `release_policy`, `resolved_licenses`, `source_headers`,
`release_distribution` and `licensing_howto`, the guide to assembling LICENSE
and NOTICE. Use `asf-policy:search_policies` for anything specific. Cite each
document's own URL, not the MCP.

Compare the two disclaimer texts in the `incubator` policy with
`references/disclaimer-standard.txt` and `references/disclaimer-wip.txt`.
If the policy wording has changed, update those files (placeholders in
braces) before step 4.

## 2. Previously raised issues

`incubator-mail:podling_release_vote_history(podling, timespan="lte=36M")`,
then read every -1, 0, CANCEL and "I checked" message in full with
`get_incubator_general_email`. Check the dev list for the PPMC vote with
`search_podling_mail`. Each issue found becomes a check in step 5: is it
fixed in this RC? Read the messages rather than adding up a tally
(`references/tools.md`).

## 3. Inventory

`incubator-releases:podling_releases(podling, dist_base="https://dist.apache.org/repos/dist/dev/incubator")`
lists what is in dist/dev and, in the same response, the podling's earlier
releases from archive.apache.org. Compare the RC with the last release:
same artifact set, checksum and signature files for each.

If the vote email names a Maven staging repository, inspect it as part of the
RC. List the staged artifacts from the repository index or metadata. Treat
the staged source release archive, source jars and any bundled/shaded jars as
part of what is being voted on. Identify the source release archive from the
vote email, Maven classifiers, repository metadata or artifact names; do not
assume a fixed file name. Download it into a separate directory and run the
script with `--rc-dir` against that directory too. For
bundled or shaded jars, list the jar contents and compare `META-INF/LICENSE`
and `META-INF/NOTICE` with what is actually inside (`references/checks.md`,
"Binary artifacts").

## 4. Script

```bash
python3 scripts/check_rc.py --url <dist/dev RC directory> --podling <slug> \
  --disclaimer-template references/disclaimer-standard.txt \
  --wip-template references/disclaimer-wip.txt \
  --tag-dir <checkout at the release tag> --out <workdir>
```

`--url` is the directory that holds the archives themselves; the script
doesn't descend into subdirectories. `--tag-dir` is optional but is what
finds modules dropped from the archive. Use `--rc-dir` for an RC already
downloaded. If the RC has been removed from dist/dev, `svn log -v` on the
podling's dist/dev directory gives the revision it was added at, and
`svn export <url>/<rc>/@<rev> <dir>` recovers the exact files that were
voted on. Read `findings.md`. `fail` items are facts and
can be reported as they are. `candidate` items go to step 5. The script
doesn't build or run RAT.

## 5. Candidates

Work through them with `references/checks.md`. Say what was looked at for
each one. Historical reviewer comments are examples, not automatic severity:
decide whether the same issue is release-blocking in this RC based on current
policy, scale, provenance risk and whether it changes the legal contents of
the release.

## 6. Published elsewhere

`ipmc:release_artifact_evidence(podling, include_platforms=true)`: is this
version already on Maven Central, PyPI, npm, crates.io or Docker Hub before
the IPMC vote has passed?

## 7. Report

1. Previously raised: each issue, fixed or not, with a link.
2. Must fix, needs a new RC: findings that change what is inside an archive,
   so the artifacts have to be rebuilt and re-signed. Path, evidence and
   policy link.
3. Must fix, no new RC needed: real problems that can be corrected while the
   vote runs without touching the artifacts. Where the RC is staged, a
   missing KEYS link, an announcement or download page. These get raised and
   fixed in flight; they are not a reason to vote against the artifacts.
4. Should fix: real issues commonly accepted for the next release, including
   minor or isolated source-header cleanup.
5. Looked at, fine: one line each.
6. Not checked: the build, RAT, anything skipped.

Sorting between 2 and 3 is the useful judgement. Ask whether fixing it
changes a byte of any artifact. If it does not, the release manager can fix
it during the vote and the vote stands.

For a mailing list, use the IPMC style: an "I checked:" list, then the
issues, no headings or bold, no vote. If nothing is found, say what was
checked; don't call the release compliant.

## 8. Vote result (only when asked)

For a release manager writing the RESULT email. Read every message in the
thread yourself and take each person's latest vote.

Only IPMC votes are binding. Check voters against the IPMC roster from
`apache-projects-mcp:get_committee("incubator")`. PPMC members who aren't on
the IPMC are non-binding. Match on @apache.org addresses and names; mark
anyone you can't match as unknown. The IPMC vote needs at least three
binding +1s and more binding +1s than -1s. Release votes can't be vetoed.

The dev@ vote before it needs at least three PPMC +1s and more +1s than -1s
(`incubator` policy). Use `get_project_people(<slug>)` to count those, but
don't call them binding.

When a vote raises something this skill missed, add it to the script if it
can be detected mechanically, otherwise to `references/checks.md`.
