from pathlib import Path
import re
import unittest


class DebugSkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "debug"
        cls.skill = (cls.root / "SKILL.md").read_text()

    def test_frontmatter_and_size(self):
        self.assertTrue(self.skill.startswith("---\n"))
        end = self.skill.find("\n---\n", 4)
        self.assertGreater(end, 0)
        frontmatter = self.skill[4:end]
        self.assertIn("name: debug", frontmatter)
        match = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE)
        if match is None:
            self.fail("description frontmatter is missing")
        description = match.group(1)
        self.assertLessEqual(len(description), 60)
        self.assertTrue(description.endswith("."))
        self.assertLess(len(self.skill.splitlines()), 220)

    def test_safety_boundaries_are_present(self):
        required = (
            "No speculative application fixes",
            "Diagnostic instrumentation is not a fix",
            "Protect sensitive data",
            "Stop before thrashing",
            "unverified",
            "human confirmation",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_references_exist_and_skill_is_standalone(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())
        self.assertNotIn("systematic-debugging", self.skill)


if __name__ == "__main__":
    unittest.main()
