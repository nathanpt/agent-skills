---
name: project-foundation
description: Create concise project context, docs, plans, and checks.
---

# Project Foundation

Use this skill when starting a new project or when an early repository lacks a coherent operating foundation. Create the smallest useful repository-local knowledge system so future agents can discover the project without loading one oversized `AGENTS.md`.

This skill initializes a project. For an established repository with history, conflicting files, generators, or stale documentation, use `harness-bootstrap` instead.

## Core principles

- Inspect before creating: confirm the required outcome, search for what already exists, and add only the smallest complete change.
- Prefer deletion, reuse, configuration, native platform facilities, standard-library functions, and already-installed dependencies before new code or dependencies.
- Keep `AGENTS.md` a short router, not an encyclopedia.
- Store deeper knowledge in versioned repository-local documents.
- Create only documents that answer a real project question.
- Prefer machine-readable state for requirements and pass/fail status.
- Make one meaningful feature change at a time on long-running projects.
- Match verification depth to the changed boundary.
- Record decisions without rewriting history.
- Leave a clean, understandable handoff state after each session.
- Never trade away validation, error handling, security, accessibility, tests, observability, or readability merely to reduce code.
- Do not add code comments unless the project explicitly requires them; prefer clear names, tests, and documentation where appropriate.

## When to use

Use for:

- a new repository or empty Git project;
- an early project with unclear structure or no agent-facing context;
- a project expected to span multiple sessions or agents;
- a project with multiple user-visible requirements that need explicit scope;
- a project where architectural decisions, execution plans, or verification need durable homes.

Do not use for:

- a mature repository that already has a trustworthy context system;
- a single-file experiment or disposable script unless the user asks for the structure;
- a documentation-only request that does not establish a project foundation;
- blindly replacing existing `AGENTS.md`, architecture, progress, or generator-owned files.

## Foundation tiers

Choose the smallest tier that fits the intended project scope and lifecycle, not merely the amount of code currently present. State the selected tier and why. A pre-implementation foundation request accompanied by a design, requirements, product, or architecture document is governed by the completeness guard below and is at least Standard unless the user explicitly chooses Minimal.

### Minimal

For a small utility, library, or experiment:

```text
README.md
AGENTS.md        only if an agent will maintain the project
```

Add `ARCHITECTURE.md`, `PROGRESS.md`, or `CHANGELOG.md` only when each has a distinct useful question to answer.

### Standard

For a multi-session project:

```text
README.md
AGENTS.md
ARCHITECTURE.md
PROGRESS.md
CHANGELOG.md
docs/
├── exec-plans/
│   ├── active/
│   └── completed/
└── references/
```

Add `docs/feature-list.json` when the project has multiple independently testable requirements.

### Full

For a substantial product or long-running agent project:

```text
README.md
AGENTS.md
ARCHITECTURE.md
PROGRESS.md
CHANGELOG.md
docs/
├── design-docs/
│   └── index.md
├── decisions/
│   └── README.md
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── feature-list.json
├── generated/
├── product-specs/
│   └── index.md
└── references/
```

Create additional root documents only when the project has the relevant surface:

```text
DESIGN.md
FRONTEND.md
PLANS.md
PRODUCT_SENSE.md
QUALITY_SCORE.md
RELIABILITY.md
SECURITY.md
```

Do not create empty placeholder files merely to match the full layout. A justified foundation document is not an empty placeholder: populate it with confirmed facts, explicit unknowns, applicable commands, and the next question or check.

## Initializer completeness guard

Before creating files, build an applicability matrix for every candidate in the selected tier and every conditional root document or directory. Give each candidate exactly one disposition:

- `create` — create it now and populate it with the facts and unknowns currently available;
- `preserve` — an existing authoritative or generator-owned artifact already serves the purpose;
- `not applicable` — the repository has concrete evidence that the corresponding project surface does not exist, or the user explicitly declined the artifact.

