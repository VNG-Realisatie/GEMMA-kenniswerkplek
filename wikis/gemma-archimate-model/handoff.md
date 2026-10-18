# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Todo "Potentiële relaties vastleggen", deel 2, voor lijkbezorging is gestopt na het tellen. Van de 109 open relatiekenmerken horen er 61 bij specialisaties zonder pagina, en verder bij onderdelen, een deelproces en synoniemen. Bij geen enkele bestond de relatie al. Dat leidde tot een herziening van de beslistabel.
- Plan [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md): vier fasen (Afbakenen, Typeren, Onderbouwen, Indelen), zeven stappen, nieuwe termen (keuzekenmerk, relatiekenmerk, toetskenmerk, standaardantwoord en afwijking), V1 tot en met V10 en A1 tot en met A8. De redacteur heeft alle besluiten genomen (hoofdstuk 7); er is nog niets gebouwd.

## Volgende klus

Uitvoering van het plan, hoofdstuk 8, stap 2 tot en met 6. Eerst de code (stap 2), daarna de bronnen van de aanpak (stap 3), de regels en skills (stap 4), de omzetting (stap 5) en beslissen, voorleggen en AKKOORD (stap 6). Pas daarna verder met lijkbezorging, deel 2 van de todo.

## Modeladvies

Stap 2 tot en met 5 zijn nauwkeurig bouwen en omzetten: denkniveau middel; een sneller model volstaat, met de tests en de vergelijking van `beslist.yaml` als vangnet. Stap 6 (voorleggen van verschillen) vraagt denkniveau hoog. Begin een nieuwe Sessie: deze is vol met analyse.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en plannen/2026-10-18-beslistabel.md. Voer hoofdstuk 8 van het plan uit, vanaf stap 2: bepaal_type.py, schema, normaliseer (tegenpartij uit relaties), render.py (alle kenmerken die tot het element leiden op de pagina, ook de standaard ja), tests en kennismodel.py; daarna stap 3 tot en met 5. De besluiten in hoofdstuk 7 gelden met zekerheid logica; vraag ze niet opnieuw. Bewaar vóór de omzetting een kopie van alle beslist.yaml en vergelijk per begrip soort, type, procesniveau en objectniveau; leg elk verschil apart voor zoals voor een architect (hoofdstuk 2). Houd je aan de woordbudgetten in wiki.yaml. Commit per afgerond deel met een prefix en commit-check.
```
