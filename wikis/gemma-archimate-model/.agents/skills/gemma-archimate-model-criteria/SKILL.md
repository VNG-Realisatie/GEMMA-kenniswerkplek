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

Deze skill is de enige plek waar staat wanneer een begrip een element van dit model wordt. Ze beschrijft alleen *wat* het begrip is. Hoe je het daarna vastlegt (GGM-match, naam, definitie, relaties) staat in skill `gemma-archimate-model-beoordelen`.

## Kenmerk en criterium

- Een **kenmerk** is een neutrale eigenschap van het begrip zelf, bijvoorbeeld *onderscheidbare exemplaren*. Je beantwoordt het met ja of nee, met een onderbouwing en de bron-id's waarop die steunt. Een kenmerk oordeelt niet over het type.
- Een **criterium** is een regel in de beslistabel hieronder (stap 0 tot 7): welke combinatie van kenmerken tot welk type leidt. De tool `tools/bepaal_type.py` past de criteria toe; jij beoordeelt ze niet los.

Zo beantwoord je alle kenmerken **één keer, tegelijk**. Je kiest dus niet eerst een type om daarna te toetsen of het klopt. Het type is de uitkomst.

## Werkwijze

1. **Stap 0: welk begrip?** Bepaal vóór de kenmerken of het woord een synoniem is van een bestaand element (of van een begrip dat nu wordt beoordeeld), en of dezelfde naam al voor een ander begrip bestaat: in de wiki, het GGM of het GEMMA-model (`tools/ggm.py kandidaten <naam>`, `tools/gemma.py kandidaten <naam>`) of een bron. Vul `synoniem_van` of `homoniem_van` in. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem.
2. Beantwoord **alle** kenmerken uit de vragenlijst hieronder, ook als ze niet bij het vermoedelijke type horen (dan nee). Gebruik de bronnen in de volgorde van de regel Bronvoorrang (`europese-regelgeving` → `rijksregelgeving` → `informatiemodel` → `richtlijn` → `gemeentelijke-regelgeving` → `beleid` → `overig`). Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; staat die niet in de bronanalyse, vul dan eerst de bronanalyse aan.
3. Let op:
   - *zelfstandige specialisatie*: kijk eerst naar boven. Zoek de generalisaties in de wiki, het GGM (`tools/ggm.py generalisaties`, `naamgenoten`) en het GEMMA-model (`tools/gemma.py zoek`) en noteer de keten (bijv. Besluit → Beschikking → Vergunning → Vergunning tot opgraving). Het kenmerk gaat over de "is een"-relatie, niet over herkomst uit wet of beleid; zie skill `gemma-archimate-model-beoordelen` §3 en `references/hierarchie.md`.
   - *los van verantwoordelijkheid* en *eigen rechtspersoon* beslissen tussen actor, rol en bedrijfssamenwerking. Een actor hangt alleen via een rol aan gedrag en objecten (*vervult een rol*).
   - *gebruikt objecten* en *wordt bewerkt*: noem de handeling uit de vaste reeks (registreren, bijwerken, beëindigen, raadplegen, verstrekken, bewaren, overbrengen, vernietigen).
   - *Procesniveau* (stap 7), volgens de ladder van GEMMA Online, Proceshiërarchie (besluit redacteur 2026-10-08): een **levensloopproces** omvat de levensloop van één kernobject, van begin tot eind (*omvat levensloop*, met `kernobject`; *Beheren grafrechten*). Per kernobject is er één; zijn taakveld en beleidsdomein zijn die van het kernobject. Alleen binnen een ketensamenwerking mag een kernobject er meer hebben, één per partij, die samen de bedrijfsinteractie met dat kernobject bedienen (*Toestaan lijkbezorging* door de gemeente als overheid en *Begraven en cremeren stoffelijk overschot* door de houder; de partij kan de gemeente in een eigen hoedanigheid zijn). In GEMMA is het een cluster van bedrijfsprocessen over één thema (GEMMA type *Bedrijfsproces (cluster)*). Een **bedrijfsproces** loopt van klant tot klant en levert een product, dienst of besluit (*bijdrage aan groter proces* met *klant tot klant*: het begint bij een aanleiding van buiten het proces en loopt door tot het resultaat voor de klant, zonder de voortzetting te zijn van een ander proces voor hetzelfde geval; *Verlenen grafrecht*). *Eigen besluit* en *eigen normering* bepalen het procesniveau niet; *levert aanbod* zonder *klant tot klant* wordt voorgelegd (besluit redacteur 2026-10-08). Het hangt onder één levensloopproces, en vaak specialiseert het een generiek GEMMA-bedrijfsproces (`gemma_generiek`). Een product of dienst valt nooit weg. Een **deelproces** (binnen één bedrijfsfunctie, levert een deeldienst) en een processtap krijgen geen pagina; de tekst gaat naar het veld `deelprocessen` van het bedrijfsproces. Triggert een bedrijfsproces een ander bedrijfsproces onder hetzelfde levensloopproces voor hetzelfde geval, dan wordt dat voorgelegd (mogelijk een deelproces); een gebeurtenis die een deelproces triggert is een fout, want een gebeurtenis van buiten start altijd een bedrijfsproces (`tools/bepaal_type.py`). Een groepering van processen (*groepeert processen*) is alleen een cluster naar soort werk, met `gemma_generiek`. De taak is geen procesniveau: boven het levensloopproces staan beleidsdomein en taakveld uit de Beleidsdomeinindeling.
   - *Ketensamenwerking*: waar de bedrijfsprocessen van meer partijen samenkomen, is dat een **bedrijfsinteractie** (*gezamenlijk gedrag*, met `kernobject`: het object dat door de keten gaat). De bedrijfsprocessen van de partijen bedienen de interactie, en een bedrijfssamenwerking of de rollen van de partijen voeren haar uit (GEMMA Online, Proceshiërarchie; GEMMA-element *Ketensamenwerking*). Een ketenproces erboven is impliciet: het staat alleen in de beschrijving van de interactie en is geen procesniveau en geen element. Een levensloopproces aggregeert dus nooit een ander levensloopproces. Voorleggen: estafette (elke partij verantwoordelijk voor haar deel: een bedrijfsinteractie, zoals *Bezorgen stoffelijk overschot*) of orkestratie (één partij verantwoordelijk, de andere voeren onder haar verantwoordelijkheid een deel uit: geen interactie; voert de gemeente het deel uit, dan specialiseert dat bedrijfsproces het GEMMA-proces *Leveren dienst aan derden*, zoals *Behandelen aanvraag verklaring omtrent het gedrag*). Een vervallen element of een samengevoegd element krijgt het besluit `afwijzen`; de controles op de indeling slaan het over.
   - *Objectniveau* (stap 7): een kernobject wordt bewerkt door één levensloopproces; een deel van dat object met een eigen bedrijfsproces is een subobject, anders een onderdeel zonder pagina. *generiek* voor een object dat in veel onderwerpen voorkomt; *invoer van een ander* krijgt geen pagina. Voor een gebeurtenis, rol of dienst met *generiek*: vul `gemma_generiek`, een specialisatie van een GEMMA-element met exacte match; ontbreekt dat element, leg het dan voor als voorstel aan GEMMA.
   - *soort partij*: een actor is een partij waarmee elke gemeente in dezelfde rol te maken heeft, zodat het element voor alle gemeenten geldt. Het criterium sluit uit wat bij één of enkele gemeenten hoort (gemeente Utrecht, provincie Utrecht), niet een partij die landelijk maar één keer bestaat: Rijk, Provincie en Waterschap zijn een soort partij (de bestuurslaag als geheel). Een afzonderlijk ministerie of rijksdienst (minister van BZK, IND) is geen eigen actor; die staat in de beschrijving van Rijk (besluit redacteur 2026-10-07).
   - Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
   - Een regeling: een concreet benoemde regeling of richtlijn die voor alle gemeenten geldt (Europese regelgeving, rijksregelgeving, een landelijke richtlijn of een VNG-model) wordt beleidskader, met de regelgever EU, rijk, landelijke organisatie of VNG-model; de soort ("verordening") is het bedrijfsobject Regeling; een verordening of beleidsnota van één gemeente blijft bron; een los artikel is *buiten dit model*. Een beleidskader in de groep Richtlijn is geen wettelijke grondslag: zijn relatie heet "geeft richtlijn voor", niet "is grondslag voor" (regel Wettelijke grondslag; besluit redacteur 2026-10-08).
