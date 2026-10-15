"""De hash van het akkoord dekt de inhoud van een beoordeling, niet de scriptvelden en niet de besluiten."""
from llmwiki import beoordeling


BASIS = {"begrip": "Graf", "kenmerken": {"gemeentelijk": {"waarde": "ja"}}, "status": "review",
         "beslist": {"uitkomst": {"soort": "element"}}, "besluiten": [{"datum": "2026-10-01", "besluit": "Opnemen."}]}


def test_besluit_wijzigen_laat_de_hash_gelijk():
    zonder = {k: v for k, v in BASIS.items() if k != "besluiten"}
    ander = {**BASIS, "besluiten": [{"datum": "2026-10-15", "besluit": "Anders.", "zekerheid": "kennis"}]}
    assert beoordeling.inhoud_hash(BASIS) == beoordeling.inhoud_hash(zonder) == beoordeling.inhoud_hash(ander)


def test_scriptvelden_laten_de_hash_gelijk():
    assert beoordeling.inhoud_hash(BASIS) == beoordeling.inhoud_hash({**BASIS, "status": "goedgekeurd", "beslist": {}})


def test_inhoud_wijzigen_verandert_de_hash():
    ander = {**BASIS, "kenmerken": {"gemeentelijk": {"waarde": "nee"}}}
    assert beoordeling.inhoud_hash(BASIS) != beoordeling.inhoud_hash(ander)


def test_inhoud_houdt_de_besluiten_voor_het_terugschrijven():
    assert "besluiten" in beoordeling.inhoud(BASIS)
