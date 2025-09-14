# 📋 Master TODO List

This document consolidates all identified tasks and action items across the project.

## 🎯 Overall Project Strategy & Prioritization

This section outlines the recommended phased approach for tackling the identified issues, prioritizing core stability and foundational improvements.

### Phase 1: Core Stability & Environment Foundation (Highest Priority)
- [ ] **Objective**: Ensure the development environment is stable, reliable, and consistent, and address critical workflow blockers.
- [ ] **Tasks**:
    - [x] **Address Makefile Python Path Resolution (Issue #1)**: Fix the `Makefile` commands to reliably use the `uv`-managed Python interpreter.
    - [x] **Enforce `uv` for `pre-commit` Hook Dependencies**: Remove `additional_dependencies` from `.pre-commit-config.yaml` and manage them via the main `uv`-managed virtual environment.
    - [ ] **Investigate and fix `fix end of files` / `update-progress` loop**: Resolve the persistent loop caused by these pre-commit hooks modifying `tracking/progress.json`.
    - [ ] **Address GPM Error Handling (Issue #2) & Rich Library Detection (Issue #3)**: Resolve these lower-severity issues for a cleaner system.

### Phase 2: Foundational Documentation Quality (High Priority)
- [ ] **Objective**: Establish a baseline for documentation quality and ensure existing validation tools are effective.
- [ ] **Tasks**:
    - [x] **Run `scripts/validate_docs.py`**: Execute the existing validation script to identify issues with YAML front matter and SVG embedding.
    - [ ] **Address `TODO: Add date format validation for 'last_updated'` in `scripts/validate_docs.py`**: Improve the existing validation tool.
    - [ ] **Implement Markdown Linting, Spell Checks, Link Validation**: Research, integrate, and run tools for comprehensive documentation quality.
    - [ ] **Address `mypy` code quality issues**: Resolve type hinting and code quality errors reported by `mypy` in Python scripts.

### Phase 3: Structured Documentation Enhancement (Medium Priority)
- [ ] **Objective**: Systematically improve the structure and content of the documentation.
- [ ] **Tasks**:
    - [ ] **Continue Documentation Refactoring (Batch 5 & 6)**: Progress through the remaining files to conform to the standard YAML front matter format.
    - [ ] **Continue Research Documentation**: Systematically document research papers and academic foundations for each Guardian agent, adding citations and updating relevant sections.

### Phase 4: Continuous Improvement & Maintenance (Ongoing)
- [ ] **Objective**: Maintain project health and ensure long-term stability.
- [ ] **Tasks**:
    - [ ] **General Testing (Regression, Integration)**: Regularly run these tests after any significant changes.
    - [ ] **Backup & Version Control**: Continue to adhere to good practices for backups and version control.

## 🔍 Issue Investigation & Resolution

### Issue #1: Makefile Python Path Resolution
- [x] **Investigation**
    - [x] Analyze Makefile python path resolution
    - [x] Test different PATH scenarios
    - [x] Document current behavior patterns
    - [x] Design improved Makefile approach
- [x] **Solution Implementation**
    - [x] Update Makefile with smart python detection
    - [ ] Test all make commands with and without activation
    - [ ] Update documentation with new behavior
    - [ ] Validate cross-platform compatibility
- [ ] **Documentation Updates**
    - [ ] Update installation guide with fixes
    - [ ] Update troubleshooting guide with solutions
    - [ ] Document new Makefile behavior
    - [ ] Update issue resolution in dry run results

### Issue #2: GPM Error Handling - Corrupted JSON Test
- [ ] **Investigation**
    - [ ] Locate failing test in validate-gpm.sh
    - [ ] Reproduce the corrupted JSON scenario
    - [ ] Analyze expected vs actual error handling
    - [ ] Determine if fix needed in code or test
- [ ] **Solution Implementation**
    - [ ] Implement proper corrupted JSON detection
    - [ ] Update error handling logic if needed
    - [ ] Fix or update the failing test
    - [ ] Run full validation suite

### Issue #3: Rich Library Detection False Negative
- [ ] **Investigation**
    - [ ] Reproduce Rich library detection timing
    - [ ] Test library availability after installation
    - [ ] Design improved validation approach
    - [ ] Verify impact on user experience
- [ ] **Solution Implementation**
    - [ ] Add retry logic to library validation
    - [ ] Improve setup script output clarity
    - [ ] Test setup script with fresh environment
    - [ ] Validate user experience improvement

### General Testing
- [ ] **Regression Testing**
    - [ ] Run complete dry run test again
    - [ ] Verify all previously working functionality still works
    - [ ] Test edge cases and error scenarios
    - [ ] Validate performance hasn't degraded
- [ ] **Integration Testing**
    - [ ] Test complete workflow from setup to reporting
    - [ ] Verify cross-script data sharing still works
    - [ ] Test error recovery and graceful degradation
    - [ ] Validate user experience improvements

### Backup & Version Control
- [ ] Create backup of current working state
- [ ] Commit fixes with detailed messages
- [ ] Create feature branch for fixes
- [ ] Test deployment in clean environment

## 🛠️ Development Environment & Tooling

### Enforce uv for pre-commit Hook Dependencies

- [x] **Objective**: Ensure `uv` is the sole manager for all Python requirements, including those for `pre-commit` hooks, by removing `pip`-managed `additional_dependencies`.
- [x] **Impact**:
    - [x] Eliminates `pre-commit` environment errors.
    - [x] Unified Dependency Management.
    - [x] Improved Reproducibility.
- [x] **Phase 1: Assessment & Preparation**
    - [x] **Step 1.1: Identify Affected Hooks and Dependencies**: Review `.pre-commit-config.yaml` to pinpoint all Python-based hooks that currently use `additional_dependencies`.
    - [x] **Step 1.2: Backup Current Configuration**: Create a backup of `.pre-commit-config.yaml` and any relevant dependency files.
- [x] **Phase 2: Configuration Modification**
    - [x] **Step 2.1: Remove `additional_dependencies` from `.pre-commit-config.yaml`**: For each identified hook, delete the `additional_dependencies` key and its associated list of packages.
    - [x] **Step 2.2: Integrate Dependencies into Main Project Requirements**: Add the identified dependencies to the project's primary dependency management file (e.g., `pyproject.toml` or ensure they are covered by `Makefile` install commands).
- [x] **Phase 3: Environment & Hook Re-initialization**
    - [x] **Step 3.1: Re-create `uv` Virtual Environment**: Perform a clean re-creation of the `uv` virtual environment (`make env-reset`).
    - [x] **Step 3.2: Re-install `pre-commit` Hooks**: Re-install `pre-commit` hooks (`pre-commit install`).
- [ ] **Phase 4: Validation & Documentation**
    - [ ] **Step 4.1: Validate `pre-commit` Hook Functionality**: Run all `pre-commit` hooks against the codebase (`make check` or `pre-commit run --all-files`).
    - [ ] **Step 4.2: Document the Change**: Update relevant project documentation (e.g., `docs/getting-started/installation.md`, `README.md`).

## 📝 Documentation Refactoring

### Documentation Verification
- [x] Run `scripts/validate_docs.py`
- [ ] Implement and run Markdown linting
- [ ] Implement and run spell checks
- [ ] Implement and run link validation
- [ ] Ensure consistency with `templates/documentation-template.md`
- [ ] Perform manual content review
- [ ] Address `TODO: Add date format validation for 'last_updated'` in `scripts/validate_docs.py`

### Batch 5: General Docs
- [ ] `docs/AGENT-CREATION-GUIDE.md`
- [ ] `docs/COMPLETE-PROGRESS-DOCUMENTATION.md`
- [ ] `docs/DOCUMENTATION-COMPLETE.md`
- [ ] `docs/DRY-RUN-RESULTS.md`
- [ ] `docs/GUARDIAN-PACKAGE-MANAGER.md`
- [ ] `docs/IMPLEMENTATION-VALIDATION.md`
- [ ] `docs/ISSUE-INVESTIGATION-PLAN.md`
- [ ] `docs/NAMING-CONVENTION.md`
- [ ] `docs/PHASE-2-IMPLEMENTATION-STATUS.md`
- [ ] `docs/PHASE-2-RESEARCH-ANALYSIS.md`
- [ ] `docs/PHASE-3-BATCH-UPDATES.md`
- [ ] `docs/PHASE-3-STATUS.md`
- [ ] `docs/PROJECT-MANAGEMENT-SYSTEM.md`
- [ ] `docs/RESEARCH-DOCUMENTATION-TODO.md`
- [ ] `docs/RESEARCH-MAPPING-STATUS.md`
- [ ] `docs/RESEARCH-PAPERS.md`
- [ ] `docs/THINK-TANK-COMPLETION-SUMMARY.MD`
- [ ] `docs/visual-overview.md`
- [ ] `docs/agents/mapping.md`
- [ ] `docs/agents/registry.md`
- [ ] `docs/agents/relationships.md`
- [ ] `docs/agents/templates.md`
- [ ] `docs/getting-started/gpm-installation.md`
- [ ] `docs/getting-started/installation.md`
- [ ] `docs/getting-started/quick-start.md`
- [ ] `docs/project-management/progress-tracking.md`
- [ ] `docs/tools/script-reference.md`
- [ ] `docs/troubleshooting/common-issues.md`
- [ ] `docs/visual-overview.md`
- [ ] `docs/workflows/AGENT-IMAGE-ASSET-PLAN.md`
- [ ] `docs/workflows/development-workflow.md`
- [ ] `docs/workflows/infrastructure-workflow.md`
- [ ] `docs/workflows/security-workflow.md`

### Batch 6: Other
- [ ] `AGENTS.md`
- [ ] `CLAUDE.md`
- [ ] `memory/constitution_update_checklist.md`
- [ ] `memory/constitution.md`

## 📚 Research Documentation

### Current Status
- [ ] Need to document research for 41+ existing agents
- [ ] Need to add citations to individual agent files

### Phase 1: Foundation
- [ ] Create research citation template
- [ ] Add "Research Foundation" section to README.md
- [ ] Add paper citation to each Think-Tank agent file (101-120)
- [ ] Create implementation-to-research mapping table

### Phase 2: Strategic Agents
- [ ] **Product Management Agents (001-006)**
    - [ ] Research Lean Startup methodology papers
    - [ ] Find Product-Market Fit research
    - [ ] Document Agile Product Management studies
    - [ ] Add citations to each Product agent file
- [ ] **Product Design Agents (021-025)**
    - [ ] Research Design Thinking papers (IDEO, Stanford d.school)
    - [ ] Find UX Research methodology papers
    - [ ] Document Human-Computer Interaction studies
    - [ ] Add citations to each Design agent file

### Phase 3: Technical Agents
- [ ] **Architecture Agents (041-045)**
    - [ ] Software Architecture in Practice (SEI)
    - [ ] Domain-Driven Design (Evans)
    - [ ] Microservices patterns research
    - [ ] Add citations to each Architecture agent file
- [ ] **Development Agents (061-069)**
    - [ ] Clean Code principles (Martin)
    - [ ] Test-Driven Development research
    - [ ] Pair Programming effectiveness studies
    - [ ] Add citations to each Development agent file
- [ ] **Quality Engineering (071-073)**
    - [ ] Testing methodologies research
    - [ ] Quality metrics studies (DORA)
    - [ ] Continuous Testing papers
    - [ ] Add citations to each Quality agent file
- [ ] **DevOps Engineering (081-083)**
    - [ ] DevOps Research and Assessment (DORA)
    - [ ] Site Reliability Engineering (Google)
    - [ ] Infrastructure as Code papers
    - [ ] Add citations to each DevOps agent file

### Phase 4: Operational Agents
- [ ] **Security Operations (092-094)**
    - [ ] NIST Cybersecurity Framework
    - [ ] OWASP research and guidelines
    - [ ] Zero Trust architecture papers
    - [ ] Add citations to each Security agent file
- [ ] **Data Operations (095-097)**
    - [ ] Data governance frameworks
    - [ ] DataOps methodology papers
    - [ ] Data quality research
    - [ ] Add citations to each Data agent file
- [ ] **IT Operations (098-100)**
    - [ ] ITIL v4 framework
    - [ ] Service Management research
    - [ ] Incident Management studies
    - [ ] Add citations to each IT Ops agent file

### Phase 5: Cross-Cutting Research
- [ ] **Multi-Agent Systems**
    - [ ] Society of Mind (Minsky)
    - [ ] Distributed AI systems
    - [ ] Agent communication protocols
    - [ ] Swarm intelligence research
- [ ] **Cognitive Science**
    - [ ] Dual Process Theory (Kahneman)
    - [ ] Theory of Mind research
    - [ ] Cognitive Load Theory
    - [ ] Problem-solving strategies
- [ ] **Organizational Theory**
    - [ ] Conway's Law implications
    - [ ] Team Topologies research
    - [ ] Organizational learning studies
    - [ ] Knowledge management frameworks

### Phase 6: Implementation Updates
- [ ] **Update Agent Files**
    - [ ] Add "Research Foundation" header to all 45+ agent files
    - [ ] Include paper citations in agent descriptions
    - [ ] Link to RESEARCH-PAPERS.md from each agent
    - [ ] Add "Based on research" activation triggers
- [ ] **Update Category READMEs**
    - [ ] 1-product/README.md - Add research section
    - [ ] 2-engineering/README.md - Add research section
    - [ ] 3-operations/README.md - Add research section
    - [ ] 4-think-tank/README.md - Add research section

### Phase 7: Validation & Testing
- [ ] **Citation Verification**
    - [ ] Verify all paper links work
    - [ ] Check DOI numbers where available
    - [ ] Confirm author names and dates
    - [ ] Add backup links where needed
- [ ] **Impact Measurement**
    - [ ] Document claimed improvements from papers
    - [ ] Design experiments to validate claims
    - [ ] Create metrics dashboard
    - [ ] Plan A/B testing framework

### Phase 8: Documentation & Communication
- [ ] **Final Documentation**
    - [ ] Update main README with research highlights
    - [ ] Create visual research-to-implementation map
    - [ ] Write blog post about research-driven agents
    - [ ] Create presentation slides
- [ ] **Change Management**
    - [ ] Update CHANGELOG.md with all research additions
    - [ ] Create migration guide for existing users
    - [ ] Document new research-based features
    - [ ] Announce updates to community

### Quick Wins (Do First)
- [ ] Add research link to main README
- [ ] Create agent template with research section
- [ ] Document top 5 most-used agents
- [ ] Add "Research" badge to documented agents
- [ ] Create research paper submission process

## 🤖 Gemini Agent Recommendations (2025-09-14)

This section outlines recommendations from the Gemini agent for improving project structure, documentation, and overall maintainability.

### A. Version Inconsistency (Critical Correctness Issue)
- [ ] **TASK: Verify `manifest.json` version and update if necessary.**
  - **Details**: Ensure `manifest.json`'s version aligns with `pyproject.toml` (currently 3.1.0). If `scripts/generate-manifest.py` is not updating it correctly, investigate and fix the script.
  - **Priority**: Critical
- [ ] **TASK: Establish a single source of truth for project version.**
  - **Details**: Centralize the project version definition (e.g., in `pyproject.toml`) and ensure all other files (like `manifest.json`, `README.md`) either reference it or are automatically updated.
  - **Priority**: High

### B. Agent Documentation Structure (Consolidation/Correctness)
- [ ] **TASK: Standardize frontmatter across all agent Markdown files.**
  - **Details**: Implement a consistent frontmatter structure (like the one seen in Think-Tank agents) for all agent Markdown files (e.g., Product/Design agents).
  - **Priority**: High
- [ ] **TASK: Automate frontmatter generation/validation.**
  - **Details**: Develop a pre-commit hook or script to ensure all new/modified agent files adhere to the standardized frontmatter.
  - **Priority**: Medium

### C. Redundant Agent Image Links (Simplification/Correctness)
- [ ] **TASK: Consolidate agent image paths.**
  - **Details**: Choose a single, consistent method for referencing agent images (e.g., always relative to the project root's `assets` directory).
  - **Priority**: Medium
- [ ] **TASK: Update all agent Markdown files with consolidated image paths.**
  - **Details**: Modify existing agent files to use the new, consistent image referencing method. This can be automated.
  - **Priority**: Medium

### D. Research Documentation (Consolidation/Simplification)
- [ ] **TASK: Centralize or reference research documentation.**
  - **Details**: Decide whether to centralize all detailed research in `docs/RESEARCH-PAPERS.md` (with agent files linking to sections) or keep details in agent files and make `docs/RESEARCH-PAPERS.md` an index.
  - **Priority**: High
- [ ] **TASK: Remove redundant detailed research content.**
  - **Details**: Ensure no duplication of detailed research information across multiple files once a strategy is decided.
  - **Priority**: Medium

### E. UV-Only Compliance (Correctness/Simplification)
- [ ] **TASK: Audit and remove non-UV package manager references.**
  - **Details**: Go through all documentation and installation scripts to eliminate references to `pip`, `conda`, `poetry`, etc., as per the "UV-Only Violations" identified.
  - **Priority**: High
- [ ] **TASK: Automate UV-only compliance validation.**
  - **Details**: Implement a pre-commit hook or CI/CD check to automatically detect and flag non-UV references.
  - **Priority**: Medium

### F. Pre-commit Hooks (Correctness/Simplification)
- [ ] **TASK: Verify and resolve problematic pre-commit hooks.**
  - **Details**: Confirm that `end-of-file-fixer` and `update-progress` (if still present or re-introduced) are correctly configured or removed to prevent commit failures. Follow the `issues_to_fix.md` roadmap.
  - **Priority**: Critical
- [ ] **TASK: Redesign problematic hooks if necessary.**
  - **Details**: If `update-progress` or similar functionality is desired, redesign it to avoid modifying staged files or creating infinite loops.
  - **Priority**: High
