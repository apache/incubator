# Report template

Title: Apache Maturity Model evidence pack for Apache <Name> (incubating),
<date>, model v<version>.

Opening paragraph, always: what was checked, which servers were available,
what the sample sizes were (pull requests read, list timespan searched,
release checked). Then the sentence: "This is an evidence pack to support a
self-assessment by the PPMC. The model is a guide, not a requirements
document, and has no scores or levels; nothing here is a verdict."

## Summary

One line per section (Code, Licenses and Copyright, Releases, Quality,
Community, Consensus Building, Independence, Trademark and Branding): the
one thing in that section most worth the PPMC's attention, then the
counts (evidenced, proxy, left to the PPMC) at the end of the line. The
counts barely vary between podlings; the attention item is the content.

## Items

One table per section, in model order.

| ID | State | Evidence | For the PPMC |
| --- | --- | --- | --- |
| CD10 | Evidenced | Repo apache/foo public; LICENSE is ALv2; 4 source releases on archive.apache.org (checked 2026-11-07) | |
| CD30 | Proxy | Maven build; CI on PRs, green on main at <sha>; build page at <url> | Has anyone outside the core team built a release from the docs alone? |
| QU10 | Human | | Does the project describe known limitations where a new user would see them? |

Rules for the cells:

- **State** is Evidenced, Proxy or Human, from `references/items.md`.
  Downgrade (never upgrade) when the tool call failed or the sample was
  too small; say why in Evidence.
- **Evidence** holds facts with their source and date, short enough to
  read. A URL per fact where there is one. Numbers carry their window
  ("12m"). A proxy cell states the signal and stops; it does not say
  "looks fine".
- **For the PPMC** holds the question from `references/items.md`, adapted
  to what was found. An Evidenced item leaves it blank unless the
  evidence turned up a gap, in which case the gap goes here as a
  question ("Release 1.2.0 has no tag; which commit was it built from?").
- An item where a fact contradicts the claim (a release with no vote, a
  Category X dependency, a missing Security link) gets the fact in
  Evidence and the question in For the PPMC. Do not write "fails".

## Gaps and findings

Facts that contradict an item, one per bullet, most consequential first,
each with its item ID and source. This is the list the PPMC acts on.

## Not checked

What was skipped, and why: a server down, a build not run, a list not
readable, a health report that was not generated for this podling.

## For a mailing list

When the result is to be posted, drop the headings, keep the opening
paragraph, the per-section one-liners, the gaps list and the not-checked
list, and attach or link the full tables. No bold, no verdict.
