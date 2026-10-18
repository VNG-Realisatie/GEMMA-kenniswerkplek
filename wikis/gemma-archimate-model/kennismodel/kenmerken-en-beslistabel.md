---
id: kenmerken-en-beslistabel
type: kennismodel
titel: Kenmerken en beslistabel
gegenereerd: tools/kennismodel.py
---

# Kenmerken en beslistabel

De beslistabel heeft vier fasen, elk met één vraag: *Afbakenen* (wordt dit begrip een eigen element?), *Typeren* (welk type en niveau?), *Onderbouwen* (voldoet het element aan zijn type?) en *Indelen* (waar hoort het in de indelingen?). De AI kiest de keuzekenmerken en beantwoordt de relatiekenmerken; het script past de vaste regels toe, toetst de toetskenmerken en leidt het type en de indeling af. De uitkomst is het type, of de reden waarom het begrip geen eigen pagina krijgt. Een type wordt nooit direct gekozen. Per elementtype staat in zijn modelleerafspraken welke toetskenmerken het type heeft; een relatiekenmerk daaronder heet kernrelatie.

## Stap 0: welk begrip?

Vóór de kenmerken: bepaal welk begrip bedoeld is. Synoniemen en homoniemen zijn geen kenmerken van een begrip, maar verhoudingen tussen een woord en een begrip.

| Veld | Vraag | Uitkomst |
|---|---|---|
| `synoniem_van` | Is dit een ander woord voor een begrip dat al een element is, of in deze run wordt beoordeeld? Noem dat element en de context van het woord. | synoniem: geen pagina; het woord naar de synoniemen van het element |
| `homoniem_van` | Bestaat dezelfde naam al voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron? Noem dat begrip en waar het voorkomt. | door naar de kenmerken; naamkeuze voorleggen |

## De ArchiMate-matrix

Typeren kiest eerst het vak: de laag, het aspect en intern of extern, zoals in ArchiMate. Het vak bepaalt welke hoofdkenmerken en soorten gedrag er zijn, en welke vragen volgen. Motivatie kent geen aspecten.

| Laag | Actief intern | Actief extern | Gedrag intern | Gedrag extern | Passief | Samengesteld |
|---|---|---|---|---|---|---|
| bedrijf | Actor, Rol, Bedrijfssamenwerking | Kanaal | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie | Dienst | Bedrijfsobject, Afspraak, Representatie (geen pagina) | Product |
| applicatie | zonder element | zonder element | zonder element | zonder element | Data-object (afgeleid uit de GGM-match) | — |
| technologie | zonder element: komt misschien nog | | | | | |
| strategie | Resource: zonder element | | Capability; Waardestroom en Handelwijze: zonder element | | | |
| motivatie | Beleidskader (element); Kwaliteitsdoel (matchdoel); de andere typen buiten dit model | | | | | |
| overig | | | | | | Locatie (geen pagina), Groepering (indeling) |

| Vak (`vak`) | Typen | Hoofdkenmerk (`hoofdkenmerk`) | Soort gedrag (`soort_gedrag`) | Typeren daarna |
|---|---|---|---|---|
| `bedrijf/actief-intern` | Actor, Rol, Bedrijfssamenwerking | *handelende partij*, *hoedanigheid*, *samenwerkingsverband* (kiezen) | — | *eigen rechtspersoon*, *los van verantwoordelijkheid*, *soort partij* |
| `bedrijf/actief-extern` | Kanaal | *toegangspunt* (volgt uit het vak) | — | — |
| `bedrijf/gedrag-intern` | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie | *gedrag* (volgt uit het vak) | *per keer doorlopen*, *gegroepeerd gedrag*, *toestandsverandering*, *gezamenlijk gedrag* (kiezen) | — |
| `bedrijf/gedrag-extern` | Dienst | *gedrag* (volgt uit het vak) | *aangeboden gedrag* (volgt uit het vak) | — |
| `bedrijf/passief` | Bedrijfsobject, Afspraak, Representatie (geen pagina) | *object*, *afspraak*, *representatie* (kiezen) | — | — |
| `bedrijf/samengesteld` | Product | *aanbod als geheel* (volgt uit het vak) | — | — |
| `strategie/gedrag` | Capability | *vermogen* (volgt uit het vak) | — | — |
| `motivatie` | Beleidskader | *regeling als geheel* (volgt uit het vak) | — | *landelijk* |
| `overig/samengesteld` | Locatie (geen pagina) | *plaats* (volgt uit het vak) | — | — |

