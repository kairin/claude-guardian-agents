---
archived: true
title: "Agent Creation Guide (Consolidated)"
description: "Short guidance for creating and registering agent roles. Full originals are in `docs/archive/`."
version: 1.0
status: "Published"
owner: "docs"
last_updated: "2025-09-13"
tags:
  - "documentation"
  - "agents"
  - "guide"
related_docs:
  - "../../agents/templates.md"
  - "../../NAMING-CONVENTION.md"
---

# Agent Creation — Summary

This file provides a minimal summary of how to create agent role files. For full templates and historical versions, see `docs/archive/agents/AGENT-CREATION-GUIDE.md` and `docs/ROLES_SUMMARY.md`.

Key steps:
- Create a new agent file in `.claude/agents/` following naming conventions.
- Keep descriptions concise and include trigger phrases.
- Prefer one-line role summaries; avoid duplicating runtime instructions.

For detailed templates and examples, consult the archived guide in `docs/archive/`.
---
title: "Agent Creation Guide"
description: "Step-by-step instructions for creating Guardian Agents in Claude Code."
version: 1.0
status: "Published"
owner: "docs"
last_updated: "2025-09-13"
tags:
  - "documentation"
  - "agents"
  - "guide"
related_docs:
  - "/docs/agents/templates.md"
  - "/docs/NAMING-CONVENTION.md"
---

# Guardian Agent Creation Guide

Step-by-step instructions for creating Guardian Agents in Claude Code.

## 🚀 Quick Start

### 1. Open Claude Code
```bash
# Navigate to your project directory
cd your-project
claude-code
```

### 2. Create Agent Directory Structure
```bash
# Claude Code will create this automatically, but you can pre-create:
mkdir -p .claude/agents/1-product/1-product-management
mkdir -p .claude/agents/1-product/2-product-design
mkdir -p .claude/agents/2-engineering/1-cto-office
mkdir -p .claude/agents/2-engineering/2-software-engineering
mkdir -p .claude/agents/3-operations/1-coo-office
```

### 3. Use `/agents` Command
1. In Claude Code, type: `/agents`
2. Choose: **"Create Project Agent"**
3. Enter agent name: `001-strategy-product-leadership-guardian`
4. Claude Code will create: `.claude/agents/001-strategy-product-leadership-guardian.md`

## 📝 Agent Template

Copy and customize this template for each agent:

```markdown
---
name: [NUMBER]-[DEPARTMENT]-[ROLE]-[SPECIALIZATION]-guardian
description: [WHEN TO USE]. [TRIGGER WORDS]. MUST BE USED for [SPECIFIC TASKS].
tools: [tool1, tool2]  # Optional: restrict available tools
---

You are a [ROLE DESCRIPTION] with [EXPERTISE AREAS]. You're responsible for [MAIN RESPONSIBILITIES].

## Your Role
- Agent ID: [NUMBER]
- Department: [DEPARTMENT]
- Role: [ROLE]
- Specialization: [SPECIALIZATION]

## Core Responsibilities
- [RESPONSIBILITY 1]
- [RESPONSIBILITY 2]
- [RESPONSIBILITY 3]

## Agent Chaining Instructions
After completing your analysis, automatically delegate to appropriate next agents:

### Sequential Chain (Primary Flow):
1. **[NEXT-AGENT-NUMBER]-[NEXT-AGENT-NAME]** - For [SPECIFIC TASK]
2. **[ANOTHER-AGENT]** - For [ANOTHER TASK]

### Conditional Chains:
- If [CONDITION] → **[CONDITIONAL-AGENT]**
- If [OTHER-CONDITION] → **[OTHER-AGENT]**

### Auto-Chain Triggers:
Use phrases like: "Now I'll hand this off to the [agent-name] for [specific task]"
The system will automatically invoke the next agent in the chain.

[ADDITIONAL CONTEXT AND PERSONALITY TRAITS]
```

## 🏗️ Directory Organization

### Strategic Agents (001-020)
```
.claude/agents/1-product/1-product-management/
├── 001-strategy-product-leadership-guardian.md
├── 1-product-strategy/
│   ├── 002-strategy-product-strategy-guardian.md
│   └── 003-strategy-product-management-guardian.md
└── 2-product-ownership/
    └── 004-strategy-product-ownership-guardian.md
```

### Technical Agents (041-083)
```
.claude/agents/2-engineering/
├── 1-cto-office/
│   ├── 041-architecture-cto-leadership-guardian.md
│   └── 042-architecture-technical-fellow-guardian.md
├── 2-software-engineering/
│   ├── 043-architecture-vp-engineering-guardian.md
│   └── [other engineering agents]
```

### Operational Agents (091-100)
```
.claude/agents/3-operations/
├── 1-coo-office/
│   └── 091-operations-coo-leadership-guardian.md
├── 2-security-operations/
│   └── 092-security-operations-director-guardian.md
```

## ✅ Agent Chaining Examples

### Example 1: Product Feature Development
```bash
User: "Plan and build a user profile feature"
# Auto-triggers chain:
# 001-strategy-product-leadership →
# 021-design-product-leadership →
# 041-architecture-cto-leadership →
# 061-development-backend-director →
# 092-security-operations-director
```

### Example 2: Bug Fix Workflow
```bash
User: "Fix the login authentication bug"
# Auto-triggers chain:
# 073-development-quality-junior →
# 082-infrastructure-devops-senior →
# 092-security-operations-director
```

## 🎯 Best Practices

### 1. Agent Descriptions
- **Be specific**: "MUST BE USED for [task type]"
- **Include triggers**: Keywords that should auto-select this agent
- **Define scope**: Clear boundaries of responsibility

### 2. Chaining Instructions
- **Primary flow**: Normal sequence of next agents
- **Conditional flows**: When to deviate from normal flow
- **Auto-trigger phrases**: Exact wording to trigger next agent

### 3. Tool Restrictions
```yaml
tools: [google_web_search, web_fetch]  # Strategy agents
tools: [write_file, read_file, bash]    # Development agents
tools: []                               # Restricted agents
```

### 4. Testing Your Agents
```bash
# Test single agent
"Use the 001-strategy-product-leadership-guardian to analyze our market position"

# Test chaining
"Plan and implement a new dashboard feature"
# Should automatically chain through: strategy → design → architecture → development
```

## 🔧 Troubleshooting

### Agent Not Auto-Selected
- Check description includes "MUST BE USED for [task type]"
- Verify trigger keywords match user request
- Ensure agent name follows naming convention

### Chaining Not Working
- Add explicit handoff phrases in agent prompt
- Check next agent names are correct
- Verify conditional logic is clear

### Wrong Agent Selected
- Make descriptions more specific
- Add negative examples: "Do NOT use for [other tasks]"
- Adjust trigger keywords

## 📚 Next Steps

1. **Create your first agent** using the template
2. **Test single agent** invocation
3. **Add chaining logic** to connect agents
4. **Test full workflows** with multiple agents
5. **Refine and optimize** based on results

---

**For more examples, see the [Agent Registry](../../agents/registry.md) file with all agent templates.**
