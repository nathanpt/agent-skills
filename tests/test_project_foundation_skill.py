from pathlib import Path
import re
import unittest


class ProjectFoundationMandatoryRulesTests(unittest.TestCase):
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
        self.assertTrue(match.group(1).endswith("."))

    def test_agents_md_rules_are_required_verbatim(self):
        required = (
            "Mandatory `AGENTS.md` rules",
            "required, verbatim, in every generated `AGENTS.md`",
            "## Planning",
            "state the plan abstractly",
            "Solve the general problem before the specific",
            "## Testing",
            "not to raise a coverage number",
            "Every test names the regression it catches",
            "A test that would still pass if the feature were deleted is worthless",
            "## End-to-end verification",
            "Only a full pipeline run counts as real verification",
            "must pass whenever the change",
            "## Verification errors",
            "how to fix it",
            "## Completion",
            "Distinguish implemented from verified",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_thin_unit_test_suppression_is_stated(self):
        required = (
            "Agents reliably produce a large volume of low-value unit tests",
            "If you cannot name the regression, do not write the test",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_no_speculative_data_layer(self):
        self.assertIn("Do not invent a data/ or storage layer speculatively", self.skill)
        self.assertIn("record where the storage actually lives", self.skill)

    def test_completion_criteria_reference_new_rules(self):
        completion = self.skill.split("## Completion criteria", 1)[1]
        self.assertIn("five mandatory rules verbatim", completion)
        self.assertIn("no data, storage, or cache layer", completion)

    def test_references_exist(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())


if __name__ == "__main__":
    unittest.main()
