# Instrumentation Guide

Use temporary instrumentation only when existing evidence cannot distinguish the active hypotheses.

## Rules

- Name the hypothesis the instrumentation tests.
- Capture only the smallest useful fields: boundary inputs/outputs, state transitions, timing, ordering, retries, resource lifecycle, or configuration propagation.
- Use stable tags such as `[DEBUG H1]` so output maps back to the hypothesis.
- Redact secrets and private data. Prefer counts, types, IDs, hashes, sizes, and boolean state over payloads.
- Mark instrumentation consistently so it can be found and removed.
- Prefer the project’s existing local diagnostic path; otherwise use an ignored local artifact only with an explicit cleanup plan.
- Do not change application behavior beyond the diagnostic effect.
- Avoid high-volume logs, new infrastructure, or broad repository-wide logging.

## Evidence transport

The runtime may be local, remote, mobile, containerized, intermittent, or otherwise unable to write into the repository. Adapt the transport rather than weakening the evidence requirement. The agent must receive evidence from a real reproduction of the failure path.

## Cleanup

After verification, search for every debug marker, temporary endpoint, diagnostic flag, and generated log. Remove temporary instrumentation and inspect the diff. Never commit captured credentials, tokens, cookies, private data, or large runtime dumps.
