# Guardian Package Manager (GPM) - Implementation Design

## 🎯 Vision
A sophisticated package management system that allows Claude Guardian Agents to be easily installed, updated, and integrated into any project for LLM reference and spec-driven development.

## 🏗️ Core Architecture

### Installation Structure
```
project/
├── .claude/
│   ├── agents/                     # Claude Code agents directory
│   └── guardian-config.json        # GPM configuration
├── .guardian/
│   ├── metadata.json              # Version tracking, checksums
│   ├── customizations/            # Local agent customizations
│   ├── templates/                 # Project-specific templates
│   └── cache/                     # Update cache
└── specs/                         # spec-kit integration
    ├── agents/                    # Agent-generated specs
    └── workflows/                 # Spec-driven workflows
```

## 🚀 Installation System

### 1. Bootstrap Installation
```bash
# Install GPM globally
curl -sSL https://raw.githubusercontent.com/kairin/claude-guardian-agents/main/install.sh | bash

# Install into project
cd my-project/
gpm init                          # Initialize guardian system
gpm install                       # Install all agents
gpm install --category=backend   # Install specific category
```

### 2. Installation Process
1. **Download latest agent repository** (no git clone)
2. **Copy agents to `.claude/agents/`** with proper naming
3. **Create metadata tracking** for versions and checksums
4. **Generate project-specific templates** based on detected tech stack
5. **Initialize spec-kit integration** if specs/ directory exists

## 🔄 Intelligent Update System

### Core Problem: No Nested Git Repos
**Solution**: Smart diff and merge system without git dependency

### Update Algorithm
```python
def intelligent_update():
    1. fetch_remote_manifest()           # Get latest version info
    2. calculate_local_checksums()       # Current state
    3. identify_changed_files()          # Diff analysis
    4. preserve_customizations()         # Backup local changes
    5. apply_smart_merge()              # 3-way merge
    6. resolve_conflicts()              # Interactive resolution
    7. update_metadata()                # Track new version
```

### Version Tracking
```json
// .guardian/metadata.json
{
  "guardian_version": "2.3.0",
  "installed_at": "2025-09-11T10:30:00Z",
  "agents": {
    "001-strategy-product-leadership-guardian": {
      "version": "2.3.0",
      "checksum": "sha256:abc123...",
      "customized": false,
      "last_updated": "2025-09-11T10:30:00Z"
    }
  },
  "customizations": {
    "local_templates": ["backend-specific.md"],
    "modified_agents": ["001-strategy-product-leadership-guardian"]
  }
}
```

### Smart Merge Strategy
1. **Unchanged files**: Direct replace
2. **Locally modified**: 3-way merge (original, remote, local)
3. **New agents**: Add with project adaptation
4. **Deprecated agents**: Archive with migration guide
5. **Conflicts**: Interactive resolution with diff view

## 🧠 LLM Integration & Claude Code

### Agent Discovery System
```json
// .guardian/agent-index.json - Auto-generated for LLM consumption
{
  "agents_by_category": {
    "backend": ["061-backend-director", "062-backend-senior"],
    "frontend": ["064-frontend-director", "065-frontend-senior"],
    "mobile": ["067-mobile-director", "068-mobile-senior"]
  },
  "agents_by_task": {
    "api_development": ["062-backend-senior", "072-quality-senior"],
    "ui_design": ["024-ui-interface", "065-frontend-senior"],
    "deployment": ["081-devops-director", "082-devops-senior"]
  },
  "workflow_chains": {
    "feature_development": [
      "002-product-strategy",
      "044-principal-architect",
      "062-backend-senior",
      "072-quality-senior",
      "081-devops-director"
    ]
  }
}
```

### Claude Code Integration
```bash
# After installation, Claude Code automatically sees:
.claude/agents/
├── 001-strategy-product-leadership-guardian.md
├── 002-strategy-product-strategy-guardian.md
├── ...
└── agent-index.json                    # For smart selection
```

### LLM Selection Logic
The LLM can now:
1. **Read agent-index.json** to understand available agents
2. **Match user tasks** to appropriate agent categories
3. **Plan multi-agent workflows** using chain definitions
4. **Adapt agents** to project-specific context

## 🔧 Spec-Kit Integration

### Spec-Driven Workflow
```bash
# Generate specs from agents
gpm generate-specs --agent=backend-senior
gpm sync-specs                        # Sync with spec-kit

# Update agents from specs
gpm update-from-specs specs/backend-api.md
```

### Agent-Spec Mapping
```yaml
# .guardian/spec-mappings.yaml
spec_to_agents:
  "api-specification": ["062-backend-senior", "072-quality-senior"]
  "ui-specification": ["024-ui-interface", "065-frontend-senior"]
  "deployment-spec": ["081-devops-director"]

agent_to_specs:
  "062-backend-senior":
    generates: ["api-specification", "database-schema"]
    consumes: ["requirements-spec", "architecture-spec"]
```

## 📦 Installation Implementation

