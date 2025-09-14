#!/bin/bash
# Guardian Agents Installation Script
# Installs Guardian Agents system into any GitHub project

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

REPO_URL="https://github.com/kairin/claude-guardian-agents"
INSTALL_DIR=".guardian"

echo -e "${BLUE}🛡️  Guardian Agents Installation${NC}"
echo "Installing into: $(pwd)/$INSTALL_DIR"
echo ""

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo -e "${RED}❌ Error: Must be run from a git repository root${NC}"
    exit 1
fi

# Create installation directory
echo -e "${BLUE}📁 Creating Guardian Agents directory...${NC}"
mkdir -p "$INSTALL_DIR"

# Download or update Guardian Agents
if [ -d "$INSTALL_DIR/.git" ]; then
    echo -e "${YELLOW}🔄 Updating existing Guardian Agents...${NC}"
    cd "$INSTALL_DIR"
    git pull origin main
    cd ..
    cp scripts/generate-manifest.py "$INSTALL_DIR/scripts/generate-manifest.py"
else
    echo -e "${BLUE}📥 Downloading Guardian Agents...${NC}"
    git clone "$REPO_URL" "$INSTALL_DIR"
    cp scripts/generate-manifest.py "$INSTALL_DIR/scripts/generate-manifest.py"
fi

# Create Claude Code integration
echo -e "${BLUE}🔗 Setting up Claude Code integration...${NC}"
mkdir -p ".claude/agents"

# Generate agent index for Claude Code
cd "$INSTALL_DIR"
python3 scripts/generate-manifest.py --claude-index "../.claude/agents/agent-index.json"
cd ..

# Create symlinks to agent categories
echo -e "${BLUE}🔗 Creating agent category links...${NC}"
cd ".claude/agents"

# Link all agent files
ln -sf "../../$INSTALL_DIR/1-product"/* . 2>/dev/null || true
ln -sf "../../$INSTALL_DIR/2-engineering"/* . 2>/dev/null || true
ln -sf "../../$INSTALL_DIR/3-operations"/* . 2>/dev/null || true
ln -sf "../../$INSTALL_DIR/4-thinktank"/* . 2>/dev/null || true

cd ../..

# Create update script
echo -e "${BLUE}📝 Creating update script...${NC}"
cat > "update-guardian-agents.sh" << 'EOF'
#!/bin/bash
# Update Guardian Agents to latest version

cd .guardian
git pull origin main
echo "🛡️ Guardian Agents updated to latest version"

# Regenerate Claude Code index
python3 scripts/generate-manifest.py --claude-index "../.claude/agents/agent-index.json"
echo "🔗 Claude Code integration updated"
EOF

chmod +x "update-guardian-agents.sh"

# Create .gitignore entry
echo -e "${BLUE}📋 Updating .gitignore...${NC}"
if [ -f ".gitignore" ]; then
    if ! grep -q "^\.guardian/$" ".gitignore"; then
        echo "" >> .gitignore
        echo "# Guardian Agents (managed separately)" >> .gitignore
        echo ".guardian/" >> .gitignore
    fi
else
    echo "# Guardian Agents (managed separately)" > .gitignore
    echo ".guardian/" >> .gitignore
fi

# Don't ignore the Claude integration
if grep -q "^\.claude/$" ".gitignore"; then
    sed -i '/^\.claude\/$/d' .gitignore
fi

echo ""
echo -e "${GREEN}✅ Guardian Agents installation complete!${NC}"
echo ""
echo "📋 What was installed:"
echo "  • .guardian/           - Complete Guardian Agents system"
echo "  • .claude/agents/      - Claude Code integration"
echo "  • update-guardian-agents.sh - Update script"
echo ""
echo "🚀 Usage:"
echo "  • Agents are now available in Claude Code"
echo "  • Run ./update-guardian-agents.sh to get latest versions"
echo "  • The .guardian/ directory is git-ignored (managed separately)"
echo ""
echo "🔍 Available agent categories:"
echo "  • Strategy & Product (001-025)"
echo "  • Technical Architecture (041-045)"
echo "  • Development (061-083)"
echo "  • Operations & Security (091-100)"
echo "  • Think-Tank Reasoning (101-108)"
echo ""
