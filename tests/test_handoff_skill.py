from pathlib import Path
import re
import unittest


class HandoffSkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "handoff"
        cls.skill = (cls.root / "SKILL.md").read_text()

    def test_frontmatter_and_size(self):
        self.assertTrue(self.skill.startswith("---\n"))
        end = self.skill.find("\n---\n", 4)
        self.assertGreater(end, 0)
        frontmatter = self.skill[4:end]
        self.assertIn("name: handoff", frontmatter)
        match = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE)
        if match is None:
            self.fail("description frontmatter is missing")
        self.assertLessEqual(len(match.group(1)), 60)
        self.assertTrue(match.group(1).endswith("."))
        self.assertLessEqual(len(self.skill.splitlines()), 220)

    def test_create_resume_and_safety_contract(self):
        required = (
            "CREATE",
            "RESUME",
            "TRANSFER",
            "FORK",
            "verified",
            "unverified",
            "Rejected alternatives",
            "side-effect gates",
            "Immediate next action",
            "credentials",
            "stale",
            "state as of",
            "predecessor link/hash",
            "operational claim",
            "verified: command/source + result + date",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.skill.lower())

    def test_references_exist_and_no_machine_local_dependency(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())
        self.assertNotIn("/home/", self.skill)
        self.assertNotIn("systematic-debugging", self.skill)


if __name__ == "__main__":
    unittest.main()
