---
name: gemma-archimate-model-criteria
description: De criteria van deze wiki voor de vraag of een begrip een ArchiMate-element is en van welk type (bedrijfsobject, afspraak, product, dienst, proces, functie, gebeurtenis, actor, rol, bedrijfssamenwerking, kanaal, beleidskader). Laad deze skill bij elke beoordeling van een begrip, vóór er een elementpagina wordt voorgesteld.
metadata:
  kind: capability
  scope: wiki
  requires-tools: "python:tools/bepaal_type.py"
  reads: "bronanalyse"
  writes: "beoordeling"
---

# Criteria: is dit begrip een ArchiMate-element, en welk?

Deze skill is de enige plek waar staat wanneer een begrip een element van dit model wordt. Ze beschrijft alleen *wat* het begrip is. Hoe je het daarna vastlegt (GGM-match, naam, definitie, relaties) staat in `gemma-archimate-model-write`.

## Kenmerk en criterium

- Een **kenmerk** is een neutrale eigenschap van het begrip zelf, bijvoorbeeld *onderscheidbare exemplaren*. Je beantwoordt het met ja of nee, met een onderbouwing en de bron-id's waarop die steunt. Een kenmerk oordeelt niet over het type.
- Een **criterium** is een regel in de beslistabel hieronder (stap 0 tot 6): welke combinatie van kenmerken tot welk type leidt. De tool `tools/bepaal_type.py` past de criteria toe; jij beoordeelt ze niet los.

Zo beantwoord je alle kenmerken **één keer, tegelijk**. Je kiest dus niet eerst een type om daarna te toetsen of het klopt. Het type is de uitkomst.

## Werkwijze

1. **Stap 0: welk begrip?** Bepaal vóór de kenmerken of het woord een synoniem is van een bestaand element (of van een begrip dat nu wordt beoordeeld), en of dezelfde naam al voor een ander begrip bestaat: in de wiki, het GGM of het GEMMA-model (`tools/ggm.py kandidaten <naam>`, `tools/gemma.py kandidaten <naam>`) of een bron. Vul `synoniem_van` of `homoniem_van` in. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem.
2. Beantwoord **alle** kenmerken uit de vragenlijst hieronder, ook als ze niet bij het vermoedelijke type horen (dan nee). Gebruik de bronnen in de volgorde van de bronvoorrang (wet → informatiemodel → beleid → overig). Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; staat die niet in de bronanalyse, vul dan eerst de bronanalyse aan.
3. Let op:
   - *zelfstandige specialisatie*: kijk eerst naar boven. Zoek de generalisaties in de wiki, het GGM (`tools/ggm.py generalisaties`, `naamgenoten`) en het GEMMA-model (`tools/gemma.py zoek`) en noteer de keten (bijv. Besluit → Beschikking → Vergunning → Vergunning tot opgraving). Het kenmerk gaat over de "is een"-relatie, niet over herkomst uit wet of beleid; zie `gemma-archimate-model-assess` §3.
   - *los van verantwoordelijkheid* en *eigen rechtspersoon* beslissen tussen actor, rol en bedrijfssamenwerking. Een actor hangt alleen via een rol aan gedrag en objecten (*vervult een rol*).
   - *gebruikt objecten* en *wordt bewerkt*: noem de handeling uit de vaste reeks (registreren, bijwerken, beëindigen, raadplegen, verstrekken, bewaren, overbrengen, vernietigen).
   - *bijdrage aan groter proces*: ja maakt een bedrijfsproces tot deelproces (procesniveau), met het grotere proces in de onderbouwing.
   - Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
   - Een regeling: een concreet benoemde landelijke regeling wordt beleidskader; de soort ("verordening") is het bedrijfsobject Regeling; een gemeentelijke verordening blijft bron; een los artikel is *buiten dit model*.
4. Vul waar nodig de extra velden in:
   - `genoemd_begrip` bij *slechts eigenschap*, *eigen identiteit* nee (het geheel), *zelfstandige specialisatie* nee (het bredere begrip) of *waarneembare vorm* (het object);
   - `archimate_buiten_model` bij *buiten dit model*.
