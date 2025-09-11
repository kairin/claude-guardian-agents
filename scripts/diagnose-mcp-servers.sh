#!/bin/bash

# MCP Server Diagnostic Script
# Helps diagnose and resolve ENOENT errors for MCP servers like imagesorcery-mcp

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_header() {
    echo -e "\n${BLUE}=================================${NC}"
    echo -e "${BLUE}  MCP Server Diagnostic Tool     ${NC}"
    echo -e "${BLUE}=================================${NC}\n"
}

check_mcp_server() {
    local server_name=$1
    print_status $YELLOW "🔍 Checking MCP server: $server_name"
    
    # Check if server is in PATH
    if command -v "$server_name" >/dev/null 2>&1; then
        print_status $GREEN "✅ $server_name found in PATH"
        local path=$(which "$server_name")
        print_status $GREEN "   Location: $path"
        return 0
    else
        print_status $RED "❌ $server_name not found in PATH"
        return 1
    fi
}

suggest_installation() {
    local server_name=$1
    
    print_status $YELLOW "\n💡 Installation suggestions for $server_name:"
    
    echo -e "\n${BLUE}1. Node.js/NPM Installation:${NC}"
    echo "   npm install -g $server_name"
    echo "   # or locally:"
    echo "   npm install $server_name"
    
    echo -e "\n${BLUE}2. Python/pip Installation:${NC}"
    echo "   pip install $server_name"
    echo "   # or with pipx:"
    echo "   pipx install $server_name"
    
    echo -e "\n${BLUE}3. Check if it's a local binary:${NC}"
    echo "   find . -name '$server_name' -type f 2>/dev/null"
    echo "   ls -la node_modules/.bin/$server_name"
    
    echo -e "\n${BLUE}4. Add to PATH if installed locally:${NC}"
    echo "   export PATH=\"\$PWD/node_modules/.bin:\$PATH\""
    echo "   # or add to ~/.bashrc:"
    echo "   echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    
    echo -e "\n${BLUE}5. Build from source (if applicable):${NC}"
    echo "   git clone https://github.com/author/$server_name"
    echo "   cd $server_name"
    echo "   npm install && npm run build"
    echo "   # or for Python:"
    echo "   pip install -e ."
}

check_common_locations() {
    local server_name=$1
    
    print_status $YELLOW "\n🔍 Checking common installation locations:"
    
    local locations=(
        "/usr/local/bin/$server_name"
        "/usr/bin/$server_name"
        "$HOME/.local/bin/$server_name"
        "$HOME/bin/$server_name"
        "./node_modules/.bin/$server_name"
        "./$server_name"
    )
    
    for location in "${locations[@]}"; do
        if [ -f "$location" ]; then
            print_status $GREEN "✅ Found at: $location"
            return 0
        fi
    done
    
    print_status $RED "❌ Not found in common locations"
    return 1
}

check_environment() {
    print_status $YELLOW "\n🔍 Environment Information:"
    echo "PATH: $PATH"
    echo "Current directory: $(pwd)"
    
    if command -v node >/dev/null 2>&1; then
        echo "Node.js version: $(node --version)"
    fi
    
    if command -v npm >/dev/null 2>&1; then
        echo "NPM version: $(npm --version)"
    fi
    
    if command -v python3 >/dev/null 2>&1; then
        echo "Python version: $(python3 --version)"
    fi
    
    if command -v pip >/dev/null 2>&1; then
        echo "Pip version: $(pip --version)"
    fi
}

main() {
    print_header
    
    # Get server name from argument or default to imagesorcery-mcp
    local server_name=${1:-"imagesorcery-mcp"}
    
    # Run diagnostics
    check_environment
    
    if ! check_mcp_server "$server_name"; then
        check_common_locations "$server_name"
        suggest_installation "$server_name"
        
        print_status $YELLOW "\n🔧 Quick Fix Commands:"
        echo "# Try these commands to resolve the issue:"
        echo "npm install -g $server_name"
        echo "# or if it's a local project dependency:"
        echo "npm install"
        echo "export PATH=\"\$PWD/node_modules/.bin:\$PATH\""
        
        print_status $RED "\n❌ $server_name is not available. Please install it using one of the suggestions above."
        exit 1
    else
        print_status $GREEN "\n✅ $server_name is properly installed and accessible!"
    fi
}

# Run main function with all arguments
main "$@"