#!/bin/bash
# GPM Validation Test Suite - Comprehensive testing of GPM implementation

set -e

# Source the fixed functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/gmp-functions-fixed.sh"

# Test configuration
TEST_DIR="/tmp/gpm-test-$$"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Test logging
test_start() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    echo -e "${BLUE}🧪 TEST $TOTAL_TESTS: $1${NC}"
}

test_pass() {
    PASSED_TESTS=$((PASSED_TESTS + 1))
    echo -e "${GREEN}   ✅ PASS: $1${NC}"
}

test_fail() {
    FAILED_TESTS=$((FAILED_TESTS + 1))
    echo -e "${RED}   ❌ FAIL: $1${NC}"
}

test_info() {
    echo -e "${PURPLE}   ℹ️  $1${NC}"
}

# Cleanup function
cleanup() {
    if [ -d "$TEST_DIR" ]; then
        rm -rf "$TEST_DIR"
    fi
}

# Setup test environment
setup_test_env() {
    echo -e "${BLUE}🔧 Setting up test environment...${NC}"

    # Create test directory
    mkdir -p "$TEST_DIR"
    cd "$TEST_DIR"

    # Copy manifest to test location
    mkdir -p .guardian/cache
    cp "$REPO_ROOT/manifest.json" ".guardian/cache/manifest.json"

    # Set GPM_REPO for testing
    export GPM_REPO="https://github.com/kairin/claude-guardian-agents"

    test_info "Test directory: $TEST_DIR"
    test_info "Repository root: $REPO_ROOT"
}

# Test 1: Manifest Loading
test_manifest_loading() {
    test_start "Manifest Loading"

    if load_manifest ".guardian/cache/manifest.json"; then
        test_pass "Manifest loaded successfully"
    else
        test_fail "Failed to load manifest"
        return 1
    fi

    # Check if manifest data is populated
    if [ -n "$MANIFEST_DATA" ]; then
        test_pass "Manifest data populated"
    else
        test_fail "Manifest data empty"
        return 1
    fi

    # Test JSON validity if jq is available
    if command -v jq >/dev/null 2>&1; then
        if echo "$MANIFEST_DATA" | jq empty >/dev/null 2>&1; then
            test_pass "Manifest is valid JSON"
        else
            test_fail "Manifest is invalid JSON"
            return 1
        fi

        # Check expected structure
        local agent_count=$(echo "$MANIFEST_DATA" | jq '.agents | length')
        if [ "$agent_count" -eq 45 ]; then
            test_pass "Correct number of agents ($agent_count)"
        else
            test_fail "Expected 45 agents, found $agent_count"
        fi
    else
        test_info "jq not available - skipping JSON validation"
    fi
}

# Test 2: Agent File Discovery
test_agent_file_discovery() {
    test_start "Agent File Discovery"

    # Test finding existing agents
    local test_agents=("001" "062" "072" "081" "092")

    for agent_id in "${test_agents[@]}"; do
        local agent_file=$(find_agent_file "$agent_id")

        if [ $? -eq 0 ] && [ -n "$agent_file" ]; then
            test_pass "Found agent $agent_id: $agent_file"

            # Verify the file actually exists in the repository
            if [ -f "$REPO_ROOT/$agent_file" ]; then
                test_pass "Agent file exists: $REPO_ROOT/$agent_file"
            else
                test_fail "Agent file missing: $REPO_ROOT/$agent_file"
            fi
        else
            test_fail "Could not find agent $agent_id"
        fi
    done

    # Test non-existent agent
    local nonexistent_agent="999"
    if ! find_agent_file "$nonexistent_agent" >/dev/null 2>&1; then
        test_pass "Correctly rejected non-existent agent $nonexistent_agent"
    else
        test_fail "Should not have found agent $nonexistent_agent"
    fi
}