5. Leg de beoordeling vast in `beoordelingen/begrippen/<id>.yaml` (schema `schemas/beoordeling.schema.json`, zie skill `gemma-archimate-model-beoordelen`) en draai `uv run python tools/afleiden.py`. De uitkomst is bindend.
6. Is de uitkomst `conflict` of staat `voorleggen` aan, dan leg je het begrip voor aan de redacteur, met de redenen uit de uitkomst. Pas je antwoorden niet aan om een conflict weg te werken, tenzij een antwoord aantoonbaar fout was.

## ArchiMate-typen in dit model

Namen en definities volgen het GEMMA-kennismodel (bron `2026-vng-over-gemma`, besluit redacteur 2026-10-01; de vergelijking staat in `analyses/gemma-kennismodel.md`). Waar GEMMA een type niet kent, geldt de definitie van ArchiMate 3.2 (Engels). De herkomst staat achter elke definitie. "Herkend" betekent: de tool herkent het type, maar deze wiki heeft er geen paginatype voor; het begrip wordt voorgelegd. "Geen pagina" betekent: vaste uitkomst, vermeld bij een ander element.

| ArchiMate-type | Paginatype | GEMMA-naam | Definitie | Duiding |
|---|---|---|---|---|
| Business Object | `bedrijfsobject` | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. (GEMMA) | Een ding waar de gemeente mee werkt: het wordt geregistreerd, bijgewerkt of geraadpleegd door gemeentelijk gedrag. De soort regeling (Regeling) is ook een bedrijfsobject. |
| Contract | `bedrijfsobject` (`archimate_type: contract`) | Afspraak | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. (GEMMA) | Een afspraak tussen partijen (overeenkomst, convenant). Een besluit of verordening is géén afspraak. |
| Product | `product` | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. (GEMMA) | Wat de gemeente als geheel aanbiedt (bijv. uit de productencatalogus): diensten met afspraken, geen losse objecten. |
| Business Service | `dienst` | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). (NORA) | Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd; gerealiseerd door een proces of functie. |
| Business Process | `bedrijfsproces` | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. (GEMMA) | Wordt per keer doorlopen en levert een resultaat op. Een rol mag aan een bedrijfsproces worden toegewezen. Procesniveau bedrijfsproces of deelproces. |
| Business Function | `bedrijfsfunctie` | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. (GEMMA) | Doorlopende groepering van gedrag; bedient processen. Niet "wat de gemeente kan": dat is een vermogen (Capability). |
| Business Event | `gebeurtenis` | Gebeurtenis | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. (GEMMA) | Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen). |
| Business Actor | `actor` | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. (GEMMA) | Persoon, organisatie of eenheid, ook extern of generiek (inwoner), en een samenwerkingsverband met eigen rechtspersoon (GGD). Hangt alleen via een rol aan gedrag en objecten. |
| Business Role | `rol` | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. (ArchiMate) | Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar). |
| Business Collaboration | `bedrijfssamenwerking` | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. (ArchiMate) | Samenwerkingsverband zonder eigen rechtspersoon (Zorg- en Veiligheidshuis). |
| Business Interface | `kanaal` | Kanaal | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. (NORA) | Loket, website, telefoon. Eén centrale set; een onderwerp koppelt alleen een dienst aan een bestaand kanaal. |
| Driver | `beleidskader` (map `motivatie/`) | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden (NORA) | Een concreet benoemde rijks- of EU-regeling of VNG-modelverordening die de gemeente een taak, bevoegdheid of plicht geeft. |
| Business Interaction | herkend | — | A unit of collective business behavior performed by two or more business actors, roles or collaborations. (ArchiMate) | Gezamenlijk gedrag (keukentafelgesprek, zitting). |
| Representation | geen pagina | — | A perceptible form of the information carried by a business object. (ArchiMate) | Document, formulier, register, bericht: vermelden bij het object. |
| Location | geen pagina | — | A conceptual or physical place or position where concepts are located or performed. (ArchiMate) | Fysieke plaats als zodanig; een gebiedsindeling als gegevensconcept is een bedrijfsobject. |
| Data Object (applicatielaag) | annotatie `data_object` | Data-object | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. (GEMMA) | Voorbereiding op `applicatiearchitectuur/`; hier alleen als signaal. In GEMMA realiseert een data-object een bedrijfsobject. |

