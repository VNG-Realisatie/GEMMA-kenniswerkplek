---
id: kenmerken-en-beslistabel
type: kennismodel
titel: Kenmerken en beslistabel
---

# Kenmerken en beslistabel

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

Elk begrip uit een bron krijgt één keer dezelfde vragen: de kenmerken. De beslistabel past daar vaste regels op toe; de uitkomst is het type, of de reden waarom het begrip geen eigen pagina krijgt. Er wordt nooit eerst een type gekozen. Per elementtype staat in zijn modelleerafspraken welke kenmerken het type bepalen, welke de kernrelatie is en welke drempel geldt.

## Stap 0: welk begrip?

Vóór de kenmerken: bepaal welk begrip bedoeld is. Synoniemen en homoniemen zijn geen kenmerken van een begrip, maar verhoudingen tussen een woord en een begrip.

| Veld | Vraag | Uitkomst |
|---|---|---|
| `synoniem_van` | Is dit een ander woord voor een begrip dat al een element is, of in deze run wordt beoordeeld? Noem dat element en de context van het woord. | synoniem: geen pagina; het woord naar de synoniemen van het element |
| `homoniem_van` | Bestaat dezelfde naam al voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron? Noem dat begrip en waar het voorkomt. | door naar de kenmerken; naamkeuze voorleggen |

## Kenmerken

Beantwoord alle vragen, ook die niet bij de aard van het begrip passen (dan nee). Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; zonder zo'n verwijzing is het antwoord nee.

**Poort.** Altijd.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 1 | *herkenbaar* | Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning) | technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel) | ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts) |
| 2 | *gemeentelijk* | Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD; behandelende arts via de overlegplicht met de lijkschouwer) | alleen context (gedeputeerde staten als beroepsinstantie), of de interne zaak van een ketenpartner (de medische behandeling door de arts) | GEMMA (gemeentelijk perspectief) |
| 3 | *buiten dit model* | Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? Noem het ArchiMate-type. | armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel) | bijstandsuitkering; Wet op de lijkbezorging (beleidskader) | ArchiMate (motivatie-, strategie- en overige lagen) |
| 4 | *slechts eigenschap* | Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een doelgroep? Noem dat begrip. | bouwjaar (van Pand); minima (indeling van Inwoner) | Pand | GEMMA (negatieve toets: eigenschap, status, classificatie) |
| 5 | *eigen identiteit* | Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? Noem bij nee dat begrip. | Beschikking; uitgifte van een graf | ondertekening van een besluit (deelstap) | GEMMA (eigen bestaan; procesarchitectuur: processtap, handeling) |
| 6 | *betekenis in onderwerp* | Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? Noem bij nee het onderwerp waar het thuishoort. | Graf in lijkbezorging | akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand) | GEMMA (betekenis binnen het onderwerp) |

