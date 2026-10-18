# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- De regel "een gebeurtenis triggert geen gebeurtenis" is gecommit en goedgekeurd, en de export is opnieuw gemaakt (commits d34b6e38, 5dd56ffc en 169b22dd).
- Nieuw plan: [plannen/2026-10-18-afleidbare-indeling.md](plannen/2026-10-18-afleidbare-indeling.md). De export laat een aggregatie van een groepering weg als het element al via een ander element onder die groepering te vinden is (de grondslagketen: *werkt uit* en *is grondslag voor*), in de Beleidsdomeinindeling en de Grondslagindeling. De besluiten van de redacteur staan in hoofdstuk 3, de voorbeelden in hoofdstuk 4 (97 van de 157 en 5 van de 20 aggregaties vallen weg).

## Volgende klus

Het plan uitvoeren, hoofdstuk 5, stap 1 tot en met 7. Stap 1 (de vaste naam afdwingen) levert één afwijking op om voor te leggen: *is model voor (algemene plaatselijke verordening)*. Daarna: de open punten in [todo.md](todo.md), "Potentiële relaties, wat open blijft", en de begrippen die nog voor te leggen zijn (`ter-beoordeling.md`).

## Modeladvies

De uitvoering is code in `tools/kennismodel.py` en `tools/archimate_export.py`, met tests, op een plan dat vastligt: denkniveau middel, met hoog voor de ankerbepaling (kringen, andere groepering) in stap 3. Begin een nieuwe Sessie: het interview heeft de context gevuld met analyses die nu in het plan staan.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en wikis/gemma-archimate-model/plannen/2026-10-18-afleidbare-indeling.md. Voer hoofdstuk 5 van het plan uit, stap voor stap; de besluiten in hoofdstuk 3 gelden en worden niet opnieuw gevraagd. Leg de afwijkende relatienaam uit stap 1 voor zoals voor een architect (references/besluiten.md). Controleer de export na stap 7 tegen de voorbeelden in hoofdstuk 4. Commit per afgerond deel met een prefix (rules, tools, export) en commit-check.
```
