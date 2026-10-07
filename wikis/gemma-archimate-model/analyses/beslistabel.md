---
id: beslistabel
type: analyse
titel: Kenmerken en beslistabel
bijgewerkt: '2026-10-07'
bronnen: [2026-vng-over-gemma]
---

# Kenmerken en beslistabel

Deze pagina documenteert hoe deze wiki bepaalt of een begrip een element van het GEMMA-architectuurmodel is, en van welk type. Elk begrip uit een bron krijgt één keer dezelfde vragen: de kenmerken. De beslistabel past daar vaste regels op toe; de uitkomst is het type, of de reden waarom het begrip geen eigen pagina krijgt. Er wordt nooit eerst een type gekozen om daarna te toetsen of het klopt.

De namen en definities van de typen volgen het GEMMA-kennismodel ([GEMMA-kennismodel](gemma-kennismodel.md)). De keuzes achter de kenmerken staan in [kenmerken per elementtype](kenmerken.md), [toegang tot een bedrijfsobject](gegevensrollen.md) en [synoniemen en homoniemen](synoniemen-en-homoniemen.md). Criteria van 1 oktober 2026.

Alles hieronder is gegenereerd uit dezelfde bron als de beslistabel zelf; wijzigingen gaan via de beslistabel, niet via deze pagina.

<!-- BEGIN gegenereerd uit de beslistabel; niet met de hand bewerken -->
### Stap 0: welk begrip?

Vóór de kenmerken: bepaal welk begrip bedoeld is. Synoniemen en homoniemen zijn geen kenmerken van een begrip, maar verhoudingen tussen een woord en een begrip.

| Veld | Vraag | Uitkomst |
|---|---|---|
| `synoniem_van` | Is dit een ander woord voor een begrip dat al een element is, of in deze run wordt beoordeeld? Noem dat element en de context van het woord. | synoniem: geen pagina; het woord naar de synoniemen van het element |
| `homoniem_van` | Bestaat dezelfde naam al voor een ander begrip, in de wiki, het GGM, het GEMMA-model of een bron? Noem dat begrip en waar het voorkomt. | door naar de kenmerken; naamkeuze voorleggen |

### Kenmerken: vragenlijst in volgorde van beoordelen

Beantwoord alle vragen, ook die niet bij de aard van het begrip passen (dan nee). Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; zonder zo'n verwijzing is het antwoord nee.

**Poort.** Altijd.

1. Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? (*herkenbaar*)
2. Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? (*gemeentelijk*)
3. Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? Noem het ArchiMate-type. (*buiten dit model*)
4. Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een doelgroep? Noem dat begrip. (*slechts eigenschap*)
5. Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? Noem bij nee dat begrip. (*eigen identiteit*)
6. Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? Noem bij nee het onderwerp waar het thuishoort. (*betekenis in onderwerp*)

**Aard.** Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.

7. Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? (*gedrag*)
8. Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? (*handelende partij*)
9. Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? (*hoedanigheid*)
10. Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? (*samenwerkingsverband*)
11. Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? (*toegangspunt*)
12. Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? (*plaats*)
13. Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? (*aanbod als geheel*)
14. Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort regeling? (*regeling als geheel*)

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*; *soort partij* bij *handelende partij* en *samenwerkingsverband*.

15. Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? (*los van verantwoordelijkheid*)
16. Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? (*eigen rechtspersoon*)
17. Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. (*vervult een rol*)
18. Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. (*voert gedrag uit*)
19. Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. (*soort partij*)
20. Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. (*ontsluit een dienst*)

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

21. Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? (*per keer doorlopen*)
22. Is het een groepering van processen rond één taak of één soort werk, die niet per geval wordt doorlopen? (*groepeert processen*)
23. Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? (*gegroepeerd gedrag*)
24. Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? (*toestandsverandering*)
25. Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? (*aangeboden gedrag*)
26. Kan het alleen door twee of meer partijen samen worden uitgevoerd? (*gezamenlijk gedrag*)

**Gedrag.** Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.

27. Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. (*toegewezen partij*)
28. Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. (*gebruikt objecten*)
29. Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. (*aanleiding*)
30. Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. (*benoembaar resultaat*)
31. Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? (*komt herhaald voor*)
32. Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. (*eigen normering*)
33. Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? (*stabiel over tijd*)
34. Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. (*afnemer*)
35. Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. (*gerealiseerd door*)
36. Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. (*leidt tot gedrag*)
37. Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? Noem dat proces. (*bijdrage aan groter proces*)
38. Omvat het minstens twee processen (bij een taak: de processen per kernobject; bij een cluster naar soort werk: de deelprocessen)? Noem ze. (*omvat processen*)
39. Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of binnen een ketenproces het deel van die levensloop dat één partij uitvoert? Noem het object. (*omvat levensloop*)
40. Voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol en niet als klant of alleen als adviseur? Noem ze. (*meer organisaties*)
41. Eindigt het in een besluit van een bevoegd orgaan of een mandataris? Noem orgaan en artikel. (*eigen besluit*)
42. Realiseert het een dienst of levert het een product aan een afnemer? Noem het (referentie: de UPL). (*levert aanbod*)
43. Ondersteunt de functie aanwijsbaar een proces? Noem het. (*bedient gedrag*)
44. Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? Noem de bovenliggende functie of het domein. (*in functie-indeling*)
45. Eindigt het in een toestandsverandering die domeinexperts benoemen, of die een ander proces start? Noem die. (*leidt tot gebeurtenis*)

**Passief.** Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en *geautomatiseerd verwerkt* bij elk begrip; *deel van object* en *invoer van een ander* bij een ding; *omvat diensten en afspraken* en *zelfstandig aanbod* bij *aanbod als geheel*.

46. Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? (*onderscheidbare exemplaren*)
47. Ontstaan, veranderen en eindigen de exemplaren? (*levenscyclus*)
48. Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. (*wordt bewerkt*)
49. Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? (*afspraak*)
50. Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. (*waarneembare vorm*)
51. Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? Noem dat object. (*deel van object*)
52. Maakt en beheert een andere partij het, terwijl de gemeente het alleen ontvangt of raadpleegt? Noem de maker. (*invoer van een ander*)
53. Wordt het onder een eigen naam aangeboden, en niet als variant of tarief van een ander product? (*zelfstandig aanbod*)
54. Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. (*omvat diensten en afspraken*)
55. Wordt het als gegevensstructuur geautomatiseerd verwerkt? (*geautomatiseerd verwerkt*)

**Beleidskader.** Alleen bij *regeling als geheel*.

56. Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen regeling van één gemeente? (*landelijk*)
57. Is de regeling geldend recht, of als modelverordening actueel? (*in werking*)
58. Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar proces, dienst of product? Noem het artikel en het gedrag. (*is grondslag voor*)

**Specialisatie.** Altijd, als het type een pagina heeft.

59. Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. (*zelfstandige specialisatie*)
60. Komt het met dezelfde betekenis in veel onderwerpen voor? (*generiek*)

### Kenmerken: naslag per groep

**Poort.** Altijd.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja: het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning). Nee: technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel). Herkomst: ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts). |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja: de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD; behandelende arts via de overlegplicht met de lijkschouwer). Nee: alleen context (gedeputeerde staten als beroepsinstantie), of de interne zaak van een ketenpartner (de medische behandeling door de arts). Herkomst: GEMMA (gemeentelijk perspectief). |
| **buiten dit model**: Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? Noem het ArchiMate-type. | Ja: armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel). Nee: bijstandsuitkering; Wet op de lijkbezorging (beleidskader). Herkomst: ArchiMate (motivatie-, strategie- en overige lagen). |
| **slechts eigenschap**: Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een doelgroep? Noem dat begrip. | Ja: bouwjaar (van Pand); minima (indeling van Inwoner). Nee: Pand. Herkomst: GEMMA (negatieve toets: eigenschap, status, classificatie). |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? Noem bij nee dat begrip. | Ja: Beschikking; uitgifte van een graf. Nee: ondertekening van een besluit (deelstap). Herkomst: GEMMA (eigen bestaan; procesarchitectuur: processtap, handeling). |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? Noem bij nee het onderwerp waar het thuishoort. | Ja: Graf in lijkbezorging. Nee: akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand). Herkomst: GEMMA (betekenis binnen het onderwerp). |