**Aard.** Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 7 | *gedrag* | Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | aanvraag behandelen; verhuizing | aanvraag | ArchiMate (gedragselement) |
| 8 | *handelende partij* | Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | college van B&W; inwoner | aanvrager | GEMMA (definitie Actor) |
| 9 | *hoedanigheid* | Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | aanvrager; houder van de begraafplaats | gemeenteraad | ArchiMate (definitie Rol) |
| 10 | *samenwerkingsverband* | Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? | Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten) | GGD-arts | ArchiMate (definitie Bedrijfssamenwerking) |
| 11 | *toegangspunt* | Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? | publieksbalie; gemeentelijke website | klantcontact | NORA (definitie Kanaal) |
| 12 | *plaats* | Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? | stadskantoor als vestigingsplaats | wijk (indeling) | ArchiMate (Location) |
| 13 | *aanbod als geheel* | Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? | bewonersparkeervergunning zoals de productencatalogus haar aanbiedt | parkeren | GEMMA (definitie Product) |
| 14 | *regeling als geheel* | Is het een concreet benoemde wet, AMvB, verordening of landelijke richtlijn als geheel, en niet één artikel of een soort regeling? | Wet op de lijkbezorging; modelverordening participatie; Circulaire adresonderzoek BRP | 'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm) | GEMMA (definitie Beleidskader) |

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*; *soort partij* bij *handelende partij* en *samenwerkingsverband*.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 15 | *los van verantwoordelijkheid* | Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | kerkgenootschap; burgemeester | houder van de begraafplaats | ArchiMate (actor tegenover rol) |
| 16 | *eigen rechtspersoon* | Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | GGD (openbaar lichaam) | Zorg- en Veiligheidshuis | wiki (scheidslijn actor en bedrijfssamenwerking) |
| 17 | *vervult een rol* | Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. | kerkgenootschap vervult Houder van de begraafplaats | partij die alleen genoemd wordt | GEMMA (actor wordt toegewezen aan rol) |
| 18 | *voert gedrag uit* | Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. | Houder van de begraafplaats → Ruimen graf | rol zonder aanwijsbaar gedrag | GEMMA (rol wordt toegewezen aan functie); wiki (ook aan proces) |
| 19 | *soort partij* | Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Gemeente; College van B&W; Kerkgenootschap; Rijk, Provincie en Waterschap (de bestuurslaag als geheel, ook al is er maar één Rijk) | gemeente Utrecht, provincie Utrecht (één exemplaar, niet elke gemeente heeft ermee te maken); een afzonderlijk ministerie of rijksdienst (minister van BZK, IND) is geen eigen actor maar staat in de beschrijving van Rijk | GEMMA (referentiemodel voor alle gemeenten); wiki (Rijk) |
| 20 | *ontsluit een dienst* | Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. | website → Melding openbare ruimte doen | kanaal zonder aanwijsbare dienst | GEMMA (kanaal wordt toegewezen aan dienst) |

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 21 | *per keer doorlopen* | Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | aanvraag omgevingsvergunning behandelen | vergunningverlening | GEMMA (definitie Bedrijfsproces) |
| 22 | *groepeert processen* | Is het een groepering van bedrijfsprocessen van één soort werk, die niet per geval wordt doorlopen? | Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk) | Beheren grafrechten (loopt per grafrecht van begin tot eind door); Verzorgen lijkbezorging (een groepering naar taak is het beleidsdomein, geen proces) | GEMMA (definitie Procescluster, regel 409 en 419-420; processenlandschap naar soort werk); wiki (geen taak) |
| 23 | *gegroepeerd gedrag* | Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? | vergunningverlening; belastingheffing | aanslag opleggen | GEMMA (definitie Bedrijfsfunctie) |
| 24 | *toestandsverandering* | Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | verhuizing; aanvraag ontvangen; beslistermijn verstreken | verhuizing doorgeven | GEMMA (definitie Gebeurtenis) |
| 25 | *aangeboden gedrag* | Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | melding openbare ruimte doen | melding afhandelen | NORA (definitie Dienst) |
| 26 | *gezamenlijk gedrag* | Kan het alleen door twee of meer partijen samen worden uitgevoerd, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen? | Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer); keukentafelgesprek | beschikking opstellen; Treffen maatregel bij besmet lijk (de GGD adviseert alleen) | ArchiMate (Business Interaction); GEMMA Online, Proceshiërarchie (ketensamenwerking als bedrijfsinteractie) |

