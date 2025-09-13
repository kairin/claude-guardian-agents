# 🛡️ Guardian Agents - Comprehensive Documentation

> **Intelligent Agent Orchestration & Project Management System**
> Transform manual agent selection into intelligent, context-aware orchestration

## 📚 Documentation Index

### **🚀 Getting Started**
- [Quick Start Guide](getting-started/quick-start.md) - Get up and running in 5 minutes
- [Installation Guide](getting-started/installation.md) - Complete setup instructions
- [GPM Installation](getting-started/gpm-installation.md) - Guardian Package Manager setup
- [First Steps Tutorial](getting-started/first-steps.md) - Your first Guardian Agents workflow

### **💼 Project Management System**
- [Project Management Overview](PROJECT-MANAGEMENT-SYSTEM.md) - Complete system architecture
- [Progress Tracking Guide](project-management/progress-tracking.md) - How to track and manage progress
- [Report Generation](project-management/report-generation.md) - Automated reporting system
- [Validation Framework](project-management/validation.md) - Quality gates and validation

### **🤖 Agent System Documentation**
- [Agent Overview](agents/README.md) - Guardian Agents system overview
- [Agent Registry](agents/registry.md) - Complete catalog of all 49 agents
- [Agent Relationships](agents/relationships.md) - How agents chain and communicate
- [Agent Templates](agents/templates.md) - Templates for creating new agents
- [Agent Mapping](agents/mapping.md) - Directory structure and conventions

### **🔧 Technical Documentation**
- [System Architecture](technical/system-architecture.md) - Overall system design
- [Python Environment](technical/python-environment-spec.md) - uv-based Python management
- [Agent Specifications](technical/agent-specs.md) - Guardian agent implementation details
- [API Reference](technical/api-reference.md) - Complete API documentation

### **🧪 Development & Testing**
- [Development Workflow](workflows/development-workflow.md) - Complete development process
- [Testing Strategy](development/testing-strategy.md) - Testing framework and guidelines
- [Code Quality Standards](development/code-quality.md) - Quality gates and standards
- [Contributing Guidelines](development/contributing.md) - How to contribute

### **📊 Features & Specifications**
- [Feature Specifications](../specs/features/) - Detailed feature requirements
- [Outstanding Implementations](project-management/outstanding-implementations.md) - What's left to build
- [Implementation Roadmap](IMPLEMENTATION-ROADMAP.md) - Timeline and priorities

### **🛠️ Tools & Scripts**
- [Script Reference](tools/script-reference.md) - All automation scripts
- [Makefile Commands](tools/makefile-commands.md) - Development commands
- [Environment Management](tools/environment-management.md) - uv and Python tools

### **🚨 Troubleshooting & Support**
- [Common Issues](troubleshooting/common-issues.md) - Solutions to frequent problems
- [Error Codes](troubleshooting/error-codes.md) - Complete error reference
- [FAQ](troubleshooting/faq.md) - Frequently asked questions
- [Support](support.md) - How to get help

## 🎯 Project Status

**Current Phase**: Implementation Planning
**Overall Completion**: 23%
**Last Updated**: 2025-09-11

### **📈 Key Metrics**
- **Total Features**: 10 (2 completed, 3 in progress, 5 pending)
- **Guardian Agents**: 45 agents implemented
- **Documentation Coverage**: 85%
- **Test Coverage**: Target 90%

### **🚨 Current Priorities**
1. **Intelligent Agent Orchestration** - Context-aware agent selection
2. **Living Code Intelligence** - Bidirectional spec-code sync
3. **Advanced Project Analysis** - Deep project understanding
4. **Multi-Agent Workflows** - Complex task orchestration

## 🏗️ System Overview

Guardian Agents provides:

- **🧠 Intelligent Orchestration**: AI-driven agent selection based on project context
- **📊 Project Management**: Comprehensive tracking and accountability system
- **🔄 Automated Workflows**: Multi-agent task coordination
- **📝 Living Documentation**: Spec-driven development with real-time sync
- **🛡️ Quality Assurance**: Built-in validation and testing frameworks

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+ (recommended 3.11)
- [uv](https://docs.astral.sh/uv/) - Python package manager
- Git for version control

### **Installation**
```bash
# Clone the repository
git clone <repository-url>
cd claude-guardian-agents

# Setup Python environment (uses uv exclusively)
./scripts/setup-python-env.sh

# Activate environment
source .venv/bin/activate

# Verify installation
make validate
```

### **First Commands**
```bash
# Generate project reports
make reports

# Track current progress
make track

# Run quality checks
make check

# View all available commands
make help
```

## 📋 Project Structure

```
claude-guardian-agents/
├── docs/                           # 📚 Complete documentation
│   ├── getting-started/           # 🚀 Setup and tutorials
│   ├── project-management/        # 💼 PM system docs
│   ├── technical/                 # 🔧 Technical specifications
│   └── troubleshooting/           # 🚨 Help and support
├── specs/                         # 📋 Feature specifications
│   ├── features/                  # 🎯 Detailed feature specs
│   ├── epics/                     # 🗺️ High-level epics
│   └── architecture/              # 🏗️ System architecture
├── agents/                        # 🤖 Guardian agent implementations
│   ├── 001-help-me-plan/         # Planning and strategy
│   ├── 002-code-guardian/        # Code quality
│   └── ... (43 more agents)
├── tracking/                      # 📊 Progress tracking system
│   ├── progress.json             # Current project status
│   ├── validation-results/       # Test and validation outputs
│   └── reports/                  # Generated status reports
├── scripts/                      # 🛠️ Automation scripts
│   ├── setup-python-env.sh      # Environment setup
│   ├── track-progress.py         # Progress tracking
│   ├── generate-reports.py       # Report generation
│   └── validate-gmp.py           # GPM validation
├── pyproject.toml                # 🐍 Python project configuration
├── Makefile                      # 🏗️ Development commands
└── manifest.json                 # 📦 Agent package manifest
```

## 🔗 Key Links

- **[Project Management System](PROJECT-MANAGEMENT-SYSTEM.md)** - Core accountability framework
- **[Feature Specifications](../specs/features/)** - What we're building
- **[Development Workflow](workflows/development-workflow.md)** - How we build it
- **[Python Environment Spec](technical/python-environment-spec.md)** - uv-based development

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](development/contributing.md) for:

- Code of conduct
- Development setup
- Pull request process
- Code quality standards
- Documentation requirements

## 📞 Support

- **📚 Documentation**: Start with this docs/ directory
- **🐛 Issues**: Report bugs and request features
- **💬 Discussions**: Ask questions and share ideas
- **📧 Contact**: Reach out to the maintainers

---

**Guardian Agents** - Making AI agent orchestration intelligent, automated, and accountable.

*Documentation last updated: 2025-09-11*
