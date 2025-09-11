# Guardian Package Manager (GPM) - Installation Guide

Transform any project into an AI-enhanced development environment with specialized Guardian agents that work seamlessly with Claude Code and spec-driven development.

## 🎯 What You Get

- **45+ Specialized AI Agents**: Expert agents for every aspect of software development
- **Smart Agent Selection**: Claude Code automatically picks the right agent for your task
- **Living Documentation**: Agents stay updated with latest best practices and research
- **Spec-Kit Integration**: Perfect for spec-driven development workflows
- **Intelligent Updates**: Preserve customizations while staying current
- **Zero Git Conflicts**: Smart package management without nested repositories

## 📋 Prerequisites

- **Claude Code**: Latest version with agent support
- **curl**: For installation (usually pre-installed)
- **Python 3.7+**: For advanced features (optional)
- **Git**: For version tracking (recommended)

## 🚀 Quick Installation

### 1. Install Guardian Package Manager

```bash
# One-line installation
curl -sSL https://raw.githubusercontent.com/kairin/claude-guardian-agents/main/install.sh | bash

# Restart terminal or reload profile
source ~/.bashrc  # or ~/.zshrc
```

### 2. Initialize Your Project

```bash
# Navigate to your project
cd your-awesome-project/

# Initialize Guardian system
gpm init

# Install all Guardian agents
gpm install
```

### 3. Start Using with Claude Code

```bash
# Claude Code will now automatically see your agents
# Just start Claude Code in your project directory
claude-code .
```

That's it! 🎉 Your project now has 45+ specialized AI agents ready to assist with development.

## 🔧 Advanced Installation Options

### Install Specific Categories

```bash
# Install only backend development agents
gpm install backend

# Install quality engineering agents
gpm install quality

# Install DevOps and infrastructure agents
gpm install devops
```

### Project-Specific Installation

GPM automatically detects your project type and recommends relevant agents:

```bash
# Node.js projects get frontend, backend, and quality agents
gmp install  # in package.json directory

# Python projects get backend, data, and quality agents
gpm install  # in requirements.txt directory

# Generic projects get core strategy and operations agents
gpm install  # in any directory
```

## 📁 What Gets Installed

After installation, your project structure includes:

```
your-project/
├── .claude/
│   ├── agents/                          # Guardian agents (45+ files)
│   │   ├── 001-strategy-product-leadership-guardian.md
│   │   ├── 062-development-backend-senior-guardian.md
│   │   ├── 072-development-quality-senior-guardian.md
│   │   └── agent-index.json            # For Claude Code smart selection
│   └── ...
├── .guardian/
│   ├── metadata.json                   # Version tracking and checksums
│   ├── customizations/                 # Your local agent modifications
│   ├── templates/                      # Project-specific templates
│   └── cache/                          # Update cache (git-ignored)
└── specs/                              # spec-kit integration (if detected)
    ├── agents/                         # Agent-generated specifications
    └── workflows/                      # Spec-driven workflows
```

## 🧠 How Claude Code Uses Guardian Agents

### Automatic Agent Selection

Claude Code reads the `agent-index.json` and automatically selects appropriate agents based on your requests:

```
You: "Build a REST API for user authentication"
Claude Code:
  🎯 Selected agents:
  - 062-development-backend-senior-guardian (API development)
  - 072-development-quality-senior-guardian (API testing)
  - 092-security-operations-director-guardian (Authentication security)
```

### Multi-Agent Workflows

Complex tasks automatically chain multiple agents:

```
You: "Implement a new feature for the mobile app"
Claude Code workflow:
  1. 002-strategy-product-strategy-guardian → Define requirements
  2. 044-architecture-principal-architect-guardian → Design architecture
  3. 068-development-mobile-senior-guardian → Implement feature
  4. 072-development-quality-senior-guardian → Write tests
  5. 081-infrastructure-devops-director-guardian → Deploy feature
```

### Project Context Awareness

Agents adapt to your specific project:

- **Technology Stack**: Agents reference your package.json, requirements.txt, etc.
- **Existing Code**: Agents understand your codebase structure and patterns
- **Project Goals**: Agents align with your project's stated objectives

## 🔄 Keeping Agents Updated

### Smart Updates

Guardian agents are "living documentation" that improves over time:

```bash
# Check for updates
gpm status

# Update all agents with intelligent conflict resolution
gpm update

# View what changed
gpm diff
```

### Customization-Preserving Updates

GPM's intelligent update system:

1. **Preserves your customizations** during updates
2. **Merges new features** automatically when possible
3. **Provides interactive resolution** for conflicts
4. **Archives deprecated agents** safely

### Update Process

```bash
$ gpm update

🔍 Checking for Guardian agent updates...
📊 Found 3 changes:
  🔄 062-development-backend-senior-guardian (updated)
  ➕ 121-thinktank-systems-thinking-guardian (new)
  🔀 072-development-quality-senior-guardian (conflict)

Proceed with update? [Y/n]: y

🔄 Updating agent: 062-development-backend-senior-guardian
➕ Installing new agent: 121-thinktank-systems-thinking-guardian
🔀 Resolving conflict for customized agent: 072-development-quality-senior-guardian

Options for 072-development-quality-senior-guardian:
  1. Keep local version (your customizations)
  2. Use remote version (lose customizations)
  3. Show diff and decide
Choose option [1-3]: 3

[Shows detailed diff with merge options...]

✅ Update completed successfully!
```

## 🔗 Spec-Kit Integration

### Automatic Integration