4. Vul waar nodig de extra velden in:
   - `genoemd_begrip` bij *slechts eigenschap*, *eigen identiteit* nee (het geheel), *zelfstandige specialisatie* nee (het bredere begrip) of *waarneembare vorm* (het object);
   - `archimate_buiten_model` bij *buiten dit model*;
   - `kernobject` bij een levensloopproces, bedrijfsproces of bedrijfsinteractie: het object waarvan het proces de levensloop omvat, waarin het een mutatie doet of dat door de keten gaat (een id van een bedrijfsobject of afspraak);
   - `gemma_generiek` (`id`, `onderbouwing`): de specialisatie van een generiek GEMMA-element;
   - de indelingsvelden `domein` (product, dienst, functie), `afnemer` (extern of intern; proces, product, dienst), `doelgroep` (actor, rol, samenwerking, kanaal) en `regelgever` (beleidskader), naast `taakveld` en `beleidsdomein`. Een relatie naar een generiek object noemt zijn specialisatie zonder pagina in `via`.
5. Leg de beoordeling vast in `beoordelingen/begrippen/<id>.yaml` (schema `schemas/beoordeling.schema.json`, zie skill `gemma-archimate-model-beoordelen`) en draai `uv run python tools/afleiden.py`. De uitkomst is bindend.
6. Is de uitkomst `conflict` of staat `voorleggen` aan, dan leg je het begrip voor aan de redacteur, met de redenen uit de uitkomst. Pas je antwoorden niet aan om een conflict weg te werken, tenzij een antwoord aantoonbaar fout was.