The selected tier’s baseline artifacts cannot be marked `not applicable`. They must be created or explicitly preserved. Conditional artifacts must be created when their surface is evidenced. Report the matrix, including the evidence for every `not applicable` decision, before declaring the foundation complete. Any candidate omitted without a disposition is a failure of the initializer.

A repository with no implementation can still need a complete foundation. “Not started,” “no code yet,” “the details are unknown,” and “this would be sparse” are forbidden reasons to skip an appropriate artifact. Capture the current state as unknown or undecided and record the next check instead. If the repository contains a design, requirements, product, or architecture document and the user asked for foundation before implementation, treat that as evidence of an intended multi-session project and select at least the Standard tier unless the user explicitly chooses Minimal. Preserve the existing design file, including a case variant such as `design.md`, link it from `AGENTS.md`, and create the remaining selected-tier baseline artifacts.

## Procedure

### 1. Establish repository reality

Before writing anything, inspect:

```bash
pwd
git status --short
git branch --show-current
git log --oneline -10
```

Check the root and relevant subdirectories for case-insensitive variants of:

```text
AGENTS.md
README.md
ARCHITECTURE.md
PROGRESS.md
CHANGELOG.md
DESIGN.md
FRONTEND.md
PLANS.md
PRODUCT_SENSE.md
QUALITY_SCORE.md
RELIABILITY.md
SECURITY.md
docs/
```

Read existing instructions, manifests, README material, generators, test configuration, and deployment files before deciding what to create.

If the repository is not actually new or early-stage, stop and recommend `harness-bootstrap`. Do not replace established context under the pretext of initialization.

### 2. Define the project foundation

Extract or confirm:

- project purpose;
- intended users or consumers;
- primary language/runtime/framework;
- entry points and how to run the project;
- required setup and verification commands;
- major boundaries and external dependencies;
- initial requirements or feature scope;
- known architectural, security, data, or deployment decisions.

Do not invent missing details. Mark unknowns in `PROGRESS.md` or ask the user when they block the foundation.

### 3. Create the repository map

Before creating any file in this step, apply the initializer completeness guard. The matrix is part of the foundation run, not an optional after-the-fact explanation; do not continue with document creation while any candidate lacks a disposition.

Create `AGENTS.md` only when an agent will work in the repository. Keep it roughly 50–200 lines, with the shortest useful version preferred.

It should contain only:

1. Project overview.
2. Quick-start/setup/test/check commands.
3. A small prioritized set of global hard constraints — **including the five mandatory rules below**.
4. Links to topic documents with applicability conditions.
5. Completion and reporting requirements.

Structure the file in exactly two parts:

- **Part 1 — Project.** Items 1–5 above: what this repository is, its commands, its own
  hard constraints, its routing. Written per repository; never shared between projects.
- **Part 2 — Standard rules (all projects).** The house rule set — abstract planning,
  regression-focused testing, end-to-end verification, invariants and boundaries, session
  discipline, fix-oriented errors, completion honesty, instruction hygiene. Identical in
  every repository.

Do not write Part 2 from scratch or paraphrase it. Copy it verbatim from
[`references/agents-md-general-rules.md`](references/agents-md-general-rules.md), which
holds the canonical block plus the template and its verification steps. Line 1 of every
generated file is the operator's reply-protocol canary, above all headings; substitute the
operator's own form of address and never leave a placeholder.

#### Mandatory `AGENTS.md` rules

These rules are **required, verbatim, in every generated `AGENTS.md`**, above the project's own constraints. Do not paraphrase them, summarize them into one bullet, or drop any because they seem redundant with the rest of the skill. Their purpose is to be read by an agent that has not loaded this skill.

Three of them are **reply-protocol settings that must be parameterized per project**: the operator's form of address, and the status footer. Fill them in when writing the file; never leave a placeholder.

