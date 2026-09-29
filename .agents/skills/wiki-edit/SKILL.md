---
name: wiki-edit
description: Werk een sync-wiki bij (een MediaWiki-site die deze repository beheert, zoals GEMMA Online) via PULL, direct bewerken in content/, VALIDATE en een menselijke gate voor PUBLISH. Gebruik wanneer de gebruiker vraagt een pagina op een sync-wiki te maken, bij te werken of te controleren.
metadata:
  kind: workflow
  scope: core
  requires-tools: "llmwiki mcp:mediawiki"
  reads: "content"
  writes: "content"
---

# Workflow wiki-edit

Voor een **sync**-wiki (`wiki.yaml` `type: sync`): een directe werkkopie van een externe MediaWiki-site, geen curatiepijplijn. Gebruik `wiki-update` in plaats hiervan voor een curatie-wiki.

Werkmap: de wiki-directory (bevat `wiki.yaml`).

## Run starten

`llmwiki run start --workflow wiki-edit` (of hervat met `llmwiki run status`). Sync-wiki's hebben maar één fase vóór de gate: `validate`.

## Stappen

1. **PULL** (optioneel — de pagina kan al lokaal staan): `llmwiki pull --titel "<titel>"`. Gebruik MCP (`mcp__mediawiki__*`) om eerst te verkennen of te zoeken welke pagina relevant is; MCP is alleen-lezen en wijst altijd naar het hoofddoel (nooit een testomgeving).
2. **BEWERK**: pas het bestand onder `content/` direct aan. Raadpleeg relevante `sources/` of een eerder geëxporteerde `knowledge-base`-bron als achtergrond; dat is geen aparte fase, gewoon leeswerk vooraf.
3. **VALIDATE**: `llmwiki validate --schema page <bestand>` per gewijzigd bestand; verzamel het resultaat in `validation-report.json` (schema `validation-report`) en rond af met `llmwiki run complete validate --run
   <run-id> --data validation-report.json`.
4. **PLAN**: laad skill `wiki-publish` en volg die instructies. Voor een sync-wiki: `llmwiki publish plan --run <run-id> [--git | --pad <content/...>] [--doel staging]`. Zonder `--pad` verzamelt de CLI zelf de gewijzigde bestanden onder `content/` via git. Een nieuw pad (nooit gepulld) heeft een titel-override nodig: `--titel "content/pad=Titel"`.
5. **AKKOORD** en **PUBLISH**: zie skill `wiki-publish` (ongewijzigd: smaak A/B, nooit zelf akkoordvelden invullen, harness vraagt na akkoord nog om een klik).
6. **COMMIT**: na een geslaagde `llmwiki publish apply` staan `content/`, `revisies.json` en `log.md` klaar om te committen; zet de run-id in het commit-bericht.

## Testdoel (staging)

`--doel <naam-uit-wiki.yaml-test_targets>` bij `pull`/`publish plan`/`publish apply` stuurt naar een testomgeving in plaats van het hoofddoel. Nooit routinematig: de harness vraagt hier altijd om een klik ('ask'), en een testomgeving kan afwijken van productie (bijvoorbeeld periodiek ververst).

## Conflicten

Een pagina die op het doel is gewijzigd sinds ophalen, wordt door `llmwiki publish apply` geweigerd met een conflictmelding. Los dat op door opnieuw te pullen en de wijziging opnieuw toe te passen, niet door te forceren.