## ArchiMate-typen in dit model

Namen en definities volgen het GEMMA-kennismodel (bron `2026-vng-over-gemma`, besluit redacteur 2026-10-01; achtergrond: `docs/gemma-kennismodel.md`). Waar GEMMA een type niet kent, geldt de definitie van ArchiMate 3.2 (Engels). De herkomst staat achter elke definitie. "Herkend" betekent: de tool herkent het type, maar deze wiki heeft er geen paginatype voor; het begrip wordt voorgelegd. "Geen pagina" betekent: vaste uitkomst, vermeld bij een ander element.

| ArchiMate-type | Paginatype | GEMMA-naam | Definitie | Duiding |
|---|---|---|---|---|
| Business Object | `bedrijfsobject` | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. (GEMMA) | Een ding waar de gemeente mee werkt: het wordt geregistreerd, bijgewerkt of geraadpleegd door gemeentelijk gedrag. De soort regeling (Regeling) is ook een bedrijfsobject. |
| Contract | `bedrijfsobject` (`archimate_type: contract`) | Afspraak | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. (GEMMA) | Een afspraak tussen partijen (overeenkomst, convenant). Een besluit of verordening is géén afspraak. |
| Product | `product` | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. (GEMMA) | Wat de gemeente als geheel aanbiedt (bijv. uit de productencatalogus): diensten met afspraken, geen losse objecten. |
| Business Service | `dienst` | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). (NORA) | Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd; gerealiseerd door een proces of functie. |
| Business Process | `bedrijfsproces` | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. (GEMMA) | Wordt per keer doorlopen en levert een resultaat op. Een rol mag aan een bedrijfsproces of deelproces worden toegewezen. Procesniveau (stap 7): levensloopproces (één per kernobject, GEMMA type *Bedrijfsproces (cluster)*), bedrijfsproces (klant-tot-klant: één mutatie, besluit, product of dienst) of cluster naar soort werk (een groepering, ook een Business Process). Een deelproces en een processtap krijgen geen pagina. |
| Business Function | `bedrijfsfunctie` | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. (GEMMA) | Doorlopende groepering van gedrag; bedient processen. Niet "wat de gemeente kan": dat is een vermogen (Capability). |
| Business Event | `gebeurtenis` | Gebeurtenis | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. (GEMMA) | Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen). |
| Business Actor | `actor` | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. (GEMMA) | Persoon, organisatie of eenheid, ook extern of generiek (inwoner), en een samenwerkingsverband met eigen rechtspersoon (GGD). Hangt alleen via een rol aan gedrag en objecten. |
| Business Role | `rol` | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. (ArchiMate) | Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar). |
| Business Collaboration | `bedrijfssamenwerking` | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. (ArchiMate) | Samenwerkingsverband zonder eigen rechtspersoon (Zorg- en Veiligheidshuis). |
| Business Interface | `kanaal` | Kanaal | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. (NORA) | Loket, website, telefoon. Eén centrale set; een onderwerp koppelt alleen een dienst aan een bestaand kanaal. |
| Driver | `beleidskader` (map `motivatie/`) | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden (NORA) | Een concreet benoemde rijks- of EU-regeling of VNG-modelverordening die de gemeente een taak, bevoegdheid of plicht geeft. |
| Business Interaction | `bedrijfsinteractie` | Bedrijfsinteractie | A unit of collective business behavior performed by two or more business actors, roles or collaborations. (ArchiMate) | Gezamenlijk gedrag, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen (GEMMA: *Ketensamenwerking*), of een keukentafelgesprek. Met een kernobject; elke nieuwe interactie wordt voorgelegd (besluit redacteur 2026-10-08). |
| Representation | geen pagina | — | A perceptible form of the information carried by a business object. (ArchiMate) | Document, formulier, register, bericht: vermelden bij het object. |
| Location | geen pagina | — | A conceptual or physical place or position where concepts are located or performed. (ArchiMate) | Fysieke plaats als zodanig; een gebiedsindeling als gegevensconcept is een bedrijfsobject. |
| Data Object (applicatielaag) | annotatie `data_object` | Data-object | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. (GEMMA) | Voorbereiding op `applicatiearchitectuur/`; hier alleen als signaal. In GEMMA realiseert een data-object een bedrijfsobject. |

