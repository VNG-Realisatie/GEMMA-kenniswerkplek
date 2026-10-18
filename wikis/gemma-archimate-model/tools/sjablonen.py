"""Sjablonen voor patronen die vaak terugkomen: een beoordeling klaarzetten met de kenmerken van fase A en B, de
standaardrelaties en de velden van de indeling.

Patroon `upl-dienst`: een extern UPL-product of -dienst (business-service), gerealiseerd door een bedrijfsproces met een
kernobject. Het proces is een bestaand proces (`--proces <id>`: alleen de relatie realisatie komt erbij) of een nieuw
proces (`--proces-naam`): dan krijgt het ook zijn kenmerken en, met `--toegang`, de relatie toegang naar het kernobject.

Het sjabloon vult de structuur in, nooit de inhoud: elk ja-kenmerk, de definitie en de beschrijving krijgen een tekst
met `TODO`, plus de bronnen die de aanroep meegeeft. `beslissen.py` meldt een fout zolang er een `TODO` staat, zodat
een afwijking van het patroon niet ongezien blijft: de AI vervangt elke TODO door de onderbouwing uit de bronnen, of
past het kenmerk aan (`beoordeling.py zet`). Een bestaande beoordeling blijft ongemoeid. Het sjabloon zet geen `status`
en geen `beslist`.

Dit bestand levert alleen de gegevens (`bouw`); het schrijven en valideren doet `beoordeling.py sjabloon`.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import bepaal_type

TODO = "TODO"
PATRONEN = ("upl-dienst",)

# De keuzevelden, de keuzekenmerken en de relatiekenmerken met ja; de scope is doorlopen, het begrip is zelfstandig en
# de toetskenmerken die geen relatie zijn, zijn standaard ja.
DIENST_VELDEN = {"vak": "bedrijf/gedrag-extern"}
DIENST_JA = ("gerealiseerd_door",)
PROCES_VELDEN = {"vak": "bedrijf/gedrag-intern", "soort_gedrag": "per_keer_doorlopen"}
PROCES_JA = ("toegewezen_partij", "aanleiding")
PROCES_KEUZE = {"procesniveau": "bedrijfsproces"}


class SjabloonFout(Exception):
    pass


@dataclass
class Params:
    id: str
    naam: str
    onderwerp: str
    kernobject: str
    bronnen: list[str]
    upl_nr: str | None = None
    taakveld: str | None = None
    beleidsdomein: str | None = None
    domein: str | None = None
    proces: str | None = None  # id van een bestaand proces
    proces_naam: str | None = None  # naam van een nieuw proces
    proces_id: str | None = None  # id van het nieuwe proces (standaard: slug van de naam)
    toegang: str | None = None  # raadplegen | registreren: de toegang van het nieuwe proces tot het kernobject


def slug(tekst: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")


def _regel(waarde: str, tekst: str, bronnen: list[str]) -> str:
    return f"{waarde} — {tekst}" + (f" [{', '.join(bronnen)}]" if bronnen else "")


def _kenmerken(ja: tuple[str, ...], bronnen: list[str], naar: dict[str, list[str]] | None = None,
               keuze: dict[str, str] | None = None) -> dict:
    """De kenmerken die een antwoord nodig hebben, in de schrijfvorm van één regel; een relatiekenmerk met een bekende
    tegenpartij krijgt `naar`. De andere kenmerken hebben een standaardantwoord."""
    naar = naar or {}
    uit: dict = {s: _regel(w, f"{TODO}: {bepaal_type.NAAM[s]}", bronnen) for s, w in (keuze or {}).items()}
    for s in ja:
        uit[s] = {"waarde": "ja", "naar": naar[s]} if s in naar else _regel("ja", f"{TODO}: {bepaal_type.NAAM[s]}", bronnen)
    return uit


def _basis(p: Params, begrip: str, definitie: str, velden: dict) -> dict:
    return {"begrip": begrip, **velden, "onderwerpen": [p.onderwerp], "afnemer": "extern", "bronnen": list(p.bronnen),
            **({"domein": p.domein} if p.domein else {}), **({"taakveld": p.taakveld} if p.taakveld else {}),
            **({"beleidsdomein": p.beleidsdomein} if p.beleidsdomein else {}),
            "definitie": f"{TODO}: {definitie}",
            "beschrijving": [f"{TODO}: beschrijving met artikelen en vindplaatsen uit de bronnen."],
            "gemma": {"sterkte": "geen", "onderbouwing": f"{TODO}: zoek de GEMMA-match (tools/gemma.py kandidaten) of "
                                                         "leg uit waarom er geen is."}}


def _relatie(soort: str, naar: str, naam: str, bronnen: list[str]) -> dict:
    return {"soort": soort, "naar": naar, "naam": naam, "ggm_match": "geen", "bronnen": bronnen,
            "vindplaats": f"{TODO}: artikel of UPL-nummer"}


def bouw(patroon: str, p: Params) -> dict[str, dict]:
    """De beoordelingen van het patroon, per id, met kenmerken in de schrijfvorm van één regel. Bij een bestaand proces
    bevat het resultaat voor dat proces alleen `relaties` (de aanroeper voegt ze toe)."""
    if patroon not in PATRONEN:
        raise SjabloonFout(f"onbekend patroon '{patroon}'; kies uit {', '.join(PATRONEN)}")
    if not p.bronnen:
        raise SjabloonFout("geef minstens één --bron: elk ja-kenmerk steunt op een bron")
    if bool(p.proces) == bool(p.proces_naam):
        raise SjabloonFout("geef --proces (een bestaand proces) of --proces-naam (een nieuw proces), niet beide of geen")
    if p.toegang and p.toegang not in ("raadplegen", "registreren"):
        raise SjabloonFout("--toegang is raadplegen of registreren")
    upl = f"UPL nr. {p.upl_nr}" if p.upl_nr else "UPL"
    proces = p.proces or p.proces_id or slug(p.proces_naam)
    uit = {p.id: {**_basis(p, p.naam, f"wat de gemeente aanbiedt ({upl}), in één zin.", DIENST_VELDEN),
                  "kenmerken": _kenmerken(DIENST_JA, p.bronnen, {"gerealiseerd_door": [proces]})}}
    realisatie = _relatie("realisatie", p.id, "realiseert", p.bronnen)
    if p.proces:
        uit[p.proces] = {"relaties": [realisatie]}
        return uit
    toegang = [_relatie(f"toegang ({p.toegang})", p.kernobject, f"{TODO}: handeling", p.bronnen)] if p.toegang else []
    uit[proces] = {
        **_basis(p, p.proces_naam, "wat het proces doet, van aanleiding tot resultaat.", PROCES_VELDEN),
        "kernobject": p.kernobject, "kenmerken": _kenmerken(PROCES_JA, p.bronnen, keuze=PROCES_KEUZE),
        "relaties": [realisatie, *toegang]}
    return uit


def open_todo(data) -> list[str]:
    """De plekken in een beoordeling waar nog een TODO staat (pad: sleutel.sleutel[0])."""
    uit: list[str] = []

    def loop(x, pad: str) -> None:
        if isinstance(x, dict):
            for k, v in x.items():
                loop(v, f"{pad}.{k}" if pad else str(k))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                loop(v, f"{pad}[{i}]")
        elif isinstance(x, str) and re.search(rf"\b{TODO}\b", x):
            uit.append(pad)

    loop(data, "")
    return uit
