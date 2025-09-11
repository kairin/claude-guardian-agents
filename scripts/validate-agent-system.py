#!/usr/bin/env python3
"""
Guardian Agents System Validation Script
Comprehensive validation of agent system integrity, metadata consistency, and intelligence features.
"""

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class ValidationResult:
    """Result of a validation check."""

    check_name: str
    passed: bool
    message: str
    details: Optional[Dict] = None


@dataclass
class AgentValidation:
    """Comprehensive agent validation results."""

    agent_id: str
    file_exists: bool
    manifest_entry: bool
    metadata_valid: bool
    triggers_valid: bool
    research_foundations: int
    personality_archetype: Optional[str]
    category: str
    complexity: str


class GuardianAgentValidator:
    """Comprehensive Guardian Agents system validator."""

    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.manifest_path = self.base_path / "manifest.json"
        self.agents_path = self.base_path
        self.results: List[ValidationResult] = []

    def run_all_validations(self) -> List[ValidationResult]:
        """Run all validation checks and return results."""
        self.results.clear()

        # Load manifest
        manifest = self._load_manifest()
        if not manifest:
            return self.results

        # Core system validations
        self._validate_manifest_structure(manifest)
        self._validate_agent_count(manifest)
        self._validate_agent_files(manifest)
        self._validate_personality_system(manifest)
        self._validate_intelligence_features(manifest)
        self._validate_workflows(manifest)
        self._validate_categories(manifest)

        return self.results

    def _load_manifest(self) -> Optional[Dict]:
        """Load and validate manifest.json exists and is valid JSON."""
        try:
            if not self.manifest_path.exists():
                self.results.append(
                    ValidationResult(
                        "manifest_exists",
                        False,
                        f"Manifest file not found: {self.manifest_path}",
                    )
                )
                return None

            with open(self.manifest_path) as f:
                manifest = json.load(f)

            self.results.append(
                ValidationResult(
                    "manifest_loaded", True, "Manifest.json loaded successfully"
                )
            )
            return manifest

        except json.JSONDecodeError as e:
            self.results.append(
                ValidationResult(
                    "manifest_json_valid", False, f"Invalid JSON in manifest.json: {e}"
                )
            )
            return None
        except Exception as e:
            self.results.append(
                ValidationResult(
                    "manifest_load_error", False, f"Error loading manifest.json: {e}"
                )
            )
            return None

    def _validate_manifest_structure(self, manifest: Dict) -> None:
        """Validate manifest.json has required structure."""
        required_sections = ["categories", "agents", "workflows", "metadata"]
        missing_sections = [
            section for section in required_sections if section not in manifest
        ]

        if missing_sections:
            self.results.append(
                ValidationResult(
                    "manifest_structure",
                    False,
                    f"Missing required sections: {missing_sections}",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "manifest_structure", True, "All required manifest sections present"
                )
            )

    def _validate_agent_count(self, manifest: Dict) -> None:
        """Validate agent counts are consistent."""
        metadata_count = manifest.get("metadata", {}).get("total_agents", 0)
        actual_agent_count = len(manifest.get("agents", {}))

        # Count agents in categories
        category_agent_count = sum(
            len(category.get("agents", []))
            for category in manifest.get("categories", {}).values()
        )

        if metadata_count == actual_agent_count == category_agent_count:
            self.results.append(
                ValidationResult(
                    "agent_count_consistency",
                    True,
                    f"Agent counts consistent: {actual_agent_count} agents",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "agent_count_consistency",
                    False,
                    f"Agent count mismatch - Metadata: {metadata_count}, "
                    f"Agents: {actual_agent_count}, Categories: {category_agent_count}",
                    {
                        "metadata": metadata_count,
                        "agents": actual_agent_count,
                        "categories": category_agent_count,
                    },
                )
            )

    def _validate_agent_files(self, manifest: Dict) -> None:
        """Validate all agents have corresponding files and vice versa."""
        agents = manifest.get("agents", {})
        missing_files = []
        invalid_paths = []

        for agent_id, agent_data in agents.items():
            file_path = self.base_path / agent_data.get("path", "")
            if not file_path.exists():
                missing_files.append(f"{agent_id}: {file_path}")
            elif not str(file_path).endswith(".md"):
                invalid_paths.append(f"{agent_id}: {file_path}")

        if missing_files:
            self.results.append(
                ValidationResult(
                    "agent_files_exist",
                    False,
                    f"Missing agent files: {len(missing_files)} files",
                    {"missing_files": missing_files},
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "agent_files_exist", True, f"All {len(agents)} agent files exist"
                )
            )

        if invalid_paths:
            self.results.append(
                ValidationResult(
                    "agent_file_paths",
                    False,
                    f"Invalid agent file paths: {len(invalid_paths)} paths",
                    {"invalid_paths": invalid_paths},
                )
            )
        else:
            self.results.append(
                ValidationResult("agent_file_paths", True, "All agent file paths valid")
            )

    def _validate_personality_system(self, manifest: Dict) -> None:
        """Validate personality archetype system implementation."""
        # Check for intelligent_selection section
        intelligent_selection = manifest.get("intelligent_selection", {})
        if not intelligent_selection:
            self.results.append(
                ValidationResult(
                    "personality_system_exists",
                    False,
                    "Intelligent selection system not found in manifest",
                )
            )
            return

        # Validate personality archetypes
        personality_archetypes = intelligent_selection.get("personality_archetypes", {})
        expected_archetypes = [
            "analytical",
            "creative",
            "human_centered",
            "unconventional",
        ]

        missing_archetypes = [
            arch for arch in expected_archetypes if arch not in personality_archetypes
        ]
        if missing_archetypes:
            self.results.append(
                ValidationResult(
                    "personality_archetypes",
                    False,
                    f"Missing personality archetypes: {missing_archetypes}",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "personality_archetypes",
                    True,
                    "All 4 personality archetypes defined",
                )
            )

        # Validate think-tank agents
        thinktank_category = manifest.get("categories", {}).get("thinktank", {})
        thinktank_agents = thinktank_category.get("agents", [])

        expected_think_tank_count = 8
        if len(thinktank_agents) == expected_think_tank_count:
            self.results.append(
                ValidationResult(
                    "think_tank_agent_count",
                    True,
                    f"Think-tank has {expected_think_tank_count} agents as expected",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "think_tank_agent_count",
                    False,
                    f"Think-tank has {len(thinktank_agents)} agents, expected {expected_think_tank_count}",
                    {
                        "actual": len(thinktank_agents),
                        "expected": expected_think_tank_count,
                    },
                )
            )

        # Validate cognitive diversity metadata
        cognitive_diversity = manifest.get("metadata", {}).get(
            "cognitive_diversity", {}
        )
        if cognitive_diversity:
            total_personalities = cognitive_diversity.get(
                "total_personality_archetypes", 0
            )
            if total_personalities == 8:
                self.results.append(
                    ValidationResult(
                        "cognitive_diversity_metadata",
                        True,
                        "Cognitive diversity metadata correctly configured",
                    )
                )
            else:
                self.results.append(
                    ValidationResult(
                        "cognitive_diversity_metadata",
                        False,
                        f"Expected 8 personality archetypes, found {total_personalities}",
                    )
                )
        else:
            self.results.append(
                ValidationResult(
                    "cognitive_diversity_metadata",
                    False,
                    "Cognitive diversity metadata missing",
                )
            )

    def _validate_intelligence_features(self, manifest: Dict) -> None:
        """Validate intelligence features are properly configured."""
        intelligence_features = manifest.get("metadata", {}).get(
            "intelligence_features", {}
        )

        required_features = [
            "context_aware_selection",
            "personality_archetype_system",
            "parallel_reasoning",
            "intelligent_workflows",
            "think_tank_integration",
        ]

        missing_features = [
            feature
            for feature in required_features
            if not intelligence_features.get(feature)
        ]

        if missing_features:
            self.results.append(
                ValidationResult(
                    "intelligence_features",
                    False,
                    f"Missing or disabled intelligence features: {missing_features}",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "intelligence_features", True, "All intelligence features enabled"
                )
            )

    def _validate_workflows(self, manifest: Dict) -> None:
        """Validate workflow definitions and intelligence integration."""
        workflows = manifest.get("workflows", {})

        # Check for breakthrough innovation workflow
        if "breakthrough_innovation" in workflows:
            breakthrough = workflows["breakthrough_innovation"]
            intelligence = breakthrough.get("intelligence", {})

            if (
                intelligence.get("think_tank_activation") == "mandatory"
                and intelligence.get("personality_diversity") == "all_4_archetypes"
            ):
                self.results.append(
                    ValidationResult(
                        "breakthrough_workflow",
                        True,
                        "Breakthrough innovation workflow properly configured",
                    )
                )
            else:
                self.results.append(
                    ValidationResult(
                        "breakthrough_workflow",
                        False,
                        "Breakthrough innovation workflow missing proper intelligence configuration",
                    )
                )
        else:
            self.results.append(
                ValidationResult(
                    "breakthrough_workflow",
                    False,
                    "Breakthrough innovation workflow not found",
                )
            )

        # Validate workflow intelligence integration
        workflows_with_intelligence = sum(
            1 for w in workflows.values() if "intelligence" in w
        )
        total_workflows = len(workflows)

        if workflows_with_intelligence == total_workflows:
            self.results.append(
                ValidationResult(
                    "workflow_intelligence",
                    True,
                    f"All {total_workflows} workflows have intelligence integration",
                )
            )
        else:
            self.results.append(
                ValidationResult(
                    "workflow_intelligence",
                    False,
                    f"Only {workflows_with_intelligence}/{total_workflows} workflows have intelligence integration",
                )
            )

    def _validate_categories(self, manifest: Dict) -> None:
        """Validate category structure and completeness."""
        categories = manifest.get("categories", {})

        # Check for think-tank category
        if "thinktank" not in categories:
            self.results.append(
                ValidationResult(
                    "thinktank_category",
                    False,
                    "Think-tank category missing from categories",
                )
            )
        else:
            thinktank = categories["thinktank"]
            if "Diverse personality archetypes" in thinktank.get("description", ""):
                self.results.append(
                    ValidationResult(
                        "thinktank_category",
                        True,
                        "Think-tank category properly described",
                    )
                )
            else:
                self.results.append(
                    ValidationResult(
                        "thinktank_category",
                        False,
                        "Think-tank category description needs personality focus",
                    )
                )

    def generate_report(self) -> str:
        """Generate comprehensive validation report."""
        if not self.results:
            return "No validation results available. Run validations first."

        passed = sum(1 for r in self.results if r.passed)
        failed = len(self.results) - passed

        report = f"""
# 🛡️ Guardian Agents System Validation Report

**Validation Date**: {self._get_timestamp()}
**Total Checks**: {len(self.results)}
**Passed**: ✅ {passed}
**Failed**: ❌ {failed}
**Success Rate**: {passed/len(self.results)*100:.1f}%

## 📊 Validation Results

"""

        # Group results by status
        passed_results = [r for r in self.results if r.passed]
        failed_results = [r for r in self.results if not r.passed]

        if passed_results:
            report += "### ✅ Passed Validations\n\n"
            for result in passed_results:
                report += f"- **{result.check_name}**: {result.message}\n"
            report += "\n"

        if failed_results:
            report += "### ❌ Failed Validations\n\n"
            for result in failed_results:
                report += f"- **{result.check_name}**: {result.message}\n"
                if result.details:
                    report += f"  - Details: {result.details}\n"
            report += "\n"

        # Summary recommendations
        if failed_results:
            report += "## 🔧 Recommendations\n\n"
            for result in failed_results:
                report += f"**{result.check_name}**: Fix {result.message.lower()}\n"

        return report

    def _get_timestamp(self) -> str:
        """Get current timestamp for reports."""
        from datetime import datetime

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    """Main validation execution."""
    validator = GuardianAgentValidator()

    print("🔍 Running Guardian Agents System Validation...")
    results = validator.run_all_validations()

    # Generate and display report
    report = validator.generate_report()
    print(report)

    # Save report to file
    report_path = Path("validation-report.md")
    with open(report_path, "w") as f:
        f.write(report)

    print(f"📄 Full report saved to: {report_path}")

    # Exit with error code if any validations failed
    failed_count = sum(1 for r in results if not r.passed)
    if failed_count > 0:
        print(f"❌ {failed_count} validation(s) failed")
        sys.exit(1)
    else:
        print("✅ All validations passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
