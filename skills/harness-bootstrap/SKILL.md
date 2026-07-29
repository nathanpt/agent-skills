---
name: harness-bootstrap
description: Bootstrap or reconcile Harness Engineering context in an existing repository by validating existing instructions, generators, Git, and real test results before maintaining canonical AGENTS.md, ARCHITECTURE.md, and PROGRESS.md.
---

# Harness Engineering Bootstrap

## Purpose

Use this skill when an existing repository needs reliable agent context, but may already contain documentation, generated instruction files, onboarding tools, or stale claims.

This is a **single-pass reconciler**, not a context-file factory. Its job is to establish one coherent, evidence-backed harness without creating case-variant duplicates, fighting generators, copying stale claims, or re-documenting a map the repository already has.

The canonical target names for newly created root documents are:

```text
AGENTS.md
ARCHITECTURE.md
PROGRESS.md
```

Do not create lowercase `agents.md`, `architecture.md`, or `progress.md` beside existing uppercase versions.

## Reference library

Use bundled sources selectively. They are guidance, not a substitute for inspecting the target repository.

| Need | Public reference | Apply it by |
|---|---|---|
| A short, stable architecture map | `skill://harness-bootstrap/references/source-index.md` → Architecture documents | Writing a codemap, boundaries, invariants, and cross-cutting concerns without a brittle implementation dump. |
| Agent legibility and feedback loops | `skill://harness-bootstrap/references/source-index.md` → OpenAI harness engineering | Making context, verification surfaces, and source-of-truth documentation easy for agents to use. Do not copy its agent-only operating model wholesale. |
| Lightweight multi-session harness patterns | `skill://harness-bootstrap/references/source-index.md` → Learn Harness Engineering | Selecting a minimal set of instruction, progress, feature-state, handoff, and evaluator patterns appropriate to repository complexity. |

The public skill vendors no third-party article text. Use the original URLs in `source-index.md` when source detail is needed. The inspected codebase and observed command output remain the source of truth.

## Non-negotiable rules

1. **Code, Git, generators, and executed commands are the evidence.** Existing prose is a hypothesis until checked.
2. **Never create case-variant context duplicates.** On Linux, `AGENTS.md` and `agents.md` silently coexist; on macOS or Windows they may collide. Detect names case-insensitively before writing.
3. **Preserve and defer to strong existing references.** Do not create a second architecture map that restates a high-quality generated or maintained map.
4. **Treat existing pass/fail counts as stale until reproduced.** Never copy “N tests pass” or similar claims into `PROGRESS.md` without running the applicable command in this bootstrap.
5. **Respect generator ownership.** Do not hand-edit generated regions or fight the tool that owns them. Put durable material in a safe user-owned region or in a separate canonical document.
6. **Do not invent certainty or backlog.** Label unclear behavior, unverified claims, missing tests, and open work plainly. Open items require a source: code marker, failed command, Git diff, existing plan, generator conflict, or direct inspection.
7. **Do not leak secrets.** Never copy `.env` values, API keys, credentials, private URLs, user data, or token-like strings into context files.
8. **Do not change application behavior.** This skill reconciles documentation and harness context only unless the user explicitly expands scope.
9. **Keep the harness readable.** A short routing document plus deep references is better than a giant instruction dump.

## Step 0 — Context and ownership triage

Perform this step before scanning code or spawning subagents.

### 0.1 Detect context files case-insensitively

Inspect the root for all case variants of:

```text
AGENTS.md
ARCHITECTURE.md
PROGRESS.md
README.md
ROADMAP.md
CHANGELOG.md
CONTRIBUTING.md
```

Also inspect project-local context directories such as `.omp/`, `.claude/`, `.codex/`, and tool-specific configuration.

### 0.2 Select one canonical file per role

Apply this decision order:

1. If a recognized agent tool already reads an existing instruction file, keep that exact file and casing as canonical. Prefer `AGENTS.md` for a new generic agent-instructions file.
2. If a valid root context file already exists, update that exact file rather than creating another case variant.
3. If no file exists for a role, create the uppercase canonical target: `AGENTS.md`, `ARCHITECTURE.md`, or `PROGRESS.md`.
4. If multiple case variants already coexist, do **not** create another. Choose the tool-recognized or established file as canonical, merge only verified durable facts into it, and record the unresolved duplicate-file cleanup in `PROGRESS.md`. Do not delete a competing file automatically.

### 0.3 Classify existing documents before editing

For every relevant context file, classify it as one or more of:

