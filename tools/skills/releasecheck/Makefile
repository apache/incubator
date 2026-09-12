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
INSTALL  := $(HOME)/.claude/skills

PYTHON   ?= python3
OUT      ?= output
TAGDIR   ?=

.DEFAULT_GOAL := help
.PHONY: help test build install check clean

help:
	@echo "make test      run the regression test (44 planted faults, 20 unit checks)"
	@echo "make build     test, then package to $(DIST)/$(SKILL).skill"
	@echo "make install   build, then unpack into $(INSTALL)/"
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
	@mkdir -p $(INSTALL)
	@rm -rf $(INSTALL)/$(SKILL)
	@unzip -q $(PACKAGE) -d $(INSTALL)
	@echo "installed to $(INSTALL)/$(SKILL)"

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