Past het hoofdkenmerk of de soort gedrag niet bij het vak, dan is er een conflict (regel 10).

## Keuzekenmerken

Een keuzekenmerk heeft een waardenlijst: precies één waarde, met één onderbouwing en bron (in `kenmerken`; het vak, het hoofdkenmerk en de soort gedrag zijn keuzevelden bovenaan). De waarde *zelfstandig* is het standaardantwoord.

**afhankelijkheid** (stap 2). Is het begrip zelfstandig, of hangt het af van één ander begrip? Noem bij een afwijking dat begrip in `genoemd_begrip`. Herkomst: GEMMA (eigen bestaan; negatieve toets: eigenschap, status, classificatie; procesarchitectuur: processtap, handeling; zelfstandig ding waar beleid op gemaakt wordt); wiki (abstractieniveau).

| Waarde | Criterium |
|---|---|
| `zelfstandig` | eigen betekenis, eigen gegevens, regels of werkwijze (standaard) |
| `eigenschap` | alleen een eigenschap, status, waarde, classificatie of indeling van het genoemde begrip, ook een doelgroep (bouwjaar van Pand; minima als indeling van Inwoner) |
| `onderdeel` | onderdeel, deelstap of handeling van het genoemde begrip, zonder eigen bedrijfsproces, dat ermee ontstaat en eindigt (grafbedekking van Graf; ondertekening van een besluit) |
| `deelproces` | deel van het genoemde bedrijfsproces, niet klant tot klant: geen eigen aanleiding van buiten en geen eigen resultaat voor de klant (toetsen indieningsvereisten in behandelen aanvraag) |
| `variant` | specialisatie van het genoemde begrip, van hetzelfde type, zonder eigen gegevens, regels of werkwijze (vergunning tot opgraving naast Vergunning) |
| `invoer_van_een_ander` | maakt en beheert een andere partij, de gemeente ontvangt of raadpleegt het alleen (verklaring van overlijden van de arts of lijkschouwer) |

**procesniveau** (stap 3). Welk niveau heeft het proces in de procesindeling naar kernobject? Noem bij een levensloopproces of bedrijfsproces het kernobject in `kernobject`. Herkomst: GEMMA Online, Proceshiërarchie (bedrijfsproces klant-tot-klant, PH 81; deelproces, PH 83; cluster van bedrijfsprocessen over één thema, PH 91); wiki (levensloopproces; één per partij binnen een ketensamenwerking).

| Waarde | Criterium |
|---|---|
| `levensloopproces` | het gedrag over de hele levensloop van één exemplaar van het kernobject, van ontstaan tot einde, of binnen een ketensamenwerking het deel dat één partij uitvoert (Beheren grafrechten) |
| `bedrijfsproces` | klant tot klant: begint bij een aanleiding van buiten het proces, loopt door tot het resultaat voor die klant, en doet een mutatie in de levensloop van het kernobject (Verlenen grafrecht) |
| `cluster naar soort werk` | een groepering van bedrijfsprocessen van één soort werk, niet per geval doorlopen; `gemma_generiek` is verplicht (Behandelen vergunningaanvragen lijkbezorging) |

**interactievorm** (stap 3). Hoe werken de partijen samen in de bedrijfsinteractie? Herkomst: GEMMA Online, Proceshiërarchie (ketensamenwerking als bedrijfsinteractie); ArchiMate (Business Interaction).

| Waarde | Criterium |
|---|---|
| `estafette` | ketensamenwerking: elke partij is verantwoordelijk voor haar eigen deel (Bezorgen stoffelijk overschot) |
| `orkestratie` | één partij is verantwoordelijk voor het geheel; de gemeente levert een dienst aan derden (Beheren Nederlanderschap) |

