#!/usr/bin/env python3
"""
Report Generation System for Guardian Agents Project
Generates weekly reports, milestone reports, and real-time dashboards
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict


class ReportGenerator:
    """Automated report generation system"""

    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root or os.getcwd())
        self.tracking_dir = self.project_root / "tracking"
        self.reports_dir = self.tracking_dir / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def load_progress(self) -> Dict:
        """Load current progress data"""
        progress_file = self.tracking_dir / "progress.json"
        if progress_file.exists():
            with open(progress_file) as f:
                return json.load(f)
        return {}

    def generate_weekly_report(self) -> str:
        """Generate weekly progress report with charts and metrics"""
        progress = self.load_progress()
        report_date = datetime.now()

        report = f"""# Weekly Progress Report - Week of {report_date.strftime('%Y-%m-%d')}

## 📊 Overall Progress
- **Project Completion**: {progress['project_status'].get('overall_completion', 0)}%
- **Current Phase**: {progress['project_status'].get('phase', 'Unknown')}
- **Last Updated**: {progress['project_status'].get('last_updated', 'Unknown')}

## 🎯 Epic Status
"""

        # Epic status
        for epic_id, epic in progress.get("epics", {}).items():
            completion = epic.get("completion_percentage", 0)
            status = epic.get("status", "unknown")
            features = epic.get("features", [])

            report += f"""
### {epic_id}: {epic.get('title', 'Untitled Epic')}
- **Status**: {status.title()}
- **Completion**: {completion}%
- **Features**: {len(features)} total
- **Priority**: {epic.get('priority', 'Unknown')}
"""

        # Feature progress
        report += """
## 🚀 Feature Progress
| Feature ID | Title | Status | Progress | Epic |
|------------|-------|--------|----------|------|
"""

        for feature_id, feature in progress.get("features", {}).items():
            title = feature.get("title", "Untitled")[:40]
            status = feature.get("status", "unknown")
            completion = feature.get("completion_percentage", 0)
            epic_id = feature.get("epic_id", "N/A")

            report += (
                f"| {feature_id} | {title} | {status} | {completion}% | {epic_id} |\n"
            )

        # This week's accomplishments (placeholder - would analyze git commits)
        report += """
## ✅ This Week's Accomplishments
- ✅ Completed comprehensive project management system design
- ✅ Created automated progress tracking infrastructure
- ✅ Established validation and accountability framework
- 🔄 Setting up automated progress tracking system

## 🚨 Blockers & Issues
"""

        blockers = progress.get("blockers", [])
        if blockers:
            for blocker in blockers:
                report += f"- **{blocker.get('type', 'Unknown').title()}**: {blocker.get('reason', blocker.get('dependency', 'Unknown issue'))}\n"
        else:
            report += "- No blockers this week\n"

        # Next week priorities
        report += """
## 📅 Next Week's Priorities
- Complete automated tracking system setup
- Begin implementation of intelligent agent orchestration engine
- Establish validation criteria for all outstanding features
- Set up continuous integration for progress tracking

## 📈 Key Metrics
"""

        metrics = progress.get("metrics", {})
        report += f"""- **Development Velocity**: {metrics.get('development_velocity', 0)} story points/week
- **Test Coverage**: {metrics.get('test_coverage', 0)}%
- **Code Quality Score**: {metrics.get('code_quality_score', 0)}/100
- **Documentation Completeness**: {metrics.get('documentation_completeness', 0)}%

---
*Report generated automatically on {report_date.isoformat()}*
"""

        # Save report
        report_file = (
            self.reports_dir / f"weekly-report-{report_date.strftime('%Y-%m-%d')}.md"
        )
        with open(report_file, "w") as f:
            f.write(report)

        return str(report_file)

    def generate_milestone_report(self, milestone_name: str = None) -> str:
        """Generate comprehensive milestone completion report"""
        progress = self.load_progress()
        report_date = datetime.now()

        if not milestone_name:
            milestone_name = f"Milestone-{report_date.strftime('%Y-%m-%d')}"

        report = f"""# Milestone Report: {milestone_name}

## 📊 Executive Summary
**Generated**: {report_date.strftime('%Y-%m-%d %H:%M:%S')}

### Overall Project Health
- **Completion**: {progress['project_status'].get('overall_completion', 0)}%
- **Active Epics**: {len([e for e in progress.get('epics', {}).values() if e.get('status') not in ['completed', 'cancelled']])}
- **Total Features**: {len(progress.get('features', {}))}
- **Completed Features**: {len([f for f in progress.get('features', {}).values() if f.get('status') == 'completed'])}

## 🎯 Epic Completion Status

