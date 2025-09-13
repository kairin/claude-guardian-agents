# Claude Guardian Agents

A comprehensive system of specialized AI agents designed to handle various aspects of software development, project management, and operations across any project type.

## 🎯 What Are Guardian Agents?

Guardian Agents are specialized Claude subagents, each with specific expertise and responsibilities. Think of them as your AI team members, each with their own role, tools, and workflows.

## 📚 Research Foundation

This system is built on solid academic research. Each agent design is informed by peer-reviewed papers and proven methodologies:

- **Parallel Reasoning**: [ParaThinker (2024)](https://www.arxiv.org/abs/2509.04475) - 12.3% accuracy improvement
- **Multi-Agent Systems**: Society of Mind (Minsky, 1986) - Specialized agents create intelligence
- **Software Engineering**: Design Patterns (GoF, 1994) - Proven architectural patterns
- **Product Management**: Lean Startup (Ries, 2011) - Validated learning approach
- **DevOps**: DORA Research - 208x deployment frequency improvement

📖 **[View Complete Research Documentation](docs/RESEARCH-PAPERS.md)** - All papers and methodologies

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "🧠 Think-Tank Layer"
        T1[First Principles]
        T2[Human Patterns]
        T3[Creative Lateral]
    end

    subgraph "🎯 Strategic Layer"
        A1[Product Guardians]
        A2[Executive Guardians]
    end

    subgraph "⚙️ Technical Layer"
        B1[Development Guardians]
        B2[Quality Guardians]
        B3[Security Guardians]
    end

    subgraph "🚀 Operational Layer"
        C1[Infrastructure Guardians]
        C2[Process Guardians]
        C3[Workflow Guardians]
    end

    T1 -.->|unstick| A1
    T2 -.->|unstick| B1
    T3 -.->|unstick| C1

    A1 --> B1
    A2 --> C2
    B1 --> B2
    B2 --> B3
    B3 --> C1
    C1 --> C3

    style T1 fill:#fff2e1
    style A1 fill:#e1f5e1
    style B2 fill:#ffe1e1
    style C1 fill:#e1e8ff
```

## 📋 Quick Start Guide

### For Project Managers & Non-Developers
- 📖 [Visual Agent Overview](docs/visual-overview.md) - See what each agent does
- 🎯 [Use Case Examples](docs/use-cases.md) - Real-world scenarios
- 📊 [Agent Workflows](docs/workflows/) - Step-by-step process diagrams

### For Developers
- 🔧 [Technical Implementation](docs/technical/) - How agents work
- ⚙️ [Configuration Guide](docs/config/) - Setup instructions
- 🚀 [API Reference](docs/api/) - Integration details

## 🗂️ Agent Categories

### 1. 🎯 Strategic Agents
**Purpose**: High-level planning and product strategy
- **Product Guardians**: Market research, product strategy, roadmapping
- **Executive Guardians**: Business alignment, stakeholder management
- [📁 View All Strategic Agents](1-product/)

### 2. ⚙️ Technical Agents
**Purpose**: Code development and technical excellence
- **Development Guardians**: Code writing, architecture, implementation
- **Quality Guardians**: Testing, code review, performance optimization
- **Security Guardians**: Security audits, vulnerability assessment
- [📁 View All Technical Agents](2-engineering/)

### 3. 🚀 Operational Agents
**Purpose**: Infrastructure, deployment, and process management
- **Infrastructure Guardians**: Deployment, monitoring, scaling
- **Process Guardians**: Workflow automation, CI/CD, orchestration
- **Workflow Guardians**: Documentation, release management, compliance
- [📁 View All Operational Agents](3-operations/)

### 4. 🧠 Think-Tank Agents (NEW)
**Purpose**: Break reasoning deadlocks through diverse parallel thinking
- **First Principles Guardians**: Strip problems to fundamental truths
- **Human Pattern Guardians**: Apply anthropological and cultural insights
- **Creative Guardians**: Lateral thinking and rule-breaking innovation
- **Simplicity Guardians**: Child-like questioning to cut through complexity
- [📁 View All Think-Tank Agents](4-thinktank/)

## 🔄 How Agents Work Together

### ✅ Verified: Subagent Chaining Supported
Claude Code **officially supports** subagent chaining as an "Advanced usage" feature. Agents can automatically call other agents in sequence.

```mermaid
sequenceDiagram
    participant User
    participant Main as Claude Code
    participant S as 001-strategy-guardian
    participant D as 021-design-guardian
    participant A as 041-architecture-guardian
    participant Dev as 061-development-guardian
    participant Sec as 091-security-guardian

    User->>Main: "Build user login feature"
    Main->>S: Auto-select strategy agent
    S->>S: Define requirements
    S->>Main: "Next: design-guardian"
    Main->>D: Auto-chain to design
    D->>D: Create UI mockups
    D->>Main: "Next: architecture-guardian"
    Main->>A: Auto-chain to architecture
    A->>A: Design system architecture
    A->>Main: "Next: development-guardian"
    Main->>Dev: Auto-chain to development
    Dev->>Dev: Implement & test
    Dev->>Main: "Next: security-guardian"
    Main->>Sec: Auto-chain to security
    Sec->>User: ✅ Feature complete & secure
```

### 🧠 Intelligent Agent Selection
Claude Code **automatically selects agents** based on:
- Task description content
- Agent configuration descriptions
- Available tools and context
- **"MUST BE USED"** triggers in descriptions

### 🔗 Agent Communication Patterns
1. **Sequential Workflow**: 001 → 002 → 003... (process flow)
2. **Conditional Routing**: Route to different agents based on results
3. **Error Recovery**: Failed agents trigger recovery agents
4. **Parallel Execution**: Multiple agents work simultaneously

## 📚 Documentation Structure

```
📁 docs/
├── 📄 visual-overview.md          # Non-developer friendly overview
├── 📄 use-cases.md               # Real-world examples
├── 📁 workflows/                 # Workflow diagrams for each agent
│   ├── 📄 product-workflow.md
│   ├── 📄 development-workflow.md
│   └── 📄 operations-workflow.md
├── 📁 technical/                 # Developer documentation
│   ├── 📄 architecture.md
│   ├── 📄 agent-communication.md
│   └── 📄 customization.md
└── 📁 config/                    # Configuration guides
    ├── 📄 setup.md
    ├── 📄 environment.md
    └── 📄 troubleshooting.md
```

## 🚀 Getting Started

### Step 1: Create Your First Guardian Agent

#### Using Claude Code's `/agents` Command:
1. **Open Claude Code** in your project directory
2. **Run the `/agents` command** to open the agent creation interface
3. **Choose "Create Project Agent"** to store in `.claude/agents/`
4. **Name your agent** using our convention: `001-strategy-product-leadership-guardian`

#### Agent Configuration Template:
```markdown
---
name: 001-strategy-product-leadership-guardian
description: Strategic product leadership and vision setting. Use for high-level product decisions, roadmap planning, and team leadership guidance. MUST BE USED for product strategy tasks.
tools: [google_web_search, web_fetch]
---

You are a visionary product leader with deep understanding of markets and customer needs. You're responsible for the company's overall product direction and building world-class product teams.

## Your Role
- Agent ID: 001
- Department: Strategy
- Role: Product Leadership
- Specialization: Strategic product vision and team leadership

## Core Responsibilities
- Develop and communicate company product vision and strategy
- Lead product teams and foster innovation culture
- Drive research and development of new products and features
- Ensure product success in the market
- Collaborate with other executives to align product with business goals
- Represent product strategy to investors, partners, and customers

## Agent Relationships
### Next Agents (Auto-chain to):
- 002-strategy-product-strategy-guardian (for detailed strategy)
- 021-design-product-leadership-guardian (for design alignment)
- 041-architecture-cto-leadership-guardian (for technical feasibility)

### Escalate To:
- User for final strategic decisions
- 029-workflow-documentation-guardian (to document decisions)

You are a key member of the executive team and play a critical role in company success.
```

### Step 2: Organize Your Agents

Create agents in the correct directory structure:
```
.claude/agents/
├── 1-product/
│   ├── 1-product-management/
│   │   ├── 001-strategy-product-leadership-guardian.md
│   │   ├── 1-product-strategy/
│   │   │   ├── 002-strategy-product-strategy-guardian.md
│   │   │   └── 003-strategy-product-management-guardian.md
│   │   └── 2-product-ownership/
│   │       └── 004-strategy-product-ownership-guardian.md
│   └── 2-product-design/
├── 2-engineering/
└── 3-operations/
```

### Step 3: Test Agent Chaining

```bash
# Single agent invocation
"Use the 001-strategy-product-leadership-guardian to create a product roadmap"

# Automatic chaining (agents call each other)
"Plan and implement a new user authentication feature"
# → Triggers: strategy → design → architecture → development → security → deployment
```

## 📈 Version & Changes
- **Current Version**: 2.0.0
- [📋 View Changelog](CHANGELOG.md)
- [🔄 Version History](docs/versions/)

## 🤝 Contributing
- [📝 Adding New Agents](docs/contributing/new-agents.md)
- [🔧 Modifying Existing Agents](docs/contributing/modifications.md)
- [📚 Documentation Guidelines](docs/contributing/documentation.md)

## 💡 Example Usage

```bash
# Ask a strategic agent for product planning
/task "Create a product roadmap" --agent product-strategy-guardian

# Get technical implementation from development agent
/task "Implement user authentication" --agent backend-guardian

# Deploy with operational agent
/task "Deploy to production" --agent deployment-guardian
```

## 🎯 Benefits

✅ **Modular**: Use only the agents you need
✅ **Scalable**: Add new agents for new domains
✅ **Clear**: Visual workflows for every process
✅ **Generic**: Works with any project type
✅ **Integrated**: Seamless agent-to-agent communication

---

**Next Steps**:
1. 📖 Read the [Visual Overview](docs/visual-overview.md)
2. 🔍 Find your first agent with [Agent Finder](docs/agent-finder.md)
3. 🚀 Follow a [workflow guide](docs/workflows/)

*Powered by Claude's advanced subagent system for specialized task delegation.*
