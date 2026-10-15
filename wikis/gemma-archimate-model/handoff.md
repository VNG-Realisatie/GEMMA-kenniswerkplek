# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits en de todo.

## Stand van zaken

- Plan [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md) is afgerond: de uitkomst van de proef staat onder *Uitkomst stap 9*, de open bevindingen in [todo.md](todo.md).
- Besluiten herzien (commits 791d423, da01fb6, fb93af5, 13c5312):
  - geen status `kandidaat` en geen opnemen-besluit meer; de redenen om voor te leggen staan bij het element tot het AKKOORD (kolom Voorleggen omdat in fase 3);
  - de besluiten tellen niet mee in de hash van het akkoord;
  - een besluit legt alleen inhoud vast, volgens de criteria in `references/besluiten.md` van skill gemma-archimate-model-beoordelen; een herzien besluit verdwijnt;
  - 328 besluiten zijn er 107 geworden; verwijzingen "(besluit 2026-…)" staan niet meer in de inhoud;
  - elk besluit heeft een zekerheid (`kennis`, `logica`, `indruk`; zonder veld `logica`), met de regel Navragen en de precedentregel;
  - twee nieuwe regels: bestuursorganen via de rol Beslisser (rol-modelleerafspraken) en eigen handeling van de gemeente (modelleerregel Gemeentelijk perspectief);
  - alle 284 elementen zijn weer goedgekeurd (AKKOORD 2026-10-15).
- Tot ongeveer 15 begrippen doet de hoofdsessie fase B zelf (skill gemma-archimate-model-update, stap 8).

## Volgende klus

In [todo.md](todo.md), in deze volgorde:

1. **Gemeentewet als grondslag voor de andere onderwerpen** (Herbeoordeling): de relaties *is grondslag voor* naar Lijkbezorging (art. 147, 149, 229), Heffingen en betalingen en Besluitvorming (art. 150 bij Beleidsnota). Klein, denkniveau middel; een onderdeel van een onderwerp volgens skill gemma-archimate-model-update, fase 3.
2. **ArchiMate-indeling als eerste selectie in de beslistabel**: een eigen klus op denkniveau hoog, met een plan, vóór de Applicatielaag.

## Modeladvies

Klus 1 vraagt denkniveau middel: relaties toevoegen met bron en vindplaats, beslissen, voorleggen in één tabel, akkoord. Een sneller model volstaat. Begin een nieuwe Sessie: deze is gevuld met de besluiten.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Voer de todo "Gemeentewet als grondslag voor de andere onderwerpen" uit volgens skill gemma-archimate-model-update (fase 3, zonder nieuwe begrippen): leg per element de relatie is grondslag voor vanuit de beoordeling gemeentewet vast, met het artikel als vindplaats en een citaat in de bronduiding (tools/bronduiding.py). Draai tools/beslissen.py, leg in één tabel voor met de kolommen Voorleggen omdat en Eerder besluit (zekerheid), en vraag om AKKOORD. Leg een besluit alleen vast volgens de criteria in references/besluiten.md. Daarna afronden met tools/afronden.py en een commit met prefix add of update.
```
