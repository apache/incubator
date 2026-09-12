# Working through the candidates

What makes each script candidate a real problem. Quote the current policy
from the Policy MCP when reporting; these notes may lag it. Historical
examples, when present, are only past failures to watch for. They are not
rules that make the same kind of finding release-blocking by default.

## header-provenance: ASF header plus another copyright

The strongest signal. Often third-party code with an ASF header added, some
of it by bulk header tools. If the other holder donated the code under the
podling's software grant, it may be fine. Otherwise search for a distinctive
identifier from the file; if it exists upstream, it needs its original
header, a LICENSE entry and a licence category check. An ASF header on
third-party code is usually a -1.

The variant "ASF header followed by a third-party banner or licence tag"
is a web asset (Bootstrap, normalize.css, Font Awesome, a minified library)
whose upstream banner survived under an added ASF header. Compare with the
upstream file; the original header goes back and the component goes in
LICENSE. Confirm the same facts before treating another RC as blocked by
this pattern.

## provenance-note: "derived from", "ported from", "copied from"

A comment in a code file naming where the code came from. Most are
harmless. When the file carries only an ASF header and LICENSE says nothing
about the upstream, it is the relabelled third-party case above, found by
its own admission. Confirm with the upstream link in the comment.

## license-text: Apache License text differs from the canonical copy

A fact, not a candidate. The Apache License 2.0 is fixed text; any change
to its terms is a different licence. The script diffs sections 1 to 9
against `references/apache-license-2.0.txt` after normalising whitespace
and http/https. The appendix (fill-in instructions, where copies differ in
bracket style) and anything appended after it are not compared.

## header-third-party: a non-ASF header

Usually fine if the licence is Category A (or B as policy allows), it's in
LICENSE with a pointer to the full text, and any upstream NOTICE is carried
into ours.

## header-other-licence and licence-signal

Read the captured context. Many matches are harmless: a README saying GPL
isn't accepted, a licence-checker config, an optional dependency that isn't
bundled. It's a problem when the file or its component is under that licence
and is in the release. Category X can't be included. "MIT or GPL" can be
taken as MIT and LICENSE should say so; "MIT and GPL" can't. GPL with
Classpath Exception has its own tests in `resolved_licenses`.

## header-spdx-only

Report what the current `source_headers` policy says about SPDX-only lines.

## no-header

RAT covers this and it's usually minor. Check the exceptions in
`source_headers` first, then read the archive's own audit configuration.
The script reports where it is, as an `info` line under this check, and how
many paths it excludes. It is not always `.rat-excludes` or
`.licenserc.yaml`: the apache-rat Maven plugin keeps the list inside
`pom.xml`, so an archive with no dotfile can still have hundreds of
excluded paths. Read the file and the comments around the exclusions, which
usually say why. A path excluded there is the project
saying it already considered the question, and the reviewers who ran RAT
saw nothing. Say so rather than reporting the count. Third-party test
material is the common case: TPC-DS and TPC-H query text, captured golden
plans and similar fixtures are not ASF-authored, so the ASF header does
not belong on them and a header is not what is missing.

A whole language's worth of files with no header, with the exclusions and a
comment explaining them, is a documented decision, not a finding. Upstream
files that never carried a header and are Apache-licensed by their origin
are the usual case. Do not call it release-blocking without reading the
exclusions first.

The exclusions cut both ways, so read what they cover and not just that they
exist. An exclusion naming files, or a generated or test-resource directory,
is a decision about those files. One that sweeps a whole file type is not: a
project can make RAT pass by excluding everything. The script reports these
separately as a candidate, for any pattern ending in `*.<ext>` that recurses
or has no directory part, where the extension is one the header policy
covers. It is common. Of six archives checked, five excluded `**/*.md`, and
one also excluded `**/*.js`, `**/*.php` and `**/*.pl`, which are source.

That is not automatically a finding either. Markdown that is all generated,
or a directory of vendored scripts, can be a fair exclusion. What it means is
that a clean RAT run says nothing about those files, so if the header
question matters for them, check them yourself rather than resting on the
project's audit. Exclusions for `.json`, `.lock`, `.iml`, `.pem` and the like
are routine and are not reported: a header does not belong in them.

Otherwise: a few test files are commonly fixed next release; many files,
or core source, is worth raising. If the file looks like a
third-party library, treat it as a provenance question. Documentation
files (.md, .rst, .adoc) are listed too, since the policy FAQ says it
applies to documentation; README and similar informational files are
exempt. Header-less documentation entries are normally "should fix" unless
they are extensive enough to show systematic release preparation problems or
they expose a provenance/licensing concern. A whole documentation tree
without headers did draw a -1 on Texera 1.2.0 RC3, so extent is what moves
this from cleanup to blocking.

## junk: macOS AppleDouble sidecar files

A "._name" beside every real entry means the archive was rolled on macOS with
COPYFILE_DISABLE unset. They are resource forks, not content. bsdtar folds
them back into extended attributes and does not list them, so a reviewer on
macOS sees a clean archive while GNU tar and Python extract two files for
every one. Reported once with a count, not per file. Check whether the count
matches the number of real entries, which tells you it is the whole archive
rather than a stray few.

## vendored

Check every component: its own licence file (not package metadata), its
category, its LICENSE entry, its NOTICE. `node_modules/` in a source release
is almost always a mistake.

## binary

A source release can't contain compiled code, including gradle-wrapper.jar
and maven-wrapper.jar. Those two are reported as facts. Binary data that
isn't compiled code is a different question.

