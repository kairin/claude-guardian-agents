#!/usr/bin/env python3
"""
Intelligent Workflow Orchestration System
Implements context-aware agent selection and personality-driven collaboration.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set


class TaskComplexity(Enum):
    SIMPLE = 1
    MODERATE = 2
    COMPLEX = 3


class PersonalityArchetype(Enum):
    ANALYTICAL = "analytical"
    CREATIVE = "creative"
    HUMAN_CENTERED = "human_centered"
    UNCONVENTIONAL = "unconventional"


@dataclass
class TaskContext:
    """Context information for a user task."""

    user_input: str
    intent_category: Optional[str] = None
    complexity_score: float = 0.0
    required_archetypes: Set[PersonalityArchetype] = field(default_factory=set)
    breakthrough_needed: bool = False
    domain_expertise: Set[str] = field(default_factory=set)


@dataclass
class AgentSelection:
    """Selected agent with reasoning."""

    agent_id: str
    agent_name: str
    selection_confidence: float
    reasoning: str
    personality_archetype: Optional[PersonalityArchetype] = None


@dataclass
class WorkflowPlan:
    """Complete workflow execution plan."""

    primary_agents: List[AgentSelection]
    think_tank_agents: List[AgentSelection]
    workflow_type: str
    estimated_duration: str
    parallel_reasoning: bool
    execution_strategy: str


class IntelligentOrchestrator:
    """Main orchestration engine for intelligent agent selection."""

    def __init__(self, manifest_path: str = "manifest.json"):
        self.manifest_path = Path(manifest_path)
        self.manifest = self._load_manifest()
        self.intelligent_selection = self.manifest.get("intelligent_selection", {})

    def _load_manifest(self) -> Dict:
        """Load manifest.json with intelligent selection data."""
        with open(self.manifest_path) as f:
            return json.load(f)

    def analyze_task_context(self, user_input: str) -> TaskContext:
        """Analyze user input to determine task context."""
        context = TaskContext(user_input=user_input)

        # Intent category classification
        context.intent_category = self._classify_intent(user_input)

        # Complexity scoring
        context.complexity_score = self._calculate_complexity(user_input)

        # Breakthrough detection
        context.breakthrough_needed = self._detect_breakthrough_need(user_input)

        # Required personality archetypes
        context.required_archetypes = self._determine_required_archetypes(user_input)

        # Domain expertise identification
        context.domain_expertise = self._identify_domain_expertise(user_input)

        return context

    def _classify_intent(self, user_input: str) -> str:
        """Classify the primary intent of the user request."""
        intent_categories = self.intelligent_selection.get("intent_categories", {})

        user_input_lower = user_input.lower()
        best_match = None
        best_score = 0

        for category, keywords in intent_categories.items():
            score = sum(
                1 for keyword in keywords if keyword.lower() in user_input_lower
            )
            if score > best_score:
                best_score = score
                best_match = category

        return best_match or "general"

    def _calculate_complexity(self, user_input: str) -> float:
        """Calculate task complexity score (0.0 - 1.0)."""
        complexity_indicators = self.intelligent_selection.get(
            "complexity_indicators", {}
        )

        user_input_lower = user_input.lower()
        complexity_score = 0.0

        # Simple indicators reduce complexity
        simple_count = sum(
            1
            for indicator in complexity_indicators.get("simple", [])
            if indicator.lower() in user_input_lower
        )

        # Moderate indicators add moderate complexity
        moderate_count = sum(
            1
            for indicator in complexity_indicators.get("moderate", [])
            if indicator.lower() in user_input_lower
        )

        # Complex indicators increase complexity significantly
        complex_count = sum(
            1
            for indicator in complexity_indicators.get("complex", [])
            if indicator.lower() in user_input_lower
        )

        # Base scoring algorithm
        complexity_score = min(
            1.0,
            (moderate_count * 0.3 + complex_count * 0.7)
            / max(1, simple_count * 0.5 + 1),
        )

        # Length and structural complexity factors
        if len(user_input.split()) > 20:
            complexity_score += 0.2

        if any(
            phrase in user_input_lower
            for phrase in ["multiple", "various", "complex", "integrate", "system"]
        ):
            complexity_score += 0.3

        return min(1.0, complexity_score)

    def _detect_breakthrough_need(self, user_input: str) -> bool:
        """Detect if breakthrough thinking is needed."""
        breakthrough_indicators = [
            "breakthrough",
            "innovative",
            "creative",
            "new approach",
            "alternative",
            "thinking outside",
            "unconventional",
            "novel",
            "revolutionary",
            "disruptive",
            "stuck",
            "failed",
            "not working",
            "traditional approaches",
        ]

        user_input_lower = user_input.lower()
        return any(
            indicator in user_input_lower for indicator in breakthrough_indicators
        )

    def _determine_required_archetypes(
        self, user_input: str
    ) -> Set[PersonalityArchetype]:
        """Determine which personality archetypes are needed."""
        personality_archetypes = self.intelligent_selection.get(
            "personality_archetypes", {}
        )
        required = set()

        user_input_lower = user_input.lower()

        for archetype_name, archetype_data in personality_archetypes.items():
            triggers = archetype_data.get("triggers", [])
            if any(trigger.lower() in user_input_lower for trigger in triggers):
                if archetype_name == "analytical":
                    required.add(PersonalityArchetype.ANALYTICAL)
                elif archetype_name == "creative":
                    required.add(PersonalityArchetype.CREATIVE)
                elif archetype_name == "human_centered":
                    required.add(PersonalityArchetype.HUMAN_CENTERED)
                elif archetype_name == "unconventional":
                    required.add(PersonalityArchetype.UNCONVENTIONAL)

        return required

    def _identify_domain_expertise(self, user_input: str) -> Set[str]:
        """Identify required domain expertise."""
        domains = set()
        user_input_lower = user_input.lower()

        domain_keywords = {
            "product": ["product", "market", "user", "strategy", "roadmap"],
            "engineering": [
                "code",
                "architecture",
                "technical",
                "system",
                "development",
            ],
            "operations": ["infrastructure", "deployment", "monitoring", "devops"],
            "quality": ["test", "quality", "validation", "performance"],
            "security": ["security", "risk", "compliance", "vulnerability"],
            "data": ["data", "analytics", "pipeline", "database"],
        }

        for domain, keywords in domain_keywords.items():
            if any(keyword in user_input_lower for keyword in keywords):
                domains.add(domain)

        return domains

    def select_primary_agents(self, context: TaskContext) -> List[AgentSelection]:
        """Select primary agents based on task context."""
        agents = self.manifest.get("agents", {})
        candidates = []

        for agent_id, agent_data in agents.items():
            if agent_data.get("category") == "thinktank":
                continue  # Handle think-tank agents separately

            score = self._calculate_agent_score(agent_data, context)
            if score > 0.3:  # Minimum relevance threshold
                selection = AgentSelection(
                    agent_id=agent_id,
                    agent_name=agent_data.get("name", ""),
                    selection_confidence=score,
                    reasoning=self._generate_selection_reasoning(
                        agent_data, context, score
                    ),
                )
                candidates.append(selection)

        # Sort by confidence and return top candidates
        candidates.sort(key=lambda x: x.selection_confidence, reverse=True)
        return candidates[:3]  # Return top 3 candidates

    def select_think_tank_agents(self, context: TaskContext) -> List[AgentSelection]:
        """Select think-tank agents based on personality archetype needs."""
        if not context.breakthrough_needed and context.complexity_score < 0.7:
            return []

        agents = self.manifest.get("agents", {})
        personality_archetypes = self.intelligent_selection.get(
            "personality_archetypes", {}
        )

        selected = []

        # If specific archetypes are required, select them
        if context.required_archetypes:
            for archetype in context.required_archetypes:
                archetype_name = archetype.value
                if archetype_name in personality_archetypes:
                    agent_ids = personality_archetypes[archetype_name].get("agents", [])
                    for agent_id in agent_ids[:1]:  # Select first agent from archetype
                        if agent_id in agents:
                            selected.append(
                                AgentSelection(
                                    agent_id=agent_id,
                                    agent_name=agents[agent_id].get("name", ""),
                                    selection_confidence=0.9,
                                    reasoning=f"Required {archetype_name} thinking for task",
                                    personality_archetype=archetype,
                                )
                            )

        # If breakthrough needed, ensure diverse archetypes
        elif context.breakthrough_needed:
            for archetype_name, archetype_data in personality_archetypes.items():
                agent_ids = archetype_data.get("agents", [])
                if agent_ids and agent_ids[0] in agents:
                    archetype_enum = PersonalityArchetype(archetype_name)
                    selected.append(
                        AgentSelection(
                            agent_id=agent_ids[0],
                            agent_name=agents[agent_ids[0]].get("name", ""),
                            selection_confidence=0.8,
                            reasoning=f"Breakthrough thinking requires {archetype_name} perspective",
                            personality_archetype=archetype_enum,
                        )
                    )

        return selected

    def _calculate_agent_score(self, agent_data: Dict, context: TaskContext) -> float:
        """Calculate relevance score for an agent given task context."""
        score = 0.0

        # Intent category matching
        if context.intent_category:
            category = agent_data.get("category", "")
            if (
                context.intent_category in ["strategic_planning"]
                and category == "strategy"
            ):
                score += 0.4
            elif context.intent_category in [
                "technical_implementation"
            ] and category in ["backend", "frontend", "architecture"]:
                score += 0.4
            elif (
                context.intent_category in ["quality_assurance"]
                and category == "quality"
            ):
                score += 0.4
            elif (
                context.intent_category in ["security_assessment"]
                and category == "security"
            ):
                score += 0.4

        # Complexity matching
        agent_complexity = agent_data.get("complexity", "")
        if context.complexity_score < 0.3 and agent_complexity == "simple":
            score += 0.3
        elif 0.3 <= context.complexity_score < 0.7 and agent_complexity == "moderate":
            score += 0.3
        elif context.complexity_score >= 0.7 and agent_complexity == "complex":
            score += 0.3

        # Trigger matching
        triggers = agent_data.get("triggers", [])
        user_input_lower = context.user_input.lower()
        trigger_matches = sum(
            1 for trigger in triggers if trigger.lower() in user_input_lower
        )
        score += min(0.4, trigger_matches * 0.1)

        return min(1.0, score)

    def _generate_selection_reasoning(
        self, agent_data: Dict, context: TaskContext, score: float
    ) -> str:
        """Generate human-readable reasoning for agent selection."""
        reasons = []

        if context.intent_category and agent_data.get("category"):
            reasons.append(
                f"Matches {context.intent_category} intent with {agent_data['category']} expertise"
            )

        if score > 0.8:
            reasons.append("High relevance match")
        elif score > 0.6:
            reasons.append("Good relevance match")
        else:
            reasons.append("Moderate relevance match")

        complexity = agent_data.get("complexity", "")
        if complexity:
            reasons.append(f"Suitable {complexity} complexity level")

        return "; ".join(reasons)

    def create_workflow_plan(self, context: TaskContext) -> WorkflowPlan:
        """Create comprehensive workflow execution plan."""
        primary_agents = self.select_primary_agents(context)
        think_tank_agents = self.select_think_tank_agents(context)

        # Determine workflow type
        if context.breakthrough_needed:
            workflow_type = "breakthrough_innovation"
        elif context.complexity_score > 0.7:
            workflow_type = "feature_development"
        elif any("api" in domain for domain in context.domain_expertise):
            workflow_type = "api_development"
        else:
            workflow_type = "standard_task"

        # Determine execution strategy
        if think_tank_agents:
            if len(think_tank_agents) >= 3:
                execution_strategy = "parallel_think_tank_synthesis"
                parallel_reasoning = True
            else:
                execution_strategy = "sequential_with_think_tank_support"
                parallel_reasoning = False
        else:
            execution_strategy = "sequential_primary_agents"
            parallel_reasoning = False

        # Estimate duration based on complexity and agent count
        if context.complexity_score > 0.8:
            estimated_duration = "3-7 days"
        elif context.complexity_score > 0.5:
            estimated_duration = "1-3 days"
        else:
            estimated_duration = "4-8 hours"

        return WorkflowPlan(
            primary_agents=primary_agents,
            think_tank_agents=think_tank_agents,
            workflow_type=workflow_type,
            estimated_duration=estimated_duration,
            parallel_reasoning=parallel_reasoning,
            execution_strategy=execution_strategy,
        )

    def generate_execution_instructions(self, plan: WorkflowPlan) -> str:
        """Generate human-readable execution instructions."""
        instructions = f"""
