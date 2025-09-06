# 🧪 Development Agents Workflow

This document shows how Development & Testing Agents work with **verified Claude Code subagent chaining** support.

## Agent Overview

```mermaid
graph LR
    A[👨‍💻 Developer] --> B[code-guardian]
    B --> C[fix-guardian]
    C --> D[refactor-guardian]
    D --> E[test-guardian]
    E --> F[ui-guardian]
    F --> G[✅ Quality Code]
    
    style B fill:#fff4e1
    style C fill:#fff4e1
    style D fill:#fff4e1
    style E fill:#fff4e1
    style F fill:#fff4e1
```

## 1. Code Guardian Workflow

**Purpose**: Audit code quality without making changes

```mermaid
flowchart TD
    A[📁 Code Submitted] --> B{code-guardian Analysis}
    B --> C[🔍 Scan Formatting]
    B --> D[🔍 Check Linting Rules]
    B --> E[🔍 Type Safety Check]
    B --> F[🔍 Security Scan]
    
    C --> G{Issues Found?}
    D --> G
    E --> G  
    F --> G
    
    G -->|Yes| H[📋 Generate Report]
    G -->|No| I[✅ Code Quality Approved]
    
    H --> J[🚨 Send to fix-guardian]
    I --> K[▶️ Continue Pipeline]
    
    style B fill:#fff4e1
    style G fill:#ffffcc
    style H fill:#ffe1e1
    style I fill:#e1f5e1
```

**What you see**:
- ✅ **Green**: Code passes quality checks  
- 🚨 **Red**: Issues found, needs fixing
- 📋 **Report**: Detailed list of problems

## 2. Fix Guardian Workflow

**Purpose**: Automatically fix code formatting and issues

```mermaid
flowchart TD
    A[🚨 Issues from code-guardian] --> B{fix-guardian Action}
    B --> C[🔧 Auto-format Code]
    B --> D[🔧 Fix Linting Issues] 
    B --> E[🔧 Standardize Style]
    B --> F[🔧 Fix Simple Bugs]
    
    C --> G[🔍 Verify Fixes]
    D --> G
    E --> G
    F --> G
    
    G --> H{All Fixed?}
    H -->|Yes| I[✅ Code Fixed]
    H -->|No| J[📋 Report Remaining Issues]
    
    I --> K[▶️ Send to refactor-guardian]
    J --> L[👨‍💻 Manual Review Needed]
    
    style B fill:#fff4e1
    style G fill:#ffffcc
    style H fill:#ffffcc
    style I fill:#e1f5e1
    style J fill:#ffe1e1
```

**What happens**:
- 🔧 **Auto-fixes**: Format, style, simple errors
- 📋 **Complex issues**: Flagged for human review
- ✅ **Success**: Code ready for refactoring

## 3. Refactor Guardian Workflow

**Purpose**: Improve code architecture and reduce technical debt

```mermaid
flowchart TD
    A[✅ Fixed Code] --> B{refactor-guardian Analysis}
    B --> C[🔍 Identify Code Smells]
    B --> D[🔍 Find Duplicate Code]
    B --> E[🔍 Check Architecture]
    B --> F[🔍 Dependency Analysis]
    
    C --> G{Improvements Needed?}
    D --> G
    E --> G
    F --> G
    
    G -->|Yes| H[🛠️ Suggest Refactoring]
    G -->|No| I[✅ Architecture Approved]
    
    H --> J[📊 Impact Analysis]
    J --> K[👨‍💻 Review Suggestions]
    K --> L{Approve Changes?}
    L -->|Yes| M[🔄 Apply Refactoring]
    L -->|No| I
    M --> I
    
    I --> N[▶️ Send to test-guardian]
    
    style B fill:#fff4e1
    style G fill:#ffffcc
    style L fill:#ffffcc
    style I fill:#e1f5e1
```

**What it does**:
- 🔍 **Analyzes**: Code structure and patterns
- 🛠️ **Suggests**: Architecture improvements
- 📊 **Impact**: Shows what changes affect
- 🔄 **Refactors**: Improves code quality

## 4. Test Guardian Workflow

**Purpose**: Generate and execute comprehensive tests

