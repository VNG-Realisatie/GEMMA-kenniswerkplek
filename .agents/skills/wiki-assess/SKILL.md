---
name: wiki-assess
description: Beoordeel op basis van de bronnen van deze run welke pagina's moeten worden toegevoegd of gewijzigd, en waarom. Gebruik als tweede fase van een wiki-update, na wiki-ingest.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "source"
  writes: "assessment"
---

# Skill wiki-assess

Doel: de ASSESS-fase. Bepaalt welke pagina's veranderen, zonder al te schrijven.

## Stappen

1. Lees eerst laag 2 (`sources/index/`, kort), dan laag 3 (de domein-lens van deze
   run). Laag 1 alleen voor specifieke passages.
2. Voor elke bron: welke bestaande pagina's raakt dit, en zijn er nieuwe pagina's
   nodig? Zie `references/criteria.md` voor de afweging nieuw/wijzigen/geen actie.
3. Schrijf per voorstel: doelpad, soort (`nieuw`/`wijzigen`/`geen_actie`), motivering
   in gewone taal, en de bron-id's waarop het voorstel steunt.
4. Rond de fase af: `llmwiki run complete assess --run <run-id> --data
   <assessment.json volgens schema 'assessment'>`.

## Uitbreidingspunt

Een wiki-Workflow mag hier een aanvullende Skill laden om domeinspecifieke
classificatie toe te voegen (bijvoorbeeld: is dit voorstel een bedrijfsobject?).
Voer die aanvulling uit ná deze skill, binnen dezelfde fase.
