"""Tests voor de categorie-laag van sync.py (page_categories, subpage_titles,
category_tree) met een nep-pywikibot-module -- geen netwerk nodig."""
import sys
import types

import pytest

NS_BY_PREFIX = {"MediaWiki": 8, "Sjabloon": 10, "Template": 10, "Categorie": 14, "Category": 14}


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
        self.page_categories: dict[str, list[str]] = {}
        self.category_articles: dict[str, list[str]] = {}
        self.category_subcats: dict[str, list[str]] = {}

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
def sync_module(monkeypatch):
    fake_module = types.SimpleNamespace(Page=FakePage, Category=FakeCategory)
    monkeypatch.setitem(sys.modules, "pywikibot", fake_module)
    from llmwiki import sync

    return sync


def test_page_categories_returns_bare_names(sync_module):
    site = FakeSite()
    site.pages["Wat is GEMMA"] = {"text": "x", "revid": 1}
    site.page_categories["Wat is GEMMA"] = ["Actueel", "Landingspagina", "Over GEMMA"]
    assert sync_module.page_categories(site, "Wat is GEMMA") == ["Actueel", "Landingspagina", "Over GEMMA"]


def test_subpage_titles_only_same_namespace_and_prefix(sync_module):
    site = FakeSite()
    for t in ["Foo", "Foo/Bar", "Foo/Bar/Baz", "FooBar", "Sjabloon:Foo/Andere"]:
        site.pages[t] = {"text": "x", "revid": 1}
    assert sorted(sync_module.subpage_titles(site, "Foo")) == ["Foo/Bar", "Foo/Bar/Baz"]


def test_category_tree_walks_subcategories_and_yields_pad(sync_module):
    site = FakeSite()
    site.category_articles["Boven"] = ["PaginaA"]
    site.category_subcats["Boven"] = ["Onder"]
    site.category_articles["Onder"] = ["PaginaB"]
    for t in ["PaginaA", "PaginaB"]:
        site.pages[t] = {"text": "x", "revid": 1}

    entries = list(sync_module.category_tree(site, "Boven"))
    by_titel = {e.titel: e.categorie_pad for e in entries}
    assert by_titel == {"PaginaA": ["Boven"], "PaginaB": ["Boven", "Onder"]}


def test_category_tree_is_cycle_safe(sync_module):
    site = FakeSite()
    site.category_subcats["A"] = ["B"]
    site.category_subcats["B"] = ["A"]  # cyclus
    site.category_articles["A"] = ["PaginaA"]
    site.category_articles["B"] = ["PaginaB"]
    site.pages["PaginaA"] = {"text": "x", "revid": 1}
    site.pages["PaginaB"] = {"text": "x", "revid": 1}

    entries = list(sync_module.category_tree(site, "A"))
    assert {e.titel for e in entries} == {"PaginaA", "PaginaB"}