If GPM detects [spec-kit](https://github.com/kairin/spec-kit) in your project:

```bash
# GPM automatically enables spec integration
gpm init  # Detects specs/ directory

✅ spec-kit detected - enabling integration
📋 Spec-driven development workflows activated
```

### Spec-Driven Workflows

Agents can generate and consume specifications:

```bash
# Generate API specification from backend agent
gpm generate-spec --agent=062 --type=api-contract

# Update agents based on specification changes
gpm sync-specs

# Validate spec-agent consistency
gmp validate-specs
```

### Example Spec-Driven Workflow

```bash
# 1. Product agent generates feature specification
gpm run-workflow feature_definition --input="user authentication"

# 2. Architecture agent creates system design spec
gpm run-workflow system_design --input=specs/feature-auth.md

# 3. Backend agent implements based on architecture spec
gpm run-workflow backend_implementation --input=specs/system-design-auth.md

# 4. Quality agent creates tests based on implementation spec
gpm run-workflow test_implementation --input=specs/backend-impl-auth.md
```

## 🛠️ Customizing Agents

### Local Customizations

Customize agents for your specific needs:

```bash
# Create local customization
gpm customize 062-development-backend-senior-guardian

# Edit the agent file
vim .claude/agents/062-development-backend-senior-guardian.md

# GPM tracks your customizations and preserves them during updates
```

### Project Templates

Create reusable project templates:

```bash
# Export current agent configuration as template
gpm template export my-nodejs-api-template

# Apply template to new projects
gpm template apply my-nodejs-api-template
```

## 📊 Managing Your Installation

### Check Status

```bash
gpm status
```

```
Guardian Package Manager Status

Installation Status: Initialized ✅
Project Type: nodejs
Guardian Version: 2.3.0
Spec Integration: Enabled ✅

Installed Agents: 45
├── Strategy: 11 agents
├── Architecture: 5 agents
├── Development: 15 agents
├── Quality: 3 agents
├── DevOps: 3 agents
├── Operations: 8 agents

Agent Index: Generated ✅
Last Updated: 2025-09-11T10:30:00Z
Local Customizations: 2 agents
```

### List Available Agents

```bash
gmp list
```

```
📋 Available Guardian Agents

🎯 STRATEGY & PRODUCT (11 agents)
  001 Product Leadership Guardian     - Strategic product vision
  002 Product Strategy Guardian       - Product strategy and planning
  021 Design Leadership Guardian      - Design strategy and systems
  ...

⚙️ DEVELOPMENT (15 agents)
  061 Backend Director Guardian       - Backend architecture leadership
  062 Backend Senior Guardian         - Senior backend development
  067 Mobile Director Guardian        - Mobile development leadership
  ...
```

### Search for Agents

```bash
# Find agents for specific tasks
gpm search "api development"
gpm search "testing"
gpm search "deployment"
```

## 🔍 Troubleshooting

### Common Issues

#### GPM Command Not Found
```bash
# Reload your shell profile
source ~/.bashrc  # or ~/.zshrc

# Or manually add to PATH
export PATH="$HOME/.gmp/bin:$PATH"
```

#### Agents Not Appearing in Claude Code
```bash
# Verify agents are installed
ls .claude/agents/

# Regenerate agent index
gpm install --force

# Check Claude Code is in project directory
cd your-project/
claude-code .
```

#### Update Conflicts
```bash
# Show current status
gpm status

# Reset specific agent to default
gpm reset 072-development-quality-senior-guardian

# Or restore from backup
gmp restore --agent=072 --version=2.2.0
```

### Getting Help

```bash
# Show GPM help
gpm help

# Show specific command help
gpm help install
gmp help update

# Check version
gpm version
```

## 🎯 Best Practices

### 1. Project Organization
- Initialize GPM in your project root directory
- Use `.gitignore` to exclude `.guardian/cache/`
- Commit `.guardian/metadata.json` for team consistency

### 2. Agent Usage
- Let Claude Code select agents automatically for best results
- Use `gpm search` to discover relevant agents for new tasks
- Customize agents only when necessary for project-specific needs

### 3. Updates
- Run `gmp update` regularly to get latest improvements
- Review changes with `gmp diff` before applying updates
- Use `gmp status` to monitor your installation health

### 4. Team Collaboration
- Share `.guardian/metadata.json` with your team
- Document customizations in your project README
- Use consistent agent versions across development environments

## 🚀 What's Next?

After installation, you can:

1. **Start a conversation with Claude Code** - It will automatically use Guardian agents
2. **Try complex workflows** - Ask Claude Code to build features end-to-end
3. **Explore spec-kit integration** - Use specification-driven development
4. **Customize agents** - Adapt agents to your project's specific needs
5. **Join the community** - Share your experiences and contribute improvements

## 📚 Additional Resources

- **[Guardian Agents Documentation](README.md)** - Complete system overview
- **[Agent Reference Guide](docs/agent-reference.md)** - Detailed agent descriptions
- **[Workflow Examples](docs/workflows/)** - Real-world usage examples
- **[Spec-Kit Integration Guide](docs/spec-kit-integration.md)** - Spec-driven development
- **[Contributing Guide](docs/contributing.md)** - Help improve the system

## 💬 Support & Community

- **Issues**: [GitHub Issues](https://github.com/kairin/claude-guardian-agents/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kairin/claude-guardian-agents/discussions)
- **Documentation**: [Full Documentation](https://github.com/kairin/claude-guardian-agents)

---

**Welcome to the future of AI-enhanced development! 🎉**

Your project now has a complete team of AI specialists ready to help with every aspect of software development, from initial planning to production deployment.
