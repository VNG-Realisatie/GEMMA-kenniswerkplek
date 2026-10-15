# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven.

## Stand van zaken

- Plan goedgekeurd: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md).
- Stap 1 en 2 uitgevoerd (commits "rules: afspraken lichtere werkwijze" en "tools: beoordeling.py").
- Herstel (commit "fix: kandidaten geven weer treffers"): in `tools/ggm.py` en `tools/gemma.py` stond sinds 8248aa5 een backspace-teken in plaats van `\b` in de zoekregel van `kandidaten`, waardoor alleen naamgenoten werden gevonden en nooit treffers op een deel van de naam of de definitie.
- Stap 3 uitgevoerd (commit "tools: werkpakket"): `tools/werkpakket.py <onderwerp> [--cluster <kernobject>] [--alles]` schrijft `.work/werkpakket/<onderwerp>[-<cluster>].md` met het onderwerp en de geldende besluiten, de onderwerpen, de begrippen uit de bronduidingen met wat de catalogus kent, de passages uit `sources/raw/`, de GGM- en GEMMA-kandidaten (met terugval op de woorden van de naam, GEMMA alleen de bedrijfslaag), de UPL (VNG-lijsten en Logius) op grondslag en naam met de dekking, de relatievoorstellen, de modelleerafspraken en de terugmeldingen. Getoetst aan het transcript van Besluitvorming plak 2: de Awb-artikelen, de UPL-producten (nr. 47, 48, 54, 64, 212, 386, en dwangsom bij niet tijdig beslissen uit Logius) en de GEMMA-kandidaten (Bezwaar- en beroepafhandeling, Klachten afhandeling, Uitvoeren inspraakprocedure) staan erin. Niet gevonden: GEMMA "Schade gerelateerde diensten" voor nadeelcompensatie (alleen via "schade" in de definitie).
- Omvang: Besluitvorming 15.000 woorden (nieuwe begrippen), 20.000 met `--alles`; cluster Bezwaar 1.900; Lijkbezorging 35.000 (veel bestaande begrippen en besluiten: gebruik daar `--cluster`).
- Nog niet gedaan: compacte uitvoer van `promote plan` (in `tools/llmwiki`) en het noemen van de nieuwe commando's en het werkpakket in de skills (stap 5).
- Volgende stap: stap 4, twee fasen (B1, A5, C1, C5).

## Scope

Stap 4 van het plan, zie de sectie Uitvoering en de rijen B1, A5, C1 en C5: `bepaal_type.py vragen <id>`, het pad en de afgeleide nee in `beslissen.py`, het schema, `normaliseer`, en het opschonen van de 453 beoordelingen. Daarna stap 5 en verder, elk in een eigen commit na akkoord.

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in deze klus: de beslistabel, de typen, de uitkomsten en de export blijven gelijk. Klaar als (stap 4): dezelfde `beslist:` voor alle 453 beoordelingen, de pagina's gelijk, de export inhoudelijk gelijk.
- Alleen de kenmerken met ja vastleggen is afgeraden; de nee die de uitkomst bepaalt, blijft als dubbelcheck.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst (voor de proef, stap 9).
- 2026-10-14: de plaats van Verzorgen gemeentebegrafenis is geparkeerd; het advies is optie 1 (voor de proef, stap 9).
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks; controles zijn gewone commando's. De vraag over `.pre-commit-config.yaml` staat in de root-`TODO.md`.
- De wiki-skills staan in `.agents/skills/`; `.claude/skills/` is een gitignored kopie, wijzig alleen `.agents/skills/`.

## Werkwijze

- Per stap: kort voorleggen wat er verandert, dan uitvoeren, dan commit met een prefix en een bericht van één of twee zinnen; controleer met `uv run python -m llmwiki commit-check <bestand>`.
- Voorleggen voor een architect: in gewone taal en analytisch, met de gevolgen voor het model, de bron als link.
- Commit direct op main.

## Modeladvies

Stap 4 vraagt denkniveau hoog: het pad door de beslistabel en de afgeleide nee bepalen of de uitkomst van 453 beoordelingen gelijk blijft. Gebruik het sterkste model of de hoogste redeneerinspanning. Begin een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 4 uit van plannen/2026-10-15-lichtere-werkwijze.md (sectie Uitvoering): twee fasen (B1, A5, C1, C5) — bepaal_type.py vragen <id>, het pad en de afgeleide nee in beslissen.py, het schema, normaliseer, en het opschonen van de 453 beoordelingen. Lees uit het plan alleen de rijen B1, A5, C1 en C5 en de sectie Controle. Klaar als beslist: voor alle 453 beoordelingen gelijk blijft, de pagina's gelijk zijn en de export inhoudelijk gelijk. Leg kort voor wat je bouwt, voer uit na mijn akkoord, en commit met een prefix.
```
