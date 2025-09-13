# 📊 Visual Agent Overview - For Non-Developers

This guide explains what each Guardian Agent does using simple terms and visual workflows.

## 🎯 What is a Guardian Agent?

Think of Guardian Agents as specialized team members, each with their own job:
- **Security Guardian** = Your security expert who checks for vulnerabilities
- **Test Guardian** = Your QA tester who makes sure everything works
- **Deploy Guardian** = Your DevOps engineer who handles releases

## 🏗️ Agent Categories Explained

### 📧 Data Processing Agents
**What they do**: Handle your project's data - files, databases, imports/exports

```mermaid
graph LR
    A[📄 Raw Data] --> B[data-guardian]
    B --> C[✅ Clean Data]

    D[📁 Files] --> E[file-guardian]
    E --> F[✅ Organized Files]

    G[🗄️ Database] --> H[database-guardian]
    H --> I[✅ Optimized DB]

    style B fill:#e1f5e1
    style E fill:#e1f5e1
    style H fill:#e1f5e1
```

**When to use**: When you have data to process, files to organize, or databases to optimize.

### 🔒 Security & Compliance Agents
**What they do**: Keep your project secure and compliant with regulations

```mermaid
graph LR
    A[🔍 Code Scan] --> B[security-guardian]
    B --> C[🛡️ Security Report]

    D[📋 Requirements] --> E[compliance-guardian]
    E --> F[✅ Compliance Check]

    G[📦 Dependencies] --> H[dependency-guardian]
    H --> I[⚠️ Vulnerability Report]

    style B fill:#ffe1e1
    style E fill:#ffe1e1
    style H fill:#ffe1e1
```

**When to use**: Before releasing features, during security audits, for regulatory compliance.

### 🧪 Development & Testing Agents
**What they do**: Write code, fix bugs, and test everything works properly

```mermaid
graph LR
    A[🐛 Bug Report] --> B[fix-guardian]
    B --> C[✅ Fixed Code]

    D[📝 New Feature] --> E[test-guardian]
    E --> F[🧪 Test Suite]

    G[🎨 UI Changes] --> H[ui-guardian]
    H --> I[✨ Tested Interface]

    style B fill:#fff4e1
    style E fill:#fff4e1
    style H fill:#fff4e1
```

**When to use**: During development, after making changes, before releases.

### 🏗️ Infrastructure Agents
**What they do**: Manage servers, deployments, backups, and system health

```mermaid
graph LR
    A[🚀 Deploy Request] --> B[deploy-guardian]
    B --> C[📱 Live Application]

    D[💾 Data] --> E[backup-guardian]
    E --> F[🛡️ Safe Backups]

    G[🔄 Migration] --> H[migration-guardian]
    H --> I[✅ Updated System]

    style B fill:#e1e8ff
    style E fill:#e1e8ff
    style H fill:#e1e8ff
```

**When to use**: For deployments, system updates, disaster recovery planning.

### ⚡ Workflow Agents
**What they do**: Manage the development process, documentation, and releases

```mermaid
graph LR
    A[📝 Code Changes] --> B[git-guardian]
    B --> C[🔄 Version Control]

    D[🎯 Project Plan] --> E[agile-guardian]
    E --> F[📊 Progress Tracking]

    G[📚 Updates] --> H[doc-guardian]
    H --> I[📖 Documentation]

    style B fill:#f0f8ff
    style E fill:#f0f8ff
    style H fill:#f0f8ff
```

**When to use**: Throughout the development lifecycle for coordination and documentation.

## 🔄 How Agents Work Together

### Example: Launching a New Feature

```mermaid
sequenceDiagram
    participant PM as 👤 Project Manager
    participant DEV as 🧪 Development Agents
    participant SEC as 🔒 Security Agents
    participant INFRA as 🏗️ Infrastructure Agents
    participant WF as ⚡ Workflow Agents

    PM->>DEV: "Build user login feature"
    DEV->>DEV: Write code & tests
    DEV->>SEC: "Please review security"
    SEC->>SEC: Security audit
    SEC->>INFRA: "Ready for deployment"
    INFRA->>INFRA: Deploy to staging
    INFRA->>WF: "Update documentation"
    WF->>PM: "Feature live & documented"
```

## 🎯 Quick Decision Guide

**Need help with...**

| Scenario | Use This Agent | What It Does |
|----------|---------------|--------------|
| 🐛 Bug fixing | fix-guardian | Automatically fixes code issues |
| 🔐 Security check | security-guardian | Scans for vulnerabilities |
| 🧪 Testing | test-guardian | Creates and runs tests |
| 🚀 Deployment | deploy-guardian | Pushes code to production |
| 📊 Data processing | data-guardian | Cleans and validates data |
| 📝 Documentation | doc-guardian | Updates project docs |
| 💾 Backups | backup-guardian | Creates system backups |
| 📋 Project tracking | agile-guardian | Tracks development progress |

## 🚀 Getting Started (Simple Steps)

1. **Identify Your Need**: Look at the table above
2. **Choose Your Agent**: Find the matching guardian
3. **Follow the Workflow**: Each agent has a simple workflow diagram
4. **Review Results**: Agents provide clear status updates

## 💡 Real-World Examples

### E-commerce Website
- **data-guardian**: Process customer orders
- **security-guardian**: Protect payment info
- **ui-guardian**: Test shopping cart
- **deploy-guardian**: Launch new features

### Mobile App
- **file-guardian**: Handle user uploads
- **test-guardian**: Test on different devices
- **backup-guardian**: Backup user data
- **release-guardian**: App store deployment

### Internal Tool
- **database-guardian**: Optimize queries
- **compliance-guardian**: Meet company policies
- **doc-guardian**: User manuals
- **agile-guardian**: Track development

---

**Next Steps**:
- 🔍 [Find Your Agent](../docs/workflows/) - See specific workflows
- 📚 [Use Cases](use-cases.md) - More detailed examples
- ❓ [FAQ](faq.md) - Common questions