# 🚀 Intelligent Workflow Execution Plan

**Workflow Type**: {plan.workflow_type}
**Execution Strategy**: {plan.execution_strategy}
**Estimated Duration**: {plan.estimated_duration}
**Parallel Reasoning**: {'Enabled' if plan.parallel_reasoning else 'Disabled'}

## 🎯 Primary Agents Selected

"""

        for agent in plan.primary_agents:
            instructions += f"### {agent.agent_id}: {agent.agent_name}\n"
            instructions += f"- **Confidence**: {agent.selection_confidence:.1%}\n"
            instructions += f"- **Reasoning**: {agent.reasoning}\n\n"

        if plan.think_tank_agents:
            instructions += "## 🧠 Think-Tank Agents (Personality Archetypes)\n\n"
            for agent in plan.think_tank_agents:
                archetype = (
                    agent.personality_archetype.value
                    if agent.personality_archetype
                    else "unknown"
                )
                instructions += f"### {agent.agent_id}: {agent.agent_name}\n"
                instructions += f"- **Personality Archetype**: {archetype.title()}\n"
                instructions += f"- **Confidence**: {agent.selection_confidence:.1%}\n"
                instructions += f"- **Reasoning**: {agent.reasoning}\n\n"

        instructions += "## 🔄 Execution Sequence\n\n"

        if plan.execution_strategy == "parallel_think_tank_synthesis":
            instructions += """1. **Parallel Think-Tank Phase**: All think-tank agents analyze the problem simultaneously
