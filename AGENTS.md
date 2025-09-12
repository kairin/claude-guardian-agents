# AGENTS.md

> **Instructions for AI coding agents working on the Guardian Agents system**

## 🎯 Project Overview

Guardian Agents is a comprehensive AI agent orchestration system with 49 specialized agents across 4 cognitive layers. This project follows spec-driven development with extensive research foundations.

## 🛠️ Development Environment Setup

### **Dependencies & Installation**
```bash
# Setup Python environment (uses uv exclusively)
./scripts/setup-python-env.sh

# Activate environment
source .venv/bin/activate

# Verify installation  
make validate
```

### **Key Commands**
```bash
# Run validation suite (target: 100% pass rate)
./scripts/validate-gpm.sh

# Generate progress reports
make reports

# Track implementation progress
make track

# Run quality checks
make check
```

## 📝 Code Style & Standards

### **Agent File Structure**
All agent files must follow this exact format:
```markdown
---
name: [ID]-[department]-[role]-[specialization]-guardian
description: Clear description with "MUST BE USED" triggers for auto-selection
tools: [google_web_search, web_fetch]
---

You are a [role] specialist in the [department] layer...

## Your Role
- Agent ID: [ID]
- Department: [Department]
- Specialization: [Specific expertise]

## Core Responsibilities
[List of key responsibilities]

## Agent Relationships
### Next Agents (Auto-chain to):
- [List of agents this can call]

### Escalate To:
- [When to escalate to human or other agents]
```

### **Naming Conventions**
- **Agent IDs**: 3-digit sequential (001, 002, etc.)
- **File Names**: `[ID]-[department]-[role]-[specialization]-guardian.md`
- **Directories**: Numbered by layer (1-product/, 2-engineering/, 3-operations/, 4-thinktank/)

### **Research Integration Requirements**
Each agent must integrate **4-6 academic research papers** with:
- Citation format: `**Paper Title** (Author, Year)`
- Implementation section showing how research applies
- Methodology descriptions with practical applications

## 🧪 Testing & Validation

### **Required Tests**
All changes must pass:
```bash
# GPM validation (target: 43/43 tests passing)
./scripts/validate-gpm.sh

# Agent discovery and classification
# URL accessibility validation  
# JSON structure validation
# Manifest integrity checks
```

### **Quality Gates**
- **Agent Count**: Must maintain 49 total agents
- **Think-Tank**: Must have 8 personality archetypes
- **Research Papers**: 35+ integrated across system
- **Validation Rate**: 100% (43/43 tests passing)

## 🚀 Agent System Workflow

### **Agent Categories & Structure**
```
4-Layer Architecture:
├── 1-product/ (11 agents)     - Strategic & Product
├── 2-engineering/ (20 agents) - Technical Development  
├── 3-operations/ (10 agents)  - Infrastructure & Operations
└── 4-thinktank/ (8 agents)    - Cognitive Diversity
```

### **Auto-Chaining Patterns**
Agents automatically chain based on:
- Task description content analysis
- "MUST BE USED" triggers in descriptions
- Agent relationship definitions
- Context-aware intelligent routing

## 📚 Key Documentation

### **Agent System Docs**
- **[Agent Registry](docs/agents/registry.md)** - Complete agent catalog
- **[Agent Relationships](docs/agents/relationships.md)** - Chaining patterns
- **[Agent Templates](docs/agents/templates.md)** - Creation templates

### **Development Guides**
- **[Research Papers](docs/RESEARCH-PAPERS.md)** - Academic foundations
- **[Progress Documentation](docs/COMPLETE-PROGRESS-DOCUMENTATION.md)** - Project status
- **[Think-Tank System](docs/THINK-TANK-COMPLETION-SUMMARY.md)** - Cognitive diversity

## ⚠️ Critical Requirements

### **DO NOT**
- Modify the 4-layer architecture without approval
- Reduce agent count below 49 total
- Break the 8-agent think-tank personality system
- Remove research paper integrations
- Change agent ID numbering system

### **ALWAYS**
- Run validation tests before committing
- Maintain 100% GPM test pass rate
- Follow semantic versioning for releases
- Include research foundations in new agents
- Test agent auto-chaining functionality

## 🔧 Commit Guidelines

### **Commit Message Format**
```
type: brief description

- Detailed changes
- Impact on agent system
- Validation results

🤖 Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

### **Pre-commit Checks**
- GPM validation passing (43/43 tests)
- JSON structure validation
- Agent discovery verification
- Link integrity checks

## 📊 Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Agent Count | 49+ | 49 ✅ |
| Validation Rate | 100% | 100% ✅ |
| Think-Tank Agents | 8 | 8 ✅ |
| Research Papers | 35+ | 35+ ✅ |

---

**Version**: 2.1.0  
**Last Updated**: September 12, 2025  
**Status**: 100% Validation Success

*This file follows the [agents.md](https://agents.md/) standard for AI coding agent instructions.*