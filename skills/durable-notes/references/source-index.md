# Source index — what this contract borrows and what it does not

This skill is a distillation, not an invention. This file records the lineage so a reader can check the reasoning and so a future version can be argued against its sources rather than against taste.

## Structural sources

**Open Knowledge Format (OKF) v0.2** — GoogleCloudPlatform, `https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md`

Borrowed: the field-tier model (required / recommended / conditional), ISO 8601 timestamps with an explicit UTC offset, the actor forms (`producer/version`, `human:identifier`, `process:identifier`), and the rule that provenance, verification, and freshness fields stay absent when unevidenced rather than filled by default.

Not borrowed: OKF prescribes no note body and no type vocabulary, and this skill preserves that restraint rather than inventing either.

**Johnny.Decimal** — `https://johnnydecimal.com/`

Borrowed: the observation that numbered top-level areas with a reserved system range keep a growing collection navigable. This is the single most common filing pattern among the environments this skill is used in.

Not borrowed: the specific numbering, the decimal numbering, or the folder names. Johnny.Decimal is an *instance* of a portable idea — stable numbered areas — and two vaults applying it differently is the normal case, not a divergence to reconcile.

## Practice sources

The default body (Summary, Key Points, Evidence and Sources, Related Notes, Gaps) and the provenance-first metadata discipline are extracted from working practice across two independent note collections that use different folder schemes and different type vocabularies, and that converged on the same section roles under different labels. That convergence is the evidence for treating the roles as invariant and the labels as environmental.

The verify-before-asserting rules — recompute from published rows, name the denominator, label vendor-run versus independent, state what could not be read — come from repeated failures where a note asserted a figure its own evidence did not support, or stayed silent about a source it had failed to open.

## Deliberately not adopted

- **A fixed type vocabulary.** Both source environments use one, and they differ. Mandating either would make the skill fight the vault it lands in, and losing that fight means the note does not get written.
- **A required index or log.** Useful where they exist, ceremony where they do not.
- **Enforced writing order.** Notes are written under time pressure; a contract that blocks a rough note produces no note and no record.
- **A validator requirement.** Some environments have one, some do not. The skill requires the check when it exists and an honest statement when it does not.
