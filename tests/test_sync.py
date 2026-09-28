"""Tests voor sync.py met een nep-pywikibot-module -- geen netwerk, geen echte
pywikibot-installatie nodig."""
import sys
import types

import pytest


class FakePage:
    def __init__(self, site, title):
        self.site = site
        self.title_ = title

    def exists(self):
        return self.title_ in self.site.pages

    @property
    def text(self):
        return self.site.pages[self.title_]["text"]

    @text.setter
    def text(self, value):
        self._pending_text = value

    @property
    def latest_revision_id(self):
        return self.site.pages[self.title_]["revid"]

    def save(self, summary, minor=False):
        current = self.site.pages.get(self.title_, {"revid": 0})
        self.site.pages[self.title_] = {
            "text": self._pending_text,
            "revid": current["revid"] + 1,
        }


class FakeSite:
    def __init__(self, pages=None):
        self.pages = pages or {}

    def preloadpages(self, pages):
        return list(pages)


@pytest.fixture(autouse=True)
def fake_pywikibot(monkeypatch):
    fake_module = types.SimpleNamespace(Page=FakePage)
    monkeypatch.setitem(sys.modules, "pywikibot", fake_module)


@pytest.fixture
def sync_module():
    from llmwiki import sync

    return sync


def test_pull_page_returns_text_and_revid(sync_module):
    site = FakeSite({"Foo": {"text": "hallo", "revid": 5}})
    result = sync_module.pull_page(site, "Foo")
    assert result.text == "hallo"
    assert result.revid == 5


def test_pull_page_missing_raises(sync_module):
    site = FakeSite({})
    with pytest.raises(sync_module.SyncError):
        sync_module.pull_page(site, "Onbekend")


def test_pull_pages_batches(sync_module):
    site = FakeSite({"A": {"text": "a", "revid": 1}, "B": {"text": "b", "revid": 2}})
    result = sync_module.pull_pages(site, ["A", "B"])
    assert set(result) == {"A", "B"}
    assert result["A"].revid == 1


def test_push_page_succeeds_without_conflict(sync_module):
    site = FakeSite({"Foo": {"text": "oud", "revid": 5}})
    result = sync_module.push_page(site, "Foo", "nieuw", base_revid=5, summary="test")
    assert result.text == "nieuw"
    assert result.revid == 6


def test_push_page_new_page_has_no_base_revid(sync_module):
    site = FakeSite({})
    result = sync_module.push_page(site, "Nieuw", "inhoud", base_revid=None, summary="test")
    assert result.revid == 1


def test_push_page_conflict_is_detected(sync_module):
    site = FakeSite({"Foo": {"text": "live-gewijzigd", "revid": 7}})
    with pytest.raises(sync_module.ConflictError):
        sync_module.push_page(site, "Foo", "mijn-versie", base_revid=5, summary="test")


def test_push_page_tolerates_trailing_newline_normalisation(sync_module):
    class NormalizingPage(FakePage):
        def save(self, summary, minor=False):
            current = self.site.pages.get(self.title_, {"revid": 0})
            # MediaWiki normaliseert: bewaar zonder trailing newline
            self.site.pages[self.title_] = {
                "text": self._pending_text.rstrip("\n"),
                "revid": current["revid"] + 1,
            }

    import sys as _sys

    _sys.modules["pywikibot"] = types.SimpleNamespace(Page=NormalizingPage)
    from llmwiki import sync

    site = FakeSite({"Foo": {"text": "oud", "revid": 1}})
    result = sync.push_page(site, "Foo", "nieuw\n", base_revid=1, summary="test")
    assert result.text == "nieuw"