```mermaid
flowchart TD
    A[🔄 Refactored Code] --> B{test-guardian Action}
    B --> C[📝 Generate Unit Tests]
    B --> D[📝 Generate Integration Tests]
    B --> E[🔧 Setup Test Environment]
    
    C --> F[🧪 Run Tests]
    D --> F
    E --> F
    
    F --> G{All Tests Pass?}
    G -->|Yes| H[✅ Tests Passed]
    G -->|No| I[❌ Test Failures]
    
    I --> J[📋 Analyze Failures]
    J --> K[🔧 Fix Test Issues]
    K --> F
    
    H --> L[📊 Coverage Report]
    L --> M{Coverage OK?}
    M -->|Yes| N[✅ Testing Complete]
    M -->|No| O[📝 Add More Tests]
    O --> F
    
    N --> P[▶️ Send to ui-guardian]
    
    style B fill:#fff4e1
    style F fill:#ffffcc
    style G fill:#ffffcc
    style M fill:#ffffcc
    style N fill:#e1f5e1
```

**What happens**:
- 📝 **Creates**: Unit and integration tests
- 🧪 **Runs**: All test suites
- 📊 **Coverage**: Ensures adequate test coverage
- ✅ **Reports**: Test results and recommendations

## 5. UI Guardian Workflow

**Purpose**: Test user interfaces across browsers and devices

```mermaid
flowchart TD
    A[✅ Tested Code] --> B{ui-guardian Testing}
    B --> C[🌐 Cross-browser Testing]
    B --> D[📱 Mobile Device Testing]
    B --> E[♿ Accessibility Testing]
    B --> F[👁️ Visual Regression Testing]
    
    C --> G[🔍 Analyze Results]
    D --> G
    E --> G
    F --> G
    
    G --> H{UI Issues Found?}
    H -->|Yes| I[📋 Generate UI Report]
    H -->|No| J[✅ UI Testing Complete]
    
    I --> K[🎨 Flag UI Problems]
    K --> L[👨‍🎨 Designer Review]
    L --> M{Fix UI Issues?}
    M -->|Yes| N[🔧 Update UI]
    M -->|No| O[📝 Document Known Issues]
    N --> B
    O --> J
    
    J --> P[🎯 Ready for Security Review]
    
    style B fill:#fff4e1
    style G fill:#ffffcc
    style H fill:#ffffcc
    style M fill:#ffffcc
    style J fill:#e1f5e1
```

**What it tests**:
- 🌐 **Browsers**: Chrome, Firefox, Safari, Edge
- 📱 **Devices**: Mobile, tablet, desktop
- ♿ **Accessibility**: Screen readers, keyboard navigation  
- 👁️ **Visual**: Layout and appearance consistency

## Complete Development Pipeline

```mermaid
sequenceDiagram
    participant Dev as 👨‍💻 Developer
    participant CG as code-guardian
    participant FG as fix-guardian  
    participant RG as refactor-guardian
    participant TG as test-guardian
    participant UG as ui-guardian
    participant Sec as 🔒 Security Review
    
    Dev->>CG: Submit code
    CG->>CG: Quality audit
    CG->>FG: Issues found
    FG->>FG: Auto-fix problems
    FG->>RG: Clean code
    RG->>RG: Architecture review
    RG->>TG: Improved code
    TG->>TG: Generate & run tests
    TG->>UG: Tested code
    UG->>UG: UI testing
    UG->>Sec: Ready for security
    Sec->>Dev: ✅ Complete!
```

## 🎯 Quick Reference

| Agent | Input | Output | Time |
|-------|-------|--------|------|
| code-guardian | Raw code | Quality report | 2-5 min |
| fix-guardian | Issues list | Fixed code | 1-3 min |
| refactor-guardian | Fixed code | Improved architecture | 5-10 min |
| test-guardian | Clean code | Test suite + results | 5-15 min |
| ui-guardian | Tested code | UI validation | 10-20 min |

**Total Pipeline Time**: 23-53 minutes (varies by code complexity)

---

**Need Help?**
- 📞 [Contact Support](../support.md)
- 📚 [Agent Configuration](../technical/agent-config.md)
- 🔧 [Troubleshooting](../troubleshooting.md)