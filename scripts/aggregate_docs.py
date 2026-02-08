#!/usr/bin/env python3
"""
Documentation Aggregation Script for O.A.S.I.S. GitHub Pages

This script aggregates documentation from component repositories into the
GitHub Pages docs/ folder for unified site generation.

Usage:
    python scripts/aggregate-docs.py [--scope-root PATH]

When run from within S.C.O.P.E. (the meta-repo), component docs are pulled
from sibling submodules. The --scope-root option specifies the S.C.O.P.E.
root directory if not auto-detected.

See ADR-0004 for documentation architecture rationale.
"""

import argparse
import shutil
import sys
from pathlib import Path


# Component documentation mappings
# Format: (source_relative_to_component, destination_relative_to_docs)
COMPONENT_DOCS = {
    "mirage": [
        ("docs/guide.md", "components/mirage.md"),
    ],
    "dawn": [
        ("docs/guide.md", "components/dawn.md"),
        ("docs/local-llm.md", "components/dawn-llm.md"),
    ],
    "aura": [
        ("docs/guide.md", "components/aura.md"),
    ],
    "spark": [
        ("docs/guide.md", "components/spark.md"),
    ],
    "beacon": [
        ("docs/parts-catalog.md", "components/beacon.md"),
    ],
    "genesis": [
        ("docs/guide.md", "components/genesis.md"),
    ],
}

# S.C.O.P.E. coordination documentation mappings
COORDINATION_DOCS = [
    ("coordination/protocols/mqtt-communication.md", "architecture/mqtt-protocols.md"),
    # Add more coordination docs as they're created
]


def find_scope_root(start_path: Path) -> Path | None:
    """
    Find S.C.O.P.E. root by looking for characteristic files/folders.
    Walks up from start_path looking for the meta-repo structure.
    """
    current = start_path.resolve()

    for _ in range(10):  # Limit search depth
        # Check for S.C.O.P.E. indicators
        if (current / "repos").is_dir() and (current / "coordination").is_dir():
            return current

        parent = current.parent
        if parent == current:  # Reached filesystem root
            break
        current = parent

    return None


def ensure_dir(path: Path) -> None:
    """Ensure directory exists, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path, dry_run: bool = False) -> bool:
    """
    Copy a file from src to dst.
    Returns True if file was copied, False if skipped.
    """
    if not src.exists():
        print(f"  SKIP: Source not found: {src}")
        return False

    if dry_run:
        print(f"  WOULD COPY: {src} -> {dst}")
        return True

    ensure_dir(dst)
    shutil.copy2(src, dst)
    print(f"  COPIED: {src.name} -> {dst}")
    return True


def aggregate_component_docs(scope_root: Path, docs_dir: Path, dry_run: bool = False) -> int:
    """
    Aggregate documentation from component repositories.
    Returns count of files copied.
    """
    copied = 0
    repos_dir = scope_root / "repos"

    print("\nAggregating component documentation...")

    for component, mappings in COMPONENT_DOCS.items():
        component_dir = repos_dir / component

        if not component_dir.exists():
            print(f"  SKIP: Component not found: {component}")
            continue

        for src_rel, dst_rel in mappings:
            src = component_dir / src_rel
            dst = docs_dir / dst_rel

            if copy_file(src, dst, dry_run):
                copied += 1

    return copied


def aggregate_coordination_docs(scope_root: Path, docs_dir: Path, dry_run: bool = False) -> int:
    """
    Aggregate documentation from S.C.O.P.E. coordination folders.
    Returns count of files copied.
    """
    copied = 0

    print("\nAggregating coordination documentation...")

    for src_rel, dst_rel in COORDINATION_DOCS:
        src = scope_root / src_rel
        dst = docs_dir / dst_rel

        if copy_file(src, dst, dry_run):
            copied += 1

    return copied


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate O.A.S.I.S. documentation from component repos"
    )
    parser.add_argument(
        "--scope-root",
        type=Path,
        help="Path to S.C.O.P.E. meta-repo root (auto-detected if not specified)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without actually copying"
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        help="Destination docs directory (default: ./docs relative to script)"
    )

    args = parser.parse_args()

    # Determine script location and docs directory
    script_dir = Path(__file__).parent.resolve()
    pages_root = script_dir.parent
    docs_dir = args.docs_dir or (pages_root / "docs")

    print(f"GitHub Pages root: {pages_root}")
    print(f"Docs directory: {docs_dir}")

    # Find S.C.O.P.E. root
    if args.scope_root:
        scope_root = args.scope_root.resolve()
    else:
        scope_root = find_scope_root(pages_root)

    if not scope_root:
        print("\nERROR: Could not find S.C.O.P.E. root directory.")
        print("Run from within S.C.O.P.E. or specify --scope-root")
        sys.exit(1)

    print(f"S.C.O.P.E. root: {scope_root}")

    if args.dry_run:
        print("\n=== DRY RUN - No files will be copied ===")

    # Aggregate documentation
    total_copied = 0
    total_copied += aggregate_component_docs(scope_root, docs_dir, args.dry_run)
    total_copied += aggregate_coordination_docs(scope_root, docs_dir, args.dry_run)

    print(f"\n{'Would copy' if args.dry_run else 'Copied'} {total_copied} files.")

    if not args.dry_run and total_copied > 0:
        print("\nNext steps:")
        print("  1. Review aggregated content in docs/components/ and docs/architecture/")
        print("  2. Update mkdocs.yml nav to include new pages")
        print("  3. Run 'mkdocs serve' to preview")


if __name__ == "__main__":
    main()
