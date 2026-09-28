# gemma-wiki (sync)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de
Context staan: lees dat bestand voordat je iets wijzigt.

## Domein

- Bron: GEMMA Online (`redactie.gemmaonline.nl`), de landelijke architectuur- en
  standaardenwiki voor gemeenten (VNG Realisatie). Taal: Nederlands.
  Doelgroep: informatiearchitecten en beleidsmedewerkers bij gemeenten en VNG.
- Naamruimtes in scope: hoofdnaamruimte (0), `MediaWiki:` (8, o.a. zijbalk) en
  `Sjabloon:`/`Template:` (10) — zie `wiki.yaml` → `content.namespaces`.
  `Categorie:`/`Category:` (14) is namespace-alias voor `Sjabloon:` t.o.v.
  `Template:`: dezelfde pagina, twee namen.
- Alleen actuele pagina's overnemen: controleer de `{{Publicatie|...|
  Redactiestatus=...}}`-header; alleen `Actueel` bijwerken, `Gearchiveerd`
  overslaan. (Nog niet geautomatiseerd in `llmwiki pull` — tot die tijd handmatig
  controleren vóór het ophalen van een pagina.)
- Staging (`gemma2-redactie.staging.wikixl.nl`, `wiki.yaml` → `test_targets.staging`)
  is een periodiek ververste testkopie van productie, geen aparte bron: alleen
  gebruiken om de `wiki-edit`-workflow te oefenen vóór publicatie naar het
  hoofddoel; niet zelf inhoudelijk bewerken alsof het de bron van waarheid is.
- Achtergrond en een oudere, los van deze monorepo werkende implementatie
  (categoriehiërarchie-mapstructuur, bulk-pull, Redactiestatus-filter) staat in
  `~/Documents/GitHub/GEMMA-wiki beheren/CLAUDE.md` — nuttig als referentie
  zolang `content.layout: category` hier nog niet is gebouwd, maar geen
  onderdeel van deze repository en niet als afhankelijkheid te gebruiken.

## Standaard Workflow

Gebruik skill `wiki-edit` voor het bijwerken van pagina's (PULL → BEWERK →
VALIDATE → PLAN → AKKOORD → PUBLISH). Dit is een sync-wiki: `content/` is een
directe werkkopie van de externe site, geen curatiepijplijn.
