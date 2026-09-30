"""Domeincontroles voor gemma-archimate-model: het uitbreidingspunt van VALIDATE.

Alles wat telbaar of structureel is, controleert deze tool; het model beoordeelt alleen wat
betekenis vraagt (bij een 'waarschuwing'). De controle kijkt naar de wiki zoals die na de run
zou zijn: werkboom plus de gestagede pagina's van de run.

Gebruik (vanuit de wikimap):
    uv run python tools/check_elementen.py --run <run-id> [--rapport .work/runs/<run-id>/validation-report.json]
    uv run python tools/check_elementen.py            # hele werkboom
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bepaal_type  # noqa: E402
import gam_gemeen  # noqa: E402
import relaties as rel_tool  # noqa: E402
from llmwiki import frontmatter, paths, runs, sources  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
VERBODEN_ZINNEN = ("structureel buiten scope", "structureel out-of-scope", "structureel geen ggm-match",
                   "per definitie", "ggm modelleert nooit")
TECHNISCHE_DOELEN = ("AGENTS.md", "ARCHITECTURE.md", ".agents/", "tools/", "schemas/")
REGISTR_RE = re.compile(r"\b\w*registr\w*", re.IGNORECASE)


@dataclass
class Bevinding:
    naam: str
    doel: str
    ernst: str  # fout | waarschuwing
    melding: str


def slug(tekst: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")


# --- De wiki zoals die na de run zou zijn ---


def _changeset(wiki_root: Path, run_id: str) -> dict:
    rdir = runs.run_dir(wiki_root, run_id)
    for naam in ("changeset.json", "changeset-concept.json"):
        if (rdir / naam).exists():
            return json.loads((rdir / naam).read_text(encoding="utf-8"))
    return {"paginas": []}


def effectieve_paginas(wiki_root: Path, run_id: str | None) -> tuple[dict[Path, frontmatter.Page], set[Path]]:
    """{doelpad: pagina} voor alle Markdown-pagina's, met de gestagede versies; plus de paden uit de run."""
    paginas: dict[Path, frontmatter.Page] = {}
    for pad in wiki_root.rglob("*.md"):
        rel = pad.relative_to(wiki_root).parts
        if rel[0] in (".work", ".agents", "voorstellen", "tools", "schemas", "ggm", "gemma") or rel[0].startswith("."):
            continue
        if pad.name in ("AGENTS.md", "ARCHITECTURE.md", "log.md", "voortgang.md"):
            continue
        paginas[pad.resolve()] = frontmatter.read(pad)
    in_run: set[Path] = set()
    if run_id:
        rdir = runs.run_dir(wiki_root, run_id)
        for p in _changeset(wiki_root, run_id)["paginas"]:
            doel = (wiki_root / p["pad"]).resolve()
            paginas[doel] = frontmatter.read(rdir / "changeset" / p["staged_bestand"])
            in_run.add(doel)
    return paginas, in_run


class Wiki:
    def __init__(self, wiki_root: Path, run_id: str | None):
        self.root = wiki_root.resolve()
        self.yaml = paths.load_wiki_yaml(wiki_root)
        self.paginas, self.in_run = effectieve_paginas(wiki_root, run_id)
        self.types = self.yaml.get("page_types", {})
        self.elementtypen = gam_gemeen.element_types(self.yaml)
        self.elementen = [
            gam_gemeen.Element(pad, p.meta.get("type"), p.meta, p.body)
            for pad, p in self.paginas.items() if p.meta.get("type") in self.elementtypen
        ]
        self.op_id = {}
        for el in self.elementen:
            self.op_id.setdefault(el.id, []).append(el)
        self.op_pad = {el.pad: el.id for el in self.elementen}
        self.repo_root = paths.find_repo_root(wiki_root)
        self.modelbronnen = {self.yaml.get("ggm", {}).get("bron"), self.yaml.get("gemma", {}).get("bron")} - {None}
        # Een bron kan in meer onderwerpen een bronanalyse hebben (bijv. de Awb bij lijkbezorging en participatie).
        self.analyse_paden: dict[str, set[Path]] = {}
        for pad, p in self.van_type("bronanalyse"):
            self.analyse_paden.setdefault(p.meta.get("id"), set()).add(pad)

    def bron_doel(self, bron_id: str) -> Path | None:
        """Waar een verwijzing naar een bron heen linkt: de bronanalyse, of bij een modelbron de tekst in sources/raw/."""
        if bron_id in self.modelbronnen:
            pad = (self.repo_root / "sources" / "raw" / f"{bron_id}.md").resolve()
            return pad if pad.exists() else None
        paden = self.analyse_paden.get(bron_id)
        return min(paden) if paden else None

    def bron_doelen(self, bron_id: str) -> set[Path]:
        """Alle toegestane doelen van een link naar deze bron: elke bronanalyse van de bron (of de modeltekst)."""
        if bron_id in self.modelbronnen:
            doel = self.bron_doel(bron_id)
            return {doel} if doel else set()
        return self.analyse_paden.get(bron_id, set())

    def van_type(self, paginatype: str) -> list[tuple[Path, frontmatter.Page]]:
        return [(pad, p) for pad, p in self.paginas.items() if p.meta.get("type") == paginatype]

    def rel(self, pad: Path) -> str:
        return pad.relative_to(self.root).as_posix()