Buiten dit model vallen de overige motivatie- en strategie-elementen (Goal, Outcome, Principle, Requirement, Constraint, Value, Capability) en Grouping (thema). Een losse norm uit één artikel is een Requirement of Constraint en valt buiten het model; de regeling als geheel is een beleidskader (landelijk) of blijft bron (gemeentelijk).

## Kenmerken en beslistabel

Gegenereerd uit de beslistabel (`uv run python tools/bepaal_type.py markdown --schrijf`); dezelfde tekst, zonder de stappentabel, staat in `analyses/beslistabel.md`.

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
6. Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? Noem bij nee dat onderwerp. (*betekenis in onderwerp*)

**Aard.** Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.

7. Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? (*gedrag*)
8. Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? (*handelende partij*)
9. Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? (*hoedanigheid*)
10. Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? (*samenwerkingsverband*)
11. Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? (*toegangspunt*)
12. Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? (*plaats*)
13. Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? (*aanbod als geheel*)
14. Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort regeling? (*regeling als geheel*)

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*.

15. Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? (*los van verantwoordelijkheid*)
16. Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? (*eigen rechtspersoon*)
17. Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. (*vervult een rol*)
18. Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. (*voert gedrag uit*)
19. Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. (*ontsluit een dienst*)

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

20. Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? (*per keer doorlopen*)
21. Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? (*gegroepeerd gedrag*)
22. Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? (*toestandsverandering*)
23. Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? (*aangeboden gedrag*)
24. Kan het alleen door twee of meer partijen samen worden uitgevoerd? (*gezamenlijk gedrag*)

**Gedrag.** Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.

25. Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. (*toegewezen partij*)
26. Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. (*gebruikt objecten*)
27. Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. (*aanleiding*)
28. Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. (*benoembaar resultaat*)
29. Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? (*komt herhaald voor*)
30. Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. (*eigen normering*)
31. Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? (*stabiel over tijd*)
32. Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. (*afnemer*)
33. Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. (*gerealiseerd door*)
34. Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. (*leidt tot gedrag*)
35. Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? Noem dat proces. (*bijdrage aan groter proces*)

**Passief.** Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en *geautomatiseerd verwerkt* bij elk begrip; *omvat diensten en afspraken* bij *aanbod als geheel*.

36. Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? (*onderscheidbare exemplaren*)
37. Ontstaan, veranderen en eindigen de exemplaren? (*levenscyclus*)
38. Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. (*wordt bewerkt*)
39. Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? (*afspraak*)
40. Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. (*waarneembare vorm*)
41. Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. (*omvat diensten en afspraken*)
42. Wordt het als gegevensstructuur geautomatiseerd verwerkt? (*geautomatiseerd verwerkt*)

**Beleidskader.** Alleen bij *regeling als geheel*.

43. Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen regeling van één gemeente? (*landelijk*)
44. Is de regeling geldend recht, of als modelverordening actueel? (*in werking*)
45. Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar proces, dienst of product? Noem het artikel en het gedrag. (*is grondslag voor*)

**Specialisatie.** Altijd, als het type een pagina heeft.

46. Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. (*zelfstandige specialisatie*)

### Kenmerken: naslag per groep

**Poort.** Altijd.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| herkenbaar | Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning) | technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel) | ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts) |
| gemeentelijk | Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD) | alleen context, of de interne zaak van een ketenpartner (behandelend arts) | GEMMA (gemeentelijk perspectief) |
| buiten dit model | Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? Noem het ArchiMate-type. | armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel) | bijstandsuitkering; Wet op de lijkbezorging (beleidskader) | ArchiMate (motivatie-, strategie- en overige lagen) |
| slechts eigenschap | Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een doelgroep? Noem dat begrip. | bouwjaar (van Pand); minima (indeling van Inwoner) | Pand | GEMMA (negatieve toets: eigenschap, status, classificatie) |
| eigen identiteit | Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? Noem bij nee dat begrip. | Beschikking; uitgifte van een graf | ondertekening van een besluit (deelstap) | GEMMA (eigen bestaan; procesarchitectuur: processtap, handeling) |
| betekenis in onderwerp | Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? Noem bij nee dat onderwerp. | Graf in lijkbezorging | akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand) | GEMMA (betekenis binnen het onderwerp) |

