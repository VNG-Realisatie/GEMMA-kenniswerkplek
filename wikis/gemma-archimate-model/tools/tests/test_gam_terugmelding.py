"""tools/terugmelding.py: rijen toevoegen aan de doorlopende lijst, gestaged in de run."""
import json

import pytest
from gam_hulp import KENMERKEN_BO, element_tekst

import terugmelding
from llmwiki import frontmatter, paths, runs


def _run(wiki):
    return runs.start(wiki, paths.load_wiki_yaml(wiki), "gemma-archimate-model-update")["run_id"]


def test_eerste_en_tweede_terugmelding_in_een_run(archimate_repo):
    root, wiki = archimate_repo
    pad = wiki / "bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/beschikking.md"
    pad.parent.mkdir(parents=True)
    pad.write_text(element_tekst({"id": "beschikking", "type": "bedrijfsobject", "status": "review", "naam": "Beschikking",
                                  "archimate_type": "business-object", "onderwerp": "o", "bronnen": ["2026-vng-ggm"],
                                  "definitie": "x", "grondslag": "bron", "kenmerken": KENMERKEN_BO}), encoding="utf-8")
    run_id = _run(wiki)
    een = terugmelding.voeg_toe(wiki, run_id, "definitie", "Vergunningen", "Beschikking", "Definitie | te smal", "beschikking")
    twee = terugmelding.voeg_toe(wiki, run_id, "hiaat", "Vergunningen", "—", "Leges ontbreekt")
    assert (een["nummer"], twee["nummer"]) == (1, 2)
    assert "[beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/beschikking.md)" in een["rij"]

    concept = json.loads((runs.run_dir(wiki, run_id) / "changeset-concept.json").read_text(encoding="utf-8"))
    (entry,) = [p for p in concept["paginas"] if p["pad"] == "analyses/ggm-terugmeldingen.md"]
    page = frontmatter.read(runs.run_dir(wiki, run_id) / "changeset" / entry["staged_bestand"])
    rijen = terugmelding.rijen(page)
    assert [r["#"] for r in rijen] == ["1", "2"]
    assert rijen[0]["Bevinding"] == "Definitie | te smal"
    assert entry["type"] == "analyse" and entry["actie"] == "nieuw"


def test_onbekend_type_of_element_wordt_geweigerd(archimate_repo):
    root, wiki = archimate_repo
    run_id = _run(wiki)
    with pytest.raises(ValueError, match="type"):
        terugmelding.voeg_toe(wiki, run_id, "klacht", "x", "y", "z")
    with pytest.raises(ValueError, match="niet gevonden"):
        terugmelding.voeg_toe(wiki, run_id, "hiaat", "x", "y", "z", "bestaat-niet")
