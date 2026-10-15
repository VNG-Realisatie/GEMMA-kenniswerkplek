"""Beoordeling: opzoeken en wijzigen van beoordelingen met een commando, zonder de yaml te knippen.

Subcommando's:
- `zoek <naam>…`: één regel per begrip (id, naam, type, niveau, thuisonderwerp, kernobject, definitie), op naam, synoniem of id;
- `besluiten <onderwerp>`: de besluiten van het onderwerp en van zijn beoordelingen, compact;
- `toon <id> --oordeel`: de beoordeling zonder `beslist:` en `status:` en zonder de standaard-nee ("Niet van toepassing");
- `zet <id> <veld> <waarde>`: zet een veld (een punt-pad als `kenmerken.herkenbaar.waarde` mag; de waarde is YAML);
- `relatie <id> --soort … --naar …`: voeg een relatie toe of vervang die met dezelfde soort en hetzelfde doel (`--verwijder`);
- `besluit <id> --datum … --gevolg … (--tekst … | --advies-gevolgd)`: voeg een besluit toe;
- `normaliseer <id>… | --alle`: de kenmerken in de opgeslagen vorm (de schrijfvorm van één regel, `herkenbaar: ja —
  onderbouwing [bron-id]`, wordt een object; een nee buiten het pad valt weg), met wat op het pad nog open staat.

Het wijzigen valideert tegen het schema en raakt `status` en `beslist` niet aan; draai daarna `tools/beslissen.py`.
Het akkoord van de redacteur blijft buiten bereik: dit gereedschap zet nooit een status.

Gebruik (vanuit de wikimap):
    uv run python tools/beoordeling.py zoek aanvraag besluit
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bepaal_type  # noqa: E402
import gam_gemeen  # noqa: E402
from llmwiki import beoordeling  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
GEWEIGERD = ("status", "beslist", "begrip", "onderwerpen")  # van de scripts, of de identiteit van het begrip
STANDAARD_NEE = "Niet van toepassing"
BRON_ID = re.compile(r"[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*")


class Fout(Exception):
    pass


def _alle(wiki: Path) -> dict[str, tuple[Path, dict]]:
    return beoordeling.alle(wiki, gam_gemeen.wiki_yaml(wiki))


def _vind(alle: dict, bid: str) -> tuple[Path, dict]:
    if bid not in alle:
        raise Fout(f"geen beoordeling '{bid}'; zoek met `zoek`")
    return alle[bid]


def _norm(tekst: str) -> str:
    return " ".join(str(tekst).lower().split())


def _regel(bid: str, data: dict) -> str:
    u = (data.get("beslist") or {}).get("uitkomst") or {}
    typ = u.get("archimate_type") or u.get("soort") or "?"
    niveau = "generiek" if u.get("generiek") or u.get("objectniveau") == "generiek" else (u.get("objectniveau") or "-")
    delen = [bid, data["begrip"], typ, niveau, data["onderwerpen"][0], data.get("kernobject") or "-",
             data.get("definitie") or "-"]
    return " | ".join(delen)


def zoek(wiki: Path, termen: list[str], alle: dict | None = None) -> list[str]:
    alle = alle if alle is not None else _alle(wiki)
    uit: list[str] = []
    for term in termen:
        t = _norm(term)
        exact, deel = [], []
        for bid, (_, d) in alle.items():
            namen = [_norm(d["begrip"]), bid, *(_norm(s["naam"]) for s in d.get("synoniemen") or [])]
            if t in namen or t.replace(" ", "-") == bid:
                exact.append(bid)
            elif any(t in n for n in namen):
                deel.append(bid)
        gevonden = exact or deel
        if not gevonden:
            uit.append(f"{term}: niet gevonden")
        for bid in gevonden:
            uit.append(_regel(bid, alle[bid][1]) + ("" if exact else f"  [deel van '{term}']"))
    return uit


def besluiten(wiki: Path, onderwerp: str) -> list[str]:
    afb = gam_gemeen.afbakeningen(wiki)
    if onderwerp not in afb:
        raise Fout(f"onderwerp '{onderwerp}' bestaat niet: {', '.join(afb)}")
    uit: list[str] = []

    def toon(label: str, lijst: list[dict]) -> None:
        for b in lijst:
            tekst = b.get("besluit") or "(advies gevolgd)"
            stand = f" [stand: {b['stand']}]" if b.get("stand") else ""
            gevolg = f" {b['gevolg']}" if b.get("gevolg") else ""
            uit.append(f"{label} {b.get('datum')}{gevolg}: {tekst}{stand}")

    toon(f"[{onderwerp}]", afb[onderwerp].get("besluiten") or [])
    for bid, (_, d) in _alle(wiki).items():
        if onderwerp in d["onderwerpen"]:
            toon(f"[{bid}]", d.get("besluiten") or [])
    return uit


def oordeel(data: dict) -> dict:
    """De beoordeling zonder scriptvelden en zonder de standaard-nee; de nee die de uitkomst bepaalt, blijft."""
    uit = {k: v for k, v in data.items() if k not in beoordeling.SCRIPTVELDEN}
    uit["kenmerken"] = {s: a for s, a in (data.get("kenmerken") or {}).items()
                        if not (isinstance(a, dict) and a.get("waarde") == "nee"
                                and str(a.get("onderbouwing", "")).startswith(STANDAARD_NEE))}
    return uit


def regel_naar_antwoord(sleutel: str, tekst: str) -> dict | str:
    """De schrijfvorm van één regel, `ja — onderbouwing [bron-id, id-…]`, als antwoord: een id met `id-` is een
    GEMMA-relatie (`gemma_relatie`), de andere zijn bronnen. Een nee zonder onderbouwing en bronnen blijft de kale nee."""
    m = re.fullmatch(r"\s*(ja|nee)\b(.*)", tekst, re.S)
    if not m:
        raise Fout(f"kenmerk {sleutel}: '{tekst}' begint niet met ja of nee")
    waarde, rest = m.group(1), m.group(2).strip()
    ids: list[str] = []
    lijst = re.fullmatch(r"(.*?)\s*\[([^\[\]]*)\]", rest, re.S)
    if lijst:
        kandidaten = [i.strip() for i in lijst.group(2).split(",") if i.strip()]
        if kandidaten and all(BRON_ID.fullmatch(i) or i.startswith("id-") for i in kandidaten):
            rest, ids = lijst.group(1), kandidaten
    onderbouwing = re.sub(r"^[\s—–:-]+", "", rest).strip()
    bronnen = [i for i in ids if not i.startswith("id-")]
    relaties = [i for i in ids if i.startswith("id-")]
    if not onderbouwing:
        if waarde == "nee" and not ids:
            return bepaal_type.KALE_NEE
        raise Fout(f"kenmerk {sleutel}: {waarde} zonder onderbouwing")
    return {"waarde": waarde, "onderbouwing": onderbouwing, **({"bronnen": bronnen} if bronnen else {}),
            **({"gemma_relatie": relaties} if relaties else {})}


def normaliseer_data(data: dict) -> tuple[dict, list[str]]:
    """De kenmerken in de opgeslagen vorm: de schrijfvorm van één regel wordt een object, een nee buiten het pad valt
    weg (behalve met bronnen of een GEMMA-relatie), de volgorde is die van de vragenlijst. Geeft ook wat op het pad nog
    open staat."""
    kenmerken = {s: regel_naar_antwoord(s, a) if isinstance(a, str) and a != bepaal_type.KALE_NEE else a
                 for s, a in (data.get("kenmerken") or {}).items()}
    tijdelijk = {**data, "kenmerken": kenmerken}
    a, b = bepaal_type.pad(bepaal_type.waarden(tijdelijk), bepaal_type.extra_velden(tijdelijk))
    op_pad = set(a) | set(b)

    def blijft(s: str, x) -> bool:
        if s in op_pad or s not in bepaal_type.NAAM or bepaal_type.antwoord(kenmerken, s)["waarde"] == "ja":
            return True
        return isinstance(x, dict) and bool(x.get("bronnen") or x.get("gemma_relatie"))

    volgorde = {s: i for i, s in enumerate(bepaal_type.SLEUTELS)}
    nieuw = dict(sorted(((s, x) for s, x in kenmerken.items() if blijft(s, x)), key=lambda p: volgorde.get(p[0], 999)))
    open_ = [bepaal_type.NAAM[s] for s in a + b if s not in nieuw]
    return {**data, "kenmerken": nieuw}, ([f"op het pad nog niet beantwoord: {', '.join(open_)}"] if open_ else [])


def normaliseer(wiki: Path, ids: list[str], alles: bool = False) -> list[str]:
    alle = _alle(wiki)
    if not ids and not alles:
        raise Fout("geef een of meer id's, of --alle")
    uit: list[str] = []
    for bid in (sorted(alle) if alles else ids):
        pad, data = _vind(alle, bid)
        nieuw, meldingen = normaliseer_data(data)
        weg = len(data.get("kenmerken") or {}) - len(nieuw["kenmerken"])
        if nieuw != data:
            _opslaan(wiki, bid, pad, nieuw)
            uit.append(f"{bid}: genormaliseerd ({weg} nee buiten het pad weggelaten)" if weg else f"{bid}: genormaliseerd")
        uit += [f"{bid}: {m}" for m in meldingen]
    if not uit:
        uit.append("Niets te normaliseren.")
    return uit + (["Draai tools/beslissen.py."] if any("genormaliseerd" in r for r in uit) else [])


def toon(wiki: Path, bid: str, alleen_oordeel: bool) -> str:
    _, data = _vind(_alle(wiki), bid)
    return beoordeling.dump(oordeel(data) if alleen_oordeel else data)


def _valideer(wiki: Path, bid: str, data: dict) -> None:
    schema = json.loads((wiki / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
    fouten = [f"{'/'.join(map(str, e.path)) or '(top)'}: {e.message}"
              for e in jsonschema.Draft202012Validator(schema).iter_errors(data)]
    if fouten:
        raise Fout(f"{bid}: niet geschreven, schemafout: " + "; ".join(fouten))


def _opslaan(wiki: Path, bid: str, pad: Path, data: dict) -> None:
    _valideer(wiki, bid, data)
    beoordeling.schrijf(pad, data)


def _zet_sleutel(data: dict, sleutel: str, waarde) -> dict:
    """Zet een sleutel op het hoogste niveau; een nieuwe sleutel komt vóór `besluiten`, `status` en `beslist`."""
    if sleutel in data:
        data[sleutel] = waarde
        return data
    uit: dict = {}
    geplaatst = False
    for k, v in data.items():
        if not geplaatst and k in ("besluiten", "status", "beslist"):
            uit[sleutel] = waarde
            geplaatst = True
        uit[k] = v
    if not geplaatst:
        uit[sleutel] = waarde
    return uit


def zet(wiki: Path, bid: str, veld: str, waarde: str) -> str:
    pad, data = _vind(_alle(wiki), bid)
    delen = veld.split(".")
    if delen[0] in GEWEIGERD:
        raise Fout(f"'{delen[0]}' zet dit gereedschap niet (scripts, of de identiteit van het begrip)")
    nieuw = yaml.safe_load(waarde)
    if len(delen) == 2 and delen[0] == "kenmerken" and isinstance(nieuw, str):
        nieuw = regel_naar_antwoord(delen[1], nieuw)
    if len(delen) == 1:
        data = _zet_sleutel(data, delen[0], nieuw)
    else:
        cur = data.setdefault(delen[0], {})
        for d in delen[1:-1]:
            if isinstance(cur.get(d), str):  # een kale nee
                cur[d] = {"waarde": cur[d]}
            cur = cur.setdefault(d, {})
        cur[delen[-1]] = nieuw
    _opslaan(wiki, bid, pad, data)
    return f"{bid}: {veld} gezet; draai tools/beslissen.py"


def relatie(wiki: Path, bid: str, soort: str, naar: str, naam: str | None = None, bronnen: list[str] | None = None,
            vindplaats: str | None = None, ggm_match: str = "geen", verwijder: bool = False) -> str:
    alle = _alle(wiki)
    pad, data = _vind(alle, bid)
    if naar not in alle:
        raise Fout(f"doel '{naar}' is geen beoordeling")
    lijst = [r for r in data.get("relaties") or [] if not (r["soort"] == soort and r["naar"] == naar)]
    had = len(lijst) != len(data.get("relaties") or [])
    if verwijder:
        if not had:
            raise Fout(f"{bid}: geen relatie {soort} naar {naar}")
        melding = "verwijderd"
    else:
        nieuw = {"soort": soort, "naar": naar, **({"naam": naam} if naam else {}), "ggm_match": ggm_match,
                 **({"bronnen": bronnen} if bronnen else {}), **({"vindplaats": vindplaats} if vindplaats else {})}
        lijst.append(nieuw)
        melding = "vervangen" if had else "toegevoegd"
    data = _zet_sleutel(data, "relaties", lijst) if lijst else {k: v for k, v in data.items() if k != "relaties"}
    _opslaan(wiki, bid, pad, data)
    return f"{bid}: relatie {soort} naar {naar} {melding}; draai tools/beslissen.py"


def besluit(wiki: Path, bid: str, datum: str, gevolg: str, tekst: str | None = None, advies_gevolgd: bool = False,
            redenen: list[str] | None = None) -> str:
    if not tekst and not advies_gevolgd:
        raise Fout("geef --tekst of --advies-gevolgd")
    pad, data = _vind(_alle(wiki), bid)
    nieuw = {"datum": datum, **({"besluit": tekst} if tekst else {}), "gevolg": gevolg,
             **({"advies": "gevolgd"} if advies_gevolgd else {}), **({"redenen": redenen} if redenen else {})}
    data = _zet_sleutel(data, "besluiten", [*(data.get("besluiten") or []), nieuw])
    _opslaan(wiki, bid, pad, data)
    return f"{bid}: besluit van {datum} toegevoegd; draai tools/beslissen.py"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("zoek")
    p.add_argument("termen", nargs="+")
    p = sub.add_parser("besluiten")
    p.add_argument("onderwerp")
    p = sub.add_parser("toon")
    p.add_argument("id")
    p.add_argument("--oordeel", action="store_true")
    p = sub.add_parser("zet")
    p.add_argument("id")
    p.add_argument("veld")
    p.add_argument("waarde")
    p = sub.add_parser("relatie")
    p.add_argument("id")
    p.add_argument("--soort", required=True)
    p.add_argument("--naar", required=True)
    p.add_argument("--naam")
    p.add_argument("--bron", action="append", dest="bronnen")
    p.add_argument("--vindplaats")
    p.add_argument("--ggm-match", default="geen", choices=["exact", "geen"])
    p.add_argument("--verwijder", action="store_true")
    p = sub.add_parser("besluit")
    p.add_argument("id")
    p.add_argument("--datum", required=True)
    p.add_argument("--gevolg", required=True, choices=["opnemen", "afwijzen", "verwerkt"])
    p.add_argument("--tekst")
    p.add_argument("--advies-gevolgd", action="store_true")
    p.add_argument("--reden", action="append", dest="redenen")
    p = sub.add_parser("normaliseer")
    p.add_argument("ids", nargs="*")
    p.add_argument("--alle", action="store_true")
    a = parser.parse_args(argv)
    try:
        if a.cmd == "zoek":
            uit = "\n".join(zoek(a.wiki, a.termen))
        elif a.cmd == "besluiten":
            uit = "\n".join(besluiten(a.wiki, a.onderwerp))
        elif a.cmd == "toon":
            uit = toon(a.wiki, a.id, a.oordeel).rstrip("\n")
        elif a.cmd == "zet":
            uit = zet(a.wiki, a.id, a.veld, a.waarde)
        elif a.cmd == "relatie":
            uit = relatie(a.wiki, a.id, a.soort, a.naar, a.naam, a.bronnen, a.vindplaats, a.ggm_match, a.verwijder)
        elif a.cmd == "normaliseer":
            uit = "\n".join(normaliseer(a.wiki, a.ids, a.alle))
        else:
            uit = besluit(a.wiki, a.id, a.datum, a.gevolg, a.tekst, a.advies_gevolgd, a.redenen)
    except Fout as exc:
        print(f"fout: {exc}")
        return 1
    print(uit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
