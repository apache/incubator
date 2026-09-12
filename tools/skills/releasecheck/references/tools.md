# Tool notes

Prefixes vary between setups (`incubator-mail:`, `IPMC MCP:`, `ipmc:`); match
on the tool name.

## When a server is not installed

None of them is required. Every server here wraps a public endpoint, so a
missing one costs convenience, not coverage: fetch the source directly, say
in the report which server was unavailable and what you used instead, and
carry on. Do not skip the step. All of these were checked and answer:

| Missing | Fetch instead |
| --- | --- |
| `asf-policy` | `incubator.apache.org/policy/incubation.html`, `apache.org/legal/release-policy.html`, `apache.org/legal/resolved.html`, `apache.org/legal/src-headers.html`, `infra.apache.org/release-distribution.html` |
| `incubator-mail` | The Pony Mail API. `lists.apache.org/api/stats.lua?list=general&domain=incubator.apache.org&q=<terms>&d=lte=12M&emailsOnly=true` to search, `lists.apache.org/api/email.lua?id=<id>` for one message. |
| `incubator-releases` | `dist.apache.org/repos/dist/dev/incubator/<podling>/` for the RC, `archive.apache.org/dist/incubator/<podling>/` for earlier releases. |
| `podlings` | `incubator.apache.org/podlings.xml` (redirects to svn.apache.org). |
| `ipmc` | The registries themselves: search.maven.org, `pypi.org/pypi/<name>/json`, `registry.npmjs.org/<name>`, crates.io, Docker Hub. Worth doing anyway, since this server times out on podlings with many releases. |
| `apache-projects-mcp` | `whimsy.apache.org/public/public_ldap_projects.json`. Under `projects.incubator`, `owners` is the IPMC (about 300 people) and is the list that decides binding votes; `members` is every podling committer and is not. |

`scripts/check_rc.py` uses none of them, so step 4 is unaffected either way.

## Policy MCP (`asf-policy`)

- Pages are cached for up to 30 days. After a policy change, call
  `refresh_cache(keys=[...])` first.
- Link to the policy's own URL as the primary source, not the MCP.
- The LICENSE and NOTICE assembly guide is the `licensing_howto` key.

## Mail MCP (`incubator-mail`)

- `podling_release_vote_history` returns one row per message, not per
  thread. Use the subjects to find each RC's thread.
- `summarize_release_vote_thread` resolves binding status against the IPMC
  roster; that was corrected and its `binding` flags can be relied on. Two
  things still need care. It returns one row per message, not per voter, so
  someone who votes and then joins the discussion appears several times, and
  the opening [VOTE] call itself appears as a row. A message with no vote in
  it is reported as a 0. So take each person's latest actual vote rather than
  adding the rows up, which is what step 8 says to do anyway.
- `search_incubator_general_mail` ignores quotation marks. Narrow with
  `timespan`.
- An empty search means nothing matched, not that nothing was said. Check
  the dev list too: `search_podling_mail(podling, list_name="dev")`.

## Release MCP (`incubator-releases`)

- For an RC, pass `dist_base="https://dist.apache.org/repos/dist/dev/incubator"`.
  The tool appends the slug itself. Don't also pass `archive_base`.
- It lists files but doesn't download, verify or open them. That's the
  script's job.
- One call returns both the dist/dev listing and the archive.apache.org
  history, so a second call isn't needed.
- The response is large. Summarise it.

## IPMC MCP (`ipmc`)

- `release_artifact_evidence(podling, include_platforms=true)`. Pass
  `maven_group_ids` or `pypi_packages` when the podling doesn't use the
  default names.
- It times out on podlings with many releases (Seata, Fesod and XTable all
  did). Don't retry more than once; ask the registries directly instead:
  `https://search.maven.org/solrsearch/select?q=g:<groupId>&rows=50&wt=json`,
  `https://crates.io/api/v1/crates/<name>` (send a User-Agent),
  `https://hub.docker.com/v2/repositories/<ns>/<repo>/tags?page_size=10`,
  `https://api.github.com/repos/apache/<repo>/releases?per_page=5`.
  Compare the publication timestamps with the vote and result dates.

## dist.apache.org

- The dist repository is Subversion. `svn log -v <dist/dev url>` shows
  when each RC directory was added, replaced or deleted, and the commit
  messages often say why. `svn export <url>@<rev>` recovers an RC that has
  been removed or overwritten since the vote.
- For an RC that passed, don't do that. A passing release is copied from
  dist/dev to dist/release, so the voted bytes are served over plain HTTP at
  `https://archive.apache.org/dist/incubator/<podling>/<version>/`. Download
  from there: it is far faster than an svn export and needs no revision
  archaeology. Don't assume the released file has the RC's name: an `-rcN` in
  the name may be stripped on release or kept, and both happen. List the
  archive directory rather than guessing the name. Keep the svn route for RCs
  that were cancelled or voted down, which never reach the archive.
- KEYS moves when a podling graduates. `downloads.apache.org/incubator/
  <podling>/KEYS` starts returning 404 and the file is then at
  `downloads.apache.org/<podling>/KEYS`, with the copy that was live during
  the vote left at `archive.apache.org/dist/incubator/<podling>/KEYS`. The
  script tries all of these, so a 404 on the URL in the vote email is not by
  itself evidence that voters could not check the signatures.

## Apache projects MCP (`apache-projects-mcp`)

- `get_committee("incubator")` returns the IPMC roster with names and Apache
  IDs; these are the binding voters. `get_project_people(<slug>)` returns a
  podling's PPMC, for counting the dev@ vote only.
- Mail archives show personal addresses truncated, so match voters by name
  as well as Apache ID. The full address is in `from_raw` from
  `get_incubator_general_email`.

## Wiki (`cwiki`)

- "Incubator Release Checklist" is what many IPMC reviewers use. It isn't
  policy.
