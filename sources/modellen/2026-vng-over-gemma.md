# Over GEMMA

Modellen die beschrijven hoe de GEMMA is opgezet, zoals het kennismodel met de gebruikte ArchiMate-concepten en -modellering en het portfoliomodel met de verzameling van producten waarmee de GEMMA is opgebouwd

Bron: ArchiMate Open Exchange (AMEFF), 368 elementen, 698 relaties, 53 views. Deze Markdown is een letterlijke weergave per view van de elementen (type, naam, documentatie, eigenschappen) en relaties; de opmaak van de diagrammen ontbreekt.

## GEMMA modellering buitengemeentelijk

Modellering van gegevensuitwisselingen met buitengemeentelijke voorzieningen.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationComponent | Buitengemeentelijke afnemer | Een landelijke- of sectorale afnemer van een gemeentelijke applicatiedienst. |  |
| ApplicationComponent | Buitengemeentelijke aanbieder | Een landelijke- of sectorale aanbieder van een voor gemeenten relevante voorziening |  |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| ApplicationComponent | Referentieafnemer | Een referentiecomponent voor het afnemen van services | Bron: GEMMA |
| ApplicationComponent | Referentieaanbieder | Een referentiecomponent voor het aanbieden van services | Bron: GEMMA |
| Grouping | Buitengemeentelijk stelsel | Groep van landelijke- of sectorale informatievoorzieningen | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Buitengemeentelijke aanbieder | Composition | Verplicht / Aanbevolen | Applicatie-interface |  |
| Referentieaanbieder | Composition | Verplicht / Aanbevolen | Applicatie-interface |  |
| Buitengemeentelijk stelsel | Aggregation |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatie-interface | Serving | Verplicht / Aanbevolen | Buitengemeentelijke afnemer |  |
| Applicatie-interface | Serving | Verplicht / Aanbevolen | Referentieafnemer |  |

### Notities

- GEMMA kennismodel uitgebreid
- GEMMA specialisaties applicatiecomponent
- Voorschrijven van koppelings- of API-standaarden via de applicatie-interface
- GEMMA modellering standaardenlijst

## GEMMA-GGM kennismodel

Kennismodel van het GEMMA-GGM model met de relatie tussen de GGM data-objecten en de GEMMA bedrijfsobjecten

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| DataObject | GEMMA-GGM ArchiMate-model |  |  |
| DataObject | GGM data-object |  |  |
| BusinessObject | GEMMA bedrijfsobject | Kopie van GGM data-object - ggm-guid Van GEMMA -Object ID |  |
| Grouping | Beleidsdomein | Een afgebakend gebied binnen gemeenten waarvoor specifieke beleidsmaatregelen, regels en verantwoordelijkheden gelden. De GEMMA en het Gemeentelijk GegevensModel gebruiken dezelfde, op IV3 gebaseerde, indeling. | URL: https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3; Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| GGM data-object | Realization | realiseert | GEMMA bedrijfsobject |  |
| GGM data-object | Association | associaties | GGM data-object |  |
| GGM data-object | Specialization | specialisaties | GGM data-object |  |
| GEMMA bedrijfsobject | Association | associaties | GEMMA bedrijfsobject |  |
| GEMMA bedrijfsobject | Specialization | specialisaties | GEMMA bedrijfsobject |  |
| Beleidsdomein | Aggregation |  | GGM data-object |  |
| Beleidsdomein | Aggregation |  | GEMMA bedrijfsobject |  |

## GEMMA modellering technische architectuur

Modellering van de technische architectuur

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| TechnologyService | Cloud dienstverleningslaag | Indeling van technologieservices waarop clouddiensten worden aangeboden, ook wel de cloud computing stack genoemd. |  |
| TechnologyService | Technologielaag | Lagen binnen cloud computing die technologieservices bieden voor het opzetten, beheren en ontwikkelen van IT-omgevingen |  |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Product | Aggregation |  | Cloud dienstverleningslaag |  |
| Cloud dienstverleningslaag | Aggregation |  | Technologielaag |  |
| Technologielaag | Aggregation |  | Technologieservice |  |
| Technologiecomponent | Realization |  | Technologieservice |  |

## GEMMA specialisaties applicatiecomponent

Deze view toont alle mogelijke specialisaties van de applicatiecomponent in de GEMMA.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| ApplicationComponent | Referentieaanbieder | Een referentiecomponent voor het aanbieden van services | Bron: GEMMA |
| ApplicationComponent | Referentieafnemer | Een referentiecomponent voor het afnemen van services | Bron: GEMMA |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationComponent | Buitengemeentelijke aanbieder | Een landelijke- of sectorale aanbieder van een voor gemeenten relevante voorziening |  |
| ApplicationComponent | Buitengemeentelijke afnemer | Een landelijke- of sectorale afnemer van een gemeentelijke applicatiedienst. |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Referentiecomponent | Specialization |  | Applicatiecomponent |  |
| Referentieaanbieder | Specialization |  | Referentiecomponent |  |
| Referentieafnemer | Specialization |  | Referentiecomponent |  |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Specialization |  | Applicatiecomponent |  |
| Buitengemeentelijke aanbieder | Specialization |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Buitengemeentelijke afnemer | Specialization |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |

## GEMMA modellering standaardenlijst

De relaties waarmee de standaarden worden voorgeschreven aan referentiecomponenten en applicatie-interfaces

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Constraint | Standaardversie | Een door de beheerder van de standaard uitgebrachte versie van de standaard | Bron: GEMMA |
| Grouping | Gradaties | Indeling van standaarden voor de (mate van) bouwbaarheid en testbaarheid. Standaarden kunnen als producten worden getypeerd in eindproducten, halffabrikaten, grondstoffen en gegevensstandaarden. Deze typering is een indicatie wat de benodigde inspanning is om de specificatie te completeren om tot een werkende koppeling te komen. | Bron: GEMMA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| ApplicationComponent | Referentieaanbieder | Een referentiecomponent voor het aanbieden van services | Bron: GEMMA |
| ApplicationComponent | Referentieafnemer | Een referentiecomponent voor het afnemen van services | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Standaardversie | Specialization | is versie van | Standaard |  |
| Gradaties | Aggregation |  | Standaard |  |
| Referentiecomponent | Realization | Verplicht / Aanbevolen | Standaard | Met de 'Verplicht / Aanbevolen' relatie wordt voor een referentiecomponent voorgeschreven welke standaard verplicht of aanbevolen is. Eigenschappen van de relatie 'aanbevolen of verplichte standaard' * Verbindingsrol = 'Aanbevolen' of 'Verplicht' |
| Referentieaanbieder | Composition | Verplicht / Aanbevolen | Applicatie-interface |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatie-interface | Serving | Verplicht / Aanbevolen | Referentieafnemer |  |

### Notities

- Voorschrijven van koppelings- of API-standaarden via de applicatie-interface
- Voorschrijven van standaarden die geen applicatie-interface kennen (b.v. TMLO, Digi-toegankelijk),
- Het relatietype bepaalt of de referentiecomponent de standaard als aanbieder of afnemer ondersteund
- GEMMA kennismodel uitgebreid
- GEMMA specialisaties applicatiecomponent

## Procesarchitectuur - Proceshiërarchie specialisatie

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessProcess | Bedrijfsproces (Behandelen evenementen-vergunningaanvraag) |  | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces (Behandelen omgevings-vergunningaanvraag) |  | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces (Behandelen vergunningaanvraag) |  | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces (Behandelen omgevings-vergunningaanvraag regulier) |  | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces (Behandelen omgevings-vergunningaanvraag uitgebreid) |  | Bron: GEMMA procesarchitectuur |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsproces (Behandelen evenementen-vergunningaanvraag) | Specialization |  | Bedrijfsproces (Behandelen vergunningaanvraag) |  |
| Bedrijfsproces (Behandelen omgevings-vergunningaanvraag) | Specialization |  | Bedrijfsproces (Behandelen vergunningaanvraag) |  |
| Bedrijfsproces (Behandelen omgevings-vergunningaanvraag regulier) | Specialization |  | Bedrijfsproces (Behandelen omgevings-vergunningaanvraag) |  |
| Bedrijfsproces (Behandelen omgevings-vergunningaanvraag uitgebreid) | Specialization |  | Bedrijfsproces (Behandelen omgevings-vergunningaanvraag) |  |

## GEMMA modellering bedrijfsobject

De modellering van de GEMMA bedrijfsobject modellen

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| Grouping | Domein | Een groep bedrijfsfuncties en -objecten die in de gemeentelijke praktijk vaak in samenhang worden ingericht en gebruikt | Bron: GEMMA |
| Grouping | Beleidsdomein | Een afgebakend gebied binnen gemeenten waarvoor specifieke beleidsmaatregelen, regels en verantwoordelijkheden gelden. De GEMMA en het Gemeentelijk GegevensModel gebruiken dezelfde, op IV3 gebaseerde, indeling. | URL: https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3; Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsobject | Association | is gerelateerd aan | Bedrijfsobject |  |
| Bedrijfsobject | Specialization | is een | Bedrijfsobject |  |
| Domein | Aggregation |  | Beleidsdomein |  |
| Beleidsdomein | Aggregation |  | Bedrijfsobject |  |

### Notities

- GEMMA kennismodel uitgebreid

## GEMMA modellering informatiearchitectuur

De ArchiMate modellering achter de GEMMA informatiearchitectuur views

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| Grouping | Domein en doelgroep | De groepering van applicatieservices voor een doelgroep binnen een domein | Bron: GEMMA |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationService | Buitengemeentelijke applicatieservice | Een voor gemeenten relevante landelijke- of sectorale applicatieservice | Bron: GEMMA |
| Grouping | Buitengemeentelijk stelsel | Groep van landelijke- of sectorale informatievoorzieningen | Bron: GEMMA |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| Grouping | Domein | Een groep bedrijfsfuncties en -objecten die in de gemeentelijke praktijk vaak in samenhang worden ingericht en gebruikt | Bron: GEMMA |
| BusinessRole | Doelgroep | De doelgroep is een ordening van de gemeentelijke applicatieservices naar de groep gebruikers. Een doelgroep is bijvoorbeeld de inwoners en ondernemers | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Applicatieservice | Association |  | Applicatieservice |  |
| Domein en doelgroep | Aggregation |  | Applicatieservice |  |
| Domein en doelgroep | Serving |  | Doelgroep |  |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Realization |  | Buitengemeentelijke applicatieservice |  |
| Buitengemeentelijke applicatieservice | Serving |  | Referentiecomponent |  |
| Buitengemeentelijk stelsel | Aggregation |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Referentiecomponent | Association |  | Applicatieservice |  |
| Domein | Aggregation |  | Domein en doelgroep |  |

### Notities

- GEMMA kennismodel uitgebreid

## GEMMA modellering product en service

Gewenste aansluiting van de GEMMA op de NORA modellering van producten en voorzieningen

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| Value | Waarde | Value represents the relative worth, utility, or importance of a core element or an outcome. | Bron: ArchiMate |
| BusinessService | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | Bron: NORA |
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| Contract | Afspraak | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Applicatieservice | Association |  | Dienst |  |
| Dienst | Association |  | Waarde |  |
| Product | Aggregation |  | Dienst |  |
| Product | Association |  | Applicatieservice |  |
| Product | Aggregation |  | Technologieservice |  |
| Product | Aggregation |  | Afspraak |  |
| Technologieservice | Association |  | Applicatieservice |  |

### Notities

- GEMMA kennismodel uitgebreid
- Af te stemmen met de NORA

## GEMMA modelleerafspraken inheritance

Deze view toont de modellering van inheritance in de GEMMA. Modellering met inheritance wordt gedaan om in het GEMMA model minder relaties te moeten onderhouden.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Constraint | Standaard 1 |  | Bron: GEMMA |
| ApplicationFunction | Functie 1 |  |  |
| ApplicationComponent | Basis | ApplicatieComponenten van GEMMA type 'Basiscomponent' definieren de te overerven objecten voor onderliggende applicatiecomponenten. | Bron: GEMMA |
| ApplicationComponent | Intermediate | ApplicatieComponenten van GEMMA type 'Basiscomponent', die een specialisatie zijn van een basiscomponent werken als een overervings intermediate. Onderliggende applicatiefuncties overerven van zowel de basiscomponent als de intermediate component. Afspraak is dat er maximaal één niveau intermediate kan bestaan (om redenen van overzichtelijkheid en beheerbaarheid). | Bron: GEMMA |
| ApplicationFunction | Functie 3 |  |  |
| Constraint | Standaard 3 |  | Bron: GEMMA |
| ApplicationComponent | Derived 1 | Een derived-component is een specialisatie van een basiscomponent. Een derived-component overerft alle relaties van bovenliggend basis of intermediate component. | Bron: GEMMA |
| ApplicationComponent | Derived 2 | Een derived-component is een specialisatie van een basiscomponent. Een derived-component overerft alle relaties van bovenliggend basis of intermediate component. |  |
| ApplicationFunction | Functie 2 |  |  |
| Constraint | Standaard 2 |  | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Basis | Realization |  | Standaard 1 |  |
| Basis | Assignment |  | Functie 1 |  |
| Intermediate | Specialization |  | Basis |  |
| Intermediate | Assignment |  | Functie 3 |  |
| Intermediate | Realization |  | Standaard 3 |  |
| Derived 1 | Realization |  | Standaard 1 |  |
| Derived 1 | Assignment |  | Functie 1 |  |
| Derived 1 | Realization |  | Standaard 2 |  |
| Derived 1 | Specialization |  | Basis |  |
| Derived 1 | Assignment |  | Functie 2 |  |
| Derived 2 | Specialization |  | Intermediate |  |
| Derived 2 | Realization |  | Standaard 3 |  |
| Derived 2 | Realization |  | Standaard 1 |  |
| Derived 2 | Assignment |  | Functie 3 |  |
| Derived 2 | Assignment |  | Functie 1 |  |

### Notities

- Relaties overerfd van Basis
- Eigen relaties, geen invloed op overerving
- Relaties overerfd van Intermediate
- Relaties overerfd van Basis

## GEMMA modellering bedrijfsfunctie

Deze view toont de ArchiMate modellering achter de views 'GEMMA bedrijfsfunctiemodel' en 'GEMMA bedrijfsfunctie en -objecten model

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Grouping | Domein | Een groep bedrijfsfuncties en -objecten die in de gemeentelijke praktijk vaak in samenhang worden ingericht en gebruikt | Bron: GEMMA |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| BusinessFunction | Laag | De lagen van het GEMMA bedrijfsfunctiemodel | Bron: GEMMA |
| BusinessFunction | Uitvoeringsdomein | Onderverdeling van de uitvoeringslaag in domeinspecifieke uitvoering | Bron: GEMMA |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Domein | Aggregation |  | Bedrijfsfunctie |  |
| Domein | Aggregation |  | Uitvoeringsdomein |  |
| Domein | Aggregation |  | Laag |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Referentiecomponent | Association |  | Applicatieservice |  |
| Laag | Aggregation |  | Bedrijfsfunctie |  |
| Laag | Aggregation |  | Uitvoeringsdomein |  |
| Uitvoeringsdomein | Aggregation |  | Bedrijfsfunctie |  |
| Bedrijfsfunctie | Aggregation |  | Bedrijfsfunctie |  |
| Bedrijfsfunctie | Serving |  | Bedrijfsproces |  |

### Notities

- GEMMA kennismodel uitgebreid

## GEMMA modellering applicatie-interface

Modellering van gegevensuitwisselingen tussen applicatiecomponenten

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Buitengemeentelijke aanbieder | Een landelijke- of sectorale aanbieder van een voor gemeenten relevante voorziening |  |
| ApplicationComponent | Buitengemeentelijke afnemer | Een landelijke- of sectorale afnemer van een gemeentelijke applicatiedienst. |  |
| ApplicationComponent | Referentieaanbieder | Een referentiecomponent voor het aanbieden van services | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |
| ApplicationComponent | Referentieafnemer | Een referentiecomponent voor het afnemen van services | Bron: GEMMA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Buitengemeentelijke aanbieder | Composition | Verplicht / Aanbevolen | Applicatie-interface |  |
| Referentieaanbieder | Composition | Verplicht / Aanbevolen | Applicatie-interface |  |
| Applicatie-interface | Serving | Verplicht / Aanbevolen | Buitengemeentelijke afnemer |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatie-interface | Association |  | Applicatieservice |  |
| Applicatie-interface | Serving | Verplicht / Aanbevolen | Referentieafnemer |  |

### Notities

- GEMMA kennismodel uitgebreid
- GEMMA specialisaties applicatiecomponent

## Procesarchitectuur - Bouwstenen bedrijfsservices

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessService | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | Bron: NORA |
| BusinessService | Deelservice | Een deelservice is een onderdeel van een Bedrijfsservice. Dit kan een externe maar ook een interne bedrijfsservice zijn. Bv. het werkproces 'besluiten' uit de GEMMA-referentieprocessen, levert zo'n deelservice. Het wordt in verschillende bedrijfsprocessen gebruikt, maar het is geen service die de organisatie levert aan de buitenwereld. | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| BusinessProcess | Processtap | Een geordende reeks handelingen die ononderbroken wordt uitgevoerd door één mens of machine binnen één bedrijfsfunctie (eenheid van tijd, plaats en handelen). | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Deelproces (werkproces) | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Bron: GEMMA procesarchitectuur |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Dienst | Aggregation |  | Deelservice |  |
| Bedrijfsproces | Realization |  | Dienst |  |
| Bedrijfsproces | Aggregation | is opgebouwd uit | Deelproces (werkproces) |  |
| Processtap | Realization |  | Deelservice |  |
| Deelproces (werkproces) | Realization |  | Deelservice |  |
| Deelproces (werkproces) | Aggregation | is opgebouwd uit | Processtap |  |

## GEMMA modellering bedrijfsproces

Deze view toont de ArchiMate modellering in de GEMMA procesarchitectuur.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessProcess | Procescluster |  | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| BusinessProcess | Processtap | Een geordende reeks handelingen die ononderbroken wordt uitgevoerd door één mens of machine binnen één bedrijfsfunctie (eenheid van tijd, plaats en handelen). | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Handeling | Kleinst mogelijke eenheid van werk, uitgevoerd door één persoon of machine op één plek op één moment. | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Deelproces (werkproces) | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Bron: GEMMA procesarchitectuur |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Procescluster | Aggregation |  | Bedrijfsproces |  |
| Procescluster | Aggregation |  | Procescluster |  |
| Bedrijfsproces | Aggregation | is opgebouwd uit | Deelproces (werkproces) |  |
| Bedrijfsproces | Triggering |  | Bedrijfsproces |  |
| Processtap | Aggregation | is opgebouwd uit | Handeling |  |
| Processtap | Triggering |  | Processtap |  |
| Handeling | Triggering |  | Handeling |  |
| Deelproces (werkproces) | Aggregation | is opgebouwd uit | Processtap |  |
| Deelproces (werkproces) | Triggering |  | Deelproces (werkproces) |  |