**Aard.** Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja: aanvraag behandelen; verhuizing. Nee: aanvraag. Herkomst: ArchiMate (gedragselement). |
| **handelende partij**: Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | Ja: college van B&W; inwoner. Nee: aanvrager. Herkomst: GEMMA (definitie Actor). |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja: aanvrager; houder van de begraafplaats. Nee: gemeenteraad. Herkomst: ArchiMate (definitie Rol). |
| **samenwerkingsverband**: Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? | Ja: Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten). Nee: GGD-arts. Herkomst: ArchiMate (definitie Bedrijfssamenwerking). |
| **toegangspunt**: Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? | Ja: publieksbalie; gemeentelijke website. Nee: klantcontact. Herkomst: NORA (definitie Kanaal). |
| **plaats**: Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? | Ja: stadskantoor als vestigingsplaats. Nee: wijk (indeling). Herkomst: ArchiMate (Location). |
| **aanbod als geheel**: Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? | Ja: bewonersparkeervergunning zoals de productencatalogus haar aanbiedt. Nee: parkeren. Herkomst: GEMMA (definitie Product). |
| **regeling als geheel**: Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort regeling? | Ja: Wet op de lijkbezorging; modelverordening participatie. Nee: 'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm). Herkomst: GEMMA (definitie Beleidskader). |

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*; *soort partij* bij *handelende partij* en *samenwerkingsverband*.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja: kerkgenootschap; burgemeester. Nee: houder van de begraafplaats. Herkomst: ArchiMate (actor tegenover rol). |
| **eigen rechtspersoon**: Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | Ja: GGD (openbaar lichaam). Nee: Zorg- en Veiligheidshuis. Herkomst: besluit redacteur 2026-10-01 (scheidslijn actor en bedrijfssamenwerking). |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. | Ja: kerkgenootschap vervult Houder van de begraafplaats. Nee: partij die alleen genoemd wordt. Herkomst: GEMMA (actor wordt toegewezen aan rol). |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. | Ja: Houder van de begraafplaats → Ruimen graf. Nee: rol zonder aanwijsbaar gedrag. Herkomst: GEMMA (rol wordt toegewezen aan functie); besluit redacteur 2026-10-01 (ook aan proces). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja: Gemeente; College van B&W; Kerkgenootschap; Rijk, Provincie en Waterschap (de bestuurslaag als geheel, ook al is er maar één Rijk). Nee: gemeente Utrecht, provincie Utrecht (één exemplaar, niet elke gemeente heeft ermee te maken); een afzonderlijk ministerie of rijksdienst (minister van BZK, IND) is geen eigen actor maar staat in de beschrijving van Rijk. Herkomst: GEMMA (referentiemodel voor alle gemeenten); besluit redacteur 2026-10-07 (Rijk). |
| **ontsluit een dienst**: Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. | Ja: website → Melding openbare ruimte doen. Nee: kanaal zonder aanwijsbare dienst. Herkomst: GEMMA (kanaal wordt toegewezen aan dienst). |

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja: aanvraag omgevingsvergunning behandelen. Nee: vergunningverlening. Herkomst: GEMMA (definitie Bedrijfsproces). |
| **groepeert processen**: Is het een groepering van processen rond één taak of één soort werk, die niet per geval wordt doorlopen? | Ja: Verzorgen lijkbezorging (taak); Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk). Nee: Beheren grafrechten (loopt per grafrecht van begin tot eind door). Herkomst: GEMMA (definitie Procescluster, regel 409 en 419-420). |
| **gegroepeerd gedrag**: Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? | Ja: vergunningverlening; belastingheffing. Nee: aanslag opleggen. Herkomst: GEMMA (definitie Bedrijfsfunctie). |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja: verhuizing; aanvraag ontvangen; beslistermijn verstreken. Nee: verhuizing doorgeven. Herkomst: GEMMA (definitie Gebeurtenis). |
| **aangeboden gedrag**: Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | Ja: melding openbare ruimte doen. Nee: melding afhandelen. Herkomst: NORA (definitie Dienst). |
| **gezamenlijk gedrag**: Kan het alleen door twee of meer partijen samen worden uitgevoerd? | Ja: keukentafelgesprek; hoorzitting. Nee: beschikking opstellen. Herkomst: ArchiMate (Business Interaction). |