A `.jar` is a zip, so the script opens it rather than judging the extension.
A jar of `.class` files is compiled code. A jar with none is a test fixture
and is reported as a nested archive: Java test trees are full of them, an
`empty.jar` for the empty case, jars of resources, jars with only a
manifest. Listing those beside a wrapper jar as though they were the same
finding sends the release manager after the wrong files. Check what the
script says is inside before calling a jar a blocker.

## nested-archive

Compressed test data with no compiled code is fine. Compiled files inside
make it a binary finding. If it couldn't be read, someone needs to open it.

## media

Mostly fine. Fonts and icon sets carry their own licences (OFL, CC-BY,
Apache-2.0) and need a LICENSE entry like any other bundled component. The
script lists them but cannot tell whether LICENSE covers them, so that part
is yours.

The question is only whether the file is in this archive. If it is, this
archive's LICENSE has to account for it, whatever the binary distribution's
LICENSE says. Web console trees are where they hide: look under `ui`,
`webapp`, `console-fe`, `static`, `assets` and `dist`. Seata 2.7.0 shipped
Roboto, aliyun and iconfont in the source tree with none of them in the
source LICENSE.

## license

LICENSE describes what's in this archive: every bundled component with a
pointer to its licence text, and nothing that isn't bundled. Compare the
vendored and third-party-header lists against its sections. Unreferenced
licence files may be stale or may be a missing entry.

A pointer that runs into a placeholder, as in "the text of each license is
also in licenses/LICENSE-[project].txt", is a sentence explaining the
convention to the reader, not a path. The script skips those. If you are
reading LICENSE yourself, do the same before reporting a missing file.

## notice

Required notices only. Common problems: licence text in NOTICE, attributions
that aren't required or aren't bundled, missing notices from bundled
Apache-licensed works. An old year is usually fixed next release.

## disclaimer

Every release needs the incubation disclaimer. The script compares it with
the standard or WIP text and lists missing wording. Different wording is
allowed only with IPMC approval, so check for that before raising it.
DISCLAIMER-WIP is for releases that knowingly don't meet policy and must list
the known issues; an empty list or the placeholder is a problem.

Only `DISCLAIMER` and `DISCLAIMER-WIP` are the incubation disclaimer. A
project may ship other documents under that prefix, such as a
`DISCLAIMER-BINARIES.txt` listing the test fixtures in the tree. The script
names those in an `info` line and does not hold them to the incubation
wording. Read them, since they often explain binaries you were about to ask
about, but don't report one as a defective disclaimer.

## vs-tag

Files in the archive but not the tag, or different from it, matter. Files
only in the tag are usually deliberate, with one exception the script
reports: a top-level directory left out of the archive while the archive's
README, Dockerfile, pom.xml or other build file still refers to it. The
documented build then fails from the released source.

Git submodules are the common false positive. A shallow or plain clone of
the tag holds an empty directory where each submodule should be, so every
file the release bundled there looks like an addition, thousands of them.
The script reads `.gitmodules`, drops those paths from the comparison and
says so in an `info` line. Those files are still worth looking at, as
bundled third-party code that LICENSE has to cover, but they are not
something the release manager added by hand.

## Binary artifacts

Review each separately. Their LICENSE and NOTICE must cover what's inside:
bundled and shaded jars, web assets, native libraries. Javadoc jars carry
third-party JavaScript and the JDK `legal/` directory; `resolved_licenses`
says when that's allowed.

## signature

A good signature from a key in KEYS is the whole check. Two things that look
wrong and are not:

- A signing key whose user ID is `<private@podling.apache.org>`, such as
  "Apache KIE Automated Release Signing". That is the PPMC's private list
  address on an automated release signing key Infra issues to projects with
  a reproducible-build pipeline. It is a sanctioned arrangement, not a
  shared personal key. It has been raised on the list and settled. Don't
  report it.
- A key that has expired since the vote. gpg judges expiry against today, so
  an older release whose signer later let a key lapse still verifies as
  valid at the time it was signed. The script compares the signature
  timestamp with the expiry and only fails when the key was already expired
  when the release was signed.

Worth raising: the key that signed the artifact is not the key the vote
email names. Both may be in KEYS and the signature verifies, but anyone
following the email checks the wrong signer.

## Not visible to the script

Say these weren't checked unless someone did:

- Copied files whose original header was replaced entirely. Libraries,
  polyfills, templates and algorithms are worth a search upstream. Doc
  comments reproduced word for word from the upstream are the giveaway.
- The Maven staging repository named in the vote email. The script only
  opens what is in dist/dev unless the staging artifacts are downloaded into
  a separate `--rc-dir`. List the staged artifacts, identify the staged
  source release archive without assuming a fixed file name, run the checker
  on that archive, and inspect bundled or shaded jars by comparing their
  contents with `META-INF/LICENSE` and `META-INF/NOTICE`. Two things that
  have gone wrong here and are invisible from dist/dev alone: the staged
  source archive was not the dist/dev one, having been assembled from the
  release manager's working directory (Fesod 2.1.0 RC2), and a BOM named an
  artifact that was never staged (Seata 2.7.0).
- Generated code that carries a licence.
- Whether the software grant and ICLAs cover the code.
- Cryptography needing an export notice (`crypto_policy`).
- Whether the source builds.
- Symlinks. The script skips them, and a link whose target is not in the
  release will not be reported.