### Notities

- Procesarchitectuur - Bouwstenen bedrijfsservices
- Procesarchitectuur - Proceshiërarchie samenstelling
- Procesarchitectuur - Proceshiërarchie specialisatie
- GEMMA kennismodel uitgebreid
- In projectarchitectuur, niet in GEMMA
- Verwijzing naar detail-view

## GEMMA modellering motivatie

Modellering van de GEMMA architectuurprincipes en implicaties

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | Bron: NORA; URL: https://www.noraonline.nl/wiki/Beleidskaders |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Beleidskader | Influence | geeft grondslag aan | Kwaliteitsdoel | Het beleidskader vormt de bindende basis voor het kwaliteitsdoel en bepaalt welke eisen en normen het doel moet vervullen |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Implicatie | Realization | ondersteunt | Architectuurprincipe | De implicatie zorgt dat het principe praktisch en toepasbaar wordt. |

## Procesarchitectuur - Proceshiërarchie samenstelling

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessProcess | Handeling | Kleinst mogelijke eenheid van werk, uitgevoerd door één persoon of machine op één plek op één moment. | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| BusinessProcess | Deelproces (werkproces) | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Processtap | Een geordende reeks handelingen die ononderbroken wordt uitgevoerd door één mens of machine binnen één bedrijfsfunctie (eenheid van tijd, plaats en handelen). | Bron: GEMMA procesarchitectuur |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsproces | Aggregation | is opgebouwd uit | Deelproces (werkproces) |  |
| Deelproces (werkproces) | Aggregation | is opgebouwd uit | Processtap |  |
| Processtap | Aggregation | is opgebouwd uit | Handeling |  |

## Motivatie overzicht Kwaliteitsdoelen

Inhoud van de tabel op de pagina Kwaliteitsdoelen

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |

## Motivatie overzicht Kernwaarden

Inhoud van de tabel op de pagina Kernwaarden

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |

## Motivatie overzicht Architectuurprincipes

Inhoud van de tabel op de pagina Architectuurprincipes

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |

## Kennismodel procesarchitectuur

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Driver | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | Bron: NORA; URL: https://www.noraonline.nl/wiki/Beleidskaders |
| Goal | Visie | Het gewenste toekomstbeeld dat de organisatie nastreeft | Bron: GEMMA procesarchitectuur |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |
| CourseOfAction | Strategie | Het plan waarmee de organisatie haar missie en visie realiseert | Bron: GEMMA procesarchitectuur |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Stakeholder | Stakeholder | Een persoon of organisatie die invloed heeft op of beïnvloed wordt door processen en doelstellingen | Bron: GEMMA procesarchitectuur |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Value | Waarde | Het voordeel of nut dat een klant of organisatie ontvangt van een product, dienst of proces | Bron: ArchiMate |
| Goal | Missie | De kernopdracht of bestaansreden van de organisatie | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Processtap | Een geordende reeks handelingen die ononderbroken wordt uitgevoerd door één mens of machine binnen één bedrijfsfunctie (eenheid van tijd, plaats en handelen). | Bron: GEMMA procesarchitectuur |
| BusinessService | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | Bron: NORA |
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| BusinessProcess | Handeling | Kleinst mogelijke eenheid van werk, uitgevoerd door één persoon of machine op één plek op één moment. | Bron: GEMMA procesarchitectuur |
| BusinessProcess | Ketenproces | Een samenhangend geheel van processen over afdelingen of organisaties gericht op het leveren van waarde | Bron: GEMMA procesarchitectuur |
| Capability | Capability | Een vermogen waarover een organisatie, persoon of systeem beschikt. | Bron: Archimate |
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| BusinessRole | Klant (intern of extern) | De ontvanger van producten of diensten, binnen of buiten de organisatie | Bron: GEMMA procesarchitectuur |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| BusinessRole | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | Bron: ArchiMate |
| Resource | Resources | Middelen zoals personeel, informatie, systemen en financiële middelen die processen ondersteunen | Bron: ArchiMate |
| BusinessProcess | Deelproces (werkproces) | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Bron: GEMMA procesarchitectuur |
| BusinessActor | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | Bron: GEMMA |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Beleidskader | Influence | geeft grondslag aan | Kwaliteitsdoel | Het beleidskader vormt de bindende basis voor het kwaliteitsdoel en bepaalt welke eisen en normen het doel moet vervullen |
| Visie | Influence |  | Missie |  |
| Implicatie | Realization | ondersteunt | Architectuurprincipe | De implicatie zorgt dat het principe praktisch en toepasbaar wordt. |
| Strategie | Realization |  | Kwaliteitsdoel |  |
| Strategie | Realization |  | Visie |  |
| Strategie | Influence |  | Waarde |  |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Stakeholder | Influence |  | Missie |  |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Missie | Influence |  | Kwaliteitsdoel |  |
| Processtap | Aggregation | is opgebouwd uit | Handeling |  |
| Ketenproces | Aggregation |  | Bedrijfsproces |  |
| Ketenproces | Realization |  | Dienst |  |
| Capability | Influence |  | Waarde |  |
| Product | Aggregation |  | Dienst |  |
| Product | Influence |  | Waarde |  |
| Product | Association |  | Beleidskader |  |
| Product | Serving |  | Klant (intern of extern) |  |
| Bedrijfsfunctie | Serving |  | Bedrijfsproces |  |
| Bedrijfsfunctie | Realization |  | Capability |  |
| Rol | Assignment |  | Deelproces (werkproces) |  |
| Resources | Assignment |  | Capability |  |
| Deelproces (werkproces) | Aggregation | is opgebouwd uit | Processtap |  |
| Actor | Assignment |  | Rol |  |
| Bedrijfsproces | Realization |  | Dienst |  |
| Bedrijfsproces | Serving |  | Bedrijfsfunctie |  |
| Bedrijfsproces | Aggregation | is opgebouwd uit | Deelproces (werkproces) |  |
| Bedrijfsproces | Access | benadert | Bedrijfsobject |  |

## Samenhang registers

een overzicht van de samenhang van de PDC, UPL, ZTC, processen en het verwerkingenregister.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | SC - Samenwerkende catalogi | Samenwerkende Catalogi is een gestandaardiseerd register dat overheidsproducten en -diensten vindbaar maakt voor burgers en ondernemers. |  |
| BusinessObject | UPL - Uniforme Productnamenlijst | De Uniforme productnamenlijst is een landelijk geharmoniseerde set van productnamen die het gebruik en hergebruik van overheidsproducten en -diensten ondersteunt. |  |
| BusinessObject | Externe producten- en dienstenlijst | Een overzicht van alle producten en diensten die een gemeente aan burgers en bedrijven levert, inclusief beschrijvingen en voorwaarden. |  |
| BusinessObject | Interne producten- en dienstenlijst | Een overzicht van producten en diensten die binnen de organisatie gebruikt of geleverd worden voor de interne bedrijfsvoering. |  |
| BusinessObject | Processenregister | Een processenregister is een overzicht van de kern- en ondersteunende processen van een organisatie, inclusief hun beschrijvingen en onderlinge relaties. |  |
| BusinessObject | Verwerkingenregister | Het verwerkingsregister legt vast welke persoonsgegevens de gemeente verwerkt, voor welk doel en op basis van welke wettelijke grondslag. | Toelichting: Het register moet zowel verwerkingen opnemen die voortkomen uit publieke taken als uit privaatrechtelijke taken van de gemeente. |
| BusinessObject | Zaaktypecatalogus | Een zaaktypecatalogus is een gestandaardiseerd overzicht van zaaktypen die een organisatie gebruikt om aanvragen, meldingen of verzoeken te registreren en af te handelen. |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| SC - Samenwerkende catalogi | Association | hergebruikt | Externe producten- en dienstenlijst |  |
| UPL - Uniforme Productnamenlijst | Association | definieert | SC - Samenwerkende catalogi |  |
| UPL - Uniforme Productnamenlijst | Association | levert vulling | Verwerkingenregister |  |
| Externe producten- en dienstenlijst | Association | publiceert | SC - Samenwerkende catalogi |  |
| Externe producten- en dienstenlijst | Association | implementeert | UPL - Uniforme Productnamenlijst |  |
| Processenregister | Specialization | specialiseert | Zaaktypecatalogus |  |
| Processenregister | Specialization | specialiseert | Verwerkingenregister |  |
| Processenregister | Association | realiseert | Externe producten- en dienstenlijst |  |
| Processenregister | Association | realiseert | Interne producten- en dienstenlijst |  |

## Common Ground modellering technische architectuur

Modellering van de technische architectuur

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| SystemSoftware | Logische technologiecomponent | Een herbruikbare, functioneel afgebakende bouwsteen van systeemsoftware vanuit ontwerp- en ontwikkelperspectief. | Toelichting: Een logische technologiecomponent beschrijft een afgebakend onderdeel van systeemsoftware dat in een architectuurontwerp wordt onderscheiden. Het is kleiner dan of gelijk aan een technologiecomponent en vertegenwoordigt een specifieke technische functie, zoals communicatie, routing, transformatie, beveiliging of logging. Meerdere logische technologiecomponenten kunnen samen één technologiecomponent vormen en zijn onafhankelijk van een specifiek product of leverancier. |
| TechnologyFunction | Technologiefunctie | Een intern gedrag van systeemsoftware dat een specifieke technische functionaliteit realiseert. |  |
| TechnologyInterface | Technologie-interface | Een technologie-interface beschrijft hoe toegang wordt verkregen tot de functionaliteit van systeemsoftware, bijvoorbeeld via een API, protocol of messaging-interface. |  |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| SystemSoftware | Fysieke technologiecomponent | Een concreet softwareproduct of -dienst dat een technologiecomponent realiseert en inzetbaar is in een specifieke technische omgeving. | Toelichting: Een fysieke technologiecomponent is de daadwerkelijke implementatie van systeemsoftware die beschikbaar is als commercieel product of open source software. Het kan gaan om software die on-premises of in de cloud wordt uitgerold en operationeel wordt gebruikt, zoals een database, ESB-platform of API-managementproduct. Hiermee wordt de abstracte technologiecomponent vertaald naar een concreet inzetbare oplossing. |
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| TechnologyService | Cloud dienstverleningslaag | Indeling van technologieservices waarop clouddiensten worden aangeboden, ook wel de cloud computing stack genoemd. |  |
| TechnologyService | Technologielaag | Lagen binnen cloud computing die technologieservices bieden voor het opzetten, beheren en ontwikkelen van IT-omgevingen |  |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Logische technologiecomponent | Composition |  | Technologie-interface |  |
| Logische technologiecomponent | Assignment |  | Technologiefunctie |  |
| Logische technologiecomponent | Realization |  | Technologieservice |  |
| Logische technologiecomponent | Specialization |  | Technologiecomponent |  |
| Technologie-interface | Realization |  | Standaard |  |
| Technologie-interface | Assignment |  | Technologieservice |  |
| Fysieke technologiecomponent | Specialization | is geschikt voor | Logische technologiecomponent |  |
| Fysieke technologiecomponent | Specialization | is geschikt voor | Technologiecomponent |  |
| Product | Aggregation |  | Cloud dienstverleningslaag |  |
| Cloud dienstverleningslaag | Aggregation |  | Technologielaag |  |
| Technologielaag | Aggregation |  | Technologieservice |  |
| Technologiecomponent | Realization |  | Technologieservice |  |

### Notities

- Technologie function assigned to fysieke technologiecomponent weggelaten. Komt niet voor in uitwerkingen

## Common Ground en specialisaties

Deze view toont alle mogelijke specialisaties van componenten in de GEMMA en hoe de SWC en Common Ground daar op aansluiten

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| SystemSoftware | Fysieke technologiecomponent | Een concreet softwareproduct of -dienst dat een technologiecomponent realiseert en inzetbaar is in een specifieke technische omgeving. | Toelichting: Een fysieke technologiecomponent is de daadwerkelijke implementatie van systeemsoftware die beschikbaar is als commercieel product of open source software. Het kan gaan om software die on-premises of in de cloud wordt uitgerold en operationeel wordt gebruikt, zoals een database, ESB-platform of API-managementproduct. Hiermee wordt de abstracte technologiecomponent vertaald naar een concreet inzetbare oplossing. |
| SystemSoftware | Logische technologiecomponent | Een herbruikbare, functioneel afgebakende bouwsteen van systeemsoftware vanuit ontwerp- en ontwikkelperspectief. | Toelichting: Een logische technologiecomponent beschrijft een afgebakend onderdeel van systeemsoftware dat in een architectuurontwerp wordt onderscheiden. Het is kleiner dan of gelijk aan een technologiecomponent en vertegenwoordigt een specifieke technische functie, zoals communicatie, routing, transformatie, beveiliging of logging. Meerdere logische technologiecomponenten kunnen samen één technologiecomponent vormen en zijn onafhankelijk van een specifiek product of leverancier. |
| ApplicationComponent | Logische applicatiecomponent |  |  |
| ApplicationComponent | Logische registercomponent | Een functioneel afgebakend, herbruikbaar component dat in ontwerp en ontwikkeling registers en hun services beschrijft. | Toelichting: Een logische registercomponent beschrijft in een architectuur- en ontwikkelcontext welke registers er zijn, welke gegevens daarin worden beheerd en welke services zij aanbieden. Het ondersteunt het ontwerp van gebruik en interactie met registers binnen het Common Ground 5-lagenmodel (lagen 1 en 2), onafhankelijk van een specifieke technische implementatie. |
| ApplicationComponent | Fysieke registercomponent | Een (component binnen een) concreet softwareproduct of -dienst dat een register en de bijbehorende services realiseert en beschikbaar stelt voor gebruik. | Toelichting: Een fysieke registercomponent is de daadwerkelijke implementatie van een register, bijvoorbeeld als applicatie, databron of dienst. Deze component stelt de gedefinieerde services beschikbaar aan applicaties en andere systemen |
| ApplicationComponent | Fysieke applicatiecomponent |  |  |
| ApplicationComponent | Applicatie |  | Specialization: Container |
| ApplicationComponent | Applicatieversie |  |  |
| SystemSoftware | Systeemsoftware |  |  |
| ApplicationComponent | Referentieafnemer | Een referentiecomponent voor het afnemen van services | Bron: GEMMA |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| ApplicationComponent | Buitengemeentelijke aanbieder | Een landelijke- of sectorale aanbieder van een voor gemeenten relevante voorziening |  |
| ApplicationComponent | Buitengemeentelijke afnemer | Een landelijke- of sectorale afnemer van een gemeentelijke applicatiedienst. |  |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationComponent | Referentieaanbieder | Een referentiecomponent voor het aanbieden van services | Bron: GEMMA |
| SystemSoftware | System Software |  |  |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Fysieke technologiecomponent | Specialization | is geschikt voor | Logische technologiecomponent |  |
| Logische technologiecomponent | Specialization |  | Technologiecomponent |  |
| Logische applicatiecomponent | Specialization |  | Referentieafnemer |  |
| Logische registercomponent | Specialization |  | Referentieaanbieder |  |
| Fysieke registercomponent | Specialization |  | Logische registercomponent |  |
| Fysieke applicatiecomponent | Realization |  | Logische applicatiecomponent |  |
| Applicatie | Specialization |  | Referentiecomponent |  |
| Systeemsoftware | Specialization |  | Technologiecomponent |  |
| Referentieafnemer | Specialization |  | Referentiecomponent |  |
| Referentiecomponent | Specialization |  | Applicatiecomponent |  |
| Buitengemeentelijke aanbieder | Specialization |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Buitengemeentelijke afnemer | Specialization |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Specialization |  | Applicatiecomponent |  |
| Referentieaanbieder | Specialization |  | Referentiecomponent |  |
| Technologiecomponent | Specialization |  | System Software |  |

### Notities

- De GEMMA-referentieafnemer en -aanbieder zijn niet uitgewerkt. We kunnen besluiten deze één-op-één te matchen met de CG logische componenten.
- De uitwerkingen sluiten grotendeels aan bij de GEMMA-technologiecomponenten. Binnen de technologie-architectuur is in de view berichtenverkeer het product OpenFSC gekoppeld aan de technologiecomponent API-gateway. Binnen de applicatiearchitectuur is laag 3 (Intermediair) verder uitgewerkt. Hierin wordt zichtbaar hoe de API-gateway is opgesplitst in meerdere logische technologiecomponenten. Daarbij worden logische en fysieke aspecten door elkaar gebruikt; dit is te verhelpen door de API-gateway als tussenlaag expliciet op te nemen.
- ArchiMate type gewijzigd van application-component naar system-software

## GEMMA kennismodel technologielaag

Technische architectuur elementen en onderlinge relaties

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Technologieservice | Serving |  | Applicatiecomponent |  |
| Technologiecomponent | Realization |  | Technologieservice |  |

## GEMMA kennismodel applicatielaag

Informatie-architectuur elementen en onderlinge relaties

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Applicatiecomponent | Composition |  | Applicatie-interface |  |
| Applicatiecomponent | Flow | gegevensuitwisseling | Applicatiecomponent |  |
| Applicatiecomponent | Realization | realiseert standaard | Standaard |  |
| Applicatiecomponent | Association |  | Applicatieservice |  |
| Applicatie-interface | Association |  | Applicatieservice |  |
| Applicatie-interface | Serving |  | Applicatiecomponent |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Applicatieservice | Association |  | Applicatiecomponent |  |
| Standaard | Specialization | is versie van | Standaard |  |

## GEMMA kennismodel strategie en motivatie

Strategie en motivatie elementen en onderlinge relaties

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |

## GEMMA kennismodel

