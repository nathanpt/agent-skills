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
2. **Nothing else.** Version markers, if present, are updated as a set.

Adjust a rule only by making it **stronger or more specific** — never weaker, and never
silently omitted.

## The block

Everything between the markers is Part 2. Reproduce it byte for byte.

```markdown
<!-- BEGIN STANDARD RULES v1.0 -->
### Planning

Before writing code, state the plan abstractly: what the system does, which
boundaries the change crosses, what data moves and in which direction, and what
would prove the change works. Solve the general problem before the specific
case. Do not enumerate implementation steps as a substitute for understanding
the shape of the problem.

Take on one unit of work at a time. Do not attempt to one-shot a multi-part task;
half-finished work left behind is worse than unstarted work.

### Testing

Tests exist to catch regressions, not to raise a coverage number. An agent will
generate many small, trivial unit tests that assert implementation details and
prove nothing; refuse that.

- Prefer a small number of high-value tests over a large number of shallow ones.
- Every test names the regression it catches in its name or its message.
- Do not test internals, private helpers, framework behavior, or constants.
- Do not mock away the behavior under test.
- For cross-component or user-visible changes, unit tests are necessary but
  insufficient: the change is not verified until the real path runs end to end.
- A test that would still pass if the feature were deleted is worthless.

### End-to-end verification

Only a full pipeline run counts as real verification. Unit tests are
systematically blind to component-boundary defects: interface mismatches, state
propagation, resource lifecycle, and environment differences all survive a green
unit suite.

- Level 1: unit tests (must pass)
- Level 2: integration tests (must pass)
- Level 3: end-to-end run through the real system (must pass whenever the change
  crosses a boundary)
- Skipping a required level means **not complete**, and is reported as
  `unverified`, never as passing.
- Record the exact command and the observed result. "Should work" is not
  evidence.
- Before starting new work, confirm the existing baseline still works. Finding
  out the project was already broken is cheaper than adding to a broken base.

### Invariants and boundaries

- Enforce invariants, not implementations. Control boundaries, data shapes, and
  dependency direction; leave the internals to the implementer.
- Parse data at the boundary. Never build on a guessed shape from an external
  system, an untyped payload, or a library's undocumented behavior.
- When a rule actually matters, encode it as a test or a lint with a fix-oriented
  error message. A rule that exists only as prose will be skipped.
- Follow the best pattern already in the repository, not merely the nearest one.
  Agents copy whatever they see first, including the bad example.

### Session discipline

- Start by reading the progress file and the recent git log, then verify the
  baseline. Do not begin by writing code.
- Work one feature at a time, selected from the feature list.
- Only a passing verification moves a feature to done. Never edit the feature
  list, weaken a requirement, or delete a test to make progress look better.
- End the session in a clean state: commit the work and update the progress file
  so the next session does not have to guess what happened.

### Verification errors

Failure messages must state what failed, why it matters, and how to fix it. An
error that says only what broke, without the fix, wastes a session.

### Completion

Never report work as complete, done, passing, or shipped on the strength of code
that was not executed. Distinguish implemented from verified. State what remains
unverified and what evidence would close it.

End any turn that reports on long-running or delegated work with a short status: **Goal**, **Done**, **Next**, **Needs you** (or "nothing").

### Instruction hygiene

This file is a router, not an encyclopedia. Keep it under roughly 200 lines and
its hard constraints under 15.

- A new rule goes into a topic document unless it is a genuine red line.
- Every rule states why it exists and when it can be removed.
- Do not restate what the code, types, or config already say.
- Critical rules belong at the top or the bottom of this file — never buried in
  the middle, where they get lost.
<!-- END STANDARD RULES -->
```

## Verifying a generated file

- Line 1 is the canary, above every heading.
- `## Part 1 — Project` and `## Part 2 — Standard rules (all projects)` both exist.
- The block is byte-identical to this file — diff it rather than eyeballing it.
- Total length stays near 200 lines and hard constraints under 15 (instruction hygiene).
- Project-specific commands, boundaries, and constraints are all in Part 1, not scattered
  into Part 2.

## Version

**v1.0** — 2026-11-01. Rule content: abstract planning, regression-focused testing,
end-to-end verification, invariants and boundaries, session discipline, fix-oriented
verification errors, completion honesty with a status footer, instruction hygiene.
