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

    def test_reply_protocol_canary(self):
        required = (
            'Start every reply with "',
            "No exceptions.",
            "functions as a canary",
            "Write a handoff note for a fresh session",
            "not left as `[your name]`",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_status_footer(self):
        for phrase in ("**Goal**", "**Done**", "**Next**", '**Needs you** (or "nothing")'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_agents_md_rules_are_required_verbatim(self):
        required = (
            "Mandatory `AGENTS.md` rules",
            "required, verbatim, in every generated `AGENTS.md`",
            "## Planning",
            "state the plan abstractly",
            "Solve the general problem before the specific",
            "Take on one unit of work at a time",
            "## Testing",
            "not to raise a coverage number",
            "Every test names the regression it catches",
            "A test that would still pass if the feature were deleted is worthless",
            "## End-to-end verification",
            "Only a full pipeline run counts as real verification",
            "must pass whenever the change",
            "confirm the existing baseline still works",
            "## Invariants and boundaries",
            "Enforce invariants, not implementations",
            "Parse data at the boundary",
            "encode it as a test or a lint",
            "Follow the best pattern already in the repository",
            "## Session discipline",
            "Only a passing verification moves a feature to done",
            "## Verification errors",
            "how to fix it",
            "## Completion",
            "Distinguish implemented from verified",
            "## Instruction hygiene",
            "router, not an encyclopedia",
            "never buried in",
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
        self.assertIn("mandatory rules verbatim", completion)
        self.assertIn("no data, storage, or cache layer", completion)
        self.assertIn("reply-protocol placeholder", completion)

    def test_mandatory_block_has_no_unfilled_placeholder(self):
        block = self.skill.split("#### Mandatory `AGENTS.md` rules", 1)[1]
        block = block.split("**Choosing the form of address.**", 1)[0]
        self.assertNotIn("[your name]", block)

    def test_references_exist(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())


if __name__ == "__main__":
    unittest.main()