def _laad_model(module, pad: Path):
    return module.laad(pad) if pad.exists() else None


# --- Controles per element ---


def controleer_element(w: Wiki, el: gam_gemeen.Element, ggm_data, gemma_data, alle_relaties) -> list[Bevinding]:
    b: list[Bevinding] = []
    doel = w.rel(el.pad)
    meta = el.meta

    def fout(naam, melding):
        b.append(Bevinding(naam, doel, "fout", melding))

    def waarschuwing(naam, melding):
        b.append(Bevinding(naam, doel, "waarschuwing", melding))

    # Uniek id en plaats in de mappen
    if len(w.op_id.get(el.id, [])) > 1:
        fout("id-uniek", f"id '{el.id}' komt meer dan eens voor")
    typedef = w.elementtypen.get(el.paginatype, {})
    verwacht = w.root / typedef.get("dir", "")
    for veld in typedef.get("submappen", []):
        verwacht = verwacht / slug(str(meta.get(veld, "")))
    if el.pad.parent != verwacht.resolve():
        fout("plaats", f"hoort in {w.rel(verwacht)}/ (map volgt {', '.join(typedef.get('submappen', [])) or 'het paginatype'})")

    # Kenmerken ↔ type en status (EL1, EL18)
    kenmerken = meta.get("kenmerken") or {}
    ontbrekend = [bepaal_type.NAAM[s] for s in bepaal_type.SLEUTELS if s not in kenmerken]
    if kenmerken and ontbrekend:
        fout("kenmerken-onvolledig", f"kenmerken niet beantwoord: {', '.join(ontbrekend)} [EL1]")
    if set(kenmerken) == set(bepaal_type.SLEUTELS):
        beoordeling = {"begrip": el.id, "kenmerken": {k: {"waarde": v, "onderbouwing": "-"} for k, v in kenmerken.items()}}
        uitkomst = bepaal_type.evalueer(beoordeling)
        toegestaan = {(uitkomst.paginatype, uitkomst.archimate_type)}
        tegenhanger = el.paginatype == "bedrijfsobject" and _is_tegenhanger(w, el)
        if (el.paginatype, meta.get("archimate_type")) not in toegestaan and not tegenhanger:
            fout("kenmerken-type", f"kenmerken leiden tot {uitkomst.soort} {uitkomst.archimate_type or ''} "
                 f"(regel {uitkomst.regel}), niet tot {el.paginatype}/{meta.get('archimate_type')}")
        if uitkomst.data_object != meta.get("data_object", "nee"):
            fout("data-object", f"data_object hoort '{uitkomst.data_object}' te zijn (kenmerk geautomatiseerd verwerkt)")
        if meta.get("status") == "review":
            status = bepaal_type.voorgestelde_status(uitkomst, (meta.get("match") or {}).get("ggm"), meta.get("grondslag"))
            if status != "review" and not tegenhanger:
                fout("status", f"status 'review' niet toegestaan: voorleggen ({'; '.join(uitkomst.redenen) or 'autonomieregel'}) [EL18]")
        if uitkomst.tegenhanger and gam_gemeen.sectie(el.body, "Tegenhanger") is None:
            waarschuwing("tegenhanger", "kenmerken wijzen op een tegenhanger (bedrijfsobject); sectie '## Tegenhanger' ontbreekt")

    if meta.get("status") == "kandidaat" and gam_gemeen.sectie(el.body, "Ter discussie") is None:
        fout("ter-discussie", "status 'kandidaat' zonder sectie '## Ter discussie' [IH6]")

    # Definities (§ bronvoorrang)
    definitie = str(meta.get("definitie", ""))
    if len(re.findall(r"[.!?](?:\s+[A-Z]|\s*$)", definitie)) > 1:
        waarschuwing("definitie-vorm", "definitie lijkt meer dan één zin [VR3]")
    contexten = {str((s or {}).get("context", "")).lower() for s in meta.get("synoniemen") or [] if isinstance(s, dict)}
    if contexten & {"beleid", "dagelijks gebruik"} and "wet" not in contexten:
        waarschuwing("naam-wetsterm", "gangbare term staat als synoniem en geen wetsterm: is de naam de wetsterm? "
                     "De naam komt uit de gangbare taal, de wetsterm wordt synoniem [SRC10]")
    eerste = re.search(r"^## (.+?)\s*$", el.body, re.M)
    if not eerste or eerste.group(1) != "Definitie":
        fout("definitie-bovenaan", "eerste sectie is niet '## Definitie' (herkenbare definitie, dan Beschrijving)")
    elif " ".join(definitie.split()) not in " ".join((gam_gemeen.sectie(el.body, "Definitie") or "").split()):
        fout("definitie-bovenaan", "'## Definitie' bevat de definitie uit de frontmatter niet letterlijk")
    if meta.get("definitie_formeel"):
        bron =(meta.get("definitie_formeel_bron") or {}).get("bron")
        try:
            brontype = sources.read_index_entry(w.repo_root, bron).get("brontype")
        except (FileNotFoundError, TypeError):
            brontype = None
            fout("definitie-formeel", f"bron '{bron}' van de formele definitie bestaat niet")
        if brontype and brontype not in ("wet", "informatiemodel"):
            fout("definitie-formeel", f"formele definitie uit een bron van brontype '{brontype}'; alleen wet of informatiemodel")
        if bron and bron == w.yaml.get("ggm", {}).get("bron"):
            fout("definitie-formeel", "formele definitie uit het GGM: die staat al in ggm_definitie")
        if " ".join(str(meta["definitie_formeel"]).split()) == " ".join(definitie.split()):
            fout("definitie-formeel", "formele definitie is gelijk aan de herkenbare; laat de formele weg")
        if " ".join(str(meta["definitie_formeel"]).split()).lower() not in " ".join((gam_gemeen.sectie(el.body, "Definitie") or "").split()).lower():
            fout("definitie-formeel", "formele definitie staat niet in '## Definitie' (als citaat, met het verschil)")

    # Modelvelden (EL12)
    if meta.get("ggm_guid"):
        import ggm

        if ggm_data is None:
            waarschuwing("ggm-velden", "GGM niet geladen (tools/ggm.py release); ggm_*-velden niet gecontroleerd")
        elif meta["ggm_guid"] not in ggm_data["entities"]:
            fout("ggm-velden", f"ggm_guid {meta['ggm_guid']} bestaat niet in het GGM")
        else:
            verwacht_v = ggm.velden(ggm_data["entities"][meta["ggm_guid"]])
            huidig = {k: meta[k] for k in ggm.GGM_VELDEN if k in meta}
            if huidig != verwacht_v:
                fout("ggm-velden", "ggm_*-velden wijken af van het GGM; vul ze met tools/ggm.py velden/verrijk [EL12]")
    if meta.get("gemma_id"):
        import gemma

        if gemma_data is None:
            waarschuwing("gemma-velden", "GEMMA-model niet geladen (tools/gemma.py release); gemma_*-velden niet gecontroleerd")
        elif meta["gemma_id"] not in gemma_data["elementen"]:
            fout("gemma-velden", f"gemma_id {meta['gemma_id']} bestaat niet in het GEMMA-model")
        else:
            verwacht_g = gemma.velden(gemma_data["elementen"][meta["gemma_id"]])
            if {k: meta[k] for k in gemma.GEMMA_VELDEN if k in meta} != verwacht_g:
                fout("gemma-velden", "gemma_*-velden wijken af van het GEMMA-model; vul ze met tools/gemma.py [EL12]")
            groepen = gemma.groepering(gemma_data, meta["gemma_id"])
            if groepen and meta.get("beleidsdomein") and meta["beleidsdomein"] not in groepen:
                waarschuwing("groepering", f"beleidsdomein '{meta['beleidsdomein']}' wijkt af van de groepering in GEMMA ({', '.join(groepen)})")

    # Geen elementverwijzingen in de frontmatter (EL17)
    if re.search(r"\]\(|\.md\b|\[\[", json.dumps(meta, ensure_ascii=False, default=str)):
        fout("frontmatter-links", "verwijzingen naar andere pagina's horen als link in de body, niet in de frontmatter [EL17]")

    # Herleidbaarheid: bron → bronanalyse → begrippenlijst → element
    analyses = {p.meta.get("id") for _, p in w.van_type("bronanalyse")}
    for bron in meta.get("bronnen", []) or []:
        if bron not in w.modelbronnen and bron not in analyses:
            fout("herleidbaarheid", f"bron '{bron}' heeft geen bronanalyse")
    if not any(el.pad in _gelinkte_paden(w, pad, p.body) for pad, p in w.van_type("onderwerp")):
        fout("herleidbaarheid", "element staat in geen enkele begrippenlijst (begrippen/<onderwerp>.md)")

    # Elke bronverwijzing is een link: pagina → bronanalyse → sources/raw/ (repository-regel Herleidbaarheid)
    for kop in ("Kenmerken", "Relaties"):
        for rij in gam_gemeen.tabel(gam_gemeen.sectie(el.body, kop)):
            for melding in _bronlinks(w, el.pad, rij.get("Bron", "")):
                fout("bron-link", f"'## {kop}': {melding}")
    in_bronnen = _gelinkte_paden(w, el.pad, gam_gemeen.sectie(el.body, "Bronnen") or "")
    for bron in meta.get("bronnen", []) or []:
        doelen = w.bron_doelen(bron)
        if doelen and not doelen & in_bronnen:
            fout("bron-link", f"'## Bronnen' linkt niet naar {'de tekst' if bron in w.modelbronnen else 'de bronanalyse'} van '{bron}'")

    # Relaties
    gezien = set()
    for r in alle_relaties.get(el.id, []):
        for f in r.fouten:
            fout("relatie", f)
        if (r.relatie, r.naar) in gezien:
            fout("relatie", f"dubbele relatie {r.relatie} naar {r.naar}")
        gezien.add((r.relatie, r.naar))
        for bron in r.bronnen:
            if bron not in w.modelbronnen and bron not in analyses:
                fout("relatie-bron", f"relatie naar {r.naar}: bron '{bron}' heeft geen bronanalyse")
        doelen = w.op_id.get(r.naar)
        if doelen and r.relatie in rel_tool.RELATIES.values():
            doel_type = doelen[0].meta.get("archimate_type", "")
            if not rel_tool.toegestaan(r.relatie, meta.get("archimate_type", ""), doel_type):
                fout("relatie-archimate", f"{r.relatie} van {meta.get('archimate_type')} naar {doel_type} is geen geldige ArchiMate-relatie")
            if r.grondslag == "ggm-exact" and ggm_data is not None:
                eindpunten = {meta.get("ggm_guid"), doelen[0].meta.get("ggm_guid")}
                for rid in r.ggm_relaties:
                    g = ggm_data["relations"].get(rid)
                    if g is None:
                        fout("relatie-ggm", f"GGM-relatie {rid} bestaat niet")
                    elif {g["source_id"], g["target_id"]} != eindpunten:
                        fout("relatie-ggm", f"GGM-relatie {rid} verbindt niet de GGM-entiteiten van beide elementen; gebruik ggm-afgeleid")
    for rij in gam_gemeen.tabel(gam_gemeen.sectie(el.body, "Specialisaties")):
        eerste = rij.get(next(iter(rij)), "")
        gelinkt = gam_gemeen.link(eerste)
        if gelinkt:
            kind = w.op_pad.get(gam_gemeen.doel_van_link(el.pad, gelinkt[1]))
            if kind and not any(r.relatie == "specialization" and r.naar == el.id for r in alle_relaties.get(kind, [])):
                fout("specialisatie", f"specialisatie '{kind}' heeft geen relatie 'specialisatie' naar {el.id}")
        elif not rij.get("Omschrijving", "").strip():
            fout("specialisatie", f"specialisatie zonder pagina '{eerste}' heeft geen omschrijving")
    for kop in ("Tegenhanger", "Homoniemen"):
        for pad in _gelinkte_paden(w, el.pad, gam_gemeen.sectie(el.body, kop) or ""):
            ander = w.op_pad.get(pad)
            if ander and el.pad not in _gelinkte_paden(w, pad, gam_gemeen.sectie(w.paginas[pad].body, kop) or ""):
                (fout if kop == "Tegenhanger" else waarschuwing)(kop.lower(), f"{ander} verwijst in '## {kop}' niet terug")

    # Formulering (WC7, WC8–WC11, EL1)
    b += _formulering(doel, el.body + "\n" + definitie)
    return b


