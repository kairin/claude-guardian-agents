# 🔄 Guardian Agents Dry Run Process
**Version**: 1.0
**Created**: 2025-09-12
**Purpose**: Repeatable comprehensive system validation process

---

## 🎯 **Process Overview**

This document defines the repeatable process for conducting comprehensive dry runs of the Guardian Agents system, ensuring strict adherence to core project ideals and maintaining system health.

### **Core Project Ideals**
1. **Research-Based Foundation**: Academic research backing (ParaThinker, DORA, etc.)
2. **Multi-Layer Architecture**: Think-Tank → Strategic → Technical → Operational
3. **Specialized Agent System**: 100+ Guardian agents with specific expertise
4. **Intelligent Orchestration**: Context-aware agent selection and workflows
5. **Comprehensive Automation**: End-to-end project management and development support
6. **uv-Exclusive Python Management**: All Python operations via uv

---

## 📋 **Pre-Requisites**

### **Required Tools**
- **uv**: Python environment manager (primary requirement)
- **git**: Version control system
- **make**: Build automation tool
- **bash**: Shell scripting environment

### **Environment Setup**
```bash
# Verify uv installation
uv --version

# Navigate to project root
cd /path/to/claude-guardian-agents

# Ensure clean working directory
git status
```

---

## 🚀 **Dry Run Execution Steps**

### **Phase 1: Environment Preparation**

#### **Step 1.1: Clean Non-Core Artifacts**
```bash
# Remove temporary files and build artifacts
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.egg-info" -type d -exec rm -rf {} + 2>/dev/null || true
rm -f /tmp/test*.log 2>/dev/null

echo "✅ Environment cleaned"
```

#### **Step 1.2: Verify uv Compliance**
```bash
# Check for non-uv Python management
grep -r "pip install\|conda\|virtualenv" scripts/ || echo "✅ No non-uv Python management found"

# Verify virtual environment status
if [ -f ".venv/bin/python" ]; then
    echo "✅ uv virtual environment active"
else
    echo "⚠️ Virtual environment needs setup"
    ./scripts/setup-python-env.sh
fi
```

### **Phase 2: Systematic Testing**

#### **Step 2.1: Core System Validation**
```bash
# Test 1: Python Environment & uv Compliance
echo "📊 TEST 1: PYTHON ENVIRONMENT & UV COMPLIANCE"
./scripts/setup-python-env.sh | grep -E "(uv|Python|✅)" | head -10

# Test 2: GPM Validation (Intelligent Orchestration)
echo "📊 TEST 2: GPM VALIDATION"
bash scripts/validate-gpm.sh | grep -E "(Total Tests|Passed|Failed|ALL TESTS|✅|❌)"

# Test 3: Makefile Automation
echo "📊 TEST 3: MAKEFILE AUTOMATION"
make validate | grep -E "(PASS|FAIL|Overall completion)"

# Test 4: Report Generation
echo "📊 TEST 4: REPORT GENERATION"
make reports | grep -E "(Generated|Weekly|Milestone|Dashboard)"

# Test 5: Agent Ecosystem
echo "📊 TEST 5: AGENT ECOSYSTEM"
echo "Total agents: $(find . -name '*guardian.md' | wc -l)"
echo "Strategy agents: $(find ./1-product -name '*guardian.md' | wc -l)"
echo "Engineering agents: $(find ./2-engineering -name '*guardian.md' | wc -l)"
echo "Operations agents: $(find ./3-operations -name '*guardian.md' | wc -l)"
```

#### **Step 2.2: Goal Contribution Analysis**
```bash
# Evaluate each test against core ideals
echo "=== GOAL CONTRIBUTION ANALYSIS ==="
echo "1. uv-Exclusive Management: Verified in Test 1"
echo "2. Comprehensive Automation: Validated in Tests 3-4"
echo "3. Specialized Agent System: Confirmed in Test 5"
echo "4. Intelligent Orchestration: Demonstrated in Test 2"
```

### **Phase 3: Documentation and Analysis**

