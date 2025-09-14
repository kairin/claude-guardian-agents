#!/bin/bash
# Update Guardian Agents to latest version

cd .guardian
git pull origin main
echo "🛡️ Guardian Agents updated to latest version"

# Regenerate Claude Code index
python3 scripts/generate-manifest.py --claude-index "../.claude/agents/agent-index.json"
echo "🔗 Claude Code integration updated"
