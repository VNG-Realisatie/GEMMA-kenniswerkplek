# Todo

Het actieve werk van deze wiki; de rest staat in [todo-later.md](todo-later.md). Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Bevindingen uit de proef van de lichtere werkwijze (plan 2026-10-15, stap 9 afgerond)

De uitkomst staat in [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md), Uitkomst stap 9. Open uit fase 2:

- **Werkpakket in fase B zonder passages en kandidaten.** `tools/werkpakket.py` geeft ze standaard alleen voor begrippen zonder beoordeling; in fase B hebben alle begrippen er een, dus stap 7 van skill gemma-archimate-model-update vraagt `--alles`.
- **Geen werkpakket voor het cluster zonder kernobject.** Het hele werkpakket met `--alles` was 21.243 woorden; een optie om op id's te filteren (bijvoorbeeld `--ids`) maakt het klein.
- **`tools/bronduiding.py citaat` leest geen bron met varianten en artikelnummers tussen haken** (de VNG-modelverordening Participatie): de citaten zijn overgetypt en met `controleer` nagekeken.
- **Beoordelingsagenten lezen precedenten buiten hun opdracht** (bestaande beoordelingen en code, 3.500 à 5.000 woorden). Sinds het opschonen van de besluiten staan brede besluiten als regel in het kennismodel; meet bij het volgende onderwerp met agenten of het lezen buiten de opdracht afneemt.

## ArchiMate-indeling, lichtere kenmerken, data-object en capability (plan 2026-10-15)

Uitvoering volgens [plannen/2026-10-15-archimate-indeling.md](plannen/2026-10-15-archimate-indeling.md): deel 1 (matrix en lichtere kenmerken), deel 2 (data-object als element), deel 3 (Capability, eerst samen bepalen). Deel 1 en 2 zijn omgezet (Uitkomst stap 3–7 en 8–11). Deel 3 is uitgevoerd: de besluiten over Capability (Uitkomst stap 12 en 13), het bouwen en de eerste drie capabilities (Uitkomst stap 14).

- **GEMMA-functies onder *Ontvangst*** (Identiteitvaststelling, Autorisatievaststelling, Voorwaardentoetsing, Vormacceptatie, Zelfredzaamheidbepaling): alleen in het domein Fysieke leefomgeving, maar domeinoverstijgend en lijkend op vermogens; een kandidaat voor een terugmelding aan het GEMMA-team (kalibratie stap 12).
- **Rechtsbescherming bieden**: een capability zodra besluitvorming een realiserende functie heeft (GEMMA: Klachten afhandeling).

- **De beslistabel herzien** volgens [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md): stap 2 tot en met 7 zijn uitgevoerd (de code, het kennismodel, de regels en skills, de omzetting van de 484 beoordelingen, het AKKOORD voor 284 elementen en de potentiële relaties, met hun AKKOORD). Open: (1) de **Model-beheersverordening begraafplaatsen** is geen element zolang niet is vastgesteld of de openbare versie van 2010 actueel is (*in werking*; nieuwere versies staan in de Kennisbank decentrale regelgeving van SDU); zodra dat zo is, wordt zij weer een element met haar acht relaties; (2) **ArchiMate** is bron via de officiële referentiekaarten van The Open Group (definities, zonder de uitleg van de specificatie); de volledige specificatie is alleen na inloggen op te halen, dus lever haar aan als de uitleg nodig is; (3) NORA heeft geen definitie van Kanaal of Dienst (alleen de pagina's Kanalen en Dienstverlening), dus de herkomst *NORA (Kanalen)* en *(Dienstverlening)* onderbouwt het idee, niet de definitie.

- **Potentiële relaties, wat open blijft** (plan 2026-10-18, stap 7 is uitgevoerd: de 82 relatiekenmerken van elementen hebben hun tegenpartij in `naar`). (1) **Zes kenmerken `ja` zonder `naar` bij begrippen die geen element zijn**: wordt_bewerkt bij Grafbedekking, Nationaliteit en Plaats van bijzetting (onderdeel van een ander begrip: loopt de relatie via het geheel?), vervult_een_rol bij de IND en de minister van BZK (Rijk is de actor), en toegewezen partij bij Benoemen gemeentelijke lijkschouwer (geen element: toetskenmerk ontbreekt voor Bedrijfsproces). (2) **Stand-ins als tegenpartij**: ca. 50 gebeurtenissen (Aanvraag … ingediend, Verzoek om … ingediend), de bedrijfsfuncties *Producten- en dienstenrealisatie publieksdiensten* en *Exploitatie fysieke leefomgeving* (GEMMA, geen wiki-element) en het bedrijfsobject Verklaring van overlijden hebben nog geen beoordeling; maak er een bij het onderwerp waar ze thuishoren. (3) **Acht levensloopprocessen** noemen rollen die aan hun deelprocessen zijn toegewezen (besluit 2026-10-18: het kenmerk verwijst naar de deelprocessen); de signalering geeft per kenmerk een waarschuwing 'potentiële relatie'. (4) Overweeg een signaal voor een relatiekenmerk `ja` zonder `naar` (eerst voorleggen: een rules-wijziging). (5) **Grafrecht** is een afspraak: een bedrijfsfunctie heeft er in het kennismodel geen toegang toe, dus Exploiteren van begraafplaatsen noemt alleen Graf en Begraafplaats.

- **GGM-match voor rollen, actoren en gebeurtenissen.** Op naam zijn er GGM-entiteiten voor Belanghebbende, Aangever (RSGBPlus), Indiener, Rechthebbende (Archief), Gemeente en de BRP-gebeurtenissen (GeboorteIngeschrevenPersoon, OverlijdenIngeschrevenPersoon, SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap, OntbindingHuwelijk/geregistreerdPartnerschap, MigratieIngeschrevenNatuurlijkPersoon). Kies de match op betekenis bij de herbeoordeling van het onderwerp; een match geeft vanzelf een data-object.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, als proef van de lichtere werkwijze (stap 9 van het plan), met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).
