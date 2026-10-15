# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md), deel 1 is omgezet (commit `rules:` van 2026-10-15): keuzevelden `vak`, `hoofdkenmerk` en `soort_gedrag`, de poort als uitzondering, standaardwaarden, en relationele kenmerken met hun tegenpartij in `naar`. De besluiten en metingen staan in *Uitkomst stap 3–7*.
- O3 is bijgesteld: het kenmerk wordt niet afgeleid uit de relatie, maar noemt zijn tegenpartij; de bron komt van de relatie als die bestaat.
- `beslist` is gelijk aan de stand vóór de omzetting (op de regelnummers na). De 285 goedgekeurde elementen staan op review, omdat het akkoord-hash de kenmerken telt.

## Volgende klus

1. Als dat nog niet gebeurd is: nieuw AKKOORD voor de 285 elementen (skill gemma-archimate-model-update, stap 13–17: `llmwiki promote plan`, AKKOORD van de redacteur, `promote apply`, `tools/afronden.py --bericht "chore: …"`). Controleer daarna dat `tools/archimate_export.py --check --rapport` gelijk is aan dat van de commit vóór de omzetting (508e1d0).
2. Deel 2 van het plan: data-object als element (stap 8–11), met de open punten *Naam van een data-object* en *Wie nog meer data-objecten heeft*.

## Modeladvies

Stap 1 is laag (scripts en het akkoord). Deel 2 vraagt denkniveau hoog voor het ontwerp (stap 8) en de 19 bedrijfsobjecten (stap 10), middel voor stap 9: een nieuwe Sessie met een sterk model of hoge redeneerinspanning.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-15-archimate-indeling.md (deel 1 omgezet, zie Uitkomst stap 3–7). Controleer eerst of de 285 elementen weer goedgekeurd zijn; zo niet, volg skill gemma-archimate-model-update stap 13–17 voor een nieuw AKKOORD. Voer daarna deel 2 uit (stap 8–11): data-object als veld `data_objecten` bij het bedrijfsobject, het element en de realisatie door het script, de GGM-terugmelding, registr*-signaal niet bij een bedrijfsobject. Leg de open punten (naam van een data-object, wie nog meer data-objecten heeft) eerst voor, en de 19 bedrijfsobjecten met geautomatiseerd verwerkt ja per geval in één tabel. Commit met prefix rules en add.
```
