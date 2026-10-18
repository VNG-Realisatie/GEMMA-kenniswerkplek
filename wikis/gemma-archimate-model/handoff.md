# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md): stap 2 tot en met 7 zijn klaar en gecommit, met hun AKKOORD (commit a3270ebe en 75093b8d).
- De regel "een gebeurtenis triggert geen gebeurtenis" staat in de volgende commit (rules): triggering Gebeurtenis → Gebeurtenis is weg uit de relatiematrix (`tools/kennismodel.py`), dus het bestaande signaal "buiten het kennismodel" meldt zo'n relatie; de afspraak bij Gebeurtenis zegt dat er altijd een bedrijfsproces tussen staat.
- Besluit van de redacteur: het verval van rechtswege loopt via de BRP-bijhouding. De vier relaties Naamswijziging, Overlijden, Verkrijging en Verlies van het Nederlanderschap → Verval van het reisdocument zijn vervallen; nieuw zijn Bijhouden persoonsgegevens ─triggering→ Verval van het reisdocument (HUP Van rechtswege vervallen) en Toevoegen latere vermelding ─stroom→ Bijhouden persoonsgegevens, "zendt akte aan" (HUP Wijziging voornaam).
- Zes elementen staan op review (`ter-beoordeling.md`): Bijhouden persoonsgegevens, Toevoegen latere vermelding en de vier gebeurtenissen. `archimate_export.py --check` en `tools/afronden.py` slagen pas na een nieuw AKKOORD.

## Volgende klus

Het AKKOORD voor de zes elementen: `uv run python -m llmwiki promote plan --wiki wikis/gemma-archimate-model`, het woord AKKOORD van de redacteur, `promote apply --akkoord-woord AKKOORD` en `uv run python tools/afronden.py --bericht "update: …"`. Daarna: de open punten in [todo.md](todo.md), "Potentiële relaties, wat open blijft", en de begrippen die nog voor te leggen zijn (`ter-beoordeling.md`).

## Modeladvies

Het AKKOORD en `afronden.py` vragen denkniveau laag: een sneller model is genoeg, en de lopende context kan blijven. De open punten van de potentiële relaties (de stand-ins beoordelen, en een signaal voor `ja` zonder `naar`) vragen denkniveau hoog; begin daarvoor een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en wikis/gemma-archimate-model/todo.md. De regel dat een gebeurtenis geen gebeurtenis triggert is gecommit (rules); zes elementen staan op review. Vraag eerst het AKKOORD: toon `uv run python -m llmwiki promote plan --wiki wikis/gemma-archimate-model` in de chat en wacht op het woord AKKOORD van de redacteur. Rond daarna af met tools/afronden.py. Ga dan verder met todo, "Potentiële relaties, wat open blijft". Leg alleen echte twijfel voor, zoals voor een architect (references/besluiten.md), met de bronpassage, de stand in GGM en GEMMA en de gevolgen per optie, en commit per afgerond deel met een prefix en commit-check.
```
