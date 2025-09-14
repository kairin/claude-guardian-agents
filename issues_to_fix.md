# Issues to Fix - Generated Analysis

**Analysis Summary**: Project has 23,915 files across 1,150 directories when original requirements were simply Ubuntu 25.04 compatibility, Python 3.13+, UV package management, better file organization, and working commits. This represents massive scope creep and over-engineering.

## Critical (Blocking Issues)

### Hook Loop Potential
- [ ] Remove duplicate Makefile targets in `/home/kkk/Apps/claude-guardian-agents/Makefile` lines 32-35 and 92-96 (identical install/dev-install targets)
- [ ] Remove duplicate development targets in `/home/kkk/Apps/claude-guardian-agents/Makefile` lines 39-48 and 99-108 (test/lint/format targets)
- [ ] Simplify pre-commit config in `/home/kkk/Apps/claude-guardian-agents/.pre-commit-config.yaml` to only essential hooks (keep trailing-whitespace, end-of-file-fixer, check-yaml, black, ruff)
- [ ] Remove GPM validation hook from pre-commit config line 67-72 that could trigger on every commit

### Configuration Conflicts
- [ ] Fix Python version inconsistency: pyproject.toml line 82 targets py38-py312 but line 100 targets py312, should be py313 only
- [ ] Remove mypy Python version override in pyproject.toml line 135 (conflicts with project Python 3.13 requirement)

## High Priority (Complexity Issues)

### Massive Agent Library (Not Requested)
- [ ] Delete entire `/home/kkk/Apps/claude-guardian-agents/1-product/` directory (4 subdirectories, ~50+ agent files)
- [ ] Delete entire `/home/kkk/Apps/claude-guardian-agents/2-engineering/` directory (6 subdirectories, agent files)
- [ ] Delete entire `/home/kkk/Apps/claude-guardian-agents/3-operations/` directory (7 subdirectories, agent files)
- [ ] Delete entire `/home/kkk/Apps/claude-guardian-agents/4-thinktank/` directory (6 subdirectories, agent files)
- [ ] Delete entire `/home/kkk/Apps/claude-guardian-agents/assets/` directory (14,322 SVG files)

### Complex Scripts Beyond Requirements
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/generate-custom-svgs.py` (34KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/add-svg-animations.py` (10KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/reorganize-svgs.py` (11KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/generate-reports.py` (18KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/track-progress.py` (14KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/gpm-lib.py` (20KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/phase4-update.sh` (12KB, not requested)

### Over-Engineered Dependencies
- [ ] Remove docs dependencies from pyproject.toml lines 50-54 (mkdocs, mkdocs-material, mkdocs-mermaid2-plugin)
- [ ] Remove validation dependencies from pyproject.toml lines 55-65 (jsonschema, openapi-spec-validator, yamllint, frontmatter, bandit)
- [ ] Remove project scripts from pyproject.toml lines 73-76 (guardian-track, guardian-reports, guardian-validate)

### Complex Documentation
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/docs/` directory entirely (10 subdirectories)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/specs/` directory entirely (5 subdirectories with complex specifications)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/templates/` directory (6 template files not requested)

## Medium Priority (Unrequested Features)

### Project Tracking/Management System
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/tracking/` directory entirely
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/manifest.json` (38KB auto-generated file)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/CHANGELOG.md` (12KB, not requested)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/AGENTS.md` (4KB, not requested)

### Unnecessary Automation
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/batch-update-phase3.sh`
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/phase4-specialized.sh`
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/create-new-feature.sh`
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/update-agent-context.sh`
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/scripts/validate-gpm.sh`

### Claude Integration Files
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/.claude/` directory entirely (4 subdirectories with agent definitions)
- [ ] Keep only CLAUDE.md in root (required for Claude Code integration)

## Low Priority (Cleanup)

### Test Infrastructure
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/test-projects/` directory (4 subdirectories for testing)
- [ ] Remove test coverage requirements from pyproject.toml lines 158-160 (cov-fail-under=80)
- [ ] Simplify pytest configuration in pyproject.toml lines 150-160 to basic test running

### Memory/Cache Cleanup
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/memory/` directory
- [ ] Remove bandit configuration from pyproject.toml lines 148-150
- [ ] Remove coverage configuration from pyproject.toml lines 162-183

### Environment Scripts
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/activate-env.sh` (use `uv venv` directly)
- [ ] Delete `/home/kkk/Apps/claude-guardian-agents/install.sh` (use `uv pip install -e .` directly)

---

**Expected Result**: Project should shrink from 23,915 files to ~50-100 files focused solely on:
- Basic Python 3.13 + UV package management
- Simple file organization
- Working git commits
- Ubuntu 25.04 compatibility

**Files to Keep**:
- `pyproject.toml` (simplified)
- `README.md` (simplified)
- `CLAUDE.md`
- `.gitignore`
- `.python-version`
- `uv.lock`
- Basic source code in `src/` directory
- Essential scripts for UV/Python setup only
