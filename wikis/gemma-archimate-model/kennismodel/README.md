---
id: kennismodel
type: kennismodel
titel: Kennismodel
gegenereerd: tools/kennismodel.py
---

# Kennismodel

Wat het model is: de elementtypen per architectuurlaag, de relaties ertussen en de indelingen. Het kennismodel is metadata; het telt niets. Waarom het model zo is, staat in [ARCHITECTURE.md](../ARCHITECTURE.md); de regels voor het modelleren, met de voorrang, in [modelleerregels](modelleerregels.md); de vragen die een begrip een type geven in [kenmerken en beslistabel](kenmerken-en-beslistabel.md).

Twee markeringen zijn verschillend:

- **Buiten het kennismodel**: niet in het kennismodel van de wiki: elementtypen zonder element, en relaties die de export weglaat. Een beoordeling legt elke gevonden relatie vast; een signaal geeft de reden. Het overzicht, voor de redacteur: [Buiten het kennismodel](../elementpaginas/overig/buiten-het-kennismodel.md).
- **Niet in Over GEMMA**: wel in het kennismodel van de wiki, maar niet in het GEMMA-kennismodel (Over GEMMA): een uitbreiding op het GEMMA-kennismodel. Het gaat mee in de export, gemarkeerd, en is een kandidaat voor een terugmelding over het kennismodel.

Een typepagina toont de relaties waarvan het type de bron is; de inkomende staan bij het brontype.

## De ArchiMate-matrix

Fase A kiest eerst het vak: de laag, het aspect en intern of extern, zoals in ArchiMate. Het vak bepaalt welke hoofdkenmerken en soorten gedrag er zijn, en welke vragen volgen. Motivatie kent geen aspecten.

| Laag | Actief intern | Actief extern | Gedrag intern | Gedrag extern | Passief | Samengesteld |
|---|---|---|---|---|---|---|
| bedrijf | Actor, Rol, Bedrijfssamenwerking | Kanaal | Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie | Dienst | Bedrijfsobject, Afspraak, Representatie (geen pagina) | Product |
| applicatie | zonder element | zonder element | zonder element | zonder element | Data-object (afgeleid uit de GGM-match) | — |
| technologie | zonder element: komt misschien nog | | | | | |
| strategie | Capability (Vermogen): buiten dit model | | | | | |
| motivatie | Beleidskader (element); Kwaliteitsdoel (matchdoel); de andere typen buiten dit model | | | | | |
| overig | | | | | | Locatie (geen pagina), Groepering (indeling) |

Wat fase A per vak vraagt, staat in [kenmerken en beslistabel](kenmerken-en-beslistabel.md).

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

Elementtypen zonder element: representatie.

## Motivatie

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Beleidskader](motivatie/beleidskader-modelleerafspraken.md) | Driver | `beleidskader` | ja |
| [Kwaliteitsdoel](motivatie/kwaliteitsdoel-modelleerafspraken.md) | Goal | matchdoel (GEMMA) | ja |

Elementtypen zonder element: uitkomst, principe, eis, beperking, waarde, kernwaarde, vermogen.

## Applicatiearchitectuur

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Data-object](applicatiearchitectuur/data-object-modelleerafspraken.md) | Data Object | `data-object` | ja |

Elementtypen zonder element: applicatiecomponent, applicatieservice, applicatiefunctie, applicatie-interface, applicatieproces, applicatie-event.

## Technologiearchitectuur

Elementtypen zonder element: node, systeemsoftware, technologieservice.

## Overig

| Elementtype | ArchiMate | Paginatype | In Over GEMMA |
|---|---|---|---|
| [Groepering](overig/groepering-modelleerafspraken.md) | Grouping | indeling | ja |

Elementtypen zonder element: locatie.

## Eigenschappen

| Eigenschap | Betekenis | Waarden |
|---|---|---|
| `kernobject` | het bedrijfsobject waarvan het proces de levensloop omvat (levensloopproces), waarin het een mutatie doet (bedrijfsproces), of dat door de keten gaat (bedrijfsinteractie) |  |
| `afnemer` | voor wie het is: extern of intern (de bovenste laag van het processenlandschap, de rol Klant en de externe en interne UPL-lijst) | extern, intern |
| `domein` | het GEMMA-domein, de plaats in de Functie-indeling naar domein | Bestuur, Fysieke leefomgeving, Niet domeingebonden, Openbare orde en veiligheid, Ondersteuning, Publieksdiensten, Sociaal domein |
| `doelgroep` | gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling | gemeente, inwoners en ondernemers, ketenpartners |
| `regelgever` | EU, rijk of VNG-modelverordening: bepaalt de groep in de Grondslagindeling | EU, rijk, VNG-modelverordening |
| `kwaliteitsdoelen` | de GEMMA-kwaliteitsdoelen waaraan het beleidskader grondslag geeft, met de sterkte van die invloed, een onderbouwing en de bronnen |  |
| `taakveld` | het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling |  |
| `beleidsdomein` | het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling |  |
| `gemma_generiek` | het generieke GEMMA-element waarvan dit een specialisatie is (exacte match) |  |
| `gemma_functie` | de bovenliggende GEMMA-functie in de functiehiërarchie, die zelf geen element is: het id, met de GEMMA-relatie of een bron met vindplaats |  |
| `deelprocessen` | de deelprocessen in volgorde, elk met één of twee zinnen en een bron (geen eigen pagina) |  |
| `gemma` | de match met het GEMMA-model: het id gaat mee in de export |  |
| `ggm` | de match met het GGM: entiteit, sterkte en onderbouwing |  |
| `data_objecten` | een extra data-object voor een andere GGM-entiteit: naam en GGM-match |  |

