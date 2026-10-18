"""tools/beoordeling.py: zoek, besluiten, toon --oordeel, zet, relatie en besluit; en de compacte uitvoer van beslissen."""
import pytest
import yaml

import beoordeling as cli
import beslissen
import archimate_export
from gam_hulp import KENMERKEN_BO, VELDEN_BO, WIKI
from llmwiki import beoordeling, paths


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
        data = {"begrip": naam, "onderwerpen": ["demo"], **VELDEN_BO, "kenmerken": _kenmerken(), "definitie": f"Definitie {naam}.",
                **extra, "beslist": {"uitkomst": {"soort": "element", "archimate_type": "business-object"}}, "status": "review"}
        beoordeling.schrijf(wiki / "onderwerpen" / "demo" / "beoordelingen" / f"{bid}.yaml", data)  # nog met beslist erin
    beoordeling.schrijf_beslist(beoordeling.alle(wiki, paths.load_wiki_yaml(wiki)), paths.load_wiki_yaml(wiki))
    for p in (wiki / "onderwerpen" / "demo" / "beoordelingen").glob("*.yaml"):
        beoordeling.schrijf(p, beoordeling.laad(p), paths.load_wiki_yaml(wiki))
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
    cli.besluit(wiki, "besluit", "2026-10-02", "verwerkt", "Breder begrip boven Beschikking.")
    uit = cli.besluiten(wiki, "demo")
    assert uit[0].startswith("[demo] 2026-10-01") and "verwerkt (logica): Breder begrip" in uit[1]
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
    assert data["status"] == "review" and "beslist" not in data       # beslist staat in beslist.yaml naast de map
    assert cli._alle(wiki)["aanvraag"][1]["beslist"]["uitkomst"]["archimate_type"] == "business-object"
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


def test_besluit_met_tekst(wiki):
    pad = wiki / "onderwerpen" / "demo" / "beoordelingen" / "besluit.yaml"
    cli.besluit(wiki, "besluit", "2026-10-15", "verwerkt", "Breder begrip.")
    assert beoordeling.laad(pad)["besluiten"][-1] == {"datum": "2026-10-15", "besluit": "Breder begrip.",
                                                      "gevolg": "verwerkt", "zekerheid": "logica"}
    cli.besluit(wiki, "besluit", "2026-10-16", "verwerkt", "Volgens de wet.", zekerheid="kennis")
    assert beoordeling.laad(pad)["besluiten"][-1]["zekerheid"] == "kennis"
    assert any("(kennis): Volgens de wet." in r for r in cli.besluiten(wiki, "demo"))


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


def test_regel_naar_antwoord():
    assert cli.regel_naar_antwoord("x", "ja — Want art. 1 [2024-wet-a, id-123]") == {
        "waarde": "ja", "onderbouwing": "Want art. 1", "bronnen": ["2024-wet-a"], "gemma_relatie": ["id-123"]}
    assert cli.regel_naar_antwoord("x", "nee - Feitelijk handelen [zie boven]") == {
        "waarde": "nee", "onderbouwing": "Feitelijk handelen [zie boven]"}
    for fout in ("misschien", "ja", "nee", "ja [2024-wet-a]"):
        with pytest.raises(cli.Fout):
            cli.regel_naar_antwoord("x", fout)


def test_normaliseer_schrijfvorm_en_nee_buiten_het_pad(wiki):
    pad = wiki / "onderwerpen" / "demo" / "beoordelingen" / "aanvraag.yaml"
    data = beoordeling.laad(pad)
    data["kenmerken"]["herkenbaar"] = "ja — Komt in de Awb voor [2024-wet-a]"
    data["kenmerken"]["afspraak"] = "nee — Geen overeenkomst"
    data["kenmerken"]["eigen_besluit"]["bronnen"] = ["2024-wet-a"]  # buiten het pad, met bron: blijft
    beoordeling.schrijf(pad, data)
    uit = cli.normaliseer(wiki, ["aanvraag"])
    assert uit[0].startswith("aanvraag: genormaliseerd (") and uit[-1] == "Draai tools/beslissen.py."
    kenmerken = beoordeling.laad(pad)["kenmerken"]
    assert kenmerken["herkenbaar"] == {"waarde": "ja", "onderbouwing": "Komt in de Awb voor", "bronnen": ["2024-wet-a"]}
    assert kenmerken["afspraak"] == {"waarde": "nee", "onderbouwing": "Geen overeenkomst"} and "eigen_besluit" in kenmerken
    assert "klant_tot_klant" not in kenmerken and "afspraak" in kenmerken  # buiten het pad weg, op het pad blijft
    assert list(kenmerken) == [s for s in cli.bepaal_type.SLEUTELS if s in kenmerken]
    assert cli.normaliseer(wiki, ["aanvraag"]) == ["Niets te normaliseren."]
    del kenmerken["afspraak"]
    beoordeling.schrijf(pad, {**beoordeling.laad(pad), "kenmerken": kenmerken})
    assert cli.normaliseer(wiki, ["aanvraag"]) == ["aanvraag: op het pad nog niet beantwoord: afspraak"]
    with pytest.raises(cli.Fout):
        cli.normaliseer(wiki, [])


