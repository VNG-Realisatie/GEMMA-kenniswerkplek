---
name: wiki-publish
description: Zet het gevalideerde changeset om in een publicatie- of promotievoorstel en begeleid de menselijke gate. Alleen op expliciete opdracht van de gebruiker aanroepen, nooit impliciet.
disable-model-invocation: true
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "validation-report"
  writes: "publish-plan"
---

# Skill wiki-publish

Doel: de GATE- en PUBLISH/PROMOTE-fase. Deze skill publiceert of promoveert nooit
zelfstandig; dat gebeurt alleen na een expliciete menselijke handeling.

## Stappen

1. `llmwiki run status` noemt de laatste fase voor deze wiki: `promote` (type B/C) of
   `publish` (type A, vereist Klus 2). Gebruik hieronder `promote`; `publish` werkt
   identiek zodra Klus 2 is gebouwd.
2. `llmwiki promote plan --run <run-id>`. Dit weigert als VALIDATE nog fouten heeft
   of als een pagina in de werkboom is gewijzigd sinds het gestagede concept is
   gemaakt. Het schrijft `voorstellen/<run-id>.md`.
3. Meld het pad van het voorstel aan de gebruiker en stop. Ga pas verder na een
   expliciete reactie:
   - **Smaak `document`**: de redacteur zet zelf `akkoord_voor_publicatie: ja` en
     `beoordeeld_door` in het voorstel, en vraagt daarna de publicatie uit te voeren.
     Wijzig deze velden nooit zelf.
   - **Smaak `chat`**: toon de samenvatting uit het voorstel in de chat en vraag
     letterlijk om het woord **AKKOORD**. "Prima" of "ziet er goed uit" is geen
     akkoord; vraag dan opnieuw.
4. Voer pas daarna uit: `llmwiki promote apply --run <run-id>` (smaak `document`) of
   `llmwiki promote apply --run <run-id> --akkoord-woord AKKOORD` (smaak `chat`,
   alleen als de gebruiker letterlijk AKKOORD typte). De CLI controleert het akkoord
   opnieuw; het harness vraagt de gebruiker daarna nog om een klik op "toestaan" —
   omzeil dat niet en zet geen automatische goedkeuring aan in een sessie waarin je
   publiceert.
5. Na een geslaagde apply staat de wijziging in `log.md` en is `voortgang.md`
   bijgewerkt. Meld dit aan de gebruiker.

## Grenzen

Deze skill roept nooit MediaWiki-schrijf-Tools rechtstreeks aan en schrijft nooit in
`voorstellen/`. Alle afdwinging loopt via `llmwiki`.
