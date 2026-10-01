---
name: wiki-publish
description: Zet de gevalideerde wijzigingen van een sync-wiki om in een publicatievoorstel en begeleid de menselijke gate. Alleen op expliciete opdracht van de gebruiker aanroepen, nooit impliciet.
disable-model-invocation: true
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "validation-report"
  writes: "publish-plan"
---

# Skill wiki-publish

Doel: de GATE- en PUBLISH-fase van `wiki-sync-edit`. Deze skill publiceert nooit zelfstandig; dat gebeurt alleen na een expliciete menselijke handeling. Een curatie-wiki met beoordelingen gebruikt deze skill niet: daar regelt `wiki-curatie-update` het akkoord (stap 6 tot 8).

## Stappen

1. `llmwiki run status` noemt de laatste fase voor deze wiki: `publish` (sync) of `promote` (curatie). Hieronder staat `<commando>` voor welke van de twee van toepassing is — verder identiek.
2. `llmwiki <commando> plan --run <run-id>` (bij een sync-wiki, optioneel `--doel staging` voor een testomgeving; zonder `--pad` verzamelt de CLI zelf de gewijzigde bestanden onder `content/` via git). Dit weigert als VALIDATE nog fouten heeft, of als een pagina gewijzigd is sinds ophalen/staging. Het schrijft het voorstel `voorstellen/<run-id>.md` en de volledige diffs in `voorstellen/<run-id>-details.md`.
3. Het voorstel is een plan: per pagina één tabelrij met een samenvatting en de kolommen **Besluit** (`goedkeuren` of `schrijven`/`publiceren`, `overslaan`, `aanpassen`) en **Opmerking**, en daaronder de open vragen uit de pagina's (*Ter discussie*). Meld het pad aan de gebruiker, noem in de chat hoeveel pagina's in elke groep staan en welke vragen open staan, en stop. De redacteur beoordeelt en wijzigt het plan in de eigen editor. Wijzig het voorstel nooit zelf: niet de akkoordvelden en niet de kolommen Besluit en Opmerking.
4. Reageer op wat de redacteur daarna vraagt:
   - **Opmerkingen verwerken** (er staat `aanpassen`, of er staan opmerkingen onder *Opmerkingen*): lees het voorstel, verwerk elke opmerking in de gestagede pagina's van de run (fase WRITE van de wiki-workflow), draai de controles van VALIDATE opnieuw op de gewijzigde pagina's en maak een nieuw plan (stap 2). Besluiten voor ongewijzigde pagina's blijven bewaard; het akkoord staat weer op `nee`. Meld per opmerking wat je hebt gedaan.
   - **Smaak `document`, uitvoeren**: de redacteur heeft zelf `akkoord_voor_publicatie: ja` en `beoordeeld_door` ingevuld.
   - **Smaak `chat`**: toon de tabellen uit het voorstel in de chat en vraag letterlijk om het woord **AKKOORD**. "Prima" of "ziet er goed uit" is geen akkoord; vraag dan opnieuw.
5. Voer pas daarna uit: `llmwiki <commando> apply --run <run-id>` (smaak `document`) of `llmwiki <commando> apply --run <run-id> --akkoord-woord AKKOORD` (smaak `chat`, alleen als de gebruiker letterlijk AKKOORD typte). De CLI controleert het akkoord opnieuw en volgt de besluiten: `overslaan` wordt niet geschreven, `aanpassen` blokkeert de uitvoering, een ontbrekende rij of een besluit dat niet mag (bijv. `goedkeuren` voor een kandidaat) ook. Het harness vraagt de gebruiker daarna nog om een klik op "toestaan" — omzeil dat niet en zet geen automatische goedkeuring aan in een sessie waarin je publiceert.
6. Na een geslaagde apply staat de wijziging in `log.md` (sync/curatie) en, voor curatie, is `voortgang.md` bijgewerkt. Meld dit aan de gebruiker.

## Grenzen

Deze skill roept nooit MediaWiki-schrijf-Tools rechtstreeks aan en schrijft nooit in `voorstellen/`. Alle afdwinging loopt via `llmwiki`.