### install.sh (Bootstrap)
```bash
#!/bin/bash
# Guardian Package Manager Installer

set -e

GPM_VERSION="1.0.0"
GPM_REPO="https://github.com/kairin/claude-guardian-agents"
INSTALL_DIR="$HOME/.gpm"

echo "🛡️  Installing Guardian Package Manager..."

# Create installation directory
mkdir -p "$INSTALL_DIR"

# Download GPM binary/script
curl -sSL "$GPM_REPO/releases/latest/download/gpm" -o "$INSTALL_DIR/gpm"
chmod +x "$INSTALL_DIR/gpm"

# Add to PATH
echo 'export PATH="$HOME/.gpm:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.gpm:$PATH"' >> ~/.zshrc

echo "✅ GPM installed successfully!"
echo "📖 Run 'gpm init' in your project directory to get started"
```

### Project Initialization
```bash
#!/bin/bash
# gpm init - Initialize guardian system in project

detect_project_type() {
  if [ -f "package.json" ]; then echo "nodejs"
  elif [ -f "requirements.txt" ]; then echo "python"
  elif [ -f "Cargo.toml" ]; then echo "rust"
  elif [ -f "go.mod" ]; then echo "golang"
  else echo "generic"
  fi
}

init_guardian_system() {
  PROJECT_TYPE=$(detect_project_type)

  # Create directory structure
  mkdir -p .claude/agents .guardian/{customizations,templates,cache}

  # Initialize configuration
  cat > .guardian/metadata.json << EOF
{
  "guardian_version": null,
  "project_type": "$PROJECT_TYPE",
  "installed_at": null,
  "agents": {},
  "customizations": {}
}
EOF

  # Check for spec-kit integration
  if [ -d "specs" ]; then
    echo "📋 spec-kit detected - enabling integration"
    mkdir -p specs/{agents,workflows}
    touch .guardian/spec-integration-enabled
  fi

  echo "✅ Guardian system initialized for $PROJECT_TYPE project"
  echo "📖 Run 'gpm install' to install agents"
}
```

## 🔄 Update System Implementation

### Smart Update Algorithm
```python
#!/usr/bin/env python3
# gpm update - Intelligent update system

import json, hashlib, requests, difflib
from pathlib import Path

class GuardianUpdater:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.guardian_dir = self.project_root / ".guardian"
        self.metadata = self.load_metadata()

    def update(self):
        print("🔍 Checking for updates...")

        # Fetch remote manifest
        remote_manifest = self.fetch_remote_manifest()
        current_version = self.metadata.get("guardian_version")

        if remote_manifest["version"] == current_version:
            print("✅ Already up to date!")
            return

        print(f"📥 Updating from {current_version} to {remote_manifest['version']}")

        # Calculate changes
        changes = self.calculate_changes(remote_manifest)

        # Apply updates with smart merge
        self.apply_updates(changes)

        # Update metadata
        self.update_metadata(remote_manifest["version"])

        print("✅ Update complete!")

    def calculate_changes(self, remote_manifest):
        changes = {
            "new_agents": [],
            "updated_agents": [],
            "deprecated_agents": [],
            "conflicts": []
        }

        for agent_id, remote_info in remote_manifest["agents"].items():
            local_info = self.metadata["agents"].get(agent_id)

            if not local_info:
                changes["new_agents"].append(agent_id)
            elif local_info["checksum"] != remote_info["checksum"]:
                if local_info.get("customized", False):
                    changes["conflicts"].append(agent_id)
                else:
                    changes["updated_agents"].append(agent_id)

        return changes

    def apply_updates(self, changes):
        # Handle new agents
        for agent_id in changes["new_agents"]:
            self.install_agent(agent_id)

        # Handle updated agents
        for agent_id in changes["updated_agents"]:
            self.update_agent(agent_id)

        # Handle conflicts with 3-way merge
        for agent_id in changes["conflicts"]:
            self.resolve_conflict(agent_id)

    def resolve_conflict(self, agent_id):
        print(f"🔀 Conflict detected in {agent_id}")

        # Load three versions: original, local, remote
        original = self.get_original_version(agent_id)
        local = self.get_local_version(agent_id)
        remote = self.get_remote_version(agent_id)

        # Attempt automatic merge
        merged = self.three_way_merge(original, local, remote)

        if merged:
            self.save_agent(agent_id, merged)
            print(f"✅ Auto-merged {agent_id}")
        else:
            # Interactive resolution
            self.interactive_resolve(agent_id, local, remote)
```

## 🎯 Benefits of This System

### For Developers
- **One-command installation**: `gpm install`
- **Smart updates**: Preserves customizations
- **Project-aware**: Adapts to tech stack
- **Spec integration**: Works with spec-driven development

### For LLMs
- **Agent discovery**: Clear index of available agents
- **Smart selection**: Match tasks to appropriate agents
- **Workflow planning**: Pre-defined agent chains
- **Context awareness**: Project-specific adaptations

### For Teams
- **Version control**: Track agent versions across team
- **Customization sharing**: Share local adaptations
- **Spec synchronization**: Keep specs and agents aligned
- **Living documentation**: Always up-to-date agent knowledge

## 🚀 Next Steps

1. **Implement core GPM script** with install/update functionality
2. **Create agent-index.json** for LLM consumption
3. **Build spec-kit integration** workflows
4. **Add project detection** and adaptation logic
5. **Create migration tools** for existing installations

This system transforms the guardian agents from a static repository into a **living, intelligent package management system** that grows with your project while maintaining the sophisticated agent knowledge base.
