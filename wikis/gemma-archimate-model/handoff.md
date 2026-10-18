# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Gedaan (todo "Potentiële relaties vastleggen", deel 2), elk met AKKOORD en commit: besluitvorming (15 kenmerken in acht processen) en participatie (3). Zonder bestaand element is `naar` een potentiële tegenpartij met naam en type: *bijdrage aan groter proces* naar een levensloopproces (bedrijfsproces, Beheren beschikkingen enzovoort), *aanleiding* naar een gebeurtenis in de voltooide vorm (Aanvraag ingediend, Besluit genomen). Bij Eindverslag inwonersparticipatie ontbrak de relatie: toegevoegd in Betrekken inwoners bij beleid (toegang, registreren).
- Inzicht: het kernrelatie-signaal controleert alleen kernrelaties van een type; bij *aanleiding* en *bijdrage aan groter proces* meldt het niets. Het getal in de todo (nu 225: lijkbezorging 109, burgerzaken 116) telt kenmerken zonder `naar`; een deel mist ook de relatie.

## Volgende klus

Kies uit [todo.md](todo.md): **Potentiële relaties vastleggen**, deel 2 voor lijkbezorging (109) of burgerzaken (116), elk in een eigen Sessie met een eigen AKKOORD en commit, eventueel in delen per kernobject; of participatie herbeoordelen, of GEMMA-functies onder *Ontvangst* terugmelden.

## Modeladvies

Eerst tellen welke kenmerken geen relatie hebben en wat het element-id of de potentiële tegenpartij is: nauwkeurig lezen, middel. Een sterker model (hoog) alleen bij de twijfelgevallen (levensloopproces of gebeurtenis die nog niet bestaat). Begin een nieuwe Sessie: beide onderwerpen zijn groot.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer deel 2 van het todo-punt "Potentiële relaties vastleggen" uit voor het onderwerp lijkbezorging (109 kenmerken): tel eerst per kenmerk of de relatie en het element bestaan (dan het id in `naar`, ontbreekt alleen de relatie dan toevoegen) of niet (dan naam en type met bron), werk in delen per kernobject, en leg elk geval waar dat twijfel geeft apart voor vóór je schrijft. Daarna beslissen, voorleggen, AKKOORD, afronden.py. Houd je aan de woordbudgetten in wiki.yaml.
```
