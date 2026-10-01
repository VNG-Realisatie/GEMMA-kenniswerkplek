---
id: kenmerken
type: analyse
titel: Kenmerken per elementtype
bijgewerkt: '2026-10-01'
bronnen: [2026-vng-over-gemma]
---

# Kenmerken per elementtype

Deze analyse loopt voor elk elementtype de kenmerken na, na de besluiten van 30 september en 1 oktober 2026 ([GEMMA-kennismodel](gemma-kennismodel.md), [toegang tot een bedrijfsobject](gegevensrollen.md)). Ze toetst of de set compleet en kloppend is, en formuleert per kenmerk de vraag die bepaalt of het kenmerk op een begrip van toepassing is. De set is nog niet doorgevoerd in de beslistabel; dat gebeurt bij de herziening uit de todo van deze wiki.

## Besluiten van de redacteur

| Datum | Besluit |
|---|---|
| 2026-10-01 | De drempel van de dienst bevat geen *toegewezen partij*: kern *gerealiseerd door*, overig *afnemer* en *benoembaar resultaat*. De verantwoordelijke rol hangt aan het realiserende proces of de functie, zoals in GEMMA. |
| 2026-10-01 | De drempel van het product bevat geen *onderscheidbare exemplaren* maar *benoembaar resultaat* (de waarde voor de afnemer): kern *omvat diensten en afspraken*, overig *afnemer* en *benoembaar resultaat*. Een verleend exemplaar is een bedrijfsobject, geen product. |
| 2026-10-01 | Een concreet benoemde regeling als geheel die rijks- of EU-regelgeving of een VNG-modelverordening is, wordt beleidskader; de soort regeling is het bedrijfsobject Regeling; een gemeentelijke verordening blijft bron en wordt geen element; een los artikel valt buiten dit model. |
| 2026-10-01 | Het kenmerk "zelfstandig beleidsbegrip" heet voortaan *zelfstandige specialisatie*, met de vraag: is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt (eigen gegevens, regels of werkwijze)? |
| 2026-10-01 | Documentatie: de kenmerken als vragenlijst in volgorde van beoordelen en als naslagtabel per groep; de beslistabel als matrix kenmerk × type en als kaart per elementtype ("wanneer is iets een …?"). Beide worden gegenereerd uit dezelfde bron als de beslistabel; de stappentabel blijft in de criteria. |

## Hoe een vraag is opgebouwd

Elke vraag is met ja of nee te beantwoorden en gaat over het begrip zelf, niet over het vermoedelijke type. Waar de vraag "Noem …" zegt, hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; zonder zo'n verwijzing is het antwoord nee. Een kenmerk dat niet bij de aard van het begrip past (een gedragskenmerk bij een ding), is nee.

## Opbouw per type

| Type | Bepaald door | Kernrelatie (moet ja) | Overige drempel (hoogstens één nee) | Uitkomst daarnaast |
|---|---|---|---|---|
| Bedrijfsobject | geen aard; *afspraak* en *waarneembare vorm* nee | *wordt bewerkt* | *onderscheidbare exemplaren*, *levenscyclus* | annotatie data-object |
| Afspraak (Contract) | *afspraak* | *wordt bewerkt* | *onderscheidbare exemplaren*, *levenscyclus* | — |
| Product | *aanbod als geheel* | *omvat diensten en afspraken* | *afnemer*, *benoembaar resultaat* | — |
| Dienst | *gedrag* en *aangeboden gedrag* | *gerealiseerd door* | *afnemer*, *benoembaar resultaat* | — |
| Bedrijfsproces | *gedrag* en *per keer doorlopen* | *toegewezen partij* | *gebruikt objecten*, *aanleiding*, *benoembaar resultaat*, *komt herhaald voor*, *eigen normering* | *bijdrage aan groter proces* ja: procesniveau deelproces |
| Bedrijfsfunctie | *gedrag* en *gegroepeerd gedrag* | *toegewezen partij* | *gebruikt objecten*, *stabiel over tijd* | — |
| Gebeurtenis | *gedrag* en *toestandsverandering* | *leidt tot gedrag* | *komt herhaald voor* | — |
| Actor | *handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* (eventueel met *handelende partij*) met *eigen rechtspersoon* | *vervult een rol* | — | tegenhanger (bedrijfsobject) bij exemplaren, levenscyclus en bewerkt |
| Rol | *hoedanigheid* zonder *los van verantwoordelijkheid* | *voert gedrag uit* | — | idem |
| Bedrijfssamenwerking | *samenwerkingsverband* zonder *eigen rechtspersoon* | *voert gedrag uit* | — | — |
| Kanaal | *toegangspunt* | *ontsluit een dienst* | — | koppelen aan de centrale set |
| Beleidskader | *regeling als geheel* en *landelijk* | *is grondslag voor* | *in werking* | map motivatie |
| Business Interaction | *gedrag* en *gezamenlijk gedrag* | — | — | herkend, voorleggen |
| Representatie | *waarneembare vorm* | — | — | geen pagina; vermelden bij het object |
| Locatie | *plaats* | — | — | geen pagina |