2. **Synthesis Phase**: Combine diverse perspectives into unified approach
3. **Primary Implementation**: Selected primary agents execute the synthesized plan
4. **Validation & Delivery**: Quality and deployment agents finalize the solution"""

        elif plan.execution_strategy == "sequential_with_think_tank_support":
            instructions += """1. **Think-Tank Consultation**: Specific personality archetypes provide insights
2. **Enhanced Planning**: Primary agents incorporate think-tank recommendations
3. **Sequential Execution**: Primary agents work in planned sequence
4. **Validation & Delivery**: Quality and deployment agents finalize the solution"""

        else:
            instructions += """1. **Sequential Execution**: Primary agents work in order of selection confidence
2. **Handoff Coordination**: Each agent prepares context for the next
3. **Quality Gates**: Validation at each major milestone
4. **Final Delivery**: Deployment and documentation completion"""

        return instructions


def main():
    """Example usage of intelligent orchestration."""
    orchestrator = IntelligentOrchestrator()

    # Example user inputs
    test_cases = [
        "I need to build a revolutionary user authentication system that learns from user behavior",
        "Create a simple API endpoint for user registration",
        "Help me optimize database performance for our analytics dashboard",
        "Design a creative solution for real-time collaboration in our app",
    ]

    for i, user_input in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"TEST CASE {i}: {user_input}")
        print("=" * 60)

        # Analyze context
        context = orchestrator.analyze_task_context(user_input)
        print(f"Intent: {context.intent_category}")
        print(f"Complexity: {context.complexity_score:.2f}")
        print(f"Breakthrough Needed: {context.breakthrough_needed}")
        print(f"Required Archetypes: {[a.value for a in context.required_archetypes]}")

        # Create workflow plan
        plan = orchestrator.create_workflow_plan(context)

        # Generate instructions
        instructions = orchestrator.generate_execution_instructions(plan)
        print(instructions)


if __name__ == "__main__":
    main()
