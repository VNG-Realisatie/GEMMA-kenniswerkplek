# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md) is uitgevoerd: deel 1, 2 en 3, zie *Uitkomst stap 14*.
- Commit ab65582: stap 13 (Capability in het kennismodel). Commit d3bcbd6: de capability gebouwd (toets op twee functies, grondslag, render, Capabilitykaart, export, tests, skills).
- Commit van deze overdracht (`add:`): de capabilities Personen registreren, Identiteit vaststellen en Lijkbezorging waarborgen, de realisaties vanuit zes functies, de GEMMA-terugmelding nummer 9, en het AKKOORD voor die negen elementen.

## Volgende klus

Kies uit [todo.md](todo.md), sectie ArchiMate-indeling en Herbeoordeling:

1. **`beslist` uit de beoordeling halen** (tools, denkniveau middel): het blok is 23.000 woorden en wordt bij elk precedent meegelezen; het kan naar een gegenereerd bestand per onderwerp. Dat maakt elke volgende beoordeling goedkoper. Advies: deze eerst.
2. **Potentiële relaties vastleggen** (inhoud, middel): 239 relationele kenmerken ja zonder relatie.
3. **Participatie herbeoordelen** met de lichtere werkwijze (inhoud, hoog voor de beoordeling).

## Modeladvies

Optie 1 is scriptwerk met een migratie van alle beoordelingen: denkniveau middel, een sterk model voor de code (de migratie raakt 481 bestanden en het akkoord-hash). Begin een nieuwe Sessie: het is een ander onderwerp.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer het todo-punt "`beslist` uit de beoordeling halen" uit: stel eerst in een korte opzet voor waar het gegenereerde blok komt, hoe beslissen.py, render.py, archimate_export.py en het akkoord-hash het lezen, en hoe de migratie gaat zonder nieuw AKKOORD (de uitkomsten, de pagina's en archimate_export.py --check blijven gelijk). Leg de opzet voor vóór je bouwt. Houd je aan de woordbudgetten in wiki.yaml.
```