Buiten dit model vallen de overige motivatie- en strategie-elementen (Goal, Outcome, Principle, Requirement, Constraint, Value, Capability) en Grouping (thema). Een losse norm uit één artikel is een Requirement of Constraint en valt buiten het model; de regeling of richtlijn als geheel is een beleidskader (voor alle gemeenten) of blijft bron (van één gemeente).

## Kenmerken en beslistabel

Gegenereerd uit de beslistabel (`uv run python tools/bepaal_type.py markdown --schrijf`); de wikipagina `naslag/beslistabel.md` heeft dezelfde tekst met de naslag per kenmerk (voorbeelden en herkomst), zonder de stappentabel.

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
14. Is het een concreet benoemde wet, AMvB, verordening of landelijke richtlijn als geheel, en niet één artikel of een soort regeling? (*regeling als geheel*)

**Partij.** Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*; *soort partij* bij *handelende partij* en *samenwerkingsverband*.

15. Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? (*los van verantwoordelijkheid*)
16. Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, vennootschap)? (*eigen rechtspersoon*)
17. Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol. (*vervult een rol*)
18. Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het. (*voert gedrag uit*)
19. Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. (*soort partij*)
20. Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst. (*ontsluit een dienst*)

**Soort gedrag.** Alleen bij *gedrag*. Precies één ja.

21. Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? (*per keer doorlopen*)
22. Is het een groepering van bedrijfsprocessen van één soort werk, die niet per geval wordt doorlopen? (*groepeert processen*)
23. Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'? (*gegroepeerd gedrag*)
24. Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? (*toestandsverandering*)
25. Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? (*aangeboden gedrag*)
26. Kan het alleen door twee of meer partijen samen worden uitgevoerd, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen? (*gezamenlijk gedrag*)

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
37. Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? Noem dat proces. (*bijdrage aan groter proces*)
38. Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? Noem begin en eind. (*klant tot klant*)
39. Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? Noem ze. (*omvat processen*)
40. Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? Noem het object. (*omvat levensloop*)
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

56. Geldt het voor alle gemeenten: Europese regelgeving of rijksregelgeving (EU-verordening, wet, AMvB, ministeriële regeling), een landelijke richtlijn (uitvoeringsvoorschrift, handleiding of circulaire van een landelijke organisatie) of een VNG-model van gemeentelijke regelgeving, en geen regeling of beleid van één gemeente? (*landelijk*)
57. Is de regeling geldend recht, of als modelverordening actueel? (*in werking*)
58. Geeft de regeling de gemeente een taak, bevoegdheid of plicht, of schrijft de richtlijn voor hoe zij die uitvoert, in een aanwijsbaar proces, dienst of product? Noem het artikel of de paragraaf en het gedrag. (*is grondslag voor*)

