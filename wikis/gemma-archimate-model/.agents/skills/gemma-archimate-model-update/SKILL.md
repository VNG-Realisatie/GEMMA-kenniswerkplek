---
name: gemma-archimate-model-update
description: Werk het GEMMA-architectuurmodel (bedrijfslaag) bij op basis van bronnen voor één onderwerp — bronanalyse, beoordeling van begrippen, elementpagina's, relaties en GGM-terugmeldingen — via de gedeelde werkstroom wiki-update met menselijke promotie. Gebruik voor elke inhoudelijke wijziging in deze wiki.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-update gemma-archimate-model-ingest gemma-archimate-model-assess gemma-archimate-model-criteria gemma-archimate-model-write"
  requires-tools: "llmwiki python:tools/check_elementen.py"
---

# Workflow gemma-archimate-model-update

Volg skill `wiki-update` volledig. Deze workflow voegt alleen de uitbreidingen van deze wiki toe; hij herhaalt geen stappen. Werkmap: `wikis/gemma-archimate-model`.

## Starten

Werk altijd vanuit één onderwerp: `uv run llmwiki run start --workflow gemma-archimate-model-update --onderwerp <onderwerp-id>`. De onderwerppagina staat in `begrippen/<onderwerp-id>.md`; bestaat die nog niet, maak haar dan eerst aan in overleg met de redacteur (zie `gemma-archimate-model-ingest`). De bronnen komen in de volgorde van de bronvoorrang (wet → informatiemodel → beleid → overig).

## Uitbreidingen per fase

| Fase | Na de generieke skill | Uitvoer |
|---|---|---|
| INGEST | Laad `gemma-archimate-model-ingest`: brontype, bronselectie, bronanalyse, kernpunten bespreken | `bronanalyses/<onderwerp>/<bron-id>.md` |
| ASSESS | Laad `gemma-archimate-model-assess` (die laadt `gemma-archimate-model-criteria`). Elk voorstel krijgt een `beoordeling` en de `relaties` uit de bronanalyses; draai `uv run python tools/bepaal_type.py evalueer <assessment.json> --schrijf` en `uv run python tools/relaties.py uit-bronnen <assessment.json>` vóór `run complete assess`. Leg begrippen met `voorleggen` of `conflict` per begrip voor en wacht op antwoord vóór WRITE | `assessment.json` met uitkomsten |
| WRITE | Laad `gemma-archimate-model-write`. Tools die pagina's stagen (`tools/terugmelding.py`, `tools/ggm.py verrijk --run`) vullen `.work/runs/<run-id>/changeset-concept.json`; zet je eigen pagina's in hetzelfde bestand en rond af met `uv run llmwiki run complete write --run <run-id> --data .work/runs/<run-id>/changeset-concept.json` | gestagede pagina's |
| VALIDATE | Na `wiki-validate` (met `--run <run-id>` per pagina): `uv run python tools/check_elementen.py --run <run-id> --rapport .work/runs/<run-id>/validation-report.json`. Een `fout` → terug naar WRITE. Een `waarschuwing` beoordeel je inhoudelijk (bijv. registr*-taal, absolute taal) en los je op of licht je toe | `validation-report.json` |
| GATE + PROMOTE | `wiki-publish` ongewijzigd. Het voorstel toont welke pagina's worden goedgekeurd (status `review`) en welke als `kandidaat` blijven staan | `log.md`, `voortgang.md` |

## Delegatie

INGEST, ASSESS en VALIDATE mogen in een subagent (alleen run-id en artefactpaden meegeven). WRITE blijft in de hoofd-Agent: pagina's, begrippenlijst en terugmeldingen worden in samenhang geschreven.

## Nieuwe modelrelease

Een nieuwe GGM-release of een nieuwe versie van het GEMMA-model is geen onderwerp-update: gebruik `gemma-archimate-model-ggm-release` of `gemma-archimate-model-gemma-release`.
