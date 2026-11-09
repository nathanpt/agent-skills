---
name: durable-notes
description: Use when capturing, filing, or updating a durable note. Defines the portable note contract — body, metadata, provenance — and leaves taxonomy and destinations to the environment.
version: 1.0.0
author: Nathan (nathanpt), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [notes, knowledge-management, provenance, documentation, portability]
    related_skills: []
---

# Durable Notes

<!-- DURABLE NOTE CONTRACT v1.0 — portable. Environment specifics belong in that environment's profile, never here. -->

A durable note is expected to stay useful after the conversation that produced it ends. This skill defines what such a note must contain, anywhere. It does not decide where notes live, which types a vault has, or what validates them — that is the environment's job.

Use it when capturing an external item, decision, procedure, or finding as a note that should outlive the session; when updating or superseding an existing note; or when auditing whether something written down is durable at all.

Not for journals, task lists, transcripts, or raw dumps. Those are operational records with a different lifecycle, and forcing them into this contract produces ceremony without value.

## 0. Read the environment profile first

Establish these five surfaces before writing. Reuse whatever the environment already declares — in its own instructions, an existing note of the same kind, or a config file. Read; do not invent.

| Surface | What you need | If the environment declares none |
|---|---|---|
| Destination | how a note's location is chosen | `references/defaults.md` § Destination |
| Type vocabulary | the values `type` may take | omit `type` and say why |
| Body sections | any override of the default body | default body, § 2 |
| Provenance shape | frontmatter, tags, inline link, ticket, attachment | `references/defaults.md` § Provenance |
| Index, log, validator | whether they exist, and the exact command | skip those steps silently |

Two vaults numbering the same subject differently is normal. Do not harmonize them, and do not import one environment's destination scheme or type vocabulary into another.

## 1. Invariants — not configurable

These hold everywhere. A "flexible" version of any of them is a note that cannot be trusted later, which makes the note worthless regardless of how well it was filed.

- **Never invent provenance, actors, or timestamps.** If the source is unknown, the note says nothing about it. An absent field is honest; a plausible guess survives review and poisons everything downstream.
- **One idea per note.** If the title needs "and", it is two notes.
- **The title and filename state the idea, not the source.** Provenance belongs in metadata. A title naming its source is a filing failure even when the file sits in the right folder.
- **Verify before asserting.** Recompute figures from their published rows, name the denominator of every percentage, and label each claim as vendor-run, independent, single-source, or corroborated. State the method, not only the number.
- **State what you could not read.** A paywall, a 403, a missing attachment, a dead link. Silence about a failed read reads as coverage.
- **Supersede explicitly.** When a new note replaces an old one, update the old one's verdict in place. Never leave two live answers.
- **Durability gate.** If it will not be useful next month, do not file it as durable knowledge.

## 2. Body — default shape

```
# <idea as title>
<one-line verdict, if the title alone is not enough>

# Summary        one paragraph: what this is and what it means
# Key Points     the durable claims, as bullets
# Evidence and Sources   what was read, what failed, figures and their vintage
# Related Notes  links to what this confirms, contradicts, or supersedes
# Gaps           what is unresolved, disputed, or unknown
```

Labels vary between environments; the roles do not. Map variants onto the roles rather than adopting a second structure: a "Key Takeaways" section is Key Points, a bare "Sources" section is Evidence and Sources, and a raw "Content" body is a capture, not a knowledge body — it earns the contract only once it has a Summary and Key Points. Omit a section with nothing true to put in it. Do not pad. Per-section guidance is in `references/defaults.md`.

## 3. Triage before writing

- Search for existing coverage of the distinctive claim, figure, or decision. If a note covers it, append with a date stamp instead of writing a second one.
- A reaction or repost pointing at a durable item is not its own note; fold it in as a line of reception.
- An item with no durable claim — an announcement with no content, an opinion with no reasoning — is reported as such and filed nowhere.

## 4. Metadata — default contract

**Required:** `type` — a non-empty value from the environment's vocabulary.

**Recommended:** `title`, `description` (one sentence), `tags` (list of short strings).

**Conditional, only when the evidence exists:** `sources`, `resource`, `generated`, `verified`, `status`, `stale_after`. The rule for each, and the timestamp and actor forms, are in `references/defaults.md`.

Never add a field to satisfy a template. Preserve unknown keys when editing someone else's note.

## 5. File it, then verify

Follow the environment's destination rule. Then, only if the environment has them: add the index row, append the log entry, attach and embed required media where documented, and run the validator with its exact command. If it has none of those, say so plainly — do not silently imply a check that did not happen.

- Re-read the note you wrote. The commonest defect is a claim in the body that its own Evidence section does not support.
- Report what the validator said, including when it ran only against your own note.
- State anything left unverified as unverified. A note is not complete because it was written; it is complete when its provenance supports its claims.

## References

- `references/defaults.md` — per-section guidance, metadata field table, provenance shapes, destination fallback, worked example.
- `references/source-index.md` — what this borrows, from where, and what it deliberately does not adopt.