# Test 3: URL Construction and Validation
test_url_validation() {
    test_start "URL Construction and Validation"

    # Test a few key agents
    local test_agents=("001" "062" "081")
    local valid_urls=0
    local tested_urls=0

    for agent_id in "${test_agents[@]}"; do
        local agent_file=$(find_agent_file "$agent_id")

        if [ -n "$agent_file" ]; then
            local test_url="$GPM_REPO/raw/main/$agent_file"
            tested_urls=$((tested_urls + 1))

            test_info "Testing URL: $test_url"

            # Test URL accessibility
            if curl -sSI "$test_url" >/dev/null 2>&1; then
                test_pass "URL accessible: $agent_id"
                valid_urls=$((valid_urls + 1))
            else
                test_fail "URL not accessible: $test_url"
            fi
        else
            test_fail "Could not get file path for agent $agent_id"
        fi
    done

    if [ $valid_urls -eq $tested_urls ] && [ $tested_urls -gt 0 ]; then
        test_pass "All tested URLs ($valid_urls/$tested_urls) are valid"
    else
        test_fail "URL validation failed ($valid_urls/$tested_urls valid)"
    fi
}

# Test 4: Category Classification
test_category_classification() {
    test_start "Category Classification"

    # Test known agent categories
    local test_cases=(
        "001:strategy"
        "044:architecture"
        "062:backend"
        "065:frontend"
        "068:mobile"
        "072:quality"
        "081:devops"
        "092:security"
        "095:data"
        "098:operations"
        "101:thinktank"
    )

    for test_case in "${test_cases[@]}"; do
        local agent_id="${test_case%:*}"
        local expected_category="${test_case#*:}"

        local actual_category=$(get_agent_category "$agent_id")

        if [ "$actual_category" = "$expected_category" ]; then
            test_pass "Agent $agent_id correctly categorized as $actual_category"
        else
            test_fail "Agent $agent_id: expected $expected_category, got $actual_category"
        fi
    done
}

# Test 5: Simulated Download (without actual download)
test_simulated_download() {
    test_start "Simulated Download Process"

    # Create mock directories
    mkdir -p .claude/agents

    # Test the download logic without actually downloading
    local test_agent="062"

    # Get agent information
    local agent_file=$(find_agent_file "$test_agent")

    if [ -n "$agent_file" ]; then
        test_pass "Retrieved file path for agent $test_agent: $agent_file"

        # Test URL construction
        local download_url="$GPM_REPO/raw/main/$agent_file"

        if curl -sSI "$download_url" >/dev/null 2>&1; then
            test_pass "Download URL is valid: $download_url"

            # Test local path construction
            local agent_name=$(basename "$agent_file" .md)
            local local_path=".claude/agents/$agent_name.md"

            test_pass "Local path constructed: $local_path"

            # Test metadata update (without actual download)
            update_agent_metadata "$test_agent" "$agent_name" "$local_path" "test-checksum"

            if [ -f ".guardian/metadata.json" ]; then
                test_pass "Metadata file created/updated"

                if command -v jq >/dev/null 2>&1; then
                    local stored_agent=$(jq -r ".agents[\"$test_agent\"].name" .guardian/metadata.json 2>/dev/null)
                    if [ "$stored_agent" = "$agent_name" ]; then
                        test_pass "Agent metadata correctly stored"
                    else
                        test_fail "Agent metadata not stored correctly"
                    fi
                fi
            else
                test_fail "Metadata file not created"
            fi
        else
            test_fail "Download URL not valid: $download_url"
        fi
    else
        test_fail "Could not retrieve file path for agent $test_agent"
    fi
}

# Test 6: Agent Index Generation
test_agent_index_generation() {
    test_start "Agent Index Generation"

    # Create output directory
    mkdir -p .claude/agents

    if command -v jq >/dev/null 2>&1; then
        if generate_agent_index; then
            test_pass "Agent index generation completed"

            if [ -f ".claude/agents/agent-index.json" ]; then
                test_pass "Agent index file created"

                # Validate the generated index
                if jq empty ".claude/agents/agent-index.json" >/dev/null 2>&1; then
                    test_pass "Generated index is valid JSON"

                    # Check structure
                    local has_categories=$(jq 'has("agents_by_category")' ".claude/agents/agent-index.json")
                    local has_workflows=$(jq 'has("workflow_chains")' ".claude/agents/agent-index.json")

                    if [ "$has_categories" = "true" ] && [ "$has_workflows" = "true" ]; then
                        test_pass "Index has required structure"
                    else
                        test_fail "Index missing required structure"
                    fi
                else
                    test_fail "Generated index is invalid JSON"
                fi
            else
                test_fail "Agent index file not created"
            fi
        else
            test_fail "Agent index generation failed"
        fi
    else
        test_info "jq not available - skipping agent index generation test"
    fi
}