**Specialisatie.** Altijd, als het type een pagina heeft.

59. Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja. (*zelfstandige specialisatie*)
60. Komt het met dezelfde betekenis in veel onderwerpen voor? (*generiek*)

### Beslistabel per elementtype

Voor elk type gelden eerst stap 0 en de poorten, daarna de toets op *zelfstandige specialisatie*. Van de overige drempelcriteria mag er hoogstens 1 nee zijn.

**Wanneer is iets een bedrijfsobject?**

- Type volgt uit: geen aard (een ding); *afspraak* en *waarneembare vorm* nee.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*); ja: subobject bij een eigen bedrijfsproces, anders onderdeel zonder pagina (*deel van object*); ja: onderdeel, geen pagina (*invoer van een ander*).
- Indeling: Beleidsdomeinindeling.
- Voorbeeld: Graf; Aanvraag; Vergunning.

**Wanneer is iets een afspraak?**

- Type volgt uit: *afspraak*.
- Moet ja zijn: *wordt bewerkt*.
- Hoogstens één nee: *onderscheidbare exemplaren*, *levenscyclus*.
- Daarna: annotatie data-object (*geautomatiseerd verwerkt*); ja: subobject bij een eigen bedrijfsproces, anders onderdeel zonder pagina (*deel van object*); ja: onderdeel, geen pagina (*invoer van een ander*).
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
- Daarna: ja: procesniveau levensloopproces (*omvat levensloop*); ja: procesniveau bedrijfsproces bij *klant tot klant*; anders deelproces of processtap zonder pagina (*bijdrage aan groter proces*); ja: procesniveau bedrijfsproces; nee: deelproces of processtap, beschreven in `deelprocessen` van het bedrijfsproces (*klant tot klant*); levert een product of dienst; zonder *klant tot klant* voorleggen: de dienst hoort bij het bedrijfsproces (*levert aanbod*); annotatie (*eigen besluit*); annotatie (*eigen normering*); annotatie (*gebruikt objecten*); annotatie (*komt herhaald voor*); triggering naar een gebeurtenis (*leidt tot gebeurtenis*).
- Indeling: Procesindeling naar kernobject en naar soort werk; een levensloopproces ook in de Beleidsdomeinindeling, onder het beleidsdomein van zijn kernobject.
- Voorbeeld: Beheren grafrechten (levensloopproces); Verlenen grafrecht (bedrijfsproces).

**Wanneer is iets een procescluster?**

- Type volgt uit: *gedrag* en *groepeert processen*.
- Moet ja zijn: *omvat processen*.
- Indeling: Procesindeling naar kernobject en naar soort werk; een levensloopproces ook in de Beleidsdomeinindeling, onder het beleidsdomein van zijn kernobject.
- Voorbeeld: Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk).

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
- Indeling: Procesindeling naar kernobject.
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
- Indeling: Beleidsdomeinindeling en Regelgevingindeling (naar de regelgever).
- Voorbeeld: Wet op de lijkbezorging; Archiefwet; AVG.

**Wanneer is iets een bedrijfsinteractie?**

- Type volgt uit: *gedrag* en *gezamenlijk gedrag*.
- Moet ja zijn: *toegewezen partij*.
- Hoogstens één nee: *aanleiding*, *benoembaar resultaat*.
- Daarna: annotatie (*gebruikt objecten*).
- Indeling: Procesindeling naar kernobject, bij haar kernobject, en Beleidsdomeinindeling, onder het beleidsdomein van haar kernobject.
- Voorbeeld: Bezorgen stoffelijk overschot (ketensamenwerking; voorleggen).

**Wanneer is iets een representatie?** (geen pagina)

- Type volgt uit: *waarneembare vorm*.
- Voorbeeld: register van begraven lijken (vermelden bij Graf).

**Wanneer is iets een locatie?** (geen pagina)

- Type volgt uit: *plaats*.
- Voorbeeld: stadskantoor als vestigingsplaats.

### Beslistabel vanuit de kenmerken

