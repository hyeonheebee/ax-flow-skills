#!/usr/bin/env python3
"""Install these two skills into a workspace without replacing existing skills."""

import argparse
from pathlib import Path
import shutil
import sys


SKILLS = ("ax-flow", "ax-data-clean")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True,
                        help="Folder where Codex will be launched")
    parser.add_argument("--skill", choices=SKILLS, action="append",
                        help="Install only this skill; may be repeated")
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    if not workspace.is_dir():
        parser.error(f"workspace does not exist: {workspace}")

    selected = args.skill or list(SKILLS)
    source_root = Path(__file__).resolve().parent / "skills"
    target_root = workspace / ".agents" / "skills"

    for name in selected:
        src = source_root / name
        dst = target_root / name
        if not (src / "SKILL.md").is_file():
            parser.error(f"missing source skill: {src}")
        if dst.exists() or dst.is_symlink():
            print(f"Existing skill left unchanged: {dst}", file=sys.stderr)
            return 1

    target_root.mkdir(parents=True, exist_ok=True)
    for name in selected:
        dst = target_root / name
        shutil.copytree(source_root / name, dst)
        print(f"Installed: {dst}")
    print("Start a new Codex chat in this workspace, then check /skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
