# Apache Incubator IPMC Skills

Claude skills for the recurring jobs an IPMC member or the VP Incubator does:
the monthly report review, release vote review, graduation and retirement,
the quarterly board report, branding sweeps, podling onboarding and name
clearance.

Each skill is a directory holding a `SKILL.md` — YAML frontmatter naming the
skill and describing when it applies, followed by the workflow an agent
follows — plus any supporting files it needs:

```
<skill-name>/SKILL.md                    the skill
<skill-name>/scripts/…                   helper scripts it runs
<skill-name>/templates/…                 email and document templates it fills in
<skill-name>/references/…                long reference material it reads on demand
<skill-name>/.claude-plugin/plugin.json  its plugin manifest (see Installing)
package-skills.py                        builds installable .skill packages
evals/<skill-name>/                      golden-scenario tests
draft/                                   not yet published
```

Everything here is source. The installable `.skill` packages are build output
and are not committed — see Building.

## The skills

| Skill | What it does |
|---|---|
| `monthly-report-review/` | The monthly IPMC report review: pull the cohort due this month, flag who hasn't filed, cross-check narratives against health data and cross-source mismatches, draft shepherd comments per podling. |
| `release-vote-reviewer/` | Given a release vote thread on general@, walk the full check — artifacts, GPG signatures, checksums, DISCLAIMER, "incubating" in filenames, vote maths — and draft the +1 or the -1 with reasons. |
| `graduation-packet-builder/` | Assemble a podling's graduation case: maturity evidence, name search status, community and release history; draft the DISCUSS email and the board resolution. |
| `graduation-self-assessment/` | Compare the `ipmc` MCP's graduation readiness verdict with what the podling says in its own reports (unfinished issues, maturity boxes, mentor and IPMC notes), check each claim against the mail archives, and give a combined view. Unlike the others it calls the MCP servers as tools. |
| `maturity-model-assessment/` | Build an evidence pack against the 38 items of the Apache Project Maturity Model: gather what the MCP servers, GitHub and the list archives show for each item, mark it evidenced, proxy or human, and write the question the PPMC still has to answer. Never a score or verdict. Calls the MCP servers as tools. |
| `retirement-shepherd/` | The counterpart to graduation: assess whether a stalled podling should retire, gather the evidence, draft the retirement discussion and announcement emails, and the shutdown checklist. |
| `board-report/` | Draft the VP Incubator's quarterly report to the ASF board: podling statistics, graduations and retirements, cohort summary, items requiring board attention. |
| `branding-sweep/` | Batch trademark and branding compliance check across all current podlings; produces a ranked fix list. Suited to a periodic run. |
| `podling-onboarding/` | New-podling onboarding: proposal review against the checklist, then bootstrap tracking — SGA, ICLAs, infra setup, first report date. Runs in five phases, one reference file each. |
| `podling-name-clearance/` | Run the PODLINGNAMESEARCH process end to end for a proposed podling name and produce the writeup in the required format. |

## Data sources

These skills do not call MCP servers over a transport; they run the server
repositories' Python directly, which means the relevant repos must be checked
out locally. The skills reference them by these default paths, and each skill
names the ones it needs:

| Referenced as | Provides |
|---|---|
| `~/ReportMCP` | Incubator report cache, report due dates |
| `~/IncubatorMCP` | IPMC oversight: watchlist, cross-source mismatches, narrative signals |
| `~/HealthMCP` | Per-podling health metrics |
| `~/PodlingsMCP` | Podling roster, status, statistics, reporting schedule |
| `~/TrademarkMCP` | Name validation and trademark search |
| `~/MailMCP` | general@ and podling mailing list archives |
| `~/PolicyMCP` | ASF policy documents |
| `~/ReleaseMCP` | Podling release history |
| `~/CwikiMCP` | Confluence wiki pages |

If your checkouts live elsewhere, adjust the paths in that skill's markdown.
Paths are written with `~`, which Python does not expand on its own — use
`os.path.expanduser()`.

## Installing

Every skill is also a plugin in the Incubator's marketplace, so it installs
and updates like any other plugin. The repository carries the catalog each
agent reads, all listing the same plugins:

| Agent | Add the marketplace, then install a skill | Catalog |
|---|---|---|
| Claude Code | `/plugin marketplace add apache/incubator`, then `/plugin install graduation-self-assessment@apache-incubator` | `.claude-plugin/marketplace.json` |
| OpenAI Codex CLI | `codex plugin marketplace add apache/incubator`, then install the plugin | `.agents/plugins/marketplace.json` |
| VS Code / GitHub Copilot | add `apache/incubator` as a plugin marketplace | `marketplace.json` |
| Kiro | install from the skill's GitHub subdirectory, e.g. `https://github.com/apache/incubator/tree/<tag>/tools/skills/graduation-self-assessment` | none; reads `SKILL.md` |

Updating is the agent's own plugin update (`/plugin update` in Claude Code).
Keep the three catalogs listing the same plugins when adding one.

Projects that use [Apache Magpie](https://github.com/apache/magpie) can pull
the same skills through Magpie instead, for any agent: the ASF organization
curates this repository as a skill source, pinned per skill to the tags
below, and Magpie wires the pinned skills into every agent's skills directory.

## Releasing a skill

Skills are versioned independently. To release one, bump `version` in its
`.claude-plugin/plugin.json` and tag the commit `<skill-name>-<version>`
(for example `releasecheck-0.5.1`). Tags are what downstream pins point at,
so never move one once it is pushed; release a new version instead.

## Building

`package-skills.py` compiles each skill into the `.skill` zip format the
Claude apps install. It validates the frontmatter first (`name` and
`description` are required), folds in the skill directory's `scripts/`, `templates/`
and `references/`, and omits `__pycache__` and `.DS_Store`.

```bash
python3 package-skills.py --all                  # every skill here → dist/
python3 package-skills.py release-vote-reviewer  # or just one
python3 package-skills.py --all /path/to/sources # sources kept elsewhere
```

Exit status is the number of skills that failed to compile. `dist/` is build
output and is gitignored.

To install a built package, open the `.skill` file in the Claude app, or
unpack it: `unzip dist/<skill-name>.skill -d ~/.claude/skills/`.

## Testing

`evals/` holds golden-scenario fixture pairs for the four judgment-heavy
skills — report review, release vote, graduation, retirement. Each pair is a
positive case that should be approved and a negative case that should be
flagged; every fixture is self-contained, so the evals make no live calls.

`evals/run-evals.sh` runs each case as a real `claude -p` invocation with a
realistic user prompt, so it tests skill triggering as well as judgment; the
exit status is the number of failed cases. It needs the `claude` CLI on PATH
and the skills installed so the CLI can find them — build and unpack them
first (see Building). Each case is a full agent run, so a complete pass costs
real tokens and takes a while.

The other four skills have no eval pairs: their output is checked by format
rather than judgment, so a wrong answer looks obviously wrong.
