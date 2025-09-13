#!/usr/bin/env python3
"""
Script to reorganize SVG files in the claude-guardian-agents project.
This script:
1. Extracts inline SVGs from markdown files to external files
2. Creates proper directory structure mirroring document locations
3. Updates all markdown references to use consistent paths
4. Creates placeholder SVGs for missing images
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

# Project root
PROJECT_ROOT = Path("/home/kkk/Apps/claude-guardian-agents")
ASSETS_DIR = PROJECT_ROOT / "assets"


def extract_inline_svg(content: str) -> Tuple[str, str]:
    """Extract inline SVG from markdown content."""
    # Check if content starts with SVG
    if content.strip().startswith("<svg"):
        # Find the end of SVG
        svg_end = content.find("</svg>") + 6
        if svg_end > 6:
            svg_content = content[:svg_end]
            remaining_content = content[svg_end:].strip()
            return svg_content, remaining_content
    return "", content


def get_svg_path_for_document(doc_path: Path) -> Path:
    """Generate the appropriate SVG path for a document."""
    # Get relative path from project root
    rel_path = doc_path.relative_to(PROJECT_ROOT)

    # Convert document path to assets path
    # e.g., 1-product/1-product-management/001-xxx.md -> assets/1-product/1-product-management/001-xxx.svg
    svg_name = doc_path.stem + ".svg"

    # Build the assets path mirroring the document structure
    parts = list(rel_path.parts[:-1])  # Remove filename
    assets_path = ASSETS_DIR / Path(*parts) / svg_name

    return assets_path


def get_relative_svg_reference(doc_path: Path, svg_path: Path) -> str:
    """Calculate the relative path from document to SVG."""
    # Get the directory of the document
    doc_dir = doc_path.parent

    # Calculate relative path from doc directory to svg
    try:
        rel_path = os.path.relpath(svg_path, doc_dir)
        return rel_path
    except ValueError:
        # If on different drives, use absolute path
        return str(svg_path)


def process_guardian_file(file_path: Path, dry_run: bool = False) -> Dict:
    """Process a single guardian markdown file."""
    result = {
        "file": str(file_path),
        "has_inline_svg": False,
        "has_svg_reference": False,
        "svg_extracted": False,
        "reference_updated": False,
        "svg_created": False,
        "error": None,
    }

    try:
        # Read the file
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Check for inline SVG
        svg_content, remaining_content = extract_inline_svg(content)
        if svg_content:
            result["has_inline_svg"] = True

            # Generate SVG path
            svg_path = get_svg_path_for_document(file_path)

            if not dry_run:
                # Create directory if needed
                svg_path.parent.mkdir(parents=True, exist_ok=True)

                # Write SVG to file
                with open(svg_path, "w", encoding="utf-8") as f:
                    f.write(svg_content)

                result["svg_extracted"] = True

                # Update content to remove inline SVG and add reference
                relative_path = get_relative_svg_reference(file_path, svg_path)
                new_reference = f"![Agent Image]({relative_path})\n\n"
                content = new_reference + remaining_content

        # Check for existing SVG reference
        svg_pattern = r"!\[.*?\]\((.*?\.svg)\)"
        svg_match = re.search(svg_pattern, content)
        if svg_match:
            result["has_svg_reference"] = True
            old_path = svg_match.group(1)

            # Calculate what the correct path should be
            svg_path = get_svg_path_for_document(file_path)
            correct_relative_path = get_relative_svg_reference(file_path, svg_path)

            # Update if different
            if old_path != correct_relative_path:
                content = re.sub(
                    svg_pattern,
                    f"![Agent Image]({correct_relative_path})",
                    content,
                    count=1,
                )
                result["reference_updated"] = True

        # If no SVG at all, add reference for placeholder
        if not result["has_inline_svg"] and not result["has_svg_reference"]:
            svg_path = get_svg_path_for_document(file_path)
            relative_path = get_relative_svg_reference(file_path, svg_path)

            # Add reference at the beginning of the file (after frontmatter if exists)
            if content.startswith("---"):
                # Find end of frontmatter
                end_frontmatter = content.find("---", 3)
                if end_frontmatter > 0:
                    frontmatter = content[: end_frontmatter + 3]
                    body = content[end_frontmatter + 3 :].lstrip()
                    content = (
                        frontmatter + f"\n\n![Agent Image]({relative_path})\n\n" + body
                    )
            else:
                content = f"![Agent Image]({relative_path})\n\n" + content

            result["reference_updated"] = True

        # Write updated content if changed
        if not dry_run and content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

    except Exception as e:
        result["error"] = str(e)

    return result


def reorganize_existing_svgs(dry_run: bool = False) -> List[Dict]:
    """Reorganize existing SVG files to mirror document structure."""
    results = []

    # Get all existing SVGs
    existing_svgs = list(ASSETS_DIR.glob("**/*.svg"))

    for svg_file in existing_svgs:
        result = {
            "original": str(svg_file),
            "new_location": None,
            "moved": False,
            "error": None,
        }

        try:
            # Extract the agent ID from the filename
            svg_name = svg_file.name
            agent_id = svg_name.split("-")[0] if "-" in svg_name else None

            if agent_id:
                # Find the corresponding markdown file
                pattern = f"**/{svg_name.replace('.svg', '.md')}"
                matching_docs = list(PROJECT_ROOT.glob(pattern))

                if matching_docs:
                    doc_path = matching_docs[0]
                    new_svg_path = get_svg_path_for_document(doc_path)

                    result["new_location"] = str(new_svg_path)

                    if svg_file != new_svg_path:
                        if not dry_run:
                            # Create directory if needed
                            new_svg_path.parent.mkdir(parents=True, exist_ok=True)

                            # Move the file
                            shutil.move(str(svg_file), str(new_svg_path))
                            result["moved"] = True

        except Exception as e:
            result["error"] = str(e)

        results.append(result)

    return results


def create_placeholder_svg(agent_name: str, agent_type: str) -> str:
    """Create a placeholder SVG for agents without images."""
    colors = {
        "product": ("#4A90E2", "#00408B", "#F8E71C", "#F5A623"),
        "engineering": ("#50E3C2", "#00664E", "#BDC3C7", "#95A5A6"),
        "operations": ("#FF6B6B", "#8B0000", "#FFD93D", "#F5A623"),
        "thinktank": ("#9013FE", "#4A0088", "#FFFFFF", "#E0E0E0"),
    }

    # Determine type from agent name
    if (
        "operations" in agent_name.lower()
        or "security" in agent_name.lower()
        or "data" in agent_name.lower()
    ):
        color_set = colors["operations"]
    elif "thinktank" in agent_name.lower() or "think" in agent_name.lower():
        color_set = colors["thinktank"]
    elif (
        "development" in agent_name.lower()
        or "architecture" in agent_name.lower()
        or "infrastructure" in agent_name.lower()
    ):
        color_set = colors["engineering"]
    else:
        color_set = colors["product"]

    return f"""<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <defs>
    <linearGradient id="main-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color_set[0]};" />
      <stop offset="100%" style="stop-color:{color_set[1]};" />
    </linearGradient>
    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color_set[2]};" />
      <stop offset="100%" style="stop-color:{color_set[3]};" />
    </linearGradient>
  </defs>
  <!-- Placeholder for {agent_name} -->
  <rect x="150" y="85" width="100" height="50" fill="url(#main-grad)" stroke="#000" stroke-width="2"/>
  <circle cx="200" cy="110" r="15" fill="url(#accent-grad)" stroke="#000" stroke-width="1.5"/>
  <text x="200" y="115" text-anchor="middle" fill="#fff" font-family="monospace" font-size="12">TBD</text>
