# Project Foundation Source Index

This directory contains source material and original synthesis for the draft skill. Third-party source text is preserved for local reference; the final skill should link to sources and summarize adopted principles rather than copy large passages into agent instructions.

## OpenAI harness engineering

- **Original:** https://openai.com/index/harness-engineering/
- **Retrieved:** 2026-08-29
- **Local copy:** `openai-harness-engineering.md`
- **Relevant sections:** “We made repository knowledge the system of record,” “Agent legibility is the goal,” “Enforcing architecture and taste,” and “Entropy and garbage collection.”
- **Candidate principles:** keep `AGENTS.md` as a short table of contents; use a structured `docs/` knowledge store; apply progressive disclosure; version execution plans; separate generated references from human-maintained guidance; enforce durable architecture and quality invariants mechanically where justified; continuously clean up documentation and code drift.

## Anthropic long-running agents

- **Original:** https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Retrieved:** 2026-08-29
- **Local copy:** `anthropic-long-running-agents.md`
- **Relevant sections:** “The long-running agent problem,” “Environment management,” “Feature list,” “Incremental progress,” “Testing,” and “Getting up to speed.”
- **Candidate principles:** use a distinct initializer phase; create a clean starting environment; maintain a structured feature list with explicit pass/fail state; make one incremental feature change per session; leave a clean git state and progress update; provide a repeatable startup/test command; require end-to-end verification before marking a feature passing.

## Walking Labs — split instructions

- **Original:** https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/
- **Repository source:** https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/lectures/lecture-04-why-one-giant-instruction-file-fails/index.md
- **Retrieved:** 2026-08-29
- **Local copy:** `walkinglabs-split-instructions.md`
- **Relevant sections:** “Core Concepts,” “How to Split,” “Real-World Example,” and “Key Takeaways.”
- **Candidate principles:** keep `AGENTS.md` as a 50–200 line entry file; put project overview, quick-start commands, a small set of hard constraints, and topic-document links there; make each topic document state when it applies; give instructions a source and expiry condition; move historical lessons into tests or delete them; use progressive disclosure and inspect the repository before creating documentation.

## Walking Labs — feature lists

- **Original:** https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/
- **Repository source:** https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/index.md
- **Retrieved:** 2026-08-29
- **Local copy:** `walkinglabs-feature-lists.md`
- **Relevant sections:** “Why Feature Lists Are Different,” “The Feature List as a Harness Primitive,” “How to Write a Good Feature List,” and “Feature Lists and Incremental Development.”
- **Candidate principles:** externalize project scope into a machine-readable feature list; make each feature independently testable with clear steps and explicit pass/fail state; treat the list as the shared contract for scheduling, verification, and handoffs; prevent agents from declaring the whole project complete after implementing only visible scaffolding; update status from evidence rather than prose.

## Walking Labs — end-to-end verification

- **Original:** https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/
- **Repository source:** https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/lectures/lecture-10-why-end-to-end-testing-changes-results/index.md
- **Retrieved:** 2026-08-29
- **Local copy:** `walkinglabs-e2e-verification.md`
- **Relevant sections:** “The Blind Spots of Unit Tests,” “End-to-End Testing Not Only Changes Results,” “The Harness Must Include an End-to-End Layer,” “Turn Architectural Rules into Executable Checks,” and “Review Feedback Promotion.”
- **Candidate principles:** match verification depth to the changed boundary; require integration or end-to-end evidence for cross-component changes; test the real user/system path where possible; turn recurring review findings into executable checks; make failure output state what failed, why, and how to fix it.
- **Interpretation:** E2E is not a blanket gate for every edit and does not prove the absence of all defects. Unit, integration, and E2E checks are complementary layers.

## MADR — Markdown Architectural Decision Records

- **Original:** https://adr.github.io/madr/
- **Retrieved:** 2026-08-29
- **Local copy:** `madr.md`
- **Relevant sections:** “Overview,” “Applying MADR to your project,” “Using MADR in large projects and product developments,” and “Full template.”
- **Candidate principles:** record significant decisions with context, drivers, options, outcome, consequences, and confirmation; keep records versioned beside the code; use `docs/decisions/`; supersede old decisions rather than silently rewriting history; use categories only when the project needs them.
- **Adoption tier:** optional but strongly recommended for projects with meaningful architectural, data, security, deployment, dependency, or user-visible tradeoffs.

## Minimal-change engineering

- **Original engineering framing:** https://x.com/techNmak/status/2096243571410276392
- **Critical response:** https://x.com/nateberkopec/status/2096480942399594633
- **Supporting implementation and benchmark:** https://github.com/DietrichGebert/ponytail and https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md
- **Retrieved:** 2026-09-06
- **Adopted principle:** before adding code or scaffolding, inspect the repository and prefer deletion, reuse, configuration, native facilities, standard-library functions, or existing dependencies; then implement the smallest complete change.
- **Safety boundary:** minimality must not remove validation, error handling, security, accessibility, tests, observability, or readability. The cited benchmark is directional rather than universal: it uses one model, one repository, and a small run count; its short YAGNI prompt was less consistent and dropped a security guard in one tested run.
- **Adoption point:** generated `AGENTS.md` under the repository map / global hard-constraints section.

## Future sources

Add OpenAI, Anthropic, and other source links here as they are provided. Record what principle each source contributes and where it is adopted in the skill.