Het GEMMA kennismodel is de invulling van de ArchiMate conventie voor de informatievoorziening van het gemeentelijk domein
In het GEMMA kennismodel zijn alle in de GEMMA gebruikte ArchiMate element- en relatietypen weergegeven.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| BusinessCollaboration | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. | Bron: ArchiMate |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| BusinessActor | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | Bron: GEMMA |
| BusinessRole | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | Bron: ArchiMate |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| Grouping | Groep | The grouping element aggregates or composes concepts that belong together based on some common characteristic. | Bron: ArchiMate |
| Capability | Capability | Een vermogen waarover een organisatie, persoon of systeem beschikt. | Bron: Archimate |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Standaard | Specialization | is versie van | Standaard |  |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Technologiecomponent | Realization |  | Technologieservice |  |
| Bedrijfsobject | Association | is gerelateerd aan | Bedrijfsobject |  |
| Bedrijfsobject | Specialization | is een | Bedrijfsobject |  |
| Bedrijfssamenwerking | Aggregation |  | Rol |  |
| Bedrijfsproces | Specialization |  | Bedrijfsproces |  |
| Bedrijfsproces | Triggering |  | Bedrijfsproces |  |
| Actor | Assignment |  | Rol |  |
| Rol | Specialization |  | Rol |  |
| Applicatiecomponent | Composition |  | Applicatie-interface |  |
| Applicatiecomponent | Flow | gegevensuitwisseling | Applicatiecomponent |  |
| Applicatiecomponent | Realization | realiseert standaard | Standaard |  |
| Applicatiecomponent | Association |  | Applicatieservice |  |
| Applicatie-interface | Association |  | Applicatieservice |  |
| Applicatie-interface | Serving |  | Applicatiecomponent |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Applicatieservice | Association |  | Applicatiecomponent |  |
| Groep | Aggregation |  | Groep |  |

### Notities

- Voor de overzichtelijkheid zijn groepen niet weergegeven: * Een groep kan alle concepten groeperen * Concepten kunnen zichzelf groeperen

## GEMMA kennismodel uitgebreid

Het GEMMA kennismodel is de invulling van de ArchiMate-conventie voor de informatievoorziening in het gemeentelijk domein.
Het beschrijft aanvullend op de in GEMMA gemodelleerde ArchiMate-concepten gewenste uitbreidingen, zoals diensten en producten, en elementen en relaties die in projectarchitecturen worden gebruikt. Een projectarchitectuur kan daarbij volledig gebruikmaken van ArchiMate.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| BusinessInterface | Kanaal | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. | Bron: NORA |
| BusinessService | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | Bron: NORA |
| BusinessCollaboration | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. | Bron: ArchiMate |
| BusinessActor | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | Bron: GEMMA |
| BusinessEvent | Gebeurtenis | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. | Bron: GEMMA |
| BusinessRole | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | Bron: ArchiMate |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| Requirement | Requirement | Een eis die geldt voor een specifiek informatiesysteem of onderdeel daarvan binnen de architectuur. | Bron: GEMMA |
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | Bron: NORA; URL: https://www.noraonline.nl/wiki/Beleidskaders |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |
| Device | Device | A device is a physical IT resource upon which system software and artifacts may be stored or deployed for execution. | Bron: ArchiMate |
| TechnologyFunction | Technologiefunctie | A technology function represents a collection of technology behavior that can be performed by a node. | Bron: ArchiMate |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| Artifact | Artifact | An artifact represents a piece of data that is used or produced in a software development process, or by deployment and operation of an IT system. | Bron: ArchiMate |
| Node | Node | A node represents a computational or physical resource that hosts, manipulates, or interacts with other computational or physical resources. | Bron: ArchiMate |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationProcess | Applicatieproces | An application process represents a sequence of application behaviors that achieves a specific outcome. | Bron: ArchiMate |
| ApplicationFunction | Applicatiefunctie | Een samenhangende groep interne gedragingen van een applicatiecomponent. Een voorbeeld van een applicatiefunctie is de Raadplegen zaakdocumenten functie. | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |
| ApplicationEvent | Applicatie-event | Iets dat binnen of buiten een applicatie is gebeurd en binnen die applicatie of daarbuiten gevolgen heeft. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| DataObject | Data-object | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. | Bron: GEMMA |
| Grouping | Groep | The grouping element aggregates or composes concepts that belong together based on some common characteristic. | Bron: ArchiMate |
| Capability | Capability | Een vermogen waarover een organisatie, persoon of systeem beschikt. | Bron: Archimate |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsobject | Association | is gerelateerd aan | Bedrijfsobject |  |
| Bedrijfsobject | Specialization | is een | Bedrijfsobject |  |
| Product | Aggregation |  | Dienst |  |
| Product | Association |  | Applicatieservice |  |
| Product | Aggregation |  | Technologieservice |  |
| Kanaal | Assignment |  | Dienst |  |
| Kanaal | Serving |  | Rol |  |
| Dienst | Serving |  | Bedrijfsproces |  |
| Bedrijfssamenwerking | Aggregation |  | Rol |  |
| Actor | Assignment |  | Rol |  |
| Gebeurtenis | Triggering |  | Bedrijfsproces |  |
| Rol | Access | heeft toegang tot | Bedrijfsobject | Heeft toegang tot een bedrijfsobject en: * Is verantwoordelijk voor * is eigenaar van * is beheerder van * is raadpleger van |
| Rol | Specialization |  | Rol |  |
| Rol | Assignment |  | Bedrijfsfunctie |  |
| Bedrijfsfunctie | Access | benadert | Bedrijfsobject |  |
| Bedrijfsfunctie | Serving |  | Bedrijfsproces |  |
| Bedrijfsfunctie | Realization |  | Dienst |  |
| Bedrijfsproces | Specialization |  | Bedrijfsproces |  |
| Bedrijfsproces | Triggering |  | Bedrijfsproces |  |
| Bedrijfsproces | Triggering |  | Gebeurtenis |  |
| Bedrijfsproces | Realization |  | Dienst |  |
| Bedrijfsproces | Serving |  | Bedrijfsfunctie |  |
| Bedrijfsproces | Access | benadert | Bedrijfsobject |  |
| Beleidskader | Influence | geeft grondslag aan | Kwaliteitsdoel | Het beleidskader vormt de bindende basis voor het kwaliteitsdoel en bepaalt welke eisen en normen het doel moet vervullen |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Standaard | Specialization | is versie van | Standaard |  |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Device | Assignment |  | Technologiecomponent |  |
| Technologiefunctie | Realization |  | Technologieservice |  |
| Technologiefunctie | Access |  | Artifact |  |
| Technologieservice | Serving |  | Applicatiefunctie |  |
| Technologieservice | Serving |  | Technologiefunctie |  |
| Technologieservice | Access |  | Artifact |  |
| Technologieservice | Serving |  | Node |  |
| Technologieservice | Serving |  | Applicatiecomponent |  |
| Artifact | Realization |  | Data-object |  |
| Node | Assignment |  | Technologiefunctie |  |
| Node | Aggregation |  | Technologiecomponent |  |
| Node | Aggregation |  | Device |  |
| Node | Realization |  | Technologieservice |  |
| Technologiecomponent | Realization |  | Technologieservice |  |
| Applicatiecomponent | Composition |  | Applicatie-interface |  |
| Applicatiecomponent | Flow | gegevensuitwisseling | Applicatiecomponent |  |
| Applicatiecomponent | Assignment |  | Applicatiefunctie |  |
| Applicatiecomponent | Realization |  | Requirement |  |
| Applicatiecomponent | Triggering |  | Applicatie-event |  |
| Applicatiecomponent | Association |  | Applicatieservice |  |
| Applicatiecomponent | Realization | realiseert standaard | Standaard |  |
| Applicatieproces | Association |  | Applicatieservice |  |
| Applicatieproces | Triggering |  | Applicatieproces |  |
| Applicatieproces | Triggering |  | Applicatie-event |  |
| Applicatiefunctie | Serving |  | Applicatieproces |  |
| Applicatiefunctie | Association |  | Applicatieservice |  |
| Applicatiefunctie | Aggregation |  | Applicatieproces |  |
| Applicatiefunctie | Access |  | Data-object |  |
| Applicatie-interface | Association |  | Applicatieservice |  |
| Applicatie-interface | Serving |  | Applicatiecomponent |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatie-event | Triggering |  | Applicatieproces |  |
| Applicatie-event | Triggering |  | Applicatiecomponent |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Applicatieservice | Association |  | Data-object |  |
| Applicatieservice | Association |  | Applicatiefunctie |  |
| Applicatieservice | Association |  | Bedrijfsproces |  |
| Applicatieservice | Association |  | Applicatiecomponent |  |
| Data-object | Realization |  | Bedrijfsobject |  |
| Groep | Aggregation |  | Groep |  |

### Notities

- In projectarchitectuur, niet in GEMMA
- Wens, nu niet in GEMMA
- Voor de overzichtelijkheid zijn groepen niet weergegeven: * Een groep kan alle concepten groeperen * Concepten kunnen zichzelf groeperen

## GEMMA kennismodel bedrijfslaag

Bedrijfsarchitectuur elementen en onderlinge relaties

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| BusinessCollaboration | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. | Bron: ArchiMate |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| BusinessActor | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | Bron: GEMMA |
| BusinessRole | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | Bron: ArchiMate |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsobject | Association | is gerelateerd aan | Bedrijfsobject |  |
| Bedrijfsobject | Specialization | is een | Bedrijfsobject |  |
| Bedrijfssamenwerking | Aggregation |  | Rol |  |
| Bedrijfsproces | Triggering |  | Bedrijfsproces |  |
| Bedrijfsproces | Specialization |  | Bedrijfsproces |  |
| Actor | Assignment |  | Rol |  |
| Rol | Specialization |  | Rol |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |

## GEMMA kennismodel uitgebreid (geen titel)

Het GEMMA kennismodel is de invulling van de ArchiMate-conventie voor de informatievoorziening in het gemeentelijk domein.
Het beschrijft aanvullend op de in GEMMA gemodelleerde ArchiMate-concepten gewenste uitbreidingen, zoals diensten en producten, en elementen en relaties die in projectarchitecturen worden gebruikt. Een projectarchitectuur kan daarbij volledig gebruikmaken van ArchiMate.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Bedrijfsobject | Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft. | Bron: GEMMA |
| Product | Product | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. | Bron: GEMMA |
| BusinessInterface | Kanaal | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. | Bron: NORA |
| BusinessService | Dienst | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). | Bron: NORA |
| BusinessCollaboration | Bedrijfssamenwerking | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. | Bron: ArchiMate |
| BusinessActor | Actor | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. | Bron: GEMMA |
| BusinessEvent | Gebeurtenis | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. | Bron: GEMMA |
| BusinessRole | Rol | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. | Bron: ArchiMate |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| BusinessProcess | Bedrijfsproces | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst. | Bron: GEMMA |
| Requirement | Requirement | Een eis die geldt voor een specifiek informatiesysteem of onderdeel daarvan binnen de architectuur. | Bron: GEMMA |
| Goal | Kwaliteitsdoel | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. | Bron: NORA |
| Driver | Beleidskader | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden | Bron: NORA; URL: https://www.noraonline.nl/wiki/Beleidskaders |
| Driver | Kernwaarde | Fundamentele overtuigingen, gebaseerd op maatschappelijke waarden, waar overheidsdienstverlening aan moet voldoen | Bron: NORA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| Principle | Architectuurprincipe | Een kwalitatieve intentieverklaring waaraan de architectuur moet voldoen. | Bron: ArchiMate |
| Requirement | Implicatie | De acties die nodig zijn om een architectuurprincipe in de praktijk toe te passen | Bron: GEMMA |
| Device | Device | A device is a physical IT resource upon which system software and artifacts may be stored or deployed for execution. | Bron: ArchiMate |
| TechnologyFunction | Technologiefunctie | A technology function represents a collection of technology behavior that can be performed by a node. | Bron: ArchiMate |
| TechnologyService | Technologieservice | Services die technische functionaliteit leveren aan applicaties. Bijvoorbeeld services voor verwerking, opslag, netwerk en beveiliging. | Bron: GEMMA |
| Artifact | Artifact | An artifact represents a piece of data that is used or produced in a software development process, or by deployment and operation of an IT system. | Bron: ArchiMate |
| Node | Node | A node represents a computational or physical resource that hosts, manipulates, or interacts with other computational or physical resources. | Bron: ArchiMate |
| SystemSoftware | Technologiecomponent | Een type systeemsoftware dat een omgeving realiseert voor het draaien en ondersteunen van applicaties en technische services. | Bron: GEMMA |
| ApplicationComponent | Applicatiecomponent | Een modulair, zelfstandig inzetbaar en vervangbaar deel van een informatiesysteem dat bepaalde functionaliteit kan leveren. | Bron: GEMMA |
| ApplicationProcess | Applicatieproces | An application process represents a sequence of application behaviors that achieves a specific outcome. | Bron: ArchiMate |
| ApplicationFunction | Applicatiefunctie | Een samenhangende groep interne gedragingen van een applicatiecomponent. Een voorbeeld van een applicatiefunctie is de Raadplegen zaakdocumenten functie. | Bron: GEMMA |
| ApplicationInterface | Applicatie-interface | Door een Applicatiecomponent aangeboden interface die (andere) Applicatiecomponenten, Nodes of Actoren Applicatieservices kunnen gebruiken. | Bron: GEMMA |
| ApplicationEvent | Applicatie-event | Iets dat binnen of buiten een applicatie is gebeurd en binnen die applicatie of daarbuiten gevolgen heeft. | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| DataObject | Data-object | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. | Bron: GEMMA |
| Capability | Capability | Een vermogen waarover een organisatie, persoon of systeem beschikt. | Bron: Archimate |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Bedrijfsobject | Association | is gerelateerd aan | Bedrijfsobject |  |
| Bedrijfsobject | Specialization | is een | Bedrijfsobject |  |
| Product | Aggregation |  | Dienst |  |
| Product | Association |  | Applicatieservice |  |
| Product | Aggregation |  | Technologieservice |  |
| Kanaal | Assignment |  | Dienst |  |
| Kanaal | Serving |  | Rol |  |
| Dienst | Serving |  | Bedrijfsproces |  |
| Bedrijfssamenwerking | Aggregation |  | Rol |  |
| Actor | Assignment |  | Rol |  |
| Gebeurtenis | Triggering |  | Bedrijfsproces |  |
| Rol | Access | heeft toegang tot | Bedrijfsobject | Heeft toegang tot een bedrijfsobject en: * Is verantwoordelijk voor * is eigenaar van * is beheerder van * is raadpleger van |
| Rol | Specialization |  | Rol |  |
| Rol | Assignment |  | Bedrijfsfunctie |  |
| Bedrijfsfunctie | Access | benadert | Bedrijfsobject |  |
| Bedrijfsfunctie | Serving |  | Bedrijfsproces |  |
| Bedrijfsfunctie | Realization |  | Dienst |  |
| Bedrijfsproces | Specialization |  | Bedrijfsproces |  |
| Bedrijfsproces | Triggering |  | Bedrijfsproces |  |
| Bedrijfsproces | Triggering |  | Gebeurtenis |  |
| Bedrijfsproces | Realization |  | Dienst |  |
| Bedrijfsproces | Serving |  | Bedrijfsfunctie |  |
| Bedrijfsproces | Access | benadert | Bedrijfsobject |  |
| Beleidskader | Influence | geeft grondslag aan | Kwaliteitsdoel | Het beleidskader vormt de bindende basis voor het kwaliteitsdoel en bepaalt welke eisen en normen het doel moet vervullen |
| Kernwaarde | Influence | motiveert | Kwaliteitsdoel | De kernwaarde inspireert en motiveert het opstellen van het kwaliteitsdoel. |
| Standaard | Specialization | is versie van | Standaard |  |
| Architectuurprincipe | Association |  | Architectuurprincipe | Het ene principe bouwt voort op het andere en zorgt voor samenhang in beleid en uitvoering |
| Architectuurprincipe | Realization | draagt bij aan | Kwaliteitsdoel | Het principe helpt het kwaliteitsdoel daadwerkelijk te realiseren. |
| Device | Assignment |  | Technologiecomponent |  |
| Technologiefunctie | Realization |  | Technologieservice |  |
| Technologiefunctie | Access |  | Artifact |  |
| Technologieservice | Serving |  | Applicatiefunctie |  |
| Technologieservice | Serving |  | Technologiefunctie |  |
| Technologieservice | Access |  | Artifact |  |
| Technologieservice | Serving |  | Node |  |
| Technologieservice | Serving |  | Applicatiecomponent |  |
| Artifact | Realization |  | Data-object |  |
| Node | Assignment |  | Technologiefunctie |  |
| Node | Aggregation |  | Technologiecomponent |  |
| Node | Aggregation |  | Device |  |
| Node | Realization |  | Technologieservice |  |
| Technologiecomponent | Realization |  | Technologieservice |  |
| Applicatiecomponent | Composition |  | Applicatie-interface |  |
| Applicatiecomponent | Flow | gegevensuitwisseling | Applicatiecomponent |  |
| Applicatiecomponent | Assignment |  | Applicatiefunctie |  |
| Applicatiecomponent | Realization |  | Requirement |  |
| Applicatiecomponent | Triggering |  | Applicatie-event |  |
| Applicatiecomponent | Association |  | Applicatieservice |  |
| Applicatiecomponent | Realization | realiseert standaard | Standaard |  |
| Applicatieproces | Association |  | Applicatieservice |  |
| Applicatieproces | Triggering |  | Applicatieproces |  |
| Applicatieproces | Triggering |  | Applicatie-event |  |
| Applicatiefunctie | Serving |  | Applicatieproces |  |
| Applicatiefunctie | Association |  | Applicatieservice |  |
| Applicatiefunctie | Aggregation |  | Applicatieproces |  |
| Applicatiefunctie | Access |  | Data-object |  |
| Applicatie-interface | Association |  | Applicatieservice |  |
| Applicatie-interface | Serving |  | Applicatiecomponent |  |
| Applicatie-interface | Realization |  | Standaard |  |
| Applicatie-event | Triggering |  | Applicatieproces |  |
| Applicatie-event | Triggering |  | Applicatiecomponent |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Applicatieservice | Association |  | Data-object |  |
| Applicatieservice | Association |  | Applicatiefunctie |  |
| Applicatieservice | Association |  | Bedrijfsproces |  |
| Applicatieservice | Association |  | Applicatiecomponent |  |
| Data-object | Realization |  | Bedrijfsobject |  |

## GEMMA doelgroepen en VNG persona's