</svg>"""


def main(dry_run: bool = False) -> None:
    """Main execution function."""
    print("Starting SVG reorganization...")

    # Step 1: Process all guardian markdown files
    print("\n1. Processing guardian files...")
    guardian_files: List[Path] = []
    for pattern in [
        "1-product/**/*.md",
        "2-engineering/**/*.md",
        "3-operations/**/*.md",
        "4-thinktank/**/*.md",
    ]:
        guardian_files.extend(PROJECT_ROOT.glob(pattern))

    # Filter out non-guardian files
    guardian_files = [f for f in guardian_files if re.match(r"\d{3}-", f.name)]

    process_results = []
    for file_path in guardian_files:
        result = process_guardian_file(file_path, dry_run)
        process_results.append(result)

        if result["svg_extracted"]:
            print(f"  ✓ Extracted SVG from {file_path.name}")
        elif result["reference_updated"]:
            print(f"  ✓ Updated reference in {file_path.name}")
        elif result["error"]:
            print(f"  ✗ Error processing {file_path.name}: {result['error']}")

    # Step 2: Reorganize existing SVGs
    print("\n2. Reorganizing existing SVG files...")
    reorg_results = reorganize_existing_svgs(dry_run)

    for result in reorg_results:
        if result["moved"]:
            print(f"  ✓ Moved {Path(result['original']).name} to new location")
        elif result["error"]:
            print(
                f"  ✗ Error moving {Path(result['original']).name}: {result['error']}"
            )

    # Step 3: Create placeholder SVGs for missing images
    print("\n3. Creating placeholder SVGs...")
    for file_path in guardian_files:
        svg_path = get_svg_path_for_document(file_path)
        if not svg_path.exists():
            if not dry_run:
                svg_path.parent.mkdir(parents=True, exist_ok=True)
                placeholder = create_placeholder_svg(file_path.stem, file_path.stem)
                with open(svg_path, "w", encoding="utf-8") as f:
                    f.write(placeholder)
            print(f"  ✓ Created placeholder for {file_path.name}")

    # Summary
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  Files processed: {len(guardian_files)}")
    print(
        f"  Inline SVGs extracted: {sum(1 for r in process_results if r['svg_extracted'])}"
    )
    print(
        f"  References updated: {sum(1 for r in process_results if r['reference_updated'])}"
    )
    print(f"  SVG files moved: {sum(1 for r in reorg_results if r['moved'])}")
    print(
        f"  Errors: {sum(1 for r in process_results + reorg_results if r.get('error'))}"
    )

    if dry_run:
        print(
            "\n[DRY RUN] No changes were made. Run without --dry-run to apply changes."
        )


if __name__ == "__main__":
    import sys

    dry_run = "--dry-run" in sys.argv
    main(dry_run)
