"""Pywikibot-laag voor sync-wiki's. Zie docs/onderbouwing.md 5.10a.

- De servers van een wiki staan in een pywikibot-family-bestand in de wiki-map
  (`wikis/<wiki>/families/<naam>_family.py`, zonder geheimen); llmwiki meldt die
  bestanden zelf aan bij pywikibot.
- Inloggegevens komen uit omgevingsvariabelen; `wiki.yaml` noemt per doel alleen
  hun namen (`inlog`, en `http_toegang` voor een extra Basic-Auth-laag). Ze gaan
  in het geheugen naar pywikibot; llmwiki schrijft ze nergens weg.
- Pywikibots werkmap (sessiecookie, throttle) is `.work/pywikibot/`, zonder
  user-config.py. Wie zelf PYWIKIBOT_DIR heeft gezet, houdt de eigen configuratie.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


class SyncError(RuntimeError):
    pass


class ConflictError(SyncError):
    """Live revisie wijkt af van de bekende basisrevisie."""


def _import_pywikibot():
    if "pywikibot" not in sys.modules and "PYWIKIBOT_DIR" not in os.environ:
        werkmap = REPO_ROOT / ".work" / "pywikibot"
        werkmap.mkdir(parents=True, exist_ok=True)
        # pywikibot gebruikt PYWIKIBOT_DIR alleen als daar een user-config.py staat; anders valt het terug op de
        # huidige map en komen sessiecookie, cache en throttle-bestand daar terecht. Het bestand blijft leeg.
        user_config = werkmap / "user-config.py"
        if not user_config.exists():
            user_config.write_text("# Leeg: llmwiki configureert pywikibot zelf (tools/llmwiki/sync.py).\n",
                                   encoding="utf-8", newline="\n")
        os.environ["PYWIKIBOT_DIR"] = str(werkmap)
        os.environ.setdefault("PYWIKIBOT_NO_USER_CONFIG", "2")
    try:
        import pywikibot
    except ImportError as exc:
        raise SyncError("pywikibot ontbreekt. Draai 'uv sync'.") from exc
    config = getattr(pywikibot, "config", None)
    if config is not None:
        for map_ in sorted((REPO_ROOT / "wikis").glob("*/families")):
            config.register_families_folder(str(map_))
    return pywikibot


def ontbrekende_variabelen(target: dict) -> list[str]:
    """Namen van de omgevingsvariabelen uit `inlog`/`http_toegang` die niet (of leeg) gezet zijn."""
    namen = [naam for blok in ("inlog", "http_toegang") for naam in (target.get(blok) or {}).values()]
    return [naam for naam in namen if not os.environ.get(naam, "").strip()]


def _uit_omgeving(blok: dict | None) -> tuple[str, str] | None:
    if not blok:
        return None
    return os.environ[blok["gebruiker"]].strip(), os.environ[blok["wachtwoord"]].strip()


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
    """Site voor 'site' (hoofddoel) of een naam uit test_targets, ingelogd.

    Family/code komen uit wiki.yaml. Heeft het doel een `inlog`-blok, dan komen gebruiker en botwachtwoord uit
    de genoemde omgevingsvariabelen (gebruiker in de vorm `Hoofdaccount@botnaam`); `http_toegang` zet een extra
    HTTP-Basic-Auth-laag (staging). Zonder `inlog`-blok logt pywikibot in volgens de eigen configuratie."""
    target = _target(wiki_yaml, doel)
    ontbrekend = ontbrekende_variabelen(target)
    if ontbrekend:
        raise SyncError(
            f"Inloggegevens voor doel '{doel}' ontbreken: omgevingsvariabele(n) {', '.join(ontbrekend)} niet gezet. "
            "Zie README, 'Inloggen op GEMMA Online'."
        )
    pywikibot = _import_pywikibot()
    inlog = _uit_omgeving(target.get("inlog"))
    http = _uit_omgeving(target.get("http_toegang"))
    if http and target.get("server"):
        pywikibot.config.authenticate[target["server"]] = http
    hoofdnaam = inlog[0].partition("@")[0] if inlog else None
    try:
        site = pywikibot.Site(target["code"], target["family"], **({"user": hoofdnaam} if hoofdnaam else {}))
    except Exception as exc:  # o.a. pywikibot.exceptions.UnknownFamilyError
        raise SyncError(
            f"Site '{target['family']}' (code '{target['code']}') onbekend: "
            f"ontbreekt wikis/<wiki>/families/{target['family']}_family.py?"
        ) from exc
    if inlog:
        # Eerst de sessiecookie van een eerdere login proberen: binnen een botwachtwoord-sessie weigert
        # MediaWiki een nieuwe login ("Cannot log in when using BotPasswordSessionProvider sessions").
        site.login(cookie_only=True)
        if site.logged_in():
            return site
        manager = pywikibot.login.ClientLoginManager(site=site, user=hoofdnaam, password=inlog[1])
        manager.login_name = inlog[0]  # botwachtwoord: 'Hoofdaccount@botnaam'
        if not manager.login():
            raise SyncError(f"Inloggen op doel '{doel}' als '{inlog[0]}' mislukt; controleer de inloggegevens.")
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


def page_categories(site, title: str) -> list[str]:
    """Categorienamen van een pagina, zonder 'Categorie:'/'Category:'-prefix."""
    pywikibot = _import_pywikibot()
    page = pywikibot.Page(site, title)
    return [c.title(with_ns=False) for c in page.categories()]


def subpage_titles(site, title: str) -> list[str]:
    """Alle subpagina's van `title`, op elke diepte, ongeacht hun eigen status
    of categorie -- pagina/subpagina is een harde link, altijd meenemen."""
    pywikibot = _import_pywikibot()
    page = pywikibot.Page(site, title)
    bare, ns_id = page.title(with_ns=False), page.namespace().id
    return [p.title() for p in site.allpages(prefix=bare + "/", namespace=ns_id)]


@dataclass
class CategoryTreeEntry:
    categorie_pad: list[str]
    titel: str
    namespace: int


def category_tree(site, root_categorie: str):
    """Wandelt een categorie en al haar subcategorieën recursief af (cykelveilig
    via een bezocht-set). Yield één CategoryTreeEntry per artikel-lid, met
    `categorie_pad` = de categorienamen van root tot en met de directe
    oudercategorie van dat lid (zonder 'Categorie:'-prefix). Categoriepagina's
    zelf worden niet als lid opgeleverd, alleen als tak in categorie_pad."""
    pywikibot = _import_pywikibot()
    prefix = "Categorie:" if not (":" in root_categorie and root_categorie.split(":", 1)[0].lower() in ("categorie", "category")) else ""
    root = pywikibot.Category(site, prefix + root_categorie)

    gezien: set[str] = set()

    def _walk(cat, pad: list[str]):
        naam = cat.title(with_ns=False)
        if naam in gezien:
            return
        gezien.add(naam)
        for lid in cat.articles(recurse=False):
            yield CategoryTreeEntry(pad, lid.title(), lid.namespace().id)
        for sub in cat.subcategories():
            yield from _walk(sub, pad + [sub.title(with_ns=False)])

    yield from _walk(root, [root.title(with_ns=False)])


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
