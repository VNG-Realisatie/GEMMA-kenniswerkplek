# Klus 2 + pywikibot pull/publish + architectuurcorrectie: drie wiki-soorten

## Context

Klus 1 en het MediaWiki-onafhankelijke deel van Klus 3 (curatie, `wikis/_template-md/`) zijn af. Deze ronde doet Klus 2 (`docs/kluswijzer.md`) plus het eerder uitgestelde MediaWiki-deel van Klus 3 (echte `llmwiki pull`/`publish`), en corrigeert onderweg `docs/onderbouwing.md`'s wiki-soortenmodel — bevestigd noodzakelijk door de gebruiker, gevalideerd tegen de al bestaande, in productie zijnde buursetup (`/home/mark/Documents/GitHub/GEMMA-wiki beheren/`, alleen als kennisbron gebruikt, niet gewijzigd) en tegen een Opus-review met codelezing.

### Architectuurcorrectie: drie wiki-soorten, benoemd naar doel, niet naar letter

| Soort (`wiki.yaml` `type:`) | Doel | Bron van waarheid | Laatste fase |
|---|---|---|---|
| `sync` | een MediaWiki-site beheren (bv. GEMMA Online) | de externe site | PUBLISH (git-diff-review + gate) |
| `curation` | gestructureerde kennis opbouwen, optioneel tot een export (ArchiMate/UML/CSV/MediaWiki) | repository | PROMOTE, en als `exports:` geconfigureerd is: daarna EXPORT per doel |
| `knowledge-base` | ongestructureerde kennis opbouwen: notities, adviezen, ontwerpen, architectuurdocumenten — eigen deliverables, niet per se ten dienste van een andere wiki | repository | geen — geen run/gate, alleen losse `llmwiki validate` (bewijsregel); review is een gewone `git diff`/commit |

**`hybrid` vervalt als apart type** (bevestigd door de gebruiker): wat voorheen type C was, is gewoon een `curation`-wiki met een ingevuld `exports:`-blok. Geen aparte typewaarde nodig voor "curatie met een exportdoel" — dat was altijd al alleen een configuratieverschil, geen ander gedrag.

**Waarom `sync` een kale werkkopie wordt** (niet de huidige onderbouwing.md 5.18, die er `onderwerpen/`+`bronnen/<onderwerp>/`+`records/` aan toevoegt): de buursetup splitste dit al bewust (commit `da310e9`, "Scheid werkkopie van kennisbank"), en `tools/llmwiki/runs.py`'s huidige vaste vier-fasen-pijplijn maakt een simpele redactionele fix onnodig zwaar. Besluit: `content/`, `revisies.json` (één gecommit conflictbasis-bestand i.p.v. een `.meta.json`-sidecar per pagina — minder bestanden, geen ongebruikte velden), `log.md` (hergebruikt het al bestaande `logbook.py`), `voorstellen/`, `.agents/skills/`, `.work/`. Geen `onderwerpen/`, geen `bronnen/`, geen `records/`.

**Waarom `knowledge-base` een eigen, derde soort is (niet een submap van `sync`, niet hetzelfde als `curation`):** het gaat om *ongestructureerde* kennisopbouw — notities, adviezen, ontwerpen, architectuurdocumenten — die op zichzelf al een volwaardig eindresultaat zijn (net als `ARCHITECTURE.md`/`docs/onderbouwing.md` dat voor dít project zijn), niet per se een tussenstap voor een andere wiki. Dat is fundamenteel anders dan `curation`'s *gestructureerde*, formele kandidaat→review→goedgekeurd-pijplijn richting een export. De buursetup's `llm-wiki/` (zie `llm-wiki-rules.md`) laat wel zien hoe licht dit kán: géén curatiestatus, géén schema-gated run, alleen de regel "elke claim herleidbaar naar bronmateriaal" (bewijsregel). Review is een gewone `git diff`/commit, zoals bij elk ander document in de repository — geen publicatiegate nodig, want er wordt niets extern gepubliceerd. Een `knowledge-base`-document kán later alsnog input worden voor een sync- of curatie-wiki (via `--from-export`, zie onder), maar dat is een mogelijk vervolg, niet het doel.

**Overdracht `knowledge-base` → andere wiki: geen nieuwe regel nodig.** Hergebruikt het bestaande, generieke mechanisme uit 5.18: `llmwiki source add --from-export
<wiki>/<pad>` (dezelfde vlag als curatie al gebruikt — de generieke laag hoeft niet
te weten of de bronwiki curatie of knowledge-base was). Regel 5.4.3 ("wiki's verwijzen niet naar elkaar") blijft intact.

