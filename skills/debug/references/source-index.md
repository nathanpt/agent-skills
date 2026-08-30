# Debug Skill Source Index

## Cursor — Debug Mode

- **Blog:** https://cursor.com/blog/debug-mode
- **Documentation:** https://cursor.com/docs/agent/debug-mode
- **Retrieved:** 2026-08-29
- **Local copy:** `cursor-debug-mode.md`
- **Relevant principles:** generate multiple hypotheses before fixing; add targeted runtime instrumentation; ask the user to reproduce; analyze actual runtime data; make a targeted fix; verify through reproduction; remove instrumentation after human confirmation.

## doraemonkeys — Claude Code Debug Mode

- **Repository:** https://github.com/doraemonkeys/claude-code-debug-mode
- **Retrieved:** 2026-08-29
- **Local copy:** `doraemonkeys-debug-mode.md`
- **Relevant principles:** reproduction and evidence are the non-negotiable core; the transport can adapt to local, remote, mobile, or intermittent systems; hypothesis-tagged logs and marked instrumentation support analysis and cleanup; avoid flooding normal terminal output.

## Ronnie Schaniel — A Debug Skill for Your Coding Agent

- **Original:** https://ronnieschaniel.com/ai/a-debug-skill-for-your-coding-agent
- **Retrieved:** 2026-08-29
- **Local copy:** `ronnie-debug-skill.md`
- **Relevant principles:** remain in diagnosis mode when evidence is weak; produce two or three bounded hypotheses; show the likely failure path; create a narrow failing reproduction; require a stopping condition to prevent endless speculative fixes; explain the issue clearly to the developer.

## Existing local foundation

- **Systematic debugging skill:** `~/.hermes/skills/software-development/systematic-debugging/SKILL.md`
- **Role:** general root-cause and no-fix-before-investigation procedure. The new skill should specialize in evidence collection and runtime instrumentation rather than duplicate it.

## Candidate name

`debug`
