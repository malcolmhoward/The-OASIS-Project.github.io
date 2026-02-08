#!/usr/bin/env python3
"""
Tests for the documentation aggregation script.

Run with: pytest scripts/test_aggregate_docs.py -v
"""

import shutil
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from aggregate_docs import (
    COMPONENT_DOCS,
    COORDINATION_DOCS,
    aggregate_component_docs,
    aggregate_coordination_docs,
    copy_file,
    ensure_dir,
    find_scope_root,
)


@pytest.fixture
def temp_scope_structure(tmp_path):
    """
    Create a temporary S.C.O.P.E.-like directory structure for testing.
    """
    # Create S.C.O.P.E. root structure
    scope_root = tmp_path / "scope"
    repos_dir = scope_root / "repos"
    coordination_dir = scope_root / "coordination"

    # Create component repos with docs
    for component in ["mirage", "dawn", "aura", "spark", "beacon", "genesis"]:
        component_dir = repos_dir / component / "docs"
        component_dir.mkdir(parents=True)

    # Create specific doc files
    (repos_dir / "mirage" / "docs" / "guide.md").write_text("# MIRAGE Guide\nContent here.")
    (repos_dir / "dawn" / "docs" / "guide.md").write_text("# DAWN Guide\nContent here.")
    (repos_dir / "dawn" / "docs" / "local-llm.md").write_text("# Local LLM\nContent here.")
    (repos_dir / "aura" / "docs" / "guide.md").write_text("# AURA Guide\nContent here.")
    (repos_dir / "spark" / "docs" / "guide.md").write_text("# SPARK Guide\nContent here.")
    (repos_dir / "beacon" / "docs" / "parts-catalog.md").write_text("# BEACON Parts\nContent here.")

    # Create coordination docs
    protocols_dir = coordination_dir / "protocols"
    protocols_dir.mkdir(parents=True)
    (protocols_dir / "mqtt-communication.md").write_text("# MQTT Protocols\nContent here.")

    # Create GitHub Pages structure
    pages_dir = repos_dir / "github-pages"
    pages_docs = pages_dir / "docs"
    pages_docs.mkdir(parents=True)
    (pages_dir / "scripts").mkdir()

    return {
        "scope_root": scope_root,
        "repos_dir": repos_dir,
        "coordination_dir": coordination_dir,
        "pages_dir": pages_dir,
        "pages_docs": pages_docs,
    }


class TestFindScopeRoot:
    """Tests for find_scope_root function."""

    def test_finds_scope_root_from_pages_dir(self, temp_scope_structure):
        """Should find S.C.O.P.E. root when starting from github-pages."""
        pages_dir = temp_scope_structure["pages_dir"]
        scope_root = temp_scope_structure["scope_root"]

        result = find_scope_root(pages_dir)

        assert result == scope_root

    def test_finds_scope_root_from_nested_dir(self, temp_scope_structure):
        """Should find S.C.O.P.E. root when starting from deeply nested directory."""
        nested_dir = temp_scope_structure["pages_dir"] / "scripts"
        scope_root = temp_scope_structure["scope_root"]

        result = find_scope_root(nested_dir)

        assert result == scope_root

    def test_returns_none_when_not_in_scope(self, tmp_path):
        """Should return None when not inside a S.C.O.P.E. structure."""
        # Create a directory that's not S.C.O.P.E.
        random_dir = tmp_path / "some" / "random" / "path"
        random_dir.mkdir(parents=True)

        result = find_scope_root(random_dir)

        assert result is None

    def test_finds_scope_root_at_current_dir(self, temp_scope_structure):
        """Should find S.C.O.P.E. root when starting at the root itself."""
        scope_root = temp_scope_structure["scope_root"]

        result = find_scope_root(scope_root)

        assert result == scope_root


class TestEnsureDir:
    """Tests for ensure_dir function."""

    def test_creates_parent_directories(self, tmp_path):
        """Should create all parent directories for a file path."""
        file_path = tmp_path / "a" / "b" / "c" / "file.md"

        ensure_dir(file_path)

        assert (tmp_path / "a" / "b" / "c").is_dir()

    def test_handles_existing_directory(self, tmp_path):
        """Should not fail if directory already exists."""
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()
        file_path = existing_dir / "file.md"

        # Should not raise
        ensure_dir(file_path)

        assert existing_dir.is_dir()


class TestCopyFile:
    """Tests for copy_file function."""

    def test_copies_file_successfully(self, tmp_path):
        """Should copy file from source to destination."""
        src = tmp_path / "source.md"
        dst = tmp_path / "dest" / "target.md"
        src.write_text("Test content")

        result = copy_file(src, dst)

        assert result is True
        assert dst.exists()
        assert dst.read_text() == "Test content"

    def test_returns_false_for_missing_source(self, tmp_path, capsys):
        """Should return False and print message when source doesn't exist."""
        src = tmp_path / "nonexistent.md"
        dst = tmp_path / "dest.md"

        result = copy_file(src, dst)

        assert result is False
        assert not dst.exists()
        captured = capsys.readouterr()
        assert "SKIP" in captured.out

    def test_dry_run_does_not_copy(self, tmp_path, capsys):
        """Should not copy file in dry run mode."""
        src = tmp_path / "source.md"
        dst = tmp_path / "dest.md"
        src.write_text("Test content")

        result = copy_file(src, dst, dry_run=True)

        assert result is True
        assert not dst.exists()
        captured = capsys.readouterr()
        assert "WOULD COPY" in captured.out

    def test_creates_destination_directory(self, tmp_path):
        """Should create destination directory if it doesn't exist."""
        src = tmp_path / "source.md"
        dst = tmp_path / "nested" / "deep" / "dest.md"
        src.write_text("Test content")

        copy_file(src, dst)

        assert dst.exists()
        assert dst.parent.is_dir()