def test_zet_kenmerk_in_schrijfvorm(wiki):
    cli.normaliseer(wiki, ["besluit"])
    with pytest.raises(cli.Fout):
        cli.zet(wiki, "besluit", "kenmerken.afspraak", "nee")   # een nee heeft een onderbouwing
    cli.zet(wiki, "besluit", "kenmerken.afspraak", "nee — Een eenzijdig besluit")
    kenmerken = beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "besluit.yaml")["kenmerken"]
    assert kenmerken["afspraak"] == {"waarde": "nee", "onderbouwing": "Een eenzijdig besluit"}


def _sjabloon_wiki(archimate_repo):
    _, wiki = archimate_repo
    (wiki / "onderwerpen" / "demo" / "beoordelingen").mkdir(parents=True)
    (wiki / "onderwerpen" / "demo" / "afbakening.yaml").write_text(yaml.safe_dump(
        {"naam": "Demo", "niveau": "eigen", "besluiten": [{"datum": "2026-10-01", "besluit": "Afbakening", "gevolg": "opnemen"}]}),
        encoding="utf-8")
    bd = wiki / "onderwerpen" / "demo" / "bronduidingen" / "rijksregelgeving"
    bd.mkdir(parents=True)
    (bd / "2026-overheid-gemeentewet.md").write_text("# Gemeentewet\n", encoding="utf-8")
    return wiki


def _bron_vervang(wiki, bid):
    """Vervang elke TODO door een tekst, zoals de AI doet."""
    import sjablonen

    pad = wiki / "onderwerpen" / "demo" / "beoordelingen" / f"{bid}.yaml"
    tekst = pad.read_text(encoding="utf-8")
    pad.write_text(tekst.replace(sjablonen.TODO + ": ", "Onderbouwd: "), encoding="utf-8")


def test_sjabloon_dienst_met_nieuw_proces_komt_door_beslissen(archimate_repo):
    wiki = _sjabloon_wiki(archimate_repo)
    import sjablonen

    p = sjablonen.Params("beroep", "Beroep", "demo", "besluit", ["2026-overheid-gemeentewet"], upl_nr="54",
                         taakveld="0 Bestuur en Ondersteuning", beleidsdomein="Besluitvorming", domein="Bestuur",
                         proces_naam="Voeren verweer in beroep", toegang="raadplegen")
    # het kernobject moet bestaan
    bo = {"begrip": "Besluit", "onderwerpen": ["demo"], **VELDEN_BO, "kenmerken": _kenmerken(), "definitie": "Besluit.",
          "beslist": {"uitkomst": {"soort": "element", "archimate_type": "business-object"}}, "status": "review"}
    beoordeling.schrijf(wiki / "onderwerpen" / "demo" / "beoordelingen" / "besluit.yaml", bo)
    uit = cli.sjabloon(wiki, "upl-dienst", p)
    assert uit[0].startswith("beroep: klaargezet") and uit[1].startswith("voeren-verweer-in-beroep: klaargezet")
    dienst = beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "beroep.yaml")
    assert "status" not in dienst and "beslist" not in dienst
    assert dienst["vak"] == "bedrijf/gedrag-extern" and dienst["bronnen"] == ["2026-overheid-gemeentewet"]
    assert dienst["kenmerken"]["gerealiseerd_door"] == {"waarde": "ja", "naar": ["voeren-verweer-in-beroep"]}
    assert dienst["kenmerken"]["afnemer"]["bronnen"] == ["2026-overheid-gemeentewet"]
    res = beslissen.beslissen(wiki, schrijven=False)
    assert any("beroep: nog een TODO" in f for f in res.fouten)          # de onderbouwing is verplicht
    assert not any("kenmerken" in f and "pad" in f for f in res.fouten)
    for bid in ("beroep", "voeren-verweer-in-beroep"):
        _bron_vervang(wiki, bid)
    res = beslissen.beslissen(wiki, schrijven=False)
    assert not [f for f in res.fouten if f.startswith(("beroep:", "voeren-verweer-in-beroep:"))], res.fouten
    assert res.uitkomsten["beroep"]["paginatype"] == "dienst"
    assert res.uitkomsten["voeren-verweer-in-beroep"]["paginatype"] == "bedrijfsproces"


