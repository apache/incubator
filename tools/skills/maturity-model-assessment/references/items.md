# Apache Project Maturity Model, item by item

Source: https://community.apache.org/apache-way/apache-project-maturity-model.html
Version 1.4, December 2024 (added TB10 to TB40). Check the page's version
history each run; if it has moved past 1.4, re-read the page and update this
file before assessing.

The model's own framing, which the report must keep:

- "This model is a guide; it is not a requirements document."
- "Contrary to other maturity models, we do not define staged partial
  compliance levels. A mature Apache project complies with all the elements
  of this model."
- "Note that we try to avoid using the word 'must' below. The model
  describes the state of a mature project, as opposed to a set of rules."
- "Projects which incubate at the ASF might not fit into all the parts of
  this model; however a major goal of incubation is to bring the project's
  community closer to it."

Each entry below gives the item text verbatim, its footnote where there is
one, how far tools can take it, and the question a person still has to
answer. The three states are:

- **Evidenced**: a tool returns a fact that settles the item either way.
- **Proxy**: tools return a signal that supports or weakens the claim. Show
  the signal; a person decides.
- **Human**: no tool output bears on it. Ask the question and leave the
  cell blank.

Tool names are `server:tool`. `references/tools.md` has the fallbacks.

---

## Code

### CD10 (Evidenced)
> The project produces Open Source software for distribution to the public, at no charge.

Footnote 1: "For distribution to the public at no charge" is straight from
the ASF Bylaws at https://apache.org/foundation/bylaws.html

Evidence: repository is public (`apache-projects-mcp:get_repositories`,
`gh api repos/apache/<repo>` shows `private: false`); LICENSE at repo root
is Apache 2.0; releases on dist or archive.apache.org
(archive.apache.org listing or `incubator-releases:podling_releases`).

### CD20 (Evidenced)
> Anyone can easily discover and access the project's code.

Evidence: homepage links to the source repository
(`asf-trademark:check_project_website` reports navigation; otherwise fetch
the homepage and look for a github.com/apache or gitbox link). Repository
listed under `gh api orgs/apache/repos` or `get_repositories`.

### CD30 (Proxy)
> Anyone using standard, widely-available tools, can build the code in a reproducible way.

Proxy: build descriptor present at repo root (pom.xml, build.gradle,
Cargo.toml, go.mod, package.json, setup.py or pyproject.toml, CMakeLists,
Makefile); CI workflow under `.github/workflows` that runs a build on
pull requests; a build or development page in the docs. Record the build
tool and whether CI is green on the default branch
(`gh api repos/apache/<repo>/commits/<default>/check-runs`).

Human: Has anyone outside the core team built a release from source by
following the documented steps alone? Does the build pull anything that is
not publicly available (private registries, pre-built binaries from a vendor
site)?

### CD40 (Evidenced)
> The full history of the project's code is available via a source code control system, in a way that allows anyone to recreate any released version.

Evidence: list release versions (archive.apache.org or `podling_releases`) and
list tags (`gh api repos/apache/<repo>/tags --paginate`). Every release
should have a tag or a commit named in its vote thread. Report versions
with no tag. Check the first commit date against the project's claimed start
to see whether pre-ASF history was imported
(`gh api "repos/apache/<repo>/commits?until=<date>&per_page=1"` or
`git log --reverse` on a checkout).

Human only if history is missing: was the pre-donation history deliberately
dropped, and does the project say so?

### CD50 (Proxy)
> The source code control system establishes the provenance of each line of code in a reliable way, based on strong authentication of the committer. When third parties contribute code, commit messages provide reliable information about the code provenance.

Footnote 2: See also LC40.

