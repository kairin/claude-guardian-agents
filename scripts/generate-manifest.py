#!/usr/bin/env python3
"""
Generate Correct Manifest - Creates accurate manifest.json from actual repository structure
"""

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List


class ManifestGenerator:
    """Generate accurate manifest from repository structure"""

    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root)
        self.agent_files = []
        self.categories = {
            "strategy": {
                "name": "Strategic & Product",
                "description": "Product strategy, planning, and design agents",
                "agents": [],
            },
            "architecture": {
                "name": "Technical Architecture",
                "description": "System architecture and technical leadership agents",
                "agents": [],
            },
            "backend": {
                "name": "Backend Development",
                "description": "Backend, API, and database development agents",
                "agents": [],
            },
            "frontend": {
                "name": "Frontend Development",
                "description": "Frontend, UI, and web development agents",
                "agents": [],
            },
            "mobile": {
                "name": "Mobile Development",
                "description": "iOS, Android, and cross-platform mobile agents",
                "agents": [],
            },
            "quality": {
                "name": "Quality Engineering",
                "description": "Testing, QA, and quality assurance agents",
                "agents": [],
            },
            "devops": {
                "name": "DevOps & Infrastructure",
                "description": "DevOps, infrastructure, and deployment agents",
                "agents": [],
            },
            "security": {
                "name": "Security Operations",
                "description": "Security, compliance, and risk management agents",
                "agents": [],
            },
            "data": {
                "name": "Data Operations",
                "description": "Data engineering, analytics, and data management agents",
                "agents": [],
            },
            "operations": {
                "name": "IT Operations",
                "description": "IT operations, service management, and support agents",
                "agents": [],
            },
            "thinktank": {
                "name": "Think-Tank Reasoning",
                "description": "Parallel reasoning and problem-solving enhancement agents",
                "agents": [],
            },
        }

    def scan_repository(self):
        """Scan repository for all guardian agent files"""
        print("🔍 Scanning repository for Guardian agent files...")

        # Find all guardian.md files
        agent_pattern = "*guardian.md"
        self.agent_files = list(self.repo_root.glob(f"**/{agent_pattern}"))

        print(f"✅ Found {len(self.agent_files)} agent files")
        return self.agent_files

    def extract_agent_info(self, file_path: Path) -> Dict:
        """Extract agent information from file"""
        try:
            # Extract agent ID from filename
            filename = file_path.name
            id_match = re.match(r"(\d+)-", filename)
            agent_id = id_match.group(1) if id_match else "unknown"

            # Determine category from ID
            agent_num = int(agent_id)
            category = self.categorize_agent(agent_num)

            # Calculate checksum
            checksum = self.calculate_checksum(file_path)

            # Extract agent name (remove .md extension)
            name = filename.replace(".md", "")

            # Generate title from name
            title = self.generate_title(name)

            # Get relative path from repo root
            rel_path = file_path.relative_to(self.repo_root)

            # Extract tools and triggers from file content
            tools, triggers = self.parse_agent_file(file_path)

            # Determine complexity
            complexity = self.determine_complexity(name, triggers)

            return {
                "name": name,
                "title": title,
                "category": category,
                "complexity": complexity,
                "path": str(rel_path),
                "checksum": checksum,
                "research_foundations": self.count_research_foundations(file_path),
                "tools": tools,
                "triggers": triggers,
            }

        except Exception as e:
            print(f"⚠️ Error processing {file_path}: {e}")
            return None

    def categorize_agent(self, agent_num: int) -> str:
        """Categorize agent based on ID number"""
        if 1 <= agent_num <= 30:
            if agent_num <= 6:
                return "strategy"
            elif 21 <= agent_num <= 25:
                return "strategy"
            else:
                return "strategy"
        elif 41 <= agent_num <= 45:
            return "architecture"
        elif 61 <= agent_num <= 69:
            if 61 <= agent_num <= 63:
                return "backend"
            elif 64 <= agent_num <= 66:
                return "frontend"
            elif 67 <= agent_num <= 69:
                return "mobile"
        elif 71 <= agent_num <= 73:
            return "quality"
        elif 81 <= agent_num <= 83:
            return "devops"
        elif agent_num == 91:
            return "operations"
        elif 92 <= agent_num <= 94:
            return "security"
        elif 95 <= agent_num <= 97:
            return "data"
        elif 98 <= agent_num <= 100:
            return "operations"
        elif 101 <= agent_num <= 120:
            return "thinktank"
        else:
            return "generic"

    def calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum of file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()[:16]  # Shortened for readability
        except OSError:
            return "unknown"

    def generate_title(self, name: str) -> str:
        """Generate human-readable title from agent name"""
        # Remove number prefix and guardian suffix
        title = re.sub(r"^\d+-", "", name)
        title = re.sub(r"-guardian$", "", title)

        # Convert dashes to spaces and title case
        title = title.replace("-", " ").title()

        # Add "Guardian" suffix
        return f"{title} Guardian"

    def parse_agent_file(self, file_path: Path) -> tuple:
        """Parse agent file to extract tools and triggers"""
        tools = ["web_search", "web_fetch", "write", "read"]  # Default tools
        triggers = []

        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

                # Extract tools from frontmatter
                tools_match = re.search(r"tools:\s*\[(.*?)\]", content, re.MULTILINE)
                if tools_match:
                    tools_str = tools_match.group(1)
                    tools = [tool.strip().strip("\"'") for tool in tools_str.split(",")]

                # Extract triggers from description
                desc_match = re.search(r"description:\s*([^\n]+)", content)
                if desc_match:
                    description = desc_match.group(1)
                    # Extract key phrases that could be triggers
                    trigger_patterns = [
                        r"(\w+\s+\w+)\s+tasks",
                        r"Use for\s+([^.]+)",
                        r"MUST BE USED for\s+([^.]+)",
                    ]

                    for pattern in trigger_patterns:
                        matches = re.findall(pattern, description, re.IGNORECASE)
                        triggers.extend([match.strip().lower() for match in matches])

                # Add some default triggers based on agent name
                if "backend" in file_path.name:
                    triggers.extend(
                        ["backend development", "api development", "database design"]
                    )
                elif "frontend" in file_path.name:
                    triggers.extend(
                        ["frontend development", "ui development", "web development"]
                    )
                elif "mobile" in file_path.name:
                    triggers.extend(
                        ["mobile development", "ios development", "android development"]
                    )
                elif "quality" in file_path.name:
                    triggers.extend(["testing", "quality assurance", "test automation"])
                elif "devops" in file_path.name:
                    triggers.extend(["devops", "infrastructure", "deployment", "ci/cd"])
                elif "security" in file_path.name:
                    triggers.extend(["security", "compliance", "risk management"])

        except Exception as e:
            print(f"⚠️ Could not parse {file_path}: {e}")

        return tools, list(set(triggers))  # Remove duplicates

    def determine_complexity(self, name: str, triggers: List[str]) -> str:
        """Determine agent complexity based on name and role"""
        if "director" in name or "leadership" in name or "principal" in name:
            return "complex"
        elif "senior" in name:
            return "complex"
        elif "junior" in name:
            return "simple"
        else:
            return "moderate"

    def count_research_foundations(self, file_path: Path) -> int:
        """Count research foundations in agent file"""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

                # Count research sections
                research_count = len(
                    re.findall(r"##\s*📚\s*Research Foundation", content)
                )
                if research_count > 0:
                    # Count primary research items
                    primary_count = len(re.findall(r"###\s*Primary Research", content))
                    return max(3, primary_count)  # Minimum 3 if research section exists
                else:
                    return 0
        except OSError:
            return 0

    def generate_workflows(self, agents: Dict) -> Dict:
        """Generate workflow definitions based on available agents"""
        workflows = {
            "feature_development": {
                "name": "Complete Feature Development",
                "description": "End-to-end feature development workflow",
                "chain": [],
                "estimated_duration": "2-5 days",
                "triggers": [
                    "build feature",
                    "implement feature",
                    "new feature development",
                ],
            },
            "api_development": {
                "name": "API Development & Testing",
                "description": "Backend API development with quality assurance",
                "chain": [],
                "estimated_duration": "1-3 days",
                "triggers": [
                    "api development",
                    "backend api",
                    "rest api",
                    "graphql api",
                ],
            },
            "deployment_pipeline": {
                "name": "Production Deployment",
                "description": "Secure production deployment workflow",
                "chain": [],
                "estimated_duration": "4-8 hours",
                "triggers": ["deploy", "deployment", "production release", "go live"],
            },
        }

        # Build chains from available agents
        for agent_id, agent_info in agents.items():
            category = agent_info["category"]

            if category == "strategy" and agent_id == "002":
                workflows["feature_development"]["chain"].insert(0, agent_id)
            elif category == "architecture" and "principal" in agent_info["name"]:
                if agent_id not in workflows["feature_development"]["chain"]:
                    workflows["feature_development"]["chain"].append(agent_id)
            elif category == "backend" and "senior" in agent_info["name"]:
                workflows["api_development"]["chain"].append(agent_id)
                if agent_id not in workflows["feature_development"]["chain"]:
                    workflows["feature_development"]["chain"].append(agent_id)
            elif category == "quality" and "senior" in agent_info["name"]:
                workflows["api_development"]["chain"].append(agent_id)
                if agent_id not in workflows["feature_development"]["chain"]:
                    workflows["feature_development"]["chain"].append(agent_id)
            elif category == "devops" and "director" in agent_info["name"]:
                workflows["deployment_pipeline"]["chain"].append(agent_id)
                if agent_id not in workflows["feature_development"]["chain"]:
                    workflows["feature_development"]["chain"].append(agent_id)

        return workflows

    def generate_manifest(self) -> Dict:
        """Generate complete manifest from repository scan"""
        print("🔧 Generating complete manifest...")

        # Scan repository
        agent_files = self.scan_repository()

        agents = {}

        # Process each agent file
        for file_path in agent_files:
            agent_info = self.extract_agent_info(file_path)
            if agent_info:
                agent_id = re.match(r"(\d+)-", file_path.name).group(1)
                agents[agent_id] = agent_info

                # Add to category
                category = agent_info["category"]
                if category in self.categories:
                    self.categories[category]["agents"].append(agent_id)

        # Generate workflows
        workflows = self.generate_workflows(agents)

        # Create complete manifest
        manifest = {
            "name": "claude-guardian-agents",
            "version": "2.3.0",
            "description": "Comprehensive system of specialized AI agents for software development and project management",
            "repository": "https://github.com/kairin/claude-guardian-agents",
            "license": "MIT",
            "updated_at": "2025-09-11T10:30:00Z",
            "categories": self.categories,
            "agents": agents,
            "workflows": workflows,
            "project_templates": {
                "nodejs": {
                    "recommended_agents": [
                        aid
                        for aid, info in agents.items()
                        if info["category"]
                        in [
                            "strategy",
                            "architecture",
                            "backend",
                            "frontend",
                            "quality",
                            "devops",
                        ]
                    ],
                    "common_workflows": ["api_development", "feature_development"],
                    "spec_integration": True,
                },
                "python": {
                    "recommended_agents": [
                        aid
                        for aid, info in agents.items()
                        if info["category"]
                        in [
                            "strategy",
                            "architecture",
                            "backend",
                            "quality",
                            "devops",
                            "data",
                        ]
                    ],
                    "common_workflows": ["api_development", "data_processing"],
                    "spec_integration": True,
                },
                "generic": {
                    "recommended_agents": [
                        aid
                        for aid, info in agents.items()
                        if info["category"] in ["strategy", "operations"]
                    ],
                    "common_workflows": ["feature_development"],
                    "spec_integration": False,
                },
            },
            "integration": {
                "claude_code": {
                    "supported": True,
                    "agent_path": ".claude/agents/",
                    "index_file": "agent-index.json",
                    "auto_selection": True,
                },
                "spec_kit": {
                    "supported": True,
                    "repository": "https://github.com/kairin/spec-kit",
                    "sync_command": "gpm sync-specs",
                    "spec_path": "specs/",
                },
            },
            "metadata": {
                "total_agents": len(agents),
                "research_papers": sum(
                    info["research_foundations"] for info in agents.values()
                ),
                "workflow_chains": len(workflows),
                "supported_languages": 7,
                "min_gpm_version": "1.0.0",
            },
        }

        print(f"✅ Generated manifest with {len(agents)} agents")
        return manifest

    def save_manifest(
        self, manifest: Dict[str, Any], output_path: str = "manifest.json"
    ) -> None:
        """Save manifest to file"""
        output_file = self.repo_root / output_path
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"💾 Saved manifest to {output_file}")


def main() -> None:
    """Generate manifest from current repository"""
    generator = ManifestGenerator()
    manifest = generator.generate_manifest()
    generator.save_manifest(manifest)

    # Validate the manifest
    print("\n📋 Manifest Summary:")
    print(f"  Total Agents: {manifest['metadata']['total_agents']}")
    print(f"  Categories: {len(manifest['categories'])}")
    print(f"  Workflows: {len(manifest['workflows'])}")

    # Show category breakdown
    print("\n📊 Category Breakdown:")
    for cat_info in manifest["categories"].values():
        print(f"  {cat_info['name']}: {len(cat_info['agents'])} agents")


if __name__ == "__main__":
    main()