```text
human-maintained source of truth
machine-generated reference
machine-generated region inside a mixed file
stale or unverified historical note
thin or incomplete stub
```

A strong existing map is not a vacuum to fill. If it already answers “where to start,” “important paths,” and “how the system works,” a new `ARCHITECTURE.md` should be a lean map that links or defers to it rather than rephrasing the same content.

### 0.4 Detect generator ownership and safe edit zones

Search context files and repository tooling for generator signals, including:

```text
<!-- <tool>:START --> ... <!-- <tool>:END -->
GENERATED / DO NOT EDIT markers
`pi-onboard` or other onboarding scripts
context-file generators
pre-commit or CI regeneration steps
```

When a generator owns a region:

- do not write durable manual facts inside its markers;
- do not “correct” volatile values there if the next generation will overwrite them;
- place durable instructions outside the owned region, if a documented safe zone exists;
- otherwise route live status, test counts, and work state to `PROGRESS.md` and make the generated document point there when appropriate;
- record the generator, ownership boundary, and safe-edit rule in the architecture or agents context.

## Step 1 — Establish repository reality

### 1.1 Read the existing context first

Read the canonical context files selected in Step 0, relevant README/roadmap/changelog material, manifests, and generator instructions.

Before adding a new document, answer:

```text
What useful question is not already answered by the strongest existing source?
Where should that answer live so it stays true?
```

### 1.2 Inspect Git state

When Git is available, capture:

```bash
git status --short
git branch --show-current
git log --oneline -12
git diff --stat
```

Use this evidence to identify active work. Uncommitted changes are not completed work.

If Git is unavailable, state that in `PROGRESS.md` rather than pretending there is commit evidence.

### 1.3 Scan the codebase deliberately

Inspect, at minimum:

- root layout and dependency manifests;
- application entry points and configuration;
- major source directories;
- tests, test configuration, and runnable scripts;
- data models, APIs, background workers, or external-service boundaries when present;
- TODO, FIXME, HACK, placeholder, and `NotImplemented` markers;
- CI, deployment, container, and environment-template files when present.

Read representative entry points and neighboring modules. Do not read every file mechanically.

### 1.4 Run real verification before recording verification state

Discover actual commands from manifests, CI, task runners, and project instructions. At minimum, run the primary test command when it is practical in the current environment.

Also run relevant lint, typecheck, build, or focused verification commands when the repository defines them and the bootstrap can safely do so.

Rules:

- Existing pass/fail counts are **not** evidence.
- Capture the exact command and observed result.
- A failed test is a real open item, not a documentation inconvenience.
- If a command cannot run, record why and mark the surface **not verified**, not passing.
- Do not let a generated or static instruction file hardcode live test counts. Point live status to `PROGRESS.md` instead.

## Step 2 — Decide whether subagents improve discovery

OMP subagents are useful for unresolved, independent evidence gathering. They are not automatically useful merely because the repository is non-trivial.

### Do not fan out when

- a strong, current context file already provides the system map;
- the repository is small enough for one focused inspection;
- the remaining work is synthesis, verification, or resolving a single contradiction;
- scouts would mostly rediscover a map already present in a trustworthy reference.

### Fan out only for uncovered independent lanes

When material uncertainty remains after Step 0 and Step 1.1, use OMP's `task` tool to dispatch read-only `explore` subagents with self-contained assignments. Possible lanes:

1. **Uncovered system map** — stack, entry points, directory responsibilities, component/data flow, external boundaries.
2. **Verification map** — tests, CI, build/lint/typecheck scripts, deployment surfaces, and missing verification.
3. **Current-state map** — active Git work, TODOs, incomplete features, stale claims, and technical debt.
4. **Generator and documentation ownership map** — context generators, marker boundaries, regeneration triggers, and safe edit zones.

Require path-backed findings and evidence, not rewritten documentation.

### Parent-agent responsibilities

The parent agent owns synthesis and all writes:

- treat child findings as leads, not authority;
- resolve contradictions against source, Git output, generator behavior, or executed commands;
- avoid duplicating strong existing documentation;
- write or update canonical context files **serially**;
- run the final self-check.

Children must not concurrently write root context files. Shared documentation outputs require one accountable synthesizer.

## Step 3 — Create or reconcile the architecture source

Use the canonical architecture source selected in Step 0. It may be `ARCHITECTURE.md`, an established `AGENTS.md`, or a generator-owned reference that already provides a trustworthy system map.

