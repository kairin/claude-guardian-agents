"""
A script to validate the YAML front matter of documentation files.

This script scans for Markdown files, parses their front matter, and
ensures that all required fields are present and correctly formatted.
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List

import frontmatter
import yaml

# --- Configuration ---

# The root directory of the repository
ROOT_DIR = Path(__file__).parent.parent

# Directories to search for documentation files
DOCS_DIRS = [
    ROOT_DIR / "1-product",
    ROOT_DIR / "2-engineering",
    ROOT_DIR / "3-operations",
    ROOT_DIR / "4-thinktank",
    ROOT_DIR / "docs",
]

# Files to exclude from validation
EXCLUDE_FILES = {
    ROOT_DIR / "README.md",
    ROOT_DIR / "CHANGELOG.md",
    ROOT_DIR / "docs/README.md",
}

# Required fields in the front matter
REQUIRED_FIELDS = {
    "title": str,
    "description": str,
    "version": float,
    "status": str,
    "owner": str,
    "last_updated": str,  # Should be in YYYY-MM-DD format
    "tags": list,
    "related_docs": list,
}

# Allowed values for the 'status' field
ALLOWED_STATUS_VALUES = {"Draft", "In Review", "Published", "Deprecated"}


def validate_file(path: Path) -> List[str]:
    """Validates a single documentation file and returns a list of errors."""
    errors = []
    try:
        post = frontmatter.load(path)
    except (yaml.YAMLError, ValueError) as e:
        return [f"Could not parse YAML front matter: {e}"]

    if not post.metadata:
        return ["No YAML front matter found."]

    metadata: Dict[str, Any] = post.metadata

    # Check for required fields and correct types
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in metadata:
            errors.append(f"Missing required field: '{field}'")
        elif not isinstance(metadata[field], expected_type):
            errors.append(
                f"Field '{field}' has incorrect type. "
                f"Expected {expected_type.__name__}, got {type(metadata[field]).__name__}"
            )

    # Specific field value checks
    if "status" in metadata and metadata["status"] not in ALLOWED_STATUS_VALUES:
        errors.append(
            f"Invalid 'status' value: '{metadata['status']}'. "
            f"Allowed values are: {', '.join(ALLOWED_STATUS_VALUES)}"
        )

    # TODO: Add date format validation for 'last_updated'

    # Check for embedded SVG
    svg_pattern = re.compile(r"<svg.*?</svg>", re.DOTALL | re.IGNORECASE)
    if svg_pattern.search(post.content):
        errors.append(
            "Embedded SVG found. SVG files should be external and linked via Markdown image syntax."
        )

    return errors


def main() -> int:
    """Main function to run the validation across all specified directories."""
    print("🛡️  Running documentation validator...")
    error_count = 0
    files_to_validate = []

    # Check for command-line arguments
    if len(sys.argv) > 1:
        # Use files provided as arguments
        for arg in sys.argv[1:]:
            path = Path(arg)
            if not path.is_file():
                print(f"⚠️  Warning: Argument is not a file, skipping: {path}")
                continue
            files_to_validate.append(path)
    else:
        # Scan default directories
        for doc_dir in DOCS_DIRS:
            for path in doc_dir.rglob("*.md"):
                if path not in EXCLUDE_FILES:
                    files_to_validate.append(path)

    if not files_to_validate:
        print("⚠️  No documentation files found to validate.")
        return 0

    print(f"Found {len(files_to_validate)} files to validate.")

    for file_path in sorted(files_to_validate):
        relative_path = file_path.relative_to(ROOT_DIR)
        validation_errors = validate_file(file_path)
        if validation_errors:
            error_count += 1
            print(f"\n❌ Errors in {relative_path}:")
            for error in validation_errors:
                print(f"  - {error}")

    if error_count > 0:
        print(f"\nFound {error_count} file(s) with validation errors.")
        return 1
    else:
        print("\n✅ All documentation files are compliant.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