**Gedrag.** Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. | Ja: Ruimen graf (Houder van de begraafplaats). Nee: draagvlak creëren. Herkomst: ArchiMate (toewijzing van rol aan gedrag). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. | Ja: Inspraak (registreert zienswijze). Nee: burgerberaad. Herkomst: ArchiMate (toegang van gedrag tot object); besluit redacteur 2026-10-01 (handelingen). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. | Ja: overheidsparticipatie (verzoek ingediend). Nee: kennisdeling. Herkomst: ArchiMate (triggering); GEMMA (procesarchitectuur). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. | Ja: opgraving (opgegraven lijk). Nee: informeren. Herkomst: GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer). |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja: inspraak (per ontwerpbesluit); overlijden. Nee: invoeren van de participatieverordening. Herkomst: GEMMA (proces als herhaalbare werkwijze). |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. | Ja: inspraak (afdeling 3.4 Awb). Nee: burgerberaad (vormvrij). Herkomst: GEMMA (proces met eigen spelregels). |
| **stabiel over tijd**: Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? | Ja: participatie; belastingheffing. Nee: projectteam Omgevingswet. Herkomst: ArchiMate en GEMMA (bedrijfsfunctiemodel). |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. | Ja: melding openbare ruimte doen (inwoner). Nee: interne registratiestap. Herkomst: NORA (definitie Dienst); GEMMA (definitie Product, rol Klant). |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. | Ja: Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt). Nee: dienst zonder aanwijsbare uitvoering. Herkomst: GEMMA (proces en functie realiseren dienst). |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. | Ja: Overlijden → Uitvoeren lijkbezorging. Nee: voorval zonder gemeentelijk gevolg. Herkomst: GEMMA (gebeurtenis triggert proces). |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? Noem dat proces. | Ja: toetsen indieningsvereisten (in behandelen aanvraag). Nee: behandelen aanvraag (levert het besluit zelf). Herkomst: GEMMA (definitie Deelproces). |
| **omvat processen**: Omvat het minstens twee processen (bij een taak: de processen per kernobject; bij een cluster naar soort werk: de deelprocessen)? Noem ze. | Ja: Verzorgen lijkbezorging (Bezorgen lijken, Beheren grafrechten, Beheren graven). Nee: een proces met één stap. Herkomst: GEMMA (procescluster aggregeert bedrijfsprocessen, regel 419-420). |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of binnen een ketenproces het deel van die levensloop dat één partij uitvoert? Noem het object. | Ja: Beheren grafrechten (Grafrecht: van uitgifte tot verval); Toestaan lijkbezorging (het deel van de gemeente als overheid in de levensloop van het stoffelijk overschot). Nee: Verlenen grafrecht (één mutatie in die levensloop). Herkomst: GEMMA (definitie Bedrijfsproces; procesbouwstenen); lezing redacteur 2026-10-07. |
| **meer organisaties**: Voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol en niet als klant of alleen als adviseur? Noem ze. | Ja: Bezorgen lijken (gemeente, arts, officier van justitie, uitvaartondernemer). Nee: Treffen maatregel bij besmet lijk (de GGD adviseert alleen). Herkomst: GEMMA (definitie Ketenproces, regel 564). |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? Noem orgaan en artikel. | Ja: Verlenen grafrecht (college, Wlb art. 28). Nee: Onderhouden graf (feitelijk handelen). Herkomst: GEMMA (procesbouwstenen: besluiten). |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? Noem het (referentie: de UPL). | Ja: Onderhouden graf (grafonderhoud). Nee: interne registratiestap. Herkomst: GEMMA (Product en dienst procesarchitectuur, UPL). |
| **bedient gedrag**: Ondersteunt de functie aanwijsbaar een proces? Noem het. | Ja: Exploiteren van begraafplaatsen bedient Ruimen graf. Nee: functie zonder aanwijsbaar proces. Herkomst: GEMMA (functie bedient proces, regel 597 en 604). |
| **in functie-indeling**: Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? Noem de bovenliggende functie of het domein. | Ja: Exploiteren van begraafplaatsen (onder Exploitatie fysieke leefomgeving). Nee: Lijkbezorging als functie. Herkomst: GEMMA (Functie-indeling naar domein). |
| **leidt tot gebeurtenis**: Eindigt het in een toestandsverandering die domeinexperts benoemen, of die een ander proces start? Noem die. | Ja: Vervallen verklaren grafrecht → Verval van het grafrecht. Nee: een tussenstap zonder eigen uitkomst. Herkomst: GEMMA (proces triggert gebeurtenis, regel 924). |

