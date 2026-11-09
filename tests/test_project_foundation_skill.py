from pathlib import Path
import re
import unittest


class ProjectFoundationStandardRulesRouteTests(unittest.TestCase):
    """SKILL.md routes to the canonical block; it must never carry a second copy of it."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "project-foundation"
        cls.skill = (cls.root / "SKILL.md").read_text()
        cls.ref = (cls.root / "references" / "agents-md-general-rules.md").read_text()
        cls.block = re.search(
            r"<!-- BEGIN STANDARD RULES[^>]*-->\n(.*?)<!-- END STANDARD RULES -->", cls.ref, re.S
        ).group(1)

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

    def test_skill_routes_to_the_canonical_block(self):
        for phrase in (
            "references/agents-md-general-rules.md",
            "The block is **not reproduced here**",
            "only source of truth for Part 2",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_skill_does_not_embed_a_second_copy_of_the_block(self):
        self.assertNotIn("<!-- BEGIN STANDARD RULES", self.skill,
                         "the block lives in references/, not in the router")
        for heading in ("### Planning", "### Testing", "### Session discipline",
                        "### Instruction hygiene"):
            with self.subTest(heading=heading):
                self.assertNotIn(heading, self.skill)

    def test_reply_protocol_canary(self):
        for phrase in ('Start every reply with "', "No exceptions."):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.ref)
        for phrase in (
            "functions as a canary",
            "Write a handoff note for a fresh session",
            "not left as `[your name]`",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_status_footer_carries_docs(self):
        for phrase in ("**Goal**", "**Done**", "**Next**", "**Docs**",
                       '**Needs you** (or "nothing")'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.block)

    def test_block_carries_the_mandatory_rules(self):
        flat = " ".join(self.block.split())
        for phrase in (
            "state the plan abstractly",
            "Do not attempt to one-shot a multi-part task",
            "Tests exist to catch regressions",
            "A test added to verify new behavior must fail when that behavior is absent",
            "Run the checks the project defines for the change",
            "Follow the best pattern already in the repository",
            "Before adding code or scaffolding",
            "Before handoff, list what the change made untrue",
            "Failure reports state what failed",
            "Distinguish implemented from verified",
            "Keep AGENTS.md a short router to topic documents",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, flat)

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
        self.assertNotIn("[your name]", self.block)
        self.assertNotIn("Skipper", self.block,
                         "the canary is per-operator; the block itself carries no name")
        self.assertIn("<OPERATOR>", self.ref)

    def test_references_exist(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())

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
        """Change discipline moved into Part 2 in v1.1; SKILL.md routes, it must not restate."""
        ref = (self.root / "references" / "agents-md-general-rules.md").read_text()
        block = re.search(r"<!-- BEGIN STANDARD RULES[^>]*-->\n(.*?)<!-- END STANDARD RULES -->",
                          ref, re.S).group(1)
        flat = " ".join(block.split())
        for phrase in (
            "### Change discipline",
            "Before adding code or scaffolding",
            "deleting, reusing, configuring, or extending",
            "smallest complete change that satisfies the requirement",
            "Do not reduce validation",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, flat)
        self.assertIn("not** a per-project block", self.skill)
        self.assertNotIn("omit this block", self.skill,
                         "Part 2 is identical everywhere; the per-project opt-out is gone")

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


class ProjectFoundationStandardRulesV11Tests(unittest.TestCase):
    """Guards the v1.1 block: promoted Change discipline, unified marker, restored PROGRESS.md."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1]
        cls.ref = (cls.root / "skills" / "project-foundation" / "references"
                   / "agents-md-general-rules.md").read_text()
        cls.block = re.search(
            r"<!-- BEGIN STANDARD RULES[^>]*-->\n(.*?)<!-- END STANDARD RULES -->", cls.ref, re.S
        ).group(1)
        cls.skill = (cls.root / "skills" / "project-foundation" / "SKILL.md").read_text()
        cls.retrofit = (cls.root / "skills" / "project-foundation" / "references"
                        / "retrofit-existing-repo.md").read_text()

    def test_marker_carries_version_and_warning(self):
        marker = re.search(r"<!-- BEGIN STANDARD RULES[^>]*-->\s*", self.ref).group(0)
        self.assertIn("v1.2", marker)
        self.assertIn("do not edit in place", marker)

    def test_all_nine_sections_present(self):
        present = re.findall(r"^### (.+)$", self.block, re.M)
        self.assertEqual(
            present,
            ["Planning", "Testing", "End-to-end verification", "Invariants and boundaries",
             "Change discipline", "Session discipline", "Verification errors", "Completion",
             "Instruction hygiene"],
        )

    def test_change_discipline_lives_in_part_2_not_part_1(self):
        self.assertIn("### Change discipline", self.block)
        self.assertNotIn("```text\n## Change discipline", self.skill,
                         "SKILL.md must not reintroduce the hand-copied per-project block")
        self.assertIn("not** a per-project block", self.skill)

    def test_session_discipline_names_progress_md_with_section_guidance(self):
        sd = self.block[self.block.index("### Session discipline"):self.block.index("### Verification errors")]
        self.assertIn("`PROGRESS.md`", sd)
        self.assertNotIn("handoff record", sd.lower(),
                         "'handoff record' was too vague; PROGRESS.md is the guaranteed artifact")
        for section in ("active-work", "blockers", "verification-status", "next-move"):
            with self.subTest(section=section):
                self.assertIn(section, sd)
        self.assertIn("wastes context", sd)

    def test_overclaiming_lines_are_gone(self):
        flat = " ".join(self.block.split())
        for banned in (
            "Only a full pipeline run counts as real verification",
            "A test that would still pass if the feature were deleted is worthless",
            "A rule that exists only as prose will be skipped",
            "An agent will generate many small, trivial unit tests",
        ):
            with self.subTest(banned=banned):
                self.assertNotIn(banned, flat)

    def test_duplicate_requirements_were_consolidated(self):
        flat = " ".join(self.block.split())
        self.assertEqual(flat.count("component or user-visible"), 1,
                         "end-to-end requirement should be stated once")
        self.assertNotIn("Every rule states why it exists", self.block)
        self.assertNotIn("never buried in", self.block)

    def test_version_note_records_the_changelog(self):
        tail = self.ref[self.ref.index("## Version"):]
        self.assertIn("v1.2", tail)
        self.assertIn("v1.1", tail)
        self.assertIn("Change discipline promoted", tail)

    def test_retrofit_reference_warns_about_the_part_1_copy(self):
        self.assertIn("Change discipline is the live case", self.retrofit)


