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


class ProjectFoundationRetrofitModeTests(unittest.TestCase):
    """Retrofit mode replaced the retired harness-bootstrap skill; these guard the merge."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1]
        cls.skill_dir = cls.root / "skills" / "project-foundation"
        cls.skill = (cls.skill_dir / "SKILL.md").read_text()
        cls.retrofit_path = cls.skill_dir / "references" / "retrofit-existing-repo.md"
        cls.retrofit = cls.retrofit_path.read_text() if cls.retrofit_path.exists() else ""
        cls.readme = (cls.root / "README.md").read_text()

    def test_skill_declares_both_modes(self):
        for marker in ("Creation mode", "Retrofit mode", "references/retrofit-existing-repo.md"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.skill)

    def test_skill_no_longer_defers_to_a_retired_skill(self):
        self.assertNotIn(
            "harness-bootstrap",
            self.skill,
            "SKILL.md must not hand off to the retired harness-bootstrap skill",
        )

    def test_retrofit_reference_exists_and_is_substantive(self):
        self.assertTrue(self.retrofit_path.exists(), "retrofit reference is missing")
        self.assertGreater(len(self.retrofit.splitlines()), 100, "retrofit reference is too thin to replace the merged skill")

    def test_retrofit_reference_targets_the_two_part_standard(self):
        for marker in (
            "references/agents-md-general-rules.md",
            "Part 1",
            "Part 2",
            "byte-identical",
            "canary",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.retrofit)

    def test_retrofit_reference_keeps_the_mechanical_safeguards(self):
        for marker in (
            "case-insensitively",
            "generator owns",
            "not verified",
            "hypothesis until checked",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.retrofit)

    def test_retrofit_reference_labels_itself_unexercised(self):
        self.assertIn(
            "unexercised",
            self.retrofit.lower(),
            "merged material must state that it has not been validated in service",
        )

    def test_retired_skill_is_gone(self):
        self.assertFalse(
            (self.root / "skills" / "harness-bootstrap").exists(),
            "harness-bootstrap should be retired; its content lives in project-foundation/references/",
        )

    def test_readme_describes_two_modes_and_drops_the_retired_skill(self):
        self.assertNotIn("harness-bootstrap", self.readme)
        for marker in ("**creation**", "**retrofit**", "two-part `AGENTS.md`"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.readme)


if __name__ == "__main__":
    unittest.main()


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
        self.assertLessEqual(len(self.skill.splitlines()), 600)

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

    def test_initializer_completeness_guard_is_explicit(self):
        marker = "## Initializer completeness guard"
        start = self.skill.index(marker)
        end = self.skill.index("## Procedure", start)
        guard = self.skill[start:end]
        required = (
            "applicability matrix",
            "`create`",
            "`preserve`",
            "`not applicable`",
            "baseline artifacts cannot be marked `not applicable`",
            "Not started",
            "no code yet",
            "would be sparse",
            "Any candidate omitted without a disposition is a failure",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, guard)

    def test_preimplementation_design_requires_a_real_foundation_tier(self):
        required = (
            "design, requirements, product, or architecture document",
            "at least the Standard tier",
            "unless the user explicitly chooses Minimal",
            "including a case variant such as `design.md`",
            "remaining selected-tier baseline artifacts",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_report_and_completion_require_full_accounting(self):
        report_start = self.skill.index("Report:")
        report_end = self.skill.index("## Completion criteria", report_start)
        report = self.skill[report_start:report_end]
        for phrase in (
            "Applicability matrix",
            "every candidate with create, preserve, or not applicable plus evidence",
            "only conditional files marked not applicable",
        ):
            with self.subTest(report_phrase=phrase):
                self.assertIn(phrase, report)

        completion_start = self.skill.index("## Completion criteria")
        completion = self.skill[completion_start:]
        for phrase in (
            "applicability matrix covers every candidate",
            "every selected-tier baseline artifact is created or explicitly preserved",
            "every conditional artifact with an evidenced project surface is created",
        ):
            with self.subTest(completion_phrase=phrase):
                self.assertIn(phrase, completion)

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


class ProjectFoundationRetrofitModeTests(unittest.TestCase):
    """Retrofit mode replaced the retired harness-bootstrap skill; these guard the merge."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1]
        cls.skill_dir = cls.root / "skills" / "project-foundation"
        cls.skill = (cls.skill_dir / "SKILL.md").read_text()
        cls.retrofit_path = cls.skill_dir / "references" / "retrofit-existing-repo.md"
        cls.retrofit = cls.retrofit_path.read_text() if cls.retrofit_path.exists() else ""
        cls.readme = (cls.root / "README.md").read_text()

    def test_skill_declares_both_modes(self):
        for marker in ("Creation mode", "Retrofit mode", "references/retrofit-existing-repo.md"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.skill)

    def test_skill_no_longer_defers_to_a_retired_skill(self):
        self.assertNotIn(
            "harness-bootstrap",
            self.skill,
            "SKILL.md must not hand off to the retired harness-bootstrap skill",
        )

    def test_retrofit_reference_exists_and_is_substantive(self):
        self.assertTrue(self.retrofit_path.exists(), "retrofit reference is missing")
        self.assertGreater(len(self.retrofit.splitlines()), 100, "retrofit reference is too thin to replace the merged skill")

    def test_retrofit_reference_targets_the_two_part_standard(self):
        for marker in (
            "references/agents-md-general-rules.md",
            "Part 1",
            "Part 2",
            "byte-identical",
            "canary",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.retrofit)

    def test_retrofit_reference_keeps_the_mechanical_safeguards(self):
        for marker in (
            "case-insensitively",
            "generator owns",
            "not verified",
            "hypothesis until checked",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.retrofit)

    def test_retrofit_reference_labels_itself_unexercised(self):
        self.assertIn(
            "unexercised",
            self.retrofit.lower(),
            "merged material must state that it has not been validated in service",
        )

    def test_retired_skill_is_gone(self):
        self.assertFalse(
            (self.root / "skills" / "harness-bootstrap").exists(),
            "harness-bootstrap should be retired; its content lives in project-foundation/references/",
        )

    def test_readme_describes_two_modes_and_drops_the_retired_skill(self):
        self.assertNotIn("harness-bootstrap", self.readme)
        for marker in ("**creation**", "**retrofit**", "two-part `AGENTS.md`"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.readme)


if __name__ == "__main__":
    unittest.main()
