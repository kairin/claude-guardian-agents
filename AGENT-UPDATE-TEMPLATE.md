# Guardian Agent Page Template

Use this template to update all remaining guardian agent pages with consistent formatting.

## Standard Format

```markdown
# [Agent Title] Guardian

**Agent ID**: [NUMBER]  
**Department**: [DEPARTMENT]  
**Role**: [ROLE]  
**Specialization**: [SPECIALIZATION]

**Task:** [Original task description]

**Persona:** [Original persona description]

**Instructions:**

[Keep original instructions as bullet points]

**Tools:**

[Keep original tools list]

**Context:**

[Keep original context]

## 🔄 Agent Workflow

```mermaid
flowchart TD
    A[📋 Input Source] --> B{[NUMBER]-[department]-[role]-[specialization]-guardian}
    B --> C[🔍 Primary Function 1]
    B --> D[⚙️ Primary Function 2]  
    B --> E[📊 Primary Function 3]
    
    C --> F[📋 Analysis Result]
    D --> F
    E --> F
    
    F --> G{Next Action?}
    G -->|Condition 1| H[👉 [NEXT-AGENT-1]]
    G -->|Condition 2| I[👉 [NEXT-AGENT-2]]
    G -->|Condition 3| J[👉 [NEXT-AGENT-3]]
    G -->|Complete| K[✅ Final Output]
    
    H --> L[📋 Specialized Work 1]
    I --> M[🎨 Specialized Work 2]
    J --> N[🏗️ Specialized Work 3]
    K --> O[📈 Direct Result]
    
    L --> P[✅ Complete Workflow]
    M --> P
    N --> P
    O --> P
    
    style B fill:#[COLOR]
    style G fill:#ffffcc
    style P fill:#e1ffe1
```

## 🔗 Agent Relationships

### Input Sources
- 👤 **[INPUT-AGENT-1]**: [What it provides]
- 📊 **[INPUT-AGENT-2]**: [What it provides]
- 🔧 **[INPUT-SOURCE-3]**: [What it provides]

### Output Destinations
**Primary Chain (Sequential)**:
1. **[NEXT-AGENT-1]** - For [specific purpose]
2. **[NEXT-AGENT-2]** - For [specific purpose]
3. **[NEXT-AGENT-3]** - For [specific purpose]

**Conditional Chains**:
- If **[condition]** → **[conditional-agent]**
- If **[other condition]** → **[other-agent]**
- If **[third condition]** → **[third-agent]**

### Trigger Phrases for Auto-Chaining
- "[Work complete] - handing to [next-agent] for [specific task]"
- "[Analysis ready] - calling [next-agent] for [next phase]"
- "[Decision made] - triggering [next-agent] for [implementation]"
```

## Agent Categories and Colors

### Strategy Agents (001-020)
- **Color**: `#e1f5e1` (light green)
- **Input**: User requirements, market data
- **Output**: Strategic decisions, roadmaps

### Design Agents (021-040)  
- **Color**: `#ffe1f5` (light pink)
- **Input**: Strategy decisions, user needs
- **Output**: Design specifications, prototypes

### Architecture Agents (041-060)
- **Color**: `#f0f8ff` (light blue)
- **Input**: Requirements, design specs
- **Output**: Technical architecture, feasibility

### Development Agents (061-090)
- **Color**: `#fff4e1` (light orange)
- **Input**: Architecture, specifications
- **Output**: Implemented code, testing

### Operations Agents (091-100)
- **Color**: `#e1e8ff` (light purple)
- **Input**: Deployed code, system needs
- **Output**: Monitoring, maintenance, support

## Quick Agent Mapping

### Product Management Chain
001 → 002 → 003 → 004 → 021 (strategy to design)

### Design Chain  
021 → 022 → 024 → 041 (design to architecture)

### Architecture Chain
041 → 042 → 044 → 061 (architecture to development)

### Development Chain
061 → 062 → 065 → 092 (development to security)

### Operations Chain
092 → 082 → 091 → 029 (security to operations to documentation)

## Batch Update Commands

For efficiency, you can update multiple agents at once:

```bash
# Update all agents in a directory
find 1-product -name "*guardian.md" -exec echo "Processing {}" \;

# Use search and replace for common patterns
sed -i 's/old-pattern/new-pattern/g' */*guardian.md
```

## Examples by Department

### Example: Frontend Development Agent
```markdown
**Agent ID**: 065  
**Department**: Development  
**Role**: Frontend Senior  
**Specialization**: UI implementation and user interface development
```

### Example: Security Operations Agent  
```markdown
**Agent ID**: 092  
**Department**: Security  
**Role**: Operations Director  
**Specialization**: Security monitoring and incident response
```

---

**Use this template to update all 40 guardian agents consistently!**