**Aard.** Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| gedrag | Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | aanvraag behandelen; verhuizing | aanvraag | ArchiMate (gedragselement) |
| handelende partij | Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | college van B&W; inwoner | aanvrager | GEMMA (definitie Actor) |
| hoedanigheid | Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | aanvrager; houder van de begraafplaats | gemeenteraad | ArchiMate (definitie Rol) |
| samenwerkingsverband | Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren? | Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten) | GGD-arts | ArchiMate (definitie Bedrijfssamenwerking) |
| toegangspunt | Is het een communicatiekanaal waarlangs een dienst beschikbaar komt? | publieksbalie; gemeentelijke website | klantcontact | NORA (definitie Kanaal) |
| plaats | Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven? | stadskantoor als vestigingsplaats | wijk (indeling) | ArchiMate (Location) |
| aanbod als geheel | Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer wordt geleverd? | bewonersparkeervergunning zoals de productencatalogus haar aanbiedt | parkeren | GEMMA (definitie Product) |
| regeling als geheel | Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort regeling? | Wet op de lijkbezorging; modelverordening participatie | 'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm) | GEMMA (definitie Beleidskader) |

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| los van verantwoordelijkheid | Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | kerkgenootschap; burgemeester | houder van de begraafplaats | ArchiMate (actor tegenover rol) |
| eigen rechtspersoon | Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? | GGD (openbaar lichaam) | Zorg- en Veiligheidshuis | besluit redacteur 2026-10-01 (scheidslijn actor en bedrijfssamenwerking) |
| vervult een rol | Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. | kerkgenootschap vervult Houder van de begraafplaats | partij die alleen genoemd wordt | GEMMA (actor wordt toegewezen aan rol) |
| voert gedrag uit | Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. | Houder van de begraafplaats → Ruimen graf | rol zonder aanwijsbaar gedrag | GEMMA (rol wordt toegewezen aan functie); besluit redacteur 2026-10-01 (ook aan proces) |
| ontsluit een dienst | Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. | website → Melding openbare ruimte doen | kanaal zonder aanwijsbare dienst | GEMMA (kanaal wordt toegewezen aan dienst) |

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| per keer doorlopen | Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | aanvraag omgevingsvergunning behandelen | vergunningverlening | GEMMA (definitie Bedrijfsproces) |
| gegroepeerd gedrag | Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? | vergunningverlening; belastingheffing | aanslag opleggen | GEMMA (definitie Bedrijfsfunctie) |
| toestandsverandering | Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | verhuizing; aanvraag ontvangen; beslistermijn verstreken | verhuizing doorgeven | GEMMA (definitie Gebeurtenis) |
| aangeboden gedrag | Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | melding openbare ruimte doen | melding afhandelen | NORA (definitie Dienst) |
| gezamenlijk gedrag | Kan het alleen door twee of meer partijen samen worden uitgevoerd? | keukentafelgesprek; hoorzitting | beschikking opstellen | ArchiMate (Business Interaction) |

**Gedrag.** Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| toegewezen partij | Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol. | Ruimen graf (Houder van de begraafplaats) | draagvlak creëren | ArchiMate (toewijzing van rol aan gedrag) |
| gebruikt objecten | Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? Noem object en handeling. | Inspraak (registreert zienswijze) | burgerberaad | ArchiMate (toegang van gedrag tot object); besluit redacteur 2026-10-01 (handelingen) |
| aanleiding | Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. | overheidsparticipatie (verzoek ingediend) | kennisdeling | ArchiMate (triggering); GEMMA (procesarchitectuur) |
| benoembaar resultaat | Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? Noem het. | opgraving (opgegraven lijk) | informeren | GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer) |
| komt herhaald voor | Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | inspraak (per ontwerpbesluit); overlijden | invoeren van de participatieverordening | GEMMA (proces als herhaalbare werkwijze) |
| eigen normering | Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? Noem het artikel. | inspraak (afdeling 3.4 Awb) | burgerberaad (vormvrij) | GEMMA (proces met eigen spelregels) |
| stabiel over tijd | Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? | participatie; belastingheffing | projectteam Omgevingswet | ArchiMate en GEMMA (bedrijfsfunctiemodel) |
| afnemer | Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die. | melding openbare ruimte doen (inwoner) | interne registratiestap | NORA (definitie Dienst); GEMMA (definitie Product, rol Klant) |
| gerealiseerd door | Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het. | Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt) | dienst zonder aanwijsbare uitvoering | GEMMA (proces en functie realiseren dienst) |
| leidt tot gedrag | Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het. | Overlijden → Uitvoeren lijkbezorging | voorval zonder gemeentelijk gevolg | GEMMA (gebeurtenis triggert proces) |
| bijdrage aan groter proces | Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? Noem dat proces. | toetsen indieningsvereisten (in behandelen aanvraag) | behandelen aanvraag (levert het besluit zelf) | GEMMA (definitie Deelproces) |

