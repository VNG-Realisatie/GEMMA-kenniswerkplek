---
id: gemma-kennismodel
type: analyse
titel: Elementtypen, kenmerken en het GEMMA-kennismodel
bijgewerkt: '2026-10-01'
bronnen:
- 2026-vng-over-gemma
---

# Elementtypen, kenmerken en het GEMMA-kennismodel

Bron: [tekst](../../../sources/raw/2026-vng-over-gemma.md) · [origineel (xml)](../../../sources/raw/2026-vng-over-gemma.xml) · [online](https://raw.githubusercontent.com/VNG-Realisatie/Over-GEMMA-Archi-repository/Master/export/Over%20GEMMA.xml)

Deze analyse vergelijkt de elementtypen van deze wiki, hun kenmerken en de beslistabel met het GEMMA-kennismodel uit Over GEMMA. Ze legt de besluiten van de redacteur vast en noemt wat er nog open is. Deze pagina is de bronanalyse van Over GEMMA: de regelnummers verwijzen naar de tekst hierboven. De wijzigingen in de beslistabel zijn besloten maar nog niet doorgevoerd; ze staan als punt in de todo van deze wiki.

## Besluiten van de redacteur

| Datum | Besluit |
|---|---|
| 2026-09-30 | Drempel: per type één kernrelatie die ja moet zijn, plus hoogstens één nee op de overige drempelcriteria. |
| 2026-09-30 | Nieuwe kenmerken *voert gedrag uit*, *afnemer*, *gerealiseerd door*, *leidt tot gedrag* en *omvat aanbod*; *relaties* en *meerdere vervullers* vervallen. |
| 2026-09-30 | *Betekenis in onderwerp* wordt een poort: een begrip dat bij een ander onderwerp hoort, krijgt hier een verwijzing en wordt daar beoordeeld. |
| 2026-09-30 | Bedrijfssamenwerking en kanaal worden paginatype. Kanalen vormen één centrale set; een onderwerp koppelt alleen een dienst aan een bestaand kanaal. |
| 2026-09-30 | Product blijft paginatype. Business Interaction blijft herkend en wordt per geval voorgelegd. Representatie en locatie worden een vaste uitkomst zonder pagina. |
| 2026-10-01 | Over GEMMA is bron. Deze wiki volgt de namen en definities van het GEMMA-kennismodel waar die passen. |
| 2026-10-01 | Een rol mag ook aan een bedrijfsproces worden toegewezen, niet alleen aan een bedrijfsfunctie. GEMMA doet dat zelf op het niveau van het deelproces (regel 599); de procesarchitectuur van GEMMA is abstract uitgewerkt, en er is geen andere reden om de relatie weg te laten. |
| 2026-10-01 | Een actor wordt alleen via een rol aan gedrag en objecten gekoppeld, zoals in GEMMA (regel 914). De kernrelatie van een actor wordt *vervult een rol*. |
| 2026-10-01 | Een relatie van rol naar object wordt gesplitst: wat de rol met het object ís, wordt toegang met een getypeerde naam (raadpleger, beheerder, eigenaar, verantwoordelijke; de lijst volgt de indeling uit de Wet basisregistraties en wordt nog vastgesteld). Een handeling, zoals aanvragen of afgeven, wordt een toewijzing van de rol aan een proces dat het object gebruikt of maakt. |
| 2026-10-01 | Een bedrijfsfunctie bedient een bedrijfsproces, zoals in GEMMA (regel 920); de aggregatie van functie naar proces vervalt. Een proces mag meerdere functies gebruiken. |
| 2026-10-01 | Een bedrijfsproces krijgt het veld *procesniveau* (bedrijfsproces of deelproces). Een deelproces krijgt een pagina als het de procesdrempel haalt, en hangt met een aggregatie onder een bedrijfsproces ("is opgebouwd uit", regel 396). Processtap en handeling worden nooit een pagina. |
| 2026-10-01 | Een concrete wet of verordening wordt een beleidskader (Driver, regel 448) in een nieuwe map `motivatie/` naast `bedrijfsarchitectuur/`, met "geeft grondslag aan" naar GEMMA-kwaliteitsdoelen waar dat aanwijsbaar is (regel 458). Alleen beleidskaders; andere motivatietypen blijven buiten dit model. Het generieke bedrijfsobject Regeling blijft voor het vaststellen, wijzigen en bekendmaken, met een associatie naar het beleidskader. |
| 2026-10-01 | De paginatypen bedrijfsdienst en bedrijfsgebeurtenis en hun mappen worden hernoemd naar dienst en gebeurtenis; de nieuwe typen heten bedrijfssamenwerking en kanaal. Engelse ArchiMate-sleutels blijven. Dit gaat mee met de herziening van de beslistabel. |
| 2026-10-01 | Na de herziening worden alle bestaande elementen opnieuw beoordeeld, met een run per onderwerp. Elke wijziging van type, relatie of status wordt apart voorgelegd; een element waarvan alleen een kenmerk is aangevuld, houdt zijn status. |
| 2026-10-01 | Een beleidskader is een landelijke wet of VNG-modelverordening die een taak, bevoegdheid of plicht van de gemeente regelt. Kernrelatie: een associatie "is grondslag voor" naar minstens één proces, dienst of product. Lokale verordeningen en beleidsnota's blijven bron; een wet die alleen een definitie levert ook; een losse norm uit een artikel blijft buiten het model. Kenmerken voor de beslistabel: herkenbaar, gemeentelijk, in werking, regelt een taak, bevoegdheid of plicht van de gemeente. |

## Het GEMMA-kennismodel

Het kennismodel is volgens GEMMA "de invulling van de ArchiMate conventie voor de informatievoorziening van het gemeentelijk domein", met "alle in de GEMMA gebruikte ArchiMate element- en relatietypen" (regel 802-803). De uitgebreide view voegt "gewenste uitbreidingen, zoals diensten en producten" toe (regel 862). De procesarchitectuur, de modellering van product en dienst en de modellering van bedrijfsobject en bedrijfsfunctie staan in eigen views.

| Paginatype in deze wiki | GEMMA-naam | ArchiMate | GEMMA-definitie | Herkomst | Regel | Verschil |
|---|---|---|---|---|---|---|
| bedrijfsobject | Bedrijfsobject | Business Object | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | GEMMA | 182 | Gelijk. Deze wiki toetst strenger: het object wordt operationeel bewerkt. |
| bedrijfsobject (contract) | Afspraak | Contract | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. | GEMMA | 246 | Naam verschilt. Alleen in de view over product en dienst, niet in de twee kennismodel-views. |
| product | Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | GEMMA | 76 | Een product bundelt diensten en afspraken, geen bedrijfsobjecten (regel 257). |
| bedrijfsdienst | Dienst | Business Service | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | NORA | 243 | Naam verschilt. |
| bedrijfsproces | Bedrijfsproces | Business Process | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | GEMMA | 320 | Gelijk. GEMMA kent daaronder deelproces, processtap en handeling. |
| bedrijfsfunctie | Bedrijfsfunctie | Business Function | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | GEMMA | 325 | Gelijk. |
| bedrijfsgebeurtenis | Gebeurtenis | Business Event | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. | GEMMA | 874 | Naam verschilt. GEMMA legt de nadruk op de gevolgen, deze wiki op het ogenblikkelijke karakter. |
| actor | Actor | Business Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | GEMMA | 572 | Gelijk. |
| rol | Rol | Business Role | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | ArchiMate | 569 | Gelijk. |
| samenwerkingsverband (besloten) | Bedrijfssamenwerking | Business Collaboration | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. | ArchiMate | 817 | GEMMA spreekt over rollen, niet over partijen, en noemt tijdelijkheid. |
| kanaal (besloten) | Kanaal | Business Interface | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. | NORA | 870 | Gelijk. |
| annotatie `data_object` | Data-object | Data Object | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. | GEMMA | 897 | Gelijk. In GEMMA realiseert een data-object een bedrijfsobject (regel 971). |
| herkend: Business Interaction | — | Business Interaction | — | — | — | Niet in het kennismodel; consistent met voorleggen. |
| geen pagina: Representation, Location | — | Representation, Location | — | — | — | Niet in het kennismodel. |
| bedrijfsobject (governance-object: wet of verordening als geheel); wordt beleidskader | Beleidskader | Driver | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | NORA | 448 | Besloten 2026-10-01: een concrete wet of verordening wordt een beleidskader in `motivatie/`; het object Regeling blijft. |
| buiten dit model: losse norm (Requirement of Constraint) | Standaard; Implicatie | Constraint; Requirement | Constraint is in GEMMA alleen een standaard; Requirement is een implicatie van een principe of een eis aan een informatiesysteem. | Wikipedia; GEMMA | 18, 450 | GEMMA heeft geen type voor een wettelijke norm. |
| buiten dit model: vermogen, groepering, doel | Capability; Domein, Beleidsdomein; Kwaliteitsdoel | Capability; Grouping; Goal | — | — | 565, 183, 54, 447 | GEMMA gebruikt ze, deze wiki modelleert ze niet. De mappen per beleidsdomein volgen dezelfde Iv3-indeling als GEMMA (regel 193). |

Ook bevestigend: GEMMA kent een rol *Klant (intern of extern)*, "de ontvanger van producten of diensten" (regel 567). Dat is de afnemer uit de nieuwe kenmerken. Het begrip *Doelgroep* is in GEMMA een rol die applicatieservices ordent naar gebruikersgroep (regel 214). Dat is iets anders dan een doelgroep in deze wiki (een indeling van een actor, zoals minima).

## Kenmerkenmatrix: huidige situatie

Rijen zijn de kenmerken, kolommen de elementtypen met hun GEMMA-naam. De laatste vijf typen herkent de beslistabel wel, maar ze hebben geen paginatype: zo'n begrip wordt altijd voorgelegd.

Legenda: **T** bepaalt het type · **K** kernrelatie, moet ja zijn · **D** telt in de drempel · **P** poort voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger of annotatie) · **x** moet nee zijn voor dit type · **E** vaste uitkomst zonder pagina.