Mapping van de GEMMA doelgroepen op de VNG persona's

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Grouping | Persona's leveranciers |  |  |
| BusinessRole | Medewerker leverancier |  |  |
| Grouping | Persona's gemeenten (bron VNG onderzoek) |  |  |
| BusinessRole | Ambtenaar |  |  |
| BusinessRole | Sturende strateeg |  |  |
| BusinessRole | Specifieke specialist |  |  |
| BusinessRole | Adviserende allrounder |  |  |
| BusinessRole | Bestuurder |  |  |
| BusinessObject | Doelgroepen |  | Algemene producten: ja |
| BusinessRole | Adviseur informatievoorziening | Adviserende rol |  |
| BusinessRole | Accountmanager |  |  |
| BusinessRole | Functioneel beheerder |  |  |
| BusinessRole | Leidinggevende |  |  |
| BusinessRole | Ontwikkelaar |  |  |
| BusinessRole | Projectleider |  |  |
| BusinessRole | Informatiemanager |  |  |
| BusinessRole | Programmamanager |  |  |
| BusinessRole | Productmanager |  |  |
| BusinessRole | Architect | Adviserende rol |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Adviseur informatievoorziening | Specialization |  | Adviserende allrounder |  |
| Adviseur informatievoorziening | Association |  | Doelgroepen |  |
| Accountmanager | Specialization |  | Medewerker leverancier |  |
| Accountmanager | Association |  | Doelgroepen |  |
| Functioneel beheerder | Specialization |  | Specifieke specialist |  |
| Functioneel beheerder | Association |  | Doelgroepen |  |
| Leidinggevende | Specialization |  | Sturende strateeg |  |
| Leidinggevende | Association |  | Doelgroepen |  |
| Ontwikkelaar | Specialization |  | Specifieke specialist |  |
| Ontwikkelaar | Specialization |  | Medewerker leverancier |  |
| Ontwikkelaar | Association |  | Doelgroepen |  |
| Projectleider | Specialization |  | Specifieke specialist |  |
| Projectleider | Specialization |  | Medewerker leverancier |  |
| Projectleider | Association |  | Doelgroepen |  |
| Bestuurder | Specialization |  | Bestuurder |  |
| Bestuurder | Association |  | Doelgroepen |  |
| Informatiemanager | Specialization |  | Sturende strateeg |  |
| Informatiemanager | Association |  | Doelgroepen |  |
| Programmamanager | Specialization |  | Sturende strateeg |  |
| Programmamanager | Association |  | Doelgroepen |  |
| Productmanager | Specialization |  | Medewerker leverancier |  |
| Productmanager | Association |  | Doelgroepen |  |
| Architect | Specialization |  | Adviserende allrounder |  |
| Architect | Association |  | Doelgroepen |  |

## GEMMA portfolio indeling

Hoofdindeling van de GEMMA

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Thema-architecturen | Een binnen de GEMMA voor een bepaald thema uitgewerkte architectuur | Thema-architecturen: ja |
| BusinessObject | Basisarchitectuur | De kern van de GEMMA met daarin o.a. architectuurprincipes en de GEMMA Bedrijfs-, Informatie- en Technische architectuur. | Basisarchitectuur: ja |
| BusinessObject | Algemene producten | Groep van producten die relevant zijn voor zowel de basisarchitectuur producten als de thema-architecturen | Algemene producten: ja |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

## GEMMA portfolio subproducten

Een gestructureerde weergave van de verzameling van producten waarmee de GEMMA is opgebouwd

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Thema-architecturen | Een binnen de GEMMA voor een bepaald thema uitgewerkte architectuur | Thema-architecturen: ja |
| BusinessObject | Werken met API's |  | Thema-architecturen: ja |
| BusinessObject | Beveiligingsrichtlijnen voor API's en webservices |  |  |
| BusinessObject | Identiteit en toegangs beheer |  |  |
| BusinessObject | APIs informatiearchitectuur |  |  |
| BusinessObject | Data | Thema-architectuur die aspecten met betrekking tot data uitwerkt. Bijvoorbeeld: datamanagement en data-uitwisseling. | Thema-architecturen: ja |
| BusinessObject | Bedrijfsobjectmodel | Een bedrijfsobjectmodel beschrijft de objecten waarmee organisaties te maken hebben. Het gaat met name over de objecten waarover ook gegevens worden vastgelegd. Het bedrijfsobjectmodel creëert een gemeenschappelijke taal voor de meest gebruikte objecten. De toepassing van het bedrijfsobjectmodel ligt vooral in het ondersteunen van organisatiebrede discussies over verantwoordelijkheden voor het beheren van gegevens. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Gegevensmanagement |  |  |
| BusinessObject | GEMMA en het GGM |  |  |
| BusinessObject | Privacy en Informatiebeveiliging | Thema-architectuur die privacy- en informatiebeveiliging uitwerkt. De thema-architectuur bevat veel verwijzingen naar voor gemeenten relevante informatie bij o.a. de NORA en de IBD. | Thema-architecturen: ja |
| BusinessObject | Betrouwbaarheidscriteria van referentiecomponenten |  |  |
| BusinessObject | Basisbeveiligingsniveau van referentiecomponenten |  |  |
| BusinessObject | Duurzame toegankelijkheid en transparantie |  | Thema-architecturen: ja |
| BusinessObject | Handreiking Selectielijst |  |  |
| BusinessObject | Duurzaam toegankelijk informatiebeheer | Dit document beschrijft in concept een aantal implicaties van en uitgangspunten voor duurzaam toegankelijk informatiebeheer in het GEMMA Gegevenslandschap. |  |
| BusinessObject | Eventorientatie | Het thema 'Zaakgericht Werken' beschrijft het waarom, wat en hoe van zaakgericht werken. | Thema-architecturen: ja |
| BusinessObject | Event-driven architectuur | Event-driven architectuur (EDA) is een architectuurbenaderijng waarbij los gekoppelde componenten via 'events' informatie over plaatsgevonden gebeurtenissen met elkaar uitwisselen |  |
| BusinessObject | Notificeren | Het via notificaties informeren over een bepaalde gebeurtenissen |  |
| BusinessObject | Zaakgericht werken | Het thema 'Zaakgericht Werken' beschrijft het waarom, wat en hoe van zaakgericht werken. | Thema-architecturen: ja |
| BusinessObject | Visie op zaakgericht werken |  |  |
| BusinessObject | Zaaktypen |  |  |
| BusinessObject | Informatiemodellen | De voor de gemeentelijke informatievoorziening relevante standaarden. Van een standaard worden enkele metagegevens vastgelegd, zoals de status, de beheerder en een verwijzing naar de specificaties van de standaard. Bron: GEMMA Online | Algemene producten: ja |
| BusinessObject | Common Ground |  | Thema-architecturen: ja |
| BusinessObject | Informatiekundige Visie Common Ground | In het document aanleiding vernieuwing gemeentelijke informatievoorziening wordt een uitgebreid overzicht gegeven van de noodzaak tot het vernieuwen van de gemeentelijke informatievoorziening. |  |
| BusinessObject | Informatiearchitectuur principes CG | In het document aanleiding vernieuwing gemeentelijke informatievoorziening wordt een uitgebreid overzicht gegeven van de noodzaak tot het vernieuwen van de gemeentelijke informatievoorziening. |  |
| BusinessObject | Globaal Programma van Eisen CG | Dit document bevat specificaties (eisen/wensen) voor softwarepakketten waarmee aan de architectuur van het GEMMA Gegevenslandschap kan worden voldaan. |  |
| BusinessObject | Aanleiding vernieuwing gemeentelijke informatievoorziening | In het document aanleiding vernieuwing gemeentelijke informatievoorziening wordt een uitgebreid overzicht gegeven van de noodzaak tot het vernieuwen van de gemeentelijke informatievoorziening. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | User story's voor informatiebeveiliging | Deze user story's kunnen worden gebruikt door ontwikkelteams (bij gemeenten of toeleveranciers) die oplossingen ontwikkelen in het kader van Common Ground. Zij kunnen de story's as-is gebruiken, of als leidraad dienen bij het opstellen van definitions of done. Bovendien kunnen de user stories bij inkoop van (software)producten of softwareontwikkeling door derden gebruikt worden als basis voor informatiebeveiligingseisen. |  |
| BusinessObject | Authenticatie en Autorisatie | Dit document beschrijft de visie van VNG Realisatie ten aanzien van authenticatie en autorisatie. |  |
| BusinessObject | Logging en verwerkingsactiviteiten | Thema-architectuur die uitwerkt hoe gemeenten in hun informatievoorziening verwerkingen kunnen loggen om te kunnen voldoen aan wet- en regelgeving. |  |
| BusinessObject | Common Ground vijflaagsmodel | Common Ground software is opgebouwd uit componenten in een architectuur op basis van het 5-lagen model. Hiermee creëren we meer flexibiliteit, spreiden we risico’s en wordt bovendien voorkomen dat een component meer doet dan waar het voor bedoeld is. |  |
| BusinessObject | Basisarchitectuur | De kern van de GEMMA met daarin o.a. architectuurprincipes en de GEMMA Bedrijfs-, Informatie- en Technische architectuur. | Basisarchitectuur: ja |
| BusinessObject | Informatiearchitectuur | De informatiearchitectuur beschrijft de inrichting van de informatievoorziening. Denk aan applicatieservices, applicaties en landelijke voorzieningen. Deze architectuur is als landelijke referentie ontwikkeld en is richtinggevend bij de inrichting van de gemeentelijke informatievoorziening. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Applicatie-interfaces |  | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Gebruik van standaarden | In de GEMMA wordt vastgelegd voor welke referentiecomponenten een standaard verplicht of aanbevolen is. De verplichte en aanbevolen standaarden kunnen door gemeenten worden gebruikt bij het opstellen van een pakket van eisen voor het aanschaffen van softwarepakketen. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en bedrijfsfuncties | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de bedrijfsfuncties de deze gebruiken | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en applicatieservices | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de ondersteunde applicatieservices | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Data-objecten | Een beschrijving van de structuur van de belangrijkste soorten en bronnen van data binnen de organisatie. Binnen de GEMMA beschrijven we applicaties en data in samenhang als onderdeel van de informatiearchitectuur. Data-architectuur wordt niet apart gemodelleerd. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Buitengemeentelijke voorzieningen |  |  |
| BusinessObject | Strategie en motivatie |  | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Kernwaarden en kwaliteitsdoelen | De GEMMA volgt de NORA kernwaarden, beleidskaders en kwaliteitsdoelen en voegt daar elementen vanuit gemeentelijk perspectief aan toe | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Achitectuurprincipes | Een principe is een normatieve eigenschap van alle systemen in een gegeven situatie of van de wijze waarop die systemen worden gerealiseerd. Bron: ArchiMate | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Implicaties |  | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Technische architectuur | The Technology Layer offers infrastructure services (e.g., processing, storage, and communication services) needed to run applications, realized by computer and communication hardware and system software. Bron: ArchiMate 2.1 | Basisarchitectuur: ja |
| BusinessObject | Technologiecomponenten en technologieservices |  |  |
| BusinessObject | Bedrijfsarchitectuur | De bedrijfsarchitectuur beschrijft wat de gemeente doet en hoe de gemeente dat doet. De bedrijfsarchitectuur wordt ondersteund door de informatievoorziening. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Procesarchitectuur | De GEMMA Procesarchitectuur biedt gemeenten ondersteuning bij het inrichten van de gemeentelijke processen. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Actoren en rollen | Het actoren en rollenmodel toont de (rechts)personen en organisatorische eenheden (actoren) en de verantwoordelijkheden (rollen) |  |
| BusinessObject | Domeinen | Uit het Gemeentelijk Gegevensmodel overgenomen indeling van bedrijfsobjecten | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Bedrijfsfunctiemodel | Een bedrijfsfunctiemodel beschrijft wat een organisatie doet onafhankelijk van hoe het wordt uitgevoerd. Het kijkt naar een organisatie als een verzameling van activiteiten die worden uitgevoerd en clustert deze tot logische eenheden die soortgelijke kennis en competenties vragen. De toepassingsmogelijkheden van een bedrijfsfunctiemodel zijn breed. Vanwege de stabiliteit van het model is het erg geschikt om gebruikt te worden als algemeen ankerpunt om andere modellen aan te relateren waarbij in eerste instantie nog niet gesproken wordt over organisatie- en IT-inrichting. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Beleidsdomeinen |  | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Architectuurvisie | Hoogover beschrijving van de gemaakte fundamentele keuzes voor ontwikkeling van de GEMMA | Basisarchitectuur: ja; Architectuurvisie: ja |
| BusinessObject | Algemene producten | Groep van producten die relevant zijn voor zowel de basisarchitectuur producten als de thema-architecturen | Algemene producten: ja |
| BusinessObject | Werken onder architectuur | Handreiking voor gemeenten hoe zij met GEMMA kunnen werken onder architectuur Dit zijn begeleidende documenten voor de verdere uitwerking van de GEMMA. | Algemene producten: ja |
| BusinessObject | Begrippenkader | Het GEMMA Begrippenkader geeft uitleg over begrippen die gebruikt worden binnen de GEMMA | Algemene producten: ja |
| BusinessObject | Doelgroepen |  | Algemene producten: ja |
| BusinessObject | Kennismodel | Definitie en toelichting op de in GEMMA architectuurmodel gebruikte elementtypen en relatietypen (is dus ook een begrippenkader). | Algemene producten: ja |
| BusinessObject | Werken met GEMMA ArchiMate-model |  | Algemene producten: ja |
| BusinessObject | Wat is GEMMA |  | Algemene producten: ja |
| BusinessObject | Standaardenlijst | De voor de gemeentelijke informatievoorziening relevante standaarden. Van een standaard worden enkele metagegevens vastgelegd, zoals de status, de beheerder en een verwijzing naar de specificaties van de standaard. Bron: GEMMA Online | Algemene producten: ja |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

## GEMMA portfolio compact

Hoofdindeling van de GEMMA en de basisarchitectuur

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Thema-architecturen | Een binnen de GEMMA voor een bepaald thema uitgewerkte architectuur | Thema-architecturen: ja |
| BusinessObject | Basisarchitectuur | De kern van de GEMMA met daarin o.a. architectuurprincipes en de GEMMA Bedrijfs-, Informatie- en Technische architectuur. | Basisarchitectuur: ja |
| BusinessObject | Informatiearchitectuur | De informatiearchitectuur beschrijft de inrichting van de informatievoorziening. Denk aan applicatieservices, applicaties en landelijke voorzieningen. Deze architectuur is als landelijke referentie ontwikkeld en is richtinggevend bij de inrichting van de gemeentelijke informatievoorziening. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Strategie en motivatie |  | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Technische architectuur | The Technology Layer offers infrastructure services (e.g., processing, storage, and communication services) needed to run applications, realized by computer and communication hardware and system software. Bron: ArchiMate 2.1 | Basisarchitectuur: ja |
| BusinessObject | Bedrijfsarchitectuur | De bedrijfsarchitectuur beschrijft wat de gemeente doet en hoe de gemeente dat doet. De bedrijfsarchitectuur wordt ondersteund door de informatievoorziening. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Architectuurvisie | Hoogover beschrijving van de gemaakte fundamentele keuzes voor ontwikkeling van de GEMMA | Basisarchitectuur: ja; Architectuurvisie: ja |
| BusinessObject | Algemene producten | Groep van producten die relevant zijn voor zowel de basisarchitectuur producten als de thema-architecturen | Algemene producten: ja |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

## GEMMA portfolio

Een gestructureerde weergave van de onderwerpen die de GEMMA beschrijft

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Thema-architecturen | Een binnen de GEMMA voor een bepaald thema uitgewerkte architectuur | Thema-architecturen: ja |
| BusinessObject | Zaakgericht werken | Het thema 'Zaakgericht Werken' beschrijft het waarom, wat en hoe van zaakgericht werken. | Thema-architecturen: ja |
| BusinessObject | Werken met API's |  | Thema-architecturen: ja |
| BusinessObject | Data | Thema-architectuur die aspecten met betrekking tot data uitwerkt. Bijvoorbeeld: datamanagement en data-uitwisseling. | Thema-architecturen: ja |
| BusinessObject | Duurzame toegankelijkheid en transparantie |  | Thema-architecturen: ja |
| BusinessObject | Privacy en Informatiebeveiliging | Thema-architectuur die privacy- en informatiebeveiliging uitwerkt. De thema-architectuur bevat veel verwijzingen naar voor gemeenten relevante informatie bij o.a. de NORA en de IBD. | Thema-architecturen: ja |
| BusinessObject | Common Ground |  | Thema-architecturen: ja |
| BusinessObject | Eventorientatie | Het thema 'Zaakgericht Werken' beschrijft het waarom, wat en hoe van zaakgericht werken. | Thema-architecturen: ja |
| BusinessObject | Basisarchitectuur | De kern van de GEMMA met daarin o.a. architectuurprincipes en de GEMMA Bedrijfs-, Informatie- en Technische architectuur. | Basisarchitectuur: ja |
| BusinessObject | Informatiearchitectuur | De informatiearchitectuur beschrijft de inrichting van de informatievoorziening. Denk aan applicatieservices, applicaties en landelijke voorzieningen. Deze architectuur is als landelijke referentie ontwikkeld en is richtinggevend bij de inrichting van de gemeentelijke informatievoorziening. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Applicatie-interfaces |  | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Gebruik van standaarden | In de GEMMA wordt vastgelegd voor welke referentiecomponenten een standaard verplicht of aanbevolen is. De verplichte en aanbevolen standaarden kunnen door gemeenten worden gebruikt bij het opstellen van een pakket van eisen voor het aanschaffen van softwarepakketen. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en bedrijfsfuncties | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de bedrijfsfuncties de deze gebruiken | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en applicatieservices | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de ondersteunde applicatieservices | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Data-objecten | Een beschrijving van de structuur van de belangrijkste soorten en bronnen van data binnen de organisatie. Binnen de GEMMA beschrijven we applicaties en data in samenhang als onderdeel van de informatiearchitectuur. Data-architectuur wordt niet apart gemodelleerd. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Buitengemeentelijke voorzieningen |  |  |
| BusinessObject | Strategie en motivatie |  | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Kernwaarden en kwaliteitsdoelen | De GEMMA volgt de NORA kernwaarden, beleidskaders en kwaliteitsdoelen en voegt daar elementen vanuit gemeentelijk perspectief aan toe | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Achitectuurprincipes | Een principe is een normatieve eigenschap van alle systemen in een gegeven situatie of van de wijze waarop die systemen worden gerealiseerd. Bron: ArchiMate | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Implicaties |  | Basisarchitectuur: ja; Strategie en motivatie: ja |
| BusinessObject | Technische architectuur | The Technology Layer offers infrastructure services (e.g., processing, storage, and communication services) needed to run applications, realized by computer and communication hardware and system software. Bron: ArchiMate 2.1 | Basisarchitectuur: ja |
| BusinessObject | Technologiecomponenten en technologieservices |  |  |
| BusinessObject | Bedrijfsarchitectuur | De bedrijfsarchitectuur beschrijft wat de gemeente doet en hoe de gemeente dat doet. De bedrijfsarchitectuur wordt ondersteund door de informatievoorziening. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Procesarchitectuur | De GEMMA Procesarchitectuur biedt gemeenten ondersteuning bij het inrichten van de gemeentelijke processen. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Domeinen | Uit het Gemeentelijk Gegevensmodel overgenomen indeling van bedrijfsobjecten | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Bedrijfsobjectmodel | Een bedrijfsobjectmodel beschrijft de objecten waarmee organisaties te maken hebben. Het gaat met name over de objecten waarover ook gegevens worden vastgelegd. Het bedrijfsobjectmodel creëert een gemeenschappelijke taal voor de meest gebruikte objecten. De toepassing van het bedrijfsobjectmodel ligt vooral in het ondersteunen van organisatiebrede discussies over verantwoordelijkheden voor het beheren van gegevens. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Bedrijfsfunctiemodel | Een bedrijfsfunctiemodel beschrijft wat een organisatie doet onafhankelijk van hoe het wordt uitgevoerd. Het kijkt naar een organisatie als een verzameling van activiteiten die worden uitgevoerd en clustert deze tot logische eenheden die soortgelijke kennis en competenties vragen. De toepassingsmogelijkheden van een bedrijfsfunctiemodel zijn breed. Vanwege de stabiliteit van het model is het erg geschikt om gebruikt te worden als algemeen ankerpunt om andere modellen aan te relateren waarbij in eerste instantie nog niet gesproken wordt over organisatie- en IT-inrichting. | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Beleidsdomeinen |  | Basisarchitectuur: ja; Bedrijfsarchitectuur: ja |
| BusinessObject | Architectuurvisie | Hoogover beschrijving van de gemaakte fundamentele keuzes voor ontwikkeling van de GEMMA | Basisarchitectuur: ja; Architectuurvisie: ja |
| BusinessObject | Algemene producten | Groep van producten die relevant zijn voor zowel de basisarchitectuur producten als de thema-architecturen | Algemene producten: ja |
| BusinessObject | Werken onder architectuur | Handreiking voor gemeenten hoe zij met GEMMA kunnen werken onder architectuur Dit zijn begeleidende documenten voor de verdere uitwerking van de GEMMA. | Algemene producten: ja |
| BusinessObject | Begrippenkader | Het GEMMA Begrippenkader geeft uitleg over begrippen die gebruikt worden binnen de GEMMA | Algemene producten: ja |
| BusinessObject | Doelgroepen |  | Algemene producten: ja |
| BusinessObject | Kennismodel | Definitie en toelichting op de in GEMMA architectuurmodel gebruikte elementtypen en relatietypen (is dus ook een begrippenkader). | Algemene producten: ja |
| BusinessObject | Werken met GEMMA ArchiMate-model |  | Algemene producten: ja |
| BusinessObject | Standaardenlijst | De voor de gemeentelijke informatievoorziening relevante standaarden. Van een standaard worden enkele metagegevens vastgelegd, zoals de status, de beheerder en een verwijzing naar de specificaties van de standaard. Bron: GEMMA Online | Algemene producten: ja |
| BusinessObject | Wat is GEMMA |  | Algemene producten: ja |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

