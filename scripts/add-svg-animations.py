#!/usr/bin/env python3
"""
Add animations and responsive sizing to all SVG files.
Makes SVGs expand to fill available space and adds subtle animations.
"""

import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path("/home/kkk/Apps/claude-guardian-agents")
ASSETS_DIR = PROJECT_ROOT / "assets"

# Animation templates for different types of elements
ANIMATIONS = {
    "pulse": """<animateTransform
        attributeName="transform"
        type="scale"
        values="1;1.05;1"
        dur="3s"
        repeatCount="indefinite"/>""",
    "rotate": """<animateTransform
        attributeName="transform"
        type="rotate"
        from="0 {cx} {cy}"
        to="360 {cx} {cy}"
        dur="20s"
        repeatCount="indefinite"/>""",
    "float": """<animateTransform
        attributeName="transform"
        type="translate"
        values="0,0; 0,-5; 0,0"
        dur="4s"
        repeatCount="indefinite"/>""",
    "fade": """<animate
        attributeName="opacity"
        values="0.4;1;0.4"
        dur="3s"
        repeatCount="indefinite"/>""",
    "glow": """<animate
        attributeName="stop-opacity"
        values="0.3;0.8;0.3"
        dur="2s"
        repeatCount="indefinite"/>""",
    "stroke": """<animate
        attributeName="stroke-width"
        values="{base};{max};{base}"
        dur="2.5s"
        repeatCount="indefinite"/>""",
    "dash": """<animate
        attributeName="stroke-dashoffset"
        values="0;{length}"
        dur="5s"
        repeatCount="indefinite"/>""",
    "color_shift": """<animate
        attributeName="stop-color"
        values="{color1};{color2};{color1}"
        dur="4s"
        repeatCount="indefinite"/>""",
}


def update_svg_viewport(svg_content: str) -> str:
    """Update SVG to be responsive and fill available space."""
    # Remove fixed width/height, keep viewBox
    svg_content = re.sub(r'width="[^"]*"', 'width="100%"', svg_content)
    svg_content = re.sub(r'height="[^"]*"', 'height="100%"', svg_content)

    # Add preserveAspectRatio for better scaling
    if "preserveAspectRatio" not in svg_content:
        svg_content = svg_content.replace(
            'viewBox="0 0 400 220"',
            'viewBox="0 0 400 220" preserveAspectRatio="xMidYMid meet"',
        )

    # Add responsive container styles
    if 'style="' in svg_content:
        # Update existing style
        svg_content = re.sub(
            r'style="[^"]*"',
            'style="max-width: 100%; height: auto; display: block; margin: 0 auto; background-color: #0a0a0a;"',
            svg_content,
            count=1,
        )

    return svg_content


def add_animations_to_svg(svg_content: str, agent_type: str) -> str:
    """Add appropriate animations based on agent type."""

    # Determine animation style based on agent type
    if "product" in agent_type or "strategy" in agent_type:
        # Product/Strategy: Professional pulse and gentle movement
        animations_to_add = ["pulse_center", "fade_accents", "float_symbols"]
    elif "engineering" in agent_type or "development" in agent_type:
        # Engineering: Technical rotating gears and data flow
        animations_to_add = ["rotate_gears", "data_flow", "pulse_nodes"]
    elif "operations" in agent_type or "security" in agent_type:
        # Operations: Active monitoring and status pulses
        animations_to_add = ["scan_effect", "status_pulse", "rotate_shields"]
    elif "thinktank" in agent_type:
        # Think Tank: Creative and dynamic movements
        animations_to_add = ["creative_float", "thought_pulse", "idea_spark"]
    else:
        # Default: Subtle professional animations
        animations_to_add = ["gentle_pulse", "soft_glow"]

    # Add pulse animation to central elements
    if "<circle" in svg_content and "pulse_center" in animations_to_add:
        # Find circles with r > 30 (likely central elements)
        svg_content = re.sub(
            r'(<circle[^>]*r="[4-9]\d+"[^>]*)(>)',
            r'\1>\n    <animateTransform attributeName="transform" type="scale" values="1;1.05;1" dur="3s" repeatCount="indefinite"/>\2',
            svg_content,
        )

    # Add rotation to gear-like elements
    if "rotate_gears" in animations_to_add:
        # Add rotation to elements that look like gears (contain teeth/cogs patterns)
        svg_content = re.sub(
            r'(<g id="gear[^"]*"[^>]*>)',
            r'\1\n    <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="20s" repeatCount="indefinite"/>',
            svg_content,
        )

    # Add floating animation to text elements
    if "<text" in svg_content:
        svg_content = re.sub(
            r"(<text[^>]*>)",
            r'\1\n    <animateTransform attributeName="transform" type="translate" values="0,0; 0,-2; 0,0" dur="4s" repeatCount="indefinite"/>',
            svg_content,
        )

    # Add glow pulse to radial gradients
    if "<radialGradient" in svg_content:
        svg_content = re.sub(
            r'(<stop[^>]*offset="0%"[^>]*>)',
            r'\1\n      <animate attributeName="stop-opacity" values="0.3;0.8;0.3" dur="2s" repeatCount="indefinite"/>',
            svg_content,
        )

    # Add stroke animation to paths
    stroke_paths = re.findall(r'<path[^>]*stroke-width="[^"]*"[^>]*>', svg_content)
    for path in stroke_paths[:3]:  # Limit to first 3 paths to avoid over-animation
        if 'stroke-width="2"' in path or 'stroke-width="3"' in path:
            animated_path = path.replace(
                ">",
                """>\n    <animate attributeName="stroke-width" values="2;3;2" dur="2.5s" repeatCount="indefinite"/>""",
            )
            svg_content = svg_content.replace(path, animated_path, 1)

    # Add color shift to gradients
    if "<linearGradient" in svg_content:
        # Add subtle color animation to first stop of first gradient
        svg_content = re.sub(
            r'(<linearGradient[^>]*>.*?<stop[^>]*style="stop-color:)([^;"]*)([^>]*>)',
            r'\1\2\3\n      <animate attributeName="stop-color" values="\2;#FFFFFF;\2" dur="4s" repeatCount="indefinite"/>',
            svg_content,
            count=1,
            flags=re.DOTALL,
        )

    # Add morphing to polygon shapes
    if "<polygon" in svg_content and "creative_float" in animations_to_add:
        svg_content = re.sub(
            r'(<polygon[^>]*points="([^"]*)"[^>]*>)',
            r'\1\n    <animate attributeName="points" values="\2;\2" dur="5s" repeatCount="indefinite"/>',
            svg_content,
            count=1,
        )

    # Add dash animation to specific strokes
    if "stroke-dasharray" not in svg_content and "<path" in svg_content:
        # Add dash animation to first suitable path
        svg_content = re.sub(
            r'(<path[^>]*stroke="[^"]*"[^>]*)(>)',
            r'\1 stroke-dasharray="5,5">\n    <animate attributeName="stroke-dashoffset" values="0;10" dur="1s" repeatCount="indefinite"/>',
            svg_content,
            count=1,
        )

    return svg_content