### Correctie: MCP-configformaat, en pywikibot-koppeling

- `@professional-wiki/mediawiki-mcp-server` (bevestigd: zelfde pakket als de buursetup) gebruikt een eigen `config.json` (`wikis`-object, env-var `CONFIG` voor het pad), niet de platte env-vars uit onderbouwing.md 5.10's huidige voorbeeld. `llmwiki harness sync` genereert dit **gecommit**, in de wiki-map, `readOnly: true` (eigen keuze: schrijven loopt alleen via de `llmwiki`-gate). Elk harness-bestand verwijst met een **relatief pad**; of dat overal oplost is nieuw verificatiepunt **V10** (naast het bestaande V6), geen blokkade.
- **MCP wijst altijd naar het hoofddoel (productie), nooit naar een testdoel.** Met een read-only `curl` vastgesteld: `gemma2-redactie.staging.wikixl.nl` geeft `401 WWW-Authenticate: Basic realm="staging"` (bevestigd door het commentaar in de al bestaande `~/.pywikibot/families/gemmaonline_family.py`); productie geeft gewoon `200`. Basic-Auth-in-URL is bij dit pakket (Node-`fetch`) vermoedelijk kansloos — geen poging daartoe. MCP is toch alleen-lezen, dus productie volstaat.
- **Pywikibot vereist een geïnstalleerde family**, geen dynamische constructie (expliciete keuze: betrouwbaarheid boven zero-config, een dynamische aanpak was niet zonder live spike te verifiëren). `wiki.yaml` verwijst naar `family`+`code` van een al geregistreerde pywikibot-family (hergebruikt de bestaande `gemmaonline_family.py`, codes `en`/`staging`). Credentials en de staging-Basic-Auth blijven volledig in pywikibots **eigen** globale `~/.pywikibot/user-config.py` — `llmwiki` schrijft of leest dat bestand nooit, het is een eenmalige installatiestap zoals nu al bij MCP-registratie.

## Wat wordt gebouwd

### 1. `wikis/_template/` (type `sync`)
- `AGENTS.md` (verwijst naar `../../AGENTS.md`).
- `wiki.yaml`:
  ```yaml
  key: template
  type: sync
  site: {family: gemmaonline, code: en, articlepath: /wiki}
  test_targets:
    staging: {family: gemmaonline, code: staging}
  content: {layout: namespace, namespaces: [0]}
  publish: {approval: document}
  mcp: {target: site}
  work: {retention_days: 30}
  ```
- Mappen: `content/`, `voorstellen/`, `.agents/skills/`, `.work/`, leeg `revisies.json` (`{}`), `log.md`.

### 2. `tools/llmwiki/titles.py` (nieuw) — titel ↔ bestandsnaam
Namespace-map met canonieke Engelse naam; spaties blijven spaties; `:` → `§`; overige Windows-verboden tekens percent-gecodeerd; `/` → geneste mappen; `_index` voor een pagina met subpagina's; `.wiki`-extensie alleen voor het wikitext-contentmodel; NFC-normalisatie; `~<hash>`-suffix alleen bij een echte botsing/gereserveerde naam/>120 tekens (titel dan in een override-blokje in `revisies.json`). `layout: namespace` nu bouwen; `layout: category` (GEMMA's conventie) gedocumenteerd voor Klus 4, niet nu. Volledig deterministisch, unit-testbaar zonder netwerk.

### 3. `tools/llmwiki/sync.py` (nieuw) — pywikibot-laag

**Ontwerpbeslissing, geverifieerd tegen het bestand zelf (niet aangenomen):** `~/.pywikibot/user-config.py` op deze machine zet `password_file = ~/.pywikibot/pywikibot.pwd` (een BotPassword-bestand). `pywikibot.Site(...). login()` leest credentials daaruit — **geen interactieve prompt, geen aparte login-laag nodig.** Dit is precies wat `Tools/push_to_wiki.py` in de buursetup nu al doet (`site = pywikibot.Site(*WIKI_SITES[args.wiki]); site.login()`). `sync.py` doet dus **niets meer dan dat**: het bouwt geen eigen credential- of authenticate-configuratie; het hergebruikt pywikibots eigen globale config volledig, zoals afgesproken. Concreet ontwerp:

