# Agent Skills

Portable, evidence-driven skills for AI coding agents.

## Included skills

### `simplify`

Reviews recent code changes for reuse, quality, and efficiency, then applies only evidence-backed cleanup. It distinguishes static review from runtime verification and scales parallel reviewer fan-out to the size and risk of the diff.

### `debug`

Investigates ambiguous bugs with bounded hypotheses, runtime evidence, targeted diagnostic instrumentation, durable reproduction, and explicit stopping rules before application fixes.

### `handoff`

Transfers active work to a fresh agent with verified context, preserved decisions, explicit side-effect gates, and a safe first action.

### `grill-me`

Pressure-tests plans, designs, and decisions through a focused, user-owned interview with dependency-aware questions and explicit stopping rules.

### `adr-red-team`

Runs one high-rigor, read-only ADR and architecture review through a named reviewer agent and a separately pinned model role.

### `project-foundation`

Brings a repository to a coherent operating foundation in whichever mode fits: **creation** for a new or early-stage project, **retrofit** for an existing repository that has history, generators, and possibly stale agent context.

Both modes produce the same artifact — a two-part `AGENTS.md` whose Part 1 describes the project and whose Part 2 is a standard rule block shared across every project — plus progressive-disclosure documentation, optional machine-readable feature state, execution plans, and MADR decision records.

Retrofit mode is designed to prevent the failure modes that turn a bootstrap into a regression: case-variant duplicates such as `AGENTS.md` and `agents.md`, architecture documents that restate a stronger existing reference, stale pass or fail counts copied from old instructions, edits inside generator-owned sections, and wasteful subagent fan-out that re-derives known context.

## Install for OMP

```bash
git clone https://github.com/nathanpt/agent-skills.git
mkdir -p ~/.omp/agent/skills
cp -R agent-skills/skills/simplify ~/.omp/agent/skills/
cp -R agent-skills/skills/project-foundation ~/.omp/agent/skills/
cp -R agent-skills/skills/debug ~/.omp/agent/skills/
cp -R agent-skills/skills/handoff ~/.omp/agent/skills/
cp -R agent-skills/skills/grill-me ~/.omp/agent/skills/
cp -R agent-skills/skills/adr-red-team ~/.omp/agent/skills/
```

Invoke it explicitly:

```text
/skill:simplify
/skill:project-foundation
/skill:debug
/skill:handoff
/skill:grill-me
/skill:adr-red-team
```

## Repository layout

```text
skills/
  simplify/
    SKILL.md
    references/
      source-index.md
  project-foundation/
    SKILL.md
    BRAINSTORM.md
    references/
      source-index.md
      openai-harness-engineering.md
      anthropic-long-running-agents.md
      walkinglabs-split-instructions.md
      walkinglabs-feature-lists.md
      walkinglabs-e2e-verification.md
      madr.md
  debug/
    SKILL.md
    BRAINSTORM.md
    evaluations.md
    references/
      source-index.md
      instrumentation.md
      investigation-record.md
      evidence-and-stopping.md
      cursor-debug-mode.md
      doraemonkeys-debug-mode.md
      ronnie-debug-skill.md
  handoff/
    SKILL.md
    BRAINSTORM.md
    references/
      source-index.md
      usage.md
      mattpocock-handoff-explained.md
      mattpocock-skills-repository.md
      softaworks-session-handoff.md
  grill-me/
    SKILL.md
    BRAINSTORM.md
    evaluations.md
    references/
      source-index.md
  adr-red-team/
    SKILL.md
    BRAINSTORM.md
    evaluations.md
    references/
      review-lenses.md
      source-index.md
    templates/
      adr-red-team-agent.md
      model-role-reviewer.yml
```

## Reference policy

This repository contains original skill instructions and short source notes. It does not vendor third-party article text. Original sources are linked in each skill's `references/source-index.md`.

## License

MIT. See [LICENSE](LICENSE).
