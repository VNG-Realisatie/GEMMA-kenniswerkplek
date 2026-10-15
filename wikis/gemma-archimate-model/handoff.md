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

In [todo.md](todo.md): **ArchiMate-indeling als eerste selectie in de beslistabel**, een eigen klus op denkniveau hoog, met een plan, vóór de Applicatielaag. Begin met een plan in `plannen/` en leg dat aan de redacteur voor; raak `tools/bepaal_type.py`, het schema en de beoordelingen pas na akkoord.

Afgerond in de laatste Sessie: de relaties *is grondslag voor* van de Gemeentewet naar Regeling (art. 147, 149), Heffingsverordening (art. 216), Heffing (art. 229, 229b) en Beleidsnota (art. 150 lid 1), via de specialisaties zonder pagina; AKKOORD 2026-10-15.

## Modeladvies

Denkniveau hoog: een sterker model of hoge redeneerinspanning, voor het plan en de omzetting van alle beoordelingen. Begin een nieuwe Sessie: de vorige draaide op een sneller model en is gevuld met de relaties.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en todo.md. Maak een plan (plannen/<datum>-archimate-indeling.md) voor de todo "ArchiMate-indeling als eerste selectie in de beslistabel": de laag en het aspect als eerste keuze, de bestaande kenmerken als controle, een omzetting met een script waarbij de uitkomsten gelijk blijven, en waar Product en Locatie komen. Leg het plan voor aan de redacteur en begin pas na akkoord met de uitvoering.
```