## Kenmerken

Beantwoord de vragen op het pad, in vier fasen (`tools/bepaal_type.py vragen <id>`). Afbakenen: alleen een afwijking in de scope (stap 1) en de *afhankelijkheid* (stap 2), met een stop als het begrip afvalt. Typeren: de keuzevelden (vak, hoofdkenmerk, soort gedrag; zie de matrix), de kenmerken van het hoofdkenmerk en de keuzekenmerken *procesniveau* en *interactievorm*. Onderbouwen: de toetskenmerken van het type. Indelen: een script, met *generiek* als afwijking. Een kenmerk buiten het pad laat je weg: het script leidt het standaardantwoord af (*standaard ja* staat erbij, anders nee). Een relatiekenmerk (†) met ja noemt zijn tegenpartij in `naar`: het id van het element (het script vult het als de relatie bestaat, en dan steunt het kenmerk op haar bron); bestaat het element (nog) niet, dan naam en type, met een onderbouwing en bron. Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; zonder zo'n verwijzing is het antwoord nee.

**Scope.** Stap 1, alleen een afwijking: zonder antwoord is de scope doorlopen (*herkenbaar*, *gemeentelijk* en *betekenis in onderwerp* ja, *buiten dit model* nee), en steunt zij op de bronnen van de beoordeling. Het begrip valt af bij de eerste die afwijkt.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 1 | *herkenbaar* (standaard ja) | Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning) | technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel) | ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts) |
| 2 | *gemeentelijk* (standaard ja) | Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD; behandelende arts via de overlegplicht met de lijkschouwer) | alleen context (gedeputeerde staten als beroepsinstantie), of de interne zaak van een ketenpartner (de medische behandeling door de arts) | GEMMA (gemeentelijk perspectief) |
| 3 | *buiten dit model* | Is het een doel, waarde, drijfveer, principe, losse norm of eis, opgave of thema, en geen beleidskader? Noem het ArchiMate-type. | armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel) | bijstandsuitkering; Wet op de lijkbezorging (beleidskader) | ArchiMate (motivatie-, strategie- en overige lagen) |
| 4 | *betekenis in onderwerp* (standaard ja) | Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? Noem bij nee het onderwerp waar het thuishoort. | Graf in lijkbezorging | akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand) | GEMMA (betekenis binnen het onderwerp) |

**Hoofdkenmerk.** Stap 3, het keuzeveld `hoofdkenmerk`: één waarde uit het vak; valt weg als het vak er maar één heeft.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 5 | *gedrag* | Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | aanvraag behandelen; verhuizing | aanvraag | ArchiMate (gedragselement) |
| 6 | *handelende partij* | Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | college van B&W; inwoner | aanvrager | GEMMA (definitie Actor) |
| 7 | *hoedanigheid* | Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | aanvrager; houder van de begraafplaats | gemeenteraad | ArchiMate (definitie Rol) |
| 8 | *samenwerkingsverband* | Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? | Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten) | GGD-arts | ArchiMate (definitie Bedrijfssamenwerking) |
| 9 | *toegangspunt* | Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? | publieksbalie; gemeentelijke website | klantcontact | NORA (definitie Kanaal) |
| 10 | *plaats* | Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? | stadskantoor als vestigingsplaats | wijk (indeling) | ArchiMate (Location) |
| 11 | *aanbod als geheel* | Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? | bewonersparkeervergunning zoals de productencatalogus haar aanbiedt | parkeren; één UPL-item als zodanig (een dienst) | GEMMA (definitie Product) |
| 12 | *regeling als geheel* | Is het een concreet benoemde wet, AMvB, ministeriële regeling of verordening als geheel, en niet één artikel, een soort regeling of een richtlijn? | Wet op de lijkbezorging; modelverordening participatie | 'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm); Circulaire adresonderzoek BRP (richtlijn, blijft bron) | GEMMA (definitie Beleidskader) |
| 13 | *vermogen* | Beschrijft het wat de gemeente moet kunnen om haar opgaven waar te maken, waarin zij investeert en wat met haar strategische opgaven verandert, los van hoe, door wie, in welke volgorde en met welk kanaal of systeem? | Identiteit vaststellen | Aanvraag controleren op volledigheid (te concreet: een processtap) | GEMMA (definitie Capability); wiki (kader Capability, functie en proces) |
| 14 | *object* | Is het een ding waarover de gemeente gegevens vastlegt of dat zij verstrekt, en geen afspraak of waarneembare vorm van een ander begrip? | Graf; Aanvraag; Vergunning | aanslagbiljet (de vorm van Aanslag); subsidieovereenkomst (een afspraak) | ArchiMate (Business Object) |
| 15 | *afspraak* | Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? | subsidieovereenkomst; uitvoeringsovereenkomst | subsidiebeschikking; verordening | GEMMA (definitie Afspraak) |
| 16 | *representatie* | Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip in `genoemd_begrip`. | aanslagbiljet (van Aanslag); register van begraven lijken | aanslag | ArchiMate (Representation) |

