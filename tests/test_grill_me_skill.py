from pathlib import Path
import re
import unittest


class GrillMeSkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "grill-me"
        cls.skill = (cls.root / "SKILL.md").read_text()

    def test_frontmatter_and_size(self):
        self.assertTrue(self.skill.startswith("---\n"))
        end = self.skill.find("\n---\n", 4)
        self.assertGreater(end, 0)
        frontmatter = self.skill[4:end]
        self.assertIn("name: grill-me", frontmatter)
        match = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE)
        if match is None:
            self.fail("description frontmatter is missing")
        self.assertLessEqual(len(match.group(1)), 60)
        self.assertTrue(match.group(1).endswith("."))
        self.assertLessEqual(len(self.skill.splitlines()), 220)

    def test_interview_control_loop_and_boundaries(self):
        required = (
            "current **frontier**",
            "one question per turn",
            "Recommendation",
            "Facts that the environment can answer",
            "Second hand-wave",
            "Unprototypable-by-conversation",
            "Ask for confirmation",
            "Do not use an arbitrary question count",
            "stateless by default",
            "Do not activate merely because a task is complex",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_references_exist_and_skill_is_agent_agnostic(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())
        self.assertNotIn("AskUserQuestion", self.skill)
        self.assertNotIn("ToolSearch", self.skill)
        self.assertNotIn("/home/", self.skill)


if __name__ == "__main__":
    unittest.main()
