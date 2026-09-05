# Grill-Me Skill Brainstorm

## Purpose

Create a portable interview mode that turns a loose plan, design, or decision into explicit, user-owned commitments without wasting turns on low-value questions or pretending that conversation can answer everything.

## Research findings

The best-known implementation separates a thin user-facing wrapper from a reusable grilling primitive. Its useful ideas are a decision tree, a dependency-aware frontier, recommendations alongside questions, and a confirmation gate before action. The wrapper-only version is compact but has a portability failure: if the primitive is not installed or not loaded, the skill does nothing useful.

Other implementations add depth-first questioning, codebase inspection, decision logging, or a repository quiz. Those behaviors are useful in the right skill but should not be silently mixed into this cross-domain skill:

- Codebase-grounded quizzing is a knowledge-test skill, not plan grilling.
- Persistent logs make a session durable but add filesystem side effects and reduce portability.
- A fixed “ask three more questions” rule creates ceremonial turns and does not measure unresolved risk.
- Asking every question at once produces a checklist dump; asking one question forever can make a broad session unnecessarily slow.

## Design decisions

- **Name:** `grill-me`.
- **Invocation:** explicit/user-invoked; do not auto-trigger for any complex task.
- **Scope:** plans, designs, ideas, and decisions across technical and non-technical domains.
- **State:** stateless by default; no files unless explicitly requested.
- **Question cadence:** one focused question by default; at most three independent questions in a speed-oriented batch.
- **Ordering:** dependency-aware frontier, highest-impact branch first, depth before breadth.
- **Recommendations:** every question gets a concrete recommendation or strawman.
- **Fact/decision split:** retrieve facts from the environment; leave choices to the user.
- **Uncertainty:** distinguish decide, defer, research, and prototype instead of forcing an answer.
- **Stopping:** risk-based convergence, explicit user stop, scope split, or prototype/test boundary; no arbitrary question count.
- **Side effects:** reaching agreement does not authorize implementation or external action.

## Performance model

Performance means useful decisions per user turn, not maximum interrogation length. The control loop therefore:

1. inspects only relevant context;
2. asks a question only if its answer can change the direction;
3. avoids dependent questions in the same batch;
4. follows the current branch until its implications are settled;
5. uses recommendations to reduce blank-page effort;
6. stops when the next action is possible rather than when the conversation is long.

The skill deliberately does not maintain a formal graph or question counter. The model must recompute the frontier from the conversation, while the evaluations test observable behavior.

## Rejected alternatives

- **One-line delegation to `grilling`:** elegant, but not standalone. It silently depends on another skill and is fragile across compatible clients.
- **Full decision-tree questionnaire:** high context cost and many invalid downstream questions.
- **Always one question at a time:** safe, but needlessly slow when decisions are independent and the user asks for speed.
- **Always batch the frontier:** efficient in ideal cases, but too much cognitive load for chat and encourages shallow answers.
- **Automatic `.grill/` or `.claude/` log:** useful for some workflows, but violates the portable stateless default and creates an unexpected write.
- **“Relentless” as a stopping rule:** intensity is not coverage. Use explicit convergence and deferral checks.

## Open questions

- Whether a future repository-specific variant should add durable decision records.
- Whether an agent client can expose a structured question UI without making this skill tool-specific.
- Whether empirical evaluations should compare one-at-a-time and independent-batch modes on real sessions.
