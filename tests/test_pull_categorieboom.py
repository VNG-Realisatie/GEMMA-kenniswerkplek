"""Tests voor 'llmwiki pull --categorieboom' (bulk-import per categorie,
content.layout: category) met een nep-pywikibot-module."""
import argparse
import json
import sys
import types

import pytest
import yaml

NS_BY_PREFIX = {"MediaWiki": 8, "Sjabloon": 10, "Bestand": 6, "Categorie": 14, "Category": 14}


class FakePage:
    def __init__(self, site, title):
        self.site = site
        self.title_ = title

    def title(self, with_ns=True):
        if with_ns or ":" not in self.title_:
            return self.title_
        return self.title_.split(":", 1)[1]

    def namespace(self):
        prefix = self.title_.split(":", 1)[0] if ":" in self.title_ else None
        return types.SimpleNamespace(id=NS_BY_PREFIX.get(prefix, 0))

    def exists(self):
        return self.title_ in self.site.pages

    @property
    def text(self):
        return self.site.pages[self.title_]["text"]

    @property
    def latest_revision_id(self):
        return self.site.pages[self.title_]["revid"]

    def categories(self):
        return [FakeCategory(self.site, c) for c in self.site.page_categories.get(self.title_, [])]


class FakeCategory(FakePage):
    def __init__(self, site, title):
        if not title.startswith(("Categorie:", "Category:")):
            title = "Categorie:" + title
        super().__init__(site, title)

    def articles(self, recurse=False):
        bare = self.title(with_ns=False)
        return [FakePage(self.site, t) for t in self.site.category_articles.get(bare, [])]

    def subcategories(self):
        bare = self.title(with_ns=False)
        return [FakeCategory(self.site, t) for t in self.site.category_subcats.get(bare, [])]


class FakeSite:
    def __init__(self):
        self.pages: dict[str, dict] = {}
        self.category_articles: dict[str, list[str]] = {}
        self.category_subcats: dict[str, list[str]] = {}
        self.page_categories: dict[str, list[str]] = {}

    def allpages(self, prefix="", namespace=0, total=None):
        out = []
        for t in self.pages:
            if FakePage(self, t).namespace().id != namespace:
                continue
            bare_t = t.split(":", 1)[1] if ":" in t else t
            if bare_t.startswith(prefix):
                out.append(FakePage(self, t))
        return out[:total] if total else out


@pytest.fixture
def cli_module(monkeypatch):
    fake_module = types.SimpleNamespace(Page=FakePage, Category=FakeCategory)
    monkeypatch.setitem(sys.modules, "pywikibot", fake_module)
    from llmwiki import cli

    return cli