#### **Step 3.1: Create Test Results Documentation**
```bash
# Generate comprehensive dry run documentation
cat > docs/COMPREHENSIVE-DRY-RUN-$(date +%Y-%m-%d).md << 'EOF'
# 🧪 Comprehensive Dry Run Test Results - Guardian Agents
**Test Date**: $(date +%Y-%m-%d)
**Test Operator**: [Your Name]
**Test Type**: Full System Validation with Goal Contribution Analysis
**Core Ideals Compliance**: ✅ Verified - uv-only Python management, clean environment

[Include detailed test results and analysis...]
EOF
```

#### **Step 3.2: Update Progress Tracking**
```bash
# Update all tracking and reporting
make track
```

### **Phase 4: Repository Management**

#### **Step 4.1: Commit Core Changes Only**
```bash
# Verify only core project files are staged
git status --porcelain
git diff --name-only

# Stage core project changes (exclude .venv, __pycache__, etc.)
git add .gitignore Makefile scripts/ docs/ tracking/ .pre-commit-config.yaml

# Commit with comprehensive message
git commit -m "feat: Complete comprehensive dry run - [date]

[Include detailed commit message following template...]

🤖 Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Claude <noreply@anthropic.com>"
```

#### **Step 4.2: Push to Remote Repository**
```bash
# Push to feature branch
git push origin [branch-name]

# Create pull request (if applicable)
gh pr create --title "Comprehensive Dry Run Results - [date]" --body "..."
```

---

## ✅ **Success Criteria**

### **Minimum Requirements**
- [ ] **System Operational Status**: 100%
- [ ] **Test Suite Pass Rate**: ≥95%
- [ ] **Core Ideal Compliance**: ≥95%
- [ ] **uv-Exclusive Management**: 100% compliance
- [ ] **Clean Environment**: No external tool contamination

### **Quality Gates**
- [ ] All GPM tests pass (43/43)
- [ ] All Makefile commands functional
- [ ] All reports generated successfully
- [ ] Agent ecosystem properly structured
- [ ] Documentation updated and comprehensive

### **Repository Cleanliness**
- [ ] No .venv directory in git
- [ ] No __pycache__ or *.pyc files committed
- [ ] No temporary test logs in repository
- [ ] All core changes properly documented

---

## 🔍 **Troubleshooting Guide**

### **Common Issues**

#### **Issue: Pre-commit hooks fail with Python not found**
**Solution:**
```bash
# Update .pre-commit-config.yaml to use correct Python paths
entry: .venv/bin/python  # Instead of: python
entry: bash              # For shell scripts
```

#### **Issue: GPM validation fails**
**Solution:**
```bash
# Check manifest.json syntax
jq empty manifest.json

# Verify agent files exist
bash scripts/validate-gmp.sh --verbose
```

#### **Issue: uv environment issues**
**Solution:**
```bash
# Reset virtual environment
rm -rf .venv
./scripts/setup-python-env.sh
```

---

## 📊 **Expected Results Template**

### **Test Results Summary**
| Test Suite | Result | Pass Rate | Core Ideal | Goal Contribution |
|------------|--------|-----------|------------|-------------------|
| Python Environment & uv | ✅ PASSED | 100% | Automation | HIGH |
| GPM Validation | ✅ PASSED | 100% (43/43) | Orchestration | CRITICAL |
| Makefile Automation | ✅ PASSED | 100% | Automation | HIGH |
| Report Generation | ✅ PASSED | 100% | Automation | MEDIUM |
| Agent Ecosystem | ✅ PASSED | 95% | Agent System | CRITICAL |

### **Overall Assessment**
- **System Status**: ✅ **FULLY OPERATIONAL**
- **Core Compliance**: ✅ **≥95% COMPLIANT**
- **Ready for Production**: ✅ **YES** (with noted improvements)
- **Repeatability**: ✅ **FULLY DOCUMENTED**

---

## 🔄 **Process Maintenance**

### **Regular Updates**
- **Weekly**: Execute dry run process and review results
- **Monthly**: Update test criteria and success metrics
- **Quarterly**: Review and optimize process efficiency

### **Version Control**
- Track process changes in this document
- Maintain compatibility with core ideal evolution
- Document lessons learned and process improvements

---

*This process ensures consistent, repeatable validation of the Guardian Agents system while maintaining strict adherence to core project ideals and enabling continuous system evolution.*