## Relatietypen

| Relatie | ArchiMate | Betekenis |
|---|---|---|
| associatie | association | een betekenisvolle verbinding; gericht als de naam een leesrichting heeft |
| aggregatie | aggregation | het geheel omvat het deel; het deel bestaat ook los |
| compositie | composition | het deel bestaat alleen in het geheel |
| specialisatie | specialization | is een: het doel is het bredere begrip van hetzelfde type |
| toewijzing | assignment | wie het gedrag uitvoert, of welke actor een rol vervult |
| toegang | access | gedrag of een rol gebruikt een object, met een vaste handeling of verantwoordelijkheid; per paar elementen één relatie, met de vereniging van de toegangstypen |
| triggering | triggering | het een start het ander, in de tijd |
| stroom | flow | gedrag geeft iets door aan ander gedrag |
| realisatie | realization | gedrag realiseert een dienst; een data-object realiseert een bedrijfsobject of afspraak |
| bediening | serving | het een ondersteunt of bedient het ander |
| invloed | influence | een motivatie-element beïnvloedt een ander, met een sterkte |

De vaste namen: een **handeling** van gedrag op een object (registreren: schrijven, bijwerken: lezen-schrijven, beëindigen: schrijven, raadplegen: lezen, verstrekken: lezen, bewaren: lezen-schrijven, overbrengen: lezen, vernietigen: schrijven), een **verantwoordelijkheid** van een rol voor een object (houder: lezen-schrijven, bronhouder: schrijven, beheerder: lezen-schrijven, verstrekker: lezen, afnemer: lezen, toezichthouder: lezen, betrokkene: lezen, partij: lezen-schrijven), en de **grondslag** van een beleidskader (*is grondslag voor*: Europese regelgeving, Rijksregelgeving; *werkt uit voor*: Gemeentelijke regelgeving: werkt de wet uit, nooit grondslag).

## Relatiematrix

Per brontype (rij) en doeltype (kolom) de toegestane relaties; \* is een uitbreiding op het GEMMA-kennismodel. Een leeg vak: buiten het kennismodel.

| Van \ naar | Bedrijfsobject | Afspraak | Product | Dienst | Bedrijfsproces | Bedrijfsfunctie | Gebeurtenis | Actor | Rol | Bedrijfssamenwerking | Kanaal | Bedrijfsinteractie | Beleidskader | Data-object |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bedrijfsobject | associatie, aggregatie, compositie, specialisatie |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Afspraak | associatie* |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Product |  | aggregatie |  | aggregatie |  |  |  |  | bediening |  |  |  |  |  |
| Dienst |  |  |  | aggregatie, specialisatie* | bediening |  |  |  | bediening |  |  |  |  |  |
| Bedrijfsproces | toegang | toegang* |  | realisatie | aggregatie, specialisatie, triggering, stroom* | bediening | aggregatie*, triggering |  |  |  |  | bediening* |  |  |
| Bedrijfsfunctie | toegang |  |  | realisatie, aggregatie* | bediening | aggregatie |  |  |  |  |  |  |  |  |
| Gebeurtenis |  |  |  |  | triggering |  | triggering*, specialisatie* |  |  |  |  | triggering* |  |  |
| Actor |  |  |  |  |  |  |  | aggregatie*, associatie* | toewijzing |  |  |  |  |  |
| Rol | toegang | toegang* |  |  | toewijzing | toewijzing |  |  | aggregatie, specialisatie |  |  | toewijzing* |  |  |
| Bedrijfssamenwerking | toegang* |  |  |  | toewijzing | toewijzing* |  | aggregatie | aggregatie |  |  | toewijzing* |  |  |
| Kanaal |  |  |  | toewijzing |  |  |  |  | bediening |  |  |  |  |  |
| Bedrijfsinteractie | toegang* |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Beleidskader | associatie* |  | associatie | associatie* | associatie* |  | associatie* |  | associatie* |  |  |  | associatie* |  |
| Data-object | realisatie | realisatie* |  |  |  |  | associatie* | associatie* | associatie* |  |  |  |  |  |

## Indelingen

| Indeling | Deelt in | Naar | Groepering |
|---|---|---|---|
| [Beleidsdomeinindeling](indelingen.md) | objecten, aanbod, beleidskaders, en de bovenste knoop van de processen | het taakveld (Iv3) en het beleidsdomein | GEMMA |
| [Functie-indeling naar domein](indelingen.md) | functies, producten en diensten | het GEMMA-domein | GEMMA |
| [Procesindeling naar kernobject](indelingen.md) | processen, gebeurtenissen en ketensamenwerkingen | het kernobject | wiki |
| [Procesindeling naar soort werk](indelingen.md) | bedrijfsprocessen; via generieke GEMMA-elementen ook gebeurtenissen, diensten en rollen | de soort werk (het processenlandschap van GEMMA) | GEMMA, uitgebreid |
| [Doelgroepindeling](indelingen.md) | partijen en kanalen | de doelgroep | wiki |
| [Grondslagindeling](indelingen.md) | beleidskaders | het brontype van de regeling, afgeleid uit de regelgever | wiki |
