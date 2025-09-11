# Changelog

All notable changes to the Claude Guardian Agents system will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2025-09-11

### ✨ Phase 2 Complete - All Product & Design Agents Researched
- **11 agents updated** with comprehensive research foundations
- **Product Management (001-006)**: Lean Startup, JTBD, Customer Development, HEART, OKRs
- **Product Design (021-025)**: Norman's principles, Shneiderman's rules, Design Thinking, Nielsen's heuristics
- **100% Phase 2 coverage**: All agents have 3-7 research sources
- **Differentiated by seniority**: Junior agents focus on fundamentals, senior on strategy

### 📚 Research Integration Details
- **Product Leadership (001)**: Lean Startup, JTBD, OKRs
- **Product Strategy (002)**: JTBD, Lean Analytics, RICE
- **Product Management (003)**: Customer Development, Agile, HEART
- **Product Ownership (004-006)**: Scrum, User Stories, varying by seniority
- **Design Leadership (021)**: Design Thinking, Norman, Design Systems
- **UX Research (022-023)**: Contextual Design, Mental Models, user research methods
- **UI Design (024-025)**: Gestalt principles, Material/HIG, typography

## [2.2.0] - 2025-09-11

### ✨ New Features
- **Research Documentation System**: Comprehensive documentation of all academic foundations
- **Think-Tank Guardian Agents**: New category of 20 agents for parallel reasoning (101-120 series)
  - Based on ParaThinker research (arxiv:2509.04475)
  - Implements diverse perspectives: physicist, anthropologist, artist, child, etc.
  - 12.3% accuracy improvement in reasoning tasks

### 📚 Documentation
- **RESEARCH-PAPERS.md**: Central repository of all research citations
- **Research Foundation sections**: Added to README and agent documentation
- **RESEARCH-DOCUMENTATION-TODO.md**: 8-phase plan for complete research coverage
- **Think-Tank Design Document**: Complete with research citations

### 🔬 Research Integration
- **ParaThinker (2024)**: Parallel reasoning paths to overcome tunnel vision
- **Society of Mind (1986)**: Multi-agent intelligence emergence
- **Lateral Thinking (1970)**: Creative problem-solving techniques
- **Design Patterns (1994)**: Software architecture foundations
- Research-to-implementation mapping for all agent categories

### 🎯 Key Improvements
- All new agents now include research paper citations
- Clear traceability from academic research to implementation
- Empirical validation metrics from source papers
- Structured approach to documenting research foundations

## [2.1.0] - 2025-09-06

### ✨ New Features
- **Agent Creation Guide**: Complete step-by-step instructions for creating agents in Claude Code
- **Subagent Chaining Support**: Verified and documented official Claude Code chaining capabilities
- **Agent Templates**: Ready-to-use templates with proper chaining instructions
- **Auto-Chain Examples**: Real-world examples of sequential agent workflows

### 📚 Documentation Updates
- Updated README.md with Claude Code `/agents` command instructions
- Added complete agent template with chaining logic
- Enhanced AGENTS-registry.md with creation workflow
- Updated AGENTS-relationships.md with verified chaining patterns
- Created comprehensive Agent Creation Guide
- Added workflow diagrams showing automatic chaining

### 🔗 Agent Chaining Features
- **Intelligent Selection**: Claude Code automatically picks appropriate agents
- **Sequential Workflows**: Agents can call next agents in process flow
- **Conditional Routing**: Route to different agents based on results
- **Auto-Chain Triggers**: Use "MUST BE USED" for automatic agent selection
- **Error Recovery**: Failed agents can trigger recovery workflows

## [2.0.0] - 2025-09-06

### 🎯 Major Changes
- **BREAKING**: Migrated from Citibank-specific to generic guardian system
- **BREAKING**: Implemented new naming convention: `number-department-role-specialization-guardian.md`
- **NEW**: Complete documentation restructure for non-developer accessibility

### ✨ Added
- Generic agent registry supporting any project type
- Visual workflow diagrams for all agent categories
- Comprehensive README.md with navigation structure
- Non-developer friendly documentation in `/docs/visual-overview.md`
- Individual workflow documentation:
  - Development agents workflow
  - Security & compliance workflow  
  - Infrastructure agents workflow
- Process-flow based numbering system (001-030)

### 🔄 Changed
- Agent registry updated from payment-specific to generic capabilities
- Agent relationships documentation updated for universal applicability
- All agents reorganized by process flow rather than organizational hierarchy
- Improved mermaid diagrams with emojis for better visual clarity

### 📚 Documentation
- Created `/docs/` structure with:
  - `/docs/visual-overview.md` - Non-developer guide
  - `/docs/workflows/` - Process diagrams for each agent type
  - `/docs/technical/` - Developer documentation
  - `/docs/config/` - Configuration guides
  - `/docs/contributing/` - Contribution guidelines

### 🏗️ Infrastructure
- Established clear agent communication protocols
- Defined priority levels and escalation procedures
- Implemented monitoring and health check systems

## [1.0.0] - 2025-08-29

### ✨ Initial Release
- Basic Citibank payment processing agent system
- 30 specialized guardian agents
- Basic registry and relationships documentation
- Organizational hierarchy structure

### 📦 Core Agents
- Email processing guardians
- Excel document guardians  
- Database operation guardians
- Security and compliance guardians
- Development and testing guardians
- Infrastructure management guardians
- Workflow and documentation guardians

---

## Version Numbering

**Major (X.0.0)**: Breaking changes, system restructure
**Minor (0.X.0)**: New agents, major features, backward compatible  
**Patch (0.0.X)**: Bug fixes, documentation updates, small improvements

## Migration Guide

### From 1.x to 2.0
1. **Agent Names**: Update all agent references to new naming convention
2. **Configuration**: Update agent configurations to use new generic capabilities
3. **Documentation**: Replace project-specific docs with generic templates
4. **Workflows**: Update agent interaction patterns to use new process flow

### Breaking Changes
- Agent file names changed from descriptive to numbered process flow
- Agent capabilities generalized from payment-specific to universal
- Documentation structure completely reorganized

## Roadmap

### 🎯 Upcoming (v2.1.0)
- [ ] Agent configuration management system
- [ ] Interactive agent finder tool
- [ ] Real-time agent status monitoring
- [ ] Agent performance metrics dashboard

### 🚀 Future (v2.2.0)
- [ ] Custom agent creation wizard
- [ ] Agent marketplace for community contributions
- [ ] Integration with popular development tools
- [ ] AI-powered agent recommendation engine

### 🔮 Vision (v3.0.0)
- [ ] Multi-project agent orchestration
- [ ] Advanced agent learning capabilities  
- [ ] Cloud-native agent deployment
- [ ] Enterprise security and compliance features

## Support

- 📚 [Documentation](README.md)
- 🐛 [Report Issues](https://github.com/anthropic/claude-guardian-agents/issues)
- 💬 [Discussions](https://github.com/anthropic/claude-guardian-agents/discussions)
- 📧 [Contact Support](docs/support/contact.md)

## Contributors

- Claude AI (Anthropic) - System Design & Implementation
- Community Contributors - Documentation & Testing

---

**Note**: This changelog is automatically maintained. For detailed commit history, see the [Git log](https://github.com/anthropic/claude-guardian-agents/commits/master).