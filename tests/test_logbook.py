"""log.md: één tabel, leesbaar voor het oude kopformaat, en alleen aan te vullen."""
from llmwiki import lint, logbook

OUD = """# Logboek

Alleen aanvullen.
## [2026-09-29] promote | overlijden | Mark Backer | b48dbcac
## [2026-09-28] publish | MediaWiki:Sidebar | site | chat | 150af32e
"""


def test_lees_log_leest_oud_formaat_met_en_zonder_doel():
    regels = logbook.lees_log(OUD)
    assert regels == [
        logbook.Logregel("2026-09-29", "promote", "overlijden", "Mark Backer", "b48dbcac"),
        logbook.Logregel("2026-09-28", "publish", "MediaWiki:Sidebar", "chat", "150af32e", doel="site"),
    ]


def test_tabel_geeft_dezelfde_gebeurtenissen_als_oud_formaat():
    regels = logbook.lees_log(OUD)
    tabel = "# Logboek\n\n" + logbook.tabelkop(True) + "".join(logbook.tabelrij(r, True) for r in regels)
    assert logbook.lees_log(tabel) == regels


def test_append_log_zet_tabelkop_en_rij(tmp_path):
    (tmp_path / "wiki.yaml").write_text("type: curation\n", encoding="utf-8")
    (tmp_path / "log.md").write_text("# Logboek\n\nAlleen aanvullen.\n", encoding="utf-8")
    logbook.append_log(tmp_path, "promote", "urn", "Redacteur", "a" * 64)
    logbook.append_log(tmp_path, "promote", "graf", "Redacteur", "b" * 64)
    tekst = (tmp_path / "log.md").read_text(encoding="utf-8")
    assert tekst.count("| Datum | Actie | Id | Door | Hash |") == 1
    assert [r.id for r in logbook.lees_log(tekst)] == ["urn", "graf"]
    assert logbook.heeft_regel(tekst, "promote", "urn", "a" * 8)
    assert not logbook.heeft_regel(tekst, "promote", "urn", "b" * 8)


def test_append_log_sync_heeft_kolom_doel(tmp_path):
    (tmp_path / "wiki.yaml").write_text("type: sync\n", encoding="utf-8")
    logbook.append_log(tmp_path, "publish", "Contact", "chat", "c" * 64, doel="site")
    tekst = (tmp_path / "log.md").read_text(encoding="utf-8")
    assert "| Datum | Actie | Pagina | Doel | Door | Hash |" in tekst
    assert logbook.lees_log(tekst)[0].doel == "site"


def test_log_alleen_aanvullen_staat_omzetting_en_aanvulling_toe(tmp_path):
    regels = logbook.lees_log(OUD)
    nieuw = logbook.tabelkop(True) + "".join(logbook.tabelrij(r, True) for r in regels)
    nieuw += logbook.tabelrij(logbook.Logregel("2026-10-08", "publish", "Contact", "chat", "dddddddd", "site"), True)
    (tmp_path / "log.md").write_text(nieuw, encoding="utf-8")
    assert lint.check_log_alleen_aanvullen(tmp_path, {"log.md": OUD}) == []


def test_log_alleen_aanvullen_weigert_gewijzigde_gebeurtenis(tmp_path):
    (tmp_path / "log.md").write_text(OUD.replace("b48dbcac", "00000000"), encoding="utf-8")
    fouten = lint.check_log_alleen_aanvullen(tmp_path, {"log.md": OUD})
    assert fouten and "gebeurtenis 1" in fouten[0]


def test_log_alleen_aanvullen_weigert_verwijderde_gebeurtenis(tmp_path):
    (tmp_path / "log.md").write_text(OUD.splitlines()[3] + "\n", encoding="utf-8")
    assert lint.check_log_alleen_aanvullen(tmp_path, {"log.md": OUD})
