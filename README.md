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

## Install for OMP

```bash
git clone https://github.com/nathanpt/agent-skills.git
mkdir -p ~/.omp/agent/skills
cp -R agent-skills/skills/harness-bootstrap ~/.omp/agent/skills/
cp -R agent-skills/skills/simplify ~/.omp/agent/skills/
```

Invoke it explicitly:

```text
/skill:harness-bootstrap
/skill:simplify
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
```

## Reference policy

This repository contains original skill instructions and short source notes. It does not vendor third-party article text. Original sources are linked in each skill's `references/source-index.md`.

## License

MIT. See [LICENSE](LICENSE).
