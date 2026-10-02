"""Afleiden: van het oordeel van de AI naar type, status en modelgegevens, met harde controles.

Leest elke beoordeling in `beoordelingen/begrippen/<id>.yaml` (het oordeel van de AI) en vult per beoordeling:
- `afgeleid.uitkomst`: de uitkomst van de beslistabel (tools/bepaal_type.py) uit de kenmerken;
- `afgeleid.voor_te_leggen` en `afgeleid.open`: waarom de redacteur moet beslissen, en wat geen besluit dekt;
- `status` (alleen bij een element): `kandidaat` als er iets open staat, anders `review`; `afgewezen` na het besluit
  `afwijzen`. `goedgekeurd` blijft staan zolang `log.md` een promotieregel met de hash van de inhoud heeft; zet
  alleen `llmwiki promote` (na akkoord). Elke inhoudelijke wijziging maakt een goedgekeurd element weer `review`;
- `afgeleid.pad`: waar het render-script de pagina zet (map uit wiki.yaml, submappen taakveld en beleidsdomein);
- `afgeleid.ggm`, `afgeleid.ggm_duplicaten`, `afgeleid.gemma`: de letterlijke velden bij de match die de AI koos
  (tools/ggm.py, tools/gemma.py); de AI vult die nooit zelf;
- `afgeleid.bronnen` en `afgeleid.herkomst`: alle bronnen van het begrip, en het brontype van de hoogste.
Nieuwe GGM-terugmeldingen in `beoordelingen/terugmeldingen.yaml` krijgen het volgende nummer.

Harde controles (fout: er wordt niets geschreven): schema, kenmerken, verplichte velden van een element, bestaan van
bronnen (met bronanalyse), GGM-guid, GEMMA-id, doelen van relaties, specialisaties, tegenhanger en homoniemen, de
ArchiMate-relatietabel, de bronanalyses en de gegenereerde modelmappen. Zachte signalen (waarschuwingen, met de naam
van de regel) staan in tools/signalen.py. Daarna draait het render-script (tools/render.py), tenzij `--zonder-render`.

Gebruik (vanuit de wikimap):
    uv run python tools/afleiden.py [--zonder-render]
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
import signalen  # noqa: E402
from llmwiki import beoordeling, frontmatter, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TERUGMELDINGEN = Path("beoordelingen") / "terugmeldingen.yaml"
ONDERWERPEN = Path("beoordelingen") / "onderwerpen"
TERUGMELDTYPEN = ("hiaat", "definitie", "structuur", "scope", "duplicaat", "homoniem", "relatie")
TERUGMELDSTATUS = ("open", "gemeld", "opgelost", "afgewezen")


@dataclass
class Resultaat:
    fouten: list[str] = field(default_factory=list)
    waarschuwingen: list[str] = field(default_factory=list)
    gewijzigd: list[str] = field(default_factory=list)


def slug(tekst: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")


def _schoon(obj):
    """Laat lege waarden weg (None, '', [], {}), zodat `afgeleid` kort en stabiel blijft."""
    if isinstance(obj, dict):
        return {k: _schoon(v) for k, v in obj.items() if v is not None and v != "" and v != [] and v != {}}
    if isinstance(obj, list):
        return [_schoon(v) for v in obj]
    return obj


class Context:
    """Wat afleiden nodig heeft van buiten de beoordeling: wiki.yaml, bronnen, GGM, GEMMA, log."""

    def __init__(self, wiki_root: Path):
        self.wiki_root = wiki_root
        self.wiki_yaml = paths.load_wiki_yaml(wiki_root)
        self.repo_root = paths.find_repo_root(wiki_root)
        self.schema = json.loads((wiki_root / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
        log = wiki_root / "log.md"
        self.log = log.read_text(encoding="utf-8") if log.exists() else ""
        self._ggm = self._gemma = None
        self._brontypen: dict[str, str | None] = {}

    def ggm(self) -> dict:
        if self._ggm is None:
            import ggm
            self._ggm = ggm.laad(self.wiki_root / "ggm" / "ggm_parsed.json")
        return self._ggm

    def gemma(self) -> dict:
        if self._gemma is None:
            import gemma
            self._gemma = gemma.laad(self.wiki_root / "gemma" / "gemma_parsed.json")
        return self._gemma

    def brontype(self, bron_id: str) -> str | None:
        """brontype uit sources/index; None als de bron niet bestaat."""
        if bron_id not in self._brontypen:
            pad = self.repo_root / "sources" / "index" / f"{bron_id}.md"
            self._brontypen[bron_id] = (frontmatter.read(pad).meta.get("brontype") or "overig") if pad.exists() else None
        return self._brontypen[bron_id]


def bronnen_van(data: dict) -> list[str]:
    """Alle bronnen van een beoordeling, in volgorde: expliciet, kenmerken, relaties, formele definitie."""
    ids = list(data.get("bronnen", []))
    for antwoord in data.get("kenmerken", {}).values():
        ids += antwoord.get("bronnen", [])
    for r in data.get("relaties", []):
        ids += r.get("bronnen", [])
    if data.get("definitie_formeel_bron"):
        ids.append(data["definitie_formeel_bron"]["bron"])
    return list(dict.fromkeys(ids))


def pagina_pad(ctx: Context, paginatype: str, data: dict, beoordeling_id: str) -> str:
    definitie = ctx.wiki_yaml["page_types"][paginatype]
    delen = [definitie["dir"]] + [slug(data[s]) for s in definitie.get("submappen", []) if data.get(s)]
    return "/".join(delen + [f"{beoordeling_id}.md"])


def _relatie_archimate(soort: str) -> tuple[str, str | None]:
    """'toegang (registreren)' → ('access', 'registreren'); 'associatie (gericht)' → ('association', None)."""
    m = re.match(r"^(\w+)(?: \((.+)\))?$", soort)
    naam, toevoeging = m.group(1), m.group(2)
    return relatietool.RELATIES[naam], (toevoeging if naam == "toegang" else None)


def _controleer_element(ctx: Context, bid: str, data: dict, uitkomst: dict, res: Resultaat) -> None:
    paginatype = uitkomst["paginatype"]
    for veld in ("definitie", "beschrijving", "grondslag", "gemma"):
        if not data.get(veld):
            res.fouten.append(f"{bid}: element zonder '{veld}'")
    for veld in ctx.wiki_yaml["page_types"][paginatype].get("submappen", []):
        if not data.get(veld):
            res.fouten.append(f"{bid}: {paginatype} zonder '{veld}' (bepaalt de map)")
    if uitkomst.get("data_object") == "ja" or paginatype in ("bedrijfsobject", "product"):
        if not data.get("ggm"):
            res.fouten.append(f"{bid}: {paginatype} zonder GGM-match ('ggm', ook bij sterkte geen)")
    for onderwerp in data.get("per_onderwerp", {}):
        if onderwerp not in data["onderwerpen"]:
            res.fouten.append(f"{bid}: per_onderwerp '{onderwerp}' staat niet in onderwerpen")
    if data.get("grondslag") in ("regelgeving", "procesobject", "ggm-afgeleid") and not data.get("grondslag_toelichting"):
        res.fouten.append(f"{bid}: grondslag {data['grondslag']} zonder grondslag_toelichting")


def _modelvelden(ctx: Context, bid: str, data: dict, res: Resultaat) -> dict:
    import gemma as gemmatool
    import ggm as ggmtool

    afgeleid = {}
    ggm_keuze = data.get("ggm") or {}
    if ggm_keuze.get("guid"):
        treffers = ggmtool.zoek_entiteit(ctx.ggm(), ggm_keuze["guid"])
        if treffers:
            afgeleid["ggm"] = ggmtool.velden(treffers[0])
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
    afgeleid["ggm_duplicaten"] = duplicaten
    gemma_keuze = data.get("gemma") or {}
    if gemma_keuze.get("id"):
        treffers = gemmatool.zoek_element(ctx.gemma(), gemma_keuze["id"])
        if treffers:
            afgeleid["gemma"] = gemmatool.velden(treffers[0])
        else:
            res.fouten.append(f"{bid}: GEMMA-id {gemma_keuze['id']} bestaat niet in het GEMMA-model")
    elif gemma_keuze and gemma_keuze.get("sterkte") != "geen":
        res.fouten.append(f"{bid}: GEMMA-match '{gemma_keuze.get('sterkte')}' zonder id")
    return afgeleid


def _controleer_bronnen(ctx: Context, bid: str, bronnen: list[str], res: Resultaat) -> None:
    for bron_id in bronnen:
        if ctx.brontype(bron_id) is None:
            res.fouten.append(f"{bid}: bron {bron_id} staat niet in sources/index")
        elif gam_gemeen.bron_doel(ctx.wiki_root, bron_id) is None:
            res.fouten.append(f"{bid}: bron {bron_id} heeft geen bronanalyse (of, bij een modelbron, geen tekst in sources/raw)")


def herkomst(ctx: Context, bronnen: list[str]) -> str | None:
    volgorde = ctx.wiki_yaml.get("bronvoorrang", [])
    typen = [ctx.brontype(b) for b in bronnen if ctx.brontype(b) in volgorde]
    return min(typen, key=volgorde.index) if typen else None


def _controleer_verwijzingen(bid: str, data: dict, uitkomsten: dict[str, dict], res: Resultaat) -> None:
    elementen = {i for i, u in uitkomsten.items() if u and u.get("soort") == "element"}
    van_type = uitkomsten[bid]["archimate_type"]
    for r in data.get("relaties", []):
        if r["naar"] not in elementen:
            res.fouten.append(f"{bid}: relatie naar '{r['naar']}', dat geen element is (of geen beoordeling heeft)")
            continue
        relatie, toegang = _relatie_archimate(r["soort"])
        naar_type = uitkomsten[r["naar"]]["archimate_type"]
        if not relatietool.toegestaan(relatie, van_type, naar_type):
            res.fouten.append(f"{bid}: relatie '{r['soort']}' van {van_type} naar {naar_type} ('{r['naar']}') "
                              "past niet in de ArchiMate-relatietabel")
        if relatie == "access":
            soort = relatietool.categorie(van_type)
            toegestaan = relatietool.HANDELINGEN if soort == "gedrag" else relatietool.VERANTWOORDELIJKHEDEN
            if toegang not in toegestaan:
                res.fouten.append(f"{bid}: toegang '{toegang}' vanuit {van_type}; kies uit {', '.join(toegestaan)}")
        if r["grondslag"] == "bron" and not r.get("bronnen"):
            res.fouten.append(f"{bid}: relatie naar '{r['naar']}' met grondslag bron zonder bronnen")
    for naam, doel in ([("specialisatie", s.get("element")) for s in data.get("specialisaties", [])]
                       + [("homoniem", h.get("element")) for h in data.get("homoniemen", [])]
                       + [("tegenhanger", (data.get("tegenhanger") or {}).get("element"))]):
        if doel and doel not in elementen:
            res.fouten.append(f"{bid}: {naam} '{doel}' is geen element (of heeft geen beoordeling)")


def _terugmeldingen(ctx: Context, uitkomsten: dict[str, dict], res: Resultaat) -> dict | None:
    pad = ctx.wiki_root / TERUGMELDINGEN
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
        if m.get("type") not in TERUGMELDTYPEN:
            res.fouten.append(f"terugmelding {m['nummer']}: type '{m.get('type')}' (kies uit {', '.join(TERUGMELDTYPEN)})")
        if m.get("status") not in TERUGMELDSTATUS:
            res.fouten.append(f"terugmelding {m['nummer']}: status '{m.get('status')}' (kies uit {', '.join(TERUGMELDSTATUS)})")
        for veld in ("domein", "bevinding"):
            if not m.get(veld):
                res.fouten.append(f"terugmelding {m['nummer']}: '{veld}' ontbreekt")
        if m.get("element") and (uitkomsten.get(m["element"]) or {}).get("soort") != "element":
            res.waarschuwingen.append(f"terugmelding {m['nummer']}: element '{m['element']}' is (nog) geen element")
    nummers = [m["nummer"] for m in meldingen]
    if len(nummers) != len(set(nummers)):
        res.fouten.append("terugmeldingen: een nummer komt dubbel voor")
    return register


def afleiden(wiki_root: Path = WIKI_ROOT, schrijven: bool = True) -> Resultaat:
    ctx = Context(wiki_root)
    res = Resultaat()
    alle = beoordeling.alle(wiki_root, ctx.wiki_yaml)
    validator = jsonschema.Draft202012Validator(ctx.schema)

    onderwerpen = {p.stem: beoordeling.laad(p) for p in sorted((wiki_root / ONDERWERPEN).glob("*.yaml"))}
    onderwerpnamen = sorted({o.get("naam", "").lower() for o in onderwerpen.values()} - {""}, key=len, reverse=True)
    uitkomsten: dict[str, dict | None] = {}
    for bid, (pad, data) in alle.items():
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", bid):
            res.fouten.append(f"{pad.name}: de bestandsnaam is het id (kleine letters, cijfers, koppeltekens)")
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

    nieuw: dict[str, dict] = {}
    for bid, (pad, data) in alle.items():
        uitkomst = uitkomsten[bid]
        if uitkomst is None:
            continue
        bronnen = bronnen_van(data)
        _controleer_bronnen(ctx, bid, bronnen, res)
        zonder_bron = [bepaal_type.NAAM[s] for s, a in data["kenmerken"].items() if a["waarde"] == "ja" and not a.get("bronnen")]
        if zonder_bron:
            res.fouten.append(f"{bid}: kenmerk 'ja' zonder bron: {', '.join(zonder_bron)} (regel Elke claim een bron)")
        for onderwerp in data["onderwerpen"]:
            if onderwerp not in onderwerpen:
                res.fouten.append(f"{bid}: onderwerp '{onderwerp}' heeft geen {ONDERWERPEN.as_posix()}/{onderwerp}.yaml")
        ggm_sterkte = (data.get("ggm") or {}).get("sterkte")
        redenen = bepaal_type.voor_te_leggen(uitkomst, ggm_sterkte, data.get("grondslag"))
        afgeleid = {"uitkomst": uitkomst, "voor_te_leggen": redenen,
                    "open": bepaal_type.open_redenen(redenen, data.get("besluiten")),
                    "bronnen": bronnen, "herkomst": herkomst(ctx, bronnen)}
        status = None
        if uitkomst["soort"] == "element":
            if not bronnen:
                res.fouten.append(f"{bid}: element zonder bron (regel Elke claim een bron)")
            _controleer_element(ctx, bid, data, uitkomst, res)
            _controleer_verwijzingen(bid, data, uitkomsten, res)
            afgeleid.update(_modelvelden(ctx, bid, data, res))
            status = bepaal_type.voorgestelde_status(uitkomst, ggm_sterkte, data.get("grondslag"), data.get("besluiten"))
            if status != "afgewezen":
                afgeleid["pad"] = pagina_pad(ctx, uitkomst["paginatype"], data, bid)
            if data.get("status") == "goedgekeurd" and status == "review" \
                    and beoordeling.goedgekeurd_in_log(ctx.log, bid, data):
                status = "goedgekeurd"
        res.waarschuwingen += signalen.per_begrip(bid, data, uitkomst, onderwerpnamen, afgeleid)
        bijgewerkt = beoordeling.inhoud(data)
        if status:
            bijgewerkt["status"] = status
        bijgewerkt["afgeleid"] = _schoon(afgeleid)
        if bijgewerkt != data:
            nieuw[bid] = bijgewerkt

    paden = {}
    for bid, d in [(b, nieuw.get(b, alle[b][1])) for b in alle]:
        pad = (d.get("afgeleid") or {}).get("pad")
        if pad and pad in paden:
            res.fouten.append(f"{bid}: zelfde paginapad als '{paden[pad]}' ({pad})")
        paden[pad] = bid

    res.waarschuwingen += signalen.over_begrippen({b: d for b, (_, d) in alle.items()}, uitkomsten)
    res.fouten += signalen.bronanalyses(wiki_root, onderwerpen) + signalen.modelmappen(wiki_root)
    register = _terugmeldingen(ctx, uitkomsten, res)
    if res.fouten:
        return res
    if not schrijven:
        res.gewijzigd = sorted(nieuw)  # wat een run met schrijven zou bijwerken: niet leeg = afgeleid is verouderd
        return res
    for bid, data in nieuw.items():
        beoordeling.schrijf(alle[bid][0], data)
        res.gewijzigd.append(bid)
    if register is not None:
        pad = wiki_root / TERUGMELDINGEN
        kop = "".join(r + "\n" for r in pad.read_text(encoding="utf-8").splitlines() if r.startswith("#"))
        tekst = kop + beoordeling.dump(register)
        if tekst != pad.read_text(encoding="utf-8"):
            pad.write_text(tekst, encoding="utf-8", newline="\n")
            res.gewijzigd.append(str(TERUGMELDINGEN))
    return res


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--zonder-render", action="store_true", help="Alleen afleiden, geen pagina's maken")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    res = afleiden(args.wiki)
    for f in res.fouten:
        print(f"fout: {f}")
    for w in res.waarschuwingen:
        print(f"waarschuwing: {w}")
    if res.fouten:
        print(f"{len(res.fouten)} fout(en): er is niets geschreven.")
        return 1
    print(f"Afgeleid: {len(res.gewijzigd)} bestand(en) bijgewerkt.")
    if not args.zonder_render:
        import render
        return render.main(["--wiki", str(args.wiki)])
    return 0


if __name__ == "__main__":
    sys.exit(main())