```python
# tools/llmwiki/sync.py
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


def get_site(wiki_yaml: dict, doel: str = "site"):
    """Site voor 'site' (hoofddoel) of een naam uit test_targets. Family/code
    komen uit wiki.yaml; credentials/Basic-Auth komen volledig uit pywikibots
    eigen ~/.pywikibot/user-config.py (password_file, authenticate-dict) —
    sync.py raakt dat bestand nooit aan."""
    pywikibot = _import_pywikibot()
    target = wiki_yaml["site"] if doel == "site" else wiki_yaml["test_targets"][doel]
    try:
        site = pywikibot.Site(target["code"], target["family"])
    except Exception as exc:  # o.a. pywikibot.exceptions.UnknownFamilyError
        raise SyncError(
            f"Pywikibot-family '{target['family']}' (code '{target['code']}') niet "
            "geregistreerd. Zie README voor een eenmalige installatiestap."
        ) from exc
    site.login()
    return site


def pull_page(site, title: str) -> PageResult:
    pywikibot = _import_pywikibot()
    page = pywikibot.Page(site, title)
    if not page.exists():
        raise SyncError(f"Pagina bestaat niet: {title}")
    return PageResult(title, page.text, page.latest_revision_id)


def pull_pages(site, titles: list[str]) -> dict[str, PageResult]:
    pywikibot = _import_pywikibot()
    pages = {t: pywikibot.Page(site, t) for t in titles}
    list(site.preloadpages(pages.values()))  # batch, zoals push_to_wiki.py
    return {t: PageResult(t, p.text, p.latest_revision_id) for t, p in pages.items() if p.exists()}


def push_page(site, title: str, new_text: str, base_revid: int | None, summary: str) -> PageResult:
    """Vlak vóór opslaan herophalen en vergelijken met base_revid (uit
    revisies.json of .work/sync/<doel>.json) -- afwijking = iemand anders
    wijzigde de pagina sinds ophalen (kluswijzer-testcase)."""
    pywikibot = _import_pywikibot()
    current = pywikibot.Page(site, title)
    current_revid = current.latest_revision_id if current.exists() else None
    if base_revid is not None and current_revid != base_revid:
        raise ConflictError(f"'{title}' is gewijzigd sinds ophalen ({base_revid} -> {current_revid})")
    current.text = new_text
    current.save(summary=summary, minor=False)
    current.text = None  # forceer herlezen
    saved = pywikibot.Page(site, title)
    if saved.text.rstrip("\n") != new_text.rstrip("\n"):  # MediaWiki normaliseert trailing newline
        raise SyncError(f"'{title}': live tekst wijkt na opslaan af van lokaal.")
    return PageResult(title, saved.text, saved.latest_revision_id)
```

`get_site`/`pull_page`/`pull_pages`/`push_page` zijn de enige plek die `import pywikibot` doet (lokaal, niet module-top-level) — de rest van `llmwiki` (CLI, `gate.py`) roept alleen deze vier functies aan en werkt met `PageResult`, nooit met pywikibot-objecten rechtstreeks. Tests injecteren een nep-versie van deze vier functies (of een fake `site`-object met `.login()`/`Page()` die `pywikibot.Page`'s interface nadoet) — geen pywikibot-installatie nodig om `gate.py`'s sync-tak te testen.

### 4. `llmwiki pull` (CLI)
`llmwiki pull --wiki <pad> --title "<titel>" [--doel staging] [--force]`. Weigert een lokaal bestand met niet-gecommitteerde wijzigingen zonder `--force`. `--doel staging` staat op 'ask' in de permissies (nooit routine).

### 5. `llmwiki publish plan|apply` echt maken (nieuwe Workflow-Skill `wiki-edit`, naast `wiki-update`)
Sync-wiki's krijgen `runs.phases_for(wiki_yaml) == ["validate"]` (i.p.v. de vaste vier fasen). Workflow: PULL (optioneel) → BEWERK (`content/` direct aangepast, evt. na raadplegen van relevante `sources/` of een eerder geëxporteerde `knowledge-base`-bron) → VALIDATE → PLAN (`llmwiki publish plan [--doel staging] [paden|--git]`: verzamelt uit `git status`/`diff`, haalt live-revisies op, weigert bij conflict, voorstel bevat een echte git-diff) → AKKOORD (smaak A/B, ongewijzigd) → PUBLISH (`llmwiki publish apply`: hercontrole plan-hash incl. live-revisies, dan **alle** live-revisies vooraf controleren vóór de eerste write; bij een fout halverwege blijven gelukte pagina's vastgelegd, run krijgt status `gedeeltelijk`, geen stille gedeeltelijke mislukking) → COMMIT.

`gate.py` splitst in een gedeeld deel (akkoordcontrole, plan-hash, `mark_final_done`, `log_event` — ongewijzigd) en twee materialisatiefuncties: de bestaande (curatie: kopie + status + `log.md`) en een nieuwe (sync: `sync.push_page`, geen frontmatter in wikitext, geen status, geen `voortgang.md`). `knowledge-base` heeft geen materialisatiefunctie — dat type gebruikt de run/gate-machinerie niet.