| Kenmerk | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol | Bedrijfssamenwerking | Kanaal | Interactie | Representatie | Locatie |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Scope** | | | | | | | | | | | | | | |
| herkenbaar | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| gemeentelijk | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| buiten kernlagen (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| **Zelfstandigheid** | | | | | | | | | | | | | | |
| betekenis in onderwerp | D | D | D | D | D | D | D | D | D |  |  |  |  |  |
| slechts eigenschap (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| eigen identiteit | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| relaties | D | D | D | D |  |  | D | D | D |  |  |  |  |  |
| zelfstandig beleidsbegrip | S | S | S | S | S | S | S | S | S |  |  |  |  |  |
| **Aard** | | | | | | | | | | | | | | |
| gedrag |  |  |  | T | T | T | T |  |  |  |  | T |  |  |
| handelende partij |  |  |  |  |  |  |  | T |  |  |  |  |  |  |
| hoedanigheid |  |  |  |  |  |  |  |  | T |  |  |  |  |  |
| samenwerkingsverband |  |  |  |  |  |  |  |  |  | T |  |  |  |  |
| toegangspunt |  |  |  |  |  |  |  |  |  |  | T |  |  |  |
| plaats |  |  |  |  |  |  |  |  |  |  |  |  |  | T |
| aanbod als geheel |  |  | T |  |  |  |  |  |  |  |  |  |  |  |
| **Partij** | | | | | | | | | | | | | | |
| los van verantwoordelijkheid |  |  |  |  |  |  |  | T | T |  |  |  |  |  |
| meerdere vervullers |  |  |  |  |  |  |  |  | D |  |  |  |  |  |
| **Soort gedrag** | | | | | | | | | | | | | | |
| per keer doorlopen |  |  |  |  | T |  |  |  |  |  |  |  |  |  |
| gegroepeerd gedrag |  |  |  |  |  | T |  |  |  |  |  |  |  |  |
| toestandsverandering |  |  |  |  |  |  | T |  |  |  |  |  |  |  |
| aangeboden gedrag |  |  |  | T |  |  |  |  |  |  |  |  |  |  |
| gezamenlijk gedrag |  |  |  |  |  |  |  |  |  |  |  | T |  |  |
| **Gedrag** | | | | | | | | | | | | | | |
| toegewezen partij |  |  |  |  | D | D |  |  |  |  |  |  |  |  |
| gebruikt objecten |  |  |  |  | D | D |  |  |  |  |  |  |  |  |
| aanleiding |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| benoembaar resultaat |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| herhaald uitgevoerd |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| eigen normering |  |  |  |  | D |  |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  | D |  |  |  |  |  |  |  |  |
| **Passief** | | | | | | | | | | | | | | |
| onderscheidbare exemplaren | D | D | D |  |  |  |  | A | A |  |  |  |  |  |
| levenscyclus | D | D |  |  |  |  |  | A | A |  |  |  |  |  |
| wordt bewerkt | D | D |  |  |  |  |  | A | A |  |  |  |  |  |
| afspraak | x | T |  |  |  |  |  |  |  |  |  |  |  |  |
| waarneembare vorm | x | x |  |  |  |  |  |  |  |  |  |  | T |  |
| geautomatiseerd verwerkt | A | A | A | A | A | A | A | A | A |  |  |  |  |  |

Aantal getelde drempelcriteria per type, en hoeveel daarvan ja moeten zijn:

| | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol |
|---|---|---|---|---|---|---|---|---|---|
| criteria in de drempel | 5 | 5 | 3 | 2 | 7 | 4 | 2 | 2 | 3 |
| minimaal ja | 4 | 4 | 2 | 1 | 6 | 3 | 1 | 1 | 2 |

## Bevindingen

- **Ongelijke drempel.** Dienst, gebeurtenis en actor tellen twee criteria, waarvan er één nee mag zijn. Een proces moet er zes van zeven halen.
- **Overlap tussen kenmerken.** *Relaties* telt bij het bedrijfsobject naast *wordt bewerkt*, dat dezelfde toegangsrelatie meet. *Per keer doorlopen* vraagt al naar een resultaat, dat daarna nog eens telt als *benoembaar resultaat*. *Meerdere vervullers* is vrijwel altijd ja; het onderscheid tussen actor en rol maakt *los van verantwoordelijkheid* al.
- **Overlap tussen typen.** Bedrijfsobject en afspraak verschillen alleen op *afspraak*, actor en rol alleen op *los van verantwoordelijkheid*; dat klopt met ArchiMate. Dienst, gebeurtenis en actor hebben dezelfde drempel, en daarin staat niets wat typisch is voor een dienst of gebeurtenis.
- **Ontbrekende kenmerken.** Bij een dienst wordt niet gevraagd naar de afnemer en niet naar het gedrag dat de dienst realiseert. Bij een gebeurtenis wordt niet gevraagd welk gedrag zij start. Bij een product wordt niet gevraagd waaruit het bestaat.
- **Eenzijdige conflictcontrole.** De beslistabel ziet "geen gedrag, wel een soort gedrag" als conflict, maar niet het omgekeerde: een gedragsbegrip met *afspraak* ja wordt zonder melding een proces.
- **Representatie wordt elke keer voorgelegd**, terwijl de redacteur al besliste hoe het moet: vermelden bij het object, geen pagina (Register van begraven lijken, 30 september 2026).

## Kenmerkenmatrix: besloten opzet

Elk type krijgt één kernrelatie (**K**). Die relaties volgen het GEMMA-kennismodel: een dienst wordt gerealiseerd door een proces of functie (regel 925, 921), een gebeurtenis triggert een proces (regel 915), een kanaal is toegewezen aan een dienst (regel 910), een product bundelt diensten en afspraken (regel 257), een rol wordt toegewezen aan een functie (regel 918) en, volgens het besluit van 1 oktober, ook aan een proces.

Legenda: **T** bepaalt het type · **K** kernrelatie, moet ja zijn · **D** telt in de drempel · **P** poort voor alle typen · **S** specialisatieniveau · **A** aanvulling (tegenhanger of annotatie) · **x** moet nee zijn voor dit type · **E** vaste uitkomst zonder pagina.

| Kenmerk | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol | Bedrijfssamenwerking | Kanaal | Interactie (herkend) | Geen pagina |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Scope en afhankelijkheid** | | | | | | | | | | | | | |
| herkenbaar | P | P | P | P | P | P | P | P | P | P | P | P | P |
| gemeentelijk | P | P | P | P | P | P | P | P | P | P | P | P | P |
| buiten kernlagen (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P |
| slechts eigenschap (moet nee) | P | P | P | P | P | P | P | P | P | P | P | P | P |
| eigen identiteit | P | P | P | P | P | P | P | P | P | P | P | P | P |
| betekenis in onderwerp (gewijzigd) | P | P | P | P | P | P | P | P | P | P | P | P | P |
| relaties (vervalt) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| zelfstandig beleidsbegrip | S | S | S | S | S | S | S | S | S | S | S |  |  |
| **Aard** | | | | | | | | | | | | | |
| gedrag |  |  |  | T | T | T | T |  |  |  |  | T |  |
| handelende partij |  |  |  |  |  |  |  | T |  |  |  |  |  |
| hoedanigheid |  |  |  |  |  |  |  |  | T |  |  |  |  |
| samenwerkingsverband (gewijzigd) |  |  |  |  |  |  |  |  |  | T |  |  |  |
| toegangspunt (gewijzigd) |  |  |  |  |  |  |  |  |  |  | T |  |  |
| plaats (gewijzigd) |  |  |  |  |  |  |  |  |  |  |  |  | E |
| aanbod als geheel |  |  | T |  |  |  |  |  |  |  |  |  |  |
| **Partij** | | | | | | | | | | | | | |
| los van verantwoordelijkheid |  |  |  |  |  |  |  | T | T |  |  |  |  |
| meerdere vervullers (vervalt) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| voert gedrag uit (nieuw) |  |  |  |  |  |  |  | K | K | K | K |  |  |
| **Soort gedrag** | | | | | | | | | | | | | |
| per keer doorlopen (gewijzigd) |  |  |  |  | T |  |  |  |  |  |  |  |  |
| gegroepeerd gedrag |  |  |  |  |  | T |  |  |  |  |  |  |  |
| toestandsverandering |  |  |  |  |  |  | T |  |  |  |  |  |  |
| aangeboden gedrag |  |  |  | T |  |  |  |  |  |  |  |  |  |
| gezamenlijk gedrag |  |  |  |  |  |  |  |  |  |  |  | T |  |
| **Gedrag** | | | | | | | | | | | | | |
| toegewezen partij (gewijzigd) |  |  |  | D | K | K |  |  |  |  |  |  |  |
| gebruikt objecten |  |  |  |  | D | D |  |  |  |  |  |  |  |
| aanleiding |  |  |  |  | D |  |  |  |  |  |  |  |  |
| benoembaar resultaat (gewijzigd) |  |  |  | D | D |  |  |  |  |  |  |  |  |
| komt herhaald voor (gewijzigd) |  |  |  |  | D |  | D |  |  |  |  |  |  |
| eigen normering |  |  |  |  | D |  |  |  |  |  |  |  |  |
| stabiel over tijd |  |  |  |  |  | D |  |  |  |  |  |  |  |
| afnemer (nieuw) |  |  | D | D |  |  |  |  |  |  |  |  |  |
| gerealiseerd door (nieuw) |  |  |  | K |  |  |  |  |  |  |  |  |  |
| leidt tot gedrag (nieuw) |  |  |  |  |  |  | K |  |  |  |  |  |  |
| **Passief** | | | | | | | | | | | | | |
| onderscheidbare exemplaren | D | D | D |  |  |  |  | A | A |  |  |  |  |
| levenscyclus | D | D |  |  |  |  |  | A | A |  |  |  |  |
| wordt bewerkt (gewijzigd) | K | K |  |  |  |  |  | A | A |  |  |  |  |
| omvat diensten en afspraken (nieuw) |  |  | K |  |  |  |  |  |  |  |  |  |  |
| afspraak | x | T |  |  |  |  |  |  |  |  |  |  |  |
| waarneembare vorm (gewijzigd) | x | x |  |  |  |  |  |  |  |  |  |  | E |
| geautomatiseerd verwerkt | A | A | A | A | A | A | A | A | A |  |  |  |  |

Toelichting bij de gewijzigde en nieuwe kenmerken:

- **betekenis in onderwerp** wordt een poort. Nee betekent: verwijzen naar het onderwerp waar het begrip hoort.
- **samenwerkingsverband** wordt het paginatype Bedrijfssamenwerking: een samenstelling van rollen die samen gedrag uitvoeren, ook tijdelijk. Een verband met eigen rechtspersoon, zoals de GGD, blijft een actor.
- **toegangspunt** wordt het paginatype Kanaal, als één centrale set.
- **plaats** en **waarneembare vorm** worden een vaste uitkomst zonder pagina. Een gebiedsindeling blijft een bedrijfsobject; een vorm wordt vermeld bij het object waarvan het de vorm is.
- **voert gedrag uit**: is de partij toegewezen aan aanwijsbaar gemeentelijk gedrag, of ontsluit het kanaal een aanwijsbare dienst?
- **per keer doorlopen** zonder de deelvraag naar een resultaat; dat telt apart.
- **toegewezen partij** is de kernrelatie van proces en functie, en telt ook bij een dienst.
- **benoembaar resultaat** telt ook bij een dienst: wat krijgt de afnemer?
- **komt herhaald voor** (was: herhaald uitgevoerd) telt ook bij een gebeurtenis.
- **afnemer**: is er een afnemer buiten de uitvoerder aanwijsbaar, de klant intern of extern?
- **gerealiseerd door**: is er een proces of functie aanwijsbaar dat de dienst uitvoert?
- **leidt tot gedrag**: start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag?
- **omvat diensten en afspraken**: bestaat het product uit aanwijsbare diensten en afspraken?
- **wordt bewerkt** is de kernrelatie van bedrijfsobject en afspraak.

Het aantal kenmerken gaat van 35 naar 38. De set wordt niet kleiner, maar elk kenmerk telt voortaan bij een type waarvoor het onderscheidend is.

## Besloten beslistabel

| Stap | Als | Dan | Status |
|---|---|---|---|
| 1 Scope | niet herkenbaar of niet gemeentelijk | buiten scope, met reden | ongewijzigd |
| 1 Scope | buiten kernlagen | buiten dit model, met het ArchiMate-type | ongewijzigd |
| 2 Afhankelijk | slechts eigenschap | eigenschap van het genoemde begrip; geen pagina | ongewijzigd |
| 2 Afhankelijk | niet eigen identiteit | onderdeel of deelstap; relaties opgetild | ongewijzigd |
| 2 Afhankelijk | niet betekenis in onderwerp | verwijzing in de begrippenlijst, beoordelen in het onderwerp waar het hoort | nieuw |
| 3 Consistentie | gedragskenmerken ja, maar niet gedrag | conflict, voorleggen | nieuw |
| 3 Consistentie | partijkenmerken ja, maar geen partij, hoedanigheid of samenwerkingsverband | conflict, voorleggen | nieuw |
| 3 Consistentie | afspraak of waarneembare vorm ja, naast een aard | conflict, voorleggen | nieuw |
| 4 Aard | handelende partij én hoedanigheid | los van verantwoordelijkheid ja: Actor, nee: Rol | ongewijzigd |
| 4 Aard | meer dan één aard (behalve actor en rol) | conflict, voorleggen | ongewijzigd |
| 4 Aard | handelende partij | Actor; conflict als niet los van verantwoordelijkheid | ongewijzigd |
| 4 Aard | hoedanigheid | Rol; conflict als los van verantwoordelijkheid | ongewijzigd |
| 4 Aard | samenwerkingsverband | Bedrijfssamenwerking | gewijzigd |
| 4 Aard | aanbod als geheel | Product | ongewijzigd |
| 4 Aard | toegangspunt | Kanaal: koppelen aan de centrale set; een nieuw kanaal alleen na besluit van de redacteur | gewijzigd |
| 4 Aard | plaats | fysieke plaats; geen pagina | gewijzigd |
| 4 Gedrag | gedrag en precies één soort gedrag | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis of Dienst; Business Interaction: herkend, voorleggen | ongewijzigd |
| 4 Gedrag | gedrag, maar geen of meer dan één soort | conflict, voorleggen | ongewijzigd |
| 4 Passief | waarneembare vorm | vorm van het genoemde object; geen pagina, vermelden bij dat object | gewijzigd |
| 4 Passief | afspraak | Afspraak (Contract) | gewijzigd (naam) |
| 4 Passief | overig passief begrip | Bedrijfsobject | ongewijzigd |
| 5 Drempel | kernrelatie van het type nee | geen element; voorleggen met de ontbrekende relatie | nieuw |
| 5 Drempel | van de overige drempelcriteria meer dan één nee | geen element; voorleggen met de ontbrekende criteria | gewijzigd |
| 6 Specialisatie | niet zelfstandig beleidsbegrip, met genoemd begrip | specialisatie zonder pagina; relaties opgetild | ongewijzigd |
| 6 Specialisatie | niet zelfstandig beleidsbegrip, zonder genoemd begrip | voorleggen: noem het bredere begrip | ongewijzigd |
| Aanvulling | Actor of Rol met exemplaren, levenscyclus en wordt bewerkt | ook een objectpagina (tegenhanger) | ongewijzigd |
| Aanvulling | Dienst waarvan het realiserende proces nog geen pagina heeft | signaal: proces als kandidaat voorleggen | nieuw |
| Aanvulling | Gebeurtenis waarvan het gestarte gedrag nog geen pagina heeft | signaal: proces als kandidaat voorleggen | nieuw |
| Aanvulling | geautomatiseerd verwerkt | annotatie data-object | ongewijzigd |

## Relaties: kennismodel en wiki

Het kennismodel legt per typepaar vast welke relatie GEMMA gebruikt. Deze wiki staat de volledige ArchiMate-set toe. Het aantal is het aantal relatierijen op de elementpagina's op 1 oktober 2026.

| Relatie in deze wiki | Aantal | In het kennismodel | Regel |
|---|---|---|---|
| bedrijfsproces → toegang → bedrijfsobject | 18 | ja | 927 |
| bedrijfsobject → associatie of specialisatie → bedrijfsobject | 13 | ja | 905-906 |
| gebeurtenis → triggering → bedrijfsproces | 3 | ja | 915 |
| actor → toewijzing → rol | 2 | ja | 914 |
| bedrijfsproces → specialisatie → bedrijfsproces | 1 | ja | 922 |
| rol → toewijzing → bedrijfsproces | 7 | ja, op het niveau van deelproces; besloten op 1 oktober | 599 |
| rol → associatie → bedrijfsobject | 20 | anders: rol → toegang → bedrijfsobject ("heeft toegang tot") | 916 |
| actor → associatie → bedrijfsobject | 17 | nee: alleen via de rol | 914, 916 |
| actor → toewijzing → bedrijfsproces | 6 | nee: actor → toewijzing → rol | 914 |
| actor → toewijzing → gebeurtenis | 1 | nee | — |
| bedrijfsfunctie → aggregatie → bedrijfsproces | 8 | nee: functie en proces bedienen elkaar | 920, 926 |
| dienst → toegang → bedrijfsobject | 2 | nee | — |
| rol → toewijzing → dienst | 1 | nee: kanaal → toewijzing → dienst | 910 |
| bedrijfsobject → aggregatie → bedrijfsobject | 1 | nee | — |
| bedrijfsproces of bedrijfsfunctie → realisatie → dienst | 0 | ja | 925, 921 |
| dienst → bediening → bedrijfsproces | 0 | ja | 912 |
| bedrijfsproces → triggering → gebeurtenis | 0 | ja | 924 |
| kanaal → toewijzing → dienst; kanaal → bediening → rol | 0 | ja | 910-911 |
| bedrijfssamenwerking → aggregatie → rol | 0 | ja | 913 |
| data-object → realisatie → bedrijfsobject | 0 | ja | 971 |

## Inhoudelijke gevolgen

Deze gevolgen leidden tot de besluiten van 1 oktober 2026 bovenaan de pagina.

- **Rol aan proces.** Het besluit van 1 oktober bevestigt wat de wiki al doet: zeven toewijzingen van een rol aan een proces blijven staan. *Toegewezen partij* blijft de kernrelatie van een proces.
- **Actor via de rol.** In GEMMA wordt een actor alleen aan een rol toegewezen (regel 914). In deze wiki staan zes actoren direct aan een proces en één aan een gebeurtenis, en zeventien actoren met een associatie naar een object. Volgt de wiki GEMMA, dan komt er steeds een rol tussen. Dan wordt de kernrelatie van een actor *vervult een rol*.
- **Rol en object.** GEMMA gebruikt "heeft toegang tot", met als betekenissen verantwoordelijk voor, eigenaar van, beheerder van en raadpleger van (regel 916). De twintig associaties van rol naar object passen daar grotendeels in.
- **Functie en proces.** GEMMA laat functie en proces elkaar bedienen (regel 920, 926) en groepeert processen in een procescluster (regel 419). De acht aggregaties van functie naar proces wijken daarvan af. Lijkbezorging en Participatie gedragen zich hier als procescluster.
- **Procesniveau.** GEMMA onderscheidt procescluster, ketenproces, bedrijfsproces, deelproces, processtap en handeling (regel 409-421, 564). Een deelproces wordt binnen één organisatorische eenheid uitgevoerd en levert een bijdrage aan een dienst (regel 388); een processtap ligt binnen één bedrijfsfunctie (regel 387). De beslistabel vraagt nu niet op welk niveau een proces ligt. Schouwen lijk, Opgraven lijk en Ruimen graf kunnen daardoor deelprocessen zijn in GEMMA-termen.
- **Product.** Een product bundelt in GEMMA diensten en afspraken (regel 257) en bedient de klant (regel 596). Het nieuwe kenmerk heet daarom *omvat diensten en afspraken*, niet meer *omvat aanbod* met objecten.
- **Afspraak.** Contract heet in GEMMA Afspraak. De twee elementen van dit type, Uitvoeringsovereenkomst en Grafrecht, blijven inhoudelijk gelijk.
- **Wetgeving.** Het GEMMA-kennismodel noemt wetten en regelgeving als beleidskader in de motivatielaag (regel 448). Het GEMMA-architectuurmodel heeft daarnaast een bedrijfsobject Regeling, overgenomen uit het GGM, waaraan het element Regeling van deze wiki gekoppeld is. GEMMA gebruikt dus beide: het beleidskader als motivatie, de regeling als object dat de gemeente vaststelt, wijzigt en bekendmaakt. De motivatielaag van het GEMMA-model bevat nog geen beleidskaders, alleen kernwaarden.
- **Namen.** De paginatypen bedrijfsdienst, bedrijfsgebeurtenis en contract heten in GEMMA Dienst, Gebeurtenis en Afspraak. In de criteria van deze wiki staan nu de GEMMA-namen en -definities. De technische namen van paginatypen en mappen zijn nog niet aangepast.

## Open vragen

Geen. De vragen van 1 oktober 2026 zijn beantwoord; zie de besluiten bovenaan. De namen voor de toegang tot een object (verantwoordelijkheden van een rol en handelingen van een functie of proces) zijn uitgewerkt en besloten in [Toegang tot een bedrijfsobject](gegevensrollen.md).
