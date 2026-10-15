---
name: gemma-archimate-model-update
description: Werk het GEMMA-architectuurmodel (bedrijfslaag) bij op basis van bronnen voor één onderwerp, in drie Sessies — bronnen en fase A met één tabel voor de redacteur; fase B per cluster in beoordelingsagenten; beslissen, voorleggen, akkoord, export en commit. Scripts maken de pagina's, de redacteur geeft akkoord in de chat. Gebruik voor elke inhoudelijke wijziging in deze wiki.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-curatie-update gemma-archimate-model-ingest gemma-archimate-model-criteria gemma-archimate-model-beoordelen gemma-archimate-model-archimate-export"
  requires-tools: "llmwiki python:tools/werkpakket.py python:tools/bepaal_type.py python:tools/beoordeling.py python:tools/beslissen.py python:tools/render.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py python:tools/archimate_export.py python:tools/afronden.py"
---

# Workflow gemma-archimate-model-update

Deze skill vult skill `wiki-curatie-update` in voor deze wiki, met alle stappen; die skill hoef je niet apart te lezen. De werkmap is `wikis/gemma-archimate-model`. Alles staat in de werkboom en is te zien in Git. Hervatten doe je door `handoff.md`, `git status` en `ter-beoordeling.md` te lezen.

Een onderwerp loopt in drie Sessies na elkaar, zonder ander werk ertussen; elke Sessie begint met een schone context. Tussen de fasen gaat de overdracht via de werkboom (beoordelingen, `vragen:`, besluiten) en via `handoff.md` (stand, clusters, besluiten, startprompt); de commit volgt in fase 3. Lees per fase alleen wat onder *Lezen* staat, plus een reference als een stap ernaar verwijst. Lees na het schrijven een bestand niet terug: de scripts controleren het. Past een onderwerp niet in één ronde, verdeel het dan in delen (een kernobject of een proces) en rond elk deel af met akkoord en commit.

## Fase 1: bronnen en fase A

**Lezen:** deze skill, skill `gemma-archimate-model-criteria`, `kennismodel/modelleerregels.md`, `references/besluiten.md` van skill `gemma-archimate-model-beoordelen`, en het werkpakket. Voor het verwachte procesniveau lees je ook de modelleerafspraken van Bedrijfsproces, tot *Relaties*.

| # | Stap | Denkniveau | Hoe | Resultaat |
|---|---|---|---|---|
| 1 | Onderwerp | middel | Bestaat `onderwerpen/<onderwerp>/afbakening.yaml` niet, maak het dan in overleg: naam, omschrijving als alinea's, bronnen, status `in-behandeling` en `niveau` (`eigen`, `thematisch` of `kern`; de criteria in ARCHITECTURE.md, sectie 3.3). De omschrijving noemt de kernobjecten, en wat buiten het onderwerp valt met het onderwerp waar het thuishoort | afbakening |
| 2 | Bronnen en bronduiding | middel | Skill `gemma-archimate-model-ingest`, in een subagent op denkniveau middel; geef de bron-id's en het onderwerp mee. Bespreek daarna de kernpunten met de redacteur | `sources/`, bronduidingen |
| 3 | Werkpakket | laag | `uv run python tools/werkpakket.py <onderwerp>` en lees `.work/werkpakket/<onderwerp>.md` (in de root van de repository). Daarin staan de begrippen met wat de catalogus kent, de passages, de kandidaten in GGM, GEMMA en UPL, de relatievoorstellen, de besluiten en de modelleerafspraken die gelden | werkpakket |
| 4 | Eerst de catalogus | middel | Een begrip dat de catalogus al kent, krijgt alleen jouw onderwerp achteraan in `onderwerpen` en, als iets alleen hier geldt, `per_onderwerp` (regel Eén element in het hele model). Synoniem of homoniem: skill criteria, stap 2 | bijgewerkte beoordelingen |
| 5 | Fase A | hoog | Per nieuw begrip skill `gemma-archimate-model-criteria`: de poort, de aard en de groep van die aard, één regel per kenmerk, daarna `normaliseer` | beoordelingen met fase A |
| 6 | Eén tabel | hoog | Leg het hele onderwerp voor in één tabel met de kolommen Begrip, Uitkomst fase A (type of de stop), Verwacht niveau, Kernobject, Thuisonderwerp en Open keuze met advies. Daaronder volgen de clusters voor fase B. Alleen een blokkerende vraag komt eerder. Leg voor zoals voor een architect (`references/besluiten.md`). Een antwoord gaat naar `besluiten:` (`uv run python tools/beoordeling.py besluit <id> …`) of naar het onderwerp; pas fase A aan waar de redacteur anders beslist | besluiten, clusters |

