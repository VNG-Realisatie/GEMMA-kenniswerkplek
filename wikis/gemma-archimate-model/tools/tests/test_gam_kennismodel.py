"""Het kennismodel (tools/kennismodel.py): compleet, consistent met de beslistabel en de ArchiMate-toets, gelijk aan de
pagina's in kennismodel/ en, waar de bron er is, aan Over GEMMA."""
import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import bepaal_type as bt  # noqa: E402
import kennismodel as km  # noqa: E402
import relaties  # noqa: E402

WIKI = TOOLS.parent
MET_ELEMENT = [e for e in km.ELEMENTTYPEN if e.paginatype]


def test_elk_type_heeft_modelleerafspraken_en_elke_laag_weggefilterd():
    paginas = km.paginas()
    for e in km.ELEMENTTYPEN:
        assert f"kennismodel/{e.laag}/{e.sleutel}-modelleerafspraken.md" in paginas, e.sleutel
    for laag in km.LAGEN:
        assert f"kennismodel/{laag}/weggefilterd.md" in paginas, laag
    for z in km.ZONDER_ELEMENT:
        assert z.laag in km.LAGEN, z.sleutel


def test_paginas_zijn_gelijk_aan_de_bron():
    for pad, inhoud in km.paginas().items():
        assert (WIKI / pad).read_text(encoding="utf-8") == inhoud, f"{pad}: draai uv run python tools/render.py"


def test_typen_van_de_beslistabel_staan_in_het_kennismodel():
    for t in bt.TYPEN:
        e = km.VAN_ARCHIMATE.get(t.archimate_type)
        z = next((z for z in km.ZONDER_ELEMENT if z.archimate_type == t.archimate_type), None)
        assert e or z, t.naam
        if t.laag == "pagina":
            assert e and e.paginatype == t.paginatype, t.naam


def test_elke_kernrelatie_staat_in_de_relaties_van_haar_type():
    for t in bt.TYPEN:
        if not t.kern:
            continue
        sleutel = km.sleutel_van(t.archimate_type)
        assert any(sleutel in (r.bron, r.doel) for r in km.kernrelaties(t.kern)), f"{t.naam}: {t.kern}"
    for r in km.RELATIES:
        for k in r.kern:
            assert k in bt.NAAM, k


def test_elk_type_met_pagina_heeft_een_indeling_en_bekende_eigenschappen():
    for e in MET_ELEMENT:
        assert km.indelingen_van(e.sleutel), e.sleutel
    for e in km.ELEMENTTYPEN:
        assert set(e.eigenschappen) <= set(km.EIGENSCHAPPEN), e.sleutel
        assert set(e.verplicht) <= set(e.eigenschappen), e.sleutel
    for i in km.INDELINGEN:
        assert set(i.typen) <= set(km.ELEMENTTYPE), i.naam
        assert set(i.velden) <= set(km.EIGENSCHAPPEN), i.naam


def _archimate(sleutel: str) -> str:
    return km.ELEMENTTYPE[sleutel].archimate_type


def test_toegestane_relaties_zijn_geldig():
    """Elke relatie in het kennismodel tussen typen met een pagina doorstaat de toets van tools/relaties.py."""
    for r in km.RELATIES:
        if r.bron in km.ELEMENTTYPE and r.doel in km.ELEMENTTYPE and km.ELEMENTTYPE[r.bron].paginatype \
                and km.ELEMENTTYPE[r.doel].paginatype:
            assert relaties.toegestaan(km.RELATIETYPEN[km.kale_soort(r.soort)], _archimate(r.bron),
                                       _archimate(r.doel)), r
            assert km.weggefilterd(r.bron, r.soort, r.doel) is None, r
    sleutels = [(r.bron, r.soort, r.doel) for r in km.RELATIES]
    assert len(sleutels) == len(set(sleutels))


def test_elke_gemma_afspraak_van_de_toets_is_weggefilterd_met_reden():
    """Wat tools/relaties.py weigert terwijl ArchiMate het toestaat, staat als weggefilterd in het kennismodel."""
    for b in MET_ELEMENT:
        for d in MET_ELEMENT:
            for soort, rel in km.RELATIETYPEN.items():
                if relaties.archimate_geldig(rel, b.archimate_type, d.archimate_type) and not relaties.toegestaan(
                        rel, b.archimate_type, d.archimate_type):
                    assert km.weggefilterd(b.sleutel, soort, d.sleutel), (b.sleutel, soort, d.sleutel)


def test_relaties_in_de_beoordelingen_zijn_toegestaan_of_weggefilterd():
    """Elke combinatie van brontype, relatie en doeltype in de beoordelingen heeft een plek: in het kennismodel, of
    weggefilterd met een reden."""
    begrippen = relaties.elementen(relaties.begrippen(WIKI))
    for d in begrippen.values():
        bron = km.sleutel_van(d["afgeleid"]["uitkomst"]["archimate_type"])
        for r in d.get("relaties") or []:
            if r["naar"] not in begrippen:
                continue
            doel = km.sleutel_van(begrippen[r["naar"]]["afgeleid"]["uitkomst"]["archimate_type"])
            assert km.toegestaan(bron, r["soort"], doel) or km.weggefilterd(bron, r["soort"], doel), \
                (d["begrip"], r["soort"], r["naar"])


def test_in_over_gemma_klopt_met_de_bron():
    from llmwiki import paths

    import archimate_export as ae

    wiki_yaml = paths.load_wiki_yaml(WIKI)
    pad = paths.find_repo_root(WIKI) / "sources" / "raw" / f"{wiki_yaml['kennismodel']['bron']}.xml"
    if not pad.exists():
        pytest.skip("Over GEMMA (AMEFF) ontbreekt")
    og = ae.laad_kennismodel(pad, wiki_yaml["kennismodel"]["views"])
    typen = {e["type"] for e in og["model_elementen"].values()}
    for e in km.ELEMENTTYPEN:
        assert e.over_gemma == (e.archimate_type in typen), e.sleutel
    drietallen = og["model_relatietypen"]
    for r in km.RELATIES:
        rel = km.RELATIETYPEN[km.kale_soort(r.soort)] + "-relationship"
        b, d = _archimate(r.bron), _archimate(r.doel)
        in_og = (rel, b, d) in drietallen or (rel == "association-relationship" and (rel, d, b) in drietallen)
        assert r.over_gemma == in_og, r
