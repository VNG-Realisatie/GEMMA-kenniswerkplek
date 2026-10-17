---
id: buiten-het-kennismodel
type: lijst
titel: Buiten het kennismodel
---

# Buiten het kennismodel

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

Wat in ArchiMate bestaat of geldig is, maar niet in het [kennismodel](../../kennismodel/README.md) van de wiki staat. Naslag voor de redacteur; de AI leest deze pagina niet: de beslistabel geeft een begrip van een type zonder element zijn uitkomst, en een signaal geeft de reden bij een vastgelegde relatie buiten het kennismodel.

## Elementtypen zonder element

Een begrip van zo'n type krijgt de uitkomst uit de beslistabel: geen pagina, of buiten dit model.

| Laag | Elementtype | In Over GEMMA | Reden |
|---|---|---|---|
| Bedrijfsarchitectuur | Representatie (Representation) | — | De waarneembare vorm (document, formulier, register, bericht) van de informatie van een object: vermelden bij dat object, geen pagina. |
| Overig | Locatie (Location) | — | Een fysieke plaats als zodanig: geen pagina. Een gebiedsindeling als gegeven is een bedrijfsobject. |
| Motivatie | Uitkomst (Outcome) | — | Buiten dit model. |
| Motivatie | Principe (Principle) | Architectuurprincipe | Buiten dit model. |
| Motivatie | Eis (Requirement) | Requirement, Implicatie | Buiten dit model: een losse norm uit één artikel ('binnen acht weken beslissen') is een eis of beperking; de regeling als geheel is een beleidskader of blijft bron. |
| Motivatie | Beperking (Constraint) | Standaard | Buiten dit model, als een eis. |
| Motivatie | Waarde (Value) | — | Buiten dit model. |
| Motivatie | Kernwaarde (Driver) | Kernwaarde | Buiten dit model: een fundamentele overtuiging waaraan overheidsdienstverlening moet voldoen. Ook een Driver; alleen het beleidskader is een element. |
| Strategie | Resource (Resource) | Resources | Buiten dit model: de houder van een capability is altijd de gemeente. |
| Strategie | Waardestroom (Value Stream) | — | Buiten dit model: de waarde voor de afnemer volgt uit dienst en product. |
| Strategie | Handelwijze (Course of Action) | Strategie | Buiten dit model: een opgave met een einde, geen vermogen. |
| Applicatiearchitectuur | Applicatiecomponent (Application Component) | Applicatiecomponent | De applicatielaag is nog niet gebouwd. |
| Applicatiearchitectuur | Applicatieservice (Application Service) | Applicatieservice | De applicatielaag is nog niet gebouwd. |
| Applicatiearchitectuur | Applicatiefunctie (Application Function) | Applicatiefunctie | De applicatielaag is nog niet gebouwd. |
| Applicatiearchitectuur | Applicatie-interface (Application Interface) | Applicatie-interface | De applicatielaag is nog niet gebouwd. |
| Applicatiearchitectuur | Applicatieproces (Application Process) | Applicatieproces | De applicatielaag is nog niet gebouwd. |
| Applicatiearchitectuur | Applicatie-event (Application Event) | Applicatie-event | De applicatielaag is nog niet gebouwd. |
| Technologiearchitectuur | Node (Node) | Node | De technologielaag is nog niet gebouwd: zij zit in GEMMA en komt misschien nog. |
| Technologiearchitectuur | Systeemsoftware (System Software) | Systeemsoftware | De technologielaag is nog niet gebouwd: zij zit in GEMMA en komt misschien nog. |
| Technologiearchitectuur | Technologieservice (Technology Service) | Technologieservice | De technologielaag is nog niet gebouwd: zij zit in GEMMA en komt misschien nog. |

## Relaties buiten de export

Geldig in ArchiMate, en een beoordeling legt ze vast als de bron ze noemt; de export laat ze weg. Een relatie die nergens in het kennismodel staat, valt er ook buiten.

