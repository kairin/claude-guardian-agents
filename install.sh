#!/bin/bash
# Guardian Package Manager (GPM) - Bootstrap Installer
# Install with: curl -sSL https://raw.githubusercontent.com/kairin/claude-guardian-agents/main/install.sh | bash

set -e

GPM_VERSION="1.0.0"
GPM_REPO="https://github.com/kairin/claude-guardian-agents"
INSTALL_DIR="$HOME/.gpm"
BIN_NAME="gpm"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}🛡️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
    exit 1
}

# Check if running on supported system
check_system() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        OS="windows"
    else
        print_error "Unsupported operating system: $OSTYPE"
    fi
}

# Check dependencies
check_dependencies() {
    if ! command -v curl &> /dev/null; then
        print_error "curl is required but not installed"
    fi

    if ! command -v python3 &> /dev/null; then
        print_warning "python3 not found - some features may be limited"
    fi

    if ! command -v git &> /dev/null; then
        print_warning "git not found - version tracking may be limited"
    fi
}

# Create installation directory
create_install_dir() {
    print_status "Creating installation directory..."
    mkdir -p "$INSTALL_DIR"

    # Create subdirectories
    mkdir -p "$INSTALL_DIR"/{bin,lib,cache,templates}
}

# Download GPM components
download_gpm() {
    print_status "Downloading Guardian Package Manager..."

    # Download main GPM script
    curl -sSL "$GPM_REPO/raw/main/scripts/gpm" -o "$INSTALL_DIR/bin/$BIN_NAME"
    chmod +x "$INSTALL_DIR/bin/$BIN_NAME"

    # Download library files
    curl -sSL "$GPM_REPO/raw/main/scripts/gpm-lib.py" -o "$INSTALL_DIR/lib/gpm-lib.py"

    # Download templates
    curl -sSL "$GPM_REPO/raw/main/templates/agent-index-template.json" -o "$INSTALL_DIR/templates/agent-index.json"
    curl -sSL "$GPM_REPO/raw/main/templates/metadata-template.json" -o "$INSTALL_DIR/templates/metadata.json"
}

# Add to PATH
setup_path() {
    print_status "Setting up PATH..."

    # Detect shell
    SHELL_NAME=$(basename "$SHELL")

    case "$SHELL_NAME" in
        "bash")
            PROFILE="$HOME/.bashrc"
            ;;
        "zsh")
            PROFILE="$HOME/.zshrc"
            ;;
        "fish")
            PROFILE="$HOME/.config/fish/config.fish"
            ;;
        *)
            PROFILE="$HOME/.profile"
            ;;
    esac

    # Add GPM to PATH if not already present
    if ! grep -q "GPM_PATH" "$PROFILE" 2>/dev/null; then
        echo "" >> "$PROFILE"
        echo "# Guardian Package Manager" >> "$PROFILE"
        echo "export GPM_PATH=\"$INSTALL_DIR/bin\"" >> "$PROFILE"
        echo "export PATH=\"\$GPM_PATH:\$PATH\"" >> "$PROFILE"

        print_success "Added GPM to PATH in $PROFILE"
    else
        print_warning "GPM already in PATH"
    fi
}

# Verify installation
verify_installation() {
    print_status "Verifying installation..."

    if [ -f "$INSTALL_DIR/bin/$BIN_NAME" ]; then
        # Test GPM command
        if "$INSTALL_DIR/bin/$BIN_NAME" --version >/dev/null 2>&1; then
            print_success "GPM installed successfully!"
        else
            print_error "GPM installation failed - command not working"
        fi
    else
        print_error "GPM installation failed - binary not found"
    fi
}

# Show post-install instructions
show_instructions() {
    echo ""
    echo -e "${GREEN}🎉 Guardian Package Manager installed successfully!${NC}"
    echo ""
    echo -e "${BLUE}📖 Quick Start:${NC}"
    echo ""
    echo "  1. Restart your terminal or run:"
    echo -e "     ${YELLOW}source $PROFILE${NC}"
    echo ""
    echo "  2. Navigate to your project directory:"
    echo -e "     ${YELLOW}cd your-project/${NC}"
    echo ""
    echo "  3. Initialize Guardian system:"
    echo -e "     ${YELLOW}gpm init${NC}"
    echo ""
    echo "  4. Install all Guardian agents:"
    echo -e "     ${YELLOW}gpm install${NC}"
    echo ""
    echo -e "${BLUE}📚 Documentation:${NC}"
    echo "  https://github.com/kairin/claude-guardian-agents/blob/main/docs/GUARDIAN-PACKAGE-MANAGER.md"
    echo ""
    echo -e "${BLUE}🆘 Support:${NC}"
    echo "  https://github.com/kairin/claude-guardian-agents/issues"
    echo ""
}

# Main installation flow
main() {
    echo -e "${BLUE}"
    echo "┌─────────────────────────────────────────┐"
    echo "│   Guardian Package Manager Installer   │"
    echo "│              Version $GPM_VERSION               │"
    echo "└─────────────────────────────────────────┘"
    echo -e "${NC}"

    check_system
    check_dependencies
    create_install_dir
    download_gpm
    setup_path
    verify_installation
    show_instructions
}

# Check if running directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
