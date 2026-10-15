"""tools/beoordeling.py: zoek, besluiten, toon --oordeel, zet, relatie en besluit; en de compacte uitvoer van beslissen."""
import pytest
import yaml

import beoordeling as cli
import beslissen
import archimate_export
from gam_hulp import KENMERKEN_BO, WIKI
from llmwiki import beoordeling


def _kenmerken():
    return {s: {"waarde": w, "onderbouwing": "Niet van toepassing: geen gedrag." if w == "nee" else "Ja, want x."}
            for s, w in KENMERKEN_BO.items()}


@pytest.fixture
def wiki(archimate_repo):
    _, wiki = archimate_repo
    (wiki / "onderwerpen" / "demo" / "beoordelingen").mkdir(parents=True)
    (wiki / "onderwerpen" / "demo" / "afbakening.yaml").write_text(yaml.safe_dump(
        {"naam": "Demo", "niveau": "eigen", "besluiten": [{"datum": "2026-10-01", "besluit": "Afbakening", "gevolg": "opnemen"}]}),
        encoding="utf-8")
    for bid, naam, extra in [("aanvraag", "Aanvraag", {"synoniemen": [{"naam": "Verzoek", "context": "Awb"}]}),
                             ("aanvraag-reisdocument", "Aanvraag reisdocument", {}), ("besluit", "Besluit", {})]:
        data = {"begrip": naam, "onderwerpen": ["demo"], "kenmerken": _kenmerken(), "definitie": f"Definitie {naam}.",
                **extra, "beslist": {"uitkomst": {"soort": "element", "archimate_type": "business-object"}}, "status": "review"}
        beoordeling.schrijf(wiki / "onderwerpen" / "demo" / "beoordelingen" / f"{bid}.yaml", data)
    return wiki


def test_zoek_naam_synoniem_id_en_deel(wiki):
    assert cli.zoek(wiki, ["aanvraag"])[0].startswith("aanvraag | Aanvraag | business-object")
    assert len(cli.zoek(wiki, ["Aanvraag"])) == 1                      # exact gaat voor deel
    assert cli.zoek(wiki, ["verzoek"])[0].startswith("aanvraag |")     # synoniem
    assert cli.zoek(wiki, ["aanvraag-reisdocument"])[0].startswith("aanvraag-reisdocument |")
    assert "[deel van" in cli.zoek(wiki, ["reis"])[0]
    assert cli.zoek(wiki, ["bestaatniet"]) == ["bestaatniet: niet gevonden"]


def test_besluiten_van_onderwerp_en_begrip(wiki):
    assert cli.zet(wiki, "besluit", "kernobject", "aanvraag")
    cli.besluit(wiki, "besluit", "2026-10-02", "opnemen", advies_gevolgd=True)
    uit = cli.besluiten(wiki, "demo")
    assert uit[0].startswith("[demo] 2026-10-01") and "(advies gevolgd)" in uit[1]
    with pytest.raises(cli.Fout):
        cli.besluiten(wiki, "bestaatniet")


def test_toon_oordeel_laat_scriptvelden_en_standaard_nee_weg(wiki):
    volledig = yaml.safe_load(cli.toon(wiki, "aanvraag", False))
    kort = yaml.safe_load(cli.toon(wiki, "aanvraag", True))
    assert "beslist" in volledig and "beslist" not in kort and "status" not in kort
    assert set(kort["kenmerken"]) == {s for s, w in KENMERKEN_BO.items() if w == "ja"}


def test_zet_valideert_en_weigert_scriptvelden(wiki):
    cli.zet(wiki, "aanvraag", "definitie", "Nieuwe definitie.")
    cli.zet(wiki, "aanvraag", "kenmerken.herkenbaar.onderbouwing", "Anders.")
    data = beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "aanvraag.yaml")
    assert data["definitie"] == "Nieuwe definitie." and data["kenmerken"]["herkenbaar"]["onderbouwing"] == "Anders."
    assert data["status"] == "review" and "beslist" in data
    with pytest.raises(cli.Fout):
        cli.zet(wiki, "aanvraag", "status", "goedgekeurd")
    with pytest.raises(cli.Fout, match="schemafout"):
        cli.zet(wiki, "aanvraag", "afnemer", "onbekend")
    assert beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "aanvraag.yaml")["definitie"] == "Nieuwe definitie."


def test_relatie_toevoegen_vervangen_verwijderen(wiki):
    pad = wiki / "onderwerpen" / "demo" / "beoordelingen" / "aanvraag.yaml"
    assert "toegevoegd" in cli.relatie(wiki, "aanvraag", "associatie (gericht)", "besluit", naam="leidt tot",
                                       bronnen=["2026-overheid-gemeentewet"], vindplaats="art. 1")
    assert "vervangen" in cli.relatie(wiki, "aanvraag", "associatie (gericht)", "besluit", naam="leidt tot nu")
    assert [r["naam"] for r in beoordeling.laad(pad)["relaties"]] == ["leidt tot nu"]
    assert list(beoordeling.laad(pad)).index("relaties") < list(beoordeling.laad(pad)).index("status")
    cli.relatie(wiki, "aanvraag", "associatie (gericht)", "besluit", verwijder=True)
    assert "relaties" not in beoordeling.laad(pad)
    with pytest.raises(cli.Fout):
        cli.relatie(wiki, "aanvraag", "associatie", "bestaatniet")
    with pytest.raises(cli.Fout, match="schemafout"):
        cli.relatie(wiki, "aanvraag", "onzin", "besluit")


def test_besluit_met_tekst_of_advies(wiki):
    pad = wiki / "onderwerpen" / "demo" / "beoordelingen" / "besluit.yaml"
    cli.besluit(wiki, "besluit", "2026-10-15", "opnemen", tekst="Opnemen.", redenen=["reden"])
    cli.besluit(wiki, "besluit", "2026-10-16", "opnemen", advies_gevolgd=True)
    b = beoordeling.laad(pad)["besluiten"]
    assert b[0]["besluit"] == "Opnemen." and b[1] == {"datum": "2026-10-16", "gevolg": "opnemen", "advies": "gevolgd"}
    with pytest.raises(cli.Fout):
        cli.besluit(wiki, "besluit", "2026-10-17", "opnemen")


def test_compacte_waarschuwingen():
    w = ["a: x (regel Een)", "b: y (regel Een)", "c: z"]
    assert beslissen.compact(w, ["a"]) == ["waarschuwing: a: x (regel Een)",
                                           "2 andere waarschuwing(en), per regel: regel Een 1; overig 1 (alles tonen: --alles)"]
    assert len(beslissen.compact(w, [], alles=True)) == 3


def test_rapport_compact():
    uit = archimate_export.rapport_compact("# Kop\n\nTekst.\n\n## A\n- x\n- y\n\n## B\n- z\n")
    assert uit.startswith("# Kop") and "- A: 2 regel(s)" in uit and "- B: 1 regel(s)" in uit


def test_zoek_vindt_elk_begrip_van_de_wiki():
    alle = beoordeling.alle(WIKI, __import__("gam_gemeen").wiki_yaml(WIKI))
    for bid, (_, d) in alle.items():
        for naam in [d["begrip"], *(s["naam"] for s in d.get("synoniemen") or [])]:
            assert any(r.startswith(f"{bid} |") for r in cli.zoek(WIKI, [naam], alle)), (bid, naam)
