---
name: ax-flow
description: Use for a scoped software or data task when the user wants an upfront five-line kickoff, clear decisions, verified results, and a concise handoff. Do not invoke for a simple factual question.
---

# AX Flow

Use the user's own project instructions and task requirements as the source of truth. Keep the user in charge of scope and decisions. Explain in plain language; give a hint first when the user is learning.

## Kickoff

For a new build or substantial change, show five short lines before editing:

1. Scope: the requested outcome and boundaries.
2. Data touched: files, databases, and accounts that may be read or changed.
3. Failure impact: what could break if the change is wrong.
4. Recovery: the available backup, version history, or other way to undo it. Say when none exists.
5. Success check: observable behavior or a test that will show it works.

Wait for the user's decision when these lines expose an unresolved choice, substantial risk, or requested review point. Otherwise continue within the authorized scope. Do not turn routine edits into an approval ritual.

## Work and decisions

- Read the relevant requirements and inspect the starting state before changing it. Summarize the problem in the user's terms.
- Make the smallest useful change, then verify it. Distinguish an attempted test from a passed test and a claimed result from something personally observed.
- Record meaningful decisions: what was chosen, why, and the tradeoff or alternative that mattered. Attribute the user's own choices accurately; do not invent their reasoning.
- When relevant, explain the data path (input, transformation, storage, output), who may access each part, where permissions are enforced, and why the chosen algorithm or data source fits. Mark unknowns instead of guessing.
- If the user changes an AI suggestion, record the actual difference and the user's reason. Do not invent a disagreement for a report.
- When a bug is reported, reproduce it if possible, identify the cause from evidence, change the cause, and check for recurrence.

## Handoff

Use filenames and formats required by the project. In the final handoff, give the run steps, observed verification, remaining limits, and the next action. Keep notes brief enough that the user can explain the work in their own words.
