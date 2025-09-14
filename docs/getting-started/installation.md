# 📦 Installation Guide

Complete setup instructions for Guardian Agents with multiple installation methods and platform-specific guidance.

## 🎯 System Requirements

### **Minimum Requirements**
- **Python**: 3.8 or higher (3.11+ recommended)
- **Memory**: 2GB RAM minimum, 4GB recommended
- **Storage**: 1GB free space
- **Network**: Internet connection for package downloads

### **Supported Platforms**
- **Linux**: Ubuntu 20.04+, CentOS 8+, Debian 11+
- **macOS**: macOS 12+ (Monterey)
- **Windows**: Windows 10+ with WSL2 or native PowerShell

### **Required Tools**
- **[uv](https://docs.astral.sh/uv/)** - Python package manager (required)
- **Git** - Version control (required)
- **Make** - Build automation (optional, but recommended)

## 🚀 Installation Methods

### **Method 1: Automated Setup (Recommended)**

The fastest way to get started:

```bash
# Clone repository
git clone <repository-url>
cd claude-guardian-agents

# Run automated setup
./scripts/setup-python-env.sh

# Activate environment
source .venv/bin/activate
```

This method:
- ✅ Installs and configures uv
- ✅ Creates Python virtual environment
- ✅ Installs all dependencies
- ✅ Sets up development tools
- ✅ Configures pre-commit hooks
- ✅ Validates installation

### **Method 2: Manual Setup**

For users who prefer step-by-step control:

#### **Step 1: Install uv**
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Verify uv installation
uv --version
```

#### **Step 2: Clone Repository**
```bash
git clone <repository-url>
cd claude-guardian-agents
```

#### **Step 3: Create Virtual Environment**
```bash
# Create environment with Python 3.11
uv venv .venv --python 3.11

# Activate environment
source .venv/bin/activate  # Linux/macOS
# or
.\.venv\Scripts\activate   # Windows
```

#### **Step 4: Install Dependencies**
```bash
# Install project with all optional dependencies
uv pip install -e ".[dev,docs,validation]"
```

#### **Step 5: Setup Development Tools**
```bash
# Install pre-commit hooks
pre-commit install

# Make scripts executable (Linux/macOS)
chmod +x scripts/*.sh scripts/*.py

# Verify installation
make validate
```

### **Method 3: Development Install**

For contributors and developers:

```bash
# After cloning repository
cd claude-guardian-agents

# Create development environment
make env-create
source .venv/bin/activate

# Install with development dependencies
make dev-install

# Setup development tools
make setup-dev

# Run full validation
make check
```

## 🔧 Platform-Specific Instructions

### **Ubuntu/Debian Linux**

```bash
# Update package list
sudo apt update

# Install required system packages
sudo apt install -y git make build-essential

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc

# Continue with standard installation
git clone <repository-url>
cd claude-guardian-agents
./scripts/setup-python-env.sh
```

### **CentOS/RHEL/Fedora**

```bash
# Install required packages
sudo dnf install -y git make gcc gcc-c++

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc

# Continue with standard installation
git clone <repository-url>
cd claude-guardian-agents
./scripts/setup-python-env.sh
```

### **macOS**

```bash
# Install Xcode command line tools (if not already installed)
xcode-select --install

# Install uv via Homebrew (alternative method)
brew install uv

# Or use curl method
curl -LsSf https://astral.sh/uv/install.sh | sh

# Continue with standard installation
git clone <repository-url>
cd claude-guardian-agents
./scripts/setup-python-env.sh
```

### **Windows**

#### **Option A: WSL2 (Recommended)**
```bash
# Install WSL2 if not already installed
wsl --install

# Inside WSL2, follow Linux instructions
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc

git clone <repository-url>
cd claude-guardian-agents
./scripts/setup-python-env.sh
```

#### **Option B: Native Windows**
```powershell
# Install uv
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Clone repository
git clone <repository-url>
cd claude-guardian-agents

# Create virtual environment
uv venv .venv --python 3.11

# Activate environment
.\.venv\Scripts\activate

# Install dependencies
uv pip install -e ".[dev,docs,validation]"

# Note: Some scripts may require adaptation for Windows
```

## 📋 Installation Verification

After installation, run these commands to verify everything works:

### **Basic Verification**
```bash
# Check Python environment
python --version  # Should show 3.8+

# Check uv installation
uv --version  # Should show uv version

# Check core dependencies
python -c "import yaml, requests, rich, click; print('✅ Core dependencies OK')"

# Check project structure
ls -la  # Should see pyproject.toml, scripts/, docs/, etc.
```

### **Advanced Verification**
```bash
# Run full validation suite
make validate

# Test progress tracking
python scripts/track-progress.py calculate-completion

# Generate test report
python scripts/generate-reports.py weekly

# Run quality checks
make check
```

### **Expected Output**
```
✅ uv is installed: uv 0.1.x
✅ Python environment setup complete
✅ Development tools configured
✅ Installation validation complete
✅ Core dependencies OK
✅ Scripts working correctly
```

## 🔄 Updating Installation

### **Update Guardian Agents**
```bash
# Pull latest changes
git pull origin main

# Update dependencies
uv pip install --upgrade -e ".[dev,docs,validation]"

# Regenerate reports
make reports
```

### **Update uv**
```bash
# Update uv itself
uv self update

# Verify new version
uv --version
```

### **Reset Environment**
```bash
# Complete environment reset
make env-reset

# This will:
# 1. Remove .venv directory
# 2. Recreate virtual environment
# 3. Reinstall all dependencies
# 4. Reconfigure development tools
```

## 🐳 Container Installation (Optional)

For containerized environments:

### **Dockerfile**
```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    make \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN uv venv .venv --python 3.11
RUN . .venv/bin/activate && uv pip install -e ".[dev,docs,validation]"

# Default command
CMD ["/bin/bash"]
```

### **Docker Build**
```bash
# Build image
docker build -t guardian-agents .

# Run container
docker run -it --rm -v $(pwd):/app guardian-agents

# Inside container
source .venv/bin/activate
make validate
```

## 🚨 Troubleshooting Installation

### **Common Issues**

#### **uv not found**
```bash
# Ensure uv is in PATH
echo $PATH | grep -q cargo || echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### **Permission denied on scripts**
```bash
# Fix script permissions
chmod +x scripts/*.sh scripts/*.py
```

#### **Python version conflicts**
```bash
# Force specific Python version
uv venv .venv --python 3.11

# Check available Python versions
uv python list
```

#### **Dependency conflicts**
```bash
# Clear cache and reinstall
uv cache clean
rm -rf .venv
uv venv .venv --python 3.11
uv pip install -e ".[dev,docs,validation]"
```

#### **Make command not found**
```bash
# Install make (Ubuntu/Debian)
sudo apt install make

# Install make (macOS)
xcode-select --install

# Use Python directly if make unavailable
python scripts/track-progress.py calculate-completion
```

### **Getting Help**

If installation fails:

1. **Check logs**: Review error messages carefully
2. **Verify requirements**: Ensure all system requirements are met
3. **Clean install**: Try `make env-reset` for fresh start
4. **Check documentation**: See [troubleshooting guide](../troubleshooting/common-issues.md)
5. **Report issues**: Create issue with detailed error information

## ✅ Installation Success

When installation is complete, you should have:

- ✅ **Python 3.11 environment** in `.venv/`
- ✅ **All dependencies installed** via uv
- ✅ **Scripts executable** and working
- ✅ **Development tools configured** (pre-commit, etc.)
- ✅ **Validation passing** with `make validate`
- ✅ **Progress tracking working** with test reports generated

## 🎯 Next Steps

After successful installation:

1. **[First Steps Tutorial](first-steps.md)** - Learn basic operations
2. **[Project Management Guide](../project-management/progress-tracking.md)** - Understand tracking system
3. **[Development Workflow](../workflows/development-workflow.md)** - Contribute to project
4. **[Script Reference](../tools/README.md#script-reference)** - Master automation tools

---

**Installation Guide** - Complete setup for Guardian Agents
*Last updated: 2025-09-11*