| Van | Relatie | Naar | Reden |
|---|---|---|---|
| [Actor](../../kennismodel/bedrijfsarchitectuur/actor-modelleerafspraken.md) | toewijzing of toegang of associatie | [Bedrijfsproces](../../kennismodel/bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md), [Bedrijfsfunctie](../../kennismodel/bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md), [Gebeurtenis](../../kennismodel/bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md), [Dienst](../../kennismodel/bedrijfsarchitectuur/dienst-modelleerafspraken.md), [Bedrijfsinteractie](../../kennismodel/bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md), [Bedrijfsobject](../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md), [Afspraak](../../kennismodel/bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| [Actor](../../kennismodel/bedrijfsarchitectuur/actor-modelleerafspraken.md) | toewijzing | [Actor](../../kennismodel/bedrijfsarchitectuur/actor-modelleerafspraken.md), [Bedrijfssamenwerking](../../kennismodel/bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md), [Kanaal](../../kennismodel/bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | tussen partijen is alleen *actor vervult rol* een toewijzing |
| [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md), [Bedrijfssamenwerking](../../kennismodel/bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md) | toewijzing | [Actor](../../kennismodel/bedrijfsarchitectuur/actor-modelleerafspraken.md), [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md), [Bedrijfssamenwerking](../../kennismodel/bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md), [Kanaal](../../kennismodel/bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | tussen partijen is alleen *actor vervult rol* een toewijzing |
| [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md), [Bedrijfssamenwerking](../../kennismodel/bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md) | toewijzing | [Dienst](../../kennismodel/bedrijfsarchitectuur/dienst-modelleerafspraken.md) | een dienst krijgt geen rol toegewezen: de rol hangt aan het proces of de functie die de dienst realiseert |
| [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md) | associatie | [Bedrijfsobject](../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md), [Afspraak](../../kennismodel/bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | wat een rol met een object is, is toegang met een verantwoordelijkheid; een handeling is een toewijzing van de rol aan het proces |
| [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md) | associatie | [Rol](../../kennismodel/bedrijfsarchitectuur/rol-modelleerafspraken.md) | een handeling tussen rollen loopt via een proces (toewijzing), een stroom of een gebeurtenis, zoals tussen actoren |
| [Kanaal](../../kennismodel/bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | elke andere relatie | elk type | een kanaal is toegewezen aan een dienst en bedient een rol |
| [Bedrijfsfunctie](../../kennismodel/bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md) | aggregatie of compositie | [Bedrijfsproces](../../kennismodel/bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | een functie bedient een proces; processen groeperen in een cluster naar soort werk |
| [Dienst](../../kennismodel/bedrijfsarchitectuur/dienst-modelleerafspraken.md) | toegang | [Bedrijfsobject](../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md), [Afspraak](../../kennismodel/bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | een dienst heeft geen toegang tot een object; het proces dat haar realiseert wel |
| [Gebeurtenis](../../kennismodel/bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | associatie | [Bedrijfsobject](../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md), [Afspraak](../../kennismodel/bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | het object volgt uit het levensloopproces waaronder de gebeurtenis hangt |
| [Bedrijfsproces](../../kennismodel/bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md), [Gebeurtenis](../../kennismodel/bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md), [Dienst](../../kennismodel/bedrijfsarchitectuur/dienst-modelleerafspraken.md), [Bedrijfsinteractie](../../kennismodel/bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) | realisatie | [Capability](../../kennismodel/strategie/capability-modelleerafspraken.md) | alleen een bedrijfsfunctie realiseert een capability; ander gedrag hangt eraan via de functie |
| [Bedrijfsobject](../../kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md), [Afspraak](../../kennismodel/bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | associatie | [Dienst](../../kennismodel/bedrijfsarchitectuur/dienst-modelleerafspraken.md) | een object hangt via het proces dat de dienst realiseert (toegang) aan een dienst |
