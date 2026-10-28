#!/usr/bin/env python3
"""Testes de regressão para detecção de pacotes inválidos, sem serviços externos."""
from pathlib import Path
import shutil
import tempfile
import unittest
from validate_skill import validate, BASE

SOURCE = Path(__file__).resolve().parents[1]

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
        self.skill = self.root / BASE / "SKILL.md"

    def test_valid_package(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_reference(self):
        (self.root / BASE / "references/hook-patterns.md").unlink()
        self.assertTrue(any("hook-patterns" in e for e in validate(self.root)))

    def test_invalid_yaml(self):
        self.skill.write_text("---\nname: [invalid\n---\n", encoding="utf-8")
        self.assertTrue(any("YAML inválido" in e for e in validate(self.root)))

    def test_duplicate_yaml_key(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: hookmaster-ultimate", "name: hookmaster-ultimate\nname: other"), encoding="utf-8")
        self.assertTrue(any("duplicada" in e for e in validate(self.root)))

    def test_wrong_name(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: hookmaster-ultimate", "name: wrong"), encoding="utf-8")
        self.assertTrue(any("Nome técnico" in e for e in validate(self.root)))

    def test_broken_internal_link(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as f:
            f.write("\n[Quebrado](missing.md)\n")
        self.assertTrue(any("Link interno" in e for e in validate(self.root)))

    def test_empty_description(self):
        s = self.skill.read_text(encoding="utf-8")
        start = s.index("description:")
        end = s.index("\n---", start)
        self.skill.write_text(s[:start] + 'description: ""' + s[end:], encoding="utf-8")
        self.assertTrue(any("Description" in e for e in validate(self.root)))

    def test_missing_test_cases(self):
        (self.root / "tests/acceptance-cases.md").write_text("# Casos\n", encoding="utf-8")
        self.assertTrue(any("20 casos" in e for e in validate(self.root)))

if __name__ == "__main__":
    unittest.main()