### 6. `knowledge-base`-ondersteuning (nieuw, lichtgewicht — geen run/gate)
- `wikis/<key>/` met `type: knowledge-base`: `<onderwerp>/<document>.md` (vrije indeling per onderwerp, niet één vast paginatype — notitie, advies, ontwerp of architectuurdocument mogen naast elkaar bestaan; frontmatter minimaal `id`/`onderwerp`/`bronnen`, geen `status`), `.agents/skills/`, `wiki.yaml` (`sources.tags`, hergebruikt de centrale `sources/raw/`+`sources/index/`, geen eigen bronlaag).
- Nieuwe gedeelde Skill (`wiki-kennis-ingest`, scope core, herbruikbaar): bron lezen → classificeren (nieuw/bijwerken/tegenstrijdig/geen_materiaal) → document direct schrijven of bijwerken. Geen artefacten, geen fasen, geen gate — review gebeurt via een gewone `git diff`/commit, zoals elke andere repo-wijziging. Bewijsregel-check ("elke claim herleidbaar naar een bron-id") via een losse `llmwiki validate --schema page` (bronnen moeten bestaan in `sources/index/` en binnen scope vallen — hergebruikt bestaande `validate_page`-logica).
- Optionele overdracht naar een andere wiki (niet het hoofddoel, wel mogelijk): `llmwiki source add --from-export <knowledge-base-wiki>/<pad>` (bestaand, generiek mechanisme, geen nieuwe vlag).

### 7. `tools/llmwiki/harness.py` (nieuw) — harness-bindingen
- Brug `.claude/skills/<naam>` (symlink → Windows-junction → kopie + `.bridge-source.json`), root en per wiki.
- `.claude/settings.json`: allow op `workspace-check`, `run *`, `validate *`, `source *`, `lint*`, `pull*` (zonder `--doel`), `promote plan*`, `publish plan*`; ask op `pull* --doel *`, `promote apply*`, `publish apply*`; deny op `*pywikibot*`, edits/writes onder `voorstellen/**` en op `revisies.json` (de Agent past de conflictbasis nooit handmatig aan).
- `.vscode/settings.json`, `opencode.json`: ongewijzigd t.o.v. eerdere ontwerpen.
- MCP-clientbestanden alleen voor `sync`-wiki's of `curation`-wiki's met MediaWiki als exportdoel, altijd wijzend op het hoofddoel.
- `check()`: regenereert alles en vergelijkt byte-voor-byte (volledig deterministisch, geen absolute paden), controleert brug-integriteit, meldt elke `CLAUDE.md`/`CLAUDE.local.md`.

### 8. `tools/llmwiki/workspace_check.py` uitbreiden
- Roept `harness.check()` aan (geen dubbele logica).
- Nieuw: `mediawiki`-extra geïnstalleerd waar nodig; pywikibot-family uit `wiki.yaml` geregistreerd (`pywikibot.family.Family.load(naam)`); `npx`/Node beschikbaar; `mediawiki-mcp.config.json` aanwezig (dus: is `harness sync` gedraaid); toont het `claude mcp add ...`-commando als registratie nog moet (niet automatisch uitgevoerd).
- Windows Developer Mode-melding (`ms-settings:developers`).

### 9. Documentatie
- `docs/onderbouwing.md`: 3.1 (LLM-wiki, Record — drie soorten), 5.2/5.3 (conceptentabel + boomstructuur), 5.4 (bevestig: geen nieuwe cross-wiki-regel nodig, `--from-export` generiek), 5.8 (nieuwe Workflow-Skill `wiki-edit`, `wiki-kennis-ingest`), 5.10 (MCP-config, hoofddoel-only), 5.11 (records-tabel: sync gebruikt `log.md`, knowledge-base heeft er geen), 5.12 (`page-meta` → `revisies`), 5.13 (bestandsnaamregels), 5.18 (volledig herschreven: drie soorten, geen A/B/C-lettering, `hybrid` vervalt ten gunste van optionele `exports:` op `curation`), 5.19 (knowledge-base hergebruikt `sources/`), 7 (samenvatting), 8 (nieuw verificatiepunt V10).
- Consequent bij naam noemen (`sync`/`curation`/`knowledge-base`), nooit als "type A/B/C" — voorkomt verwarring met "Model A–D" en "smaak A/B" in dezelfde documenten.
- `ARCHITECTURE.md` §1: tabel met drie rijen (`sync`/`curation`/`knowledge-base`, doel/bron-van-waarheid/laatste-stap zoals de tabel bovenaan dit plan), plus een korte, nieuwe subsectie direct erna over wanneer welk gereedschap gebruikt wordt bij een sync-wiki (kort houden; het volledige ontwerp van `sync.py` staat al hierboven, gedetailleerde onderbouwing hoort in `docs/onderbouwing.md` 5.10, niet in het Kompas):

  ```markdown
  ### Gereedschap bij een sync-wiki

  | Gereedschap | Wanneer | Wat |
  |---|---|---|
  | MCP (`mediawiki`) | Tijdens het bewerken: verkennen, opzoeken, een pagina lezen | Alleen-lezen, interactief vanuit de AI-omgeving, wijst altijd naar het hoofddoel (nooit een testomgeving) |
  | `llmwiki pull` / `llmwiki publish` (pywikibot) | Vóór het bewerken (ophalen naar `content/`) en ná akkoord (schrijven) | Enige weg naar schrijven; nooit via MCP, altijd na de publicatiegate |
  ```

  §3 (plattegrond-voorbeeld met een `knowledge-base`-wiki).
