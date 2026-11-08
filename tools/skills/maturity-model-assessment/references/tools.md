# Tool notes

Prefixes vary between setups (`ipmc:`, `IPMC MCP:`); match on the tool name.
None of these servers is required. Every one wraps a public source, so when
one is missing fetch the source directly, say so in the report, and still do
the step.

## Identify the podling first

| Need | Tool |
| --- | --- |
| Confirm it exists, get slug, mentors, homepage | `podlings:get_podling` |
| Rosters | `apache-projects-mcp:get_project_people(<slug>)` |
| Repositories | `apache-projects-mcp:get_repositories` |
| Releases | `ipmc:release_artifact_evidence` or `incubator-releases:podling_releases`; curl listing (below) for a source the tool reports as incomplete |
| Roster history, SGA, name search status | podling status page `incubator.apache.org/projects/<slug>.html`; often stale, sometimes empty (KIE has no roster, Hamilton's reads "Pending"), so compare with LDAP and the proposal and report the gap under CS10 |

A graduated project also appears in podlings.xml with an end date. This
skill reads Incubator sources, so it is for current podlings; say so and
stop if the name has graduated.

## GitHub (`gh` in a shell)

`gh` is the workhorse for repository facts and needs no MCP. Most podling
repositories are `apache/incubator-<slug>`, but not all (apache/hamilton,
apache/amoro); always take the names from `get_repositories`. KIE has
dozens; pick the main one by 90-day commits and say which. Useful calls:

```bash
gh api repos/apache/<repo>                                   # private flag, default branch, created_at
gh api repos/apache/<repo>/tags --paginate --jq '.[].name'   # CD40
gh api repos/apache/<repo>/contents/SECURITY.md              # QU30 (404 means absent)
gh api repos/apache/<repo>/contents/CONTRIBUTING.md          # CO20
gh pr list --repo apache/<repo> --state merged --limit 30 \
  --json number,author,mergedBy,title,mergedAt               # CD50, CO20, CO60
gh api repos/apache/<repo>/contents/.asf.yaml                # required_approving_review_count, to set against self-merges
gh api "repos/apache/<repo>/issues?state=open&sort=created&direction=asc&per_page=20"   # QU50
gh api repos/apache/<repo>/contributors --paginate --jq 'length'                        # CO20
gh api repos/apache/<repo>/community/profile                 # README, CONTRIBUTING, licence, CoC flags in one call
gh run list --repo apache/<repo> --branch <default> --limit 20   # CD30; check-runs on a commit returned 0 for some repos
gh api repos/apache/<repo>/git/tags/<sha>                     # date of an annotated tag (git/ref/tags gives the tag object, not the commit)
```

For CD50, a squash merge keeps the author (GraphAr) but a true merge
commit carries the merger as Author (OpenServerless); when the merge commit
shows the merger, read the PR's own commits. Pass the full 40-character
sha to `git/tags/<sha>`; a short sha returns 404. Percent-encode quotes in
`search/issues` URLs.

The shell here is bash 3.2: keep each command simple, one `$(...)` per
line, no nested loops with sed inside. The system grep is ugrep and
rejects long alternations; keep patterns short. `gh search code` rejects quoted
phrases combined with an `org:` scope; search one repository with plain
words.

Pull request authors and mergers are GitHub logins, not Apache IDs. Match
them to the roster by name where you can; otherwise count distinct logins
and say they were not mapped.

## Mailing lists (`incubator-mail`)

`search_podling_mail(podling, list_name="dev", query, timespan)` searches
the podling's dev list; `list_name="users"` where one exists (CO70).
`podling_release_vote_history(podling, timespan)` returns the general@
vote and result threads; pass `list_name="dev"` and
`domain="<slug>.apache.org"` for the PPMC vote on dev@. Searches ignore
quotation marks and `OR`: a query with `OR` returns zero hits, so search
each term separately. Narrow with `timespan` (`lte=12M`). The private list
is not readable and nothing here should try.

`podling_release_vote_history` searches "<podling> VOTE release", so it
returns nothing when subjects omit the word release ("[VOTE] Apache Toree
0.6.0 RC5") or the podling name (XTable's dev@ results read "[RESULT][VOTE]
Release 0.4.0-incubating"). When it returns zero or fewer threads than
there are releases, fall back to `search_podling_mail` and
`search_incubator_general_mail` with the plain query "VOTE" or "RESULT"
and filter subjects yourself.

Bracketed tags are tokenised: a query for "[DISCUSS]" also returned
[HEADS-UP] threads and "[PROPOSAL]" returned [VOTE] threads, so count
tagged threads from the subject lines, not the hit count. "veto" matched
"not veto" in a reply. Wildcard queries (`*`) return nothing. For a list's
raw volume with no query, call the API directly:
`curl -s "https://lists.apache.org/api/stats.lua?list=users&domain=<slug>.apache.org&d=lte%3D12M"`
and read `hits`. A lists.apache.org thread permalink fetched over HTTP
returns only the JavaScript shell; messages are readable only through the
mail tools. A deep-quoted message can be 50 KB or more; grep the body
rather than reading it.

For vote tallies read the [RESULT] message itself with
`get_incubator_general_email(id)` or `get_podling_email(podling, "dev", id)`;
`summarize_release_vote_thread` fetched only the opening message in the
GraphAr run and counted no votes. A 404 from `get_podling_email` on a
thread id quoted in a general@ message means the thread is on private@
(Pegasus); record that as the fact it is. GitHub Discussions mirrored to
dev@ arrive with "[D]" subjects and inflate [DISCUSS] and [VOTE] counts
(Texera); count native threads from the subject lines. The stats.lua
participants list shows only the top ten senders, usually GitHub relays;
use apache-health `dev_unique_posters` for human poster counts. For a list
that may not exist, stats.lua returns no `hits` field; confirm the list
set with `https://lists.apache.org/api/preferences.lua`.

An empty search means nothing matched, not that nothing was said. Say
which list and timespan were searched.

## Health metrics (`apache-health`)

`get_window_metrics(podling, window)` with windows `3m`,
`6m`, `12m`, `to-date`. Metrics and the items they inform:

| Metric | Items |
| --- | --- |
| `new_contributors`, `unique_authors` | CO20, CO40 (new_contributors read 0 for GraphAr while four reports named new contributors; quote both) |
| `unique_committers`, `unique_reviewers`, `bus50`, `bus75`, `pr_author_div_eff`, `reviewer_div_eff` | CO60, IN10 |
| `issues_opened`, `issues_closed`, `median_merge_days`, `median_gap_days` | QU50 |
| `dev_messages`, `dev_unique_posters`, `commits` | CS20 |
| `releases` | RE10, RE50 |

`compare_windows(podling, ["3m","12m"])` shows direction. Report the window
with each number, and the report's `generated_on` date: the health reports
are regenerated periodically and can be a couple of months old.

Known disagreements with other sources, seen across six podlings. Quote
the metric and the other source side by side, never the metric alone:

- `new_contributors` read 0 for GraphAr and Amoro while four consecutive
  reports named new contributors with merged PRs.
- `dev_messages` (48 for Amoro) was lower than the raw count of [VOTE]
  plus [DISCUSS] hits on dev@ over the same year.
- `unique_committers` (25 for Hamilton) exceeded the 10-person roster.
- `releases` counted 1 for Toree in a window with no completed release
  (an rc tag, most likely).
- `issues_opened` and `issues_closed` read GitHub Issues only. Toree uses
  JIRA: `https://issues.apache.org/jira/rest/api/2/search?jql=project=<KEY>...`
  answers anonymously and gives the QU50 counts.

## Incubator reports (`incubator-reports`, `ipmc`)

`incubator-reports:get_podling_reports(podling)` gives the
quarterly reports (the cache held one Hamilton report twice under one id,
so count distinct periods); new committers and PPMC members (CO40), mentor
comments and off-list concerns (CS50), self-assessed maturity boxes. The
graduation-self-assessment skill reads the same reports for graduation;
run it alongside this one when the question is graduation.

`ipmc:graduation_readiness(podling, include_evidence=true)` is a metric
score. Quote its dimension scores as proxies where they map to an item
(release_maturity to RE items, community dimensions to CO items). Never
quote its verdict: it rated OpenServerless "near_ready" with strong
community scores while the podling had never released and coordinated on
WhatsApp, and Seata "ready, high confidence" with its mail source
unavailable. Its output, `get_podling_reports` (76 KB for Pegasus) and
`trademark_list` (98 KB) can exceed the tool output limit and be saved to
a file; use jq or grep on the file rather than re-reading.

## Releases

`ipmc:release_artifact_evidence` and `incubator-releases:podling_releases`
list downloads.apache.org and archive.apache.org together, down to
`<version>/<subproject>/` trees (Toree keeps `toree/` and `toree-pip/`
under each version), and answer in 3 to 9 seconds. Use them first. Each
source in `source_statuses` (under `release_source` in the ipmc output)
carries an `error` when a directory could not be read; only then list
that source by hand. archive.apache.org can be
slow and sometimes returns an empty body on the first try, so use
`--max-time 300`, print the HTTP code, and retry once:

```bash
B=https://downloads.apache.org/incubator/<slug>
curl -s --max-time 300 -w '
%{http_code}
' $B/ | grep -oE 'href="[0-9][^"]*/"|^[0-9]{3}$' | sed -E 's/href="//; s/"//'
curl -s --max-time 300 $B/<version>/ | grep -oE 'href="[^"?/][^"]*"' | sed -E 's/href="//; s/"//'
curl -s -o /dev/null -w '%{http_code}
' $B/KEYS
```

Registries, all fast and anonymous: Maven Central
`https://search.maven.org/solrsearch/select?q=g:org.apache.<slug>&rows=20&wt=json`;
PyPI `https://pypi.org/pypi/<name>/json` (author and project_urls say who
publishes, uploads are not attributed); Docker Hub
`https://hub.docker.com/v2/repositories/apache/<slug>/` and also
`apache/incubator-<slug>/` (Cloudberry publishes under the latter); crates.io
`https://crates.io/api/v1/crates/<name>` (send a User-Agent). Also look for
packages under the project's name published by the originating company
(GraphAr found pygraphar by the GraphScope team).

For LICENSE, NOTICE, DISCLAIMER, headers and sidecars, download the
release from downloads.apache.org into a fresh scratchpad directory
(`check_rc.py --url` against the archive timed out) and run the
podling-release-check skill's script:
`scripts/check_rc.py --rc-dir <dir> --keys <KEYS> --disclaimer-template
<path> --wip-template <path> --out <dir>`. Without the templates it will not
compare disclaimer text. It verifies signatures only when gpg is
installed. Note any expired key in KEYS (Hamilton's only key had expired);
`gpg --show-keys KEYS` prints an expiry only for keys that have one, so
"no expired key" needs the count of keys with no expiry alongside it.

For a podling older than three years, `lte=36M` misses earlier releases:
Pegasus needed `lte=80M` on general@ to recover all five RESULT emails.
Match the window to the incubation length for RE20 and RE50.

Release directory names are not consistent even within one podling
(seata-go has `2.0.0/` and `v2.1.0/`); list the parent, never guess.

When a release directory has no matching [RESULT], search general@ for
"<podling> <version>" and read the hits: XTable's 0.1.0 had a cancelled
IPMC vote and a "release without IPMC vote" thread that the vote-history
tool never surfaced.

## Website content

When a live page returns 404 or an empty shell, read the page source from
the website repository (`apache/<slug>-website` or `-site`) with `gh api
.../contents/...`; Seata's English release, committer, team and security
pages are "Placeholder. DO NOT DELETE." files while the text sits under
`i18n/zh-cn/`. Say which language the content exists in. Versioned docs
sites move paths (`/docs/v1.2.0/...`), so take links from the page rather
than guessing.

## Scratchpad hygiene

Use one fresh directory per podling and per download, named with the
podling and date (`<slug>-<version>-<yyyymmdd>`); a shared scratchpad with
stale `keys` and `wiki` entries from another run broke a mkdir chain and
dropped a download into the root in the OpenServerless run.

## Branding (`asf-trademark`, `ipmc`)

`asf-trademark:check_project_website(url, stage="podling", project_name)` for CO10, QU30 (Security link), TB10, TB20. Pass
`project_name` with the project's own capitalisation (GraphAr, not
Graphar). `ipmc:trademark_branding_check` wraps the same checks but
returns SKIP when the ipmc server was installed without its trademark
dependency (`pip install -e ~/TrademarkMCP` into the Python that runs
the ipmc server fixes that); use the standalone server first.

Two of its rules need a second look before recording: the "(Incubating)"
check flagged Amoro although the page text uses "(incubating)" in lower
case elsewhere, so confirm by reading the heading yourself; and the
Privacy navigation rule flags a site that links its own privacy page
rather than privacy.apache.org (Toree), which is a different finding. `asf-trademark:get_branding_checklist(stage)` lists what
it checks. For TB30 use the status page's name-check date and the reports'
PODLINGNAMESEARCH reference; `asf-trademark:validate_name` is for new
names and reports an existing podling as a conflict with itself.
`asf-trademark:check_third_party_use(url, mark)` for a named page under
TB40. The PODLINGNAMESEARCH JIRA ticket is not reachable from here.

## Policy (`asf-policy`)

Read, do not quote from memory: `resolved_licenses` (LC20), `voting`
(CS30, CS40), `project_independence` (IN10), `branding` (TB items),
`trademark_list` (TB30), `security_committers` (QU30), `release_policy`
(RE items). The maturity model page itself is not in the policy server;
fetch https://community.apache.org/apache-way/apache-project-maturity-model.html
and compare its version line with `references/items.md`.

## Incubation proposal (`cwiki`)

`cwiki:cwiki_search_pages(query="<Name>Proposal")` with the default
full-text search finds the proposal page; titles vary ("GraphArProposal",
"XTable Proposal", "KIE Proposal") and `title_only=true` matches whole
tokens only, so it returned nothing for Texera, OpenServerless, Cloudberry
and Pegasus whose titles are one token. Then `cwiki_get_page(title=...)`.
The proposal can be 50 KB and get spilled to a file; grep it.
Podlings from before 2016 have no cwiki proposal (Toree's lived on the old
MoinMoin wiki, now gone); the text survives in the general@ [DISCUSS]
thread. The proposal gives: initial committers with affiliations (IN10), the
dependency list at donation (LC20), the "Reliance on Salaried Developers"
and "Homogenous Developers" answers. Pass `title`; `page_id` must be a
string and the search result returns it as a number.

## GitHub wiki

Meeting notes may live in the repository wiki. The web page hides dates;
clone it instead:
`git clone --depth 50 https://github.com/apache/<repo>.wiki.git` into the
scratchpad, then `git log --format='%ad %s' --date=short`. The GraphAr run
found the "meetings no longer held" note this way while the website still
advertised a weekly meeting. A wiki with no pages, or a disabled wiki,
clones as "Repository not found" even when `has_wiki` is true; say so and
move on. Minutes may instead be in GitHub Discussions, sometimes on a
different repository (KIE kept them on incubator-kie-issues); the GraphQL
`discussions` query lists them.

## Example self-assessments

Linked from the model page. Useful for the shape of the output, not as
answers:

- OpenDAL (2024): https://opendal.apache.org/community/maturity
- ServiceComb (2018): https://cwiki.apache.org/confluence/display/SERVICECOMB/Apache+Maturity+Model+Assessment+for+ServiceComb
- CarbonData (2017): https://cwiki.apache.org/confluence/display/CARBONDATA/Apache+Maturity+Model+Assessment+for+CarbonData
- Taverna (2016): https://cwiki.apache.org/confluence/display/TAVERNADEV/2016-03+Taverna+Graduation+Maturity+Assessment
- Groovy (2015): https://github.com/apache/groovy/blob/576b3c5d6a7022ac4a8df1ef118666456ce627fb/MATURITY.adoc