# Test 7: Installation Validation
test_installation_validation() {
    test_start "Installation Validation"

    # Create minimal installation structure
    mkdir -p .claude/agents .guardian

    # Create some mock agent files
    echo "mock agent content" > .claude/agents/001-strategy-product-leadership-guardian.md
    echo "mock agent content" > .claude/agents/062-development-backend-senior-guardian.md

    # Run validation
    if validate_installation >/dev/null 2>&1; then
        test_pass "Installation validation passed"
    else
        test_fail "Installation validation failed"
    fi
}

# Test 8: Error Handling
test_error_handling() {
    test_start "Error Handling"

    # Test with missing manifest
    mv .guardian/cache/manifest.json .guardian/cache/manifest.json.bak 2>/dev/null || true

    if ! load_manifest ".guardian/cache/manifest.json" >/dev/null 2>&1; then
        test_pass "Correctly handled missing manifest"
    else
        test_fail "Should have failed with missing manifest"
    fi

    # Restore manifest
    mv .guardian/cache/manifest.json.bak .guardian/cache/manifest.json 2>/dev/null || true

    # Test with invalid agent ID
    if ! find_agent_file "invalid-agent" >/dev/null 2>&1; then
        test_pass "Correctly handled invalid agent ID"
    else
        test_fail "Should have failed with invalid agent ID"
    fi

    # Test with corrupted JSON
    echo "invalid json" > .guardian/cache/corrupt.json

    if ! load_manifest ".guardian/cache/corrupt.json" >/dev/null 2>&1; then
        test_pass "Correctly handled corrupted JSON"
    else
        test_fail "Should have failed with corrupted JSON"
    fi
}

# Run all tests
run_all_tests() {
    echo -e "${BLUE}🧪 GPM VALIDATION TEST SUITE${NC}"
    echo -e "${BLUE}=============================${NC}\n"

    setup_test_env

    # Run individual test suites
    test_manifest_loading
    test_agent_file_discovery
    test_url_validation
    test_category_classification
    test_simulated_download
    test_agent_index_generation
    test_installation_validation
    test_error_handling

    # Print summary
    echo -e "\n${BLUE}📊 TEST SUMMARY${NC}"
    echo -e "${BLUE}===============${NC}"
    echo -e "Total Tests: ${TOTAL_TESTS}"
    echo -e "${GREEN}Passed: ${PASSED_TESTS}${NC}"
    echo -e "${RED}Failed: ${FAILED_TESTS}${NC}"

    if [ $FAILED_TESTS -eq 0 ]; then
        echo -e "\n${GREEN}🎉 ALL TESTS PASSED! GPM implementation is functional.${NC}"
        cleanup
        return 0
    else
        echo -e "\n${RED}💥 SOME TESTS FAILED! GPM implementation needs fixes.${NC}"
        cleanup
        return 1
    fi
}

# Main execution
main() {
    case "${1:-all}" in
        "all")
            run_all_tests
            ;;
        "manifest")
            setup_test_env
            test_manifest_loading
            cleanup
            ;;
        "discovery")
            setup_test_env
            test_agent_file_discovery
            cleanup
            ;;
        "urls")
            setup_test_env
            test_url_validation
            cleanup
            ;;
        "download")
            setup_test_env
            test_simulated_download
            cleanup
            ;;
        "help")
            echo "Usage: $0 [all|manifest|discovery|urls|download|help]"
            echo ""
            echo "Tests:"
            echo "  all        - Run all validation tests (default)"
            echo "  manifest   - Test manifest loading only"
            echo "  discovery  - Test agent file discovery only"
            echo "  urls       - Test URL validation only"
            echo "  download   - Test download simulation only"
            echo "  help       - Show this help message"
            ;;
        *)
            echo "Unknown test: $1"
            echo "Run '$0 help' for available tests"
            exit 1
            ;;
    esac
}

# Set trap for cleanup
trap cleanup EXIT

# Run main function
main "$@"