def _is_tegenhanger(w: Wiki, el) -> bool:
    """Een bedrijfsobjectpagina die als tegenhanger van een actor/rol is vastgelegd."""
    for pad in _gelinkte_paden(w, el.pad, gam_gemeen.sectie(el.body, "Tegenhanger") or ""):
        ander = w.op_pad.get(pad)
        if ander and w.op_id[ander][0].paginatype in ("actor", "rol"):
            return True
    return False


def _gelinkte_paden(w: Wiki, van: Path, tekst: str) -> set[Path]:
    return {gam_gemeen.doel_van_link(van, m.group("doel")) for m in gam_gemeen.LINK_RE.finditer(tekst or "")
            if not m.group("doel").startswith(("http://", "https://", "#", "mailto:"))}


def _bronlinks(w: Wiki, van: Path, cel: str) -> list[str]:
    """Meldingen voor een Bron-cel: elk bron-id staat als link naar de bronanalyse (bij een modelbron: de tekst)."""
    meldingen = []
    for bron in dict.fromkeys(gam_gemeen.BRON_ID_RE.findall(gam_gemeen.LINK_RE.sub("", cel or ""))):
        meldingen.append(f"bron '{bron}' staat er als tekst; maak er een link naar de bronanalyse van"
                         if w.bron_doel(bron) else f"bron '{bron}' heeft geen bronanalyse")
    for m in gam_gemeen.LINK_RE.finditer(cel or ""):
        if gam_gemeen.BRON_ID_RE.fullmatch(m.group("tekst")):
            doel = w.bron_doel(m.group("tekst"))
            if doel is None:
                meldingen.append(f"bron '{m.group('tekst')}' heeft geen bronanalyse")
            elif gam_gemeen.doel_van_link(van, m.group("doel")) not in w.bron_doelen(m.group("tekst")):
                meldingen.append(f"link '{m.group('tekst')}' wijst niet naar de bronanalyse van die bron")
    return meldingen


