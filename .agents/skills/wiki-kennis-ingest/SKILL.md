---
name: wiki-kennis-ingest
description: Verwerk een bron tot een notitie, advies, ontwerp of architectuurdocument in een knowledge-base-wiki. Gebruik wanneer de gebruiker vraagt een bron te verwerken of een document bij te werken in een wiki van soort knowledge-base.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "source"
  writes: "page"
---

# Skill wiki-kennis-ingest

Voor een **knowledge-base**-wiki (`wiki.yaml` `type: knowledge-base`):
ongestructureerde kennisopbouw — notities, adviezen, ontwerpen,
architectuurdocumenten. Dit zijn op zichzelf al volwaardige eindresultaten, geen
tussenstap. Geen run, geen fasen, geen gate: review gebeurt via een gewone `git
diff`/commit, zoals bij elk ander document in de repository.

## Stappen

1. Bestaat de bron nog niet in `sources/index/`? Volg eerst skill `wiki-ingest`
   (laag 1/2). Deze skill gaat verder vanaf een bestaande bronintake.
2. Lees de volledige bron.
3. Zoek relevante bestaande documenten in deze wiki (per onderwerp-map) op
   hetzelfde of een verwant onderwerp.
4. Classificeer:
   - **nieuw** — nog geen document over dit onderwerp;
   - **bijwerken** — een bestaand document moet inhoudelijk worden aangepast;
   - **tegenstrijdig** — de bron spreekt een bestaand document tegen: markeer dit
     expliciet in het document, overschrijf niets stilzwijgend;
   - **geen materiaal** — de bron voegt niets toe; geen wijziging.
5. Schrijf of werk het document direct bij (`<onderwerp>/<document>.md`).
   Frontmatter minimaal `id`/`onderwerp`/`bronnen`; geen `status`-veld. Elke
   feitelijke claim moet herleidbaar zijn naar een bron-id in `bronnen:`
   (bewijsregel) — bij onvoldoende bewijs: niet wijzigen, rapporteer wat
   ontbreekt.
6. Controleer de bewijsregel: `llmwiki validate --schema page <bestand>`
   (controleert dat elke genoemde bron bestaat in `sources/index/` en binnen de
   scope van deze wiki valt).
7. Meld aan de gebruiker welke documenten zijn bijgewerkt, welke bronnen zijn
   gebruikt, en of er conflicten zijn gevonden. De gebruiker beoordeelt via
   `git diff` en commit zelf (of vraagt dat te doen).

## Overdracht naar een andere wiki (optioneel)

Een document kan later input worden voor een sync- of curatie-wiki:
`llmwiki source add --from-export <deze-wiki>/<pad>`. Dat is een mogelijk
vervolg, niet het doel van deze skill.

## Grenzen

Publiceert nooit rechtstreeks naar een externe site. Een wijziging die daarvan
afhangt, is een gewone bewerking in de betreffende sync-wiki, via skill
`wiki-edit` — niet vanuit deze skill.
