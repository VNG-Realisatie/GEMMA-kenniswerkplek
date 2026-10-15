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

DIENST_JA = ("herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp", "gedrag", "aangeboden_gedrag",
             "benoembaar_resultaat", "komt_herhaald_voor", "eigen_normering", "afnemer", "gerealiseerd_door",
             "zelfstandige_specialisatie")
PROCES_JA = ("herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp", "gedrag", "per_keer_doorlopen",
             "toegewezen_partij", "gebruikt_objecten", "aanleiding", "benoembaar_resultaat", "komt_herhaald_voor",
             "eigen_normering", "bijdrage_aan_groter_proces", "klant_tot_klant", "eigen_besluit", "levert_aanbod",
             "zelfstandige_specialisatie")
STANDAARD_NEE = {"buiten_dit_model": "Geen doel, waarde, principe, losse norm, vermogen of thema.",
                 "slechts_eigenschap": "Geen eigenschap, status of indeling van één ander begrip."}
KALE = set(bepaal_type.AARD) | {s for s, k in bepaal_type.KENMERK.items() if k.groep == "Soort gedrag"}


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


def _kenmerken(ja: tuple[str, ...], bronnen: list[str], soort: str, extra: dict[str, str] | None = None) -> dict:
    """Alle kenmerken in de schrijfvorm van één regel; `normaliseer_data` laat de nee's buiten het pad weg."""
    extra = extra or {}
    uit: dict = {}
    for s in bepaal_type.SLEUTELS:
        if s in ja:
            uit[s] = _regel("ja", f"{TODO}: {extra.get(s) or bepaal_type.NAAM[s]}", bronnen)
        elif s in KALE:
            uit[s] = bepaal_type.KALE_NEE
        elif s in STANDAARD_NEE:
            uit[s] = _regel("nee", STANDAARD_NEE[s], [])
        elif s in ("generiek", "geautomatiseerd_verwerkt"):
            uit[s] = _regel("nee", f"{TODO}: bevestig dat {bepaal_type.NAAM[s]} hier niet geldt", bronnen)
        else:
            uit[s] = _regel("nee", f"Niet van toepassing: {soort}.", [])
    return uit


def _basis(p: Params, begrip: str, definitie: str) -> dict:
    return {"begrip": begrip, "onderwerpen": [p.onderwerp], "afnemer": "extern",
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
    uit = {p.id: {**_basis(p, p.naam, f"wat de gemeente aanbiedt ({upl}), in één zin."),
                  "kenmerken": _kenmerken(DIENST_JA, p.bronnen, "dienst",
                                          {"herkenbaar": f"product in de UPL ({upl}); gangbare term"})}}
    realisatie = _relatie("realisatie", p.id, "realiseert", p.bronnen)
    if p.proces:
        uit[p.proces] = {"relaties": [realisatie]}
        return uit
    toegang = [_relatie(f"toegang ({p.toegang})", p.kernobject, f"{TODO}: handeling", p.bronnen)] if p.toegang else []
    uit[p.proces_id or slug(p.proces_naam)] = {
        **_basis(p, p.proces_naam, "wat het proces doet, van aanleiding tot resultaat."),
        "kernobject": p.kernobject, "kenmerken": _kenmerken(PROCES_JA, p.bronnen, "bedrijfsproces"),
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
