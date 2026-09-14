# Build, test and install the releasecheck skill.
#
# The packager lives one level up and writes to tools/skills/dist/, so this
# only drives it. `output/` is the default working directory for a real run:
# package-skills.py already excludes a skill's root-level output/ from the
# .skill file, so a stale one can never ship.

SKILL    := releasecheck
SKILLS   := $(abspath $(CURDIR)/..)
PACKAGER := $(SKILLS)/package-skills.py
DIST     := $(SKILLS)/dist
PACKAGE  := $(DIST)/$(SKILL).skill

# make install puts the skill into each client that is present. OpenCode also
# reads ~/.claude/skills, so it only gets its own copy when there is no
# ~/.claude; two copies just produce "duplicate skill name" warnings.
CLAUDE_HOME     ?= $(HOME)/.claude
CLAUDE_SKILLS   ?= $(CLAUDE_HOME)/skills
CODEX_HOME      ?= $(HOME)/.codex
CODEX_SKILLS    ?= $(CODEX_HOME)/skills
XDG_CONFIG_HOME ?= $(HOME)/.config
OPENCODE_HOME   ?= $(XDG_CONFIG_HOME)/opencode
OPENCODE_SKILLS ?= $(OPENCODE_HOME)/skills
OPENCODE        ?= $(shell command -v opencode)

PYTHON   ?= python3
OUT      ?= output
TAGDIR   ?=
MCP_ARGS ?=

.DEFAULT_GOAL := help
.PHONY: help test build install mcp check clean

help:
	@echo "make test      run the regression test (44 planted faults, 20 unit checks)"
	@echo "make build     test, then package to $(DIST)/$(SKILL).skill"
	@echo "make install   build, then unpack into the skills directory of each client present:"
	@echo "               Claude Code, Codex, and OpenCode when there is no ~/.claude"
	@echo "make mcp       install the six MCP servers and register them with Claude Code,"
	@echo "               asking first: make mcp [MCP_ARGS=\"--desktop --codex --opencode\"]"
	@echo "make check     run the checker on a real RC:"
	@echo "               make check URL=<dist/dev RC dir> PODLING=<slug> [TAGDIR=<checkout>] [OUT=dir]"
	@echo "make clean     remove $(OUT)/, __pycache__ and the built package"

test:
	@$(PYTHON) scripts/test_check_rc.py

# Tests gate the package: never ship something that has not passed.
build: test
	@test -f $(PACKAGER) || { \
	  echo "no packager at $(PACKAGER)"; \
	  echo "build runs from the skill's place in the tools/skills tree, not from an installed copy"; \
	  exit 2; }
	@$(PYTHON) $(PACKAGER) $(CURDIR)

install: build
	@installed=; \
	put() { mkdir -p "$$1" && rm -rf "$$1/$(SKILL)" && unzip -q $(PACKAGE) -d "$$1" || exit 1; \
	        echo "installed to $$1/$(SKILL)"; installed=1; }; \
	if [ -d "$(CLAUDE_HOME)" ]; then put "$(CLAUDE_SKILLS)"; fi; \
	if [ -d "$(CODEX_HOME)" ]; then put "$(CODEX_SKILLS)"; fi; \
	if [ ! -d "$(CLAUDE_HOME)" ] && { [ -d "$(OPENCODE_HOME)" ] || [ -n "$(OPENCODE)" ]; }; then \
	  put "$(OPENCODE_SKILLS)"; fi; \
	if [ -z "$$installed" ]; then \
	  echo "no Claude Code, Codex or OpenCode found; using the Claude Code location"; \
	  put "$(CLAUDE_SKILLS)"; fi

# Separate from install: the skill works without the servers, and this clones
# and pip-installs from GitHub and asks before touching any client config.
mcp:
	@$(PYTHON) scripts/setup_mcps.py $(MCP_ARGS)

check:
	@test -n "$(URL)$(RCDIR)" || { \
	  echo "usage: make check URL=<dist/dev RC dir> PODLING=<slug> [TAGDIR=<checkout>]"; \
	  echo "   or: make check RCDIR=<downloaded artifacts> PODLING=<slug>"; exit 2; }
	@$(PYTHON) scripts/check_rc.py \
	  $(if $(URL),--url "$(URL)") $(if $(RCDIR),--rc-dir "$(RCDIR)") \
	  $(if $(PODLING),--podling "$(PODLING)") $(if $(TAGDIR),--tag-dir "$(TAGDIR)") \
	  --disclaimer-template references/disclaimer-standard.txt \
	  --wip-template references/disclaimer-wip.txt \
	  --out "$(OUT)" || true
	@echo; echo "read $(OUT)/findings.md"

clean:
	@rm -rf $(OUT) scripts/__pycache__ .pytest_cache $(PACKAGE)
	@echo "cleaned"
