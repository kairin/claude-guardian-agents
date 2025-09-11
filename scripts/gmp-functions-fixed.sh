#!/bin/bash
# Fixed GPM Functions - Working implementations that use actual repository structure

# Load manifest data
load_manifest() {
    local manifest_file="$1"
    if [ ! -f "$manifest_file" ]; then
        echo "❌ Manifest file not found: $manifest_file" >&2
        return 1
    fi

    # Check if jq is available
    if command -v jq >/dev/null 2>&1; then
        export MANIFEST_DATA=$(cat "$manifest_file")
        return 0
    else
        echo "⚠️ jq not found - using basic parsing" >&2
        export MANIFEST_DATA=$(cat "$manifest_file")
        return 0
    fi
}

# Fixed find_agent_file function
find_agent_file() {
    local agent_id="$1"
    local manifest_file="${2:-.guardian/cache/manifest.json}"

    # Load manifest if not already loaded
    if [ -z "$MANIFEST_DATA" ]; then
        load_manifest "$manifest_file" || return 1
    fi

    if command -v jq >/dev/null 2>&1; then
        # Use jq for JSON parsing
        local path=$(echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"].path // empty")
        if [ -n "$path" ]; then
            echo "$path"
            return 0
        fi
    else
        # Fallback: direct file search in repository
        local agent_file=$(find . -name "${agent_id}-*guardian.md" -type f | head -1)
        if [ -n "$agent_file" ]; then
            # Remove leading ./
            echo "${agent_file#./}"
            return 0
        fi
    fi

    echo "❌ Agent $agent_id not found" >&2
    return 1
}

# Fixed download_single_agent function
download_single_agent() {
    local agent_id="$1"
    local base_url="${GPM_REPO:-https://github.com/kairin/claude-guardian-agents}"

    print_info "Downloading agent $agent_id..."

    # Get agent file path from manifest
    local agent_file=$(find_agent_file "$agent_id")

    if [ $? -ne 0 ] || [ -z "$agent_file" ]; then
        print_warning "Agent $agent_id not found in manifest"
        return 1
    fi

    # Get agent info from manifest
    local agent_info
    if command -v jq >/dev/null 2>&1; then
        agent_info=$(echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"]")
        local agent_name=$(echo "$agent_info" | jq -r ".name")
        local checksum=$(echo "$agent_info" | jq -r ".checksum")
    else
        # Extract name from path
        agent_name=$(basename "$agent_file" .md)
        checksum="unknown"
    fi

    # Construct download URL
    local download_url="$base_url/raw/main/$agent_file"
    local local_path=".claude/agents/$agent_name.md"

    # Create directory if needed
    mkdir -p "$(dirname "$local_path")"

    # Download the file
    if curl -sSL "$download_url" -o "$local_path"; then
        print_success "Downloaded $agent_name"

        # Update local metadata
        update_agent_metadata "$agent_id" "$agent_name" "$local_path" "$checksum"
        return 0
    else
        print_error "Failed to download $agent_name from $download_url"
        return 1
    fi
}

# Test download URLs
test_download_urls() {
    local manifest_file="${1:-.guardian/cache/manifest.json}"
    local base_url="${GPM_REPO:-https://github.com/kairin/claude-guardian-agents}"

    print_status "Testing download URLs..."

    load_manifest "$manifest_file" || return 1

    if ! command -v jq >/dev/null 2>&1; then
        print_warning "jq not available - limited testing"
        return 1
    fi

    local total_agents=$(echo "$MANIFEST_DATA" | jq -r '.agents | keys | length')
    local tested=0
    local successful=0

    echo "$MANIFEST_DATA" | jq -r '.agents | keys[]' | while read -r agent_id; do
        local agent_path=$(echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"].path")
        local agent_name=$(echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"].name")
        local test_url="$base_url/raw/main/$agent_path"

        tested=$((tested + 1))

        if curl -sSI "$test_url" >/dev/null 2>&1; then
            print_success "✅ $agent_id ($agent_name) - URL valid"
            successful=$((successful + 1))
        else
            print_warning "❌ $agent_id ($agent_name) - URL invalid: $test_url"
        fi

        # Progress indicator
        if [ $((tested % 10)) -eq 0 ]; then
            print_info "Tested $tested/$total_agents URLs..."
        fi
    done

    print_info "URL Test Results: $successful/$total_agents URLs are valid"
}