## KCA portfolio

Hoofdindeling van de producten van het Kenniscentrum Architectuur

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Kenniscentrum architectuur portfolio | Verzameling van producten die door het KCA worden geleverd |  |
| BusinessObject | Projectarchitecturen | Groep van projecten die gebruik maken van de GEMMA |  |
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | VNG standaarden | De door het KCA beheerde standaardspecificaties en ondersteunende voorzieningen |  |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

### Notities

- GEMMA doelgroepen en VNG persona's
- GEMMA portfolio
- KCA kanalen

## KCA portfolio standaarden en projecten

Producten die onderdeel zijn van de VNG standaarden

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessObject | Kenniscentrum architectuur portfolio | Verzameling van producten die door het KCA worden geleverd |  |
| BusinessObject | Projectarchitecturen | Groep van projecten die gebruik maken van de GEMMA |  |
| BusinessObject | Verwerkingenlogging API project | Voor het vastleggen van verwerkingen van (persoons)gegevens vanuit procesapplicaties en de ontsluiting van die gegevens naar geautoriseerde afnemers is de Verwerkingenlogging API-standaard ontwikkeld |  |
| BusinessObject | Omgevingswet | Ter ondersteuning van de uitvoering van de nieuwe Omgevingswet ontwikkelt VNG in samenwerking met gemeenten en andere overheidspartijen een doelarchitectuur voor de Omgevingswet. Een doelarchitectuur voor 2022 en daarmee een groeipad voor nu. Met de komst van de nieuwe Omgevingswet moet onder andere de inzichtelijkheid en het gebruiksgemak van het omgevingsrecht worden vergroot. Bron: GEMMA online |  |
| BusinessObject | Omnichannel | Thema-architectuur die uitwerkt hoe gemeenten hun informatievoorziening zo kunnen inrichten dat burgers en bedrijven meerdere kanalen kunnen gebruiken waarbij het resultaat hetzelfde is | Thema-architecturen: ja |
| BusinessObject | Totaal 3 Dimensionaal (T3D) | Met de T3D architectuur wordt richting gegeven aan initiatieven die gemeenten willen uitvoeren op het gebied van 3D objectbeheer. De T3D architectuur beschrijft welke kaders er zijn en beschrijft daarnaast inrichtingsonafhankelijk wat er nodig is om 3D objectbeheer toe te passen. |  |
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | VNG standaarden | De door het KCA beheerde standaardspecificaties en ondersteunende voorzieningen |  |
| BusinessObject | GEMMA Zaaktypecatalogus | De ZTC2 helpt gemeenten om het proces vanuit de 'vraag van een klant' (productaanvraag, melding, aangifte, informatieverzoek e.d.) tot en met het leveren van een passend antwoord daarop in te richten, inclusief de bijbehorende informatievoorziening. |  |
| BusinessObject | API-standaarden | * (API-)standaard: Een standaard of norm is een (technisch) document met erkende afspraken, specificaties of criteria over een product, dienst of methode. Standaarden dragen eraan bij dat processen op een afgesproken, veilige, betrouwbare en consistente manier uitgevoerd worden. * API-specificatie: Een (technisch) document welke een nauwkeurige en accurate beschrijving geeft van de opzet en bijzonderheden van een API. * API: Software die ervoor zorgt dat verschillende systemen gegevens met elkaar kunnen delen en uitwisselen. |  |
| BusinessObject | ZGW API-standaarden |  |  |
| BusinessObject | Verwerkingenlogging API-standaard |  |  |
| BusinessObject | Regels bij activiteiten API |  |  |
| BusinessObject | Standaardisatieleidraad | De Standaardisatieleidraad biedt ondersteuning bij de ontwikkeling van standaarden om tot een ‘vastgestelde VNG uitwisselstandaarden’ te komen. Het wordt aanbevolen de stappen in deze leidraad bij de ontwikkeling van uitwisselstandaarden te volgen. |  |
| BusinessObject | Ontwikkelagenda API-standaarden | De Ontwikkelagenda API-standaarden is een dynamisch overzicht van API-specificaties voor gegevensuitwisseling in het gemeentelijk domein. |  |
| BusinessObject | Gegevens- en berichtenstandaarden | De gegevens- en berichtenarchitectuur geven we vorm met de GEMMA-gegevens- en -berichtenstandaarden. Deze richten zich op de uitwisseling van gegevens binnen een gemeente, tussen een gemeente en andere overheden en ten behoeve van de dienstverlening aan burgers en bedrijven. Bron: GEMMA Online |  |
| BusinessObject | Berichtenstandaarden (StUF) | De gemeentelijke berichtenstandaarden zijn gebaseerd op het Standaard UitwisselFormaat, kortweg StUF. StUF schrijft de vorm voor waarin de gegevens uitgewisseld moeten worden en regelt onder meer de communicatie over verschillende ICT-infrastructuren. De structuren waarin gegevens uitgewisseld worden leggen we vast in berichtenstandaarden zoals sectormodellen en koppelvlakken. Er zijn berichtstandaarden voor: * Basis- en kerngegevens * Zaken en documenten * Dienstverleningsdomein * Ruimtelijk domein * Sociaal domein * Bedrijfsvoeringsdomein Bron: GEMMA Online |  |
| BusinessObject | Informatiemodel | Een informatiemodel vormt de formele beschrijving van alle informatie die van belang is binnen een gegeven domein. Een informatiemodel beschrijft dit domein in termen van objecten, gegevens (attributen) daarvan en relaties daartussen en doet dat op een inhoudelijke manier. Met inhoudelijk (of semantisch) bedoelen we dat er geen enkele relatie is naar een mogelijke implementatie of toepassingsomgeving (software). Er worden geen regels toegepast die gerelateerd zijn aan de manier waarop de informatie ingewonnen, opgeslagen, beheerd en uitgewisseld wordt. Er wordt puur naar de semantiek gekeken. Voorbeelden zijn: RSGB, RGBZ en ImZTC. Bron: GEMMA Online |  |
| BusinessObject | RSGB |  |  |
| BusinessObject | RGBZ |  |  |
| BusinessObject | Compliancy testset | Een compliancy testset beschrijft de testdekking en de testscenario’s die minimaal uitgevoerd moeten worden door een leverancier om compliancy van zijn softwareproduct op een standaard aan te tonen. De testen dienen voorafgaand aan in productiename van het softwareproduct uitgevoerd te worden. Een testscenario bestaat uit één of meerdere StUF berichten die tussen het StUF Testplatform en de geteste applicatie zijn uitgewisseld. Bron: GEMMA Online |  |
| BusinessObject | Compliancy | Compliancy beschrijft de mate waarin overeengekomen afspraken en conventies daadwerkelijk worden gerealiseerd. Het gaat over het nakomen van normen of het zich er naar schikken. Het toetsen van compliancy is erop gericht om inzicht te krijgen in de mate van realisatie, maar ook op het ontdekken van aanknopingspunten voor het verder ontwikkelen en uitwerken van standaarden. Bron: GEMMA Online |  |
| BusinessObject | StUF Testplatform (STP) | Het StUF Testplatform is een onafhankelijk testinstrument voor het testen van koppelingen gebaseerd op StUF. Leveranciers kunnen het platform gebruiken tijdens de ontwikkeling van softwareproducten en om aan te tonen dat een koppeling werkt volgens de regels van een StUF standaard. Voor gemeenten geven de testrapportages uit het StUF Testplatform inzicht in de kwaliteit van het juist toepassen van de StUF standaard. Bron: https://vng.nl/projecten/stuf-testplatform |  |
| BusinessObject | API Testvoorziening (ATV) |  |  |
| Grouping | Gebruik van de GEMMA door VNG | Groep van producten van de VNG waarin één of meerdere GEMMA producten worden gebruikt |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| BusinessObject | VNG-projecten | Korte introductie van en verwijzigen naar (architectuur)projecten met relevantie voor de GEMMA - Wat is Common Ground en hoe sluit het aan op de GEMMA |  |
| BusinessObject | GIBIT |  |  |
| BusinessObject | VNG-standaardspecificaties | Introducte van en verwijzigen naar door VNG ontwikkelde en beheerde standaardspecificaties., waaronder Informatiemodellen, StUF en API's | Standaarden: ja; GEMMA: nee |

### Notities

- GEMMA portfolio

## KCA kanalen

Overzicht van de Websites waar GEMMA architectuurproducten getoond worden.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Grouping | Communicatiekanalen & voorzieningen | Faciliteiten die bijdragen aan de verdere totstandkoming van de GEMMA |  |
| ApplicationInterface | forum.vng.nl |  |  |
| BusinessObject | Forum Regie op ICT | In het VNG Forum Regie op ICT vindt u nadere toelichting op het gebruik van de Softwarecatalogus en Gemmaonline. |  |
| ApplicationInterface | Softwarecatalogus.nl | Website van de softwarecatalogus |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| ApplicationInterface | VNG.nl |  |  |
| BusinessObject | Gemeentelijke Model Architectuur (GEMMA) |  |  |
| BusinessObject | VNG (vastgestelde) standaarden |  |  |
| BusinessObject | GIBIT |  |  |
| ApplicationInterface | github.com/VNG-Realisatie | Github landingspagina van VNG Realisatie voor de ontwikkeling van standaarden |  |
| BusinessObject | VNG standaarden | De door het KCA beheerde standaardspecificaties en ondersteunende voorzieningen |  |
| Grouping | VNG Archi-repositories | Verzameling van door VNG beheerde ArchiMate repositories. De repository is de fysieke opslag van een architectuurmodel. Opslag met behulp van git maakt versiebeheer en samenwerking in één model mogelijk. |  |
| ApplicationInterface | GEMMA Online | Publicatieomgeving voor de GEMMA en VNG projecten met een sterke architectuurcomponent |  |
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Projectarchitecturen | Groep van projecten die gebruik maken van de GEMMA |  |

## Wiki applicatiearchitectuur

Welke functionaliteit bieden de verschillende onderdelen van het WikiXL platform

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| TechnologyService | WikiXL™ cloud service | De door de leverancier ArchiXL beheerde wiki services |  |
| ApplicationComponent | GEMMA wiki | Het wiki-platform waarop de GEMMA geschreven en gepubliceerd wordt |  |
| ApplicationInterface | GEMMA redactie wiki | Toegang tot de interne redactieomgeving. De redactieomgeving is voor de redacteuren om te schrijven en te ontwikkelen. |  |
| ApplicationInterface | GEMMA publicatie wiki | Toegang tot de publieke GEMMA wiki |  |
| ApplicationComponent | MediaWiki | MediaWiki is the software on which Wikipedia is built. |  |
| ApplicationFunction | Editen en tonen van wikipagina's |  |  |
| ApplicationFunction | Gebruikersbeheer |  |  |
| ApplicationComponent | WikiXL™ kennismanagementplatform | WikiXL™ is een semantisch wikiplatform waarmee data, informatie en kennis eenvoudig kunnen worden gedeeld binnen en buiten uw organisatie. Het maakt het mogelijk om naast teksten ook gestructureerde informatie beschikbaar te stellen, waardoor een rijke combinatie van content ontstaat. |  |
| ApplicationComponent | SmartConnectArchiMate™ | SmartConnect™ biedt een koppelvlak voor het importeren en exporteren van ArchiMate™ modellen uit willekeurig welke architectuurtool, voor zover dat de ArchiMate Exchange Format standaard van The Open Group ondersteunt. |  |
| ApplicationFunction | Importeren, tonen en exporteren ArchiMate-modellen |  |  |
| ApplicationComponent | SmartConnectSoftwarecatalogus | Maatwerk toevoegingen aan SmartConnectArchiMate™ voor het importeren van het GEMMA model en het tonen van specifieke GEMMA concepten |  |
| ApplicationFunction | Importeren, exporteren en SWC API |  |  |
| ApplicationComponent | SmartComments™ | SmartFeedback™ biedt gebruikers van een wiki de mogelijkheid opmerkingen te plaatsen over wikipagina's, op een gebruiksvriendelijke wijze via formulieren gekoppeld aan de ‘Overleg’-tab die op elke wikipagina getoond wordt. Redacteuren kunnen op de opmerkingen reageren, en de status van elke opmerking monitoren en beheren. Ook kunnen zij overzichten maken van openstaande opmerkingen; |  |
| ApplicationFunction | Reviewen van wikipagina's |  |  |
| ApplicationComponent | SmartPublish™ | SmartPublish™ biedt een afgeschermde ontwikkelwiki waarin gewerkt kan worden aan nieuwe content of wijzigingen in bestaande content. Hierdoor wordt een gecontroleerd redactie- en publicatieproces mogelijk. |  |
| ApplicationFunction | Publiceren vanuit een afgeschermde wiki |  |  |
| ApplicationComponent | SmartCore™ | SmartCore™ is een uitbreiding om eenvoudig kennismodellen te configureren. Een kennismodel bepaalt de structuur en het datamodel van de informatie in de wiki en vormt daarmee de basis. |  |
| ApplicationFunction | Configureren en tonen objecten kennismodel |  |  |
| ApplicationComponent | Semantic MediaWiki (SMW) | Semantic MediaWiki (or SMW for short) is an extension to the well-known MediaWiki software. The purpose of SMW is to allow users to improve the structure and organization of the knowledge in a wiki by adding simple, machine-processable information to wiki articles. With this additional information, you can greatly improve searching, browsing, and sharing the wiki's knowledge; both within the wiki's pages and from external computer programs. |  |
| ApplicationFunction | Structured data in wiki pages |  |  |
| ApplicationService | Beheer en publicatie van teksten en media |  |  |
| ApplicationService | Beheer en publicatie van gestructureerde data |  |  |
| ApplicationService | Beheer en publicatie van (ArchiMate-)modellen |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| WikiXL™ cloud service | Serving |  | MediaWiki |  |
| WikiXL™ cloud service | Serving |  | Semantic MediaWiki (SMW) |  |
| WikiXL™ cloud service | Serving |  | WikiXL™ kennismanagementplatform |  |
| MediaWiki | Realization |  | Beheer en publicatie van teksten en media |  |
| WikiXL™ kennismanagementplatform | Realization |  | Beheer en publicatie van (ArchiMate-)modellen |  |
| Semantic MediaWiki (SMW) | Realization |  | Beheer en publicatie van gestructureerde data |  |
| Beheer en publicatie van teksten en media | Serving |  | GEMMA wiki |  |
| Beheer en publicatie van gestructureerde data | Serving |  | GEMMA wiki |  |
| Beheer en publicatie van (ArchiMate-)modellen | Serving |  | GEMMA wiki |  |

## GEMMA en Softwarecatalogus

