---
name: gemma-archimate-model-update
description: Werk het GEMMA-architectuurmodel (bedrijfslaag) bij op basis van bronnen voor één onderwerp — bronanalyse, beoordeling per begrip, relaties en GGM-terugmeldingen; scripts maken de pagina's, de redacteur geeft akkoord in de chat. Gebruik voor elke inhoudelijke wijziging in deze wiki.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-curatie-update gemma-archimate-model-ingest gemma-archimate-model-beoordelen gemma-archimate-model-criteria"
  requires-tools: "llmwiki python:tools/afleiden.py python:tools/render.py python:tools/relaties.py python:tools/ggm.py python:tools/gemma.py"
---

# Workflow gemma-archimate-model-update

Volg skill `wiki-curatie-update`. Deze workflow vult de stappen in voor deze wiki. Werkmap: `wikis/gemma-archimate-model`. Er is geen run: alles staat in de werkboom en is te zien in Git. Hervatten = `git status` en `ter-beoordeling.md` lezen.

## Stappen

| # | Stap | Wie | Denkniveau | Hoe | Resultaat |
|---|---|---|---|---|---|
| 1 | Onderwerp | AI met redacteur | middel | Bestaat `beoordelingen/onderwerpen/<onderwerp>.yaml` niet, maak het dan in overleg (naam, omschrijving als alinea's, bronnen, status `in-behandeling`) | onderwerp |
| 2 | Bronnen en bronanalyse | AI | middel | Skill `gemma-archimate-model-ingest`; daarna de kernpunten bespreken met de redacteur | `sources/`, `bronanalyses/<onderwerp>/` |
| 3 | Beoordelen | AI | hoog | Skill `gemma-archimate-model-beoordelen`: per begrip een beoordeling met kenmerken, tekst, match, relaties en terugmeldingen; lees eerst `analyses/besluiten-redacteur.md` | `beoordelingen/begrippen/<id>.yaml`, `beoordelingen/terugmeldingen.yaml` |
| 4 | Afleiden en renderen | script | hoog | `uv run python tools/afleiden.py`. Een fout lost de AI op in de beoordeling en draait opnieuw. Een waarschuwing beoordeelt de AI inhoudelijk: oplossen of toelichten | status, pagina's, `ter-beoordeling.md` |
| 5 | Voorleggen | AI → redacteur | hoog | Elk begrip met open redenen (`afgeleid.open`, ook in `ter-beoordeling.md`) en elke open vraag één voor één in de chat: context, argumenten voor en tegen, advies. Het antwoord komt in `besluiten:` (datum, besluit, `gevolg`, en bij `opnemen` de redenen die het besluit dekt); daarna stap 4 | `kandidaat` → `review` of `afgewezen` |
| 6 | Bekijken | redacteur | laag | `uv run python -m llmwiki promote plan [--onderwerp <id>]` en de samenvatting in de chat tonen. De redacteur leest `ter-beoordeling.md`, de pagina's en de wijzigingen in Source Control. Wil de redacteur iets anders: aanpassen in de beoordeling, terug naar stap 4 | — |
| 7 | Akkoord | redacteur | laag | De redacteur typt AKKOORD. "Prima" of "ziet er goed uit" is geen akkoord; vraag dan opnieuw | — |
| 8 | Vastleggen | script | laag | `uv run python -m llmwiki promote apply --akkoord-woord AKKOORD`; het harness vraagt de redacteur om een klik | `goedgekeurd`, `log.md`, pagina's |
| 9 | Commit | redacteur of AI | laag | Beoordelingen, pagina's en `log.md` samen; de pre-commit-controle eist dat de pagina's gelijk zijn aan de render | Git |

## Grenzen

- Pagina's (`bedrijfsarchitectuur/`, `motivatie/`, `begrippen/`, `analyses/ggm-terugmeldingen.md`, `ter-beoordeling.md`, `voortgang.md`) nooit met de hand bewerken: wijzig de beoordeling en draai `tools/afleiden.py`.
- `status:` en `afgeleid:` in een beoordeling nooit zelf invullen; de scripts zetten ze.
- Nooit zelf AKKOORD typen of `promote apply` draaien zonder dat de redacteur letterlijk AKKOORD typte.

## Delegatie

Bronanalyses mogen in een subagent, op denkniveau middel (geef de bron-id's en het onderwerp mee). Het beoordelen blijft in de hoofd-Agent: begrippen, relaties en terugmeldingen worden in samenhang gewogen.

## Nieuwe modelrelease

Een nieuwe GGM-release of een nieuwe versie van het GEMMA-model is geen onderwerp-update: gebruik `gemma-archimate-model-ggm-release` of `gemma-archimate-model-gemma-release`.