**Passief.** Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en *geautomatiseerd verwerkt* bij elk begrip; *deel van object* en *invoer van een ander* bij een ding; *omvat diensten en afspraken* en *zelfstandig aanbod* bij *aanbod als geheel*.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja: aanvraag (elke aanvraag apart). Nee: gemeentefonds (er is er één). Herkomst: GEMMA (kan in meervoud bestaan). |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja: vergunning (verleend, gewijzigd, ingetrokken). Nee: kadastrale gemeentecode. Herkomst: GEMMA (eigen levenscyclus). |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. | Ja: aanvraag (geregistreerd, beoordeeld). Nee: preventieakkoord (alleen beleidsmatig). Herkomst: GEMMA (proces en functie benaderen bedrijfsobject). |
| **afspraak**: Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? | Ja: subsidieovereenkomst; uitvoeringsovereenkomst. Nee: subsidiebeschikking; verordening. Herkomst: GEMMA (definitie Afspraak). |
| **waarneembare vorm**: Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. | Ja: aanslagbiljet (van Aanslag); register van begraven lijken. Nee: aanslag. Herkomst: ArchiMate (Representation). |
| **deel van object**: Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? Noem dat object. | Ja: grafbedekking (van Graf). Nee: Graf. Herkomst: GEMMA (negatieve toets: eigen identiteit). |
| **invoer van een ander**: Maakt en beheert een andere partij het, terwijl de gemeente het alleen ontvangt of raadpleegt? Noem de maker. | Ja: verklaring van overlijden (de arts of lijkschouwer). Nee: vergunning (de gemeente verleent haar). Herkomst: wiki (abstractieniveau). |
| **zelfstandig aanbod**: Wordt het onder een eigen naam aangeboden, en niet als variant of tarief van een ander product? | Ja: bewonersparkeervergunning. Nee: bezoekersparkeervergunning als tarief van parkeervergunning. Herkomst: UPL (één product per productnaam). |
| **omvat diensten en afspraken**: Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. | Ja: parkeervergunning (dienst parkeren, voorwaarden). Nee: losse dienst. Herkomst: GEMMA (product bundelt dienst en afspraak). |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja: zaak in het zaaksysteem. Nee: keukentafelgesprek. Herkomst: GEMMA (definitie Data-object). |

**Beleidskader.** Alleen bij *regeling als geheel*.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **landelijk**: Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen regeling van één gemeente? | Ja: Wet op de lijkbezorging; AVG; modelverordening. Nee: beheersverordening van één gemeente (blijft bron). Herkomst: besluit redacteur 2026-10-01. |
| **in werking**: Is de regeling geldend recht, of als modelverordening actueel? | Ja: Archiefwet 1995. Nee: ingetrokken wet. Herkomst: besluit redacteur 2026-10-01. |
| **is grondslag voor**: Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar proces, dienst of product? Noem het artikel en het gedrag. | Ja: Wet op de lijkbezorging art. 28 → Verlenen grafrecht. Nee: BW boek 2, gebruikt voor één definitie. Herkomst: GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader). |

**Specialisatie.** Altijd, als het type een pagina heeft.

| Kenmerk | Voorbeelden en herkomst |
|---|---|
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. | Ja: Omgevingsvergunning naast Vergunning (eigen wet en procedure); Houder van het crematorium naast Houder van de begraafplaats (eigen plichten). Nee: vergunning tot opgraving (variant van Vergunning); aanvrager van een vergunning tot opgraving (variant van Aanvrager). Herkomst: GEMMA (zelfstandig ding waar beleid op gemaakt wordt; specialisatie). |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja: Besluit; Beschikking; aanvraag ontvangen; Klant. Nee: Graf; Ruimen graf. Herkomst: wiki (abstractieniveau; GEMMA generieke elementen). |