**Soort gedrag.** Stap 3, het keuzeveld `soort_gedrag`, alleen bij *gedrag*: één waarde uit het vak; valt weg bij gedrag extern (*aangeboden gedrag*).

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 17 | *per keer doorlopen* | Is het een proces: een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen, of een groepering van zulke processen naar soort werk (een cluster)? | aanvraag omgevingsvergunning behandelen; Behandelen vergunningaanvragen lijkbezorging (cluster) | vergunningverlening; Verzorgen lijkbezorging (een groepering naar taak is het beleidsdomein, geen proces) | GEMMA (definitie Bedrijfsproces en Procescluster, regel 409 en 419-420; processenlandschap naar soort werk); wiki (geen taak) |
| 18 | *gegroepeerd gedrag* | Is het een doorlopende groepering van werk dat de organisatie uitvoert, op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd? Wat de gemeente moet kunnen, strategisch, is een capability (vak strategie). | vergunningverlening; belastingheffing | aanslag opleggen (proces) | GEMMA (definitie Bedrijfsfunctie) |
| 19 | *toestandsverandering* | Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | verhuizing; aanvraag ontvangen; beslistermijn verstreken | verhuizing doorgeven | GEMMA (definitie Gebeurtenis) |
| 20 | *aangeboden gedrag* | Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | melding openbare ruimte doen | melding afhandelen | NORA (definitie Dienst) |
| 21 | *gezamenlijk gedrag* | Kan het alleen door twee of meer partijen samen worden uitgevoerd, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen? | Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer); keukentafelgesprek | beschikking opstellen; Treffen maatregel bij besmet lijk (de GGD adviseert alleen) | ArchiMate (Business Interaction); GEMMA Online, Proceshiërarchie (ketensamenwerking als bedrijfsinteractie) |

**Partij en regeling.** Stap 3, alleen bij *handelende partij*, *hoedanigheid* of *samenwerkingsverband* (*eigen rechtspersoon* en *soort partij*; *los van verantwoordelijkheid* alleen als afwijking: het volgt uit het hoofdkenmerk) en bij *regeling als geheel* (*landelijk*).

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 22 | *los van verantwoordelijkheid* | Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | kerkgenootschap; burgemeester | houder van de begraafplaats | ArchiMate (actor tegenover rol) |
| 23 | *eigen rechtspersoon* | Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | GGD (openbaar lichaam) | Zorg- en Veiligheidshuis | wiki (scheidslijn actor en bedrijfssamenwerking) |
| 24 | *soort partij* | Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Gemeente; College van B&W; Kerkgenootschap; Rijk, Provincie en Waterschap (de bestuurslaag als geheel, ook al is er maar één Rijk) | gemeente Utrecht, provincie Utrecht (één exemplaar, niet elke gemeente heeft ermee te maken); een afzonderlijk ministerie of rijksdienst (minister van BZK, IND) is geen eigen actor maar staat in de beschrijving van Rijk | GEMMA (referentiemodel voor alle gemeenten); wiki (Rijk) |
| 25 | *landelijk* | Geldt het voor alle gemeenten: Europese regelgeving of rijksregelgeving (EU-verordening, wet, AMvB, ministeriële regeling) of een VNG-modelverordening van gemeentelijke regelgeving, en geen regeling of beleid van één gemeente? | Wet op de lijkbezorging; AVG; modelverordening | beheersverordening of beleidsnota van één gemeente (blijft bron) | GEMMA (definitie Beleidskader); wiki |

