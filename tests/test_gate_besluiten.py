"""Het voorstel als plan: per pagina een besluit dat de redacteur in het document kan wijzigen."""
import re

import pytest

from llmwiki import frontmatter, gate, paths, runs

from test_curatie_status import _page, _run_with_pages


def _zet_besluit(voorstel, pad, besluit, opmerking=""):
    """Wijzigt de kolommen Besluit en Opmerking van één rij, zoals de redacteur dat in de editor doet."""
    regels = []
    for regel in voorstel.read_text(encoding="utf-8").splitlines():
        if f'"{pad}")' in regel:
            cellen = regel.strip().strip("|").split("|")
            cellen[3], cellen[4] = f" {besluit} ", f" {opmerking} "
            regel = "|" + "|".join(cellen) + "|"
        regels.append(regel)
    voorstel.write_text("\n".join(regels) + "\n", encoding="utf-8")


def _akkoord(voorstel):
    page = frontmatter.read(voorstel)
    page.meta.update(akkoord_voor_publicatie="ja", beoordeeld_door="M. Jansen")
    frontmatter.write(voorstel, page)


@pytest.fixture
def plan_met_twee(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_with_pages(wiki_root, wiki_yaml, {"klaar": "review", "twijfel": "kandidaat"})
    voorstel = gate.plan(wiki_root, wiki_yaml, run_id)
    return wiki_root, wiki_yaml, run_id, voorstel


def test_plan_is_leesbaar_en_diffs_staan_apart(plan_met_twee):
    wiki_root, _, run_id, voorstel = plan_met_twee
    tekst = voorstel.read_text(encoding="utf-8")
    assert '"kandidaten/klaar.md")<br>nieuw · kandidaat |' in tekst and "| goedkeuren |" in tekst
    assert '"kandidaten/twijfel.md")<br>nieuw · kandidaat |' in tekst and "| schrijven |" in tekst
    assert "```diff" not in tekst
    assert "```diff" in (wiki_root / "voorstellen" / f"{run_id}-details.md").read_text(encoding="utf-8")


def test_standaardbesluiten_na_akkoord(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    _akkoord(voorstel)
    gate.apply(wiki_root, wiki_yaml, run_id)
    assert frontmatter.read(wiki_root / "kandidaten" / "klaar.md").meta["status"] == "goedgekeurd"
    assert frontmatter.read(wiki_root / "kandidaten" / "twijfel.md").meta["status"] == "kandidaat"


def test_overslaan_schrijft_de_pagina_niet(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    _zet_besluit(voorstel, "kandidaten/twijfel.md", "overslaan")
    _akkoord(voorstel)
    gate.apply(wiki_root, wiki_yaml, run_id)
    assert (wiki_root / "kandidaten" / "klaar.md").exists()
    assert not (wiki_root / "kandidaten" / "twijfel.md").exists()


def test_aanpassen_blokkeert_uitvoeren(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    _zet_besluit(voorstel, "kandidaten/klaar.md", "aanpassen", "definitie te lang")
    _akkoord(voorstel)
    with pytest.raises(gate.GateError, match="definitie te lang"):
        gate.apply(wiki_root, wiki_yaml, run_id)
    assert not (wiki_root / "kandidaten" / "klaar.md").exists()


def test_goedkeuren_van_kandidaat_is_niet_toegestaan(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    _zet_besluit(voorstel, "kandidaten/twijfel.md", "goedkeuren")
    _akkoord(voorstel)
    with pytest.raises(gate.GateError, match="niet toegestaan"):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_verwijderde_rij_blokkeert_uitvoeren(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    tekst = "\n".join(r for r in voorstel.read_text(encoding="utf-8").splitlines() if "kandidaten/twijfel.md" not in r)
    voorstel.write_text(tekst + "\n", encoding="utf-8")
    _akkoord(voorstel)
    with pytest.raises(gate.GateError, match="ontbreekt"):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_overslaan_mag_geen_link_breken(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_with_pages(wiki_root, wiki_yaml, {"klaar": "review", "doel": "review"})
    staged = runs.run_dir(wiki_root, run_id) / "changeset" / "klaar.md"
    staged.write_text(_page("klaar", "review") + "\nZie [doel](doel.md).\n", encoding="utf-8")
    voorstel = gate.plan(wiki_root, wiki_yaml, run_id)
    _zet_besluit(voorstel, "kandidaten/doel.md", "overslaan")
    _akkoord(voorstel)
    with pytest.raises(gate.GateError, match="linkt naar"):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_nieuw_plan_bewaart_besluiten_van_ongewijzigde_paginas(plan_met_twee):
    wiki_root, wiki_yaml, run_id, voorstel = plan_met_twee
    _zet_besluit(voorstel, "kandidaten/twijfel.md", "overslaan", "later")
    _zet_besluit(voorstel, "kandidaten/klaar.md", "aanpassen", "korter")
    # De Agent verwerkt de opmerking bij 'klaar' en maakt een nieuw plan.
    staged = runs.run_dir(wiki_root, run_id) / "changeset" / "klaar.md"
    staged.write_text(_page("klaar", "review") + "\nKorter.\n", encoding="utf-8")
    voorstel = gate.plan(wiki_root, wiki_yaml, run_id)
    tekst = voorstel.read_text(encoding="utf-8")
    assert re.search(r'kandidaten/twijfel\.md"\).*\| overslaan \| later \|', tekst)
    assert re.search(r'kandidaten/klaar\.md"\).*\| goedkeuren \|  \|', tekst)
    assert frontmatter.read(voorstel).meta["akkoord_voor_publicatie"] == "nee"