**Passief.** Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en *geautomatiseerd verwerkt* bij elk begrip; *omvat diensten en afspraken* bij *aanbod als geheel*.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| onderscheidbare exemplaren | Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | aanvraag (elke aanvraag apart) | gemeentefonds (er is er één) | GEMMA (kan in meervoud bestaan) |
| levenscyclus | Ontstaan, veranderen en eindigen de exemplaren? | vergunning (verleend, gewijzigd, ingetrokken) | kadastrale gemeentecode | GEMMA (eigen levenscyclus) |
| wordt bewerkt | Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag. | aanvraag (geregistreerd, beoordeeld) | preventieakkoord (alleen beleidsmatig) | GEMMA (proces en functie benaderen bedrijfsobject) |
| afspraak | Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit of regeling? | subsidieovereenkomst; uitvoeringsovereenkomst | subsidiebeschikking; verordening | GEMMA (definitie Afspraak) |
| waarneembare vorm | Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt vastgelegd of overgebracht? Noem dat begrip. | aanslagbiljet (van Aanslag); register van begraven lijken | aanslag | ArchiMate (Representation) |
| omvat diensten en afspraken | Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze. | parkeervergunning (dienst parkeren, voorwaarden) | losse dienst | GEMMA (product bundelt dienst en afspraak) |
| geautomatiseerd verwerkt | Wordt het als gegevensstructuur geautomatiseerd verwerkt? | zaak in het zaaksysteem | keukentafelgesprek | GEMMA (definitie Data-object) |

**Beleidskader.** Alleen bij *regeling als geheel*.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| landelijk | Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen regeling van één gemeente? | Wet op de lijkbezorging; AVG; modelverordening | beheersverordening van één gemeente (blijft bron) | besluit redacteur 2026-10-01 |
| in werking | Is de regeling geldend recht, of als modelverordening actueel? | Archiefwet 1995 | ingetrokken wet | besluit redacteur 2026-10-01 |
| is grondslag voor | Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar proces, dienst of product? Noem het artikel en het gedrag. | Wet op de lijkbezorging art. 28 → Verlenen grafrecht | BW boek 2, gebruikt voor één definitie | GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader) |

**Specialisatie.** Altijd, als het type een pagina heeft.

| Kenmerk | Vraag | Ja, bijvoorbeeld | Nee, bijvoorbeeld | Herkomst |
|---|---|---|---|---|
| zelfstandige specialisatie | Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. | Omgevingsvergunning naast Vergunning (eigen wet en procedure); Houder van het crematorium naast Houder van de begraafplaats (eigen plichten) | vergunning tot opgraving (variant van Vergunning); aanvrager van een vergunning tot opgraving (variant van Aanvrager) | GEMMA (zelfstandig ding waar beleid op gemaakt wordt; specialisatie) |

### Beslistabel per elementtype

Voor elk type gelden eerst stap 0 en de poorten, daarna de toets op *zelfstandige specialisatie*. Van de overige drempelcriteria mag er hoogstens 1 nee zijn.

**Wanneer is iets een bedrijfsobject?**

- Type volgt uit: geen aard (een ding); *afspraak* en *waarneembare vorm* nee.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*).
- Voorbeeld: Graf; Aanvraag; Vergunning.

**Wanneer is iets een afspraak?**

