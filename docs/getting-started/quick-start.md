# 🚀 Quick Start Guide

Get Guardian Agents running in under 5 minutes!

## 🎯 Prerequisites

Before starting, ensure you have:
- **Python 3.13+** (Ubuntu 25.04 built-in, required for compatibility)
- **[uv](https://docs.astral.sh/uv/)** - Modern Python package manager (UV only)
- **Git** - For repository cloning

### Install uv (if not already installed)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Verify installation
uv --version
```

## ⚡ 30-Second Setup

```bash
# 1. Clone repository
git clone <your-repository-url>
cd claude-guardian-agents

# 2. Automated setup (handles everything)
./scripts/setup-python-env.sh

# 3. Activate environment
source .venv/bin/activate
# Or use: source activate-env.sh

# 4. Verify installation
make validate
```

**That's it!** 🎉 Guardian Agents is now ready to use.

## 🧪 Test Drive

Try these commands to explore the system:

### **Generate Your First Report**
```bash
make reports
# Creates: tracking/reports/weekly-report-YYYY-MM-DD.md
```

### **Check Project Status**
```bash
make track
# Shows: Overall completion, feature status, blockers
```

### **View All Available Commands**
```bash
make help
# Lists: All development and management commands
```

### **Run Quality Checks**
```bash
make check
# Runs: Linting, type checking, and tests
```

## 📊 Understanding Your Setup

After setup, you'll have:

### **Project Structure**
```
claude-guardian-agents/
├── .venv/              # uv-managed Python environment
├── tracking/           # Progress tracking data
│   ├── progress.json   # Current project status
│   └── reports/        # Generated reports
├── scripts/            # Automation tools
└── docs/               # This documentation
```

### **Key Files Created**
- **`.venv/`** - Virtual environment (Python 3.13)
- **`Makefile`** - Development commands
- **`tracking/progress.json`** - Project status data
- **`activate-env.sh`** - Environment activation helper

## 🎮 Try These Examples

### **1. Track a Feature**
```bash
# Update feature status
python scripts/track-progress.py update-feature FEAT-001 in_progress "Starting implementation"

# Complete a task
python scripts/track-progress.py complete-task FEAT-001 requirements_analysis

# Check completion
python scripts/track-progress.py calculate-completion
```

### **2. Generate Reports**
```bash
# Weekly progress report
python scripts/generate-reports.py weekly

# Milestone report
python scripts/generate-reports.py milestone "Sprint 1"

# Real-time dashboard
python scripts/generate-reports.py blockers
```

### **3. Validate System**
```bash
# Validate GPM system
python scripts/validate-gpm.sh

# Check all dependencies
uv pip check

# Run full test suite
make test
```

## 🔧 Common Next Steps

### **For Developers**
1. **Explore Agents**: Check out `agents/` directory
2. **Read Specs**: Review `specs/features/` for upcoming work
3. **Set Up IDE**: Configure your editor with Python tools
4. **Install Pre-commit**: `pre-commit install` for quality gates

### **For Project Managers**
1. **Review Progress**: Open `tracking/progress.json`
2. **Check Reports**: View generated reports in `tracking/reports/`
3. **Understand Features**: Read feature specs in `specs/features/`
4. **Track Milestones**: Use milestone report generation

### **For Contributors**
1. **Read Contributing Guide**: See `docs/development/contributing.md`
2. **Check Quality Standards**: Review `docs/development/code-quality.md`
3. **Understand Workflow**: Study `docs/workflows/development-workflow.md`
4. **Set Up Development Tools**: Follow Python environment spec

## 🚨 Troubleshooting Quick Fixes

### **Environment Issues**
```bash
# Reset environment completely
make env-reset

# Just recreate virtual environment
rm -rf .venv
uv venv .venv --python 3.11
uv pip install -e ".[dev,docs,validation]"
```

### **Permission Errors**
```bash
# Fix script permissions
chmod +x scripts/*.sh scripts/*.py
```

### **Missing Dependencies**
```bash
# Update all dependencies
make update-deps

# Check for conflicts
uv pip check
```

### **Validation Failures**
```bash
# Clean and rebuild
make clean
make dev-install
make validate
```

## 📖 What's Next?

Now that you're set up, explore:

1. **[Installation Guide](installation.md)** - Detailed setup options
2. **[First Steps Tutorial](first-steps.md)** - Guided walkthrough
3. **[Project Management System](../project-management/README.md)** - Core framework
4. **[Development Workflow](../workflows/development-workflow.md)** - How we work

## 💡 Pro Tips

- **Use `make help`** to see all available commands
- **Activate environment** with `source activate-env.sh` for convenience
- **Generate reports regularly** to track progress
- **Use pre-commit hooks** to maintain code quality
- **Check `tracking/progress.json`** for current status

## 🤝 Need Help?

- **📚 Full Documentation**: Browse `docs/` directory
- **🐛 Issues**: Check `docs/troubleshooting/common-issues.md`
- **💬 Questions**: See `docs/troubleshooting/faq.md`
- **📞 Support**: Contact maintainers via repository issues

---

**🎉 Congratulations!** Guardian Agents is ready for your intelligent agent orchestration needs.

*Quick Start Guide - Last updated: 2025-09-11*