Welke onderdelen uit de GEMMA en de projectarchitecturen worden gebruikt in de Softwarecatalogus

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationInterface | Softwarecatalogus.nl | Website van de softwarecatalogus |  |
| BusinessObject | Softwarecatalogus | De Softwarecatalogus is het online informatiesysteem van de gemeentelijke softwaremarkt. IT-leveranciers presenteren op de GEMMA Softwarecatalogus hun aanbod voor de gemeentelijke markt, en ze spelen in op de ondersteuning van de standaarden. Gemeenten gebruiken de GEMMA Softwarecatalogus bij ICT-vervangings- of investeringsvraagstukken. Gemeenten registreren de gebruikte software en koppelingen en kunnen onderling kennis en informatie uitwisselen. |  |
| ApplicationInterface | github.com/VNG-Realisatie | Github landingspagina van VNG Realisatie voor de ontwikkeling van standaarden |  |
| Grouping | VNG Archi-repositories | Verzameling van door VNG beheerde ArchiMate repositories. De repository is de fysieke opslag van een architectuurmodel. Opslag met behulp van git maakt versiebeheer en samenwerking in één model mogelijk. |  |
| Artifact | Omgevingswet Archi-repository | Thema Omgevingswet Voor 2021 staat een nieuwe Nederlandse Omgevingswet op stapel. Deze wet richt zich op onze fysieke leefomgeving. Hiermee worden onder andere bouwwerken, infrastructuur, water, bodem, lucht, landschappen, natuur en cultureel erfgoed bedoeld. Een belangrijk onderwerp, want vrijwel alle activiteiten die burgers, bedrijven en overheden uitvoeren hebben grote invloed op de fysieke leefomgeving. |  |
| Artifact | GEMMA Archi-repository |  |  |
| ApplicationInterface | GEMMA Online | Publicatieomgeving voor de GEMMA en VNG projecten met een sterke architectuurcomponent |  |
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Informatiearchitectuur | De informatiearchitectuur beschrijft de inrichting van de informatievoorziening. Denk aan applicatieservices, applicaties en landelijke voorzieningen. Deze architectuur is als landelijke referentie ontwikkeld en is richtinggevend bij de inrichting van de gemeentelijke informatievoorziening. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Gebruik van standaarden | In de GEMMA wordt vastgelegd voor welke referentiecomponenten een standaard verplicht of aanbevolen is. De verplichte en aanbevolen standaarden kunnen door gemeenten worden gebruikt bij het opstellen van een pakket van eisen voor het aanschaffen van softwarepakketen. | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en applicatieservices | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de ondersteunde applicatieservices | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Referentiecomponenten en bedrijfsfuncties | Weergave van de in een gemeente gebruikte referentiecomponenten geordend binnen de bedrijfsfuncties de deze gebruiken | Basisarchitectuur: ja; Informatiearchitectuur: ja |
| BusinessObject | Algemene producten | Groep van producten die relevant zijn voor zowel de basisarchitectuur producten als de thema-architecturen | Algemene producten: ja |
| BusinessObject | Standaardenlijst | De voor de gemeentelijke informatievoorziening relevante standaarden. Van een standaard worden enkele metagegevens vastgelegd, zoals de status, de beheerder en een verwijzing naar de specificaties van de standaard. Bron: GEMMA Online | Algemene producten: ja |
| BusinessObject | Projectarchitecturen | Groep van projecten die gebruik maken van de GEMMA |  |
| BusinessObject | Omgevingswet | Ter ondersteuning van de uitvoering van de nieuwe Omgevingswet ontwikkelt VNG in samenwerking met gemeenten en andere overheidspartijen een doelarchitectuur voor de Omgevingswet. Een doelarchitectuur voor 2022 en daarmee een groeipad voor nu. Met de komst van de nieuwe Omgevingswet moet onder andere de inzichtelijkheid en het gebruiksgemak van het omgevingsrecht worden vergroot. Bron: GEMMA online |  |
| BusinessObject | Referentiecomponenten op Omgevingswet views |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Softwarecatalogus.nl | Access |  | Referentiecomponenten op Omgevingswet views |  |
| Softwarecatalogus.nl | Access |  | Standaardenlijst |  |
| Softwarecatalogus.nl | Access |  | Informatiearchitectuur |  |
| Omgevingswet Archi-repository | Realization |  | Omgevingswet |  |
| GEMMA Archi-repository | Realization |  | GEMMA |  |

## Koppeling wiki en Architectuurtool

Hoe de architectuurtools Archi en het WikiXL platform architectuurmodellen uitwisselen

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | WikiXL™ kennismanagementplatform | WikiXL™ is een semantisch wikiplatform waarmee data, informatie en kennis eenvoudig kunnen worden gedeeld binnen en buiten uw organisatie. Het maakt het mogelijk om naast teksten ook gestructureerde informatie beschikbaar te stellen, waardoor een rijke combinatie van content ontstaat. |  |
| ApplicationComponent | SmartConnectArchiMate™ | SmartConnect™ biedt een koppelvlak voor het importeren en exporteren van ArchiMate™ modellen uit willekeurig welke architectuurtool, voor zover dat de ArchiMate Exchange Format standaard van The Open Group ondersteunt. |  |
| ApplicationFunction | Importeren, tonen en exporteren ArchiMate-modellen |  |  |
| ApplicationComponent | SmartConnectSoftwarecatalogus | Maatwerk toevoegingen aan SmartConnectArchiMate™ voor het importeren van het GEMMA model en het tonen van specifieke GEMMA concepten |  |
| ApplicationFunction | Importeren, exporteren en SWC API |  |  |
| DataObject | ArchiMate-model in SmartCore format | Geïmporteerde ArchiMate-objecten omgezet in pagina's met eigenschappen uit het SmartCoreArchiMate kennismodel |  |
| Artifact | cache AMEFF publicatiebestand | SmartCore architectuurmodel omgezet naar AMEFF bestand. Het gegeneerde bestand wordt als cache gebruikt voor download en het maken van een SWC AMEFF export |  |
| ApplicationComponent | Archi | Open source architectuur modelleringstool |  |
| Artifact | GEMMA AMEFF-bestand |  |  |
| ApplicationInterface | Beheren Archimate-modellen | Formulier voor het importeren, exporteren, tonen en verwijderen van ArchiMate-modellen |  |
| Artifact | AMEFF publicatiebestand ArchiMate-model |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| WikiXL™ kennismanagementplatform | Access | Export | AMEFF publicatiebestand ArchiMate-model |  |
| WikiXL™ kennismanagementplatform | Composition |  | Beheren Archimate-modellen |  |
| WikiXL™ kennismanagementplatform | Access | Download | AMEFF publicatiebestand ArchiMate-model |  |
| WikiXL™ kennismanagementplatform | Access | Import | GEMMA AMEFF-bestand |  |
| Archi | Access | export | GEMMA AMEFF-bestand |  |
| Archi | Access | Import from AMEFF | AMEFF publicatiebestand ArchiMate-model |  |

## Koppeling GEMMA-GGM

De GGM-community stelt een CSV-bestand op met de GGM-objecten en relaties. Dit bestand wordt door VNG KCA ingelezen en verwerkt in de GEMMA. De resulterende bedrijfsobjecten worden vervolgens in een CSV-bestand teruggeleverd.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Artifact | GGM export csv-bestanden | Afgesproken kolommen voor aanleveren Gemeentelijk GegevensModel in csv formaat |  |
| Artifact | GEMMA bedrijfsobjecten csv-bestanden |  |  |
| BusinessActor | KCA - Kenniscentrum architectuur |  |  |
| ApplicationComponent | Archi | Open source architectuur modelleringstool |  |
| ApplicationComponent | jArchi scripting |  |  |
| DataObject | GEMMA-GGM ArchiMate-model |  |  |
| DataObject | GEMMA ArchiMate-model |  |  |
| Artifact | GEMMA-GGM Archi-repository |  |  |
| Artifact | GEMMA Archi-repository |  |  |
| Artifact | GEMMA-GGM Archi-bestand |  |  |
| BusinessActor | Community Gemeentelijk Gegevensmodel (GGM) |  |  |
| ApplicationComponent | python script |  |  |
| ApplicationComponent | Enterprise Architect (Sparx) |  |  |
| DataObject | GGM UML-model |  |  |
| Artifact | GGM EA-database |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Archi | Access |  | GEMMA-GGM Archi-repository |  |
| Archi | Access |  | GEMMA Archi-repository |  |
| jArchi scripting | Access |  | GGM export csv-bestanden |  |
| jArchi scripting | Access |  | GEMMA bedrijfsobjecten csv-bestanden |  |
| GEMMA-GGM ArchiMate-model | Association | save | GEMMA-GGM Archi-bestand |  |
| GEMMA-GGM Archi-bestand | Association | import | GEMMA ArchiMate-model |  |
| python script | Access |  | GEMMA bedrijfsobjecten csv-bestanden |  |
| python script | Access |  | GGM export csv-bestanden |  |
| python script | Access |  | GGM EA-database |  |
| Enterprise Architect (Sparx) | Access |  | GGM EA-database |  |

### Notities

- Draai scripts * importeer GGM objecten en relaties * afleiden bedrijfsobjecten * genereer views
- Draai script * exporteer GEMMA bedrijfsobjecten
- Modelleren * relateren bedrijfsobjecten aan domeinen en * bv. bedrijfsfuncties
- Modelleren GEMMA bedrijfsobjecten * markeren kandidaat bedrijfsobjecten * doorontwikkelen en onderhouden bedrijfsobjecten
- draai script * exporteer GGM objects en relations
- draai script * importeer GEMMA bedrijfsobjecten
- Modelleren GGM * bepalen wat met de GEMMA bedrijfsobjectdefinities wordt gedaan
- Modelleren GGM * doorontwikkelen en onderhouden GGM UML model

## Wiki technische architectuur

Technische architectuur van het WikiXL-platform

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| TechnologyService | WikiXL™ cloud service | De door de leverancier ArchiXL beheerde wiki services |  |
| ApplicationComponent | GEMMA wiki | Het wiki-platform waarop de GEMMA geschreven en gepubliceerd wordt |  |
| ApplicationInterface | GEMMA redactie wiki | Toegang tot de interne redactieomgeving. De redactieomgeving is voor de redacteuren om te schrijven en te ontwikkelen. |  |
| ApplicationInterface | GEMMA publicatie wiki | Toegang tot de publieke GEMMA wiki |  |
| Node | Wiki node |  |  |
| SystemSoftware | MediaWiki |  |  |
| SystemSoftware | Semantic MediaWiki extensie |  |  |
| SystemSoftware | WikiXL extensies |  |  |
| SystemSoftware | Database-systeem |  |  |
| Artifact | Redactie database |  |  |
| Artifact | Publicatie database |  |  |
| SystemSoftware | OS, ... |  |  |
| Grouping | Omgeving VNG | Toegankelijk voor VNG |  |
| Device | Productieserver | Server voor schrijven en publiceren van de GEMMA architectuur |  |
| Device | Staging-server | Server voor acceptatietesten nieuwe versies en functionaliteit |  |
| Grouping | Omgeving leverancier |  |  |
| Device | Testserver | Server voor het (integratie)testen van nieuwe functionaliteit |  |
| Device | Ontwikkelwerkplek | Server voor het ontwikkelen van nieuwe functionaliteit. |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| WikiXL™ cloud service | Serving |  | GEMMA wiki |  |
| Wiki node | Aggregation |  | Testserver |  |
| Wiki node | Aggregation |  | Productieserver |  |
| Wiki node | Aggregation |  | Staging-server |  |
| Wiki node | Realization |  | WikiXL™ cloud service |  |
| Wiki node | Aggregation |  | Ontwikkelwerkplek |  |

## Koppeling wiki en Softwarecatalogus

Hoe de wiki het GEMMA ArchiMate-model beschikbaar stelt aan de Softwarecatalogus

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationInterface | SWC API |  |  |
| ApplicationInterface | Export | Genereer een gemeentespecifiek ArchiMate-model in ArchiMate Exchange Format (AMEFF) |  |
| ApplicationInterface | List | Beschikbaarstellen GEMMA standaarden en referentiecomponenten |  |
| ApplicationInterface | View | Genereer een plaat in SVG formaat van gemeentelijke pakketten geplot op een bepaalde ArchiMate view |  |
| ApplicationComponent | Softwarecatalogus |  |  |
| ApplicationFunction | Toon kaart | Tonen van gemeentelijke pakketten op een bepaalde view. |  |
| ApplicationFunction | Download AMEFF export |  |  |
| ApplicationFunction | Importeer ArchiMate objecten | Bijwerken van de referentiecomponenten, standaarden en beschikbare views vanuit de list-API |  |
| Artifact | AMEFF export met pakketten | Gemeentespecifiek ArchiMate-model in ArchiMate Exchange Format (AMEFF) |  |
| Artifact | SVG architectuurplaat met pakketten | Plaat van gemeentelijke pakketten geplot op een ArchiMate view |  |
| ApplicationComponent | WikiXL™ kennismanagementplatform | WikiXL™ is een semantisch wikiplatform waarmee data, informatie en kennis eenvoudig kunnen worden gedeeld binnen en buiten uw organisatie. Het maakt het mogelijk om naast teksten ook gestructureerde informatie beschikbaar te stellen, waardoor een rijke combinatie van content ontstaat. |  |
| ApplicationComponent | SmartConnectArchiMate™ | SmartConnect™ biedt een koppelvlak voor het importeren en exporteren van ArchiMate™ modellen uit willekeurig welke architectuurtool, voor zover dat de ArchiMate Exchange Format standaard van The Open Group ondersteunt. |  |
| ApplicationFunction | Importeren, tonen en exporteren ArchiMate-modellen |  |  |
| ApplicationComponent | SmartConnectSoftwarecatalogus | Maatwerk toevoegingen aan SmartConnectArchiMate™ voor het importeren van het GEMMA model en het tonen van specifieke GEMMA concepten |  |
| ApplicationFunction | Importeren, exporteren en SWC API |  |  |
| DataObject | ArchiMate-model in SmartCore format | Geïmporteerde ArchiMate-objecten omgezet in pagina's met eigenschappen uit het SmartCoreArchiMate kennismodel |  |
| Artifact | cache AMEFF publicatiebestand | SmartCore architectuurmodel omgezet naar AMEFF bestand. Het gegeneerde bestand wordt als cache gebruikt voor download en het maken van een SWC AMEFF export |  |
| BusinessProcess | Werken met SWC |  |  |
| BusinessProcess | Releasen ArchiMate-model |  |  |
| BusinessProcess | Importeren GEMMA in Softwarecatalogus |  |  |
| BusinessProcess | Publiceren GEMMA |  |  |
| BusinessActor | Gemeente | Een gemeente is een groep van woonkernen (dorpen, steden) met het bijbehorende gebied die samen worden bestuurd door een politiek apparaat. | Bron: Softwarecatalogus; Toelichting: Eigenschappen van een gemeente * GEMMA type='Gemeente' * Object ID - Unieke sleutel van een gemeente; GUID gegenereerd door Softwarecatalogus * CBS code - Unieke gemeente code toegekend door het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties in samenwerking met het CBS.; Toelichting: Basisgegevens * Object GUID * Naam * Beschrijving * Toelichting * Elementtype=''Gemeente'' Gemeente gegevens * Gemeente CBS -> SWC en persoonsgegevens die niet meegaan in het architectuurmodel * Gemeente contact -> * Gemeente Contact email -> Gemeente e-mail * Voortgang -> Gemeente voortgang * Laatste activiteit -> Gemeente laatste wijziging |
| BusinessActor | VNG |  |  |
| TechnologyService | SWC opslag |  |  |
| Artifact | Softwarecatalogus database | Database met gemeentelijke pakketten ingedeeld volgens de GEMMA referentiearchitectuur |  |
| BusinessActor | Leverancier (Visma Roxit) | Aanbieders van standaard-software(pakketten) voor gemeentelijke taken. Alleen leveranciers die het convenant met VNG/KING ondertekend hebben, mogen hun gegevens in de Softwarecatalogus zetten. | Toelichting: De AMEFF export bevat de leveranciers van de door de gemeente gebruikte pakketten; Eigenschappen van een leverancier * GEMMA type='Leverancier' * Object ID - Unieke sleutel van een leveranciers; GUID gegenereerd door Softwarecatalogus * URL - Website van de leverancier |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Export | Serving | genereer AMEFF met pakketten | Download AMEFF export |  |
| List | Serving | importeren ArchiMate-objecten | Importeer ArchiMate objecten |  |
| View | Serving | genereer view met pakketten | Toon kaart |  |
| Softwarecatalogus | Serving |  | Importeren GEMMA in Softwarecatalogus |  |
| Softwarecatalogus | Serving |  | Werken met SWC |  |
| Importeer ArchiMate objecten | Access |  | Softwarecatalogus database |  |
| WikiXL™ kennismanagementplatform | Serving |  | Publiceren GEMMA |  |
| SmartConnectSoftwarecatalogus | Composition |  | SWC API |  |
| Publiceren GEMMA | Triggering |  | Importeren GEMMA in Softwarecatalogus |  |
| Gemeente | Assignment |  | Werken met SWC |  |
| VNG | Assignment |  | Releasen ArchiMate-model |  |
| Leverancier (Visma Roxit) | Assignment |  | Werken met SWC |  |

## Releasen ArchiMate-model

Proces voor het releasen van het GEMMA ArchiMate-model op GEMMA online en de Softwarecatalogus

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Archi | Open source architectuur modelleringstool |  |
| Artifact | GEMMA AMEFF-bestand |  |  |
| ApplicationComponent | GEMMA wiki | Het wiki-platform waarop de GEMMA geschreven en gepubliceerd wordt |  |
| ApplicationComponent | Softwarecatalogus |  |  |
| ApplicationInterface | SWC API |  |  |
| BusinessProcess | Bijwerken GEMMA |  |  |
| BusinessProcess | Controleren release |  |  |
| BusinessProcess | Exporteren AMEFF-bestand |  |  |
| BusinessProcess | Modelleren GEMMA ArchiMate-model |  |  |
| BusinessProcess | Publiceren GEMMA |  |  |
| BusinessProcess | Importeren AMEFF bestand |  |  |
| BusinessProcess | Controleren import |  |  |
| BusinessProcess | Importeren GEMMA in Softwarecatalogus |  |  |
| BusinessProcess | Importeren |  |  |
| BusinessProcess | Indexeren |  |  |
| BusinessProcess | Controleren import |  |  |
| BusinessProcess | Configureren |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Archi | Serving |  | Bijwerken GEMMA |  |
| Archi | Access | export | GEMMA AMEFF-bestand |  |
| GEMMA wiki | Access | import | GEMMA AMEFF-bestand |  |
| GEMMA wiki | Composition |  | SWC API |  |
| GEMMA wiki | Serving |  | Publiceren GEMMA |  |
| Softwarecatalogus | Serving |  | Importeren GEMMA in Softwarecatalogus |  |
| SWC API | Serving | import | Softwarecatalogus |  |
| Bijwerken GEMMA | Triggering |  | Publiceren GEMMA |  |
| Controleren release | Triggering |  | Exporteren AMEFF-bestand |  |
| Modelleren GEMMA ArchiMate-model | Triggering |  | Controleren release |  |
| Publiceren GEMMA | Triggering |  | Importeren GEMMA in Softwarecatalogus |  |
| Importeren AMEFF bestand | Triggering |  | Controleren import |  |
| Importeren | Triggering |  | Indexeren |  |
| Indexeren | Triggering |  | Controleren import |  |
| Configureren | Triggering |  | Importeren |  |

## GitHub Archi-repositorie inrichting