- Type volgt uit: *afspraak*.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*).
- Voorbeeld: Uitvoeringsovereenkomst; Grafrecht.

**Wanneer is iets een product?**

- Type volgt uit: *aanbod als geheel*.
- Moet ja zijn: *omvat diensten en afspraken*.
- Hoogstens één nee: *afnemer*, *benoembaar resultaat*.
- Voorbeeld: bewonersparkeervergunning in de productencatalogus.

**Wanneer is iets een dienst?**

- Type volgt uit: *gedrag* en *aangeboden gedrag*.
- Moet ja zijn: *gerealiseerd door*.
- Hoogstens één nee: *afnemer*, *benoembaar resultaat*.
- Voorbeeld: Onderhoud van graven.

**Wanneer is iets een bedrijfsproces?**

- Type volgt uit: *gedrag* en *per keer doorlopen*.
- Moet ja zijn: *toegewezen partij*.
- Hoogstens één nee: *gebruikt objecten*, *aanleiding*, *benoembaar resultaat*, *komt herhaald voor*, *eigen normering*.
- Daarna: ja: procesniveau deelproces (*bijdrage aan groter proces*).
- Voorbeeld: Ruimen graf; Uitvoeren inspraakprocedure.

**Wanneer is iets een bedrijfsfunctie?**

- Type volgt uit: *gedrag* en *gegroepeerd gedrag*.
- Moet ja zijn: *toegewezen partij*.
- Hoogstens één nee: *gebruikt objecten*, *stabiel over tijd*.
- Voorbeeld: Lijkbezorging; Participatie.

**Wanneer is iets een gebeurtenis?**

- Type volgt uit: *gedrag* en *toestandsverandering*.
- Moet ja zijn: *leidt tot gedrag*.
- Hoogstens één nee: *komt herhaald voor*.
- Voorbeeld: Overlijden; Verval van het grafrecht.

**Wanneer is iets een actor?**

- Type volgt uit: *handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*.
- Moet ja zijn: *vervult een rol*.
- Daarna: tegenhanger bij *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*.
- Voorbeeld: College van B&W; Kerkgenootschap; GGD.

**Wanneer is iets een rol?**

- Type volgt uit: *hoedanigheid*, niet *los van verantwoordelijkheid*.
- Moet ja zijn: *voert gedrag uit*.
- Daarna: tegenhanger bij *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*.
- Voorbeeld: Houder van de begraafplaats; Rechthebbende op het graf.

**Wanneer is iets een bedrijfssamenwerking?**

- Type volgt uit: *samenwerkingsverband* zonder *eigen rechtspersoon*.
- Moet ja zijn: *voert gedrag uit*.
- Voorbeeld: Zorg- en Veiligheidshuis.

**Wanneer is iets een kanaal?**

- Type volgt uit: *toegangspunt*.
- Moet ja zijn: *ontsluit een dienst*.
- Kanalen vormen één centrale set: koppelen aan een bestaand kanaal; een nieuw kanaal alleen na besluit van de redacteur.
- Voorbeeld: publieksbalie; gemeentelijke website (centrale set).

**Wanneer is iets een beleidskader?**

- Type volgt uit: *regeling als geheel* en *landelijk*.
- Moet ja zijn: *is grondslag voor*.
- Hoogstens één nee: *in werking*.
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

Per kenmerk: bij welke typen het telt, en hoe. **T** bepaalt het type · **x** moet nee zijn voor dit type · **K** kernrelatie: moet ja zijn · **D** telt in de drempel (hoogstens één nee) · **P** poort: geldt voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger, procesniveau, annotatie).

Typen: Obj = Bedrijfsobject · Afspr = Afspraak · Prod = Product · Dienst = Dienst · Proc = Bedrijfsproces · Func = Bedrijfsfunctie · Gebt = Gebeurtenis · Actor = Actor · Rol = Rol · Samw = Bedrijfssamenwerking · Kan = Kanaal · Bkad = Beleidskader · Inter = Interaction (herkend) · Repr = Representatie (geen pagina) · Loc = Locatie (geen pagina).

