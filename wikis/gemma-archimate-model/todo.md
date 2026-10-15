# Todo

Het actieve werk van deze wiki; de rest staat in [todo-later.md](todo-later.md). Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Werkwijze lichter maken (vraag redacteur 2026-10-14, eerst, vóór het volgende onderwerp)

Uitvoeren volgens het goedgekeurde plan [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), sectie Uitvoering, stap 1 tot en met 9; elke stap een eigen commit na akkoord. Daarna de punten Levensloopproces realiseert altijd een dienst en Verzorgen gemeentebegrafenis als proef (stap 9).

## ArchiMate-indeling als eerste selectie in de beslistabel (vraag redacteur 2026-10-15, na de lichtere werkwijze en vóór de Applicatielaag)

De AI kiest eerst het vak in de ArchiMate-matrix: de laag (bedrijf, applicatie, technologie, motivatie, …) en het aspect (actieve structuur, gedrag, passieve structuur), met intern of extern. De bestaande kenmerken worden de controle op die keuze. Nu herkent de aard vooral de actieve structuur en het gedrag; een passief ding is "geen van de acht". Product en Locatie passen niet in één aspect; bepaal waar ze komen. Winst: fase A wordt een paar keuzes; de redacteur beoordeelt in de taal van ArchiMate; de applicatielaag wordt een laag in dezelfde matrix. Het raakt `tools/bepaal_type.py`, het schema en alle beoordelingen (omzetting met een script, de uitkomsten moeten gelijk blijven). Een eigen klus op denkniveau hoog.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).

## Proef (stap 9 van het plan)

- **Levensloopproces realiseert altijd een dienst** (besluit redacteur 2026-10-14, nog niet uitgevoerd): elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst, zelf of via zijn bedrijfsprocessen; niet elk bedrijfsproces (Schouwen stoffelijk overschot, Sluiten begraafplaats, Vervallen verklaren grafrecht en andere ambtshalve processen realiseren er geen). Ontbreekt de dienst in de UPL: een procesarchitectuur-terugmelding én een dienst in de wiki waarin expliciet staat dat ze in de UPL ontbreekt. Afspraak in het kennismodel (Bedrijfsproces, Dienst), signaal in `tools/signalen.py`, test. Nu zonder dienst: Verzorgen gemeentebegrafenis (geen UPL-dienst voor Wlb art. 20–22).
- **Verzorgen gemeentebegrafenis: levensloopproces of bedrijfsproces** (vraag redacteur 2026-10-14): het is een levensloopproces zonder bedrijfsprocessen of gebeurtenissen eronder, omdat een gemeentebegrafenis één keer wordt doorlopen (melding art. 20, zorg art. 21, kostenverhaal art. 22); eigenlijk ligt de levensloop op het niveau van de keten (Bezorgen stoffelijk overschot). Opties: (1) levensloop en proces vallen samen, de stappen in `deelprocessen` (kleinste wijziging, advies); (2) bedrijfsproces onder Toestaan lijkbezorging, maar dat is bewust de gemeente als overheid (besluit 2026-10-07) en Gemeentebegrafenis (GGM en GEMMA sterk) verliest dan objectniveau kernobject (beslistabel regel 38); (3) levensloopproces met kernobject Stoffelijk overschot als deel van de gemeente als verzorger in de keten, met hetzelfde gevolg voor Gemeentebegrafenis. Daarnaast de dienst Gemeentebegrafenis met terugmelding (punt hierboven). Stappen uit de praktijk (nabestaanden zoeken, uitvaartondernemer inschakelen) alleen met een bron. Na het lichter maken van de werkwijze.
