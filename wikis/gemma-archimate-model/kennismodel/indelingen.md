---
id: indelingen
type: kennismodel
titel: Indelingen
---

# Indelingen

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

Waar staat elk element in het model? Een **indeling** ordent naar één criterium, met benoemde niveaus. Een view toont één indeling voor één of meer elementtypen.

## Voor alle indelingen

- Alles ingedeeld: elk element staat in minstens één indeling, ook in de export.
- GEMMA volgen: de GEMMA-indelingen blijven ongewijzigd; een nieuwe indeling komt er alleen waar GEMMA er geen heeft, en een tweede elementtype met hetzelfde criterium valt in de bestaande indeling.
- Specialisatie koppelt aan een GEMMA-indeling (wat voor soort is het?), aggregatie aan een eigen indeling (waar hoort het bij?).
- Bij voorkeur hiërarchisch; meer ouders geeft een signaal, behalve de twee ouders van een bedrijfsproces (levensloopproces en cluster naar soort werk).

## Beleidsdomeinindeling

|  |  |
|---|---|
| Deelt in | [Bedrijfsobject](bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md); [Afspraak](bedrijfsarchitectuur/afspraak-modelleerafspraken.md); [Product](bedrijfsarchitectuur/product-modelleerafspraken.md); [Dienst](bedrijfsarchitectuur/dienst-modelleerafspraken.md); [Beleidskader](motivatie/beleidskader-modelleerafspraken.md); [Bedrijfsproces](bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) (alleen een levensloopproces, onder het beleidsdomein van zijn kernobject); [Bedrijfsinteractie](bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) (onder het beleidsdomein van haar kernobject) |
| Naar | het taakveld (Iv3) en het beleidsdomein |
| Niveaus | taakveld › beleidsdomein › element |
| Groepering | GEMMA |
| In Archi | aggregatie vanuit de groepering van het beleidsdomein; een beleidsdomein dat GEMMA niet kent wordt een nieuwe groepering onder het taakveld, in de map van de wiki |
| Eigenschappen | `taakveld`, `beleidsdomein` |

- Een bedrijfsobject heeft één beleidsdomein; het beleidsdomein van een levensloopproces en een bedrijfsinteractie volgt uit hun kernobject.
- Een beleidsdomein dat GEMMA niet kent, wordt een gemeentelijk beleidsdomein met een terugmelding; zijn beschrijving staat in het register van beleidsdomeinen.
- Het domein van een product of dienst past bij de GEMMA-domeinen van zijn beleidsdomein.

## Functie-indeling naar domein

|  |  |
|---|---|
| Deelt in | [Bedrijfsfunctie](bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md); [Product](bedrijfsarchitectuur/product-modelleerafspraken.md); [Dienst](bedrijfsarchitectuur/dienst-modelleerafspraken.md) |
| Naar | het GEMMA-domein |
| Niveaus | domein › functie (de keten tot het domeinniveau) › dienst; domein › product |
| Groepering | GEMMA |
| In Archi | aggregatie vanuit de domeingroepering (een functie op domeinniveau, een product) of vanuit de bovenliggende functie (een functie, een dienst) |
| Eigenschappen | `domein` |

- De Functie-indeling is een relatie, geen eigenschap: de bovenliggende functie wordt een element en aggregeert de functie eronder, volgens de GEMMA-functieketen, tot en met de functie op domeinniveau (GEMMA type *Bedrijfsfunctie domein*); alleen die hangt via `domein` aan de domeingroepering.
- Een dienst hangt onder één functie in hetzelfde domein.
- Een product hangt via `domein` direct aan de domeingroepering: ArchiMate laat een functie geen product aggregeren. De diensten die het omvat, hangen onder hun functie.
- Een functie bedient een proces; ze aggregeert geen proces.

## Procesindeling naar kernobject

|  |  |
|---|---|
| Deelt in | [Bedrijfsproces](bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) (levensloopproces en bedrijfsproces); [Gebeurtenis](bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md); [Bedrijfsinteractie](bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) |
| Naar | het kernobject |
| Niveaus | levensloopproces (per kernobject) › bedrijfsproces; een gebeurtenis onder het levensloopproces van het object waarvan de toestand verandert; een bedrijfsinteractie bij haar kernobject |
| Groepering | wiki |
| In Archi | aggregatie; in de map Procesindeling naar kernobject, een bedrijfsinteractie in de map Ketensamenwerking |
| Eigenschappen | `kernobject` |

