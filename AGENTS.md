# LLM Instructions - Guardian Agents Development

> **Consolidated instructions for ALL AI coding agents (Claude, Gemini, etc.) working on Guardian Agents**

## 🎯 Project Overview

Guardian Agents is a production-ready AI agent orchestration system with **52 agents** (49 specialized + 3 meta-agents) across 5 cognitive layers. The 3 meta-agents are specifically designed to prevent code creep and over-engineering at the earliest stages of development. Ubuntu 25.04 + Python 3.13 + UV package manager ONLY.

📖 **[Learn more about the Three-Tier Guardian Agent System](docs/three-tier-guardian-system.md)**

## ⚡ Critical Requirements - NO EXCEPTIONS

### **Branch Management - MANDATORY WORKFLOW**
- **ALL changes MUST be made on a dedicated branch** following the "Branch Naming - MANDATORY SCHEMA".
- **Direct commits to `main` are ABSOLUTELY PROHIBITED.**
- **Branch Naming - MANDATORY SCHEMA**
  **Format**: `YYYYMMDD-HHMMSS-type-short-description`
  Examples:
  - `20250914-143000-feat-user-profile-management`
  - `20250914-143515-fix-login-bug-authentication`
  - `20250914-144030-docs-api-endpoint-updates`
- **Branch Preservation**
  - **NEVER delete branches** without explicit user permission
  - All branches contain valuable historical information
  - **NO** automatic cleanup with `git branch -d`
  - **YES** automatic merge to main branch and ensure dedicated branch has preserved all new changes.

### **Environment & Dependencies**
- **Python 3.13+ ONLY** (Ubuntu 25.04 built-in)
- **UV package manager ONLY** - NO pip, conda, poetry, or other package managers
- **Cross-project installation**: System installs into any GitHub project via `install-guardian-agents.sh`
- **Version**: Currently 2.5.1 - keep ALL files synchronized

### **System Specifications**
- **Agent Count**: 52 agents (49 specialized + 3 meta-agents). The 3 meta-agents are specifically designed to prevent code creep and over-engineering at the earliest stages of development. New agents will be added.
- **Architecture**: 5 layers (1-product, 2-engineering, 3-operations, 4-thinktank, 5-meta-agents)
- **Installation Method**: Single script (`install-guardian-agents.sh`) only
- **Progress Tracking**: Single file (`issues_to_fix.md`) only

## 🛠️ Development Commands

```bash
# Environment setup (UV only)
uv venv .venv && source .venv/bin/activate
uv pip install -e .

# Quality checks (must pass before commit)
.venv/bin/python -m ruff check scripts/
.venv/bin/python -m mypy scripts/ --ignore-missing-imports

# Installation testing
./install-guardian-agents.sh
```

## 📝 Code Style - MANDATORY

### **File Naming Convention**
- Agents: `[ID]-[department]-[role]-[specialization]-guardian.md`
- IDs: 3-digit sequential (001, 002, 003...)
- NO file renaming without explicit approval

### **Agent File Structure - EXACT FORMAT**
```markdown
---
name: [ID]-[department]-[role]-[specialization]-guardian
description: [Clear description]. MUST BE USED for [specific trigger].
tools: [list]
---

You are a [role] specialist...

## Your Role
- Agent ID: [ID]
- Department: [Department]
- Specialization: [Specific area]

## Core Responsibilities
[List key responsibilities]

## Agent Relationships
### Next Agents (Auto-chain to):
- [Specific agent IDs and conditions]
```

### **Modern Python Requirements**
- Type annotations: `X | Y` (not `Union[X, Y]`)
- Target version: py312 (Ruff/Black compatible)
- Requirements-python: ">=3.13"



## ⚠️ ABSOLUTE PROHIBITIONS

### **DO NOT**
- Use any package manager except UV
- Change agent count from the documented total
- Break the 4-layer architecture
- Create additional installation methods
- Modify version numbers without synchronizing ALL files
- Add complex validation or automation not explicitly requested
- Create multiple progress tracking systems

### **DO NOT BYPASS**
- Pre-commit hooks (fix issues, don't skip)
- Version consistency checks across files
- Agent count accuracy requirements
- UV-only package management compliance

## ✅ MANDATORY ACTIONS

### **Before Every Commit**
1. **Version Check**: All files must show same version (currently 2.5.1)
2. **Agent Count**: Reflects the documented total.
3. **Pre-commit**: Must pass without loops or conflicts
4. **Installation Test**: `install-guardian-agents.sh` must work

### **Quality Gates**
- Pre-commit hooks pass without infinite loops
- Version consistency across pyproject.toml, manifest.json, README files
- Agent count claims match reality (documented total).
- Single installation method only

## 🔧 Commit Guidelines

### **Commit Message Format - MANDATORY**
```
type: brief description

DETAILED CHANGES:
- Specific change 1
- Specific change 2
- Impact on system

VALIDATION:
- Pre-commit: ✅ Passed
- Version sync: ✅ All files 2.5.1
- Agent count: ✅ 52 agents

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## 📊 System Status Requirements

**Production Ready Status:**
- ✅ Ubuntu 25.04 + Python 3.13 + UV compliance
- ✅ Pre-commit hooks without loops
- ✅ Version consistency (2.5.1) across all files
- ✅ Single installation method
- ✅ 52 agents accurately documented
- ✅ Cross-project installation functional

## 🎯 Current Focus Areas

**From issues_to_fix.md (consolidated todo list):**
1. Maintain production readiness
2. Further complexity reduction if requested
3. Phase 2 research implementation for agents 002-006, 021-025
4. Environment setup time validation (< 2 minutes)
5. Cross-platform compatibility testing

---

**Version**: 2.5.1
**Status**: Production Ready
**Last Updated**: 2025-09-14

**CRITICAL**: These instructions override all previous guidelines. Follow exactly as written.
