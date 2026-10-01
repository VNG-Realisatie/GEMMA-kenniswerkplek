"""Hulpfuncties voor de tests van gemma-archimate-model."""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WIKI = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import bepaal_type  # noqa: E402,F401

KENMERKEN_BO = {s: "nee" for s in bepaal_type.SLEUTELS} | {
    s: "ja" for s in ("herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp",
                      "zelfstandige_specialisatie", "onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")
}


def element_tekst(meta: dict, body: str = "# Titel\n", definitie_bovenaan: bool = True) -> str:
    """Paginatekst; een elementpagina krijgt `## Definitie` als eerste sectie, zoals het sjabloon voorschrijft."""
    import re

    import yaml

    if definitie_bovenaan and meta.get("archimate_type") and "## Definitie" not in body:
        sectie = f"## Definitie\n\n{meta.get('definitie', '')}\n\n"
        eerste = re.search(r"^## ", body, re.M)
        body = body[: eerste.start()] + sectie + body[eerste.start():] if eerste else body.rstrip("\n") + "\n\n" + sectie
    return f"---\n{yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{body}"


