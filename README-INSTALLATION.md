# Guardian Agents - Project Installation

Install Guardian Agents into any of your GitHub projects to get access to 100+ specialized AI agents.

## 🚀 Quick Installation

Run this command from your project root:

```bash
curl -sSL https://raw.githubusercontent.com/kairin/claude-guardian-agents/main/install-guardian-agents.sh | bash
```

Or download and run manually:

```bash
wget https://raw.githubusercontent.com/kairin/claude-guardian-agents/main/install-guardian-agents.sh
chmod +x install-guardian-agents.sh
./install-guardian-agents.sh
```

## 📁 What Gets Installed

```
your-project/
├── .guardian/                    # Complete Guardian Agents system (git-ignored)
│   ├── 1-product/               # Strategy & Product agents (001-025)
│   ├── 2-engineering/           # Technical & Development agents (041-083)
│   ├── 3-operations/            # Operations & Security agents (091-100)
│   ├── 4-thinktank/            # Think-Tank reasoning agents (101-108)
│   └── scripts/                 # Management scripts
├── .claude/agents/              # Claude Code integration
│   └── agent-index.json         # Auto-generated agent index
├── update-guardian-agents.sh    # Update script
└── .gitignore                   # Updated to ignore .guardian/
```

## 🔄 Keeping Updated

Update to the latest Guardian Agents version:

```bash
./update-guardian-agents.sh
```

This will:
- Pull latest agents from the repository
- Update Claude Code integration
- Preserve your project files (agents are managed separately)

## 🛡️ Available Agent Categories

### Strategy & Product (001-025)
- Product Leadership & Strategy
- Product Management & Ownership
- UX Research & Design
- UI Design & Interface

### Technical Architecture (041-045)
- CTO Office & Technical Leadership
- Principal & Senior Architects
- VP Engineering Management

### Development (061-083)
- Backend Development (API, Database)
- Frontend Development (UI, Web)
- Mobile Development (iOS, Android)
- Quality Engineering (Testing, QA)
- DevOps & Infrastructure

### Operations & Security (091-100)
- COO Office & Operations Strategy
- Security Operations & Compliance
- Data Operations & Analytics
- IT Operations & Support

### Think-Tank Reasoning (101-108)
- First Principles Analysis
- Creative & Lateral Thinking
- Human Pattern Analysis
- Mathematical & Logical Reasoning

## 🎯 Usage in Claude Code

After installation, agents are automatically available in Claude Code:

1. **Automatic Selection**: Claude Code will choose appropriate agents based on your task
2. **Manual Selection**: Use `/agents` command to see available agents
3. **Agent Chaining**: Agents can call other agents for complex workflows

## 🔧 Customization

### Project-Specific Agents
Add your own agents to `.claude/agents/` - they won't be overwritten during updates.

### Agent Configuration
Modify agent behavior by editing files in `.guardian/` directory (changes will be lost on update).

## 🚫 What This Doesn't Affect

- **Your project code** - Agents are installed separately
- **Your git history** - `.guardian/` is git-ignored
- **Your dependencies** - No changes to package.json, requirements.txt, etc.
- **Your build process** - No impact on existing workflows

## ⚠️ Requirements

- **Git repository** - Must be run from a git project root
- **Internet connection** - For downloading agents
- **Python 3.8+** - For generating Claude Code integration
- **Claude Code** - To use the agents (optional but recommended)

## 🗑️ Uninstallation

Remove Guardian Agents from your project:

```bash
rm -rf .guardian/
rm -rf .claude/agents/
rm update-guardian-agents.sh
# Remove .guardian/ line from .gitignore if desired
```

## 📋 Troubleshooting

### Installation fails
- Ensure you're in a git repository root
- Check internet connection
- Verify Python 3.8+ is available

### Agents not appearing in Claude Code
- Run `./update-guardian-agents.sh` to refresh integration
- Check that `.claude/agents/agent-index.json` exists
- Restart Claude Code if necessary

### Update fails
- Delete `.guardian/` directory and run installation script again
- This will give you a fresh copy without losing your project files

---

**Repository**: https://github.com/kairin/claude-guardian-agents
**Version**: 3.1.0
**Last Updated**: 2025-09-14
