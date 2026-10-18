# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Gedaan (todo "Potentiële relaties vastleggen", deel 2, besluitvorming), met AKKOORD: de 15 relationele kenmerken `ja` zonder `naar` in acht processen. Er bestond bij geen enkele een relatie en geen element om naar te wijzen, dus `naar` is een potentiële tegenpartij met naam en type: *bijdrage aan groter proces* naar Beheren beschikkingen, Beheren bezwaarschriften, Beheren schriftelijke klachten en Beheren besluiten (bedrijfsproces); *aanleiding* naar gebeurtenissen (Aanvraag ingediend, Bezwaarschrift ingediend, Besluit genomen enzovoort). De onderbouwing van *bijdrage* bij Behandelen bezwaar volgt nu het kernobject Bezwaarschrift.
- Inzicht: het kernrelatie-signaal controleert alleen kernrelaties van een type; bij *aanleiding* en *bijdrage aan groter proces* meldt het niets. Het getal in de todo (nu 228) telt kenmerken zonder `naar`; een deel mist ook de relatie.

## Volgende klus

Kies uit [todo.md](todo.md): **Potentiële relaties vastleggen**, deel 2 voor participatie (3), daarna lijkbezorging (109) en burgerzaken (116), elk onderwerp met een eigen AKKOORD en commit; of participatie herbeoordelen, of GEMMA-functies onder *Ontvangst* terugmelden.

## Modeladvies

Eerst tellen welke kenmerken geen relatie hebben en wat het element-id of de potentiële tegenpartij is: nauwkeurig lezen, middel. Een sterker model (hoog) alleen bij de twijfelgevallen (levensloopproces of gebeurtenis die nog niet bestaat); die leg je apart voor. Een nieuwe Sessie is verstandig voor lijkbezorging of burgerzaken (veel kenmerken, volle context).

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer deel 2 van het todo-punt "Potentiële relaties vastleggen" uit voor het onderwerp participatie (3 kenmerken): bepaal per relationeel kenmerk ja zonder `naar` of de relatie en het element bestaan (dan het id in `naar`) of niet (dan naam en type met bron), en leg elk geval waar dat twijfel geeft apart voor vóór je schrijft. Daarna beslissen, voorleggen, AKKOORD, afronden.py. Houd je aan de woordbudgetten in wiki.yaml.
```
