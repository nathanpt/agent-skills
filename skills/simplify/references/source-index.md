# Simplify Skill Source Index

This skill is an original workflow synthesis. It does not vendor third-party prompt text.

## Hermes simplify proposal

- **Original:** https://github.com/NousResearch/hermes-agent/issues/379
- **Use for:** three focused parallel review lanes, evidence-based reconciliation, and fixing rather than merely reporting.
- **Applied here:** reviewer fan-out is proportional to diff size; findings are hypotheses; accepted fixes remain bounded to the change surface.

## OMP skills

- **Original:** https://omp.sh/docs/skills
- **Use for:** skill discovery, explicit invocation, frontmatter, and supporting-file conventions.
- **Applied here:** the skill is self-contained and uses the standard `skills/simplify/SKILL.md` layout.

## Pi CLI reference

- **Original:** https://pi.dev/docs/latest/usage
- **Use for:** the runtime-verification distinction that matters for CLI adapters and effective argv behavior.
- **Applied here:** static reviewers cannot prove which executable, flag, provider, or configuration value wins at runtime; exercise the real boundary when the change affects one.

## Observed validation lesson

The Herdr Lantern Pi-support change demonstrated that a green test suite can still miss:

- a precedence bug where an extra CLI flag overrides the displayed model/provider;
- a misleading comment copied from a plan;
- a narrow test that checks only an enumerated denylist rather than the invariant;
- runtime behavior that requires a real CLI invocation.

The skill uses these as general review principles without hardcoding Lantern-specific paths or names.
