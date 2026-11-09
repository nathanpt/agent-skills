# Standard AGENTS.md rules (Part 2)

The canonical house rule set for every project. Copy this into the **Part 2** section of
each project's `AGENTS.md` verbatim. Do not paraphrase it, summarise it, reorder it, or
drop rules because they look redundant with the rest of the skill — its whole purpose is
to be read by an agent that never loads this skill.

## The two-part file

Every `AGENTS.md` has exactly two parts:

```markdown
Start every reply with "<OPERATOR>,". No exceptions.

# AGENTS.md — <Project>

## Part 1 — Project

<overview, quick-start commands, this repo's own hard constraints, routing>

## Part 2 — Standard rules (all projects)

<the block below, unmodified>
```

**Part 1** is written per repository and differs everywhere. **Part 2** is identical
everywhere. Part 1 may add constraints; it may never relax a Part 2 rule.

Order matters: project content comes first because commands are what an agent needs
most, and burying them under ~90 lines of universal boilerplate is why agents skim.

## Substitutions the template requires

Only two things may differ in Part 2:

1. **The reply-protocol canary on line 1.** Use the operator's own distinctive form of
   address — a token personal to them, not a legal or common name, so no generic
   assistant emits it by accident. It is a canary: if the first line stops appearing,
   the file's rules are being dropped. When that happens, ask for a handoff note and
   start a fresh session.
2. **Nothing else.** The marker line carries the version and the do-not-edit warning, and
   must match this file exactly, including that warning.

Adjust a rule only by making it **stronger or more specific** — never weaker, and never
silently omitted.

## The block

Everything between the markers is Part 2. Reproduce it byte for byte, marker included.

```markdown
<!-- BEGIN STANDARD RULES v1.2 — identical across all projects; do not edit in place -->
### Planning

Before writing code, state the plan abstractly: what the system does, which
boundaries the change crosses, what data moves and in which direction, and what
would prove the change works. Do not enumerate implementation steps as a
substitute for understanding the shape of the problem.

Do not attempt to one-shot a multi-part task; half-finished work left behind is
worse than unstarted work.

### Testing

Tests exist to catch regressions, not to raise a coverage number.

- A test added to verify new behavior must fail when that behavior is absent.
- Every test names the behavior or regression it protects, in its name or its
  message.
- Prefer observable-behavior tests; test internal logic, private helpers, or
  framework interaction when they carry a specific correctness risk.
- Do not mock away the behavior under test.

### End-to-end verification

Unit tests are systematically blind to component-boundary defects: interface
mismatches, state propagation, resource lifecycle, and environment differences
all survive a green unit suite.

Run the checks the project defines for the change: unit, then integration, then
end-to-end through the real system when the change crosses a component or
user-visible boundary.

Record the exact command and the observed result. "Should work" is not evidence.

### Invariants and boundaries

- Control boundaries, data shapes, and dependency direction; leave the internals
  to the implementer.
- Parse data at the boundary. Never build on a guessed shape from an external
  system, an untyped payload, or a library's undocumented behavior.
- Encode mechanically checkable invariants in tests or lint rules, with
  actionable failure messages.
- Follow the best pattern already in the repository, not merely the nearest one.
  Agents copy whatever they see first, including the bad example.

### Change discipline

- Before adding code or scaffolding, inspect the relevant paths and ask whether
  the requested outcome can be met by deleting, reusing, configuring, or
  extending something already present.
- Check existing implementations, platform facilities, standard-library
  functions, and installed dependencies before adding new code or dependencies.
- Implement the smallest complete change that satisfies the requirement. Do not
  add speculative abstractions, generality, files, or configuration.
- Do not reduce validation, error handling, security checks, accessibility,
  tests, observability, or readability merely to reduce lines.

### Session discipline

- Start by reading `PROGRESS.md` — the active-work, blockers, verification-status,
  and next-move sections, not the whole file — then the recent git log. Reading
  the entire file wastes context; read the sections that decide what to do now.
- Then run the baseline checks and record any pre-existing failures. Do not begin
  by writing code.
- Work on one bounded unit at a time, selected from the feature list when the
  project has one.
- Only a passing verification moves a feature to done. Never weaken acceptance
  criteria or delete a test to make progress look better.
- At handoff, record what changed, the verification results, and what is
  unfinished in the progress file. Commit only when the project workflow or the
  user asks for it.
- Before handoff, list what the change made untrue and update every document
  that describes it — module maps, invariants, contracts, verification
  baselines. A routed document must never describe retired behavior or a
  superseded baseline.
- If `CHANGELOG.md` exists, add each user-visible change to `## Unreleased`
  under Added, Changed, or Fixed in the same session. Set versions and dates
  only at release; never edit an entry that has shipped.

### Verification errors

Failure reports state what failed, its impact, and either a known fix or the next
diagnostic step. Label uncertain causes rather than inventing a remedy.

### Completion

