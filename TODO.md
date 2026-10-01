# Takenlijst

## Open

- [ ] **Technische index vullen (laag 2).** `sources/index/` is een technische index om context te sparen, geen schakel in de herleidbaarheid (besloten 2026-09-30; zie `ARCHITECTURE.md`, *Bronnen: drie lagen*, en `docs/onderbouwing.md` 5.19). Alle 271 bestaande indexen bevatten alleen gegevens en "Nog geen samenvatting.". Eerst deterministisch voor alle bronnen de inhoudsopgave zetten (`llmwiki source inhoud <bron-id> --schrijf`), daarna per bron skill `wiki-intake` voor samenvatting, trefwoorden en begrippen. Volgorde: eerst de bronnen van onderwerpen waar een wiki actief aan werkt (nu `lijkbezorging` in gemma-archimate-model), dan de rest.
- [ ] **Controle op de index.** `llmwiki validate --schema source-index` accepteert alleen JSON, niet de frontmatter van `sources/index/<bron-id>.md`. Laat `llmwiki lint` de frontmatter tegen het schema controleren en waarschuwen bij tekstsecties boven 400 woorden of een index zonder `## Inhoud`.
- [ ] **Controle op de bronregel voor alle wiki's.** Dat een domein-lens onder de titel naar laag 1 linkt, controleert nu alleen `wikis/gemma-archimate-model/tools/check_elementen.py`. Maak er een gedeelde controle van in `llmwiki validate` (domein-lens herkennen via `wiki.yaml` `page_types`) zodra een tweede wiki domein-lenzen heeft.
- [ ] **Wet BRO opnieuw ophalen.** `sources/raw/2026-rijk-wet-bro-bwbr0037095.md` is een verkorte webclip (744 woorden, begrippen ingekort), geen letterlijke kopie van de wettekst; er is geen origineel naast. Opnieuw opnemen met `llmwiki source add --url https://wetten.overheid.nl/BWBR0037095/...` en de oude bron vervangen (gevonden 2026-10-01 bij de analyse van gegevensrollen).
- [ ] **Pad met backslashes in zes indexen.** Zes indexen in `sources/index/` (bronnen met een html-origineel van vóór 2026-10-01) hebben een `pad` met backslashes in plaats van slashes. `llmwiki source add` schrijft sinds 2026-10-01 slashes; de bestaande paden nog omzetten.

## Afgerond

- [x] Harde regelovergangen verwijderd uit alle Markdown waarvoor de regel in `AGENTS.md` (Schrijfwijze) geldt (35 bestanden), met `llmwiki ontvouw --schrijf`. `llmwiki lint` meldt nieuwe harde regelovergangen; codeblokken, frontmatter, tabellen, koppen en tekst zijn ongewijzigd gebleven (gecontroleerd).