def _formulering(doel: str, tekst: str) -> list[Bevinding]:
    b = []
    for m in gam_gemeen.LINK_RE.finditer(tekst):
        if any(t in m.group("doel") for t in TECHNISCHE_DOELEN):
            b.append(Bevinding("technische-verwijzing", doel, "fout", f"link naar '{m.group('doel')}' [WC7]"))
    laag = tekst.lower()
    for zin in VERBODEN_ZINNEN:
        if zin in laag:
            b.append(Bevinding("absolute-taal", doel, "waarschuwing", f"'{zin}': alleen met concrete, domeinspecifieke reden [WC8–WC11]"))
    for m in REGISTR_RE.finditer(tekst):
        b.append(Bevinding("anti-patroon", doel, "waarschuwing", f"'{m.group(0)}': beoordeel of dit als argument voor het type wordt gebruikt [EL1]"))
    return b


# --- Controles op begrippenlijsten, bronanalyses en gegenereerde bestanden ---


def controleer_overig(w: Wiki) -> list[Bevinding]:
    b: list[Bevinding] = []
    onderwerpen = {p.meta.get("id"): (pad, p) for pad, p in w.van_type("onderwerp")}
    for pad, p in onderwerpen.values():
        rijen = gam_gemeen.tabel(gam_gemeen.sectie(p.body, "Begrippen"))
        if gam_gemeen.sectie(p.body, "Begrippen") is None:
            b.append(Bevinding("begrippenlijst", w.rel(pad), "fout", "sectie '## Begrippen' met de begrippentabel ontbreekt"))
        elif rijen and not {"Begrip", "Uitkomst", "Reden"} <= set(rijen[0]):
            b.append(Bevinding("begrippenlijst", w.rel(pad), "fout", "begrippentabel mist kolom Begrip, Uitkomst of Reden"))
        b += _formulering(w.rel(pad), p.body)
    for pad, p in w.van_type("bronanalyse"):
        onderwerp, bron_id = p.meta.get("onderwerp"), p.meta.get("id")
        if pad.parent.name != onderwerp:
            b.append(Bevinding("bronanalyse", w.rel(pad), "fout", f"hoort in bronanalyses/{onderwerp}/"))
        relatietabel = gam_gemeen.sectie(p.body, "Relaties")
        rijen = gam_gemeen.tabel(relatietabel)
        if relatietabel is not None and rijen and not {"Van", "Werkwoord", "Naar", "Vindplaats"} <= set(rijen[0]):
            b.append(Bevinding("bronanalyse", w.rel(pad), "fout", "relatietabel mist kolom Van, Werkwoord, Naar of Vindplaats"))
        if bron_id not in (p.meta.get("bronnen") or []):
            b.append(Bevinding("bronanalyse", w.rel(pad), "fout", "de eigen bron-id ontbreekt in bronnen:"))
        tekst = (w.repo_root / "sources" / "raw" / f"{bron_id}.md").resolve()
        regel = re.search(r"(?m)^Bron: .*$", p.body)
        if regel is None or tekst not in _gelinkte_paden(w, pad, regel.group(0)):
            b.append(Bevinding("bronregel", w.rel(pad), "fout", f"onder de titel ontbreekt 'Bron:' met een link naar "
                               f"sources/raw/{bron_id}.md (llmwiki source bronregel {bron_id} --van <pad> --schrijf)"))
        begrippen = onderwerpen.get(onderwerp)
        if begrippen is None or bron_id not in (begrippen[1].meta.get("bronnen") or []):
            b.append(Bevinding("bronanalyse", w.rel(pad), "fout", f"bron staat niet in de bronnenlijst van begrippen/{onderwerp}.md"))
        b += _formulering(w.rel(pad), p.body)
    return b