Bij elk type met een paginatype gelden eerst de poorten en daarna het specialisatieniveau (*zelfstandige specialisatie*). Bij een type met hoogstens één overig drempelcriterium is de kernrelatie in feite de enige eis.

## Kenmerken en hun vraag

**Poort (alle typen).** Nee bij een van deze vragen (ja bij *buiten dit model* en *slechts eigenschap*) betekent: geen element van dit type.

| Kenmerk | Vraag | Ja | Nee |
|---|---|---|---|
| herkenbaar | Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning) | technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel) |
| gemeentelijk | Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD) | alleen context, of de interne zaak van een ketenpartner (behandelend arts) |
| buiten dit model | Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? Noem het ArchiMate-type. | armoedebestrijding (doel), "binnen acht weken beslissen" (norm uit één artikel) | bijstandsuitkering; Wet op de lijkbezorging (beleidskader) |
| slechts eigenschap | Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een doelgroep? Noem dat begrip. | bouwjaar (van Pand), minima (indeling van Inwoner) | Pand |
| eigen identiteit | Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? Noem bij nee dat begrip. | Beschikking; uitgifte van een graf | ondertekening van een besluit (deelstap) |
| betekenis in onderwerp | Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? Noem bij nee dat onderwerp. | Graf in lijkbezorging | akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand) |

**Specialisatieniveau (alle typen met een paginatype).** Dit kenmerk gaat over de "is een"-relatie tussen twee verschillende begrippen van hetzelfde type, nadat het type vaststaat. Het zegt niets over herkomst uit wet of beleid. Synoniemen (ander woord, zelfde betekenis) en homoniemen (zelfde woord, andere betekenis) zijn naamconflicten die vóór de beslistabel worden afgehandeld.

| Kenmerk | Vraag | Ja | Nee |
|---|---|---|---|
| zelfstandige specialisatie (was: zelfstandig beleidsbegrip) | Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. | Omgevingsvergunning naast Vergunning (eigen wet en procedure); Houder van het crematorium naast Houder van de begraafplaats (eigen plichten); Behandelen omgevingsvergunningaanvraag uitgebreid (eigen termijnen) | vergunning tot opgraving (variant van Vergunning); aanvrager van een vergunning tot opgraving (variant van Aanvrager) |

**Aard (precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen).** Bij *handelende partij* en *samenwerkingsverband* samen beslist *eigen rechtspersoon*: ja is actor, nee is bedrijfssamenwerking.

| Kenmerk | Vraag | Ja | Nee |
|---|---|---|---|
| gedrag | Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | aanvraag behandelen; verhuizing | aanvraag |
| handelende partij | Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | college van B&W; inwoner | aanvrager |
| hoedanigheid | Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | aanvrager; houder van de begraafplaats | gemeenteraad |
| samenwerkingsverband | Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? | Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten) | GGD-arts |
| toegangspunt | Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? | publieksbalie; gemeentelijke website | klantcontact |
| plaats | Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? | stadskantoor als vestigingsplaats | wijk (indeling) |
| aanbod als geheel | Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? | bewonersparkeervergunning zoals de productencatalogus haar aanbiedt | parkeren |
| regeling als geheel | Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort regeling? | Wet op de lijkbezorging; modelverordening participatie | "verordening" als soort (bedrijfsobject Regeling); artikel 16 (losse norm) |

**Partij.**

| Kenmerk | Vraag | Ja | Nee | Telt bij |
|---|---|---|---|---|
| los van verantwoordelijkheid | Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | kerkgenootschap; burgemeester | houder van de begraafplaats | actor (ja), rol (nee) |
| eigen rechtspersoon | Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | GGD (openbaar lichaam) | Zorg- en Veiligheidshuis | samenwerkingsverband: ja → actor, nee → bedrijfssamenwerking |
| vervult een rol | Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. | kerkgenootschap vervult Houder van de begraafplaats | partij die alleen genoemd wordt | kern actor |
| voert gedrag uit | Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. | Houder van de begraafplaats → Ruimen graf | rol zonder aanwijsbaar gedrag | kern rol, bedrijfssamenwerking |
| ontsluit een dienst | Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. | website → Melding openbare ruimte doen | kanaal zonder aanwijsbare dienst | kern kanaal |