Per kenmerk: bij welke typen het telt, en hoe. **T** bepaalt het type · **x** moet nee zijn voor dit type · **K** kernrelatie: moet ja zijn · **D** telt in de drempel (hoogstens één nee) · **P** poort: geldt voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger, procesniveau, objectniveau, annotatie) · **E** eis: moet ja zijn naast de kernrelatie.

Typen: Obj = Bedrijfsobject · Afspr = Afspraak · Prod = Product · Dienst = Dienst · Proc = Bedrijfsproces · Clus = Procescluster · Func = Bedrijfsfunctie · Gebt = Gebeurtenis · Actor = Actor · Rol = Rol · Samw = Bedrijfssamenwerking · Kan = Kanaal · Bkad = Beleidskader · Inter = Bedrijfsinteractie · Repr = Representatie (geen pagina) · Loc = Locatie (geen pagina).

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
| toegewezen partij |  |  |  |  | K |  | D |  |  |  |  |  |  | K |  |  |
| gebruikt objecten |  |  |  |  | A |  | D |  |  |  |  |  |  | A |  |  |
| aanleiding |  |  |  |  | E |  |  |  |  |  |  |  |  | D |  |  |
| benoembaar resultaat |  |  | D | D | E |  |  |  |  |  |  |  |  | D |  |  |
| komt herhaald voor |  |  |  |  | A |  |  | D |  |  |  |  |  |  |  |  |
| eigen normering |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| afnemer |  |  | D | D |  |  |  |  |  |  |  |  |  |  |  |  |
| gerealiseerd door |  |  |  | K |  |  |  |  |  |  |  |  |  |  |  |  |
| leidt tot gedrag |  |  |  |  |  |  |  | K |  |  |  |  |  |  |  |  |
| bijdrage aan groter proces |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| klant tot klant |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
| omvat processen |  |  |  |  |  | K |  |  |  |  |  |  |  |  |  |  |
| omvat levensloop |  |  |  |  | A |  |  |  |  |  |  |  |  |  |  |  |
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
| zelfstandige specialisatie | S | S | S | S | S | S | S | S | S | S | S | S | S | S |  |  |
| generiek |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Stappentabel

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
<!-- EINDE gegenereerd -->

## Scope

- **Gemeentelijk perspectief.** Alleen wat de gemeente ziet, doet of beslist, of een partij waarmee zij structureel samenwerkt. Een ketenpartner (UWV, IND, COA, GGD …) krijgt ALLEEN een actorpagina bij een structurele relatie met de gemeente: opdrachtgever, mede-eigenaar (gemeenschappelijke regeling), prestatieafspraken of een wettelijke overlegplicht. Een partij die alleen als context of afbakening in de bron staat, of die alleen per geval en op verzoek beslist (gedeputeerde staten als beroepsinstantie), krijgt *gemeentelijk*: nee. De interne processen en rollen van een ketenpartner blijven altijd buiten scope. Precedenten: GGD (gemeente is mede-eigenaar en opdrachtgever); Officier van justitie en Arts als behandelende arts (wettelijke meld- en overlegplicht met de gemeentelijke lijkschouwer, ketenpartner in Bezorgen lijken).
- **Een begrip met uitkomst "geen element"** wordt niet weggelaten: het blijft in de begrippenlijst van het onderwerp staan, met de uitkomst en de reden.

## Anti-patronen

Deze argumenten tellen **nooit** mee, ook niet impliciet of als synoniem:
- registreren of registreerbaar zijn ("wat de gemeente registreert", "registratieobject");
- eigendom ("eigendom ligt bij X"), systeembeheer, "regie, niet registratie", "extern systeem".

Het kenmerk *geautomatiseerd verwerkt* is de enige plek waar gegevensvastlegging meetelt, en alleen als annotatie (`data_object`): het bepaalt nooit of iets een element is.

## Begripstype en entiteitstype

De uitkomst van de beslistabel typeert een **begrip uit een bron** ("wat is het?"). Een GGM-entiteit heeft daarnaast een eigen classificatie (entiteitstype, bij de dekkingsanalyse van het GGM). Die twee zijn niet uitwisselbaar: een GGM-entiteit is geen begrip en wordt pas via een bron beoordeeld.