**Toets.** Stap 5: de toetskenmerken van het type (zie de tabel per type). Een relatiekenmerk (†) is altijd ja of nee, met de tegenpartij; de andere zijn standaard ja en staan alleen als nee in de beoordeling. Alle moeten ja zijn; een nee wordt voorgelegd.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 26 | *toegewezen partij* † | Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. | Ruimen graf (Houder van de begraafplaats) | draagvlak creëren | ArchiMate (toewijzing van rol aan gedrag) |
| 27 | *aanleiding* † | Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. | overheidsparticipatie (verzoek ingediend) | kennisdeling | ArchiMate (triggering); GEMMA (procesarchitectuur) |
| 28 | *benoembaar resultaat* (standaard ja) | Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. | opgraving (opgegraven lijk) | informeren | GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer) |
| 29 | *omvat processen* † | Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? Noem ze. | Behandelen vergunningaanvragen lijkbezorging (Verlenen verlof tot begraving of crematie, Opgraven stoffelijk overschot) | een proces met één stap | GEMMA (procescluster aggregeert bedrijfsprocessen, regel 419-420) |
| 30 | *bedient gedrag* † | Ondersteunt de functie aanwijsbaar een proces? Noem het. | Exploiteren van begraafplaatsen bedient Ruimen graf | functie zonder aanwijsbaar proces | GEMMA (functie bedient proces, regel 597 en 604) |
| 31 | *gebruikt objecten* † | Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. | Inspraak (registreert zienswijze) | burgerberaad | ArchiMate (toegang van gedrag tot object); wiki (handelingen) |
| 32 | *in functie-indeling* † | Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? Noem de bovenliggende functie of het domein. | Exploiteren van begraafplaatsen (onder Exploitatie fysieke leefomgeving) | Lijkbezorging als functie | GEMMA (Functie-indeling naar domein) |
| 33 | *stabiel over tijd* (standaard ja) | Blijft het bestaan als de organisatie, de werkwijze of de systemen veranderen, en is het geen opgave met een einde? | participatie; belastingheffing; Identiteit vaststellen | projectteam Omgevingswet; invoering van de Omgevingswet (een opgave) | ArchiMate en GEMMA (bedrijfsfunctiemodel); wiki (kader Capability) |
| 34 | *leidt tot gedrag* † | Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. | Overlijden → Uitvoeren lijkbezorging | voorval zonder gemeentelijk gevolg | GEMMA (gebeurtenis triggert proces) |
| 35 | *komt herhaald voor* (standaard ja) | Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | overlijden; aanvraag ontvangen | invoeren van de participatieverordening | GEMMA (gebeurtenis als herhaalbaar voorval) |
| 36 | *gerealiseerd door* † | Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? Noem ze. | Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt); Personen registreren (Bevolkingsadministratie bijhouding, Burgerlijke stand diensten) | dienst of vermogen zonder aanwijsbare uitvoering | GEMMA (proces en functie realiseren dienst; functie realiseert capability) |
| 37 | *afnemer* (standaard ja) | Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. | melding openbare ruimte doen (inwoner) | interne registratiestap | NORA (definitie Dienst); GEMMA (definitie Product, rol Klant) |
| 38 | *omvat diensten en afspraken* † | Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. | parkeervergunning (dienst parkeren, voorwaarden) | losse dienst | GEMMA (product bundelt dienst en afspraak) |
| 39 | *zelfstandig aanbod* (standaard ja) | Wordt het onder een eigen naam aangeboden, en niet als variant of tarief van een ander product? | bewonersparkeervergunning | bezoekersparkeervergunning als tarief van parkeervergunning | UPL (één naam per aanbod) |
| 40 | *wordt bewerkt* † | Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. | aanvraag (geregistreerd, beoordeeld) | preventieakkoord (alleen beleidsmatig) | GEMMA (proces en functie benaderen bedrijfsobject) |
| 41 | *onderscheidbare exemplaren* (standaard ja) | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | aanvraag (elke aanvraag apart) | gemeentefonds (er is er één) | GEMMA (kan in meervoud bestaan) |
| 42 | *levenscyclus* (standaard ja) | Ontstaan, veranderen en eindigen de exemplaren? | vergunning (verleend, gewijzigd, ingetrokken) | kadastrale gemeentecode | GEMMA (eigen levenscyclus) |
| 43 | *vervult een rol* † | Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. | kerkgenootschap vervult Houder van de begraafplaats | partij die alleen genoemd wordt | GEMMA (actor wordt toegewezen aan rol) |
| 44 | *voert gedrag uit* † | Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. | Houder van de begraafplaats → Ruimen graf | rol zonder aanwijsbaar gedrag | GEMMA (rol wordt toegewezen aan functie); wiki (ook aan proces) |
| 45 | *ontsluit een dienst* † | Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. | website → Melding openbare ruimte doen | kanaal zonder aanwijsbare dienst | GEMMA (kanaal wordt toegewezen aan dienst) |
| 46 | *is grondslag voor* † | Geeft de regeling de gemeente een taak, bevoegdheid of plicht, of werkt de VNG-modelverordening die uit, in een aanwijsbaar proces, dienst of product? Noem het artikel of de paragraaf en het gedrag. | Wet op de lijkbezorging art. 28 → Verlenen grafrecht | BW boek 2, gebruikt voor één definitie | GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader) |
| 47 | *in werking* (standaard ja) | Is de regeling geldend recht, of als modelverordening actueel? | Archiefwet 1995 | ingetrokken wet | wiki |
| 48 | *beoordeelbaar* | Kun je er volwassenheid of ontwikkelbehoefte van bepalen en er apart in investeren? Noem de investeringsvraag. | Identiteit vaststellen (fraudebestrijding, biometrie) | Dienstverlening (te breed) | wiki (kader Capability: beoordeelbaar) |
| 49 | *onderscheidend* | Is het af te grenzen van de andere capabilities, zonder dat een functie er voor een deel in valt? Noem de naaste capability. | Personen registreren naast Identiteit vaststellen | Burgers helpen naast Dienstverlening | wiki (kader Capability: onderscheidend) |

