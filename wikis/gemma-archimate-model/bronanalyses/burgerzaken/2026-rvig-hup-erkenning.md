---
id: 2026-rvig-hup-erkenning
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-erkenning
relevant: ja
bijgewerkt: 2026-10-06
---

# HUP BRP: Erkenning

Bron: [tekst](../../../../sources/raw/2026-rvig-hup-erkenning.md) · [origineel (html)](../../../../sources/raw/2026-rvig-hup-erkenning.html) · [online](https://www.rvig.nl/hup/erkenning)

## Samenvatting

De HUP-pagina beschrijft de verwerking van een erkenning na de geboorteaangifte en van een nietige of vernietigde erkenning. Voor het model levert ze de gebeurtenis erkenning, het bedrijfsobject akte van erkenning (als latere vermelding op de geboorteakte, ook notarieel) en de rollen erkenner en moeder; registratiedetails (akteaanduidingen C en N, categorieën 04, 09 en 12) blijven buiten het model.

Vanaf 1 april 2014 kan zowel een man als een vrouw een kind erkennen. De ambtenaar van de burgerlijke stand voegt een latere vermelding toe aan de geboorteakte; een notariële akte van erkenning leidt ook tot een latere vermelding. Een nietige erkenning is nooit geldig geweest en wordt gecorrigeerd; een vernietigde erkenning is door de rechter vernietigd (bijvoorbeeld door bedreiging, dwaling of bedrog) en krijgt een nieuwe latere vermelding. Beide werken terug tot de erkenningsdatum. Gevolgen buiten de afstamming: het kind kan de Nederlandse nationaliteit krijgen en een geldig Nederlands reisdocument vervalt van rechtswege bij naamswijziging.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| erkenning | rechtsfeit waardoor een familierechtelijke betrekking ontstaat tussen kind en erkenner; vanaf 1 april 2014 door een man of een vrouw | kind erkennen | regel 24 |
| erkenning na de geboorteaangifte | erkenning op een later moment dan de geboorteaangifte; verwerkt als latere vermelding op de geboorteakte | — | regel 26, 30 |
| erkenner | persoon die het kind erkent | persoon door wie het kind is erkend | regel 68 |
| notariële akte van erkenning | brondocument; leidt tot een latere vermelding op de geboorteakte | — | regel 34 |
| latere vermelding erkenning | vermelding op de geboorteakte, ten grondslag aan de BRP-registratie | — | regel 28, 44 |
| nietige erkenning | erkenning die nooit rechtsgeldig is geweest; latere vermelding wordt doorgehaald | — | regel 28, 3298 |
| vernietiging van de erkenning | vernietiging door de rechter; nieuwe latere vermelding op de geboorteakte | vernietigde erkenning | regel 28, 3300 |
| erkenning in het buitenland | erkenning waarvoor geen Nederlandse geboorteakte is; gegevens uit het buitenlandse document | — | regel 38-40 |
| familierechtelijke betrekking bij erkenning | ontstaat door erkenning; vóór 1 september 1948 door erkenning door de ongehuwde moeder, 1948-2014 automatisch voor de moeder | — | regel 24 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| ambtenaar van de burgerlijke stand | voegt toe | latere vermelding erkenning (aan de geboorteakte) | regel 32, 44 |
| notaris | maakt op | notariële akte van erkenning | regel 34, 52 |
| bijhoudingsgemeente | actualiseert | persoonslijsten van de erkenner, de moeder en het kind | regel 36, 68-70 |
| rechtbank | vernietigt | erkenning | regel 3300 |
| rechtbank | haalt door (op last van) | latere vermelding erkenning (nietige erkenning) | regel 3298 |
| erkenner | erkent | kind | regel 24 |
| gemeente 's-Gravenhage | bewaart voor onbepaalde tijd | notariële akte van erkenning (zonder Nederlandse akte) | regel 34 |

## Relevantie voor de architectuur

- Gebeurtenissen erkenning (na de aangifte), nietigheid en vernietiging van de erkenning; bedrijfsobject akte van erkenning met latere vermelding op de geboorteakte; rollen erkenner en moeder.
- Product of dienst bij de gemeente: Kind erkennen (Utrecht, aparte bronanalyse). De HUP beschrijft alleen de verwerking in de BRP.
- Raakvlak met geboorte (erkenning voor of bij de aangifte staat op de pagina Geboorte), gezag (gezag na erkenning, pagina Gezag over een minderjarige) en nationaliteit.
- Termverschil: HUP-erkenning 'na de geboorteaangifte' versus erkenning 'ongeboren vrucht' bij de aangifte; de gemeentelijke naam is erkenning.

## Citaten

> Een nietige erkenning is een erkenning die nooit rechtsgeldig is geweest. (regel 3298)