# Get agent category
get_agent_category() {
    local agent_id="$1"

    if [ -z "$MANIFEST_DATA" ]; then
        load_manifest ".guardian/cache/manifest.json" || return 1
    fi

    if command -v jq >/dev/null 2>&1; then
        echo "$MANIFEST_DATA" | jq -r ".agents[\"$agent_id\"].category // \"unknown\""
    else
        # Fallback based on agent ID ranges
        local agent_num=$((10#$agent_id))

        if [ $agent_num -le 30 ]; then
            echo "strategy"
        elif [ $agent_num -ge 41 ] && [ $agent_num -le 45 ]; then
            echo "architecture"
        elif [ $agent_num -ge 61 ] && [ $agent_num -le 63 ]; then
            echo "backend"
        elif [ $agent_num -ge 64 ] && [ $agent_num -le 66 ]; then
            echo "frontend"
        elif [ $agent_num -ge 67 ] && [ $agent_num -le 69 ]; then
            echo "mobile"
        elif [ $agent_num -ge 71 ] && [ $agent_num -le 73 ]; then
            echo "quality"
        elif [ $agent_num -ge 81 ] && [ $agent_num -le 83 ]; then
            echo "devops"
        elif [ $agent_num -ge 92 ] && [ $agent_num -le 94 ]; then
            echo "security"
        elif [ $agent_num -ge 95 ] && [ $agent_num -le 97 ]; then
            echo "data"
        elif [ $agent_num -eq 91 ] || ([ $agent_num -ge 98 ] && [ $agent_num -le 100 ]); then
            echo "operations"
        elif [ $agent_num -ge 101 ] && [ $agent_num -le 120 ]; then
            echo "thinktank"
        else
            echo "unknown"
        fi
    fi
}

# List agents by category
list_agents_by_category() {
    local category="$1"
    local manifest_file="${2:-.guardian/cache/manifest.json}"

    load_manifest "$manifest_file" || return 1

    if command -v jq >/dev/null 2>&1; then
        echo "$MANIFEST_DATA" | jq -r ".categories[\"$category\"].agents[]?"
    else
        print_warning "jq not available - cannot list agents by category"
        return 1
    fi
}

# Generate working agent index
generate_agent_index() {
    local output_file="${1:-.claude/agents/agent-index.json}"
    local manifest_file="${2:-.guardian/cache/manifest.json}"

    print_status "Generating agent index for Claude Code..."

    load_manifest "$manifest_file" || return 1

    if ! command -v jq >/dev/null 2>&1; then
        print_error "jq is required to generate agent index"
        return 1
    fi

    # Create agent index from manifest
    local agent_index=$(cat << 'EOF'
{
    "system": "claude-guardian-agents",
    "version": "2.3.0",
    "description": "Specialized AI agents for software development and operations",
    "usage": "Claude Code automatically selects appropriate agents based on task descriptions",
    "agents_by_category": {},
    "workflow_chains": {},
    "selection_hints": {}
}
EOF
)

    # Populate from manifest
    agent_index=$(echo "$agent_index" | jq --argjson manifest "$MANIFEST_DATA" '
        .version = $manifest.version |
        .agents_by_category = $manifest.categories |
        .workflow_chains = $manifest.workflows |
        .selection_hints = ($manifest.agents | to_entries | map({key: (.value.triggers[]?), value: .value.name}) | from_entries)
    ')

    # Ensure output directory exists
    mkdir -p "$(dirname "$output_file")"

    # Write agent index
    echo "$agent_index" | jq '.' > "$output_file"

    print_success "Generated agent index: $output_file"
}

# Update local agent metadata
update_agent_metadata() {
    local agent_id="$1"
    local agent_name="$2"
    local local_path="$3"
    local checksum="$4"

    local metadata_file=".guardian/metadata.json"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Create metadata file if it doesn't exist
    if [ ! -f "$metadata_file" ]; then
        mkdir -p "$(dirname "$metadata_file")"
        cat > "$metadata_file" << EOF
{
    "guardian_version": "2.3.0",
    "project_type": "generic",
    "installed_at": "$timestamp",
    "agents": {},
    "customizations": {}
}
EOF
    fi

    # Update metadata with agent info
    if command -v jq >/dev/null 2>&1; then
        local temp_file=$(mktemp)
        jq --arg id "$agent_id" --arg name "$agent_name" --arg path "$local_path" --arg checksum "$checksum" --arg timestamp "$timestamp" '
            .agents[$id] = {
                "name": $name,
                "local_path": $path,
                "checksum": $checksum,
                "customized": false,
                "installed_at": $timestamp
            }
        ' "$metadata_file" > "$temp_file" && mv "$temp_file" "$metadata_file"
    fi

    print_info "Updated metadata for agent $agent_id"
}

# Validate installation
validate_installation() {
    print_status "Validating Guardian installation..."

    local errors=0

    # Check required files
    if [ ! -f ".guardian/metadata.json" ]; then
        print_error "Missing metadata file"
        errors=$((errors + 1))
    fi

    if [ ! -d ".claude/agents" ]; then
        print_error "Missing agents directory"
        errors=$((errors + 1))
    fi

    if [ ! -f ".claude/agents/agent-index.json" ]; then
        print_warning "Missing agent index (will be generated)"
    fi

    # Check agent files
    local agent_count=$(find .claude/agents -name "*guardian.md" -type f 2>/dev/null | wc -l)
    if [ "$agent_count" -eq 0 ]; then
        print_error "No agent files found"
        errors=$((errors + 1))
    else
        print_success "Found $agent_count agent files"
    fi

    # Validate agent index if it exists
    if [ -f ".claude/agents/agent-index.json" ]; then
        if command -v jq >/dev/null 2>&1; then
            if jq empty ".claude/agents/agent-index.json" 2>/dev/null; then
                print_success "Agent index is valid JSON"
            else
                print_error "Agent index is invalid JSON"
                errors=$((errors + 1))
            fi
        fi
    fi

    if [ $errors -eq 0 ]; then
        print_success "Installation validation passed!"
        return 0
    else
        print_error "Installation validation failed with $errors errors"
        return 1
    fi
}

# Print functions (define if not already available)
if ! type print_status >/dev/null 2>&1; then
    print_status() { echo -e "\033[0;34m🛡️  $1\033[0m"; }
    print_success() { echo -e "\033[0;32m✅ $1\033[0m"; }
    print_warning() { echo -e "\033[1;33m⚠️  $1\033[0m"; }
    print_error() { echo -e "\033[0;31m❌ $1\033[0m"; exit 1; }
    print_info() { echo -e "\033[0;35mℹ️  $1\033[0m"; }
fi

# Export functions for use in other scripts
export -f find_agent_file
export -f download_single_agent
export -f test_download_urls
export -f get_agent_category
export -f list_agents_by_category
export -f generate_agent_index
export -f update_agent_metadata
export -f validate_installation
export -f load_manifest