Sluit af met `handoff.md` (de clusters met hun id's en de besluiten) en een startprompt voor fase 2.

## Fase 2: fase B per cluster

**Lezen (hoofdsessie):** deze skill en `handoff.md`. De beoordelingsagent leest wat zijn opdracht noemt.

| # | Stap | Denkniveau | Hoe | Resultaat |
|---|---|---|---|---|
| 7 | Werkpakketten | laag | Per cluster `uv run python tools/werkpakket.py <onderwerp> --cluster <kernobject>`. Een cluster is een kernobject met zijn processen, gebeurtenissen en diensten. Actoren, rollen, beleidskaders, functies en kanalen zonder kernobject vormen samen één cluster, met het werkpakket van het hele onderwerp | werkpakketten |
| 8 | Beoordelingsagenten | hoog | Start per cluster een subagent op denkniveau hoog, parallel, met de opdracht hieronder. Bij één cluster of een handvol begrippen doet de hoofdsessie fase B zelf, met dezelfde opdracht | beoordelingen met fase B |
| 9 | Verslagen bundelen | hoog | Zet de terugmeldingen uit de verslagen in de registers (`references/terugmeldingen.md`). Maak een nieuw begrip dat een agent noemt aan met fase A, en wijs het een cluster toe. Volgt het antwoord op een vraag uit een besluit of uit een ander cluster, beantwoord haar dan zelf; anders blijft ze in `vragen:` voor fase 3. Moet een agent verder, zet dan dezelfde agent voort in plaats van een nieuwe te starten | registers, `vragen:` |
| 10 | Beslissen | hoog | `uv run python tools/beslissen.py`. Los hier de fouten tussen clusters op, zoals relaties en dubbele begrippen | status, pagina's |

Sluit af met `handoff.md` en een startprompt voor fase 3.

### Opdracht voor de beoordelingsagent

```text
Je bent beoordelingsagent voor het cluster <kernobject> van het onderwerp <onderwerp> in wikis/gemma-archimate-model, op denkniveau hoog. Lees: wikis/gemma-archimate-model/AGENTS.md tot de sectie "Waar vind je wat"; skill gemma-archimate-model-beoordelen; kennismodel/modelleerregels.md; het werkpakket .work/werkpakket/<onderwerp>-<kernobject>.md; en van de modelleerafspraken die het werkpakket noemt het deel tot "## Relaties". Besluiten van de redacteur uit fase A: <besluiten>. Jouw beoordelingen: <id's>. Werk fase B uit volgens skill gemma-archimate-model-beoordelen. Schrijf alleen in je eigen beoordelingen. Een ander begrip, een register of een onderwerp wijzig je niet, en een nieuw begrip maak je niet aan: noem het in je verslag. Controleer met uv run python tools/beslissen.py --alleen <id's> (nooit zonder --alleen) tot er geen fout meer is. Een vraag aan de redacteur zet je in vragen: van de beoordeling, met context en advies; je stelt geen vragen in de chat. Lees na het schrijven geen bestand terug. Je verslag is kort: per id de regel uit --alleen; de open vragen; de terugmeldingen die je voorstelt (register, element, Bevinding, Voorstel); en de begrippen en relaties buiten je cluster.
```

## Fase 3: beslissen, voorleggen en vastleggen

**Lezen:** deze skill, `handoff.md` en `references/besluiten.md`; bij stap 16 ook skill `gemma-archimate-model-archimate-export`.

| # | Stap | Wie | Denkniveau | Hoe | Resultaat |
|---|---|---|---|---|---|
| 11 | Beslissen | script | hoog | `uv run python tools/beslissen.py`. Een fout los je op in de beoordeling, en daarna draai je opnieuw. Een waarschuwing beoordeel je inhoudelijk: oplossen of toelichten. Kijk ook naar de indelingspagina's (`elementpaginas/overig/indelingen/`, met dekking) en naar `elementpaginas/overig/zonder-grondslag.md`: elke dienst daarop heeft een procesarchitectuur-terugmelding | status, pagina's, `ter-beoordeling.md` |
| 12 | Voorleggen | AI → redacteur | hoog | Leg in één tabel voor wat een keuze van de redacteur vraagt: open redenen (`beslist.open`, `ter-beoordeling.md`), `vragen:`, twijfel over een kenmerk, een nieuw element, of een afwijking van een eerder besluit. Leg voor zoals voor een architect, in gewone taal en analytisch: de stand in GGM en GEMMA, de opties, het gevolg voor het model, een advies en de bron als link. Wat je niet los voorlegt en hoe je vastlegt: `references/besluiten.md`. Na de antwoorden volgt stap 11 opnieuw | `kandidaat` → `review` of `afgewezen` |
| 13 | Bekijken | redacteur | laag | Per afgerond onderwerp of deel, niet per begrip: `uv run python -m llmwiki promote plan [--onderwerp <id>]` en de samenvatting in de chat tonen. De redacteur leest `ter-beoordeling.md`, de pagina's en de wijzigingen in Source Control. Wil de redacteur iets anders, pas dan de beoordeling aan en ga terug naar stap 11 | — |
| 14 | Akkoord | redacteur | laag | De redacteur typt AKKOORD. "Prima" of "ziet er goed uit" is geen akkoord; vraag dan opnieuw | — |
| 15 | Vastleggen | script | laag | `uv run python -m llmwiki promote apply --akkoord-woord AKKOORD`, als los commando, nooit samen met lint of commit. Het harness vraagt de redacteur om een klik, en die klik geldt alleen voor het akkoord | `goedgekeurd`, `log.md`, pagina's |
| 16 | Exporteren | script | laag | Direct na stap 15, zonder nieuwe vraag: het AKKOORD dekt de export. Skill `gemma-archimate-model-archimate-export`, stap 1 en 2: `uv run python tools/archimate_export.py --check`, dan `uv run python tools/archimate_export.py`. Geef het rapport door zoals die skill voorschrijft. Weigert de export, meld dan waarom en commit niet voordat het is opgelost. Stap 16 en 17 kunnen samen met `uv run python tools/afronden.py --bericht "<prefix>: …"` (draait na `promote apply` de berichtcontrole, export-check, export, render-check en lint, en commit pas als alles slaagt; weigert zonder een gewijzigde `log.md`); geef daarna `export/rapport.md` door | `export/gemma-archimate-model.archimate`, `export/rapport.md` |
| 17 | Commit | redacteur of AI | laag | Direct na stap 16, zonder nieuwe vraag, op main, met een prefix (AGENTS.md, Werkwijze; controle: `uv run python -m llmwiki commit-check <bestand>`). Commit de beoordelingen, de pagina's, `log.md`, de export en `handoff.md` samen; de pre-commit-controle eist dat de pagina's gelijk zijn aan de render. `afronden.py` doet deze stap ook, na stap 16. Importeren in GEMMA doet de redacteur (skill `gemma-archimate-model-archimate-export`, stap 4) | Git |

## Grenzen

- Pagina's bewerk je nooit met de hand: `elementpaginas/` (ook `elementpaginas/overig/`), `onderwerpen/<onderwerp>/begrippen.md` en `overzicht.md`, de lijsten bij `modellen/*/terugmeldingen`, `ter-beoordeling.md`, `voortgang.md` en alles met paginatype `lijst`. Wijzig de beoordeling of het register en draai `tools/beslissen.py`.
- `status:` en `beslist:` in een beoordeling vul je nooit zelf in; de scripts zetten ze.
- Bij hernoemen, samenvoegen of splitsen van een element leg je in `object_van` vast welk Archi-object het voortzet (regel Objectbehoud). Bij samenvoegen en splitsen vraag je het eerst aan de redacteur.
- Typ nooit zelf AKKOORD, en draai `promote apply` nooit zonder dat de redacteur letterlijk AKKOORD typte.

## Nieuwe modelrelease

Een nieuwe GGM-release of een nieuwe versie van het GEMMA-model is geen onderwerp-update: gebruik dan `gemma-archimate-model-ggm-release` of `gemma-archimate-model-gemma-release`. Voor het model in Archi bekijken of naar GEMMA brengen: `gemma-archimate-model-archimate-export`.
