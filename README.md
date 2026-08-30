# Agent Skills

Portable, evidence-driven skills for AI coding agents.

## Included skills

### `harness-bootstrap`

Bootstraps or reconciles Harness Engineering context in an existing repository. It validates existing instructions, generators, Git state, and real test results before maintaining canonical agent context.

It is designed to prevent common failure modes:

- case-variant duplicates such as `AGENTS.md` and `agents.md`;
- redundant architecture documents that restate a stronger existing reference;
- stale pass or fail counts copied from old instructions;
- edits inside generator-owned context sections;
- wasteful subagent fan-out that re-derives known context.

### `simplify`

Reviews recent code changes for reuse, quality, and efficiency, then applies only evidence-backed cleanup. It distinguishes static review from runtime verification and scales parallel reviewer fan-out to the size and risk of the diff.

### `debug`

Investigates ambiguous bugs with bounded hypotheses, runtime evidence, targeted diagnostic instrumentation, durable reproduction, and explicit stopping rules before application fixes.

### `project-foundation`

Scaffolds a new or early-stage project with a concise `AGENTS.md`, progressive-disclosure documentation, optional machine-readable feature state, execution plans, and MADR decision records.

## Install for OMP

```bash
git clone https://github.com/nathanpt/agent-skills.git
mkdir -p ~/.omp/agent/skills
cp -R agent-skills/skills/harness-bootstrap ~/.omp/agent/skills/
cp -R agent-skills/skills/simplify ~/.omp/agent/skills/
cp -R agent-skills/skills/project-foundation ~/.omp/agent/skills/
cp -R agent-skills/skills/debug ~/.omp/agent/skills/
```

Invoke it explicitly:

```text
/skill:harness-bootstrap
/skill:simplify
/skill:project-foundation
/skill:debug
```

## Repository layout

```text
skills/
  harness-bootstrap/
    SKILL.md
    references/
      source-index.md
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
```

## Reference policy

This repository contains original skill instructions and short source notes. It does not vendor third-party article text. Original sources are linked in each skill's `references/source-index.md`.

## License

MIT. See [LICENSE](LICENSE).