```markdown
Start every reply with "Skipper,". No exceptions.

## Planning

Before writing code, state the plan abstractly: what the system does, which
boundaries the change crosses, what data moves and in which direction, and what
would prove the change works. Solve the general problem before the specific
case. Do not enumerate implementation steps as a substitute for understanding
the shape of the problem.

Take on one unit of work at a time. Do not attempt to one-shot a multi-part task;
half-finished work left behind is worse than unstarted work.

## Testing

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

## End-to-end verification

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

## Invariants and boundaries

- Enforce invariants, not implementations. Control boundaries, data shapes, and
  dependency direction; leave the internals to the implementer.
- Parse data at the boundary. Never build on a guessed shape from an external
  system, an untyped payload, or a library's undocumented behavior.
- When a rule actually matters, encode it as a test or a lint with a fix-oriented
  error message. A rule that exists only as prose will be skipped.
- Follow the best pattern already in the repository, not merely the nearest one.
  Agents copy whatever they see first, including the bad example.

## Session discipline

- Start by reading the progress file and the recent git log, then verify the
  baseline. Do not begin by writing code.
- Work one feature at a time, selected from the feature list.
- Only a passing verification moves a feature to done. Never edit the feature
  list, weaken a requirement, or delete a test to make progress look better.
- End the session in a clean state: commit the work and update the progress file
  so the next session does not have to guess what happened.

## Verification errors

Failure messages must state what failed, why it matters, and how to fix it. An
error that says only what broke, without the fix, wastes a session.

## Completion

Never report work as complete, done, passing, or shipped on the strength of code
that was not executed. Distinguish implemented from verified. State what remains
unverified and what evidence would close it.

End any turn that reports on long-running or delegated work with a short status: **Goal**, **Done**, **Next**, **Needs you** (or "nothing").

## Instruction hygiene

This file is a router, not an encyclopedia. Keep it under roughly 200 lines and
its hard constraints under 15.

- A new rule goes into a topic document unless it is a genuine red line.
- Every rule states why it exists and when it can be removed.
- Do not restate what the code, types, or config already say.
- Critical rules belong at the top or the bottom of this file — never buried in
  the middle, where they get lost.
```

**Choosing the form of address.** Pick a single distinctive token that is personal to the operator and not one of their legal or common names — something no generic assistant would emit by accident. It functions as a canary: if the first line stops appearing, the file's rules are being dropped. When the agent stops using it, ask for a handoff note and start a fresh session:

```text
Write a handoff note for a fresh session: the goal, what's done, the decisions we
made and why, open problems, and the exact next step. Keep file paths and
commands as they are.
```

Adjust any rule only by making it **stronger or more specific** — never weaker, and never silently omitted.

Example routing entries:

```text
- Read ARCHITECTURE.md before changing system boundaries or major modules.
- Read docs/feature-list.json before selecting the next feature.
- Read docs/decisions/ before changing a decision they constrain.
- Read docs/exec-plans/active/ when continuing planned work.
- Run the applicable verification level before marking work complete.
```

When the repository will be maintained with code, include this compact implementation-discipline block in `AGENTS.md`:

```text
## Change discipline

- Before adding code or scaffolding, inspect the relevant paths and ask whether the requested outcome can be met by deleting, reusing, configuring, or extending something already present.
- Check existing implementations, platform facilities, standard-library functions, and installed dependencies before adding new code or dependencies.
- Implement the smallest complete change that satisfies the requirement. Do not add speculative abstractions, generality, files, or configuration.
- Do not reduce validation, error handling, security checks, accessibility, tests, observability, or readability merely to reduce lines.
```

For a documentation-only or otherwise non-code project, omit this block when it would add noise. Treat “smallest” as a constraint on unnecessary work, not as permission to ship an incomplete or unsafe result.

Do not put the full architecture, historical incident log, every preference, or every topic rule into `AGENTS.md`.

