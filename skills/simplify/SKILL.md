---
name: simplify
description: Review recent code changes for reuse, quality, and efficiency, then apply justified cleanup.
---

# Simplify Recent Changes

Use this skill after implementing a feature or finishing a meaningful code change. Review the current change set, search the repository for better existing patterns, and simplify only when the evidence supports it. This is a post-work cleanup pass, not permission to redesign the feature.

## Scope and safety

- Review the current repository diff before changing anything.
- Prefer unstaged and staged changes together when the user says "my changes"; if the target is ambiguous, ask which diff to review.
- Preserve the user's intent, public behavior, APIs, error semantics, and project conventions.
- Do not reset, clean, stash, revert, or overwrite unrelated work.
- Do not expand the feature, extract a framework, rename unrelated code, or modernize files outside the change surface.
- Do not apply speculative improvements merely because they are stylistically preferred.
- If no meaningful diff exists, inspect only recently modified files or the files named by the user and say which fallback was used.
- Treat review findings as hypotheses. Verify each finding against the repository before changing code.
- Treat plans and self-reported verification as claims, not evidence. Check the implementation and effective runtime behavior.
- Separate static review from runtime verification: static review finds contract/code drift, reuse, and structural issues; real execution finds CLI/API/environment behavior that source inspection cannot prove.

## Procedure

### 1. Establish the change surface

Inspect:

- `git status`
- `git diff`
- `git diff --cached`
- recent commit diff when the user explicitly means the last commit
- repository instructions such as `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and relevant package guidance

Record the exact files under review and the unrelated dirty paths that must remain untouched. If the diff is very large, summarize it by file and review the highest-risk portions first rather than blindly passing an oversized prompt to every reviewer.

### 2. Launch focused reviews in parallel

Give every reviewer the complete relevant diff plus the repository instructions. Ask each reviewer to return findings only, with file/line references, evidence, severity, confidence, and a concrete recommendation. They must not edit files.

Use three reviewers when the diff is substantive, contract-heavy, security-sensitive, or broad enough that independent search has real value. For a small or cold-path diff, use two reviewers or one focused review; do not spend three agent turns to manufacture confidence. Record why the chosen fan-out was proportionate.

#### Reviewer A — reuse and duplication

Look for:

- Existing helpers, utilities, constants, types, or components that should be reused.
- New functions duplicating existing behavior.
- Copy-pasted branches with minor variation.
- Hand-rolled parsing, path handling, environment checks, validation, or serialization where repository utilities already exist.
- New abstractions that duplicate a nearby abstraction.

Do not recommend reuse merely because two pieces of code look superficially similar. Confirm compatible inputs, outputs, error behavior, and ownership. Search all relevant repository occurrences before calling a local idiom non-standard; distinguish a real convention break from personal style.

#### Reviewer B — code quality and boundaries

Look for:

- Redundant state or values that can be derived safely.
- Parameter sprawl and awkward APIs.
- Leaky abstractions or broken module boundaries.
- Stringly-typed values where an established constant/type exists.
- Unclear naming, unreachable branches, dead code, and error handling that hides failures.
- Changes that make the code harder to understand or test.
- Plans, labels, and status output that do not match the code's effective behavior.
- Precedence bugs where an extra flag, environment variable, config layer, or later override wins at runtime while the displayed label or explanation reports an earlier value.

Preserve intentional explicitness. A shorter implementation is not automatically a better implementation.

#### Reviewer C — efficiency and operational behavior

Look for:

- Repeated file reads, API calls, computations, or subprocesses.
- Independent work performed sequentially where concurrency is safe and materially useful.
- N+1 behavior, blocking work on startup or hot paths, and unnecessary network round trips.
- Unbounded memory growth, missing cleanup, and listener/process leaks.
- TOCTOU checks that should instead perform the operation and handle the error.
- Overly broad filesystem or repository scans.

Do not optimize cold paths or tiny operations without evidence that the complexity is worth it.

### 3. Reconcile findings

After all reviewers finish:

1. Deduplicate overlapping findings.
2. Discard findings that misunderstand the repository or the requested behavior.
3. Resolve conflicts by checking the source, tests, and project instructions.
4. Rank findings:
   - **Must fix:** correctness, security, data loss, broken boundary, or clear regression.
   - **Should fix:** strong reuse, clarity, or measurable unnecessary work within the change surface.
   - **Consider later:** valid but speculative, broad, or unrelated improvements.
5. Keep the final change set small. If no finding clears the bar, leave the code unchanged and report that result.

Before editing, state the accepted findings and the exact files each fix will touch. Do not apply reviewer suggestions automatically.

### 4. Apply only accepted fixes

Implement the smallest changes that address the accepted findings. Preserve:

- Existing public behavior unless a bug fix explicitly changes it.
- Error messages and exit codes unless the finding concerns their correctness.
- Existing configuration and environment-variable precedence.
- Unrelated dirty work.
- The original feature's scope.

Do not turn a simplify pass into a general refactor.

### 5. Verify the cleanup

Run the narrowest relevant checks first, then the repository's documented focused tests. At minimum:

- Inspect `git diff` again.
- Confirm every changed file is intentional.
- Confirm unrelated dirty paths are unchanged.
- Run the relevant test/lint/typecheck command when the repository documents one.
- Check that no secrets, generated artifacts, or debug output were added.
- Re-read the changed code and verify each accepted finding is actually addressed.
- Exercise the real boundary when the change affects a CLI, API, environment, configuration precedence, serialization format, process lifecycle, or other runtime contract. Static review cannot prove what executable actually runs or what value wins.
- Prefer invariant tests over a fixed denylist: assert that unsupported flags cannot leak, effective values match displayed labels, and all relevant precedence paths agree.

If checks fail, diagnose whether the failure came from the cleanup or the pre-existing baseline. Do not hide failures or claim success from a partial command.

## Output format

Report:

1. Change surface reviewed.
2. Review summaries for each lane actually run: reuse, quality, and/or efficiency.
3. Accepted findings and why.
4. Rejected/deferred findings and why, when useful.
5. Exact files changed.
6. Verification commands and real results.
7. Remaining concerns.

If the pass made no changes, say so plainly and explain why. "No cleanup needed" is a valid result.

## Invocation examples

- `Use /skill:simplify to review my recent changes.`
- `Simplify the current diff, focusing on unnecessary API calls.`
- `Run a post-work cleanup pass on the feature I just implemented; do not expand scope.`

## Non-goals

This skill does not:

- Replace a security review.
- Replace project-specific tests or code review.
- Automatically commit, push, open a pull request, or deploy.
- Review the entire repository when a bounded diff exists.
- Force parallelism when the available diff is too small or the work is not independently reviewable.
