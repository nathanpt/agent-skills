# Retrofit mode — reconciling an existing repository

Use this when the repository already has history, code, and probably some agent-facing
documents, and the goal is to make its `AGENTS.md` compliant with the standard rather
than to scaffold from nothing.

This procedure is the **retrofit half** of project-foundation. Creation mode is in
`SKILL.md`. The two modes produce the same artifact: a two-part `AGENTS.md` per
`references/agents-md-general-rules.md`.

**Status: unexercised.** This material was consolidated from a separate skill that was
never invoked in service. It reads as sound, but it has not yet survived contact with a
real repository. Treat its rules as hypotheses to be validated, and report what breaks.

## The one rule that matters most

**Existing prose is a hypothesis until checked against code, Git, generators, or an
executed command.** A repository's documents are the claim; the repository is the
evidence. Every stale instruction you copy forward costs a future agent a wrong turn.

## Step 1 — Context and ownership triage

Do this before reading code.

### 1.1 Detect context files case-insensitively

Check the root for all case variants of:

```text
AGENTS.md  ARCHITECTURE.md  PROGRESS.md  README.md
ROADMAP.md  CHANGELOG.md  CONTRIBUTING.md
```

Also inspect tool-specific directories that may carry context: `.omp/`, `.claude/`,
`.codex/`, `.cursor/`, and any project-local configuration.

`AGENTS.md` and `agents.md` coexist silently on Linux and collide on macOS and Windows.
Detect before writing; never create a case variant beside an established file.

### 1.2 Select one canonical file per role

1. If a recognised agent tool already reads an existing file, keep that exact filename and
   casing as canonical.
2. If a valid root file already exists for a role, update that file rather than adding
   another.
3. If nothing exists for a role, create the uppercase canonical name.
4. If case variants already coexist, do not add a third. Pick the tool-recognised file as
   canonical, merge only verified durable facts into it, and record the duplicate cleanup
   as an open item. Never delete a competing file automatically.

### 1.3 Classify every document before editing

Each relevant file is one or more of:

```text
human-maintained source of truth
machine-generated reference
machine-generated region inside a mixed file
stale or unverified historical note
thin or incomplete stub
```

The classification decides what you may edit. It also stops the common error of writing a
second map that restates a better one: if an existing document already answers *where does
work start* and *how do the parts relate*, link it instead of paraphrasing it.

### 1.4 Detect generator ownership and safe edit zones

Search for generator signals:

```text
<!-- <tool>:START --> ... <!-- <tool>:END -->
GENERATED / DO NOT EDIT markers
onboarding or context-file generators
pre-commit or CI regeneration steps
```

When a generator owns a region:

- do not write durable facts inside its markers;
- do not "correct" volatile values there, because the next run overwrites them;
- put durable instructions outside the owned region if a documented safe zone exists;
- otherwise route live status, test counts, and work state to the progress document;
- record the generator, its boundary, and the safe-edit rule in the agent context.

## Step 2 — Establish repository reality

### 2.1 Read the existing context first

Read the canonical files from step 1, plus relevant README, roadmap, changelog, manifests,
and generator instructions. Before adding any document, answer:

```text
What useful question is not already answered by the strongest existing source?
Where should that answer live so it stays true?
```

If there is no answer, do not create the document.

### 2.2 Inspect Git state

```bash
git status --short
git branch --show-current
git log --oneline -12
git diff --stat
```

Uncommitted changes are not completed work. If Git is unavailable, say so rather than
implying commit evidence exists.

### 2.3 Scan deliberately

At minimum: root layout and manifests; entry points and configuration; major source
directories; tests and runnable scripts; data models, APIs, workers, external boundaries;
`TODO` / `FIXME` / `HACK` / `NotImplemented` markers; CI, deployment, container, and
environment templates. Read representative entry points and their neighbours. Do not read
every file mechanically.

### 2.4 Run real verification before recording verification state

Discover commands from manifests, CI, and project instructions, then actually run the
primary test command where practical, plus lint, typecheck, or build when the repository
defines them and they are safe to run.

- Existing pass/fail counts are not evidence.
- Capture the exact command and the observed result.
- A failing test is a real open item, not a documentation inconvenience.
- If a command cannot run, record why and mark the surface **not verified**, never passing.
- Do not hardcode live test counts into a generated or static instruction file; point to
  the progress document instead.

## Step 3 — Decide whether subagents help

Fan out only for genuinely independent, uncovered lanes — not because the repo is large.

**Do not fan out when** an existing context file already provides the map, the repository is
small enough for one inspection, or the remaining work is synthesis or resolving a single
contradiction.

