# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven.

## Stand van zaken

- Plan goedgekeurd: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md).
- Stap 1 tot en met 3 uitgevoerd (commits "rules: afspraken lichtere werkwijze", "tools: beoordeling.py", "fix: kandidaten geven weer treffers", "tools: werkpakket").
- Stap 4 uitgevoerd in twee commits:
  - "tools: twee fasen in de beslistabel": `bepaal_type.pad` (fase A: poort met stop, aard en de groep van die aard; fase B: de kenmerken van het type, stap 6 en 7 en de naregels). Een kenmerk buiten het pad leidt het script af als nee (`waarden`, `antwoord`, `antwoorden`). Elk kenmerk op het pad staat er expliciet in, en een nee op het pad heeft een onderbouwing; alleen in Aard en Soort gedrag mag een kale `nee` (schema `$defs/kenmerk`). Verder `bepaal_type.py vragen [<id>] [--type <paginatype>]` en `beoordeling.py normaliseer <id>… | --alle`, voor de schrijfvorm van één regel `sleutel: ja — onderbouwing [bron-id, id-…]` en het weglaten van een nee buiten het pad. `beslissen.py` geeft bij de schrijfvorm van één regel een fout met de verwijzing naar `normaliseer`. De gegenereerde vragenlijsten (criteria-skill, `kenmerken-en-beslistabel.md`) noemen het pad.
  - "chore: opschonen 453 beoordelingen": 16.402 nee's buiten het pad zijn weggelaten en 3.828 standaardteksten in Aard en Soort gedrag zijn een kale nee geworden. 22 eigen teksten zijn blijven staan, net als de nee's met bronnen. De beoordelingen gingen van 115.824 naar 58.962 regels. Gecontroleerd tegen een nulmeting: `beslist` en de status gelijk voor alle 453, pagina's en export gelijk (op de exportdatum na), waarschuwingen gelijk.
  - De inhoudshash veranderde, dus de 274 goedgekeurde elementen gingen naar review. De redacteur gaf AKKOORD (2026-10-15) en `llmwiki promote apply` zette de regels in `log.md`.
- Een ja buiten het pad blijft staan (282 keer, bijvoorbeeld *komt herhaald voor* bij een dienst). Het telt mee in de consistentie en staat op de pagina.
- Nog niet gedaan: compacte uitvoer van `llmwiki promote plan`. Het plan voor de 274 gaf 276 regels; dit valt onder stap 2 of 8, of als eigen punt in de todo.

## Scope

Stap 5 van het plan (A6, B2, B3, E2, A8): de update-, beoordelen- en criteria-skill herschrijven met fase A en B (`bepaal_type.py vragen`, schrijfvorm van één regel, `normaliseer`), het werkpakket, de tabel en de opdracht voor de beoordelingsagent; `beslissen.py --alleen`; ARCHITECTURE.md sectie 4 inkorten. Klaar als: gelezen regels per fase ≤ 12.000 woorden; lint zonder fouten. Daarna stap 6 en verder, elk in een eigen commit na akkoord.

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in deze klus: de beslistabel, de typen, de uitkomsten en de export blijven gelijk.
- Alleen de kenmerken met ja vastleggen is afgeraden; de nee die de uitkomst bepaalt, blijft als dubbelcheck (nu afgedwongen: elk kenmerk op het pad staat er expliciet in).
- 2026-10-15: na een opschoning die de inhoudshash raakt, gaat het akkoord opnieuw via de gewone poort (`promote plan`, AKKOORD, `promote apply`), met het bewijs dat `beslist`, de pagina's en de export gelijk blijven; commit pas na het akkoord.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst (voor de proef, stap 9).
- 2026-10-14: de plaats van Verzorgen gemeentebegrafenis is geparkeerd; het advies is optie 1 (voor de proef, stap 9).
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks; controles zijn gewone commando's. De vraag over `.pre-commit-config.yaml` staat in de root-`TODO.md`.
- De wiki-skills staan in `.agents/skills/`; `.claude/skills/` is een gitignored kopie, wijzig alleen `.agents/skills/`.

## Werkwijze

- Per stap: kort voorleggen wat er verandert, dan uitvoeren, dan commit met een prefix en een bericht van één of twee zinnen; controleer met `uv run python -m llmwiki commit-check <bestand>`.
- Voorleggen voor een architect: in gewone taal en analytisch, met de gevolgen voor het model, de bron als link.
- Commit direct op main.

## Modeladvies

Stap 5 vraagt denkniveau hoog: de skills bepalen hoe elke volgende beoordeling verloopt, en het woordbudget per fase vraagt afwegen wat blijft. Gebruik het sterkste model of de hoogste redeneerinspanning. Begin een nieuwe Sessie: deze context is vol met stap 4.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 5 uit van plannen/2026-10-15-lichtere-werkwijze.md (sectie Uitvoering): de skills herschrijven (A6, B2, B3, E2, A8) met fase A en B (bepaal_type.py vragen, de schrijfvorm van één regel, beoordeling.py normaliseer), het werkpakket, de tabel en de opdracht voor de beoordelingsagent; beslissen.py --alleen; ARCHITECTURE.md sectie 4 inkorten. Lees uit het plan alleen die rijen en de sectie Controle. Klaar als de gelezen regels per fase ≤ 12.000 woorden zijn en lint zonder fouten is. Leg kort voor wat je bouwt, voer uit na mijn akkoord, en commit met een prefix.
```