### Beslistabel per elementtype

Voor elk type gelden eerst stap 0 en de poorten, daarna de toets op *zelfstandige specialisatie*. Van de overige drempelcriteria mag er hoogstens 1 nee zijn.

**Wanneer is iets een bedrijfsobject?**

- Type volgt uit: geen aard (een ding); *afspraak* en *waarneembare vorm* nee.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*); ja: subobject bij een eigen deelproces, anders onderdeel zonder pagina (*deel van object*); ja: onderdeel, geen pagina (*invoer van een ander*).
- Indeling: Beleidsdomeinindeling.
- Voorbeeld: Graf; Aanvraag; Vergunning.

**Wanneer is iets een afspraak?**

- Type volgt uit: *afspraak*.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*); ja: subobject bij een eigen deelproces, anders onderdeel zonder pagina (*deel van object*); ja: onderdeel, geen pagina (*invoer van een ander*).
- Indeling: Beleidsdomeinindeling.
- Voorbeeld: Uitvoeringsovereenkomst; Grafrecht.

**Wanneer is iets een product?**

- Type volgt uit: *aanbod als geheel*.
- Moet ja zijn: *omvat diensten en afspraken* en *zelfstandig aanbod*.
- Hoogstens één nee: *afnemer*, *benoembaar resultaat*.
- Indeling: Beleidsdomeinindeling en Functie-indeling naar domein.
- Voorbeeld: bewonersparkeervergunning in de productencatalogus.

**Wanneer is iets een dienst?**

- Type volgt uit: *gedrag* en *aangeboden gedrag*.
- Moet ja zijn: *gerealiseerd door*.
- Hoogstens één nee: *afnemer*, *benoembaar resultaat*.
- Indeling: Beleidsdomeinindeling en Functie-indeling naar domein.
- Voorbeeld: Onderhoud van graven.

**Wanneer is iets een bedrijfsproces?**

- Type volgt uit: *gedrag* en *per keer doorlopen*.
- Moet ja zijn: *toegewezen partij* en *aanleiding* en *benoembaar resultaat*.
- Daarna: ja: procesniveau bedrijfsproces, of ketenproces bij *meer organisaties* (*omvat levensloop*); ja: procesniveau deelproces, bij *eigen besluit*, *eigen normering* of *levert aanbod*; anders processtap zonder pagina (*bijdrage aan groter proces*); levert een product of dienst: nooit een processtap (*levert aanbod*); ja: ketenproces (*meer organisaties*); telt voor het deelproces (*eigen besluit*); telt voor het deelproces (*eigen normering*); annotatie (*gebruikt objecten*); annotatie (*komt herhaald voor*); triggering naar een gebeurtenis (*leidt tot gebeurtenis*).
- Indeling: Procesindeling naar taak en naar soort werk.
- Voorbeeld: Beheren grafrechten; Verlenen grafrecht (deelproces).

**Wanneer is iets een procescluster?**

- Type volgt uit: *gedrag* en *groepeert processen*.
- Moet ja zijn: *omvat processen*.
- Indeling: Procesindeling naar taak en naar soort werk.
- Voorbeeld: Verzorgen lijkbezorging (taak); Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk).

**Wanneer is iets een bedrijfsfunctie?**

- Type volgt uit: *gedrag* en *gegroepeerd gedrag*.
- Moet ja zijn: *bedient gedrag*.
- Hoogstens één nee: *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd*, *in functie-indeling*.
- Indeling: Functie-indeling naar domein.
- Voorbeeld: Exploiteren van begraafplaatsen; Burgerlijke stand diensten.

**Wanneer is iets een gebeurtenis?**

- Type volgt uit: *gedrag* en *toestandsverandering*.
- Moet ja zijn: *leidt tot gedrag*.
- Hoogstens één nee: *komt herhaald voor*.
- Indeling: Procesindeling naar taak.
- Voorbeeld: Overlijden; Verval van het grafrecht.

**Wanneer is iets een actor?**

- Type volgt uit: *handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*.
- Moet ja zijn: *vervult een rol* en *soort partij*.
- Daarna: tegenhanger bij *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*.
- Indeling: Doelgroepindeling.
- Voorbeeld: College van B&W; Kerkgenootschap; GGD.

