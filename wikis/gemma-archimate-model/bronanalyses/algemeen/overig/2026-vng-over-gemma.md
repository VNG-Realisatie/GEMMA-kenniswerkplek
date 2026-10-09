---
id: 2026-vng-over-gemma
type: bronanalyse
onderwerp: algemeen
bronnen:
- 2026-vng-over-gemma
relevant: ja
bijgewerkt: '2026-10-08'
---

# Over GEMMA (kennismodel en modelleerafspraken)

Bron: [tekst](../../../../../sources/raw/2026-vng-over-gemma.md) · [origineel (xml)](../../../../../sources/raw/2026-vng-over-gemma.xml) · [online](https://raw.githubusercontent.com/VNG-Realisatie/Over-GEMMA-Archi-repository/Master/export/Over%20GEMMA.xml)

## Samenvatting

Regelnummers verwijzen naar de tekst van deze bron. Verplaatst uit de analyse Elementtypen, kenmerken en het GEMMA-kennismodel (2026-10-08).

Het kennismodel is volgens GEMMA "de invulling van de ArchiMate conventie voor de informatievoorziening van het gemeentelijk domein", met "alle in de GEMMA gebruikte ArchiMate element- en relatietypen" (regel 802-803). De uitgebreide view voegt "gewenste uitbreidingen, zoals diensten en producten" toe (regel 862). De procesarchitectuur, de modellering van product en dienst en de modellering van bedrijfsobject en bedrijfsfunctie staan in eigen views.

Ook bevestigend: GEMMA kent een rol *Klant (intern of extern)*, "de ontvanger van producten of diensten" (regel 567). Dat is de afnemer uit de nieuwe kenmerken. Het begrip *Doelgroep* is in GEMMA een rol die applicatieservices ordent naar gebruikersgroep (regel 214). Dat is iets anders dan een doelgroep in deze wiki (een indeling van een actor, zoals minima).

De elementtypen van het kennismodel naast de paginatypen van deze wiki:

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
| herkend: Business Interaction (sinds 2026-10-08 paginatype bedrijfsinteractie) | — | Business Interaction | — | — | — | Niet in het kennismodel; in het GEMMA-model wel, als *Ketensamenwerking*. |
| geen pagina: Representation, Location | — | Representation, Location | — | — | — | Niet in het kennismodel. |
| bedrijfsobject (governance-object: wet of verordening als geheel); wordt beleidskader | Beleidskader | Driver | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | NORA | 448 | Besloten 2026-10-01: een concrete wet of verordening wordt een beleidskader in `motivatie/`; het object Regeling blijft. |
| buiten dit model: losse norm (Requirement of Constraint) | Standaard; Implicatie | Constraint; Requirement | Constraint is in GEMMA alleen een standaard; Requirement is een implicatie van een principe of een eis aan een informatiesysteem. | Wikipedia; GEMMA | 18, 450 | GEMMA heeft geen type voor een wettelijke norm. |
| buiten dit model: vermogen, groepering, doel | Capability; Domein, Beleidsdomein; Kwaliteitsdoel | Capability; Grouping; Goal | — | — | 565, 183, 54, 447 | GEMMA gebruikt ze, deze wiki modelleert ze niet. De mappen per beleidsdomein volgen dezelfde Iv3-indeling als GEMMA (regel 193). |

## Kernbegrippen

Zie de tabel onder Samenvatting: per elementtype de GEMMA-naam, de definitie en de regel.

## Relaties

Geen relatietabel: de bron beschrijft typen van elementen en relaties, geen begrippen van gemeenten.

## Relevantie voor de architectuur

Levert de namen en definities van de elementtypen (skill gemma-archimate-model-criteria) en het kennismodel dat de export naar Archi meeneemt (`wiki.yaml` `kennismodel`). De vergelijking met de wiki staat in ARCHITECTURE.md, sectie [4.1 Elementtypen en kenmerken](../../../ARCHITECTURE.md#41-elementtypen-en-kenmerken), en in de [modelleerafspraken per elementtype](../../../kennismodel/README.md).

## Citaten

> de invulling van de ArchiMate conventie voor de informatievoorziening van het gemeentelijk domein (regel 802-803)

> gewenste uitbreidingen, zoals diensten en producten (regel 862)