"""

        for epic_id, epic in progress.get("epics", {}).items():
            completion = epic.get("completion_percentage", 0)
            status = epic.get("status", "unknown")
            effort_estimate = epic.get("effort_estimate", "Unknown")
            business_value = epic.get("business_value", "Unknown")

            # Calculate feature breakdown
            features = epic.get("features", [])
            feature_statuses = {}
            for fid in features:
                feature = progress.get("features", {}).get(fid, {})
                fstatus = feature.get("status", "unknown")
                feature_statuses[fstatus] = feature_statuses.get(fstatus, 0) + 1

            report += f"""### {epic_id}: {epic.get('title', 'Untitled')}
- **Status**: {status.title()}
- **Completion**: {completion}%
- **Business Value**: {business_value}
- **Effort Estimate**: {effort_estimate}
- **Features**: {len(features)} total
"""

            for status_name, count in feature_statuses.items():
                report += f"  - {status_name.replace('_', ' ').title()}: {count}\n"

            # Success metrics
            success_metrics = epic.get("success_metrics", {})
            if success_metrics:
                report += "- **Success Metrics**:\n"
                for metric, data in success_metrics.items():
                    target = data.get("target", "N/A")
                    current = data.get("current", 0)
                    unit = data.get("unit", "")
                    report += f"  - {metric.replace('_', ' ').title()}: {current}/{target} {unit}\n"

            report += "\n"

        # Detailed feature analysis
        report += """## 🚀 Feature Implementation Analysis

### Completed Features
"""
        completed_features = [
            f
            for f in progress.get("features", {}).values()
            if f.get("status") == "completed"
        ]
        if completed_features:
            for feature in completed_features:
                report += f"- **{feature.get('id', 'Unknown')}**: {feature.get('title', 'Untitled')}\n"
        else:
            report += "- No features completed yet\n"

        report += """
### In Progress Features
"""
        in_progress_features = [
            f
            for f in progress.get("features", {}).values()
            if f.get("status") == "in_progress"
        ]
        if in_progress_features:
            for feature in in_progress_features:
                completion = feature.get("completion_percentage", 0)
                report += f"- **{feature.get('id', 'Unknown')}**: {feature.get('title', 'Untitled')} ({completion}%)\n"
        else:
            report += "- No features currently in progress\n"

        # Risk assessment
        report += """
## 🚨 Risk Assessment

### Current Blockers
"""
        blockers = progress.get("blockers", [])
        if blockers:
            for blocker in blockers:
                report += f"- **{blocker.get('type', 'Unknown').title()}**: {blocker.get('reason', blocker.get('dependency', 'Unknown'))}\n"
        else:
            report += "- No current blockers identified\n"

        # Recommendations
        report += """
## 💡 Recommendations

### Immediate Actions Required
1. **Setup Validation Framework**: Establish automated testing for all implementation criteria
2. **Resource Allocation**: Assign development resources to high-priority features
3. **Dependency Resolution**: Address any blocking dependencies preventing progress

### Strategic Improvements
1. **Automated Progress Tracking**: Implement git-based progress tracking
2. **Continuous Integration**: Set up automated validation pipeline
3. **Stakeholder Communication**: Regular progress updates to maintain alignment

---
*Milestone report generated automatically on {report_date.isoformat()}*
"""

        # Save report
        report_file = (
            self.reports_dir
            / f"milestone-report-{milestone_name.lower().replace(' ', '-')}.md"
        )
        with open(report_file, "w") as f:
            f.write(report)

        return str(report_file)

    def generate_blockers_dashboard(self) -> str:
        """Generate real-time blockers and dependencies dashboard"""
        progress = self.load_progress()
        report_date = datetime.now()

        dashboard = f"""# Real-Time Blockers Dashboard

**Last Updated**: {report_date.strftime('%Y-%m-%d %H:%M:%S')}

## 🚨 Critical Blockers

"""

        blockers = progress.get("blockers", [])
        critical_blockers = [b for b in blockers if b.get("priority") == "critical"]

        if critical_blockers:
            for blocker in critical_blockers:
                dashboard += f"""### {blocker.get('type', 'Unknown').title()} Blocker
- **Issue**: {blocker.get('reason', 'Unknown')}
- **Affected**: {blocker.get('epic', blocker.get('id', 'Unknown'))}
- **Impact**: Critical - project cannot proceed
- **Required Action**: {blocker.get('required_action', 'Investigation needed')}

"""
        else:
            dashboard += "✅ No critical blockers currently identified\n\n"

        # All blockers
        dashboard += """## 📋 All Active Blockers

| Type | Issue | Affected | Priority | Status |
|------|-------|----------|----------|---------|
"""

        if blockers:
            for blocker in blockers:
                blocker_type = blocker.get("type", "Unknown")
                issue = blocker.get("reason", blocker.get("dependency", "Unknown"))[:50]
                affected = blocker.get("epic", blocker.get("id", "Unknown"))
                priority = blocker.get("priority", "medium")
                status = blocker.get("status", "active")

                dashboard += f"| {blocker_type} | {issue} | {affected} | {priority} | {status} |\n"
        else:
            dashboard += "| - | No blockers | - | - | - |\n"

        # Dependencies status
        dashboard += """