| Kenmerk | Obj | Afspr | Prod | Dienst | Proc | Func | Gebt | Actor | Rol | Samw | Kan | Bkad | Inter | Repr | Loc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Poort** | | | | | | | | | | | | | | | |
| herkenbaar | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| gemeentelijk | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| buiten dit model | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| slechts eigenschap | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| eigen identiteit | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| betekenis in onderwerp | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| **Aard** | | | | | | | | | | | | | | | |
| gedrag |  |  |  | T | T | T | T |  |  |  |  |  | T |  |  |
| handelende partij |  |  |  |  |  |  |  | T |  |  |  |  |  |  |  |
| hoedanigheid |  |  |  |  |  |  |  |  | T |  |  |  |  |  |  |
| samenwerkingsverband |  |  |  |  |  |  |  | T |  | T |  |  |  |  |  |
| toegangspunt |  |  |  |  |  |  |  |  |  |  | T |  |  |  |  |
| plaats |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T |
| aanbod als geheel |  |  | T |  |  |  |  |  |  |  |  |  |  |  |  |
| regeling als geheel |  |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| **Partij** | | | | | | | | | | | | | | | |
| los van verantwoordelijkheid |  |  |  |  |  |  |  | T | x |  |  |  |  |  |  |
| eigen rechtspersoon |  |  |  |  |  |  |  | T |  | x |  |  |  |  |  |
| vervult een rol |  |  |  |  |  |  |  | K |  |  |  |  |  |  |  |
| voert gedrag uit |  |  |  |  |  |  |  |  | K | K |  |  |  |  |  |
| ontsluit een dienst |  |  |  |  |  |  |  |  |  |  | K |  |  |  |  |
| **Soort gedrag** | | | | | | | | | | | | | | | |
| per keer doorlopen |  |  |  |  | T |  |  |  |  |  |  |  |  |  |  |
| gegroepeerd gedrag |  |  |  |  |  | T |  |  |  |  |  |  |  |  |  |
| toestandsverandering |  |  |  |  |  |  | T |  |  |  |  |  |  |  |  |
| aangeboden gedrag |  |  |  | T |  |  |  |  |  |  |  |  |  |  |  |
| gezamenlijk gedrag |  |  |  |  |  |  |  |  |  |  |  |  | T |  |  |
| **Gedrag** | | | | | | | | | | | | | | | |
| toegewezen partij |  |  |  |  | K | K |  |  |  |  |  |  |  |  |  |
| gebruikt objecten |  |  |  |  | D | D |  |  |  |  |  |  |  |  |  |
| aanleiding |  |  |  |  | D |  |  |  |  |  |  |  |  |  |  |
| benoembaar resultaat |  |  | D | D | D |  |  |  |  |  |  |  |  |  |  |
| komt herhaald voor |  |  |  |  | D |  | D |  |  |  |  |  |  |  |  |
| eigen normering |  |  |  |  | D |  |  |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| afnemer |  |  | D | D |  |  |  |  |  |  |  |  |  |  |  |
| gerealiseerd door |  |  |  | K |  |  |  |  |  |  |  |  |  |  |  |
| leidt tot gedrag |  |  |  |  |  |  | K |  |  |  |  |  |  |  |  |
| bijdrage aan groter proces |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |
| **Passief** | | | | | | | | | | | | | | | |
| onderscheidbare exemplaren | D | D |  |  |  |  |  | A | A |  |  |  |  |  |  |
| levenscyclus | D | D |  |  |  |  |  | A | A |  |  |  |  |  |  |
| wordt bewerkt | K | K |  |  |  |  |  | A | A |  |  |  |  |  |  |
| afspraak | x | T |  |  |  |  |  |  |  |  |  |  |  |  |  |
| waarneembare vorm | x | x |  |  |  |  |  |  |  |  |  |  |  | T |  |
| omvat diensten en afspraken |  |  | K |  |  |  |  |  |  |  |  |  |  |  |  |
| geautomatiseerd verwerkt | A | A |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Beleidskader** | | | | | | | | | | | | | | | |
| landelijk |  |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| in werking |  |  |  |  |  |  |  |  |  |  |  | D |  |  |  |
| is grondslag voor |  |  |  |  |  |  |  |  |  |  |  | K |  |  |  |
| **Specialisatie** | | | | | | | | | | | | | | | |
| zelfstandige specialisatie | S | S | S | S | S | S | S | S | S | S | S | S |  |  |  |