class TestAggregateComponentDocs:
    """Tests for aggregate_component_docs function."""

    def test_aggregates_all_component_docs(self, temp_scope_structure):
        """Should copy all component docs to destination."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        copied = aggregate_component_docs(scope_root, docs_dir)

        # Check expected files exist
        assert (docs_dir / "components" / "mirage.md").exists()
        assert (docs_dir / "components" / "dawn.md").exists()
        assert (docs_dir / "components" / "dawn-llm.md").exists()
        assert (docs_dir / "components" / "aura.md").exists()
        assert (docs_dir / "components" / "spark.md").exists()
        assert (docs_dir / "components" / "beacon.md").exists()

        # Should have copied 6 files
        assert copied == 6

    def test_preserves_file_content(self, temp_scope_structure):
        """Should preserve original file content."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        aggregate_component_docs(scope_root, docs_dir)

        content = (docs_dir / "components" / "mirage.md").read_text()
        assert "# MIRAGE Guide" in content

    def test_handles_missing_component(self, temp_scope_structure, capsys):
        """Should skip missing components gracefully."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        # Remove a component
        shutil.rmtree(scope_root / "repos" / "aura")

        copied = aggregate_component_docs(scope_root, docs_dir)

        # Should still copy other components
        assert (docs_dir / "components" / "mirage.md").exists()
        assert not (docs_dir / "components" / "aura.md").exists()
        captured = capsys.readouterr()
        assert "SKIP" in captured.out

    def test_dry_run_does_not_modify(self, temp_scope_structure):
        """Should not create files in dry run mode."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        copied = aggregate_component_docs(scope_root, docs_dir, dry_run=True)

        assert copied > 0
        assert not (docs_dir / "components").exists()


class TestAggregateCoordinationDocs:
    """Tests for aggregate_coordination_docs function."""

    def test_aggregates_coordination_docs(self, temp_scope_structure):
        """Should copy coordination docs to destination."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        copied = aggregate_coordination_docs(scope_root, docs_dir)

        assert (docs_dir / "architecture" / "mqtt-protocols.md").exists()
        assert copied == 1

    def test_preserves_content(self, temp_scope_structure):
        """Should preserve original file content."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        aggregate_coordination_docs(scope_root, docs_dir)

        content = (docs_dir / "architecture" / "mqtt-protocols.md").read_text()
        assert "# MQTT Protocols" in content

    def test_dry_run_does_not_modify(self, temp_scope_structure):
        """Should not create files in dry run mode."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        copied = aggregate_coordination_docs(scope_root, docs_dir, dry_run=True)

        assert copied > 0
        assert not (docs_dir / "architecture").exists()


class TestIntegration:
    """Integration tests for the full aggregation workflow."""

    def test_full_aggregation_workflow(self, temp_scope_structure):
        """Should aggregate all docs in a complete workflow."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        # Run both aggregation functions
        component_count = aggregate_component_docs(scope_root, docs_dir)
        coordination_count = aggregate_coordination_docs(scope_root, docs_dir)

        total = component_count + coordination_count

        # Verify structure
        assert (docs_dir / "components").is_dir()
        assert (docs_dir / "architecture").is_dir()

        # Verify all expected files
        expected_files = [
            "components/mirage.md",
            "components/dawn.md",
            "components/dawn-llm.md",
            "components/aura.md",
            "components/spark.md",
            "components/beacon.md",
            "architecture/mqtt-protocols.md",
        ]

        for file_path in expected_files:
            assert (docs_dir / file_path).exists(), f"Missing: {file_path}"

        assert total == len(expected_files)

    def test_idempotent_aggregation(self, temp_scope_structure):
        """Should be safe to run multiple times."""
        scope_root = temp_scope_structure["scope_root"]
        docs_dir = temp_scope_structure["pages_docs"]

        # Run twice
        aggregate_component_docs(scope_root, docs_dir)
        aggregate_component_docs(scope_root, docs_dir)

        # Should still have correct content
        content = (docs_dir / "components" / "mirage.md").read_text()
        assert "# MIRAGE Guide" in content


class TestComponentDocsMapping:
    """Tests to verify COMPONENT_DOCS mapping is valid."""

    def test_component_docs_has_expected_components(self):
        """Should have mappings for all expected components."""
        expected = {"mirage", "dawn", "aura", "spark", "beacon", "genesis"}
        actual = set(COMPONENT_DOCS.keys())

        assert actual == expected

    def test_all_mappings_are_tuples(self):
        """All mappings should be (source, destination) tuples."""
        for component, mappings in COMPONENT_DOCS.items():
            for mapping in mappings:
                assert isinstance(mapping, tuple), f"Invalid mapping in {component}"
                assert len(mapping) == 2, f"Mapping should have 2 elements in {component}"

    def test_destinations_are_under_components(self):
        """All component doc destinations should be under components/."""
        for component, mappings in COMPONENT_DOCS.items():
            for _, dst in mappings:
                assert dst.startswith("components/"), f"Destination not under components/: {dst}"


class TestCoordinationDocsMapping:
    """Tests to verify COORDINATION_DOCS mapping is valid."""

    def test_coordination_docs_not_empty(self):
        """Should have at least one coordination doc mapping."""
        assert len(COORDINATION_DOCS) > 0

    def test_all_mappings_are_tuples(self):
        """All mappings should be (source, destination) tuples."""
        for mapping in COORDINATION_DOCS:
            assert isinstance(mapping, tuple)
            assert len(mapping) == 2

    def test_destinations_are_under_architecture(self):
        """All coordination doc destinations should be under architecture/."""
        for _, dst in COORDINATION_DOCS:
            assert dst.startswith("architecture/"), f"Destination not under architecture/: {dst}"
