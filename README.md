# AX Flow skills

Two small, public-ready Codex skills for scoped work and CSV/Excel cleanup. They contain reusable instructions only. No private work files, account settings, hooks, or API keys are included.

- `ax-flow`: five-line kickoff, decisions, verification, and handoff.
- `ax-data-clean`: profile, clean, and verify tabular data while keeping the original.

## Bring into a workspace

From a terminal in the workspace where you will run Codex:

```bash
git clone https://github.com/hyeonheebee/ax-flow-skills.git
python3 ax-flow-skills/install.py --workspace .
codex
```

The GitHub address works only after this repository has been published there. The installer copies both skills into `.agents/skills/` in the workspace and refuses to overwrite an existing skill. It does not run the skills or change your project data.

In Codex, run `/skills` to check that both names appear. Start a new chat if an already-open chat does not refresh the list. Then try:

```text
$ax-flow Read this project's README and give me the five kickoff lines before a small change.
```

```text
$ax-data-clean Inspect practice/sample.csv. Count missing values, repeated IDs, exact duplicate rows, and ambiguous dates. Tell me which rules are needed before cleaning; do not guess.
```

For the sample, the date `03/04/2026` and the repeated ID `A102` are intentionally ambiguous. A good first response flags both instead of silently changing or deleting them.

For a folder with many tables, start with:

```text
$ax-data-clean Make a compact data map for this task. Calculate file counts, sizes, headers, and row counts locally. Show me only the most relevant tables and why they matter. Do not paste full data or clean anything yet.
```

These skills do not grant permissions or override the rules of a particular task or environment. Use only tools and data allowed in that environment.
