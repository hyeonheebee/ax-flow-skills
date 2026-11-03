---
name: ax-data-clean
description: Use to profile and clean CSV or Excel tables with missing values, duplicates, inconsistent dates, or mixed types while preserving the source and explaining each transformation. Do not use for unstructured text or an unspecified production database.
---

# AX Data Clean

Treat the source as evidence. Preserve it unchanged and write cleaned data to a separate file or sheet unless the user explicitly requests replacement. When there are many files or rows, keep the model's context small: compute counts locally and return a compact summary instead of printing table contents.

## Map first when there is a lot of data

- Use the task requirements to identify which tables may matter. First inspect filenames, file sizes, sheet names, headers, and approximate row counts. Do not read or paste whole tables into the chat.
- If the inventory is long, save the full file list in the workspace and report only the most relevant files plus the total count. Say why those files matter; leave the others available for later inspection.
- Profile selected tables with local code or formulas that output aggregate counts. Show at most a few representative, non-sensitive values only when a count cannot explain a problem. Limit command output before it reaches the chat.
- Reuse the saved profile and inspect individual rows or columns only to answer a specific question. Do not repeatedly scan or summarize the full dataset.

## Inspect

- Identify the source, intended use, row count, column names, data types, and any stated key or uniqueness rule. Start with the tables relevant to the task.
- Count missing cells, exact duplicate rows, repeated keys, mixed types, and date formats. Show a few safe examples without revealing private values.
- Separate definite defects from ambiguous values. A repeated person or transaction ID is not automatically a duplicate record. A date such as `03/04/2026` has no safe month/day interpretation without a rule.

## Clean

- State proposed transformations and their reasons before changing the table. Ask only for a rule that materially affects the result, such as the meaning of ambiguous dates, a deduplication key, or whether missing values should be filled.
- Apply reversible changes with standard local tools. Prefer a small script or transparent formulas when the transformation must be repeated. Avoid adding dependencies that the environment does not need.
- Record what happened to each row when rows are removed or merged. Keep unresolved values marked for review instead of guessing.

## Verify and report

- Compare before and after row counts, missing-value counts, duplicate counts, and relevant types. Reopen the output to confirm it can be read.
- Report what was changed, what was left unresolved, the rules used, and the path to both source and output. Never present an inferred value as original data.
