from pathlib import Path
import re
import unittest


class ProjectFoundationSkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "project-foundation"
        cls.skill = (cls.root / "SKILL.md").read_text()

    def test_frontmatter_and_size(self):
        self.assertTrue(self.skill.startswith("---\n"))
        end = self.skill.find("\n---\n", 4)
        self.assertGreater(end, 0)
        frontmatter = self.skill[4:end]
        self.assertIn("name: project-foundation", frontmatter)
        match = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE)
        if match is None:
            self.fail("description frontmatter is missing")
        self.assertLessEqual(len(match.group(1)), 60)
        self.assertTrue(match.group(1).endswith("."))
        self.assertLessEqual(len(self.skill.splitlines()), 500)

    def test_minimal_change_principles_are_explicit(self):
        required = (
            "smallest complete change",
            "Prefer deletion, reuse, configuration",
            "native platform facilities",
            "standard-library functions",
            "already-installed dependencies",
            "Never trade away validation",
            "security",
            "observability",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_generated_agents_contract_is_scoped_and_safe(self):
        marker = "When the repository will be maintained with code, include this compact implementation-discipline block"
        start = self.skill.index(marker)
        end = self.skill.index("Do not put the full architecture", start)
        block = self.skill[start:end]
        required = (
            "## Change discipline",
            "Before adding code or scaffolding",
            "deleting, reusing, configuring, or extending",
            "smallest complete change that satisfies the requirement",
            "Do not reduce validation",
            "For a documentation-only or otherwise non-code project, omit this block",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, block)

    def test_references_exist_and_skill_is_portable(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())
        self.assertNotIn("/home/", self.skill)

    def test_readme_wiring_is_preserved(self):
        readme = (self.root.parents[1] / "README.md").read_text()
        for marker in (
            "### `project-foundation`",
            "cp -R agent-skills/skills/project-foundation ~/.omp/agent/skills/",
            "/skill:project-foundation",
            "  project-foundation/",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, readme)


if __name__ == "__main__":
    unittest.main()
