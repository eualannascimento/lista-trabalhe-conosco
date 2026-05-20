"""Utilitários de score e normalização de nomes."""

import os
import re
from pathlib import Path

import yaml
from unidecode import unidecode

ROOT = Path(__file__).resolve().parents[1]


def load_scoring_config():
    path = ROOT / "data/seeds/scoring.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize_name(name: str) -> str:
    n = unidecode((name or "").lower())
    n = re.sub(r"\s*(s/?a|ltda|sa|holding|grupo|brasil)\s*", " ", n)
    n = re.sub(r"[^a-z0-9]+", "", n)
    return n.strip()


def compute_score(signals: dict, config: dict) -> int:
    pts = config["signals"]
    score = 0
    if signals.get("b3"):
        score += pts["b3_listed"]
    if signals.get("revenue"):
        score += pts["revenue_1b_plus"]
    if signals.get("employees"):
        score += pts["employees_2000_plus"]
    if signals.get("top"):
        score += pts["top_sector_leader"]
    if signals.get("fortune"):
        score += pts["fortune_global_br"]
    return score


def should_exclude_name(name: str, config: dict) -> bool:
    n = name.lower()
    for pat in config.get("exclude_name_patterns", []):
        if pat.lower() in n:
            return True
    if re.match(r"^[a-z0-9\-]{1,12}$", unidecode(name.lower())) and " " not in name:
        if any(x in n for x in ("analytics", "docs", "new", "novo", "proxy")):
            return True
    return False
