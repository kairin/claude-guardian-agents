# Gemini Branch Management Guidelines

These guidelines are for managing branches within this project to ensure historical information is preserved and development workflows are clear.

## 1. Branch Preservation Policy

**Branches will NOT be automatically deleted** after commit, push, and merge tasks are completed. All branches, especially those following the specified naming schema, are considered valuable historical information and should be retained.

-   **Do NOT** use `git branch -d` or `git push origin --delete` unless explicitly instructed by a human user for a specific branch.
-   **Purpose**: To maintain a complete historical record of development efforts, experiments, and specific feature implementations, allowing for easier review, debugging, and understanding of project evolution over time.

## 2. Branch Naming Schema

All new branches created for development tasks (features, bug fixes, refactoring, documentation updates, etc.) **MUST** follow the `date-time-details-of-commit` schema.

**Format**: `YYYYMMDD-HHMMSS-type-short-description`

-   `YYYYMMDD`: Current date (YearMonthDay)
-   `HHMMSS`: Current time (HourMinuteSecond)
-   `type`: A short, descriptive type for the change (e.g., `feat` for feature, `fix` for bug fix, `docs` for documentation, `refactor` for refactoring, `chore` for maintenance).
-   `short-description`: A concise, hyphen-separated description of the changes.

**Example Branch Names**:
-   `20250914-143000-feat-user-profile-management`
-   `20250914-143515-fix-login-bug-authentication`
-   `20250914-144030-docs-api-endpoint-updates`
-   `20250914-144545-refactor-auth-service-cleanup`

**How to Create a Branch with this Schema**:
1.  Determine the current date and time.
2.  Identify the type of change and a short description.
3.  Combine them into the specified format.
4.  Execute `git checkout -b YYYYMMDD-HHMMSS-type-short-description`

**Purpose**:
-   **Historical Traceability**: Easily identify when a branch was created and what its primary purpose was, even years later.
-   **Uniqueness**: Minimize the chance of naming conflicts.
-   **Clarity**: Provide immediate context about the branch's content.

---

**Note**: These guidelines supersede any previous instructions regarding branch deletion or naming conventions.
