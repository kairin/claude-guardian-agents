#!/usr/bin/env python3
"""
Progress Tracking System for Guardian Agents Project
Automatically tracks progress, validates implementations, and generates reports
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class ProgressTracker:
    """Main progress tracking system"""

    def __init__(self, project_root: str | None = None):
        self.project_root = Path(project_root or os.getcwd())
        self.tracking_dir = self.project_root / "tracking"
        self.progress_file = self.tracking_dir / "progress.json"
        self.specs_dir = self.project_root / "specs"

    def load_progress(self) -> dict[str, Any]:
        """Load current progress data"""
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return json.load(f)
        return self._initialize_progress()

    def save_progress(self, progress_data: dict) -> None:
        """Save progress data with timestamp"""
        progress_data["project_status"]["last_updated"] = datetime.now().isoformat()
        with open(self.progress_file, "w") as f:
            json.dump(progress_data, f, indent=2)

    def update_feature_status(
        self, feature_id: str, status: str, notes: str | None = None
    ) -> None:
        """Update feature status with timestamp and notes"""
        progress = self.load_progress()

        if feature_id not in progress["features"]:
            print(f"Feature {feature_id} not found")
            return

        progress["features"][feature_id]["status"] = status
        progress["features"][feature_id]["last_updated"] = datetime.now().isoformat()

        if notes:
            if "notes" not in progress["features"][feature_id]:
                progress["features"][feature_id]["notes"] = []
            progress["features"][feature_id]["notes"].append(
                {"timestamp": datetime.now().isoformat(), "note": notes}
            )

        # Update completion percentage based on checklist
        self._calculate_feature_completion(progress, feature_id)

        self.save_progress(progress)
        print(f"Updated {feature_id} status to: {status}")

    def update_task_completion(
        self, feature_id: str, task_name: str, completed: bool
    ) -> None:
        """Update individual task completion in feature checklist"""
        progress = self.load_progress()

        if feature_id in progress["features"]:
            checklist = progress["features"][feature_id]["implementation_checklist"]
            if task_name in checklist:
                checklist[task_name] = completed
                self._calculate_feature_completion(progress, feature_id)
                self.save_progress(progress)
                print(
                    f"Task '{task_name}' marked as {'completed' if completed else 'pending'}"
                )
            else:
                print(f"Task '{task_name}' not found in feature {feature_id}")
        else:
            print(f"Feature {feature_id} not found")

    def calculate_completion_percentage(self) -> dict:
        """Calculate overall and per-epic completion rates"""
        progress = self.load_progress()

        # Calculate overall completion
        total_features = len(progress["features"])
        completed_features = sum(
            1 for f in progress["features"].values() if f["status"] == "completed"
        )

        overall_completion = (
            (completed_features / total_features * 100) if total_features > 0 else 0
        )

        # Calculate per-epic completion
        epic_completion = {}
        for epic_id, epic in progress["epics"].items():
            epic_features = epic.get("features", [])
            if epic_features:
                epic_completed = sum(
                    1
                    for fid in epic_features
                    if progress["features"].get(fid, {}).get("status") == "completed"
                )
                epic_completion[epic_id] = (epic_completed / len(epic_features)) * 100
            else:
                epic_completion[epic_id] = 0

        # Update progress data
        progress["project_status"]["overall_completion"] = int(overall_completion)
        for epic_id, completion in epic_completion.items():
            progress["epics"][epic_id]["completion_percentage"] = int(completion)

        self.save_progress(progress)

        return {
            "overall_completion": overall_completion,
            "epic_completion": epic_completion,
            "total_features": total_features,
            "completed_features": completed_features,
        }

    def generate_blockers_report(self) -> list[dict]:
        """Identify blocked tasks and their dependencies"""
        progress = self.load_progress()
        blockers = []

        # Check for blocked features
        for feature_id, feature in progress["features"].items():
            if feature["status"] == "blocked":
                blockers.append(
                    {
                        "type": "feature",
                        "id": feature_id,
                        "title": feature["title"],
                        "epic": feature["epic_id"],
                        "blocked_since": feature.get("blocked_since"),
                        "reason": feature.get("blocked_reason", "Unknown"),
                    }
                )

        # Check dependencies
        for epic_id, epic in progress["epics"].items():
            for dep in epic.get("dependencies", []):
                if not self._check_dependency_satisfied(dep):
                    blockers.append(
                        {
                            "type": "dependency",
                            "epic": epic_id,
                            "dependency": dep,
                            "blocking": "Epic cannot start until dependency resolved",
                        }
                    )

        # Add to progress data
        progress["blockers"] = blockers
        self.save_progress(progress)

        return blockers

    def validate_implementation(self, feature_id: str) -> dict:
        """Run automated tests and validation for a feature"""
        progress = self.load_progress()

        if feature_id not in progress["features"]:
            return {"error": f"Feature {feature_id} not found"}

        feature = progress["features"][feature_id]
        validation_results = {
            "feature_id": feature_id,
            "timestamp": datetime.now().isoformat(),
            "validation_criteria": [],
            "test_results": {},
            "overall_status": "unknown",
        }

        # Check validation criteria
        criteria = feature.get("validation_criteria", [])
        for criterion in criteria:
            # This would contain actual validation logic
            result = self._validate_criterion(feature_id, criterion)
            validation_results["validation_criteria"].append(
                {
                    "criterion": criterion,
                    "passed": result,
                    "details": f"Validation for: {criterion}",
                }
            )

        # Run tests if implementation exists
        test_results = self._run_feature_tests(feature_id)
        validation_results["test_results"] = test_results

        # Determine overall status
        all_criteria_passed = all(
            vc["passed"] for vc in validation_results["validation_criteria"]
        )
        tests_passed = test_results.get("all_passed", False)

        if all_criteria_passed and tests_passed:
            validation_results["overall_status"] = "passed"
        elif not all_criteria_passed:
            validation_results["overall_status"] = "criteria_failed"
        else:
            validation_results["overall_status"] = "tests_failed"

        # Save validation results
        results_file = (
            self.tracking_dir / "validation-results" / f"{feature_id}_validation.json"
        )
        results_file.parent.mkdir(parents=True, exist_ok=True)
        with open(results_file, "w") as f:
            json.dump(validation_results, f, indent=2)

        return validation_results

    def add_feature(self, feature_data: dict) -> None:
        """Add a new feature to tracking"""
        progress = self.load_progress()

        feature_id = feature_data["id"]
        progress["features"][feature_id] = {
            **feature_data,
            "status": "not_started",
            "completion_percentage": 0,
            "created": datetime.now().isoformat(),
            "implementation_checklist": feature_data.get(
                "implementation_checklist",
                {
                    "requirements_analysis": False,
                    "technical_design": False,
                    "core_implementation": False,
                    "unit_tests": False,
                    "integration_tests": False,
                    "documentation": False,
                    "stakeholder_review": False,
                },
            ),
        }

        # Add to epic's feature list
        epic_id = feature_data.get("epic_id")
        if epic_id and epic_id in progress["epics"]:
            if "features" not in progress["epics"][epic_id]:
                progress["epics"][epic_id]["features"] = []
            if feature_id not in progress["epics"][epic_id]["features"]:
                progress["epics"][epic_id]["features"].append(feature_id)

        self.save_progress(progress)
        print(f"Added feature {feature_id}: {feature_data.get('title', 'Untitled')}")

    def _initialize_progress(self) -> dict:
        """Initialize default progress structure"""
        return {
            "project_status": {
                "overall_completion": 0,
                "last_updated": datetime.now().isoformat(),
                "phase": "planning",
            },
            "epics": {},
            "features": {},
            "tasks": {},
            "blockers": [],
            "metrics": {
                "development_velocity": 0,
                "test_coverage": 0,
                "code_quality_score": 0,
                "documentation_completeness": 0,
            },
        }

    def _calculate_feature_completion(
        self, progress: dict[str, Any], feature_id: str
    ) -> None:
        """Calculate feature completion based on implementation checklist"""
        feature = progress["features"][feature_id]
        checklist = feature.get("implementation_checklist", {})

        if checklist:
            completed_tasks = sum(1 for completed in checklist.values() if completed)
            total_tasks = len(checklist)
            completion = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            feature["completion_percentage"] = int(completion)

            # Auto-update status based on completion
            if completion == 100 and feature["status"] != "completed":
                feature["status"] = "ready_for_review"
            elif completion > 0 and feature["status"] == "not_started":
                feature["status"] = "in_progress"

    def _validate_criterion(self, feature_id: str, criterion: str) -> bool:
        """Validate a specific criterion (placeholder implementation)"""
        # This would contain actual validation logic
        # For now, return False to indicate not yet implemented
        return False

    def _run_feature_tests(self, feature_id: str) -> dict[str, Any]:
        """Run tests for a specific feature"""
        # Placeholder implementation
        return {
            "unit_tests": {"passed": 0, "failed": 0, "total": 0},
            "integration_tests": {"passed": 0, "failed": 0, "total": 0},
            "all_passed": False,
        }

    def _check_dependency_satisfied(self, dependency: str) -> bool:
        """Check if a dependency is satisfied"""
        # Placeholder implementation
        dependency_status = {
            "GPM_VALIDATION_COMPLETE": True,  # We completed this
            "AGENT_METADATA_ENRICHMENT": False,
            "CLAUDE_CODE_INTEGRATION": False,
        }
        return dependency_status.get(dependency, False)


def main() -> None:
    """CLI interface for progress tracking"""
    if len(sys.argv) < 2:
        print("Usage: python track-progress.py <command> [args...]")
        print("Commands:")
        print("  update-feature <feature_id> <status> [notes]")
        print("  complete-task <feature_id> <task_name>")
        print("  calculate-completion")
        print("  generate-blockers")
        print("  validate <feature_id>")
        return

    tracker = ProgressTracker()
    command = sys.argv[1]

    if command == "update-feature":
        if len(sys.argv) < 4:
            print("Usage: update-feature <feature_id> <status> [notes]")
            return
        feature_id = sys.argv[2]
        status = sys.argv[3]
        notes = sys.argv[4] if len(sys.argv) > 4 else None
        if notes is not None:
            tracker.update_feature_status(feature_id, status, notes)

    elif command == "complete-task":
        if len(sys.argv) < 4:
            print("Usage: complete-task <feature_id> <task_name>")
            return
        feature_id = sys.argv[2]
        task_name = sys.argv[3]
        tracker.update_task_completion(feature_id, task_name, True)

    elif command == "calculate-completion":
        results = tracker.calculate_completion_percentage()
        print(f"Overall completion: {results['overall_completion']:.1f}%")
        print(f"Features: {results['completed_features']}/{results['total_features']}")
        for epic_id, completion in results["epic_completion"].items():
            print(f"Epic {epic_id}: {completion:.1f}%")
        sys.exit(0)

    elif command == "generate-blockers":
        blockers = tracker.generate_blockers_report()
        if blockers:
            print("Current blockers:")
            for blocker in blockers:
                print(
                    f"  - {blocker['type']}: {blocker.get('title', blocker.get('dependency'))}"
                )
        else:
            print("No blockers found")

    elif command == "validate":
        if len(sys.argv) < 3:
            print("Usage: validate <feature_id>")
            return
        feature_id = sys.argv[2]
        results = tracker.validate_implementation(feature_id)
        print(f"Validation results for {feature_id}: {results['overall_status']}")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