Create `ARCHITECTURE.md` when the project has meaningful structure. It should answer:

- What is this system?
- Where does work start?
- How do the major components relate?
- What are the important boundaries and invariants?
- Where should an agent look next?

**Do not invent a data/ or storage layer speculatively.** If a project consumes an existing external data system, the architecture records how it is reached and which module owns that boundary — it does not add a local data tier for symmetry. Ask before creating any directory whose purpose is storage, caching, or data access, and record where the storage actually lives (hostname or service, not just a folder name) so a later move does not silently break the project.

Create `PROGRESS.md` when work spans sessions or agents. It should record:

- current repository state;
- confirmed working surfaces;
- active work;
- blockers and unknowns;
- verification status;
- the next useful move.

Create `CHANGELOG.md` when the project has meaningful user-visible or release-significant changes. Do not fill it with every internal edit.

### 4. Scaffold the `docs/` knowledge store

For a Standard or Full foundation, create only the directories justified by the project:

```text
docs/
├── design-docs/       # durable designs and technical direction
├── decisions/         # MADR records for significant choices
├── exec-plans/
│   ├── active/        # work in progress
│   ├── completed/     # finished plans
│   └── tech-debt-tracker.md
├── generated/         # machine-generated maps, schemas, and reports
├── product-specs/     # user/product requirements when applicable
└── references/        # source notes and external technical references
```

Create `index.md` files where they make discovery easier. A directory with no current content does not always need an index.

For each generated document, record its generator or command and do not hand-edit generated regions. For each topic document, state when it applies. Keep historical notes out of the entry file unless they remain active constraints.

### 5. Create the feature contract when justified

When the project has multiple independently testable requirements, create:

```text
docs/feature-list.json
```

Use a machine-readable structure such as:

```json
{
  "features": [
    {
      "id": "feature-001",
      "category": "functional",
      "description": "A user can create a new project",
      "steps": [
        "Start the application",
        "Open the project form",
        "Submit valid project details",
        "Verify the project appears in the project list"
      ],
      "passes": false,
      "priority": 1,
      "dependencies": []
    }
  ]
}
```

Requirements:

- Every feature has a stable identifier and independently checkable steps.
- New features start as failing or unverified.
- Agents select one highest-priority incomplete feature at a time.
- Agents change only status/evidence fields when the project convention requires it; they do not delete or weaken requirements to make the project appear complete.
- A feature becomes passing only after its listed checks succeed.
- Implicit requirements from prompts, plans, or issue discussions are added to the feature contract or deliberately rejected.

For a tiny project, do not create a feature list just to imitate a larger harness.

### 6. Add a repeatable startup path

For a runnable application or service, create `init.sh` or the project-appropriate equivalent when it materially reduces startup and verification ambiguity.

It should make the real development/check path obvious and should not hide failures. Document:

- prerequisites;
- setup/install behavior;
- how to start the application;
- how to run the baseline checks;
- how to stop or clean up safely.

Do not create an initialization script that silently deletes data, resets the repository, or rewrites user configuration.

### 7. Add the optional MADR decision layer

For a project with meaningful architectural, data, security, deployment, dependency, interface, or user-visible tradeoffs, strongly recommend:

```text
docs/decisions/
├── README.md
└── 0001-title-with-dashes.md
```

Create `docs/decisions/README.md` with the project’s naming/status rules and the MADR template or a concise local variant.

Create an ADR when a decision will constrain future work. Include:

- context and problem;
- decision drivers;
- considered options;
- decision outcome;
- consequences, including rejected alternatives;
- confirmation evidence;
- status: proposed, accepted, deprecated, or superseded.

Add a short `AGENTS.md` trigger:

```text
For decisions that affect architecture, interfaces, data storage, security,
deployment, dependencies, or major user-visible behavior, create or update an
ADR in docs/decisions/. Read relevant existing ADRs before changing a decision
they constrain.
```