### Stappentabel

Stap 0–4 van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig type op. Een voorlopig type met een pagina gaat door naar stap 5 (drempel) en stap 6 (zelfstandige specialisatie). Daarna gelden de aanvullingen.

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
| 17 | 4 Type | *gedrag* en precies één soort gedrag | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis of Dienst; *gezamenlijk gedrag*: Interaction, voorleggen |
| 18 | 4 Type | *gedrag*, maar geen of meer dan één soort gedrag | conflict: voorleggen |
| 19 | 4 Type | geen aard, *waarneembare vorm* | Representatie: geen pagina; vermelden bij het genoemde object |
| 20 | 4 Type | geen aard, *afspraak* | Afspraak (Contract) |
| 21 | 4 Type | geen aard, overig | Bedrijfsobject |
| 22 | 5 Drempel | kernrelatie van het type nee | geen element: voorleggen met de ontbrekende relatie |
| 23 | 5 Drempel | meer dan 1 van de overige drempelcriteria nee | geen element: voorleggen met de ontbrekende criteria |
| 24 | 6 Specialisatie | niet *zelfstandige specialisatie*, met `genoemd_begrip` | specialisatie zonder pagina; relaties naar het genoemde, bredere begrip |
| 25 | 6 Specialisatie | niet *zelfstandige specialisatie*, zonder `genoemd_begrip` | voorleggen: noem het bredere begrip |
| 26 | 6 Specialisatie | anders | element van het voorlopige type |
| — | Aanvulling | `homoniem_van` ingevuld | voorleggen: naamkeuze; `## Homoniemen` bij beide; bij een GGM-homoniem een terugmelding |
| — | Aanvulling | Actor of Rol met *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt* | ook een bedrijfsobjectpagina (tegenhanger) |
| — | Aanvulling | Bedrijfsproces met *bijdrage aan groter proces* | procesniveau deelproces, onder het genoemde bedrijfsproces |
| — | Aanvulling | *geautomatiseerd verwerkt* | annotatie `data_object: ja` |
| — | Signaal (controle) | Dienst zonder realiserend proces of functie met pagina; Gebeurtenis zonder gestart gedrag met pagina | waarschuwing: proces als kandidaat voorleggen |
<!-- EINDE gegenereerd -->

## Scope

- **Gemeentelijk perspectief.** Alleen wat de gemeente ziet, doet of beslist, of een partij waarmee zij structureel samenwerkt. Een ketenpartner (UWV, IND, COA, GGD …) krijgt ALLEEN een actorpagina bij een structurele relatie met de gemeente: opdrachtgever, mede-eigenaar (gemeenschappelijke regeling), prestatieafspraken of een wettelijke overlegplicht. Een partij die alleen als context of afbakening in de bron staat (behandelend arts, gedeputeerde staten), krijgt *gemeentelijk*: nee. De interne processen en rollen van een ketenpartner blijven altijd buiten scope. Precedent: GGD (gemeente is mede-eigenaar en opdrachtgever).
- **Een begrip met uitkomst "geen element"** wordt niet weggelaten: het blijft in de begrippenlijst van het onderwerp staan, met de uitkomst en de reden.

## Anti-patronen

Deze argumenten tellen **nooit** mee, ook niet impliciet of als synoniem:
- registreren of registreerbaar zijn ("wat de gemeente registreert", "registratieobject");
- eigendom ("eigendom ligt bij X"), systeembeheer, "regie, niet registratie", "extern systeem".

Het kenmerk *geautomatiseerd verwerkt* is de enige plek waar gegevensvastlegging meetelt, en alleen als annotatie (`data_object`): het bepaalt nooit of iets een element is.

## Begripstype en entiteitstype

De uitkomst van de beslistabel typeert een **begrip uit een bron** ("wat is het?"). Een GGM-entiteit heeft daarnaast een eigen classificatie (entiteitstype, bij de dekkingsanalyse van het GGM). Die twee zijn niet uitwisselbaar: een GGM-entiteit is geen begrip en wordt pas via een bron beoordeeld.
