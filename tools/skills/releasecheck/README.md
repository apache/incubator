# releasecheck

Check a podling release candidate before or during its vote: signatures,
checksums, naming, DISCLAIMER, LICENSE and NOTICE, headers, bundled code,
binaries, and whether issues from earlier votes are fixed. Runs
`scripts/check_rc.py` for the mechanical part and reports findings for a
person; it never votes.

These are maintainer notes. The skill itself is `SKILL.md`; read that to run
a review.

## Layout

| Path | What it is |
| --- | --- |
| `SKILL.md` | The review process, eight steps. The agent's entry point. |
| `scripts/check_rc.py` | The mechanical checks. Standard library plus the `gpg` binary, no MCP, no third-party packages. |
| `scripts/test_check_rc.py` | Regression test. Builds a release candidate with known faults, runs the checker over it, asserts every planted fault is found and that known false positives stay absent. |
| `references/checks.md` | What each check means and how to judge it. Read when working through candidates. |
| `references/tools.md` | Quirks of the MCP servers the review steps use. |
| `references/apache-license-2.0.txt` | Canonical AL2 text, for comparing a LICENSE against. |
| `references/disclaimer-standard.txt`, `disclaimer-wip.txt` | Disclaimer templates, placeholders as `{}`. |

## What the script checks

All of it is deterministic: the same archive gives the same `findings.md`
under any model, or none. Findings are graded, and the grade is the contract.
A `fail` is a fact that needs no judgement. A `candidate` is something a
person has to look at, and most turn out to be fine.

| Check | What it does |
| --- | --- |
| `artifacts`, `extract` | Inventories the RC directory, unpacks each archive, finds the real root even when the archive nests twice. |
| `naming` | "incubating" in every artifact name; identifies which archive is the source release. |
| `checksum` | SHA-512/256 recomputed and compared; flags MD5 and SHA-1 as too weak. |
| `signature` | GPG verify against KEYS, tried across the release area, dist/dev, the archive, and the project's own name. Key expiry is judged against the signature date, not today. |
| `root-files`, `layout` | LICENSE, NOTICE and DISCLAIMER at the top level; single top-level directory. |
| `disclaimer` | Compared with the standard and WIP templates, placeholders skipped. Reads back the WIP known-issues list and spots an unfilled one. Other `DISCLAIMER-*` documents are named, not judged. |
| `license`, `license-text` | AL2 body diffed against the canonical text; pointers to licence files resolved, placeholders ignored; licence files nothing references. |
| `notice` | Licence text in NOTICE, stale copyright year. |
| `header-*`, `no-header`, `licence-signal`, `provenance-note` | Every text file classified: ASF header, third-party header, ASF header over a foreign copyright, SPDX-only, no header. Flags "copied from" notes and licence strings needing a look. Finds the project's own RAT config and reports exclusions that sweep a whole file type. |
| `binary`, `nested-archive` | Compiled code in a source release. Jars and zips are opened and judged on contents, so a wrapper jar and an empty test fixture are not the same finding. |
| `vendored`, `junk`, `media`, `data` | Bundled third-party directories, `.idea`/`.DS_Store`/macOS sidecars, fonts and images carrying their own licences, test data. |
| `vs-tag` | Archive against the git tag: files that differ, files not at the tag, and directories dropped from the archive that the archive still refers to. Unfetched git submodules are excluded. |

It never says whether a release should pass.

## MCP servers

The script needs none. The review steps in `SKILL.md` use six, all read-only,
and a review still works without them at reduced coverage.

| Server | Used for | Step |
| --- | --- | --- |
| `asf-policy` | The current `incubator`, `release_policy`, `resolved_licenses`, `source_headers` and `release_distribution` documents, re-read each run because policy changes. | 1 |
| `incubator-mail` | The podling's earlier vote threads, to check whether what was raised last time is fixed. Also the dev list for the PPMC vote. | 2 |
| `incubator-releases` | What is staged in dist/dev and what the podling released before, to compare artifact sets. | 3 |
| `podlings` | Confirming a name is a current podling when the vote email gives nothing else. | Setup |
| `ipmc` | Whether the version is already on Maven Central, PyPI, npm, crates.io or Docker Hub before the vote has passed. | 6 |
| `apache-projects-mcp` | The IPMC roster, to work out which votes are binding. | 8 |

`references/tools.md` records each server's quirks and, for each one, the
public endpoint to fetch directly when it is not installed.

## Running the checker on its own

```
python3 scripts/check_rc.py --url <dist/dev RC directory> --podling <slug> \
  --disclaimer-template references/disclaimer-standard.txt \
  --wip-template references/disclaimer-wip.txt \
  --tag-dir <git checkout at the tag> --out <working directory>
```

`--rc-dir` replaces `--url` for artifacts already downloaded. Read the
`findings.md` it writes, not `findings.json`; the JSON carries every item with
full evidence and is for grepping one check.

An RC that has passed its vote is in the archive at
`https://archive.apache.org/dist/incubator/<podling>/<version>/`, which is far
faster than recovering it from Subversion. Only cancelled RCs need `svn`.

## Running the test

```
python3 scripts/test_check_rc.py
```

It prints `PASS` and exits 0. The `exit code 1 (expected 1)` line above that
is the checker's own exit code, asserted to be 1 because the fixture contains
hard failures. Add a planted fault for every behaviour change.

## How this was evaluated

Run blind against 50 release candidates from 40 podlings, voted between
30 January 2024 and 7 September 2026: the opening vote email only, findings
written down, then the thread read and compared. 53 runs in all, because a
release staged as several archives is one run per archive.

The sample: Amoro, Answer, Asyncband, Auron, Baremaps, BifroMQ, Burr, Casbin,
Celeborn, Cloudberry, DevLake, Fesod, Fluss, Fory, GeaFlow, Gluten, GraphAr,
Gravitino, Hamilton, HertzBeat, HugeGraph, Iggy, KIE, Livy, Otava, OzHera,
Paimon, Polaris, ResilientDB, SDAP, Seata, Seata-go, StormCrawler,
StreamPark, Teaclave, Texera, Training, Uniffle, Wayang, XTable.

| Result | Count |
| --- | --- |
| Correct call | 46 |
| Partial | 1 |
| Missed a real blocker | 2 |
| False blocker | 1 |

Four of those releases passed their vote carrying a clear policy violation:
compiled code in a source release three times, and an archive name with no
"incubating" in it once. In total the checker surfaced 13 problems that no
reviewer mentioned in the thread.

Most changes to `check_rc.py` came from its own false positives rather than
from misses. A false failure is worse than a missed one: it sends a release
manager after nothing and teaches reviewers to discount the report. Anything
reported as `fail` must be a fact that needs no judgement.

## Cost

`check_rc.py` writes `findings.md`, which is what a reviewer reads. Across
those 53 runs it averaged 8.8 KB, roughly 2,200 tokens. The spread is wide:
513 bytes for the cleanest candidate, and 29 KB for a source release holding
four repositories and 40,000 files.

The report is not the cost. A full review is dominated by step 5, working
through the candidates by hand. Budget roughly 20k to 50k tokens per release
in a warm session. A small, clean candidate runs nearer 10k to 15k; a large
one with a lot to look at runs 50k to 80k. Step 1 reads six policy
documents, about 40k tokens, but that is once per session rather than once
per release, so a single review in a fresh session costs 60k to 90k all in.

Read `findings.md`, not `findings.json`. The JSON holds every item with full
evidence and is meant for grepping a specific check. One candidate with
thousands of repeated findings produced a 3.4 MB JSON file, around 870k
tokens if anything read it whole, against a 25 KB summary.
