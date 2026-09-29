"""Hulpfuncties voor de tests van gemma-archimate-model."""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WIKI = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import bepaal_type  # noqa: E402,F401

KENMERKEN_BO = {s: "nee" for s in bepaal_type.SLEUTELS} | {
    s: "ja" for s in ("herkenbaar", "gemeentelijk", "eigen_identiteit", "onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")
}


def element_tekst(meta: dict, body: str = "# Titel\n") -> str:
    import yaml

    return f"---\n{yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{body}"