- Strikt hiërarchisch: per kernobject één levensloopproces, of één per partij als ze samen een bedrijfsinteractie met dat kernobject bedienen; een levensloopproces aggregeert geen levensloopproces; een bedrijfsproces hangt onder hoogstens één levensloopproces.
- Het taakveld en beleidsdomein van een levensloopproces en een bedrijfsinteractie zijn die van hun kernobject.

## Procesindeling naar soort werk

|  |  |
|---|---|
| Deelt in | [Bedrijfsproces](bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) (cluster naar soort werk en bedrijfsproces); [Gebeurtenis](bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) (bij *generiek*); [Dienst](bedrijfsarchitectuur/dienst-modelleerafspraken.md) (bij *generiek*); [Rol](bedrijfsarchitectuur/rol-modelleerafspraken.md) (bij *generiek*) |
| Naar | de soort werk (het processenlandschap van GEMMA) |
| Niveaus | generiek GEMMA-element › cluster naar soort werk › bedrijfsproces |
| Groepering | GEMMA, uitgebreid |
| In Archi | specialisatie naar het generieke GEMMA-element (exacte match); aggregatie van cluster naar bedrijfsproces |
| Eigenschappen | `gemma_generiek` |

- Specialisatie en bediening naar GEMMA lopen alleen via een exacte match.
- Een cluster naar soort werk breidt het processenlandschap uit zonder GEMMA-elementen te wijzigen.

## Doelgroepindeling

|  |  |
|---|---|
| Deelt in | [Actor](bedrijfsarchitectuur/actor-modelleerafspraken.md); [Rol](bedrijfsarchitectuur/rol-modelleerafspraken.md); [Bedrijfssamenwerking](bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md); [Kanaal](bedrijfsarchitectuur/kanaal-modelleerafspraken.md) |
| Naar | de doelgroep |
| Niveaus | doelgroep (gemeente, inwoners en ondernemers, ketenpartners) › element |
| Groepering | wiki |
| In Archi | aggregatie vanuit de groepering van de doelgroep, in de map Doelgroepindeling |
| Eigenschappen | `doelgroep` |

- Een doelgroep is een ordening, geen hoedanigheid: in de wiki een groepering. GEMMA modelleert de doelgroep als rol (GEMMA type *Groep*) die applicatieservices ordent; die afwijking is teruggemeld.

## Grondslagindeling

|  |  |
|---|---|
| Deelt in | [Beleidskader](motivatie/beleidskader-modelleerafspraken.md) |
| Naar | het brontype van de regeling, afgeleid uit de regelgever |
| Niveaus | groep (Europese regelgeving, Rijksregelgeving, Richtlijn, Gemeentelijke regelgeving) › beleidskader |
| Groepering | wiki |
| In Archi | aggregatie vanuit de groep; groep en map heten als het brontype, in de map Grondslagindeling |
| Eigenschappen | `regelgever` |

| Regelgever | Groep | Omschrijving |
|---|---|---|
| EU | Europese regelgeving | Regelgeving van de Europese Unie die voor alle gemeenten geldt, zoals verordeningen die rechtstreeks werken (AVG, AI-verordening). |
| rijk | Rijksregelgeving | Regelgeving van het Rijk die voor alle gemeenten gelijk is: wetten, algemene maatregelen van bestuur en ministeriële regelingen, en door Nederland goedgekeurde verdragen. |
| landelijke organisatie | Richtlijn | Landelijke uitvoeringsvoorschriften, handleidingen, circulaires en handreikingen van het Rijk, uitvoeringsorganisaties en koepels (HUP van RvIG, NVVB, VNG, Divosa). |
| VNG-model | Gemeentelijke regelgeving | Verordeningen, nadere regels, beleidsregels en regelingen van gemeenschappelijke regelingen, die elke gemeente zelf vaststelt, en de VNG-modellen daarvan. Omdat de inhoud per gemeente verschilt, staat in het model het VNG-model als gemeenschappelijke vorm; de regeling van één gemeente is een voorbeeld en geen element. |

- Alleen gevulde groepen bestaan.
- De naam van de relatie van een beleidskader volgt de groep: *is grondslag voor*, *werkt uit voor* of *geeft richtlijn voor*.