**Indeling.** Stap 6, alleen een afwijking: zonder antwoord is een bedrijfsobject niet generiek.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 50 | *generiek* | Komt het met dezelfde betekenis in veel onderwerpen voor? | Besluit; Beschikking; aanvraag ontvangen; Klant | Graf; Ruimen graf | wiki (abstractieniveau; GEMMA generieke elementen) |

## Toetskenmerken per type

Alle toetskenmerken van het type moeten ja zijn; een nee wordt voorgelegd. Een relatiekenmerk (†) is een kernrelatie: altijd ja of nee, met de tegenpartij. De andere zijn standaard ja; de beoordeling schrijft alleen een nee, de elementpagina toont ze allemaal.

| Type | Toetskenmerken |
|---|---|
| Bedrijfsobject | *wordt bewerkt* †, *onderscheidbare exemplaren*, *levenscyclus* |
| Afspraak | *wordt bewerkt* †, *onderscheidbare exemplaren*, *levenscyclus* |
| Product | *omvat diensten en afspraken* †, *zelfstandig aanbod*, *afnemer*, *benoembaar resultaat* |
| Dienst | *gerealiseerd door* †, *afnemer*, *benoembaar resultaat* |
| Bedrijfsproces | *toegewezen partij* †, *aanleiding* †, *benoembaar resultaat* |
| Procescluster | *omvat processen* † |
| Bedrijfsfunctie | *bedient gedrag* †, *gebruikt objecten* †, *in functie-indeling* †, *stabiel over tijd* |
| Gebeurtenis | *leidt tot gedrag* †, *komt herhaald voor* |
| Actor | *vervult een rol* † |
| Rol | *voert gedrag uit* † |
| Bedrijfssamenwerking | *voert gedrag uit* † |
| Kanaal | *ontsluit een dienst* † |
| Beleidskader | *is grondslag voor* †, *in werking* |
| Bedrijfsinteractie | *toegewezen partij* †, *aanleiding* †, *benoembaar resultaat* |
| Capability | *gerealiseerd door* †, *beoordeelbaar* (expliciet), *onderscheidend* (expliciet), *stabiel over tijd* (expliciet) |