## 🔗 Dependency Status

### Epic Dependencies
"""

        for epic_id, epic in progress.get("epics", {}).items():
            dependencies = epic.get("dependencies", [])
            if dependencies:
                dashboard += f"\n#### {epic_id}: {epic.get('title', 'Untitled')}\n"
                for dep in dependencies:
                    # Check dependency status (placeholder logic)
                    status = (
                        "✅ Completed"
                        if dep == "GPM_VALIDATION_COMPLETE"
                        else "⏳ Pending"
                    )
                    dashboard += f"- {dep}: {status}\n"

        # Resource allocation
        dashboard += """
## 👥 Resource Allocation

### Features Needing Assignment
"""

        unassigned_features = [
            f
            for f in progress.get("features", {}).values()
            if not f.get("assignee") and f.get("status") != "completed"
        ]

        if unassigned_features:
            for feature in unassigned_features:
                priority = feature.get("priority", "medium")
                effort = feature.get("effort_estimate", "Unknown")
                dashboard += f"- **{feature.get('id')}**: {feature.get('title')} (Priority: {priority}, Effort: {effort})\n"
        else:
            dashboard += "✅ All active features have assigned resources\n"

        dashboard += f"""
---
*Dashboard auto-refreshed every hour. Last update: {report_date.isoformat()}*
"""

        # Save dashboard
        dashboard_file = self.reports_dir / "blockers-dashboard.md"
        with open(dashboard_file, "w") as f:
            f.write(dashboard)

        # Also generate HTML version for better visualization
        html_dashboard = self._generate_html_dashboard(dashboard)
        html_file = self.reports_dir / "blockers-dashboard.html"
        with open(html_file, "w") as f:
            f.write(html_dashboard)

        return str(dashboard_file)

    def _generate_html_dashboard(self, markdown_content: str) -> str:
        """Convert markdown dashboard to HTML with styling"""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Guardian Agents - Blockers Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .status-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .status-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-left: 4px solid #007bff;
        }}
        .status-card.critical {{
            border-left-color: #dc3545;
        }}
        .status-card.warning {{
            border-left-color: #ffc107;
        }}
        .status-card.success {{
            border-left-color: #28a745;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f8f9fa;
            font-weight: 600;
        }}
        .priority-high {{ color: #dc3545; font-weight: bold; }}
        .priority-critical {{ color: #721c24; font-weight: bold; }}
        .priority-medium {{ color: #6c757d; }}
        .priority-low {{ color: #28a745; }}
        .auto-refresh {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #007bff;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 12px;
        }}
    </style>
    <script>
        // Auto-refresh every 5 minutes
        setTimeout(() => location.reload(), 300000);
    </script>
</head>
<body>
    <div class="auto-refresh">
        🔄 Auto-refresh: 5 min
    </div>

    <div class="header">
        <h1>🚨 Guardian Agents - Blockers Dashboard</h1>
        <p>Real-time project status and blocker tracking</p>
        <p><strong>Last Updated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

    <div class="status-grid">
        <div class="status-card success">
            <h3>✅ Project Health</h3>
            <p>Overall system operational</p>
        </div>
        <div class="status-card warning">
            <h3>⏳ Pending Actions</h3>
            <p>Implementation phase starting</p>
        </div>
        <div class="status-card">
            <h3>📊 Progress Tracking</h3>
            <p>Automated system active</p>
        </div>
    </div>

    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <pre style="white-space: pre-wrap; font-family: inherit;">{markdown_content}</pre>
    </div>
</body>
</html>"""

        return html


def main():
    """CLI interface for report generation"""
    if len(sys.argv) < 2:
        print("Usage: python generate-reports.py <command> [args...]")
        print("Commands:")
        print("  weekly                    - Generate weekly progress report")
        print("  milestone [name]          - Generate milestone report")
        print("  blockers                  - Generate blockers dashboard")
        print("  all                       - Generate all reports")
        return

    generator = ReportGenerator()
    command = sys.argv[1]

    if command == "weekly":
        report_file = generator.generate_weekly_report()
        print(f"Weekly report generated: {report_file}")

    elif command == "milestone":
        milestone_name = sys.argv[2] if len(sys.argv) > 2 else None
        if milestone_name is not None:
            report_file = generator.generate_milestone_report(milestone_name)
            print(f"Milestone report generated: {report_file}")

    elif command == "blockers":
        dashboard_file = generator.generate_blockers_dashboard()
        print(f"Blockers dashboard generated: {dashboard_file}")

    elif command == "all":
        weekly_file = generator.generate_weekly_report()
        milestone_file = generator.generate_milestone_report()
        dashboard_file = generator.generate_blockers_dashboard()
        print("All reports generated:")
        print(f"  Weekly: {weekly_file}")
        print(f"  Milestone: {milestone_file}")
        print(f"  Dashboard: {dashboard_file}")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
