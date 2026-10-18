# Handoff

Overdracht naar de volgende Sessie (2026-10-18). Wordt bij elke overdracht overschreven. De regels staan in AGENTS.md en de skills; dit bestand verwijst naar de commits, het plan en de todo.

## Stand van zaken

- Plan [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md), stap 2 tot en met 5 zijn klaar en gecommit (hoofdstuk 10 beschrijft de uitkomst): de code en tests (`rules:`), de omzetting van de 484 beoordelingen (`update:`), de bronnen NORA met herkomstlinks (`add:`) en de regels en skills (`rules:`). `tools/beslissen.py`, de tests (262), `render.py --check`, `archimate_export.py --check` en `llmwiki lint` zijn schoon.
- Soort, type, procesniveau en objectniveau zijn voor 482 van 484 begrippen gelijk gebleven. De twee verschillen zijn voorgelegd en besloten: Eindverslag inwonersparticipatie is geen element (de toegang van Betrekken inwoners bij beleid is vervallen); Model-beheersverordening begraafplaatsen is geen element tot de actuele versie is gecontroleerd. *Toegewezen partij* is geen toetskenmerk meer van Bedrijfsfunctie.
- Alle goedgekeurde elementen staan op review: de inhoud is veranderd, dus er is één nieuw AKKOORD nodig.
- Open: de volledige ArchiMate-specificatie ontbreekt (alleen na inloggen; de referentiekaarten van The Open Group zijn wel bron), de beheersverordening, en de 88 relatiekenmerken zonder tegenpartij in lijkbezorging en burgerzaken (zie [todo.md](todo.md)). `tools/omzetten_beslistabel.py` is eenmalig; verwijder het na het AKKOORD (`chore:`).

## Volgende klus

Stap 6: de redacteur bekijkt de pagina's (`uv run python -m llmwiki promote plan`, de samenvatting in de chat), typt AKKOORD, daarna `promote apply --akkoord-woord AKKOORD` en `uv run python tools/afronden.py --bericht "<prefix>: …"`. Daarna stap 7: verder met lijkbezorging, deel 2 van de todo (potentiële relaties vastleggen).

## Modeladvies

Het AKKOORD en `afronden.py` zijn denkniveau laag; een sneller model volstaat en de lopende context is nog te gebruiken. De relaties vastleggen (stap 7) is denkniveau middel, met alleen echte twijfel voorleggen: dat kan met hetzelfde model. Deze Sessie is door de omzetting en de vergelijking vol; begin voor stap 7 een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md, plannen/2026-10-18-beslistabel.md (hoofdstuk 10) en wikis/gemma-archimate-model/todo.md. De nieuwe beslistabel staat (commits 2165df61, 04384129 en daarna); alle elementen staan op review. Vraag eerst het AKKOORD: toon `uv run python -m llmwiki promote plan` in de chat en wacht op het woord AKKOORD van de redacteur. Ga daarna met stap 7 verder: de 88 relatiekenmerken `ja` zonder `naar` in lijkbezorging en burgerzaken (todo "Potentiële relaties vastleggen"). Leg alleen echte twijfel voor, zoals voor een architect (references/besluiten.md), en commit per afgerond deel met een prefix en commit-check.
```
