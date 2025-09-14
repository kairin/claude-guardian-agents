# The Three-Tier Guardian Agent System

This document describes a powerful, lightweight system for maintaining project quality and preventing scope creep. It consists of three specialized "meta" agents that work together to analyze, simplify, and fix code.

This system is designed to be used as a lightweight alternative or a meta-layer on top of the 49-agent system. It is particularly useful when you need to enforce standards and prevent scope creep, but do not have the time to implement and manage all 49 agents.

## The Three Tiers

The system is composed of three agents, each with a distinct role and corresponding to a different Claude model:

1.  **The Orchestrator (Opus Model):** The high-level reviewer and delegator.
2.  **The Analyzer (Sonnet Model):** The complexity detector and todo generator.
3.  **The Fixer (Haiku Model):** The minimalist code fixer.

### 👑 The Orchestrator (Opus Agent)

-   **Agent Name:** `architectural-orchestrator`
-   **Role:** High-level review, delegation, and verification.
-   **Purpose:** To ensure that all changes align with the original project requirements and to prevent scope creep and over-engineering.

### 🔍 The Analyzer (Sonnet Agent)

-   **Agent Name:** `codebase-complexity-analyzer`
-   **Role:** Codebase analysis and todo generation.
-   **Purpose:** To scan the codebase for complexity, identify unnecessary features, and create actionable todos for the Fixer agent.

### 🎯 The Fixer (Haiku Agent)

-   **Agent Name:** `minimal-todo-fixer`
-   **Role:** Direct issue resolution.
-   **Purpose:** To execute fixes from a todo list with minimal changes and no additional complexity.

## 🔄 How the System Works

The Three-Tier Guardian Agent System works in a continuous cycle of analysis, simplification, and verification:

1.  **The Orchestrator** reviews proposed changes against the project requirements.
2.  If the changes are complex or have the potential for scope creep, **The Orchestrator** delegates the analysis to **The Analyzer**.
3.  **The Analyzer** scans the codebase and generates a list of specific, actionable todos to simplify the code and remove unnecessary complexity.
4.  **The Fixer** executes the todos, making only the minimal changes required.
5.  **The Orchestrator** verifies the fixes and approves the changes.

This system provides a powerful way to maintain project quality and prevent the kind of over-engineering that can lead to technical debt and maintenance nightmares.
