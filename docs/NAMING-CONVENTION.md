# Agent Naming Convention

## Format

`{number}-{department}-{role}-{specialization}-guardian.md`

Where:
- **number**: Process flow order (001, 002, etc.)
- **department**: Main functional area
- **role**: Developer role or function
- **specialization**: Specific expertise area
- **guardian**: Fixed suffix

## Process Flow Order

### 📧 Data Processing Agents (001-005)
- `001-data-processing-data-validation-guardian.md`
- `002-data-processing-file-handling-guardian.md`
- `003-data-processing-database-optimization-guardian.md`

### 🧪 Development & Quality Agents (006-015)
- `006-development-code-quality-guardian.md`
- `007-development-code-fixing-guardian.md`
- `008-development-refactoring-guardian.md`
- `009-development-testing-unit-guardian.md`
- `010-development-testing-ui-guardian.md`
- `011-development-frontend-ui-guardian.md`
- `012-development-backend-api-guardian.md`
- `013-development-mobile-app-guardian.md`
- `014-development-architecture-design-guardian.md`
- `015-development-performance-optimization-guardian.md`

### 🔒 Security & Compliance Agents (016-020)
- `016-security-vulnerability-scanning-guardian.md`
- `017-security-compliance-regulatory-guardian.md`
- `018-security-environment-configuration-guardian.md`
- `019-security-dependency-audit-guardian.md`
- `020-security-penetration-testing-guardian.md`

### 🏗️ Infrastructure Agents (021-025)
- `021-infrastructure-backup-recovery-guardian.md`
- `022-infrastructure-migration-database-guardian.md`
- `023-infrastructure-deployment-orchestration-guardian.md`
- `024-infrastructure-process-monitoring-guardian.md`
- `025-infrastructure-scaling-performance-guardian.md`

### ⚡ Workflow Agents (026-030)
- `026-workflow-agile-development-guardian.md`
- `027-workflow-release-management-guardian.md`
- `028-workflow-git-version-control-guardian.md`
- `029-workflow-documentation-guardian.md`
- `030-workflow-feedback-support-guardian.md`

## Directory Structure

```
guardians/
├── 001-data-processing-data-validation-guardian.md
├── 002-data-processing-file-handling-guardian.md
├── 003-data-processing-database-optimization-guardian.md
├── 006-development-code-quality-guardian.md
├── 007-development-code-fixing-guardian.md
├── ...
└── 030-workflow-feedback-support-guardian.md
```

## Migration from Old Structure

### Current → New Mapping

**Product Management**
- `cpo-guardian.md` → `026-workflow-agile-development-guardian.md`
- `pds-guardian.md` → `027-workflow-release-management-guardian.md`
- `psm-guardian.md` → `028-workflow-git-version-control-guardian.md`

**Engineering - Backend**
- `dbe-guardian.md` → `012-development-backend-api-guardian.md`
- `sbe-guardian.md` → `012-development-backend-api-guardian.md`
- `jbe-guardian.md` → `012-development-backend-api-guardian.md`

**Engineering - Frontend**
- `dfe-guardian.md` → `011-development-frontend-ui-guardian.md`
- `sfe-guardian.md` → `011-development-frontend-ui-guardian.md`
- `jfe-guardian.md` → `011-development-frontend-ui-guardian.md`

**Engineering - Mobile**
- `dme-guardian.md` → `013-development-mobile-app-guardian.md`
- `sme-guardian.md` → `013-development-mobile-app-guardian.md`
- `jme-guardian.md` → `013-development-mobile-app-guardian.md`

**Quality Engineering**
- `dqe-guardian.md` → `009-development-testing-unit-guardian.md`
- `sqe-guardian.md` → `010-development-testing-ui-guardian.md`
- `jqe-guardian.md` → `009-development-testing-unit-guardian.md`

**DevOps Engineering**
- `dde-guardian.md` → `023-infrastructure-deployment-orchestration-guardian.md`
- `sde-guardian.md` → `024-infrastructure-process-monitoring-guardian.md`
- `jde-guardian.md` → `025-infrastructure-scaling-performance-guardian.md`

**Security Operations**
- `dso-guardian.md` → `016-security-vulnerability-scanning-guardian.md`
- `sse-guardian.md` → `017-security-compliance-regulatory-guardian.md`
- `jse-guardian.md` → `018-security-environment-configuration-guardian.md`

## Benefits of New Convention

### 1. Process Flow Clarity
- Numbers indicate execution order
- Easy to understand agent dependencies
- Clear workflow progression

### 2. Department Organization
- Logical grouping by function
- Consistent department names
- Scalable structure

### 3. Role Specification
- Clear role definitions
- Specialization areas identified
- Avoid naming conflicts

### 4. Scalability
- Easy to add new agents
- Maintain numbering sequence
- Clear insertion points

## Implementation Steps

1. **Create new directory structure**
2. **Map existing agents to new names**
3. **Update all references in documentation**
4. **Update AGENTS.md hierarchy diagram**
5. **Update workflow diagrams**
6. **Test all agent references**

## Validation Rules

- **Number**: Must be 3 digits (001-999)
- **Department**: Must be from approved list
- **Role**: Must describe function clearly
- **Specialization**: Must be specific area of expertise
- **Guardian**: Fixed suffix, never changes

## Approved Departments

- `data-processing`: Data handling and validation
- `development`: Code writing and quality
- `security`: Security and compliance
- `infrastructure`: System operations
- `workflow`: Process management

---

**Last Updated**: 2025-09-06
**Version**: 2.0.0
