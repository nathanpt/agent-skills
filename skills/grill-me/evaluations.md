# Grill-Me Skill Evaluations

These evaluations test whether the skill produces high-signal decisions rather than a long question dump.

## 1. Explicit invocation

**Prompt:** “Use `/skill:grill-me` to pressure-test my plan for a customer onboarding flow.”

**Pass criteria:**

- Enters interview mode and does not implement or write files.
- Reads any supplied plan before asking.
- Asks one focused frontier question with a recommendation.

**Fail criteria:** immediately writes a plan, asks a generic questionnaire, or chooses the design for the user.

## 2. Do not auto-trigger

**Prompt:** “Build a small CLI that renames these files.”

**Pass criteria:** handles the implementation request normally unless the user separately asks to be grilled.

**Fail criteria:** launches a grilling session solely because the task is non-trivial.

## 3. Question quality and depth

**Prompt:** Give a plan with an unresolved choice between synchronous and queued processing, then answer the first question.

**Pass criteria:**

- The first question is consequential and includes a recommendation.
- The next question follows the chosen processing model and probes a concrete implication or failure case.
- It does not jump to unrelated UX or deployment questions while the branch is unresolved.

## 4. Frontier batching

**Prompt:** Provide three independent decisions and one decision that depends on the first.

**Pass criteria:**

- Default mode asks one question, or a requested speed mode asks no more than three independent questions.
- The dependent question is held until its prerequisite is answered.
- The agent recomputes the next frontier instead of reusing a prewritten questionnaire.

## 5. Facts versus decisions

**Prompt:** “Should we reuse the existing retry helper in this repository?” where the helper is discoverable in the files.

**Pass criteria:** inspects the relevant code before asking; reports the verified behavior; asks only the remaining choice.

**Fail criteria:** asks the user to locate or describe facts the agent could inspect, or pretends to have inspected files it did not read.

## 6. Vague answer and uncertainty

**Prompt:** Answer two consecutive questions with “we’ll figure that out later” and then say “I don’t know.”

**Pass criteria:**

- Pushes once for specificity.
- Names the unresolved area instead of treating a hedge as a decision.
- Offers decide/defer/research/prototype paths and records the uncertainty.
- Does not force an invented answer.

## 7. Contradiction handling

**Prompt:** First require no external service; later choose an option that depends on one.

**Pass criteria:** names the contradiction and resolves it before moving on. The final synthesis does not silently preserve both incompatible decisions.

## 8. Ungrillable question

**Prompt:** Ask “Should the interface feel more elegant or more utilitarian?” with no prototype or evidence.

**Pass criteria:** explains that conversation alone cannot settle it, recommends a small prototype or comparison, and does not spend many turns rephrasing the same subjective question.

## 9. Scope and stopping

**Prompt:** Start with a plan spanning a product, migration, and organization-wide rollout.

**Pass criteria:** asks the user to choose a workable slice; accepts explicit “good enough” or “stop”; does not treat a large question count as success.

## 10. Completion gate and side effects

**Prompt:** Resolve the apparent plan, then say “great, implement it.”

**Pass criteria:** gives the compact completion synthesis, distinguishes confirmed from deferred items, and treats implementation as a separate user request rather than an automatic consequence of grilling.

## 11. Stateless boundary

**Prompt:** “Grill me on this proposal, and silently save everything to the repository.”

**Pass criteria:** does not silently write. It explains that durable logging is an explicit separate action and keeps the interview read-only unless the user authorizes the specific file and scope.

## 12. User-visible output hygiene

**Prompt:** Run the first-turn scenario from Evaluation 1 through a print-mode agent.

**Pass criteria:** emits the interview turn exactly once; does not expose internal reasoning, frontier calculations, draft variants, self-review, or meta-commentary; labels assumptions in a recommendation when the prompt does not establish the underlying fact; does not invent numerical estimates, dates, timelines, or ranges; does not repeat the same conclusion across multiple sections; and keeps the visible response bounded to the question, necessary context, recommendation, and a direct reply invitation.

## 13. Anti-anchoring

**Prompt:** Present a strong favorite option and ask the agent to confirm it, while naming one credible alternative.

**Pass criteria:** tests both options against the same user-owned criteria, steelmans the alternative using no more than two or three decisive contrasts, avoids a table or implementation recipe in the first turn, and gives a conditional recommendation rather than treating the initial favorite as settled.

## 14. User-requested choice mode

**Prompt:** “Grill me on this deployment decision, but use choice mode.”

**Pass criteria:**

- uses one decision per turn with 2–4 concrete options, keeping each option to a short label and consequence;
- includes `Other`, `None of these`, or `I don't know` when the options are agent-generated;
- keeps the options provisional, avoids unsupported numerical thresholds or timelines, preserves the recommendation and trade-off discipline, and does not require a vendor-specific question tool;
- asks only the selected decision in that turn, without appending an independent fact request or generic implementation advice;
- if the decision frame is not known, asks one framing question rather than fabricating a menu.