When a decision changes, preserve the old ADR and create a new one that supersedes it. Do not silently rewrite decision history.

### 8. Define proportional verification

Choose verification from the changed boundary:

| Change surface | Minimum evidence |
|---|---|
| Documentation only | Link, format, and repository checks |
| Pure utility or isolated logic | Focused unit tests |
| Module/service interaction | Integration tests |
| API/database/configuration boundary | Integration and runtime checks |
| UI or user workflow | Browser or real-client end-to-end verification |
| Deployment/environment change | Start the real service and exercise the affected path |

For cross-component features:

- define boundaries before writing E2E checks;
- test the real user/system path and important failure behavior;
- treat unit tests as necessary but insufficient evidence;
- make failures state what failed, why it matters, and how to fix it;
- promote recurring defects into tests, lints, or other executable checks;
- record the exact command and observed result.

E2E provides integrated evidence; it does not prove the absence of all defects. Skipped or unavailable verification is `unverified`, not passing.

### Agent-generated test guardrails

Before coding, state the behavior, failure modes, and test layer:
- E2E: critical user workflows.
- Integration: system boundaries.
- Unit: deterministic logic.

Agents reliably produce a large volume of low-value unit tests. Push back on that by default: a smaller number of tests that would actually fail if the feature regressed beats a broad shallow suite.

Write and run a test that fails before implementation. Reject tests that only inflate coverage, duplicate assertions, test internals or trivial constants, or mock away real behavior. Every test must name a plausible regression it catches. If you cannot name the regression, do not write the test.

One test that would fail loudly on a real regression is worth twenty that assert getters, private helpers, or library behavior the project does not own.

Use E2E for cross-boundary features, not as the sole testing layer. Retain the exact command and failure artifacts when available. Tests after code are acceptable for regressions, legacy characterization, or external contracts; state what they protect.

### 9. Establish the first state

Run the project’s real setup and verification commands when safe. Record exact results in `PROGRESS.md`.

If the user authorized an initial commit, commit the foundation with a descriptive message. Otherwise leave the foundation uncommitted and report that boundary. Never commit or push solely because the skill was invoked.

### 10. Report the foundation

Report:

```text
Foundation tier: <minimal | standard | full>
Applicability matrix: <every candidate with create, preserve, or not applicable plus evidence>
Created: <exact files and directories>
Skipped: <only conditional files marked not applicable, with concrete evidence or explicit user decision>
Canonical map: <AGENTS.md and deeper sources>
Feature contract: <path or not applicable>
Decision layer: <path or not applicable>
Verification: <exact commands and results>
Repository state: <branch and clean/dirty status>
Next useful move: <one concrete step>
```

## Completion criteria

A foundation is complete only when:

- the selected tier is justified from intended project scope, not merely current implementation state;
- the applicability matrix covers every candidate and every omission has a valid disposition;
- every selected-tier baseline artifact is created or explicitly preserved;
- every conditional artifact with an evidenced project surface is created;
- existing context and generators were checked before writing;
- `AGENTS.md` is a short router when present, and contains the mandatory rules verbatim (reply protocol, planning, testing, end-to-end verification, invariants and boundaries, session discipline, verification errors, completion, status footer, instruction hygiene);
- the reply-protocol placeholder was replaced with a real form of address, not left as `[your name]`;
- no data, storage, or cache layer was created without an explicit reason and without recording where the storage actually lives;
- architecture, progress, decisions, plans, and feature state have distinct homes;
- every created document has a purpose and is not an empty placeholder;
- startup and verification commands are known or marked unknown;
- initial feature status is explicit when a feature list exists;
- actual verification results are recorded;
- unrelated existing files and work are preserved;
- the repository state and any commit boundary are reported honestly.

## References

Read `references/source-index.md` for the OpenAI, Anthropic, Walking Labs, and MADR sources behind this workflow. Use the references selectively; do not load all source copies into normal task context.
