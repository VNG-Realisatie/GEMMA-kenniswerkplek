---
name: wiki-update
description: Werk pagina's van een LLM-wiki bij op basis van nieuw bronmateriaal via INGEST, ASSESS, WRITE, VALIDATE en een menselijke gate voor PUBLISH of PROMOTE. Gebruik wanneer de gebruiker vraagt een wiki bij te werken of een bron te verwerken.
metadata:
  kind: workflow
  scope: core
  requires-skills: "wiki-ingest wiki-assess wiki-write wiki-validate wiki-publish"
  requires-tools: "llmwiki"
---

# Workflow wiki-update

Werkmap: de wiki-directory (bevat `wiki.yaml`). Bepaal die eerst met `llmwiki run
status` of door te zoeken naar `wiki.yaml` vanaf de huidige map.

## Run starten of hervatten

1. `llmwiki run start --workflow <naam-van-aanroepende-workflow> [--onderwerp
   <onderwerp-id>]`, of `llmwiki run resume <run-id>` als er al een run loopt
   (`llmwiki run status` zonder `--run` toont de laatst gestarte run).
2. `llmwiki run status` geeft de eerstvolgende fase. Voer alleen die fase uit.
3. Startte de run met `--onderwerp`: alleen de bronnen uit de `bronnen:`-lijst van die
   onderwerppagina zijn in scope voor INGEST en ASSESS.

## Fasen

| Fase | Rol | Skill | Leest | Schrijft |
|---|---|---|---|---|
| INGEST | ingester | wiki-ingest | bron(nen) | source.json |
| ASSESS | assessor | wiki-assess | source.json, bestaande pagina's | assessment.json |
| WRITE | writer | wiki-write | assessment.json | changeset.json + gestagede pagina's |
| VALIDATE | validator | wiki-validate | changeset.json | validation-report.json |
| GATE + PROMOTE/PUBLISH | (mens) + wiki-publish | wiki-publish | validation-report.json | promote-plan.json / publish-plan.json |

Na elke fase: `llmwiki run complete <fase> --run <run-id> --data <artefact>.json`.
Dit valideert het artefact tegen het schema en weigert bij fouten; de fase telt dan
niet als afgerond.

## Uitbreidingspunten

Een wiki-Workflow mag per fase aanvullende Skills en controles opgeven. Voer die uit
binnen dezelfde fase, ná de generieke Skill hierboven.

## Delegatie

Als het harness subagents ondersteunt: voer INGEST, ASSESS en VALIDATE elk uit in een
aparte subagent met als opdracht "laad skill <naam>, lees <artefact>, schrijf
<artefact>". Geef geen gespreksgeschiedenis mee, alleen de run-id en artefactpaden.
WRITE blijft in de hoofd-Agent: parallelle schrijvende Agents veroorzaken conflicten.

## Gate

Na VALIDATE: laad skill `wiki-publish` en volg die instructies volledig. Wijzig nooit
zelf de akkoordvelden in een voorstel, en zet geen automatische goedkeuring aan in een
sessie waarin wordt gepubliceerd of gepromoveerd.

## Afbreken

Wil de gebruiker de run niet afmaken: `llmwiki run close <run-id> --besluit "<reden>"`
als er bewust geen wijziging komt, of `llmwiki run abandon <run-id>` bij een fout of
een overbodige run. Beide laten de wiki ongewijzigd; alleen het kladblok verdwijnt.