def controleer_gegenereerd(wiki_root: Path) -> list[Bevinding]:
    b = []
    for map_ in ("ggm", "gemma"):
        for pad in sorted((wiki_root / map_).rglob("*")):
            melding = None
            if pad.suffix == ".md":
                melding = gam_gemeen.controleer_gegenereerd(pad)
            elif pad.suffix == ".json":
                melding = gam_gemeen.controleer_json_gegenereerd(pad)
            if melding:
                b.append(Bevinding("gegenereerd", pad.relative_to(wiki_root).as_posix(), "fout", melding + " [SRC5]"))
    return b


def controleer(wiki_root: Path = WIKI_ROOT, run_id: str | None = None) -> list[Bevinding]:
    import gemma
    import ggm

    w = Wiki(wiki_root, run_id)
    ggm_data = _laad_model(ggm, wiki_root / "ggm" / "ggm_parsed.json")
    gemma_data = _laad_model(gemma, wiki_root / "gemma" / "gemma_parsed.json")
    op_pad = {el.pad: el.id for el in w.elementen}
    alle_relaties = {el.id: rel_tool.lees_tabel(el.pad, el.body, op_pad) for el in w.elementen}

    bevindingen = []
    for el in w.elementen:
        if run_id is None or el.pad in w.in_run:
            bevindingen += controleer_element(w, el, ggm_data, gemma_data, alle_relaties)
    bevindingen += [x for x in controleer_overig(w) if run_id is None or (w.root / x.doel).resolve() in w.in_run]
    bevindingen += controleer_gegenereerd(wiki_root)
    return bevindingen