Autorisatiestructuur voor (schrijf)toegang tot de Archi-repositories

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessRole | team Archi |  |  |
| BusinessRole | team Archi-admin |  |  |
| Artifact | test Archi-repository |  |  |
| Artifact | Archi-script |  |  |
| BusinessRole | team Archi-GEMMA |  |  |
| Artifact | GEMMA portfolio Archi-repository | De fysieke opslag van het GEMMA portfoliomodel |  |
| Artifact | GEMMA Archi-repository |  |  |
| Artifact | GEMMA Kennismodel Archi-repository | Het GEMMA kennismodel toont de ArchiMate concepten en de onderlinge samenhang van de concepten zoals deze zijn uitgewerkt in het GEMMA architectuurmodel. |  |
| BusinessRole | team Archi-projecten |  |  |
| Artifact | Omnichannel Archi-repository |  |  |
| Artifact | Omgevingswet Archi-repository | Thema Omgevingswet Voor 2021 staat een nieuwe Nederlandse Omgevingswet op stapel. Deze wet richt zich op onze fysieke leefomgeving. Hiermee worden onder andere bouwwerken, infrastructuur, water, bodem, lucht, landschappen, natuur en cultureel erfgoed bedoeld. Een belangrijk onderwerp, want vrijwel alle activiteiten die burgers, bedrijven en overheden uitvoeren hebben grote invloed op de fysieke leefomgeving. |  |
| Artifact | T3D Archi-repository |  |  |
| BusinessRole | team Archi-gemeenten |  |  |
| Artifact | GEMMA Turfbrug Archi-repository |  |  |
| Artifact | Gennep Archi-repository |  |  |
| Artifact | Alle voor gemeenten relevante Archi-repositories |  |  |

### Notities

- Leden zijn de GEMMA beheerders Team admin heeft admin rechten op alle repositories
- Leden zijn de GEMMA architecten. De GEMMA-repositories geven team Archi-GEMMA schrijfrechten
- Leden zijn de projectarchitecten van VNG projecten. De project-repositories geven het team leesrechten. De eigenaar van de repository deelt verdere rechten uit.
- Leden zijn de gemeenten met een eigen repositories Gemeenten hebben via dit team leesrechten in elkaar repository Schrijfrechten worden per repository toegekend (of met een gemeente-x-team). De gemeente heeft admin rechten op de eigen repository
- Iedereen die niet in één van de sub-team past. Bijvoorbeeld een gemeente zonder eigen repository. Repositories geven team-Archi leesrechten, tenzij er een goede reden is dit niet te doen. Bijvoorbeeld een gemeente kan besluiten zijn repository alleen te delen met gemeenten die ook een repository hebben

## Werken met Archi en git

Hoe werkt Archi met git

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationService | ArchiMate modellering | Applicatieservice voor het beschrijven, analyseren en visualiseren van de architectuur van bedrijfsdomeinen en IT |  |
| ApplicationComponent | Archi | Open source architectuur modelleringstool |  |
| ApplicationFunction | Beschrijven concepten en onderlinge relaties | Gestructureerd vastleggen van de beschrijving van ArchiMate-concepten en de onderlinge relaties |  |
| ApplicationFunction | Maken views | De beschreven concepten in hun onderlinge relaties weergeven in een tekening |  |
| ApplicationComponent | git | Git is a distributed version control system: tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. |  |
| ApplicationFunction | Versiebeheer | Het bijhouden van wijzigingen in een willekeurige verzameling van bestanden |  |
| TechnologyService | Lokale opslag | Opslag direct verbonden aan de computer, bijvoorbeeld een interne schijf of een netwerkschijf |  |
| Artifact | local Archi-repository | De fysieke opslag van het GEMMA architectuurmodel |  |
| Artifact | Workspace .archimate-bestand |  |  |
| TechnologyService | cloud opslag |  |  |
| Artifact | remote Archi-repository | De fysieke opslag van het GEMMA architectuurmodel |  |
| ApplicationComponent | github | GitHub is een online platform voor softwareontwikkeling en versiebeheer (wikipedia) |  |
| ApplicationFunction | Samenwerken | Functionaliteit voor het samenwerken aan de ontwikkeling van software en documentatie. |  |
| ApplicationFunction | Issues aanmaken en volgen | Funcionaliteit voor het beschrijven en bediscussieren van wensen, wijzigingen en correcties |  |
| ApplicationService | Samenwerken en versiebeheer |  |  |
| BusinessActor | Gemeente | Een gemeente is een groep van woonkernen (dorpen, steden) met het bijbehorende gebied die samen worden bestuurd door een politiek apparaat. | Bron: Softwarecatalogus; Toelichting: Eigenschappen van een gemeente * GEMMA type='Gemeente' * Object ID - Unieke sleutel van een gemeente; GUID gegenereerd door Softwarecatalogus * CBS code - Unieke gemeente code toegekend door het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties in samenwerking met het CBS.; Toelichting: Basisgegevens * Object GUID * Naam * Beschrijving * Toelichting * Elementtype=''Gemeente'' Gemeente gegevens * Gemeente CBS -> SWC en persoonsgegevens die niet meegaan in het architectuurmodel * Gemeente contact -> * Gemeente Contact email -> Gemeente e-mail * Voortgang -> Gemeente voortgang * Laatste activiteit -> Gemeente laatste wijziging |
| BusinessRole | Architect | Adviserende rol |  |
| BusinessRole | Adviseur informatievoorziening | Adviserende rol |  |
| BusinessActor | VNG |  |  |
| BusinessProcess | Samenwerken aan GEMMA model |  |  |
| BusinessProcess | Modelleren | Het maken van een vereenvoudigde beschrijving van de werkelijkheid |  |
| BusinessProcess | Issues rapporteren en oplossen |  |  |
| BusinessProcess | Review en feedback |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| ArchiMate modellering | Serving |  | Samenwerken aan GEMMA model |  |
| Archi | Realization |  | ArchiMate modellering |  |
| Archi | Access | save | Workspace .archimate-bestand |  |
| Archi | Flow | Publish model | github |  |
| git | Access | commit | local Archi-repository |  |
| git | Flow | push | git |  |
| github | Flow | Refresh model | Archi |  |
| github | Flow | Import remote model | Archi |  |
| github | Realization |  | Samenwerken en versiebeheer |  |
| git | Access |  | remote Archi-repository |  |
| git | Flow | pull | git |  |
| Samenwerken en versiebeheer | Serving |  | Samenwerken aan GEMMA model |  |
| Architect | Assignment |  | Samenwerken aan GEMMA model |  |
| Adviseur informatievoorziening | Assignment |  | Samenwerken aan GEMMA model |  |

## Kenniscentrum architectuur repositories

Overzicht van de Archi-repositories en doelgroepen

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Grouping | Communicatiekanalen & voorzieningen | Faciliteiten die bijdragen aan de verdere totstandkoming van de GEMMA |  |
| ApplicationInterface | github.com/VNG-Realisatie | Github landingspagina van VNG Realisatie voor de ontwikkeling van standaarden |  |
| Grouping | VNG Archi-repositories | Verzameling van door VNG beheerde ArchiMate repositories. De repository is de fysieke opslag van een architectuurmodel. Opslag met behulp van git maakt versiebeheer en samenwerking in één model mogelijk. |  |
| Artifact | Omnichannel Archi-repository |  |  |
| Artifact | Omgevingswet Archi-repository | Thema Omgevingswet Voor 2021 staat een nieuwe Nederlandse Omgevingswet op stapel. Deze wet richt zich op onze fysieke leefomgeving. Hiermee worden onder andere bouwwerken, infrastructuur, water, bodem, lucht, landschappen, natuur en cultureel erfgoed bedoeld. Een belangrijk onderwerp, want vrijwel alle activiteiten die burgers, bedrijven en overheden uitvoeren hebben grote invloed op de fysieke leefomgeving. |  |
| Artifact | GEMMA Kennismodel Archi-repository | Het GEMMA kennismodel toont de ArchiMate concepten en de onderlinge samenhang van de concepten zoals deze zijn uitgewerkt in het GEMMA architectuurmodel. |  |
| Artifact | T3D Archi-repository |  |  |
| Artifact | GEMMA portfolio Archi-repository | De fysieke opslag van het GEMMA portfoliomodel |  |
| Artifact | GEMMA Archi-repository |  |  |
| BusinessObject | VNG standaarden | De door het KCA beheerde standaardspecificaties en ondersteunende voorzieningen |  |
| Grouping | VNG standaarden repositories |  |  |
| Artifact | Verwerkingenlogging API standaardspecificatie |  |  |
| Artifact | Verwerkingenlogging API Archi-repository | Het thema Logging en verwerkingsactiviteiten beschrijft de architectuurproducten en standaarden die op voor zowel verwerkingsactiviteiten als voor verwerkingen zijn ontwikkeld. Vanuit de de Algemene Verordening Gegevensbescherming (AVG) en de Uitvoeringswet AVG zijn gemeenten verplicht dit gebruik van persoonsgegevens vast te leggen, en inzichtelijk te maken voor burgers. Door deze transparantie over het gebruik van persoonsgegevens heeft de burger de mogelijkheid om na te gaan of de gemeente zijn of haar gegevens rechtmatig gebruikt. |  |
| Artifact | ZGW API-standaardspecificaties |  |  |
| BusinessRole | Adviseur informatievoorziening | Adviserende rol |  |
| BusinessRole | Architect | Adviserende rol |  |
| BusinessRole | Ontwikkelaar |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Adviseur informatievoorziening | Access |  | VNG Archi-repositories |  |
| Architect | Access |  | VNG Archi-repositories |  |
| Ontwikkelaar | Access |  | VNG standaarden |  |

## Begrippen architectuurmodel

Begrippen voor de onderdelen waaruit een architectuur is samengesteld

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| DataObject | ArchiMate-model |  |  |
| DataObject | elementen | Architectuur concepten |  |
| DataObject | views |  |  |
| BusinessObject | Architectuur | De fundamentele concepten of eigenschappen van een systeem in zijn omgeving belichaamd in zijn elementen, relaties en in de principes van zijn ontwerp en evolutie. |  |
| BusinessObject | Concept |  |  |
| BusinessObject | Principe |  |  |
| BusinessObject | Beschrijving |  |  |
| Artifact | Archi-repository |  |  |
| DataObject | Document |  |  |
| DataObject | Plaat |  |  |
| Artifact | wiki-database |  |  |
| Artifact | Bestanden |  |  |
| DataObject | Pagina |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| ArchiMate-model | Realization |  | Architectuur |  |
| elementen | Association | relaties | elementen |  |
| Archi-repository | Realization |  | ArchiMate-model |  |
| Document | Realization |  | Architectuur |  |
| Plaat | Realization |  | Architectuur |  |
| wiki-database | Realization |  | Pagina |  |
| Bestanden | Realization |  | Document |  |
| Bestanden | Realization |  | Plaat |  |
| Pagina | Realization |  | Architectuur |  |

## Begrippen architectuurmodel voorbeeld

De GEMMA architectuur onderdelen en hoe deze zijn samengesteld

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Archi | Open source architectuur modelleringstool |  |
| BusinessObject | GEMMA | De GEMeentelijke ModelArchitectuur met een verzameling samenhangende kaders, richtlijnen, referentiemodellen en standaarden die gemeenten helpt bij het inrichten van hun IT-omgeving en processen. |  |
| BusinessObject | Basisarchitectuur | De kern van de GEMMA met daarin o.a. architectuurprincipes en de GEMMA Bedrijfs-, Informatie- en Technische architectuur. | Basisarchitectuur: ja |
| BusinessObject | Achitectuurprincipes | Een principe is een normatieve eigenschap van alle systemen in een gegeven situatie of van de wijze waarop die systemen worden gerealiseerd. Bron: ArchiMate | Basisarchitectuur: ja; Strategie en motivatie: ja |
| DataObject | Teksten in katern architectuurprincipes |  |  |
| ApplicationComponent | wikiXL |  |  |
| DataObject | Platen in katern architectuurprincipes |  |  |
| ApplicationComponent | PowerPoint |  |  |
| Artifact | remote Archi-repository | De fysieke opslag van het GEMMA architectuurmodel |  |
| DataObject | GEMMA ArchiMate-model |  |  |
| DataObject | principes |  |  |
| TechnologyService | Lokale opslag | Opslag direct verbonden aan de computer, bijvoorbeeld een interne schijf of een netwerkschijf |  |
| ApplicationService | ArchiMate modellering | Applicatieservice voor het beschrijven, analyseren en visualiseren van de architectuur van bedrijfsdomeinen en IT |  |
| ApplicationService | Tekstverwerking |  |  |
| ApplicationService | Tekenen |  |  |
| Artifact | PowerPoint bestand |  |  |
| Artifact | GEMMA redactie database |  |  |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Archi | Realization |  | ArchiMate modellering |  |
| Archi | Access |  | GEMMA ArchiMate-model |  |
| Teksten in katern architectuurprincipes | Realization |  | Achitectuurprincipes |  |
| wikiXL | Access |  | Teksten in katern architectuurprincipes |  |
| wikiXL | Realization |  | Tekstverwerking |  |
| Platen in katern architectuurprincipes | Realization |  | Achitectuurprincipes |  |
| PowerPoint | Access |  | Platen in katern architectuurprincipes |  |
| PowerPoint | Realization |  | Tekenen |  |
| remote Archi-repository | Realization |  | GEMMA ArchiMate-model |  |
| GEMMA ArchiMate-model | Realization |  | Achitectuurprincipes |  |
| Lokale opslag | Access |  | remote Archi-repository |  |
| Lokale opslag | Serving |  | Archi |  |
| Lokale opslag | Serving |  | PowerPoint |  |
| Lokale opslag | Access |  | PowerPoint bestand |  |
| PowerPoint bestand | Realization |  | Platen in katern architectuurprincipes |  |
| Lokale opslag | Access |  | GEMMA redactie database |  |
| Lokale opslag | Serving |  | wikiXL |  |
| GEMMA redactie database | Realization |  | Teksten in katern architectuurprincipes |  |

## Softwarecatalogus modellering pakketten

Deze view toont de modellering van pakketten in het AMEFF exportbestand van de Softwarecatalogus.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| BusinessActor | Leverancier (Visma Roxit) | Aanbieders van standaard-software(pakketten) voor gemeentelijke taken. Alleen leveranciers die het convenant met VNG/KING ondertekend hebben, mogen hun gegevens in de Softwarecatalogus zetten. | Toelichting: De AMEFF export bevat de leveranciers van de door de gemeente gebruikte pakketten; Eigenschappen van een leverancier * GEMMA type='Leverancier' * Object ID - Unieke sleutel van een leveranciers; GUID gegenereerd door Softwarecatalogus * URL - Website van de leverancier |
| ApplicationComponent | Pakket | Een pakket is een door een leverancier in de softwarecatalogus geregistreerde (gemeentelijke) applicatie. Een pakket is zelfstandig inzetbaar, installeerbaar en beheerbaar. | Toelichting: Eigenschappen van een pakket: * SWC type='Pakket' * Object ID - Unieke sleutel van een pakket; GUID gegenereerd door Softwarecatalogus * URL - Pagina op de website van de leverancier met meer gegevens over het pakket * Mutatiedatum pakket- Datum pakket toegevoegd of gewijzigd in productportfolio leverancier (formaat DD-MM-YY) In de export voor een gemeente/samenwerking wordt van een pakket tevens de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie; Bron: Softwarecatalogus |
| ApplicationComponent | Pakketversie (Squit 20/20 VTH) | De opeenvolgende fasen in de ontwikkeling van een pakket. Van iedere pakketversie wordt door de leverancier geregistreerd voor welke referentiecomponenten de versie geschikt is en wat de ondersteunde functionaliteit en standaarden zijn. De gemeente registreert voor welke referentiecomponenten en functionaliteit het pakket gebruikt wordt. | Toelichting: Een pakketversie bevat in de AMEFF export de volgende eigenschappen in zowel de export van een gemeente als van een leverancier. Algemene eigenschappen van een pakketversie * GEMMA type='Pakketversie' * Documentatie - Korte toelichting op deze versie van het pakket * Naam - Naam van het pakket met versieaanduiding * Versie-aanduiding - Versieaanduiding van het pakket * Object ID - Unieke sleutel van een pakketversie; GUID gegenereerd door Softwarecatalogus In de AMEFF export voor een leverancier worden van een pakketversie tevens de volgende eigenschappen meegegeven: * Pakketversie Status - lifecycle pakketversie zoals aangegeven door leverancier ** in ontwikkeling ** in test ** distributie ** einde ondersteuning * Start ontwikkeling * Start test * Start distributie * Ondersteunde technologie - Opsomming ondersteunde technologie, komma gescheiden In de AMEFF export voor een gemeente/samenwerking worden van een pakketversie de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie. * Gebruik status - Lifecycle status van een door een gemeente geregistreerde pakketversie ** Gepland ** In productie ** Uit te faseren ** Uitgefaseerd * Gebruik datum - Datum waarop de gebruik status van een pakket of in gaat of in is gegaan * Gebruik mutatiedatum - Datum laatste wijziging gebruiksgegevens pakket(versie) |
| BusinessCollaboration | Samenwerkingsverband | Een samenwerking (of samenwerkingverband) is een juridische vorm waarin gemeenten vastleggen welke specifiek omschreven taken en bevoegdheden aan de samenwerking worden gedelegeerd. | Bron: Softwarecatalogus |
| BusinessActor | Gemeente | Een gemeente is een groep van woonkernen (dorpen, steden) met het bijbehorende gebied die samen worden bestuurd door een politiek apparaat. | Bron: Softwarecatalogus; Toelichting: Eigenschappen van een gemeente * GEMMA type='Gemeente' * Object ID - Unieke sleutel van een gemeente; GUID gegenereerd door Softwarecatalogus * CBS code - Unieke gemeente code toegekend door het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties in samenwerking met het CBS.; Toelichting: Basisgegevens * Object GUID * Naam * Beschrijving * Toelichting * Elementtype=''Gemeente'' Gemeente gegevens * Gemeente CBS -> SWC en persoonsgegevens die niet meegaan in het architectuurmodel * Gemeente contact -> * Gemeente Contact email -> Gemeente e-mail * Voortgang -> Gemeente voortgang * Laatste activiteit -> Gemeente laatste wijziging |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| Constraint | Standaardversie | Een door de beheerder van de standaard uitgebrachte versie van de standaard | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Leverancier (Visma Roxit) | Association | levert | Pakket | Een pakket wordt geleverd door één leverancier |
| Pakket | Serving | gebruikt door | Samenwerkingsverband | Pakket wordt gebruikt door samenwerking |
| Pakket | Serving | gebruikt door | Gemeente | Pakket wordt gebruikt door gemeente |
| Pakket | Serving | heeft klant | Gemeente |  |
| Pakket | Serving | heeft klant | Samenwerkingsverband | Pakket van leverancier heeft samenwerking als klant |
| Pakket | Specialization | wordt gebruikt voor | Referentiecomponent | De door de gemeente geregistreerde referentiecomponenten, waarvoor het pakket of de pakketversie gebruikt wordt. |
| Pakket | Association | wordt gebruikt voor | Applicatieservice | De door de gemeente/samenwerking geregistreerde applicatie(sub)functies, waarvoor de pakketversie gebruikt wordt. |
| Pakketversie (Squit 20/20 VTH) | Realization | ondersteunt | Standaardversie | Een pakketversie ondersteunt één of meerdere standaardversies. Een pakketversie is compliant, indien de leverancier d.m.v. het uploaden van een testrapport aantoont aan de standaard te voldoen. |
| Pakketversie (Squit 20/20 VTH) | Specialization | is geschikt voor | Referentiecomponent | De door de leverancier geregistreerde referentiecomponenten, waarvoor de pakketversie geschikt is. |
| Pakketversie (Squit 20/20 VTH) | Specialization |  | Referentiecomponent |  |
| Pakketversie (Squit 20/20 VTH) | Association | is geschikt voor | Applicatieservice | De door de leverancier geregistreerde applicatie(sub)functies, waarvoor de pakketversie geschikt is. |
| Pakketversie (Squit 20/20 VTH) | Association |  | Applicatieservice |  |
| Pakketversie (Squit 20/20 VTH) | Flow | binnengemeentelijke koppeling | Pakketversie (Squit 20/20 VTH) | Een door de gemeente geregistreerde koppeling tussen twee pakketversie in het gemeentelijk pakketoverzicht |
| Pakketversie (Squit 20/20 VTH) | Flow | buitengemeentelijke koppeling | Buitengemeentelijk component (MijnOverheid berichtenbox) | Een door de gemeente geregistreerde koppeling tussen een gemeentelijke pakketversie en een buitengemeentelijke component |
| Samenwerkingsverband | Aggregation |  | Gemeente | Een samenwerking groepeert één of meerdere deelnemende gemeenten. |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Flow |  | Pakketversie (Squit 20/20 VTH) |  |
| Referentiecomponent | Association |  | Applicatieservice |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |

