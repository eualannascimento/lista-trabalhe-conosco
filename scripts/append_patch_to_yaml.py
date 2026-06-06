#!/usr/bin/env python3
"""Anexa o patch verificado ao final de known_career_urls.yaml."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = ROOT / "data/seeds/known_career_urls.yaml"
PATCH_PATH = ROOT / "artifacts/known_career_urls_patch.yaml"


def main() -> None:
    base = YAML_PATH.read_text(encoding="utf-8").rstrip() + "\n"
    patch = PATCH_PATH.read_text(encoding="utf-8")

    # Remove cabeçalho duplicado se já existir no patch
    lines = patch.splitlines()
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("- name:"):
            body_start = i
            break
    header = "\n".join(lines[:body_start]).rstrip()
    body = "\n".join(lines[body_start:]).rstrip() + "\n"

    if "# === Lote curado:" in base:
        out = base.rstrip() + "\n\n" + body
    else:
        out = base.rstrip() + "\n\n" + header + "\n\n" + body

    YAML_PATH.write_text(out, encoding="utf-8")
    count = body.count("- name:")
    print(f"Anexadas {count} empresas -> {YAML_PATH}")


if __name__ == "__main__":
    main()
