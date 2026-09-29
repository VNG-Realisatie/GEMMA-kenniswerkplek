"""Relaties tussen elementen: afleiden uit het GGM, toetsen aan ArchiMate, lezen uit de pagina's.

Een relatie staat één keer, als rij in `## Relaties` op de pagina van het bronelement, met een
relatieve link naar het doelelement (Obsidian toont de omgekeerde kant als backlink):

    | Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie |
    |---|---|---|---|---|---|
    | compositie | [Onderdeel beschikking](onderdeel-beschikking.md) | bevat | 1 → 1..* | ggm-exact | EAID_… |

Relatie: associatie, associatie (gericht), aggregatie, compositie, specialisatie, toewijzing,
toegang (lezen|schrijven|lezen-schrijven), triggering, stroom, realisatie, bediening.
Grondslag: ggm-exact | ggm-afgeleid | bron. GGM-relatie: één of meer GUID's (komma-gescheiden), leeg bij `bron`.

Gebruik (vanuit de wikimap):
    uv run python tools/relaties.py voorstel <element-id> [--markdown]   # kandidaten uit het GGM
    uv run python tools/relaties.py inkomend <element-id>                # relaties die naar dit element wijzen
    uv run python tools/relaties.py lees <pagina.md>                     # de relatietabel als JSON
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT

# Nederlandse relatienaam → ArchiMate-relatie
RELATIES = {
    "associatie": "association",
    "aggregatie": "aggregation",
    "compositie": "composition",
    "specialisatie": "specialization",
    "toewijzing": "assignment",
    "toegang": "access",
    "triggering": "triggering",
    "stroom": "flow",
    "realisatie": "realization",
    "bediening": "serving",
}
TOEGANG = ("lezen", "schrijven", "lezen-schrijven")
GRONDSLAGEN = ("ggm-exact", "ggm-afgeleid", "bron")
KOLOMMEN = ["Relatie", "Naar", "Naam", "Kardinaliteit", "Grondslag", "GGM-relatie"]

ACTIEF = {"business-actor", "business-role", "business-collaboration", "business-interface"}
GEDRAG = {"business-process", "business-function", "business-event", "business-service", "business-interaction"}
PASSIEF = {"business-object", "contract", "representation"}
SAMENGESTELD = {"product"}

# Deelverzameling van de ArchiMate-relatietabel voor de business-laag (conservatief).
# (relatie, categorie bron, categorie doel); 'zelfde' = hetzelfde ArchiMate-type.
TOEGESTAAN = {
    ("association", "*", "*"),
    ("specialization", "zelfde", "zelfde"),
    ("composition", "passief", "passief"), ("aggregation", "passief", "passief"),
    ("composition", "actief", "actief"), ("aggregation", "actief", "actief"),
    ("composition", "gedrag", "gedrag"), ("aggregation", "gedrag", "gedrag"),
    ("composition", "samengesteld", "*"), ("aggregation", "samengesteld", "*"),
    ("assignment", "actief", "actief"), ("assignment", "actief", "gedrag"),
    ("access", "gedrag", "passief"), ("access", "actief", "passief"),
    ("triggering", "gedrag", "gedrag"), ("flow", "gedrag", "gedrag"),
    ("realization", "gedrag", "gedrag"), ("realization", "passief", "passief"),
    ("serving", "gedrag", "gedrag"), ("serving", "gedrag", "actief"),
}
STERKTE = {"composition": 3, "aggregation": 2, "association": 1}
DEEL_GEHEEL_WERKWOORDEN = ("bevat", "bestaat uit", "omvat", "onderdeel van", "deel van", "maakt deel uit van",
                           "heeft als onderdeel", "is samengesteld uit")


def categorie(archimate_type: str) -> str:
    for naam, typen in (("actief", ACTIEF), ("gedrag", GEDRAG), ("passief", PASSIEF), ("samengesteld", SAMENGESTELD)):
        if archimate_type in typen:
            return naam
    return "onbekend"


def toegestaan(relatie: str, bron_type: str, doel_type: str) -> bool:
    if relatie == "specialization":
        return bron_type == doel_type or {bron_type, doel_type} == {"business-object", "contract"}
    cb, cd = categorie(bron_type), categorie(doel_type)
    return any(r == relatie and b in ("*", cb) and d in ("*", cd) for r, b, d in TOEGESTAAN if b != "zelfde")


# --- Relatietabel op een pagina ---


@dataclass
class Relatie:
    relatie: str  # ArchiMate-relatie
    naar: str  # doel-id (of het linkdoel als dat niet te herleiden is)
    naam: str = ""
    kardinaliteit: str = ""
    grondslag: str = ""
    ggm_relaties: list[str] = field(default_factory=list)
    gericht: bool = False
    toegang: str | None = None
    fouten: list[str] = field(default_factory=list)


def lees_tabel(pad: Path, body: str, index_op_pad: dict[Path, str]) -> list[Relatie]:
    result = []
    for rij in gam_gemeen.tabel(gam_gemeen.sectie(body, "Relaties")):
        fouten = []
        label = rij.get("Relatie", "").strip().lower()
        m = re.fullmatch(r"(?P<soort>[a-z]+)(?:\s*\((?P<extra>[a-z-]+)\))?", label)
        soort = m.group("soort") if m else label
        extra = m.group("extra") if m else None
        if soort not in RELATIES:
            fouten.append(f"onbekende relatie '{label}'")
        gericht = soort == "associatie" and extra == "gericht"
        toegang = extra if soort == "toegang" else None
        if soort == "toegang" and toegang not in TOEGANG:
            fouten.append(f"toegang zonder geldige soort ({'/'.join(TOEGANG)})")
        gelinkt = gam_gemeen.link(rij.get("Naar", ""))
        if gelinkt is None:
            fouten.append("kolom 'Naar' bevat geen link")
            naar = rij.get("Naar", "")
        else:
            doelpad = gam_gemeen.doel_van_link(pad, gelinkt[1])
            naar = index_op_pad.get(doelpad, gelinkt[1])
            if doelpad not in index_op_pad:
                fouten.append(f"link '{gelinkt[1]}' wijst niet naar een elementpagina")
        grondslag = rij.get("Grondslag", "").strip()
        if grondslag not in GRONDSLAGEN:
            fouten.append(f"grondslag '{grondslag}' onbekend ({', '.join(GRONDSLAGEN)})")
        ggm = [g.strip() for g in rij.get("GGM-relatie", "").split(",") if g.strip()]
        if grondslag.startswith("ggm") and not ggm:
            fouten.append("grondslag ggm-* zonder GGM-relatie")
        result.append(Relatie(RELATIES.get(soort, soort), naar, rij.get("Naam", ""), rij.get("Kardinaliteit", ""),
                              grondslag, ggm, gericht, toegang, fouten))
    return result


def index_op_pad(elementen: list) -> dict[Path, str]:
    return {el.pad.resolve(): el.id for el in elementen}


def alle_relaties(wiki_root: Path = WIKI_ROOT) -> dict[str, list[Relatie]]:
    elementen = gam_gemeen.elementen(wiki_root)
    op_pad = index_op_pad(elementen)
    return {el.id: lees_tabel(el.pad, el.body, op_pad) for el in elementen}


def inkomend(element_id: str, wiki_root: Path = WIKI_ROOT) -> list[dict]:
    return [{"van": bron, **asdict(r)} for bron, rels in alle_relaties(wiki_root).items() for r in rels if r.naar == element_id]


# --- Afleiden uit het GGM ---


def _grens(waarde: str) -> int | str | None:
    if waarde == "*":
        return "*"
    return int(waarde) if waarde.isdigit() else None


def _mult(m: str) -> tuple | None:
    m = (m or "").strip()
    if not m:
        return None
    onder, _, boven = m.partition("..")
    boven = boven or onder
    o, b = _grens(onder), _grens(boven)
    return None if o is None or b is None else (o, b)


def samengestelde_multipliciteit(a: str, b: str) -> str:
    """Multipliciteit langs twee schakels: ondergrenzen vermenigvuldigen, bovengrens * zodra één * is."""
    ma, mb = _mult(a), _mult(b)
    if ma is None or mb is None:
        return ""
    onder = ma[0] * mb[0] if "*" not in (ma[0], mb[0]) else "*"
    boven = "*" if "*" in (ma[1], mb[1]) else ma[1] * mb[1]
    return f"{onder}..{boven}"


def is_deel_geheel_naam(naam: str) -> bool:
    n = (naam or "").strip().lower()
    return not n or any(w in n for w in DEEL_GEHEEL_WERKWOORDEN)


def archimate_van_ggm(rel: dict) -> dict:
    """ArchiMate-relatie voor één GGM-relatie: {relatie, bron, doel, gericht, terugmelding}.

    Volgt de mapping in ARCHITECTURE.md (Relaties): specialisatie, compositie/aggregatie alleen bij een
    deel-geheel-naam, anders (gerichte) associatie; een onjuist gebruikte aggregatie is een terugmeldkandidaat.
    """
    import ggm

    soort = rel["uml_type"]
    if soort == "Generalization":
        return {"relatie": "specialization", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": False, "terugmelding": None}
    if rel.get("aggregatie"):
        paar = ggm.geheel_en_deel(rel)
        if paar is None:
            return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                    "terugmelding": "aggregatie zonder herkenbaar geheel (richting deel-geheel onbekend)"}
        if is_deel_geheel_naam(rel.get("name", "")):
            relatie = "composition" if rel["aggregatie"] == "composite" else "aggregation"
            return {"relatie": relatie, "bron": paar[0], "doel": paar[1], "gericht": False, "terugmelding": None}
        return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                "terugmelding": f"aggregatie gebruikt voor '{rel.get('name')}': geen deel-geheel-relatie"}
    if soort == "Abstraction":
        if (rel.get("name") or "").strip().lower() in ("is een", "is a"):
            return {"relatie": "specialization", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": False,
                    "terugmelding": "specialisatie gemodelleerd als Abstraction"}
        return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                "terugmelding": "Abstraction zonder duidelijke betekenis"}
    return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"],
            "gericht": bool((rel.get("name") or "").strip()), "terugmelding": None}


def ggm_toewijzing(elementen: list) -> dict[str, tuple[str, str]]:
    """GGM-GUID → (element-id, hoe): 'eigen', 'duplicaat', 'specialisatie' of 'component'.

    Specialisaties zonder pagina en GGM-componenten worden opgetild naar het element dat ze draagt
    (`## Specialisaties`- en `## GGM-componenten`-tabellen met kolom 'GGM-guid').
    """
    toewijzing = {}
    for el in elementen:
        if el.meta.get("ggm_guid"):
            toewijzing[el.meta["ggm_guid"]] = (el.id, "eigen")
        for dup in el.meta.get("ggm_duplicaat_entiteiten", []) or []:
            toewijzing.setdefault(dup.get("guid"), (el.id, "duplicaat"))
        for kop, hoe in (("Specialisaties", "specialisatie"), ("GGM-componenten", "component")):
            for rij in gam_gemeen.tabel(gam_gemeen.sectie(el.body, kop)):
                guid = rij.get("GGM-guid", "").strip("` ")
                if guid and gam_gemeen.link(rij.get(next(iter(rij)), "")) is None:
                    toewijzing.setdefault(guid, (el.id, hoe))
    return toewijzing


@dataclass
class Kandidaat:
    relatie: str
    bron: str
    doel: str
    naam: str
    kardinaliteit: str
    grondslag: str
    ggm_relaties: list[str]
    gericht: bool = False
    terugmelding: str | None = None
    toelichting: str = ""


def _kaart(rel: dict, eind: str) -> str:
    return rel["source_card"] if eind == rel["source_id"] else rel["target_card"]


def voorstel(element_id: str, data: dict, wiki_root: Path = WIKI_ROOT) -> list[Kandidaat]:
    """Kandidaat-relaties uit het GGM voor één element (uitgaand én inkomend), na optillen en ketenen."""
    elementen = gam_gemeen.elementen(wiki_root)
    toewijzing = ggm_toewijzing(elementen)
    eigen_guids = {g for g, (e, _) in toewijzing.items() if e == element_id}
    entiteiten, relaties_ggm = data["entities"], list(data["relations"].values())

    def is_enum(guid: str) -> bool:
        return entiteiten.get(guid, {}).get("uml_type") == "Enumeration"

    kandidaten: dict[tuple, Kandidaat] = {}

    def voeg_toe(k: Kandidaat) -> None:
        if k.bron == k.doel:
            return  # lus na optillen
        sleutel = (k.relatie, k.bron, k.doel)
        if sleutel in kandidaten:  # samenvoegen
            kandidaten[sleutel].ggm_relaties += [g for g in k.ggm_relaties if g not in kandidaten[sleutel].ggm_relaties]
            return
        kandidaten[sleutel] = k

    for rel in relaties_ggm:
        if not ({rel["source_id"], rel["target_id"]} & eigen_guids):
            continue
        hier = rel["source_id"] if rel["source_id"] in eigen_guids else rel["target_id"]
        daar = rel["target_id"] if hier == rel["source_id"] else rel["source_id"]
        if is_enum(daar):
            continue  # typering/waardelijst: eigenschap, geen relatie
        a = archimate_van_ggm(rel)
        opgetild = toewijzing.get(hier, ("", ""))[1] != "eigen"

        if daar in toewijzing:
            ander, hoe = toewijzing[daar]
            if a["relatie"] == "specialization" and (opgetild or hoe != "eigen"):
                continue  # specialisatie wordt niet opgetild of geketend
            bron = element_id if a["bron"] == hier else ander
            doel = ander if bron == element_id else element_id
            voeg_toe(Kandidaat(a["relatie"], bron, doel, rel.get("name", ""),
                               f"{_kaart(rel, a['bron']) or '?'} → {_kaart(rel, a['doel']) or '?'}",
                               "ggm-exact" if not opgetild and hoe == "eigen" else "ggm-afgeleid",
                               [rel["id"]], a["gericht"], a["terugmelding"] if not opgetild and hoe == "eigen" else None,
                               "" if hoe == "eigen" and not opgetild else f"opgetild ({hoe if hoe != 'eigen' else 'eigen zijde'})"))
            continue

        # Keten A–X–B via een niet-opgenomen X (één tussenstap)
        if a["relatie"] == "specialization":
            continue
        for rel2 in relaties_ggm:
            if rel2["id"] == rel["id"] or daar not in (rel2["source_id"], rel2["target_id"]):
                continue
            verder = rel2["target_id"] if rel2["source_id"] == daar else rel2["source_id"]
            if verder not in toewijzing or toewijzing[verder][0] == element_id or is_enum(verder):
                continue
            a2 = archimate_van_ggm(rel2)
            if a2["relatie"] == "specialization":
                continue
            zwakste = min((a["relatie"], a2["relatie"]), key=lambda r: STERKTE.get(r, 1))
            zwakste = zwakste if zwakste in STERKTE else "association"
            kaart_b = samengestelde_multipliciteit(_kaart(rel, daar), _kaart(rel2, verder))
            kaart_a = samengestelde_multipliciteit(_kaart(rel2, daar), _kaart(rel, hier))
            voeg_toe(Kandidaat(zwakste, element_id, toewijzing[verder][0],
                               f"{rel.get('name', '')} / {rel2.get('name', '')}".strip(" /"),
                               f"{kaart_a or '?'} → {kaart_b or '?'}", "ggm-afgeleid", [rel["id"], rel2["id"]],
                               zwakste == "association", None,
                               f"via {entiteiten.get(daar, {}).get('name', daar)} (niet opgenomen)"))
    return sorted(kandidaten.values(), key=lambda k: (k.bron != element_id, k.relatie, k.doel))


def markdown_rijen(element_id: str, kandidaten: list[Kandidaat], wiki_root: Path = WIKI_ROOT) -> str:
    index = gam_gemeen.element_index(wiki_root)
    terug = {v: k for k, v in RELATIES.items()}
    van = index[element_id].pad
    regels = ["| " + " | ".join(KOLOMMEN) + " |", "|" + "---|" * len(KOLOMMEN)]
    for k in kandidaten:
        if k.bron != element_id:
            continue
        doel = index.get(k.doel)
        naar = f"[{doel.meta.get('naam', k.doel)}]({gam_gemeen.relatief(van, doel.pad)})" if doel else k.doel
        label = terug[k.relatie] + (" (gericht)" if k.gericht and k.relatie == "association" else "")
        regels.append(f"| {label} | {naar} | {k.naam} | {k.kardinaliteit} | {k.grondslag} | {', '.join(k.ggm_relaties)} |")
    return "\n".join(regels) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Relaties tussen elementen (zie docstring).")
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("voorstel")
    v.add_argument("element")
    v.add_argument("--markdown", action="store_true", help="Alleen uitgaande relaties, als tabelrijen voor ## Relaties")
    sub.add_parser("inkomend").add_argument("element")
    sub.add_parser("lees").add_argument("pagina")
    a = p.parse_args(argv)

    if a.cmd == "voorstel":
        import ggm

        kandidaten = voorstel(a.element, ggm.laad())
        if a.markdown:
            sys.stdout.write(markdown_rijen(a.element, kandidaten))
        else:
            print(json.dumps([asdict(k) for k in kandidaten], indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "inkomend":
        print(json.dumps(inkomend(a.element), indent=2, ensure_ascii=False))
        return 0
    from llmwiki import frontmatter

    pad = Path(a.pagina).resolve()
    rels = lees_tabel(pad, frontmatter.read(pad).body, index_op_pad(gam_gemeen.elementen()))
    print(json.dumps([asdict(r) for r in rels], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