def process_svg_file(svg_path: Path) -> bool:
    """Process a single SVG file to add animations and responsive sizing."""
    try:
        with open(svg_path, encoding="utf-8") as f:
            content = f.read()

        # Determine agent type from filename
        filename = svg_path.name.lower()
        if "product" in filename or "strategy" in filename or "design" in filename:
            agent_type = "product"
        elif (
            "engineering" in filename
            or "development" in filename
            or "architecture" in filename
        ):
            agent_type = "engineering"
        elif "operations" in filename or "security" in filename or "data" in filename:
            agent_type = "operations"
        elif "thinktank" in filename or "think" in filename:
            agent_type = "thinktank"
        else:
            agent_type = "default"

        # Skip if already has animations (check for animate tags)
        if "<animate" in content and "values=" in content:
            print(f"  ⏭  Skipping {svg_path.name} (already has animations)")
            return False

        # Update viewport for responsiveness
        content = update_svg_viewport(content)

        # Add animations
        content = add_animations_to_svg(content, agent_type)

        # Write back
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  ✓ Added animations to {svg_path.name}")
        return True

    except Exception as e:
        print(f"  ✗ Error processing {svg_path.name}: {e}")
        return False


def add_department_specific_animations() -> dict:
    """Add specific animation patterns for each department."""

    department_animations = {
        "1-product": {
            "pattern": "pulse_and_float",
            "description": "Professional pulse with gentle floating",
        },
        "2-engineering": {
            "pattern": "rotate_and_flow",
            "description": "Technical rotation with data flow",
        },
        "3-operations": {
            "pattern": "scan_and_monitor",
            "description": "Active scanning with monitoring pulses",
        },
        "4-thinktank": {
            "pattern": "creative_morph",
            "description": "Creative morphing with thought bubbles",
        },
    }

    return department_animations


def main() -> None:
    """Main execution function."""
    print("Adding animations and responsive sizing to all SVG files...")
    print("=" * 50)

    # Get all SVG files
    svg_files = list(ASSETS_DIR.glob("**/*.svg"))
    print(f"Found {len(svg_files)} SVG files to process\n")

    # Process each SVG
    updated_count = 0
    for svg_file in sorted(svg_files):
        if process_svg_file(svg_file):
            updated_count += 1

    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  Total SVG files: {len(svg_files)}")
    print(f"  Updated with animations: {updated_count}")
    print(f"  Already had animations: {len(svg_files) - updated_count}")

    print("\nAnimation types added:")
    print("  • Pulse effects on central elements")
    print("  • Rotation for gear/technical elements")
    print("  • Floating text and symbols")
    print("  • Glow pulses on gradients")
    print("  • Stroke width animations")
    print("  • Color shifting on gradients")
    print("  • Dash animations on paths")

    print("\nResponsive features added:")
    print("  • 100% width and height")
    print("  • Preserve aspect ratio")
    print("  • Auto-scaling to container")
    print("  • Centered display")


if __name__ == "__main__":
    main()