**Wanneer is iets een rol?**

- Type volgt uit: *hoedanigheid*, niet *los van verantwoordelijkheid*.
- Moet ja zijn: *voert gedrag uit*.
- Daarna: tegenhanger bij *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*.
- Indeling: Doelgroepindeling.
- Voorbeeld: Houder van de begraafplaats; Rechthebbende op het graf.

**Wanneer is iets een bedrijfssamenwerking?**

- Type volgt uit: *samenwerkingsverband* zonder *eigen rechtspersoon*.
- Moet ja zijn: *voert gedrag uit* en *soort partij*.
- Indeling: Doelgroepindeling.
- Voorbeeld: Zorg- en Veiligheidshuis.

**Wanneer is iets een kanaal?**

- Type volgt uit: *toegangspunt*.
- Moet ja zijn: *ontsluit een dienst*.
- Kanalen vormen één centrale set: koppelen aan een bestaand kanaal; een nieuw kanaal alleen na besluit van de redacteur.
- Indeling: Doelgroepindeling.
- Voorbeeld: publieksbalie; gemeentelijke website (centrale set).

**Wanneer is iets een beleidskader?**

- Type volgt uit: *regeling als geheel* en *landelijk*.
- Moet ja zijn: *is grondslag voor*.
- Hoogstens één nee: *in werking*.
- Indeling: Beleidsdomeinindeling.
- Voorbeeld: Wet op de lijkbezorging; Archiefwet; AVG.

**Wanneer is iets een interaction?** (herkend)

- Type volgt uit: *gedrag* en *gezamenlijk gedrag*.
- Voorbeeld: keukentafelgesprek (voorleggen).

**Wanneer is iets een representatie?** (geen pagina)

- Type volgt uit: *waarneembare vorm*.
- Voorbeeld: register van begraven lijken (vermelden bij Graf).

**Wanneer is iets een locatie?** (geen pagina)

- Type volgt uit: *plaats*.
- Voorbeeld: stadskantoor als vestigingsplaats.

### Beslistabel vanuit de kenmerken

Per kenmerk: bij welke typen het telt, en hoe. **T** bepaalt het type · **x** moet nee zijn voor dit type · **K** kernrelatie: moet ja zijn · **D** telt in de drempel (hoogstens één nee) · **P** poort: geldt voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger, procesniveau, objectniveau, annotatie) · **E** eis: moet ja zijn naast de kernrelatie.

Typen: Obj = Bedrijfsobject · Afspr = Afspraak · Prod = Product · Dienst = Dienst · Proc = Bedrijfsproces · Clus = Procescluster · Func = Bedrijfsfunctie · Gebt = Gebeurtenis · Actor = Actor · Rol = Rol · Samw = Bedrijfssamenwerking · Kan = Kanaal · Bkad = Beleidskader · Inter = Interaction (herkend) · Repr = Representatie (geen pagina) · Loc = Locatie (geen pagina).