Never report work as complete, done, passing, or shipped on the strength of code
that was not executed. Distinguish implemented from verified. Report complete or
passing only when the applicable required checks have run and passed; otherwise
state what remains unverified and what evidence would close it.

End any turn that reports on long-running or delegated work with a short status: **Goal**, **Done**, **Next**, **Docs**, **Needs you** (or "nothing"). **Docs** names the routed documents this change updated, or states that no routed document describes it.

### Instruction hygiene

Keep AGENTS.md a short router to topic documents: check the combined Part 1 and
Part 2 against the roughly 200-line budget, with hard constraints under 15.

- A new rule goes into a topic document unless it is a genuine red line.
- Do not restate what the code, types, or config already say.
<!-- END STANDARD RULES -->
```

## Verifying a generated file

- Line 1 is the canary, above every heading.
- `## Part 1 — Project` and `## Part 2 — Standard rules (all projects)` both exist.
- The marker line matches this file exactly, including the do-not-edit warning.
- The block is byte-identical to this file — diff it rather than eyeballing it.
- All nine sections are present: Planning, Testing, End-to-end verification, Invariants
  and boundaries, Change discipline, Session discipline, Verification errors, Completion,
  Instruction hygiene.
- The Completion status footer carries all five fields, including **Docs**.
- Total length stays near 200 lines and hard constraints under 15 (instruction hygiene).
- Project-specific commands, boundaries, and constraints are all in Part 1, not scattered
  into Part 2.

## Applying an update to an existing project

Part 2 changed, so a project on an older version needs two edits, not one:

1. Replace everything between the markers with the current block.
2. **Delete any rule that now lives in Part 2 from Part 1.** Change discipline is the
   v1.1 case: earlier versions hand-copied those four bullets into Part 1 of every
   project. Leaving the copy in place recreates the duplication the promotion removed,
   and the two copies will drift. The document-refresh and `CHANGELOG.md` rules are the
   v1.2 case: any project that already states them in Part 1 (as a "keep ARCHITECTURE
   fresh" or "maintain CHANGELOG" hard constraint) deletes those lines rather than
   carrying both.
3. **Check the status footer.** A footer missing **Docs** is a pre-v1.2 file even if
   every other line matches.

## Version

**v1.2** — 2026-11-09. Nine sections, 99 lines, 737 words.

Changed from v1.1 (92 lines, 651 words):

- **Two session-discipline rules for documents a change makes untrue.** v1.1 required
  reading a routed topic document before changing its subject but never required updating
  it afterwards, and never mentioned `CHANGELOG.md` at all. An agent following v1.1 exactly
  could hand off a correct diff whose architecture document still described a retired
  algorithm and whose changelog had no entry, and would have been compliant. Both rules
  are change-time process, which is Session discipline's job, and both are gated on the
  artifact existing so a Minimal-tier project without a `CHANGELOG.md` incurs no
  unsatisfiable obligation.
- **Added `Docs` to the status footer.** The two rules above are prose an agent has to
  remember; that is the mechanism that already failed. The footer field makes the answer
  visible in every handoff and checkable by the operator without a hook — the same
  observable-canary approach as the reply protocol, which is the one enforcement pattern
  this block already trusts.
- **Changelog categories held to Added / Changed / Fixed.** A project needing `Removed`,
  `Deprecated`, or `Security` names them in Part 1 rather than widening the shared block;
  three categories already cover every user-visible change, and a longer taxonomy invites
  each repo to pick a different subset.

**v1.1** — 2026-11-01. Nine sections, 92 lines, 651 words.

Changed from v1.0 (87 lines, 684 words):

- **Change discipline promoted from Part 1 into Part 2.** The four bullets were
  hand-copied into every project's Part 1, where they drifted and contradicted Part 2.
  They now have one home. A project gains ~5 lines in Part 2 and loses 6–11 from Part 1
  when the copy is removed, so consolidation is roughly neutral on line count — the gain
  is a single source of truth, not brevity.
- **Removed the overbroad "Only a full pipeline run counts as real verification."** The
  block's own level ladder contradicted it five lines later; an agent obeying it literally
  would run the whole pipeline for a one-line rename.
- **Collapsed three duplicate statements of end-to-end verification into one.**
- **Scoped the "worthless test" line** so it no longer condemns existing-behaviour
  regression tests, and **softened the blanket ban on testing internals.**
- **Deleted two unfalsifiable predictions** ("an agent will generate many small, trivial
  unit tests", "a rule that exists only as prose will be skipped").
- **Fixed a self-contradiction in session discipline:** "never edit the feature list"
  blocked the update the preceding sentence requires.
- **Restored an explicit `PROGRESS.md` instruction** with section-level reading guidance,
  so an agent skims the four sections that decide what to do next instead of loading the
  whole file.
- **Made commits conditional** on the project workflow or the user asking, rather than
  unconditional.
- **Cut two instruction-hygiene bullets** addressed to the file's maintainer rather than
  the agent reading it.
- **Unified the version marker** with the do-not-edit warning that project copies already
  carried.
