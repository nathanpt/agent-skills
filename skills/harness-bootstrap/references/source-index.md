# Harness Engineering Source Index

This public skill does not redistribute third-party articles. These sources informed the skill; visit the original URLs for full context, current wording, and any applicable terms of use.

## Architecture documents as a codebase map

- **Original:** https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- **Retrieved:** 2026-07-29
- **Use for:** deciding what belongs in a durable architecture map.
- **Application:** keep an architecture document short and stable. Make it a codemap of major modules, relationships, invariants, boundaries, and cross-cutting concerns rather than a brittle implementation dump.

## OpenAI harness engineering

- **Original:** https://openai.com/index/harness-engineering/
- **Retrieved:** 2026-07-29
- **Use for:** agent legibility, repository knowledge as a system of record, feedback loops, and verification design.
- **Application:** make the context and validation surfaces agents need discoverable. Keep top-level instructions short and route them to deeper, maintained sources of truth. Do not copy an agent-only operating model blindly.

## Learn Harness Engineering resource library

- **Original:** https://walkinglabs.github.io/learn-harness-engineering/en/resources/
- **Retrieved:** 2026-07-29
- **Use for:** lightweight progress, feature-state, handoff, clean-exit, and evaluator patterns.
- **Application:** begin with the smallest maintained context system that solves the current coordination problem; add governance only when repository complexity actually requires it.

## Use rule

Use these sources to form a repository-specific rule, not to paste generic advice or article prose into generated context files. The target repository, its generators, and commands actually executed remain the source of truth for any bootstrap run.
