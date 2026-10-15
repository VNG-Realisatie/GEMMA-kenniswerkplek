# Todo

Het actieve werk van deze wiki; de rest staat in [todo-later.md](todo-later.md). Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Bevindingen uit de proef van de lichtere werkwijze (plan 2026-10-15, stap 9 afgerond)

De uitkomst staat in [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), Uitkomst stap 9. Open uit fase 2:

- **Werkpakket in fase B zonder passages en kandidaten.** `tools/werkpakket.py` geeft ze standaard alleen voor begrippen zonder beoordeling; in fase B hebben alle begrippen er een, dus stap 7 van skill gemma-archimate-model-update vraagt `--alles`.
- **Geen werkpakket voor het cluster zonder kernobject.** Het hele werkpakket met `--alles` was 21.243 woorden; een optie om op id's te filteren (bijvoorbeeld `--ids`) maakt het klein.
- **`tools/bronduiding.py citaat` leest geen bron met varianten en artikelnummers tussen haken** (de VNG-modelverordening Participatie): de citaten zijn overgetypt en met `controleer` nagekeken.
- **Beoordelingsagenten lezen precedenten buiten hun opdracht** (bestaande beoordelingen en code, 3.500 à 5.000 woorden). Sinds het opschonen van de besluiten staan brede besluiten als regel in het kennismodel; meet bij het volgende onderwerp met agenten of het lezen buiten de opdracht afneemt.

## ArchiMate-indeling, lichtere kenmerken, data-object en capability (plan 2026-10-15)

Uitvoering volgens [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md): deel 1 (matrix en lichtere kenmerken), deel 2 (data-object als element), deel 3 (Capability, eerst samen bepalen). Stap 1 en 2 zijn gedaan (O2 en O3: ja); volgende stap: stap 3–7, de omzetting.

- **`beslist` uit de beoordeling halen** (uit de analyse van het plan): het blok is 23.000 woorden en wordt meegelezen bij elk precedent; het kan naar een gegenereerd bestand per onderwerp.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, als proef van de lichtere werkwijze (stap 9 van het plan), met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).
