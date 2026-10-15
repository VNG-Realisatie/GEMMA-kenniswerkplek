# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 1 tot en met 8 uitgevoerd. Stap 9 (de proef) is verplaatst naar het onderwerp Participatie (plan, Afwijking bij stap 9).
- De regel "Levensloopproces realiseert altijd een dienst" is vervallen. De niveauvraag van Verzorgen gemeentebegrafenis en de ontbrekende Logius-diensten van Lijkbezorging (crematoriumvergunning, rijden motorvoertuig op begraafplaats ontheffing) staan in [todo-later.md](todo-later.md), sectie Lijkbezorging.
- Participatie: `afbakening.yaml` (niveau `eigen`, status `in-behandeling`) en bronduidingen bestaan, beoordelingen nog niet.
- Nog niet gedaan: compacte uitvoer van `llmwiki promote plan`.

## Scope

Stap 9, de proef: het onderwerp Participatie (todo.md, Herbeoordeling), in een Sessie per fase (skill `gemma-archimate-model-update`). Meet per fase uit het transcript: beurten, totale invoer, grootste context, vragen en besluiten, en vergelijk ze met de tabel "Totaal per onderwerp" in het plan. Meet ook de ingest-subagent, hoe vaak een bronduiding na fase A wordt aangevuld (plan, Afwijking bij stap 7) en de omvang van het werkpakket, van het onderwerp en per cluster (plan, Afwijking bij stap 9).

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in de beslistabel, de typen en de uitkomsten.
- 2026-10-15: een levensloopproces groepeert één of meer bedrijfsprocessen die de UPL-diensten realiseren; het realiseert zelf geen dienst, en er komt geen regel of signaal voor.
- 2026-10-15: export alleen op verzoek van de redacteur, per afronding `--check`; een nieuwe regel die het woordbudget overschrijdt gaat eerst naar de redacteur.
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks.

## Modeladvies

De proef vraagt denkniveau hoog (een sterker model of hoge redeneerinspanning), in een nieuwe Sessie per fase. Begin een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 9 (de proef) uit van plannen/2026-10-15-lichtere-werkwijze.md: fase 1 van skill gemma-archimate-model-update voor het onderwerp Participatie, met de participatie-modelverordening als mogelijk beleidskader. Leg kort voor wat je doet, voer uit na mijn akkoord, en commit met een prefix. Houd bij hoeveel beurten en woorden de fase kost, en hoe groot het werkpakket is.
```
