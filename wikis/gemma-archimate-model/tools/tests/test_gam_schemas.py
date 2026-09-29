"""De paginatype-schema's van deze wiki, toegepast via `llmwiki validate` (core)."""
from gam_hulp import KENMERKEN_BO, element_tekst
from llmwiki import paths, validate


def _bo(**over):
    meta = {
        "id": "beschikking",
        "type": "bedrijfsobject",
        "status": "review",
        "naam": "Beschikking",
        "archimate_type": "business-object",
        "onderwerp": "vergunningen",
        "taakveld": "8 Volkshuisvesting",
        "beleidsdomein": "Vergunningen",
        "bronnen": ["2026-overheid-gemeentewet"],
        "definitie": "Schriftelijk besluit van de gemeente over een individueel geval.",
        "grondslag": "ggm-entiteit",
        "match": {"ggm": "exact"},
        "data_object": "ja",
        "kenmerken": KENMERKEN_BO,
        "ggm_entiteit": "Beschikking",
        "ggm_guid": "EAID_1234",
    }
    meta.update(over)
    return {k: v for k, v in meta.items() if v is not None}


def _valideer(wiki, meta, pad="bedrijfsarchitectuur/bedrijfsobjecten/8-volkshuisvesting/vergunningen/beschikking.md"):
    page = wiki / pad
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(element_tekst(meta), encoding="utf-8")
    return validate.validate_page(wiki, page, paths.load_wiki_yaml(wiki))


def test_geldige_bedrijfsobjectpagina(archimate_repo):
    root, wiki = archimate_repo
    assert _valideer(wiki, _bo()) == []


def test_oude_bo_velden_worden_geweigerd(archimate_repo):
    root, wiki = archimate_repo
    errors = _valideer(wiki, _bo(bo_definitie="oud veld"))
    assert any("bo_definitie" in e for e in errors)


def test_definitie_te_lang_of_verwijzend(archimate_repo):
    root, wiki = archimate_repo
    assert any("definitie" in e for e in _valideer(wiki, _bo(definitie="x" * 161)))
    assert any("definitie" in e for e in _valideer(wiki, _bo(definitie="Gelijk aan GGM.")))


def test_formele_definitie_vereist_bron(archimate_repo):
    root, wiki = archimate_repo
    errors = _valideer(wiki, _bo(definitie_formeel="Een besluit dat niet van algemene strekking is."))
    assert any("definitie_formeel_bron" in e for e in errors)


def test_genest_type_vereist_taakveld(archimate_repo):
    root, wiki = archimate_repo
    errors = _valideer(wiki, _bo(taakveld=None))
    assert any("taakveld" in e for e in errors)


def test_onvolledige_kenmerken_worden_geweigerd(archimate_repo):
    root, wiki = archimate_repo
    kenmerken = dict(KENMERKEN_BO)
    del kenmerken["plaats"]
    assert any("plaats" in e for e in _valideer(wiki, _bo(kenmerken=kenmerken)))


def test_actor_is_plat_en_zonder_taakveld_geldig(archimate_repo):
    root, wiki = archimate_repo
    meta = _bo(id="inwoner", type="actor", naam="Inwoner", archimate_type="business-actor",
               taakveld=None, beleidsdomein=None, ggm_entiteit=None, ggm_guid=None, match=None,
               grondslag="bron", data_object="nee")
    assert _valideer(wiki, meta, "bedrijfsarchitectuur/actoren/inwoner.md") == []


def test_onderwerp_afgerond_vereist_conclusie(archimate_repo):
    root, wiki = archimate_repo
    meta = {"id": "vergunningen", "type": "onderwerp", "naam": "Vergunningen", "status": "afgerond", "bronnen": []}
    errors = _valideer(wiki, meta, "begrippen/vergunningen.md")
    assert any("conclusie" in e for e in errors)
    meta["conclusie"] = "Twee elementen; de overige begrippen zijn eigenschappen."
    assert _valideer(wiki, meta, "begrippen/vergunningen.md") == []
