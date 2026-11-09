from pathlib import Path
import re
import unittest


class DurableNotesContractTests(unittest.TestCase):
    """The portable note contract: shape, invariants, and what it must refuse to dictate."""

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1] / "skills" / "durable-notes"
        cls.skill = (cls.root / "SKILL.md").read_text()
        cls.defaults = (cls.root / "references" / "defaults.md").read_text()
        cls.sources = (cls.root / "references" / "source-index.md").read_text()
        cls.flat = " ".join(cls.skill.split())

    def test_frontmatter_and_trigger(self):
        self.assertTrue(self.skill.startswith("---\n"))
        end = self.skill.find("\n---\n", 4)
        self.assertGreater(end, 0)
        frontmatter = self.skill[4:end]
        self.assertIn("name: durable-notes", frontmatter)
        match = re.search(r"^description: (.+)$", frontmatter, re.MULTILINE)
        if match is None:
            self.fail("description frontmatter is missing")
        description = match.group(1)
        self.assertTrue(description.startswith("Use when"),
                        "description must open with a self-contained trigger")
        first_sentence = description.split(". ")[0]
        self.assertLessEqual(len(first_sentence), 70,
                             "the trigger phrase must survive truncation")
        self.assertIn("version:", frontmatter)

    def test_version_marker_is_present_and_consistent(self):
        marker = re.search(r"<!-- DURABLE NOTE CONTRACT v(\d+\.\d+)[^>]*-->", self.skill)
        if marker is None:
            self.fail("contract version marker is missing")
        self.assertEqual(marker.group(1), "1.0")
        self.assertIn("version: 1.0.0", self.skill.split("---")[1])

    def test_stays_small(self):
        lines = len(self.skill.splitlines())
        self.assertLessEqual(
            lines, 95,
            f"SKILL.md is {lines} lines; a contract read every session has to stay small — "
            "push detail into references/",
        )

    def test_no_environment_specific_paths(self):
        for leak in ("/home/", "40_Knowledge", "90_System", "_index/",
                     "validate_okf", ".docs/", "Obsidian/", "obsidian/"):
            with self.subTest(leak=leak):
                self.assertNotIn(leak, self.skill)
                self.assertNotIn(leak, self.defaults)

    def test_does_not_impose_a_type_vocabulary(self):
        for vocabulary_value in ("`concept`", "`procedure`", "`evaluation`",
                                 "`tooling`", "`research`", "`decision`"):
            with self.subTest(value=vocabulary_value):
                self.assertNotIn(vocabulary_value, self.skill)
        self.assertIn("do not carry one environment's vocabulary into another",
                      " ".join(self.defaults.split()).lower())
        self.assertIn("omit `type` and say why", self.flat)

    def test_profile_handshake_names_five_surfaces(self):
        handshake = self.skill[self.skill.index("## 0."):self.skill.index("## 1.")]
        for surface in ("Destination", "Type vocabulary", "Body sections",
                        "Provenance shape", "Index, log, validator"):
            with self.subTest(surface=surface):
                self.assertIn(surface, handshake)
        self.assertIn("Read; do not invent.", handshake)

    def test_invariants_are_stated_and_not_optional(self):
        invariants = self.skill[self.skill.index("## 1."):self.skill.index("## 2.")]
        required = (
            "Never invent provenance, actors, or timestamps",
            "One idea per note",
            "state the idea, not the source",
            "Verify before asserting",
            "State what you could not read",
            "Supersede explicitly",
            "Durability gate",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, invariants)
        self.assertIn("not configurable", invariants)

    def test_default_body_order_is_fixed(self):
        body = self.skill[self.skill.index("## 2."):self.skill.index("## 3.")]
        order = ["Summary", "Key Points", "Evidence and Sources", "Related Notes", "Gaps"]
        positions = [body.index(section) for section in order]
        self.assertEqual(positions, sorted(positions),
                         "default body sections are out of order")

    def test_variant_labels_map_onto_roles(self):
        for variant in ("Key Takeaways", "Sources", "Content"):
            with self.subTest(variant=variant):
                self.assertIn(variant, self.skill)
        self.assertIn("the roles do not", self.flat)

    def test_metadata_tiers(self):
        metadata = self.skill[self.skill.index("## 4."):self.skill.index("## 5.")]
        self.assertIn("**Required:** `type`", metadata)
        for field in ("title", "description", "tags", "sources", "resource",
                      "generated", "verified", "status", "stale_after"):
            with self.subTest(field=field):
                self.assertIn(field, metadata)
        self.assertIn("Never add a field to satisfy a template", metadata)

    def test_absence_of_tooling_is_stated_not_implied(self):
        filing = self.skill[self.skill.index("## 5."):]
        self.assertIn("do not silently imply a check that did not happen", filing)

    def test_verification_requires_rereading_the_note(self):
        verify = self.skill[self.skill.index("## 5."):]
        self.assertIn("Re-read the note you wrote", verify)
        self.assertIn("unverified", verify)

    def test_scope_excludes_operational_records(self):
        self.assertIn("Not for journals, task lists, transcripts, or raw dumps", self.flat)

    def test_references_exist_and_are_all_linked(self):
        for reference in re.findall(r"`(references/[^`]+\.md)`", self.skill):
            with self.subTest(reference=reference):
                self.assertTrue((self.root / reference).is_file())
        on_disk = {p.name for p in (self.root / "references").glob("*.md")}
        self.assertEqual(on_disk, {"defaults.md", "source-index.md"},
                         "every reference must be linked from SKILL.md")

    def test_attribution_is_recorded(self):
        for source in ("Open Knowledge Format", "johnnydecimal.com",
                       "Deliberately not adopted"):
            with self.subTest(source=source):
                self.assertIn(source, self.sources)

    def test_no_unfilled_placeholders(self):
        for text in (self.skill, self.defaults, self.sources):
            for placeholder in ("[your name]", "TODO", "TBD", "FIXME", "XXX"):
                with self.subTest(placeholder=placeholder):
                    self.assertNotIn(placeholder, text)


class DurableNotesReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).parents[1]
        cls.readme = (cls.root / "README.md").read_text()

    def test_readme_lists_the_skill(self):
        self.assertIn("### `durable-notes`", self.readme)
        layout = self.readme[self.readme.index("## Repository layout"):self.readme.index("## Reference policy")]
        self.assertIn("  durable-notes/\n    SKILL.md", layout,
                      "the skill must appear inside the repository layout tree")
        self.assertIn("references/\n      defaults.md", layout)

    def test_readme_documents_install_and_invocation(self):
        self.assertIn("cp -R agent-skills/skills/durable-notes", self.readme)
        self.assertIn("/skill:durable-notes", self.readme)


if __name__ == "__main__":
    unittest.main()
