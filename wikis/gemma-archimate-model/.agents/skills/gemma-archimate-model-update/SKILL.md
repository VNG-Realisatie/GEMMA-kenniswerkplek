---
name: gemma-archimate-model-update
description: Werk het GEMMA-architectuurmodel (bedrijfslaag) bij op basis van bronnen voor één onderwerp — bronanalyse, beoordeling per begrip, relaties en GGM-terugmeldingen; scripts maken de pagina's, de redacteur geeft akkoord in de chat. Gebruik voor elke inhoudelijke wijziging in deze wiki.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-curatie-update gemma-archimate-model-ingest gemma-archimate-model-beoordelen gemma-archimate-model-criteria gemma-archimate-model-archimate-export"
  requires-tools: "llmwiki python:tools/beslissen.py python:tools/render.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py python:tools/archimate_export.py"
---

# Workflow gemma-archimate-model-update

Volg skill `wiki-curatie-update`. Deze workflow vult de stappen in voor deze wiki. Werkmap: `wikis/gemma-archimate-model`. Er is geen run: alles staat in de werkboom en is te zien in Git. Hervatten = `git status` en `ter-beoordeling.md` lezen.

## Stappen

| # | Stap | Wie | Denkniveau | Hoe | Resultaat |
|---|---|---|---|---|---|
| 1 | Onderwerp | AI met redacteur | middel | Bestaat `beoordelingen/onderwerpen/<onderwerp>.yaml` niet, maak het dan in overleg (naam, omschrijving als alinea's, bronnen, status `in-behandeling`); noem in de omschrijving de kernobjecten, en wat buiten het onderwerp valt met het onderwerp waar het thuishoort (regel Thuishoren) | onderwerp |
| 2 | Bronnen en bronanalyse | AI | middel | Skill `gemma-archimate-model-ingest`; daarna de kernpunten bespreken met de redacteur | `sources/`, `bronanalyses/<onderwerp>/` |
| 3 | Beoordelen | AI | hoog | Skill `gemma-archimate-model-beoordelen`: per begrip een beoordeling met kenmerken, tekst, match, relaties en terugmeldingen; lees eerst de `besluiten:` van het onderwerp en van de beoordelingen (regel Navragen) | `beoordelingen/begrippen/<id>.yaml`, `beoordelingen/terugmeldingen/ggm.yaml` |
| 4 | Beslissen en renderen | script | hoog | `uv run python tools/beslissen.py`. Een fout lost de AI op in de beoordeling en draait opnieuw. Een waarschuwing beoordeelt de AI inhoudelijk: oplossen of toelichten | status, pagina's, `ter-beoordeling.md` |
| 5 | Voorleggen | AI → redacteur | hoog | Wat een keuze van de redacteur vraagt (een element met open redenen in `beslist.open` of `ter-beoordeling.md`, een open vraag, twijfel over een kenmerk, een nieuw element, een afwijking van een eerder besluit), één voor één in de chat, in eenvoudige taal met context, argumenten, advies en per optie wat er gebeurt. Het antwoord komt in `besluiten:`; daarna stap 4. Wat je niet los voorlegt en hoe je vastlegt: skill `gemma-archimate-model-beoordelen`, `references/besluiten.md` | `kandidaat` → `review` of `afgewezen` |
| 6 | Bekijken | redacteur | laag | `uv run python -m llmwiki promote plan [--onderwerp <id>]` en de samenvatting in de chat tonen. De redacteur leest `ter-beoordeling.md`, de pagina's en de wijzigingen in Source Control. Wil de redacteur iets anders: aanpassen in de beoordeling, terug naar stap 4 | — |
| 7 | Akkoord | redacteur | laag | De redacteur typt AKKOORD. "Prima" of "ziet er goed uit" is geen akkoord; vraag dan opnieuw | — |
| 8 | Vastleggen | script | laag | `uv run python -m llmwiki promote apply --akkoord-woord AKKOORD` als los commando, nooit samen met lint of commit; het harness vraagt de redacteur om een klik, en die klik geldt alleen voor het akkoord | `goedgekeurd`, `log.md`, pagina's |
| 9 | Exporteren | script | laag | Direct na stap 8, zonder nieuwe vraag: het AKKOORD dekt de export. Skill `gemma-archimate-model-archimate-export`, stap 1 en 2: `uv run python tools/archimate_export.py --check`, dan `uv run python tools/archimate_export.py`. Geef het rapport door zoals die skill voorschrijft. Weigert de export, meld dan waarom en commit niet voordat het is opgelost | `export/gemma-archimate-model.archimate`, `export/rapport.md` |
| 10 | Commit | redacteur of AI | laag | Direct na stap 9, zonder nieuwe vraag, op main. Beoordelingen, pagina's, `log.md` en de export samen; de pre-commit-controle eist dat de pagina's gelijk zijn aan de render. Importeren in GEMMA doet de redacteur (skill `gemma-archimate-model-archimate-export`, stap 4) | Git |

## Grenzen

- Pagina's (`bedrijfsarchitectuur/`, `motivatie/`, `begrippen/`, `overzichten/`, `terugmeldingen/`, `ter-beoordeling.md`, `voortgang.md`, alles met paginatype `lijst`) nooit met de hand bewerken: wijzig de beoordeling of het register en draai `tools/beslissen.py`.
- `status:` en `beslist:` in een beoordeling nooit zelf invullen; de scripts zetten ze.
- Hernoemen, samenvoegen of splitsen van een element: leg in `beoordelingen/objecten.yaml` vast welk Archi-object het voortzet (regel Objectbehoud). Bij samenvoegen en splitsen eerst de redacteur vragen.
- Nooit zelf AKKOORD typen of `promote apply` draaien zonder dat de redacteur letterlijk AKKOORD typte.

## Delegatie

Bronanalyses mogen in een subagent, op denkniveau middel (geef de bron-id's en het onderwerp mee). Het beoordelen blijft in de hoofd-Agent: begrippen, relaties en terugmeldingen worden in samenhang gewogen.

## Nieuwe modelrelease

Een nieuwe GGM-release of een nieuwe versie van het GEMMA-model is geen onderwerp-update: gebruik `gemma-archimate-model-ggm-release` of `gemma-archimate-model-gemma-release`. Het model in Archi bekijken of naar GEMMA brengen: `gemma-archimate-model-archimate-export`.