Evidence for the first sentence: every apache/* repository is written
through ASF-authenticated accounts, so strong authentication of the
committer is given by the hosting. State that and move on.

Proxy for the second sentence: sample the last 30 merged pull requests
(`gh pr list --repo apache/<repo> --state merged --limit 30 --json
number,author,mergedBy,title`). Count how many were authored by someone
other than the merger. For a sample of five of those, read the merge commit
or squash commit (`gh api repos/apache/<repo>/commits/<sha>`) and check it
carries the author's identity (Author field or Co-authored-by trailer), not
just the committer's.

Human: Are there large contributions whose origin is not recorded in the
commit, such as a code drop from a company that arrived as one commit by a
committer? Was IP clearance filed for them (`asf-policy:get_policy
incubator_ip_clearance` describes the record)?

---

## Licenses and Copyright

### LC10 (Evidenced)
> The Apache License, version 2.0, covers the released code.

Evidence: LICENSE in the latest source release is the Apache 2.0 text;
source headers present. The podling-release-check skill's script checks
both. Record the release checked.

### LC20 (Proxy)
> Libraries that are mandatory dependencies of the project's code do not create more restrictions than the Apache License does.

Footnote 3: It's ok for platforms (like a runtime used to execute our code)
to have different licenses as long as they don't impose reciprocal
licensing on what we are distributing.
Footnote 4: https://apache.org/legal/resolved.html has information about
acceptable licenses for third-party dependencies.

Proxy: enumerate direct dependencies from the build descriptor and
classify each licence against `asf-policy:get_policy resolved_licenses`
(Category A, B or X). The magpie-repo-health dependency-license-audit skill
does this where it is installed. Report any Category X and any Category B
dependency, with whether the Category B item is bundled or only linked.

Human: Which Category B dependencies are mandatory at runtime rather than
optional? Are any dependencies loaded dynamically from a non-free source?

### LC30 (Evidenced)
> The libraries mentioned in LC20 are available as Open Source software.

Evidence: comes out of the same dependency enumeration as LC20. A
dependency with no open source licence, or resolved only from a private
repository, fails this. Otherwise record "all direct dependencies
resolve from public registries under OSI-approved licences".

### LC40 (Evidenced)
> Committers are bound by an Individual Contributor Agreement (the "Apache iCLA") that defines which code they may commit and how they need to identify code that is not their own.

Evidence: an ASF account is only created once an ICLA is on file, so every
member of the committer LDAP group (`apache-projects-mcp:get_project_people`
or `get_group_members`) is covered. Record the committer count and the date
checked. Nothing further to check.

### LC50 (Proxy)
> The project clearly defines and documents the copyright ownership of everything that the project produces.

Footnote 5: In Apache projects, the ASF owns the copyright for the
collective work, i.e. the project's releases. Contributors retain copyright
on their contributions but grant the ASF a perpetual copyright license for
them.

Proxy: NOTICE file in the source release names the ASF as copyright holder
for the collective work with a current year range; LICENSE and NOTICE
account for bundled third-party code (podling-release-check covers this
for podlings). For a podling, the Software Grant Agreement for the initial
code drop is recorded in the podling's status page or IP clearance records.

Human: Is there anything the project produces that falls outside the
release and the NOTICE, such as a logo, a website theme or documentation
donated separately? Who owns it?

---

## Releases

### RE10 (Evidenced)
> Releases consist of source code, distributed using standard and open archive formats that are expected to stay readable in the long term.

Footnote 6: See https://www.apache.org/legal/release-policy.html for more
info on Apache releases.

Evidence: a directory listing of `archive.apache.org/dist/incubator/<slug>/`,
with
`incubator-releases:podling_releases` as a convenience when it answers
(`references/tools.md` has the curl form). Every release has a source
archive in .tar.gz or .zip. Report any release with binaries only.

### RE20 (Evidenced)
> The project's PMC (Project Management Committee, see CS10) approves each software release in order to make the release an act of the Foundation.

Evidence: `ipmc:release_vote_evidence(podling)` and
`incubator-mail:podling_release_vote_history(podling, timespan="lte=36M")`
give the [VOTE] and [RESULT] threads on general@; the same tool with
`list_name="dev"` gives the PPMC vote. Match each release in RE10 to a
RESULT with at least three binding +1 votes (IPMC members, from
`apache-projects-mcp:get_committee("incubator")`). Report releases with
no matching vote.

Human: only when a release has no vote thread that can be found.

### RE30 (Evidenced)
> Releases are signed and/or distributed along with digests that anyone can reliably use to validate the downloaded archives.

Evidence: list each release directory on archive.apache.org (or
`podling_releases` when it answers) and check .asc and .sha512 sidecars per
artifact. A KEYS file is present
at the project's dist root. Report any artifact missing either sidecar.

### RE40 (Proxy)
> The project can distribute convenience binaries alongside source code, but they are not Apache Releases, they are provided with no guarantee.

Proxy: fetch the download page (`ipmc:release_artifact_evidence(podling,
release_page_url="auto")` or the project's download page) and quote the
text around the binary links. Look for the source release being presented
first and binaries described as convenience. `release_artifact_evidence`
with `include_platforms=true` lists Maven, PyPI, npm and Docker Hub
publications.

Human: Does the page make clear to a user which artifact is the release?
Are binaries on registries labelled as Apache releases when they are not?

### RE50 (Proxy)
> The project documents a repeatable release process so that someone new to the project can independently generate the complete set of artifacts required for a release.

Proxy: a release guide exists in the repo or site (search for
RELEASE.md, release-process, "how to release", "release manager"). From the
vote threads in RE20, count distinct release managers over the last 36
months. One release manager for every release is a warning sign.

Human: Has anyone who did not write the release guide used it to cut a
release? Does it cover signing, staging, the vote and the announcement?

---

## Quality

### QU10 (Human)
> The project is open and honest about the quality of its code. Various levels of quality and maturity for various modules are natural and acceptable as long as they are clearly communicated.

Weak proxy: README or docs mark modules or features as experimental,
alpha or stable; semantic versioning or an explicit stability policy.

Human: Does the project describe known limitations and unstable areas
where a new user would see them? Do release notes own up to regressions?

### QU20 (Human)
> The project puts a very high priority on producing secure software.

Footnote 7: The required level of security depends on the software's
intended uses, of course. Projects should clearly document security
expectations.

Weak proxy: published CVEs for the project (`cveprocess.apache.org` or
the project's security page) and how long each took from report to
fix where the advisory says; dependency update automation (Dependabot or
Renovate config) in the repo.

Human: Does the project document its security expectations as footnote 7
asks? Did past vulnerabilities get fixed and announced in a way the
Security Team would call prompt?

### QU30 (Evidenced)
> The project provides a well-documented, secure and private channel to report security issues, along with a documented way of responding to them.

Footnote 8: Apache projects can just point to
https://www.apache.org/security/ or use their own security contacts page,
which should also point to that.

Evidence: SECURITY.md in the repo (`gh api
repos/apache/<repo>/contents/SECURITY.md`), a security page on the site,
and a Security link in site navigation (`asf-trademark:check_project_website`
checks the navigation set). The page should point to
security@<project>.apache.org or security@apache.org and to
apache.org/security/. Report which of the three are present.

### QU40 (Proxy)
> The project puts a high priority on backwards compatibility and aims to document any incompatible changes and provide tools and documentation to help users transition to new features.

Proxy: CHANGELOG or release notes exist per release; a compatibility or
versioning policy page; a migration or upgrade guide for the last major
version change. Record which exist.

Human: When the project last broke compatibility, did users get a
deprecation period and a migration path?

### QU50 (Proxy)
> The project strives to respond to documented bug reports in a timely manner.

Proxy: `apache-health:get_window_metrics(podling, "12m")` gives
`issues_opened`, `issues_closed`, `median_merge_days`, `median_gap_days`;
`gh api "repos/apache/<repo>/issues?state=open&sort=created&direction=asc&per_page=20"`
for the oldest open issues and whether they have any comment. Report
open versus closed counts and the share of open issues with no response
after 30 days.

Human: What counts as timely for this project's users? Is the
unanswered backlog made of real bugs or of questions and feature wishes?

---

## Community

### CO10 (Evidenced)
> The project has a well-known homepage that points to all the information required to operate according to this maturity model.

Evidence: `asf-trademark:check_project_website(url, stage="podling",
project_name)` reports the required navigation links. Also confirm the homepage links to: source, downloads, mailing
lists, issue tracker, security, team or PPMC page, and how to contribute.
List the ones missing.

### CO20 (Proxy)
> The community welcomes contributions from anyone who acts in good faith and in a respectful manner, and who adds value to the project.

Proxy: CONTRIBUTING file; issues labelled good first issue or similar;
`apache-health` `new_contributors` and `unique_authors` over 12 months;
share of
merged pull requests from non-committers (from the CD50 sample).

Human: Read the last month of dev list and a handful of first-time
contributor pull requests. Were newcomers answered, and how were they
spoken to?

### CO30 (Human)
> Contributions include source code, documentation, constructive bug reports, constructive discussions, marketing and generally anything that adds value to the project.

No tool evidence. Human: Has anyone been made a committer or PPMC member
mainly for documentation, community, design or evangelism work? Does the
contributor guide describe non-code ways to contribute?

### CO40 (Proxy)
> The community strives to be meritocratic and gives more rights and responsibilities to contributors who, over time, add value to the project.

Proxy: current committer and PPMC rosters
(`apache-projects-mcp:get_project_people`); the initial roster from the
podling status page; new committers and PPMC members per quarter from the
Incubator reports (`incubator-reports:get_podling_reports`). Report
additions in the last 12 and 24 months against the initial roster.

Human: Were recent additions people who had been contributing for a
while, or were they appointed at the start by their employer?

### CO50 (Proxy)
> The project documents how contributors can earn rights such as commit access or decision power, and applies these principles consistently.

Proxy: a page describing how committers and PPMC members are chosen exists
(search the site and repo for "becoming a committer", "committer
guidelines", "new committer").

Human: Do the additions in CO40 match what that page says? Has anyone
with a comparable record been passed over?

### CO60 (Proxy)
> The community operates based on consensus of its members (see CS10) who have decision power. Dictators, benevolent or not, are not welcome in Apache projects.

Proxy: `apache-health` `bus50`, `bus75`, `pr_author_div_eff`,
`reviewer_div_eff`, `unique_committers`, `unique_reviewers` over 12
months; from the CD50 sample, how many distinct people merged. One person merging most pull requests, or a bus50 of 1, is a
signal, not a verdict.

Also read `.asf.yaml` for `required_approving_review_count` and set it
against the self-merge count in the sample: a two-review rule alongside
mostly self-merges is a finding.

Human: Does one person decide contested questions on the list? Are
decisions ever made by announcement rather than discussion?

### CO70 (Human)
> The project strives to answer user questions in a timely manner.

Weak proxy: `incubator-mail:search_podling_mail(podling, list_name="users")`
(or dev where there is no user list): count threads with a single message
in the last 90 days. GitHub Discussions, if enabled, the same way.

Human: Sample ten user questions from the last quarter. How many were
answered, by whom, and how fast?

---

## Consensus Building

### CS10 (Evidenced)
> The project maintains a public list of its contributors who have decision power. The project's PMC (Project Management Committee) consists of those contributors.

Evidence: `apache-projects-mcp:get_project_people(<slug>)` for the PPMC
roster and the podling status page. The project site has a team page that
matches. Report mismatches between the site and LDAP.

### CS20 (Human)
> Decisions require a consensus among PMC members and are documented on the project's main communications channel. The PMC takes community opinions into account, but the PMC has the final word.

Footnote 9: In Apache projects, "consensus" means _widespread agreement
among people who have decision power_. It does not necessarily mean
"unanimity".

Weak proxy: count [DISCUSS] and [VOTE] threads on dev@ in the last 12
months (`incubator-mail:search_podling_mail`) against the number of releases, new committers and significant
changes in the same period. Dev list volume relative to commits
(`dev_messages` versus `commits` in apache-health).

Human: Pick three recent significant changes (a new module, a dropped
feature, a process change). Where was each decided, and is the decision
findable on the list?

### CS30 (Proxy)
> The project uses documented voting rules to build consensus when discussion is not sufficient.

Footnote 10: For Apache projects,
https://www.apache.org/foundation/voting.html defines the voting rules.

Proxy: a project bylaws, governance or voting page exists, or the
contributor guide points to apache.org/foundation/voting.html. The vote
threads found for RE20 follow the [VOTE] and [RESULT] form with a stated
close time.

Human: only if there is no page and votes are informal.

### CS40 (Human)
> In Apache projects, vetoes are only valid for code commits. The person exercising the veto must justify it with a technical explanation, as per the Apache voting rules defined in CS30.

Weak proxy: search dev@ for "veto" and "-1" in the last 24 months. Hits
are rare and need reading in context.

Human: Has a -1 ever been treated as blocking a release or a procedural
vote? Were code vetoes explained technically?

### CS50 (Human)
> All "important" discussions happen asynchronously in written form on the project's main communications channel. Offline, face-to-face or private discussions that affect the project are also documented on that channel.

Footnote 11: Each Apache project has a private mailing list that its PMC
is expected to use only when really needed. The private list is typically
used for discussions about people, for example to discuss and to vote on
PPMC and committer candidates.

Weak proxy: the community page's meeting and chat links and whether the
meeting notes they point to are current (clone the GitHub wiki,
`references/tools.md`); mentions on dev@ or in pull requests of Slack,
Discord, WeChat, DingTalk, meetings or "as discussed offline" without a
summary;
pull requests merged with design discussion only in the PR and never on
the list. Mentor comments in Incubator reports about off-list decisions
(`incubator-reports:get_podling_reports`, the graduation-self-assessment
skill extracts these).

Human: This is the item that most needs someone who reads the list. Do
decisions arrive on the list already made? Are sync meetings minuted to
the list?

---

## Independence

### IN10 (Proxy)
> The project is independent from any corporate or organizational influence.

Footnote 12: Independence can be understood as basing the project's
decisions on the open discussions that happen on the project's main
communications channel, with no hidden agendas.

Proxy: affiliation of PPMC and committers where it is stated: the
proposal (`cwiki:cwiki_get_page(title="<Name>Proposal")`, Initial
Committers and Reliance on Salaried Developers sections), the team page,
Incubator reports. Registry packages published by the originating company
under the project's name are a signal too. Email domains of
contributors in the CD50 sample as a crude signal. No MCP holds
affiliation data; say so. Project independence guidance is
`asf-policy:get_policy project_independence`.

Human: Does one employer hold a majority of the PPMC? Do roadmap
decisions track that employer's product releases? Does the project
website or repo link to a vendor's commercial offering ahead of the
Apache release?

### IN20 (Human)
> Contributors act as themselves, not as representatives of a corporation or organization.

No tool evidence. Human: Do people on the list speak as "we at Company"?
Do votes split along employer lines?

---

## Trademark and Branding

Intro on the page: "Notable items from the Trademark Policy, FAQ, Guide,
and PPMC Branding Responsibilities. The project's PPMC should comply with
ASF's branding and trademark policy in all places it controls."

### TB10 (Evidenced)
> The project uses "Apache Foo™" as the project and software product name consistently, with appropriate trademark attributions.

Footnote 13: See https://apache.org/foundation/marks/pmcs#attributions for
more information on trademark attributions.

Evidence: `asf-trademark:check_project_website(url, stage="podling",
project_name)` reports the Apache-form heading, TM on first use, footer attribution,
logo attribution, bare sibling marks and, for a podling, the incubation
disclaimer and "(Incubating)" suffix. Also spot-check the README and
the download page.

### TB20 (Evidenced for the homepage, Proxy for other domains)
> The project's primary homepage is at `projectname.apache.org`. When exceptions exist to use alternate domains for any purpose, any `non-apache.org` domain names are owned by the ASF.

Evidence: homepage URL from `podlings:get_podling` is on apache.org.

Proxy: any other domains the site or README links to as the project's own
(docs sites, demo sites). `whois` on each; the registrant should be the
ASF. Report domains whose registrant is a company or an individual.

### TB30 (Proxy)
> The ASF has trademark rights, including any registrations, to the project name, logo, and any other major branding elements.

Footnote 14: For example, any transfers of existing trademark
registrations during Incubation must completed before graduation.

Proxy: the podling status page records the name search status;
`asf-policy:get_policy trademark_list` says whether the name is a
registered mark. The PODLINGNAMESEARCH JIRA ticket is the record; it is not reachable through an MCP, so ask for
its key and status. `asf-trademark:validate_name` re-runs the automated
part of the name check.

Human: Did any pre-existing registration (name or logo) get assigned to
the ASF? Is the logo's copyright assigned?

### TB40 (Human)
> The project monitors for any major misuses of their project's brand by others, and reports any potential misuses to Brand Management.

Footnote 15: See also https://apache.org/foundation/marks/reporting.html#pmcs
for more information on reporting misuses. TB40 is a balancing act: we
hope that PMCs are spending some time responding to any obvious or blatant
misuses of their brand. But PMCs sometimes can't handle all the details of
actually stopping a potential infringement; what we really need is for
PMCs to actively report them, and then promptly respond if Brand
Managment (or other officers) ask for information when addressing a
misuse.

Weak proxy: if the PPMC names a third-party page it is unsure about,
`asf-trademark:check_third_party_use(url, mark)` scores it against the
policy. Nothing shows whether the PPMC monitors.

Human: Has the PPMC ever reported a misuse to trademarks@? Who on the PPMC
watches for it?
