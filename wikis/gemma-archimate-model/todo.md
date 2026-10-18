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

- **De beslistabel herzien** volgens [plannen/2026-10-18-beslistabel.md](plannen/2026-10-18-beslistabel.md): stap 2 tot en met 5 zijn uitgevoerd (de code, het kennismodel, de regels en skills, de omzetting van de 484 beoordelingen); stap 6 staat open: `tools/beslissen.py` is schoon, nu één nieuw AKKOORD voor alle elementen (ze staan weer op review). Open: (1) de **Model-beheersverordening begraafplaatsen** is geen element zolang niet is vastgesteld of de openbare versie van 2010 actueel is (*in werking*; nieuwere versies staan in de Kennisbank decentrale regelgeving van SDU); zodra dat zo is, wordt zij weer een element met haar acht relaties; (2) **ArchiMate** staat als herkomst in het kennismodel zonder bron, want de specificatie van The Open Group is alleen na inloggen op te halen: lever de tekst aan (hoofdstuk 8 Business Layer volstaat), dan volgen bron, bronduiding en link; (3) NORA heeft geen definitie van Kanaal of Dienst (alleen de pagina's Kanalen en Dienstverlening), dus de herkomst *NORA (Kanalen)* en *(Dienstverlening)* onderbouwt het idee, niet de definitie.

- **Potentiële relaties vastleggen**, deel 2, na het AKKOORD van de nieuwe beslistabel: besluitvorming en participatie zijn gedaan. Nog 88 relatiekenmerken `ja` zonder `naar` (de omzetting vulde er 137 uit bestaande relaties en liet de kenmerken van begrippen zonder pagina vervallen; 7 daarvan, *in functie-indeling*, steunen op een GEMMA-relatie): lijkbezorging 33 en burgerzaken 55; vooral *aanleiding* (54) en *toegewezen partij* (12). Het kernrelatie-signaal controleert alleen kernrelaties van een type, niet *aanleiding*, dus een deel mist ook de relatie. Bestaat het element, dan het id in `naar` (ontbreekt de relatie, dan die toevoegen met `tools/beoordeling.py relatie`); anders naam en type met bron (gebeurtenis voor een aanleiding, bedrijfsproces voor een levensloopproces). Leg elk twijfelgeval apart voor. Overweeg een signaal voor een relatiekenmerk `ja` zonder `naar` of relatie (eerst voorleggen: een rules-wijziging).

- **GGM-match voor rollen, actoren en gebeurtenissen.** Op naam zijn er GGM-entiteiten voor Belanghebbende, Aangever (RSGBPlus), Indiener, Rechthebbende (Archief), Gemeente en de BRP-gebeurtenissen (GeboorteIngeschrevenPersoon, OverlijdenIngeschrevenPersoon, SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap, OntbindingHuwelijk/geregistreerdPartnerschap, MigratieIngeschrevenNatuurlijkPersoon). Kies de match op betekenis bij de herbeoordeling van het onderwerp; een match geeft vanzelf een data-object.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, als proef van de lichtere werkwijze (stap 9 van het plan), met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).