## Stappentabel

Vier fasen, zeven stappen. Afbakenen (stap 0 tot en met 2) en het type in Typeren (stap 3) van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig type op. Stap 4 (grondslag) doet het script, stap 5 toetst de toetskenmerken, stap 6 deelt in.

| Nr | Stap | Als | Dan |
|---|---|---|---|
| 1 | 0 Welk begrip | `synoniem_van` ingevuld | synoniem: geen pagina; het woord naar `synoniemen` van het element, met context |
| 2 | 1 Scope | niet *herkenbaar* of niet *gemeentelijk* | buiten scope, met reden |
| 3 | 1 Scope | *buiten dit model* | buiten dit model, met het ArchiMate-type |
| 4 | 1 Scope | niet *betekenis in onderwerp* | verwijzing in de begrippenlijst; beoordelen in het onderwerp waar het hoort |
| 5 | 2 Afhankelijk | *afhankelijkheid* eigenschap | eigenschap van het genoemde begrip; geen pagina |
| 6 | 2 Afhankelijk | *afhankelijkheid* onderdeel | onderdeel van het genoemde begrip; geen pagina, relaties naar het geheel; een bedrijfsobject dat kernobject is van een bedrijfsproces wordt in stap 6 een subobject |
| 7 | 2 Afhankelijk | *afhankelijkheid* deelproces | deelproces of processtap van het genoemde bedrijfsproces; geen pagina, de tekst naar zijn `deelprocessen` |
| 8 | 2 Afhankelijk | *afhankelijkheid* invoer van een ander | onderdeel: geen pagina; vermelden bij het genoemde proces |
| 9 | 2 Afhankelijk | *afhankelijkheid* variant | specialisatie zonder pagina; relaties naar het genoemde, bredere begrip van hetzelfde type |
| 10 | 3 Type en niveau | het hoofdkenmerk of de soort gedrag past niet bij het vak, of een kenmerk is ja dat niet bij het hoofdkenmerk past (zie *alleen bij* per groep) | conflict: voorleggen |
| 11 | 3 Type en niveau | *samenwerkingsverband* | *eigen rechtspersoon*: ja Actor, nee Bedrijfssamenwerking |
| 12 | 3 Type en niveau | *handelende partij* | Actor; conflict als niet *los van verantwoordelijkheid* |
| 13 | 3 Type en niveau | *hoedanigheid* | Rol; conflict als *los van verantwoordelijkheid* |
| 14 | 3 Type en niveau | *aanbod als geheel* | Product |
| 15 | 3 Type en niveau | *toegangspunt* | Kanaal: koppelen aan de centrale set; voorleggen |
| 16 | 3 Type en niveau | *plaats* | Locatie: geen pagina |
| 17 | 3 Type en niveau | *regeling als geheel* | *landelijk*: ja Beleidskader, nee bron (geen element) |
| 18 | 3 Type en niveau | *vermogen* | Capability |
| 19 | 3 Type en niveau | *gedrag* | naar de soort gedrag: Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Dienst of Bedrijfsinteractie |
| 20 | 3 Type en niveau | *representatie* | Representatie: geen pagina; vermelden bij het genoemde object |
| 21 | 3 Type en niveau | *afspraak* | Afspraak (Contract) |
| 22 | 3 Type en niveau | *object* | Bedrijfsobject |
| 23 | 3 Type en niveau | Actor of Bedrijfssamenwerking, niet *soort partij* | geen element: voorleggen; het element geldt niet voor alle gemeenten |
| 24 | 3 Type en niveau | Bedrijfsproces | *procesniveau*: levensloopproces, bedrijfsproces of cluster naar soort werk; het cluster krijgt de toetskenmerken van een Procescluster |
| — | Stap 4 Grondslag | geen landelijke bron (`europese-regelgeving`, `rijksregelgeving`) bij een element, behalve een UPL-dienst, een bedrijfsfunctie, een beleidskader en een capability die volgt wat zij omvat | geen grondslag: stop. Een UPL-dienst zonder grondslag staat in de hoek zonder grondslag (tools/beslissen.py) |
| 25 | 5 Toetskenmerken | een toetskenmerk van het type is nee, of een capability heeft minder dan twee functies | geen element: voorleggen met de kenmerken die nee zijn |
| 26 | 6 Indeling | procesniveau cluster naar soort werk | `gemma_generiek` verplicht, anders voorleggen: een taak is geen procesniveau, de groepering naar taak is het beleidsdomein |
| 27 | 6 Indeling | procesniveau levensloopproces | `kernobject` verplicht. Per kernobject één levensloopproces, met het beleidsdomein van het kernobject; meer alleen als ze samen een bedrijfsinteractie met dat kernobject bedienen, elk het deel van één partij |
| 28 | 6 Indeling | procesniveau bedrijfsproces | `kernobject` verplicht; geaggregeerd door één levensloopproces |
| 29 | 6 Indeling | bedrijfsinteractie | `kernobject` verplicht; het beleidsdomein van het kernobject |
| 30 | 6 Indeling | bedrijfsobject met *generiek* | objectniveau generiek (thuis in een thematisch gedeeld onderwerp of Kern) |
| 31 | 6 Indeling | gebeurtenis, rol of dienst met *generiek* | specialisatie van een generiek GEMMA-element (exacte match) |
| 32 | 6 Indeling | bedrijfsobject dat `kernobject` is van een levensloopproces | objectniveau kernobject; per kernobject één levensloopproces, of één per partij in een ketensamenwerking |
| 33 | 6 Indeling | bedrijfsobject met *afhankelijkheid* onderdeel dat `kernobject` is van een bedrijfsproces | objectniveau subobject (het script beoordeelt het dan als element) |
| 34 | 6 Indeling | ander bedrijfsobject | voorleggen: geen proces bepaalt zijn levensloop |
| — | Aanvulling | `homoniem_van` ingevuld | voorleggen: naamkeuze; `## Homoniemen` bij beide; bij een GGM-homoniem een terugmelding |
| — | Aanvulling | Bedrijfsobject, afspraak, rol, actor of gebeurtenis met een GGM-match, of met sterkte geen en een GGM-terugmelding hiaat | het data-object *<naam>-data* (tools/beslissen.py); `data_objecten` voor een extra GGM-entiteit |
| — | Signaal (controle) | Dienst zonder realiserend proces of functie met pagina; Gebeurtenis zonder gestart gedrag met pagina | waarschuwing: proces als kandidaat voorleggen |
| — | Signaal (controle) | Functie onder domeinniveau of dienst zonder (bovenliggende) functie, met meer (bovenliggende) functies, met een ander domein, of een functie buiten de GEMMA-functieketen; product onder een functie | waarschuwing: de (bovenliggende) functie wordt een element met een aggregatie naar de functie of de dienst; een functie met GEMMA type *Bedrijfsfunctie domein* en een product hangen via `domein` aan de domeingroepering |
| — | Signaal (controle) | Product of dienst waarvan het domein niet past bij de GEMMA-domeinen van zijn beleidsdomein; een beleidsdomein dat GEMMA niet kent met producten en diensten in meer domeinen | waarschuwing: domein of beleidsdomein herzien, of het verschil voorleggen als voorstel aan het GEMMA-team |