**Soort gedrag (bij *gedrag* precies één ja).**

| Kenmerk | Vraag | Ja | Nee |
|---|---|---|---|
| per keer doorlopen | Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | aanvraag omgevingsvergunning behandelen | vergunningverlening |
| gegroepeerd gedrag | Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet "wat de gemeente kan"? | vergunningverlening; belastingheffing | aanslag opleggen |
| toestandsverandering | Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | verhuizing; aanvraag ontvangen; beslistermijn verstreken | verhuizing doorgeven |
| aangeboden gedrag | Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | melding openbare ruimte doen | melding afhandelen |
| gezamenlijk gedrag | Kan het alleen door twee of meer partijen samen worden uitgevoerd? | keukentafelgesprek; hoorzitting | beschikking opstellen |

**Gedrag (drempel; nee als het geen gedrag is).**

| Kenmerk | Vraag | Ja | Nee | Telt bij |
|---|---|---|---|---|
| toegewezen partij | Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. | Ruimen graf (Houder van de begraafplaats) | draagvlak creëren | kern proces, functie |
| gebruikt objecten | Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. | Inspraak (registreert zienswijze) | burgerberaad | proces, functie |
| aanleiding | Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. | overheidsparticipatie (verzoek ingediend) | kennisdeling | proces |
| benoembaar resultaat | Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. | opgraving (opgegraven lijk) | informeren | proces, dienst, product |
| komt herhaald voor | Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | inspraak (per ontwerpbesluit); overlijden | invoeren van de participatieverordening | proces, gebeurtenis |
| eigen normering | Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. | inspraak (afdeling 3.4 Awb) | burgerberaad (vormvrij) | proces |
| stabiel over tijd | Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? | participatie; belastingheffing | projectteam Omgevingswet | functie |
| afnemer | Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. | melding openbare ruimte doen (inwoner) | interne registratiestap | dienst, product |
| gerealiseerd door | Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. | Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt) | dienst zonder aanwijsbare uitvoering | kern dienst |
| leidt tot gedrag | Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. | Overlijden → Uitvoeren lijkbezorging | voorval zonder gemeentelijk gevolg | kern gebeurtenis |
| bijdrage aan groter proces | Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? Noem dat proces. | toetsen indieningsvereisten (in behandelen aanvraag) | behandelen aanvraag (levert het besluit zelf) | proces: ja → procesniveau deelproces |

**Passief.**

| Kenmerk | Vraag | Ja | Nee | Telt bij |
|---|---|---|---|---|
| onderscheidbare exemplaren | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | aanvraag (elke aanvraag apart) | gemeentefonds (er is er één) | bedrijfsobject, afspraak |
| levenscyclus | Ontstaan, veranderen en eindigen de exemplaren? | vergunning (verleend, gewijzigd, ingetrokken) | kadastrale gemeentecode | bedrijfsobject, afspraak |
| wordt bewerkt | Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. | aanvraag (geregistreerd, beoordeeld) | preventieakkoord (alleen beleidsmatig) | kern bedrijfsobject, afspraak |
| afspraak | Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? | subsidieovereenkomst; uitvoeringsovereenkomst | subsidiebeschikking; verordening | type afspraak |
| waarneembare vorm | Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. | aanslagbiljet (van Aanslag); register van begraven lijken | aanslag | geen pagina |
| omvat diensten en afspraken | Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. | parkeervergunning (dienst parkeren, voorwaarden) | losse dienst | kern product |
| geautomatiseerd verwerkt | Wordt het als gegevensstructuur geautomatiseerd verwerkt? | zaak in het zaaksysteem | keukentafelgesprek | annotatie data-object |

**Beleidskader.**

| Kenmerk | Vraag | Ja | Nee | Telt bij |
|---|---|---|---|---|
| landelijk | Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen regeling van één gemeente? | Wet op de lijkbezorging; AVG; modelverordening | beheersverordening van één gemeente (blijft bron) | type beleidskader |
| in werking | Is de regeling geldend recht, of als modelverordening actueel? | Archiefwet 1995 | ingetrokken wet | beleidskader |
| is grondslag voor | Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar proces, dienst of product? Noem het artikel en het gedrag. | Wet op de lijkbezorging art. 28 → Verlenen grafrecht | BW boek 2, gebruikt voor één definitie | kern beleidskader |

