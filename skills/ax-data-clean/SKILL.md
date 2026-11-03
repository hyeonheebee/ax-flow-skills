---
name: ax-data-clean
description: Use to profile and clean CSV or Excel tables with missing values, duplicates, inconsistent dates, or mixed types while preserving the source and explaining each transformation. Do not use for unstructured text or an unspecified production database.
---

# AX Data Clean

Treat the source as evidence. Preserve it unchanged and write cleaned data to a separate file or sheet unless the user explicitly requests replacement.

## Inspect

- Identify the source, intended use, row count, column names, data types, and any stated key or uniqueness rule.
- Count missing cells, exact duplicate rows, repeated keys, mixed types, and date formats. Show a few safe examples without revealing private values.
- Separate definite defects from ambiguous values. A repeated person or transaction ID is not automatically a duplicate record. A date such as `03/04/2026` has no safe month/day interpretation without a rule.

## Clean

- State proposed transformations and their reasons before changing the table. Ask only for a rule that materially affects the result, such as the meaning of ambiguous dates, a deduplication key, or whether missing values should be filled.
- Apply reversible changes with standard local tools. Prefer a small script or transparent formulas when the transformation must be repeated. Avoid adding dependencies that the environment does not need.
- Record what happened to each row when rows are removed or merged. Keep unresolved values marked for review instead of guessing.

## Verify and report

- Compare before and after row counts, missing-value counts, duplicate counts, and relevant types. Reopen the output to confirm it can be read.
- Report what was changed, what was left unresolved, the rules used, and the path to both source and output. Never present an inferred value as original data.