class ProjectFoundationStandardRulesV12Tests(unittest.TestCase):
    """Guards the v1.2 block: documents a change makes untrue, gated changelog, Docs footer."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1]
        cls.ref = (cls.root / "skills" / "project-foundation" / "references"
                   / "agents-md-general-rules.md").read_text()
        cls.block = re.search(
            r"<!-- BEGIN STANDARD RULES[^>]*-->\n(.*?)<!-- END STANDARD RULES -->", cls.ref, re.S
        ).group(1)

    def slice(self, start, end=None):
        head = self.block.index(start)
        return self.block[head:self.block.index(end)] if end else self.block[head:]

    def test_documents_a_change_makes_untrue_must_be_updated(self):
        session = self.slice("### Session discipline", "### Verification errors")
        for phrase in (
            "what the change made untrue",
            "module maps, invariants, contracts",
            "retired behavior",
            "superseded baseline",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, session)

    def test_document_refresh_is_change_time_process_not_topic_content(self):
        self.assertIn("Before handoff", self.slice("### Session discipline", "### Verification errors"))
        self.assertNotIn("what the change made untrue", self.slice("### Instruction hygiene"))
        self.assertNotIn(
            "what the change made untrue",
            self.slice("### Change discipline", "### Session discipline"),
        )

    def test_changelog_rule_is_gated_on_the_file_existing(self):
        session = self.slice("### Session discipline")
        self.assertIn("If `CHANGELOG.md` exists", session,
                      "a Minimal-tier project without a CHANGELOG.md must not inherit an "
                      "unsatisfiable obligation")
        self.assertIn("## Unreleased", session)

    def test_changelog_taxonomy_stays_minimal(self):
        session = self.slice("### Session discipline")
        for category in ("Added", "Changed", "Fixed"):
            with self.subTest(category=category):
                self.assertIn(category, session)
        self.assertNotIn("Performance", self.block,
                         "Performance is a project-local heading, not a shared category")
        for widened in ("Deprecated", "Security"):
            with self.subTest(widened=widened):
                self.assertNotIn(widened, self.block)

    def test_version_dating_is_deferred_to_release(self):
        session = self.slice("### Session discipline")
        self.assertIn("only at release", session)
        self.assertIn("never edit an entry that has shipped", session)

    def test_status_footer_docs_field_is_observable(self):
        completion = self.slice("### Completion")
        self.assertIn("**Docs**", completion)
        self.assertIn("no routed document describes it", completion)

    def test_nine_sections_and_budget_are_unchanged(self):
        self.assertEqual(len(re.findall(r"^### ", self.block, re.M)), 9)
        self.assertLessEqual(len(self.block.splitlines()), 100)

    def test_the_skill_still_routes_and_does_not_restate(self):
        skill = (self.root / "skills" / "project-foundation" / "SKILL.md").read_text()
        self.assertNotIn("<!-- BEGIN STANDARD RULES", skill)
        self.assertIn("not** a per-project block", skill)



class ProjectFoundationInvocationScopeTests(unittest.TestCase):
    """The skill must not compete for automatic selection, and must say so if opened anyway."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "project-foundation"
        cls.skill = (cls.root / "SKILL.md").read_text()
        end = cls.skill.find("\n---\n", 4)
        cls.frontmatter = cls.skill[4:end]
        match = re.search(r"^description: (.+)$", cls.frontmatter, re.MULTILINE)
        cls.description = match.group(1) if match else ""
        cls.gate = cls.skill[
            cls.skill.index("## Stop gate") : cls.skill.index("## Choose the mode first")
        ]
        cls.when_to_use = cls.skill[
            cls.skill.index("## When to use") : cls.skill.index("## Foundation tiers")
        ]

    def test_model_invocation_is_disabled(self):
        self.assertIn(
            "disable-model-invocation: true",
            self.frontmatter,
            "skill must not compete for automatic selection",
        )

    def test_description_names_the_artifact_not_generic_task_nouns(self):
        self.assertIn("AGENTS.md", self.description)
        self.assertIn("not feature plans", self.description)
        for generic in ("docs, plans", "context, docs"):
            with self.subTest(generic=generic):
                self.assertNotIn(generic, self.description)

    def test_stop_gate_precedes_the_procedure(self):
        self.assertLess(
            self.skill.index("## Stop gate"), self.skill.index("## Choose the mode first")
        )
        self.assertLess(self.skill.index("## Stop gate"), self.skill.index("## Procedure"))

    def test_stop_gate_closes_the_skill_for_feature_work(self):
        for phrase in (
            "plan, design, implement, debug, refactor, review, or document a feature",
            "overrides the gate",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.gate)

    def test_trigger_list_is_state_based_not_project_property(self):
        for banned in (
            "a project expected to span multiple sessions",
            "multiple user-visible requirements that need explicit scope",
            "or verification need durable homes",
        ):
            with self.subTest(banned=banned):
                self.assertNotIn(banned, self.when_to_use)


if __name__ == "__main__":
    unittest.main()
