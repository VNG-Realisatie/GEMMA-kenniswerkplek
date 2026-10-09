---
id: kennismodel
type: kennismodel
titel: Kennismodel
---

# Kennismodel

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

Wat het model is: de elementtypen per architectuurlaag, de relaties ertussen en de indelingen. Het kennismodel is metadata; het telt niets. Waarom het model zo is, staat in [ARCHITECTURE.md](../ARCHITECTURE.md); de regels voor het modelleren, met de voorrang, in [modelleerregels](modelleerregels.md); de vragen die een begrip een type geven in [kenmerken en beslistabel](kenmerken-en-beslistabel.md).

Twee markeringen zijn verschillend:

- **Weggefilterd**: niet in het kennismodel van de wiki. Een beoordeling legt elke gevonden relatie vast; de export laat een weggefilterde relatie weg, met de reden.
- **Niet in Over GEMMA**: wel in het kennismodel van de wiki, maar niet in het GEMMA-kennismodel (Over GEMMA): een uitbreiding op het GEMMA-kennismodel. Het gaat mee in de export, gemarkeerd, en is een kandidaat voor een terugmelding over het kennismodel.

## Bedrijfsarchitectuur

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Bedrijfsobject](bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | Business Object | `bedrijfsobject` | ja |
| [Afspraak](bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | Contract | `bedrijfsobject` | ja |
| [Product](bedrijfsarchitectuur/product-modelleerafspraken.md) | Product | `product` | ja |
| [Dienst](bedrijfsarchitectuur/dienst-modelleerafspraken.md) | Business Service | `dienst` | ja |
| [Bedrijfsproces](bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | Business Process | `bedrijfsproces` | ja |
| [Bedrijfsfunctie](bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md) | Business Function | `bedrijfsfunctie` | ja |
| [Gebeurtenis](bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | Business Event | `gebeurtenis` | ja |
| [Actor](bedrijfsarchitectuur/actor-modelleerafspraken.md) | Business Actor | `actor` | ja |
| [Rol](bedrijfsarchitectuur/rol-modelleerafspraken.md) | Business Role | `rol` | ja |
| [Bedrijfssamenwerking](bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md) | Business Collaboration | `bedrijfssamenwerking` | ja |
| [Kanaal](bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | Business Interface | `kanaal` | ja |
| [Bedrijfsinteractie](bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) | Business Interaction | `bedrijfsinteractie` | nee |

Elementtypen zonder element: [weggefilterd](bedrijfsarchitectuur/weggefilterd.md) (representatie).

## Motivatie

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Beleidskader](motivatie/beleidskader-modelleerafspraken.md) | Driver | `beleidskader` | ja |
| [Kwaliteitsdoel](motivatie/kwaliteitsdoel-modelleerafspraken.md) | Goal | matchdoel (GEMMA) | ja |

Elementtypen zonder element: [weggefilterd](motivatie/weggefilterd.md) (uitkomst, principe, eis, beperking, waarde, kernwaarde, vermogen).

## Applicatiearchitectuur

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Data-object](applicatiearchitectuur/data-object-modelleerafspraken.md) | Data Object | annotatie | ja |

Elementtypen zonder element: [weggefilterd](applicatiearchitectuur/weggefilterd.md) (applicatiecomponent, applicatieservice, applicatiefunctie, applicatie-interface, applicatieproces, applicatie-event).

## Overig

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Groepering](overig/groepering-modelleerafspraken.md) | Grouping | indeling | ja |

Elementtypen zonder element: [weggefilterd](overig/weggefilterd.md) (locatie).

## Relatietypen

| Relatie | ArchiMate | Betekenis |
|---|---|---|
| associatie | association | een betekenisvolle verbinding; gericht als de naam een leesrichting heeft |
| aggregatie | aggregation | het geheel omvat het deel; het deel bestaat ook los |
| compositie | composition | het deel bestaat alleen in het geheel |
| specialisatie | specialization | is een: het doel is het bredere begrip van hetzelfde type |
| toewijzing | assignment | wie het gedrag uitvoert, of welke actor een rol vervult |
| toegang | access | gedrag of een rol gebruikt een object, met een vaste handeling of verantwoordelijkheid |
| triggering | triggering | het een start het ander, in de tijd |
| stroom | flow | gedrag geeft iets door aan ander gedrag |
| realisatie | realization | gedrag realiseert een dienst; een data-object realiseert een bedrijfsobject |
| bediening | serving | het een ondersteunt of bedient het ander |
| invloed | influence | een motivatie-element beïnvloedt een ander, met een sterkte |

De vaste namen: een **handeling** van gedrag op een object (registreren: schrijven, bijwerken: lezen-schrijven, beëindigen: schrijven, raadplegen: lezen, verstrekken: lezen, bewaren: lezen-schrijven, overbrengen: lezen, vernietigen: schrijven), een **verantwoordelijkheid** van een rol voor een object (houder: lezen-schrijven, bronhouder: schrijven, beheerder: lezen-schrijven, verstrekker: lezen, afnemer: lezen, toezichthouder: lezen, betrokkene: lezen, partij: lezen-schrijven), en de **grondslag** van een beleidskader (*is grondslag voor*: Europese regelgeving, Rijksregelgeving; Gemeentelijke regelgeving alleen naar een UPL-product of -dienst zonder landelijke grondslag; *werkt uit voor*: Gemeentelijke regelgeving: werkt de wet uit; *geeft richtlijn voor*: Richtlijn: geen wettelijke grondslag).

## Relatiematrix

Per brontype (rij) en doeltype (kolom) de toegestane relaties; \* is een uitbreiding op het GEMMA-kennismodel. Een leeg vak: weggefilterd.

| Van \ naar | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol | Bedrijfssamenwerking | Kanaal | Bedrijfsinteractie | Beleidskader |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bedrijfsobject | associatie, aggregatie, compositie, specialisatie |  |  |  |  |  |  |  |  |  |  |  |  |
| Afspraak | associatie* |  |  |  |  |  |  |  |  |  |  |  |  |
| Product |  | aggregatie |  | aggregatie |  |  |  |  | bediening |  |  |  |  |
| Dienst |  |  |  | aggregatie, specialisatie* | bediening |  |  |  | bediening |  |  |  |  |
| Bedrijfsproces | toegang | toegang* |  | realisatie | aggregatie, specialisatie, triggering, stroom* | bediening | aggregatie*, triggering |  |  |  |  | bediening* |  |
| Bedrijfsfunctie | toegang |  |  | realisatie, aggregatie* | bediening | aggregatie |  |  |  |  |  |  |  |
| Gebeurtenis |  |  |  |  | triggering |  | triggering*, specialisatie* |  |  |  |  | triggering* |  |
| Actor |  |  |  |  |  |  |  | aggregatie*, associatie* | toewijzing |  |  |  |  |
| Rol | toegang | toegang* |  |  | toewijzing | toewijzing |  |  | aggregatie, specialisatie |  |  | toewijzing* |  |
| Bedrijfssamenwerking | toegang* |  |  |  | toewijzing | toewijzing* |  | aggregatie | aggregatie |  |  | toewijzing* |  |
| Kanaal |  |  |  | toewijzing |  |  |  |  | bediening |  |  |  |  |
| Bedrijfsinteractie | toegang* |  |  |  |  |  |  |  |  |  |  |  |  |
| Beleidskader | associatie* |  | associatie | associatie* | associatie* |  | associatie* |  | associatie* |  |  |  | associatie* |

## Indelingen

| Indeling | Deelt in | Naar | Groepering |
|---|---|---|---|
| [Beleidsdomeinindeling](indelingen.md) | objecten, aanbod, beleidskaders, en de bovenste knoop van de processen | het taakveld (Iv3) en het beleidsdomein | GEMMA |
| [Functie-indeling naar domein](indelingen.md) | functies, producten en diensten | het GEMMA-domein | GEMMA |
| [Procesindeling naar kernobject](indelingen.md) | processen, gebeurtenissen en ketensamenwerkingen | het kernobject | wiki |
| [Procesindeling naar soort werk](indelingen.md) | bedrijfsprocessen; via generieke GEMMA-elementen ook gebeurtenissen, diensten en rollen | de soort werk (het processenlandschap van GEMMA) | GEMMA, uitgebreid |
| [Doelgroepindeling](indelingen.md) | partijen en kanalen | de doelgroep | wiki |
| [Grondslagindeling](indelingen.md) | beleidskaders | het brontype van de regeling, afgeleid uit de regelgever | wiki |
