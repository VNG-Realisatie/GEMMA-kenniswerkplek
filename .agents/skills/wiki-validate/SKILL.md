---
name: wiki-validate
description: Controleer de gestagede pagina's uit WRITE op vorm, links en statusovergangen voordat een publicatie- of promotievoorstel wordt gemaakt. Gebruik als vierde fase van een wiki-update, na wiki-write.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "changeset"
  writes: "validation-report"
---

# Skill wiki-validate

Doel: de VALIDATE-fase. Alle controles die zonder Model kunnen, lopen via code; deze
skill roept ze aan en interpreteert het resultaat.

## Stappen

1. Draai voor elke pagina in `changeset.json`: `llmwiki validate
   <gestaged-bestand> --schema page` (of, voor een wiki-specifiek domeinobject, het
   schema dat de wiki-Workflow noemt).
2. Verzamel de resultaten in `validation-report.json` volgens schema
   `validation-report`: per controle naam, doel, resultaat (`ok`/`fout`) en ernst
   (`info`/`waarschuwing`/`fout`).
3. Bevat het rapport een `fout`: los dat op door WRITE opnieuw uit te voeren (niet
   door de fout te negeren) en valideer opnieuw.
4. Rond de fase af: `llmwiki run complete validate --run <run-id> --data
   validation-report.json`. Een voorstel (`promote plan` / `publish plan`) wordt
   geweigerd zolang er een `fout` in het rapport staat.

## Uitbreidingspunt

Een wiki-Workflow mag hier een extra script aanroepen (bijvoorbeeld een
domeincontrole) en het resultaat toevoegen aan dezelfde `validation-report.json`.