| Kenmerk | Obj | Afspr | Prod | Dienst | Proc | Clus | Func | Gebt | Actor | Rol | Samw | Kan | Bkad | Inter | Repr | Loc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Poort** | | | | | | | | | | | | | | | | |
| herkenbaar | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| gemeentelijk | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| buiten dit model | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| slechts eigenschap | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| eigen identiteit | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| betekenis in onderwerp | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| **Aard** | | | | | | | | | | | | | | | | |
| gedrag |  |  |  | T | T | T | T | T |  |  |  |  |  | T |  |  |
| handelende partij |  |  |  |  |  |  |  |  | T |  |  |  |  |  |  |  |
| hoedanigheid |  |  |  |  |  |  |  |  |  | T |  |  |  |  |  |  |
| samenwerkingsverband |  |  |  |  |  |  |  |  | T |  | T |  |  |  |  |  |
| toegangspunt |  |  |  |  |  |  |  |  |  |  |  | T |  |  |  |  |
| plaats |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T |
| aanbod als geheel |  |  | T |  |  |  |  |  |  |  |  |  |  |  |  |  |
| regeling als geheel |  |  |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| **Partij** | | | | | | | | | | | | | | | | |
| los van verantwoordelijkheid |  |  |  |  |  |  |  |  | T | x |  |  |  |  |  |  |
| eigen rechtspersoon |  |  |  |  |  |  |  |  | T |  | x |  |  |  |  |  |
| vervult een rol |  |  |  |  |  |  |  |  | K |  |  |  |  |  |  |  |
| voert gedrag uit |  |  |  |  |  |  |  |  |  | K | K |  |  |  |  |  |
| soort partij |  |  |  |  |  |  |  |  | E |  | E |  |  |  |  |  |
| ontsluit een dienst |  |  |  |  |  |  |  |  |  |  |  | K |  |  |  |  |
| **Soort gedrag** | | | | | | | | | | | | | | | | |
| per keer doorlopen |  |  |  |  | T |  |  |  |  |  |  |  |  |  |  |  |
| groepeert processen |  |  |  |  |  | T |  |  |  |  |  |  |  |  |  |  |
| gegroepeerd gedrag |  |  |  |  |  |  | T |  |  |  |  |  |  |  |  |  |
| toestandsverandering |  |  |  |  |  |  |  | T |  |  |  |  |  |  |  |  |
| aangeboden gedrag |  |  |  | T |  |  |  |  |  |  |  |  |  |  |  |  |
| gezamenlijk gedrag |  |  |  |  |  |  |  |  |  |  |  |  |  | T |  |  |
| **Gedrag** | | | | | | | | | | | | | | | | |
| toegewezen partij |  |  |  |  | K |  | D |  |  |  |  |  |  |  |  |  |
| gebruikt objecten |  |  |  |  | A |  | D |  |  |  |  |  |  |  |  |  |
| aanleiding |  |  |  |  | E |  |  |  |  |  |  |  |  |  |  |  |
| benoembaar resultaat |  |  | D | D | E |  |  |  |  |  |  |  |  |  |  |  |
| komt herhaald voor |  |  |  |  | A |  |  | D |  |  |  |  |  |  |  |  |
| eigen normering |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| afnemer |  |  | D | D |  |  |  |  |  |  |  |  |  |  |  |  |
| gerealiseerd door |  |  |  | K |  |  |  |  |  |  |  |  |  |  |  |  |
| leidt tot gedrag |  |  |  |  |  |  |  | K |  |  |  |  |  |  |  |  |
| bijdrage aan groter proces |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| omvat processen |  |  |  |  |  | K |  |  |  |  |  |  |  |  |  |  |
| omvat levensloop |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| meer organisaties |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| eigen besluit |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| levert aanbod |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| bedient gedrag |  |  |  |  |  |  | K |  |  |  |  |  |  |  |  |  |
| in functie-indeling |  |  |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| leidt tot gebeurtenis |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| **Passief** | | | | | | | | | | | | | | | | |
| onderscheidbare exemplaren | D | D |  |  |  |  |  |  | A | A |  |  |  |  |  |  |
| levenscyclus | D | D |  |  |  |  |  |  | A | A |  |  |  |  |  |  |
| wordt bewerkt | K | K |  |  |  |  |  |  | A | A |  |  |  |  |  |  |
| afspraak | x | T |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| waarneembare vorm | x | x |  |  |  |  |  |  |  |  |  |  |  |  | T |  |
| deel van object | A | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| invoer van een ander | A | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| zelfstandig aanbod |  |  | E |  |  |  |  |  |  |  |  |  |  |  |  |  |
| omvat diensten en afspraken |  |  | K |  |  |  |  |  |  |  |  |  |  |  |  |  |
| geautomatiseerd verwerkt | A | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Beleidskader** | | | | | | | | | | | | | | | | |
| landelijk |  |  |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| in werking |  |  |  |  |  |  |  |  |  |  |  |  | D |  |  |  |
| is grondslag voor |  |  |  |  |  |  |  |  |  |  |  |  | K |  |  |  |
| **Specialisatie** | | | | | | | | | | | | | | | | |
| zelfstandige specialisatie | S | S | S | S | S | S | S | S | S | S | S | S | S |  |  |  |
| generiek |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
<!-- EINDE gegenereerd -->
