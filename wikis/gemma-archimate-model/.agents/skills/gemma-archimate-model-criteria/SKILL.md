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

Deze skill zegt hoe je beoordeelt of een begrip een element van dit model wordt, en van welk type. Wat de typen zijn, met hun kernrelatie, niveaus, eigenschappen, indelingen en naamvorm, staat in het kennismodel: [kennismodel/README.md](../../../kennismodel/README.md), per type de modelleerafspraken. De vragen met voorbeelden en herkomst, en de stappentabel van de beslistabel, staan in [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md); de regels voor het modelleren in [modelleerregels](../../../kennismodel/modelleerregels.md). Hoe je het begrip daarna vastlegt (GGM-match, naam, definitie, relaties) staat in skill `gemma-archimate-model-beoordelen`.

## Kenmerk en criterium

- Een **kenmerk** is een neutrale eigenschap van het begrip zelf, bijvoorbeeld *onderscheidbare exemplaren*. Je beantwoordt het met ja of nee, met een onderbouwing en de bron-id's waarop die steunt. Een kenmerk oordeelt niet over het type.
- Een **criterium** is een regel in de beslistabel (stap 0 tot 7): welke combinatie van kenmerken tot welk type leidt. De tool `tools/bepaal_type.py` past de criteria toe; jij beoordeelt ze niet los.

Zo beantwoord je alle kenmerken **één keer, tegelijk**. Je kiest dus niet eerst een type om daarna te toetsen of het klopt. Het type is de uitkomst.

## Werkwijze

1. **Stap 0: welk begrip?** Bepaal vóór de kenmerken of het woord een synoniem is van een bestaand element (of van een begrip dat nu wordt beoordeeld), en of dezelfde naam al voor een ander begrip bestaat: in de wiki, het GGM of het GEMMA-model (`tools/ggm.py kandidaten <naam>`, `tools/gemma.py kandidaten <naam>`) of een bron. Vul `synoniem_van` of `homoniem_van` in. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem.
2. Beantwoord **alle** kenmerken uit de vragenlijst hieronder, ook als ze niet bij het vermoedelijke type horen (dan nee). Gebruik de bronnen in de volgorde van de regel Bronvoorrang. Bij "Noem …" hoort bij ja een concreet begrip, artikel of relatie uit de bronnen; staat die niet in de bronanalyse, vul dan eerst de bronanalyse aan. Twijfel je over een kenmerk, kijk dan naar de voorbeelden in [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md).
3. Let op:
   - *zelfstandige specialisatie*: kijk eerst naar boven. Zoek de generalisaties in de wiki, het GGM (`tools/ggm.py generalisaties`, `naamgenoten`) en het GEMMA-model (`tools/gemma.py zoek`) en noteer de keten (bijv. Besluit → Beschikking → Vergunning → Vergunning tot opgraving). Het kenmerk gaat over de "is een"-relatie, niet over herkomst uit wet of beleid; zie skill `gemma-archimate-model-beoordelen` §3 en `references/hierarchie.md`.
   - *los van verantwoordelijkheid* en *eigen rechtspersoon* beslissen tussen actor, rol en bedrijfssamenwerking; *soort partij* volgt de afspraken in de modelleerafspraken van [Actor](../../../kennismodel/bedrijfsarchitectuur/actor-modelleerafspraken.md).
   - *gebruikt objecten* en *wordt bewerkt*: noem de handeling uit de vaste reeks (zie het [kennismodel](../../../kennismodel/README.md), Relatietypen).
   - Een proces: bepaal het procesniveau (stap 7) met de niveaus en afspraken in de modelleerafspraken van [Bedrijfsproces](../../../kennismodel/bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md); een ketensamenwerking met die van [Bedrijfsinteractie](../../../kennismodel/bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md). Een vervallen of samengevoegd element krijgt het besluit `afwijzen`; de controles op de indeling slaan het over.
   - Een object: bepaal het objectniveau (stap 7) met de modelleerafspraken van [Bedrijfsobject](../../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md). Voor een gebeurtenis, rol of dienst met *generiek*: vul `gemma_generiek`, een specialisatie van een GEMMA-element met exacte match; ontbreekt dat element, leg het dan voor als voorstel aan GEMMA.
   - Een doelgroep (minima, jongeren) is geen actor of rol maar een indeling van een actor: *slechts eigenschap* ja, met de actor als `genoemd_begrip`.
   - Een regeling: volg de modelleerafspraken van [Beleidskader](../../../kennismodel/motivatie/beleidskader-modelleerafspraken.md); een los artikel is *buiten dit model*.
4. Vul waar nodig de extra velden in:
   - `genoemd_begrip` bij *slechts eigenschap*, *eigen identiteit* nee (het geheel), *zelfstandige specialisatie* nee (het bredere begrip) of *waarneembare vorm* (het object);
   - `archimate_buiten_model` bij *buiten dit model*;
   - de eigenschappen van het type uit zijn modelleerafspraken, zoals `kernobject`, `gemma_generiek` en de indelingsvelden `domein`, `afnemer`, `doelgroep` en `regelgever`, naast `taakveld` en `beleidsdomein`. Een relatie naar een generiek object noemt zijn specialisatie zonder pagina in `via`.
5. Leg de beoordeling vast in `beoordelingen/begrippen/<id>.yaml` (schema `schemas/beoordeling.schema.json`, zie skill `gemma-archimate-model-beoordelen`) en draai `uv run python tools/afleiden.py`. De uitkomst is bindend.
6. Is de uitkomst `conflict` of staat `voorleggen` aan, dan leg je het begrip voor aan de redacteur, met de redenen uit de uitkomst. Pas je antwoorden niet aan om een conflict weg te werken, tenzij een antwoord aantoonbaar fout was.

## Vragenlijst

Gegenereerd uit de beslistabel (`uv run python tools/bepaal_type.py markdown --schrijf`); dezelfde vragen met voorbeelden en herkomst, en de stappentabel, staan in [kenmerken en beslistabel](../../../kennismodel/kenmerken-en-beslistabel.md).

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
<!-- EINDE gegenereerd -->

Een begrip met uitkomst "geen element" wordt niet weggelaten: het blijft in de begrippenlijst van het onderwerp staan, met de uitkomst en de reden.
