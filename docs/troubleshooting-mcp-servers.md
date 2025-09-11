# MCP Server Troubleshooting Guide

This guide helps you resolve common issues with MCP (Model Context Protocol) servers, including the dreaded `ENOENT` error.

## Quick Fix for ENOENT Errors

If you're seeing an error like:
```
Connection state: Error spawn imagesorcery-mcp ENOENT
```

Run our diagnostic script:
```bash
./scripts/diagnose-mcp-servers.sh imagesorcery-mcp
```

## Common MCP Server Issues

### 1. ENOENT Error (File Not Found)

**What it means**: The system cannot find the MCP server executable.

**Common causes**:
- Server is not installed
- Server is not in your PATH
- Typo in the server name
- Permission issues

**Solutions**:

1. **Check if installed**:
   ```bash
   which imagesorcery-mcp
   ```

2. **Install the server**:
   ```bash
   # For Node.js/NPM servers
   npm install -g imagesorcery-mcp
   
   # For Python servers
   pip install imagesorcery-mcp
   # or
   pipx install imagesorcery-mcp
   ```

3. **Add to PATH if locally installed**:
   ```bash
   export PATH="$PWD/node_modules/.bin:$PATH"
   ```

4. **Make executable**:
   ```bash
   chmod +x /path/to/imagesorcery-mcp
   ```

### 2. Installation Issues

**Node.js/NPM servers**:
```bash
# Global installation
npm install -g @anthropic/mcp-server-filesystem
npm install -g @anthropic/mcp-server-sqlite

# Local installation
npm install
export PATH="$PWD/node_modules/.bin:$PATH"
```

**Python servers**:
```bash
# Using pip
pip install mcp-server-git
pip install mcp-server-postgres

# Using pipx (recommended for CLI tools)
pipx install mcp-server-git
```

### 3. Configuration Issues

**Check configuration files**:
- `~/.config/claude/claude_desktop_config.json`
- `.claude/mcp.json` (project-specific)

**Example configuration**:
```json
{
  "mcpServers": {
    "imagesorcery": {
      "command": "imagesorcery-mcp",
      "args": []
    }
  }
}
```

## Diagnostic Tools

### Automated Diagnostic Script
```bash
# Check specific server
./scripts/diagnose-mcp-servers.sh imagesorcery-mcp

# General diagnosis
./scripts/diagnose-mcp-servers.sh
```

### Manual Diagnostics
```bash
# Check environment
echo $PATH
which node npm python pip

# Check common installation locations
ls -la ~/.local/bin/
ls -la /usr/local/bin/
ls -la node_modules/.bin/

# Test server directly
imagesorcery-mcp --help
```

## Environment Setup

### Setting up PATH
Add to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):
```bash
# For pipx installations
export PATH="$HOME/.local/bin:$PATH"

# For npm global installations
export PATH="$HOME/.npm-global/bin:$PATH"

# For local project installations
export PATH="$PWD/node_modules/.bin:$PATH"
```

### Reload shell configuration:
```bash
source ~/.bashrc
# or
source ~/.zshrc
```

## Troubleshooting Workflow

1. **Identify the error**:
   - Look for `ENOENT` in error messages
   - Note the exact server name causing issues

2. **Run diagnostics**:
   ```bash
   ./scripts/diagnose-mcp-servers.sh [server-name]
   ```

3. **Follow suggested fixes**:
   - Install missing servers
   - Fix PATH issues
   - Resolve permissions

4. **Verify the fix**:
   ```bash
   which [server-name]
   [server-name] --help
   ```

5. **Restart your MCP client** (Claude Desktop, etc.)

## Common MCP Servers

| Server Name | Installation | Purpose |
|-------------|--------------|---------|
| `imagesorcery-mcp` | `npm install -g imagesorcery-mcp` | Image processing |
| `@anthropic/mcp-server-filesystem` | `npm install -g @anthropic/mcp-server-filesystem` | File operations |
| `@anthropic/mcp-server-sqlite` | `npm install -g @anthropic/mcp-server-sqlite` | SQLite database |
| `mcp-server-git` | `pip install mcp-server-git` | Git operations |
| `mcp-server-postgres` | `pip install mcp-server-postgres` | PostgreSQL database |

## Getting Help

If you're still having issues:

1. **Use the MCP Troubleshooting Guardian**:
   Ask Claude: "Use the 999-operations-mcp-troubleshooting-guardian to help me fix my MCP server issue"

2. **Provide detailed error information**:
   - Full error message
   - Server name
   - Operating system
   - Installation method attempted

3. **Check server documentation**:
   - GitHub repository for the specific MCP server
   - Installation and configuration guides

## Prevention

To avoid future issues:

1. **Use package managers consistently**:
   - `pipx` for Python CLI tools
   - `npm -g` for Node.js CLI tools

2. **Document your MCP server setup**:
   - Keep track of installed servers
   - Note configuration changes

3. **Regular maintenance**:
   - Update servers periodically
   - Clean up unused servers

---

*This guide is maintained by the MCP Troubleshooting Guardian (999-operations-mcp-troubleshooting-guardian). For complex issues, invoke this guardian directly.*