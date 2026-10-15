"""Beslissen: van het oordeel van de AI naar type, status en modelgegevens, met harde controles.

Leest elke beoordeling in `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml` (het oordeel van de AI) en vult per beoordeling:
- `beslist.uitkomst`: de uitkomst van de beslistabel (tools/bepaal_type.py) uit de kenmerken;
- `beslist.voor_te_leggen` en `beslist.open`: waarom de redacteur moet beslissen, en wat daarvan nog voorligt (bij een
  element tot het akkoord, bij een begrip zonder pagina tot een besluit `afwijzen`);
- `status` (alleen bij een element): `review`, of `afgewezen` na het besluit `afwijzen`; de redenen om voor te leggen
  houden de status niet tegen. `goedgekeurd` blijft staan zolang `log.md` een promotieregel met de hash van de inhoud heeft; zet
  alleen `llmwiki promote` (na akkoord). Elke inhoudelijke wijziging maakt een goedgekeurd element weer `review`;
- `beslist.pad`: waar het render-script de pagina zet (map en submappen uit wiki.yaml: taakveld en beleidsdomein, bij een functie het domein);
- `beslist.ggm`, `beslist.ggm_duplicaten`, `beslist.gemma`: de letterlijke velden bij de match die de AI koos
  (tools/ggm.py, tools/gemma.py); de AI vult die nooit zelf;
- `beslist.kwaliteitsdoelen`: bij een beleidskader de letterlijke naam en definitie van elk GEMMA-kwaliteitsdoel;
- `beslist.bronnen` en `beslist.herkomst`: alle bronnen van het begrip, en het brontype van de hoogste.
Nieuwe GGM-terugmeldingen in `modellen/ggm/terugmeldingen.yaml` krijgen het volgende nummer.

Harde controles (fout: er wordt niets geschreven): schema, kenmerken, verplichte velden van een element, bestaan van
bronnen (met bronduiding), GGM-guid, GEMMA-id, doelen van relaties, specialisaties, tegenhanger en homoniemen, de
ArchiMate-relatietabel, de bronduidingen, de omzettingen van de modellen in `sources/modellen/`, het veld `object_van` (Archi-objecten), het register van beleidsdomeinen (`modellen/gemma/indelingen/beleidsdomeinen.yaml`) en de besluiten van onderwerpen en beoordelingen (vorm, geen bestandspad). Zachte signalen (waarschuwingen, met de naam
van de regel) staan in tools/signalen.py. Daarna draait het render-script (tools/render.py), tenzij `--zonder-render`.

Met `--alleen <id>…` beslist het script over alles, maar schrijft en rendert het niets, en toont het alleen de fouten,
waarschuwingen en uitkomsten van die beoordelingen: zo controleert een beoordelingsagent zijn eigen bestanden zonder
de bestanden van een andere agent te raken.

Gebruik (vanuit de wikimap):
    uv run python tools/beslissen.py [--zonder-render] [--alles]
    uv run python tools/beslissen.py --alleen <id> [<id> …]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import jsonschema

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bepaal_type  # noqa: E402
import gam_gemeen  # noqa: E402
import relaties as relatietool  # noqa: E402
import sjablonen  # noqa: E402
import signalen  # noqa: E402
from llmwiki import beoordeling, frontmatter, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TERUGMELDINGEN = gam_gemeen.GGM_TERUGMELDINGEN
TERUGMELDTYPEN = ("hiaat", "definitie", "structuur", "scope", "duplicaat", "homoniem", "relatie")
TERUGMELDSTATUS = ("open", "gemeld", "opgelost", "afgewezen")
PA_TERUGMELDINGEN = gam_gemeen.PA_TERUGMELDINGEN
PA_TYPEN = ("indeling", "grondslag", "product", "kennismodel")
GEMMA_TERUGMELDINGEN = gam_gemeen.GEMMA_TERUGMELDINGEN
GEMMA_TYPEN = ("element", "indeling", "definitie", "relatie")
BELEIDSDOMEINEN = gam_gemeen.BELEIDSDOMEINEN


@dataclass
class Resultaat:
    fouten: list[str] = field(default_factory=list)
    waarschuwingen: list[str] = field(default_factory=list)
    gewijzigd: list[str] = field(default_factory=list)
    uitkomsten: dict[str, dict] = field(default_factory=dict)  # per beoordeling: soort, paginatype, status, open


def slug(tekst: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")


def _schoon(obj):
    """Laat lege waarden weg (None, '', [], {}), zodat `beslist` kort en stabiel blijft."""
    if isinstance(obj, dict):
        return {k: _schoon(v) for k, v in obj.items() if v is not None and v != "" and v != [] and v != {}}
    if isinstance(obj, list):
        return [_schoon(v) for v in obj]
    return obj


class Context:
    """Wat beslissen nodig heeft van buiten de beoordeling: wiki.yaml, bronnen, GGM, GEMMA, log."""

    def __init__(self, wiki_root: Path):
        self.wiki_root = wiki_root
        self.wiki_yaml = paths.load_wiki_yaml(wiki_root)
        self.repo_root = paths.find_repo_root(wiki_root)
        self.schema = json.loads((wiki_root / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
        log = wiki_root / "log.md"
        self.log = log.read_text(encoding="utf-8") if log.exists() else ""
        self._ggm = self._gemma = self._functies = None
        self._brontypen: dict[str, str | None] = {}

    def ggm(self) -> dict:
        if self._ggm is None:
            import ggm
            self._ggm = ggm.laad(gam_gemeen.model_json(self.wiki_root, "ggm"))
        return self._ggm

    def gemma(self) -> dict:
        if self._gemma is None:
            import gemma
            self._gemma = gemma.laad(gam_gemeen.model_json(self.wiki_root, "gemma"))
        return self._gemma

    def functies(self) -> dict:
        """De functiehiërarchie van GEMMA as-is (tools/gemma.py `functiehierarchie`)."""
        if self._functies is None:
            import gemma
            self._functies = gemma.functiehierarchie(self.gemma())
        return self._functies

    def brontype(self, bron_id: str) -> str | None:
        """brontype uit sources/index; None als de bron niet bestaat."""
        if bron_id not in self._brontypen:
            pad = self.repo_root / "sources" / "index" / f"{bron_id}.md"
            self._brontypen[bron_id] = (frontmatter.read(pad).meta.get("brontype") or "overig") if pad.exists() else None
        return self._brontypen[bron_id]


def bronnen_van(data: dict) -> list[str]:
    """Alle bronnen van een beoordeling, in volgorde: expliciet, kenmerken, relaties, formele definitie."""
    ids = list(data.get("bronnen", []))
    for antwoord in bepaal_type.antwoorden(data).values():
        ids += antwoord.get("bronnen", [])
    for r in data.get("relaties", []):
        ids += r.get("bronnen", [])
    for dp in data.get("deelprocessen", []):
        ids += dp.get("bronnen", [])
    for k in data.get("kwaliteitsdoelen", []):
        ids += k.get("bronnen", [])
    ids += (data.get("gemma_functie") or {}).get("bronnen", [])
    if data.get("definitie_formeel_bron"):
        ids.append(data["definitie_formeel_bron"]["bron"])
    return list(dict.fromkeys(ids))


def pagina_pad(ctx: Context, paginatype: str, data: dict, beoordeling_id: str) -> str:
    definitie = ctx.wiki_yaml["page_types"][paginatype]
    delen = [definitie["dir"]] + [slug(w) for s in definitie.get("submappen", []) if (w := bepaal_type.submap(data, s))]
    return "/".join(delen + [f"{beoordeling_id}.md"])


def _relatie_archimate(soort: str) -> tuple[str, str | None]:
    """'toegang (registreren)' → ('access', 'registreren'); 'associatie (gericht)' → ('association', None)."""
    m = re.match(r"^(\w+)(?: \((.+)\))?$", soort)
    naam, toevoeging = m.group(1), m.group(2)
    return relatietool.RELATIES[naam], (toevoeging if naam == "toegang" else None)


def _controleer_element(ctx: Context, bid: str, data: dict, uitkomst: dict, res: Resultaat) -> None:
    paginatype = uitkomst["paginatype"]
    for veld in ("definitie", "beschrijving", "gemma"):
        if not data.get(veld):
            res.fouten.append(f"{bid}: element zonder '{veld}'")
    for veld in ctx.wiki_yaml["page_types"][paginatype].get("submappen", []):
        if not bepaal_type.submap(data, veld):
            res.fouten.append(f"{bid}: {paginatype} zonder '{veld}' (bepaalt de map)")
    if uitkomst.get("data_object") == "ja" or paginatype in ("bedrijfsobject", "product"):
        if not data.get("ggm"):
            res.fouten.append(f"{bid}: {paginatype} zonder GGM-match ('ggm', ook bij sterkte geen)")
    res.fouten += [f"{bid}: {f}" for f in bepaal_type.controleer_indelingsvelden(data, uitkomst)]
    for onderwerp in data.get("per_onderwerp", {}):
        if onderwerp not in data["onderwerpen"]:
            res.fouten.append(f"{bid}: per_onderwerp '{onderwerp}' staat niet in onderwerpen")


def _modelvelden(ctx: Context, bid: str, data: dict, res: Resultaat) -> dict:
    import gemma as gemmatool
    import ggm as ggmtool

    beslist = {}
    ggm_keuze = data.get("ggm") or {}
    if ggm_keuze.get("guid"):
        treffers = ggmtool.zoek_entiteit(ctx.ggm(), ggm_keuze["guid"])
        if treffers:
            beslist["ggm"] = ggmtool.velden(treffers[0])
        else:
            res.fouten.append(f"{bid}: GGM-guid {ggm_keuze['guid']} bestaat niet in het GGM")
    elif ggm_keuze and ggm_keuze.get("sterkte") != "geen":
        res.fouten.append(f"{bid}: GGM-match '{ggm_keuze.get('sterkte')}' zonder guid")
    duplicaten = []
    for d in ggm_keuze.get("duplicaten", []):
        treffers = ggmtool.zoek_entiteit(ctx.ggm(), d["guid"])
        if not treffers:
            res.fouten.append(f"{bid}: GGM-duplicaat {d['guid']} bestaat niet in het GGM")
            continue
        v = ggmtool.velden(treffers[0])
        duplicaten.append({"entiteit": v.get("ggm_entiteit"), "guid": d["guid"],
                           "beleidsdomein": v.get("ggm_beleidsdomein"), "taakveld": v.get("ggm_taakveld")})
    beslist["ggm_duplicaten"] = duplicaten
    gemma_keuze = data.get("gemma") or {}
    if gemma_keuze.get("id"):
        treffers = gemmatool.zoek_element(ctx.gemma(), gemma_keuze["id"])
        if treffers:
            beslist["gemma"] = gemmatool.velden(treffers[0])
        else:
            res.fouten.append(f"{bid}: GEMMA-id {gemma_keuze['id']} bestaat niet in het GEMMA-model")
    elif gemma_keuze and gemma_keuze.get("sterkte") != "geen":
        res.fouten.append(f"{bid}: GEMMA-match '{gemma_keuze.get('sterkte')}' zonder id")
    generiek = data.get("gemma_generiek") or {}
    if generiek.get("id"):
        treffers = gemmatool.zoek_element(ctx.gemma(), generiek["id"])
        if treffers:
            beslist["gemma_generiek"] = gemmatool.velden(treffers[0])
        else:
            res.fouten.append(f"{bid}: gemma_generiek '{generiek['id']}' bestaat niet in het GEMMA-model")
    functie = data.get("gemma_functie") or {}
    if functie.get("id"):
        treffers = [e for e in gemmatool.zoek_element(ctx.gemma(), functie["id"]) if e["type"] == "business-function"]
        if treffers:
            beslist["gemma_functie"] = {
                **gemmatool.velden(treffers[0]),
                "gemma_paden": [" › ".join(p) for p in gemmatool.functie_paden(ctx.gemma(), ctx.functies(), treffers[0]["id"])]}
    return beslist


def _kwaliteitsdoelen(ctx: Context, bid: str, data: dict, uitkomst: dict, res: Resultaat) -> dict:
    """`kwaliteitsdoelen` van een beleidskader: elk een kwaliteitsdoel van GEMMA, op id, één keer; met de letterlijke
    naam en definitie."""
    doelen = data.get("kwaliteitsdoelen") or []
    if doelen and uitkomst.get("paginatype") != "beleidskader":
        res.fouten.append(f"{bid}: kwaliteitsdoelen horen alleen bij een beleidskader")
        return {}
    velden, gezien = [], set()
    for k in doelen:
        e = ctx.gemma()["elementen"].get(k["id"])
        if e is None or e["type"] != "goal" or e["eigenschappen"].get("GEMMA type") != "Kwaliteitsdoel":
            res.fouten.append(f"{bid}: '{k['id']}' is geen kwaliteitsdoel in het GEMMA-model "
                              "(zoek met tools/gemma.py kandidaten)")
            continue
        if e["id"] in gezien:
            res.fouten.append(f"{bid}: kwaliteitsdoel {e['naam']} staat er twee keer")
            continue
        gezien.add(e["id"])
        velden.append({"gemma_id": e["id"], "gemma_naam": e["naam"], "gemma_definitie": e["documentatie"]})
    return {"kwaliteitsdoelen": velden}


def _controleer_bronnen(ctx: Context, bid: str, bronnen: list[str], res: Resultaat) -> None:
    for bron_id in bronnen:
        if ctx.brontype(bron_id) is None:
            res.fouten.append(f"{bid}: bron {bron_id} staat niet in sources/index")
        elif gam_gemeen.bron_doel(ctx.wiki_root, bron_id) is None:
            res.fouten.append(f"{bid}: bron {bron_id} heeft geen bronduiding")


def herkomst(ctx: Context, bronnen: list[str]) -> str | None:
    volgorde = ctx.wiki_yaml.get("bronvoorrang", [])
    typen = [ctx.brontype(b) for b in bronnen if ctx.brontype(b) in volgorde]
    return min(typen, key=volgorde.index) if typen else None


def _controleer_verwijzingen(bid: str, data: dict, uitkomsten: dict[str, dict], res: Resultaat,
                             namen: dict[str, str] | None = None) -> None:
    elementen = {i for i, u in uitkomsten.items() if u and u.get("soort") == "element"}
    namen = namen or {}
    for r in data.get("relaties", []):
        via = r.get("via")
        if not via:
            continue
        u = uitkomsten.get(via)
        doel = namen.get(r["naar"], r["naar"]).lower()
        if not u or u.get("soort") != "specialisatie" or str(u.get("genoemd_begrip") or "").lower() != doel:
            res.fouten.append(f"{bid}: via '{via}' bij de relatie naar '{r['naar']}' is geen specialisatie van dat doel")
    if bepaal_type.waarden(data)["leidt_tot_gebeurtenis"] == "ja" and not any(
            r["soort"] == "triggering" and (uitkomsten.get(r["naar"]) or {}).get("paginatype") == "gebeurtenis"
            for r in data.get("relaties", [])):
        res.fouten.append(f"{bid}: leidt tot gebeurtenis, maar geen relatie 'triggering' naar een gebeurtenis")
    van_type = uitkomsten[bid]["archimate_type"]
    for r in data.get("relaties", []):
        if r["naar"] not in elementen:
            res.fouten.append(f"{bid}: relatie naar '{r['naar']}', dat geen element is (of geen beoordeling heeft)")
            continue
        relatie, toegang = _relatie_archimate(r["soort"])
        naar_type = uitkomsten[r["naar"]]["archimate_type"]
        if not relatietool.archimate_geldig(relatie, van_type, naar_type):  # buiten het kennismodel: signaal
            res.fouten.append(f"{bid}: relatie '{r['soort']}' van {van_type} naar {naar_type} ('{r['naar']}') "
                              "is niet geldig in de ArchiMate-relatietabel")
        if relatie == "access":
            soort = relatietool.categorie(van_type)
            toegestaan = relatietool.HANDELINGEN if soort == "gedrag" else relatietool.VERANTWOORDELIJKHEDEN
            if toegang not in toegestaan:
                res.fouten.append(f"{bid}: toegang '{toegang}' vanuit {van_type}; kies uit {', '.join(toegestaan)}")
        if not r.get("bronnen") and not r.get("gemma_relatie"):   # het GGM is matchdoel, geen bron
            res.fouten.append(f"{bid}: relatie naar '{r['naar']}' zonder bronnen of gemma_relatie "
                              "(regel Elke claim een bron)")
        if r["ggm_match"] == "exact" and not r.get("ggm_relatie"):
            res.fouten.append(f"{bid}: relatie naar '{r['naar']}' met ggm_match exact zonder ggm_relatie")
    for naam, doel in ([("specialisatie", s.get("element")) for s in data.get("specialisaties", [])]
                       + [("homoniem", h.get("element")) for h in data.get("homoniemen", [])]
                       + [("tegenhanger", (data.get("tegenhanger") or {}).get("element"))]):
        if doel and doel not in elementen:
            res.fouten.append(f"{bid}: {naam} '{doel}' is geen element (of heeft geen beoordeling)")
    for dp in data.get("deelprocessen", []):
        u = uitkomsten.get(dp.get("begrip")) if dp.get("begrip") else None
        if dp.get("begrip") and (not u or u.get("soort") != "onderdeel"):
            res.fouten.append(f"{bid}: deelproces '{dp['begrip']}' is geen beoordeling van een deelproces zonder pagina")


def _controleer_gemma_relaties(ctx: Context, bid: str, data: dict, alle: dict[str, dict], res: Resultaat) -> None:
    """Een kenmerk of relatie die steunt op de plek in een GEMMA-indeling (`gemma_relatie`) in plaats van op een bron:
    de GEMMA-relatie moet in het model staan, tussen de gematchte elementen (regel Elke claim een bron)."""
    eigen = (data.get("gemma") or {}).get("id")
    gebruikt = [s for s, a in bepaal_type.antwoorden(data).items() if a.get("gemma_relatie")] \
        + [r["naar"] for r in data.get("relaties", []) if r.get("gemma_relatie")]
    if not gebruikt:
        return
    if not eigen:
        res.fouten.append(f"{bid}: gemma_relatie zonder GEMMA-match (gemma.id)")
        return
    model = ctx.gemma()["relaties"]
    for s, a in bepaal_type.antwoorden(data).items():
        for rid in a.get("gemma_relatie") or []:
            g = model.get(rid)
            if s not in bepaal_type.GEMMA_KENMERKEN or a["waarde"] != "ja":
                res.fouten.append(f"{bid}: gemma_relatie bij kenmerk {bepaal_type.NAAM[s]}; alleen bij 'ja' en bij "
                                  + ", ".join(bepaal_type.NAAM[k] for k in bepaal_type.GEMMA_KENMERKEN))
            elif g is None:
                res.fouten.append(f"{bid}: GEMMA-relatie {rid} bij {bepaal_type.NAAM[s]} staat niet in het GEMMA-model")
            elif g["doel"] != eigen or g["type"] not in ("aggregation-relationship", "composition-relationship"):
                res.fouten.append(f"{bid}: GEMMA-relatie {rid} bij {bepaal_type.NAAM[s]} is geen aggregatie of "
                                  "compositie naar de GEMMA-match van dit element")
        if s == "zelfstandige_specialisatie" and a.get("gemma_relatie") and any(
                g["bron"] == eigen and g["type"] == "specialization-relationship" for g in model.values()):
            res.fouten.append(f"{bid}: zelfstandige specialisatie op grond van GEMMA, maar de GEMMA-match "
                              "specialiseert in het model een ander element")
    for r in data.get("relaties", []):
        rid = r.get("gemma_relatie")
        if not rid:
            continue
        naar = ((alle.get(r["naar"]) or {}).get("gemma") or {}).get("id")
        g = model.get(rid)
        verwacht = f"{_relatie_archimate(r['soort'])[0]}-relationship"
        if g is None:
            res.fouten.append(f"{bid}: GEMMA-relatie {rid} naar '{r['naar']}' staat niet in het GEMMA-model")
        elif (g["bron"], g["doel"], g["type"]) != (eigen, naar, verwacht):
            res.fouten.append(f"{bid}: GEMMA-relatie {rid} is geen {r['soort']} van de GEMMA-match van dit element "
                              f"naar die van '{r['naar']}'")


def _controleer_gemma_functie(ctx: Context, bid: str, data: dict, uitkomst: dict, alle: dict[str, dict],
                              res: Resultaat) -> None:
    """`gemma_functie`: de plek van een functie of dienst in de GEMMA-functiehiërarchie, als het id van de bovenliggende
    GEMMA-functie. Ze steunt op de GEMMA-relatie van die functie naar de GEMMA-match van dit element, of op een bron
    met vindplaats (regel Elke claim een bron)."""
    f = data.get("gemma_functie")
    if not f:
        return
    if uitkomst.get("paginatype") not in ("bedrijfsfunctie", "dienst"):
        res.fouten.append(f"{bid}: gemma_functie hoort alleen bij een bedrijfsfunctie of dienst")
        return
    model = ctx.gemma()
    ouder = model["elementen"].get(f["id"])
    if ouder is None or ouder["type"] != "business-function":
        res.fouten.append(f"{bid}: gemma_functie '{f['id']}' is geen bedrijfsfunctie in het GEMMA-model "
                          "(zoek met tools/gemma.py functie)")
        return
    if bool(f.get("gemma_relatie")) == bool(f.get("bronnen")):
        res.fouten.append(f"{bid}: gemma_functie steunt op de GEMMA-relatie (gemma_relatie) of op bronnen met vindplaats, "
                          "niet op beide of geen van beide (regel Elke claim een bron)")
    elif f.get("bronnen") and not f.get("vindplaats"):
        res.fouten.append(f"{bid}: gemma_functie met bronnen zonder vindplaats (regel Elke claim een bron)")
    elif f.get("gemma_relatie"):
        eigen = (data.get("gemma") or {}).get("id")
        g = model["relaties"].get(f["gemma_relatie"])
        if not eigen:
            res.fouten.append(f"{bid}: gemma_functie met gemma_relatie zonder GEMMA-match (gemma.id)")
        elif g is None:
            res.fouten.append(f"{bid}: GEMMA-relatie {f['gemma_relatie']} bij gemma_functie staat niet in het GEMMA-model")
        elif (g["bron"], g["doel"]) != (f["id"], eigen) or g["type"] not in gemmatool_functieketen():
            res.fouten.append(f"{bid}: GEMMA-relatie {f['gemma_relatie']} is geen aggregatie van '{ouder['naam']}' "
                              "naar de GEMMA-match van dit element")
    if any(r["soort"] == "aggregatie" and r["naar"] == bid for d in alle.values()
           if (d.get("gemma") or {}).get("id") == f["id"] for r in d.get("relaties", [])):
        res.fouten.append(f"{bid}: '{ouder['naam']}' is een element van de wiki dat dit element al aggregeert: één plek "
                          "(laat gemma_functie weg)")


def gemmatool_functieketen() -> tuple[str, ...]:
    import gemma as gemmatool
    return gemmatool.FUNCTIEKETEN


def _zonder_grondslag(alle: dict[str, tuple[Path, dict]], nieuw: dict[str, dict], zonder: set[str]) -> None:
    """`beslist.zonder_grondslag`: een UPL-dienst zonder landelijke wettelijke grondslag (`signalen.zonder_grondslag`).
    De render meldt het op de pagina en zet haar op de lijst; de export laat haar weg."""
    for bid in alle:
        data = nieuw.get(bid, alle[bid][1])
        beslist = data.get("beslist")
        if beslist is None or bool(beslist.get("zonder_grondslag")) == (bid in zonder):
            continue
        beslist = {k: v for k, v in beslist.items() if k != "zonder_grondslag"}
        if bid in zonder:
            beslist["zonder_grondslag"] = True
        data = {**data, "beslist": beslist}
        if data == alle[bid][1]:
            nieuw.pop(bid, None)   # gelijk aan de beoordeling: niets te schrijven
        else:
            nieuw[bid] = data


def _terugmeldingen(ctx: Context, uitkomsten: dict[str, dict], res: Resultaat, rel: Path = TERUGMELDINGEN,
                    typen: tuple[str, ...] = TERUGMELDTYPEN, verplicht: tuple[str, ...] = ("domein", "bevinding"),
                    label: str = "terugmelding") -> dict | None:
    """Een register van terugmeldingen (GGM of procesarchitectuur): nummers geven, type, status en velden toetsen."""
    pad = ctx.wiki_root / rel
    if not pad.exists():
        return None
    register = beoordeling.laad(pad)
    meldingen = register.get("terugmeldingen", [])
    hoogste = max((m["nummer"] for m in meldingen if isinstance(m.get("nummer"), int)), default=0)
    for m in meldingen:
        if not isinstance(m.get("nummer"), int):
            hoogste += 1
            m["nummer"] = hoogste
            m.setdefault("status", "open")
        if m.get("type") not in typen:
            res.fouten.append(f"{label} {m['nummer']}: type '{m.get('type')}' (kies uit {', '.join(typen)})")
        if m.get("status") not in TERUGMELDSTATUS:
            res.fouten.append(f"{label} {m['nummer']}: status '{m.get('status')}' (kies uit {', '.join(TERUGMELDSTATUS)})")
        for veld in verplicht:
            if not m.get(veld):
                res.fouten.append(f"{label} {m['nummer']}: '{veld}' ontbreekt")
        b = m.get("bevinding")
        if b and not (isinstance(b, str) or (isinstance(b, list) and all(isinstance(a, str) and a for a in b))):
            res.fouten.append(f"{label} {m['nummer']}: 'bevinding' is een tekst of een lijst alinea's")
        elif b and m.get("status") == "open":
            # een open melding is leesbaar en bruikbaar: de bevinding en een voorstel elk in een eigen alinea
            alineas = [b] if isinstance(b, str) else b
            for kop in ("**Bevinding:**", "**Voorstel:**"):
                if not any(a.startswith(kop) for a in alineas):
                    res.fouten.append(f"{label} {m['nummer']}: een open melding heeft een alinea die begint met {kop}")
        for element in ([m["element"]] if m.get("element") else []) + list(m.get("elementen") or []):
            if (uitkomsten.get(element) or {}).get("soort") != "element":
                res.waarschuwingen.append(f"{label} {m['nummer']}: element '{element}' is (nog) geen element")
    nummers = [m["nummer"] for m in meldingen]
    if len(nummers) != len(set(nummers)):
        res.fouten.append(f"{label}en: een nummer komt dubbel voor")
    return register


def _objecten(alle: dict[str, tuple[Path, dict]], uitkomsten: dict[str, dict], res: Resultaat) -> None:
    """Het veld `object_van`: welk bestaand Archi-object een element voortzet na hernoemen, samenvoegen of splitsen.
    Een element zet hoogstens één object voort, een object wordt door hoogstens één element voortgezet, en een begrip
    dat nog een element is, geeft zijn object niet door."""
    objecten: dict[str, str] = {}
    for bid, (_, data) in alle.items():
        o = data.get("object_van")
        if not o or uitkomsten.get(bid) is None:
            continue
        naam = f"{bid}: object_van"
        if (uitkomsten.get(bid) or {}).get("soort") != "element":
            res.fouten.append(f"{naam}: '{bid}' is geen element")
        if (uitkomsten.get(o["id"]) or {}).get("soort") == "element":
            res.fouten.append(f"{naam}: '{o['id']}' is zelf nog een element en houdt zijn eigen object")
        if o["id"] in objecten:
            res.fouten.append(f"{naam}: het object van '{o['id']}' wordt al door '{objecten[o['id']]}' voortgezet")
        objecten[o["id"]] = bid


BESTANDSPAD = re.compile(r"(?<![\w./-])(?!ARCHITECTURE\.md\b)[\w./-]+\.(?:md|ya?ml|py|json)\b|\b(?:docs|tools|beoordelingen"
                         r"|besluiten|kennismodel|bronduidingen|onderwerpen|modellen|elementpaginas|sources|references|schemas|plannen|export)/[\w./-]*")


def _besluittekst(naam: str, besluit: dict, res: Resultaat) -> None:
    """Een besluittekst (en de stand) noemt een regel of sectie bij naam, nooit een bestandspad."""
    for veld in ("besluit", "stand"):
        pad = BESTANDSPAD.search(str(besluit.get(veld) or ""))
        if pad:
            res.fouten.append(f"{naam}: '{veld}' noemt het bestandspad '{pad.group(0)}'; noem de regel of de sectie "
                              "van ARCHITECTURE.md bij naam")


def _besluiten_onderwerp(oid: str, onderwerp: dict, begrippen: dict[str, str], res: Resultaat) -> None:
    """De besluiten van een onderwerp: over het onderwerp als geheel, of over een begrip zonder beoordeling (`begrip`).
    Elk besluit heeft een datum en een besluit; krijgt het begrip een beoordeling, dan hoort het besluit daar."""
    for i, b in enumerate(onderwerp.get("besluiten") or [], 1):
        naam = f"onderwerp {oid}, besluit {i}"
        if not isinstance(b, dict):
            res.fouten.append(f"{naam}: geen datum en besluit")
            continue
        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", str(b.get("datum") or "")):
            res.fouten.append(f"{naam}: 'datum' ontbreekt of is geen datum (jjjj-mm-dd)")
        if not b.get("besluit"):
            res.fouten.append(f"{naam}: 'besluit' ontbreekt")
        for veld in sorted(set(b) - {"datum", "besluit", "begrip", "zekerheid", "stand"}):
            res.fouten.append(f"{naam}: onbekend veld '{veld}'")
        if b.get("zekerheid", "logica") not in bepaal_type.ZEKERHEID:
            res.fouten.append(f"{naam}: zekerheid '{b['zekerheid']}' is niet een van {', '.join(bepaal_type.ZEKERHEID)}")
        if b.get("begrip") and str(b["begrip"]).lower() in begrippen:
            res.fouten.append(f"{naam}: '{b['begrip']}' heeft een beoordeling ({begrippen[str(b['begrip']).lower()]}); "
                              "zet het besluit daar (regel Letterlijk verplaatsen)")
        _besluittekst(naam, b, res)


def _beleidsdomeinen(ctx: Context, alle: dict[str, tuple[Path, dict]], uitkomsten: dict[str, dict], res: Resultaat) -> None:
    """Het register van beleidsdomeinen: de beschrijving van een beleidsdomein in de Beleidsdomeinindeling (de tekst van een vervallen taak). Elk beleidsdomein komt hoogstens één keer voor, wordt door
    een element gebruikt, heeft het taakveld van die elementen, een beschrijving en bestaande bronnen."""
    pad = ctx.wiki_root / BELEIDSDOMEINEN
    if not pad.exists():
        return
    gebruikt: dict[str, set[str]] = {}
    for bid, (_, data) in alle.items():
        if (uitkomsten.get(bid) or {}).get("soort") == "element" and data.get("beleidsdomein"):
            gebruikt.setdefault(data["beleidsdomein"], set()).add(data.get("taakveld") or "")
    gezien = set()
    for i, b in enumerate(beoordeling.laad(pad).get("beleidsdomeinen", []), 1):
        naam = f"beleidsdomeinen {i} ({b.get('beleidsdomein')})"
        for veld in ("beleidsdomein", "taakveld", "beschrijving", "bronnen"):
            if not b.get(veld):
                res.fouten.append(f"{naam}: '{veld}' ontbreekt")
        if b.get("beleidsdomein") in gezien:
            res.fouten.append(f"{naam}: staat al in het register")
        gezien.add(b.get("beleidsdomein"))
        if b.get("beleidsdomein") and b["beleidsdomein"] not in gebruikt:
            res.fouten.append(f"{naam}: geen element heeft dit beleidsdomein")
        elif b.get("taakveld") and gebruikt.get(b.get("beleidsdomein"), set()) - {b["taakveld"]}:
            res.fouten.append(f"{naam}: taakveld '{b['taakveld']}' wijkt af van dat van de elementen "
                              f"({', '.join(sorted(gebruikt[b['beleidsdomein']]))})")
        for bron in b.get("bronnen") or []:
            if gam_gemeen.bron_doel(ctx.wiki_root, bron) is None:
                res.fouten.append(f"{naam}: bron '{bron}' heeft geen bronduiding")


def _pa_terugmeldingen(ctx: Context, uitkomsten: dict[str, dict], res: Resultaat) -> dict | None:
    """Procesarchitectuur-terugmeldingen: het model mag afwijken van de UPL-indeling, mits teruggemeld."""
    register = _terugmeldingen(ctx, uitkomsten, res, PA_TERUGMELDINGEN, PA_TYPEN, ("bevinding",),
                               "procesarchitectuur-terugmelding")
    for m in (register or {}).get("terugmeldingen", []):
        if not m.get("elementen") and not m.get("beleidsdomein"):
            res.fouten.append(f"procesarchitectuur-terugmelding {m['nummer']}: noem 'elementen' of 'beleidsdomein'")
    return register


def _gemma_terugmeldingen(ctx: Context, uitkomsten: dict[str, dict], res: Resultaat) -> dict | None:
    """GEMMA-terugmeldingen: voorstellen aan het GEMMA-team over elementen, indelingen, definities en relaties van het
    GEMMA-model. Een melding noemt elementen van de wiki of GEMMA-elementen (`id` en
    `naam`, zoals in het GEMMA-model)."""
    register = _terugmeldingen(ctx, uitkomsten, res, GEMMA_TERUGMELDINGEN, GEMMA_TYPEN, ("bevinding",),
                               "GEMMA-terugmelding")
    gemma_model = gam_gemeen.model_json(ctx.wiki_root, "gemma").exists()
    for m in (register or {}).get("terugmeldingen", []):
        if not m.get("elementen") and not m.get("gemma_elementen"):
            res.fouten.append(f"GEMMA-terugmelding {m['nummer']}: noem 'elementen' of 'gemma_elementen'")
        for g in m.get("gemma_elementen") or []:
            if not isinstance(g, dict) or not g.get("id") or not g.get("naam"):
                res.fouten.append(f"GEMMA-terugmelding {m['nummer']}: een GEMMA-element heeft 'id' en 'naam'")
                continue
            if gemma_model:
                gevonden = ctx.gemma()["elementen"].get(g["id"])
                if not gevonden:
                    res.fouten.append(f"GEMMA-terugmelding {m['nummer']}: GEMMA-element '{g['id']}' bestaat niet")
                elif gevonden["naam"] != g["naam"]:
                    res.fouten.append(f"GEMMA-terugmelding {m['nummer']}: GEMMA-element '{g['id']}' heet "
                                      f"'{gevonden['naam']}', niet '{g['naam']}'")
    return register


def beslissen(wiki_root: Path = WIKI_ROOT, schrijven: bool = True) -> Resultaat:
    ctx = Context(wiki_root)
    res = Resultaat()
    alle = beoordeling.alle(wiki_root, ctx.wiki_yaml)
    validator = jsonschema.Draft202012Validator(ctx.schema)

    onderwerpen = gam_gemeen.afbakeningen(wiki_root)
    onderwerpnamen = sorted({o.get("naam", "").lower() for o in onderwerpen.values()} - {""}, key=len, reverse=True)
    uitkomsten: dict[str, dict | None] = {}
    for bid, (pad, data) in alle.items():
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", bid):
            res.fouten.append(f"{pad.name}: de bestandsnaam is het id (kleine letters, cijfers, koppeltekens)")
        regelvorm = bepaal_type.regelvorm(data)
        if regelvorm:
            res.fouten.append(f"{bid}: kenmerken in de schrijfvorm van één regel ({', '.join(regelvorm)}); draai "
                              f"tools/beoordeling.py normaliseer {bid}")
            uitkomsten[bid] = None
            continue
        schemafouten = [f"{bid}: {'/'.join(map(str, e.path)) or '(top)'}: {e.message}" for e in validator.iter_errors(data)]
        if schemafouten:
            res.fouten += schemafouten
            uitkomsten[bid] = None
            continue
        try:
            uitkomsten[bid] = asdict(bepaal_type.evalueer(data))
        except bepaal_type.BeoordelingFout as exc:
            res.fouten += [f"{bid}: {f}" for f in exc.fouten]
            uitkomsten[bid] = None

    res.fouten += [f"{f}" for f in bepaal_type.indeling({b: d for b, (_, d) in alle.items()}, uitkomsten)]

    nieuw: dict[str, dict] = {}
    for bid, (pad, data) in alle.items():
        uitkomst = uitkomsten[bid]
        if uitkomst is None:
            continue
        open_todo = sjablonen.open_todo(data)
        if open_todo:
            res.fouten.append(f"{bid}: nog een TODO uit een sjabloon in {', '.join(open_todo[:4])}"
                              f"{' …' if len(open_todo) > 4 else ''} ({len(open_todo)}); vul de onderbouwing in")
        bronnen = bronnen_van(data)
        _controleer_bronnen(ctx, bid, bronnen, res)
        modelbronnen = sorted({b for a in [*bepaal_type.antwoorden(data).values(), *data.get("relaties", []),
                                           data.get("gemma_functie") or {}]
                               for b in a.get("bronnen") or [] if ctx.brontype(b) == "model"})
        if modelbronnen:
            res.waarschuwingen.append(f"{bid}: {', '.join(modelbronnen)} is een model, matchdoel en geen bron; noem bij "
                                      "het kenmerk of de relatie de bron van de bewering (regel Bronvoorrang)")
        zonder_bron = [bepaal_type.NAAM[s] for s, a in bepaal_type.antwoorden(data).items()
                       if a["waarde"] == "ja" and not a.get("bronnen") and not a.get("gemma_relatie")]
        if zonder_bron:
            res.fouten.append(f"{bid}: kenmerk 'ja' zonder bron: {', '.join(zonder_bron)} (regel Elke claim een bron)")
        if pad.parent.parent.name != gam_gemeen.thuis(data):
            res.fouten.append(f"{bid}: het thuisonderwerp is '{gam_gemeen.thuis(data)}' (het eerste in onderwerpen) en de "
                              f"beoordeling staat in de map van '{pad.parent.parent.name}' (regel Thuishoren)")
        for onderwerp in data["onderwerpen"]:
            if onderwerp not in onderwerpen:
                res.fouten.append(f"{bid}: onderwerp '{onderwerp}' heeft geen {gam_gemeen.afbakening_pad(onderwerp).as_posix()}")
        ggm_sterkte = (data.get("ggm") or {}).get("sterkte")
        redenen = bepaal_type.voor_te_leggen(uitkomst, ggm_sterkte)
        beslist = {"uitkomst": uitkomst, "voor_te_leggen": redenen, "open": [],
                    "bronnen": bronnen, "herkomst": herkomst(ctx, bronnen)}
        status = None
        if uitkomst["soort"] == "element":
            if not bronnen:
                res.fouten.append(f"{bid}: element zonder bron (regel Elke claim een bron)")
            _controleer_element(ctx, bid, data, uitkomst, res)
            _controleer_verwijzingen(bid, data, uitkomsten, res, {b: d["begrip"] for b, (_, d) in alle.items()})
            _controleer_gemma_relaties(ctx, bid, data, {b: d for b, (_, d) in alle.items()}, res)
            _controleer_gemma_functie(ctx, bid, data, uitkomst, {b: d for b, (_, d) in alle.items()}, res)
            beslist.update(_modelvelden(ctx, bid, data, res))
            beslist.update(_kwaliteitsdoelen(ctx, bid, data, uitkomst, res))
            status = bepaal_type.voorgestelde_status(uitkomst, ggm_sterkte, data.get("besluiten"))
            if status != "afgewezen":
                beslist["pad"] = pagina_pad(ctx, uitkomst["paginatype"], data, bid)
            if data.get("status") == "goedgekeurd" and status == "review" \
                    and beoordeling.goedgekeurd_in_log(ctx.log, bid, data):
                status = "goedgekeurd"
        beslist["open"] = bepaal_type.open_redenen(redenen, status, data.get("besluiten"))
        for i, b in enumerate(data.get("besluiten") or [], 1):
            _besluittekst(f"{bid}: besluit {i}", b, res)
        res.waarschuwingen += signalen.per_begrip(bid, data, uitkomst, onderwerpnamen, beslist)
        res.uitkomsten[bid] = {"soort": uitkomst["soort"], "paginatype": uitkomst.get("paginatype"),
                               "procesniveau": uitkomst.get("procesniveau"), "status": status, "open": beslist["open"]}
        bijgewerkt = beoordeling.inhoud(data)
        if status:
            bijgewerkt["status"] = status
        bijgewerkt["beslist"] = _schoon(beslist)
        if bijgewerkt != data:
            nieuw[bid] = bijgewerkt

    paden = {}
    for bid, d in [(b, nieuw.get(b, alle[b][1])) for b in alle]:
        pad = (d.get("beslist") or {}).get("pad")
        if pad and pad in paden:
            res.fouten.append(f"{bid}: zelfde paginapad als '{paden[pad]}' ({pad})")
        paden[pad] = bid

    pa_register = _pa_terugmeldingen(ctx, uitkomsten, res)
    gemma_register = _gemma_terugmeldingen(ctx, uitkomsten, res)
    gemeld = [m for m in (pa_register or {}).get("terugmeldingen", []) if m.get("status") != "afgewezen"]
    elementen = {b: u for b, u in uitkomsten.items()   # een vervallen element (besluit afwijzen) telt niet mee
                 if u and u["soort"] == "element" and not bepaal_type.is_afgewezen(alle[b][1])}
    brontype = lambda i: gam_gemeen.brontype(wiki_root, i)  # noqa: E731
    zonder = signalen.zonder_grondslag({b: nieuw.get(b, alle[b][1]) for b in alle}, elementen, brontype)
    _zonder_grondslag(alle, nieuw, zonder)
    res.waarschuwingen += signalen.over_begrippen({b: d for b, (_, d) in alle.items()}, uitkomsten,
                                                  {e for m in gemeld if m["type"] == "kennismodel" for e in m.get("elementen") or []},
                                                  zonder)
    res.waarschuwingen += signalen.kennismodel({b: d for b, (_, d) in alle.items()}, uitkomsten, zonder)
    res.waarschuwingen += signalen.modulariteit({b: d for b, (_, d) in alle.items()}, uitkomsten, onderwerpen, zonder)
    res.waarschuwingen += signalen.zonder_grondslag_terugmelding(zonder, gemeld)
    functies = [b for b, u in elementen.items() if u["paginatype"] == "bedrijfsfunctie"]
    if any(u["paginatype"] in ("bedrijfsfunctie", "product", "dienst") for u in elementen.values()):
        gekoppeld = any((alle[b][1].get("gemma") or {}).get("id") for b in functies) \
            or any(alle[b][1].get("gemma_functie") for b in elementen)
        res.waarschuwingen += signalen.functie_indeling(
            {b: d for b, (_, d) in alle.items()}, elementen,
            [(van, r) for van in elementen for r in alle[van][1].get("relaties", [])], ctx.gemma() if gekoppeld else {})
    _objecten(alle, uitkomsten, res)
    _beleidsdomeinen(ctx, alle, uitkomsten, res)
    begripnamen = {d["begrip"].lower(): b for b, (_, d) in alle.items()}
    for oid, onderwerp in onderwerpen.items():
        if onderwerp.get("niveau") not in gam_gemeen.NIVEAUS:
            res.fouten.append(f"onderwerp {oid}: niveau '{onderwerp.get('niveau')}'; kies {', '.join(gam_gemeen.NIVEAUS)} "
                              "(regel Thuishoren)")
        _besluiten_onderwerp(oid, onderwerp, begripnamen, res)
    if any(u["paginatype"] in ("product", "dienst") for u in elementen.values()) \
            and gam_gemeen.model_json(wiki_root, "gemma").exists():
        res.waarschuwingen += signalen.domein_en_beleidsdomein({b: d for b, (_, d) in alle.items()}, elementen,
                                                              ctx.gemma(), gemeld)
    res.fouten += signalen.bronduidingen(wiki_root, onderwerpen) + signalen.modelbestanden(wiki_root)
    res.fouten += signalen.citaten(wiki_root)
    fouten, waarschuwingen = signalen.wettelijke_grondslag({b: nieuw.get(b, alle[b][1]) for b in alle}, elementen, brontype)
    res.fouten += fouten
    res.waarschuwingen += waarschuwingen
    register = _terugmeldingen(ctx, uitkomsten, res)
    if res.fouten:
        return res
    if not schrijven:
        res.gewijzigd = sorted(nieuw)  # wat een run met schrijven zou bijwerken: niet leeg = beslist is verouderd
        return res
    for bid, data in nieuw.items():
        beoordeling.schrijf(alle[bid][0], data)
        res.gewijzigd.append(bid)
    for reg, rel in ((register, TERUGMELDINGEN), (pa_register, PA_TERUGMELDINGEN), (gemma_register, GEMMA_TERUGMELDINGEN)):
        if reg is None:
            continue
        pad = wiki_root / rel
        kop = "".join(r + "\n" for r in pad.read_text(encoding="utf-8").splitlines() if r.startswith("#"))
        tekst = kop + beoordeling.dump(reg)
        if tekst != pad.read_text(encoding="utf-8"):
            pad.write_text(tekst, encoding="utf-8", newline="\n")
            res.gewijzigd.append(str(rel))
    return res


def compact(waarschuwingen: list[str], gewijzigd: list[str], alles: bool = False) -> list[str]:
    """De regels die de run toont: alle met `alles`, anders die over een in deze run gewijzigde beoordeling en een
    telling van de rest per regel (de laatste term tussen haakjes). De volledige lijst blijft op te vragen."""
    if alles:
        return [f"waarschuwing: {w}" for w in waarschuwingen]
    uit = [f"waarschuwing: {w}" for w in waarschuwingen if w.split(":", 1)[0] in gewijzigd]
    rest = [w for w in waarschuwingen if w.split(":", 1)[0] not in gewijzigd]
    if rest:
        telling: dict[str, int] = {}
        for w in rest:
            m = re.search(r"\(([^()]*)\)\s*$", w)
            telling[m.group(1) if m else "overig"] = telling.get(m.group(1) if m else "overig", 0) + 1
        uit.append(f"{len(rest)} andere waarschuwing(en), per regel: "
                   + "; ".join(f"{k} {n}" for k, n in sorted(telling.items(), key=lambda x: -x[1]))
                   + " (alles tonen: --alles)")
    return uit


def eigen(melding: str, ids: set[str]) -> bool:
    """Gaat de melding over een van deze beoordelingen (`<id>: …` of `<id>.yaml: …`)?"""
    kop = melding.split(":", 1)[0]
    return kop in ids or kop.removesuffix(".yaml") in ids


def alleen(res: Resultaat, ids: list[str], bekend: set[str]) -> list[str]:
    """De uitvoer van `--alleen`: fouten, waarschuwingen en uitkomst van deze beoordelingen, en een telling van de rest."""
    uit = [f"fout: '{i}' is geen beoordeling" for i in ids if i not in bekend]
    gekozen = set(ids)
    uit += [f"fout: {f}" for f in res.fouten if eigen(f, gekozen)]
    uit += [f"waarschuwing: {w}" for w in res.waarschuwingen if eigen(w, gekozen)]
    for i in ids:
        u = res.uitkomsten.get(i)
        if u:
            soort = " ".join(filter(None, [u["soort"], u["paginatype"], u["procesniveau"]]))
            uit.append(f"{i}: {soort}" + (f", {u['status']}" if u["status"] else "")
                       + (f"; open: {'; '.join(u['open'])}" if u["open"] else ""))
    rest = [f for f in res.fouten if not eigen(f, gekozen)]
    if rest:
        uit.append(f"{len(rest)} fout(en) bij andere beoordelingen of registers, niet getoond.")
    return uit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--zonder-render", action="store_true", help="Alleen beslissen, geen pagina's maken")
    parser.add_argument("--alles", action="store_true",
                        help="Alle waarschuwingen tonen (standaard: die van de gewijzigde beoordelingen, plus een telling)")
    parser.add_argument("--alleen", nargs="+", metavar="ID",
                        help="Alleen deze beoordelingen controleren; er wordt niets geschreven of gerenderd")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.alleen:
        res = beslissen(args.wiki, schrijven=False)
        uit = alleen(res, args.alleen, set(beoordeling.alle(args.wiki, paths.load_wiki_yaml(args.wiki))))
        print("\n".join(uit))
        return 1 if any(r.startswith("fout:") for r in uit) else 0
    res = beslissen(args.wiki)
    for f in res.fouten:
        print(f"fout: {f}")
    for w in compact(res.waarschuwingen, res.gewijzigd, args.alles):
        print(w)
    if res.fouten:
        print(f"{len(res.fouten)} fout(en): er is niets geschreven.")
        return 1
    print(f"Beslist: {len(res.gewijzigd)} bestand(en) bijgewerkt.")
    if not args.zonder_render:
        import render
        return render.main(["--wiki", str(args.wiki)])
    return 0


if __name__ == "__main__":
    sys.exit(main())
