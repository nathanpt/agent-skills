# Defaults — used only when the environment declares nothing

Every section here is a fallback, not a standard. If the environment states its own destination rule, type vocabulary, body sections, or provenance shape, that wins and this file is not consulted.

## Destination

When no filing scheme exists:

- Place the note beside the work it belongs to, in a `notes/` directory at that project's root.
- Name the directory after the kind of note only if there is more than one kind in play.
- If the note spans several projects, place it where the majority of its evidence lives and link it from the others.
- State the chosen location in your reply. An unannounced filing decision is indistinguishable from a guess.

Do not create a numbered hierarchy, a PARA structure, or any taxonomy on the environment's behalf. A destination scheme is a decision the environment owner makes, and inventing one in a project that has none creates a system nobody agreed to maintain.

## Type vocabulary

The contract requires a `type`. It does not prescribe the values, because types follow the work: an engineering notebook, an email archive, and a research vault will partition the world differently and all three can be internally consistent.

When the environment declares no vocabulary, prefer a small set of lowercase nouns describing the note's function rather than its subject — typically four to eight values total. If you cannot choose without inventing a taxonomy, omit `type` and say in your reply that the environment declares no vocabulary.

Do not carry one environment's vocabulary into another. A note type that exists in one vault and not another is not a defect to fix.

## Body sections

The default order in `SKILL.md` is Summary, Key Points, Evidence and Sources, Related Notes, Gaps. Guidance per section:

- **Summary** — one paragraph, verdict first. Someone who reads only this should know what the note concludes. Do not restate the title.
- **Key Points** — the durable claims as bullets, one claim each. Every numbered claim carries its denominator, benchmark, or date. Bullets that only restate the Summary are noise and should be cut.
- **Evidence and Sources** — what was actually read, what could not be read, and how attributable each figure is. Include the failure lines: a 403, a paywall, a missing attachment.
- **Related Notes** — links to notes this confirms, contradicts, or supersedes. When it supersedes, say so and update the superseded note in the same pass.
- **Gaps** — what remains unresolved, disputed, or unknown, and what evidence would close it.

A note with no Gaps section is either complete or uncritical; say which, rather than leaving the absence ambiguous.

## Provenance

The invariant is that a note must be able to answer "where did this come from", and must never answer falsely. The shape is the environment's choice. Two shapes that both satisfy it:

**Frontmatter array** — structured, queryable, good when one note synthesises several sources.

```yaml
sources:
  - resource: https://example.org/primary-document
    title: Primary Document
    author: Example Organisation
  - resource: internal meeting notes, 2026-11-04
```

**Inline fields or tags** — good when a note traces to exactly one origin, and when the origin is often a ticket, a person, or an attachment rather than a URL.

```yaml
status: follow-up open
source: linked from the central reference folder
ticket: OPS-1234
```

Both are correct. What fails the contract is a `sources` field containing a guessed author, a fabricated URL, or a timestamp nobody recorded.

## Metadata field reference

| Field | Tier | Rule |
|---|---|---|
| `type` | required | non-empty, from the environment's vocabulary |
| `title` | recommended | human-readable display title, states the idea |
| `description` | recommended | one sentence, what the note contains |
| `tags` | recommended | YAML list of short strings |
| `sources` | conditional | only when identifiable material contributed |
| `resource` | conditional | only for a note about one specific canonical asset |
| `generated` | conditional | only when producer and edit time are known |
| `verified` | conditional | only after a real review, naming who reviewed |
| `status` | conditional | lifecycle only, if the environment has one |
| `stale_after` | conditional | only when the note can genuinely become false |

Timestamps, when present, are ISO 8601 with an explicit UTC offset. Actors are one of: `producer/version` for a tool, `human:identifier` for a person, `process:identifier` for an automated process.

## Worked example

```markdown
---
type: <environment's value>
title: Retry Window Sized to the Scheduler, Not the Timeout
description: A circuit breaker sized for the old schedule silenced the job for hours after three failures.
tags: [reliability, scheduling]
sources:
  - resource: https://example.org/run-log-2026-11-04
    title: Run log, 4 November
stale_after: 2027-05-01T00:00:00Z
---

# Retry Window Sized to the Scheduler, Not the Timeout

# Summary

A three-failure cap inside a twelve-hour window meant a job that failed at
03:50 stayed silent until the next day. The cap was never the problem; the
window was.

# Key Points

- Three failures inside 12h produced roughly 20 hours of silence (window 12h,
  next scheduled attempt more than 12h away).
- Shrinking the window to 2h and raising the cap to 4 allows recovery in the
  same night. Observed: 4 attempts across 2h.
- Timeout and attempt count were left unchanged deliberately. Stretching the
  timeout to fix throughput would have hidden the real cause.

# Evidence and Sources

- Read the run log for 4 November in full (14 attempts). Rates recomputed from
  the log's own timestamps, not from the summary table.
- Could not read the scheduler's internal queue state; not exported.

# Related Notes

- Supersedes the earlier note sizing the breaker to the nightly window. That
  note is now marked superseded.

# Gaps

- Untested: whether 4 attempts is enough on a night with an upstream outage
  longer than 2h. Evidence would be one such night in the run log.
```
