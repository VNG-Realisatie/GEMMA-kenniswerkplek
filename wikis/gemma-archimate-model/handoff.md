# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Gedaan in deze Sessie (todo "Potentiële relaties vastleggen", deel 1): de twee kenmerken *wordt bewerkt* zonder relatie zijn opgelost, met AKKOORD. Beleidsregel heeft een toegang vanuit Bekendmaken besluit (Awb art. 3:42, 4:83) en de potentiële relatie "Vaststellen beleidsregel" (bedrijfsproces, art. 4:81); Heffingsverordening de potentiële relatie "Heffen van belastingen en rechten" (bedrijfsproces), volgens het besluit van 2026-10-10.
- Inzicht: het getal 239 in de todo telde kenmerken zonder `naar`, niet zonder relatie. De regel (kennismodel/kenmerken-en-beslistabel.md) vraagt bij elk relationeel kenmerk `ja` een `naar`; het kernrelatie-signaal controleert alleen of de relatie bestaat. Nu nog 243 zonder `naar`, alle met relatie: burgerzaken 116, lijkbezorging 109, besluitvorming 15, participatie 3.

## Volgende klus

Kies uit [todo.md](todo.md), sectie ArchiMate-indeling en Herbeoordeling:

1. **Potentiële relaties vastleggen**, deel 2: de `naar` aanvullen bij de bestaande relaties, per onderwerp (besluitvorming eerst, 15; dan participatie, lijkbezorging, burgerzaken), elk onderwerp met een eigen AKKOORD en commit.
2. **Participatie herbeoordelen** met de lichtere werkwijze (inhoud, hoog voor de beoordeling).
3. **GEMMA-functies onder *Ontvangst*** terugmelden (inhoud, middel), of **GGM-match voor rollen, actoren en gebeurtenissen**.

## Modeladvies

Optie 1 is vooral nauwkeurig vastleggen (middel): een sneller model volstaat, met een sterker model alleen als een `naar` naar een ander element wijst dan de relatie suggereert. Dit kan in een nieuwe Sessie; het tellen gaat met de kenmerken uit `tools/bepaal_type.py` (RELATIONEEL) zonder `naar`. Overweeg een signaal in `tools/signalen.py` voor een relationeel kenmerk `ja` zonder `naar` (leg dat eerst voor: een nieuw signaal is een rules-wijziging).

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer deel 2 van het todo-punt "Potentiële relaties vastleggen" uit voor het onderwerp besluitvorming: vul bij elk relationeel kenmerk ja zonder `naar` het id van het element met de relatie in, en leg elk geval waar de relatie twijfel geeft apart voor vóór je schrijft. Daarna beslissen, voorleggen, AKKOORD, afronden.py. Houd je aan de woordbudgetten in wiki.yaml.
```
