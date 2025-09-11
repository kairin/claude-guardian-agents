# 🚨 Troubleshooting Guide

Complete troubleshooting guide for common issues in Guardian Agents project.

## 🎯 Quick Diagnostics

### **Health Check Commands**
Run these first to identify issues:

```bash
# Overall system health
make validate

# Python environment check
source .venv/bin/activate && python --version

# Dependency verification
uv pip check

# Script functionality test
python scripts/track-progress.py calculate-completion

# File permissions check
ls -la scripts/
```

### **Common Symptoms & Quick Fixes**
| Symptom | Quick Fix | Section |
|---------|-----------|---------|
| `uv: command not found` | Install uv | [uv Installation](#uv-installation-issues) |
| `Permission denied` | Fix permissions | [Permission Issues](#permission-issues) |
| `No module named 'yaml'` | Reinstall dependencies | [Dependency Issues](#dependency-issues) |
| `Progress not updating` | Validate JSON | [Progress Tracking](#progress-tracking-issues) |
| `Reports not generating` | Check file paths | [Report Generation](#report-generation-issues) |

## 🐍 Python Environment Issues

### **uv Installation Issues**

#### **Symptom**: `uv: command not found`
```bash
# Check if uv is installed
which uv

# If not found, install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (Linux/macOS)
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
uv --version
```

#### **Symptom**: `uv` installed but not working
```bash
# Check uv location
which uv
echo $PATH

# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Update shell configuration
source ~/.bashrc  # or ~/.zshrc
```

### **Virtual Environment Issues**

#### **Symptom**: Virtual environment not activating
```bash
# Check if .venv exists
ls -la .venv/

# If missing, recreate environment
rm -rf .venv
uv venv .venv --python 3.11

# Activate environment
source .venv/bin/activate  # Linux/macOS
# or
.\.venv\Scripts\activate   # Windows

# Verify activation
which python
python --version
```

#### **Symptom**: Wrong Python version in environment
```bash
# Check current Python version
python --version

# Recreate with specific version
rm -rf .venv
uv venv .venv --python 3.11

# Reactivate and verify
source .venv/bin/activate
python --version  # Should show 3.11.x
```

### **Dependency Issues**

#### **Symptom**: `No module named 'xyz'`
```bash
# Check installed packages
uv pip list

# Reinstall dependencies
uv pip install -e ".[dev,docs,validation]"

# Verify specific package
python -c "import yaml; print('✅ PyYAML works')"
python -c "import requests; print('✅ Requests works')"
python -c "import rich; print('✅ Rich works')"
```

#### **Symptom**: Dependency conflicts
```bash
# Check for conflicts
uv pip check

# Clear cache and reinstall
uv cache clean
rm -rf .venv
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[dev,docs,validation]"

# Verify resolution
uv pip check
```

#### **Symptom**: Package installation fails
```bash
# Try with verbose output
uv pip install -e ".[dev,docs,validation]" --verbose

# Check for system dependencies
# Ubuntu/Debian:
sudo apt update
sudo apt install build-essential python3-dev

# macOS:
xcode-select --install

# Then retry installation
uv pip install -e ".[dev,docs,validation]"
```

## 🔧 Permission Issues

### **Script Permission Errors**

#### **Symptom**: `Permission denied` when running scripts
```bash
# Fix script permissions
chmod +x scripts/*.sh
chmod +x scripts/*.py

# Verify permissions
ls -la scripts/

# Should show: -rwxr-xr-x for executable scripts
```

#### **Symptom**: Cannot write to tracking directory
```bash
# Check tracking directory permissions
ls -la tracking/

# Fix permissions
chmod 755 tracking/
chmod 644 tracking/progress.json

# Verify write access
touch tracking/test_file && rm tracking/test_file && echo "✅ Write access OK"
```

### **File Access Issues**

#### **Symptom**: Cannot read configuration files
```bash
# Check file existence and permissions
ls -la pyproject.toml
ls -la .python-version
ls -la .pre-commit-config.yaml

# Fix if needed
chmod 644 pyproject.toml .python-version .pre-commit-config.yaml
```

#### **Symptom**: Git hooks not executable
```bash
# Check git hooks
ls -la .git/hooks/

# Install pre-commit hooks
pre-commit install

# Verify hooks
ls -la .git/hooks/pre-commit
```

## 📊 Progress Tracking Issues

### **Progress Data Problems**

#### **Symptom**: Progress not updating
```bash
# Check progress.json file
ls -la tracking/progress.json

# Validate JSON format
python -m json.tool tracking/progress.json

# If corrupted, restore from backup or recreate
cp tracking/progress.json tracking/progress.json.corrupted
python scripts/track-progress.py calculate-completion --force-rebuild
```

#### **Symptom**: Invalid progress data
```bash
# Validate data structure
python -c "
import json
with open('tracking/progress.json') as f:
    data = json.load(f)
    print('✅ Valid JSON')
    print(f'Features: {len(data.get(\"features\", {}))}')
    print(f'Epics: {len(data.get(\"epics\", {}))}')
"

# Reset to default structure if needed
mv tracking/progress.json tracking/progress.json.backup
python scripts/track-progress.py calculate-completion
```

### **Feature Status Issues**

#### **Symptom**: Feature status not changing
```bash
# Check feature exists
python scripts/track-progress.py calculate-completion | grep FEAT-001

# Update status manually
python scripts/track-progress.py update-feature FEAT-001 in_progress "Manual status update"

# Verify update
cat tracking/progress.json | grep -A5 "FEAT-001"
```

#### **Symptom**: Completion percentage wrong
```bash
# Force recalculation
python scripts/track-progress.py calculate-completion --force

# Check specific feature checklist
python -c "
import json
with open('tracking/progress.json') as f:
    data = json.load(f)
    checklist = data['features']['FEAT-001']['implementation_checklist']
    completed = sum(1 for v in checklist.values() if v)
    total = len(checklist)
    print(f'Completed tasks: {completed}/{total} ({completed/total*100:.1f}%)')
"
```

## 📋 Report Generation Issues

### **Report Creation Problems**

#### **Symptom**: Reports not generating
```bash
# Check reports directory
ls -la tracking/reports/

# Create directory if missing
mkdir -p tracking/reports

# Test report generation
python scripts/generate-reports.py weekly --debug

# Check for template issues
python -c "
from scripts.generate_reports import ReportGenerator
gen = ReportGenerator()
progress = gen.load_progress()
print('✅ Progress data loaded')
print(f'Features: {len(progress.get(\"features\", {}))}')
"
```

#### **Symptom**: Empty or malformed reports
```bash
# Check progress data completeness
cat tracking/progress.json | jq '.features | length'
cat tracking/progress.json | jq '.epics | length'

# Regenerate with verbose output
python scripts/generate-reports.py weekly --verbose

# Manually inspect generated report
ls -la tracking/reports/
head -20 tracking/reports/weekly-report-*.md
```

### **Dashboard Issues**

#### **Symptom**: HTML dashboard not working
```bash
# Check HTML generation
python scripts/generate-reports.py blockers

# Verify HTML file
ls -la tracking/reports/blockers-dashboard.html

# Test HTML validity
python -c "
import os
html_file = 'tracking/reports/blockers-dashboard.html'
if os.path.exists(html_file):
    with open(html_file) as f:
        content = f.read()
    if '<html' in content and '</html>' in content:
        print('✅ HTML structure OK')
    else:
        print('❌ HTML structure invalid')
else:
    print('❌ HTML file not found')
"

# Open dashboard in browser (Linux/macOS)
xdg-open tracking/reports/blockers-dashboard.html  # Linux
open tracking/reports/blockers-dashboard.html      # macOS
```

## 🧪 Validation Issues

### **GPM Validation Problems**

#### **Symptom**: GPM validation failing
```bash
# Run detailed validation
python scripts/validate-gmp.py --verbose

# Check manifest file
ls -la manifest.json
python -m json.tool manifest.json

# Regenerate manifest if corrupted
python scripts/generate-manifest.py --validate

# Test specific GPM functions
source scripts/gmp-functions-fixed.sh
find_agent_file "001"
list_available_agents | head -5
```

#### **Symptom**: Agent files not found
```bash
# Check agent directory structure
ls -la agents/
find agents/ -name "*.md" | head -10

# Verify manifest paths
python -c "
import json
with open('manifest.json') as f:
    manifest = json.load(f)
    for agent_id, agent in manifest['agents'].items():
        path = agent['path']
        import os
        if not os.path.exists(path):
            print(f'❌ Missing: {agent_id} -> {path}')
        else:
            print(f'✅ Found: {agent_id}')
        if agent_id == '005':  # Check first few
            break
"
```

### **Quality Check Failures**

#### **Symptom**: `make check` failing
```bash
# Run individual checks
make lint    # Check linting
make test    # Run tests
make format  # Check formatting

# Fix common linting issues
black scripts/ src/ tests/
ruff check --fix scripts/ src/ tests/

# Update pre-commit hooks
pre-commit autoupdate
pre-commit run --all-files
```

#### **Symptom**: Tests not running
```bash
# Check test directory
ls -la tests/

# Create basic test structure if missing
mkdir -p tests
touch tests/__init__.py
echo "def test_basic(): assert True" > tests/test_basic.py

# Run tests with verbose output
pytest tests/ -v

# Check pytest configuration
cat pyproject.toml | grep -A10 "\[tool.pytest"
```

## 🔄 Environment Reset

### **Complete Environment Reset**
When all else fails, reset everything:

```bash
# 1. Clean all artifacts
make clean

# 2. Remove virtual environment
rm -rf .venv

# 3. Clear caches
uv cache clean
rm -rf __pycache__/
find . -name "*.pyc" -delete

# 4. Recreate environment
./scripts/setup-python-env.sh

# 5. Validate installation
make validate
```

### **Partial Reset Options**

#### **Reset only Python environment**
```bash
make env-reset
```

#### **Reset only progress tracking**
```bash
cp tracking/progress.json tracking/progress.json.backup
python scripts/track-progress.py calculate-completion --force-rebuild
```

#### **Reset only reports**
```bash
rm -rf tracking/reports/
make reports
```

## 🔍 Debugging Tips

### **Enable Debug Output**
```bash
# Debug progress tracking
python scripts/track-progress.py calculate-completion --debug

# Debug report generation
python scripts/generate-reports.py weekly --verbose

# Debug GPM validation
python scripts/validate-gmp.py --verbose
```

### **Check Log Files**
```bash
# System logs (if available)
tail -f /tmp/guardian-agents-*.log

# Python errors
python scripts/track-progress.py calculate-completion 2>&1 | tee debug.log
```

### **Inspect Data Structures**
```python
# Interactive debugging
python -c "
import json
from scripts.track_progress import ProgressTracker

tracker = ProgressTracker()
progress = tracker.load_progress()

print('Progress data structure:')
for key in progress.keys():
    print(f'  {key}: {type(progress[key])}')

print(f'Total features: {len(progress.get(\"features\", {}))}')
print(f'Total epics: {len(progress.get(\"epics\", {}))}')
"
```

## 📞 Getting Additional Help

### **Self-Diagnosis Checklist**
Before seeking help, verify:

- [ ] **Environment**: `source .venv/bin/activate && python --version`
- [ ] **Dependencies**: `uv pip check`
- [ ] **Permissions**: `ls -la scripts/` shows executable files
- [ ] **Data integrity**: `python -m json.tool tracking/progress.json`
- [ ] **Basic functionality**: `make validate` passes

### **Information to Collect**
When reporting issues, include:

```bash
# System information
echo "OS: $(uname -a)"
echo "Python: $(python --version)"
echo "uv: $(uv --version)"

# Environment status
echo "Virtual env: $(which python)"
echo "Installed packages: $(uv pip list | wc -l) packages"

# Project status
echo "Progress tracking: $(ls -la tracking/progress.json)"
echo "Recent errors: $(tail -5 debug.log 2>/dev/null || echo 'No debug log')"
```

### **Support Channels**
- **📚 Documentation**: Check complete docs/ directory
- **🔧 Scripts**: Run `make help` for available commands
- **🧪 Validation**: Use `make validate` for health checks
- **📊 Reports**: Generate reports to understand current state

## 💡 Prevention Tips

### **Daily Maintenance**
```bash
# Keep environment healthy
source .venv/bin/activate
uv pip check
make validate
```

### **Weekly Maintenance**
```bash
# Update dependencies
make update-deps

# Clean artifacts
make clean

# Regenerate reports
make reports
```

### **Best Practices**
1. **Always activate environment** before running scripts
2. **Validate changes** with `make check` before commits
3. **Back up progress data** before major changes
4. **Run validation** after updates or installations
5. **Monitor reports** for early issue detection

---

**Troubleshooting Guide** - Resolve common Guardian Agents issues
*Last updated: 2025-09-11*
