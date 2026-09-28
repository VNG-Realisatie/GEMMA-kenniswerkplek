"""Pywikibot-laag voor sync-wiki's. Zie docs/onderbouwing.md 5.10 voor de reden:
credentials en Basic-Auth voor een testomgeving blijven volledig in pywikibots
eigen ~/.pywikibot/user-config.py (password_file, authenticate-dict); dit
bestand construeert nooit zelf een Site, credentials of authenticate-config.
"""
from __future__ import annotations

from dataclasses import dataclass


class SyncError(RuntimeError):
    pass


class ConflictError(SyncError):
    """Live revisie wijkt af van de bekende basisrevisie."""


def _import_pywikibot():
    try:
        import pywikibot
    except ImportError as exc:
        raise SyncError("pywikibot ontbreekt. Draai 'uv sync --extra mediawiki'.") from exc
    return pywikibot


@dataclass
class PageResult:
    title: str
    text: str
    revid: int
    namespace: int = 0
    contentmodel: str = "wikitext"


def _target(wiki_yaml: dict, doel: str) -> dict:
    if doel == "site":
        return wiki_yaml["site"]
    try:
        return wiki_yaml["test_targets"][doel]
    except KeyError as exc:
        raise SyncError(f"Onbekend doel '{doel}' (niet in wiki.yaml test_targets)") from exc


def get_site(wiki_yaml: dict, doel: str = "site"):
    """Site voor 'site' (hoofddoel) of een naam uit test_targets. Family/code
    komen uit wiki.yaml; credentials/Basic-Auth komen volledig uit pywikibots
    eigen ~/.pywikibot/user-config.py."""
    pywikibot = _import_pywikibot()
    target = _target(wiki_yaml, doel)
    try:
        site = pywikibot.Site(target["code"], target["family"])
    except Exception as exc:  # o.a. pywikibot.exceptions.UnknownFamilyError
        raise SyncError(
            f"Pywikibot-family '{target['family']}' (code '{target['code']}') niet "
            "geregistreerd. Zie README voor een eenmalige installatiestap."
        ) from exc
    site.login()
    return site


def _page_result(title: str, page) -> PageResult:
    # page.namespace()/.content_model: exacte pywikibot-attribuutnamen nog te
    # bevestigen tegen een live site (zie plan, open punten); redelijke
    # standaardwaarden als een attribuut ontbreekt (zoals de nep-client in
    # tests, die geen namespace/contentmodel kent).
    try:
        namespace = page.namespace().id
    except Exception:
        namespace = 0
    contentmodel = getattr(page, "content_model", "wikitext")
    return PageResult(title, page.text, page.latest_revision_id, namespace, contentmodel)


def pull_page(site, title: str) -> PageResult:
    pywikibot = _import_pywikibot()
    page = pywikibot.Page(site, title)
    if not page.exists():
        raise SyncError(f"Pagina bestaat niet: {title}")
    return _page_result(title, page)


def pull_pages(site, titles: list[str]) -> dict[str, PageResult]:
    pywikibot = _import_pywikibot()
    pages = {t: pywikibot.Page(site, t) for t in titles}
    list(site.preloadpages(pages.values()))
    return {t: _page_result(t, p) for t, p in pages.items() if p.exists()}


def push_page(site, title: str, new_text: str, base_revid: int | None, summary: str) -> PageResult:
    """Vlak vóór opslaan herophalen en vergelijken met base_revid (uit
    revisies.json of .work/sync/<doel>.json) -- afwijking = iemand anders
    wijzigde de pagina sinds ophalen."""
    pywikibot = _import_pywikibot()
    current = pywikibot.Page(site, title)
    current_revid = current.latest_revision_id if current.exists() else None
    if base_revid is not None and current_revid != base_revid:
        raise ConflictError(f"'{title}' is gewijzigd sinds ophalen ({base_revid} -> {current_revid})")
    current.text = new_text
    current.save(summary=summary, minor=False)
    current.text = None
    saved = pywikibot.Page(site, title)
    if saved.text.rstrip("\n") != new_text.rstrip("\n"):
        raise SyncError(f"'{title}': live tekst wijkt na opslaan af van lokaal.")
    return _page_result(title, saved)
