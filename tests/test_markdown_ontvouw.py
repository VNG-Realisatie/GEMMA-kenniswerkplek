"""Harde regelovergangen binnen alinea's verwijderen, zonder blokken aan te tasten."""
from llmwiki.markdown import bestanden, ontvouw


def test_alinea_en_lijstitem_worden_een_regel():
    tekst = "Eerste regel\nloopt door.\n\n- item een\n  loopt door\n- item twee\n\n1. stap\n   verder\n"
    assert ontvouw(tekst) == "Eerste regel loopt door.\n\n- item een loopt door\n- item twee\n\n1. stap verder\n"


def test_blokken_blijven_heel():
    tekst = ("---\nid: x\ndescription: a\n  b\n---\n\n# Kop\nTekst\n\n```text\nregel 1\nregel 2\n```\n\n"
             "| a | b |\n|---|---|\n| 1 | 2 |\n\n<!-- marker -->\nNa marker\n---\nNa lijn\n")
    assert ontvouw(tekst) == tekst


def test_bewuste_overgang_en_lijst_na_alinea():
    assert ontvouw("regel met twee spaties  \nvolgende\n") == "regel met twee spaties  \nvolgende\n"
    assert ontvouw("Regels:\n- een\n- twee\n") == "Regels:\n- een\n- twee\n"


def test_blockquote():
    assert ontvouw("> citaat\n> loopt door\n>\n> nieuwe alinea\n") == "> citaat loopt door\n>\n> nieuwe alinea\n"
    assert ontvouw("Tekst\n> citaat\n") == "Tekst\n> citaat\n"


def test_ingesprongen_fence_in_lijst():
    tekst = "1. Stap:\n   ```yaml\n   a: 1\n   b: 2\n   ```\n2. Volgende\n"
    assert ontvouw(tekst) == tekst


def test_idempotent():
    tekst = "a\nb\n\n- c\n  d\n"
    assert ontvouw(ontvouw(tekst)) == ontvouw(tekst)


def test_bestanden_sluit_bronnen_werkkopie_en_logboek_uit(tmp_path):
    for pad in ["AGENTS.md", "sources/raw/x.md", "sources/index/x.md", "wikis/w/content/p.md", "wikis/w/log.md",
                "wikis/w/AGENTS.md", ".work/runs/r/x.md", "Prompt en antwoorden/a.md"]:
        (tmp_path / pad).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / pad).write_text("x\n", encoding="utf-8")
    namen = [p.relative_to(tmp_path).as_posix() for p in bestanden(tmp_path)]
    assert namen == ["AGENTS.md", "sources/index/x.md", "wikis/w/AGENTS.md"]
