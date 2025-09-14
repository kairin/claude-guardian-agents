# 🛠️ Script Reference

Complete reference for all automation scripts in the Guardian Agents project.

## 📋 Script Overview

Guardian Agents includes powerful automation scripts for project management, progress tracking, and system validation. All scripts use `uv` for Python dependency management.

### **Core Scripts**
- [`track-progress.py`](#track-progresspy) - Progress tracking and management
- [`generate-reports.py`](#generate-reportspy) - Automated report generation
- [`validate-gpm.py`](#validate-gpmpy) - GPM system validation
- [`setup-python-env.sh`](#setup-python-envsh) - Environment setup
 - [Guardian Package Manager](guardian-package-manager.md) - Design and usage for GPM

### **Utility Scripts**
- [`generate-manifest.py`](#generate-manifestpy) - Manifest generation
- [`gmp-functions-fixed.sh`](#gmp-functions-fixedsh) - GPM function library

## 📊 track-progress.py

**Purpose**: Comprehensive progress tracking and project management

### **Usage**
```bash
python scripts/track-progress.py <command> [args...]
```

### **Commands**

#### **calculate-completion**
Calculate overall and per-epic completion percentages
```bash
python scripts/track-progress.py calculate-completion

# Output:
# Overall completion: 23.0%
# Features: 2/10
# Epic EPIC-001: 0.0%
```

#### **update-feature**
Update feature status with optional notes
```bash
python scripts/track-progress.py update-feature FEAT-001 in_progress "Starting development"

# Parameters:
# - feature_id: Feature identifier (e.g., FEAT-001)
# - status: not_started|in_progress|blocked|ready_for_review|completed|cancelled
# - notes: Optional description of update
```

#### **complete-task**
Mark individual task as completed in feature checklist
```bash
python scripts/track-progress.py complete-task FEAT-001 requirements_analysis

# Parameters:
# - feature_id: Feature identifier
# - task_name: Task from implementation_checklist
```

#### **generate-blockers**
Identify and report current project blockers
```bash
python scripts/track-progress.py generate-blockers

# Output:
# Current blockers:
#   - dependency: GPM_VALIDATION_COMPLETE
#   - resource: FEAT-003 needs assignment
```

#### **validate**
Run automated validation for specific feature
```bash
python scripts/track-progress.py validate FEAT-001

# Output:
# Validation results for FEAT-001: criteria_failed
# - System analyzes project structure: ❌ Not implemented
# - Agent selection accuracy >= 90%: ❌ Not tested
```

### **Implementation Details**

#### **Core Classes**
```python
class ProgressTracker:
    def __init__(self, project_root: str = None):
        """Initialize tracker with project root directory"""

    def load_progress(self) -> Dict:
        """Load current progress data from progress.json"""

    def save_progress(self, progress_data: Dict) -> None:
        """Save progress data with timestamp"""

    def update_feature_status(self, feature_id: str, status: str, notes: str = None):
        """Update feature status with audit trail"""

    def calculate_completion_percentage(self) -> Dict:
        """Calculate completion rates for project and epics"""
```

#### **Data Model**
```python
# Progress tracking data structure
{
    "project_status": {
        "overall_completion": int,      # 0-100 percentage
        "last_updated": str,            # ISO timestamp
        "phase": str                    # Current project phase
    },
    "epics": {
        "EPIC-001": {
            "completion_percentage": int,
            "features": List[str],
            "success_metrics": Dict
        }
    },
    "features": {
        "FEAT-001": {
            "status": str,                      # Feature status
            "completion_percentage": int,       # Auto-calculated
            "implementation_checklist": Dict,   # Task completion tracking
            "validation_criteria": List[str]    # Acceptance criteria
        }
    }
}
```

### **Makefile Integration**
```bash
# Quick progress check
make track

# Equivalent to:
# python scripts/track-progress.py calculate-completion
# python scripts/generate-reports.py weekly
```

## 📋 generate-reports.py

**Purpose**: Automated generation of project reports and dashboards

### **Usage**
```bash
python scripts/generate-reports.py <command> [args...]
```

### **Commands**

#### **weekly**
Generate weekly progress report
```bash
python scripts/generate-reports.py weekly

# Creates: tracking/reports/weekly-report-YYYY-MM-DD.md
# Contains:
# - Overall progress summary
# - Epic status breakdown
# - Feature implementation status
# - Week's accomplishments
# - Next week's priorities
# - Current blockers
```

#### **milestone**
Generate comprehensive milestone report
```bash
python scripts/generate-reports.py milestone "Sprint 1"

# Parameters:
# - milestone_name: Optional milestone identifier
#
# Creates: tracking/reports/milestone-report-sprint-1.md
# Contains:
# - Executive summary
# - Epic completion analysis
# - Feature implementation details
# - Risk assessment
# - Strategic recommendations
```

#### **blockers**
Generate real-time blockers dashboard
```bash
python scripts/generate-reports.py blockers

# Creates:
# - tracking/reports/blockers-dashboard.md (text)
# - tracking/reports/blockers-dashboard.html (interactive)
#
# Contains:
# - Critical blockers requiring immediate attention
# - All active blockers with priority levels
# - Dependency status monitoring
# - Resource allocation recommendations
```

#### **all**
Generate all report types
```bash
python scripts/generate-reports.py all

# Equivalent to running:
# generate-reports.py weekly
# generate-reports.py milestone
# generate-reports.py blockers
```

### **Report Templates**

#### **Weekly Report Structure**
```markdown
# Weekly Progress Report - Week of YYYY-MM-DD

## 📊 Overall Progress
- Project Completion: XX%
- Current Phase: implementation_planning

## 🎯 Epic Status
### EPIC-001: Intelligent Agent Orchestration
- Status: In Progress
- Completion: XX%
- Features: X total

## 🚀 Feature Progress
| Feature ID | Title | Status | Progress | Epic |
|------------|-------|--------|----------|------|

## ✅ This Week's Accomplishments
- Completed items...

## 🚨 Blockers & Issues
- Current blockers...

## 📅 Next Week's Priorities
- Upcoming priorities...
```

#### **Interactive Dashboard Features**
```html
<!-- HTML dashboard includes -->
- Real-time auto-refresh every 5 minutes
- Color-coded priority indicators
- Interactive status cards
- Responsive design for all devices
- Export functionality for sharing
```

### **Customization**

#### **Custom Report Templates**
```python
# Extend ReportGenerator for custom formats
class CustomReportGenerator(ReportGenerator):
    def generate_executive_summary(self) -> str:
        """Custom executive report format"""
        progress = self.load_progress()

        # Custom report logic
        return formatted_report
```

#### **Report Scheduling**
```bash
# Add to crontab for automated generation
0 9 * * 1 cd /path/to/guardian-agents && python scripts/generate-reports.py weekly
0 17 * * 5 cd /path/to/guardian-agents && python scripts/generate-reports.py milestone
```

## ✅ validate-gpm.py

**Purpose**: Comprehensive GPM (Guardian Package Manager) system validation

### **Usage**
```bash
python scripts/validate-gpm.py [--verbose] [--fix]
```

### **Options**
- `--verbose`: Detailed validation output with diagnostic information
- `--fix`: Attempt to automatically fix detected issues

### **Validation Checks**

#### **Manifest Validation**
```bash
# Tests performed:
✅ Manifest file exists and is readable
✅ Manifest JSON format is valid
✅ All 45 agents have manifest entries
✅ Agent file paths are correct
✅ Checksums match actual files
✅ Download URLs are accessible
```

#### **Agent Discovery**
```bash
# Tests performed:
✅ Agent directory structure is correct
✅ All agent files are present
✅ Agent metadata is complete
✅ Agent descriptions are properly formatted
```

#### **Function Library**
```bash
# Tests performed:
✅ GPM functions are implemented (not placeholder)
✅ Agent lookup functions work correctly
✅ Download simulation succeeds
✅ Installation validation passes
```

### **Example Output**
```
🧪 Guardian Package Manager (GPM) Validation

📦 Manifest Validation
✅ Manifest file exists: manifest.json
✅ Valid JSON format
✅ Contains 45 agents (expected: 45)
✅ All agent paths exist
✅ All checksums valid

🔍 Agent Discovery
✅ Found 45 agent files
✅ All agents have valid metadata
✅ No missing descriptions

🛠️ Function Library
✅ find_agent_file() working correctly
✅ download_agent() simulation successful
✅ install_agent() validation passed

📊 Validation Summary
✅ 42/43 tests passed (97% success rate)
❌ 1 test failed: Network connectivity check

Overall Status: ✅ VALIDATION PASSED
```

### **Error Resolution**
```bash
# Common fixes available with --fix flag:
- Regenerate manifest.json with correct paths
- Update checksums for modified files
- Fix file permissions on scripts
- Validate and repair JSON formatting
```

## 🚀 setup-python-env.sh

**Purpose**: Automated Python environment setup using uv exclusively

### **Usage**
```bash
./scripts/setup-python-env.sh
```

### **Setup Process**

#### **Phase 1: Verification**
```bash
# Checks performed:
✅ uv installation verification
✅ Python 3.8+ availability
✅ Git installation check
✅ System requirements validation
```

#### **Phase 2: Environment Creation**
```bash
# Actions performed:
🗑️ Remove existing .venv (if present)
🏗️ Create new virtual environment with Python 3.11
📦 Activate virtual environment
📥 Install project dependencies with uv
```

#### **Phase 3: Development Tools**
```bash
# Tools configured:
🔧 Install pre-commit hooks
📝 Create Makefile with uv commands
✅ Make scripts executable
🧪 Set up validation framework
```

#### **Phase 4: Validation**
```bash
# Installation verification:
✅ Python version check
✅ Core dependency verification
✅ Script functionality testing
✅ Development tool configuration
```

### **Generated Files**
```bash
# Files created during setup:
.venv/                  # Virtual environment
Makefile               # Development commands
activate-env.sh        # Environment activation helper
.pre-commit-config.yaml # Quality automation (if not exists)
```

### **Platform Support**
- **Linux**: Ubuntu 20.04+, CentOS 8+, Debian 11+
- **macOS**: macOS 12+ with Homebrew or curl installation
- **Windows**: WSL2 recommended, native PowerShell supported

## 📦 generate-manifest.py

**Purpose**: Generate accurate manifest.json from repository structure

### **Usage**
```bash
python scripts/generate-manifest.py [--output manifest.json] [--validate]
```

### **Options**
- `--output`: Specify output file (default: manifest.json)
- `--validate`: Validate generated manifest after creation

### **Generation Process**
```python
# Manifest generation algorithm:
1. Scan agents/ directory for all guardian agents
2. Extract metadata from each agent file
3. Calculate SHA-256 checksums
4. Generate download URLs
5. Create JSON manifest with proper formatting
6. Validate generated manifest integrity
```

### **Manifest Schema**
```json
{
  "package_manager": "gpm",
  "version": "1.0.0",
  "repository": "claude-guardian-agents",
  "agents": {
    "001": {
      "name": "Help Me Plan Guardian",
      "path": "agents/001-help-me-plan/guardian.md",
      "description": "Strategic planning and task breakdown agent",
      "checksum": "sha256:abc123...",
      "download_url": "https://example.com/agents/001-help-me-plan/guardian.md",
      "version": "1.0.0",
      "capabilities": ["planning", "strategy", "analysis"],
      "last_updated": "2025-09-11T00:00:00Z"
    }
  },
  "metadata": {
    "total_agents": 45,
    "generated": "2025-09-11T00:00:00Z"
  }
}
```

## 🔧 gmp-functions-fixed.sh

**Purpose**: Core GPM function library with working implementations

### **Usage**
```bash
# Source the functions
source scripts/gmp-functions-fixed.sh

# Use GPM functions
find_agent_file "001"
download_agent "001" "/tmp/"
install_agent "001"
```

### **Available Functions**

#### **find_agent_file()**
```bash
find_agent_file() {
    local agent_id="$1"
    # Returns actual file path from manifest
    echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"].path"
}

# Usage:
path=$(find_agent_file "001")
echo "Agent 001 located at: $path"
```

#### **download_agent()**
```bash
download_agent() {
    local agent_id="$1"
    local destination="$2"
    # Simulates agent download process
    # Returns success/failure status
}

# Usage:
if download_agent "001" "/tmp/agents/"; then
    echo "Download successful"
fi
```

#### **install_agent()**
```bash
install_agent() {
    local agent_id="$1"
    # Validates agent and marks as installed
    # Updates local agent registry
}

# Usage:
install_agent "001" && echo "Agent 001 installed"
```

#### **list_available_agents()**
```bash
list_available_agents() {
    # Lists all agents from manifest
    echo "$MANIFEST_DATA" | jq -r '.agents | keys[]'
}

# Usage:
list_available_agents | head -5
```

### **Error Handling**
```bash
# All functions include comprehensive error handling:
- Input validation
- Manifest data verification
- Network connectivity checks
- File system permission validation
- Atomic operations with rollback
```

## 🎯 Script Best Practices

### **Common Usage Patterns**

#### **Daily Development Workflow**
```bash
# Morning standup preparation
make track                    # Check overnight progress
make reports                  # Generate status reports

# During development
python scripts/track-progress.py update-feature FEAT-001 in_progress "Working on requirements"
python scripts/track-progress.py complete-task FEAT-001 requirements_analysis

# End of day
make validate                 # Ensure quality standards
python scripts/generate-reports.py weekly  # Update progress
```

#### **Weekly Project Review**
```bash
# Generate comprehensive reports
python scripts/generate-reports.py milestone "Week 12"
python scripts/generate-reports.py blockers

# Validate system health
python scripts/validate-gpm.py --verbose
make check
```

#### **Release Preparation**
```bash
# Pre-release validation
make validate
python scripts/validate-gpm.py --fix
python scripts/generate-reports.py milestone "Release 1.0"

# Update documentation
python scripts/generate-manifest.py --validate
make reports
```

### **Error Handling**

#### **Script Debugging**
```bash
# Run scripts with debug output
python scripts/track-progress.py calculate-completion --debug
python scripts/generate-reports.py weekly --verbose

# Check script logs
tail -f /tmp/guardian-agents-*.log
```

#### **Common Issues**
```bash
# Permission errors
chmod +x scripts/*.sh scripts/*.py

# Python environment issues
source .venv/bin/activate
uv pip check

# Data corruption
cp tracking/progress.json tracking/progress.json.backup
python scripts/track-progress.py calculate-completion --force-rebuild
```

## 📊 Performance Considerations

### **Script Performance**
- **track-progress.py**: < 1 second for status updates
- **generate-reports.py**: < 5 seconds for full report generation
- **validate-gmp.py**: < 10 seconds for complete validation
- **setup-python-env.sh**: < 120 seconds for full environment setup

### **Optimization Tips**
```bash
# Cache manifest data for repeated operations
export MANIFEST_CACHE_ENABLED=true

# Use parallel validation for large feature sets
python scripts/validate-gpm.py --parallel

# Enable incremental report generation
python scripts/generate-reports.py weekly --incremental
```

## 🔗 Integration Examples

### **CI/CD Integration**
```yaml
# GitHub Actions example
- name: Update Progress
  run: |
    python scripts/track-progress.py calculate-completion
    python scripts/generate-reports.py weekly

- name: Validate System
  run: |
    python scripts/validate-gpm.py
    make check
```

### **IDE Integration**
```json
// VS Code tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Track Progress",
      "type": "shell",
      "command": "python",
      "args": ["scripts/track-progress.py", "calculate-completion"],
      "group": "build"
    }
  ]
}
```

### **Git Hooks**
```bash
#!/bin/sh
# .git/hooks/post-commit
# Auto-update progress after commits

python scripts/track-progress.py calculate-completion
python scripts/generate-reports.py weekly
```

## 📞 Support

### **Getting Help**
```bash
# Script help
python scripts/track-progress.py --help
python scripts/generate-reports.py --help

# System diagnostics
make validate
python scripts/validate-gmp.py --verbose

# Environment debugging
source activate-env.sh
uv pip check
```

### **Common Commands Reference**
```bash
# Quick reference card
make help                     # All available commands
make track                    # Update progress
make reports                  # Generate reports
make validate                 # System validation
make check                    # Quality checks
make clean                    # Clean build artifacts
```

---

**Script Reference** - Complete automation toolkit for Guardian Agents
*Last updated: 2025-09-11*
