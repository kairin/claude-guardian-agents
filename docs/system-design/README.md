# System Design Documentation

This directory contains system architecture and design documents for preventing common implementation issues.

## Documents

### Core System Design
- **[requirements-guardian-agent.md](requirements-guardian-agent.md)** - Requirements filter to prevent scope creep and over-engineering
- **[guardian-agent-system.md](guardian-agent-system.md)** - Complete guardian system architecture
- **[guardian-agent-system-3tier.md](guardian-agent-system-3tier.md)** - Three-tier model specialization system
- **[guardian-agent-system-3tier-goal.md](guardian-agent-system-3tier-goal.md)** - Goals and objectives for 3-tier system

## Purpose

These documents address recurring issues experienced during development:
- Scope creep and over-engineering
- Unnecessary automation loops (like pre-commit hooks)
- Features nobody asked for
- Time-wasting complexity

## Implementation Status

⚠️ **Design Phase** - These are architectural documents, not yet implemented as active agents.

## Usage

These documents serve as:
1. **Prevention Guidelines** - Reference when designing new features
2. **Architecture Blueprints** - For future guardian agent implementation
3. **Decision Framework** - YAGNI principle enforcement
4. **Problem History** - Learning from past scope creep issues

---

*These system designs emerged from real problems encountered during project development and aim to prevent similar issues in the future.*
