PYTHON ?= python3
SKILL_NAME ?= incubator-concierge
BUILD_DIR ?= build
STAGE_DIR := $(BUILD_DIR)/$(SKILL_NAME)
ARTIFACT := $(BUILD_DIR)/$(SKILL_NAME).skill

.PHONY: help validate package clean evals-self-test evals-content evals evals-trigger evals-all check

help:
	@echo "Build:"
	@echo "  validate         Frontmatter, description length, references, excluded sources"
	@echo "  package          Validate, then build $(ARTIFACT)"
	@echo "  clean            Remove $(BUILD_DIR) and eval results"
	@echo "Evals (no model, free):"
	@echo "  evals-self-test  Prove the eval grader itself works"
	@echo "  evals-content    Static regression assertions over the skill files"
	@echo "  check            validate + evals-self-test + evals-content"
	@echo "Evals (need claude on PATH):"
	@echo "  evals            Behaviour suite: routing, traps, register"
	@echo "  evals-trigger    Triggering suite: fires on real phrasings, quiet on near-misses"
	@echo "  evals-all        Every suite"

validate:
	$(PYTHON) scripts/validate_skill.py .

package: validate
	rm -rf $(STAGE_DIR) $(ARTIFACT)
	mkdir -p $(STAGE_DIR)/references
	cp SKILL.md $(STAGE_DIR)/
	cp references/*.md $(STAGE_DIR)/references/
	cd $(BUILD_DIR) && zip -q -r $(SKILL_NAME).skill $(SKILL_NAME) -x '*.DS_Store'
	rm -rf $(STAGE_DIR)
	@echo "Built $(ARTIFACT)"
	@unzip -l $(ARTIFACT)

evals-self-test:
	$(PYTHON) scripts/self_test_evals.py

evals-content:
	$(PYTHON) scripts/run_evals.py --suite content

evals:
	$(PYTHON) scripts/run_evals.py --suite behaviour

evals-trigger:
	$(PYTHON) scripts/run_evals.py --suite triggering

evals-all:
	$(PYTHON) scripts/run_evals.py --suite all

check: validate evals-self-test evals-content

clean:
	rm -rf $(BUILD_DIR) evals/results
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
