"""Tests voor de sync-tak van gate.py, met een nep-pywikibot-module (geen
netwerk, geen echte pywikibot-installatie)."""
import json
import sys
import types

import pytest
import yaml

from llmwiki import gate, paths, runs


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

    def namespace(self):
        return types.SimpleNamespace(id=0)

    def save(self, summary, minor=False):
        current = self.site.pages.get(self.title_, {"revid": 0})
        self.site.pages[self.title_] = {"text": self._pending_text, "revid": current["revid"] + 1}


class FakeSite:
    def __init__(self, code, family):
        self.code = code
        self.family = family
        self.pages: dict[str, dict] = {}

    def login(self):
        pass

    def preloadpages(self, pages):
        return list(pages)


@pytest.fixture
def fake_pywikibot(monkeypatch):
    site_registry: dict[tuple[str, str], FakeSite] = {}

    def _site_factory(code, family):
        key = (code, family)
        if key not in site_registry:
            site_registry[key] = FakeSite(code, family)
        return site_registry[key]

    fake_module = types.SimpleNamespace(Site=_site_factory, Page=FakePage)
    monkeypatch.setitem(sys.modules, "pywikibot", fake_module)
    return site_registry


@pytest.fixture
def sync_repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    (root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")

    wiki_root = root / "wikis" / "template"
    (wiki_root / "content" / "main").mkdir(parents=True)
    (wiki_root / "voorstellen").mkdir()
    (wiki_root / ".work").mkdir()

    wiki_yaml = {
        "key": "template",
        "type": "sync",
        "site": {"family": "gemmaonline", "code": "en"},
        "test_targets": {"staging": {"family": "gemmaonline", "code": "staging"}},
        "publish": {"approval": "chat"},
    }
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")
    (wiki_root / "revisies.json").write_text("{}", encoding="utf-8")
    (wiki_root / "log.md").write_text("# Logboek\n", encoding="utf-8")
    return root, wiki_root


def _complete(wiki_root, wiki_yaml, run_id, phase, data):
    import tempfile
    from pathlib import Path

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(data, fh)
        path = Path(fh.name)
    runs.complete(wiki_root, wiki_yaml, run_id, phase, path)
    path.unlink()


def _start_run_through_validate(wiki_root, wiki_yaml):
    state = runs.start(wiki_root, wiki_yaml, "wiki-edit")
    run_id = state["run_id"]
    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "validate",
        {"run": run_id, "controles": [{"naam": "wikitext", "resultaat": "ok", "ernst": "info"}]},
    )
    return run_id


def test_plan_and_apply_publishes_new_page(sync_repo, fake_pywikibot):
    root, wiki_root = sync_repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _start_run_through_validate(wiki_root, wiki_yaml)

    content_path = wiki_root / "content" / "main" / "Contact.wiki"
    content_path.write_text("Nieuwe inhoud.\n", encoding="utf-8")

    gate.plan(wiki_root, wiki_yaml, run_id, paths=["content/main/Contact.wiki"], titel_overrides={"content/main/Contact.wiki": "Contact"})
    gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD")

    site = fake_pywikibot[("en", "gemmaonline")]
    assert site.pages["Contact"]["text"].rstrip("\n") == "Nieuwe inhoud."

    revisies = json.loads((wiki_root / "revisies.json").read_text())
    assert revisies["content/main/Contact.wiki"]["titel"] == "Contact"

    log_text = (wiki_root / "log.md").read_text()
    assert "Contact" in log_text
    assert "| site |" in log_text


def test_apply_to_staging_logs_the_doel(sync_repo, fake_pywikibot):
    root, wiki_root = sync_repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _start_run_through_validate(wiki_root, wiki_yaml)

    content_path = wiki_root / "content" / "main" / "Contact.wiki"
    content_path.write_text("Nieuwe inhoud.\n", encoding="utf-8")

    gate.plan(
        wiki_root, wiki_yaml, run_id, doel="staging",
        paths=["content/main/Contact.wiki"], titel_overrides={"content/main/Contact.wiki": "Contact"},
    )
    gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD", doel="staging")

    log_text = (wiki_root / "log.md").read_text()
    assert "| staging |" in log_text


def test_apply_detects_conflict_when_live_page_changed_since_plan(sync_repo, fake_pywikibot):
    root, wiki_root = sync_repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _start_run_through_validate(wiki_root, wiki_yaml)

    fake_pywikibot[("en", "gemmaonline")] = FakeSite("en", "gemmaonline")
    site = fake_pywikibot[("en", "gemmaonline")]
    site.pages["Contact"] = {"text": "bestaand", "revid": 1}
    (wiki_root / "revisies.json").write_text(
        json.dumps({"content/main/Contact.wiki": {"titel": "Contact", "revid": 1}}), encoding="utf-8"
    )

    content_path = wiki_root / "content" / "main" / "Contact.wiki"
    content_path.write_text("Mijn wijziging.\n", encoding="utf-8")

    gate.plan(wiki_root, wiki_yaml, run_id, paths=["content/main/Contact.wiki"])

    # Iemand anders wijzigt de live pagina na het maken van het voorstel.
    site.pages["Contact"] = {"text": "externe wijziging", "revid": 2}

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD")


def test_plan_without_known_title_requires_override(sync_repo, fake_pywikibot):
    root, wiki_root = sync_repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _start_run_through_validate(wiki_root, wiki_yaml)

    content_path = wiki_root / "content" / "main" / "Onbekend.wiki"
    content_path.write_text("x\n", encoding="utf-8")

    with pytest.raises(gate.GateError):
        gate.plan(wiki_root, wiki_yaml, run_id, paths=["content/main/Onbekend.wiki"])


def test_apply_document_mode_for_sync(sync_repo, fake_pywikibot):
    from llmwiki import frontmatter

    root, wiki_root = sync_repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    wiki_yaml["publish"]["approval"] = "document"
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")

    run_id = _start_run_through_validate(wiki_root, wiki_yaml)
    content_path = wiki_root / "content" / "main" / "Contact.wiki"
    content_path.write_text("Inhoud.\n", encoding="utf-8")

    gate.plan(
        wiki_root, wiki_yaml, run_id,
        paths=["content/main/Contact.wiki"],
        titel_overrides={"content/main/Contact.wiki": "Contact"},
    )

    voorstel_path = wiki_root / "voorstellen" / f"{run_id}.md"
    page = frontmatter.read(voorstel_path)
    page.meta["akkoord_voor_publicatie"] = "ja"
    page.meta["beoordeeld_door"] = "M. Jansen"
    frontmatter.write(voorstel_path, page)

    gate.apply(wiki_root, wiki_yaml, run_id)
    site = fake_pywikibot[("en", "gemmaonline")]
    assert site.pages["Contact"]["text"].rstrip("\n") == "Inhoud."
