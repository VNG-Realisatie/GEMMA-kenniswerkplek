# Todo

Het actieve werk van deze wiki; de rest staat in [todo-later.md](todo-later.md). Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Werkwijze lichter maken (vraag redacteur 2026-10-14, eerst, vóór het volgende onderwerp)

Uitgevoerd volgens het goedgekeurde plan [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), stap 1 tot en met 8. Stap 9, de proef, is het onderwerp Participatie (Herbeoordeling hieronder), gemeten volgens het plan (Afwijking bij stap 9).

Bevindingen uit fase 2 van de proef (2026-10-15), voor te leggen bij de samenvatting van de proef:

- **Werkpakket in fase B zonder passages en kandidaten.** `tools/werkpakket.py` geeft ze standaard alleen voor begrippen zonder beoordeling; in fase B hebben alle begrippen er een, dus stap 7 van skill gemma-archimate-model-update vraagt `--alles`.
- **Geen werkpakket voor het cluster zonder kernobject.** Het hele werkpakket met `--alles` was 21.243 woorden; een optie om op id's te filteren (bijvoorbeeld `--ids`) maakt het klein.
- **`tools/bronduiding.py citaat` leest geen bron met varianten en artikelnummers tussen haken** (de VNG-modelverordening Participatie): de citaten zijn overgetypt en met `controleer` nagekeken.
- **Beoordelingsagenten lezen precedenten buiten hun opdracht** (bestaande beoordelingen en code, 3.500 à 5.000 woorden) en hebben 44 à 65 beurten; bij een klein onderwerp is fase B in de hoofdsessie waarschijnlijk goedkoper (meting in `handoff.md`).

## Zekerheid van besluiten (besluit redacteur 2026-10-15, direct na de afronding van Participatie, commit `rules:`)

Elk besluit krijgt een veld `zekerheid`: `kennis` (domeinkennis van de redacteur of een bron: geldt als regel, telt als precedent), `logica` (afgeleid uit regels en samenhang: uitgangspunt, opnieuw voorleggen als nieuwe informatie de redenering raakt, telt alleen ondersteunend) of `indruk` (voorlopig: in fase 3 van hetzelfde onderwerp altijd opnieuw aanbieden, telt niet als precedent). De AI stelt het niveau voor, de redacteur bevestigt; `kennis` kiest de AI nooit zelf. Een heroverweging is een nieuw besluit; het oude krijgt `stand: herzien` of `bevestigd`, en een bevestiging die de zekerheid verhoogt wordt wel vastgelegd. Bestaande besluiten zonder veld tellen als `logica`. Het werkpakket toont het niveau; een beoordelingsagent volgt alleen `kennis` als regel en zet een afwijking van `indruk` of `logica` in `vragen:`. In fase 3 krijgt de tabel een kolom Eerder besluit (zekerheid). Raakt: regel Navragen in AGENTS.md, `references/besluiten.md` en de precedentregel van skill gemma-archimate-model-beoordelen, `tools/beoordeling.py` (`--zekerheid`), `tools/werkpakket.py` en het schema; eerst het woordbudget controleren. Tot dan staat de zekerheid in de besluittekst (Participatie: K4 heroverwogen).

## ArchiMate-indeling als eerste selectie in de beslistabel (vraag redacteur 2026-10-15, na de lichtere werkwijze en vóór de Applicatielaag)

De AI kiest eerst het vak in de ArchiMate-matrix: de laag (bedrijf, applicatie, technologie, motivatie, …) en het aspect (actieve structuur, gedrag, passieve structuur), met intern of extern. De bestaande kenmerken worden de controle op die keuze. Nu herkent de aard vooral de actieve structuur en het gedrag; een passief ding is "geen van de acht". Product en Locatie passen niet in één aspect; bepaal waar ze komen. Winst: fase A wordt een paar keuzes; de redacteur beoordeelt in de taal van ArchiMate; de applicatielaag wordt een laag in dezelfde matrix. Het raakt `tools/bepaal_type.py`, het schema en alle beoordelingen (omzetting met een script, de uitkomsten moeten gelijk blijven). Een eigen klus op denkniveau hoog.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, als proef van de lichtere werkwijze (stap 9 van het plan), met de participatie-modelverordening als mogelijk beleidskader.
- **Gemeentewet als grondslag voor de andere onderwerpen** (besluit 2026-10-15 bij Gemeentewet): de relaties *is grondslag voor* naar de elementen van Lijkbezorging (art. 147, 149, 229), Heffingen en betalingen en Besluitvorming (art. 150 bij Beleidsnota), na de afronding van Participatie.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).
