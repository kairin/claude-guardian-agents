# Outstanding Issues & Documentation Todo List

## CI/CD Implementation
- Create `.github/workflows/main.yml` for automated builds, tests, linting, and manifest generation.
- Configure branch protection rules for `main` to enforce passing CI checks and required reviews.

## CI/CD Agent Group
- Define a new agent category for "CI/CD Agents" or "DevOps Agents".
- Create specialized agents within this group (e.g., `ci-workflow-guardian`, `deployment-guardian`, `pipeline-monitor-guardian`).

## Documentation Reorganization Todo List

- [ ] Group agent-related docs under agents/
	- Move AGENT-CREATION-GUIDE.md and any agent mapping/registry/relationship/template docs into docs/agents/. Add or update README.md to describe the folder.
- [ ] Move system design docs to system-design/
	- Move three-tier-guardian-system.md, requirements-guardian-agent.md, and related files into docs/system-design/. Ensure README.md summarizes the folder.
- [ ] Organize validation and progress docs
	- Create docs/validation/ for IMPLEMENTATION-VALIDATION.md, IMPLEMENTATION-VERIFICATION-REPORT.md, COMPLETE-PROGRESS-DOCUMENTATION.md, DOCUMENTATION-COMPLETE.md, DRY-RUN-RESULTS.md, and similar. Add README.md to explain purpose.
- [ ] Move research docs to research/
	- Create docs/research/ and move RESEARCH-PAPERS.md and related files there. Add README.md for context.
- [ ] Consolidate getting started and installation docs
	- Ensure all onboarding docs (`getting-started/gpm-installation.md`, `getting-started/installation.md`, `getting-started/quick-start.md`, `getting-started/USAGE_AND_WORKFLOW.md`) are in `docs/getting-started/`. Add or update `docs/getting-started/README.md`.
- [ ] Organize project management and workflows
	- Move PROJECT-MANAGEMENT-SYSTEM.md, progress-tracking.md, and all workflow docs into docs/project-management/ and docs/workflows/. Add README.md to each as needed.
- [ ] Organize project management and workflows
	- Move PROJECT-MANAGEMENT-SYSTEM.md, progress-tracking.md, and all workflow docs into docs/project-management/ and docs/workflows/. Add README.md to each as needed.
	- `ISSUE-INVESTIGATION-PLAN.md` moved to `docs/project-management/ISSUE-INVESTIGATION-PLAN.md`
- [ ] Move troubleshooting and tools docs
	- Ensure common-issues.md is in docs/troubleshooting/ and script-reference.md is in docs/tools/. Add README.md if missing.
- [ ] Clean up docs root folder
	- After moving files, keep only a high-level README.md and a TOC in docs/. Remove or relocate all other files to appropriate subfolders.
