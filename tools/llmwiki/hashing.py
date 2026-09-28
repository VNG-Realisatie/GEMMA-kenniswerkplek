"""Deterministische hashing voor content, plannen en akkoordcontrole."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hash_text(text: str) -> str:
    return hash_bytes(text.encode("utf-8"))


def hash_file(path: Path) -> str:
    return hash_bytes(path.read_bytes())


def hash_json(obj) -> str:
    """Hash van canonieke JSON-representatie (stabiele sleutelvolgorde)."""
    canonical = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hash_text(canonical)


def short(digest: str, length: int = 8) -> str:
    return digest[:length]