**Fan out when** material uncertainty remains after steps 1 and 2. Useful read-only lanes:

1. system map — stack, entry points, directory responsibilities, data flow, boundaries;
2. verification map — tests, CI, build/lint/typecheck, deployment surfaces, gaps;
3. current-state map — active work, TODOs, incomplete features, stale claims, debt;
4. generator and documentation ownership map — markers, regeneration triggers, safe zones.

Require path-backed findings, not rewritten documentation. The parent owns synthesis and
**all** writes; children never write root context files concurrently. Treat child findings
as leads and resolve contradictions against source.

## Step 4 — Architecture source

Use the canonical architecture source chosen in step 1.2. It may be `ARCHITECTURE.md`, an
established `AGENTS.md`, or a generator-owned reference that already provides a trustworthy
map.

Create a separate `ARCHITECTURE.md` **only** when it adds distinct durable value: no strong
source exists, or a short routing layer removes ambiguity without duplicating the existing
reference. If a good document already answers the architecture questions, do not create a
second file to satisfy a three-file pattern — record the real canonical source in the
progress document and point the agent context at it.

When warranted, use only the sections the repository justifies: system purpose, stack and
runtime, entry points and execution flow, directory map, core components and data flow,
external boundaries, testing and verification surfaces, constraints and unknowns. Name
concrete files and describe relationships, not a file dump. Defer live pass/fail state to
the progress document. State configuration and secret-entry patterns without exposing
values.

## Step 5 — Progress and feature state

Reconcile the progress document (or the project's `.docs/PROGRESS.md` equivalent) so it
answers *what is true now, what is active, and what still needs evidence*. Useful shape:

```markdown
# Project Progress

**Last assessed:** YYYY-MM-DD
**Repository state:** branch / clean or dirty

## Confirmed working surfaces
## Active work
## Open tasks and technical debt
## Verification status
## Decisions, generators, and constraints
## Next useful checks
```

Requirements: use checkboxes only for evidence-backed completion or concrete open items;
source every open item (failed command, missing verification, Git diff, code marker, plan,
generator conflict, inspection); record exact commands and observed results; separate
**passing**, **failing**, and **not verified**; capture branch and notable uncommitted
changes without dumping diffs; keep live test counts here rather than in a generated
region.

Plans do not get a root `PLAN.md`. Active plans live in `docs/exec-plans/active/`,
completed ones in `docs/exec-plans/completed/` — see `SKILL.md`.

## Step 6 — Reconcile `AGENTS.md` into two parts

This is the step that replaces the pre-existing 10-point checklist this material used to
carry. The file must end up in the standard shape from
`references/agents-md-general-rules.md`.

1. **Line 1 is the reply-protocol canary**, above every heading.
2. **Part 1 — Project** holds what this repository is: overview, real commands, this repo's
   own hard constraints, routing to deeper documents. Preserve verified existing content —
   do not rewrite a working project section for style.
3. **Part 2 — Standard rules** is copied byte-identically from the canonical block. Never
   paraphrase, reorder, or trim it.
4. Content that does not survive verification is dropped or marked unverified; it is not
   silently carried forward.
5. Live status, test counts, and work state belong in the progress document, not in
   `AGENTS.md`.
6. Where the repository already had instructions that duplicate Part 2, the Part 1 copy is
   removed and Part 2 is the single source.
7. If `AGENTS.md` is deliberately gitignored (a public repository that carries no
   agent-facing files), say so in the file itself and record where the local-only
   convention is documented. An untracked file has no history to recover it from.
8. Push durable material into reference documents; `AGENTS.md` stays a router.

## Step 7 — Self-check before reporting

1. Re-read every canonical file touched.
2. Confirm no case-variant was newly created beside an established file.
3. Confirm referenced files, commands, and paths exist.
4. Confirm generated regions were not treated as hand-editable.
5. Confirm stale verification claims were reproduced, corrected, or marked unverified.
6. Confirm `AGENTS.md` is two-part and Part 2 is byte-identical to the canonical block.
7. Confirm no secret-like values or private data entered the documents.
8. Report what was created, updated, deferred, and left unresolved.

## Output format

```text
Mode: retrofit
Canonical files used: <exact filenames and casing>
Created/updated: <exact files>
Existing references deferred to: <files or generators>
Repository state assessed: <branch/status or unavailable>
Verification run: <exact commands and results, or not run>
AGENTS.md: <two-part? Part 2 byte-identical? canary on line 1?>
Open items: <brief list>
```

Do not ask for step-by-step confirmation during the reconcile. Stop when the harness is
consistent unless the user explicitly asks for implementation work.
