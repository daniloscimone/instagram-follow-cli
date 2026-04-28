"""Tests for the CLI file-driven flow."""

from __future__ import annotations

from io import StringIO
import tempfile
import unittest
from pathlib import Path

from rich.console import Console

from instagram_follow_cli import cli
from instagram_follow_cli.instagram_export import load_export_data


class CliTests(unittest.TestCase):
    def test_load_export_data_supports_extracted_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "relationships").mkdir()
            (root / "relationships" / "followers_1.json").write_text(
                '{"relationships_followers": [{"string_list_data": [{"value": "anna"}]}, {"string_list_data": [{"value": "@luca"}]}]}',
                encoding="utf-8",
            )
            (root / "relationships" / "following.json").write_text(
                '{"relationships_following": [{"string_list_data": [{"value": "anna"}]}, {"string_list_data": [{"value": "maria"}]}]}',
                encoding="utf-8",
            )

            data = load_export_data(str(root))

            self.assertEqual(data.followers, ["anna", "luca"])
            self.assertEqual(data.following, ["anna", "maria"])

    def test_run_with_file_data_returns_success(self) -> None:
        buffer = StringIO()
        original_console = cli.console
        cli.console = Console(file=buffer, force_terminal=False, color_system=None, width=80)
        try:
            exit_code = cli.run(
                "danilo",
                followers=["anna", "luca"],
                following=["anna", "luca", "maria"],
            )
        finally:
            cli.console = original_console

        output = buffer.getvalue()
        self.assertEqual(exit_code, 0)
        self.assertIn("maria", output)


if __name__ == "__main__":
    unittest.main()
