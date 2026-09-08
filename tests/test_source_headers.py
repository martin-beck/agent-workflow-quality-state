# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for exact tracked-source license-header verification."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import ModuleType


def load_checker() -> ModuleType:
    path = Path(__file__).resolve().parents[1] / "tools" / "check_source_headers.py"
    spec = importlib.util.spec_from_file_location("check_source_headers", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load source-header checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checker = load_checker()


class SourceHeaderTests(unittest.TestCase):
    def test_comment_prefix_selects_only_reviewed_source_formats(self) -> None:
        self.assertEqual(checker.comment_prefix(Path("worker.py")), "# ")
        self.assertEqual(checker.comment_prefix(Path("verify.sh")), "# ")
        self.assertEqual(checker.comment_prefix(Path("Model.tla")), r"\* ")
        self.assertEqual(checker.comment_prefix(Path("tools/handoffctl")), "# ")
        self.assertIsNone(checker.comment_prefix(Path("workflow.yml")))
        self.assertIsNone(checker.comment_prefix(Path("model.cfg")))
        self.assertIsNone(checker.comment_prefix(Path("schema.json")))

    def test_check_file_accepts_hash_header_after_shebang(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            (root / path).write_text(
                f"#!/usr/bin/env python3\n# {checker.COPYRIGHT}\n# {checker.SPDX}\n\npass\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.check_file(root, path), [])

    def test_check_file_accepts_tla_header(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("Model.tla")
            (root / path).write_text(
                f"---- MODULE Model ----\n\\* {checker.COPYRIGHT}\n\\* {checker.SPDX}\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.check_file(root, path), [])

    def test_check_file_rejects_nonmatching_tla_module_prologue(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("Model.tla")
            for prologue in ("not a module declaration", "---- MODULE Other ----"):
                with self.subTest(prologue=prologue):
                    (root / path).write_text(
                        f"{prologue}\n\\* {checker.COPYRIGHT}\n\\* {checker.SPDX}\n",
                        encoding="utf-8",
                    )
                    issues = checker.check_file(root, path)
                    self.assertEqual(len(issues), 1)
                    self.assertIn("matching TLA+ MODULE declaration", issues[0])

    def test_check_file_reports_position_content_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            (root / path).write_text(
                f"# {checker.SPDX}\n# {checker.COPYRIGHT}\n# {checker.SPDX}\n"
                f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n",
                encoding="utf-8",
            )
            issues = checker.check_file(root, path)
            self.assertEqual(len(issues), 2)
            self.assertIn("expected exact Huawei/MIT header", issues[0])
            self.assertIn("exactly one canonical Huawei/MIT header pair", issues[1])

    def test_check_file_requires_tla_module_before_header(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("Model.tla")
            (root / path).write_text(
                f"\\* {checker.COPYRIGHT}\n\\* {checker.SPDX}\n---- MODULE Model ----\n",
                encoding="utf-8",
            )
            issues = checker.check_file(root, path)
            self.assertEqual(len(issues), 2)
            self.assertIn("matching TLA+ MODULE declaration", issues[0])
            self.assertIn("at line 2", issues[1])

    def test_check_file_counts_adjacent_header_pairs_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            header = f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n"
            isolated = f"# {checker.COPYRIGHT}\nvalue = 1\n# {checker.SPDX}\n"
            (root / path).write_text(header + "\n" + isolated, encoding="utf-8")
            self.assertEqual(checker.check_file(root, path), [])
            (root / path).write_text(header + "\n" + header, encoding="utf-8")
            issues = checker.check_file(root, path)
            self.assertEqual(len(issues), 1)
            self.assertIn("exactly one canonical Huawei/MIT header pair", issues[0])

    def test_check_file_reports_non_utf8_and_rejects_unsupported_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = Path("tool.py")
            (root / binary).write_bytes(b"\xff")
            self.assertIn("not valid UTF-8", checker.check_file(root, binary)[0])
            with self.assertRaisesRegex(checker.HeaderCheckError, "unsupported source"):
                checker.check_file(root, Path("data.json"))

    def test_tracked_files_and_main_results(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            (root / "ok.py").write_text(
                f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n", encoding="utf-8"
            )
            (root / "ignored.json").write_text("{}\n", encoding="utf-8")
            subprocess.run(["git", "add", "ok.py", "ignored.json"], cwd=root, check=True)
            self.assertEqual(checker.tracked_source_files(root), (Path("ok.py"),))
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.assertEqual(checker.main(["--root", str(root)]), 0)
            self.assertIn("1 tracked source files", stdout.getvalue())

            (root / "bad.sh").write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            subprocess.run(["git", "add", "bad.sh"], cwd=root, check=True)
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                self.assertEqual(checker.main(["--root", str(root)]), 1)
            self.assertIn("bad.sh: expected exact Huawei/MIT header", stderr.getvalue())

    def test_main_reports_git_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                self.assertEqual(checker.main(["--root", directory]), 2)
            self.assertIn("git ls-files failed", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