Samen 46 kenmerken: 6 poorten, 1 voor het specialisatieniveau, 8 voor de aard, 5 voor de partij, 5 voor de soort gedrag, 11 voor gedrag, 7 passief en 3 voor het beleidskader.

## Bevindingen

**Volgt uit de besluiten, nu verwerkt in de vragen:**

- *buiten kernlagen* heet nu *buiten dit model* en sluit het beleidskader uit; anders zou elk beleidskader in stap 1 al buiten het model vallen.
- De kernrelatie van een actor is *vervult een rol* (actor alleen via een rol). *voert gedrag uit* geldt voor rol en bedrijfssamenwerking; een kanaal heeft een eigen kernrelatie *ontsluit een dienst*, omdat het kanaal aan een dienst is toegewezen en niet aan een proces.
- *eigen rechtspersoon* maakt de scheidslijn tussen actor en bedrijfssamenwerking toetsbaar (GGD wel, Zorg- en Veiligheidshuis niet).
- *bijdrage aan groter proces* maakt het procesniveau toetsbaar, met de GEMMA-definitie van deelproces: binnen één organisatorische eenheid, als bijdrage aan een dienst (Over GEMMA, regel 388). Een processtap of handeling is *eigen identiteit* nee.
- *gebruikt objecten* en *wordt bewerkt* vragen nu naar de handelingen uit de vaste reeks.
- *regeling als geheel* is nodig als aard voor het beleidskader; het onderscheidt een concreet benoemde regeling (beleidskader) van de soort regeling (bedrijfsobject Regeling) en van een los artikel (buiten dit model).
- *toestandsverandering* volgt de GEMMA-definitie van gebeurtenis ("gevolgen heeft", regel 874) en houdt het ogenblikkelijke karakter.
- *afspraak* volgt de GEMMA-definitie: "meerdere partijen" in plaats van "tweezijdig" (regel 246).

**Correcties (besloten 2026-10-01):**

- **Dienst zonder toegewezen partij.** In het GEMMA-kennismodel wordt geen rol aan een dienst toegewezen; de dienst wordt gerealiseerd door een proces of functie, en daaraan hangt de rol (regel 925, 918). *toegewezen partij* in de drempel van de dienst is dan dubbel met *gerealiseerd door*. Voorstel: weglaten, en *benoembaar resultaat* (wat de afnemer krijgt) houden.
- **Product zonder onderscheidbare exemplaren.** Een product is een aanbod, geen exemplaar: de verleende parkeervergunningen zijn exemplaren van het bedrijfsobject Vergunning, niet van het product. Voorstel: *onderscheidbare exemplaren* weglaten bij product, en *benoembaar resultaat* opnemen, omdat GEMMA een product definieert als aanbod "met waarde voor die afnemer" (regel 76).
- **Beleidskader of bedrijfsobject Regeling.** *regeling als geheel* zegt: een concreet benoemde regeling wordt beleidskader, de soort blijft het object Regeling. Een gemeentelijke verordening (niet landelijk) is dan nee bij *landelijk* en wordt geen element; zij blijft bron, en het begrip "verordening" valt onder Regeling.
- **Naam van het specialisatiekenmerk.** "Zelfstandig beleidsbegrip" wekte de indruk dat het over herkomst uit beleid of wet gaat, of dat het een type bepaalt. Het gaat over de "is een"-relatie: besloten is de naam *zelfstandige specialisatie*.

**Gecontroleerd en in orde:**

- Elk type met een paginatype heeft precies één typebepalend kenmerk (of een vaste combinatie), één kernrelatie en een specialisatietoets.
- Elk kenmerk telt bij minstens één type; er is geen kenmerk zonder functie.
- De consistentieregels (gedrags-, partij- en passieve kenmerken alleen bij de passende aard) blijven nodig en dekken de nieuwe kenmerken: *eigen rechtspersoon*, *vervult een rol* en *ontsluit een dienst* zijn partijkenmerken, *bijdrage aan groter proces* is een gedragskenmerk, de drie beleidskaderkenmerken horen alleen bij *regeling als geheel*.
- Twee extra controles volgen uit de set: *eigen normering* ja bij een proces hoort samen te gaan met een beleidskader dat er *grondslag voor* is; en de verantwoordelijkheid van een rol hoort te passen bij de handeling van het gedrag waaraan zij is toegewezen.

## Open vragen

Geen; de vragen van 1 oktober 2026 zijn beantwoord (zie de besluiten bovenaan).