@pytest.fixture
def wiki_root(tmp_path):
    root = tmp_path / "repo"
    (root / "wikis" / "gemma" / "content").mkdir(parents=True)
    wiki_yaml = {
        "key": "gemma",
        "type": "sync",
        "site": {"family": "gemmaonline", "code": "en"},
        "content": {"layout": "category", "namespaces": [0, 8]},
    }
    wiki_dir = root / "wikis" / "gemma"
    (wiki_dir / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")
    return wiki_dir, wiki_yaml


def _args(**overrides):
    base = dict(categorieboom="Boven", categorie=None, titel=None, skip_if_match=None, dry_run=False, force=False)
    base.update(overrides)
    return argparse.Namespace(**base)


def test_categorieboom_places_pages_under_namespace_and_categorie(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.category_articles["Boven"] = ["PaginaA", "MediaWiki:Widget", "Bestand:Img.png"]
    site.category_subcats["Boven"] = ["Onder"]
    site.category_articles["Onder"] = ["PaginaB"]
    site.pages["PaginaA"] = {"text": "Inhoud A", "revid": 1}
    site.pages["MediaWiki:Widget"] = {"text": "Inhoud Widget", "revid": 2}
    site.pages["Bestand:Img.png"] = {"text": "n.v.t.", "revid": 3}
    site.pages["PaginaB"] = {"text": "Inhoud B", "revid": 4}

    rc = cli_module._pull_categorieboom(root, wiki_yaml, site, "site", _args())
    assert rc == 0

    assert (root / "content/main/Boven/PaginaA.wiki").read_text() == "Inhoud A"
    assert (root / "content/mediawiki/Boven/Widget.wiki").read_text() == "Inhoud Widget"
    assert (root / "content/main/Boven/Onder/PaginaB.wiki").read_text() == "Inhoud B"
    # Bestand: (namespace 6) staat niet in content.namespaces -> nooit opgehaald
    assert list((root / "content").rglob("Img*")) == []

    revisies = json.loads((root / "revisies.json").read_text())
    assert revisies["content/main/Boven/PaginaA.wiki"] == {"titel": "PaginaA", "revid": 1}


def test_categorieboom_includes_subpages_as_hard_link(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.category_articles["Boven"] = ["PaginaA"]
    site.pages["PaginaA"] = {"text": "Inhoud A", "revid": 1}
    site.pages["PaginaA/Sub"] = {"text": "Inhoud Sub", "revid": 2}

    rc = cli_module._pull_categorieboom(root, wiki_yaml, site, "site", _args())
    assert rc == 0

    # PaginaA heeft nu zelf een subpagina -> eigen inhoud verhuist naar _index
    assert (root / "content/main/Boven/PaginaA/_index.wiki").read_text() == "Inhoud A"
    assert (root / "content/main/Boven/PaginaA/Sub.wiki").read_text() == "Inhoud Sub"


def test_categorieboom_skip_if_match_excludes_page_but_not_its_subpages(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.category_articles["Boven"] = ["PaginaA", "PaginaB"]
    site.pages["PaginaA"] = {"text": "Redactiestatus=Gearchiveerd", "revid": 1}
    site.pages["PaginaB"] = {"text": "Inhoud B", "revid": 2}

    rc = cli_module._pull_categorieboom(root, wiki_yaml, site, "site", _args(skip_if_match="Gearchiveerd"))
    assert rc == 0

    assert not (root / "content/main/Boven/PaginaA.wiki").exists()
    assert (root / "content/main/Boven/PaginaB.wiki").read_text() == "Inhoud B"


def test_categorieboom_dry_run_writes_nothing(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.category_articles["Boven"] = ["PaginaA"]
    site.pages["PaginaA"] = {"text": "Inhoud A", "revid": 1}

    rc = cli_module._pull_categorieboom(root, wiki_yaml, site, "site", _args(dry_run=True))
    assert rc == 0
    assert not (root / "content/main/Boven/PaginaA.wiki").exists()
    assert not (root / "revisies.json").exists()


def test_categorieboom_requires_category_layout(cli_module, tmp_path):
    root = tmp_path / "repo" / "wikis" / "gemma"
    root.mkdir(parents=True)
    wiki_yaml = {"key": "gemma", "type": "sync", "content": {"layout": "namespace", "namespaces": [0]}}
    site = FakeSite()
    rc = cli_module._pull_categorieboom(root, wiki_yaml, site, "site", _args())
    assert rc == 1


def test_resolve_categorie_pad_zonder_categorie_is_none(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.pages["PaginaA"] = {"text": "x", "revid": 1}
    assert cli_module._resolve_categorie_pad(root, site, wiki_yaml, "PaginaA", None) is None


def test_resolve_categorie_pad_eén_categorie_automatisch_en_krijgt_voorrang(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.pages["PaginaA"] = {"text": "x", "revid": 1}
    site.page_categories["PaginaA"] = ["Landingspagina"]
    assert cli_module._resolve_categorie_pad(root, site, wiki_yaml, "PaginaA", None) == ["Landingspagina"]
    assert cli_module._load_categorie_voorrang(root) == ["Landingspagina"]


def test_resolve_categorie_pad_meerdere_categorieën_vereist_override(cli_module, wiki_root):
    from llmwiki import sync as sync_module

    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.pages["PaginaA"] = {"text": "x", "revid": 1}
    site.page_categories["PaginaA"] = ["Landingspagina", "Over GEMMA"]
    with pytest.raises(sync_module.SyncError):
        cli_module._resolve_categorie_pad(root, site, wiki_yaml, "PaginaA", None)
    assert cli_module._resolve_categorie_pad(root, site, wiki_yaml, "PaginaA", "Over GEMMA") == ["Over GEMMA"]


def test_resolve_categorie_pad_voorrang_lost_volgende_ambiguïteit_automatisch_op(cli_module, wiki_root):
    root, wiki_yaml = wiki_root
    site = FakeSite()
    site.pages["Wat is GEMMA"] = {"text": "x", "revid": 1}
    site.page_categories["Wat is GEMMA"] = ["Actueel", "Landingspagina", "Over GEMMA", "SmartPublish-Watched"]
    # Landingspagina expliciet gekozen voor deze pagina -> krijgt voorrang.
    cli_module._resolve_categorie_pad(root, site, wiki_yaml, "Wat is GEMMA", "Landingspagina")

    site.pages["Andere pagina"] = {"text": "x", "revid": 1}
    site.page_categories["Andere pagina"] = ["Actueel", "Landingspagina"]
    # Van de 2 categorieën heeft precies 1 (Landingspagina) al voorrang -> geen nieuwe vraag.
    assert cli_module._resolve_categorie_pad(root, site, wiki_yaml, "Andere pagina", None) == ["Landingspagina"]


def test_resolve_categorie_pad_twee_voorrangscategorieën_moet_alsnog_vragen(cli_module, wiki_root):
    from llmwiki import sync as sync_module

    root, wiki_yaml = wiki_root
    site = FakeSite()
    cli_module._geef_voorrang(root, "Landingspagina")
    cli_module._geef_voorrang(root, "Over GEMMA")

    site.pages["PaginaC"] = {"text": "x", "revid": 1}
    site.page_categories["PaginaC"] = ["Landingspagina", "Over GEMMA"]
    with pytest.raises(sync_module.SyncError):
        cli_module._resolve_categorie_pad(root, site, wiki_yaml, "PaginaC", None)
