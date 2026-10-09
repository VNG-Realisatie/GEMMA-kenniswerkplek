"""Van beoordeling tot goedkeuring: llmwiki promote plan/apply met het akkoord in de chat (llmwiki/akkoord.py)."""
import pytest
import yaml
from gam_hulp import TOOLS
from test_gam_beslissen_render import _bo, _lees, _proces, _schrijf, wiki  # noqa: F401  (fixture)

from llmwiki import akkoord, beoordeling, lint, paths


@pytest.fixture
def wiki_met_scripts(wiki):  # noqa: F811
    """De fixture-wiki met de echte scripts (absoluut pad in wiki.yaml)."""
    y = paths.load_wiki_yaml(wiki)
    y["curation"].update(beslissen=str(TOOLS / "beslissen.py"), render=str(TOOLS / "render.py"), approval="chat")
    (wiki / "wiki.yaml").write_text(yaml.safe_dump(y, sort_keys=False, allow_unicode=True), encoding="utf-8")
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    return wiki, y


def test_plan_en_akkoord_keuren_goed_en_leggen_vast(wiki_met_scripts):
    wiki, y = wiki_met_scripts
    s = akkoord.plan(wiki, y)
    assert [e["id"] for e in s["te_keuren"]] == ["behandelen-aanvraag", "beschikking"]
    assert akkoord.apply(wiki, y, "AKKOORD", door="Redacteur") == ["behandelen-aanvraag", "beschikking"]

    assert _lees(wiki, "beschikking")["status"] == "goedgekeurd"
    log = (wiki / "log.md").read_text(encoding="utf-8")
    assert "promote | beschikking | Redacteur |" in log
    pagina = (wiki / _lees(wiki, "beschikking")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "**Status: goedgekeurd**" in pagina
    assert lint.check_goedgekeurd_guard(wiki.parent.parent) == []
    akkoord.draai_script(wiki, y, "beslissen")  # een volgende run van beslissen houdt goedgekeurd vast
    assert _lees(wiki, "beschikking")["status"] == "goedgekeurd"


@pytest.mark.parametrize("woord", [None, "prima", "akkoord"])
def test_zonder_letterlijk_akkoord_wordt_geweigerd(wiki_met_scripts, woord):
    wiki, y = wiki_met_scripts
    akkoord.plan(wiki, y)
    with pytest.raises(akkoord.AkkoordFout, match="AKKOORD"):
        akkoord.apply(wiki, y, woord)
    assert _lees(wiki, "beschikking")["status"] == "review"


def test_wijziging_na_het_plan_wordt_geweigerd(wiki_met_scripts):
    wiki, y = wiki_met_scripts
    akkoord.plan(wiki, y)
    data = _lees(wiki, "beschikking")
    data["definitie"] = "Gewijzigd na het tonen."
    _schrijf(wiki, "beschikking", data)
    with pytest.raises(akkoord.AkkoordFout, match="gewijzigd"):
        akkoord.apply(wiki, y, "AKKOORD")


def test_plan_per_onderwerp(wiki_met_scripts):
    wiki, y = wiki_met_scripts
    beoordeling.schrijf(wiki / "beoordelingen/onderwerpen/ander.yaml", {"naam": "Ander", "bronnen": []})
    data = _lees(wiki, "beschikking")
    data["onderwerpen"] = ["ander"]
    _schrijf(wiki, "beschikking", data)
    s = akkoord.plan(wiki, y, onderwerp="ander")
    assert [e["id"] for e in s["te_keuren"]] == ["beschikking"]


def test_guard_vangt_goedgekeurd_zonder_logregel(wiki_met_scripts):
    wiki, y = wiki_met_scripts
    akkoord.draai_script(wiki, y, "beslissen")
    data = _lees(wiki, "beschikking")
    data["status"] = "goedgekeurd"
    _schrijf(wiki, "beschikking", data)
    assert any("beschikking.yaml" in f for f in lint.check_goedgekeurd_guard(wiki.parent.parent))