def test_sjabloon_bestaand_proces_krijgt_realisatie_en_bestaande_beoordeling_blijft(archimate_repo):
    wiki = _sjabloon_wiki(archimate_repo)
    import sjablonen

    for bid in ("besluit", "behandelen"):
        beoordeling.schrijf(wiki / "onderwerpen" / "demo" / "beoordelingen" / f"{bid}.yaml",
                            {"begrip": bid, "onderwerpen": ["demo"], **VELDEN_BO, "kenmerken": _kenmerken()})
    p = sjablonen.Params("beschikking-aanvragen", "Beschikking aanvragen", "demo", "besluit", ["2026-overheid-gemeentewet"],
                         proces="behandelen")
    uit = cli.sjabloon(wiki, "upl-dienst", p)
    assert uit[0].startswith("beschikking-aanvragen: klaargezet") and "relatie realisatie naar beschikking-aanvragen" in uit[1]
    proces = beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "behandelen.yaml")
    assert proces["relaties"][0]["naar"] == "beschikking-aanvragen" and proces["kenmerken"]
    with pytest.raises(cli.Fout, match="bestaat al"):
        cli.sjabloon(wiki, "upl-dienst", p)


def test_sjabloon_weigert_onbekend_onderwerp_kernobject_en_foute_opties(archimate_repo):
    wiki = _sjabloon_wiki(archimate_repo)
    import sjablonen

    basis = dict(id="d", naam="D", onderwerp="demo", kernobject="bestaatniet", bronnen=["2026-overheid-gemeentewet"],
                 proces_naam="P")
    with pytest.raises(cli.Fout, match="geen beoordeling 'bestaatniet'"):
        cli.sjabloon(wiki, "upl-dienst", sjablonen.Params(**basis))
    with pytest.raises(cli.Fout, match="onderwerp 'nergens'"):
        cli.sjabloon(wiki, "upl-dienst", sjablonen.Params(**{**basis, "onderwerp": "nergens"}))
    with pytest.raises(cli.Fout, match="--bron"):
        cli.sjabloon(wiki, "upl-dienst", sjablonen.Params(**{**basis, "bronnen": []}))
    with pytest.raises(cli.Fout, match="niet beide"):
        cli.sjabloon(wiki, "upl-dienst", sjablonen.Params(**{**basis, "proces": "x"}))
    assert not list((wiki / "onderwerpen" / "demo" / "beoordelingen").glob("*.yaml"))


def test_beslist_staat_apart_en_alle_voegt_het_samen(wiki):
    yaml_ = paths.load_wiki_yaml(wiki)
    bestand = wiki / "onderwerpen" / "demo" / "beslist.yaml"
    assert set(yaml.safe_load(bestand.read_text(encoding="utf-8"))) == {"aanvraag", "aanvraag-reisdocument", "besluit"}
    assert bestand.read_text(encoding="utf-8").startswith("# Gegenereerd")
    alle = beoordeling.alle(wiki, yaml_)
    assert all(d["beslist"]["uitkomst"]["soort"] == "element" for _, d in alle.values())
    assert beoordeling.schrijf_beslist(alle, yaml_) == []                  # ongewijzigd: niets geschreven
    assert "beslist" not in beoordeling.laad(wiki / "onderwerpen" / "demo" / "beoordelingen" / "besluit.yaml")
    hash_ = beoordeling.inhoud_hash(alle["besluit"][1])
    alle["besluit"][1]["beslist"]["open"] = ["iets"]                       # een ander blok: wel het bestand, niet het akkoord-hash
    assert beoordeling.schrijf_beslist(alle, yaml_) == [bestand]
    assert beoordeling.inhoud_hash(beoordeling.alle(wiki, yaml_)["besluit"][1]) == hash_
