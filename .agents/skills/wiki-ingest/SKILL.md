---
name: wiki-ingest
description: Neem een bron op in de centrale bronnen (laag 1 en 2) en maak of hergebruik de wiki-specifieke domein-lens (laag 3). Gebruik dit als eerste fase van elke wiki-update, wanneer nieuw bronmateriaal moet worden verwerkt.
metadata:
  kind: capability
  scope: core
  requires-tools: "llmwiki"
  reads: "bestand (pdf, docx, md)"
  writes: "source"
---

# Skill wiki-ingest

Doel: de INGEST-fase van de generieke workflow. Zorgt dat een bron beschikbaar is in de drie lagen uit `docs/onderbouwing.md` 5.19, zonder dubbel werk.

## Stappen

1. Bepaal het bron-id: `<jaar>-<uitgever>-<korte-titel>`, kleine letters en koppeltekens.
2. Bestaat `sources/index/<bron-id>.md` al? Dan staat de bron in laag 1; heeft de index nog geen `## Samenvatting`, volg dan eerst `wiki-intake`. Ga daarna naar stap 4.
3. Anders: `llmwiki source add <bestand> --id <bron-id> --titel "<titel>" --tags <tag1,tag2> [--brontype <wet|informatiemodel|beleid|overig>]`, of met `--url <url>` in plaats van een bestand (optioneel `--url-pagina` voor de pagina waarop de link stond). Dit kopieert het origineel en de Markdown-conversie naar `sources/raw/` en maakt in `sources/index/` een index met alleen gegevens en inhoudsopgave. Volg daarna `wiki-intake`: die controleert de conversie en vult de index.
   - Een bron is een letterlijke kopie: haal een webpagina altijd op met `--url`, nooit met een samenvattende web-tool, en vertaal of herschrijf de tekst niet.
   - Staan er op een pagina links naar documenten die bij de bron horen (één niveau diep), voeg elk toe als eigen bron met `--url <document> --url-pagina <pagina>`.
   - Of `--brontype` verplicht is en welke volgorde geldt, staat in de wiki-Rules en `wiki.yaml` (`bronvoorrang`).
4. Schrijf de domein-lens: een korte analyse van wat deze bron betekent voor het onderwerp van deze run, met paragraafverwijzingen naar laag 1, in `bronnen/<onderwerp>/<bron-id>.md` (of de locatie die `wiki.yaml` `page_types.bron.dir` aangeeft). Zet direct onder de titel de links naar laag 1: `llmwiki source bronregel <bron-id> --van <pad van de domein-lens> --schrijf`. Die regel is de schakel in de herleidbaarheid van pagina naar brontekst; de index (laag 2) is dat niet.
5. Rond de fase af: `llmwiki run complete ingest --run <run-id> --data <source.json volgens schema 'source'>`.

## Grenzen

Deze skill kent geen wiki-specifieke domeinkennis. Wiki-specifieke interpretatie (bijvoorbeeld: "is dit een bedrijfsobject?") hoort in een wiki-Skill die na deze fase wordt aangeroepen vanuit de wiki-Workflow.
