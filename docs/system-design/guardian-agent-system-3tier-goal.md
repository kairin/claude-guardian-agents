Looking at the issues you've experienced, I'll help you create a **Requirements Guardian Agent** to prevent these problems. This agent will act as a filter to catch over-engineering, scope creep, and unnecessary complexity before they waste your time.I've created a **Requirements Guardian Agent** specification based on your exact pain points. This agent acts as a protective filter against the problems you experienced:

## Key Features:

1. **YAGNI Enforcement** - "You Aren't Gonna Need It" principle that rejects ANY feature you didn't explicitly request

2. **Anti-Pattern Detection** - Specifically catches:
   - Hook/automation loops (like your pre-commit issue)
   - "Helpful" features nobody asked for
   - Over-engineering simple requirements
   - Scope creep disguised as "completeness"

3. **Simple Decision Framework**:
   - Did they ask for it? → No → Don't build it
   - Is there a simpler way? → Yes → Use that
   - Will this create problems? → Yes → Don't do it

## How to Use:

1. **Before any implementation**, require listing:
   - What you ACTUALLY requested
   - What's being proposed
   - If they don't match → rejection

2. **For Claude/AI prompts**, add:
   ```
   "Follow Requirements Guardian rules:
   - Build ONLY what I explicitly request
   - No 'helpful' additions
   - Simplest solution only
   - If you want to add something I didn't ask for, DON'T"
   ```

3. **Red flag phrases to watch for**:
   - "This will be helpful..."
   - "While we're at it..."
   - "Most projects have..."
   - "For completeness..."

This guardian would have prevented your pre-commit hook issue entirely - you never asked for progress tracking automation, so it would have been rejected at the design phase.

The core philosophy: **Your time > AI's "helpfulness"**
