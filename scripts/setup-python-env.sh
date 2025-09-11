#!/bin/bash
# Guardian Agents Python Environment Setup
# Uses uv for all Python dependency management and virtual environment operations

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BLUE}🐍 Guardian Agents Python Environment Setup${NC}"
echo "Using uv for all Python operations"
echo "Project root: $PROJECT_ROOT"
echo ""

# Check if uv is installed
check_uv() {
    if ! command -v uv &> /dev/null; then
        echo -e "${RED}❌ uv is not installed${NC}"
        echo "Please install uv first:"
        echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
        echo "  or visit: https://docs.astral.sh/uv/getting-started/installation/"
        exit 1
    fi

    echo -e "${GREEN}✅ uv is installed: $(uv --version)${NC}"
}

# Setup Python environment using uv
setup_environment() {
    echo -e "${BLUE}📦 Setting up Python environment with uv...${NC}"

    # Remove any existing .venv to ensure clean setup
    if [ -d ".venv" ]; then
        echo -e "${YELLOW}🗑️  Removing existing .venv directory${NC}"
        rm -rf .venv
    fi

    # Create virtual environment using uv
    echo -e "${BLUE}🏗️  Creating virtual environment...${NC}"
    uv venv .venv --python 3.11

    # Activate virtual environment
    source .venv/bin/activate

    # Install project dependencies
    echo -e "${BLUE}📥 Installing project dependencies...${NC}"
    uv pip install -e ".[dev,docs,validation]"

    echo -e "${GREEN}✅ Python environment setup complete${NC}"
}

# Install development tools
setup_dev_tools() {
    echo -e "${BLUE}🛠️  Setting up development tools...${NC}"

    # Install pre-commit hooks
    if [ -f ".pre-commit-config.yaml" ]; then
        echo "Installing pre-commit hooks..."
        pre-commit install
    fi

    # Make scripts executable
    chmod +x scripts/*.sh
    chmod +x scripts/*.py

    echo -e "${GREEN}✅ Development tools configured${NC}"
}

# Validate installation
validate_installation() {
    echo -e "${BLUE}🧪 Validating installation...${NC}"

    # Check Python version
    python_version=$(python --version)
    echo "Python version: $python_version"

    # Check installed packages
    echo "Key dependencies:"
    python -c "import yaml; print(f'  ✅ PyYAML: {yaml.__version__}')" 2>/dev/null || echo "  ❌ PyYAML not found"
    python -c "import requests; print(f'  ✅ Requests: {requests.__version__}')" 2>/dev/null || echo "  ❌ Requests not found"
    python -c "import rich; print(f'  ✅ Rich: {rich.__version__}')" 2>/dev/null || echo "  ❌ Rich not found"
    python -c "import click; print(f'  ✅ Click: {click.__version__}')" 2>/dev/null || echo "  ❌ Click not found"

    # Test scripts
    echo ""
    echo "Testing core scripts:"
    if python scripts/track-progress.py calculate-completion &>/dev/null; then
        echo "  ✅ track-progress.py working"
    else
        echo "  ❌ track-progress.py has issues"
    fi

    if python scripts/generate-reports.py --help &>/dev/null; then
        echo "  ✅ generate-reports.py working"
    else
        echo "  ❌ generate-reports.py has issues"
    fi

    echo -e "${GREEN}✅ Installation validation complete${NC}"
}

# Create development workflow helpers
create_dev_helpers() {
    echo -e "${BLUE}📝 Creating development workflow helpers...${NC}"

    # Create Makefile for common tasks
    cat > Makefile << 'EOF'
# Guardian Agents Development Makefile
# All Python operations use uv

.PHONY: help install dev-install test lint format check clean reports validate

# Default target
help:
	@echo "Guardian Agents Development Commands (using uv)"
	@echo ""
	@echo "Setup:"
	@echo "  install     Install project dependencies"
	@echo "  dev-install Install with development dependencies"
	@echo ""
	@echo "Development:"
	@echo "  test        Run test suite"
	@echo "  lint        Run linting checks"
	@echo "  format      Format code"
	@echo "  check       Run all quality checks"
	@echo ""
	@echo "Project Management:"
	@echo "  reports     Generate all project reports"
	@echo "  validate    Run project validation"
	@echo "  track       Update progress tracking"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean       Clean build artifacts"
	@echo "  update-deps Update dependencies"

# Installation targets
install:
	uv pip install -e .

dev-install:
	uv pip install -e ".[dev,docs,validation]"

# Development targets
test:
	pytest tests/ -v --cov=src --cov-report=term-missing

lint:
	ruff check src/ scripts/ tests/
	mypy src/ scripts/

format:
	black src/ scripts/ tests/
	ruff check --fix src/ scripts/ tests/

check: lint test
	@echo "All quality checks passed!"

# Project management targets
reports:
	python scripts/generate-reports.py all

validate:
	python scripts/validate-gpm.py
	python scripts/track-progress.py calculate-completion

track:
	python scripts/track-progress.py calculate-completion
	python scripts/generate-reports.py weekly

# Maintenance targets
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

update-deps:
	uv pip install --upgrade -e ".[dev,docs,validation]"

# Environment management
env-create:
	uv venv .venv --python 3.11

env-activate:
	@echo "Run: source .venv/bin/activate"

env-reset: clean
	rm -rf .venv
	$(MAKE) env-create
	uv pip install -e ".[dev,docs,validation]"
EOF

    # Create uv-specific activation helper
    cat > activate-env.sh << 'EOF'
#!/bin/bash
# Guardian Agents Environment Activation Helper
# Ensures uv virtual environment is properly activated

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$PROJECT_ROOT/.venv" ]; then
    echo "❌ Virtual environment not found. Run: ./scripts/setup-python-env.sh"
    exit 1
fi

source "$PROJECT_ROOT/.venv/bin/activate"
echo "✅ Guardian Agents environment activated (using uv)"
echo "Python: $(python --version)"
echo "Location: $(which python)"
EOF

    chmod +x activate-env.sh

    echo -e "${GREEN}✅ Development helpers created${NC}"
}

# Main execution
main() {
    echo "Starting Guardian Agents Python environment setup..."

    check_uv
    setup_environment
    setup_dev_tools
    validate_installation
    create_dev_helpers

    echo ""
    echo -e "${GREEN}🎉 Setup complete!${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Activate environment: source .venv/bin/activate"
    echo "  2. Or use helper:        source activate-env.sh"
    echo "  3. Run tests:           make test"
    echo "  4. Generate reports:    make reports"
    echo "  5. View all commands:   make help"
    echo ""
    echo -e "${BLUE}All Python operations will use uv for dependency management${NC}"
}

# Run main function
main "$@"
