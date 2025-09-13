# Guardian Agents: Usage and Workflow

This document outlines the official, non-negotiable workflow for integrating and updating the Guardian Agents knowledge base within another project. Adherence to this process ensures project stability and prevents Git history conflicts.

## The `git submodule` Standard

To embed this repository into a parent project, you **must** use the `git submodule` command. This creates a "live link" to this repository, keeping its Git history separate and independent from the parent project.

**Do not** copy the files directly. This is an unsupported method that will cause update and versioning conflicts.

The required command-line tool for all submodule operations is the standard `git` CLI. The `gh` (GitHub CLI) tool is not used for this workflow.

---

## The Full Workflow

### Phase 1: One-Time Setup (Adding Guardians to a Project)

To "install" the guardians into a subdirectory of a `ParentProject`:

1.  **Navigate to your Parent Project:**
    ```bash
    cd /path/to/ParentProject
    ```

2.  **Add the Submodule:**
    This command creates the live link to the guardians repository.
    ```bash
    git submodule add https://github.com/kairin/claude-guardian-agents.git guardians
    ```

3.  **Commit the Link:**
    This commit does not contain all the files from the guardians repo. It only contains a "bookmark" to a specific version.
    ```bash
    git commit -m "feat: Integrate the Guardian Agents knowledge base"
    ```

### Phase 2: The Update Cycle

There are two scenarios for updates:

#### Scenario A: Pulling Downstream Changes (Updating Your Project with the Latest Guardians)

1.  A change is pushed to the main `claude-guardian-agents` repository.
2.  To get these changes, navigate into the submodule directory and pull them:
    ```bash
    cd guardians
    git pull origin main
    cd ..
    ```
3.  Back in `ParentProject`, `git status` will show `modified: guardians (new commits)`.
4.  Commit this updated "bookmark" to your `ParentProject`:
    ```bash
    git add guardians
    git commit -m "chore: Update Guardian Agents to latest version"
    git push
    ```

#### Scenario B: Pushing Upstream Changes (Updating Guardians from within Your Project)

1.  Navigate into the submodule to make a change:
    ```bash
    cd guardians
    ```
2.  You are now inside the `claude-guardian-agents` repository. Edit files as needed.
3.  Commit your changes to the submodule itself:
    ```bash
    git add .
    git commit -m "docs: Describe a change to a guardian"
    ```
4.  **Push these changes directly to the central `claude-guardian-agents` repository:**
    ```bash
    git push origin main
    ```
5.  Finally, `cd ..` back to `ParentProject` and commit the new "bookmark" to lock in the new version, as shown in Scenario A.