**Gedrag.** Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 27 | *toegewezen partij* | Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. | Ruimen graf (Houder van de begraafplaats) | draagvlak creëren | ArchiMate (toewijzing van rol aan gedrag) |
| 28 | *gebruikt objecten* | Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. | Inspraak (registreert zienswijze) | burgerberaad | ArchiMate (toegang van gedrag tot object); wiki (handelingen) |
| 29 | *aanleiding* | Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. | overheidsparticipatie (verzoek ingediend) | kennisdeling | ArchiMate (triggering); GEMMA (procesarchitectuur) |
| 30 | *benoembaar resultaat* | Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. | opgraving (opgegraven lijk) | informeren | GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer) |
| 31 | *komt herhaald voor* | Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | inspraak (per ontwerpbesluit); overlijden | invoeren van de participatieverordening | GEMMA (proces als herhaalbare werkwijze) |
| 32 | *eigen normering* | Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. | inspraak (afdeling 3.4 Awb) | burgerberaad (vormvrij) | GEMMA (proces met eigen spelregels) |
| 33 | *stabiel over tijd* | Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? | participatie; belastingheffing | projectteam Omgevingswet | ArchiMate en GEMMA (bedrijfsfunctiemodel) |
| 34 | *afnemer* | Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. | melding openbare ruimte doen (inwoner) | interne registratiestap | NORA (definitie Dienst); GEMMA (definitie Product, rol Klant) |
| 35 | *gerealiseerd door* | Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. | Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt) | dienst zonder aanwijsbare uitvoering | GEMMA (proces en functie realiseren dienst) |
| 36 | *leidt tot gedrag* | Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. | Overlijden → Uitvoeren lijkbezorging | voorval zonder gemeentelijk gevolg | GEMMA (gebeurtenis triggert proces) |
| 37 | *bijdrage aan groter proces* | Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? Noem dat proces. | Verlenen grafrecht (in Beheren grafrechten); toetsen indieningsvereisten (in behandelen aanvraag) | Beheren grafrechten (omvat zelf de hele levensloop) | GEMMA Online, Proceshiërarchie (bedrijfsproces en deelproces) |
| 38 | *klant tot klant* | Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? Noem begin en eind. | Behandelen aanvraag reisdocument (van de aanvraag tot de uitreiking of weigering) | Uitreiken reisdocument (volgt op de verstrekking, voor hetzelfde geval) | GEMMA Online, Proceshiërarchie (bedrijfsproces klant-tot-klant, PH 81; deelproces levert een deeldienst, PH 83) |
| 39 | *omvat processen* | Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? Noem ze. | Behandelen vergunningaanvragen lijkbezorging (Verlenen verlof tot begraving of crematie, Opgraven stoffelijk overschot) | een proces met één stap | GEMMA (procescluster aggregeert bedrijfsprocessen, regel 419-420) |
| 40 | *omvat levensloop* | Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? Noem het object. | Beheren grafrechten (Grafrecht: van uitgifte tot verval); Toestaan lijkbezorging (het deel van de gemeente als overheid in de levensloop van het stoffelijk overschot) | Verlenen grafrecht (één mutatie in die levensloop) | GEMMA Online, Proceshiërarchie (cluster van bedrijfsprocessen over één thema, PH 91); wiki (levensloopproces; één per partij binnen een ketensamenwerking) |
| 41 | *eigen besluit* | Eindigt het in een besluit van een bevoegd orgaan of een mandataris? Noem orgaan en artikel. | Verlenen grafrecht (college, Wlb art. 28) | Onderhouden graf (feitelijk handelen) | GEMMA (procesbouwstenen: besluiten) |
| 42 | *levert aanbod* | Realiseert het een dienst of levert het een product aan een afnemer? Noem het (referentie: de UPL). | Onderhouden graf (grafonderhoud) | interne registratiestap | GEMMA (Product en dienst procesarchitectuur, UPL) |
| 43 | *bedient gedrag* | Ondersteunt de functie aanwijsbaar een proces? Noem het. | Exploiteren van begraafplaatsen bedient Ruimen graf | functie zonder aanwijsbaar proces | GEMMA (functie bedient proces, regel 597 en 604) |
| 44 | *in functie-indeling* | Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? Noem de bovenliggende functie of het domein. | Exploiteren van begraafplaatsen (onder Exploitatie fysieke leefomgeving) | Lijkbezorging als functie | GEMMA (Functie-indeling naar domein) |
| 45 | *leidt tot gebeurtenis* | Eindigt het in een toestandsverandering die domeinexperts benoemen, of die een ander proces start? Noem die. | Vervallen verklaren grafrecht → Verval van het grafrecht | een tussenstap zonder eigen uitkomst | GEMMA (proces triggert gebeurtenis, regel 924) |

