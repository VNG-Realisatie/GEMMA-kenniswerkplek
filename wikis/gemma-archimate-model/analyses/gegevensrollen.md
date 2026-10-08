---
id: gegevensrollen
type: analyse
titel: 'Toegang tot een bedrijfsobject: verantwoordelijkheden en handelingen'
bijgewerkt: '2026-10-01'
bronnen: [2026-bzk-rollen-stelsel-basisregistraties, 2026-rijk-wet-bag-bwbr0023466, 2026-rijk-wet-bgt-bwbr0034026, 2026-rijk-wet-brp-bwbr0033715, 2026-rijk-wet-woz-bwbr0007119, 2026-rijk-handelsregisterwet-2007-bwbr0021777, 2015-rijk-wmo, 2026-rijk-wet-suwi-bwbr0013060, 2026-rijk-wet-op-de-lijkbezorging-wettekst, 1992-tweede-kamer-memorie-van-toelichting-archiefwet-1995, 2026-vng-over-gemma, 2026-vng-gemma-2026-07-01, 2016-eu-avg-geconsolideerd, 2026-rijk-archiefwet-1995-bwbr0007376]
---

# Toegang tot een bedrijfsobject: verantwoordelijkheden en handelingen

De redacteur besloot op 1 oktober 2026 dat een relatie van een rol naar een bedrijfsobject wordt gesplitst: wat de rol met het object ís, wordt een toegangsrelatie met een getypeerde naam; een handeling wordt een toewijzing van de rol aan een proces ([besluiten](gemma-kennismodel.md#besluiten-van-de-redacteur)). De indeling van die namen moest komen uit de wetgeving over basisregistraties. Deze analyse bepaalt twee reeksen namen: de verantwoordelijkheid van een rol voor een object, en de handeling van een functie of proces op een object. Ze beoordeelt ook of de verantwoordelijkheden passen bij andere gegevensbronnen van de gemeente, intern en extern. Ze is de bronanalyse van de bronnen hieronder; regelnummers verwijzen naar hun tekst.

Een algemene "Wet basisregistraties" bestaat niet. Het stelsel van basisregistraties heeft vaste rollen, die per basisregistratie in een eigen wet zijn uitgewerkt. Deze analyse gebruikt de rollenbeschrijving van het stelsel en de wetten van de basisregistraties waarin de gemeente bronhouder of afnemer is.

## Besluiten van de redacteur

| Datum | Besluit |
|---|---|
| 2026-10-01 | De toegang van een functie of proces tot een object krijgt een handeling uit een vaste reeks: registreren, bijwerken, beëindigen, raadplegen, verstrekken. In de kolom Relatie staat `toegang (<handeling>)`; het ArchiMate-toegangstype volgt eruit; het werkwoord uit de bron blijft de naam. |
| 2026-10-01 | De verantwoordelijkheid van een rol voor een object komt uit een vaste reeks van acht: houder, bronhouder, beheerder, verstrekker, afnemer, toezichthouder, betrokkene, partij (alleen bij een afspraak). Notatie: `toegang (<verantwoordelijkheid>)`. |
| 2026-10-01 | Verwerkingsverantwoordelijke (AVG) wordt een toevoeging in de kolom Naam, bijvoorbeeld "houder (verwerkingsverantwoordelijke)", met het wetsartikel in de kolom Bron. |
| 2026-10-01 | De volledige AVG (geconsolideerd) en de geldende Archiefwet worden als bron opgenomen, als grondslag voor verwerkingsverantwoordelijke, betrokkene en zorgdrager. |
| 2026-10-01 | Archiveren krijgt drie eigen handelingen volgens de Archiefwet: bewaren, overbrengen en vernietigen. De reeks handelingen wordt acht; beëindigen gaat alleen over het ophouden te gelden (intrekken, vervallen, opheffen). |

## Bronnen

- **2026-bzk-rollen-stelsel-basisregistraties** (Rollen Stelsel van basisregistraties): [tekst](../../../sources/raw/2026-bzk-rollen-stelsel-basisregistraties.md) · [origineel (html)](../../../sources/raw/2026-bzk-rollen-stelsel-basisregistraties.html) · [online](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/rollen-stelsel-basisregistraties/)
- **2026-rijk-wet-bag-bwbr0023466** (Wet basisregistratie adressen en gebouwen): [tekst](../../../sources/raw/2026-rijk-wet-bag-bwbr0023466.md) · [origineel (html)](../../../sources/raw/2026-rijk-wet-bag-bwbr0023466.html) · [online](https://wetten.overheid.nl/BWBR0023466/2025-02-12)
- **2026-rijk-wet-bgt-bwbr0034026** (Wet basisregistratie grootschalige topografie): [tekst](../../../sources/raw/2026-rijk-wet-bgt-bwbr0034026.md) · [origineel (html)](../../../sources/raw/2026-rijk-wet-bgt-bwbr0034026.html) · [online](https://wetten.overheid.nl/BWBR0034026/2025-02-12)
- **2026-rijk-wet-brp-bwbr0033715** (Wet basisregistratie personen): [tekst](../../../sources/raw/2026-rijk-wet-brp-bwbr0033715.md) · [origineel (html)](../../../sources/raw/2026-rijk-wet-brp-bwbr0033715.html) · [online](https://wetten.overheid.nl/BWBR0033715/2026-10-01)
- **2026-rijk-wet-woz-bwbr0007119** (Wet waardering onroerende zaken): [tekst](../../../sources/raw/2026-rijk-wet-woz-bwbr0007119.md) · [origineel (html)](../../../sources/raw/2026-rijk-wet-woz-bwbr0007119.html) · [online](https://wetten.overheid.nl/BWBR0007119/2026-07-01)
- **2026-rijk-handelsregisterwet-2007-bwbr0021777** (Handelsregisterwet 2007): [tekst](../../../sources/raw/2026-rijk-handelsregisterwet-2007-bwbr0021777.md) · [origineel (html)](../../../sources/raw/2026-rijk-handelsregisterwet-2007-bwbr0021777.html) · [online](https://wetten.overheid.nl/BWBR0021777/2025-07-16)
- **2015-rijk-wmo** (Wet maatschappelijke ondersteuning 2015): [tekst](../../../sources/raw/2015-rijk-wmo.md) · [online](https://wetten.overheid.nl/BWBR0035362/2026-01-01)
- **2026-rijk-wet-suwi-bwbr0013060** (Wet structuur uitvoeringsorganisatie werk en inkomen (Wet SUWI)): [tekst](../../../sources/raw/2026-rijk-wet-suwi-bwbr0013060.md) · [online](https://wetten.overheid.nl/BWBR0013060/2026-01-01)
- **1992-tweede-kamer-memorie-van-toelichting-archiefwet-1995** (Memorie van toelichting Archiefwet 1995): [tekst](../../../sources/raw/1992-tweede-kamer-memorie-van-toelichting-archiefwet-1995.md)
- **2026-rijk-wet-op-de-lijkbezorging-wettekst**: [bronanalyse](../bronanalyses/lijkbezorging/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md)
- **2026-vng-over-gemma**: [bronanalyse](gemma-kennismodel.md)
- **2016-eu-avg-geconsolideerd** (Algemene verordening gegevensbescherming, geconsolideerde tekst): [tekst](../../../sources/raw/2016-eu-avg-geconsolideerd.md) · [origineel (html)](../../../sources/raw/2016-eu-avg-geconsolideerd.html) · [online](http://publications.europa.eu/resource/celex/02016R0679-20160504)
- **2026-rijk-archiefwet-1995-bwbr0007376** (Archiefwet 1995): [tekst](../../../sources/raw/2026-rijk-archiefwet-1995-bwbr0007376.md) · [origineel (html)](../../../sources/raw/2026-rijk-archiefwet-1995-bwbr0007376.html) · [online](https://wetten.overheid.nl/BWBR0007376/2024-06-19)
- **2026-vng-gemma-2026-07-01** (GEMMA-architectuurmodel, modelbron): [tekst](../../../sources/raw/2026-vng-gemma-2026-07-01.md)

## Stelselrollen

Het stelsel kent vijf rollen (rollenpagina, regel 15-23):

| Rol | Omschrijving in de bron | Regel |
|---|---|---|
| Opdrachtgever | "het voor de basisregistratie verantwoordelijke ministerie, dat opdrachtgever is voor de 'verstrekker' (de beheerder van de landelijke voorziening)" | 29 |
| Toezichthouder | "de partij die er verantwoordelijk voor is dat wordt toegezien of de basisregistratie in overeenstemming met eisen, afspraken en wetgeving opereert" | 33 |
| Bronhouder | "verantwoordelijk voor het inwinnen en bijhouden van de authentieke en niet-authentieke gegevens in een basisregistratie en voor het borgen van de kwaliteit van die gegevens (onder meer naar aanleiding van ontvangen terugmeldingen)" | 37 |
| Verstrekker | "verantwoordelijk voor het verstrekken van de gegevens aan afnemers", ook "het faciliteren van het gebruik" | 41 |
| Afnemer | "een overheidsorganisatie of private partij die gegevens afneemt van een basisregistratie voor gebruik in de eigen processen"; voor bestuursorganen is "het afnemen en gebruiken van relevante authentieke gegevens verplicht" | 45 |

De bron zegt er uitdrukkelijk bij: "Een organisatie kan zowel verstrekker, bronhouder als afnemer zijn" (regel 47). Rollen zijn dus verantwoordelijkheden, geen organisaties; dat past bij het besluit dat een actor alleen via een rol aan gedrag en objecten hangt.

## Rollen per wet

De wetten gebruiken niet overal dezelfde woorden. Het werkwoord *houden* wijst de partij aan die de registratie heeft; *bijhouden* is de taak van de bronhouder.

| Rol | Wet BAG | Wet BGT | Wet BRP | Wet WOZ | Handelsregisterwet 2007 |
|---|---|---|---|---|---|
| Houder van de registratie | burgemeester en wethouders "houden" de basisregistratie (art. 2, regel 78) | de Dienst (Kadaster) (art. 2, regel 57) | niet benoemd; zie bronhouder | "door de gemeenten gehouden basisregistratie WOZ" (art. 37aa, regel 1197) | de Kamer van Koophandel (art. 3-4, regel 144, 165) |
| Bronhouder | burgemeester en wethouders, bijhouden op basis van brondocumenten (art. 10, regel 311) | "bestuursorgaan of rechtspersoon aan wie bij deze wet de verantwoordelijkheid voor het bijhouden van geografische gegevens is opgedragen" (art. 1, regel 15), waaronder burgemeester en wethouders (art. 10, regel 323) | het college "is verantwoordelijk voor het bijhouden" voor ingezetenen, de minister voor niet-ingezetenen (art. 1.4, regel 198) | het college levert het waardegegeven (art. 37b, regel 1225) | de Kamer |
| Verstrekker, beheerder van de landelijke voorziening | de Dienst "houdt" en "beheert" de landelijke voorziening (art. 26 en 29, regel 725, 790); verstrekking aan eenieder (art. 32, regel 901) | de Dienst (art. 17, regel 509) | college en minister zijn "verantwoordelijk voor de verstrekking" die zij doen (art. 1.5, regel 218) | de Dienst "houdt en beheert" de landelijke voorziening WOZ (art. 37aa, regel 1197) | de Kamer zorgt voor beschikbaarheid en werking (art. 4, regel 165) |
| Afnemer, verplicht gebruik | een bestuursorgaan "gebruikt dat authentieke gegeven" (art. 35, regel 1002) | art. 23, regel 719 | art. 1.7, regel 269 | afnemer: "bestuursorgaan dat op grond van een wettelijk voorschrift bevoegd is tot gebruik van een waardegegeven" (art. 2, regel 35); gebruik art. 37d, regel 1281 | art. 31, regel 1361 |
| Terugmelding bij gerede twijfel | art. 37, regel 1083 | art. 25, regel 804 | mededeling aan het college van de bijhoudingsgemeente (art. 2.34, regel 1594) | art. 37f, regel 1319 | art. 32, regel 1393 |
| Toezichthouder | de minister (hoofdstuk 7, art. 42, regel 1219) | controle (hoofdstuk 7, regel 914) | hoofdstuk 4, regel 4277 | de Waarderingskamer "houdt toezicht" (art. 4, regel 107) | hoofdstuk 8, regel 1707 |
| Verwerkingsverantwoordelijke (AVG) | burgemeester en wethouders en het bestuur van de Dienst, ieder voor zijn deel (art. 4, regel 137) | — | — | — | de Kamer (art. 3, regel 144) |
| Degene over wie de gegevens gaan | — | — | de ingeschrevene: "degene ten aanzien van wie een persoonslijst in de basisregistratie is opgenomen" (art. 1.1, regel 29) | — | — |

## Verantwoordelijkheden van een rol

Een verantwoordelijkheid zegt wat de rol ten opzichte van het object ís. Wat de rol dóét (bijhouden, leveren, verstrekken, terugmelden, toezicht houden) is een handeling en wordt een toewijzing aan een proces. Het GEMMA-kennismodel noemt vier betekenissen van toegang: "Is verantwoordelijk voor", "is eigenaar van", "is beheerder van", "is raadpleger van" ([Over GEMMA](gemma-kennismodel.md), regel 916).

| Verantwoordelijkheid | Betekenis | ArchiMate-toegang | GEMMA (regel 916) | Herkomst |
|---|---|---|---|---|
| houder | heeft het object of de registratie en is er eindverantwoordelijk voor | lezen-schrijven | is eigenaar van | Wet BAG art. 2; Wet BGT art. 2; Wet WOZ art. 37aa; Wet op de lijkbezorging art. 27 ("De houder van een begraafplaats houdt een register", regel 371) |
| bronhouder | wint de gegevens in, houdt ze bij en borgt hun kwaliteit | schrijven | is verantwoordelijk voor | rollenpagina regel 37; Wet BGT art. 1; Wet BRP art. 1.4 |
| beheerder | zorgt namens de houder voor de werking, beschikbaarheid of het onderhoud van het object of de voorziening | lezen-schrijven | is beheerder van | Wet BAG art. 29 ("beheert de landelijke voorziening"); Wet WOZ art. 37aa |
| verstrekker | stelt de gegevens beschikbaar aan anderen | lezen | — (in GEMMA onder beheerder) | rollenpagina regel 41; Wet BRP art. 1.5 |
| afnemer | gebruikt de gegevens voor de eigen taak, met plicht tot gebruik en terugmelding waar de wet dat bepaalt | lezen | is raadpleger van | rollenpagina regel 45; Wet WOZ art. 2 |
| toezichthouder | ziet toe of het object of de registratie aan eisen en wetgeving voldoet | lezen | — | rollenpagina regel 33; Wet WOZ art. 4 |
| betrokkene | de gegevens gaan over deze partij | lezen | — | AVG art. 4: de geïdentificeerde of identificeerbare natuurlijke persoon over wie persoonsgegevens gaan, "de betrokkene" (regel 135); Wet BRP art. 1.1 (ingeschrevene) |
| partij | is partij bij een afspraak (contract), met rechten en plichten | lezen-schrijven | — | GEMMA-definitie van Afspraak: "Overeenkomst tussen meerdere partijen" (Over GEMMA regel 246) |

Toelichting bij de keuzes:

- **Houder in plaats van eigenaar.** De wetten spreken van *houden*, niet van eigendom. Eigendom van gegevens is juridisch geen gangbaar begrip, en "eigendom" is in deze wiki uitdrukkelijk geen argument (regel Beslistabel beslist). De GEMMA-betekenis "is eigenaar van" valt onder houder.
- **Beheerder en verstrekker apart.** In de Wet BAG en de Wet WOZ houdt en beheert de Dienst de landelijke voorziening, en verstrekt de gemeente ook zelf aan eenieder (Wet BAG art. 32). Beheer (de voorziening werkt) en verstrekking (anderen krijgen de gegevens) zijn dus verschillende verantwoordelijkheden. De verantwoordelijkheid *beheerder* is iets anders dan de rol [Beheerder van de begraafplaats](../bedrijfsarchitectuur/rollen/beheerder-van-de-begraafplaats.md); die rol kan wel de verantwoordelijkheid beheerder hebben.
- **Afnemer in plaats van raadpleger.** Afnemer is de wettelijke term, en draagt de plicht tot gebruik en terugmelding mee. Raadplegen is een handeling.
- **Partij alleen bij een afspraak.** Een rol bij een contract heeft rechten en plichten, geen gegevensverantwoordelijkheid. Zonder deze naam blijft die relatie een associatie.
- **Opdrachtgever hoort niet in deze reeks.** De opdrachtgever stuurt de verstrekker aan en heeft geen eigen toegang tot de gegevens; het is een relatie tussen partijen, en meestal een ministerie buiten het gemeentelijk perspectief (regel Gemeentelijk perspectief).
- **Verwerkingsverantwoordelijke is een aanduiding, geen aparte verantwoordelijkheid.** De wet wijst de verwerkingsverantwoordelijke aan voor de verwerking van persoonsgegevens; dat is meestal de houder (Wet BAG art. 4, Handelsregisterwet art. 3, Wmo art. 5.1.1 lid 7, regel 1844). Vermeld het in de kolom Naam als toevoeging, bijvoorbeeld "houder (verwerkingsverantwoordelijke)". De AVG definieert de verwerkingsverantwoordelijke als degene die "alleen of samen met anderen, het doel van en de middelen voor de verwerking van persoonsgegevens vaststelt", en laat het recht van een lidstaat toe te bepalen "wie de verwerkingsverantwoordelijke is" (AVG art. 4, regel 159). Wie namens die partij verwerkt, is verwerker (regel 165); dat is een toevoeging van dezelfde soort.
- **Eén toegang per rol.** Vervult één actor meerdere rollen (de gemeente is houder, bronhouder én verstrekker van de BAG), dan krijgt elke rol haar eigen toegangsrelatie. Een rol krijgt alleen een pagina als de beslistabel dat zegt; de verantwoordelijkheid zelf is geen element.

## Toepasbaarheid op andere gegevensbronnen

| Soort gegevensbron | Voorbeeld | Bruikbare namen | Beoordeling |
|---|---|---|---|
| Basisregistratie waarvan de gemeente houder of bronhouder is | BAG, BGT, BRP, WOZ | alle | Volledig van toepassing en wettelijk vastgelegd. Verplicht gebruik en terugmelding zijn handelingen van de afnemer. |
| Basisregistratie waarvan de gemeente afnemer is | Handelsregister, BRK, BRV, BRI | afnemer; terugmelding als handeling | Van toepassing. Houder, bronhouder en verstrekker zijn ketenpartners (Kamer van Koophandel, Kadaster, RDW, Belastingdienst; rollenpagina regel 53-117); die krijgen alleen een actorpagina bij een structurele relatie (regel Gemeentelijk perspectief). |
| Wettelijk register buiten het stelsel, gehouden door de gemeente of een partner | register van begraven lijken (Wet op de lijkbezorging art. 27, regel 371) | houder, betrokkene, afnemer | Van toepassing. Houder, bronhouder en verstrekker vallen meestal samen: de wet noemt alleen een houder en maakt het register openbaar (regel 374). Er is geen plicht tot gebruik of terugmelding. |
| Gegevensverwerking in het sociaal domein | Wmo-dossier; Suwinet | houder (verwerkingsverantwoordelijke), afnemer, betrokkene | Van toepassing. De wet wijst de verwerkingsverantwoordelijke aan: het college voor de Wmo (art. 5.1.1 lid 7, regel 1844), het UWV voor de polisadministratie die de gemeente via Suwinet afneemt (Wet SUWI art. 33, regel 862). |
| Interne gemeentelijke administratie zonder eigen wet | zaakregistratie, subsidieadministratie, klantcontacten | houder, bronhouder, afnemer; beheerder bij een gedeelde voorziening | Van toepassing als ordeningsprincipe. De rollen worden toegekend binnen de gemeente (welke rol houdt bij, welke gebruikt), zonder wettelijke plicht tot gebruik of terugmelding. Grondslag van de relatie is dan de bron die de werkwijze beschrijft, niet een wet. |
| Externe administratie van een aanbieder of partner | administratie van een Wmo-aanbieder; uitvaartondernemer | afnemer (gemeente), partij (bij een contract) | Beperkt. De administratie van de partner valt buiten het gemeentelijk perspectief (regel Gemeentelijk perspectief); alleen wat de gemeente ontvangt (verantwoording, opdracht) wordt een object met een gemeentelijke rol als afnemer. De Wmo maakt de aanbieder verwerkingsverantwoordelijke voor zijn eigen verwerking (art. 5.1.2, regel 1880). |
| Archief | archiefbescheiden van de gemeente | houder (zorgdrager), beheerder | Van toepassing. De zorgdrager is "degene die bij of krachtens de wet belast is met de zorg voor de archiefbescheiden" (Archiefwet art. 1, regel 56); voor gemeentelijke organen zijn dat burgemeester en wethouders (art. 30, regel 972). De gemeentelijke archiefbewaarplaats "wordt beheerd door een gemeentearchivaris" (art. 32, regel 1031): de verantwoordelijkheid beheerder. Zorgdrager wordt, net als verwerkingsverantwoordelijke, een toevoeging bij houder. |

**Conclusie.** Vijf namen zijn breed bruikbaar voor elke gegevensbron: houder, bronhouder, beheerder, verstrekker en afnemer. Toezichthouder en betrokkene zijn situatief: toezicht is buiten de basisregistraties zelden apart geregeld, en betrokkene speelt alleen bij gegevens over personen. Partij is nodig voor afspraken. Bij kleine en interne bronnen vallen houder, bronhouder en verstrekker vaak samen bij één rol; modelleer dan alleen de rollen die in de bron te onderscheiden zijn.

## Gevolgen voor de bestaande relaties

Een voorlopige indeling van de 21 relaties van een rol naar een object, volgens het besluit van 1 oktober. Elke wijziging wordt bij de herbeoordeling apart voorgelegd (regel Per geval).

| Rol | Werkwoord nu | Object | Voorstel |
|---|---|---|---|
| [Gemeente](../bedrijfsarchitectuur/rollen/gemeente.md) | houdt in stand | Begraafplaats | toegang: houder |
| [Gemeente](../bedrijfsarchitectuur/rollen/gemeente.md) | heeft het uitsluitend recht tot begraven in | Graf | toegang: houder |
| [Houder van de begraafplaats](../bedrijfsarchitectuur/rollen/houder-van-de-begraafplaats.md) | houdt | Begraafplaats | toegang: houder |
| [Houder van een plaats van bijzetting](../bedrijfsarchitectuur/rollen/houder-van-een-plaats-van-bijzetting.md) | houdt | Plaats van bijzetting | toegang: houder |
| [Houder van het crematorium](../bedrijfsarchitectuur/rollen/houder-van-het-crematorium.md) | houdt | Crematorium | toegang: houder |
| [Beheerder van de begraafplaats](../bedrijfsarchitectuur/rollen/beheerder-van-de-begraafplaats.md) | heeft de dagelijkse leiding van | Begraafplaats | toegang: beheerder |
| [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) | onderhoudt | Grafbedekking | toegang: beheerder |
| [Nabestaande](../bedrijfsarchitectuur/rollen/nabestaande.md) | draagt zorg voor | Urn | toegang: beheerder |
| [Beheerder van de begraafplaats](../bedrijfsarchitectuur/rollen/beheerder-van-de-begraafplaats.md) | ontvangt (verlof tot begraving of crematie) | Vergunning | toegang: afnemer |
| [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) | heeft | Grafrecht | toegang: partij |
| [Indiener](../bedrijfsarchitectuur/rollen/indiener.md) | legt met de gemeente vast | Uitvoeringsovereenkomst | toegang: partij |
| [Ambtenaar van de burgerlijke stand](../bedrijfsarchitectuur/rollen/ambtenaar-van-de-burgerlijke-stand.md) | geeft af (verlof tot begraving of crematie) | Vergunning | handeling: proces dat het verlof verleent (nog geen pagina) |
| [Belanghebbende](../bedrijfsarchitectuur/rollen/belanghebbende.md) | brengt naar voren | Zienswijze | handeling: Uitvoeren inspraakprocedure |
| [Degene die in de lijkbezorging voorziet](../bedrijfsarchitectuur/rollen/degene-die-in-de-lijkbezorging-voorziet.md) | vraagt aan (verlof tot begraving of crematie) | Vergunning | handeling: Uitvoeren lijkbezorging |
| [Gemeentelijke lijkschouwer](../bedrijfsarchitectuur/rollen/gemeentelijke-lijkschouwer.md) | geeft af | Verklaring van overlijden | handeling: Schouwen lijk |
| [Houder van de begraafplaats](../bedrijfsarchitectuur/rollen/houder-van-de-begraafplaats.md) | stelt de identiteit vast van | Lijk | handeling: Uitvoeren lijkbezorging |
| [Houder van de begraafplaats](../bedrijfsarchitectuur/rollen/houder-van-de-begraafplaats.md) | bepaalt wie begraven wordt in | Graf | handeling: Verlenen grafrecht |
| [Houder van de begraafplaats](../bedrijfsarchitectuur/rollen/houder-van-de-begraafplaats.md) | stelt op (verklaring van verwaarlozing) | Beschikking | handeling: proces rond verwaarlozing (nog geen pagina) |
| [Houder van een plaats van bijzetting](../bedrijfsarchitectuur/rollen/houder-van-een-plaats-van-bijzetting.md) | ruimt en houdt register van | Urn | handeling: Ruimen graf; het register is een vorm zonder pagina, de rol is er houder van |
| [Houder van het crematorium](../bedrijfsarchitectuur/rollen/houder-van-het-crematorium.md) | bergt as in | Urn | handeling: Uitvoeren lijkbezorging |
| [Rechthebbende op het graf](../bedrijfsarchitectuur/rollen/rechthebbende-op-het-graf.md) | vraagt aan (vergunning grafbedekking); bepaalt wie begraven wordt in | Vergunning; Graf | handeling: processen nog te bepalen |

Samen: elf toegangsrelaties (vijf houder, drie beheerder, één afnemer, twee partij) en tien handelingen. Voor drie handelingen bestaat het proces nog niet; die worden bij de herbeoordeling kandidaat.

## Toegang van gedrag tot een object

De acht namen hierboven zeggen welke verantwoordelijkheid een rol, en via de rol een actor, voor een object heeft. Een functie of proces heeft geen verantwoordelijkheid maar doet iets met het object. Daarvoor is een tweede, aparte reeks namen nodig: de handeling.

**Wat er nu is.** Het GEMMA-kennismodel laat een bedrijfsfunctie en een bedrijfsproces een bedrijfsobject "benaderen" ([Over GEMMA](gemma-kennismodel.md), regel 919 en 606), zonder verdere indeling. Het GEMMA-model zelf heeft maar acht toegangsrelaties naar een bedrijfsobject, alle in de procesarchitectuur; de enige namen zijn "registreren" (Uitvoeren intake → zaak) en "bijwerken" (vier deelprocessen → zaak) ([GEMMA-model](../../../sources/raw/2026-vng-gemma-2026-07-01.md)). GEMMA noemt wel een "GEMMA bedrijfsfunctie en -objecten model" (Over GEMMA, regel 313), maar legt de samenhang daar via groepering per domein, niet via toegang. In deze wiki heeft geen enkele functie een toegangsrelatie; processen en de dienst hebben er 22, met een werkwoord uit de bron ("graaft op", "ruimt", "legt vast in") en het ArchiMate-toegangstype.

**Besloten: acht handelingen langs de levenscyclus van het object.** Het kenmerk *levenscyclus* vraagt of exemplaren ontstaan, veranderen en eindigen. Die drie momenten, plus gebruiken en doorgeven, geven vijf handelingen die voor elk object werken; de Archiefwet voegt er drie toe voor de archieffase. Het toegangstype van ArchiMate volgt dan uit de handeling.

| Handeling | Betekenis | Toegangstype | Herkomst | Hoort bij de verantwoordelijkheid |
|---|---|---|---|---|
| registreren | het object ontstaat of wordt voor het eerst vastgelegd | schrijven | GEMMA-model (Uitvoeren intake); Wet BRP: inschrijving, "de opneming van een persoonslijst in de basisregistratie" (art. 1.1, regel 55) | bronhouder |
| bijwerken | het object verandert | lezen-schrijven | GEMMA-model (vier deelprocessen); *bijhouden* in Wet BAG art. 10, Wet BGT art. 11, Wet BRP art. 1.4 | bronhouder, beheerder |
| beëindigen | het object houdt op te gelden (intrekken, vervallen, opheffen) | schrijven | kenmerk *levenscyclus*; Wet BRP: "opheffing van het adres" (regel 1292) | bronhouder, houder |
| raadplegen | het gedrag gebruikt het object om zijn taak uit te voeren | lezen | Over GEMMA: "is raadpleger van" (regel 916); verplicht gebruik, Wet BAG art. 35 | afnemer |
| verstrekken | het gedrag geeft het object of de gegevens aan een ander | lezen | Wet BAG art. 32; Wet BRP art. 1.5 | verstrekker |
| bewaren | het object wordt in goede, geordende en toegankelijke staat gebracht en gehouden | lezen-schrijven | Archiefwet art. 3: "in goede, geordende en toegankelijke staat te brengen en te bewaren" (regel 160) | houder (zorgdrager) |
| overbrengen | het object gaat naar een archiefbewaarplaats, waar het beheer overgaat | lezen | Archiefwet art. 12 (regel 354) | houder (zorgdrager); daarna beheerder van de archiefbewaarplaats |
| vernietigen | het object wordt vernietigd omdat het daarvoor in aanmerking komt | schrijven | Archiefwet art. 3 en 5 (regel 162, 209) | houder (zorgdrager) |

Waarom deze vorm:

- **Eén reeks voor functie en proces.** Bij een functie is de handeling het enige wat telt: een functie is een stabiele groepering, en het werkwoord uit één bron is te specifiek. Het resultaat is een functie-objectmatrix, met per functie en object de handelingen; dat is wat GEMMA "bedrijfsfunctie en -objecten model" noemt. Bij een proces blijft het werkwoord uit de bron in de kolom Naam staan, omdat het herleidbaar is en de gangbare taal volgt; de handeling deelt het in.
- **De handeling vervangt het toegangstype in de kolom Relatie.** "toegang (bijwerken)" in plaats van "toegang (lezen-schrijven)": het toegangstype volgt er eenduidig uit, er komt geen kolom bij, en de controle kan de afleiding doen. Voor een rol werkt het net zo: "toegang (bronhouder)".
- **GEMMA-namen waar ze bestaan.** Registreren en bijwerken zijn de namen die GEMMA al gebruikt. Raadplegen sluit aan op "raadpleger" in het kennismodel.
- **De twee reeksen controleren elkaar.** Een rol die bronhouder is van een object, hoort toegewezen te zijn aan gedrag dat dat object registreert of bijwerkt; een afnemer aan gedrag dat het raadpleegt; een verstrekker aan gedrag dat het verstrekt. Een object met *levenscyclus* ja hoort gedrag te hebben dat het registreert én beëindigt.
- **Archiveren.** Bewaren, overbrengen en vernietigen zijn eigen handelingen (besluit 2026-10-01). Ze horen bij de zorgdrager, als toevoeging bij houder, en na overbrenging bij de beheerder van de archiefbewaarplaats.

**Voorlopige indeling van de bestaande relaties.** Elke wijziging wordt bij de herbeoordeling apart voorgelegd (regel Per geval).

| Gedrag | Werkwoord nu | Object | Toegang nu | Handeling |
|---|---|---|---|---|
| Behandelen verzoek om overheidsparticipatie | begint met | Verzoek om overheidsparticipatie | lezen | raadplegen |
| Behandelen verzoek om overheidsparticipatie | legt vast | Uitvoeringsovereenkomst | schrijven | registreren |
| Uitvoeren inspraakprocedure | ontvangt | Zienswijze | lezen | registreren (toegang wordt schrijven: een ontvangen zienswijze wordt vastgelegd) |
| Uitvoeren inwonersparticipatie | legt vooraf vast in | Plan voor inwonersparticipatie | schrijven | registreren |
| Uitvoeren inwonersparticipatie | legt vast in | Eindverslag inwonersparticipatie | schrijven | registreren |
| Schouwen lijk | leidt tot | Verklaring van overlijden | schrijven | registreren |
| Schouwen lijk | schouwt | Lijk | lezen | raadplegen |
| Opgraven lijk | vereist (vergunning tot opgraving) | Vergunning | lezen | raadplegen |
| Opgraven lijk | graaft op | Lijk | lezen-schrijven | bijwerken |
| Ruimen graf | ruimt | Graf | lezen-schrijven | bijwerken |
| Uitvoeren lijkbezorging | vereist (verlof tot begraving of crematie) | Vergunning | lezen | raadplegen |
| Uitvoeren lijkbezorging | bezorgt | Lijk | lezen-schrijven | bijwerken |
| Uitvoeren lijkbezorging | geschiedt in | Graf | lezen-schrijven | bijwerken |
| Uitvoeren lijkbezorging | zet bij of verstrooit de as uit | Urn | lezen-schrijven | bijwerken |
| Uitvoeren lijkbezorging | geschiedt op | Begraafplaats | lezen-schrijven | raadplegen (toegang wordt lezen: de begraafplaats verandert niet) |
| Uitvoeren lijkbezorging | geschiedt in | Crematorium | lezen-schrijven | raadplegen (toegang wordt lezen) |
| Verlenen grafrecht | verleent | Grafrecht | schrijven | registreren |
| Verlenen grafrecht | leidt tot (lijkbezorgingsrechten) | Heffing | schrijven | registreren |
| Verzorgen gemeentebegrafenis | leidt tot | Gemeentebegrafenis | schrijven | registreren |
| Verzorgen gemeentebegrafenis | betreft | Lijk | lezen-schrijven | raadplegen (toegang wordt lezen) |
| Onderhoud van graven (dienst) | onderhoudt | Grafbedekking | lezen-schrijven | bijwerken |
| Onderhoud van graven (dienst) | leidt tot (lijkbezorgingsrechten) | Heffing | schrijven | registreren |

Samen: negen keer registreren, zes keer bijwerken, zeven keer raadplegen; vier relaties krijgen een ander toegangstype. Twee relaties vertrekken uit een dienst; in GEMMA heeft een dienst geen toegang tot een object (de dienst wordt gerealiseerd door een proces), dus die gaan bij de herbeoordeling naar het realiserende proces.

**Wat de indeling laat zien.** Geen enkel proces beëindigt een object, terwijl Grafrecht, Graf en Vergunning een levenscyclus hebben. Het vervallen van het grafrecht is nu alleen een [gebeurtenis](../bedrijfsarchitectuur/gebeurtenissen/verval-van-het-grafrecht.md); het gedrag dat het grafrecht vervallen verklaart en beëindigt, ontbreekt. De handelingen maken zulke gaten in de levenscyclus zichtbaar, en een functie-objectmatrix maakt ze per functie zichtbaar.

## Open vragen

Geen; de vragen van 1 oktober 2026 zijn beantwoord (zie de besluiten bovenaan).
