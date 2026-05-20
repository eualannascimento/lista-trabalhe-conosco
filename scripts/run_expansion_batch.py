#!/usr/bin/env python3
"""Orquestra um lote de expansão: universo → score → discover → ingest → higiene."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], env: dict | None = None):
    print(f"\n>> {' '.join(cmd)}")
    merged = os.environ.copy()
    if env:
        merged.update(env)
    subprocess.run(cmd, cwd=ROOT, check=True, env=merged)


def main():
    limit = os.environ.get("DISCOVER_LIMIT", "350")
    run([sys.executable, "scripts/build_candidate_universe.py"])
    run([sys.executable, "scripts/score_candidates.py"])
    run(
        [sys.executable, "scripts/discover_career_urls.py"],
        env={"DISCOVER_LIMIT": limit},
    )
    run([sys.executable, "scripts/expand_ready_from_profiles.py"])
    run([sys.executable, "scripts/ingest_batch.py"])
    run([sys.executable, "scripts/audit_hygiene.py"])

    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        total = sum(1 for _ in f) - 1
    print(f"\nBatch complete. list.csv rows: {total}")


if __name__ == "__main__":
    main()