**Passief.** Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en *geautomatiseerd verwerkt* bij elk begrip; *deel van object* en *invoer van een ander* bij een ding; *omvat diensten en afspraken* en *zelfstandig aanbod* bij *aanbod als geheel*.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 46 | *onderscheidbare exemplaren* | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | aanvraag (elke aanvraag apart) | gemeentefonds (er is er één) | GEMMA (kan in meervoud bestaan) |
| 47 | *levenscyclus* | Ontstaan, veranderen en eindigen de exemplaren? | vergunning (verleend, gewijzigd, ingetrokken) | kadastrale gemeentecode | GEMMA (eigen levenscyclus) |
| 48 | *wordt bewerkt* | Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. | aanvraag (geregistreerd, beoordeeld) | preventieakkoord (alleen beleidsmatig) | GEMMA (proces en functie benaderen bedrijfsobject) |
| 49 | *afspraak* | Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? | subsidieovereenkomst; uitvoeringsovereenkomst | subsidiebeschikking; verordening | GEMMA (definitie Afspraak) |
| 50 | *waarneembare vorm* | Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. | aanslagbiljet (van Aanslag); register van begraven lijken | aanslag | ArchiMate (Representation) |
| 51 | *deel van object* | Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? Noem dat object. | grafbedekking (van Graf) | Graf | GEMMA (negatieve toets: eigen identiteit) |
| 52 | *invoer van een ander* | Maakt en beheert een andere partij het, terwijl de gemeente het alleen ontvangt of raadpleegt? Noem de maker. | verklaring van overlijden (de arts of lijkschouwer) | vergunning (de gemeente verleent haar) | wiki (abstractieniveau) |
| 53 | *zelfstandig aanbod* | Wordt het onder een eigen naam aangeboden, en niet als variant of tarief van een ander product? | bewonersparkeervergunning | bezoekersparkeervergunning als tarief van parkeervergunning | UPL (één product per productnaam) |
| 54 | *omvat diensten en afspraken* | Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. | parkeervergunning (dienst parkeren, voorwaarden) | losse dienst | GEMMA (product bundelt dienst en afspraak) |
| 55 | *geautomatiseerd verwerkt* | Wordt het als gegevensstructuur geautomatiseerd verwerkt? | zaak in het zaaksysteem | keukentafelgesprek | GEMMA (definitie Data-object) |

**Beleidskader.** Alleen bij *regeling als geheel*.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 56 | *landelijk* | Geldt het voor alle gemeenten: Europese regelgeving of rijksregelgeving (EU-verordening, wet, AMvB, ministeriële regeling), een landelijke richtlijn (uitvoeringsvoorschrift, handleiding of circulaire van een landelijke organisatie) of een VNG-model van gemeentelijke regelgeving, en geen regeling of beleid van één gemeente? | Wet op de lijkbezorging; AVG; Circulaire adresonderzoek BRP (RvIG); modelverordening | beheersverordening of beleidsnota van één gemeente (blijft bron) | GEMMA (definitie Beleidskader); wiki |
| 57 | *in werking* | Is de regeling geldend recht, of als modelverordening actueel? | Archiefwet 1995 | ingetrokken wet | wiki |
| 58 | *is grondslag voor* | Geeft de regeling de gemeente een taak, bevoegdheid of plicht, of schrijft de richtlijn voor hoe zij die uitvoert, in een aanwijsbaar proces, dienst of product? Noem het artikel of de paragraaf en het gedrag. | Wet op de lijkbezorging art. 28 → Verlenen grafrecht | BW boek 2, gebruikt voor één definitie | GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader) |

**Specialisatie.** Altijd, als het type een pagina heeft.

| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |
|---|---|---|---|---|---|
| 59 | *zelfstandige specialisatie* | Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. | Omgevingsvergunning naast Vergunning (eigen wet en procedure); Houder van het crematorium naast Houder van de begraafplaats (eigen plichten) | vergunning tot opgraving (variant van Vergunning); aanvrager van een vergunning tot opgraving (variant van Aanvrager) | GEMMA (zelfstandig ding waar beleid op gemaakt wordt; specialisatie) |
| 60 | *generiek* | Komt het met dezelfde betekenis in veel onderwerpen voor? | Besluit; Beschikking; aanvraag ontvangen; Klant | Graf; Ruimen graf | wiki (abstractieniveau; GEMMA generieke elementen) |

## Stappentabel

Stap 0–4 van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig type op. Een voorlopig type met een pagina gaat door naar stap 5 (drempel), stap 6 (zelfstandige specialisatie) en stap 7 (indeling: procesniveau en objectniveau). Daarna gelden de aanvullingen.

| Nr | Stap | Als | Dan |
|---|---|---|---|
| 1 | 0 Welk begrip | `synoniem_van` ingevuld | synoniem: geen pagina; het woord naar `synoniemen` van het element, met context |
| 2 | 1 Scope | niet *herkenbaar* of niet *gemeentelijk* | buiten scope, met reden |
| 3 | 1 Scope | *buiten dit model* | buiten dit model, met het ArchiMate-type |
| 4 | 2 Afhankelijk | *slechts eigenschap* | eigenschap van het genoemde begrip; geen pagina |
| 5 | 2 Afhankelijk | niet *eigen identiteit* | onderdeel van het genoemde begrip; geen pagina, relaties naar het geheel |
| 6 | 2 Afhankelijk | niet *betekenis in onderwerp* | verwijzing in de begrippenlijst; beoordelen in het onderwerp waar het hoort |
| 7 | 3 Consistentie | een kenmerk is ja dat niet bij de aard past (zie *alleen bij* per groep) | conflict: voorleggen |
| 8 | 4 Type | *handelende partij* en *hoedanigheid* | *los van verantwoordelijkheid*: ja Actor, nee Rol |
| 9 | 4 Type | *samenwerkingsverband* (eventueel met *handelende partij*) | *eigen rechtspersoon*: ja Actor, nee Bedrijfssamenwerking |
| 10 | 4 Type | andere combinatie van meer dan één aard | conflict: voorleggen |
| 11 | 4 Type | *handelende partij* | Actor; conflict als niet *los van verantwoordelijkheid* |
| 12 | 4 Type | *hoedanigheid* | Rol; conflict als *los van verantwoordelijkheid* |
| 13 | 4 Type | *aanbod als geheel* | Product |
| 14 | 4 Type | *toegangspunt* | Kanaal: koppelen aan de centrale set; voorleggen |
| 15 | 4 Type | *plaats* | Locatie: geen pagina |
| 16 | 4 Type | *regeling als geheel* | *landelijk*: ja Beleidskader, nee bron (geen element) |
| 17 | 4 Type | *gedrag* en precies één soort gedrag | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Dienst of Bedrijfsinteractie |
| 18 | 4 Type | *gedrag*, maar geen of meer dan één soort gedrag | conflict: voorleggen |
| 19 | 4 Type | geen aard, *waarneembare vorm* | Representatie: geen pagina; vermelden bij het genoemde object |
| 20 | 4 Type | geen aard, *afspraak* | Afspraak (Contract) |
| 21 | 4 Type | geen aard, overig | Bedrijfsobject |
| 22 | 5 Drempel | kernrelatie of eis van het type nee | geen element: voorleggen met de ontbrekende relatie |
| 23 | 5 Drempel | meer dan 1 van de overige drempelcriteria nee | geen element: voorleggen met de ontbrekende criteria |
| 24 | 6 Specialisatie | niet *zelfstandige specialisatie*, met `genoemd_begrip` | specialisatie zonder pagina; relaties naar het genoemde, bredere begrip |
| 25 | 6 Specialisatie | niet *zelfstandige specialisatie*, zonder `genoemd_begrip` | voorleggen: noem het bredere begrip |
| 26 | 6 Specialisatie | anders | element van het voorlopige type |
| 27 | 7 Indeling | procescluster (*groepeert processen*) | procesniveau cluster naar soort werk; `gemma_generiek` verplicht, anders voorleggen: een taak is geen procesniveau, de groepering naar taak is het beleidsdomein |
| 28 | 7 Indeling | *omvat levensloop* | procesniveau levensloopproces; `kernobject` verplicht. Per kernobject één levensloopproces, met het beleidsdomein van het kernobject; meer alleen als ze samen een bedrijfsinteractie met dat kernobject bedienen, elk het deel van één partij |
| 29 | 7 Indeling | *bijdrage aan groter proces* met *klant tot klant* | procesniveau bedrijfsproces; `kernobject` verplicht; geaggregeerd door één levensloopproces |
| 30 | 7 Indeling | *bijdrage aan groter proces* zonder *klant tot klant* | deelproces of processtap: onderdeel, geen pagina; `genoemd_begrip` is het bedrijfsproces, de tekst naar zijn `deelprocessen`; met *levert aanbod* voorleggen |
| 31 | 7 Indeling | geen levensloop en geen bijdrage aan een groter proces | voorleggen: procesniveau niet te bepalen |
| 32 | 7 Indeling | bedrijfsobject met *generiek* | objectniveau generiek (verhuist later naar een algemeen onderwerp) |
| 33 | 7 Indeling | bedrijfsobject met *invoer van een ander* | onderdeel: geen pagina; vermelden bij het genoemde proces |
| 34 | 7 Indeling | gebeurtenis, rol of dienst met *generiek* | specialisatie van een generiek GEMMA-element (exacte match) |
| 35 | 7 Indeling | bedrijfsobject dat `kernobject` is van een levensloopproces | objectniveau kernobject; per kernobject één levensloopproces, of één per partij in een ketensamenwerking |
| 36 | 7 Indeling | bedrijfsobject met *deel van object* en een eigen bedrijfsproces | objectniveau subobject |
| 37 | 7 Indeling | bedrijfsobject met *deel van object* zonder eigen bedrijfsproces | onderdeel: geen pagina |
| 38 | 7 Indeling | ander bedrijfsobject | voorleggen: geen proces bepaalt zijn levensloop |
| 39 | 7 Indeling | bedrijfsinteractie | `kernobject` verplicht; voorleggen: ketensamenwerking (estafette) of orkestratie (de gemeente levert een dienst aan derden) |
| — | Aanvulling | `homoniem_van` ingevuld | voorleggen: naamkeuze; `## Homoniemen` bij beide; bij een GGM-homoniem een terugmelding |
| — | Aanvulling | Actor of Rol met *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt* | ook een bedrijfsobjectpagina (tegenhanger) |
| — | Aanvulling | *geautomatiseerd verwerkt* | annotatie `data_object: ja` |
| — | Signaal (controle) | Dienst zonder realiserend proces of functie met pagina; Gebeurtenis zonder gestart gedrag met pagina | waarschuwing: proces als kandidaat voorleggen |
| — | Signaal (controle) | Functie onder domeinniveau of dienst zonder (bovenliggende) functie, met meer (bovenliggende) functies, met een ander domein, of een functie buiten de GEMMA-functieketen; product onder een functie | waarschuwing: de (bovenliggende) functie wordt een element met een aggregatie naar de functie of de dienst; een functie met GEMMA type *Bedrijfsfunctie domein* en een product hangen via `domein` aan de domeingroepering |
| — | Signaal (controle) | Product of dienst waarvan het domein niet past bij de GEMMA-domeinen van zijn beleidsdomein; een beleidsdomein dat GEMMA niet kent met producten en diensten in meer domeinen | waarschuwing: domein of beleidsdomein herzien, of het verschil voorleggen als voorstel aan het GEMMA-team |
