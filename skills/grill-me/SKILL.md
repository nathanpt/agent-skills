---
name: grill-me
description: Pressure-test plans or decisions before commitment.
version: 0.1.0
author: Nathan (nathanpt)
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [planning, decisions, requirements, critical-thinking, alignment]
  related_skills: []
---

# Grill Me

Use this as a user-invoked interview mode for a plan, design, idea, or decision that is not yet precise enough to commit to. The goal is shared understanding and explicit decisions, not a longer conversation for its own sake.

## When to use

Activate when the user explicitly asks to:

- use `/skill:grill-me` or “grill me”;
- pressure-test a plan, design, proposal, or decision;
- poke holes in an idea or ask what they are missing;
- interview them before they commit to a consequential direction.

Do not activate merely because a task is complex. Do not implement, draft, redesign, or create a plan unless the user asks after the interview.

## Core contract

1. The user owns the decisions. Surface gaps and trade-offs; do not quietly choose for them.
2. Be rigorous, not performatively hostile. Push on weak reasoning without manufacturing objections.
3. Ask only about unresolved decisions. Facts that the environment can answer are the agent’s job to inspect or research.
4. Prefer high-impact questions: outcome, constraints, boundaries, dependencies, failure behavior, alternatives, reversibility, and success evidence.
5. Keep the session stateless by default. Do not write a transcript, decision log, or project file unless the user explicitly requests one.
6. Never take implementation, external communication, or other side effects as a consequence of reaching agreement.
7. Keep internal reasoning private. Emit each question and recommendation exactly once; never expose frontier calculations, draft variants, self-review, or meta-commentary.

## Workflow

### 1. Establish the shape

Read the user’s material first. If they point to files, a repository, or an existing artifact, inspect the smallest relevant surface and follow its local instructions. Do not ask the user for facts you can retrieve.

Build a private map of:

- desired outcome and who it serves;
- non-negotiable constraints and explicit non-goals;
- decisions already made versus assumed;
- dependencies between decisions;
- important risks, alternatives, and evidence still missing.

If the scope is too broad for one session, ask the user to choose a slice before opening a large decision tree.

### 2. Select the frontier

Ask from the current **frontier**: decisions whose prerequisites are known and whose answer can materially change the direction. Prefer the highest-impact unresolved decision, then continue down that branch before moving sideways.

Do not ask a downstream question while its upstream choice is still open. Recompute the frontier after every answer; do not prewrite a questionnaire.

### 3. Ask a useful question

Default to one question per turn. This means one answerable decision and one reply, not one heading containing several subquestions. If the user asks for speed, or several decisions are clearly independent, use a batch of no more than three; each item must still be independently answerable. If another uncertainty appears while writing a question, queue it for a later frontier rather than asking it inline.

Use this shape:

```text
❓ **Q<n> — <decision>**

<One focused question. State the consequence or trade-off when useful. Give concrete options only when they clarify the choice.>

➡️ **Recommendation:** <a reasoned default or strawman the user can accept, reject, or modify>
```

A good question is narrow enough to answer, consequential enough to matter, and attached to a branch. Do not ask a question whose answer would not change the work. Keep the user-visible turn to the question, necessary context, and recommendation; do not append an internal quality check or a second draft. Recommendations must separate evidence from assumptions. If the prompt does not establish a customer capability, budget, staffing level, or operational fact, label it as a hypothesis or ask for it; do not smuggle it into the recommendation as settled context. Do not invent numerical estimates unless the user supplied them or explicitly asked for an estimate; ask for the missing budget or use qualitative bounds instead.

### 4. Follow the answer

After each answer:

1. Restate the decision internally in precise terms.
2. Check it against earlier constraints and decisions.
3. If it creates a material implication, ask that implication next.
4. If it contradicts earlier information, name the contradiction and resolve it before moving on.
5. Move to another frontier branch only when the current branch is settled or explicitly deferred.

Do not end the interview with a progress summary while important branches remain open.

### 5. Handle uncertainty honestly

- **Vague answer:** ask once for a concrete value, boundary, example, or choice.
- **Second hand-wave:** say that the area is still unresolved, offer a smaller strawman, and ask whether to decide, defer, research, or prototype it.
- **“I don’t know”:** treat it as valid information. Suggest the smallest experiment, prototype, measurement, or research step that would make it answerable; do not invent certainty.
- **Fact question:** inspect the repository, files, tools, or authoritative sources. Report what is verified and keep the user’s decision separate.
- **Unprototypable-by-conversation question:** stop grilling that branch. Recommend a throwaway implementation, comparison, or test, then return only if the result changes a decision.

### 6. Check convergence

The interview is ready to close when all of the following hold:

- the desired outcome and scope are concrete;
- high-impact decisions have an owner and an explicit choice;
- constraints, non-goals, dependencies, and success evidence are stated;
- important alternatives were rejected or intentionally left open;
- assumptions are labeled, contradictions are resolved, and deferred questions have a next trigger;
- the next concrete action is possible without silently inventing a decision.

Ask for confirmation of shared understanding before declaring completion. Respect “stop,” “good enough,” or “use defaults for the rest”; record the resulting uncertainty rather than reopening it.

## Stopping rules

Stop or pause when:

- the user asks to stop or proceed;
- the session is circling the same question without new evidence;
- the remaining uncertainty can only be resolved by a prototype, test, or external fact;
- the scope needs to be split into smaller sessions;
- the frontier is empty and the user confirms the understanding is shared.

Do not use an arbitrary question count as a quality target. A short session can be correct; a long session can be avoidance.

## Output when complete

Keep the final synthesis compact:

```text
## Grill complete

**Outcome:** <what the user is committing to>
**Decisions:** <chosen paths and material rationale>
**Constraints and non-goals:** <load-bearing boundaries>
**Assumptions/evidence:** <what is verified and what remains assumed>
**Deferred:** <open item, trigger, and owner if known>
**Next action:** <the smallest concrete action now possible>
```

If the user did not confirm shared understanding, label the result `paused` rather than `complete`. Do not claim that grilling produced a sound plan; report only what was actually settled.

## Non-goals

This skill is not:

- a repository quiz or code-knowledge test;
- a bug hunt, security review, or architecture review by itself;
- a substitute for research, prototyping, testing, or user judgment;
- permission to edit files, commit, send messages, deploy, or spend money;
- a fixed checklist of questions.

## References

- `references/source-index.md` — research sources and adopted design decisions.