Create a separate `ARCHITECTURE.md` only when it adds distinct, durable value: there is no strong existing architecture source, or a short stable routing layer would reduce ambiguity without duplicating the established reference.

If a high-quality existing document already answers the architecture questions and a separate file would merely restate it, **do not create `ARCHITECTURE.md` just to satisfy a three-file pattern**. Record the actual canonical architecture source in `PROGRESS.md` and make future agent instructions point to it.

When a separate `ARCHITECTURE.md` is warranted, it must answer: **What is this system, where does work start, and how do the major parts relate?**

Use only the sections justified by the repository:

```markdown
# Architecture

## System purpose

## Stack and runtime

## Entry points and execution flow

## Directory map

## Core components and data flow

## External boundaries

## Testing and verification surfaces

## Important constraints, generators, and unknowns
```

Requirements:

- Name concrete files, modules, and directories.
- Describe relationships and flow, not a file dump.
- Prefer stable facts: codemap, invariants, boundaries, cross-cutting concerns.
- If an existing generator or reference already owns detailed paths, write a concise routing layer and defer to that source rather than duplicating it.
- Include actual commands only when observed in project tooling; defer live pass/fail state to `PROGRESS.md`.
- State configuration and secret-entry patterns without exposing values.

## Step 4 — Create or reconcile `PROGRESS.md`

Use the canonical `PROGRESS.md` file selected in Step 0. Create it only if no canonical progress/status source exists.

It must answer: **What is true now, what is active, and what still needs evidence or work?**

Use this structure where applicable:

```markdown
# Project Progress

**Last assessed:** YYYY-MM-DD
**Repository state:** branch / clean or dirty working tree

## Confirmed working surfaces

## Active work

## Open tasks and technical debt

## Verification status

## Decisions, generators, and constraints

## Next useful checks
```

Requirements:

- Use checkboxes only for evidence-backed completion or concrete open items.
- Identify each open item’s source: failed command, missing verification, Git diff, code marker, existing plan, generator conflict, or direct inspection.
- Record exact commands actually run and their observed results.
- Separate **passing**, **failing**, and **not verified**.
- Capture the current branch and notable uncommitted changes without dumping diffs.
- Keep live test counts and current status here, not in a generator-owned instruction region.

## Step 5 — Create or reconcile `AGENTS.md`

Use the canonical `AGENTS.md` file selected in Step 0. Create it only if no recognized agent-instructions file exists.

`AGENTS.md` is a routing contract for future agents, not an encyclopedia. If a strong generated context already exists, add only durable human-owned instructions in a safe region and link deeper references.

It must make these requirements explicit:

1. Read the canonical architecture source (which may be `ARCHITECTURE.md`, `AGENTS.md`, or a documented generated reference) and canonical progress context before meaningful changes.
2. Read repository-specific instructions, relevant source, and generator ownership boundaries before editing.
3. State intended scope, affected files, and verification plan before non-trivial implementation.
4. Preserve established patterns unless there is a documented reason to change them.
5. Run the full applicable verification pipeline. A build or render alone is not behavioral proof.
6. Report commands actually run, results, changed files, and known gaps honestly.
7. Update the architecture context when stable structure, entry points, data flow, core boundaries, or generator ownership changes.
8. Update the progress context when work state, verification state, technical debt, or active priorities materially change.
9. Do not commit secrets, generated clutter, unrelated formatting churn, or edits inside generator-owned regions.
10. Treat “it compiles” as a baseline, not proof of completion.

Tailor the rest to the actual language, framework, tests, deployment model, and generator behavior found in the repository.

## Step 6 — Self-check the harness

Before finishing:

1. Re-read every canonical file touched.
2. Confirm no case-variant context file was newly created beside an established file.
3. Confirm referenced files, commands, and paths exist.
4. Confirm generated regions were not treated as durable manual-edit surfaces.
5. Confirm stale verification claims were either reproduced, corrected outside generator-owned regions, or marked unverified.
6. Confirm `AGENTS.md` points agents to canonical architecture and progress sources.
7. Confirm no secret-like values or private data entered the documents.
8. Report exactly what was created, updated, deferred, or left unresolved.

## Output format to the user

Provide a short completion report:

```text
Canonical files used: <exact filenames and casing>
Created/updated: <exact files>
Existing references deferred to: <files or generators>
Repository state assessed: <branch/status or unavailable>
Verification run: <exact commands and results, or not run>
Important open items: <brief list>
```

Do not ask for step-by-step confirmation during this bootstrap. Stop after the harness reconciliation is complete unless the user explicitly asks for implementation work.
