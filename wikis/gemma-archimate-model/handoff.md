# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md): stap 2 tot en met 6 zijn klaar en gecommit; het AKKOORD voor 284 elementen staat in [log.md](log.md) (commit a3270ebe) en het eenmalige omzetscript is verwijderd.
- Stap 7 (potentiële relaties) is uitgevoerd in de volgende commit: de 82 relatiekenmerken `ja` zonder `naar` van elementen hebben hun tegenpartij (ca. 50 stand-in gebeurtenissen, de GEMMA-functies als bedrijfsfunctie, id's van rollen en objecten) en de ontbrekende relaties zijn toegevoegd (toewijzingen voor Onderhouden graf, Verlenen toestemming asverstrooiing en Verlenen vergunning grafbedekking; toegang voor zes functies; triggering Overlijden → Toestaan lijkbezorging).
- Besluiten van de redacteur in deze Sessie: rollen van een levensloopproces blijven bij de deelprocessen (het kenmerk verwijst ernaar); een gebeurtenis mag geen gebeurtenis triggeren (Verval van het reisdocument triggert nu direct Inhouden reisdocument); Verklaring van overlijden wordt een nieuw bedrijfsobject (stand-in) naast Vergunning.
- Alle elementen die stap 7 raakte, staan op review: `tools/afronden.py` en `archimate_export.py --check` slagen pas na een nieuw AKKOORD. Open punten: [todo.md](todo.md), "Potentiële relaties, wat open blijft".

## Volgende klus

De redacteur bekijkt de pagina's (`uv run python -m llmwiki promote plan --wiki wikis/gemma-archimate-model`), typt AKKOORD, daarna `promote apply --akkoord-woord AKKOORD` en `uv run python tools/afronden.py --bericht "<prefix>: …"`. Daarna: de regel over gebeurtenissen die gebeurtenissen triggeren voorleggen (rules), en de 15 begrippen die nog zijn voor te leggen (`ter-beoordeling.md`).

## Modeladvies

Het AKKOORD en `afronden.py` zijn denkniveau laag: een sneller model volstaat en de lopende context is nog te gebruiken. De regelwijziging voor gebeurtenissen (matrix, signaal, de vier relaties) is denkniveau hoog; begin daarvoor een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en wikis/gemma-archimate-model/todo.md. Stap 7 van plan 2026-10-18 (potentiële relaties) is gecommit; de geraakte elementen staan op review. Vraag eerst het AKKOORD: toon `uv run python -m llmwiki promote plan --wiki wikis/gemma-archimate-model` in de chat en wacht op het woord AKKOORD van de redacteur. Rond daarna af met tools/afronden.py. Ga dan verder met het voorleggen van de regel dat een gebeurtenis geen gebeurtenis triggert (todo, "Potentiële relaties, wat open blijft", punt 1). Leg alleen echte twijfel voor, zoals voor een architect (references/besluiten.md), en commit per afgerond deel met een prefix en commit-check.
```