def naar_rapport(bevindingen: list[Bevinding], rapport: Path, run_id: str) -> None:
    data = json.loads(rapport.read_text(encoding="utf-8")) if rapport.exists() else {"run": run_id, "controles": []}
    data["controles"] = [c for c in data["controles"] if not c.get("naam", "").startswith("gemma-archimate-model:")]
    if not bevindingen:
        data["controles"].append({"naam": "gemma-archimate-model:domein", "resultaat": "ok", "ernst": "info"})
    for x in bevindingen:
        data["controles"].append({"naam": f"gemma-archimate-model:{x.naam}", "doel": x.doel, "resultaat": "fout",
                                  "ernst": x.ernst, "melding": x.melding})
    rapport.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Domeincontroles voor gemma-archimate-model (zie docstring).")
    p.add_argument("--run")
    p.add_argument("--rapport", help="validation-report.json om aan te vullen (vereist --run)")
    a = p.parse_args(argv)
    bevindingen = controleer(WIKI_ROOT, a.run)
    for x in bevindingen:
        print(f"{x.ernst.upper()}: {x.doel}: [{x.naam}] {x.melding}")
    if a.rapport:
        if not a.run:
            print("FOUT: --rapport vereist --run", file=sys.stderr)
            return 2
        naar_rapport(bevindingen, Path(a.rapport), a.run)
    fouten = sum(1 for x in bevindingen if x.ernst == "fout")
    print(f"check_elementen: {fouten} fout(en), {len(bevindingen) - fouten} waarschuwing(en)")
    return 1 if fouten else 0


if __name__ == "__main__":
    sys.exit(main())