- `docs/kluswijzer.md` Klus 2 (folderlijst `_template`), Klus 4 (`gemma` blijft `sync`; een eventuele kennisbank is een apart `type: knowledge-base`, niet een curatie-wiki).
- `README.md`: status + de openstaande actiepunten hieronder.

### 10. Pre-commit en CI
- `.pre-commit-config.yaml`: hook `llmwiki-harness-check`.
- `.github/workflows/check.yml`: `uv sync`, `pytest`, `llmwiki lint`, `llmwiki harness check`, op push/PR naar `VNG-Realisatie/GEMMA-kenniswerkplek`.

### 11. Tests
- `titles.py`: heen-en-terug-mapping, `§`, `_index`, percent-encoding, botsing.
- `sync.py`: `push_page`/`pull_page` tegen een nep-client: conflictdetectie, trailing-newline-tolerantie.
- `gate.py`: bestaande curatie-tests blijven groen; nieuwe sync-tak-tests (nep-client, conflict, plan-hash ongeldig na tussentijdse wijziging, gedeeltelijke-mislukking legt gelukte pagina's toch vast).
- `harness.py`: gegenereerde inhoud klopt; `check()` schoon na `sync()`, meldt afwijking; brug-fallback (symlink gemockt tot falen) → kopie + `.bridge-source.json`; deny-regel op `revisies.json` staat in de permissies.
- `runs.py`: `phases_for` klopt voor alle drie de soorten (sync: `[validate]`, curation: de bestaande vier fasen, knowledge-base: niet van toepassing/geen run nodig — test dat `llmwiki run start` een duidelijke fout geeft voor dit type, in plaats van stil iets verkeerds te doen).
- Nieuwe knowledge-base-validatie: bewijsregel-check (ontbrekende/buiten-scope bron wordt gemeld), net als de bestaande `validate_page`-tests.

## Open punten — nodig van de gebruiker, niet gegokt
1. Bevestiging van staging's `articlepath` (aanname: `/wiki`, gelijk aan productie — de bestaande family file noemt dit zelf ook nog "niet geverifieerd").
2. Een testpagina-titel op staging voor de volledige workflow-test (pull → bewerken → plan → akkoord → apply); verder niets anders op staging aanraken.

## Wat hier bewust niet gebeurt
- Geen `--category`-pull, geen move/rename-detectie (nuttig, geen kluswijzer-vereiste nu).
- Geen automatische uitvoering van `claude mcp add` of andere harness-CLI's namens de gebruiker.
- Geen dynamische pywikibot-family-constructie.
- Geen wijziging aan de bestaande buursetup — alleen gelezen.
- Geen `layout: category` — pas bouwen bij Klus 4.
- Geen daadwerkelijke `knowledge-base`-wiki-instantie deze ronde (alleen het type/de skill/de tooling); een concrete instantie (bv. voor GEMMA) is Klus 4.

## Verificatie
1. `uv run pytest -q`, `uv run llmwiki lint` — groen, met nep-clients (geen netwerk nodig).
2. `uv run llmwiki harness sync` + `harness check`: geen meldingen, root en `wikis/_template`.
3. `uv run llmwiki workspace-check` (+ `--json`): npx/mediawiki-extra/ family-registratie correct gemeld; toont het MCP-registratiecommando.
4. Met de open punten ingevuld: de volledige workflow op de afgesproken staging-testpagina, inclusief een bewust geforceerd conflict (extern wijzigen tussen plan en apply).