### Notities

- Legenda
- rode relaties voor gemeenten en samenwerkingen
- blauwe relaties voor leveranciers

## Softwarecatalogus modellering koppelingen

Modellering van een koppeling in het AMEFF exportbestand van de Softwarecatalogus

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| ApplicationComponent | Pakket | Een pakket is een door een leverancier in de softwarecatalogus geregistreerde (gemeentelijke) applicatie. Een pakket is zelfstandig inzetbaar, installeerbaar en beheerbaar. | Toelichting: Eigenschappen van een pakket: * SWC type='Pakket' * Object ID - Unieke sleutel van een pakket; GUID gegenereerd door Softwarecatalogus * URL - Pagina op de website van de leverancier met meer gegevens over het pakket * Mutatiedatum pakket- Datum pakket toegevoegd of gewijzigd in productportfolio leverancier (formaat DD-MM-YY) In de export voor een gemeente/samenwerking wordt van een pakket tevens de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie; Bron: Softwarecatalogus |
| ApplicationComponent | Pakketversie (Squit 20/20 VTH) | De opeenvolgende fasen in de ontwikkeling van een pakket. Van iedere pakketversie wordt door de leverancier geregistreerd voor welke referentiecomponenten de versie geschikt is en wat de ondersteunde functionaliteit en standaarden zijn. De gemeente registreert voor welke referentiecomponenten en functionaliteit het pakket gebruikt wordt. | Toelichting: Een pakketversie bevat in de AMEFF export de volgende eigenschappen in zowel de export van een gemeente als van een leverancier. Algemene eigenschappen van een pakketversie * GEMMA type='Pakketversie' * Documentatie - Korte toelichting op deze versie van het pakket * Naam - Naam van het pakket met versieaanduiding * Versie-aanduiding - Versieaanduiding van het pakket * Object ID - Unieke sleutel van een pakketversie; GUID gegenereerd door Softwarecatalogus In de AMEFF export voor een leverancier worden van een pakketversie tevens de volgende eigenschappen meegegeven: * Pakketversie Status - lifecycle pakketversie zoals aangegeven door leverancier ** in ontwikkeling ** in test ** distributie ** einde ondersteuning * Start ontwikkeling * Start test * Start distributie * Ondersteunde technologie - Opsomming ondersteunde technologie, komma gescheiden In de AMEFF export voor een gemeente/samenwerking worden van een pakketversie de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie. * Gebruik status - Lifecycle status van een door een gemeente geregistreerde pakketversie ** Gepland ** In productie ** Uit te faseren ** Uitgefaseerd * Gebruik datum - Datum waarop de gebruik status van een pakket of in gaat of in is gegaan * Gebruik mutatiedatum - Datum laatste wijziging gebruiksgegevens pakket(versie) |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationService | Buitengemeentelijke applicatieservice | Een voor gemeenten relevante landelijke- of sectorale applicatieservice | Bron: GEMMA |
| ApplicationComponent | Intermediair-pakket | Een intermediair is een infrastructurele component waarmee een koppeling gerealiseerd wordt In de Softwarecatalogus is gedefinieerd welke referentiecomponenten gebruikt kunnen worden als intermediair | Bron: Softwarecatalogus |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| Constraint | Standaardversie | Een door de beheerder van de standaard uitgebrachte versie van de standaard | Bron: GEMMA |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Pakketversie (Squit 20/20 VTH) | Realization | ondersteunt | Standaardversie | Een pakketversie ondersteunt één of meerdere standaardversies. Een pakketversie is compliant, indien de leverancier d.m.v. het uploaden van een testrapport aantoont aan de standaard te voldoen. |
| Pakketversie (Squit 20/20 VTH) | Flow | buitengemeentelijke koppeling | Buitengemeentelijk component (MijnOverheid berichtenbox) | Een door de gemeente geregistreerde koppeling tussen een gemeentelijke pakketversie en een buitengemeentelijke component |
| id-81009 | Association |  | Intermediair-pakket |  |
| id-81009 | Association |  | Standaardversie |  |
| Pakketversie (Squit 20/20 VTH) | Flow | binnengemeentelijke koppeling | Pakketversie (Squit 20/20 VTH) | Een door de gemeente geregistreerde koppeling tussen twee pakketversie in het gemeentelijk pakketoverzicht |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Flow |  | Pakketversie (Squit 20/20 VTH) |  |
| Buitengemeentelijke applicatieservice | Realization | ondersteunt | Standaard |  |
| id-80963 | Association |  | Intermediair-pakket |  |
| id-80963 | Association |  | Standaardversie |  |

## Softwarecatalogus modellering AMEFF-export

Deze view documenteert de ArchiMate export die de Softwarecatalogus genereert. Alle elementen en relaties die het exportbestand bevat worden in deze view getoond.

### Elementen

| Type | Naam | Documentatie | Eigenschappen |
|---|---|---|---|
| Grouping | Domein | Een groep bedrijfsfuncties en -objecten die in de gemeentelijke praktijk vaak in samenhang worden ingericht en gebruikt | Bron: GEMMA |
| BusinessFunction | Laag | De lagen van het GEMMA bedrijfsfunctiemodel | Bron: GEMMA |
| BusinessFunction | Uitvoeringsdomein | Onderverdeling van de uitvoeringslaag in domeinspecifieke uitvoering | Bron: GEMMA |
| BusinessFunction | Bedrijfsfunctie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. | Bron: GEMMA |
| ApplicationComponent | Buitengemeentelijk component (MijnOverheid berichtenbox) | De sectorale en landelijke voorzieningen waar gemeenten informatie ophalen, delen en of uitwisselen van gegevens met overheidsorganisaties, ketenpartners, burgers en bedrijven. | Toelichting: Eigenschappen van een buitengemeentelijke component * GEMMA type='buitengemeentelijke component' * Naam - Naam van de buitengemeentelijke component * Documentatie - definitie van de buitengemeentelijke component * Object ID - Unieke sleutel van buitengemeentelijke component, GUID overgenomen uit KING architectuurtool |
| ApplicationComponent | Referentiecomponent | Een type applicatiecomponent dat binnen een referentiearchitectuur benoemd is als elementair bouwblok | Bron: GEMMA |
| Grouping | Domein en doelgroep | De groepering van applicatieservices voor een doelgroep binnen een domein | Bron: GEMMA |
| ApplicationService | Buitengemeentelijke applicatieservice | Een voor gemeenten relevante landelijke- of sectorale applicatieservice | Bron: GEMMA |
| ApplicationService | Applicatieservice | In een service gebundelde functionaliteit die gebruikt kan worden middels één of meerdere Applicatie-interfaces. | Bron: GEMMA |
| Grouping | Buitengemeentelijk stelsel | Groep van landelijke- of sectorale informatievoorzieningen | Bron: GEMMA |
| Constraint | Standaard | Een document met erkende afspraken, specificaties of criteria over een product, een dienst of een methode. | Bron: Wikipedia |
| Constraint | Standaardversie | Een door de beheerder van de standaard uitgebrachte versie van de standaard | Bron: GEMMA |
| Grouping | Gradaties | Indeling van standaarden voor de (mate van) bouwbaarheid en testbaarheid. Standaarden kunnen als producten worden getypeerd in eindproducten, halffabrikaten, grondstoffen en gegevensstandaarden. Deze typering is een indicatie wat de benodigde inspanning is om de specificatie te completeren om tot een werkende koppeling te komen. | Bron: GEMMA |
| BusinessRole | Doelgroep | De doelgroep is een ordening van de gemeentelijke applicatieservices naar de groep gebruikers. Een doelgroep is bijvoorbeeld de inwoners en ondernemers | Bron: GEMMA |
| BusinessActor | Leverancier (Visma Roxit) | Aanbieders van standaard-software(pakketten) voor gemeentelijke taken. Alleen leveranciers die het convenant met VNG/KING ondertekend hebben, mogen hun gegevens in de Softwarecatalogus zetten. | Toelichting: De AMEFF export bevat de leveranciers van de door de gemeente gebruikte pakketten; Eigenschappen van een leverancier * GEMMA type='Leverancier' * Object ID - Unieke sleutel van een leveranciers; GUID gegenereerd door Softwarecatalogus * URL - Website van de leverancier |
| ApplicationComponent | Pakket | Een pakket is een door een leverancier in de softwarecatalogus geregistreerde (gemeentelijke) applicatie. Een pakket is zelfstandig inzetbaar, installeerbaar en beheerbaar. | Toelichting: Eigenschappen van een pakket: * SWC type='Pakket' * Object ID - Unieke sleutel van een pakket; GUID gegenereerd door Softwarecatalogus * URL - Pagina op de website van de leverancier met meer gegevens over het pakket * Mutatiedatum pakket- Datum pakket toegevoegd of gewijzigd in productportfolio leverancier (formaat DD-MM-YY) In de export voor een gemeente/samenwerking wordt van een pakket tevens de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie; Bron: Softwarecatalogus |
| ApplicationComponent | Pakketversie (Squit 20/20 VTH) | De opeenvolgende fasen in de ontwikkeling van een pakket. Van iedere pakketversie wordt door de leverancier geregistreerd voor welke referentiecomponenten de versie geschikt is en wat de ondersteunde functionaliteit en standaarden zijn. De gemeente registreert voor welke referentiecomponenten en functionaliteit het pakket gebruikt wordt. | Toelichting: Een pakketversie bevat in de AMEFF export de volgende eigenschappen in zowel de export van een gemeente als van een leverancier. Algemene eigenschappen van een pakketversie * GEMMA type='Pakketversie' * Documentatie - Korte toelichting op deze versie van het pakket * Naam - Naam van het pakket met versieaanduiding * Versie-aanduiding - Versieaanduiding van het pakket * Object ID - Unieke sleutel van een pakketversie; GUID gegenereerd door Softwarecatalogus In de AMEFF export voor een leverancier worden van een pakketversie tevens de volgende eigenschappen meegegeven: * Pakketversie Status - lifecycle pakketversie zoals aangegeven door leverancier ** in ontwikkeling ** in test ** distributie ** einde ondersteuning * Start ontwikkeling * Start test * Start distributie * Ondersteunde technologie - Opsomming ondersteunde technologie, komma gescheiden In de AMEFF export voor een gemeente/samenwerking worden van een pakketversie de volgende eigenschappen meegegeven: * Extern pakket - 'ja/nee'; een externe pakketversie, is een door de gemeente in de softwarecatalogus geregistreerde (versie van een) applicatie. * Gebruik status - Lifecycle status van een door een gemeente geregistreerde pakketversie ** Gepland ** In productie ** Uit te faseren ** Uitgefaseerd * Gebruik datum - Datum waarop de gebruik status van een pakket of in gaat of in is gegaan * Gebruik mutatiedatum - Datum laatste wijziging gebruiksgegevens pakket(versie) |
| BusinessCollaboration | Samenwerkingsverband | Een samenwerking (of samenwerkingverband) is een juridische vorm waarin gemeenten vastleggen welke specifiek omschreven taken en bevoegdheden aan de samenwerking worden gedelegeerd. | Bron: Softwarecatalogus |
| BusinessActor | Gemeente | Een gemeente is een groep van woonkernen (dorpen, steden) met het bijbehorende gebied die samen worden bestuurd door een politiek apparaat. | Bron: Softwarecatalogus; Toelichting: Eigenschappen van een gemeente * GEMMA type='Gemeente' * Object ID - Unieke sleutel van een gemeente; GUID gegenereerd door Softwarecatalogus * CBS code - Unieke gemeente code toegekend door het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties in samenwerking met het CBS.; Toelichting: Basisgegevens * Object GUID * Naam * Beschrijving * Toelichting * Elementtype=''Gemeente'' Gemeente gegevens * Gemeente CBS -> SWC en persoonsgegevens die niet meegaan in het architectuurmodel * Gemeente contact -> * Gemeente Contact email -> Gemeente e-mail * Voortgang -> Gemeente voortgang * Laatste activiteit -> Gemeente laatste wijziging |

### Relaties

| Van | Relatie | Naam | Naar | Documentatie |
|---|---|---|---|---|
| Domein | Aggregation |  | Bedrijfsfunctie |  |
| Domein | Aggregation |  | Uitvoeringsdomein |  |
| Domein | Aggregation |  | Laag |  |
| Domein | Aggregation |  | Domein en doelgroep |  |
| Laag | Aggregation |  | Bedrijfsfunctie |  |
| Laag | Aggregation |  | Uitvoeringsdomein |  |
| Uitvoeringsdomein | Aggregation |  | Bedrijfsfunctie |  |
| Bedrijfsfunctie | Aggregation |  | Bedrijfsfunctie |  |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Realization |  | Buitengemeentelijke applicatieservice |  |
| Buitengemeentelijk component (MijnOverheid berichtenbox) | Flow |  | Pakketversie (Squit 20/20 VTH) |  |
| Referentiecomponent | Realization | Verplicht / Aanbevolen | Standaard | Met de 'Verplicht / Aanbevolen' relatie wordt voor een referentiecomponent voorgeschreven welke standaard verplicht of aanbevolen is. Eigenschappen van de relatie 'aanbevolen of verplichte standaard' * Verbindingsrol = 'Aanbevolen' of 'Verplicht' |
| Referentiecomponent | Association |  | Applicatieservice |  |
| Domein en doelgroep | Serving |  | Doelgroep |  |
| Domein en doelgroep | Aggregation |  | Applicatieservice |  |
| Buitengemeentelijke applicatieservice | Realization | ondersteunt | Standaard |  |
| Buitengemeentelijke applicatieservice | Serving |  | Referentiecomponent |  |
| Applicatieservice | Association |  | Bedrijfsfunctie |  |
| Applicatieservice | Association |  | Applicatieservice |  |
| Buitengemeentelijk stelsel | Aggregation |  | Buitengemeentelijk component (MijnOverheid berichtenbox) |  |
| Standaardversie | Specialization | is versie van | Standaard |  |
| Gradaties | Aggregation |  | Standaard |  |
| Leverancier (Visma Roxit) | Association | levert | Pakket | Een pakket wordt geleverd door één leverancier |
| Pakket | Serving | gebruikt door | Samenwerkingsverband | Pakket wordt gebruikt door samenwerking |
| Pakket | Serving | gebruikt door | Gemeente | Pakket wordt gebruikt door gemeente |
| Pakket | Serving | heeft klant | Gemeente |  |
| Pakket | Serving | heeft klant | Samenwerkingsverband | Pakket van leverancier heeft samenwerking als klant |
| Pakket | Specialization | wordt gebruikt voor | Referentiecomponent | De door de gemeente geregistreerde referentiecomponenten, waarvoor het pakket of de pakketversie gebruikt wordt. |
| Pakket | Association | wordt gebruikt voor | Applicatieservice | De door de gemeente/samenwerking geregistreerde applicatie(sub)functies, waarvoor de pakketversie gebruikt wordt. |
| Pakketversie (Squit 20/20 VTH) | Realization | ondersteunt | Standaardversie | Een pakketversie ondersteunt één of meerdere standaardversies. Een pakketversie is compliant, indien de leverancier d.m.v. het uploaden van een testrapport aantoont aan de standaard te voldoen. |
| Pakketversie (Squit 20/20 VTH) | Specialization | is geschikt voor | Referentiecomponent | De door de leverancier geregistreerde referentiecomponenten, waarvoor de pakketversie geschikt is. |
| Pakketversie (Squit 20/20 VTH) | Specialization |  | Referentiecomponent |  |
| Pakketversie (Squit 20/20 VTH) | Association | is geschikt voor | Applicatieservice | De door de leverancier geregistreerde applicatie(sub)functies, waarvoor de pakketversie geschikt is. |
| Pakketversie (Squit 20/20 VTH) | Association |  | Applicatieservice |  |
| Pakketversie (Squit 20/20 VTH) | Flow | binnengemeentelijke koppeling | Pakketversie (Squit 20/20 VTH) | Een door de gemeente geregistreerde koppeling tussen twee pakketversie in het gemeentelijk pakketoverzicht |
| Pakketversie (Squit 20/20 VTH) | Flow | buitengemeentelijke koppeling | Buitengemeentelijk component (MijnOverheid berichtenbox) | Een door de gemeente geregistreerde koppeling tussen een gemeentelijke pakketversie en een buitengemeentelijke component |
| Samenwerkingsverband | Aggregation |  | Gemeente | Een samenwerking groepeert één of meerdere deelnemende gemeenten. |

### Notities

- Legenda
- rode relaties voor gemeenten en samenwerkingen
- blauwe relaties voor leveranciers
