---
title: "Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) 2.02 - Deel II: Specificaties"
source: "https://vng-realisatie.github.io/RSGB/documenten/RSG_Basisgegevens_2.02_deel_II_(in_gebruik).pdf"
source_page: "https://standaarden.vng.nl/Informatiemodellen"
author: "VNG Realisatie (voorheen KING)"
published:
created: 2026-09-23
description: "Gegevenscatalogus van het RSGB 2.02: specificaties van alle 62 objecttypen, attribuutsoorten en relatiesoorten, inclusief de door KING toegevoegde detailentiteiten bovenop de basisregistraties."
tags:
  - "Standaarden"
---

**==> picture [226 x 112] intentionally omitted <==**

**==> picture [426 x 372] intentionally omitted <==**

## **Referentiemodel** 

**Stelsel van Gemeentelijke Basisgegevens** Deel II: Specificaties 

onderdeel van de GEMeentelijke Model Architectuur (GEMMA) 

In deel I van de gelijknamige rapportage is versie 2.02 van het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) op hoofdlijnen beschreven en nader toegelicht. Dit deel II bevat de specificaties van de componenten waaruit versie 2.02 van het RSGB is opgebouwd: objecttypen (hoofdstuk 1), attribuutsoorten en relatiesoorten (hoofdstuk 2). In bijlage 1 specificeren we de gebruikte metagegevens. 

## **Inhoudsopgave** 

**1. De soorten van objecten van registratie......................................................6** 1.1. Aard recht verkort..............................................................................................................9 1.2. Aard verkregen recht........................................................................................................10 1.3. Academische titel.............................................................................................................11 1.4. Adresseerbaar object.......................................................................................................12 1.5. Adresseerbaar object aanduiding....................................................................................13 1.6. Ander natuurlijk persoon..................................................................................................14 1.7. Ander niet natuurlijk persoon...........................................................................................16 1.8. Appartementsrecht ..........................................................................................................18 1.9. Benoemd object...............................................................................................................20 1.10. Benoemd Terrein...........................................................................................................21 1.11. Buurt..............................................................................................................................22 1.12. Functionaris...................................................................................................................23 1.13. Gebouwd object.............................................................................................................24 1.14. Gemeente......................................................................................................................25 1.15. Gemeentelijke Openbare Ruimte...................................................................................26 1.16. Huishouden....................................................................................................................27 1.17. Huishoudenrelatie..........................................................................................................29 1.18. Huwelijk/geregistreerd partnerschap .............................................................................30 1.19. Ingeschreven niet-natuurlijk persoon.............................................................................31 1.20. Ingeschreven persoon....................................................................................................33 1.21. Ingezetene.....................................................................................................................36 1.22. Inrichtingselement..........................................................................................................39 1.23. Kadastrale gemeente.....................................................................................................40 1.24. Kadastrale onroerende zaak .........................................................................................41 1.25. Kadastrale onroerende zaak aantekening......................................................................43 1.26. Kadastrale onroerende zaak historie relatie...................................................................44 1.27. Kadastraal perceel ........................................................................................................45 1.28. Kunstwerkdeel...............................................................................................................47 1.29. Land...............................................................................................................................48 1.30. Ligplaats.........................................................................................................................49 1.31. Maatschappelijke activiteit.............................................................................................50 1.32. Nationaliteit....................................................................................................................51 1.33. Natuurlijk persoon..........................................................................................................52 1.34. Niet-ingezetene..............................................................................................................54 1.35. Niet-natuurlijk persoon...................................................................................................57 1.36. Nummeraanduiding........................................................................................................59 1.37. Openbare Ruimte...........................................................................................................61 1.38. Ouder-kind-relatie..........................................................................................................62 1.39. Overige adresseerbaar object aanduiding.....................................................................63 1.40. Overig gebouwd object..................................................................................................65 1.41. Overig Terrein................................................................................................................67 1.42. Pand...............................................................................................................................68 1.43. Rechtspersoon ..............................................................................................................69 1.44. Reisdocument................................................................................................................71 1.45. Reisdocumentsoort........................................................................................................72 

1.46. Spoorbaandeel...............................................................................................................73 1.47. Standplaats....................................................................................................................74 1.48. Subject...........................................................................................................................75 1.49. Terreindeel.....................................................................................................................77 1.50. Verblijfsobject.................................................................................................................78 1.51. Verblijfstitel.....................................................................................................................80 1.52. Vestiging........................................................................................................................81 1.53. Waterdeel.......................................................................................................................83 1.54. Wegdeel.........................................................................................................................84 1.55. Wijk................................................................................................................................85 1.56. Woonplaats....................................................................................................................86 1.57. WOZ-belang...................................................................................................................87 1.58. WOZ-deelobject.............................................................................................................88 1.59. WOZ-object....................................................................................................................89 1.60. WOZ-waarde..................................................................................................................90 1.61. Zakelijk recht .................................................................................................................91 1.62. Zakelijk recht aantekening.............................................................................................92 **2. Beschrijving van de attributen en relaties ................................................93** 2.1. Aard recht verkort............................................................................................................99 2.2. Aard verkregen recht......................................................................................................101 2.3. Academische titel...........................................................................................................103 2.4. Adresseerbaar object.....................................................................................................107 2.5. Adresseerbaar object aanduiding..................................................................................108 2.6. Ander natuurlijk persoon................................................................................................121 2.7. Ander niet-natuurlijk persoon.........................................................................................123 2.8. Appartementsrecht.........................................................................................................124 2.9. Authentiek terrein...........................................................................................................127 2.10. Benoemd object...........................................................................................................130 2.11. Benoemd Terrein.........................................................................................................135 2.12. Buurt............................................................................................................................140 2.13. Functionaris.................................................................................................................146 2.14. Gebouwd object...........................................................................................................150 2.15. Gemeente....................................................................................................................163 2.16. Gemeentelijke Openbare Ruimte.................................................................................170 2.17. Huishouden..................................................................................................................179 2.18. Huishoudenrelatie........................................................................................................186 2.19. Huwelijk/geregistreerd partnerschap............................................................................188 2.20. Ingeschreven niet-natuurlijk persoon...........................................................................196 2.21. Ingeschreven persoon..................................................................................................200 2.22. Ingezetene...................................................................................................................231 2.23. Inrichtingselement........................................................................................................238 2.24. Kadastrale gemeente...................................................................................................244 2.25. Kadastrale onroerende zaak .......................................................................................247 2.26. Kadastrale onroerende zaak aantekening....................................................................273 2.27. Kadastrale onroerende zaak historie relatie.................................................................278 2.28. Kadastraal perceel.......................................................................................................281 2.29. Kunstwerkdeel.............................................................................................................287 2.30. Land.............................................................................................................................293 

2.31. Ligplaats.......................................................................................................................301 2.32. Maatschappelijke activiteit...........................................................................................305 2.33. Nationaliteit..................................................................................................................315 2.34. Natuurlijk persoon........................................................................................................319 2.35. Niet-ingezetene............................................................................................................332 2.36. Niet-natuurlijk persoon.................................................................................................333 2.37. Nummeraanduiding......................................................................................................337 2.38. Openbare Ruimte.........................................................................................................345 2.39. Ouder-kind-relatie........................................................................................................353 2.40. Overige adresseerbaar object aanduiding...................................................................357 2.41. Overig gebouwd object................................................................................................359 2.42. Overig Terrein..............................................................................................................364 2.43. Pand.............................................................................................................................366 2.44. Rechtspersoon.............................................................................................................381 2.45. Reisdocument..............................................................................................................386 2.46. Reisdocumentsoort......................................................................................................392 2.47. Spoorbaandeel.............................................................................................................396 2.48. Standplaats..................................................................................................................403 2.49. Subject.........................................................................................................................408 2.50. Terreindeel...................................................................................................................426 2.51. Verblijfsobject...............................................................................................................433 2.52. Verblijfstitel...................................................................................................................445 2.53. Vestiging......................................................................................................................449 2.54. Waterdeel.....................................................................................................................460 2.55. Wegdeel.......................................................................................................................467 2.56. Wijk..............................................................................................................................474 2.57. Woonplaats..................................................................................................................479 2.58. WOZ-belang.................................................................................................................489 2.59. WOZ-deelobject...........................................................................................................493 2.60. WOZ-object..................................................................................................................499 2.61. WOZ-waarde................................................................................................................510 2.62. Zakelijk recht................................................................................................................513 2.63. Zakelijk recht aantekening...........................................................................................520 **Bijlage 1: Metagegevens...............................................................................524** Metagegevens betreffende materiële historie...................................................................525 Metagegevens betreffende formele historie.....................................................................527 Metagegevens betreffende gebeurtenissen.....................................................................528 Metagegevens betreffende brondocumenten...................................................................529 Metagegevens betreffende ‘in onderzoek’........................................................................532 Metagegevens betreffende strijdigheid / nietigheid..........................................................533 

## **1. De soorten van objecten van registratie** 

In dit hoofdstuk worden de onderscheiden objecttypen gespecificeerd naar analogie van de voor basisregistratie-catalogi gebruikelijke wijze. In afwijking daarvan wordt hier uitgegaan van de specificatie van een semantisch model (met objecten, attributen en relaties) daar waar in de basisregistratiecatalogi wordt uitgegaan van objecttypen als berichten d.w.z. veel meer van een berichtenmodel. Hiervoor is gekozen omdat het ten eerste van belang is de semantiek van het model te specificeren. Ten tweede geeft dit bij de vertaling naar berichten de vrijheid die nodig is om een zo optimaal mogelijke berichtenuitwisseling te verkrijgen. Een andere afwijking is de wijze waarop we omgaan met gegevens over brondocumenten, over het in onderzoek zijn van gegevens, over strijdigheid en nietigheid van gegevens en over gebeurtenissen. Deze gegevens specificeren we niet als attribuutsoorten (zoals gebruikelijk in de basisregistratiecatalogi) maar nemen we op als metagegevens bij de attribuutsoorten waarop ze betrekking hebben. 

De objecttypen worden naar de volgende aspecten gespecificeerd. 

- **Naam objecttype** De naam van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegd objecttype betreft, de door KING vastgestelde naam van het objecttype. 

- **Mnemonic objecttype** De in StUF-BG gehanteerde afkorting voor de naam van het objecttype. Objecttypen met een mnemonic tussen (haakjes) worden (nog) niet als zelfstandige entiteit in StUF-BG gebruikt. 

- **Herkomst objecttype** De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd t.o.v. de basisregistratie-catalogus aangezien het hier niet om een basisregistratie gaat maar wel duidelijk moet zijn in welke basisregistratie het objecttype voorkomt (indien van toepassing). 

- **(Code objecttype)** De door de desbetreffende basisregistratiehouder aan het objecttype toegekende uniek code. Deze wordt hier niet vermeld aangezien deze gespecificeerd is in de desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van het specificeren van deze code. 

- **(Afkorting objecttype)** De door de desbetreffende basisregistratiehouder gehanteerde afkorting van de naam van het objecttype. Deze wordt hier niet vermeld aangezien deze gespecificeerd is in de desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van het specificeren van deze afkorting. 

- **Definitie objecttype** De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegd objecttype betreft, de door KING vastgestelde definitie van het objecttype. 

> **Herkomst definitie objecttype** Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd objecttype betreft. 

- **Datum opname objecttype** 

De datum waarop het objecttype is opgenomen in het RSGB. 

- **Toelichting objecttype** Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de daarin opgenomen toelichting. De toelichting wordt dan ook alleen gegeven indien het een door KING toegevoegd objecttype betreft dan wel indien een toelichting nodig is, aanvullend op de toelichting in de desbetreffende catalogus. 

- **(Relatie met semantische** De door de desbetreffende basisregistratiehouder gehanteerde **kern)** beschrijving van de wijze waarop het objecttype in relatie staat tot de semantische kern van het stelsel van basisregistraties. Deze wordt hier niet vermeld aangezien deze gespecificeerd is in de desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van het specificeren van deze relatie. 

- **Unieke aanduiding objecttype** Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de wijze waarop daarin voorkomende objecten (van dit type) uniek in de registratie worden aangeduid. Deze aanduiding wordt dan ook alleen vermeld indien het een door KING toegevoegd objecttype betreft. 

- **(Identificatie objecttype)** De door de desbetreffende basisregistratiehouder gehanteerde vermelding door middel van welke aan het object zelf waarneembare eigenschappen deze uniek kan worden aangeduid (‘wanneer is sprake van één exemplaar?’). Deze wordt hier niet vermeld aangezien deze gespecificeerd is in de desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van deze vermelding. 

- **Populatie objecttype** Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende basisregistratie voorhanden zijn. Deze beschrijving wordt dan ook alleen gegeven indien het een door KING toegevoegd objecttype betreft. 

- **Kwaliteitsbegrip objecttype** Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de waarborgen voor de juistheid van de in de registratie opgenomen objecten van het desbetreffende type. Deze beschrijving wordt dan ook alleen gegeven indien het een door KING toegevoegd objecttype betreft. 

- **Overzicht attributen** _Code Gegevensnaam Herkomst_ 

Hier worden de attribuutsoorten gespecificeerd die behoren tot het desbetreffende objecttype. In afwijking van hetgeen in de basisregistratiecatalogi gebruikelijk is, worden de attribuutsoorten gespecificeerd van het objecttype en niet van een daarop te baseren bericht. ‘Relatie-attribuutsoorten’ komen dan ook niet voor; de desbetreffende relaties worden onder de attribuutsoorten gespecificeerd. Attribuutsoorten kunnen deel uit maken van een zgn. attribuutgroep. De tot een dergelijke groep behorende attribuutsoorten zijn inspringend vermeld. Een attribuutsoort kan gespecificeerd zijn bij het desbetreffende objecttype in de desbetreffende catalogus dan wel door KING toegevoegd zijn. In het eerste geval is de attribuutsoortcode opgenomen, voor zover dit gespecificeerd is in de desbetreffende catalogus. In de kolom ‘Herkomst’ is aangegeven in welke basisregistratiecatalogus dit attribuutsoort is gespecificeerd (indien van toepassing). Indien hier een basisregistratiecatalogus vermeld wordt terwijl het objecttype niet afkomstig is van dezelfde basisregistratie, dan betreft het een generalisatie van andere objecttypen en is de attribuutsoort van toepassing op alle laatstgenoemde objecttypen (de zgn. specialisaties waaronder het objecttype in de basisregistratie waarbij de attribuutsoort hoort) en derhalve bij het eerstgenoemde objecttype (de generalisatie van de andere objecttypen) gemodelleerd. 

## **Overzicht relaties** 

Een bijzondere situatie doet zich voor indien het objecttype een generalisatie is van andere objecttypen dan wel dat het een specialisatie betreft van een ander objecttype.  Bij het eerstgenoemde objecttype worden de attribuutsoorten gespecificeerd die van toepassing zijn op alle specialisaties daarvan. Bij het andere objecttype worden om redenen van semantiek cq. leesbaarheid tevens genoemd de attribuutsoorten die behoren tot de generalisatie van dit objecttype. De attribuutsoorten worden nader gespecificeerd in hoofdstuk 2. _Relatienaam incl. gerelateerd objecttype Herkomst_ In afwijking van hetgeen in de basisregistratiecatalogi gebruikelijk is, worden hier de relaties gespecificeerd die het desbetreffende objecttype heeft met andere objecttypen. Naar analogie van de specificatie van attribuutsoorten worden bij specialisaties van objecttypen tevens de relaties genoemd die behoren tot de generalisatie van dit objecttype. De relatiesoorten worden nader gespecificeerd in hoofdstuk 2. 

De tussen haken vermelde specificaties zijn derhalve niet opgenomen. Bij een objecttype dat deel uit maakt van een basisregistratie worden slechts een beperkt aantal specificaties opgenomen met het oog op de onderhoudbaarheid van het model. Voor de niet vermelde specificaties wordt verwezen naar de specificatie van het objecttype in de catalogus van de desbetreffende basisregistratie. 

## **1.1. Aard recht verkort** 

**Naam objecttype** 

AARD RECHT VERKORT 

## **Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype Overzicht attributen** 

## **Overzicht relaties** 

## BRK 

De EDI code en de verkorte omschrijving van de aard van een zakelijk recht 

## 30 maart 2009 

Zie de catalogus van de BRK en de beschrijving van IMKAD. Daarin is sprake van het attribuut Aanduiding aard zakelijk recht verkort. Deze verwijst naar een tabel. Die tabel modelleren we met dit objecttype. 

Aanduiding aard verkregen recht 

_Code Gegevensnaam Herkomst_ Aanduiding aard recht verkort BRK Omschrijving aard recht verkort KING _Relatienaam incl. gerelateerd objecttype Herkomst_ Betreft ZAKELIJKe RECHTen KING/BRK 

## **1.2. Aard verkregen recht** 

**Naam objecttype** 

AARD VERKREGEN RECHT 

**Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype Overzicht attributen** 

**Overzicht relaties** 

## BRK 

De aanduiding en omschrijving van de aard van een zakelijk recht 

## 30 maart 2009 

Zie de catalogus van de BRK en de beschrijving van IMKAD. Daarin is sprake van het attribuut Aanduiding aard verkregen zakelijk recht. Deze verwijst naar een tabel. Die tabel modelleren we met dit objecttype. 

Aanduiding aard verkregen recht 

_Code Gegevensnaam Herkomst_ Aanduiding aard verkregen recht BRK Omschrijving aard verkregen recht KING _Relatienaam incl. gerelateerd objecttype Herkomst_ Betreft ZAKELIJKe RECHTen KING/BRK 

## **1.3. Academische titel** 

**Naam objecttype** 

## ACADEMISCHE TITEL 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype** 

ACD 

## GFO 

Een formeel via het Staatsblad gepubliceerde aanduiding van een wetenschappelijke of andere graad van opleiding welke bij aanschrijving voorafgaat aan de voornamen (dan wel de daarvan afgeleide naamgegevens) dan wel volgt op de achternaam. NEN 1888, december 1991 

**Datum opname objecttype Toelichting objecttype** 

1 november 2008 

Buitenlandse titels worden niet geregistreerd. 

> **Unieke aanduiding objecttype** Academische titelcode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

_Code Gegevensnaam Herkomst_ 94.80 Academische titelcode GFO BG 95.62 Omschrijving academische titel GFO BG 95.72 Positie academische titel tov naam GFO BG Datum begin geldigheid titel KING Datum einde geldigheid titel KING 

_Relatienaam incl. gerelateerd objecttype_ hoort bij NATUURLIJK PERSOONen 

_Herkomst_ KING/GFO 

## **1.4. Adresseerbaar object** 

> **Naam objecttype** ADRESSEERBAAR OBJECT 

> **Mnemonic objecttype** AOT 

> **Herkomst objecttype** BAG **Code objecttype** 

> **Definitie objecttype** Een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 1 maart 2009 

> **Toelichting objecttype** Het betreft de generalisatie van genoemde objecttypen. Daarmee wordt aangesloten bij deze in de BAG gehanteerde terminologie cq. groepering. Het objecttype is enkel en alleen opgenomen als referentie naar de BAG en kent geen andere attribuut- en relatiesoorten dan de attribuut- en relatiesoorten van de specialisaties. 

> **Unieke aanduiding objecttype** De unieke aanduidingen van de specialisaties van dit objecttype. **Populatie objecttype Kwaliteitsbegrip objecttype** 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ 

> **Overzicht relaties** _Relatienaam incl. gerelateerd objecttype Herkomst_ 

## **1.5. Adresseerbaar object aanduiding** 

> **Naam objecttype** ADRESSEERBAAR OBJECT AANDUIDING 

> **Mnemonic objecttype** AOA 

> **Herkomst objecttype** Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

> **Definitie objecttype** Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een OVERIG GEBOUWD OBJECT of een OVERIG TERREIN. 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Het betreft de verzameling van, tot de BAG behorende, officieel vastgestelde nummeraanduidingen (van verblijfsobjecten, stand- en ligplaatsen, in de BAG gezamenlijk aangeduid als adresseerbare objecten) en overige, eveneens officieel door de gemeente vastgestelde, nummeraanduidingen van overige gebouwde objecten en overige terreinen. De Adresseerbaar object aanduiding heeft dus betrekking op alle 'benoemde objecten', d.w.z. naast de specialisaties van het Adresseerbaar object (Verblijfsobject, Ligplaats en Standplaats) ook op Overig gebouwd object en op Overig terrein! 

Het betreft een generalisatie van twee objecttypen (de specialisaties) waarbij de attributen en relaties die op beide specialisaties van toepassing zijn, bij dit objecttype worden gespecificeerd. 

> **Unieke aanduiding objecttype** Identificatiecode adresseerbaar object aanduiding 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_<br>_Gegevensnaam_|_Herkomst_|_Herkomst_|
|---|---|---|---|
||BAG-gegevens|KING||
||11.02 Identificatiecode adresseerbaar object|aanduiding|BAG|
||11.20 Huisnummer|BAG||
||11.30 Huisletter|BAG||
||11.40 Huisnummertoevoeging|BAG||
||11.60 Postcode|BAG||
||Datum begin geldigheid adresseerbaar object|||
||aanduiding|KING||
||Datum einde geldigheid adresseerbaar object|||
||aanduiding|KING||
||Adresseerbaar object aanduiding typering|KING||
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_||
||BAG-gegevens|KING||
||Ligt aan OPENBARE RUIMTE|BAG||
||Ligt in WOONPLAATS|BAG||
||Is correspondentieadres van SUBJECT|KING/GFO||
||Is bezoekadres van NIET-NATUURLIJK PERSOON|KING/NHR||
||Is bezoekadres van ANDER NATUURLIJK PERSOON|KING||
||is locatie-adres van VESTIGINGen|KING/NHR||
||bepaalt aanduiding van WOZ-OBJECT|BRWOZ/KING||



## **1.6. Ander natuurlijk persoon** 

**Naam objecttype** 

ANDER NATUURLIJK PERSOON 

**Mnemonic objecttype** 

## ANP 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

Een NATUURLIJK PERSOON, niet ingeschreven in de BasisRegistratie Personen (GBA en RNI), woonachtig in Nederland dan wel woonachtig in het buitenland en van belang voor de gemeentelijke taakuitoefening. 

## KING 

9 april 2007 

Het betreft hier de natuurlijke personen die niet ingeschreven zijn in de GBA en het RNI maar wel van belang zijn voor de gemeentelijke taakuitoefening. Het kan gaan om zowel in Nederland woonachtige personen als in het buitenlandse verblijvende personen. 

Een ANDER NATUURLIJK PERSOON  is een specialisatie (‘deelverzameling’) van NATUURLIJK PERSOON. 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

De SUBJECT.Subjecttypering gevolgd door het Nummer ander natuurlijk persoon 

Alle andere natuurlijke personen die op enigerlei wijze van belang zijn voor de gemeentelijke taakuitoefening. 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Nummer ander natuurlijk persoon|KING|
|Attributen van de generalisatie NATUURLIJK PERSOON:|||
|01|Persoonsgegevens|GBA|
||01.02 Naam|GBA|
||01.02.10 Voornamen|GBA|
||01.02.20  Adellijke titel/predikaat|GBA|
||01.02.30  Voorvoegsels geslachtsnaam|GBA|
||01.02.40 Geslachtsnaam|GBA|
||01.04.10 Geslachtsaanduiding|GBA|
||01.61.10 Aanduiding naamgebruik|GBA|
||01.03 Geboorte|GBA|
||01.03.10  Geboortedatum|GBA|
|Naam|aanschrijving|KING|
||Aanhef aanschrijving|KING|
||Voorletters aanschrijving|KING|
||Voornamen aanschrijving|KING|
||Geslachtsnaam aanschrijving|KING|
|06|Overlijden|GBA|
||06.08.10 Overlijdensdatum|GBA|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|



## **Overzicht relaties** 

|08.13<br>Verblijf buitenland|KING/GBA|
|---|---|
|08.13.30 Adres buitenland 1|KING/GBA|
|08.13.40 Adres buitenland 2|KING/GBA|
|08.13.50 Adres buitenland 3|KING/GBA|
|95.80<br>Telefoonnummer|GFO BG|
|95.27<br>Fax-nummer|GFO BG|
|95.16<br>Emailadres|GFO BG|
|Website-URL|KING|
|94.87<br>Bank/girorekeningnummer|GFO BG|
|Subjecttypering|KING|
|Naam|KING|
|Identificatie|KING|
|Adres binnenland|KING|
|Adres buitenland|KING|
|KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|heeft als bezoekadres ADRESSEERBAAR OBJECTAANDUIDING||
||KING|
|Relaties van de generalisatie NATUURLIJK PERSOON:||
|Heeft ACADEMISCHE TITEL|GFO BG|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.7. Ander niet natuurlijk persoon** 

**Naam objecttype** 

ANDER NIET NATUURLIJK PERSOON 

**Mnemonic objecttype** 

## ANN 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

Een NIET-NATUURLIJK PERSOON, niet ingeschreven in het Nieuw HandelsRegister. Gevestigd in Nederland dan wel in het buitenland, en van belang voor de gemeentelijke taakuitoefening, 

## KING 

## 9 april 2007 

Het betreft hier de niet-natuurlijke personen die van belang zijn voor de gemeentelijke taakuitoefening maar niet ingeschreven zijn in het NHR. Te denken valt aan in Nederland gevestigde niet-natuurlijke personen die niet inschrijfplichtig zijn in de NHR zoals de rechterlijke macht en kerkelijke organisaties. En verder buitenland se  niet-natuurlijke personen die geen vestigingen in Nederland hebben en dus niet ingeschreven zijn in het NHR. 

De SUBJECT.Subjecttypering gevolgd door het Nummer ander nietnatuurlijk persoon 

Alle niet natuurlijke personen die niet ingeschreven zijn in het NHR maar die op enigerlei wijze van belang zijn voor de gemeentelijke taakuitoefening. 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Nummer ander niet-natuurlijk persoon|KING|
|Attributen van de generalisatie NIET-NATUURLIJK PERSOON:|||
||(Statutaire) Naam|NHR|
||Datum aanvang|NHR|
||Datum beëindiging|NHR|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|



## **Overzicht relaties** 

|KvK-nummer|KING|
|---|---|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Relaties van de generalisatie NIET-NATUURLIJK PERSOON:||
|Is vereniging van eigenaars bij appartementencomplex||
|met APPARTEMENTSRECHTen|BRK|
|Heeft als bezoekadres ADRESSEERBAAR OBJECT|NHR|
|AANDUIDING||
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS|KING|
|Is aangewezen belanghebbende bij WOZ-BELANG               BRWOZ/KING||
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.8. Appartementsrecht** 

**Naam objecttype** 

## APPARTEMENTSRECHT 

> **Mnemonic objecttype** APR 

> **Herkomst objecttype** Door KING toegevoegd objecttype, ontleend aan de BRK. 

> **Definitie objecttype** Een KADASTRALE ONROERENDE ZAAK dat is aangeduid, bestaande uit een aandeel in recht(en) op de onroerende zaak/zaken die in de splitsing is/zijn betrokken en dat de bevoegdheid bevat tot het uitsluitend gebruik van bepaalde gedeelten van een onroerende zaak, die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt. Het aandeel kan omvatten de bevoegdheid tot het uitsluitend gebruik van bepaalde gedeelten van een gebouw en van de bij het gebouw behorende grond (definitie is ontleend aan art 2, Kadasterbesluit). 

> **Herkomst definitie objecttype** BRK 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## 9 april 2007 

Een APPARTEMENTSRECHT behoort tezamen met het KADASTRAAL PERCEEL  tot de generalisatie KADASTRALE ONROERENDE ZAAK. 

**Unieke aanduiding objecttype** 

Unieke aanduiding van de KADASTRALE ONROERENDE ZAAK gevolgd door de Kadastrale onroerende zaak.kadastrale onroerende zaak typering en de Appartementsindex 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding||
|||BRK|
||Appartementsindex|BRK|
|Attributen van de generalisatie KADASTRALE ONROERENDE ZAAK:|||
||Kadastrale identificatie|BRK|
||Kadastrale aanduiding|BRK|
||Kadastrale gemeentecode|BRK|
||Sectie|BRK|
||Perceelnummer|BRK|
||Locatie onroerende zaak|BRK|
||Locatie-omschrijving|BRK|
||Cultuur bebouwd|BRK|
||Koopsom|BRK|
||Valutasoort|BRK|
||Aard bedrag|BRK|
||Bedrag|BRK|
||Koopjaar|BRK|
||Meer onroerendgoed|BRK|
||Transactiedatum|KING|
||Landinrichtingsrente|BRK|
||Aanduiding aard Liproject|BRK|
||Valutasoort|BRK|
||Aard bedrag|BRK|
||Bedrag|BRK|



## **Overzicht relaties** 

|Eindjaar|BRK|
|---|---|
|Cultuur onbebouwd|BRK|
|Aard cultuur onbebouwd|BRK|
|Aard bebouwing|BRK|
|Meer culturen|BRK|
|81.20<br>Datum begin geldigheid kadastrale onroerende zaak|KING/GFO|
|81.30<br>Datum einde geldigheid kadastrale onroerende zaak|KING/GFO|
|Kadastrale onroerende zaak typering|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|maakt deel uit van appartementencomplex met als vereniging||
|van eigenaars NIET-NATUURLIJK PERSOON|BRK|
|maakt deel uit van appartementencomplex dat||
|staat op KADASTRAAL PERCEEL|BRK|
|Relaties van de generalisatie KADASTRALE ONROERENDE ZAAK:||
|Ligt in KADASTRALE GEMEENTE|KING/brk|
|Heeft één of meer ZAKELIJK RECHT|KING/BRK|
|Locatie onroerende zaak||
|Is ondergrond van of heeft ruimtelijke overlap met BENOEMD|OBJECT|
||KING/BRK|
|Is ontstaan uit andere kadastrale onroerende zaak bij||
|KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
|Is overgegaan in andere kadastrale onroerende zaak bij||
|KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
|Is hoofdperceel bij mandelige KADASTRALE ONROERENDE||
|ZAAKen|KING/BRK|
|Heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON|GFO BG|
|Behoort tot WOZ-OBJECT                                                       BRWOZ/KING||
|heeft KADASTRALE  ONROERENDE ZAAK AANTEKENING|BRK/KING|



## **1.9. Benoemd object** 

> **Naam objecttype** BENOEMD OBJECT 

> **Mnemonic objecttype** TGO 

> **Herkomst objecttype** KING 

> **Code objecttype** TGO 

> **Definitie objecttype** Een GEBOUWD OBJECT of een BENOEMD TERREIN 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 1 maart 2009 

> **Toelichting objecttype** Het objecttype betreft alle objecten die van een, al dan niet authentieke, nummeraanduiding voorzien worden. Anders gezegd, alle objecten ‘met een adres’. Het is aldus de generalisatie van zowel GEBOUWD OBJECT en BENOEMD TERREIN en daarmee tevens van alle specialsaties van deze objecttypen, met name VERBLIJFSOBJECT, OVERIG GEBOUWD OBJECT, STANDPLAATS, LIGPLAATS en OVERIG TERREIN. 

> **Unieke aanduiding objecttype** De unieke aanduiding van het GEBOUWD OBJECT of het BENOEMD TERREIN 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|ligt in BUURT|KING/GFO|
|staat op of heeft ruimtelijke overlap met KADASTRALE||
|ONROERENDE ZAAK|KING/BRK|
|bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
|is hoofdlocatie van VESTIGINGen|KING|
|is nevenlocatie van VESTIGINGen|KING|
|is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.10. Benoemd Terrein** 

> **Naam objecttype** BENOEMD TERREIN 

> **Mnemonic objecttype** BTR 

> **Herkomst objecttype** Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

> **Definitie objecttype** Een STANDPLAATS, LIGPLAATS, of een OVERIG TERREIN 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Een benoemd terrein is de groepering van de authentieke stand- en ligplaatsen en de overige terreinen en modelleert daarmee de terreinen op het niveau van stand- en ligplaatsen en daarmee vergelijkbare onbe- en ongebouwde objecten voor zover dat door de gemeente als relevant wordt gezien. Het gaat daarbij om terreinen met een verblijfsfunctie, naar analogie van de stand- en ligplaatsen, zijnde geen stand- en ligplaatsen en waarvan de vindbaarheid in het maatschappelijk verkeer op basis van een officieel adres dringend gewenst is. De minimale verzameling is die van de stand- en ligplaatsen; een gemeente kan daaraan toevoegen andere (overige) terreinen. Een BENOEMD TERREIN is een specialisatie van BENOEMD OBJECT. 

> **Unieke aanduiding objecttype** Benoemd terrein Identificatie **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|---|
||BAG-gegevens|KING|
||57.01/58.01  Benoemd terrein Identificatie|BAG|
||57.20/58.20  Geometrie|BAG|
||Datum begin geldigheid benoemd terrein|KING|
||Datum einde geldigheid benoemd terrein|KING|
||Benoemd terrein typering|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||Relaties van de generalisatie BENOEMD OBJECT:||
||ligt in BUURT|KING/GFO|
||staat op of heeft ruimtelijke overlap met KADASTRALE||
||ONROERENDE ZAAK|KING/BRK|
||bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
||is hoofdlocatie van VESTIGINGen|KING|
||is nevenlocatie van VESTIGINGen|KING|
||is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.11. Buurt** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

## BUURT 

## BRT 

Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). 

Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. GFO BG 

## 9 april 2007 

Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten. 

Combinarie van de unieke aanduiding van de WIJK waarin de BUURT gelegen is met de Buurtcode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen t** 

**Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|94.99|Buurtcode|GFO BG|
|95.00|Buurtnaam|GFO BG|
||Buurtgeometrie|IMGeo|
|81.20|Datum begin geldigheid buurt|KING|
|81.30|Datum einde geldigheid buurt|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Ligt in|WIJK|GFO|
|Omvat|nul of meer BENOEMDe OBJECTen|KING|
|Omvat|PAND|KING|



## **1.12. Functionaris** 

**Naam objecttype** 

## FUNCTIONARIS 

> **Mnemonic objecttype** (FUN) 

> **Herkomst objecttype** NHR **Definitie objecttype** 

Het verband tussen een NIET-NATUURLIJK PERSOON en één of meerdere RECHTSPERSOONen (NATUURLIJKE OF NIET NATUURLIJKE PERSOONen) die namens de NIET-NATUURLIJK PERSOON als functionaris optreden. 

**Datum opname objecttype Toelichting objecttype** 

9 april 2007 

Iedere niet-natuurlijke persoon heeft functionarissen die namens deze nietnatuurlijke persoon optreden. Dit kunnen zowel natuurlijke personen als andere niet-natuurlijke personen zijn. Concernrelaties zijn bijvoorbeeld functionarisrelaties. 

Het betreft een zogenaamd relatie-objecttype oftewel objecten van dit type kunnen niet zelfstandig bestaan maar alleen in combinatie met objecten van de gerelateerde objecttypen. 

> **Unieke aanduiding objecttype** Combinatie van de unieke aanduiding van de INGESCHREVEN NIETNATUURLIJK PERSOON met het Functionaristype en de unieke aanduiding van de RECHTSPERSOON. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Functionaristype NHR Datum toetreding NHR Datum uittreding NHR 

> **Overzicht relaties** _Relatienaam incl. gerelateerd objecttype Herkomst_ van INGESCHREVEN NIET-NATUURLIJK PERSOON NHR rol wordt vervuld door RECHTSPERSOON NHR 

## **1.13. Gebouwd object** 

> **Naam objecttype** GEBOUWD OBJECT 

> **Mnemonic objecttype** GBO 

> **Herkomst objecttype** Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

> **Definitie objecttype** Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Een gebouwd object is de groepering van de authentieke verblijfsobjecten en de overige gebouwde objecten en modelleert daarmee de gebouwde omgeving op het niveau van het verblijfsobject en daarmee vergelijkbare objecten voor zover dat door de gemeente als relevant wordt gezien. Het gaat daarbij primair om objecten met een verblijfsfunctie, naar analogie van de verblijfsobjecten, zijnde geen verblijfsobjecten en waarvan de vindbaarheid in het maatschappelijk verkeer op basis van een officieel adres dringend gewenst is. De minimale verzameling is die van de verblijfsobjecten; een gemeente kan daaraan toevoegen andere (overige) gebouwde objecten. Een GEBOUWD OBJECT is een specialisatie van BENOEMD OBJECT. 

> **Unieke aanduiding objecttype** Gebouwd object identificatie 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

||||
|---|---|---|
|**Overzicht attributen**|_Code_<br>_Gegevensnaam_|_Herkomst_|
||BAG-gegevens|KING|
||56.01 Gebouwd object identificatie|BAG|
||56.20 Gebouwd object puntgeometrie|BAG|
||56.30 Gebruiksdoel gebouwd object|BAG|
||56.31 Oppervlakte (verblijfs)object|BAG|
||Inwinningswijze oppervlakte|KING|
||Gebouwd object vlakgeometrie|IMGeo|
||94.93<br>Bouwkundige bestemming actueel|GFO BG|
||94.96<br>Bruto inhoud|GFO BG|
||95.11<br>Datum begin geldigheid gebouwd object|KING/GFO|
||96.23<br>Datum einde geldigheid gebouwd object|KING/GFO|
||Gebouwd object typering|KING|
||Status voortgang bouw|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||Relaties van de generalisatie BENOEMD OBJECT:||
||lligt in BUURT|KING/GFO|
||staat op of heeft ruimtelijke overlap met KADASTRALE||
||ONROERENDE ZAAK|KING/BRK|
||bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
||is hoofdlocatie van VESTIGINGen|KING|
||is nevenlocatie van VESTIGINGen|KING|
||is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.14. Gemeente** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

## GEMEENTE 

## GEM 

Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). 

Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet. 

## GFO BG 

## 9 april 2007 

De gemeente fungeert in het model als geo-object. Door de relatie van gemeente met andere objecttypen kan achterhaald worden welke gemeente verantwoordelijk is voor het beheer van de hieraan gerelateerde objecten en gegevens. 

Gemeentecode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|92.10|Gemeentecode|GFO BG|
|09.11|Gemeentenaam|GFO BG|
||Gemeentenaam NEN|KING|
||Gemeentegeometrie|IMGeo|
|81.20|Datum begin geldigheid gemeente|GFO BG|
|81.30|Datum einde geldigheid gemeente|GFO BG|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Omvat|GEMEENTELIJKE OPENBARE RUIMTE|KING|
|Omvat|WIJK|GFO BG|
|Omvat|WOONPLAATS|KING|
|Is overgegaan in GEMEENTE||KING/GFO|



## **1.15. Gemeentelijke Openbare Ruimte** 

**Naam objecttype** 

GEMEENTELIJKE OPENBARE RUIMTE 

> **Mnemonic objecttype** GOR 

> **Herkomst objecttype** Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

> **Definitie objecttype** Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen openbaar gedeelte van het gemeentelijk grondgebied 

> **Herkomst definitie objecttype** KING, o.b.v. catalogus BAG 

> **Datum opname objecttype** 9 april 2007 

**Toelichting objecttype** 

De OPENBARE RUIMTE zoals die gedefinieerd is in de BAG ligt binnen één woonplaats. De hier bedoelde openbare ruimte ligt binnen de gemeente en kan zich derhalve uitstrekken over meerdere woonplaatsen. De openbare ruimte is in de BAG gedefinieerd als benaming; de hier bedoelde openbare ruimte is daarentegen gedefinieerd als geo-object. De geometrie is dan ook één van de gegevenssoorten hetgeen aansluit bij de verplichting om een ‘kaartje’ deel uit te laten maken van het openbare ruimte besluit. Aangezien alle openbare ruimten die deel uit maken van een gemeentelijke openbare ruimte dezelfde gegevens delen, zoals openbare ruimte naam en brondocumentgegevens, zijn deze gegevens gemodelleerd bij GEMEENTELIJKE OPENBARE RUIMTE. 

> **Unieke aanduiding objecttype** Identificatiecode gemeentelijke openbare ruimte 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
|||Identificatiecode gemeentelijke openbare ruimte|KING|
|||BAG-gegevens|KING|
|||11.10 Naam openbare ruimte|BAG|
|||11.11 Indicatie geconstateerde openbare ruimte|BAG|
|||11.16 Type openbare ruimte|BAG|
|||11.19 Status openbare ruimte|BAG|
|||Geometrie gemeentelijke openbare ruimte|IMGeo|
|||Datum begin geldigheid Gemeentelijke||
|||Openbare Ruimte|KING|
|||Datum einde geldigheid Gemeentelijke||
|||Openbare Ruimte|KING|
||11.10|Straatnaam|GFO BG|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||ligt in|GEMEENTE|KING|
||Heeft|OPENBARE RUIMTE|KING|



## **1.16. Huishouden** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## HUISHOUDEN 

## HHD 

Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). 

Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS. o.b.v. GFO-BG 

## 9 april 2007 

## (overgenomen uit het GFO-BG) 

Het gaat om de feitelijke leefvorm. Globaal zijn huishoudens in twee groepen te verdelen: de institutionele bevolking en particuliere huishoudens. Een institutioneel huishouden bestaat uit personen die langer dan een jaar in een instelling verblijven, zoals verpleeg-, bejaarden- en kindertehuizen, opvoedingsinternaten, revalidatiecentra en gevangenissen. Particuliere huishoudens bestaan uit een of meer personen die alleen of samen in een woonruimte zijn gehuisvest en zelf in hun dagelijkse onderhoud voorzien (definities van Institutioneel huishouden en Particulier huishouden zijn overgenomen van het CBS, Huishoudensprognose 1996). 

In de definitie van Huishouden zijn de gemeenschappelijke ingrediënten aangegeven die in wetgeving op specifieke terreinen voorkomt: duurzaam, verzameling van personen, binnen één adresseerbaar object. Afhankelijk van de toepassing (bijstand, huursubsidie, woningbehoefte) is verdere concretisering mogelijk binnen de informatiehuishouding van het desbetreffende beleidsveld. 

Verdergaande afbakeningseisen aan een huishouden moeten nog uitgewerkt worden. De mate van duurzaamheid kan voor een particulier huishouden bijvoorbeeld als volgt nader worden gedefinieerd: de personen bewonen het object meer dan 180 dagen in een aaneengesloten periode van 360 dagen. Met het oog op de invoering van de Basisregistratie WOZ ligt het in de lijn, vanwege onderhoudbaarheid van de gegevens, zoveel mogelijk aan te sluiten bij de WOZ-object-afbakening. 

De verblijfsrelaties van ingeschreven personen op adresseerbare objecten zijn in zekere zin een dubbelling met de relaties via huishouden. Voor het separaat modellen van deze relaties is gekozen aangezien het huishouden geen verplicht gegeven is, bij het wijzigen van verblijfsrelaties niet altijd direct de nieuwe huishoudensamenstelling bekend is en de eerstgenoemde relatie deel uit maakt van het stelsel van basisregistraties en één van de meest gevraagde relaties is. 

**Unieke aanduiding objecttype** 

Huishoudennummer 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ 96.28 Huishoudennummer GFO-BG 94.69 Huishoudensoort GFO-BG 96.07 Huishoudengrootte GFO-BG 

||Datum begin geldigheid huishouden|KING|
|---|---|---|
||Datum einde geldigheid huishouden|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||is gehuisvest in VERBLIJFSOBJECT|KING/GFO|
||is gehuisvest op LIGPLAATS|KING/GFO|
||is gehuisvest op STANDPLAATS|KING/GFO|
||heeft  HUISHOUDENRELATIES|KING/GFO|



## **1.17. Huishoudenrelatie** 

**Naam objecttype** 

Huishoudenrelatie 

> **Mnemonic objecttype** (HHR) 

> **Herkomst objecttype** GFO BG **Definitie objecttype** 

> **Definitie objecttype** De relatie van de INGESCHRVEN PERSOON tot het HUISHOUDEN 

> **Herkomst definitie objecttype** GFO BG 

> **Datum opname objecttype** 1 november 2008 

## **Toelichting objecttype** 

> **Unieke aanduiding objecttype** Combinatie van de unieke aanduidingen van de gerelateerde INGESCHRVEN PERSOON en HUISHOUDEN 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen Overzicht relaties** 

_Code Gegevensnaam Herkomst_ 96.32 Huishoudenrelatiecode GFO _Relatienaam incl. gerelateerd objecttype Herkomst_ betreft INGESCHREVEN PERSOON KING/GFO hoort bij HUISHOUDEN KING/GFO 

## **1.18. Huwelijk/geregistreerd partnerschap** 

**Naam objecttype** 

HUWELIJK/GEREGISTREERD PARTNERSCHAP 

**Mnemonic objecttype Herkomst objecttype** 

HUW 

GFO 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

**Unieke aanduiding objecttype** 

Gegevens over een huwelijk/geregistreerd partnerschap van de ingeschreven persoon. 

KING op basis van GFO 

9 april 2007 

Het betreft de modellering van categorie 05 () in de GBA. Het gaat telkens om een huwelijk of geregistreerd partnerschip tussen twee ingeschreven personen. 

- De combinatie van de unieke aanduidingen van de beide INGESCHREVEN PERSOONen waarnaar de relatie HUWELIJK/GEREGISTREERD PARTNERSCHAP betreft twee INGESCHREVEN PERSOONen verwijst. 

**Populatie objecttype** 

**Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|||||
|---|---|---|---|
|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
||05.15.10|Soort verbintenis|GBA|
||05.06|Huwelijkssluiting/aangaan geregistreerd partnerschap|GBA|
|||05.06.10 Datum huwelijkssluiting/aangaan geregistreerd||
||partnerschap||GBA|
|||05.06.20 Plaats huwelijkssluiting/aangaan geregistreerd||
||partnerschap||GBA|
||||GBA|
||05.07|Ontbinding huwelijk/geregistreerd partnerschap|GBA|
|||05.07.10 Datum ontbinding huwelijk/geregistreerd partnerschap||
||||GBA|
|||05.07.20 Plaats ontbinding huwelijk/geregistreerd partnerschap||
||||GBA|
|||05.07.40 Reden ontbinding huwelijk/geregistreerd partnerschap||
||||GBA|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||Betreft twee INGESCHREVEN PERSOONen||KING/GBA|
||05.06|Huwelijkssluiting/aangaan geregistreerd partnerschap||
|||05.06.30 is gesloten/aangegaan in LAND|KING/GBA|
||05.07|Ontbinding huwelijk/geregistreerd partnerschap||
|||05.07.30 is ontbonden in LAND|KING/GBA|



## **1.19. Ingeschreven niet-natuurlijk persoon** 

**Naam objecttype** 

INGESCHREVEN NIET-NATUURLIJK PERSOON 

**Mnemonic objecttype Herkomst objecttype** 

INN 

NHR 

## **Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype Overzicht attributen** 

**Overzicht relaties** 

Een rechtspersoon of een samenwerkingsverband van natuurlijke personen, niet-natuurlijke personen en/of van andere samenwerkingsverbanden die ingeschreven is in het NHR. 

9 april 2007 

Het gaat hier om niet-natuurlijke personen met één of meer vestigingen in Nederland die ingeschreven zijn in het NHR. 

De SUBJECT.Subjecttypering gevolgd door de NNP-ID 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||NNP-ID|NHR|
||Rechtsvorm|NHR|
||Statutaire zetel|NHR|
||Datum voortzetting|NHR|
|Attributen van de generalisatie NIET-NATUURLIJK PERSOON:|||
||(Statutaire) Naam|NHR|
||Datum aanvang|NHR|
||Datum beëindiging|NHR|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Heeft|FUNCTIONARIS|NHR|



Relaties van de generalisatie NIET-NATUURLIJK PERSOON: Heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING NHR Is vereniging van eigenaars bij appartementencomplex met APPARTEMENTSRECHTen BRK 

|Relaties van de generalisatie RECHTSPERSOON:||
|---|---|
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.20. Ingeschreven persoon** 

**Naam objecttype** 

INGESCHREVEN PERSOON 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype Populatie objecttype** 

INP 

Door KING toegevoegd objecttype. 

Een INGEZETENE of NIET-INGEZETENE 

## KING 

9 april 2007 

Het betreft de verzameling van personen, ingeschreven in de GBA (ingezetenen) en het RNI (niet-ingezetene), woonachtig in de gemeente dan wel elders en van belang voor de gemeentelijke taakuitoefening. Een INGESCHREVEN PERSOON  is een specialisatie (‘deelverzameling’) van NATUURLIJK PERSOON. 

De SUBJECT.Subjecttypering gevolgd door het Burgerservicenummer. 

**Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|01|Natuurlijk persoon . Persoonsgegevens|GBA|
||01.01 Identificatienummers|GBA|
||01.01.20 Burgerservicenummer|GBA|
||01.01.10 A-nummer|GBA|
||01.03 Natuurlijk persoon . Persoonsgegevens Geboorte     GBA||
||01.03.20 Geboorteplaats|GBA|
|06|Natuuurlijk persoon . Overlijden|GBA|
||06.08.20 Overlijdenplaats|GBA|
|04|Nationaliteit|GBA|
||04.63.10 Reden verkrijging Nederlandse nat.|GBA|
||04.64.10 Reden verlies Nederlandse nat.|GBA|
||04.65.10 Aanduiding bijzonder Nederlandrschap|GBA|
||Datum verkrijging nationaliteit|KING|
||Datum verlies nationaliteit|KING|
|08|Verblijfplaats|GBA|
||08.09.10 Gemeente van inschrijving|GBA|
||08.12 Woonadreslocatie|GBA/KING|
||08.12.10 Locatiebeschrijving|GBA|
||08.10.10 Adresherkomst|KING/GBA|
||Datum begin geldigheid verblijfplaats|KING|
|09.20|Datum inschrijving in gemeente|GFO-BG|
|14.20|Datum vestiging in Nederland|GFO|
|13.20|Datum vertrek uit Nederland|GFO|
|07|Inschrijving|GBA|
||07.67.20 Reden opschorting bijhouding|GBA|
||07.70.10 Indicatie geheim|GBA|
|67.10|Datum opschorting bijhouding|GFO-BG|
|12.35|Reisdocument|GBA|
||12.36.10 Signalering reisdocument|GBA|
||12.37.10 Buitenlands reisdocument|GBA|
|94.98|Burgerlijke staat|GFO-BG|



||Attributen van de generalisatie NATUURLIJK PERSOON:|Attributen van de generalisatie NATUURLIJK PERSOON:||
|---|---|---|---|
||01|Persoonsgegevens|GBA|
|||01.02 Naam|GBA|
|||01.02.10 Voornamen|GBA|
|||01.02.20  Adellijke titel/predikaat|GBA|
|||01.02.30  Voorvoegsels geslachtsnaam|GBA|
|||01.02.40 Geslachtsnaam|GBA|
|||01.04.10 Geslachtsaanduiding|GBA|
|||01.61.10 Aanduiding naamgebruik|GBA|
|||01.03 Geboorte|GBA|
|||01.03.10  Geboortedatum|GBA|
||Naam aanschrijving||KING|
|||Aanhef aanschrijving|KING|
|||Voorletters aanschrijving|KING|
|||Voornamen aanschrijving|KING|
|||Geslachtsnaam aanschrijving|KING|
||06|Overlijden|GBA|
|||06.08.10 Overlijdensdatum|GBA|
||Attributen van de generalisatie SUBJECT:|||
|||Postadres|KING|
|||Postadrestype|KING|
|||Postbus- of antwoordnummer|KING/GFO|
|||Postadres postcode|KING|
||08.13|Verblijf buitenland|KING/GBA|
|||08.13.30 Adres buitenland 1|KING/GBA|
|||08.13.40 Adres buitenland 2|KING/GBA|
|||08.13.50 Adres buitenland 3|KING/GBA|
||95.80|Telefoonnummer|GFO BG|
||95.27|Fax-nummer|GFO BG|
||95.16|Emailadres|GFO BG|
|||Website-URL|KING|
||94.87|Bank/girorekeningnummer|GFO BG|
|||Subjecttypering|KING|
|||Naam|KING|
|||Identificatie|KING|
|||Adres binnenland|KING|
|||Adres buitenland|KING|
|||KvK-nummer|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||04|Nationaliteit|GBA|
|||04.05.10   heeft NATIONALITEIT|GBA|
||08|Verblijfplaats|GBA|
|||08.11.80 Verblijft in VERBLIJFSOBJECT|GBA|
|||08.11.80 Verblijft op LIGPLAATS|GBA|
|||08.11.80 Verblijft op STANDPLAATS|GBA|
|||08.11.90 Is ingeschreven op NUMMERAANDUIDING|GBA|
|||08.12 Woonadreslocatie|GBA|
|||verblijft op locatie in WOONPLAATS|GBA|
|||08.13.10 is vertrokken naar LAND|GBA|
|||08.14.10 is ingeschreven vanuit LAND|GBA|
||12.35  Reisdocument|||



|is houder van REISDOCUMENT|GBA/KING|
|---|---|
|is bijgeschreven in REISDOCUMENT|GBA/KING|
|Is kind in OUDER-KIND-RELATIEs|GBA/KING|
|Is ouder in OUDER-KINDRELATIEs|GBA/KING|
|Is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen||
||GBA/KING|
|heeft HUISHOUDENRELATIE|GFO BG|
|01<br>Natuurlijk persoon . Persoonsgegevens|GBA|
|01.03 Natuurlijk persoon . Persoonsgegevens . Geboorte     GBA||
|is geboren in LAND|GBA/KING|
|06<br>Natuurlijk persoon . Overlijden|GBA|
|Is overleden in LAND|GBA/KING|
|Relaties van de generalisatie NATUURLIJK PERSOON:||
|Heeft ACADEMISCHE TITEL|GFO BG|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.21. Ingezetene** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype Populatie objecttype** 

## INGEZETENE 

## ING 

GBA (aldaar PERSOON genoemd) 

Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister. 

o.b.v. GFO-BG (o.b.v. NEN 1888, december 1991) 

9 april 2007 

Het betreft hier de personen die deel uitmaken van de GBA als onderdeel van de BasisRegistratie Personen, aldaar aangeduid met cq. gemodelleerd als persoon. 

Zie INGESCHREVEN PERSOON 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|13|Kiesrecht|GBA|
||13.31.10 Aanduiding Europees kiesrecht|GBA|
||13.38.10  Aanduiding uitgesloten kiesrecht|GBA|
|11|Gezagsverhouding|GBA|
||11.32.10 Indicatie gezag minderjarige|GBA|
||11.33.10 Indicatie curateleregister|GBA|
|96.30|Datum verkrijging verblijfstitel|GFO-BG|
|39.20|Datum verlies verblijfstitel|GFO-BG|
|07|Ingeschreven persoon . Inschrijving||
||07.66 Indicatie blokkering|GBA/KING|
|Attributen|van de generalisatie INGESCHREVEN PERSOON:||
|01|Natuurlijk persoon . Persoonsgegevens|GBA|
||01.01 Identificatienummers|GBA|
||01.01.20 Burgerservicenummer|GBA|
||01.01.10 A-nummer|GBA|
||01.03 Natuurlijk persoon . Persoonsgegevens Geboorte     GBA||
||01.03.20 Geboorteplaats|GBA|
|06|Natuuurlijk persoon . Overlijden|GBA|
||06.08.20 Overlijdenplaats|GBA|
|04|Nationaliteit|GBA|
||04.63.10 Reden verkrijging Nederlandse nat.|GBA|
||04.64.10 Reden verlies Nederlandse nat.|GBA|
||04.65.10 Aanduiding bijzonder Nederlandrschap|GBA|
||Datum verkrijging nationaliteit|KING|
||Datum verlies nationaliteit|KING|
|08|Verblijfplaats|GBA|
||08.09.10 Gemeente van inschrijving|GBA|
||08.12 Woonadreslocatie|GBA/KING|
||08.12.10 Locatiebeschrijving|GBA|
||08.10.10 Adresherkomst|KING/GBA|
||Datum begin geldigheid verblijfplaats|KING|



|09.20|Datum inschrijving in gemeente|GFO-BG|
|---|---|---|
|14.20|Datum vestiging in Nederland|GFO|
|13.20|Datum vertrek uit Nederland|GFO|
|07|Inschrijving|GBA|
||07.67.20 Reden opschorting bijhouding|GBA|
||07.70.10 Indicatie geheim|GBA|
|67.10|Datum opschorting bijhouding|GFO-BG|
|12.35|Reisdocument|GBA|
||12.36.10 Signalering reisdocument|GBA|
||12.37.10 Buitenlands reisdocument|GBA|
|94.98|Burgerlijke staat|GFO-BG|
|Attributen van de generalisatie NATUURLIJK PERSOON:|||
|01|Persoonsgegevens|GBA|
||01.02 Naam|GBA|
||01.02.10 Voornamen|GBA|
||01.02.20  Adellijke titel/predikaat|GBA|
||01.02.30  Voorvoegsels geslachtsnaam|GBA|
||01.02.40 Geslachtsnaam|GBA|
||01.04.10 Geslachtsaanduiding|GBA|
||01.61.10 Aanduiding naamgebruik|GBA|
||01.03 Geboorte|GBA|
||01.03.10  Geboortedatum|GBA|
|Naam aanschrijving||KING|
||Aanhef aanschrijving|KING|
||Voorletters aanschrijving|KING|
||Voornamen aanschrijving|KING|
||Geslachtsnaam aanschrijving|KING|
|06|Overlijden|GBA|
||06.08.10 Overlijdensdatum|GBA|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|heeft VERBLIJFSTITEL||KING/GFO|



|Relaties van de generalisatie INGESCHREVEN PERSOON:||
|---|---|
|04<br>Nationaliteit|GBA|
|04.05.10   heeft NATIONALITEIT|GBA|
|08<br>Verblijfplaats|GBA|
|08.11.80 Verblijft in VERBLIJFSOBJECT|GBA|
|08.11.80 Verblijft op LIGPLAATS|GBA|
|08.11.80 Verblijft op STANDPLAATS|GBA|
|08.11.90 Is ingeschreven op NUMMERAANDUIDING GBA||
|08.12 Woonadreslocatie|GBA|
|verblijft op locatie in WOONPLAATS|GBA|
|08.13.10 is vertrokken naar LAND|GBA|
|08.14.10 is ingeschreven vanuit LAND|GBA|
|12.35  Reisdocument||
|is houder van REISDOCUMENT|GBA/KING|
|is bijgeschreven in REISDOCUMENT|GBA/KING|
|Is kind in OUDER-KIND-RELATIEs|GBA/KING|
|Is ouder in OUDER-KINDRELATIEs|GBA/KING|
|Is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen||
||GBA/KING|
|heeft HUISHOUDENRELATIE|GFO BG|
|01<br>Natuurlijk persoon . Persoonsgegevens|GBA|
|01.03 Natuurlijk persoon . Persoonsgegevens . Geboorte     GBA||
|is geboren in LAND|GBA/KING|
|06<br>Natuurlijk persoon . Overlijden|GBA|
|Is overleden in LAND|GBA/KING|
|Relaties van de generalisatie NATUURLIJK PERSOON:||
|Heeft ACADEMISCHE TITEL|GFO BG|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.22. Inrichtingselement** 

> **Naam objecttype** INRICHTINGSELEMENT 

> **Mnemonic objecttype** IRE 

> **Herkomst objecttype** IMGeo 

> **Definitie objecttype** Een ruimtelijk object al dan niet ter detaillering dan wel ter inrichting van de overige benoemde ruimtelijke objecten of een ander inrichtingselement. 

> **Herkomst definitie objecttype** IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een INRICHTINGSELEMENT is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. In het voorliggende model zijn de subklassen van INRICHTINGSELEMENT niet als afzonderlijke objecttypen gemodelleerd. De subklasse is te herkennen aan de attribuutsoort ‘Inrichtingselementtype’. 

**Unieke aanduiding objecttype Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
|||Inrichtingselementtype|KING|
|||Identificatie inrichtingselement|IMGeo|
|||Status inrichtingselement|IMGeo|
|||Naam inrichtingselement|IMGeo|
|||Geometrie inrichtingselement|IMGeo|
|||Relatieve hoogteligging inrichtingselement|IMGeo|
|||Datum begin geldigheid inrichtingselement|IMGeo|
|||Datum einde geldigheid inrichtingselement|IMGeo|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||-|||



## **1.23. Kadastrale gemeente** 

**Naam objecttype** 

KADASTRALE GEMEENTE 

> **Mnemonic objecttype** (KDG) 

> **Herkomst objecttype** BRK 

## **Code objecttype** 

**Definitie objecttype** 

Een gedeelte van het grondgebied van Nederland, volgens de Dienst van het Kadaster en de Openbare Registers, zoals nader omschreven in het Kadasterbesluit 

> **Herkomst definitie objecttype** KING 

**Datum opname objecttype** 

1 maart 2009 

**Toelichting objecttype** 

**Unieke aanduiding objecttype** 

Het betreft een zgn. tabel-objecttype, afgeleid van de kadastrale gemeente tabel in de BRK (IMKAD). 

Kadastrale gemeentecode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Kadastrale gemeentecode|BRK|
||Kadastrale gemeentenaam|BRK|
||Indicatie vervallen|BRK|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|heeft|KADASTRALE ONROERENDE ZAAKen|KING/BRK|



## **1.24. Kadastrale onroerende zaak** 

**Naam objecttype** 

## KADASTRALE ONROERENDE ZAAK 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## KOZ 

BRK 

Een geregistreerd goed waarvoor bij overdracht of vestiging van rechten inschrijving in de openbare registers van het Kadaster is vereist zijnde een KADASTRAAL PERCEEL of een APPARTEMENTSRECHT. 

KING O.B.V. BRK 

## 9 april 2007 

Zie de concept catalogus BRK. Daarin is sprake van een ‘onroerende zaak’ zijnde een ‘perceel’, ‘appartementsrecht’ of ‘leidingnetwerk’. Geoordeeld is dat alleen de eerste twee objecttypen zodanig van belang zijn voor de gemeentelijke taakuitoefening dat zij deel moeten uit maken van het voorliggende referentiemodel. Zij zijn hierin gezamenlijk gemodelleerd als KADASTRALE ONROERENDE ZAAK. 

In de BRK wordt de Kadaster identificatie onroerende zaak (hier: Kadastrale identificatie) als unieke aanduiding beschouwd Aangezien de gegevenslevering door het Kadaster hier nog niet op aangepast is hanteren we vooralsnog de Kadastrale aanduiding als unieke identificatie. Deze Kadastrale aanduiding is een groepattribuutsoort.  Naast de hieronder vermelde attribuutsoorten maken daarvan tevens deel uit de attribuutsoort Deelperceelnummer van de specialisatie KADASTRAAL PERCEEL en de attribuutsoort Appartementsindex van de specialisatie APPARTEMENTSRECHT. 

In de BRK wordt een relatie naar het adresseerbaar object (verblijfsobject, standplaats of ligplaats) onderkend teneinde via een adres (nummeraanduiding) een kadastraal object te kunnen lokaliseren. Vanwege de uitbreiding in dit model naar gebouwde objecten en benoemde terreinen is deze relatie naar deze beide laatstgenoemde objecttypen gelegd. Niet alle kadastrale objecten komen qua ligging overeen met een gebouwd object of benoemd terrein. In die gevallen opteert de BRK om voor het aanduiden van de globale ligging gebruik te maken van een dichtbijgelegen adres i.c.m. de aanduiding ‘Bij’ of ‘Tegenover’ dan wel een locatieomschrijving met daarin de beschrijving van de locatie, veelal door middel van een woonplaatsnaam en een straatnaam. Beide wijzen van aanduiden van de locatie zijn hier opgenomen in Locatie-omschrijving zodat de relaties naar gebouwde objecten en benoemde terreinen alleen ruimtelijke relaties tussen de objecten betreffen. 

> **Unieke aanduiding objecttype** Kadastrale identificatie (zolang de gegevensverstrekking door het Kadaster nog niet gebaseerd is op de BRK vormt de Kadastrale aanduiding de unieke aanduiding) 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Kadastrale identificatie BRK Kadastrale aanduiding BRK Kadastrale gemeentecode BRK Sectie BRK Perceelnummer BRK Locatie onroerende zaak BRK Locatie-omschrijving BRK 

**Overzicht relaties** 

|Cultuur bebouwd|BRK|
|---|---|
|Koopsom|BRK|
|Valutasoort|BRK|
|Aard bedrag|BRK|
|Bedrag|BRK|
|Koopjaar|BRK|
|Meer onroerendgoed|BRK|
|Transactiedatum|KING|
|Landinrichtingsrente|BRK|
|Aanduiding aard Liproject|BRK|
|Valutasoort|BRK|
|Aard bedrag|BRK|
|Bedrag|BRK|
|Eindjaar|BRK|
|Cultuur onbebouwd|BRK|
|Aard cultuur onbebouwd|BRK|
|Aard bebouwing|BRK|
|Meer culturen|BRK|
|81.20<br>Datum begin geldigheid kadastrale onroerende zaak|KING/GFO|
|81.30<br>Datum einde geldigheid kadastrale onroerende zaak|KING/GFO|
|Kadastrale onroerende zaak typering|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Ligt in KADASTRALE GEMEENTE|KING/BRK|
|Heeft één of meer ZAKELIJK RECHT|KING/BRK|
|Locatie onroerende zaak||
|Is ondergrond van of heeft ruimtelijke overlap met BENOEMD|OBJECT|
||KING/BRK|
|Is ontstaan uit andere kadastrale onroerende zaak bij||
|KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
|Is overgegaan in andere kadastrale onroerende zaak bij||
|KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
|Is hoofdperceel bij mandelige KADASTRALE ONROERENDE||
|ZAAKen|KING/BRK|
|Heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON|GFO BG|
|Behoort tot WOZ-OBJECT                                                       BRWOZ/KING||
|heeft KADASTRALE  ONROERENDE ZAAK AANTEKENING|BRK/KING|



## **1.25. Kadastrale onroerende zaak aantekening** 

**Naam objecttype** 

Kadastrale onroerende zaak aantekening 

> **Mnemonic objecttype** KZA 

> **Herkomst objecttype** BRK 

> **Definitie objecttype** Aanduiding van het feit, genoemd in een Stuk, dat betrekking heeft op een onroerende zaak en dat gevolgen kan hebben voor de uitoefening van rechten op de onroerende zaak. 

> **Herkomst definitie objecttype** BRK 

> **Datum opname objecttype** 1 november 2008 

> **Toelichting objecttype** Toegevoegd ten opzichte van de BRK is de begindatum. Aangezien een aantekening niet gewijzigd kan worden, bepaalt de begin- en einddatum de materiele historie van alle attribuutsoortensoorten. Deze hebben dan ook materiele historie ‘Nee’ gekregen. Zie verder de catalogus BRK 

> **Unieke aanduiding objecttype** Kadaster identificatie aantekening kadastraal object 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Kadaster identificatie aantekening BRK Aard aantekening kadastraal object BRK Beschrijving aantekening kadastraal object BRK Begindatum aantekening kadastraal object KING Einddatum aantekening kadastraal object BRK Splitsing aantekening kadastraal object BRK 

**Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype Herkomst_ behoort bij KADASTRALE ONROERENDE ZAAK KING/BRK heeft betrokken RECHTSPERSOON KING/BRK 

## **1.26. Kadastrale onroerende zaak historie relatie** 

**Naam objecttype** 

KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

## FIL 

KING o.b.v. GFO BG 

De afstammingsverwantschap van een KADASTRALE ONROERENDE ZAAK, waarmee de historie kan worden nagegaan 

KING o.b.v. GFO BG 

1 mei 2008 

**Toelichting objecttype** 

Het betreft de modellering van de gegevensgroep ‘Onroerende zaak historie’ bij de (Kadastrale) Onroerende zaak in de BRK. Een Onroerende zaak historie geeft de relatie (overgegaan in of ontstaan uit) aan tussen een oude en een nieuwe Onroerende zaak. Ook geeft Onroerende zaak historie de relatie weer tussen appartementsrechten en de desbetreffende in de splitsing betrokken percelen. 

In het GFO BG betrof dit het objecttype ‘Filiatie Kadastraal object’ met de volgende toelichting. Wanneer een deel van een geheel perceel wordt vervreemd, gaat men, in afwachting van de meting over tot het administratief verdelen van het perceel in zogeheten deelpercelen. Om deze delen in een geautomatiseerde registratie te kunnen opslaan dienen aan deze delen unieke nummers te worden toegekend. 

**Unieke aanduiding objecttype** 

**Overzicht attributen** 

## **Overzicht relaties** 

Combinatie van de unieke aanduidingen van de gerelateerde kadastrale onroerende zaken door middel van de relaties ‘KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het ontstaan uit een KADASTRALE ONROERENDE ZAAK’ en ‘KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het overgaan in een KADASTRALE ONROERENDE ZAAK’. 

_Code Gegevensnaam Herkomst_ Overgangsgrootte BRK Aard BRK _Relatienaam incl. gerelateerd objecttype Herkomst_ Betreft het ontstaan uit een KADASTRALE ONROERENDE ZAAK KING/BRK Betreft het overgaan in een KADASTRALE ONROERENDE ZAAK KING/BRK 

## **1.27. Kadastraal perceel** 

**Naam objecttype** 

KADASTRAAL PERCEEL 

> **Mnemonic objecttype** KDP 

> **Herkomst objecttype** Door KING toegevoegd objecttype, ontleend aan de BRK. 

> **Definitie objecttype** Een KADASTRALE ONROERENDE ZAAK, onderkend als een deel van het Nederlands grondgebied van welk deel de Dienst de begrenzing met behulp van landmeetkundige gegevens heeft vastgelegd op grond van gegevens betreffende de rechtstoestand, bestemming en het gebruik en dat door zijn kadastrale aanduiding is gekenmerkt dan wel een gedeelte daarvan. (Definitie is ontleend aan art 1, Kadasterwet). Als onderdeel van het Nederlands grondgebied is het een driedimensionaal ruimtelijk object. 

> **Herkomst definitie objecttype** KING op basis van BRK 

**Herkomst definitie objecttype Datum opname objecttype** 

9 april 2007 

**Toelichting objecttype** 

Een KADASTRAAL PERCEEL  behoort tezamen met het APPARTEMENTSRECHT tot de generalisatie KADASTRALE ONROERENDE ZAAK. 

**Unieke aanduiding objecttype** 

Unieke aanduiding van de KADASTRALE ONROERENDE ZAAK gevolgd door de Kadastrale onroerende zaak.kadastrale onroerende zaak typering en het Deelperceelnummer. 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding||
|||BRK|
||Deelperceelnummer|BRK|
||Plaatscoördinaten perceel|BRK|
||Grootte perceel|BRK|
||Aanduiding soort grootte|BRK|
||Begrenzing perceel|BRK|
||Omschrijving deelperceel|BRK|
|Attributen van de generalisatie KADASTRALE ONROERENDE ZAAK:|||
||Kadastrale identificatie|BRK|
||Kadastrale aanduiding|BRK|
||Kadastrale gemeentecode|BRK|
||Sectie|BRK|
||Perceelnummer|BRK|
||Locatie onroerende zaak|BRK|
||Locatie-omschrijving|BRK|
||Cultuur bebouwd|BRK|
||Koopsom|BRK|
||Valutasoort|BRK|
||Aard bedrag|BRK|
||Bedrag|BRK|
||Koopjaar|BRK|
||Meer onroerendgoed|BRK|
||Transactiedatum|KING|



||Landinrichtingsrente|BRK|
|---|---|---|
||Aanduiding aard Liproject|BRK|
||Valutasoort|BRK|
||Aard bedrag|BRK|
||Bedrag|BRK|
||Eindjaar|BRK|
||Cultuur onbebouwd|BRK|
||Aard cultuur onbebouwd|BRK|
||Aard bebouwing|BRK|
||Meer culturen|BRK|
||81.20<br>Datum begin geldigheid kadastrale onroerende zaak|KING/GFO|
||81.30<br>Datum einde geldigheid kadastrale onroerende zaak|KING/GFO|
||Kadastrale onroerende zaak typering|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||Is ondergrond van  appartementencomplex met||
||APPARTEMENTSRECHTen|BRK|
||ligt binnen KADASTRAAL PERCEEL|KING|
||Relaties van de generalisatie KADASTRALE ONROERENDE ZAAK:||
||Ligt in KADASTRALE GEMEENTE|KING/brk|
||Heeft één of meer ZAKELIJK RECHT|KING/BRK|
||Locatie onroerende zaak||
||Is ondergrond van of heeft ruimtelijke overlap met BENOEMD|OBJECT|
|||KING/BRK|
||Is ontstaan uit andere kadastrale onroerende zaak bij||
||KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
||Is overgegaan in andere kadastrale onroerende zaak bij||
||KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE|KING/BRK|
||Is hoofdperceel bij mandelige KADASTRALE ONROERENDE||
||ZAAKen|KING/BRK|
||Heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON|GFO BG|
||Behoort tot WOZ-OBJECT                                                       BRWOZ/KING||
||heeft KADASTRALE  ONROERENDE ZAAK AANTEKENING|BRK/KING|



## **1.28. Kunstwerkdeel** 

**Naam objecttype** 

## KUNSTWERKDEEL 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype** 

## KWD 

IMGeo 

Een civieltechnisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen en niet bedoeld voor permanent menselijk verblijf. 

IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een KUNSTWERKDEEL is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Type Kunstwerk IMGeo Identificatie kunstwerkdeel IMGeo Status kunstwerkdeel IMGeo Naam kunstwerkdeel IMGeo Geometrie kunstwerkdeel IMGeo Relatieve hoogteligging kunstwerkdeel IMGeo Datum begin geldigheid kunstwerkdeel IMGeo Datum einde geldigheid kunstwerkdeel IMGeo 

## **Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype Herkomst_ 

- 

## **1.29. Land** 

**Naam objecttype** 

LAND 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

LND 

GFO BG 

Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. 

GFO BG 

1 november 2008 

## **Toelichting objecttype** 

> **Unieke aanduiding objecttype** Landcode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|94.10|Landcode|GFO BG|
|95.56|Landnaam|GFO BG|
|81.20|Ingangsdatum land|GFO BG|
|81.30|Einddatum land|GFO BG|
||Landcode ISO|ISO|



## **Overzicht relaties** 

|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|---|---|
|Is deel van verblijf buitenland van SUBJECT|KING|
|waarin is gesloten/aangegaan||
|HUWELIJK/GEREGISTREERD PARTNERSCHAP|KING/GBA|
|waarin is ontbonden||
|HUWELIJK/GEREGISTREERD PARTNERSCHAP|KING/GBA|
|waarin is geboren INGESCHREVEN PERSOON|KING/GBA|
|waarin is overleden INGESCHREVEN PERSOON|KING/GBA|
|vanwaaruit is ingeschreven INGESCHREVEN PERSOON|KING/GBA|
|waarnaar is vertrokken INGESCHREVEN PERSOON|KING/GBA|



## **1.30. Ligplaats** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

## **Overzicht attributen** 

**Overzicht relaties** 

## LIGPLAATS 

## LPL 

## BAG 

Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt vaartuig. 

9 april 2007 

Een ligplaats maakt in de BAG-terminologie deel uit van de groep adresseerbare objecten. Hier maakt het, gezamenlijk met de STANDPLAATS en het OVERIG TERREIN deel uit van de groep BENOEMD TERREIN. 

|TERREIN.||
|---|---|
|_Code_<br>_Gegevensnaam_|_Herkomst_|
|BENOEMD TERREIN . BAG-gegevens|KING|
|57.02  Indicatie geconstateerde ligplaats|BAG|
|57.03  Ligplaatsstatus|BAG|
|Attributen van de generalisatie BENOEMD TERREIN:||
|BAG-gegevens|KING|
|57.01/58.01  Benoemd terrein Identificatie|BAG|
|57.20/58.20  Geometrie|BAG|
|Datum begin geldigheid benoemd terrein|KING|
|Datum einde geldigheid benoemd terrein|KING|
|Benoemd terrein typering|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|BENOEMD TERREIN . BAG-gegevens|KING|
|heeft als hoofdadres NUMMERAANDUIDING|KING/BAG|
|heeft als nevenadressen NUMMERAANDUIDING|KING/BAG|
|heeft daarop verblijvende  INGESCHREVEN PERSOONen|GBA|
|Is huisvesting van HUISHOUDEN|KING|
|Relaties van de generalisatie BENOEMD OBJECT:||
|ligt in BUURT|KING/GFO|
|staat op of heeft ruimtelijke overlap met KADASTRALE||
|ONROERENDE ZAAK|KING/BRK|
|bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
|is hoofdlocatie van VESTIGINGen|KING|
|is nevenlocatie van VESTIGINGen|KING|
|is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.31. Maatschappelijke activiteit** 

**Naam objecttype** 

MAATSCHAPPELIJKE ACTIVITEIT 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Datum opname objecttype** 

MAC 

NHR 

Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit). 9 april 2007 

## **Toelichting objecttype** 

**Unieke aanduiding objecttype Overzicht attributen** 

**Overzicht relaties** 

## KvK-nummer 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||KvK-nummer|NHR|
||Datum aanvang|NHR|
||Datum voortzetting|NHR|
||Datum beëindiging|NHR|
||Handelsnamen|NHR|
||Handelsnaam|NHR|
||Verkorte naam|NHR|
||Volgorde|NHR|
||Activiteiten|NHR|
||Indicatie hoofdactiviteit|NHR|
||Volgorde|NHR|
||Activiteit code|NHR|
||Activiteit|NHR|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Heeft als eigenaar RECHTSPERSOON||NHR|
|Oefent activiteit uit in VESTIGING||NHR|



## **1.32. Nationaliteit** 

**Naam objecttype** 

## NATIONALITEIT 

**Mnemonic objecttype Herkomst objecttype** 

(NAT) 

GFO BG 

## **Code objecttype** 

**Definitie objecttype Herkomst definitie objecttype** GFO BG **Datum opname objecttype** 1 maart 2009 

De hoedanigheid van tot een bepaalde natie te behoren. 

**Toelichting objecttype** 

**Unieke aanduiding objecttype** 

Het betreft een zgn. tabel-objecttype, afgeleid van de nationaliteitentabel in de GBA. 

Nationaliteitcode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
||04.05.10|Nationaliteitcode|GBA|
||95.65|Nationaliteitomschrijving|GFO|
||81.20|Datum begin geldigheid nationaliteit|GFO|
||81.30|Datum einde geldigheid nationaliteit|GFO|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||05.10   hoort bij INGESCHREVEN PERSOON||KING/GFO|



## **1.33. Natuurlijk persoon** 

> **Naam objecttype** NATUURLIJK PERSOON 

> **Mnemonic objecttype** NPS 

> **Herkomst objecttype** Door KING toegevoegd objecttype, ontleend aan het GFO BG. 

> **Definitie objecttype** Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Het betreft de verzameling van personen, ingeschreven in de BasisRegistratie Personen (GBA en RNI), woonachtig in de gemeente dan wel elders en van belang voor de gemeentelijke taakuitoefening (ingezetenen) alsmede andere personen, woonachtig in het binnen- of buitenland, niet ingeschreven in de BRP maar wel van belang voor de gemeentelijke taakuitoefening zoals buitenlanders die bijvoorbeeld belastingplichtig zijn voor een gemeentelijke belasting. NATUURLIJK PERSOON is een specialisatie (‘deelverzameling’) van RECHTSPERSOON. 

**Unieke aanduiding objecttype** 

Zie SUBJECT 

**Populatie objecttype** 

**Kwaliteitsbegrip objecttype Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|01|Persoonsgegevens|GBA|
||01.02 Naam|GBA|
||01.02.10 Voornamen|GBA|
||01.02.20  Adellijke titel/predikaat|GBA|
||01.02.30  Voorvoegsels geslachtsnaam|GBA|
||01.02.40 Geslachtsnaam|GBA|
||01.04.10 Geslachtsaanduiding|GBA|
||01.61.10 Aanduiding naamgebruik|GBA|
||01.03 Geboorte|GBA|
||01.03.10  Geboortedatum|GBA|
|Naam|aanschrijving|KING|
||Aanhef aanschrijving|KING|
||Voorletters aanschrijving|KING|
||Voornamen aanschrijving|KING|
||Geslachtsnaam aanschrijving|KING|
|06|Overlijden|GBA|
||06.08.10 Overlijdensdatum|GBA|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|



**Overzicht relaties** 

|95.80<br>Telefoonnummer|GFO BG|
|---|---|
|95.27<br>Fax-nummer|GFO BG|
|95.16<br>Emailadres|GFO BG|
|Website-URL|KING|
|94.87<br>Bank/girorekeningnummer|GFO BG|
|Subjecttypering|KING|
|Naam|KING|
|Identificatie|KING|
|Adres binnenland|KING|
|Adres buitenland|KING|
|KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Heeft ACADEMISCHE TITEL|GFO BG|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.34. Niet-ingezetene** 

> **Naam objecttype** NIET-INGEZETENE 

> **Mnemonic objecttype** NIN 

> **Herkomst objecttype** RNI 

> **Definitie objecttype** Een individueel menselijk wezen, ingeschreven in het Register NietIngezetenen (RNI). **Herkomst definitie objecttype** 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Het betreft hier de personen die geen deel uitmaken van de GBA maar die om één of andere reden van belang zijn voor de taakuitoefening van de overheid en om die reden ingeschreven zijn in de registratie nietingezetenen. Dit RNI is weliswaar onderkend maar wordt nog niet ingevoerd. 

> **Unieke aanduiding objecttype** Zie INGESCHREVEN PERSOON 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|Attributen van de generalisatie INGESCHREVEN PERSOON:|||
|01|Natuurlijk persoon . Persoonsgegevens|GBA|
||01.01 Identificatienummers|GBA|
||01.01.20 Burgerservicenummer|GBA|
||01.01.10 A-nummer|GBA|
||01.03 Natuurlijk persoon . Persoonsgegevens Geboorte     GBA||
||01.03.20 Geboorteplaats|GBA|
|06|Natuuurlijk persoon . Overlijden|GBA|
||06.08.20 Overlijdenplaats|GBA|
|04|Nationaliteit|GBA|
||04.63.10 Reden verkrijging Nederlandse nat.|GBA|
||04.64.10 Reden verlies Nederlandse nat.|GBA|
||04.65.10 Aanduiding bijzonder Nederlandrschap|GBA|
||Datum verkrijging nationaliteit|KING|
||Datum verlies nationaliteit|KING|
|08|Verblijfplaats|GBA|
||08.09.10 Gemeente van inschrijving|GBA|
||08.12 Woonadreslocatie|GBA/KING|
||08.12.10 Locatiebeschrijving|GBA|
||08.10.10 Adresherkomst|KING/GBA|
||Datum begin geldigheid verblijfplaats|KING|
|09.20|Datum inschrijving in gemeente|GFO-BG|
|14.20|Datum vestiging in Nederland|GFO|
|13.20|Datum vertrek uit Nederland|GFO|
|07|Inschrijving|GBA|
||07.67.20 Reden opschorting bijhouding|GBA|
||07.70.10 Indicatie geheim|GBA|
|67.10|Datum opschorting bijhouding|GFO-BG|
|12.35|Reisdocument|GBA|
||12.36.10 Signalering reisdocument|GBA|



|||12.37.10 Buitenlands reisdocument|GBA|
|---|---|---|---|
||94.98|Burgerlijke staat|GFO-BG|
||Attributen van de generalisatie NATUURLIJK PERSOON:|||
||01|Persoonsgegevens|GBA|
|||01.02 Naam|GBA|
|||01.02.10 Voornamen|GBA|
|||01.02.20  Adellijke titel/predikaat|GBA|
|||01.02.30  Voorvoegsels geslachtsnaam|GBA|
|||01.02.40 Geslachtsnaam|GBA|
|||01.04.10 Geslachtsaanduiding|GBA|
|||01.61.10 Aanduiding naamgebruik|GBA|
|||01.03 Geboorte|GBA|
|||01.03.10  Geboortedatum|GBA|
||Naam aanschrijving||KING|
|||Aanhef aanschrijving|KING|
|||Voorletters aanschrijving|KING|
|||Voornamen aanschrijving|KING|
|||Geslachtsnaam aanschrijving|KING|
||06|Overlijden|GBA|
|||06.08.10 Overlijdensdatum|GBA|
||Attributen van de generalisatie SUBJECT:|||
|||Postadres|KING|
|||Postadrestype|KING|
|||Postbus- of antwoordnummer|KING/GFO|
|||Postadres postcode|KING|
||08.13|Verblijf buitenland|KING/GBA|
|||08.13.30 Adres buitenland 1|KING/GBA|
|||08.13.40 Adres buitenland 2|KING/GBA|
|||08.13.50 Adres buitenland 3|KING/GBA|
||95.80|Telefoonnummer|GFO BG|
||95.27|Fax-nummer|GFO BG|
||95.16|Emailadres|GFO BG|
|||Website-URL|KING|
||94.87|Bank/girorekeningnummer|GFO BG|
|||Subjecttypering|KING|
|||Naam|KING|
|||Identificatie|KING|
|||Adres binnenland|KING|
|||Adres buitenland|KING|
|||KvK-nummer|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||Relaties van de generalisatie INGESCHREVEN PERSOON:|||
||04|Nationaliteit|GBA|
|||04.05.10   heeft NATIONALITEIT|GBA|
||08|Verblijfplaats|GBA|
|||08.11.80 Verblijft in VERBLIJFSOBJECT|GBA|
|||08.11.80 Verblijft op LIGPLAATS|GBA|
|||08.11.80 Verblijft op STANDPLAATS|GBA|
|||08.11.90 Is ingeschreven op NUMMERAANDUIDING|GBA|
|||08.12 Woonadreslocatie|GBA|



|verblijft op locatie in WOONPLAATS|GBA|
|---|---|
|08.13.10 is vertrokken naar LAND|GBA|
|08.14.10 is ingeschreven vanuit LAND|GBA|
|12.35  Reisdocument||
|is houder van REISDOCUMENT|GBA/KING|
|is bijgeschreven in REISDOCUMENT|GBA/KING|
|Is kind in OUDER-KIND-RELATIEs|GBA/KING|
|Is ouder in OUDER-KINDRELATIEs|GBA/KING|
|Is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen||
||GBA/KING|
|heeft HUISHOUDENRELATIE|GFO BG|
|01<br>Natuurlijk persoon . Persoonsgegevens|GBA|
|01.03 Natuurlijk persoon . Persoonsgegevens . Geboorte     GBA||
|is geboren in LAND|GBA/KING|
|06<br>Natuurlijk persoon . Overlijden|GBA|
|Is overleden in LAND|GBA/KING|
|Relaties van de generalisatie NATUURLIJK PERSOON:||
|Heeft ACADEMISCHE TITEL|GFO BG|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.35. Niet-natuurlijk persoon** 

> **Naam objecttype** NIET-NATUURLIJK PERSOON 

> **Mnemonic objecttype** NNP 

> **Herkomst objecttype** KING 

> **Definitie objecttype** Een INGESCHREVEN NIET-NATUURLIJK PERSOON of een ANDER NIET-NATUURLIJK PERSOON 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** In het handelsregister worden natuurlijke personen met één of meer vestigingen in Nederland ingeschreven. De hier bedoelde verzameling nietnatuurlijke personen betreft tevens andere (buitenlandse) niet natuurlijke personen voor zover deze van belang zijn voor het uitoefenen van de gemeentelijke taken, ongeacht of deze een vestiging in Nederland hebben. Zo kan het een buitenlandse niet-natuurlijke persoon betreffen die onroerend goed binnen de gemeentegrens in eigendom heeft en daarover belasting dient te betalen. 

NIET-NATUURLIJK PERSOON is een specialisatie (‘deelverzameling’) van RECHTSPERSOON. 

> **Unieke aanduiding objecttype** Zie SUBJECT 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||(Statutaire) Naam|NHR|
||Datum aanvang|NHR|
||Datum beëindiging|NHR|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|



|Heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING<br>NHR|Heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING<br>NHR|
|---|---|
|Is vereniging van eigenaars bij appartementencomplex||
|met APPARTEMENTSRECHTen|BRK|
|Relaties van de generalisatie RECHTSPERSOON:||
|Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT|KING/NHR|
|Heeft rol als FUNCTIONARIS|KING/NHR|
|Is gerechtigde van ZAKELIJK RECHT|KING/BRK|
|Is betrokken bij KADASTRALE||
|ONROERENDE ZAAK AANTEKENING|KING/BRK|
|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.36. Nummeraanduiding** 

**Naam objecttype** 

NUMMERAANDUIDING 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

NRA 

BAG 

Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. 

**Datum opname objecttype Toelichting objecttype** 

9 april 2007 

||||
|---|---|---|
|**Toelichting objecttype**|Zie de toelichting in de Catalogus BAG. In aanvulling hierop het volgende.||
||Het betreft alle gegevens en relaties van de NUMMERAANDUIDING zoals||
||deze in de BAG gedefinieerd zijn. NUMMERAANDUIDING is gemodelleerd||
||als een specialisatie van ADRESSEERBAAR OBJECT AANDUIDING. Daar||
||bij overige (officieel vastgestelde) adressen deels vergelijkbare gegevens en||
||relaties van toepassing zijn, zijn desbetreffende gegevens gemodelleerd bij||
||ADRESSEERBAAR OBJECT AANDUIDING, de verzameling van||
||nummeraanduidingen en overige adresseerbaar object aanduidingen.||
|**Overzicht attributen**|_Code_<br>_Gegevensnaam_|_Herkomst_|
||ADRESSEERBAAR OBJECT AANDUIDING .BAG-gegevens||
||11.21 Indicatie geconstateerde nummeraanduiding|BAG|
||11.69 Nummeraanduidingstatus|BAG|
||Indicatie hoofdadres|KING|
||Attributen van de generalisatie ADRESSEERBAAR OBJECT AANDUIDING:||
||BAG-gegevens|KING|
||11.02 Identificatiecode adresseerbaar object aanduiding<br>BAG||
||11.20 Huisnummer|BAG|
||11.30 Huisletter|BAG|
||11.40 Huisnummertoevoeging|BAG|
||11.60 Postcode|BAG|
||Datum begin geldigheid adresseerbaar object||
||aanduiding|KING|
||Datum einde geldigheid adresseerbaar object||
||aanduiding|KING|
||Adresseerbaar object aanduiding typering|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||ADRESSEERBAAR OBJECT AANDUIDING .BAG-gegevens|KING|
||Is hoofdadres van VERBLIJFSOBJECT|KING/BAG|
||Is nevenadres van VERBLIJFSOBJECT|KING/BAG|
||Is hoofdadres van LIGPLAATS|KING/BAG|
||Is nevenadres van LIGPLAATS|KING/BAG|
||Is hoofdadres van STANDPLAATS|KING/BAG|
||Is nevenadres van STANDPLAATS|KING/BAG|
||Maakt deel uit van locatie-adres van||
||OVERIG GEBOUWD OBJECT|KING|
||heeft daarop INGESCHREVEN PERSOONen|KING/GBA|



Relaties van de generalisatie ADRESSEERBAAR OBJECT AANDUIDING: 

|Is bezoekadres van ANDER NATUURLIJK PERSOON||
|---|---|
|Is bezoekadres van NIET-NATUURLIJK PERSOON|NHR|
|BAG-gegevens|KING|
|Ligt aan OPENBARE RUIMTE|BAG|
|Ligt in WOONPLAATS|BAG|
|Is correspondentie- of aanschrijvingsadres van SUBJECT|KING/GFO|



## **1.37. Openbare Ruimte** 

**Naam objecttype** 

## OPENBARE RUIMTE 

**Mnemonic objecttype Herkomst objecttype** 

## OPR 

## BAG 

**Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

## **Overzicht attributen** 

**Overzicht relaties** 

Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen 9 april 2007 

Dit betreft het gedeelte van de GEMEENTELIJKE OPENBARE RUIMTE dat binnen één woonplaats gelegen is. Proces- cq. metagegevens worden vastgelegd op het niveau waarop de gemeenteraad het besluit neemt: de openbare ruimte binnen de gemeente. 

|openbare ruimte binnen de gemeente.||
|---|---|
|_Code_<br>_Gegevensnaam_|_Herkomst_|
|BAG-gegevens|KING|
|11.01 Identificatiecode openbare ruimte|BAG|
|Huisnummerrange even nummers|KING|
|Huisnummerrange oneven nummers|KING|
|Huisnummerrange even en oneven nummers|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|BAG-gegevens||
|ligt in WOONPLAATS|BAG|
|maakt deel uit van GEMEENTELIJKE OPENBARE RUIMTE|KING|
|Heeft ADRESSEERBAAR OBJECT AANDUIDING|KING/BAG|
|Maakt deel uit van straatadres van OVERIG GEBOUWD||
|OBJECT|KING|
|heeft nabijgelegen WOZ-OBJECT                                  BRWOZ/KING||



## **1.38. Ouder-kind-relatie** 

**Naam objecttype** 

OUDER-KIND-RELATIE 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

OUD, KND 

KING op basis van GFO 

Het verband tussen een kind en één van zijn of haar juridische ouders. 

KING op basis van GFO 

9 april 2007 

Het betreft de modellering van de categoriën 02 (Ouder 1), 03 (Ouder 2) en 09 (Kind) uit de GBA. 

- De combinatie van de unieke aanduidingen waarnaar verwezen wordt in de relaties OUDER-KIND-RELATIE betreft ouder zijnde INGESCHREVEN PERSOON en OUDER-KIND-RELATIE betreft kind zijnde  INGESCHREVEN PERSOON. 

## **Populatie objecttype** 

**Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

## **Overzicht relaties** 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|02/03 62.10  Datum ingang familierechtelijke betrekking|GBA/KING|
|95.18<br>Datum einde familierechtelijke betrekking|GFO|
|Ouder-aanduiding|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Betreft ouder zijnde INGESCHREVEN PERSOON|KING/GBA|
|Betreft kind zijnde  INGESCHREVEN PERSOON|KING/GBA|



## **1.39. Overige adresseerbaar object aanduiding** 

**Naam objecttype** 

OVERIGE ADRESSEERBAAR OBJECT AANDUIDING 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype Herkomst definitie objecttype Datum opname objecttype** 

## **Toelichting objecttype** 

OAO 

Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

Een door de gemeenteraad als zodanig toegekende aanduiding van een overig gebouwd object of een overig terrein. 

## KING 

## 9 april 2007 

Het betreft alle gegevens en relaties van een officieel vastgesteld adres (van een overig gebouwd object of een overig terrein) zijnde geen NUMMERAANDUIDING zoals deze in de BAG gedefinieerd is. OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is gemodelleerd als een specialisatie van ADRESSEERBAAR OBJECT AANDUIDING. Daar bij NUMMERAANDUIDINGen deels vergelijkbare gegevens en relaties van toepassing zijn, zijn desbetreffende gegevens en relaties gemodelleerd bij ADRESSEERBAAR OBJECT AANDUIDING, de verzameling van nummeraanduidingen en overige adressen. Het OVERIGE ADRESSEERBAAR OBJECT AANDUIDING heeft dientengevolge geen specifieke gegevens, wel is er sprake van specifieke relaties. Van belang is verder dat een specifiek overig adres slechts een adres kan zijn van of een overig gebouwd object of een overig terrein. 

**Unieke aanduiding objecttype** 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|_Herkomst_|
|---|---|---|---|
|Attributen van de generalisatie ADRESSEERBAAR OBJECT AANDUIDING:||||
||BAG-gegevens|KING||
||11.02 Identificatiecode adresseerbaar object aanduiding||BAG|
||11.20 Huisnummer|BAG||
||11.30 Huisletter|BAG||
||11.40 Huisnummertoevoeging|BAG||
||11.60 Postcode|BAG||
||Datum begin geldigheid adresseerbaar object|||
||aanduiding|KING||
||Datum einde geldigheid adresseerbaar object|||
||aanduiding|KING||
||Adresseerbaar object aanduiding typering|KING||



|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|---|---|---|
||Is officieel adres van OVERIG GEBOUWD OBJECT|KING|
||Is officieel adres van OVERIG TERREIN|KING|
||Relaties van de generalisatie ADRESSEERBAAR OBJECT|AANDUIDING:|
||BAG-gegevens||
||Ligt aan OPENBARE RUIMTE|BAG|
||Ligt in WOONPLAATS|BAG|
||Is bezoekadres van NIET-NATUURLIJK PERSOON|NHR|
||Is correspondentie- of aanschrijvingsadres van SUBJECT|KING/GFO|



## **1.40. Overig gebouwd object** 

**Naam objecttype** 

OVERIG GEBOUWD OBJECT 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

## OGO 

Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). 

De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een bij de totstandkoming functioneel en bouwkundig constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden. 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## KING 

## 9 april 2007 

> **Toelichting objecttype** Een overig gebouwd object is een onderdeel van de gebouwde omgeving, bouwtechnisch op het niveau van panden en qua gebruik op het niveau van verblijfsobjecten. Door het registreren van overige gebouwde objecten, in aanvulling op de verblijfsobjecten en panden, verkrijgt de gemeente een – voor zover gewenst – totale registratie van de gebouwde omgeving. Verblijfsobjecten betreffen bouwvergunningplichtige gebouwde objecten waarin verbleven kan worden; overige gebouwde objecten bieden de mogelijkheid ook bouwvergunningplichtige gebouwde objecten te registreren waarin niet verbleven kan worden in de zin van de BAG. Overige gebouwde objecten worden alleen geregistreerd voor zover dat door de gemeente als relevant wordt gezien. Het gaat daarbij primair om objecten met een verblijfsfunctie, naar analogie van de verblijfsobjecten, zijnde geen verblijfsobjecten en waarvan de vindbaarheid in het maatschappelijk verkeer op basis van een officieel adres dringend gewenst is. Dit betreft bijvoorbeeld onbemande benzinestations en niet-afsluitbare parkeergarages. Het staat de gemeente vrij een bredere afbakening te hanteren vanuit het oogpunt van centraal beheer en voor zover de gemeente daarvan adressen wil vaststellen. Dit betreft bijvoorbeeld hoogspanningsmasten, GSMzendmasten en windturbines. Vermeldenswaard is dat bouwvergunningplichtige objecten zonder verblijfsfunctie al als INRICHTINGSELEMENT geregistreerd worden. Essentieel is derhalve dat elk overig gebouwd object voorzien wordt van een (niet-authentiek) adres: een officieel vastgesteld OVERIGE ADRESSEERBAAR OBJECT AANDUIDING, een bestaande NUMMERAANDUIDING aangevuld met een locatie-aanduiding of een bestaande OPENBARE RUIMTE aangevuld met een locatie-aanduiding. Elk overig gebouwd object heeft dus precies één van de drie genoemde relaties waarmee het voorzien is van een adres. **Unieke aanduiding objecttype Populatie objecttype Kwaliteitsbegrip objecttype** 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Overig gebouwd object locatie-aanduiding KING 95.83 Overig gebouwd object type KING/GFO 61.20 Bouwjaar KING/WOZ Attributen van de generalisatie GEBOUWD OBJECT: 

## **Overzicht relaties** 

|BAG-gegevens|KING|
|---|---|
|56.01 Gebouwd object identificatie|BAG|
|56.20 Gebouwd object puntgeometrie|BAG|
|56.30 Gebruiksdoel gebouwd object|BAG|
|56.31 Oppervlakte (verblijfs)object|BAG|
|Inwinningswijze oppervlakte|KING|
|Gebouwd object vlakgeometrie|IMGeo|
|94.93<br>Bouwkundige bestemming actueel|GFO BG|
|94.96<br>Bruto inhoud|GFO BG|
|95.11<br>Datum begin geldigheid gebouwd object|KING/GFO|
|96.23<br>Datum einde geldigheid gebouwd object|KING/GFO|
|Gebouwd object typering|KING|
|Status voortgang bouw|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Heeft als officieel adres OVERIGE ADRESSEERBAAR||
|OBJECT AANDUIDING|KING|
|Heeft locatie-adres i.c.m. NUMMERAANDUIDING|KING|
|heeft straatadres i.c.m. OPENBARE RUIMTE|KING|
|Relaties van de generalisatie BENOEMD OBJECT:||
|lligt in BUURT|KING/GFO|
|staat op of heeft ruimtelijke overlap met KADASTRALE||
|ONROERENDE ZAAK|KING/BRK|
|bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
|is hoofdlocatie van VESTIGINGen|KING|
|is nevenlocatie van VESTIGINGen|KING|
|is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.41. Overig Terrein** 

|**Naam objecttype**|OVERIG TERREIN||
|---|---|---|
|**Mnemonic objecttype**|OTR||
|**Herkomst objecttype**|Door KING toegevoegd objecttype (maakt geen deel uit van enige||
||basisregistratie).||
|**Definitie objecttype**|Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen||
||onbebouwd terrein of een gedeelte daarvan, geen standplaats of gedeelte||
||van een ligplaats zijnde, dat bestemd is voor het gedurende langere tijd||
||verrichten van een maatschappelijke activiteit.||
|**Herkomst definitie objecttype**|KING||
|**Datum opname objecttype**|9 april 2007||
|**Toelichting objecttype**|Een overig terrein is bedoeld om, naast stand- en ligplaatsen, terreinen te||
||kunnen registreren waaraan de gemeente een weliswaar|officieel maar niet-|
||authentiek adres wil toekennen. Het gaat om terreinen zoals autosloperijen,||
||volkstuincomplexen en sportvelden (zonder opstallen).||
||Overige terreinen worden alleen geregistreerd voor zover|dat door de|
||gemeente als relevant wordt gezien. Het gaat daarbij om terreinen met een||
||verblijfsfunctie, naar analogie van de stand- en ligplaatsen, zijnde geen||
||stand- en ligplaatsen en waarvan de vindbaarheid in het maatschappelijk||
||verkeer op basis van een officieel adres dringend gewenst is.||
|**Unieke aanduiding objecttype**|Zie BENOEMD TERREIN||
|**Populatie objecttype**|||
|**Kwaliteitsbegrip objecttype**|||
|**Overzicht attributen**|_Code_<br>_Gegevensnaam_|_Herkomst_|
||Gebruiksdoel overig terrein|KING|
||Attributen van de generalisatie BENOEMD TERREIN:||
||BAG-gegevens|KING|
||57.01/58.01  Benoemd terrein Identificatie|BAG|
||57.20/58.20  Geometrie|BAG|
||Datum begin geldigheid benoemd terrein|KING|
||Datum einde geldigheid benoemd terrein|KING|
||Benoemd terrein typering|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||Heeft als officieel adres OVERIGE ADRESSEERBAAR||
||OBJECT AANDUIDING|KING|
||Relaties van de generalisatie BENOEMD OBJECT:||
||ligt in BUURT|KING/GFO|
||staat op of heeft ruimtelijke overlap met KADASTRALE||
||ONROERENDE ZAAK|KING/BRK|
||bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
||is hoofdlocatie van VESTIGINGen|KING|
||is nevenlocatie van VESTIGINGen|KING|
||is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.42. Pand** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

## PAND 

PND 

## BAG 

De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. 

9 april 2007 

Zie de catalogus BAG. 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||BAG-gegevens|KING|
||55.01 Pandidentificatie|BAG|
||55.02 Indicatie geconstateerd pand|BAG|
||55.20 Pandgeometrie bovenaanzicht|BAG|
||55.30 Oorspronkelijk bouwjaar pand|BAG|
||55.31 Pandstatus|BAG|
||Inwinningswijze geometrie bovenaanzicht|KING|
||Pandgeometrie maaiveld|IMGeo|
||Inwinningswijze geometrie maaiveld|KING|
|95.53|Laagste bouwlaag pand|GFO BG|
|95.32|Hoogste bouwlaag pand|GFO BG|
||Relatieve hoogteligging pand|IMGeo|
||Datum begin geldigheid pand|KING|
||Datum einde geldigheid pand|KING|
||Status voortgang bouw|KING|
|56.31|Oppervlakte pand|KING|
|94.96|Bruto inhoud pand|GFO BG|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|BAG-gegevens|||
|Heeft|inliggend VERBLIJFSOBJECT|BAG|
|Zonder verblijfsobject ligt in BUURT||KING|
|Bestaat|uit WOZ-DEELOBJECTen|KING|



## **1.43. Rechtspersoon** 

**Naam objecttype Mnemonic objecttype Herkomst objecttype Definitie objecttype Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

## RECHTSPERSOON 

## RPS 

Door KING toegevoegd objecttype 

Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON 

## KING 

1 mei 2008 

Het betreft de verzameling van alle natuurlijke en niet-natuurlijke personen waarvan het gegevensbeheer van essentieel belang is voor de uitoefening van de gemeentelijke taken. Overigens beschouwd het NHR niet alle Nietnatuurlijke personen als rechtspersonen. Samenwerkingsverbanden vormen een deelverzameling van Niet-natuurlijk persoon maar zijn in formele zin geen rechtspersonen. Om wille van de eenvoud scharen we deze personen hier wel onder de term rechtspersoon. Het is een specialisatie cq. deelverzameling van SUBJECT. Zie SUBJECT. 

**Populatie objecttype** 

De minimale verzameling betreft de ingezetenen zijnde de inwoners van de gemeente en de in de gemeente gevestigde niet-natuurlijke personen. 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
||Attributen van de generalisatie SUBJECT:|||
|||Postadres|KING|
|||Postadrestype|KING|
|||Postbus- of antwoordnummer|KING/GFO|
|||Postadres postcode|KING|
||08.13|Verblijf buitenland|KING/GBA|
|||08.13.30 Adres buitenland 1|KING/GBA|
|||08.13.40 Adres buitenland 2|KING/GBA|
|||08.13.50 Adres buitenland 3|KING/GBA|
||95.80|Telefoonnummer|GFO BG|
||95.27|Fax-nummer|GFO BG|
||95.16|Emailadres|GFO BG|
|||Website-URL|KING|
||94.87|Bank/girorekeningnummer|GFO BG|
|||Subjecttypering|KING|
|||Naam|KING|
|||Identificatie|KING|
|||Adres binnenland|KING|
|||Adres buitenland|KING|
|||KvK-nummer|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||Is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT||KING/NHR|
||Heeft|rol als FUNCTIONARIS|KING/NHR|
||Is gerechtigde van ZAKELIJK RECHT||KING/BRK|
||Is betrokken bij KADASTRALE|||
||ONROERENDE ZAAK AANTEKENING||KING/BRK|



|Is betrokken bij ZAKELIJK RECHT AANTEKENING|KING/BRK|
|---|---|
|Is voornaamste zakelijk gerechtigde van KADASTRALE||
|ONROERENDE ZAAK|GFO BG|
|Relaties van de generalisatie SUBJECT:||
|Heeft als correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.44. Reisdocument** 

**Naam objecttype** 

## REISDOCUMENT 

> **Mnemonic objecttype** RSD **Herkomst objecttype Definitie objecttype** 

Door KING toegevoegd objecttype o.b.v. GFO BG. 

Een document dat men op reis nodig heeft. 

> **Herkomst definitie objecttype** KING 

> **Datum opname objecttype** 1 mei 2008 

**Toelichting objecttype** 

**Unieke aanduiding objecttype** 

Het is de modellering van categorie 12 uit het LO GBA 3.6. en het Persoonlijk identiteitsbewijs uit het GFO BG. Het kan bijvoorbeeld een paspoort of visum betreffen. Meerdere ingeschreven personen kunnen aan een reisdocument gerelateerd zijn. Aan degene met de langst geleden geboortedatum is het reisdocument verstrekt. De overige personen zijn daarin bijgeschreven. 

Reisdocumentsoort, reisdocumentnummer 

**Populatie objecttype** 

**Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|||||
|---|---|---|---|
|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
||35.20|Reisdocumentnummer|GBA|
||35.30|Datum uitgifte|GBA|
||35.40|Autoriteit uitgifte|GBA|
||35.50|Einddatum geldigheid document|GBA|
||35.60|Datum inhouding of vermissing|GBA|
||35.70|Aanduiding inhouding of vermissing|GBA|
||35.80|Lengte houder|GBA|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||35.10   is van REISDOCUMENTSOORT||GBA/KING|
||Heeft als houder INGESCHREVEN PERSOON||GBA/KING|
||Kent als|bijgeschrevene INGESCHREVEN PERSOON|GBA/KING|



## **1.45. Reisdocumentsoort** 

**Naam objecttype** 

REISDOCUMENTSOORT 

> **Mnemonic objecttype** (RDS) 

> **Herkomst objecttype** GBA 

**Code objecttype** 

48 

**Definitie objecttype Herkomst definitie objecttype** GBA **Datum opname objecttype Toelichting objecttype** 

Een opsomming van de modellen van de Nederlandse reisdocumenten. 

1 maart 2009 

Het betreft een zgn. tabel-objecttype, afgeleid van de Tabel Nederlands reisdocument in de GBA. 

**Unieke aanduiding objecttype** 

Reisdocumentcode 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|35.11|Reisdocumentcode|GBA|
|35.12|Reisdocumentomschrijving|GBA|
|99.98|Datum begin geldigheid reisdocumentsoort|GBA|
|99.99|Datum einde geldigheid reisdocumentsoort|GBA|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|35.10|hoort bij INGESCHREVEN PERSOONen|KING|



## **1.46. Spoorbaandeel** 

> **Naam objecttype** SPOORBAANDEEL 

> **Mnemonic objecttype** SBD 

> **Herkomst objecttype** IMGeo 

> **Definitie objecttype** Het kleinste functioneel onafhankelijk stukje van een gebaand gedeelte voor het verkeer over rails met gelijkblijvende, homogene eigenschappen en relaties dat er binnen een spoorwegnet wordt onderscheiden. 

> **Herkomst definitie objecttype** IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een SPOORBAANDEEL is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. De hier gehanteerde definitie is een samenstelling van de definities van ‘Spoorbaan’ en ‘Spoorbaandeel’ in het IMGeo. 

**Unieke aanduiding objecttype** 

**Populatie objecttype Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
|||Type Spoorbaan|IMGeo|
|||Type Infrastructuur|IMGeo|
|||Identificatie spoorbaandeel|IMGeo|
|||Status spoorbaandeel|IMGeo|
|||Naam spoorbaandeel|IMGeo|
|||Geometrie spoorbaandeel|IMGeo|
|||Relatieve hoogteligging spoorbaandeel|IMGeo|
|||Datum begin geldigheid spoorbaandeel|IMGeo|
|||Datum einde geldigheid spoorbaandeel|IMGeo|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||-|||



## **1.47. Standplaats** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

## STANDPLAATS 

## SPL 

## BAG 

Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte. 9 april 2007 

Een standplaats maakt in de BAG-terminologie deel uit van de groep adresseerbare objecten. Hier maakt het, gezamenlijk met de LIGPLAATS en het OVERIG TERREIN deel uit van de groep BENOEMD TERREIN. 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|BENOEMD TERREIN . BAG-gegevens|KING|
|58.02  Indicatie geconstateerde standplaats|BAG|
|58.03  Standplaatsstatus|BAG|
|Attributen van de generalisatie BENOEMD TERREIN:||
|BAG-gegevens|KING|
|57.01/58.01  Benoemd terrein Identificatie|BAG|
|57.20/58.20  Geometrie|BAG|
|Datum begin geldigheid benoemd terrein|KING|
|Datum einde geldigheid benoemd terrein|KING|
|Benoemd terrein typering|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|BENOEMD TERREIN . BAG-gegevens|KING|
|heeft als hoofdadres NUMMERAANDUIDING|KING/BAG|
|heeft als nevenadressen NUMMERAANDUIDING|KING/BAG|
|heeft daarop verblijvende  INGESCHREVEN PERSOONen|GBA|
|is huisvesting van HUISHOUDEN|KING|
|Relaties van de generalisatie BENOEMD OBJECT:||
|ligt in BUURT|KING/GFO|
|staat op of heeft ruimtelijke overlap met KADASTRALE||
|ONROERENDE ZAAK|KING/BRK|
|bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
|is hoofdlocatie van VESTIGINGen|KING|
|is nevenlocatie van VESTIGINGen|KING|
|is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.48. Subject** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## SUBJECT 

## SUB 

Door KING toegevoegd objecttype, ontleend aan het GFO BG 

## Een RECHTSPERSOON of een VESTIGING 

## KING 

9 april 2007 

Het betreft de verzameling van alle natuurlijke personen, niet-natuurlijke personen en vestigingen waarvan het gegevensbeheer van essentieel belang is voor de uitoefening van de gemeentelijke taken. Grofweg kan gesteld worden dat kenmerkend voor een subject is dat daarmee gecommuniceerd kan worden, wat zich onder meer uit in correspondentiegegevens. 

Veel subjectgegevens en –relaties zijn specifiek voor een specialisatie daarvan. Zo zijn de datums van ontstaan en einde uitgewerkt per NATUURLIJK PERSOON (geboorte- en overlijdendatum), NIETNATUURLIJK PERSOON en VESTIGING (telkens Datum aanvang en Datum beeindiging). 

**Unieke aanduiding objecttype** 

De code voor de Subjecttypering gevolgd door de unieke aanduding van de specialisatie (van SUBJECT): INGESCHREVEN PERSOON, INGESCHREVEN NIET-NATUURLIJK PERSOON, ANDER NATUURLIJK PERSOON, ANDER NIET NATUURLIJK PERSOON of VESTIGING (of het afleidbaar gegeven Identificatie). 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Heeft|als correspondentieadres||



|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|---|---|
|Postadres||
|Heeft als correspondentieadres postadres in WOONPLAATS KING||
|Is aangewezen belanghebbende bij WOZ-BELANG|BRWOZ/KING|
|08.13<br>Verblijf buitenland|GBA|
|heeft verblijfsadres in LAND|KING/GBA|



## **1.49. Terreindeel** 

> **Naam objecttype** TERREINDEEL 

> **Mnemonic objecttype** TDL 

> **Herkomst objecttype** IMGeo 

> **Definitie objecttype** Het kleinste functioneel onafhankelijk stukje van een door een type landgebruik gekarakteriseerd zichtbaar begrensd stuk grond met gelijkblijvende homogene eigenschappen dat er binnen de Klasse Terrein wordt onderscheiden. 

> **Herkomst definitie objecttype** IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een TERREINDEEL is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. De hier gehanteerde definitie is een samenstelling van de definities van ‘Terrein’ en ‘Terreindeel’ in het IMGeo. 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Type terrein|IMGeo|
||Verharding|IMGeo|
||Identificatie terreindeel|IMGeo|
||Status terreindeel|IMGeo|
||Naam terreindeel|IMGeo|
||Geometrie terreindeel|IMGeo|
||Relatieve hoogteligging terreindeel|IMGeo|
||Datum begin geldigheid terreindeel|IMGeo|
||Datum einde geldigheid terreindeel|IMGeo|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|



- 

## **1.50. Verblijfsobject** 

**Naam objecttype** 

## VERBLIJFSOBJECT 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

## VBO 

## BAG 

De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is. 

**Datum opname objecttype** 

## 9 april 2007 

**Toelichting objecttype** 

Zie de catalogus BAG. Zie v.w.b. de t.o.v. de BAG toegevoegde optionele relatie naar PAND de desbetreffende toelichting bij dit objecttype. 

**Overzicht attributen** 

|||||
|---|---|---|---|
|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|||GEBOUWD OBJECT.BAG-gegevens|KING|
|||56.02 Indicatie geconstateerd verblijfsobject|BAG|
|||56.32 Verblijfsobjectstatus|BAG|
||95.32|Hoogste bouwlaag verblijfsobject|GFO BG|
||95.53|Laagste bouwlaag verblijfsobject|GFO BG|
|||Toegang bouwlaag verblijfsobject|KING|
||95.78|Soort woonobject|GFO BG|
||61.25|Aantal kamers|WOZ/KING|
||61.23|Ontsluiting verdieping|WOZ/KING|
||Attributen van de generalisatie GEBOUWD OBJECT:|||
|||BAG-gegevens|KING|
|||56.01 Gebouwd object identificatie|BAG|
|||56.20 Gebouwd object puntgeometrie|BAG|
|||56.30 Gebruiksdoel gebouwd object|BAG|
|||56.31 Oppervlakte (verblijfs)object|BAG|
|||Inwinningswijze oppervlakte|KING|
|||Gebouwd object vlakgeometrie|IMGeo|
||94.93|Bouwkundige bestemming actueel|GFO BG|
||94.96|Bruto inhoud|GFO BG|
||95.11|Datum begin geldigheid gebouwd object|KING/GFO|
||96.23|Datum einde geldigheid gebouwd object|KING/GFO|
|||Gebouwd object typering|KING|
|||Status voortgang bouw|KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||GEBOUWD OBJECT .BAG-gegevens||KING|
||Heeft als hoofdadres NUMMERAANDUIDING||BAG|
||Heeft als nevenadres(sen) NUMMERAANDUIDING||BAG|
||Maakt deel uit van één of meer PANDEN||BAG|
||heeft daarin verblijvende  INGESCHREVEN PERSOONen||GBA|
||is huisvesting van HUISHOUDEN||KING|
||Relaties van de generalisatie BENOEMD OBJECT:|||
||lligt in BUURT||KING/GFO|
||staat op of heeft ruimtelijke overlap met KADASTRALE|||



|ONROERENDE ZAAK|KING/BRK|
|---|---|
|bestaat uit één of meer WOZ-DEELOBJECTen|KING/BRWOZ|
|is hoofdlocatie van VESTIGINGen|KING|
|is nevenlocatie van VESTIGINGen|KING|
|is ontstaan uit / overgegaan in BENOEMD OBJECT|KING/GFO|



## **1.51. Verblijfstitel** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

VERBLIJFSTITEL 

(VBT) 

GFO BG 

## **Code objecttype** 

**Definitie objecttype Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

**Unieke aanduiding objecttype** 

Rechtsgrond op basis waarvan men bevoegd is in een land te verblijven. 

GFO BG 

1 maart 2009 

Het betreft een zgn. tabel-objecttype, afgeleid van de Verblijfstiteltabel in de GBA. 

Aanduiding verblijfstitel 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|10.39.10|Aanduiding verblijfstitel|GBA|
|95.88|Verblijfstitelomschrijving|GFO|
|81.20|Datum begin geldigheid verblijfstitel|GFO|
|81.30|Datum einde geldigheid verblijfstitel|GFO|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|39.10   hoort bij INGEZETENE||KING/GFO|



## **1.52. Vestiging** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## VESTIGING 

## VES 

## NHR 

Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. 

## NHR 

## 9 april 2007 

Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie (‘deelverzameling’) van SUBJECT. De toelichting in de catalogus NHR lijkt dit te bevestigen: 

“De vestiging van een onderneming of een maatschappelijke activiteit (type niet onderneming) moet men opvatten als een (kleinste eenheid) bundeling van economische activiteiten. De vestiging is een combinatie van activiteiten en locatie. Wisseling van zowel de activiteiten als de locatie maakt dat er sprake is van een nieuwe vestiging. In de toekomstige situatie is er een eenduidige verwijzing naar een ADRESSEERBAAR OBJECT (BAG) voor het bezoekadres. Als er sprake is van een inschrijfplichtige onderneming maar het adresseerbare object is nog niet bekend, omdat bijv. een bedrijfspand nog gebouwd wordt of er vanuit huis gewerkt wordt, kan als adres het woonadres (van de eigenaar) worden genomen. De vestiging mag met een eigen Handelsnaam naar buiten treden, zoniet dan voert zij de Handelsnaam van de onderneming waartoe zij behoort.”. De vestiging kan aldus verhuizen, heeft een bezoekadres en een postadres en een naam. Allemaal zeer ongewone aspecten voor een locatie cq. gebouwd object. Het lijkt dan ook meer weg te hebben van een subject (die activiteiten uitvoert) in een gebouwd object. Dit wordt versterkt doordat het wenselijk is bij het registreren van de WOZ-belanghebbende of een vergunningaanvraag een contactpersoon vast te leggen: iemand die werkzaam is in een vestiging (een NNP kent geen medewerkers) en voor dat geval optreedt als vertegenwoordiger van de vestiging van de onderneming/NNP. 

De definitie beperkt de locaties van VESTIGINGen tot gebouwen, In het RSGB gaan we er van uit dat een VESTIGING haar activiteiten ook kan uitoefenen op een STANDPLAATS, op een LIGPLAATS, op een OVERIG TERREIN of in een OVERIG GEBOUWD OBJECT. 

**Unieke aanduiding objecttype** 

**Overzicht attributen** 

VESTIGING overeft gegevens van de generalisatie SUBJECT. Ondermeer zijn dat de Datum begin geldigheid en Datum einde geldigheid voor resp. Datum in gebruikname en Datum beeindiging in het NHR. Ook het buitenlands adres indien een vestiging verplaatst wordt naar het buitenland. SUBJECT.Subjecttypering gevolgd door het Vestigingsnummer 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Vestigingsnummer|NHR|
||Handelsnamen|NHR|
||Handelsnaam|NHR|
||Verkorte naam|NHR|
||Volgorde|NHR|



**Overzicht relaties** 

||Activiteiten|NHR|
|---|---|---|
||Indicatie hoofdactiviteit|NHR|
||Activiteitcode|NHR|
||Activiteit|NHR|
||Typering hoofd/nevenvestiging|NHR|
||Datum aanvang|NHR|
||Datum beëindiging|NHR|
|Attributen van de generalisatie SUBJECT:|||
||Postadres|KING|
||Postadrestype|KING|
||Postbus- of antwoordnummer|KING/GFO|
||Postadres postcode|KING|
|08.13|Verblijf buitenland|KING/GBA|
||08.13.30 Adres buitenland 1|KING/GBA|
||08.13.40 Adres buitenland 2|KING/GBA|
||08.13.50 Adres buitenland 3|KING/GBA|
|95.80|Telefoonnummer|GFO BG|
|95.27|Fax-nummer|GFO BG|
|95.16|Emailadres|GFO BG|
||Website-URL|KING|
|94.87|Bank/girorekeningnummer|GFO BG|
||Subjecttypering|KING|
||Naam|KING|
||Identificatie|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||KvK-nummer|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|betreft|uitoefening van activiteiten door MAATSCHAPPELIJKE||
|ACTIVITEIT||KING/NHR|
|Heeft hoofdlocatie in of op BENOEMD OBJECT||KING/NHR|
|Heeft nevenlocatie in of op BENOEMD OBJECT||KING|
|Heeft als locatie-adres ADRESSEERBAAR OBJECTAANDUIDING|||
|||KING/NHR|
|Relaties van de generalisatie SUBJECT:|||
|Heeft als correspondentieadres|||
|ADRESSEERBAAR OBJECT AANDUIDING||KING|
|Postadres|||
|Heeft als correspondentieadres postadres in WOONPLAATS||KING|
|Is aangewezen belanghebbende bij WOZ-BELANG               BRWOZ/KING|||
|08.13|Verblijf buitenland|GBA|
||heeft verblijfsadres in LAND|KING/GBA|



## **1.53. Waterdeel** 

**Naam objecttype** 

## WATERDEEL 

> **Mnemonic objecttype** WDL 

> **Herkomst objecttype** IMGeo 

> **Definitie objecttype** Het kleinste functioneel onafhankelijk stukje van een grondoppervlakte bedekt met water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen de klasse Water wordt onderscheiden. 

> **Herkomst definitie objecttype** IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een WATERDEEL is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. De hier gehanteerde definitie is een samenstelling van de definities van ‘Water’ en ‘Waterdeel’ in het IMGeo. 

## **Unieke aanduiding objecttype** 

**Populatie objecttype** 

**Kwaliteitsbegrip objecttype** 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
|||Type Waterdeel|IMGeo|
|||Type Infrastructuur|IMGeo|
|||Identificatie waterdeel|IMGeo|
|||Status waterdeel|IMGeo|
|||Naam waterdeel|IMGeo|
|||Geometrie waterdeel|IMGeo|
|||Relatieve hoogteligging waterdeel|IMGeo|
|||Datum begin geldigheid waterdeel|IMGeo|
|||Datum einde geldigheid waterdeel|IMGeo|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||-|||



## **1.54. Wegdeel** 

**Naam objecttype** 

## WEGDEEL 

> **Mnemonic objecttype** WGD 

> **Herkomst objecttype** IMGeo 

> **Definitie objecttype** Het kleinste functioneel onafhankelijk stuk  van een gebaand gedeelte voor wegverkeer en vliegverkeer te land, met gelijkblijvende, homogene eigenschappen en relaties voor wegverkeer en vliegverkeer te land. 

> **Herkomst definitie objecttype** IMGeo 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie het IMGeo. In aanvulling daarop het volgende. Een WEGDEEL is een voorbeeld van een, in het IMGeo onderscheiden, Geo-object zijnde een abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van het aardoppervlak. De hier gehanteerde definitie is een samenstelling van de definities van ‘Weg’ en ‘Wegdeel’ in het IMGeo. 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

**Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

**Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Type weg|IMGeo|
||Type Infrastructuur|IMGeo|
||Verharding|IMGeo|
||Identificatie wegdeel|IMGeo|
||Status wegdeel|IMGeo|
||Naam wegdeel|IMGeo|
||Geometrie wegdeel|IMGeo|
||Relatieve hoogteligging wegdeel|IMGeo|
||Datum begin geldigheid wegdeel|IMGeo|
||Datum einde geldigheid wegdeel|IMGeo|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|



- 

## **1.55. Wijk** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

**Unieke aanduiding objecttype** 

## WIJK 

## WYK 

Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). 

Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken. 

## GFO BG 

## 9 april 2007 

Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. 

Combinatie van de unieke aanduiding van de GEMEENTE waarin de WIJK gelegen is met de Wijkcode. 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen bericht** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|95.90|Wijkcode|GFO BG|
|95.91|Wijknaam|GFO BG|
||Wijkgeometrie|IMGeo|
||Datum begin geldigheid wijk|KING|
||Datum einde geldigheid wijk|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Ligt in GEMEENTE||GFO BG|
|Bestaat|uit BUURTen|GFO BG|



## **1.56. Woonplaats** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

**Definitie objecttype** 

**Datum opname objecttype Toelichting objecttype** 

## **Overzicht attributen bericht** 

## **Overzicht relaties** 

## WOONPLAATS 

## WPL 

## BAG 

Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente. 9 april 2007 

In incidentele gevallen komt het voor dat een woonplaats (in de zin van het gebied dat in de praktijk aangeduid wordt met dezelfde woonplaatsnaam) doorsneden wordt door een gemeentegrens. Volgens de definitie zou dit niet kunnen cq. is een woonplaats anders gedefinieerd en dus afgebakend: “gedeelte van het gemeentelijk grondgebied”. Vooralsnog wordt uitgegaan van de BAG-insteek en wordt afgewacht hoe dit opgelost wordt in de landelijk te specificeren woonplaatsentabel. 

|landelijk te specificeren woonplaatsentabel.|||
|---|---|---|
|_Code_<br>_Gegevensnaam_|_Herkomst_||
|BAG-gegevens|KING||
|11.03 Woonplaatsidentificatie|BAG||
|11.70 Woonplaatsnaam|BAG||
|11.71 Woonplaatsgeometrie|BAG||
|11.72 Indicatie geconstateerde woonplaats|BAG||
|11.79 Woonplaatsstatus|BAG||
|Woonplaatsnaam NEN|NEN||
|Datum begin geldigheid woonplaats|KING||
|Datum einde geldigheid woonplaats|KING||
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_||
|ligt in GEMEENTE|KING||
|BAG-gegevens|||
|Heeft OPENBARE RUIMTE|KING/BAG||
|Betreft ADRESSEERBAAR OBJECT AANDUIDING|KING/BAG||
|maakt deel uit van woonadreslocatie van|||
|INGESCHREVEN PERSOON|KING/GBA||
|Is deel van correspondentieadres zijnde postadres van|SUBJECT|KING|



## **1.57. WOZ-belang** 

**Naam objecttype** 

WOZ-BELANG 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

(WBL) 

BRWOZ 

De (rechts-)persoon die door de gemeente is aangewezen als "belanghebbende eigenaar", "belanghebbende gebruiker" of eventueel "medebelanghebbende" van het WOZ-object. 

> **Datum opname objecttype** 1 februari 2008 **Toelichting objecttype** 

Belang wordt in de Basisregistratie WOZ, opgenomen, zodra dit bekend is. Opname wordt door eerstvolgende WOZ-beschikking aan de belanghebbende kenbaar gemaakt. 

**Overzicht attributen Overzicht relaties** 

|Opname wordt door eerstvolgende WOZ-beschikking<br>belanghebbende kenbaar gemaakt.|aan de|
|---|---|
|_Code_<br>_Gegevensnaam_|_Herkomst_|
|15.89<br>Status belang|BRWOZ|
|41.10<br>Aanduiding eigenaar/gebruiker|BRWOZ|
|81.22<br>Datum begin geldigheid belang|WOZ/KING|
|81.32<br>Datum einde geldigheid belang|WOZ/KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|betreft WOZ-OBJECT|BRWOZ/KING|
|heeft als aangewezen belanghebbende SUBJECT|BRWOZ/KING|



## **1.58. WOZ-deelobject** 

**Naam objecttype** 

WOZ-DEELOBJECT 

**Mnemonic objecttype Herkomst objecttype Code objecttype** 

WDO 

WOZ-gegevenswoordenboek (2002) 

22 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn. 

WOZ-gegevenswoordenboek (2002) 

1 februari 2008 

Het betreft zowel (delen van) gebouwde objecten, benoemde terreinen en panden als (delen van) andersoortige objecten. 

Het is vooral bedoeld om de doorsnede van WOZ-OBJECTen met VERBLIJFSOBJECTen en PANDen te kunnen maken.  WOZDEELOBJECT-gegevens die vergelijkbaar zijn met (gemeentelijke) basisgegevens, maken deel uit van de gerelateerde objecttypen GEBOUWD OBJECT  en PAND. 

> **Unieke aanduiding objecttype** Verwijzing naar WOZ-object i.c.m. Nummer deelobject 

**Identificatie objecttype** 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ 11.71 Nummer WOZ-deelobject WOZ/KING 61.15 Code WOZ-deelobject WOZ/KING 64.23 Status WOZ-deelobject WOZ/KING 81.21 Datum begin geldigheid deelobject WOZ/KING 81.31 Datum einde geldigheid deelobject WOZ/KING 

**Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype Herkomst_ is onderdeel van WOZ-OBJECT WOZ/KING bestaat uit BENOEMD OBJECT KING bestaat uit PAND KING 

## **1.59. WOZ-object** 

**Naam objecttype** 

WOZ-OBJECT 

> **Mnemonic objecttype** WOZ 

> **Herkomst objecttype** BRWOZ 

> **Definitie objecttype** De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld. 

> **Datum opname objecttype** 1 februari 2008 

> **Toelichting objecttype** Dit objecttype komt voort uit de objectafbakeningsvoorschriften van artikel 

Dit objecttype komt voort uit de objectafbakeningsvoorschriften van artikel 16 van de Wet WOZ. 

De unieke identificatie van het WOZ-object is het WOZ-objectnummer. De WOZ-object-aanduiding, een secundaire identificatie, wordt samengesteld uit de adresgegevens van één van de, aan het WOZ-object via het WOZdeelobject, gerelateerde gebouwde objecten en/of benoemde terreinen dan wel van een nabij gelegen gebouwd object of benoemd terrein, in beide gevallen (eventueel) aangevuld met de locatie-omschrijving. 

|**Overzicht attributen**|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|---|
||01.01|WOZ-objectnummer|BRWOZ|
||11.80|Locatie-omschrijving|BRWOZ|
||15.71|Geometrie WOZ-object|BRWOZ|
||15.79|Status WOZ-object|BRWOZ|
||12.10|Grondoppervlakte|WOZ/KING|
||12.20|Gebruikscode|WOZ/KING|
||61.10|Soort-object-code|WOZ/KING|
||15.10|Vastgestelde waarde|BRWOZ|
||15.20|Waardepeildatum|BRWOZ|
||81.21|Datum begin geldigheid WOZ-object|WOZ/KING|
||81.31|Datum einde geldigheid WOZ-object|WOZ/KING|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
||Heeft WOZ-BELANG||BRWOZ/KING|
||heeft WOZ-DEELOBJECT||KING|
||heeft WOZ-WAARDE||BRWOZ/KING|
||bevat KADASTRALE ONROERENDE ZAAK||BRWOZ/KING|
||heeft aanduiding afgeleid van ADRESSEERBAAR||OBJECT AANDUIDING|
||||BRWOZ/KING|
||ligt aan|OPENBARE RUIMTE|BRWOZ/KING|



## **1.60. WOZ-waarde** 

**Naam objecttype** 

## WOZ-WAARDE 

> **Mnemonic objecttype** WRD 

> **Herkomst objecttype** BRWOZ **Code objecttype Definitie objecttype Herkomst definitie objecttype** 

> **Datum opname objecttype** 2 februari 2009 **Toelichting objecttype** 

De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum. Catalogus BRWOZ versie 1.3 

De vastgestelde waarde wordt meegedeeld in de WOZ-beschikking. Indien er op één datum meerdere beschikkimgen worden afgegeven, dan wordt slechts één van deze geregistreerd. 

Zie verder de toelichting in de BRWOZ. 

> **Unieke aanduiding objecttype** Combinatie van de unieke aanduiding van het gerelateerde WOZ-OBJECT met de Waardepeildatum. 

**Overzicht attributen Overzicht relaties** 

_Code Gegevensnaam Herkomst_ 15.10 Vastgestelde waarde BRWOZ 15.20 Waardepeildatum BRWOZ 15.25 Toestandspeildatum BRWOZ 15.99 Status beschikking BRWOZ _Relatienaam incl. gerelateerd objecttype Herkomst_ 01.01 Hoort bij WOZ-OBJECT BRWOZ/KING 

## **1.61. Zakelijk recht** 

> **Naam objecttype** ZAKELIJK RECHT 

> **Mnemonic objecttype** ZKR 

> **Herkomst objecttype** BRK 

> **Definitie objecttype** Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (RECHTSPERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen). 

> **Datum opname objecttype** 9 april 2007 

> **Toelichting objecttype** Zie de catalogus van de BRK. Daarin is sprake van een zowel rechten als zekerheidsrechten op onroerende zaken (zie de toelichting bij KADASTRALE ONROERENDE ZAAK). Geoordeeld is dat alleen de rechten zodanig van belang zijn voor de gemeentelijke taakuitoefening dat zij deel moeten uit maken van het voorliggende referentiemodel. Zij zijn hierin gezamenlijk gemodelleerd als ZAKELIJK RECHT tussen KADASTRALE ONROERENDE ZAAK en RECHTSPERSOON. (Zakelijke) rechten worden beschouwd vanuit één onroerende zaak, in dit geval het kadastrale object. Recht vormt de relatie tussen één onroerende zaak en één rechtspersoon en heeft betrekking op het eigendom van dat rechtspersoon van één onroerende zaak of op een beperkt recht van dat rechtspersoon op één onroerende zaak. Met een beperkt recht op een onroerende zaak wordt erfpacht, opstal, ed. bedoeld. Het betreft een zogenaamd relatie-objecttype oftewel objecten van dit type kunnen niet zelfstandig bestaan maar alleen in combinatie met objecten van de gerelateerde objecttypen. 

> **Unieke aanduiding objecttype** Combinatie van de unieke aanduidingen van de gerelateerde KADASTRALE ONROERENDE ZAAK en de gerelateerde RECHTSPERSOON (via ZAKELIJK RECHT heeft als gerechtigde RECHTSPERSOON) met de Aanduiding aard verkregen recht. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Kadaster identificatie zakelijk recht BRK Aandeel in recht BRK Teller BRK Noemer BRK Ingangsdatum recht GFO BG Einddatum recht BRK Indicatie betrokken in splitsing BRK 

> **Overzicht relaties** _Relatienaam incl. gerelateerd objecttype Herkomst_ Is van AARD VERKREGEN RECHT KING/BRK Is van AARD RECHT VERKORT KING/BRK Betreft KADASTRALE ONROERENDE ZAAK BRK Heeft als gerechtigde RECHTSPERSOON BRK Heeft ZAKELIJK RECHT AANTEKENINGen BRK 

## **1.62. Zakelijk recht aantekening** 

> **Naam objecttype** Zakelijk recht aantekening 

> **Mnemonic objecttype** ZRA 

> **Herkomst objecttype** BRK 

> **Definitie objecttype** Aanduiding van het feit, genoemd in een Stuk, dat betrekking heeft op een zakelijk recht op een onroerende zaak en dat gevolgen kan hebben voor de uitoefening van rechten op de onroerende zaak. 

> **Herkomst definitie objecttype** BRK 

> **Datum opname objecttype** 29 december 2008 

> **Toelichting objecttype** Toegevoegd ten opzichte van de BRK is de begindatum. Aangezien een aantekening niet gewijzigd kan worden, bepaalt de begin- en einddatum de materiele historie van alle attribuutsoortensoorten. Deze hebben dan ook materiele historie ‘Nee’ gekregen. Zie verder de catalogus BRK 

> **Unieke aanduiding objecttype** Kadaster identificatie aantekening recht 

**Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Kadaster identificatie aantekening recht|BRK|
||Aard aantekening recht|BRK|
||Beschrijving aantekening recht|BRK|
||Begindatum aantekening recht|KING|
||Einddatum aantekening recht|BRK|



## **Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype Herkomst_ behoort bij ZAKELIJK RECHT KING/BRK heeft betrokken RECHTSPERSOON KING/BRK 

## **2. Beschrijving van de attributen en relaties** 

In dit hoofdstuk worden de onderscheiden attributen en relaties, naar analogie van de basisregistratie-catalogi verder te noemen attribuutsoorten en relatiesoorten, gespecificeerd, per objecttype, op basis van de voor basisregistratie-catalogi gebruikelijke wijze, als volgt. 

## **Specificatie attribuutsoort** 

> **Naam attribuutsoort** De naam van de attribuutsoort zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde attribuutsoort betreft, de door KING vastgestelde naam van de attribuutsoort. De naam van de attribuutsoort wordt uniek gemaakt door voorafgaand aan de naam de afkorting van het objecttype op te nemen, waarop de attribuutsoort betrekking heeft. 

> **Herkomst attribuutsoort** De basisregistratie in wiens catalogus de attribuutsoort is gespecificeerd (oftewel de basisregistratie waar de attribuutsoort deel van uitmaakt). Deze specificatie is toegevoegd t.o.v. de basisregistratie-catalogus aangezien het hier niet om een basisregistratie gaat maar wel duidelijk moet zijn in welke basisregistratie de attribuutsoort voorkomt (indien van toepassing). 

> **Code attribuutsoort** De door de desbetreffende basisregistratiehouder aan de attribuutsoort toegekende uniek code. Voor door KING toegevoegde attribuutsoorten is vooralsnog afgezien van het specificeren van deze code. 

> **XML-tag attribuutsoort** De naam van de attribuutsoort in de gestructureerde beschrijving van de attribuutsoort in het XML-formaat zoals gespecificeerd in de desbetreffende catalogus. De XML-tag wordt dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft. 

> **Definitie attribuutsoort** De beschrijving van de betekenis van de attribuutsoort zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde attribuutsoort betreft, de door KING vastgestelde definitie van de attribuutsoort. 

> **Herkomst definitie attribuutsoort** Voor attribuutsoorten die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft. 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

De datum waarop de attribuutsoort is opgenomen in het RSGB. 

Voor attribuutsoorten die deel uitmaken van een basisregistratie betreft dit de daarin opgenomen toelichting. De toelichting wordt dan ook alleen gegeven indien het een door KING toegevoegde attribuutsoort betreft dan wel indien een toelichting nodig is, aanvullend op de toelichting in de desbetreffende catalogus. 

> **Domein attribuutsoort** Formaat: Het aantal karakters (lengte) en het soort tekens waarmee waarden van deze attribuutsoort worden vastgelegd. Waardenverzameling: De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben (opsomming, bereik of verwijzing naar tabel). Voor attribuutsoorten die deel uitmaken van een basisregistratie betreft dit het daarin gespecificeerde domein. Het domein wordt dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft. OnvolledigeDatum 

> **Indicatie materiële historie** Indicatie of de materiële historie van de attribuutsoort te bevragen is (indien van toepassing: als attribuutsoort binnen het groepattribuutsoort). Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de attribuutwaarde. Met het opnemen van deze indicatie zien we af van de specificatie van ‘historie-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Datum begin geldigheid gegevens’, zoals dat gebruikelijk is in sommige basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen logsicherwijs uit deze indicatie. Om duidelijk te maken om welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de indicatie. Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan geldt de specificatie aldaar ook voor het attribuutsoort, zij het op groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan ‘Nee’ geldt dan alleen binnen het groepattribuutsoort. 

> **Indicatie formele historie** Indicatie of de formele historie van de attribuutsoort te bevragen is (indien van toepassing: als attribuutsoort binnen het groepattribuutsoort). Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt). Met het opnemen van deze indicatie zien we af van de specificatie van ‘historie-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Datum wjziging gegevens’ en ‘Datum en tijdstip registratie gegevens’ zoals dat gebruikelijk is in sommige basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen logsicherwijs uit deze indicatie. Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan geldt de specificatie aldaar ook voor het attribuutsoort, zij het op groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan ‘Nee’ geldt dan alleen binnen het groepattribuutsoort. 

|**Aanduiding gebeurtenis**|Indicatie of bij een opname, mutatie of verwijdering van de|
|---|---|
||attribuutwaarde de gebeurtenis aangeduid wordt  die aanleiding gaf tot|
||verandering van de attribuutwaarde (indien van toepassing: als|
||attribuutsoort binnen het groepattribuutsoort) en zo ja, de specificatie van|
||het metagegeven waarmee de gebeurtenis aangeduid wordt:|
||Gebeurtenisomschrijving. Dit metagegeven specificeren we in bijlage 1.|
||Met het opnemen van deze aanduiding zien we af van de specificatie van|
||‘gebeurtenis-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Aanduiding|
||gebeurtenis begin’, zoals dat gebruikelijk is in sommige|
||basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen|
||logsicherwijs uit deze aanduiding.|
||Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan|
||geldt de specificatie aldaar ook voor het attribuutsoort, zij het op|
||groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan|
||‘Nee’ geldt dan alleen binnen het groepattribuutsoort.|
|**Aanduiding brondocument**|Indicatie of bij een opname, mutatie of verwijdering van de|
||attribuutwaarde het brondocument aangeduid wordt op basis waarvan de|
||verandering van de attribuutwaarde heeft plaatsgevonden (indien van|
||toepassing: als attribuutsoort binnen het groepattribuutsoort) en zo ja, de|
||specificatie van de metagegevens waarmee het brondcument aangeduid|
||wordt, zijnde één of meer van de volgende metagegevens:|
||Documentidentificatie, Documentdatum, Documentomschrijving,|
||AktKINGeente en Documentgemeente. Deze metagegevens specificeren|
||we in bijlage 1.|
||Met het opnemen van deze aanduiding zien we af van de specificatie van|
||‘brondocument-attributen’ bij objecttypen, zoals bijvoorbeeld|
||‘Documentnummer mutatie …’ en ‘Aktenummer’, zoals dat gebruikelijk is|
||in sommige basisregistratiecatalogi. Dergelijke attributen (meta-|
||gegevens) volgen logsicherwijs uit deze aanduiding. Om duidelijk te|
||maken om welke attribuutsoorten in welke basisregistratie het gaat,|
||geven we dit aan in de aanduiding.|
||Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan|
||geldt de specificatie aldaar ook voor het attribuutsoort, zij het op|
||groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan|
||‘Nee’ geldt dan alleen binnen het groepattribuutsoort.|
|**Indicatie in onderzoek**|De indicatie of te bevragen is dat er twijfel is of is geweest aan de|
||juistheid van de attribuutwaarde en dat een onderzoek wordt of is|
||uitgevoerd naar de juistheid van de attribuutwaarde (indien van|
||toepassing: als attribuutsoort binnen het groepattribuutsoort). Dit|
||metagegeven specificeren we in bijlage 1.|
||Met het opnemen van deze indicatie zien we af van de specificatie van|
||‘onderzoek-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Aanduiding|
||gegevens in onderzoek’ zoals dat gebruikelijk is in sommige|
||basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen|
||logsicherwijs uit deze indicatie.|
||Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan|
||geldt de specificatie aldaar ook voor het attribuutsoort, zij het op|
||groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan|
||‘Nee’ geldt dan alleen binnen het groepattribuutsoort.|



> **Aanduiding strijdigheid/nietigheid** De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de openbare orde dan wel nietig is (indien van toepassing: als attribuutsoort binnen het groepattribuutsoort). Dit metagegeven specificeren we in bijlage 1. Met het opnemen van deze aanduiding zien we af van de specificatie van ‘strijdigheid/nietigheid-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Aanduiding strijdigheid / nietigheid’ zoals dat gebruikelijk is in sommige basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen logsicherwijs uit deze aanduiding. Indien het attribuutsoort deel uit maakt van een groepattribuutsoort dan geldt de specificatie aldaar ook voor het attribuutsoort, zij het op groepsniveau. Een eventuele specificatie bij het attribuutsoort anders dan ‘Nee’ geldt dan alleen binnen het groepattribuutsoort. 

> **Indicatie kardinaliteit** Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype (dan wel, indien van toepassing, binnen het groepattribuutsoort): 0-1: is soms niet beschikbaar 1-1: is altijd beschikbaar 0-N: is niet altijd beschikbaar, kan een opsomming zijn 1-N: is altijd beschikbaar, kan een opsomming zijn. 

> **Indicatie authentiek** Aanduiding of het een authentiek gegeven (attribuutsoort) betreft. 

> **Regels attribuutsoort** Optionaliteitsregels of waardebeperkende regels zoals gespecificeerd in de desbetreffende catalogus. De regels worden dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft.. 

## **Specificatie relatiesoort** 

**Naam relatiesoort** 

De naam van de relatiesoort zoals afgeleid is van de overeenkomstige attribuutsoort in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde relatiesoort betreft, de door KING vastgestelde naam van de relatiesoort. 

> **Herkomst relatiesoort** De basisregistratie in wiens catalogus de attribuutsoort is gespecificeerd waarvan de relatiesoort is afgeleid (oftewel de basisregistratie waar de relatiesoort impliciet deel van uitmaakt). 

> **Code relatiesoort** De door de desbetreffende basisregistratiehouder aan de overeenkomstige attribuutsoort toegekende uniek code. Voor door KING toegevoegde attribuutsoorten is vooralsnog afgezien van het specificeren van deze code. 

> **Definitie relatiesoort** De beschrijving van de betekenis van de relatiesoort zoals afgeleid van de definitie van de overeenkomstige attribuutsoort in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde relatiesoort betreft, de door KING vastgestelde definitie van de relatiesoort. 

> **Herkomst definitie relatiesoort** Voor een relatiesoort waarvan het overeenkomstige attribuutsoort deel uitmaakt van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft. 

**Datum opname relatiesoort** 

De datum waarop de relatiesoort is opgenomen in het RSGB. 

|**Toelichting relatiesoort**|Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit|
|---|---|
||de daarin opgenomen toelichting bij de overeenkomstige attribuutsoort.|
||De toelichting wordt dan ook alleen gegeven indien het een door KING|
||toegevoegde relatiesoort betreft dan wel indien een toelichting nodig is,|
||aanvullend op de toelichting in de desbetreffende catalogus.|
|**Indicatie materiële historie**|Indicatie of de materiële historie van de relatiesoort te bevragen is (indien|
||van toepassing: als relatiesoort binnen het groepattribuutsoort). Materiële|
||historie geeft aan wanneer een verandering is opgetreden in de|
||werkelijkheid die heeft geleid tot veranderjng van de relatie.|
||Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit|
||de daarin, bij de overeenkomstige attribuutsoorten, gespecificeerde|
||indicatie. De indicatie wordt dan ook alleen vermeld indien het een door|
||KING toegevoegde relatiesoort betreft.|
||In sommige basisregistratiecatalogi is het gebruikelijk de materiële|
||historie te specificeren met specifieke ‘historie-attributen’. Van dergelijke|
||attribuutsoorten zien we hier af.|
|**Indicatie formele historie**|Indicatie of de formele historie van de relatiesoort te bevragen is (indien|
||van toepassing: als relatiesoort binnen het groepattribuutsoort). Formele|
||historie geeft aan wanneer in de administratie een verandering is verwerkt|
||van de relatie (wanneer was de verandering bekend en is deze verwerkt).|
||Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit|
||de daarin, bij de overeenkomstige attribuutsoort, gespecificeerde|
||indicatie. De indicatie wordt dan ook alleen vermeld indien het een door|
||KING toegevoegde relatiesoort betreft.|
||In sommige basisregistratiecatalogi is het gebruikelijk de formele historie|
||te specificeren met specifieke ‘historie-attributen’. Van dergelijke|
||attribuutsoorten zien we hier af.|
|**Aanduiding gebeurtenis**|Indicatie of bij een opname, mutatie of verwijdering van de relatie de|
||gebeurtenis aangeduid wordt  die aanleiding gaf tot verandering van de|
||relatie (indien van toepassing: als relatiesoort binnen het|
||groepattribuutsoort) en zo ja, de specificatie van het metagegeven|
||waarmee de gebeurtenis aangeduid wordt: Gebeurtenisomschrijving. Dit|
||metagegeven specificeren we in bijlage 1.|
||In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te|
||specificeren met specifieke ‘gebeurtenis-attributen’. Van dergelijke|
||attribuutsoorten zien we hier af. Om duidelijk te maken om welke|
||attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de|
||aanduiding.|
|**Aanduiding brondocument**|Indicatie of bij een opname, mutatie of verwijdering van de relatie het|
||brondocument aangeduid wordt op basis waarvan de verandering van de|
||relatie heeft plaatsgevonden (indien van toepassing: als relatiesoort|
||binnen het groepattribuutsoort) en zo ja, de specificatie van de|
||metagegevens waarmee het brondcument aangeduid wordt, zijnde één of|
||meer van de volgende metagegevens: Documentidentificatie,|
||Documentdatum, Documentomschrijving, Aktegemeente en|
||Documentgemeente. Deze metagegevens specificeren we in bijlage 1.|
||In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te|
||specificeren met specifieke ‘brondocument-attributen’. Van dergelijke|
||attribuutsoorten zien we hier af. Om duidelijk te maken om welke|
||attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de|
||aanduiding.|



> **Indicatie in onderzoek** De indicatie of te bevragen is dat er twijfel is of is geweest aan de juistheid van de relatie en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de relatie (indien van toepassing: als relatiesoort binnen het groepattribuutsoort). Dit metagegeven specificeren we in bijlage 1. In sommige basisregistratiecatalogi is het gebruikelijk deze indicatie te specificeren met specifieke ‘in-onderzoek-attributen’. Van dergelijke attribuutsoorten zien we hier af. 

> **Aanduiding strijdigheid/nietigheid** De aanduiding of te bevragen is dat de relatie strijdig met de openbare orde dan wel nietig is (indien van toepassing: als relatiesoort binnen het groepattribuutsoort). Dit metagegeven specificeren we in bijlage 1. In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te specificeren met specifieke ‘strijdigheid/nietigheid-attributen’. Van dergelijke attribuutsoorten zien we hier af. 

> **Indicatie kardinaliteit** Deze indicatie geeft aan hoeveel keer waarden van deze relatiesoort (i.c. relaties) kunnen voorkomen bij een object van het betreffende objecttype (of, indien van toepassing, binnen het groepattribuutsoort):. 0-1: is soms niet beschikbaar 1-1: is altijd beschikbaar 0-N: is niet altijd beschikbaar, kunnen meerdere relaties zijn 1-N: is altijd beschikbaar, kunnen meerdere relaties zijn N-M: is niet altijd beschikbaar, kunnen meerdere relaties zijn tussen objecten van hetzelfde objecttype. 

> **Indicatie authentiek** Aanduiding of de attribuutsoort waarvan de relatiesoort is afgeleid, een authentiek gegeven (attribuutsoort) betreft. 

> **Regels relatiesoort** Optionaliteitsregels of waardebeperkende regels zoals gespecificeerd in de desbetreffende catalogus. De regels worden dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft.. 

## **2.1. Aard recht verkort** 

## **Attribuutsoort Aanduiding aard recht verkort** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Aanduiding aard recht verkort 

BRK 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** aardVerkort 

> **Definitie attribuutsoort** EDI code voor de aard zakelijk recht, uit de verkorte waardenlijst 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 30 maart 2009 

> **Toelichting attribuutsoort** Het overeenkomstige attribuut in de BRK is aldaar opgenomen bij Zakelijk recht 

> **Domein attribuutsoort** Formaat: AN4 Waardenverzameling: zie BRK-tabel Aard zakelijk recht verkort 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk basisgegeven 

Het overeenkomstige attribuut in de BRK is aldaar opgenomen bij Zakelijk recht 

## **Attribuutsoort Omschrijving aard recht verkort** 

**Naam attribuutsoort** 

Omschrijving aard recht verkort 

> **Herkomst attribuutsoort** BRK 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

omschrijvingVerkort 

De omschrijving bij de EDI code voor de aard zakelijk recht, uit de verkorte waardenlijst BRK 

**Datum opname attribuutsoort** 

30 maart 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Formaat: AN100 Waardenverzameling: zie BRK-tabel Aard zakelijk recht verkort 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Landelijk basisgegeven|



## **Relatiesoort AARD RECHT VERKORT betreft ZAKELIJKe RECHTen** 

> **Naam relatiesoort** AARD RECHT VERKORT betreft ZAKELIJKe RECHTen 

> **Herkomst relatiesoort** KING/BRK **Code relatiesoort** 

> **Definitie relatiesoort** De ZAKELIJKe RECHTen die zijn van de AARD RECHT VERKORT 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Landelijk basisgegeven **Regels relatiesoort** 

## **2.2. Aard verkregen recht** 

## **Attribuutsoort Aanduiding aard verkregen recht** 

**Naam attribuutsoort** 

Aanduiding aard verk regenrecht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** aard 

> **Definitie attribuutsoort** Een aanduiding voor de aard van het recht. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 30 maart 2009 

> **Toelichting attribuutsoort** Het overeenkomstige attribuut in de BRK is aldaar opgenomen bij Zakelijk recht 

> **Domein attribuutsoort** Formaat: AN6 Waardenverzameling: zie BRK-tabel Aard verkregen zakelijk recht 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk basisgegeven 

Het overeenkomstige attribuut in de BRK is aldaar opgenomen bij Zakelijk recht 

## **Attribuutsoort Omschrijving aard verkregen recht** 

**Naam attribuutsoort** 

**Omschrijving** aard verk regenrecht 

> **Herkomst attribuutsoort** BRK 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

omschrijving 

De omschrijving bij de aanduiding voor de aard van het zakelijk recht. 

> **Herkomst definitie attribuutsoort** BRK 

**Datum opname attribuutsoort** 

30 maart 2009 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Het overeenkomstige attribuut in de BRK is aldaar opgenomen bij Zakelijk recht 

Formaat: AN200 Waardenverzameling: zie BRK-tabel Aard verkregen zakelijk recht 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Landelijk basisgegeven|



## **Relatiesoort AARD VERKREGEN RECHT betreft ZAKELIJKe RECHTen** 

> **Naam relatiesoort** AARD VERKREGEN RECHT betreft ZAKELIJKe RECHTen 

> **Herkomst relatiesoort** KING/BRK **Code relatiesoort** 

> **Definitie relatiesoort** De ZAKELIJKe RECHTen die zijn van de AARD VERKREGEN RECHT 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Landelijk basisgegeven **Regels relatiesoort** 

## **2.3. Academische titel** 

## **Attribuutsoort Academische titelcode** 

**Naam attribuutsoort** 

## Academische titelcode 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.80 

> **XML-tag attribuutsoort** code **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN3 Waardenverzameling: zie NEN 1888 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

Een code die aangeeft welke academische titel behoort tot de naam. 

**Regels attribuutsoort** 

## **Attribuutsoort Omschrijving academische titel** 

**Naam attribuutsoort** 

Omschrijving academische titel 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.62 

> **XML-tag attribuutsoort** omschrijving 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De omschrijving behorende bij NEN-tabel 'Academische titelcode'. 

GFO BG 

**Datum opname attribuutsoort** 

1 november 2008 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: zie NEN 1888 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Positie academische titel tov naam** 

**Naam attribuutsoort** 

Positie academische titel tov naam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.72 **XML-tag attribuutsoort** 

> **Definitie attribuutsoort** Aanduiding of de academische titel voorafgaand aan de voornamen of achter de geslachtsnaam wordt geplaatst. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1 Waardenverzameling: N = Na de geslachtsnaam V = Voor de voornamen 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Datum begin geldigheid titel** 

## **Naam attribuutsoort** 

Datum begin geldigheid titel 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 2 februari 2009 **Toelichting attribuutsoort** bestaat en toegepast kan worden. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

De datum waarop de ACADEMISCHE TITEL is ontstaan. 

Met deze datum wordt aangegeven vanaf wanneer de academische titel bestaat en toegepast kan worden. 

## **Attribuutsoort Datum einde geldigheid titel** 

**Naam attribuutsoort Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort Herkomst definitie attribuutsoort** GFO BG **Datum opname attribuutsoort** 9 april 2007 

Datum einde geldigheid titel 

De datum waarop de ACADEMISCHE TITEL is opgeheven. 

9 april 2007 

**Toelichting attribuutsoort** 

Met deze datum wordt aangegeven vanaf wanneer de academische titel niet meer bestaat en niet meer toegepast kan worden. 

**Domein attribuutsoort** 

OnvolledigeDatum 

Formaat: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid titel’ kan in de registratie worden opgenomen. 

## **Relatiesoort ACADEMISCHE TITEL hoort bij NATUURLIJK PERSOONen** 

> **Naam relatiesoort** ACADEMISCHE TITEL hoort bij NATUURLIJK PERSOONen 

> **Herkomst relatiesoort** GFO BG 

> **Code relatiesoort** 94.00 

> **Definitie relatiesoort** De NATUURLIJK PERSOONen met deze ACADEMISCHE TITEL 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van NATUURLIJK PERSOON heeft ACADEMISCHE TITEL 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

De relatiesoort is de tegenhanger van NATUURLIJK PERSOON heeft ACADEMISCHE TITEL 

## **2.4. Adresseerbaar object** 

Dit objecttype kent geen andere attribuut- en relatiesoorten dan de attribuut- en relatiesoorten van de specialisaties (VERBLIJFSOBJECT, STANDPLAATS en LIGPLAATS). 

## **2.5. Adresseerbaar object aanduiding** 

## **Attribuutsoort BAG-gegevens** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

BAG-gegevens 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

De gegevens van de ADRESSEERBAAR OBJECT AANDUIDING zoals die zijn opgenomen in de BasisRegistratie Adressen. 

KING 

19 november 2008 

Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. 

Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 11.02 Identificatiecode adresseerbaar object aanduiding 11.20 Huisnummer 11.30 Huisletter 11.40 Huisnummertoevoeging 11.60 Postcode 11.21 NUMMERAANDUIDING .Indicatie geconstateerde nummeraanduiding 11.69 NUMMERAANDUIDING . Nummeraanduidingstatus en de volgende relatiesoorten: ADRESSEERBAAR OBJECT AANDUIDING ligt aan OPENBARE RUIMTE 

ADRESSEERBAAR OBJECT AANDUIDING ligt in WOONPLAATS NUMMERAANDUIDING  is hoofdadres van ADRESSEERBAAR OBJECT NUMMERAANDUIDING is nevenadres van ADRESSEERBAAR OBJECT n.v.t 

> **Domein attribuutsoort** n.v.t 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Identificatiecode adresseerbaar object aanduiding** 

**Naam attribuutsoort** 

Identificatiecode adresseerbaar object aanduiding 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.02 

> **XML-tag attribuutsoort** identificatie **Definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De unieke aanduiding van een ADRESSEERBAAR OBJECT AANDUIDING. 

Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype NUMMERAANDUIDING. Het is bij de ADRESSEERBAAR OBJECT AANDUIDING opgenomen aangezien naast de NUMMERAANDUIDING de OVERIG ADRESSEERBAAR OBJECT AANDUIDING wordt onderscheiden. Aangezien de ADRESSEERBAAR OBJECT AANDUIDING een generalisatie is van NUMMERAANDUIDING en OVERIG ADRESSEERBAAR OBJECT AANDUIDING overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: zie BAG Waardenverzameling: Combinatie van de viercijferige 'gemeentecode' (volgens GBA tabel 33), de tweecijferige 'objecttypecode' en een voor het betreffende objecttype binnen een gemeente uniek tiencijferig 'objectvolgnummer'. De objecttypecode kent in de BAG de volgende waarde: 20 nummeraanduiding Voor de gevallen dat het gebouwd object geen verblijfsobject maar een overig gebouwd object betreft, is de volgende domeinwaarde toegevoegd: 90 overig adresseerbaar object aanduiding 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Huisnummer** 

> **Naam attribuutsoort** Huisnummer 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.20 

> **XML-tag attribuutsoort** huisnummer 

> **Definitie attribuutsoort** Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende nummering. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype NUMMERAANDUIDING. Het is bij de ADRESSEERBAAR OBJECT AANDUIDING opgenomen aangezien naast de NUMMERAANDUIDING de OVERIG ADRESSEERBAAR OBJECT AANDUIDING wordt onderscheiden. Aangezien de ADRESSEERBAAR OBJECT AANDUIDING een generalisatie is van NUMMERAANDUIDING en OVERIG ADRESSEERBAAR OBJECT AANDUIDING overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Huisletter** 

> **Naam attribuutsoort** Huisletter 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.30 

> **XML-tag attribuutsoort** huisletter 

## **Definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende toevoeging aan een huisnummer in de vorm van een alfanumeriek teken. 

9 april 2007 

Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype NUMMERAANDUIDING. Het is bij de ADRESSEERBAAR OBJECT AANDUIDING opgenomen aangezien naast de NUMMERAANDUIDING de OVERIG ADRESSEERBAAR OBJECT AANDUIDING wordt onderscheiden. Aangezien de ADRESSEERBAAR OBJECT AANDUIDING een generalisatie is van NUMMERAANDUIDING en OVERIG ADRESSEERBAAR OBJECT AANDUIDING overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Huisnummertoevoeging** 

**Naam attribuutsoort Herkomst attribuutsoort** BAG **Code attribuutsoort** 11.40 **XML-tag attribuutsoort Definitie attribuutsoort** 

Huisnummertoevoeging 

huisnummertoevoeging 

Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende nadere toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter. 9 april 2007 

**Datum opname attribuutsoort** 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype NUMMERAANDUIDING. Het is bij de ADRESSEERBAAR OBJECT AANDUIDING opgenomen aangezien naast de NUMMERAANDUIDING de OVERIG ADRESSEERBAAR OBJECT AANDUIDING wordt onderscheiden. Aangezien de ADRESSEERBAAR OBJECT AANDUIDING een generalisatie is van NUMMERAANDUIDING en OVERIG ADRESSEERBAAR OBJECT AANDUIDING overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Postcode** 

> **Naam attribuutsoort** Postcode 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.60 

> **XML-tag attribuutsoort** postcode 

> **Definitie attribuutsoort** De door TNT Post vastgestelde code behorende bij een bepaalde combinatie van een naam van een woonplaats, naam van een openbare ruimte en een huisnummer 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype NUMMERAANDUIDING. Het is bij de ADRESSEERBAAR OBJECT AANDUIDING opgenomen aangezien naast de NUMMERAANDUIDING de OVERIG ADRESSEERBAAR OBJECT AANDUIDING wordt onderscheiden. Aangezien de ADRESSEERBAAR OBJECT AANDUIDING een generalisatie is van NUMMERAANDUIDING en OVERIG ADRESSEERBAAR OBJECT AANDUIDING overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Datum begin geldigheid addresserbaar object aanduiding** 

**Naam attribuutsoort** 

Datum begin geldigheid addresserbaar object aanduiding 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

De datum waarop de ADDRESSERBAAR OBJECT AANDUIDING formeel is vastgesteld. 

**Herkomst definitie attribuutsoort** 

KING 

|**Datum opname attribuutsoort**|9 april 2007||
|---|---|---|
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|N||
|**Indicatie formele historie**|J||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk|basisgegeven|
|**Regels attribuutsoort**|-||



## **Attribuutsoort Datum einde geldigheid addresserbaar object aanduiding** 

|**Naam attribuutsoort**|Datum einde geldigheid addresserbaar object aanduiding|Datum einde geldigheid addresserbaar object aanduiding|
|---|---|---|
|**Herkomst attribuutsoort**|KING||
|**Code attribuutsoort**|-||
|**XML-tag attribuutsoort**|einddatumObject||
|**Definitie attribuutsoort**|De datum waarop de|addresserbaar object aanduiding formeel is|
||ingetrokken.||
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|N||
|**Indicatie formele historie**|J||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|Alleen een datum die|gelijk is aan of die gelegen is na de datum zoals|
||opgenomen onder 'Datum begin geldigheid …’ kan in de registratie||
||worden opgenomen.||



## **Attribuutsoort Adresseerbaar object aanduiding typering** 

> **Naam attribuutsoort** Adresseerbaar object aanduiding typering 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** typering 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Het onderscheid van een ADRESSEERBAAR OBJECT AANDUIDING in een NUMMERAANDUIDING dan wel een OVERIG ADRESSEERBAAR OBJECT AANDUIDING. 

KING 

**Datum opname attribuutsoort** 

9 april 2007 

|**Toelichting attribuutsoort**|Het attribuutsoort is benodigd om bij uitwisseling van gegevens van het||
|---|---|---|
||objecttype ADRESSEERBAAR OBJECT AANDUIDING aan te kunnen||
||geven of het desbetreffende ‘adres’ een NUMMERAANDUIDING dan wel||
||een OVERIG ADRESSEERBAAR OBJECT AANDUIDING betreft.||
|**Domein attribuutsoort**|Formaat:<br>AN40||
||Waardenverzameling: Nummeraanduiding||
||Overig adresseerbaar object aanduiding||
|**Indicatie materiële historie**|N||
|**Indicatie formele historie**|J||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Relatiesoort ADRESSEERBAAR OBJECT AANDUIDING ligt aan OPENBARE RUIMTE** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECT AANDUIDING ligt aan OPENBARE RUIMTE 

> **Herkomst relatiesoort** BAG 

> **Code relatiesoort** 11.65 

> **Definitie relatiesoort** De unieke aanduiding van een OPENBARE RUIMTE waaraan het object, waaraan de ADRESSEERBAAR OBJECT AANDUIDING is toegekend, is gelegen. 

> **Herkomst definitie relatiesoort** KING op basis van BAG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** In de BAG is dit gemodelleerd als het attribuutsoort ‘Identificatiecode bijbehorende openbare ruimte’ bij het objecttype NUMMERAANDUIDING. In RSGB wordt dit hergebruikt als relatiesoort en overerven de objecttypen NUMMERAANDUIDING en OVERIG ADDRESSEERBAAR OBJECT AANDUIDING dit relatiesoort van het objecttype ADDRESSEERBAAR OBJECT AANDUIDING. De relatie is de tegenhanger van OPENBARE RUIMTE heeft ADRESSEERBAAR OBJECT AANDUIDING. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

> **Regels relatiesoort** Zie de BAG. 

## **Relatiesoort ADRESSEERBAAR OBJECT AANDUIDING ligt in WOONPLAATS** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECT AANDUIDING ligt in WOONPLAATS 

> **Herkomst relatiesoort** BAG 

> **Code relatiesoort** 11.61 

> **Definitie relatiesoort** De unieke aanduiding van de WOONPLAATS waarbinnen het object, waaraan de ADRESSEERBAAR OBJECT AANDUIDING is toegekend, is gelegen. 

> **Herkomst definitie relatiesoort** KING op basis van BAG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** In de BAG is dit gemodelleerd als het attribuutsoort ‘Identificatiecode bijbehorende woonplaats’ bij het objecttype NUMMERAANDUIDING. In RSGB wordt dit hergebruikt als relatiesoort en overerven de objecttypen NUMMERAANDUIDING en OVERIG ADDRESSEERBAAR OBJECT AANDUIDING dit relatiesoort van het objecttype ADDRESSEERBAAR OBJECT AANDUIDING. De relatie is de tegenhanger van WOONPLAATS betreft ADRESSEERBAAR OBJECT AANDUIDING. Deze relatie dient te worden opgenomen op het moment dat een object is gelegen in een andere woonplaats dan de openbare ruimte waaraan de adresseerbaar object aanduiding is gerelateerd. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

||Dez<br>gele<br>adre<br>De r<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|



## **Indicatie authentiek** 

**Regels relatiesoort** 

Het betreft een authentiek gegeven indien de adresseerbaar object aanduiding een nummeraanduiding betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. Zie de BAG. 

## **Relatiesoort ADRESSEERBAAR OBJECT AANDUIDING is correspondentieadres van SUBJECT** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECT AANDUIDING is correspondentieadres van SUBJECT 

> **Herkomst relatiesoort** KING op basis van GFO BG **Code relatiesoort** 

> **Definitie relatiesoort** De SUBJECTen die in de regel schriftelijk bereikbaar zijn op het adres dat gevormd wordt door de combinatie van de ADRESSEERBAAR OBJECT AANDUIDING met  de bijbehorende (GEMEENTELIJKE) OPENBARE RUIMTE en WOONPLAATS. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING. Een correspondentieadres kan het in de GBA opgenomen briefadres betreffen. 

> **Indicatie materiële historie** Ja indien het een GBA-briefadres betreft, anders Nee 

> **Indicatie formele historie** Ja indien het een GBA-briefadres betreft, anders Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Niet verplicht te registreren 

## **Relatiesoort ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van INGESCHREVEN NIET-NATUURLIJK PERSOON** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van INGESCHREVEN NIET-NATUURLIJK PERSOON 

> **Herkomst relatiesoort** KING op basis van NHR 

**Code relatiesoort** 

## **Definitie relatiesoort** 

> **Definitie relatiesoort** De NIET-NATUURLIJKe PERSOONen die de ADRESSEERBAAR OBJECT AANDUIDING als binnenlands bezoekadres hebben. 

> **Herkomst definitie relatiesoort** KING {definitie in NHR ontbreekt vooralsnog} 

> **Datum opname relatiesoort** 2 februari 2009 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Bezoekadres’ bij het objecttype Niet-natuurlijk persoon in het NHR. De relatie is de tegenhanger van INGESCHREVEN NIET-NATUURLIJK PERSOON heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING. Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van ANDER NATUURLIJK PERSOON** 

|**Naam relatiesoort**|ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van ANDER|
|---|---|
||NATUURLIJK PERSOON|
|**Herkomst relatiesoort**|KING|
|**Code relatiesoort**||
|**Definitie relatiesoort**|De ANDERe NATUURLIJKe PERSOONen die de ADRESSEERBAAR|
||OBJECT AANDUIDING als binnenlands bezoekadres hebben.|
|**Herkomst definitie relatiesoort**|KING|
|**Datum opname relatiesoort**|1 maart 2009|
|**Toelichting relatiesoort**|De relatie is de tegenhanger van ANDER NATUURLIJK PERSOON heeft|
||als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|



> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N **Indicatie authentiek** 

Gemeentelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort ADRESSEERBAAR OBJECTAANDUIDING is locatie-adres van VESTIGINGen** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECTAANDUIDING is locatie-adres van VESTIGINGen 

> **Herkomst relatiesoort** KING op basis van NHR 

**Code relatiesoort** 

> **Definitie relatiesoort** De VESTIGING(en) die bij inschrijving gekozen hebben om als vestigingsadres de  ADRESSEERBAAR OBJECTAANDUIDING te gebruiken bij het BENOEMD OBJECT waarin de VESTIGINGen (één van) haar lokatie(s) heeft. 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** Vestigingen kunnen er aldus voor kiezen zich op een hoofd- of op een nevenadres te laten inschrijven. De relatie is de tegenhanger van VESTIGING heeft als locatie-adres ADRESSEERBAAR OBJECTAANDUIDING. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

**Regels attribuutsoort** 

## **Relatiesoort ADRESSEERBAAR OBJECTAANDUIDING bepaalt aanduiding van WOZOBJECT** 

> **Naam relatiesoort** ADRESSEERBAAR OBJECTAANDUIDING bepaalt aanduiding van WOZ-OBJECT 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.02 

> **Definitie relatiesoort** De unieke aanduidingen van de WOZ-OBJECTen waarvan de aanduidingen worden afgeleid met behulp van het adres van het ADRESSEERBAAR OBJECTAANDUIDING en de locatie-omschrijving van het WOZ-OBJECT. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Adresseerbaar object voor aanduiding WOZ-object’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZ-OBJECT heeft adres dat is afgeleid van ADRESSEERBAAR OBJECTAANDUIDING. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **2.6. Ander natuurlijk persoon** 

## **Attribuutsoort Nummer ander natuurlijk persoon** 

**Naam attribuutsoort** 

Nummer ander natuurlijk persoon 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Het door de gemeente uitgegeven unieke nummer voor een ANDER NATUURLIJK PERSOON 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Natuurlijke personen, zijnde (nog) geen ingeschreven personen, die wel relevant zijn voor de gemeentelijke taakuitoefening wordem geregistreerd en door de gemeente voorzien van een unieke aanduiding. Het kan aldus voorkomen dat dezelfde natuurlijke persoon bij twee gemeenten geregistreerd is onder een ander nummer. 

De attribuutsoort kent historie omdat het mogelijk is dat het wijzigt, bijvoorbeeld omdat het Ander natuurlijk persoon overgaat in een Ingeschreven natuurlijk persoon. 

|**Domein attribuutsoort**|Formaat:|AN17|
|---|---|---|
||Waardenverzameling: viercijferige gemeentecode gevolgd door een||
|||volgnummer van 13 cijfers met voorloopnullen|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||



**Regels attribuutsoort** 

## **Relatiesoort ANDER NATUURLIJK PERSOON heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** ANDER NATUURLIJK PERSOON heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

## **Definitie relatiesoort** 

Het binnenlands bezoekadres van de ANDER NATUURLIJK PERSOON 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** Het betreft het binnenlandse adres van een ander natuurlijk persoon indien deze in Nederland woonachtig is. Zo niet dan heeft deze een buitenlands adres. De relatie is de tegenhanger van ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van ANDER NATUURLIJK PERSOON. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien deze relatie voorkomt dan heeft het SUBJECT zijnde de ANDER NATUURLIJK PERSOON geen buitenlands adres. 

## **2.7. Ander niet-natuurlijk persoon** 

## **Attribuutsoort Nummer ander niet-natuurlijk persoon** 

**Naam attribuutsoort** 

Nummer ander niet-natuurlijk persoon 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Het door de gemeente uitgegeven unieke nummer voor een ANDER NIET-NATUURLIJK PERSOON 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Niet-natuurlijke personen, zijnde (nog) niet ingeschreven in het Handelsregister, die wel relevant zijn voor de gemeentelijke taakuitoefening worden geregistreerd en door de gemeente voorzien van een unieke aanduiding. Het kan aldus voorkomen dat dezelfde nietnatuurlijke persoon bij twee gemeenten geregistreerd is onder een ander nummer. 

||nummer.|nummer.|
|---|---|---|
||De attribuutsoort kent historie omdat het mogelijk is dat het wijzigt,||
||bijvoorbeeld omdat het Ander niet-natuurlijk persoon overgaat in een||
||Ingeschreven niet-natuurlijk persoon.||
|**Domein attribuutsoort**|Formaat:|AN17|
||Waardenverzameling:|viercijferige gemeentecode gevolgd door een|
|||volgnummer van 13 cijfers met voorloopnullen|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|||



## **2.8. Appartementsrecht** 

## **Attribuutsoort Appartementsindex** 

> **Naam attribuutsoort** Appartementsindex 

> **Herkomst attribuutsoort** BRK 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** kadastraleAanduiding.appartementsIndex 

> **Definitie attribuutsoort** Een nummer dat onderdeel uitmaakt van de kadastrale aanduiding waarmee een Appartementsrecht wordt geïdentificeerd. Dat nummer is verbonden met het kadastraal nummer als volgnummer van het betrokken Appartementsrecht. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Deze attribuutsoort maakt deel uit van de groepattribuutsoort KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding. De aldaar gespecificeerde metagegevens zoals historie gelden ook voor deze attribuutsoort. Het betreft het subdomein ‘Appartementsindex’ van het domein ‘Kadastrale aanduiding’ van de gelijknamige attribuutsoort ‘ in de BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

**Regels attribuutsoort** 

## **Relatiesoort APPARTEMENTSRECHT maakt deel uit van appartementencomplex met als vereniging van eigenaars NIET-NATUURLIJK PERSOON** 

> **Naam relatiesoort** APPARTEMENTSRECHT maakt deel uit van appartementencomplex met als vereniging van eigenaars NIET-NATUURLIJK PERSOON 

> **Herkomst relatiesoort** BRK **Code relatiesoort** 

> **Definitie relatiesoort** Een rechtspersoon (NIET-NATUURLIJK PERSOON) die het beheer voert over de statuten van de vereniging en over de gemeenschap, met uitzondering van de gedeelten die bestemd zijn als afzonderlijk geheel te worden gebruikt, met als doel het behartigen van gemeenschappelijke belangen van de appartementseigenaars. 

> **Herkomst definitie relatiesoort** BRK 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . appartementsrecht . Appartementencomplex . Vereniging van eigenaars’ bij het objecttype ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van NIET-NATUURLIJK PERSOON is vereniging van eigenaars bij appartementencomplex met APPARTEMENTSRECHTen. Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels attribuutsoort** De relatie komt alleen voor indien de appartementsindex de waarde nul heeft. 

## **Relatiesoort APPARTEMENTSRECHT maakt deel uit van appartementencomplex dat staat op KADASTRAAL PERCEEL** 

**Naam relatiesoort** 

APPARTEMENTSRECHT maakt deel uit van appartementencomplex dat staat op KADASTRAAL PERCEEL BRK 

> **Herkomst relatiesoort** BRK **Code relatiesoort** 

> **Definitie relatiesoort** Een appartementencomplex bevindt zich op een of meer percelen. 

> **Herkomst definitie relatiesoort** BRK 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . appartementsrecht . Appartementencomplex . perceel’ bij het objecttype ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van KADASTRAAL PERCEEL is ondergrond van appartementencomplex met APPARTEMENTSRECHTen. Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels attribuutsoort** De relatie komt alleen voor indien de appartementsindex de waarde nul heeft. 

## **2.9. Authentiek terrein** 

## **Attribuutsoort Indicatie geconstateerd authentiek terrein** 

> **Naam attribuutsoort** Indicatie geconstateerd authentiek terrein 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.02/58.02 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd als het attribuutsoort ‘Indicatie geconstateerde ligplaats’ bij het objecttype LIGPLAATS en als attribuutsoort ‘Indicatie geconstateerde standplaats’ bij het objecttype STANDPLAATS. Het is hier opgenomen aangezien het AUTHENTIEK TERREIN de generalisatie is van LIGPLAATS en STANDPLAATS. Beide laatstgenoemde objecttypen overerven dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

||TERREIN de generalisatie is van LIGP<br>laatstgenoemde objecttypen overerven<br>De attribuutsoort maakt deel uit van de<br>gegevens. Zie verder de toelichtingen<br>attribuutsoorten.|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Status authentiek terrein** 

> **Naam attribuutsoort** Status authentiek terrein 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.03/58.03 

> **Definitie attribuutsoort** De fase van de levenscyclus van een AUTHENTIEK TERREIN, waarin het betreffende AUTHENTIEKE TERREIN zich bevindt. 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd als het attribuutsoort ‘Ligplaatsstatus’ bij het objecttype LIGPLAATS en als attribuutsoort ‘Standplaatsstatus’ bij het objecttype STANDPLAATS. Het is hier opgenomen aangezien het AUTHENTIEK TERREIN de generalisatie is van LIGPLAATS en STANDPLAATS. Beide laatstgenoemde objecttypen overerven dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort AUTHENTIEK TERREIN heeft als hoofdadres NUMMERAANDUIDING** 

**Naam relatiesoort** 

AUTHENTIEK TERREIN heeft als hoofdadres NUMMERAANDUIDING 

**Herkomst relatiesoort Code relatiesoort** 57.10/58.10 **Definitie relatiesoort** 

KING op basis van BAG 

De identificatiecode nummeraanduiding waaronder het hoofdadres van een LIGPLAATS of STANDPLAATS, dat in het kader van de basisregistratie gebouwen als zodanig is aangemerkt, is opgenomen in de basisregistratie adressen. 

## **Herkomst definitie relatiesoort** 

KING op basis van BAG 

> **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** 

In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding hoofdadres ligplaats’ bij het objecttype LIGPLAATS en als attribuutsoort ‘Aanduiding hoofdadres standplaats’ bij het objecttype STANDPLAATS. Het is hier opgenomen aangezien het AUTHENTIEK TERREIN de generalisatie is van LIGPLAATS en STANDPLAATS. Beide laatstgenoemde objecttypen overerven dit relatiesoort. 

De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is hoofdadres van AUTHENTIEK TERREIN 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort AUTHENTIEK TERREIN heeft als nevenadressen NUMMERAANDUIDING** 

**Naam relatiesoort** 

AUTHENTIEK TERREIN heeft als nevenadressen NUMMERAANDUIDING 

> **Herkomst relatiesoort** KING op basis van BAG 

> **Code relatiesoort** 57.11/58.11 **Definitie relatiesoort** 

De identificatiecodes nummeraanduiding waaronder nevenadressen van een LIGPLAATS of STANDPLAATS, die in het kader van de basisregistratie gebouwen als zodanig zijn aangemerkt, zijn opgenomen in de basisregistratie adressen. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** 

KING op basis van BAG 

In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding nevenadressen ligplaats’ bij het objecttype LIGPLAATS en als attribuutsoort ‘Aanduiding nevenadressen standplaats’ bij het objecttype STANDPLAATS. Het is hier opgenomen aangezien het AUTHENTIEK TERREIN de generalisatie is van LIGPLAATS en STANDPLAATS. Beide laatstgenoemde objecttypen overerven dit relatiesoort. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is nevenadres van AUTHENTIEK TERREIN De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Authentiek gegeven|
|**Regels relatiesoort**|-|



## **2.10. Benoemd object** 

## **Relatiesoort BENOEMD OBJECT ligt in BUURT** 

> **Naam relatiesoort** BENOEMD OBJECT ligt in BUURT 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 94.07 

> **Definitie relatiesoort** De BUURT waarin een BENOEMD OBJECT is gelegen. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** Het is de tegenhanger van het relatiesoort BUURT omvat nul of meer BENOEMDe OBJECTen. 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort BENOEMD OBJECT staat op of heeft ruimtelijke overlap met KADASTRALE ONROERENDE ZAAK** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

BENOEMD OBJECT staat op of heeft ruimtelijke overlap met KADASTRALE ONROERENDE ZAAK 

KING op basis van BRK 

**Code attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De kadastrale (deel)percelen die het deel van het aardoppervlak gemeen hebben waar het BENOEMD OBJECT het aardoppervlak raakt cq. doorsnijdt dan wel de kadastrale appartementsrechten die betrekking hebben op het BENOEMD OBJECT. 

KING 

**Datum opname attribuutsoort** 

1 maart 2009 

> **Toelichting attribuutsoort** Het doel van de relatie is dat de eigendomssituatie van het benoemd object (een gebouwd object of benoemd terrein) afgeleid kan worden uit de rechten die rusten op de gerelateerde kadastrale onroerende zaken. Het gaat nadrukkelijk om ruimtelijke relaties en niet om gebruiksrelaties, zoals bij de WOZ gebruikelijk is. V.w.b. het gebouwd object is bepalend de doorsnijding hiervan met het aardoppervlak d.w.z. de situatie op het maaiveld. Luchtbruggen e.d.  maken dus geen deel uit van de ruimtelijke relatie. 

De relatie is één van de tegenhangers van het attribuutsoort ‘locatie onroerende zaak . locatie aanduiding’ bij de ONROERENDE ZAAK in de BRK cq. de tegenhanger van het relatiesoort KADASTRALE ONROERENDE ZAAK is ondergrond van of heeft ruimtelijke overlap met BENOEMD OBJECT. **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Ja: Documentidentificatie **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-N **Indicatie authentiek** Gemeentelijk basisgegeven (vooralsnog niet authentiek) **Regels attribuutsoort** - 

## **Relatiesoort BENOEMD OBJECT bestaat uit één of meer WOZ-DEELOBJECTen** 

> **Naam relatiesoort** BENOEMD OBJECT bestaat uit één of meer WOZ-DEELOBJECTen 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 56.01 

> **Definitie relatiesoort** De unieke aanduidingen van de WOZ-DEELOBJECTen die deel uitmaken van het BENOEMD OBJECT. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde verblijfsobjecten, standplaatsen en ligplaatsen’ bij het WOZ-object. In het RSGB wordt dit hergebruikt als relatiesoort vanuit WOZ-DEELOBJECT. De relatie is de tegenhanger van WOZ-DEELOBJECT is gedeelte van BENOEMD OBJECT. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort BENOEMD OBJECT is hoofdlocatie van VESTIGINGen** 

**Naam relatiesoort** 

BENOEMD OBJECT is hoofdlocatie van VESTIGINGen 

**Herkomst relatiesoort** 

KING op basis van NHR 

**Code relatiesoort** 

**Definitie relatiesoort** 

## **Herkomst definitie relatiesoort** 

De VESTIGINGen die zich bevinden in het BENOEMD OBJECT en die beschouwd worden als hoofdlocaties voor de uitvoering van de activiteitenen van die VESTIGINGEN 

KING 

**Datum opname relatiesoort Toelichting relatiesoort** 

1 maart 2009 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Bezoekadres’ bij het objecttype Vestiging in het NHR v.w.b. benoemde objecten d.w.z. naast adresseerbare objecten ook overige gebouwde objecten en overige terreinen. 

De relatie is de tegenhanger van VESTIGING heeft hoofdlocatie in BENOEMD OBJECT. 

Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **Relatiesoort BENOEMD OBJECT is nevenlocatie van VESTIGINGen** 

> **Naam relatiesoort** BENOEMD OBJECT is nevenlocatie van VESTIGINGen 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De VESTIGINGen die zich bevinden in het BENOEMD OBJECT en die niet beschouwd worden als hoofdlocaties voor de uitvoering van de activiteiten van die VESTIGINGEN 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** De relatie is de tegenhanger van VESTIGING heeft nevenlocatie in BENOEMD OBJECT. Zie verder de toelichting bij die relatiesoort 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-M 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort BENOEMD OBJECT is ontstaan uit / overgegaan in BENOEMD OBJECT** 

**Naam relatiesoort** 

BENOEMD OBJECT is ontstaan uit / overgegaan in BENOEMD OBJECT 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 95.96 / 95.97 **Definitie relatiesoort** 

De verwijzing naar vervallen BENOEMD(e) OBJECT(en) waaruit het BENOEMD OBJECT is ontstaan en naar  BENOEMD(e) OBJECT (en) waarin een vervallen BENOEMD OBJECT is overgegaan. KING op basis van GFO BG 

**Herkomst definitie relatiesoort** 

> **Datum opname relatiesoort** 30 maart 2009 **Toelichting relatiesoort** 

Een nieuw benoemd object kan ontstaan zijn uit één of meer vervallen benoemde objecten. Eén of meer vervallen benoemde objecten kunnen zijn overgegaan in een nieuw benoemd object. De relatie wordt ook wel aangeduid met ‘filiatie’. 

## **Indicatie materiële historie** 

Ja 

**Indicatie formele historie** 

Ja 

|**Aanduiding gebeurtenis**|Nee|
|---|---|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|N-M|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **2.11. Benoemd Terrein** 

## **Attribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De gegevens van het BENOEMD TERREIN zoals die zijn opgenomen in de BasisGebouwenRegistratie. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 

> **Toelichting attribuutsoort** Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 57.01/58.01  Benoemd terrein Identificatie 57.20/58.20  Geometrie 57.02/58.02  AUTHENTIEK TERREIN . Indicatie geconstateerd authentiek terrein 57.03/58.03  AUTHENTIEK TERREIN . Status authentiek terrein en de volgende relatiesoorten: AUTHENTIEK TERREIN heeft als hoofdadres NUMMERAANDUIDING AUTHENTIEK TERREIN heeft als nevenadressen NUMMERAANDUIDING 

> **Domein attribuutsoort** n.v.t 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Benoemd terrein identificatie** 

**Naam attribuutsoort** 

Benoemd terrein identificatie 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.01/58.01 **Definitie attribuutsoort Herkomst attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De unieke aanduiding van een BENOEMD TERREIN. 

KING op basis van BAG 

Dit attribuutsoort wordt in de BAG gespecificeerd als ‘Standplaatsidentificatie’ bij objecttype STANDPLAATS en als ‘Ligplaatsidentificatie’ bij objecttype LIGPLAATS. Het is bij het BENOEMD TERREIN opgenomen aangezien naast de STANDPLAATS en de LIGPLAATS het OVERIG TERREIN wordt onderscheiden. Aangezien het BENOEMD TERREIN een generalisatie is van AUTHENTIEK TEREIN en OVERIG TERREIN overerven beide laatstgenoemde objecttypen dit attribuutsoort alsmede de objecttypen STANDPLAATS en LIGPLAATS die specialisaties zijn van AUTHENTIEK TERREIN. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: zie BAG Waardenverzameling: Combinatie van de viercijferige 'gemeentecode' (volgens GBA tabel 33), de tweecijferige 'objecttypecode' en een voor het betreffende objecttype binnen een gemeente uniek tiencijferig 'objectvolgnummer'. De objecttypecode kent in de BAG de volgende waarden: 02 ligplaats 03 standplaats Voor de gevallen dat het benoemd terrein geen stand- en ligplaats maar een overig terrein betreft, is de volgende domeinwaarde toegevoegd: 92 overig terrein 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien het benoemd terrein een authentiek terrein betreft, zijnde een standplaats of ligplaats. indien benoemd terrein een overig terrein betreft is het een gemeentelijk basisgegeven. 

## **Attribuutsoort Benoemd terrein geometrie** 

**Naam attribuutsoort** 

Benoemd terrein geometrie 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.20/58.20 

> **XML-tag attribuutsoort** vlakGeometrie 

> **Definitie attribuutsoort** De tweedimensionale geometrische representatie van de omtrekken van een BENOEMD TERREIN. 

> **Herkomst attribuutsoort** KING op basis van BAG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort wordt in de BAG gespecificeerd als 

> **Toelichting attribuutsoort** Dit attribuutsoort wordt in de BAG gespecificeerd als ‘Standplaatsgeometrie’ bij objecttype STANDPLAATS en als ‘Ligplaatsgeometrie’ bij objecttype LIGPLAATS. Het is bij het BENOEMD TERREIN opgenomen aangezien naast de STANDPLAATS en de LIGPLAATS het OVERIG TERREIN wordt onderscheiden. Aangezien het BENOEMD TERREIN een generalisatie is van AUTHENTIEK TEREIN en OVERIG TERREIN overerven beide laatstgenoemde objecttypen dit attribuutsoort alsmede de objecttypen STANDPLAATS en LIGPLAATS die specialisaties zijn van AUTHENTIEK TERREIN. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien het benoemd terrein een authentiek terrein betreft, zijnde een standplaats of ligplaats. indien benoemd terrein een overig terrein betreft is het een gemeentelijk basisgegeven. 

## **Attribuutsoort Datum begin geldigheid benoemd terrein** 

> **Naam attribuutsoort** Datum begin geldigheid benoemd terrein 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject 

## **Definitie attribuutsoort** 

||||
|---|---|---|
|**Definitie attribuutsoort**|De datum waarop|van gemeentewege het benoemd terrein formeel is|
||aangewezen.||
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|Onvolledige datum|
||Waardenverzameling: geldige, evt. onvolledige datums||
|**Indicatie materiële historie**|N||
|**Indicatie formele historie**|J||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Attribuutsoort Datum einde geldigheid benoemd terrein** 

> **Naam attribuutsoort** Datum einde geldigheid benoemd terrein 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop van gemeentewege het benoemd terrein formeel is ingetrokken. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. 

## **Attribuutsoort Benoemd terrein typering** 

> **Naam attribuutsoort** Benoemd terrein typering 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** typering 

## **Definitie attribuutsoort** 

> **Definitie attribuutsoort** Het onderscheid van een BENOEMD TERREIN in een STANDPLAATS, LIGPLAATS dan wel OVERIG TERREIN. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort is benodigd om bij uitwisseling van gegevens van het objecttype BENOEMD TERREIN aan te kunnen geven of het een STANDPLAATS, LIGPLAATS dan wel een  OVERIG TERREIN betreft. 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: Standplaats Ligplaats Overig terrein 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **2.12. Buurt** 

## **Attribuutsoort Buurtcode** 

> **Naam attribuutsoort** Buurtcode 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.99 

> **XML-tag attribuutsoort** buurtCode **Definitie attribuutsoort** 

De code behorende bij de naam van de buurt. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

De gehanteerde codering is de CBS-buurtcode. De buurtgrenzen worden in overleg tussen gemeente en CBS vastgesteld. Een buurt is een onderdeel van een wijk. Een unieke buurtcode ontstaat door combinatie van de gemeentecode (4 posities), de wijkcode (2 posities) en de buurtcode (2 posities). 

Formaat: N2 Waardeverzameling: Buurtcode conform CBS-tabel 

N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Buurtnaam** 

> **Naam attribuutsoort** Buurtnaam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.00 

> **XML-tag attribuutsoort** buurtNaam 

> **Definitie attribuutsoort** De naam van de buurt, zoals die door het CBS wordt gebruikt. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: AN..40 Waardenverzameling: Alle bestaande alfanumerieke tekens. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Buurtgeometrie** 

> **Naam attribuutsoort** Buurtgeometrie 

> **Herkomst attribuutsoort** IMGeo **Code attribuutsoort** 

> **XML-tag attribuutsoort** geometrie 

## **Definitie attribuutsoort** 

De tweedimensionale geometrische representatie van de omtrekken van de buurt. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De buurtgrenzen zijn zoveel mogelijk gebaseerd op topografische elementen. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: alle binnen Nederland gelegen waarden van het RD-stelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

## **Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Datum begin geldigheid buurt** 

> **Naam attribuutsoort** Datum begin geldigheid buurt 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.20 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop de buurt is gecreëerd. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** In het GFO BG was de attribuutnaam ‘Ingangsdatum buurt’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid buurt** 

> **Naam attribuutsoort** Datum einde geldigheid buurt 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop de buurt is komen te vervallen. 

> **Herkomst definitie attribuutsoort** GFO BG 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** In het GFO BG was de attribuutnaam ‘Einddatum buurt’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid buurt’ kan in de registratie worden opgenomen. 

## **Relatiesoort BUURT ligt in WIJK** 

|**Naam relatiesoort**|BUURT ligt in WIJK|
|---|---|
|**Herkomst relatiesoort**|GFO BG|
|**Code relatiesoort**|94.08|
|**Definitie relatiesoort**|De wijk waarin de buurt is g|
|**Herkomst definitie relatiesoort**|GFO BG|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|Een wijk bestaat uit een of|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



De wijk waarin de buurt is gelegen. 

Een wijk bestaat uit een of meer buurten. Een buurt ligt in 1 wijk. 

## **Regels relatiesoort** 

- 

## **Relatiesoort BUURT omvat nul of meer BENOEMDe OBJECTen** 

**Naam relatiesoort** 

BUURT omvat nul of meer BENOEMDe OBJECTen 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De BENOEMDe OBJECTen die gelegen zijn in de buurt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het is de tegenhanger van het relatiesoort BENOEMD OBJECT ligt in BUURT 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort BUURT omvat PAND** 

**Naam relatiesoort** 

BUURT omvat PAND 

**Herkomst relatiesoort** 

## KING 

## **Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De panden die gelegen zijn in de buurt en waarbinnen zich geen verblijfsobjecten bevinden. 

## KING 

**Datum opname relatiesoort Toelichting relatiesoort** 

## 9 april 2007 

De relatie wordt alleen gelegd voor panden waarbinnen geen verblijfsobjecten zijn afgebakend, zoals bijvoorbeeld een vrijstaande garage bij een woonhuis. Verder wordt de relatie alleen gelegd indien het desbetreffende pand niet is geregistreerd als bijgebouw van een verblijfsobject. 

De relatie is de tegenhanger van het relatiesoort PAND zonder verblijfsobject ligt in BUURT 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **2.13. Functionaris** 

## **Attribuutsoort Functionaristype** 

> **Naam attribuutsoort** Functionaristype 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** functionarisType 

> **Definitie attribuutsoort** De functie die een RECHTSPERSOON kan vervullen voor een INGESCHREVEN NIET-NATUURLIJK PERSOON. 

> **Herkomst definitie attribuutsoort** KING op basis van Catalogus NHR 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: door de KvK onderscheiden functierollen 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum toetreding** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum toetreding 

NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort Datum opname attribuutsoort** 

tijdvakRelatie.beginRelatie 

nog niet in NHR uitgewerkt 9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Formaat: OnvolledigeDatum 

**Indicatie materiële historie** 

Nee 

|**Indicatie formele historie**|Ja|
|---|---|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Datum uittreding** 

|**Naam attribuutsoort**|Datum uittreding||
|---|---|---|
|**Herkomst attribuutsoort**|NHR||
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|tijdvakRelatie.eindRelatie||
|**Definitie attribuutsoort**|nog niet in NHR|uitgewerkt|
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven||



## **Relatiesoort FUNCTIONARIS van INGESCHREVEN NIET-NATUURLIJK PERSOON** 

> **Naam relatiesoort** FUNCTIONARIS van INGESCHREVEN NIET-NATUURLIJK PERSOON 

> **Herkomst relatiesoort** NHR **Code relatiesoort** 

> **Definitie relatiesoort** nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van INGESCHREVEN NIET-NATUURLIJK PERSOON heeft FUNCTIONARIS. Het betreft de ingeschreven niet-natuurlijke persoon waarbij een functionaris zijnde een subject is geregistreerd die namens deze persoon optreedt. Zie verder de toelichting bij het objecttype FUNCTIONARIS. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven indien het gerelateerde subject zijnde de functionaris een maat of vennoot (met uitzondering van de commanditaire vennoten) betreft en de niet-natuurlijke persoon een maatschap, een vennootschap onder firma of een commanditaire vennootschap is. Anders een niet authentiek landelijk basisgegeven. 

## **Relatiesoort FUNCTIONARIS rol wordt vervuld door RECHTSPERSOON** 

> **Naam relatiesoort** FUNCTIONARIS rol wordt vervuld door RECHTSPERSOON 

> **Herkomst relatiesoort** NHR **Code relatiesoort** 

> **Definitie relatiesoort** nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van RECHTSPERSOON heeft rol als FUNCTIONARIS. Het betreft de rechtspersoon die als functionaris is geregistreerd voor de gerelateerde ingeschreven niet natuurlijke persoon en als functionaris namens deze personen optreedt. Zie verder de toelichting bij het objecttype FUNCTIONARIS. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek** 

## 1-1 

Authentiek gegeven indien het subject een maat of vennoot (met uitzondering van de commanditaire vennoten) betreft die behoort bij een maatschap, een vennootschap onder firma of een commanditaire vennootschap. Anders een niet authentiek landelijk basisgegeven. 

## **2.14. Gebouwd object** 

## **Attribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De gegevens van het GEBOUWD OBJECT zoals die zijn opgenomen in de BasisGebouwenRegistratie. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 

> **Toelichting attribuutsoort** Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 56.01 Gebouwd object identificatie 56.20 Gebouwd object puntgeometrie 56.30 Gebruiksdoel gebouwd object 56.02 VERBLIJFSOBJECT. Indicatie geconstateerd verblijfsobject 56.31 Oppervlakte verblijfsobject 56.32 VERBLIJFSOBJECT . Verblijfsobjectstatus en de volgende relatiesoorten: VERBLIJFSOBJECT  heeft als hoofdadres NUMMERAANDUIDING VERBLIJFSOBJECT  heeft als nevenadres(sen) NUMMERAANDUIDING VERBLIJFSOBJECT maakt deel uit van één of meer PANDEN 

> **Domein attribuutsoort** n.v.t 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Gebouwd object identificatie** 

**Naam attribuutsoort** 

Gebouwd object identificatie 

**Herkomst attribuutsoort Code attribuutsoort Definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

BAG 

56.01 

De unieke identificatie van een GEBOUWD OBJECT. 

9 april 2007 

Dit attribuutsoort is in de BAG gespecificeerd als ‘Verblijfsobject identificatie’ bij het objecttype VERBLIJFSOBJECT. Het is bij het GEBOUWD OBJECT opgenomen aangezien naast het VERBLIJFSOBJECT het OVERIG GEBOUWD OBJECT wordt onderscheiden. Aangezien het GEBOUWD OBJECT een generalisatie is van VERBLIJFSOBJECT en OVERIG GEBOUWD OBJECT overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: zie BAG Waardenverzameling: Combinatie van de viercijferige 'gemeentecode' (volgens GBA tabel 33), de tweecijferige 'objecttypecode' en een voor het betreffende objecttype binnen een gemeente uniek tiencijferig 'objectvolgnummer'. De objecttypecode kent in de BAG de volgende waarde: 01 verblijfsobject Voor de gevallen dat het gebouwd object geen verblijfsobject maar een overig gebouwd object betreft, is de volgende domeinwaarde toegevoegd: 91 overig gebouwd object 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien het gebouwd object een verblijfsobject betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Gebouwd objectpuntgeometrie** 

> **Naam attribuutsoort** Gebouwd objectpuntgeometrie 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 56.20 

> **XML-tag attribuutsoort** puntGeometrie 

> **Definitie attribuutsoort** De minimaal tweedimensionale geometrische representatie van een GEBOUWD OBJECT. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd als ‘Verblijfsobject geometrie’ bij het objecttype VERBLIJFSOBJECT. Het is bij het GEBOUWD OBJECT opgenomen aangezien naast het VERBLIJFSOBJECT het OVERIG GEBOUWD OBJECT wordt onderscheiden. Aangezien het GEBOUWD OBJECT een generalisatie is van VERBLIJFSOBJECT en OVERIG GEBOUWD OBJECT overerven beide laatstgenoemde objecttypen dit attribuutsoort. In de attribuutnaam is de term ‘punt’ toegevoegd ter onderscheid van de eveneens (optioneel) te registreren vlakgeometrie. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien het gebouwd object een verblijfsobject betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Gebruiksdoel gebouwd object** 

> **Naam attribuutsoort** Gebruiksdoel gebouwd object 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 56.30 

> **XML-tag attribuutsoort** gebruiksdoel 

> **Definitie attribuutsoort** Een categorisering van de gebruiksdoelen van het betreffende GEBOUWD OBJECT zoals dit  formeel door de overheid als zodanig is toegestaan. 

**Datum opname attribuutsoort** 

## 9 april 2007 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Dit attribuutsoort is in de BAG gespecificeerd als ‘Gebruiksdoel verblijfsobject’ bij het objecttype VERBLIJFSOBJECT. Het is bij het GEBOUWD OBJECT opgenomen aangezien naast het VERBLIJFSOBJECT het OVERIG GEBOUWD OBJECT wordt onderscheiden. Aangezien het GEBOUWD OBJECT een generalisatie is van VERBLIJFSOBJECT en OVERIG GEBOUWD OBJECT overerven beide laatstgenoemde objecttypen dit attribuutsoort. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Het betreft een authentiek gegeven indien het gebouwd object een verblijfsobject betreft. In andere gevallen betreft het een gemeentelijk basisgegeven. 

## **Attribuutsoort Oppervlakte (verblijfs)object** 

> **Naam attribuutsoort** Oppervlakte (verblijfs)object 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 56.31 

> **Definitie attribuutsoort** De gebruiksoppervlakte van een VERBLIJFSOBJECT of het OVERIG GEBOUWD OBJECT 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Indien het gebouwd object een verblijfsobject betreft dan maakt het deel uit van de BAG. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

**Indicatie authentiek** 

Authentiek gegeven indien het een verblijfsobject betreft (dan kardinaliteit 1-1), anders een gemeentelijk basisgegeven (met kardinaliteit 0-1). 

## **Attribuutsoort Inwinningswijze oppervlakte** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Inwinningswijze oppervlakte 

## KING 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

- 

## inwinningswijzeOppervlakte 

De wijze waarop de gebruiksoppervlakte van het GEBOUWD OBJECT verkregen is 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 27-04-09 **Toelichting attribuutsoort** 

De waarde van het attribuut bij een object geeft een indicatie van de betrouwbaatheid van de waarde van de gebruiksoppervlakte. 

**Domein attribuutsoort** 

Formaat: AN24 Waardeverzameling: overgenomen uit bouwaanvraag ter plaatse ingemeten gemeten op basis van de bouwtekening initiële vulling d.m.v. conversietabel inhoud-oppervlak initiële vulling d.m.v. gegevens woningbouwvereniging initiële vulling d.m.v. oppervlaktegegevens WOZ-administratie initiële vulling d.m.v. gegevens bouw- en woningtoezicht initiële vulling d.m.v. overige brongegevens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Gebouwd object vlakgeometrie** 

> **Naam attribuutsoort** Gebouwd object vlakgeometrie 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

**XML-tag attribuutsoort** 

## vlakGeometrie 

**Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

De tweedimensionale geometrische representatie van de omtrekken van een GEBOUWD OBJECT 

## KING 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een verblijfsobject. 

**Domein attribuutsoort** 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (vlak of multivlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. J 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De begrenzing treedt niet buiten de geometrie van het pand en is gebaseerd op het bovenaanzicht van het pand. 

## **Attribuutsoort Bouwkundige bestemming actueel** 

**Naam attribuutsoort** 

Bouwkundige bestemming actueel 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.93 **XML-tag attribuutsoort** 

bouwkundigeBestemming 

**Definitie attribuutsoort** 

De feitelijke bestemming van een GEBOUWD OBJECT zoals vastgelegd in de bouwvergunning of een toetsing van een melding bouwvoornemen dan wel vastgelegd in een zogenaamde herbeschrijving van een bestemming. 

**Herkomst definitie attribuutsoort** 

KING op basis van GFO 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

Een gemengde bestemming kan worden vastgelegd door twee of meer codes te registreren. 

**Domein attribuutsoort** 

Formaat: 

N4 

Waardenverzameling: 1000 = doeleinden voor wonen 1001 = eensgezinswoning 

1002 = bejaardenwoning 1004 = recreatiewoning 1005 = meergezinswoning 1006 = dienstwoning 1007 = zorgwoonverblijf 1008 = aanleunwoonverblijf 1009 = bejaardenwoonverblijf (in bejaardenoord, centrale keuken) 1010 = jongerenwooneenheid 1011 = gehandicaptenwooneenheid 

2000 = doeleinden voor niet-wonen 2100 = doeleinden voor handel, horeca en bedrijf 2110 = detailhandel 2120 = cafe/bar/restaurant 2130 = hotel/logies 2150 = kantoor 2160 = opslag en distributie 2170 = fabricage en productie 2180 = onderhoud en reparatie 2190 = laboratoria 2199 = overige 

2200 = doeleinden voor cultuur 2210 = wijk-/buurt-/verenigingsactiviteiten 2220 = congres 2230 = theater en concert 2240 = musea 2250 = expositie 2260 = bioscoop 2270 = bibliotheek 2299 = overige 

2300 = doeleinden voor recreatie 2310 = sport buiten 2320 = sport binnen 2330 = recreatie 2340 = zwembad 2350 = dierenverzorging 2360 = natuur en landschap 2399 = overige 

2400 = doeleinden voor agrarisch bedrijf 2410 = akkerbouw 2420 = veeteelt 2430 = tuinbouw 2440 = gemengd bedrijf 2499 = overige 

2500 = doeleinden voor onderwijs 2510 = kinderopvang 2520 = basisschool 2530 = algemeen voortgezet onderwijs 

2540 = hoger beroepsonderwijs 2550 = academisch onderwijs 2560 = bijzonder onderwijs 2570 = vrijetijds onderwijs 2599 = overige 

2600 = doeleinden voor gezondheidszorg 2610 = ziekenhuis 2620 = polikliniek 2630 = praktijkruimte 2640 = verpleegtehuis 2650 = verzorgingstehuis en bejaardentehuis 2660 = dagverblijf 2670 = wijkverzorging 2680 = psychiatrische inrichting 2699 = overige 

2700 = doeleinden voor verkeer 2710 = stalling (fietsen/auto's) 2720 = wegverkeer 2730 = spoorwegverkeer 2740 = luchtvaart 2750 = scheepvaart 2799 = overige 

2800 = doeleinden voor nutsvoorzieningen 2810 = waternuts doeleinden 2820 = gas 2830 = elektriciteit 2840 = CAI 2850 = telecommunicatie 2860 = waterschaps en waterverdediging 2899 = overige 

2900 = andere doeleinden van openbaar nut 2910 = gemeentehuis 2920 = politie 2930 = brandweer 2940 = gevangenis/gesticht 2950 = begraafplaats/crematorium 2960 = godsdienst (kerk, klooster e.d.) 2970 = defensie 2999 = overige 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|N|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



**Indicatie kardinaliteit** 

0-N 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

Niet verplicht te registreren 

## **Attribuutsoort Bruto inhoud** 

> **Naam attribuutsoort** Bruto inhoud 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.96 

> **XML-tag attribuutsoort** brutoInhoud **Definitie attribuutsoort** 

Aanduiding in kubieke meters van de bruto inhoud van het GEBOUWD OBJECT. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

KING op basis van GFO BG 

Bruto inhoud betreft de buitenwerks gemeten inhoud, inclusief dakopbouwen en kelders, maar exclusief lichtkoepels, loggia's, schoorstenen, dakkapellen en bijgebouwen, die niet onder dezelfde dakconstructie zijn gelegen. Bij een dakopbouw is de gevel doorgetrokken of de nok verhoogd. Een dakkapel is slechts een uitbouw uit het schuine dakvlak. Bijgebouwen die inpandig zijn, dus die onder dezelfde dakconstructie vallen, dienen te worden gekubeerd bij de bruto inhoud van het object. Een loggia is een veelal overdekt inpandig balkon (Stuf-WOZ, p. 272). Alternatieve definities voor inhouden zijn te vinden in NEN 2580 (2e druk, 1997). 

|**Domein attribuutsoort**|Formaat:|N6|
|---|---|---|
||Waardenverzameling: 0 – 999999 kubieke meter||
|**Indicatie materiële historie**|J||
|**Indicatie formele historie**|N||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|Niet verplicht te registreren||



## **Attribuutsoort Datum begin geldigheid gebouwd object** 

## **Naam attribuutsoort** 

Datum begin geldigheid gebouwd object 

> **Herkomst attribuutsoort** KING op basis van GFO BG 

> **Code attribuutsoort** 95.11 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

De datum waarop van gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een GEBOUWD OBJECT conform de vergunning, de melding of de aanschrijving zijn uitgevoerd. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

KING op basis van GFO BG 9 april 2007 

> **Toelichting attribuutsoort** Aangezien een gebouwd object al geregistreerd wordt voordat de bouwgereedmelding is ontvangen, of mogelijkerwijs al voordat de bouw is aangevangen of voordat de bouwvergunning is verleend, kan het gegeven gedurende een bepaalde periode niet gevuld zijn. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Verplicht te registreren 

## **Attribuutsoort Datum einde geldigheid gebouwd object** 

**Naam attribuutsoort** 

Datum einde geldigheid gebouwd object 

**Herkomst attribuutsoort Code attribuutsoort** 96.23 **XML-tag attribuutsoort Definitie attribuutsoort** 

KING op basis van GFO BG 

einddatumObject 

De datum waarop het gebouwd object is gesloopt volgens de sloopgereedmelding. 

**Herkomst definitie attribuutsoort** 

KING 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Onder sloop wordt verstaan dat alle muren, wanden, vloeren en daken zijn verdwenen. De fundering hoeft niet te zijn verwijderd. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** 

## Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

Verplicht te registreren. Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. 

## **Attribuutsoort Gebouwd object typering** 

**Naam attribuutsoort** 

Gebouwd object typering 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** typering **Definitie attribuutsoort** 

Het onderscheid van een GEBOUWD OBJECT in een VERBLIJFSOBJECT dan wel OVERIG GEBOUWD OBJECT. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort is benodigd om bij uitwisseling van gegevens van het objecttype GEBOUWD OBJECT aan te kunnen geven of het een VERBLIJFSOBJECT dan wel een  OVERIG GEBOUWD OBJECT betreft. 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: Verblijfsobject Overig gebouwd object 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status voortgang bouw** 

**Naam attribuutsoort** 

Status voortgang bouw 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** statusVoortgangBouw **Definitie attribuutsoort** 

De fase van de bouw, verbouw of sloop waarin het betreffende GEBOUWD OBJECT zich bevindt 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 30 november 2007 **Toelichting attribuutsoort** 

Aangezien een gebouwd object één of meer malen verbouwd kan worden, kan het attribuut meerdere malen de onderscheiden domeinwaarden verkrijgen. 

De attribuutsoort is gedeeltelijk een samenvoeging van de volgende attribuutsoorten uit het GFO Basisgegevens: 

- Datum aanvang bouw: de datum waarop met het treffen van de ingrijpende voorzieningen aan een vastgoedobject een aanvang is gemaakt, dan wel de datum waarop een start is gemaakt met de aanleg van de fundering; 

- Datum bouw gereed: De datum waarop van gemeentewege is vastgesteld dat de bouwwerkzaamheden van of aan een vastgoedobject conform de vergunning, de melding of de aanschrijving zijn uitgevoerd (onder bouwwerkzaamheden wordt verstaan het plaatsen, het geheel of gedeeltelijk oprichten, vernieuwen of veranderen en het vergroten van het bouwwerk); 

- Datum sloop: de datum waarop het verblijfsobject is gesloopt (onder sloop wordt verstaan dat alle muren, wanden, vloeren en daken zijn verdwenen; de fundering hoeft niet te zijn verwijderd). 

Voor wat betreft de definities van de domeinwaarden is leidend het in de Catalogus BAG in dit verband gestelde. Formaat: AN24 Waardeverzameling: Vergunning aangevraagd Vergunning verleend Bouw of sloop gestart Bouw of sloop gereed Vergunning ingetrokken Ja 

**Domein attribuutsoort Indicatie materiële historie** Ja **Indicatie formele historie** Ja 

|**Aanduiding gebeurtenis**|Nee|
|---|---|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels attribuutsoort**|-|



## **2.15. Gemeente** 

## **Attribuutsoort Gemeentecode** 

**Naam attribuutsoort** 

Gemeentecode 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 92.10 

> **XML-tag attribuutsoort** gemeenteCode 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Een numerieke aanduiding waarmee een Nederlandse gemeente uniek wordt aangeduid 

GFO BG op basis van GBA, Logisch Ontwerp 2.0, 1-10-1994, p. 220 9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: N4 Waardeverzameling: GBA-tabel 33, Gemeententabel. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Gemeentenaam** 

## **Naam attribuutsoort** 

Gemeentenaam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 09.11 

> **XML-tag attribuutsoort** gemeenteNaam 

> **Definitie attribuutsoort** De officiële door de gemeente vastgestelde gemeentenaam. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

9 april 2007 

> **Toelichting attribuutsoort** De definitie is overgenomen uit NEN 5825, 1e druk, december 1991, p. 5. Dit gegeven is terug te vinden in Stuf-WOZ. Het aantal posities is echter overgenomen uit de GBA. Volgens de NEN zijn 24 posities gereserveerd. Voor gemeentenamen met meer dan 24 posities gelden inkortingsregels (zie NEN 5825, 1e druk, december 1991, Bijlage D). 

> **Domein attribuutsoort** Formaat: AN..40 Waardenverzameling: alle bestaande alfanumerieke tekens. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Gemeentenaam NEN** 

> **Naam attribuutsoort** Gemeentenaam NEN 

> **Herkomst attribuutsoort** NEN 5825 (2002) **Code attribuutsoort** 

> **XML-tag attribuutsoort** gemeenteNaamNen 

> **Definitie attribuutsoort** De officieel vastgestelde en waar nodig ingekorte naam van de gemeente 

> **Herkomst definitie attribuutsoort** NEN 5825 (2002) 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het betreft de verkorte naam van de gemeente. 

> **Domein attribuutsoort** Formaat: AN24 Waardenverzameling: gemeentenamen conform NEN 5825 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

**Indicatie authentiek** 

## Gemeentelijk basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Gemeentegeometrie** 

**Naam attribuutsoort** 

Gemeentegeometrie 

> **Herkomst attribuutsoort** IMGeo 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** geometrie 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort Domein attribuutsoort** 

De tweedimensionale geometrische representatie van de omtrekken van het grondgebied van een gemeente. 

KING op basis van IMGeo 

9 april 2007 

- Formaat: GeometrieVlak Waardenverzameling: alle binnen Nederland gelegen waarden van het RD-stelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Het betreft één gesloten vlak. 

## **Attribuutsoort Datum begin geldigheid gemeente** 

> **Naam attribuutsoort** Datum begin geldigheid gemeente 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.20 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop de gemeente is ontstaan. 

## **Herkomst definitie attribuutsoort** GFO BG 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

## 9 april 2007 

In het GFO BG was de attribuutnaam ‘Ingangsdatum gemeente’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

OnvolledigeDatum 

## **Attribuutsoort Datum einde geldigheid gemeente** 

**Naam attribuutsoort** 

Datum einde geldigheid gemeente 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort** 

De datum waarop de gemeente is opgeheven. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

In het GFO BG was de attribuutnaam ‘Einddatum gemeente’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

**Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||



**Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek Regels attribuutsoort** 

Gemeentelijk basisgegeven 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid gemeente’ kan in de registratie worden opgenomen. 

## **Relatiesoort GEMEENTE omvat GEMEENTELIJKE OPENBARE RUIMTE** 

**Naam relatiesoort** 

GEMEENTE omvat GEMEENTELIJKE OPENBARE RUIMTE 

**Herkomst relatiesoort Code relatiesoort** 

KING 

**Definitie relatiesoort** 

De unieke aanduiding van een gemeentelijke openbare ruimte gelegen in een gemeente. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort GEMEENTE omvat WIJK** 

> **Naam relatiesoort** GEMEENTE omvat WIJK 

> **Herkomst relatiesoort** GFO BG 

> **Code relatiesoort** 94.64 

> **Definitie relatiesoort** De gemeente waarin de wijk is gelegen. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** - 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort GEMEENTE omvat WOONPLAATS** 

|**Naam relatiesoort**|GEMEENTE omvat WOONPLAATS|
|---|---|
|**Herkomst relatiesoort**|KING|
|**Code relatiesoort**||
|**Definitie relatiesoort**|De unieke aanduiding van een woonplaats gelegen in een gemeente.|
|**Herkomst definitie relatiesoort**|KING|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|-|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort GEMEENTE is overgegaan in GEMEENTE** 

> **Naam relatiesoort** GEMEENTE is overgegaan in GEMEENTE 

> **Herkomst relatiesoort** KING/GFO BG 

> **Code relatiesoort** 96.20 

## **Definitie relatiesoort** 

De nieuwe GEMEENTE waarin de GEMEENTE bij zijn opheffing cq. na herindeling is overgegaan. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** De relatie biedt de mogelijkheid om aan te geven in welke gemeente de gemeente is overgegaan. In de praktijk kan het voorkomen dat een gemeente in delen overgaan naar meerdere andere gemeenten. Het model voorziet niet in deze situaties teneinde het model eenvoudig te houden en omdat er meestal sprake van is dat het grootste deel over gaat naar één andere gemeente. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** N-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **2.16. Gemeentelijke Openbare Ruimte** 

## **Attribuutsoort Identificatiecode gemeentelijke openbare ruimte** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Identificatiecode gemeentelijke openbare ruimte 

## KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## identificatie 

De unieke aanduiding van een gemeentelijke openbare ruimte. 

## KING 

9 april 2007 

Elke gemeentelijke openbare ruimte waarvan gegevens zijn opgenomen in de registratie, wordt uniek aangeduid door middel van een identificatiecode. Deze identificatiecode bestaat uit de gemeentecode volgens GBA tabel 33 gevolgd door een codering voor de objecttypering en een voor de registrerende gemeente uniek volgnummer. Dit volgnummer kan bijvoorbeeld de veel gehanteerde ‘straatcode’ zijn mits dit straten betreft die door meerdere woonplaatsen kunnen lopen. 

Formaat: AN16 Waardenverzameling: Combinatie van de viercijferige 'gemeentecode' (volgens GBA tabel 33) , de tweecijferige 'objecttypecode’ (waarde: 99)  met een binnen een gemeente uniek (tiencijferig) volgnummer. 

|**Domein attribuutsoort**|Formaat:<br>AN16<br>Waardenverzameling: Comb<br>(volge<br>'objec<br>een g|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijke basisgegeven|
|**Regels attribuutsoort**|-|



## **Attribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

## **XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

> **Definitie attribuutsoort** De gegevens van de GEMEENTELIJKE OPENBARE RUIMTE zoals die zijn opgenomen in de BasisRegistratie Adressen. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 

> **Toelichting attribuutsoort** Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. 

Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 11.10 Naam openbare ruimte 11.11 Indicatie geconstateerde openbare ruimte 11.16 Type openbare ruimte 11.19 Status openbare ruimte **Domein attribuutsoort** n.v.t **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum **Indicatie in onderzoek** Ja **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Naam openbare ruimte** 

> **Naam attribuutsoort** Naam openbare ruimte 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.10 

> **XML-tag attribuutsoort** openbareRuimteNaam 

> **Definitie attribuutsoort** Een door het bevoegde gemeentelijke orgaan aan een GEMEENTELIJKE OPENBARE RUIMTE toegekende benaming 

> **Herkomst definitie attribuutsoort** KING op basis van BAG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort wordt in de BAG gespecificeerd bij objecttype OPENBARE RUIMTE. In RSGB wordt dit attribuutsoort gespecificeerd bij GEMEENTELIJKE OPENBARE RUIMTE en overerft OPENBARE RUIMTE dit attribuutsoort van GEMEENTELIJKE OPENBARE RUIMTE. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Indicatie geconstateerde openbare ruimte** 

**Naam attribuutsoort** 

Indicatie geconstateerde openbare ruimte 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.11 

> **XML-tag attribuutsoort** geconstateerd 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname 

**Herkomst definitie attribuutsoort** 

BAG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort wordt in de BAG gespecificeerd bij objecttype OPENBARE RUIMTE. In RSGB wordt dit attribuutsoort gespecificeerd bij GEMEENTELIJKE OPENBARE RUIMTE en overerft OPENBARE RUIMTE dit attribuutsoort van GEMEENTELIJKE OPENBARE RUIMTE. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

1-1 

**Indicatie authentiek** 

Niet authentiek landelijk basis gegeven 

## **Attribuutsoort Type openbare ruimte** 

> **Naam attribuutsoort** Type openbare ruimte 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.16 

> **XML-tag attribuutsoort** type 

> **Definitie attribuutsoort** De aard van de als zodanig benoemde GEMEENTELIJKE OPENBARE RUIMTE. 

> **Herkomst definitie attribuutsoort** KING op basis van BAG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Dit attribuutsoort wordt in de BAG gespecificeerd bij objecttype OPENBARE RUIMTE. In RSGB wordt dit attribuutsoort gespecificeerd bij GEMEENTELIJKE OPENBARE RUIMTE en overerft OPENBARE RUIMTE dit attribuutsoort van GEMEENTELIJKE OPENBARE RUIMTE. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Status openbare ruimte** 

> **Naam attribuutsoort** Status openbare ruimte 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.19 

> **XML-tag attribuutsoort** status 

> **Definitie attribuutsoort** De fase van de levenscyclus van een GEMEENTELIJKE OPENBARE RUIMTE, waarin de betreffende GEMEENTELIJKE OPENBARE RUIMTE zich bevindt 

> **Herkomst definitie attribuutsoort** KING op basis van BAG 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

9 april 2007 

Dit attribuutsoort is in de BAG gespecificeerd bij het objecttype OPENBARE RUIMTE. In RSGB wordt dit attribuutsoort gespecificeerd bij GEMEENTELIJKE OPENBARE RUIMTE en overerft OPENBARE RUIMTE dit attribuutsoort van GEMEENTELIJKE OPENBARE RUIMTE. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Geometrie gemeentelijke openbare ruimte** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort** 

Geometrie gemeentelijke openbare ruimte 

IMGeo 

- 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De tweedimensionale geometrische representatie van de omtrekken van een GEMEENTELIJKE OPENBARE RUIMTE 

## KING 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een openbare ruimte. 

**Domein attribuutsoort** 

Formaat: Geometrie (GML) Waardenverzameling: Vlakgeometrie: aanduiding van het type geometrie (vlak of multivlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RD-stelsel. 

## **Indicatie materiële historie** 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De begrenzing wordt afgeleid uit formeel vastgestelde documenten en hoeft daarom niet als zodanig ingemeten te worden in het veld. 

## **Attribuutsoort Datum begin geldigheid Gemeentelijke Openbare Ruimte** 

|**Naam attribuutsoort**|Datum begin geldigheid gemeentelijke openbare ruimte|Datum begin geldigheid gemeentelijke openbare ruimte|
|---|---|---|
|**Herkomst attribuutsoort**|KING||
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|ingangsdatumObject||
|**Definitie attribuutsoort**|De datum waarop de|GEMEENTELIJKE OPENBARE RUIMTE formeel is|
||benoemd.||
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|-||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|N||
|**Indicatie formele historie**|J||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Attribuutsoort Datum einde geldigheid Gemeentelijke Openbare Ruimte** 

> **Naam attribuutsoort** Datum einde geldigheid gemeentelijke openbare ruimte 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

KING 

einddatumObject 

De datum waarop formeel is besloten de GEMEENTELIJKE OPENBARE RUIMTE niet langer te laten bestaan. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. 

## **Attribuutsoort Straatnaam** 

> **Naam attribuutsoort** Straatnaam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 11.10 

> **XML-tag attribuutsoort** straatnaam **Definitie attribuutsoort** 

De officiële straatnaam zoals door het bevoegd gemeentelijk orgaan is vastgesteld, zo nodig ingekort conform de specificaties van de NEN 5825. KING o.b.v. GFO BG 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Voor straatnamen langer dan 24 posities gelden inkortingsregels (deze staan bekend als de BOCO-norm en zijn vastgelegd in NEN 5825, 1e druk, december 1991, Bijlage A, pp. 9-11). Er staat ook een definitie in NEN 5825: De officiële door de gemeente vastgestelde naam van een straat. Deze definitie is overgenomen in STUF-WOZ. De hier gehanteerde schrijfwijze kan afwijken van de PTT-schrijfwijze. 

> **Domein attribuutsoort** Formaat: AN24 Waardenverzameling: alle alfanumrieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort GEMEENTELIJKE OPENBARE RUIMTE ligt in GEMEENTE** 

> **Naam relatiesoort** GEMEENTELIJKE OPENBARE RUIMTE ligt in GEMEENTE 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** - 

> **Definitie relatiesoort** De GEMEENTE waarin de GEMEENTELIJKE OPENBARE RUIMTE is gelegen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Deze relatie is de tegenhanger van de relatie GEMEENTE omvat GEMEENTELIJKE OPENBARE RUIMTE. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort GEMEENTELIJKE OPENBARE RUIMTE heeft OPENBARE RUIMTE** 

> **Naam relatiesoort** GEMEENTELIJKE OPENBARE RUIMTE heeft OPENBARE RUIMTE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De OPENBARE RUIMTEn die deel uitmaken van de GEMEENTELIJKE 

De OPENBARE RUIMTEn die deel uitmaken van de GEMEENTELIJKE OPENBARE RUIMTE. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Deze relatie is de tegenhanger van OPENBARE RUIMTE maakt deel uit van GEMEENTELIJKE OPENBARE RUIMTE. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **2.17. Huishouden** 

## **Attribuutsoort Huishoudennummer** 

**Naam attribuutsoort** 

## Huishoudennummer 

**Herkomst attribuutsoort** 

GFO BG 

**Code attribuutsoort XML-tag attribuutsoort** 

96.28 

## nummer 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Uniek identificerend administratienummer van een huishouden zoals toegekend door de gemeente waarin het huishouden woonachtig is. GFO GB 

9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: N12 Waardenverzameling: 

Combinatie van de viercijferige 'gemeentecode' (volgens GBA tabel 33) en een binnen een gemeente uniek achtcijferig objectvolgnummer. 

N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Huishoudensoort** 

> **Naam attribuutsoort** Huishoudensoort 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.69 

> **XML-tag attribuutsoort** soort 

> **Definitie attribuutsoort** Typering van het huishouden naar grootte en verbondenheid. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

9 april 2007 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

Voor de definities van institutioneel huishouden en particulier huishouden: zie de toelichting bij het objecttype Huishouden. Onder Thuiswonende kinderen wordt verstaan: alle in het huishouden van hun ouder(s) aanwezige eigen, pleeg-, stief- of adoptiekinderen die ongehuwd zijn en zelf geen kinderen hebben (CBS, Huishoudensprognose 1996). In een adresseerbaar object kunnen één of meer huishoudens wonen. In de tabel worden de huishoudens gekarakteriseerd, uitgaande van de CBS-Huishoudensprognose. Tot de categorie Overig particulier huishouden behoren bijvoorbeeld: een woongroep, studenten die gezamenlijk een huishouden vormen, een kamerbewoner die in zijn eigen onderhoud voorziet, twee zussen die samenwonen. 

Formaat: N2 Waardenverzameling: 1 = institutioneel huishouden 2 = alleenstaand (inclusief andere personen die in hetzelfde object wonen, maar een eigen huishouding voeren) 3 = 2 personen, vaste partners, geen thuiswonende kinderen 4 = 2 personen, vaste partners, een of meer thuiswonende kinderen 5 = eenoudergezin, ouder met een of meer thuiswonende kinderen 

6 = overig particulier huishouden (samenwoning van personen die geen partnerrelatie onderhouden of een ouder-kindrelatie hebben, maar wel gezamenlijk een huishouding voeren) 

||6 = ov<br>v<br>o<br>h<br>h|
|---|---|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijke basisgegeven|
|**Regels attribuutsoort**|-|



## **Attribuutsoort Huishoudengrootte** 

|**Naam attribuutsoort**|Huishoudengrootte|
|---|---|
|**Herkomst attribuutsoort**|GFO BG|
|**Code attribuutsoort**|96.07|
|**XML-tag attribuutsoort**|grootte|



## **Definitie attribuutsoort** 

Het aantal personen waaruit het huishouden bestaat. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: N2 Waardenverzameling: 1 - 99 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum begin geldigheid huishouden** 

> **Naam attribuutsoort** Datum begin geldigheid huishouden 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop het HUISHOUDEN is ontstaan. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

**Indicatie authentiek Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Datum einde geldigheid huishouden** 

> **Naam attribuutsoort** Datum einde geldigheid huishouden 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het HUISHOUDEN is komen te vervallen. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. 

## **Relatiesoort HUISHOUDEN is gehuisvest in VERBLIJFSOBJECT** 

> **Naam relatiesoort** HUISHOUDEN is gehuisvest in VERBLIJFSOBJECT 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 96.01 

> **Definitie relatiesoort** Het VERBLIJFSOBJECT waarin het HUISHOUDEN woont. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

## **Toelichting relatiesoort** 

Een huishouden is ‘woonachtig’ in één verblijfs-object, standplaats of ligplaats. In één verblijfsobject kunnen nul, één of meer huishoudens ‘wonen’. 

De relatie is de tegenhanger van het relatiesoort VERBLIJFSOBJECT is huisvesting van HUISHOUDEN. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding** Nee **strijdigheid/nietigheid** 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

De relatie moet aanwezig zijn indien de relatieS HUISHOUDEN is gehuisvest op STANDPLAATS en HUISHOUDEN is gehuisvest op LIGPLAATS niet aanwezig zijn. 

## _**Relatiesoort HUISHOUDEN is gehuisvest op LIGPLAATS**_ 

> **Naam relatiesoort** HUISHOUDEN is gehuisvest op LIGPLAATS 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 96.01 

> **Definitie relatiesoort** De LIGPLAATS waarop het HUISHOUDEN woont. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Een huishouden is ‘woonachtig’ in één verblijfs-object, standplaats of ligplaats. In één dergelijk object kunnen nul, één of meer huishoudens ‘wonen’. 

De relatie is de tegenhanger van het relatiesoort LIGPLAATS is huisvesting van HUISHOUDEN. 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding** Nee **strijdigheid/nietigheid** 

**Indicatie kardinaliteit** 

0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** De relatie moet aanwezig zijn indien de relaties HUISHOUDEN is gehuisvest in VERBLIJFSOBJECT en HUISHOUDEN is gehuisvest op STANDPLAATS niet aanwezig zijn. 

## **Relatiesoort HUISHOUDEN is gehuisvest op STANDPLAATS** 

> **Naam relatiesoort** HUISHOUDEN is gehuisvest op STANDPLAATS 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 96.01 

> **Definitie relatiesoort** De STANDPLAATS waarop het HUISHOUDEN woont. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Een huishouden is ‘woonachtig’ in één verblijfs-object, standplaats of ligplaats. In één dergelijk object kunnen nul, één of meer huishoudens ‘wonen’. 

De relatie is de tegenhanger van het relatiesoort STANDPLAATS is huisvesting van HUISHOUDEN. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding** Nee **strijdigheid/nietigheid** 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** De relatie moet aanwezig zijn indien de relaties HUISHOUDEN is gehuisvest in VERBLIJFSOBJECT en HUISHOUDEN is gehuisvest op LIGPLAATS niet aanwezig zijn. 

## **Relatiesoort HUISHOUDEN heeft HUISHOUDENRELATIEs** 

> **Naam relatiesoort** HUISHOUDEN heeft HUISHOUDENRELATIEs 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 94.40 

**Definitie relatiesoort** 

Een verwijzing die aangeeft uit welke huishoudenrelaties een huishouden bestaat. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Uit deze relatie(s) kan worden afgeleid uit hoeveel personen een huishouden bestaat. De relatie is de tegenhanger van het relatiesoort HUISHOUDENRELATIE hoort bij HUISHOUDEN. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

## **2.18. Huishoudenrelatie** 

## **Attribuutsoort Huishoudenrelatiecode** 

**Naam attribuutsoort** 

Huishoudenrelatiecode 

**Herkomst attribuutsoort** 

GFO BG 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

96.32 

code 

De positie die de persoon binnen het huishouden inneemt. 

## GFO BG 

## 9 april 2007 

Het hoofd is degene die als vertegenwoordiger van het huishouden wordt aangesproken. 

Formaat: N1 Waardenverzameling: 1 = hoofd van het huishouden 2 = partner van het hoofd van het huishouden 3 = kind 4 = overig lid van het huishouden 

Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Relatiesoort HUISHOUDENRELATIE betreft INGESCHREVEN PERSOON** 

> **Naam relatiesoort** HUISHOUDENRELATIE betreft INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 94.40 

> **Definitie relatiesoort** De INGESCHREVEN PERSOON die de HUISHOUDENRELATIE heeft 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 1 november 2008 

## **Toelichting relatiesoort** 

De relatie is de tegenhanger van het relatiesoort INGESCHREVEN PERSOON heeft HUISHOUDENRELATIE. 

> **Indicatie materiële historie** nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort HUISHOUDENRELATIE hoort bij HUISHOUDEN** 

> **Naam relatiesoort** HUISHOUDENRELATIE hoort bij HUISHOUDEN 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 94.40 

> **Definitie relatiesoort** Het HUISHOUDEN waarvan de HUISHOUDENRELATIE deel uit maakt. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatie is de tegenhanger van HUISHOUDEN heeft HUISHOUDENRELATIEs. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

## **2.19. Huwelijk/geregistreerd partnerschap** 

## **Attribuutsoort Soort verbintenis** 

> **Naam attribuutsoort** Soort verbintenis 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 05.15.10 

> **XML-tag attribuutsoort** soortVerbintenis 

> **Definitie attribuutsoort** Een aanduiding voor de soort verbintenis die is aangegaan. 

> **Herkomst definitie attribuutsoort** GBA 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Zie de GBA 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Aktegemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** 

## **Groepattribuutsoort Huwelijkssluiting/aangaan geregistreerd partnerschap** 

**Naam attribuutsoort** 

Huwelijkssluiting/aangaan geregistreerd partnerschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 05.06 

> **Definitie attribuutsoort** Gegevens over het gesloten huwelijk of het aangegane geregistreerd partnerschap. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Datum huwelijkssluiting/aangaan geregistreerd partnerschap Plaats huwelijkssluiting/aangaan geregistreerd partnerschap en de volgende relatiesoort: 

HUWELIJK/GEREGISTREERD PARTNERSCHAP is gesloten/aangegaan in LAND. 

Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Aktegemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum huwelijkssluiting/aangaan geregistreerd partnerschap** 

> **Naam attribuutsoort** Datum huwelijkssluiting/aangaan geregistreerd partnerschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 06.06.10 

> **XML-tag attribuutsoort** datumSluiting 

> **Definitie attribuutsoort** De datum waarop het huwelijk is voltrokken of het partnerschap is aangegaan. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Huwelijkssluiting/aangaan geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Plaats huwelijkssluiting/aangaan geregistreerd partnerschap** 

> **Naam attribuutsoort** Plaats huwelijkssluiting/aangaan geregistreerd partnerschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 05.06.20 

**XML-tag attribuutsoort** 

## plaatsSluiting 

## **Definitie attribuutsoort** 

> **Definitie attribuutsoort** De code uit de GBA/Gemeententabel of een buitenlandse plaats of een plaatsbepaling, die aangeeft waar het huwelijk is voltrokken of het partnerschap is aangegaan. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Huwelijkssluiting/aangaan geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Groepattribuutsoort Ontbinding huwelijk/geregistreerd partnerschap** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

Ontbinding huwelijk/geregistreerd partnerschap 

GBA 

05.07 

Gegevens over het ontbonden huwelijk of geregistreerd partnerschap. 

## GBA 

## 1 mei 2008 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Datum ontbinding huwelijk/geregistreerd partnerschap Plaats ontbinding huwelijk/geregistreerd partnerschap Reden ontbinding huwelijk/geregistreerd partnerschap en de volgende relatiesoort: 

HUWELIJK/GEREGISTREERD PARTNERSCHAP is ontbonden in LAND. 

Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Ja 

Nee 

Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum ontbinding huwelijk/geregistreerd partnerschap** 

> **Naam attribuutsoort** Datum ontbinding huwelijk/geregistreerd partnerschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 05.07.10 

> **XML-tag attribuutsoort** datumOntbinding 

> **Definitie attribuutsoort** De datum waarop het huwelijk/geregistreerd partnerschap is ontbonden of nietig verklaard. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Ontbinding huwelijk/geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Plaats ontbinding huwelijk/geregistreerd partnerschap** 

**Naam attribuutsoort** 

Plaats ontbinding huwelijk/geregistreerd partnerschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 05.07.20 

> **XML-tag attribuutsoort** plaatsOntbinding 

> **Definitie attribuutsoort** De code uit de GBA-Gemeententabel of een buitenlandse plaats of een plaatsbepaling die aangeeft waar het huwelijk/ geregistreerd partnerschap is ontbonden of nietig verklaard. 

> **Datum opname attribuutsoort** 9 april 2007 

## **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Ontbinding huwelijk/geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Reden ontbinding huwelijk/geregistreerd partnerschap** 

|**Naam attribuutsoort**|Reden ontbinding huwelijk/geregistreerd partnerschap|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|05.07.40|
|**XML-tag attribuutsoort**|redenOntbinding|
|**Definitie attribuutsoort**|De code uit de Tabel Reden ontbinding/|
||nietigverklaring huwelijk/geregistreerd partnerschap, die aangeeft om|
||welke reden het huwelijk/geregistreerd partnerschap is ontbonden of|
||nietig verklaard.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort Ontbinding|
||huwelijk/geregistreerd partnerschap.|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Relatiesoort PARTNER-RELATIE betreft twee INGESCHREVEN PERSOONen** 

> **Naam relatiesoort** PARTNER -RELATIE betreft twee INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 05.01 

> **Definitie relatiesoort** De INGESCHREVEN PERSOON bij wie de PARTNER-RELATIE is geregistreerd. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) in categorie 05 (Huwelijk/geregistreerd partnerschap) in de GBA. De relatie is de tegenhanger van INGESCHREVEN PERSOON heeft HUWELIJK/GEREGISTREERD PARTNERSCHAPpen. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Aktegemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 2-2 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort HUWELIJK/GEREGISTREERD PARTNERSCHAP is gesloten/aangegaan in LAND** 

> **Naam relatiesoort** HUWELIJK/GEREGISTREERD PARTNERSCHAP is gesloten/aangegaan in LAND 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 05.06.30 

> **Definitie relatiesoort** Het LAND waar het huwelijk is voltrokken of het partnerschap is aangegaan. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

Het LAND waar het huwelijk is voltrokken of het partnerschap is aangegaan. 

> **Toelichting relatiesoort** In afwijking van het corresponderende GBA-attribuutsoort ‘Land huwelijkssluiting/aangaan geregistreerd partnerschap’ wordt niet de landcode vastgelegd maar de de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 06.30. De relatiesoort maakt deel uit van het groepattribuutsoort Huwelijkssluiting/aangaan geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort HUWELIJK/GEREGISTREERD PARTNERSCHAP is ontbonden in LAND** 

**Naam relatiesoort Herkomst relatiesoort** KING **Code relatiesoort** 05.07.30 **Definitie relatiesoort** 

HUWELIJK/GEREGISTREERD PARTNERSCHAP is ontbonden in LAND 

Het LAND waar het huwelijk/geregistreerd partnerschap is ontbonden of nietig verklaard. 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

KING op basis van GBA 

1 november 2008 

In afwijking van het corresponderende GBA-attribuutsoort ‘Land ontbinding huwelijk/geregistreerd partnerschap’ wordt niet de landcode vastgelegd maar de de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 07.30. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Ontbinding huwelijk/geregistreerd partnerschap. Zie verder de toelichting in de GBA. 

||vast<br>betr<br>Het<br>huw<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



**Indicatie kardinaliteit Indicatie authentiek Regels relatiesoort** 

1-1 Niet authentiek landelijk basisgegeven 

## **2.20. Ingeschreven niet-natuurlijk persoon** 

## **Attribuutsoort NNP-ID** 

**Naam attribuutsoort** 

## NNP-ID 

**Herkomst attribuutsoort** 

NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

## nnpId 

Een in het handelsregister over een NIET-NATUURLIJK PERSOON opgenomen, door de Kamer van Koophandel toegekend, uniek nummer. De attribuutsoort kent onder meer historie omdat het mogelijk is dat de NNP-ID van een ingeschreven niet-natuurlijk persoon wijzigt, met name vanwege ‘ambtelijke’ correcties. 

KING op basis van Catalogus NHR 

9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: N9 Waardenverzameling: alle cijfers 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Rechtsvorm** 

**Naam attribuutsoort** 

Rechtsvorm 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** rechtsvorm 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

Aanduiding van de vorm die in rechte bekend is van de INGESCHREVEN NIET-NATUURLIJKE PERSOON 

KING op basis van GFO BG 

9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

|**Domein attribuutsoort**|Formaat:|AN100|
|---|---|---|
||Waardenverzameling:|door de Kamers van Koophandel vastgestelde|
|||rechtsvormen van binnelandse rechtspersonen en|
|||samenwerkingsverbanden|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Authentiek gegeven||



## **Attribuutsoort Statutaire zetel** 

> **Naam attribuutsoort** Statutaire zetel 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** statutaireZetel **Definitie attribuutsoort** 

De plaats waar de INGESCHREVEN NIET-NATUURLIJKE PERSOON volgens haar statuten gevestigd is. 

**Herkomst definitie attribuutsoort** 

KING 

> **Datum opname attribuutsoort** 9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum voortzetting** 

**Naam attribuutsoort** 

Datum voortzetting 

|**Herkomst attribuutsoort**|NHR||
|---|---|---|
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|datumVoortzetting||
|**Definitie attribuutsoort**|{nog niet in NHR uitgewerkt||
|**Herkomst definitie attribuutsoort**|||
|**Datum opname attribuutsoort**|1 mei 2008||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Authentiek gegeven||



## **Regels attribuutsoort** 

## **Relatiesoort INGESCHREVEN NIET-NATUURLIJK PERSOON heeft FUNCTIONARIS** 

**Naam relatiesoort** 

INGESCHREVEN NIET-NATUURLIJK PERSOON heeft FUNCTIONARIS 

**Herkomst relatiesoort** 

KING op basis van NHR 

**Code relatiesoort** 

**Definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

{nog niet in NHR uitgewerkt 

9 april 2007 

De relatie is de tegenhanger van FUNCTIONARIS van INGESCHREVEN NIET-NATUURLIJK PERSOON. 

Het betreft de verwijzing naar de relaties die aangeven welke subjecten als functionaris namens deze persoon optreden. Zie verder de toelichting bij het objecttype FUNCTIONARIS. 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven indien een gerelateerd subject zijnde de functionaris een maat of vennoot (met uitzondering van de commanditaire vennoten) betreft en de niet-natuurlijke persoon een maatschap, een vennootschap onder firma of een commanditaire vennootschap is. Anders een niet authentiek landelijk basisgegeven. 

## **2.21. Ingeschreven persoon** 

## **Groepattribuutsoort Identificatienummers** 

> **Naam attribuutsoort** Identificatienummers 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01. 01 

> **Definitie attribuutsoort** Gegevens over de identificatienummers van de INGESCHREVEN PERSOON. 

> **Datum opname attribuutsoort** 18 november 2008 

> **Toelichting attribuutsoort** Het groepattribuutsoort is afgeleid van groep 01.01 in de GBA. Het maakt deel uit van het groepattribuutsoort Natuurlijk persoon . Persoonsgegevens. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Burgerservicenummer** 

**Naam attribuutsoort** 

Burgerservicenummer 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01. 01.20 

> **XML-tag attribuutsoort** bsn **Definitie attribuutsoort** 

Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Elk ingeschreven persoon heeft een BSN, een nummer dat de persoon uniek identificeert in overheidsadministraties. 

De attribuutsoort kent onder meer historie omdat het mogelijk is dat het Burgerservicenummer van een persoon wijzigt, met name vanwege ambtelijke correcties. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Identificatienummers. Zie verder de toelichting in de GBA. 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Attribuutsoort A-nummer** 

**Naam attribuutsoort** 

A-nummer 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.01.10 

> **XML-tag attribuutsoort** a-nummer 

> **Definitie attribuutsoort** Het administratienummer, bedoeld in artikel 50 van de Wet GBA. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Identificatienummers. Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Geboorteplaats** 

**Naam attribuutsoort** 

Geboorteplaats 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.03.20 

> **XML-tag attribuutsoort** geboorteplaats 

## **Definitie attribuutsoort** 

|||
|---|---|
|**Definitie attribuutsoort**|De naam van de Nederlandse gemeente of een buitenlandse plaats of|
||een plaatsbepaling, die aangeeft waar de persoon is geboren.|
|**Herkomst definitie attribuutsoort**|KING op basis van GBA|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|In afwijking van het corresponderende GBA-attribuutsoort wordt voor|
||Nederlandse gemeenten niet de code vastgelegd maar de|
||gemeentenaam.|
||Het attribuutsoort maakt deel uit van het groepattribuutsoort Natuurlijk|
||persoon . Persoonsgegevens . Geboorte.|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Overlijdenplaats** 

|**Naam attribuutsoort**|Overlijdenplaats|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|06.08.20|
|**XML-tag attribuutsoort**|overlijdenplaats|
|**Definitie attribuutsoort**|De naam van de Nederlandse gemeente of een buitenlandse plaats of|
||een plaatsbepaling, die aangeeft waar de persoon is overleden.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|In afwijking van het corresponderende GBA-attribuutsoort wordt voor|
||Nederlandse gemeenten niet de code vastgelegd maar de|
||gemeentenaam.|
||Het attribuutsoort maakt deel uit van het groepattribuutsoort Natuurlijk|
||persoon . Overlijden.|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|



> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Groepattribuutsoort Nationaliteit** 

> **Naam attribuutsoort** Nationaliteit 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 04 **Definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Gegevens over de nationaliteit. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Reden verkrijging Nederlandse nat. Reden verlies Nederlandse nat. Aanduiding bijzonder Nederlanderschap en de relatiesoort: 

INGESCHREVEN PERSOON heeft NATIONALITEIT. 

De groepattribuutsoort is samengesteld overeenkomstig categorie 04 in de GBA. Daarin kan de categorie meerdere malen voorkomen, de attribuutsoorten binnen de groep telkens slechts één maal. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels attribuutsoort** Zie GBA LO, Beschrijving categorie 04 

## **Attribuutsoort Reden verkrijging Nederlandse nationaliteit** 

> **Naam attribuutsoort** Reden verkrijging Nederlandse nationaliteit 

> **Herkomst attribuutsoort** GBA 

**Code attribuutsoort** 

## 04.63.10 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

## redenVerkrijging 

Een code die aanduidt op grond waarvan de ingeschrevene de Nederlandse nationaliteit verkregen heeft. 

9 april 2007 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Nationaliteit. Zie verder de toelichting in de GBA. 

## Nee 

Nee 

Nee 

Nee 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek** 

Nee 

0-1 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Reden verlies Nederlandse nationaliteit** 

**Naam attribuutsoort** 

Reden verlies Nederlandse nationaliteit 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 04.64.10 

> **XML-tag attribuutsoort** redenVerlies **Definitie attribuutsoort** 

Een code die aanduidt op grond waarvan de ingeschrevene de Nederlandse nationaliteit verloren heeft. 

|**Definitie attribuutsoort**|Een code die aanduidt op grond waarv<br>Nederlandse nationaliteit verloren heeft|
|---|---|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van he|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



Het attribuutsoort maakt deel uit van het groepattribuutsoort Nationaliteit. Zie verder de toelichting in de GBA. 

## **Attribuutsoort Aanduiding bijzonder Nederlanderschap** 

**Naam attribuutsoort** 

Aanduiding bijzonder Nederlanderschap 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 04.65.10 

> **XML-tag attribuutsoort** aanduidingBijzonderNederlanderschap **Definitie attribuutsoort** 

> **Definitie attribuutsoort** Een aanduiding die of aangeeft dat de ingeschrevene behandeld wordt als Nederlander, of dat door de rechter is vastgesteld dat de ingeschrevene niet de Nederlandse nationaliteit bezit. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Nationaliteit. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Nationaliteit. Zie verder de toelichting in de GBA. 

## **Attribuutsoort Datum verkrijging nationaliteit** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum verkrijging nationaliteit 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

datumVerkrijging 

De datum waarop de Nederlandse nationaliteit van een natuurlijk persoon zijn geldigheid heeft verkregen. 

KING 

**Datum opname attribuutsoort** 

2 februari 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: Onvolledige datum Waardenverzameling: 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee\ 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit  de begindatum van de laatst bekende nationaliteit in het gelijknamige groepattribuutsoort. 

## **Attribuutsoort Datum verlies nationaliteit** 

> **Naam attribuutsoort** Datum verlies nationaliteit 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumVerlies 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

De datum waarop de Nederlandse nationaliteit van een natuurlijk persoon zijn geldigheid heeft verloren. 

KING 

2 februari 2009 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee\ 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit  de einddatum van de laatst bekende nationaliteit in de gelijknamige groepattribuut. 

## **Groepattribuutsoort Verblijfplaats** 

**Naam attribuutsoort Herkomst attribuutsoort Code attribuutsoort** 08 **Definitie attribuutsoort** 

Verblijfplaats 

GBA 

De gegevens over het verblijf en adres van de INGESCHREVEN PERSOON 

> **Datum opname attribuutsoort** 18 november 2008 **Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende (groep)attribuutsoorten: 

08.09.10 Gemeente van inschrijving 08.12 Woonadreslocatie 08.10.10 Adresherkomst 

en de volgende relatiesoorten: 

08.11.80 Ingeschreven persoon verblijft in of op ADRESSEERBAAR OBJECT 

08.11.90 Is ingeschreven op NUMMERAANDUIDING 08.13.10 Ingeschreven persoon is vertrokken naar LAND. 08.14.10 Ingeschreven persoon is ingeschreven vanuit LAND. Het groepattribuutsoort is ontleend aan categorie 08 in de GBA (LO 3.6). Daarin betreft een verblijfplaats van een persoon telkens een woon- of een briefadres. Met het groepattribuutsoort Verblijfsplaats modelleren we v.w.b. de GBA alleen verblijfplaatsen zijnde woonadressen. GBAverblijfplaatsen zijnde briefadressen modelleren we als correspondentieadres bij SUBJECT.  Indien in de GBA bij een persoon alleen een briefadres is opgenomen, kan een andere bron toch beschikken over een woonadres. Vandaar dat met de attribuutsoort Adresherkomst wordt aangegeven of de verblijfplaats al dan niet als authentieke bron de GBA heeft. Zie ook de toelichting  bij laatstgenoemd attribuutsoort. 

||adres bij SUBJECT.  Indien in de GBA bij een persoon alleen een<br>briefadres is opgenomen, kan een andere bron toch beschikken over e<br>woonadres. Vandaar dat met de attribuutsoort Adresherkomst wordt<br>aangegeven of de verblijfplaats al dan niet als authentieke bron de GB<br>heeft. Zie ook de toelichting  bij laatstgenoemd attribuutsoort.|
|---|---|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven indien ontleend aan de GBA,|
||anders gemeentelijk basisgegeven (zie attribuutsoort Adresherkomst).|



## **Attribuutsoort Gemeente van inschrijving** 

**Naam attribuutsoort** 

Gemeente van inschrijving 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 08.09.10 

> **XML-tag attribuutsoort** gemeenteVanInschrijving **Definitie attribuutsoort** 

> **Definitie attribuutsoort** Een code die aangeeft in welke gemeente de PL zich bevindt of de gemeente waarnaar de PL is uitgeschreven of de gemeente waar de PL voor de eerste keer is opgenomen. 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Verbljfsplaats .Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Groepattribuutsoort Woonadreslocatie** 

**Naam attribuutsoort** 

Woonadreslocatie 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 08.12 **Definitie attribuutsoort** 

Gegevens over de plaatsbepaling van een adres indien het niet aan te duiden is als adres. 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoort: 

Locatiebeschrijving 

en de volgende relatiesoort: 

## INGESCHREVEN PERSOON verblijft op locatie in WOONPLAATS 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Verblijfsplaats Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels attribuutsoort** Indien het groepattribuutsoort niet van waarden voorzien is dan is één van de relaties INGESCHREVEN PERSOON verblijft in VERBLIJFSOBJECT, INGESCHREVEN PERSOON verblijft op AUTHENTIEK TERREIN of SUBJECT heeft als correspondentie- of aanschrijvingsadres    ADRESSEERBAAR OBJECT AANDUIDING aanwezig (het zgn. briefadres in GBA-terminologie). 

## **Attribuutsoort Locatiebeschrijving** 

|**Naam attribuutsoort**|Locatie beschrijving|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|08.12.10|
|**XML-tag attribuutsoort**|locatiebeschrijving|
|**Definitie attribuutsoort**|Een geheel of gedeeltelijke omschrijving van de ligging van een object,|
||indien dit niet kan worden aangegeven in het groepattribuutsoort|
||Woonadres.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort|
||Woonadreslocatie (dat weer deel uitmaakt van het groepattribuutsoort|
||Verblijfsplaats).|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Attribuutsoort Adresherkomst** 

**Naam attribuutsoort** 

## Adresherkomst 

**Herkomst attribuutsoort** 

KING 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** adresHerkomst 

> **Definitie attribuutsoort** Aanduiding welk adres van de INGESCHREVEN PERSOON ontleend is aan de GBA: het woonadres of het correspondentie-adres 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsoort is ontleend aan het GBA-attribuut ‘Functie adres’. 

De attribuutsoort is ontleend aan het GBA-attribuut ‘Functie adres’. Daarmee wordt aangegeven of het verblijfsadres in de GBA de functie heeft van woonadres of van briefadres. 

Een briefadres wordt in het RSGB overgenomen als correspondentieadres bij Subject, een woonadres als Woonadres of Woonadreslocatie bij Ingeschreven persoon. Indien het uit de GBA overgenomen adres een briefadres betreft, dan kan uit een andere bron het Woonadres of de Woonadreslocatie overgenomen zijn. Evenzo, indien het uit de GBA overgenomen adres een woonadres betreft, dan kan uit een andere bron het Correspondentie-adres overgenomen zijn. Het attribuutsoort maakt deel uit van het groepattribuutsoort Verblijfsplaats **Domein attribuutsoort** Formaat: AN1 Waardenverzameling: B (=brief- cq. correspondentie-adres is ontleend aan de GBA) W (=woonadres cq. woonadreslocatie is ontleend aan de GBA) **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Datum begin geldigheid verblijfplaats** 

> **Naam attribuutsoort** Datum begin geldigheid verblijfplaats 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

begindatumVerblijf 

**Definitie attribuutsoort** 

> **Definitie attribuutsoort** De datum waarop de INGESCHREVEN PERSOON is ingeschreven op zijn of haar laatst bekende verblijfsplaats 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 30 maart 2009 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit de datum begin geldigheid van het laatst bekende voorkomen van het groepattribuut Verblijfsplaats 

## **Attribuutsoort Datum inschrijving in gemeente** 

**Naam attribuutsoort** 

Datum inschrijving in gemeente 

> **Herkomst attribuutsoort** GFO-BG 

> **Code attribuutsoort** 09.20 

> **XML-tag attribuutsoort** datumInschrijving **Definitie attribuutsoort** 

Bij inschrijving op grond van een aangifte door de burger van zijn vestiging in een (volgende) gemeente is dit de aangiftedatum. Bij inschrijving op grond van een geboorte-akte is dit de geboortedatum. Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen van ambtshalve opneming mededeling is gedaan. 

**Herkomst definitie attribuutsoort** 

GFO-BG 

**Datum opname attribuutsoort** 

2 februari 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: Onvolledige datum Waardenverzameling: Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit de datum begin geldigheid van het attribuut Gemeente van inschrijving 

## **Attribuutsoort Datum vestiging in Nederland** 

> **Naam attribuutsoort** Datum vestiging in Nederland 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 14.20 

> **XML-tag attribuutsoort** datumVestigingInNederland **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

Datum vestiging in Nederland 

De datum van de inschrijving in Nederland. 

Zogenaamd afleidbaar gegeven (zie regels attribuutsoort). Bij ambtshalve inschrijving is dit de datum waarop de betrokkene schriftelijk van het voornemen tot ambtshalve inschrijving mededeling is gedaan. In andere gevallen is dit de datum waarop de aangifte is ontvangen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het gegeven is afleidbaar uit de materiele historie van het eerste woonadres, woonadreslocatie of correspondentieadres van een ononderbroken reeks binnenlandse adressen. 

## **Attribuutsoort Datum vertrek uit Nederland** 

## **Naam attribuutsoort** 

Datum vertrek uit Nederland 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 13.20 

> **XML-tag attribuutsoort** datumVertrekUitNederland **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

De datum van het vertrek naar het buitenland. 

Zogenaamd afleidbaar gegeven (zie regels attribuutsoort). Bij ambtshalve uitschrijving is dit de datum waarop betrokkene schriftelijk van het voornemen tot ambtshalve uitschrijving mededeling is gedaan. Bij uitschrijving wegens het ingaan van een Ministerieel besluit is dat de datum van dat besluit. In alle andere gevallen is dit de datum waarop de aangifte is ontvangen. Formaat: OnvolledigeDatum 

## **Domein attribuutsoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het gegeven is afleidbaar uit de materiele historie van het eerste van een ononderbroken reeks buitenlandse adressen. 

## **Groepattribuutsoort Inschrijving** 

> **Naam attribuutsoort** Inschrijving 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 07 

> **Definitie attribuutsoort** Gegevens over de opneming en de status van de persoonslijst in de GBA. 

**Datum opname attribuutsoort** 

18 november 2008 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 07.67.20 Reden opschorting bijhouding 07.70.10 Indicatie geheim. Het groepattribuutsoort is ontleend aan categorie 07 in de GBA. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Reden opschorting bijhouding** 

|**Naam attribuutsoort**|Reden opschorting bijhouding|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|07.67.20|
|**XML-tag attribuutsoort**|redenOpschortingBijhouding|
|**Definitie attribuutsoort**|Een aanduiding van de reden waarom de bijhouding van de PL is|
||opgeschort.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort Inschrijving.|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Indicatie geheim** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

## Indicatie geheim 

GBA 

> **Code attribuutsoort** 07.70.10 

> **XML-tag attribuutsoort** indicatieGeheim 

**Definitie attribuutsoort** 

Een aanduiding die aangeeft dat gegevens wel of niet verstrekt mogen worden. 

> **Datum opname attribuutsoort** 9 april 2007 

## **Toelichting attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Inschrijving. Zie verder de toelichting in de GBA. 

Nee 

Nee 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum opschorting bijhouding** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum opschorting bijhouding 

LO GBA 

> **Code attribuutsoort** 67.10 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

datumOpschortingBijhouding 

De datum waarop de bijhouding van de persoonslijst is gestaakt. 

LO GBA 

**Datum opname attribuutsoort** 

2 februari 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: Onvolledige datum Waardenverzameling: 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit de datum begin geldigheid van het attribuut  Omschrijving reden opschorting 

## **Groepattribuutsoort Reisdocument** 

> **Naam attribuutsoort** Reisdocument 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 12 

> **Definitie attribuutsoort** Gegevens over de reisdocumenten van de INGESCHREVEN PERSOON. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 12.36.10 Signalering reisdocument 12.37.10 Buitenlands reisdocument en de relatiesoort: INGESCHREVEN PERSOON is houder van REISDOCUMENTen INGESCHREVEN PERSOON is bijgeschreven in REISDOCUMENT. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Signalering reisdocument** 

> **Naam attribuutsoort** Signalering reisdocument 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 12.36.10 

> **XML-tag attribuutsoort** signaleringReisdocument 

> **Definitie attribuutsoort** Een aanduiding dat aan de ingeschrevene geen reisdocument mag worden verstrekt. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Reisdocument. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

Een aanduiding dat aan de ingeschrevene geen reisdocument mag worden verstrekt. 

## **Attribuutsoort Buitenlands reisdocument** 

> **Naam attribuutsoort** Buitenlands reisdocument 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 12.37.10 

> **XML-tag attribuutsoort** buitenlandsReisdocument 

> **Definitie attribuutsoort** Een aanduiding dat de ingeschrevene beschikt over één of meer buitenlandse reisdocumenten of is bijgeschreven in een buitenlands reisdocument. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Reisdocument. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Burgerlijke staat** 

**Naam attribuutsoort** 

Burgerlijke staat 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.98 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

Aanduiding van de burgerlijke staat van de INGESCHREVEN PERSOON 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

Zogenaamd afleidbaar gegeven (zie regels attribuutsoort). De gehanteerde domeinwaarden zijn ontleend aan NEN 1888, p.10 en aangepast vanwege introductie geregistreerd partnerschap. 

**Domein attribuutsoort** 

Formaat: N1 Waardenverzameling: 0 = Onbekend 1 = Ongehuwd en nooit gehuwd geweest 2 = Gehuwd 3 = Gescheiden 4 = Weduwe/weduwnaar 5 = Partnerschap 6 = Partnerschap beëindigd 7 = Achtergebleven partner 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Gegeven is af te leiden uit de relatie ‘INGESCHREVEN PERSOON is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen’ en de gegevens van het desbetreffende huwelijk of partnerschap. 

## **Relatiesoort INGESCHREVEN PERSOON heeft NATIONALITEIT** 

**Naam relatiesoort Herkomst relatiesoort** KING o.b.v. GFO BG **Code relatiesoort** 94.46 

INGESCHREVEN PERSOON heeft NATIONALITEIT 

**Definitie relatiesoort** 

De NATIONALITEIT die op een zeker moment door de INGESCHREVEN PERSOON is verkregen. 

> **Herkomst definitie relatiesoort** KING o.b.v. GFO 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Nationaliteit. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (binnen het groepattribuutsoort) 

> **Indicatie authentiek** Authentiek gegeven 

**Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN PERSOON verblijft in VERBLIJFSOBJECT** 

> **Naam relatiesoort** INGESCHREVEN PERSOON verblijft in VERBLIJFSOBJECT 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11 

> **Definitie relatiesoort** Het VERBLIJFSOBJECT behorende bij het woonadres van de persoon 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van 

Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats) in de GBA in de gevallen dat de persoon verblijft in een verblijfsobject. De relatie is de tegenhanger van VERBLIJFSOBJECT heeft daarop INGESCHREVEN PERSOONen. 

De relatiesoort maakt deel uit van het groepattribuutsoort Subject . Verblijfsplaats. Zie verder de toelichting in de GBA bij genoemde groep en bijbehorende  elementen. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

Indien de relatie niet aanwezig is dan is of het groepattribuutsoort Woonadreslocatie van waarden voorzien of is (precies) één van de relaties ‘INGESCHREVEN PERSOON verblijft op STANDPLAATS’, 'INGESCHREVEN PERSOON verblijft op LIGPLAATS' of ‘SUBJECT heeft als correspondentie- of aanschrijvingsadres ADRESSEERBAAR OBJECT AANDUIDING’ aanwezig (het zgn. briefadres in GBAterminologie). 

## **Relatiesoort INGESCHREVEN PERSOON verblijft op LIGPLAATS** 

> **Naam relatiesoort** INGESCHREVEN PERSOON verblijft op LIGPLAATS 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11 

> **Definitie relatiesoort** De LIGPLAATS behorende bij het woonadres van de persoon 

> **Datum opname relatiesoort** 24 april 2009 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats)  in de GBA in de gevallen dat de persoon verblijft op een ligplaats. De relatie is de tegenhanger van LIGPLAATS heeft daarop INGESCHREVEN PERSOONen. De relatiesoort maakt deel uit van het groepattribuutsoort Subject . Verblijfsplaats. Zie verder de toelichting in de GBA bij genoemde groep en bijbehorende  elementen. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding** Nee **strijdigheid/nietigheid** 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

**Regels attribuutsoort** 

Indien de relatie niet aanwezig is dan is of het groepattribuutsoort Woonadreslocatie van waarden voorzien of is (precies) één van de relaties ‘INGESCHREVEN PERSOON verblijft in VERBLIJFSOBJECT’, 'INGESCHREVEN PERSOON verblijft op STANDPLAATS' of ‘SUBJECT heeft als correspondentie- of aanschrijvingsadres ADRESSEERBAAR OBJECT AANDUIDING’ aanwezig (het zgn. briefadres in GBA-terminologie). 

## **Relatiesoort INGESCHREVEN PERSOON verblijft op STANDPLAATS** 

**Naam relatiesoort** 

INGESCHREVEN PERSOON verblijft op STANDPLAATS 

**Herkomst relatiesoort Code relatiesoort** 08.11 **Definitie relatiesoort Datum opname relatiesoort** 24-04-09 **Toelichting relatiesoort** 

KING op basis van GBA 

De STANDPLAATS behorende bij het woonadres van de persoon 

Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats)  in de GBA in de gevallen dat de persoon verblijft op een standplaats. 

De relatie is de tegenhanger van STANDPLAATS heeft daarop INGESCHREVEN PERSOONen. 

De relatiesoort maakt deel uit van het groepattribuutsoort Subject . Verblijfsplaats. Zie verder de toelichting in de GBA bij genoemde groep en bijbehorende  elementen. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

## 0-1 

Authentiek gegeven 

Indien de relatie niet aanwezig is dan is of het groepattribuutsoort Woonadreslocatie van waarden voorzien of is (precies) één van de relaties ‘INGESCHREVEN PERSOON verblijft in VERBLIJFSOBJECT’, 'INGESCHREVEN PERSOON verblijft op LIGPLAATS' of ‘SUBJECT heeft als correspondentie- of aanschrijvingsadres ADRESSEERBAAR OBJECT AANDUIDING’ aanwezig (het zgn. briefadres in GBA-terminologie). 

## **Relatiesoort INGESCHREVEN PERSOON is ingeschreven op NUMMERAANDUIDING** 

**Naam relatiesoort Herkomst relatiesoort Code relatiesoort** 08.11.90 **Definitie relatiesoort** 

INGESCHREVEN PERSOON is ingeschreven op NUMMERAANDUIDING KING op basis van GBA 

De NUMMERAANDUIDING bij het ADRESSEERBAAR OBJECT waarin de INGESCHREVEN PERSOON  verblijft en die hij/zij gekozen heeft als inschrijvingsadres. 

**Datum opname relatiesoort Toelichting relatiesoort** 

1 maart 2009 

Het betreft het hergebruik als relatiesoort van element 08.11.90 (Identificatiecode nummeraanduiding) van groep 11 (Adres) van categorie 08 (Verblijfplaats)  in de GBA in de gevallen dat de persoon verblijft op een adresseerbaar object. De ingeschreven persoon kan er aldus voor kiezen zich op een hoofd- of op een nevenadres te laten inschrijven. De relatie is de tegenhanger van NUMMERAANDUIDING heeft daarop INGESCHREVEN PERSOONen. 

De relatiesoort maakt deel uit van het groepattribuutsoort Verblijfsplaats. Zie verder de toelichting in de GBA bij genoemde groep en bijbehorende elementen. 

Het huisnu mmer kan de waarde 0 hebben. 

## **Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels attribuutsoort** De relatie is aanwezig in combinatie met de relatie ‘INGESCHREVEN PERSOON verblijft in  of op ADRESSEERBAAR OBJECT’, anders niet. 

## **Relatiesoort INGESCHREVEN PERSOON verblijft op locatie in WOONPLAATS** 

> **Naam relatiesoort** INGESCHREVEN PERSOON verblijft op locatie  in WOONPLAATS 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.12 

> **Definitie relatiesoort** De WOONPLAATS die hoort bij de aanduiding van het adres waarop de persoon is ingeschreven indien dit adres geen NUMMERAANDUIDING betreft. 

> **Datum opname relatiesoort** 9 april 2007 

## **Toelichting relatiesoort** 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van attribuutsoort 10.20 (Gemeentedeel) in de GBA in de gevallen dat de persoon niet ingeschreven kan worden op een verblijfsobject, stand- of ligplaats. De relatie is de tegenhanger van WOONPLAATS maakt deel uit van woonadreslocatie van INGESCHREVEN PERSOON. De relatie maakt deel uit van het groepattribuutsoort Woonadreslocatie. Zie verder de toelichting in de GBA bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort INGESCHREVEN PERSOON is vertrokken naar LAND** 

> **Naam relatiesoort** INGESCHREVEN PERSOON is vertrokken naar LAND 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 08.13.10 

> **Definitie relatiesoort** Het LAND dat de INGESCHREVEN PERSOON opgeeft bij vertrek naar het buitenland. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 2 februari 2008 

> **Toelichting relatiesoort** In afwijking van het corresponderende GBA-attribuutsoort ‘Land waarnaar vertrokken’ wordt niet de landcode vastgelegd maar de de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 13.10. De relatiesoort maakt deel uit van het groepattribuutsoort Verblijfsplaats. Zie verder de toelichting in de GBA. 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN PERSOON is ingeschreven vanuit LAND** 

**Naam relatiesoort Herkomst relatiesoort** KING **Code relatiesoort** 08.14.10 **Definitie relatiesoort** 

INGESCHREVEN PERSOON is ingeschreven vanuit LAND 

Het LAND waar de INGESCHREVEN PERSOON verblijf hield voor (her)vestiging in Nederland. KING op basis van GBA 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 1 november 2008 

**Toelichting relatiesoort** 

In afwijking van het corresponderende GBA-attribuutsoort ‘Land vanwaar ingeschreven’ wordt niet de landcode vastgelegd maar de de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 14.10. De relatiesoort maakt deel uit van het groepattribuutsoort Verblijfsplaats. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN PERSOON is houder van REISDOCUMENT** 

> **Naam relatiesoort** INGESCHREVEN PERSOON is houder van REISDOCUMENT 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 12.35 

> **Definitie relatiesoort** De REISDOCUMENTen die aan de INGESCHREVEN PERSOON zijn verstrekt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 mei 2008 

**Toelichting relatiesoort** 

Het betreft het hergebruik als relatiesoort van groep (12.)35 (Nederlands reisdocument) in de GBA. 

De relatie is de tegenhanger van REISDOCUMENT heeft als houder INGESCHREVEN PERSOON. 

De relatie maakt deel uit van het groepattribuutsoort Reisdocument. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

Indien de relatie niet aanwezig is dan moet of Signalering reisdocument of Buitenlands reisdocument van een waarde voorzien zijn of moet de relatie INGESCHREVEN PERSOON is bijgeschreven in REISDOCUMENT aanwezig zijn. 

## **Relatiesoort INGESCHREVEN PERSOON is bijgeschreven in REISDOCUMENT** 

**Naam relatiesoort** 

INGESCHREVEN PERSOON is bijgeschreven in REISDOCUMENT 

**Herkomst relatiesoort Code relatiesoort** 12.35 **Definitie relatiesoort** 

KING op basis van GBA 

De REISDOCUMENT waarin de INGESCHREVEN PERSOON is bijgeschreven. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 2 februari 2008 **Toelichting relatiesoort** 

Het betreft het hergebruik als relatiesoort van groep (12.)35 (Nederlands reisdocument) in de GBA. 

De relatie is de tegenhanger van REISDOCUMENT kent als bijgeschrevene INGESCHREVEN PERSOON. 

De relatie maakt deel uit van het groepattribuutsoort Reisdocument. Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (N-M) **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN-PERSOON is kind in  OUDER-KIND-RELATIEs** 

> **Naam relatiesoort** INGESCHREVEN-PERSOON is kind in OUDER-KIND-RELATIEs 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 09.01 

> **Definitie relatiesoort** De OUDER-KIND–RELATIEs waarin de INGESCHREVEN-PERSOON kind is. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) in categorie 09 (Kind) in de GBA.  Een INGESCHREVEN PERSOON heeft 0, 1 of 2 OUDER-KIND-RELATIES naar  INGESCHREVEN PERSOONen zijnde ‘Ouder1’ en/of ‘Ouder2’. De relatie is de tegenhanger van OUDER-KIND-RELATIE betreft kind zijnde de INGESCHREVEN-PERSOON. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-2 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven **Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN-PERSOON is ouder in  OUDER-KIND-RELATIEs** 

> **Naam relatiesoort** INGESCHREVEN-PERSOON is ouder in  OUDER-KIND-RELATIEs 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 02/03.01 

## **Definitie relatiesoort** 

> **Definitie relatiesoort** De OUDER–KIND-RELATIEs waarin de INGESCHREVEN-PERSOON de ouder is. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) in categoriën 02 (Ouder1) en 03 (Ouder2) in de GBA.  Een INGESCHREVEN PERSOON kan  zowel als ‘Ouder1’ als ook als ‘Ouder2’ ouder zijn van meerdere (verschillende) kinderen. De relatie is de tegenhanger van OUDER-KIND-RELATIE betreft ouder zijnde INGESCHREVEN-PERSOON. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN-PERSOON is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen** 

> **Naam relatiesoort** INGESCHREVEN-PERSOON is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 05.01 

> **Definitie relatiesoort** De huwelijken en/of geregistreerde partnersachappen waarin de INGESCHREVEN-PERSOON partner is 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) in categorie 05 (Huwelijk/geregistreerd partnerschap)in de GBA. 

De relatie is de tegenhanger van HUWELIJK/GEREGISTREERD PARTNERSCHAP betreft twee INGESCHREVEN-PERSOONen Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

J 

**Indicatie formele historie** 

J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN PERSOON heeft HUISHOUDENRELATIE** 

> **Naam relatiesoort** INGESCHREVEN PERSOON heeft HUISHOUDENRELATIE 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 94.40 

> **Definitie relatiesoort** De HUISHOUDENRELATIE van een  INGESCHREVEN PERSOON 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het relatiesoort HUISHOUDENRELATIE betreft INGESCHREVEN PERSOON. 

> **Indicatie materiële historie** nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort INGESCHREVEN PERSOON is geboren in LAND** 

> **Naam relatiesoort** INGESCHREVEN PERSOON is geboren in LAND 

> **Herkomst relatiesoort** GBA 

> **Code relatiesoort** 01.03.30 **Definitie relatiesoort** 

Het LAND waar de INGESCHREVEN PERSOON is geboren. 

## **Herkomst definitie relatiesoort** 

**Datum opname relatiesoort Toelichting relatiesoort** 

KING op basis van GBA 

1 november 2008 

In afwijking van het corresponderende GBA-attribuutsoort wordt niet de landcode vastgelegd maar de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 03.30. 

Het relatiesoort maakt deel uit van het groepattribuutsoort Natuurlijk persoon . Persoonsgegevens .Geboorte. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort INGESCHREVEN PERSOON is overleden in LAND** 

> **Naam relatiesoort** INGESCHREVEN PERSOON is overleden in LAND 

> **Herkomst relatiesoort** GBA 

> **Code relatiesoort** 06.08.30 

> **Definitie relatiesoort** Het LAND waar de INGESCHREVEN PERSOON is overleden. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** In afwijking van het corresponderende GBA-attribuutsoort wordt niet de landcode vastgelegd maar de de relatie naar het objecttype LAND. In het GFO BG betreft dit relatiesoort 08.30. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Overlijden. Zie verder de toelichting in de GBA. 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



**Indicatie kardinaliteit Indicatie authentiek Regels relatiesoort** 

1-1 Niet authentiek landelijk basisgegeven - 

## **2.22. Ingezetene** 

## **Groepattribuutsoort Kiesrecht** 

> **Naam attribuutsoort** Kiesrecht 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 13 

> **Definitie attribuutsoort** Gegevens over het kiesrecht van de ingezetne 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: Aanduiding Europees kiesrecht Aanduiding uitgesloten kiesrecht Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aanduiding Europees kiesrecht** 

## **Naam attribuutsoort** 

Aanduiding Europees kiesrecht 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 13.31.10 

> **XML-tag attribuutsoort** aanduidingEuropeesKiesrecht 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Een aanduiding die aangeeft of de persoon een oproep moet ontvangen voor verkiezingen voor het Europees parlement. 

## GBA 

> **Datum opname attribuutsoort** 1 mei 2008 

**Toelichting attribuutsoort Indicatie materiële historie Indicatie formele historie** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Kiesrecht. Zie verder de toelichting in de GBA. 

Nee 

Nee 

## **Aanduiding gebeurtenis** 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aanduiding uitgesloten kiesrecht** 

**Naam attribuutsoort** 

Aanduiding uitgesloten kiesrecht 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 13.38.10 

> **XML-tag attribuutsoort** aanduidingUitgeslotenKiesrecht **Definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

Een aanduiding ter uitvoering van de Kieswet. 

**Toelichting attribuutsoort** 

Het betreft een aanduiding dat de persoon niet gerechtigd is in Nederland deel te nemen aan verkiezingen. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Kiesrecht. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Groepattribuutsoort Gezagsverhouding** 

> **Naam attribuutsoort** Gezagsverhouding 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 11 

> **Definitie attribuutsoort** Gegevens betreffende het gezag over de ingeschrevene. 

> **Datum opname attribuutsoort** 9 april 2007 

|**Toelichting attribuutsoort**|Het betreft een groepattribuutsoort dat bestaat uit de volgende|
|---|---|
||attribuutsoorten:|
||Indicatie gezag minderjarige|
||Indicatie curateleregister|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentgemeente, Documentdatum, Documentbeschrijving|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Indicatie gezag minderjarige** 

|**Naam attribuutsoort**|Indicatie gezag minderjarige|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|11.32.10|
|**XML-tag attribuutsoort**|:indicatieGezagMinderjarige|
|**Definitie attribuutsoort**|Een aanduiding die aangeeft wie belast is met het gezag over de|
||minderjarige ingezetene.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort|
||Gezagsverhouding.|
||Zie verder de toelichting in de GBA.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Indicatie curateleregister** 

> **Naam attribuutsoort** Indicatie curateleregister 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 11.33.10 

> **XML-tag attribuutsoort** IndicatieCurateleRegister 

> **Definitie attribuutsoort** Een aanduiding dat de ingezetene onder curatele is gesteld. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Gezagsverhouding. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum verkrijging verblijfstitel** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort** 

Datum verkrijging verblijfstitel 

GFO-BG 

96.30 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

datumVerkrijgingVerblijfstitel 

De datum waarop de verblijfstitel van een natuurlijke persoon zijn geldigheid heeft verkregen. 

GFO-BG 

**Datum opname attribuutsoort** 

2 februario 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: Onvolledige datum Waardenverzameling: Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

## **Aanduiding brondocument** 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit de begindatum geldigheid van een verblijfstitel 

## **Attribuutsoort Datum verlies verblijfstitel** 

**Naam attribuutsoort** 

Datum verlies verblijfstitel 

> **Herkomst attribuutsoort** GFO-BG 

> **Code attribuutsoort** 39.20 

> **XML-tag attribuutsoort** datumVerliesVerblijfstitel **Definitie attribuutsoort** geldigheid zal verliezen. 

> **Herkomst definitie attribuutsoort** GFO-BG 

> **Datum opname attribuutsoort** 2 februario 2009 

De datum waarop de verblijfstitel van een natuurlijke persoon zijn geldigheid zal verliezen. 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit de einddatum geldigheid van een verblijfstitel 

## **Attribuutsoort Indicatie blokkering** 

> **Naam attribuutsoort** Indicatie blokkering 

> **Herkomst attribuutsoort** KING op basis van GBA 

> **Code attribuutsoort** 07.66 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

## indicatieBlokkering 

De indicatie dat de PL is geblokkeerd wegens een intergemeentelijke verhuizing. 

## **Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort is afgeleid van groep 66 )Blokkering) van categorie 07 (Inschrijving) in de GBA. Het maakt deel uit van groepattribuutsoort Ingeschreven persoon . Inschrijving. Zie verder de toelichting in de GBA. 

> **Domein attribuutsoort** Formaat: AN1 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

Formaat: AN1 Waardenverzameling: J (= geblokkeerd) N (= niet geblokkeerd) 

## **Relatiesoort INGEZETENE heeft VERBLIJFSTITEL** 

> **Naam relatiesoort** INGEZETENE heeft VERBLIJFSTITEL 

> **Herkomst relatiesoort** KING/GFO 

> **Code relatiesoort** 39.10 

> **Definitie relatiesoort** De verwijzing naar de VERBLIJFSTITEL die aangeeft over welke verblijfsrechtelijke status de ingezetene beschikt. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 1 maart 2009 

KING o.b.v. GBA 

**Toelichting relatiesoort** 

De relatiesoort is afgeleid van het GBA-attribuut Aanduiding verblijfstitel. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven **Regels relatiesoort** 

## **2.23. Inrichtingselement** 

## **Attribuutsoort Inrichtingselementtype** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Inrichtingselementtype 

## KING 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

- 

## type 

Specificatie van de aard van het inrichtingselement 

## KING 

## 9 april 2007 

Het attribuutsoort is toegevoegd teneinde aan te kunnen geven welk basistype dan wel plustype, zoals onderscheiden in het IMGeo, het inrichtingselement betreft. 

Formaat: AN40 

Waardenverzameling: basistypen en plustypen zoals gespecificeerd in het IMGeo 

**Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Ja 

Ja 

Nee 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Identificatie inrichtingselement** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Identificatie inrichtingselement 

IMGeo 

**Code attribuutsoort** 

- 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

identificatie 

Een unieke identificatie voor een inrichtingselement 

## IMGeo 

**Datum opname attribuutsoort** 

9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

Formaat: AN25 Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (06) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status inrichtingselement** 

> **Naam attribuutsoort** Status inrichtingselement 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** status 

> **Definitie attribuutsoort** De status gekoppeld aan de levenscyclus van het inrichtingselement. 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

> **Domein attribuutsoort** Formaat: A8 Waardenverzameling: Plan Bestaand Historie 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Naam inrichtingselement** 

**Naam attribuutsoort** 

Naam inrichtingselement 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** naam 

> **Definitie attribuutsoort** Benaming van het inrichtingselement 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: ScopedName Waardenverzameling: - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Geometrie inrichtingselement** 

> **Naam attribuutsoort** Geometrie inrichtingselement 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

## geometrie 

De minimaal tweedimensionale geometrische representatie van een inrichtingselement 

## KING 

**Datum opname attribuutsoort** 

## 9 april 2007 

## **Toelichting attribuutsoort** 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een specifiek basisinrichtingselement dan wel een plusinrichingselement. 

**Domein attribuutsoort** 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Punt, Lijn., Vlak, PuntVlak, LijnVlak, PuntLijnVlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RD-stelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Zie verder de inwinningsregels zoals beschreven in het IMGeo per specifiek basisinrichtingselement. 

## **Attribuutsoort Relatieve hoogteligging inrichtingselement** 

**Naam attribuutsoort** 

Relatieve hoogteligging inrichtingselement 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** relatieveHoogteligging 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** IMGeo **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Aanduiding voor de relatieve hoogte van het inrichtingselement 

Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

## **Domein attribuutsoort** 

Formaat: 

N1 

Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De objecten op maaiveldniveau moeten een gebiedsdekkend geheel vormen. 

## **Attribuutsoort Datum begin geldigheid inrichtingselement** 

**Naam attribuutsoort Herkomst attribuutsoort** IMGeo **Code attribuutsoort** - **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort Herkomst definitie attribuutsoort** KING **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Datum begin geldigheid inrichtingselement 

De datum waarop het inrichtingselement is ontstaan. 

Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: OnvolledigeDatum 

**Domein attribuutsoort** 

|**Indicatie materiële historie**|N|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



## **Regels attribuutsoort** 

- 

## **Attribuutsoort Datum einde geldigheid inrichtingselement** 

## **Naam attribuutsoort** 

Datum einde geldigheid inrichtingselement 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het inrichtingselement ongeldig is geworden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

**Domein attribuutsoort Indicatie materiële historie** N **Indicatie formele historie** J **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

**Indicatie in onderzoek** 

## **Aanduiding strijdigheid/nietigheid** 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid inrichtingselement’ kan in de registratie worden opgenomen. 

## **2.24. Kadastrale gemeente** 

## **Attribuutsoort Kadastrale gemeentecode** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

Kadastrale gemeentecode 

KING op basis van de BRK 

- 

code 

De code van de KADASTRALE GEMEENTE volgens de Dienst van het Kadaster en de Openbare Registers, zoals nader omschreven in het Kadasterbesluit 

KING op basis van de BRK 

1 mei 2008 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN5 Waardenverzameling: 3 letters gevolgd door 2 cijfers 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Kadastrale gemeentenaam** 

## **Naam attribuutsoort** 

## naam 

> **Herkomst attribuutsoort** BRK / IMKAD 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## Kadastrale Gemeentenaam 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De naam van de KADASTRALE GEMEENTE volgens de Dienst van het Kadaster en de Openbare Registers, zoals nader omschreven in het Kadasterbesluit 

KING 

**Datum opname attribuutsoort** 

1 maart 2009 

## **Toelichting attribuutsoort** 

|**Domein attribuutsoort**|Formaat:|
|---|---|
||Waardenverzameling:|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Regels attribuutsoort** 

## **Attribuutsoort Indicatie vervallen** 

**Naam attribuutsoort** 

## Indicatie vervallen 

**Herkomst attribuutsoort** 

KING 

**Code attribuutsoort** 

|**XML-tag attribuutsoort**|indicatieVervallen||
|---|---|---|
|**Definitie attribuutsoort**|Aanduiding of de kadastrale gemeente niet meer geldig is.||
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|1 maart 2009||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|boolean|
||Waardenverzameling:||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||



**Regels attribuutsoort** 

## **Relatiesoort KADASTRALE GEMEENTE heeft KADASTRALE ONROERENDE ZAAKen** 

> **Naam relatiesoort** KADASTRALE GEMEENTE heeft KADASTRALE ONROERENDE ZAAKen 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De KADASTRALE ONROERENDE ZAAKen die binnen de KADASTRALE GEMEENTE liggen 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **2.25. Kadastrale onroerende zaak** 

## **Attribuutsoort Kadastrale identificatie** 

**Naam attribuutsoort** 

Kadastrale identificatie 

**Herkomst attribuutsoort** 

BRK 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** kadastraleIdentificatie **Definitie attribuutsoort** 

Een door het Kadaster toegekende landelijk uniek nummer aan een kadastrale onroerende zaak. 

> **Datum opname attribuutsoort** 29 december 2008 **Toelichting attribuutsoort** 

Het betreft de attribuutsoort ‘Kadaster identificatie onroerende zaak’ in de Catalogus BRK. Daarin is deze attribuutsoort de unieke identificatie van de (kadastrale) onroerende zaak en niet langer de kadastrale aanduiding. Het kan in die situatie bijvoorbeeld voorkomen dat de kadastrale aanduiding van een perceel wijzigt. 

Aangezien de gegevenslevering door het Kadaster hier nog niet op aangepast is hanteren we vooralsnog de Kadastrale aanduiding als unieke identificatie. Na aanpassing van de gegevenslevering door het Kadaster op de BRK wordt de Kadastrale identificatie de unieke aanduiding van de Kadastrale onroerende zaak. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Groepattribuutsoort Kadastrale aanduiding** 

> **Naam attribuutsoort** Kadastrale aanduiding 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort Definitie attribuutsoort** 

De unieke aanduiding van een onroerende zaak, die door het kadaster wordt vastgesteld. 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Kadastrale gemeentecode Sectie Perceelnummer KADASTRAAL PERCEEL . Deelperceelnummer APPARTEMENTSRECHT . Appartementsindex. **Indicatie materiële historie** Ja} **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Ja: Documentidentificatie **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Kadastrale gemeentecode** 

**Naam attribuutsoort Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

Kadastrale gemeentecode 

KING op basis van de BRK 

- 

kadastraleAanduiding.kadastrale Gemeentecode 

De officiële aanduiding van de kadastrale gemeente, deel van de kadastrale aanduiding van de onroerende zaak. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 1 mei 2008 **Toelichting attribuutsoort** 

KING op basis van de BRK 

Maakt deel uit van het groepattribuutsoort Kadastrale aanduiding. Het betreft het subdomein ‘AKRkadastrale Gemeentecode’ van het domein ‘Kadastrale aanduiding’ van de gelijknamige attribuutsoort ‘ in de BRK. Zie verder de toelichting in de BRK. 

|**Toelichting attribuutsoort**|Maa<br>betr<br>‘Kad<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|



**Indicatie authentiek** 

**Regels attribuutsoort** 

Authentiek gegeven 

Afleidbaar gegeven uit de relatie KADASTRALE ONROERENDE ZAAK ligt in KADASTRALE GEMEENTE. 

## **Attribuutsoort Sectie** 

**Naam attribuutsoort** 

## Sectie 

> **Herkomst attribuutsoort** BRK 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** kadastraleAanduiding.kadastraleSectie **Definitie attribuutsoort** 

De sectie die een deel van de kadastrale gemeente uniek identificeert. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 mei 2008 **Toelichting attribuutsoort** 

Maakt deel uit van het groepattribuutsoort Kadastrale aanduiding. Het betreft het subdomein ‘Sectie’ van het domein ‘Kadastrale aanduiding’ van de gelijknamige attribuutsoort ‘ in de BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Perceelnummer** 

**Naam attribuutsoort** 

Perceelnummer 

> **Herkomst attribuutsoort** BRK 

> **Code attribuutsoort** - **XML-tag attribuutsoort Definitie attribuutsoort** 

kadastraleAanduiding.kadastraalPerceelnummer 

Een nummer dat onderdeel uitmaakt van de kadastrale aanduiding waarmee een Kadastrale onroerende zaak wordt geïdentificeerd. BRK 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

1 mei 2008 

## **Toelichting attribuutsoort** 

Maakt deel uit van het groepattribuutsoort Kadastrale aanduiding. Het betreft het subdomein ‘Perceelnummer’ van het domein ‘Kadastrale aanduiding’ van de gelijknamige attribuutsoort ‘ in de BRK. Zie verder de toelichting in de BRK. Nee 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Groepattribuutsoort Locatie onroerende zaak** 

**Naam attribuutsoort** 

Locatie onroerende zaak 

**Herkomst attribuutsoort** 

BRK 

## **Code attribuutsoort** 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

Deze wordt gebruikt om één of meer locatieaanduiding(en) van een onroerende zaak weer te geven. 

9 april 2007 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Locatie-omschrijving Cultuur bebouwd en de volgende relatiesoort: 

Is ondergrond van of heeft ruimtelijke overlap met BENOEMD 

## OBJECT 

De Locatie onroerende zaak is in het RSGB opgenomen als een ruimtelijke relatie naar BENOEMD OBJECT (GEBOUWD OBJECT of BENOEMD TERREIN) dan wel een omschrijving van de locatie door middel van woonplaats- en straatnaam of door middel van adres i.c.m. een bij- of tegenover-aanduiding. Zie ook de toelichting bij KADASTRALE ONROERENDE ZAAK. 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

1-N 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Authentiek gegeven 

Van de attribuutsoort Locatie-omschrijving en de beide relatiesoorten komt er per Locatie-onroerende zaak telkens slechts één voor. 

## **Attribuutsoort Locatie-omschrijving** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Locatie- omschrijving 

KING op basis van BRK 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

locatieOnroerendeZaak.locatieOmschrijving 

Omschrijving van de locatie van de onroerende zaak ingeval de locatie niet kan worden aangeduid met een relatie naar een GEBOUWD OBJECT of BENOEMD TERREIN. 

**Herkomst definitie attribuutsoort** 

KING op basis van BRK 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het betreft een interpretatie van de attribuutsoorten ‘omschrijving’ en ‘bij of tegenover locatie’ bij de locatie van de onroerende zaak in de BRK. In het laatste geval is het attribuut gevuld met de naam van de woonplaats, gevolgd door een komma en de tekst ‘bij’ of ‘tegenover’ uit het attribuut, gevolgd door de openbare ruimtenaam en de nummeraanduidinggegevens van het adres. 

Maakt deel uit van het groepattribuutsoort Locatie onroerende zaak. Zie verder de toelichting in de BRK. 

## **Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven **Regels attribuutsoort** 

Het attribuut kan alleen van een waarde voorzien zijn als de relaties KADASTRALE ONROERENDE ZAAK is ondergrond van GEBOUWD OBJECT en KADASTRALE ONROERENDE ZAAK heeft ruimtelijke overlap met BENOEMD TERREIN niet voorkomen. 

## **Attribuutsoort Cultuur bebouwd** 

> **Naam attribuutsoort** Cultuur bebouwd 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** LocatieOnroerendeZaak.cultuurBebouwd 

> **Definitie attribuutsoort** Een aanduiding van de cultuur van een locatie. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Maakt deel uit van het groepattribuutsoort Locatie onroerende zaak. Zie verder de toelichting in de BRK. 

> **Domein attribuutsoort** Formaat: AN65 Waardenverzameling: zie BRK-document "cultuurbebouwd.xml" 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Koopsom** 

**Naam attribuutsoort Herkomst attribuutsoort** BRK **Code attribuutsoort** 

Koopsom 

## **Definitie attribuutsoort** 

Het in een ter inschrijving aangeboden stuk vermelde bedrag, waarvoor één of meer onroerende zaken zijn verkregen. 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Valutasoort Aard bedrag Bedrag Koopjaar Meer onroerendgoed Transactiedatum 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Valutasoort** 

> **Naam attribuutsoort** Valutasoort 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** koopsom.valutasoort 

> **Definitie attribuutsoort** Aanduiding van de valutasoort 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsort maakt deel uit van het groepattribuutsoort Koopsom en is afgeleid van het subdomein CurrencyID van het domein Koopsom in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard bedrag** 

> **Naam attribuutsoort** Aard bedrag 

> **Herkomst attribuutsoort** BRK 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

koopsom.aardBedrag 

## **Definitie attribuutsoort** 

Geeft aan of er sprake is van meerdere getotaliseerde hoofdsommen. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

**Toelichting attribuutsoort** 

De attribuutsort maakt deel uit van het groepattribuutsoort Koopsom en is afgeleid van het subdomein AardBedrag van het domein Koopsom in de catalogus BRK. Zie verder de toelichting in de BRK. Nee 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Bedrag** 

|**Naam attribuutsoort**|Bedrag|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|koopsom.bedrag|
|**Definitie attribuutsoort**|A number of monetary units specified in a currency where the unit of|
||currency is explicit or implied.|
|**Herkomst definitie attribuutsoort**|BRK|
|**Datum opname attribuutsoort**|1 november 2008|
|**Toelichting attribuutsoort**|De attribuutsort maakt deel uit van het groepattribuutsoort Koopsom en is|
||afgeleid van het subdomein Amount van het domein Koopsom in de|
||catalogus BRK. Zie verder de toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|



## **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Koopjaar** 

|**Naam attribuutsoort**|Koopjaar|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|koopsom.koopjaar|
|**Definitie attribuutsoort**|Transactiejaar van de aankoop|
|**Herkomst definitie attribuutsoort**|BRK|
|**Datum opname attribuutsoort**|1 november 2008|
|**Toelichting attribuutsoort**|De attribuutsort maakt deel uit van het groepattribuutsoort Koopsom en is|
||afgeleid van het subdomein Koopjaar van het domein Koopsom in de|
||catalogus BRK. Zie verder de toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Meer onroerendgoed** 

> **Naam attribuutsoort** Meer onroerendgoed 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** koopsom.meerOnroerendGoed **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

Indicatie of betrokken onroerendgoed wel/niet samen met met ander onroerendgoed in een akte onder een koopsom is verkregen. BRK 

**Toelichting attribuutsoort** 

De attribuutsort maakt deel uit van het groepattribuutsoort Koopsom en is afgeleid van het subdomein ‘Meer onroerendgoed’ van het domein Koopsom in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Transactiedatum** 

> **Naam attribuutsoort** Transactiedatum 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** koopsom.transactiedatum **Definitie attribuutsoort** 

Datum en tijdstip waarop een ter inschrijving aangeboden stuk, waarmee één of meer onroerende zaken zijn overgedragen, is ondertekend door de opsteller van het stuk. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van het groepattribuutsoort Koopsom. In de BRK komt het niet in dit groepattribuutsoort voor maar maakt het deel uit van de gegevens van het objecttype Stuk (BRK.ST.tia stuk.Tijdstip ondertekening TIA stuk). Zie verder de toelichting in de BRK. 

> **Domein attribuutsoort** Formaat: datum/tijd Waardenverzameling: onvolledige datum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Afleidbaar uit  de materiële historie van het groepattribuutsoort Koopsom. 

## **Attribuutsoort Landinrichtingsrente** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Landinrichtingsrente 

BRK 

**Code attribuutsoort** 

## **Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

Het bedrag waarmee de Onroerende zaak is belast in het kader van de landinrichtingswet 

9 april 2007 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Aanduiding aard LIproject Valutasoort Aard bedrag Bedrag Eindjaar 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aanduiding aard LIproject** 

> **Naam attribuutsoort** Aanduiding aard LIproject 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** landinrichtingsRente.aardLIProject 

> **Definitie attribuutsoort** Een aanduiding voor de aard van het landinrichtingsproject. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsort maakt deel uit van het groepattribuutsoort Landinrichtingsrente en is afgeleid van het subdomein AanduidingAardLIproject’ van het domein Landinrichtingsrente in de catalogus BRK. Zie verder de toelichting in de BRK. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Valutasoort** 

> **Naam attribuutsoort** Valutasoort 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** landinrichtingsRente.valutasoort 

> **Definitie attribuutsoort** Aanduiding van de valutasoort 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

De attribuutsort maakt deel uit van het groepattribuutsoort Landinrichtingsrente en is afgeleid van het subdomein CurrencyID van het domein Landinrichtingsrente in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard bedrag** 

> **Naam attribuutsoort** Aard bedrag 

> **Herkomst attribuutsoort** BRK 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** landinrichtingsRente.aardBedrag 

> **Definitie attribuutsoort** Geeft aan of er sprake is van meerdere getotaliseerde hoofdsommen. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsort maakt deel uit van het groepattribuutsoort Landinrichtingsrente en is afgeleid van het subdomein AardBedrag van het domein Landinrichtingsrente in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Bedrag** 

|**Naam attribuutsoort**|Bedrag|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|landinrichtingsRente.bedrag|
|**Definitie attribuutsoort**|A number of monetary units specified in a currency where the unit of|
||currency is explicit or implied.|
|**Herkomst definitie attribuutsoort**|BRK|
|**Datum opname attribuutsoort**|1 november 2008|
|**Toelichting attribuutsoort**|De attribuutsort maakt deel uit van het groepattribuutsoort|
||Landinrichtingsrente en is afgeleid van het subdomein Amount van het|
||domein Landinrichtingsrente in de catalogus BRK. Zie verder de|
||toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|



> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Eindjaar** 

|**Naam attribuutsoort**|Eindjaar|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|landinrichtingsRente.eindjaar|
|**Definitie attribuutsoort**|Het jaar tot wanneer de Landinrichtingsrente van toepassing is.|
|**Herkomst definitie attribuutsoort**|BRK|
|**Datum opname attribuutsoort**|1 november 2008|
|**Toelichting attribuutsoort**|De attribuutsoort maakt deel uit van het groepattribuutsoort|
||Landinrichtingsrente en is afgeleid van het subdomein Eindjaar van het|
||domein Landinrichtingsrente in de catalogus BRK. Zie verder de|
||toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Cultuur onbebouwd** 

> **Naam attribuutsoort** Cultuur onbebouwd 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **Definitie attribuutsoort** Een aanduiding voor het onbebouwde gedeelte van de cultuur van een onroerende zaak. 

**Datum opname attribuutsoort** 

9 april 2007 

## **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: Aard cultuur onbebouwd Aard bebouwing Meer culturen 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard cultuur onbebouwd** 

|**Naam attribuutsoort**|Aard cultuur onbebouwd|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|cultuurOnbebouwd|
|**Definitie attribuutsoort**|Een aanduiding voor de soort cultuur van (het onbebouwde gedeelte) van|
||de onroerende zaak.|
|**Herkomst definitie attribuutsoort**|BRK|
|**Datum opname attribuutsoort**|1 november 2008|
|**Toelichting attribuutsoort**|De attribuutsoort maakt deel uit van het groepattribuutsoort ‘Cultuur|
||onbebouwd’ en is afgeleid van het subdomein AardCultuurOnbebouwd|
||van het domein CultuurOnbebouwd in de catalogus BRK. Zie verder de|
||toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Aard bebouwing** 

> **Naam attribuutsoort** Aard bebouwing 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** aardBebouwing 

> **Definitie attribuutsoort** Een aanduiding voor het al dan niet bebouwd zijn van de onroerende zaak. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van het groepattribuutsoort ‘Cultuur onbebouwd’ en is afgeleid van het subdomein AardBebouwing van het domein CultuurOnbebouwd in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Meer culturen** 

> **Naam attribuutsoort** Meer culturen 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** meerCulturen 

> **Definitie attribuutsoort** Indicatie van wel/geen aanwezigheid van meer culturen. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van het groepattribuutsoort ‘Cultuur onbebouwd’ en is afgeleid van het subdomein MeerCulturen van het domein CultuurOnbebouwd in de catalogus BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

Nee 

|**Indicatie formele historie**|Nee|
|---|---|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Datum begin geldigheid kadastrale onroerende zaak** 

**Naam attribuutsoort** 

Datum begin geldigheid kadastrale onroerende zaak 

> **Herkomst attribuutsoort** KING/GFO 

> **Code attribuutsoort** 81.20 

> **XML-tag attribuutsoort** ingangsdatumObject 

**Definitie attribuutsoort** 

De datum waarop de gegevens van de kadastrale onroerende zaak voor het eerst geldig zijn geworden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum wordt afgeleid van de gegevens van het Stuk in de BRK waarnaar vanuit de Onroerende zaak in de BRK verwezen wordt d.m.v. het attribuut  ‘Stuk ontstaan onroerende zaak’. 

**Domein attribuutsoort** 

Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** 

Ja:  Documentidentificatie 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid kadastrale onroerende zaak** 

> **Naam attribuutsoort** Datum einde geldigheid kadastrale onroerende zaak 

> **Herkomst attribuutsoort** KING/GFO 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop de gegevens van de kadastrale onroerende zaak voor het laatst geldig zijn geweest. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De datum wordt afgeleid van de gegevens van het Stuk in de BRK waarnaar vanuit de Onroerende zaak in de BRK verwezen wordt d.m.v. het attribuut  ‘Stuk vervallen onroerende zaak’. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja:  Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. 

## **Attribuutsoort Kadastrale onroerende zaak typering** 

> **Naam attribuutsoort** Kadastrale onroerende zaak typering 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** typering 

> **Definitie attribuutsoort** Het onderscheid van een KADASTRALE ONROERENDE ZAAK in een geheel KADASTRAAL PERCEEL, een KADASTRAAL deelPERCEEL dan wel APPARTEMENTSRECHT. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 mei 2008 

**Toelichting attribuutsoort** 

Het attribuutsoort is benodigd om bij uitwisseling van gegevens van het objecttype KADASTRALE ONROERENDE ZAAK aan te kunnen geven welke van de onderscheiden typen kadastrale onroerende zaken het betreft en daarmee of het om de specialisatie KADASTRAAL PERCEEL dan wel APPARTEMENTSRECHT gaat. Met de domeinwaarden wordt aangesloten bij de huidige praktijk van het gebruik van de zgn. ‘kadastraal object letter’ als onderdeel van de idientificatie van genoemde typen kadastrale onroerende zaken. 

**Domein attribuutsoort** 

Formaat: AN1 Waardenverzameling: G (= geheel perceel) D (= deelperceel) A (= appartementsrecht) 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Indien het attrinuut de waarde ‘G’ of ‘D” heeft dan moet het object de specialisatie Kadastraal perceel betreffen. Indien het attrinuut de waarde ‘A” heeft dan moet het object de specialisatie Appartementsrecht betreffen. 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK ligt in KADASTRALE GEMEENTE** 

**Naam relatiesoort Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK ligt in KADASTRALE GEMEENTE KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De KADASTRALE GEMEENTE waarin de KADASTRALE ONROERENDE ZAAK gelegen is. 

KING 

**Datum opname relatiesoort** 

1 maart 2009 

## **Toelichting relatiesoort** 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

## **Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK heeft één of meer ZAKELIJK RECHT** 

> **Naam relatiesoort** KADASTRALE ONROERENDE ZAAK heeft één of meer ZAKELIJK RECHT **Herkomst relatiesoort** 

KING op basis van BRK 

**Code relatiesoort** 

> **Definitie relatiesoort** De ZAKELIJKe RECHTen van één of meer SUBJECTen op een KADASTRALE ONROERENDE ZAAK 

> **Herkomst definitie relatiesoort** KING op basis van BRK 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het attribuutsoort ‘kadastrale aanduiding’ bij het RECHT in de BRK cq. van het relatiesoort ZAKELIJK RECHT betreft KADASTRALE ONROERENDE ZAAK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK is ondergrond van of heeft ruimtelijke overlap met BENOEMD OBJECT** 

> **Naam relatiesoort** KADASTRALE ONROERENDE ZAAK is ondergrond van of heeft ruimtelijke overlap met BENOEMD OBJECT 

> **Herkomst relatiesoort** KING op basis van BRK 

**Code relatiesoort** 

> **Definitie relatiesoort** De BENOEMDe OBJECTen die de delen van het aardoppervlak gemeen hebben met de KADASTRALE ONROERENDE ZAAK zijnde een (deel)perceel waar de GEBOUWDe OBJECTen het aardoppervlak raken cq. doorsnijden dan wel de GEBOUWDe OBJECTen die betrokken zijn in de KADASTRALE ONROERENDE ZAAK zijnde een appartementsrecht. 

> **Herkomst definitie relatiesoort** KING op basis van BRK 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft de uitbreiding op het hergebruik als relatiesoort van het attribuutsoort ‘locatie onroerende zaak . adres’ bij het objecttype ONROERENDE ZAAK in de BRK. Dit BRK-attribuutsoort betreft de verwijzing naar een nummeraanduiding in de BAG. Hier is dit gemodelleerd als relatie naar BENOEMD OBJECT d.w.z. ook naar het OVERIG GEBOUWD OBJECT en het OVERIG TERREIN. De relatie maakt deel uit van het groepattribuutsoort Locatie onroerende zaak. 

Het doel van de relatie is dat de eigendomssituatie van een gerelateerd benoemd object afgeleid kan worden uit de rechten die rusten op de kadastrale onroerende zaak en op eventueel andere aan dat benoemd object gerelateerde kadastrale onroerende zaken. Het gaat nadrukkelijk om ruimtelijke relaties en niet om gebruiksrelaties, zoals bij de WOZ gebruikelijk is. V.w.b. het benoemd object is bepalend de doorsnijding hiervan met het aardoppervlak d.w.z. de situatie op het maaiveld. Luchtbruggen e.d.  maken dus geen deel uit van de ruimtelijke relatie. 

||Het gaat nadrukkelijk om ruimtelijke relaties en niet om gebruiksrelaties,<br>zoals bij de WOZ gebruikelijk is. V.w.b. het benoemd object is bepalend<br>de doorsnijding hiervan met het aardoppervlak d.w.z. de situatie op het<br>maaiveld. Luchtbruggen e.d.  maken dus geen deel uit van de ruimtelijke<br>relatie.|
|---|---|
||De relatie is de tegenhanger van BENOEMD OBJECT staat op of heeft|
||ruimtelijke overlap met KADASTRALE ONROERENDE ZAAK.|
||Zie verder de toelichting in de BRK bij genoemd attribuutsoort.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Authentiek gegeven indien het een relatie naar een VERBLIJFSOBJECT,|
||STANDPLAATS of LIGPLAATS betreft, anders een gemeentelijk|
||basisgegeven|
|**Regels relatiesoort**|De relatie kan binnen de groepattribuut Locatie onroerende zaak alleen|
||aanwezig zijn als het attribuut Locatie-omschrijving niet van een waarde|
||is voorzien.|



## **Relatiesoort KADASTRALE ONROERENDE ZAAK is ontstaan uit andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK is ontstaan uit andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE 

KING op basis van BRK 

## **Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

De verwijzing naar andere KADASTRALE ONROERENDE ZAAKen waaruit de KADASTRALE ONROERENDE ZAAK is ontstaan. KING op basis van BRK 

9 april 2007 

Een nieuwe kadastrale onroerende zaak is ontstaan uit 1 of meer vervallen kadastrale onroerende zaken. Vanwege eigenschappen van deze relatie (aard, overgangsgrootte) is dit gemodelleerd via KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het ontstaan uit een KADASTRALE ONROERENDE ZAAK. 

Het betreft het hergebruik als relatiesoort van de attribuutsoort ‘Onroerende zaak historie . Kadastrale aanduiding’ bij het objecttype ONROERENDE ZAAK in de BRK. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. Het betreft tevens de relatie ‘Filiatie kadastraal object is ontstaan uit kadastraal object’ bij het Kadastraal object in het GFO BG. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK is overgegaan in andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK is overgegaan in andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE 

KING op basis van BRK 

## **Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

De verwijzing naar andere KADASTRALE ONROERENDE ZAAKen waarin de KADASTRALE ONROERENDE ZAAK is overgegaan. 

KING op basis van BRK 

1 mei 2008 

Een vervallen kadastrale onroerende zaak is overgegaan in 1 of meer nieuwe kadastrale onroerende zaken. Vanwege eigenschappen van deze relatie (aard, overgangsgrootte) is dit gemodelleerd via KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het overgaan in een KADASTRALE ONROERENDE ZAAK. Het betreft het hergebruik als relatiesoort van de attribuutsoort ‘Onroerende zaak historie . Kadastrale aanduiding’ bij het objecttype ONROERENDE ZAAK in de BRK. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. Het betreft tevens de relatie ‘Filiatie kadastraal object is overgegaan in kadastraal object’ bij het Kadastraal object in het GFO BG. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

**Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK is hoofdperceel bij mandelige KADASTRALE ONROERENDE ZAAKen** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK is hoofdperceel bij mandelige KADASTRALE ONROERENDE ZAAKen 

KING op basis van BRK 

## **Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De verwijzing naar andere KADASTRALE ONROERENDE ZAAKen De relatie tussen een KADASTRALE ONROERENDE ZAAK, ten behoeve waarvan een mandeligheid tot stand is gekomen (het hoofdperceel) en de andere KADASTRALE ONROERENDE ZAAKen, welke tot gemeenschappelijk nut bestemd zijn (de mandelige onroerende zaken). KING op basis van BRK 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van de attribuutsoorten ‘Mandelige onroerende zaak’ en ‘Hoofd onroerende zaak’ bij het objecttype ONROERENDE ZAAK in de BRK. Een kadstrale onroerende zaak kan hoofdperceel zijn bij meerdere mandelige onroerende zaken; tevens kunnen er meerdere hoofdpercelen zijn bij een mandelige onroerende zaak. Zie verder de toelichting in de BRK bij genoemde attribuutsoorten. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** N-M 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON** 

**Naam relatiesoort** 

KADASTRALE ONROERENDE ZAAK heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON 

> **Herkomst relatiesoort** GFO BG 

> **Code relatiesoort** 94.23 **Definitie relatiesoort** 

De rechtspersoon dat de voornaamste zakelijk gerechtigde bij een kadastraal object is. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** 

Wie de voornaamste zakelijk gerechtigde is, kan worden afgeleid uit de gegevens 'Teller aandeel zakelijk recht' en 'Noemer aandeel zakelijk recht'. Overigens kan het voorkomen dat de voornaamste zakelijk gerechtigde niet als zakelijk gerechtigde is geregistreerd. Bijvoorbeeld bij de van vader op zoon doorgifte van een boerenbedrijf wordt veelal geen acte bij de notaris opgemaakt. De zakelijke rechten liggen vaak nog bij de (over-overgroot)vader. Het voornaamste zakelijk recht wordt echter uitgeoefend door de zoon. 

Bij een kadastraal object hoort één voornaamste zakelijk gerechtigde. Een rechtspersoon kan voornaamste zakelijk gerechtigde van nul, één of meer kadastrale objecten zijn. 

De relatie is de tegenhanger van RECHTSPERSOON is voornaamste zakelijk gerechtigde van KADASTRALE ONROERENDE ZAAK. 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort KADASTRALE ONROERENDE ZAAK behoort tot WOZ-OBJECT** 

> **Naam relatiesoort** KADASTRALE ONROERENDE ZAAK behoort tot WOZ-OBJECT 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 51.01b **Definitie relatiesoort** 

De unieke aanduidingen van de WOZ-OBJECTEN waarvan de KADASTRALE ONROERENDE ZAAK geheel of gedeeltelijk deel uitmaakt. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

KING op basis van de catalogus BRWOZ 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde kadastrale objecten’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZOBJECT bevat KADASTRALE ONROERENDE ZAAK. Zie verder de toelichting in de BRWOZ. 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Niet-authentiek landelijk basisgegeven.|
|**Regels relatiesoort**|-|



## **Relatiesoort KADASTRALE  ONROERENDE ZAAK heeft KADASTRALE  ONROERENDE ZAAK AANTEKENINGen** 

> **Naam relatiesoort** KADASTRALE  ONROERENDE ZAAK heeft KADASTRALE ONROERENDE ZAAK AANTEKENINGen 

> **Herkomst relatiesoort** KING op basis van BRK **Code relatiesoort** 

> **Definitie relatiesoort** De KADASTRALE ONROERENDE ZAAK AANTEKENINGen die geplaatst zijn bij de . KADASTRALE ONROERENDE ZAAK 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . aantekening’ bij het objecttype KADASTRALE ONROERENDE ZAAK in de BRK. 

De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK AANTEKENING behoort bij KADASTRALE ONROERENDE ZAAK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **2.26. Kadastrale onroerende zaak aantekening** 

## **Attribuutsoort Kadaster identificatie aantekening** 

> **Naam attribuutsoort** Kadaster identificatie aantekening 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Een door het Kadaster toegekend landelijk uniek nummer aan een aantekening. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Zie de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard aantekening kadastraal object** 

> **Naam attribuutsoort** Aard aantekening kadastraal object 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** aard 

> **Definitie attribuutsoort** Aanduiding welk feit er bestaat, genoemd in een Stuk, dat betrekking heeft op een onroerende zaak en dat gevolgen kan hebben voor de uitoefening van rechten op de onroerende zaak. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Zie de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

|**Indicatie in onderzoek**|Nee|
|---|---|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Beschrijving aantekening kadastraal object** 

|**Naam attribuutsoort**|Beschrijving aantekening kadastraal object|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|omschrijving|
|**Definitie attribuutsoort**|Een tekstuele toelichting inzake de aantekening bij het kadastraal object.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Zie de toelichting in de BRK.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentidentificatie|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Begindatum aantekening kadastraal object** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Begindatum aantekening kadastraal object 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

ingangsdatumObject 

Deze begindatum geeft aan wanneer een bepaalde aantekening rechtsgeldig geworden is. 

KING 

2 februari 2009 

## **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** De attribuutsoort komt niet voor in de BRK. De waarde wordt afgeleid van de datum ondertekening van het stuk waarin het feit genoemd is waarop de aantekening is gebaseerd. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, eventueel onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Attribuutsoort Einddatum aantekening kadastraal object** 

> **Naam attribuutsoort** Einddatum aantekening kadastraal object 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** Deze einddatum geeft aan wanneer een bepaalde aantekening niet langer meer rechtsgeldig is. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Zie de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Splitsing aantekening kadastraal object** 

> **Naam attribuutsoort** Splitsing aantekening kadastraal object 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** splitsing 

> **Definitie attribuutsoort** Bij een aantekening die betrekking heeft op een gedeelte van het object wordt verwezen naar de ingeschreven tekening voor de ligging. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Zie de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK AANTEKENING behoort bij KADASTRALE ONROERENDE ZAAK** 

> **Naam relatiesoort** KADASTRALE ONROERENDE ZAAK AANTEKENING behoort bij KADASTRALE ONROERENDE ZAAK 

> **Herkomst relatiesoort** KING op basis van BRK **Code relatiesoort** 

> **Definitie relatiesoort** De KADASTRALE ONROERENDE ZAAK waarbij de AANTEKENING geplaatst is. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . aantekening’ bij het objecttype KADASTRALE ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van KADASTRALE  ONROERENDE ZAAK heeft KADASTRALE  ONROERENDE ZAAK AANTEKENINGen. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

## **Aanduiding gebeurtenis** 

## Nee 

**Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** 

Ja: Documentidentificatie 

Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK AANTEKENING heeft betrokken RECHTSPERSOON** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK AANTEKENING heeft betrokken RECHTSPERSOON 

BRK 

**Code relatiesoort** 

**Definitie relatiesoort** 

Een uniek nummer van de eventueel betrokken RECHTSPERSOON bij deze aantekening. 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting relatiesoort** 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . aantekening . betrokken persoon’ bij het objecttype KADASTRALE ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van RECHTSPERSOON Is betrokken bij KADASTRALE  ONROERENDE ZAAK AANTEKENING. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **2.27. Kadastrale onroerende zaak historie relatie** 

## **Attribuutsoort Overgangsgrootte** 

> **Naam attribuutsoort** Overgangsgrootte 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** overgangsgrootte 

> **Definitie attribuutsoort** Een door de Dienst op grond van de kadastrale grenzen van een perceel berekende indicatieve grootte van een perceel bij de ontstaansvorming van dat perceel uit een eerder perceel. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Betreft de attribuutsoort Onroerende zaak historie.Overgangsgrootte bij de Onroerende zaak in de BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard** 

|**Naam attribuutsoort**|Aard|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|aard|
|**Definitie attribuutsoort**|Aanduiding hoe het kadastraal object (historisch) tot stand gekomen is.|
|**Datum opname attribuutsoort**|1 mei 2008|
|**Toelichting attribuutsoort**|Betreft de attribuutsoort Onroerende zaak historie.Aard bij de Onroerende|
||zaak in de BRK. Zie verder de toelichting in de BRK.|
||Het betreft de attribuutsoort Filiatiecode bij het objecttype Filiatie|
||kadastraal object in het GFO BG.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|



## **Aanduiding gebeurtenis** 

## Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

Ja: Documentidentificatie 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het ontstaan uit een KADASTRALE ONROERENDE ZAAK** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het ontstaan uit een KADASTRALE ONROERENDE ZAAK 

KING op basis van BRK 

**Code relatiesoort** 

**Definitie relatiesoort** 

De KADASTRALE ONROERENDE ZAAKen waaruit andere gerelateerde KADASTRALE ONROERENDE ZAAKen zijn ontstaan. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 1 mei 2007 **Toelichting relatiesoort** 

KING op basis van BRK 

Een nieuwe kadastrale onroerende zaak is ontstaan uit 1 of meer vervallen kadastrale onroerende zaken. Vanwege eigenschappen van deze relatie (aard, overgangsgrootte) is dit gemodelleerd via KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK is ontstaan uit andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. 

Het betreft het hergebruik als relatiesoort van de attribuutsoort ‘Onroerende zaak historie . Kadastrale aanduiding’ bij het objecttype ONROERENDE ZAAK in de BRK. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. Het betreft tevens de relatie ‘Filiatie kadastraal object is ontstaan uit kadastraal object’ bij het Filiatie kadastraal object in het GFO BG. 

**Indicatie materiële historie** 

## Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Regels relatiesoort** 

## **Relatiesoort KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het overgaan in een KADASTRALE ONROERENDE ZAAK** 

> **Naam relatiesoort** KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE betreft het overgaan in een KADASTRALE ONROERENDE ZAAK 

> **Herkomst relatiesoort** KING op basis van BRK 

**Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 1 mei 2008 **Toelichting relatiesoort** 

De KADASTRALE ONROERENDE ZAAKen waarin andere KADASTRALE ONROERENDE ZAAKen zijn overgegaan. KING op basis van BRK 

Een vervallen kadastrale onroerende zaak is overgegaan in 1 of meer nieuwe kadastrale onroerende zaken. Vanwege eigenschappen van deze relatie (aard, overgangsgrootte) is dit gemodelleerd via KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. 

De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK is overgegaan in andere kadastrale onroerende zaak bij KADASTRALE ONROERENDE ZAAK HISTORIE RELATIE. 

Het betreft het hergebruik als relatiesoort van de attribuutsoort ‘Onroerende zaak historie . Kadastrale aanduiding’ bij het objecttype ONROERENDE ZAAK in de BRK. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. Het betreft tevens de relatie ‘Filiatie kadastraal object is overgegaan in kadastraal object’ bij Filiatie kadastraal object in het GFO BG. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **2.28. Kadastraal perceel** 

## **Attribuutsoort Deelperceelnummer** 

> **Naam attribuutsoort** Deelperceelnummer 

> **Herkomst attribuutsoort** BRK 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** kadastraleAanduiding.deelperceelNummer 

> **Definitie attribuutsoort** Volgnummer waarmee een deelperceel wordt geïdentificeerd. 

> **Herkomst definitie attribuutsoort** BRK 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Deze attribuutsoort maakt deel uit van de groepattribuutsoort KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding. De aldaar gespecificeerde metagegevens zoals historie gelden ook voor deze attribuutsoort. Het betreft het subdomein ‘Deelperceelnummer’ van het domein ‘Kadastrale aanduiding’ van de gelijknamige attribuutsoort ‘ in de BRK. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels attribuutsoort** Indien het attribuut de waarde nul heeft moet het attribuut Kadastrale onroerende zaak . Kadastrale onroerende zaak typering de waarde ‘G” hebben (en betreft het een geheel perceel). Indien het attribuut een waarde groter dan nul heeft moet het attribuut Kadastrale onroerende zaak . Kadastrale onroerende zaak typering de waarde ‘D” hebben (en betreft het een deelperceel). 

## **Attribuutsoort Plaatscoördinaten perceel** 

> **Naam attribuutsoort** Plaatscoördinaten perceel 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** plaatscoordinaten 

## **Definitie attribuutsoort** 

De aanduiding van een kaartpunt voor de weergave van de identificatie van een perceel (centroïde). 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Grootte perceel** 

> **Naam attribuutsoort** Grootte perceel 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** grootte 

> **Definitie attribuutsoort** Een door de Dienst op grond van de kadastrale grenzen van een perceel berekende indicatieve grootte van een perceel ten tijde van vorming van dat perceel. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Aanduiding soort grootte** 

> **Naam attribuutsoort** Aanduiding soort grootte 

> **Herkomst attribuutsoort** BRK 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** vastgesteldeGrootte 

> **Definitie attribuutsoort** Een aanduiding die voorafgaand aan de meting middels een melding in de aktetekst wordt bepaald en aangeeft of er bij de afsplitsing van een deel van een perceel sprake zal zijn van een vastgestelde grootte, dan wel een indicatieve grootte. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Begrenzing perceel** 

> **Naam attribuutsoort** Begrenzing perceel 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** begrenzing 

> **Definitie attribuutsoort** Het geheel van lijnketens waarmee de vlakomtrek van een perceel wordt gevormd. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Hier wordt er vanuit gegaan dat de geometrie als zgn. GML-string wordt uitgewisseld. Zie verder de toelichting bij dit attribuutsoort in de BRK. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Omschrijving deelperceel** 

> **Naam attribuutsoort** Omschrijving deelperceel 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** omschrijvingDeelperceel 

> **Definitie attribuutsoort** Het in een ter inschrijving aangeboden stuk beschreven tekst, dat een nadere omschrijving geeft van het gekochte deel van een perceel. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Relatiesoort KADASTRAAL PERCEEL is ondergrond van  appartementencomplex met APPARTEMENTSRECHTen** 

**Naam relatiesoort** 

> **Naam relatiesoort** KADASTRAAL PERCEEL is ondergrond van  appartementencomplex met APPARTEMENTSRECHTen 

> **Herkomst relatiesoort** BRK **Code relatiesoort** 

> **Definitie relatiesoort** Een appartementencomplex bevindt zich op een of meer percelen. 

> **Herkomst definitie relatiesoort** BRK 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . appartementsrecht . Appartementencomplex . perceel’ bij het objecttype ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van APPARTEMENTSRECHT maakt deel uit van appartementencomplex dat staat op KADASTRAAL PERCEEL. Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels attribuutsoort** De relatie komt alleen voor indien de appartementsindex de waarde nul heeft. 

## **Relatiesoort KADASTRAAL deelPERCEEL ligt binnen KADASTRAAL PERCEEL** 

> **Naam relatiesoort** KADASTRAAL deelPERCEEL ligt binnen KADASTRAAL PERCEEL 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Een geheel perceel waarmee de ligging van het deelperceel aangeduid kan worden. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Dit heeft ten doel om van elk kadastraal perceel vast te kunnen leggen op welk deel van het gemeentelijk grondgebied dit betrekking heeft. Gehele percelen beschikken over geometrie (de perceelgrens), voor deelpercelen en appartementsrechten is dit (nog) niet het geval. Via deze relatie wordt van een deelperceel vastgelegd op welk geheel percelen het qua ligging betrekking heeft. 

Voor appartementsrechten vindt dit op analoge wijze plaats met de relatie APPARTEMENTSRECHT betreft appartementencomplex dat staat op KADASTRAAL PERCEEL 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentidentificatie|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|N-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



**Regels relatiesoort** 

Niet verplicht te registreren 

## **2.29. Kunstwerkdeel** 

## **Attribuutsoort Type kunstwerk** 

**Naam attribuutsoort** 

Type kunstwerk 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** type 

> **Definitie attribuutsoort** Specificatie van het soort Kunstwerk 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie IMGeo, CodeList TypeKunstwerk 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Identificatie kunstwerkdeel** 

> **Naam attribuutsoort** Identificatie kunstwerkdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Een unieke identificatie voor een kunstwerkdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

**Domein attribuutsoort** 

## Formaat: 

## AN25 

Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (05) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status kunstwerkdeel** 

> **Naam attribuutsoort** Status kunstwerkdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** status **Definitie attribuutsoort** 

De status gekoppeld aan de levenscyclus van het kunstwerkdeel. 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: A8 Waardenverzameling: Plan Bestaand Historie 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Naam kunstwerkdeel** 

> **Naam attribuutsoort** Naam kunstwerkdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** naam 

> **Definitie attribuutsoort** Benaming van het kunstwerkdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: ScopedName Waardenverzameling: - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Geometrie kunstwerkdeel** 

**Naam attribuutsoort** 

Geometrie kunstwerkdeel 

**Herkomst attribuutsoort Code attribuutsoort** - **XML-tag attribuutsoort Definitie attribuutsoort** 

IMGeo 

geometrie 

De minimaal tweedimensionale geometrische representatie van een kunstwerkdeel 

## **Herkomst definitie attribuutsoort** KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

## 9 april 2007 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een kunstwerk. 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Lijn., Vlak, LijnVlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RD-stelsel. 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Zie verder de inwinningsregels zoals beschreven in het IMGeo bij Kunstwerk en Kunstwerkdeel. 

## **Attribuutsoort Relatieve hoogteligging kunstwerkdeel** 

**Naam attribuutsoort Herkomst attribuutsoort** IMGeo **Code attribuutsoort** - **XML-tag attribuutsoort** relatieveHoogteligging **Definitie attribuutsoort** 

Relatieve hoogteligging kunstwerkdeel 

Aanduiding voor de relatieve hoogte van het kunstwerkdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. Formaat: N1 

**Domein attribuutsoort** 

Formaat: N1 Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De objecten op maaiveldniveau moeten een gebiedsdekkend geheel vormen. 

## **Attribuutsoort Datum begin geldigheid kunstwerkdeel** 

**Naam attribuutsoort** 

Datum begin geldigheid kunstwerkdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop het kunstwerkdeel is ontstaan. 

Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Formaat: OnvolledigeDatum 

## **Attribuutsoort Datum einde geldigheid kunstwerkdeel** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum einde geldigheid kunstwerkdeel 

## IMGeo 

**Code attribuutsoort** 

- 

**XML-tag attribuutsoort** 

## einddatumObject 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** KING **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop het kunstwerkdeel ongeldig is geworden. 

Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: OnvolledigeDatum 

**Domein attribuutsoort** 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid kunstwerkdeel’ kan in de registratie worden opgenomen. 

## **2.30. Land** 

## **Attribuutsoort Landcode** 

**Naam attribuutsoort** 

Landcode 

**Herkomst attribuutsoort Code attribuutsoort** 94.10 **XML-tag attribuutsoort** code **Definitie attribuutsoort** de GBA. **Herkomst definitie attribuutsoort** GFO BG **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

GFO BG op basis van GBA 

De code, behorende bij de landnaam, opgenomen in de Landentabel van de GBA. 

Het attribuutsoort komt tevens voor in de GBA (zie de relaties van LAND naar SUBJECT en specialisaties daarvan). 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: N4 Waardenverzameling: GBA-tabel 34 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Landnaam** 

**Naam attribuutsoort** 

## Landnaam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.56 

> **XML-tag attribuutsoort** naam 

**Definitie attribuutsoort** 

De naam van het land, zoals opgenomen in de Landentabel van de GBA. 

> **Herkomst definitie attribuutsoort** GFO BG **Datum opname attribuutsoort** 

1 november 2008 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: GBA-tabel 34 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Ingangsdatum land** 

|**Naam attribuutsoort**|Ingangsdatum land||
|---|---|---|
|**Herkomst attribuutsoort**|GFO BG||
|**Code attribuutsoort**|81.20||
|**XML-tag attribuutsoort**|TijdvakObject.beginObject||
|**Definitie attribuutsoort**|De datum waarop het|land is ontstaan.|
|**Herkomst definitie attribuutsoort**|GFO BG||
|**Datum opname attribuutsoort**|1 november 2008||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|Onvolledigedatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Attribuutsoort Einddatum land** 

> **Naam attribuutsoort** Einddatum land 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** TijdvakObject.eindObject 

> **Definitie attribuutsoort** De datum waarop het land is opgeheven. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 november 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Landcode ISO** 

**Naam attribuutsoort** 

## Landcode ISO 

> **Herkomst attribuutsoort** ISO **Code attribuutsoort** 

> **XML-tag attribuutsoort** codeIso 

**Definitie attribuutsoort** 

De code van een huidig land of gebiedsdeel conform ISO 3166 

> **Herkomst definitie attribuutsoort** ISO 

**Datum opname attribuutsoort** 

2 februari 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: A2 Waardenverzameling: landentabel ISO 3166-1 Nee 

|**Indicatie formele historie**|Nee|
|---|---|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



## **Regels attribuutsoort** 

## **Relatiesoort LAND is deel van verblijf buitenland van SUBJECT** 

|**Naam relatiesoort**|LAND is deel van verblijf buitenland van SUBJECT|
|---|---|
|**Herkomst relatiesoort**|KING|
|**Code relatiesoort**||
|**Definitie relatiesoort**|Het SUBJECT dat heeft aangegeven te (gaan) verblijven dan wel verblijft|
||in het LAND.|
|**Herkomst definitie relatiesoort**|KING op basis van GBA|
|**Datum opname relatiesoort**|1 november 2008|
|**Toelichting relatiesoort**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven indien het een ingeschreven|
||natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk|
||basisgegeven.|
|**Regels relatiesoort**|-|



## **Relatiesoort LAND waarin is gesloten/aangegaan HUWELIJK/GEREGISTREERD PARTNERSCHAP** 

> **Naam relatiesoort** LAND waarin is gesloten/aangegaan HUWELIJK/GEREGISTREERD PARTNERSCHAP 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 05.06.30 

> **Definitie relatiesoort** De huwelijken die zijn voltrokken of de partnerschappen die ziijn aangegaan in LAND. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van de relatiesoort ‘HUWELIJK/GEREGISTREERD PARTNERSCHAP is gesloten/aangegaan in LAND’. Zie verder de toelichting aldaar. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort LAND waarin is ontbonden HUWELIJK/GEREGISTREERD PARTNERSCHAP** 

> **Naam relatiesoort** LAND waarin is ontbonden HUWELIJK/GEREGISTREERD PARTNERSCHAP 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 05.07.30 

> **Definitie relatiesoort** De HUWELIJKen/GEREGISTREERDe PARTNERSCHAPpen die zijn ontbonden of nietig verklaard in LAND. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

De relatiesoort is de tegenhanger van de relatiesoort ‘HUWELIJK/GEREGISTREERD PARTNERSCHAP is ontbonden in LAND’. Zie verder de toelichting aldaar. 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort LAND waarin is geboren INGESCHREVEN PERSOON** 

> **Naam relatiesoort** LAND waarin is geboren INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 01.03.30 

> **Definitie relatiesoort** De INGESCHREVEN PERSOONen die zijn geboren in LAND. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van de relatiesoort ‘INGESCHREVEN PERSOON is geboren in LAND’. Zie verder de toelichting aldaar. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort LAND waarin is overleden INGESCHREVEN PERSOON** 

> **Naam relatiesoort** LAND waarin is overleden INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING 

## **Code relatiesoort** 

## 06.08.30 

> **Definitie relatiesoort** De INGESCHREVEN PERSOONen die zijn overleden in LAND. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van de relatiesoort ‘INGESCHREVEN PERSOON is overleden in LAND’. Zie verder de toelichting aldaar. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort LAND vanwaaruit is ingeschreven INGESCHREVEN PERSOON** 

> **Naam relatiesoort** LAND vanwaaruit is ingeschreven INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 08.14.10 

> **Definitie relatiesoort** De INGESCHREVEN PERSOONen die verblijf hielden in LAND voor (her)vestiging in Nederland. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van de relatiesoort ‘INGESCHREVEN PERSOON is ingeschreven vanuit LAND’. Zie verder de toelichting aldaar. 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|



## **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort LAND waarnaar is vertrokken INGESCHREVEN PERSOON** 

> **Naam relatiesoort** LAND waarnaar is vertrokken INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 08.13.10 

> **Definitie relatiesoort** De INGESCHREVEN PERSOONen die bij vertrek naar het buitenland dit LAND hebben opgegeven. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 2 februari 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van de relatiesoort INGESCHREVEN PERSOON is vertrokken naar LAND. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **2.31. Ligplaats** 

## **Attribuutsoort Indicatie geconstateerde ligplaats** 

**Naam attribuutsoort** 

Indicatie geconstateerde ligplaats 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.02/58.02 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

> **Datum opname attribuutsoort** 24-04-09 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Ligplaatsstatus** 

**Naam attribuutsoort** 

Ligplaatsstatus 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 57.03/58.03 

**Definitie attribuutsoort** 

De fase van de levenscyclus van een LIGPLAATS waarin de betreffende LIGPLAATS zich bevindt. 

> **Datum opname attribuutsoort** 24-04-09 

**Toelichting attribuutsoort** 

**Indicatie materiële historie** 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort LIGPLAATS heeft als hoofdadres NUMMERAANDUIDING** 

**Naam relatiesoort** 

LIGPLAATS heeft als hoofdadres NUMMERAANDUIDING 

**Herkomst relatiesoort Code relatiesoort** 57.10/58.10 **Definitie relatiesoort** 

KING op basis van BAG 

De identificatiecode nummeraanduiding waaronder het hoofdadres van een LIGPLAATS, dat in het kader van de basisregistratie gebouwen als zodanig is aangemerkt, is opgenomen in de basisregistratie adressen. KING op basis van BAG 

**Herkomst definitie relatiesoort** 

> **Datum opname relatiesoort** 24-04-09 **Toelichting relatiesoort** 

In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding hoofdadres ligplaats’ bij het objecttype LIGPLAATS. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is hoofdadres van LIGPLAATS. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort LIGPLAATS heeft als nevenadressen NUMMERAANDUIDING** 

> **Naam relatiesoort** LIGPLAATS heeft als nevenadressen NUMMERAANDUIDING 

> **Herkomst relatiesoort** KING op basis van BAG 

> **Code relatiesoort** 57.11/58.11 

## **Definitie relatiesoort** 

De identificatiecodes nummeraanduiding waaronder nevenadressen van een LIGPLAATS, die in het kader van de basisregistratie gebouwen als zodanig zijn aangemerkt, zijn opgenomen in de basisregistratie adressen. KING op basis van BAG 

> **Herkomst definitie relatiesoort** KING op basis van BAG 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding nevenadressen ligplaats’ bij het objecttype LIGPLAATS. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is nevenadres van LIGPLAATS. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort LIGPLAATS heeft daarop INGESCHREVEN PERSOONen** 

**Naam relatiesoort** 

LIGPLAATS heeft daarop INGESCHREVEN PERSOONen 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11 **Definitie relatiesoort** 

De personen die ingeschreven zijn in de gemeente op het adres dat hoort bij de LIGPLAATS 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 24-04-09 

**Toelichting relatiesoort** 

Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats) in de GBA in de gevallen dat de personen verblijven op de ligplaats. 

De relatie is de tegenhanger van INGESCHREVEN PERSOON verblijft op LIGPLAATS. 

||Zie verder de toelichting in de GBA bij genoemd attribuutsoort.|
|---|---|
|**Indicatie materiële historie**|J|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Authentiek gegeven|



## **Regels relatiesoort** 

## **Relatiesoort LIGPLAATS is huisvesting van HUISHOUDEN** 

|**Naam relatiesoort**|LIGPLAATS is huisvesting van HUISHOUDEN|
|---|---|
|**Herkomst relatiesoort**|KING op basis van GFO BG|
|**Code relatiesoort**|96.01|
|**Definitie relatiesoort**|De LIGPLAATS waarop één of meer HUISHOUDENs wonen.|
|**Herkomst definitie relatiesoort**|KING op basis van GFO BG|
|**Datum opname relatiesoort**|24-04-09|
|**Toelichting relatiesoort**|Een huishouden is ‘woonachtig’ in één verblijfs-object, standplaats of|
||ligplaats. In één dergelijk object kunnen nul, één of meer huishoudens|
||‘wonen’.|
||De relatie is de tegenhanger van het relatiesoort HUISHOUDEN is|
||gehuisvest op LIGPLAATS.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**||



## **2.32. Maatschappelijke activiteit** 

## **Attribuutsoort KvK-nummer** 

> **Naam attribuutsoort** KvK-nummer 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** kvkNummer 

> **Definitie attribuutsoort** Landelijk uniek identificerend administratienummer van een MAATSCHAPPELIJKE ACTIVITEIT zoals toegewezen door de Kamer van Koophandel (KvK). 

> **Herkomst definitie attribuutsoort** KING op basis van GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN8 Waardenverzameling: 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum aanvang** 

> **Naam attribuutsoort** Datum aanvang 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumAanvang 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum voortzetting** 

**Naam attribuutsoort** 

Datum voortzetting 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumVoortzetting 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum beëindiging** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum einde geldig (beëindiging) 

NHR 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** datumEinde 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Groepattribuutsoort Handelsnamen** 

**Naam attribuutsoort Herkomst attribuutsoort** NHR 

Handelsnamen 

**Code attribuutsoort** 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

{nog niet in NHR uitgewerkt} 

## NHR 

2 februari 2009 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Handelsnaam Verkorte naam Volgorde. Zie verder de catalogus NHR. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Handelsnaam** 

> **Naam attribuutsoort** Handelsnaam 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** handelsnaam 

> **Definitie attribuutsoort** De naam waaronder de onderneming handelt. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Handelsnamen. .Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: bij de KvK ingeschreven handelsnamen 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Verkorte naam** 

**Naam attribuutsoort** 

Verkorte naam 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

NHR 

## handelsnaamVerkort 

De door de Kamer van Koophandel bepaalde naam van de onderneming ten behoeve van adresseringsdoeleinden. 

KING op basis van GFO BG 

9 april 2007 

## **Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Handelsnamen. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: AN45 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Attribuutsoort Volgorde** 

> **Naam attribuutsoort** Volgorde 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** volgorde 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Herkomst definitie attribuutsoort** NHR 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Handelsnamen. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: N6 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Groepattribuutsoort Activiteiten** 

> **Naam attribuutsoort** Activiteiten 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** NHR **Datum opname attribuutsoort** 2 februari 2009 **Toelichting attribuutsoort** 

Het totaal van alle activiteiten van alle bij de MAATSCHAPPELIJKE ACTIVITEIT behorende vestigingen. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

|**Toelichting attribuutsoort**|Het betreft een groepattribuutso<br>attribuutsoorten:|
|---|---|
||Indicatie hoofdactiviteit|
||Volgorde|
||Activiteitcode|
||Activiteit.|
||Zie verder de catalogus NHR.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Landelijk basisgegeven|



**Regels attribuutsoort** 

## **Attribuutsoort Indicatie hoofdactiviteit** 

> **Naam attribuutsoort** Indicatie hoofdactiviteit 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** activiteit.indicatieHoofdactiviteit 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt} 

> **Herkomst definitie attribuutsoort** NHR 

> **Datum opname attribuutsoort** 2 februari 2009 

## **Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

**Domein attribuutsoort** 

Formaat: {?AN1 Waardenverzameling: J (=ja), N (nee)} Nee 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk  basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Volgorde** 

> **Naam attribuutsoort** Volgorde 

> **Herkomst attribuutsoort** NHR 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** activiteit.volgorde 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt} 

> **Herkomst definitie attribuutsoort** NHR 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: N6 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk  basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Activiteitcode** 

> **Naam attribuutsoort** Activiteitcode 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** activiteit.activiteitCode 

> **Definitie attribuutsoort** Een door een standaardcode weergegeven typering behorende bij een MAATSCHAPPELIJKE ACTIVITEIT 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: N15 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Activiteit** 

> **Naam attribuutsoort** Activiteit 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** activiteit.omschrijving **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** NHR 

> **Datum opname attribuutsoort** 2 februari 2009 

Eén van de activiteiten van één of meer bij de MAATSCHAPPELIJKE ACTIVITEIT behorende vestigingen 

**Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk  basisgegeven 

## **Regels attribuutsoort** 

## **Relatiesoort MAATSCHAPPELIJKE ACTIVITEIT heeft als eigenaar RECHTSPERSOON** 

## **Naam relatiesoort** 

> **Naam relatiesoort** MAATSCHAPPELIJKE ACTIVITEIT heeft als eigenaar RECHTSPERSOON 

> **Herkomst relatiesoort** NHR **Code relatiesoort** 

> **Definitie relatiesoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft de rechtspersoon die de maatschappelijke activiteit uitvoert. Zowel natuurlijke als niet-natuurlijke personen kunnen maatschappelijke activiteiten uitvoeren. Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘FInummer eigenaar’ bij het objecttype Maatschappelijke activiteit in het NHR. 

||Zowel natuurlijke als niet-natuurlijke personen kunnen maatschappelijk<br>activiteiten uitvoeren.<br>Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘FI-<br>nummer eigenaar’ bij het objecttype Maatschappelijke activiteit in het<br>NHR.|
|---|---|
||De relatie is de tegenhanger van RECHTSPERSOON Is eigenaar van|
||MAATSCHAPPELIJKE ACTIVITEIT.|
||Zie verder de toelichting in het NHR bij genoemd attribuutsoort.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Relatiesoort MAATSCHAPPELIJKE ACTIVITEIT oefent activiteit uit in VESTIGING** 

**Naam relatiesoort Herkomst relatiesoort** 

MAATSCHAPPELIJKE ACTIVITEIT oefent activiteit uit in VESTIGING 

NHR 

**Code relatiesoort** 

**Definitie relatiesoort Datum opname attribuutsoort** 9 april 2007 **Toelichting relatiesoort** 

{nog niet in NHR uitgewerkt 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Vestigingnummer(s) van de bijbehorende vestiging(en)’ bij het objecttype Maatschappelijke activiteit in het NHR. 

De relatie is de tegenhanger van VESTIGING betreft uitoefening van activiteiten door MAATSCHAPPELIJKE    ACTIVITEIT. Zie verder de toelichting in het NHR bij genoemd attribuutsoort. Ja 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

## **2.33. Nationaliteit** 

## **Attribuutsoort Nationaliteitcode** 

> **Naam attribuutsoort** Nationaliteitcode 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 04.05.10 

> **XML-tag attribuutsoort** code **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING o.b.v. GBA 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Zie het LO GBA 

> **Domein attribuutsoort** Formaat: N4 Waardenverzameling: GBA-nationaliteitentabel 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

Een code die aangeeft welke nationaliteit de ingeschrevene bezit. 

**Regels attribuutsoort** 

## **Attribuutsoort Nationaliteitomschrijving** 

**Naam attribuutsoort** 

Nationaliteitomschrijving 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.65 

> **XML-tag attribuutsoort** omschrijving 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** KING o.b.v. GFO BG **Datum opname attribuutsoort** 1 maart 2009 

De omschrijving van de nationaliteit. 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN42|
||Waardenverzameling: GBA-nationaliteitentabel||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Landelijk basisgegeven||



## **Regels attribuutsoort** 

## **Attribuutsoort Begindatum geldigheid nationaliteit** 

> **Naam attribuutsoort** Begindatum geldigheid nationaliteit 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.20 

> **XML-tag attribuutsoort** tijdvakObject.beginObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 maart 2008 

De datum waarop de nationaliteit is ontstaan. 

**Toelichting attribuutsoort** 

Het gaat hier om veranderingen in de lijst van codes en omschrijvingen. Niet te verwarren met de datum waarop een natuurlijke persoon zijn of haar nationaliteit verkrijgt. 

|**Domein attribuutsoort**|Formaat:|onvolledige datum|
|---|---|---|
||Waardenverzameling:||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Landelijk basisgegeven||
|**Regels attribuutsoort**|||



## **Attribuutsoort Einddatum geldigheid nationaliteit** 

## **Naam attribuutsoort** 

Einddatum geldigheid nationaliteit 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** tijdvakObject.eindObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 maart 2008 

De datum waarop de nationaliteit is opgeheven. 

**Toelichting attribuutsoort** 

Het gaat hier om veranderingen in de lijst van codes en omschrijvingen. Niet te verwarren met de datum waarop een natuurlijke persoon zijn of haar nationaliteit verliest. 

> **Domein attribuutsoort** Formaat: onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Landelijk basisgegeven 

**Regels attribuutsoort** 

## **Relatiesoort NATIONALITEIT hoort bij INGESCHREVEN PERSOON** 

**Naam relatiesoort** 

NATIONALITEIT hoort bij INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING o.b.v. GFO BG 

> **Code relatiesoort** 94.46 

**Definitie relatiesoort** 

De INGESCHREVEN PERSOONen die op een zeker moment  de NATIONALITEIT hebben verkregen. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 1 maart 2009 **Toelichting relatiesoort** 

KING o.b.v. GFO 

De relatiesoort is de tegenhanger van de relatiesoort INGESCHREVEN PERSOON heeft NATIONALITEIT. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **2.34. Natuurlijk persoon** 

## **Groepattribuutsoort Persoonsgegevens** 

**Naam attribuutsoort** 

Persoonsgegevens 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01 

> **Definitie attribuutsoort** Gegevens over de NATUURLIJK PERSOON 

> **Herkomst definitie attribuutsoort** KING op basis van GBA 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende (groep)attribuutsoorten: 01.02 Naam 01.04.10 Geslachtsaanduiding 01.61.10 Aanduiding naamgebruik 01.03     Geboorte 01.01      Ingeschreven persoon . Identificatienummers.. Het is ontleend aan categorie 01 in de GBA. Zie verder de toelichting in de GBA. 

**Indicatie materiële historie Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** 

Ja indien het een INGESCHREVEN PERSOON betreft, anders: Nee 

Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving indien het een INGESCHREVEN PERSOON betreft, anders: Nee 

**Indicatie in onderzoek** 

Ja indien het een INGESCHREVEN PERSOON betreft, anders: Nee 

> **Aanduiding strijdigheid/nietigheid** Ja indien het een INGESCHREVEN PERSOON betreft, anders: Nee 

> **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Groepattribuutsoort Naam** 

**Naam attribuutsoort** 

## Naam 

**Herkomst attribuutsoort** 

## GBA 

> **Code attribuutsoort** 01.02 **Definitie attribuutsoort Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

Gegevens over de naam van de natuurlijk persoon 

KING op basis van GBA 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Voornamen Adellijke titel/predikaat Voorvoegsels geslachtsnaam Geslachtsnaam. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Persoonsgegevens. .Zie verder de toelichting in de GBA. **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Voornamen** 

> **Naam attribuutsoort** Voornamen 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.02.10 

> **XML-tag attribuutsoort** voornamen 

> **Definitie attribuutsoort** De verzameling namen die, gescheiden door spaties, aan de geslachtsnaam voorafgaat.. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Adellijke titel/ predikaat** 

**Naam attribuutsoort** 

Adellijke titel/ predikaat 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort** 

GBA 

01.02.20 

adellijkeTitelPredikaat 

## **Definitie attribuutsoort** 

Een omschrijving die aangeeft welke titel of welk predikaat behoort tot de naam (bij adellijke titel geslachtsnaam, bij predikaat voornaam). KING op basis van GBA. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

9 april 2007 

Het betreft de omschrijving van de adellijke titel/predikaat zoals deze voorkomt in de desbetreffende GBA-tabel, dus niet de code. Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam. Zie verder de toelichting in de GBA. 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN10|
||Waardenverzameling: GBA Tabel 38, Tabel Adellijke titel/predikaat:||
|||Baron (titel)|
|||Barones (titel)|
|||Graaf (titel)|
|||Gravin (titel)|
|||Hertog (titel)|
|||Hertogin (titel)|
|||Jonkheer (predikaat)|
|||Jonkvrouw (predikaat)|
|||Markies (titel)|
|||Markiezin (titel)|
|||Prins (titel)|
|||Prinses (titel)|
|||Ridder (titel)|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven indien het een ingeschreven||
||persoon betreft, anders een gemeentelijk basisgegeven.||



## **Attribuutsoort Voorvoegsel geslachtsnaam** 

**Naam attribuutsoort** 

Voorvoegsel geslachtsnaam 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.02.30 

> **XML-tag attribuutsoort** voorvoegselGeslachtsnaam 

> **Definitie attribuutsoort** Dat deel van de geslachtsnaam dat voorkomt in GBA Tabel 36, Voorvoegseltabel en, gescheiden door een spatie, vooraf gaat aan de rest van de geslachtsnaam. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Geslachtsnaam** 

> **Naam attribuutsoort** Geslachtsnaam 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.02.40 

> **XML-tag attribuutsoort** geslachtsnaam 

> **Definitie attribuutsoort** De (geslachts)naam waarvan de eventueel aanwezige voorvoegsels en adellijke titel/predikaat zijn afgesplitst. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam. Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

## **Indicatie in onderzoek** 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Geslachtsaanduiding** 

**Naam attribuutsoort** 

Geslachtsaanduiding 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01-04-10 

> **XML-tag attribuutsoort** geslachtsaanduiding **Definitie attribuutsoort** 

Een aanduiding die aangeeft dat de ingeschrevene een man of een vrouw is, of dat het geslacht (nog) onbekend is. 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Persoonsgegevens. .Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Aanduiding naamgebruik** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Aanduiding naamgebruik 

## GBA 

**Code attribuutsoort** 

01.61.10 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

aanduidingNaamgebruik 

Een aanduiding voor de wijze van aanschrijving van de ingeschrevene. 

## GBA 

**Datum opname attribuutsoort** 

1 mei 2008 

**Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Persoonsgegevens. .Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Groepattribuutsoort Geboorte** 

> **Naam attribuutsoort** Geboorte 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.03 

> **Definitie attribuutsoort** Gegevens over de geboorte van de persoon. 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoort: 01.03.10 Geboortedatum 01.03.20 Ingeschreven persoon . Geboorteplaats en de volgende relatiesoort: INGESCHREVEN PERSOON is geboren in LAND. De Geboortedatum is een attribuutsoort van NATUURLIJK PERSOON Het attribuutsoort maakt deel uit van het groepattribuutsoort Persoonsgegevens. .Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven. **Regels attribuutsoort** 

## **Attribuutsoort Geboortedatum** 

> **Naam attribuutsoort** Geboortedatum 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 01.03.06 

> **XML-tag attribuutsoort** geboortedatum 

> **Definitie attribuutsoort** De datum waarop de persoon is geboren. 

> **Herkomst definitie attribuutsoort** GBA 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Geboorte. .Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Groepattribuutsoort Naam aanschrijving** 

**Naam attribuutsoort Herkomst attribuutsoort** KING 

Naam aanschrijving 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De naamgegevens waarmee de persoon heeft aangegeven aangeschreven te willen worden 

9 april 2007 

## KING 

**Toelichting attribuutsoort** 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Aanhef aanschrijving Voorletters aanschrijving Voornamen aanschrijving Geslachtsnaam aanschrijving Het bevat de opgemaakte naamgegevens. 

> **Domein attribuutsoort** Formaat: n.v.t. Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven. **Regels attribuutsoort** 

Afleidbaar gegeven indien de natuurlijk persoon terzake geen opgave heeft gedaan 

## **Attribuutsoort Aanhef aanschrijving** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Aanhef aanschrijving 

## KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

aanhefAanschrijving 

De aanhef waarmee de persoon aangeschreven wil worden. 

## KING 

**Datum opname attribuutsoort** 

## 9 april 2007 

**Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam aanschrijving. 

**Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN50|
||Waardenverzameling: Indien de burger terzake geen opgave gedaan||
|||heeft dan, afhankelijk van de Geslachtsaanduiding|
|||‘Mijnheer’, ‘Mevrouw’ of ‘Mevrouw/Mijnheer’.|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||



**Regels attribuutsoort** 

Afleidbaar gegeven indien de natuurlijk persoon terzake geen opgave heeft gedaan. Afleidbaar uit de Geslachtsaanduiding 

## **Attribuutsoort Voorletters aanschrijving** 

## **Naam attribuutsoort** 

Voorletters aanschrijving 

> **Herkomst attribuutsoort** KING 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** voorletters 

> **Definitie attribuutsoort** De voorletters waarmee een persoon aangeschreven wil worden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort biedt de mogelijkheid de natuurlijk persoon zelf te laten bepalen hoe hij aangeschreven wil worden indien in de aanschrijving gebruik gemaakt wordt van voorletters. Bijvoorbeeld “A.C.’’ maar ook “Ch.IJ.”. Indien geen opgave is gedaan bevat het attribuut de eerste letters van de voornamen van de persoon gescheiden door punten. Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam aanschrijving. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: één of meer voorletters per voornaam, gescheiden door leestekens. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Afleidbaar gegeven indien de natuurlijk persoon terzake geen opgave heeft gedaan. Afleidbaar uit de voornamen van de natuurlijk persoon 

## **Attribuutsoort Voornamen aanschrijving** 

|**Naam attribuutsoort**|Voornamen aanschrijving|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**||



**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

voornamenAanschrijving 

De voornamen waarmee een persoon aangeschreven wil worden. 

## **Herkomst definitie attribuutsoort** 

|**Datum opname attribuutsoort**|9 april 2007||
|---|---|---|
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam||
||aanschrijving.||
|**Domein attribuutsoort**|Formaat:|AN200|
||Waardenverzameling:||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|Afleidbaar gegeven indien de natuurlijk persoon terzake geen opgave||
||heeft gedaan. Afleidbaar uit de voornamen van de persoon (kopie)||



## **Attribuutsoort Geslachtsnaam aanschrijving** 

> **Naam attribuutsoort** Geslachtsnaam aanschrijving 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** geslachtsnaamAanschrijving **Definitie attribuutsoort** 

De geslachtsnaam waarmee de persoon aangeschreven wil worden. 

## **Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Naam aanschrijving. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels attribuutsoort** Afleidbaar gegeven uit de Geslachtsnaam (G) en de Voorvoegsels (V) van de natuurlijk persoon en de Geslachtsnaam (GP) en Voorvoegsels (VP) van de laatst ingeschreven actuele partner van de natuurlijk persoon (via de relatiesoort INGESCHREVEN PERSOON is partner in HUWELIJK/GEREGISTREERD PARTNERSCHAPpen). Onderstaande tabel geeft de regels voor de omzetting naar de samengestelde Naam Aanschrijving. De spatie na V en VP wordt alleen opgenomen, als ook V of VP zelf wordt opgenomen. Een Naam Aanschrijving die volgens deze regels is opgebouwd, kan weer worden afgebroken naar de samenstellende elementen ervan uitgaande dat het voorvoegsel voorkomt in GBA-tabel 36. 

|Aanduiding naamgebruik|Naam aanschrijving|
|---|---|
|E|V G|
|N|V G-VP GP|
|P|VP GP|
|V|VP GP-V G|



## **Groepattribuutsoort Overlijden** 

|**Naam attribuutsoort**|Overlijden|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|06|
|**Definitie attribuutsoort**|Gegevens over het overlijden.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: AkteGemeente, Documentidentificatie, Documentgemeente,|
||Documentdatum, Documentbeschrijving|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Datum opname attribuutsoort**|18 november 2008|
|**Toelichting attribuutsoort**|Het betreft een groepattribuutsoort dat bestaat uit de volgende|
||attribuutsoorten:|
||06.08.10 Overlijdensdatum|
||06.08.20 Ingeschreven persoon . Overlijdenplaats|
||en de relatiesoort:|
||INGESCHREVEN PERSOON is overleden in LAND.|
||Zie verder de toelichting in de GBA.|



## **Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek** 

Niet authentiek landelijk basisgegeven. 

## **Attribuutsoort Overlijdensdatum** 

> **Naam attribuutsoort** Overlijdensdatum 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 06.08.10 

> **XML-tag attribuutsoort** overlijdensdatum 

> **Definitie attribuutsoort** De datum van overlijden. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Overlijden. Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven indien het een ingeschreven persoon betreft, anders een gemeentelijk basisgegeven. 

## **Relatiesoort NATUURLIJK PERSOON heeft ACADEMISCHE TITEL** 

> **Naam relatiesoort** NATUURLIJK PERSOON heeft ACADEMISCHE TITEL 

> **Herkomst relatiesoort** GFO BG 

> **Code relatiesoort** 94.00 

> **Definitie relatiesoort** De ACADEMISCHE TITELs van een NATUURLIJK PERSOON. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort is de tegenhanger van ACADEMISCHE TITEL hoort bij NATUURLIJK PERSOONen 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

|**Aanduiding brondocument**|Nee|
|---|---|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**||



## **2.35. Niet-ingezetene** 

Dit objecttype overerft attributen en relaties van generalisaties van het objecttype, welke  aldaar zijn gespecificeerd, en kent geen specifieke attributen en relaties. 

## **2.36. Niet-natuurlijk persoon** 

## **Attribuutsoort (Statutaire) Naam** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

(Statutaire) Naam 

NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

## statutaireNaam 

Naam van de niet-natuurlijke persoon zoals deze is vastgelegd in de statuten (rechtspersoon) of in de vennootschapsovereenkomst is overeengekomen (Vennootschap onder firma of Commanditaire vennootschap). 

GFO BG 

**Datum opname attribuutsoort** 

9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN500 Waardenverzameling: 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum aanvang** 

> **Naam attribuutsoort** Datum aanvang 

> **Herkomst attribuutsoort** NHR 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** datumAanvang 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 2 februari 2009 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven indien het een Ingeschreven niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven 

## **Attribuutsoort Datum beëindiging** 

> **Naam attribuutsoort** Datum beëindiging 

> **Herkomst attribuutsoort** NHR 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumEinde 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 2 februari 2009 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven indien het een Ingeschreven niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven 

## **Relatiesoort NIET-NATUURLIJK PERSOON is vereniging van eigenaars bij appartementencomplex met APPARTEMENTSRECHTen** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

NIET-NATUURLIJK PERSOON is vereniging van eigenaars bij appartementencomplex met APPARTEMENTSRECHTen KING op basis van BRK 

## **Code relatiesoort** 

## **Definitie relatiesoort** 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

De statuten van de verenigingen en de gemeenschappen, met uitzondering van de gedeelten die bestemd zijn als afzonderlijk geheel te worden gebruikt, waarover de NIET-NATUURLIJK PERSOON het beheer voert met als doel het behartigen van gemeenschappelijke belangen van de appartementseigenaars. KING op basis van BRK 

9 april 2007 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . appartementsrecht . Appartementencomplex . Vereniging van eigenaars’ bij het objecttype ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van APPARTEMENTSRECHT maakt deel uit van appartementencomplex met als vereniging van eigenaars NIET-NATUURLIJK PERSOON. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort NIET-NATUURLIJK PERSOON heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** NIET-NATUURLIJK PERSOON heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING op basis van NHR 

**Code relatiesoort** 

> **Definitie relatiesoort** Het binnenlands bezoekadres van de NIET-NATUURLIJK PERSOON 

> **Herkomst definitie relatiesoort** KING {definitie in NHR ontbreekt vooralsnog} 

> **Datum opname relatiesoort** 2 februari 2009 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Bezoekadres’ bij het objecttype Niet-natuurlijk persoon in het NHR. De relatie is de tegenhanger van ADRESSEERBAAR OBJECT AANDUIDING is bezoekadres van INGESCHREVEN NIET-NATUURLIJK PERSOON. Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Landelijk basisgegeven 

> **Regels relatiesoort** Indien deze relatie voorkomt dan heeft het SUBJECT zijnde de NIETNATUURLIJK PERSOON geen buitenlands adres. 

## **2.37. Nummeraanduiding** 

## **Attribuutsoort Indicatie geconstateerde nummeraanduiding** 

**Naam attribuutsoort** 

Indicatie geconstateerde nummeraanduiding 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.21 

> **XML-tag attribuutsoort** geconstateerd 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Nummeraanduidingstatus** 

> **Naam attribuutsoort** Nummeraanduidingstatus 

> **Herkomst attribuutsoor** BAG 

> **Code attribuutsoort** 11.69 

> **XML-tag attribuutsoort** status 

**Definitie attribuutsoort** 

De fase van de levenscyclus van een NUMMERAANDUIDING, waarin de betreffende NUMMERAANDUIDING zich bevindt. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Indicatie hoofdadres** 

> **Naam attribuutsoort** Indicatie hoofdadres 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** IndicatieHoofdadres 

> **Definitie attribuutsoort** Indicatie of de NUMMERAANDUIDING een hoofdadres is van het gerelateerde VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 30 maart 2009 

> **Toelichting attribuutsoort** Indien de NUMMERAANDUIDING Geen hoofdadres is van het de genoemde objecten, dan is het daarvan een nevenadres. 

> **Domein attribuutsoort** Formaat: boolean Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Afleidbaar gegeven uit de hoofd- en nevenadresrelaties. 

Indicatie of de NUMMERAANDUIDING een hoofdadres is van het gerelateerde VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS KING 

Indien de NUMMERAANDUIDING Geen hoofdadres is van het de genoemde objecten, dan is het daarvan een nevenadres. 

## **Relatiesoort NUMMERAANDUIDING is hoofdadres van VERBLIJFSOBJECT** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

NUMMERAANDUIDING is hoofdadres van VERBLIJFSOBJECT KING op basis van BAG 

**Code relatiesoort** 

## **Definitie relatiesoort** 

Het VERBLIJFSOBJECT waarbij de NUMMERAANDUIDING als onderdeel van het hoofdadres is opgenomen. KING 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 **Toelichting relatiesoort** 

De relatie is de tegenhanger van het attribuutsoort ‘Aanduiding hoofdadres bij verblijfsobject’ bij het VERBLIJFSOBJECT in de BAG cq. van het relatiesoort VERBLIJFSOBJECT heeft als hoofdadres NUMMERAANDUIDING. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Authentiek 

> **Regels relatiesoort** Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject of een authentiek terrein. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een authentiek terrein. 

## **Relatiesoort NUMMERAANDUIDING is nevenadres van VERBLIJFSOBJECT** 

> **Naam relatiesoort** NUMMERAANDUIDING is nevenadres van VERBLIJFSOBJECT 

**Herkomst relatiesoort** 

KING op basis van BAG 

**Code relatiesoort** 

> **Definitie relatiesoort** Het VERBLIJFSOBJECT waarbij de NUMMERAANDUIDING als onderdeel van het nevenadres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het attribuutsoort ‘Aanduiding nevenadressen bij verblijfsobject’ bij het VERBLIJFSOBJECT in de BAG cq. van het relatiesoort VERBLIJFSOBJECT heeft als nevenadres(sen) NUMMERAANDUIDING. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject of een authentiek terrein. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een authentiek terrein. 

## **Relatiesoort NUMMERAANDUIDING is hoofdadres van LIGPLAATS** 

> **Naam relatiesoort** NUMMERAANDUIDING is hoofdadres van LIGPLAATS 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

**Definitie relatiesoort** 

De LIGPLAATS waarbij de NUMMERAANDUIDING als onderdeel van het hoofdadres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** De relatie is de tegenhanger van de attribuutsoort ‘Aanduiding hoofdadres ligplaats’ bij de LIGPLAATS in de BAG cq. van het relatiesoort LIGPLAATS heeft als hoofdadres NUMMERAANDUIDING. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Authentiek 

> **Regels relatiesoort** Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject, ligplaats of standplaats. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een lig- of standplaats. 

## **Relatiesoort NUMMERAANDUIDING is nevenadres van** LIGPLAATS 

**Naam relatiesoort Herkomst relatiesoort** 

NUMMERAANDUIDING is nevenadres van LIGPLAATS 

KING 

**Code relatiesoort** 

## **Definitie relatiesoort** 

De LIGPLAATS waarbij de NUMMERAANDUIDING als onderdeel van het nevenadres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 **Toelichting relatiesoort** 

De relatie is de tegenhanger van de attribuutsoor ‘Aanduiding nevenadressen ligplaats’ bij de LIGPLAATS in de BAG cq. van het relatiesoort LIGPLAATS heeft als nevenadres(sen) NUMMERAANDUIDING. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

**Indicatie materiële historie** 

## Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject of een authentiek terrein. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een authentiek terrein. 

## **Relatiesoort NUMMERAANDUIDING is hoofdadres van STANDPLAATS** 

> **Naam relatiesoort** NUMMERAANDUIDING is hoofdadres van STANDPLAATS 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De STANDPLAATS waarbij de NUMMERAANDUIDING als onderdeel van het hoofdadres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 

## **Toelichting relatiesoort** 

De relatie is de tegenhanger van de attribuutsoort ‘Aanduiding hoofdadres standplaats’ bij de STANDPLAATS in de BAG cq. van het relatiesoort STANDPLAATS heeft als hoofdadres NUMMERAANDUIDING. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Authentiek 

> **Regels relatiesoort** Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject, ligplaats of standplaats. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een lig- of standplaats. 

## **Relatiesoort NUMMERAANDUIDING is nevenadres van** STANDPLAATS 

> **Naam relatiesoort** NUMMERAANDUIDING is nevenadres van STANDPLAATS 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De STANDPLAATS waarbij de NUMMERAANDUIDING als onderdeel van het nevenadres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** De relatie is de tegenhanger van de attribuutsoor ‘Aanduiding nevenadressen standplaats’ bij de STANDPLAATS in de BAG cq. van het relatiesoort STANDPLAATS heeft als nevenadres(sen) NUMMERAANDUIDING. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

||neve<br>relat<br>NUM<br>De r<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



**Indicatie kardinaliteit Indicatie authentiek Regels relatiesoort** 

## 0 - 1 

Authentiek gegeven 

Elke nummeraanduiding heeft deze relatie dan wel precies één van de andere hoofd- of nevenadresrelaties naar een verblijfsobject of een authentiek terrein. Een nummeraanduiding kan dus slechts het hoofd- of het nevenadres zijn van een verblijfsobject dan wel een authentiek terrein. 

## **Relatiesoort NUMMERAANDUIDING maakt deel uit van locatie-adres van OVERIG GEBOUWD OBJECT** 

> **Naam relatiesoort** NUMMERAANDUIDING maakt deel uit van locatie-adres van OVERIG GEBOUWD OBJECT 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Het OVERIG GEBOUWD OBJECT waarbij de NUMMERAANDUIDING als onderdeel van het locatie-adres is opgenomen 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De nummeraanduiding kan gebruikt worden om in combinatie met de locatie-omschrijving (van het overig gebouwd object) een unieke locatieaanduiding van een overig gebouwd object te creëren. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** De relatie is alleen geldig naar een overig gebouwd object met een gevulde locatie-omschrijving zodanig dat daarmee sprake is van een uniek adres. 

## **Relatiesoort NUMMERAANDUIDING heeft daarop INGESCHREVEN PERSOONen** 

> **Naam relatiesoort** NUMMERAANDUIDING heeft daarop INGESCHREVEN PERSOONen 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11.90 

## **Definitie relatiesoort** 

|||
|---|---|
|**Definitie relatiesoort**|De INGESCHREVEN PERSOONen die als inschrijvingsadres gekozen|
||hebben voor de NUMMERAANDUIDING bij het ADRESSEERBAAR|
||OBJECT waarin zij verblijven.|
|**Datum opname relatiesoort**|1 maart 2009|
|**Toelichting relatiesoort**|Het betreft het hergebruik als relatiesoort van element 08.11.90|
||(Identificatiecode nummeraanduiding) van groep 11 (Adres) van categorie|
||08 (Verblijfplaats)  in de GBA in de gevallen dat de persoon verblijft op|
||een adresseerbaar object. De ingeschreven persoon kan er aldus voor|
||kiezen zich op een hoofd- of op een nevenadres te laten inschrijven.|
||De relatie is de tegenhanger van INGESCHREVEN PERSOON is|
||ingeschreven op NUMMERAANDUIDING.|
||Zie verder de toelichting in de GBA bij genoemde groep en bijbehorende|
||elementen.|
||Het huisnummer kan de waarde 0 hebben.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Authentiek gegeven|
|**Regels attribuutsoort**||



## **2.38. Openbare Ruimte** 

## **Attribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De gegevens van de OPENBARE RUIMTE zoals die zijn opgenomen in de BasisRegistratie Adressen. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 

> **Toelichting attribuutsoort** Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. Het groepattribuutsoort bestaat uit de volgende attribuutsoort: 11.01 Identificatiecode openbare ruimte en de volgende relatiesoorten: OPENBARE RUIMTE ligt in WOONPLAATS OPENBARE RUIMTE heeft ADRESSEERBAAR OBJECT AANDUIDING 

> **Domein attribuutsoort** n.v.t 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Identificatiecode openbare ruimte** 

> **Naam attribuutsoort** Identificatiecode openbare ruimte 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.01 

> **XML-tag attribuutsoort** identificatie 

## **Definitie attribuutsoort** 

De unieke aanduiding van een OPENBARE RUIMTE. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Huisnummerrange even nummers** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Huisnummerrange even nummers 

KING 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** huisnummerrangeEven **Definitie attribuutsoort** 

Het laagste en het hoogste huisnummer, zijnde even getallen, van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd  zijn aan de OPENBARE RUIMTE en die gelegen zijn aan één van beide zijden van de OPENBARE RUIMTE. 

**Herkomst definitie attribuutsoort** 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

9 april 2007 

Veelal liggen de even huisnummers aan één van beide zijden van de openbare ruimte. Het komt evenwel voor dat deze aan beide zijden liggen.  In dat geval wordt de huisnummerrange vastgelegd met ‘Huisnummerrange even en oneven nummers’. 

Formaat: AN11 (NNNNN-NNNNN) Waardenverzameling: even huisnummers van nummeraanduidingen die gerelateerd zijn aan de openbare ruimte 

N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Het is geen verplicht te registreren gegeven. Als dit gegeven gevuld is dan mogen de gegevens ‘Huisnummerrange oneven nummers’ en ‘Huisnummerrange even en oneven nummers’ niet gevuld zijn. 

## **Attribuutsoort Huisnummerrange oneven nummers** 

|**Naam attribuutsoort**|Huisnummerrange oneven nummers|
|---|---|
|**Herkomst attribuutsoort**|KING|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|huisnummerrangeOneven|
|**Definitie attribuutsoort**|Het laagste en het hoogste huisnummer, zijnde oneven getallen, van de|
||objecten waaraan NUMMERAANDUIDINGen zijn toegekend die|
||gerelateerd  zijn aan de OPENBARE RUIMTE en die gelegen zijn aan|
||één van beide zijden van de OPENBARE RUIMTE.|
|**Herkomst definitie attribuutsoort**|KING|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|Veelal liggen de oneven huisnummers aan één van beide zijden van de|
||openbare ruimte. Het komt evenwel voor dat deze aan beide zijden|
||liggen.  In dat geval wordt de huisnummerrange vastgelegd met|
||‘Huisnummerrange even en oneven nummers’.|
|**Domein attribuutsoort**|Formaat:<br>AN11 (NNNNN-NNNNN)|
||Waardenverzameling: oneven huisnummers van nummeraanduidingen|
||die gerelateerd zijn aan de openbare ruimte|
|**Indicatie materiële historie**|N|
|**Indicatie formele historie**|N|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels attribuutsoort**|Het is geen verplicht te registreren gegeven. Als dit gegeven gevuld is|
||dan mogen de gegevens ‘Huisnummerrange even nummers’ en|
||‘Huisnummerrange even en oneven nummers’ niet gevuld zijn.|



## **Attribuutsoort Huisnummerrange even en oneven nummers** 

**Naam attribuutsoort** 

Huisnummerrange even en oneven nummers 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

KING 

huisnummerrangeEvenOneven 

> **Definitie attribuutsoort** Het laagste en het hoogste huisnummer van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd  zijn aan de OPENBARE RUIMTE in die gevallen dat aan één of beide zijden van de OPENBARE RUIMTE zowel even als oneven huisnummers voorkomen dan wel dat even en/of oneven huisnummers aan beide zijden van de openbare ruimte voorkomen. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Veelal liggen de even en de oneven huisnummers telkens aan één van beide zijden van de openbare ruimte. Het komt evenwel voor dat deze aan beide zijden liggen of dat er aan één zijde zowel even als oneven huisnummers voorkomen. Dit gegeven voorziet in de twee laatstgenoemde situaties. 

> **Domein attribuutsoort** Formaat: AN11 (NNNNN-NNNNN) Waardenverzameling: huisnummers van nummeraanduidingen die gerelateerd zijn aan de openbare ruimte 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Het is geen verplicht te registreren gegeven. Als dit gegeven gevuld is dan mogen de gegevens ‘Huisnummerrange even nummers’ en ‘Huisnummerrange oneven nummers’ niet gevuld zijn. 

## **Relatiesoort OPENBARE RUIMTE ligt in WOONPLAATS** 

> **Naam relatiesoort** OPENBARE RUIMTE ligt in WOONPLAATS 

> **Herkomst relatiesoort** BAG 

> **Code relatiesoort** 11.15 

## **Definitie relatiesoort** 

> **Definitie relatiesoort** Unieke aanduiding van de woonplaats waarbinnen een OPENBARE RUIMTE is gelegen. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het attribuutsoort ‘Identificatiecode bijbehorende woonplaats’ bij de NUMMERAANDUIDING in de BAG. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort OPENBARE RUIMTE heeft ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** OPENBARE RUIMTE heeft ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING op basis van BAG 

> **Code relatiesoort** 11.65 

> **Definitie relatiesoort** De ADRESSEERBAAR OBJECT AANDUIDINGen van de objecten die gelegen zijn aan de OPENBARE RUIMTE. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het attribuutsoort ‘Identificatiecode 

OPENBARE RUIMTE heeft ADRESSEERBAAR OBJECT AANDUIDING 

De relatie is de tegenhanger van het attribuutsoort ‘Identificatiecode bijbehorende openbare ruimte’ bij de NUMMERAANDUIDING in de BAG cq. van het relatiesoort ADRESSEERBAAR OBJECT AANDUIDING ligt aan OPENBARE RUIMTE. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

||bijbe<br>cq. v<br>aan<br>De r<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|



**Indicatie authentiek** 

**Regels relatiesoort** 

Gemeentelijk basisgegeven 

- 

## **Relatiesoort OPENBARE RUIMTE maakt deel uit van GEMEENTELIJKE OPENBARE RUIMTE** 

> **Naam relatiesoort** OPENBARE RUIMTE maakt deel uit van GEMEENTELIJKE OPENBARE RUIMTE 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** - 

> **Definitie relatiesoort** De GEMEENTELIJKE OPENBARE RUIMTE waarvan de OPENBARE RUIMTE deel uit maakt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Deze relatie is de tegenhanger van de relatie GEMEENTELIJKE OPENBARE RUIMTE heeft OPENBARE RUIMTE. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort OPENBARE RUIMTE maakt deel uit van straatadres van OVERIG GEBOUWD OBJECT** 

> **Naam relatiesoort** OPENBARE RUIMTE maakt deel uit van straatadres van OVERIG GEBOUWD OBJECT 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De OVERIGe GEBOUWDe OBJECTen waaraan geen officieel adres is toegekend die gelegen zijn aan of nabij de OPENBARE RUIMTE 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

De OVERIGe GEBOUWDe OBJECTen waaraan geen officieel adres is toegekend die gelegen zijn aan of nabij de OPENBARE RUIMTE KING 

9 april 2007 

**Toelichting relatiesoort** 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het relatiesoort OVERIG GEBOUWD OBJECT heeft straatadres i.c.m. OPENBARE RUIMTE. De relatie wordt alleen geregistreerd indien bij een overig gebouwd object geen overig adres als officieel adres is vastgelegd. Het heeft de voorkeur geen gebruik te maken van deze relatie d.w.z. om ook aan overige gebouwde objecten officiële adressen toe te kennen. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort OPENBARE RUIMTE heeft nabijgelegen WOZ-OBJECT** 

**Naam relatiesoort Herkomst relatiesoort** BRWOZ/KING **Code relatiesoort** 11.01b **Definitie relatiesoort** 

OPENBARE RUIMTE bepaalt aanduiding van WOZ-OBJECT 

De unieke aanduidingen van de WOZ-OBJECTen waarvan de aanduidingen worden afgeleid met behulp van de naam van de OPENBARE RUINTE  en de locatieaanduiding van het WOZ-OBJECT. KING op basis van de catalogus BRWOZ 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Adresseerbaar object voor aanduiding WOZ-object’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZ-OBJECT ligt aan OPENBARE RUIMTE. Zie verder de toelichting in de BRWOZ. 

|**Toelichting relatiesoort**|In d<br>obje<br>het<br>tege<br>Zie|
|---|---|
|**Indicatie materiële historie**|J|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|



**Indicatie authentiek Regels relatiesoort** 

Niet-authentiek landelijk basisgegeven. 

- 

## **2.39. Ouder-kind-relatie** 

## **Attribuutsoort Datum ingang familierechtelijke betrekking** 

> **Naam attribuutsoort** Datum ingang familierechtelijke betrekking 

> **Herkomst attribuutsoort** KING op basis van GBA 

> **Code attribuutsoort** 02/03.62.10 

> **XML-tag attribuutsoort** datumIngangFamilierechtelijkeBetrekking 

> **Definitie attribuutsoort** De datum waarop de familierechtelijke betrekking is ontstaan. 

> **Herkomst definitie attribuutsoort** GBA 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Afhankelijk of de OUDER-KIND-RELATIE ouder1 of ouder2 betreft, gaat het om het GBA-element 62.10 in GBA-categorie 02 (Ouder1) resp. 03 (Ouder2). Zie verder de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Attribuutsoort Datum einde familierechtelijke betrekking** 

> **Naam attribuutsoort** Datum einde familierechtelijke betrekking 

> **Herkomst attribuutsoort** GFO 

> **Code attribuutsoort** 95.18 

> **XML-tag attribuutsoort** datumEindeFamilierechtelijkeBetrekking **Definitie attribuutsoort** eindigt. 

> **Herkomst definitie attribuutsoort** GFO 

> **Datum opname attribuutsoort** 1 mei 2008 **Toelichting attribuutsoort** 

Datum einde familierechtelijke betrekking 

De datum waarop de familierechtelijke betrekking tussen ouder en kind eindigt. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Attribuutsoort Ouder-aanduiding** 

> **Naam attribuutsoort** Ouder-aanduiding 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** ouderAanduiding **Definitie attribuutsoort** 

Aanduiding of de OUDER-KIND-RELATIE Ouder1 of Ouder2 betreft, zoals aangeduid in de GBA 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 mei 2008 **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Elke ouder-kind-relatie specificeert de relatie tussen een kind en één van beide ouders. Deze ouders zijn in de GBA aangeduid als Ouder1 en Ouder2. Dit attribuutsoort geeft aan op welke van beide ouders de ouderkind-relatie betrekking heeft. Dit is onder meer van belang voor de juiste interpretatie van de attribuutsoort INGESCHREVEN PERSOON . Indicatie gezag minderjarige. 

> **Domein attribuutsoort** Formaat: AN6 Waardenverzameling: Ouder1, Ouder2 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Regels attribuutsoort** 

## **Relatiesoort OUDER-KIND-RELATIE betreft kind zijnde INGESCHREVEN PERSOON** 

> **Naam relatiesoort** OUDER-KIND-RELATIE betreft kind zijnde INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 09 

> **Definitie relatiesoort** De INGESCHREVEN PERSOON zijnde het kind waarnaar de OUDERKIND-RELATIE verwijst. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) incategorie 09 (Kind) in de GBA. De relatie is de tegenhanger van INGESCHREVEN PERSOON is kind in OUDER–KIND-RELATIEs. Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort OUDER-KIND-RELATIE betreft ouder zijnde INGESCHREVEN-PERSOON** 

> **Naam relatiesoort** OUDER-KIND-RELATIE betreft ouder zijnde  INGESCHREVENPERSOON 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 02/03 

> **Definitie relatiesoort** De INGESCHREVEN-PERSOON, zijnde de ouder, waarnaar de KINDOUDER–RELATIE verwijst. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

De INGESCHREVEN-PERSOON, zijnde de ouder, waarnaar de KINDOUDER–RELATIE verwijst. 

9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 01 (Identificatienummers) in de categoriën 02 (Ouder1) en 03 (Ouder2) in de GBA. De relatie is de tegenhanger van INGESCHREVEN-PERSOON is ouder in  OUDER–KIND-RELATIEs Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: AkteGemeente, Documentidentificatie, Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

> **Regels relatiesoort** . 

## **2.40. Overige adresseerbaar object aanduiding** 

## **Relatiesoort OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG GEBOUWD OBJECT** 

> **Naam relatiesoort** OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG GEBOUWD OBJECT 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Het OVERIG GEBOUWD OBJECT waarbij de OVERIGE ADRESSEERBAAR OBJECT AANDUIDING als onderdeel van het officiële adres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het relatiesoort OVERIG GEBOUWD OBJECT heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentnummer 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Elk overig adres heeft of deze relatie dan wel de vergelijkbare relatie naar een overig terrein. Een overig adres kan dus slechts het officiële adres zijn van een overig gebouwd object dan wel een overig terrein. 

## **Relatiesoort OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG TERREIN** 

> **Naam relatiesoort** OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG TERREIN 

> **Herkomst relatiesoort** KING **Code relatiesoort Definitie relatiesoort** 

Het OVERIG TERREIN waarbij de OVERIGE ADRESSEERBAAR OBJECT AANDUIDING als onderdeel van het officiële adres is opgenomen. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van het relatiesoort OVERIG TERREIN heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentnummer 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0 - 1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Elk overig adres heeft of deze relatie dan wel de vergelijkbare relatie naar een overig gebouwd object. Een overig adres kan dus slechts het officiële adres zijn van een overig gebouwd object dan wel een overig terrein. 

## **2.41. Overig gebouwd object** 

## **Attribuutsoort Overig gebouwd object locatie-aanduiding** 

> **Naam attribuutsoort** Overig gebouwd object locatie-aanduiding 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** locatieAanduiding 

> **Definitie attribuutsoort** De aanvullende omschrijving van de ligging van een OVERIG GEBOUWD OBJECT ten opzichte van de dichtstbijzijnde VERBLIJFSOBJECT, STANDPLAATS, LIGPLAATS of OPENBARE RUIMTE. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Indien aan een overig gebouwd object geen officieel adres wordt toegekend (door middel van de overige adresseerbaar object aanduiding) wordt een unieke adresaanduiding verkregen door een ‘authentiek’ adres dan wel woonplaats/straatnaam te combineren met de locatie-aanduiding. 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: alle bestaande alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Het gegeven moet worden geregistreerd indien de relatie OVERIG GEBOUWD OBJECT heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING niet is geregistreerd. Is laatstgenoemde relatie wel aanwezig, dan mag het gegeven niet worden geregistreerd. 

## **Attribuutsoort Overig gebouwd object type** 

> **Naam attribuutsoort** Overig gebouwd object type 

> **Herkomst attribuutsoort** KING op basis van GFO BG 

> **Code attribuutsoort** 95.83 

> **XML-tag attribuutsoort** type 

> **Definitie attribuutsoort** Indeling naar de aard van het OVERIG GEBOUWD OBJECT 

> **Herkomst definitie attribuutsoort** KING op basis van GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: nog nader te bepalen 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Niet verplicht te registreren 

## **Attribuutsoort Bouwjaar** 

> **Naam attribuutsoort** Bouwjaar 

> **Herkomst attribuutsoort** KING op basis van StUF-TAX 

> **Code attribuutsoort** 61.20 **XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De aanduiding van het jaar waarin het OVERIG GEBOUWD OBJECT oorspronkelijk als bouwkundig gereed is opgeleverd. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 november 2008 

> **Toelichting attribuutsoort** Analoog aan het PAND is ook bij OVERIG GEBOUWD OBJECT het Bouwjaar opgenomen. Bijhouding kan plaatsvinden vanuit het WOZproces. 

> **Domein attribuutsoort** Formaat: N4 Waardenverzameling: 0-9999 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

## **Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Regels attribuutsoort** 

## **Relatiesoort OVERIG GEBOUWD OBJECT heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING** 

**Naam relatiesoort Herkomst relatiesoort** 

OVERIG GEBOUWD OBJECT heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De OVERIGE ADRESSEERBAAR OBJECT AANDUIDING waaronder het officiële adres is opgenomen. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Met deze relatie wordt het mogelijk aan een overig gebouwd object een officieel adres toe te kennen zijnde geen nummeraanduiding als onderdeel van een ‘authentiek adres’. De relatie is de tegenhanger van OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG GEBOUWD OBJECT. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentnummer 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien de relatie is geregistreerd mag het gegeven ‘Overig gebouwd object locatie-aanduiding’ niet worden geregistreerd en mogen de relaties naar nummeraanduiding en openbare ruimte evenmin worden geregistreerd. 

## **Relatiesoort OVERIG GEBOUWD OBJECT heeft locatie-adres i.c.m. NUMMERAANDUIDING** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

OVERIG GEBOUWD OBJECT heeft locatie-adres i.c.m. NUMMERAANDUIDING KING 

**Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

De NUMMERAANDUIDING waaronder het locatie-adres is opgenomen. 

## KING 

9 april 2007 

Met een locatie-adres wordt bedoeld de combinatie van woonplaatsnaam, openbare ruimte naam, huisnummer, huisletter, huisnummertoevoeging en overig gebouwd object locatie-aanduiding. Met deze relatie wordt het mogelijk aan een overig gebouwd object een locatie-adres toe te kennen dat verwijst naar de nummeraanduiding van het dichtstbijzijnde verblijfsobject, standplaats of ligplaats. De relatie is de tegenhanger van NUMMERAANDUIDING maakt deel uit van locatie-adres van OVERIG GEBOUWD OBJECT. 

J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien de relatie is geregistreerd moet het gegeven ‘Overig gebouwd object locatie-aanduiding’ eveneens worden geregistreerd en mogen de relaties naar overige adresseerbaar object aanduiding en openbare ruimte niet worden geregistreerd. 

## **Relatiesoort OVERIG GEBOUWD OBJECT heeft straatadres i.c.m. OPENBARE RUIMTE** 

> **Naam relatiesoort** OVERIG GEBOUWD OBJECT heeft straatadres i.c.m. OPENBARE RUIMTE 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

> **Definitie relatiesoort** De OPENBARE RUIMTE waaraan of waar nabij het OVERIG GEBOUWD OBJECT is gelegen. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Met een straatadres wordt bedoeld de combinatie van woonplaatsnaam, openbare ruimte naam en overig gebouwd object locatie-aanduiding. Met deze relatie wordt het mogelijk aan een overig gebouwd object een ‘straatadres’ toe te kennen dat verwijst naar de dichtstbijzijnde openbare ruimte. De relatie is de tegenhanger van OPENBARE RUIMTE maakt deel uit van straatadres van OVERIG GEBOUWD OBJECT. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien de relatie is geregistreerd moet het gegeven ‘Overig gebouwd object locatie-aanduiding’ eveneens worden geregistreerd en mogen de relaties naar overige adresseerbaar object aanduiding en nummeraanduiding niet worden geregistreerd. 

## **2.42. Overig Terrein** 

## **Attribuutsoort Gebruiksdoel overig terrein** 

**Naam attribuutsoort** 

Gebruiksdoel overig terrein 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** gebruiksdoel 

> **Definitie attribuutsoort** Een categorisering van de gebruiksdoelen van het betreffende OVERIG TERREIN, zoals dit formeel door de overheid als zodanig is toegestaan. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort en de definitie zijn afgeleid van het gebruiksdoel bij het verblijfsobject in de BAG cq. bij het gebouwd object in het voorliggende model. 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: het domein ‘gebruiksdoeleinden’ in de BAG 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Een categorisering van de gebruiksdoelen van het betreffende OVERIG TERREIN, zoals dit formeel door de overheid als zodanig is toegestaan. 

## **Relatiesoort OVERIG TERREIN heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** OVERIG TERREIN heeft als officieel adres OVERIGE ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De OVERIGE ADRESSEERBAAR OBJECT AANDUIDING waaronder het officiële adres is opgenomen. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Met deze relatie wordt het mogelijk aan een benoemd terrein een officieel adres toe te kennen zijnde geen nummeraanduiding als onderdeel van een ‘authentiek adres’. De relatie is de tegenhanger van OVERIGE ADRESSEERBAAR OBJECT AANDUIDING is officieel adres van OVERIG TERREIN. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentnummer 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **2.43. Pand** 

## **Attribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De gegevens van het PAND zoals die zijn opgenomen in de BasisGebouwenRegistratie. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 **Toelichting attribuutsoort** 

Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. 

Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 55.01 Pandidentificatie 55.02 Indicatie geconstateerd pand 55.20 Pandgeometrie bovenaanzicht 55.30 Oorspronkelijk bouwjaar pand 55.31 Pandstatus en de volgende relatiesoort: PAND heeft inliggend VERBLIJFSOBJECT **Domein attribuutsoort** n.v.t **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum **Indicatie in onderzoek** Ja **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Pandidentificatie** 

> **Naam attribuutsoort** Pandidentificatie 

> **Herkomst attribuutsoort** BAG 

## **Code attribuutsoort** 

## 55.01 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** De unieke aanduiding van een PAND 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Indicatie geconstateerd pand** 

**Naam attribuutsoort** 

Indicatie geconstateerd pand 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 55.02 

> **XML-tag attribuutsoort** geconstateerd 

**Definitie attribuutsoort** 

|||
|---|---|
|**Definitie attribuutsoort**|Een aanduiding waarmee kan worden aangegeven dat een object in de|
||registratie is opgenomen als gevolg van een feitelijke constatering,|
||zonder dat er op het moment van opname sprake is van een formele|
||grondslag voor deze opname.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|De attribuutsoort maakt deel uit van de groepattribuutsoort BAG-|
||gegevens. Zie verder de toelichting in de BAG.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|



**Indicatie authentiek** 

Niet authentiek gegeven 

## **Attribuutsoort Pandgeometrie bovenaanzicht** 

> **Naam attribuutsoort** Pandgeometrie bovenaanzicht 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 55.20 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

De  minimaal  tweedimensionale  geometrische  representatie  van  het bovenaanzicht van de omtrekken van een PAND 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** In de attribuutnaam is de term ‘bovenaanzicht’ toegevoegd ter onderscheid van de eveneens (optioneel) te registreren geometrie op maaiveld. 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Oorspronkelijk bouwjaar pand** 

**Naam attribuutsoort** 

Oorspronkelijk bouwjaar pand 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 55.30 

> **XML-tag attribuutsoort** bouwjaar 

> **Definitie attribuutsoort** De aanduiding van het jaar waarin een PAND oorspronkelijk als bouwkundig gereed is of wordt opgeleverd. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Pandstatus** 

> **Naam attribuutsoort** Pandstatus 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 55.31 

> **XML-tag attribuutsoort** status **Definitie attribuutsoort** PAND zich bevindt. 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

De fase van de levenscyclus van een PAND, waarin het betreffende PAND zich bevindt. 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

## **Attribuutsoort Inwinningswijze geometrie bovenaanzicht** 

**Naam attribuutsoort** 

Inwinningswijze geometrie bovenaanzicht 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** inwinningswijzeGometrieBovenaanzicht 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De wijze waarop de geometrie van het bovenaanzicht van het PAND verkregen is 

KING 

**Datum opname attribuutsoort** 

30 november 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Ontleend aan NEN1878 (eerste vijf domeinen), aangevuld met voor de BAG relervante inwinningstechnieken 

Formaat: AN24 Waardeverzameling: niet bekend terrestrische meting fotogrammetrische meting (stereo) digitalisering kaart scanning kaart fotogrammetrische meting (mono) Ontleend aan de bouwplantekening Ontleend aan het matenplan 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Pandgeometrie maaiveld** 

> **Naam attribuutsoort** Pandgeometrie maaiveld 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** geometrieOpMaaiveld 

> **Definitie attribuutsoort** De tweedimensionale geometrische representatie van de omtrekken van een PAND op maaiveldniveau 

**Herkomst definitie attribuutsoort** 

KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een pand. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De begrenzing treedt niet buiten de geometrie van het bovenaanzicht van het pand. 

## **Attribuutsoort Inwinningswijze geometrie maaiveld** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Inwinningswijze geometrie maaiveld 

KING 

- 

inwinningswijzeGometrieMaaiveld 

De wijze waarop de geometrie van het PAND op maaiveldniveau verkregen is 

KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

30 november 2007 

Ontleend aan NEN1878 (eerste vijf domeinen), aangevuld met voor de BAG relervante inwinningstechnieken 

Formaat: AN24 Waardeverzameling: niet bekend terrestrische meting fotogrammetrische meting (stereo) digitalisering kaart scanning kaart fotogrammetrische meting (mono) Ontleend aan de bouwplantekening Ontleend aan het matenplan 

|**Indicatie materiële historie**|N|
|---|---|
|**Indicatie formele historie**|N|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|



## **Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Laagste bouwlaag pand** 

**Naa atttribuutsoort** Laagste bouwlaag pand 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.53 

> **XML-tag attribuutsoort** laagsteBouwlaag **Definitie attribuutsoort** 

De ligging van de laagste bouwlaag van het pand gerekend ten opzichte van het straatpeil. 

## **Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

Voor de definitie van bouwlaag wordt verwezen naar NEN 2580 (2e druk, 1997): 'Een deel van een gebouw, dat bestaat uit een of meer ruimten, waarbij de bovenkanten van de afgewerkte vloeren van twee aan elkaar grenzende ruimten niet meer dan 1,5 meter in hoogte verschillen'. Onder straatpeil wordt verstaan: 

a. Voor een bouwwerk, waarvan de hoofdtoegang direct aan de weg grenst, de krachtens besluit van burgemeester en wethouders vastgestelde hoogte van de weg ter plaatse van de hoofdtoegang; b. Voor een bouwwerk, waarvan de hoofdtoegang niet direct aan de weg grenst: de hoogte van het terrein ter plaatse van de hoofdtoegang bij voltooiing van de bouw (Model-bouwverordening). De bouwlaag op straatpeil heeft de waarde 0. Indien de laagste bouwlaag onbekend is, wordt geen waarde ingevuld. **Domein attribuutsoort** Formaat: N3 Waardenverzameling: -99 tot +999 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** - 

## **Attribuutsoort Hoogste bouwlaag pand** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Hoogste bouwlaag pand 

## GFO BG 

> **Code attribuutsoort** 95.32 

> **XML-tag attribuutsoort** hoogsteBouwlaag **Definitie attribuutsoort** 

De ligging van de hoogste bouwlaag van het pand gerekend ten opzichte van het straatpeil. 

## **Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

Voor de definitie van bouwlaag wordt verwezen naar NEN 2580 (2e druk, 1997): 'Een deel van een gebouw, dat bestaat uit een of meer ruimten, waarbij de bovenkanten van de afgewerkte vloeren van twee aan elkaar grenzende ruimten niet meer dan 1,5 meter in hoogte verschillen'. Onder straatpeil wordt verstaan: 

a. Voor een bouwwerk, waarvan de hoofdtoegang direct aan de weg grenst, de krachtens besluit van burgemeester en wethouders vastgestelde hoogte van de weg ter plaatse van de hoofdtoegang; b. Voor een bouwwerk, waarvan de hoofdtoegang niet direct aan de weg grenst: de hoogte van het terrein ter plaatse van de hoofdtoegang bij voltooiing van de bouw (Model-bouwverordening). De hoogste bouwlaag pand geeft dus niet aan uit hoeveel bouwlagen het pand bestaat. Dit laatste kan berekend worden uit 'hoogste bouwlaag' en 'laagste bouwlaag' van het pand. De bouwlaag op straatpeil heeft de waarde 0. Indien de hoogste bouwlaag onbekend is, wordt geen waarde ingevuld. **Domein attribuutsoort** Formaat: N3 Waardenverzameling: -99 tot +999 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** - 

## **Attribuutsoort Relatieve hoogteligging pand** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Relatieve hoogteligging pand 

IMGeo 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

relatieveHoogteligging 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** IMGeo **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Aanduiding voor de relatieve hoogte van het object 

Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: N1 Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum begin geldigheid pand** 

**Naam attribuutsoort** 

Datum begin geldigheid pand 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

De datum waarop van gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een PAND conform de vergunning, de melding of de aanschrijving zijn uitgevoerd. KING 

**Herkomst definitie attribuutsoort** 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Aangezien een pand al geregistreerd wordt voordat de bouwgereedmelding is ontvangen, of mogelijkerwijs al voordat de bouw is aangevangen of voordat de bouwvergunning is verleend, kan het gegeven gedurende een bepaalde periode niet gevuld zijn. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Verplicht te registreren 

## **Attribuutsoort Datum einde geldigheid pand** 

> **Naam attribuutsoort** Datum einde geldigheid pand 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het pand is gesloopt volgens de sloopgereedmedling. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Onder sloop wordt verstaan dat alle muren, wanden, vloeren en daken zijn verdwenen. De fundering hoeft niet te zijn verwijderd. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: geldige, evt. onvolledige datums 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

## Gemeentelijk basisgegeven 

## Verplicht te registreren. 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid …’ kan in de registratie worden opgenomen. Aangezien zich in een vervallen pand geen geldige verblijfsobjecten kunnen bevinden dient de datum op of na de einddatum geldigheid van het verblijfsobject te liggen. 

## **Attribuutsoort Status voortgang bouw** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Status voortgang bouw 

## KING 

- 

statusVoortgangBouw 

De fase van de bouw, verbouw of sloop waarin het betreffende PAND zich bevindt 

KING 

|**Datum opname attribuutsoort**|30 november 2007||
|---|---|---|
|**Toelichting attribuutsoort**|Zie ‘Status voortgang|bouw’ bij VERBLIJFSOBJE|
|**Domein attribuutsoort**|Formaat:|AN24|
||Waardeverzameling:|Vergunning aangevraagd|
|||Vergunning verleend|
|||Bouw of sloop gestart|
|||Bouw of sloop gereed|
|||Vergunning ingetrokken|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



Zie ‘Status voortgang bouw’ bij VERBLIJFSOBJECT. 

## **Attribuutsoort Oppervlakte pand** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

## Oppervlakte pand 

## KING 

> **Code attribuutsoort** 56.31 

> **XML-tag attribuutsoort** oppervlakte 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** KING **Datum opname attribuutsoort** 1 maart 2009 

De gebruiksoppervlakte van een PAND in gehele vierkante meters. 

**Toelichting attribuutsoort** 

De BAG kent dit gegeven niet bij PAND, wel bij VERBLIJFSOBJECT. Het is aan PAND toegevoegd omdat dit gegeven wel vanuit het WOZ-proces wordt bijgehouden voor panden zonder verblijfsobjecten. Zie verder de toelichting bij het vergelijkbare gegeven in de BAG en de bijbehorende domeinbeschrijving.. 

## **Domein attribuutsoort** 

Formaat: N6 Waardenverzameling: 0 – 999999 vierkante meter Ja 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Niet verplicht te registreren 

## **Attribuutsoort Bruto inhoud pand** 

**Naam attribuutsoort** 

Bruto inhoud pand 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** 94.96 

> **XML-tag attribuutsoort** brutoInhoud 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** 

Aanduiding in kubieke meters van de bruto inhoud van het PAND. 

## KING 

**Datum opname attribuutsoort** 

1 maart 2009 

> **Toelichting attribuutsoort** De BAG kent dit gegeven niet. Het is aan PAND toegevoegd omdat dit gegeven wel vanuit het WOZ-proces wordt bijgehouden voor panden zonder verblijfsobjecten. Bruto inhoud betreft de buitenwerks gemeten inhoud, inclusief dakopbouwen en kelders, maar exclusief lichtkoepels, loggia's, schoorstenen, dakkapellen en bijgebouwen, die niet onder dezelfde dakconstructie zijn gelegen. Bij een dakopbouw is de gevel doorgetrokken of de nok verhoogd. Een dakkapel is slechts een uitbouw uit het schuine dakvlak. Bijgebouwen die inpandig zijn, dus die onder dezelfde dakconstructie vallen, dienen te worden gekubeerd bij de bruto inhoud van het object. Een loggia is een veelal overdekt inpandig balkon (Stuf-WOZ, p. 272). Alternatieve definities voor inhouden zijn te vinden in NEN 2580 (2e druk, 1997). 

> **Domein attribuutsoort** Formaat: N6 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Niet verplicht te registreren 

Formaat: N6 Waardenverzameling: 0 – 999999 kubieke meter Ja 

## **Relatiesoort PAND heeft inliggend VERBLIJFSOBJECT** 

**Naam relatiesoort Herkomst relatiesoort** 

PAND heeft inliggend VERBLIJFSOBJECT 

KING op basis van BAG 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De unieke aanduidingen van de VERBLIJFSOBJECTen die geheel of gedeeltelijk gelegen zijn binnen het PAND. 

KING 

**Datum opname relatiesoort** 

**Toelichting relatiesoort** 

9 april 2007 

De relatie is de tegenhanger van het attribuutsoort ‘pandrelatering’ bij het VERBLIJFSOBJECT in de BAG cq. van het relatiesoort VERBLIJFSOBJECT maakt deel uit van één of meer PANDen. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichting in de BAG. 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-M 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort PAND zonder verblijfsobject ligt in BUURT** 

**Naam relatiesoort Herkomst relatiesoort** 

PAND zonder verblijfsobject ligt in BUURT 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De BUURT waarin het PAND gelegen is waarbinnen zich geen verblijfsobjecten bevinden. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** 

De relatie wordt alleen gelegd voor panden waarbinnen geen verblijfsobjecten zijn afgebakend, zoals bijvoorbeeld een vrijstaande garage bij een woonhuis. Verder wordt de relatie alleen gelegd indien het desbetreffende pand niet is geregistreerd als bijgebouw van een verblijfsobject. 

De relatie is de tegenhanger van het relatiesoort BUURT omvat PAND. 

**Indicatie materiële historie** 

## Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

Voor elk pand waarbinnen geen verblijfsobjecten zijn onderscheiden wordt deze relatie gelegd dan wel de relatie PAND is bijgebouw van VERBLIJFSOBJECT. 

## **Relatiesoort PAND bestaat uit WOZ-DEELOBJECTen** 

**Naam relatiesoort** 

PAND bestaat uit WOZ-DEELOBJECTen 

**Herkomst relatiesoort Code relatiesoort Definitie relatiesoort** 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

**Indicatie materiële historie** 

KING 

55.01b 

De unieke aanduidingen van de WOZ-DEELOBJECTen die deel uitmaken van het PAND. 

KING op basis van de catalogus BRWOZ 

30 november 2007 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde panden’ bij het WOZ-object. In het RSGB wordt dit hergebruikt als relatiesoort vanuit WOZ-DEELOBJECT. De relatie is de tegenhanger van WOZ-DEELOBJECT is gedeelte van PAND. 

J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven. 

**Regels relatiesoort** 

- 

## **2.44. Rechtspersoon** 

## **Relatiesoort RECHTSPERSOON is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT** 

> **Naam relatiesoort** RECHTSPERSOON is eigenaar van MAATSCHAPPELIJKE ACTIVITEIT 

> **Herkomst relatiesoort** KING op basis van NHR **Code relatiesoort** 

> **Definitie relatiesoort** nog niet in NHR uitgewerkt 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft de maatschappelijke activiteit die door de rechtspersoon wordt uitgevoerd. Deze maatschappelijke activiteit kan al dan niet de vorm hebben van een onderneming. Zowel natuurlijke als niet-natuurlijke personen kunnen maatschappelijke activiteiten uitvoeren. Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘FInummer eigenaar’ bij het objecttype Maatschappelijke activiteit in het NHR. De relatie is de tegenhanger van MAATSCHAPPELIJKE ACTIVITEIT heeft als eigenaar. RECHTSPERSOON Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort RECHTSPERSOON heeft rol als FUNCTIONARIS** 

> **Naam relatiesoort** RECHTSPERSOON heeft rol als FUNCTIONARIS 

> **Herkomst relatiesoort** KING op basis van NHR **Code relatiesoort** 

> **Definitie relatiesoort** nog niet in NHR uitgewerkt 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** De relatie is de tegenhanger van FUNCTIONARIS rol wordt vervuld door RECHTSPERSOON. 

Het betreft de verwijzing naar de relaties die aangeven van welke ingeschreven niet natuurlijke personen de rechtspersoon is geregistreerd als functionaris die namens deze personen optreedt. Zie verder de toelichting bij het objecttype FUNCTIONARIS. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven indien het subject een maat of vennoot (met uitzondering van de commanditaire vennoten) betreft die behoort bij een maatschap, een vennootschap onder firma of een commanditaire vennootschap. Anders een niet authentiek landelijk basisgegeven. 

## **Relatiesoort RECHTSPERSOON is gerechtigde van ZAKELIJK RECHT** 

**Naam relatiesoort Herkomst relatiesoort** 

RECHTSPERSOON is gerechtigde van ZAKELIJK RECHT 

KING op basis van BRK 

**Code relatiesoort** 

**Definitie relatiesoort** 

De ZAKELIJKe RECHTen die op naam van de RECHTSPERSOON zijn gesteld. 

> **Herkomst definitie relatiesoort** KING op basis van BRK 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht . gerechtigde’ bij het objecttype RECHT in de BRK. De relatie is de tegenhanger van ZAKELIJK RECHT heeft als gerechtigde RECHTSPERSOON. 

Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

**Indicatie authentiek** 

## **Regels relatiesoort** 

## **Relatiesoort RECHTSPERSOON is betrokken bij KADASTRALE ONROERENDE ZAAK AANTEKENING** 

> **Naam relatiesoort** RECHTSPERSOON is betrokken bij KADASTRALE ONROERENDE ZAAK AANTEKENING 

> **Herkomst relatiesoort** KING op basis van BRK **Code relatiesoort** 

> **Definitie relatiesoort** De aantekeningen op KADASTRALE ONROERENDE ZAAKen waarbij de RECHTSPERSOON betrokken is. 

> **Herkomst definitie relatiesoort** KING op basis van BRK **Datum opname relatiesoort** 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘onroerende zaak . aantekening . betrokken persoon’ bij het objecttype KADASTRALE ONROERENDE ZAAK in de BRK. De relatie is de tegenhanger van KADASTRALE  ONROERENDE ZAAK AANTEKENING heeft betrokken RECHTSPERSOON. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven **Regels relatiesoort** 

## **Relatiesoort RECHTSPERSOON is betrokken bij ZAKELIJK RECHT AANTEKENING** 

> **Naam relatiesoort** RECHTSPERSOON is betrokken bij ZAKELIJK RECHT AANTEKENING 

> **Herkomst relatiesoort** KING op basis van BRK **Code relatiesoort** 

> **Definitie relatiesoort** De ZAKELIJK RECHT AANTEKENINGen waarbij de RECHTSPERSOON betrokken is. 

> **Herkomst definitie relatiesoort** KING op basis van BRK 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht . aantekening recht . betrokken persoon’ bij het objecttype RECHT in de BRK. De relatie is de tegenhanger van ZAKELIJK RECHT AANTEKENING heeft betrokken RECHTSPERSOON. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort RECHTSPERSOON is voornaamste zakelijk gerechtigde van KADASTRALE ONROERENDE ZAAK** 

**Naam relatiesoort** 

RECHTSPERSOON is voornaamste zakelijk gerechtigde van KADASTRALE ONROERENDE ZAAK 

**Herkomst relatiesoort Code relatiesoort** 94.23 **Definitie relatiesoort** 

KING o.b.v. GFO BG 

De kadastrale objecten waarvan de rechtspersoon de voornaamste zakelijk gerechtigde is. 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

KING o.b.v. GFO BG 

## 1 mei 2008 

Waarvan de rechtspersoo de voornaamste zakelijk gerechtigde is, kan worden afgeleid uit de gegevens 'Teller aandeel zakelijk recht' en 'Noemer aandeel zakelijk recht'. Overigens kan het voorkomen dat de voornaamste zakelijk gerechtigde niet als zakelijk gerechtigde is geregistreerd. Bijvoorbeeld bij de van vader op zoon doorgifte van een boerenbedrijf wordt veelal geen acte bij de notaris opgemaakt. De zakelijke rechten liggen vaak nog bij de (over-overgroot)vader. Het voornaamste zakelijk recht wordt echter uitgeoefend door de zoon. Bij een kadastraal object hoort één voornaamste zakelijk gerechtigde. Een rechtspersoon kan voornaamste zakelijk gerechtigde van nul, één of meer kadastrale objecten zijn. 

De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK heeft als voornaamste zakelijk gerechtigde RECHTSPERSOON. 

**Indicatie materiële historie** 

J 

|**Indicatie formele historie**|J|
|---|---|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **2.45. Reisdocument** 

## **Attribuutsoort Reisdocumentnummer** 

> **Naam attribuutsoort** Reisdocumentnummer 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.20 

> **XML-tag attribuutsoort** nummer 

> **Definitie attribuutsoort** Het nummer van het verstrekte Nederlandse reisdocument of het nummer van het Nederlandse reisdocument waarin de ingeschrevene is bijgeschreven. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** In het GFO BG betreft dit het attribuut ‘Nummer identiteitsbewijs’ (96.38). Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum uitgifte** 

> **Naam attribuutsoort** Datum uitgifte 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.30 

> **XML-tag attribuutsoort** datumUitgifte 

> **Definitie attribuutsoort** De datum waarop het Nederlands reisdocument is uitgegeven of de datum van bijschrijving van de ingeschrevene in een Nederlands reisdocument. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

|**Aanduiding brondocument**|Ja: Documentgemeente, Documentdatum, Documentbeschrijving|
|---|---|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Autoriteit uitgifte** 

|**Naam attribuutsoort**|Autoriteit uitgifte|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|35.40|
|**XML-tag attribuutsoort**|autoriteitUitgifte|
|**Definitie attribuutsoort**|Een codering die aangeeft welke autoriteit het Nederlands reisdocument|
||heeft verstrekt of de bijschrijving heeft verricht.|
|**Datum opname attribuutsoort**|1 mei 2008|
|**Toelichting attribuutsoort**|Zie de toelichting in de GBA.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentgemeente, Documentdatum, Documentbeschrijving|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Einddatum geldigheid document** 

|**Naam attribuutsoort**|Einddatum geldigheid document|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|35.50|
|**XML-tag attribuutsoort**|einddatumGeldigheid|
|**Definitie attribuutsoort**|De datum waarop een Nederlands reisdocument, dat aan de|
||ingeschrevene is verstrekt of waarin de ingeschrevene is bijgeschreven,|
||zijn geldigheid verliest.|
|**Datum opname attribuutsoort**|1 mei 2008|



## **Toelichting attribuutsoort** 

Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum inhouding of vermissing** 

**Naam attribuutsoort** 

Datum inhouding of vermissing 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.60 

> **XML-tag attribuutsoort** datumInhoudingVermissing 

**Definitie attribuutsoort** 

De datum waarop een Nederlands reisdocument is vermist, ingehouden, dan wel ingeleverd. 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Toelichting attribuutsoort** Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aanduiding inhouding of vermissing** 

> **Naam attribuutsoort** Aanduiding inhouding of vermissing 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.70 

|**XML-tag attribuutsoort**|aanduidingInhoudingVermissing|
|---|---|
|**Definitie attribuutsoort**|Een aanduiding dat een Nederlands reisdocument is vermist,|
||ingehouden, dan wel ingeleverd.|
|**Datum opname attribuutsoort**|1 mei 2008|
|**Toelichting attribuutsoort**|Zie de toelichting in de GBA.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentgemeente, Documentdatum, Documentbeschrijving|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Lengte houder** 

|**Naam attribuutsoort**|Lengte houder|
|---|---|
|**Herkomst attribuutsoort**|GBA|
|**Code attribuutsoort**|35.80|
|**XML-tag attribuutsoort**|lengteHouder|
|**Definitie attribuutsoort**|De lengte van de ingeschrevene in hele centimeters zoals vermeld in het|
||Nederlands reisdocument.|
|**Datum opname attribuutsoort**|1 mei 2008|
|**Toelichting attribuutsoort**|Zie de toelichting in de GBA.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentgemeente, Documentdatum, Documentbeschrijving|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Relatiesoort REISDOCUMENT is van REISDOCUMENTSOORT** 

> **Naam relatiesoort** REISDOCUMENT is van REISDOCUMENTSOORT 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 12.35 

> **Definitie relatiesoort** De modelREISDOCUMENTSOORT van het REISDOCUMENT. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2008 

> **Toelichting relatiesoort** In het GFO BG betreft dit het attribuut cq. de relatie ‘Soort identiteitsbewijs’ (96.34). Zie verder de toelichting in de GBA. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort REISDOCUMENT heeft als houder INGESCHREVEN PERSOON** 

> **Naam relatiesoort** REISDOCUMENT heeft als houder INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 12.35 

> **Definitie relatiesoort** De INGESCHREVEN PERSOON waaraan het REISDOCUMENT is verstrekt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 mei 2008 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep (12.)35 (Nederlands reisdocument) in de GBA. 

De relatie is de tegenhanger van INGESCHREVEN PERSOON is houder van REISDOCUMENT. 

Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort REISDOCUMENT kent als bijgeschrevene INGESCHREVEN PERSOON** 

**Naam relatiesoort** 

REISDOCUMENT kent als bijgeschrevene INGESCHREVEN PERSOON 

**Herkomst relatiesoort Code relatiesoort** 12.35 **Definitie relatiesoort** 

KING op basis van GBA 

De INGESCHREVEN PERSOON(en) die zijn bijgeschreven in het REISDOCUMENT. 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

## KING 

## 2 februari 2008 

Het betreft het hergebruik als relatiesoort van groep (12.)35 (Nederlands reisdocument) in de GBA. 

De relatie is de tegenhanger van INGESCHREVEN PERSOON is bijgeschreven in REISDOCUMENT. Zie verder de toelichting in de GBA. 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie Aanduiding gebeurtenis** 

Ja 

## Nee 

**Aanduiding brondocument** 

**Indicatie in onderzoek** 

Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

## Ja 

**Aanduiding strijdigheid/nietigheid** 

## Nee 

**Indicatie kardinaliteit** 

**Indicatie authentiek** 

## 0-N (M-N) 

Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **2.46. Reisdocumentsoort** 

## **Attribuutsoort Reisdocumentcode** 

> **Naam attribuutsoort** Reisdocumentcode 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.11 

> **XML-tag attribuutsoort** code 

> **Definitie attribuutsoort** Een code voor het model van een Nederlands reisdocument. 

> **Herkomst definitie attribuutsoort** KING o.b.v. GBA 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Zie het LO GBA 

> **Domein attribuutsoort** Formaat: A2 Waardenverzameling: GBA-reisdocumententabek 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Reisdocumentomschrijving** 

**Naam attribuutsoort** 

Reisdocumentomschrijving 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 35.12 

> **XML-tag attribuutsoort** omschrijving 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

De omschrijving van het model van het Nederlands reisdocument. KING o.b.v. GBA 1 maart 2009 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN80|
||Waardenverzameling: GBA-reisdocumententabel||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Landelijk basisgegeven||



## **Regels attribuutsoort** 

## **Attribuutsoort Begindatum geldigheid reisdocumentsoort** 

> **Naam attribuutsoort** Begindatum geldigheid reisdocumentsoort 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 99.98 

> **XML-tag attribuutsoort** tijdvakObject.beginObject 

> **Definitie attribuutsoort** De datum waarop de reisdocumentsoort is ontstaan. 

> **Herkomst definitie attribuutsoort** KING o.b.v, GBA 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Het gaat hier om veranderingen in de lijst van codes en omschrijvingen. Niet te verwarren met de datum waarop een natuurlijke persoon zijn of haar reisdocument verkrijgt. 

|**Domein attribuutsoort**|Formaat:|onvolledige datum|
|---|---|---|
||Waardenverzameling:||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Landelijk basisgegeven||



**Regels attribuutsoort** 

## **Attribuutsoort Einddatum geldigheid reisdocumentsoort** 

**Naam attribuutsoort** 

Einddatum geldigheid reisdocumentsoort 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 99.99 

> **XML-tag attribuutsoort** tijdvakObject.eindObject 

> **Definitie attribuutsoort** De datum waarop de reisdocumentsoort is opgeheven. 

> **Herkomst definitie attribuutsoort** KING o.b.v. GBA 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Het gaat hier om veranderingen in de lijst van codes en omschrijvingen. Niet te verwarren met de datum waarop een natuurlijke persoon zijn of haar residocument verliest. 

> **Domein attribuutsoort** Formaat: onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Landelijk basisgegeven 

**Regels attribuutsoort** 

## **Relatiesoort REISDOCUMENTSOORT hoort bij REISDOCUMENT** 

> **Naam relatiesoort** REISDOCUMENTSOORT hoort bij REISDOCUMENT 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 12.35 

> **Definitie relatiesoort** De REISDOCUMENTen van de modelREISDOCUMENTSOORT 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentgemeente, Documentdatum, Documentbeschrijving 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven **Regels relatiesoort** 

## **2.47. Spoorbaandeel** 

## **Attribuutsoort Type Spoorbaan** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Type Spoorbaan 

IMGeo 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

- 

type 

Specificatie van het soort Spoorbaan 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Formaat: AN40 

Waardenverzameling: zie IMGeo, CodeList TypeSpoorbaan Ja 

Ja 

Nee 

Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Type Infrastructuur** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Type infrastructuur 

IMGeo 

- 

typeInfrastructuur 

Soort infrastructureel element 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie IMGeo, CodeList TypeInfrastructuur 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Identificatie spoorbaandeel** 

**Naam attribuutsoort** 

Identificatie spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** identificatie **Definitie attribuutsoort** 

Een unieke identificatie voor een spoorbaandeel 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

## IMGeo 

9 april 2007 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

**Domein attribuutsoort** 

Formaat: AN25 Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (02) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|



> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status spoorbaandeel** 

**Naam attribuutsoort** 

## Status spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** status **Definitie attribuutsoort** 

## IMGeo 

De status gekoppeld aan de levenscyclus van het spoorbaandeel. 

|**Herkomst definitie attribuutsoort**|IMGeo||
|---|---|---|
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|In het IMGeo betreft dit de status||
|**Domein attribuutsoort**|Formaat:|A8|
||Waardenverzameling: Plan||
|||Bestaand|
|||Historie|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijke basisgegeven||
|**Regels attribuutsoort**|-||



In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

## **Attribuutsoort Naam spoorbaandeel** 

|**Naam attribuutsoort**|Naam spoorbaandeel|
|---|---|
|**Herkomst attribuutsoort**|IMGeo|
|**Code attribuutsoort**|-|
|**XML-tag attribuutsoort**|naam|



## **Definitie attribuutsoort** 

Benaming van het spoorbaandeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: ScopedName. Waardenverzameling: - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Geometrie spoorbaandeel** 

**Naam attribuutsoort** 

Geometrie spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De minimaal tweedimensionale geometrische representatie van de omtrekken van een spoorbaandeel 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

9 april 2007 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een spoorbaandeel. 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Zie de inwinningsregels zoals beschreven in het IMGeo bij Spoorbaandeel. 

## **Attribuutsoort Relatieve hoogteligging spoorbaandeel** 

> **Naam attribuutsoort** Relatieve hoogteligging spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** relatieveHoogteligging 

> **Definitie attribuutsoort** Aanduiding voor de relatieve hoogte van het spoorbaandeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

|**Domein attribuutsoort**|Formaat:|N1|
|---|---|---|
||Waardenverzameling: gehele positieve en negatieve getallen in het||
|||bereik van -5 tot +5|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|De objecten op maaiveldniveau moeten een gebiedsdekkend geheel||
||vormen.||



## **Attribuutsoort Datum begin geldigheid spoorbaandeel** 

## **Naam attribuutsoort** 

Datum begin geldigheid spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop het spoorbaandeel is ontstaan. 

Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: Onvolledige datum 

**Domein attribuutsoort** 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid spoorbaandeel** 

> **Naam attribuutsoort** Datum einde geldigheid spoorbaandeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het spoorbaandeel ongeldig is geworden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: Onvolledige datum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid spoorbaandeel’ kan in de registratie worden opgenomen. 

## **2.48. Standplaats** 

## **Attribuutsoort Indicatie geconstateerde standplaats** 

> **Naam attribuutsoort** Indicatie geconstateerde standplaats 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 58.02 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

> **Datum opname attribuutsoort** 24-04-09 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Standplaatsstatus** 

> **Naam attribuutsoort** Standplaatsstatus 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 58.03 

> **Definitie attribuutsoort** De fase van de levenscyclus van een STANDPLAATS waarin de betreffende STANDPLAATS zich bevindt. 

> **Datum opname attribuutsoort** 24-04-09 

**Toelichting attribuutsoort** 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort STANDPLAATS heeft als hoofdadres NUMMERAANDUIDING** 

**Naam relatiesoort** 

STANDPLAATS heeft als hoofdadres NUMMERAANDUIDING 

**Herkomst relatiesoort Code relatiesoort** 58.10 **Definitie relatiesoort** 

KING op basis van BAG 

De identificatiecode nummeraanduiding waaronder het hoofdadres van een STANDPLAATS, dat in het kader van de basisregistratie gebouwen als zodanig is aangemerkt, is opgenomen in de basisregistratie adressen. KING op basis van BAG 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 24-04-09 **Toelichting relatiesoort** 

In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding hoofdadres standplaats’ bij het objecttype STANDPLAATS. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is hoofdadres van STANDPLAATS. 

De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort STANDPLAATS heeft als nevenadressen NUMMERAANDUIDING** 

> **Naam relatiesoort** STANDPLAATS heeft als nevenadressen NUMMERAANDUIDING 

> **Herkomst relatiesoort** KING op basis van BAG 

> **Code relatiesoort** 58.11 

> **Definitie relatiesoort** De identificatiecodes nummeraanduiding waaronder nevenadressen van een STANDPLAATS, die in het kader van de basisregistratie gebouwen als zodanig zijn aangemerkt, zijn opgenomen in de basisregistratie adressen. 

> **Herkomst definitie relatiesoort** KING op basis van BAG 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** In de BAG is dit gemodelleerd als het attribuutsoort ‘Aanduiding nevenadressen standplaats’ bij het objecttype STANDPLAATS. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is nevenadres van STANDPLAATS. De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. Zie verder de toelichtingen in de BAG bij beide attribuutsoorten. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort STANDPLAATS heeft daarop INGESCHREVEN PERSOONen** 

> **Naam relatiesoort** STANDPLAATS heeft daarop INGESCHREVEN PERSOONen 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11 

> **Definitie relatiesoort** De personen die ingeschreven zijn in de gemeente op het adres dat hoort bij de STANDPLAATS 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 24-04-09 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats) in de GBA in de gevallen dat de personen verblijven op de standplaats. 

De relatie is de tegenhanger van INGESCHREVEN PERSOON verblijft op STANDPLAATS. 

||Zie verder de toelichting in de GBA bij genoemd attribuutsoort.|
|---|---|
|**Indicatie materiële historie**|J|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Authentiek gegeven|



## **Regels relatiesoort** 

## **Relatiesoort STANDPLAATS is huisvesting van HUISHOUDEN** 

|**Naam relatiesoort**|STANDPLAATS is huisvesting van HUISHOUDEN|
|---|---|
|**Herkomst relatiesoort**|KING op basis van GFO BG|
|**Code relatiesoort**|96.01|
|**Definitie relatiesoort**|De STANDPLAATS waarop één of meer HUISHOUDENs wonen.|
|**Herkomst definitie relatiesoort**|KING op basis van GFO BG|
|**Datum opname relatiesoort**|24-04-09|
|**Toelichting relatiesoort**|Een huishouden is ‘woonachtig’ in één verblijfs-object, standplaats of|
||standplaats. In één dergelijk object kunnen nul, één of meer huishoudens|
||‘wonen’.|
||De relatie is de tegenhanger van het relatiesoort HUISHOUDEN is|
||gehuisvest op STANDPLAATS.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



## **Regels relatiesoort** 

## **2.49. Subject** 

## **Groepattribuutsoort Postadres** 

> **Naam attribuutsoort** Postadres 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

> **Definitie attribuutsoort** De gegevens die tezamen een postbusadres of antwoordnummeradres vormen 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

De gegevens die tezamen een postbusadres of antwoordnummeradres vormen 

Postadrestype Postbus- of antwoordnummer Postadres postcode en het volgende relatiesoort: SUBJECT heeft postadres dat zich bevindt in WOONPLAATS. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Postadrestype** 

> **Naam attribuutsoort** Postadrestype 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** correspondentieAdres.postadresType 

> **Definitie attribuutsoort** Aanduiding van het soort postadres 

> **Herkomst definitie attribuutsoort** KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## 9 april 2007 

Door middel van de aanduiding wordt duidelijk of de waarde van het gegeven ‘Postbus- of antwoordnummer’ een postbus- of een antwoordnummer betreft. Het attribuutsoort maakt deel uit van het groepattribuutsoort Postadres. Formaat: A1 Waardenverzameling: A: Antwoordnummer P: Postbusnummer 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Postbus- of antwoordnummer** 

**Naam attribuutsoort** 

Postbus- of antwoordnummer 

**Herkomst attribuutsoort Code attribuutsoort** 11.80 / 94.86 **XML-tag attribuutsoort Definitie attribuutsoort** 

KING op basis van GFO BG 

correspondentieAdres.postadresNummer 

De numerieke aanduiding zoals deze door de Nederlandse PTT is vastgesteld voor postbusadressen en antwoordnummeradressen. KING op basis van GFO 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

9 april 2007 

In combinatie met postadrestype wordt duidelijk of de waarde van het gegeven een postbus- of een antwoordnummer betreft. Het attribuutsoort maakt deel uit van het groepattribuutsoort Postadres. Formaat: N5 Waardenverzameling: 1 - 99999 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Postadres postcode** 

**Naam attribuutsoort** 

Postadres postcode 

**Herkomst attribuutsoort Code attribuutsoort** 11.60 **XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

KING op basis van GFO 

correspondentieAdres.postcode 

De officiële Nederlandse PTT codering, bestaande uit een numerieke woonplaatscode en een alfabetische lettercode ( 

NEN 5825 

9 april 2007 

De postcode is opgebouwd uit een woonplaatscode en een lettercode. Het Besluit Standaardadressering zegt hierover: 

Woonplaatscode: een door de PTT ontworpen 4-cijferige code die een unieke aanduiding vormt voor alle woonplaatsen in Nederland. Lettercode: twee alfabetische tekens in hoofdletters. 

De combinatie woonplaatscode/lettercode vormt de cijfer/lettercombinatie van een aantal besteladressen die algemeen bekend staan als postcode. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Postadres. 

> **Domein attribuutsoort** Formaat: AN6 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Formaat: AN6 Waardenverzameling: 1000AA – 9999ZZ 

## **Groepattribuutsoort Verblijf buitenland** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

**Code attribuutsoort** 

Verblijf buitenland 

KING op basis van GBA 

## 08.13 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De gegevens over het verblijf in het buitenland 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

08.13.30  Adres buitenland 1 08.13.40  Adres buitenland 2 08.13.50  Adres buitenland 3 en de volgende relatiesoort: 

SUBJECT heeft verblijfsadres in LAND. 

Het groepattribuutsoort is ontleend aan groep 13: Emigratie in de GBA (LO 3.6) maar betreft in tegenstelling tot de GBA het actuele buitenlandse verblijfs/ of bezoekadres en geldt hier ook voor niet-natuurlijke personen en vestigingen. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Adres buitenland 1** 

**Naam attribuutsoort** 

Adres buitenland 1 

> **Herkomst attribuutsoort** KING op basis van GBA 

> **Code attribuutsoort** 08.13.30 **XML-tag attribuutsoort Definitie attribuutsoort** 

verblijfBuitenland.adresBuitenland1 

Het eerste deel van het adres in het buitenland dat het SUBJECT opgeeft bij vertrek naar het buitenland dan wel waar het SUBJECT in het buitenland verblijft. 

**Herkomst definitie attribuutsoort** 

KING op basis van GBA 

> **Datum opname attribuutsoort** 9 april 2007 

## **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het attribuutsoort is ontleend aan de GBA, betreft het eerste deel van het actuele verblijfs- of bezoekadres in het buitenland en geldt hier ook voor niet-natuurlijke personen en vestigingen. Het attribuutsoort maakt deel uit van het groepattribuutsoort Verblijf buitenland. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Adres buitenland 2** 

> **Naam attribuutsoort** Adres buitenland 2 

> **Herkomst attribuutsoort** KING op basis van GBA 

> **Code attribuutsoort** 08.13.30 

> **XML-tag attribuutsoort** verblijfBuitenland.adresBuitenland2 **Definitie attribuutsoort** 

Het tweede deel van het adres in het buitenland dat het SUBJECT opgeeft bij vertrek naar het buitenland dan wel waar het SUBJECT in het buitenland verblijft. 

**Herkomst definitie attribuutsoort** 

KING op basis van GBA 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

Het attribuutsoort is ontleend aan de GBA, betreft het tweede deel van het actuele verblijfs- of bezoekadres in het buitenland en geldt hier ook voor niet-natuurlijke personen en vestigingen. Dit tweede adresdeel bevat de buitenlandse woonplaats. Het attribuutsoort maakt deel uit van het groepattribuutsoort Verblijf buitenland. 

||het<br>voor<br>Dit t<br>Het<br>buite|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|



> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven indien het een ingeschreven natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Adres buitenland 3** 

**Naam attribuutsoort** 

Adres buitenland 3 

> **Herkomst attribuutsoort** KING op basis van GBA 

> **Code attribuutsoort** 08.13.50 

> **XML-tag attribuutsoort** verblijfBuitenland.adresBuitenland3 

**Definitie attribuutsoort** 

Het derde deel van het adres in het buitenland dat het SUBJECT opgeeft bij vertrek naar het buitenland dan wel waar het SUBJECT in het buitenland verblijft. 

> **Herkomst definitie attribuutsoort** KING op basis van GBA 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het attribuutsoort is ontleend aan de GBA, betreft het derde deel van het actuele verblijfs- of bezoekadres in het buitenland en geldt hier ook voor niet-natuurlijke personen en vestigingen. Het attribuutsoort maakt deel uit van het groepattribuutsoort Verblijf buitenland. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven. 

## **Attribuutsoort Telefoonnummer** 

> **Naam attribuutsoort** Telefoonnummer 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.80 

> **XML-tag attribuutsoort** telefoonnummer 

## **Definitie attribuutsoort** 

Telefoonnummer waaronder het subject in de regel bereikbaar is. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

GFO BG 

9 april 2007 

In tegenstelling tot het GFO BG is hier alleen sprake van één telefoonnummer dat het subject beschouwd als zijn ‘primaire’ telefoonnummer. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle bestaande alfanumerieke tekens. 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Fax-nummer** 

> **Naam attribuutsoort** Fax-nummer 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.27 

> **XML-tag attribuutsoort** faxnummer 

> **Definitie attribuutsoort** Faxnummer waaronder het subject in de regel bereikbaar is. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** In tegenstelling tot het GFO BG is hier alleen sprake van één faxnummer dat het subject beschouwd als zijn ‘primaire’ faxnummer. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle bestaande alfanumerieke tekens. 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Emailadres** 

> **Naam attribuutsoort** Emailadres 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.16 

> **XML-tag attribuutsoort** emailadres 

> **Definitie attribuutsoort** Elektronisch postadres waaronder het subject in de regel bereikbaar is. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** In tegenstelling tot het GFO BG is hier alleen sprake van één emailadres dat het subject beschouwd als zijn ‘primaire’ emailadres. 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle bestaande alfanumerieke tekens waarin zich, aan het begin noch aan het eind, een ‘@’ moet bevinden. 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Website-URL** 

|**Naam attribuutsoort**|Website-URL|
|---|---|
|**Herkomst attribuutsoort**|KING|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|url|



## **Definitie attribuutsoort** 

Het label of etiket dat aan de specifieke informatiebron, zoals een webpagina, een bestand of een plaatje op internet is toegewezen waar het SUBJECT in de regel op het internet vindbaar is. 

**Herkomst definitie attribuutsoort** 

KING op basis van WikipediA 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

9 april 2007 

In de gegevenscatalogus van het NHR wordt dit attrbuutsoort Domeinnaam genoemd. 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Formaat: AN200 Waardenverzameling: alle bestaande alfanumerieke tekens N 

## **Attribuutsoort Bank/girorekeningnummer** 

**Naam attribuutsoort** 

Bank/girorekeningnummer 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 94.87 

> **XML-tag attribuutsoort** rekeningnummerBankGiro **Definitie attribuutsoort** 

Het nummer van een Nederlandse bank/girorekening, zoals dat door een bankinstelling als identificator aan een overeenkomst tussen de bank en een of meer subjecten wordt toegekend, op basis waarvan het SUBJECT in de regel financieel communiceert. 

**Herkomst definitie attribuutsoort** 

KING op basis van GFO BG 

**Datum opname attribuutsoort** 

9 april 2007 

**Toelichting attribuutsoort** 

In tegenstelling tot het GFO BG is hier alleen sprake van één rekeningnummer dat het subject beschouwd als zijn ‘primaire’ rekeningnummer. 

**Domein attribuutsoort** 

N10 

Formaat: 

Waardenverzameling: alle gehele natuurlijke getallen, m.u.v. nul 

**Indicatie materiële historie** 

N 

**Indicatie formele historie** 

N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Subjecttypering** 

> **Naam attribuutsoort** Subjecttypering 

> **Herkomst attribuutsoort** KING 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** typering **Definitie attribuutsoort** 

Het onderscheid van een SUBJECT in een INGEZETENE, een NIETINGEZETENE, een ANDER NATUURLIJK PERSOON, een INGESCHREVEN NIET-NATUURLIJK PERSOON, een ANDER NIETNATUURLIJK PERSOON dan wel een VESTIGING. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het attribuutsoort is benodigd om bij uitwisseling van gegevens van het objecttype SUBJECT aan te kunnen geven welk van de genoemde specialisaties het betreft. 

Een code voor elke domeinwaarde wordt gebruikt in de subjectsleutel om te bereiken dat deze sleutel uniek is over alle subjecten heen: 11: Ingezetene 

12: Niet-ingezetene 13: Ander natuurlijk persoon 21: Ingeschreven niet-natuurlijk persoon 23: Ander niet-natuurlijk persoon 31: Vestiging 

**Domein attribuutsoort** 

Formaat: AN50 Waardenverzameling: Ingezetene Niet-ingezetene Ander natuurlijk persoon Ingeschreven niet-natuurlijk persoon Ander buitenlands niet-natuurlijk persoon Vestiging 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Naam** 

> **Naam attribuutsoort** Naam 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** naam 

> **Definitie attribuutsoort** De benaming van het SUBJECT 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 27-04-09 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om subjecten te kunnen zoeken op naam. Deze is immers voor de verschillende specificaties (Natuurlijk persoon, Niet-natuurlijk persoon en Vestiging) anders samengesteld dan wel benoemd. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Voor een Natuurlijk persoon samengesteld uit de Geslachtsnaam, de eerste voorletter uit Voorletters aanschrijving en de Voorvoegsels geslachtsnaam. Voor een Niet-natuurlijk persoon is dit de Statutaire naam. Voor een Vestiging is dit de eerste Handelsnaam. 

## **Attribuutsoort Identificatie** 

**Definitie attribuutsoort Herkomst attribuutsoort** KING 

## Identificatie 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** bsFiVesNummerOfId **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 27-04-09 **Toelichting attribuutsoort** 

De unieke identificatie van het SUBJECT 

Het betreft een afleidbaar gegeven dat is opgenomen om subjecten te kunnen zoeken op hun identificatie. Deze is immers voor de verschillende specificaties (Natuurlijk persoon, Niet-natuurlijk persoon en Vestiging) anders gespecificeerd. 

**Domein attribuutsoort** 

Formaat: AN17 Waardenverzameling: alle cijfers en letters 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Voor een Ingeschreven persoon: de Subjecttypering gevolgd door het Burgerservicenummer. 

Voor een Ander natuurlijk persoon: de Subjecttypering gevolgd door het Nummer ander natuurlijk persoon. 

Voor een Ingeschreven niet-natuurlijk persoon: de Subjecttypering gevolgd door de NNP-ID . 

Voor een Ander niet-natuurlijk persoon: de Subjecttypering gevolgd door het Nummer ander niet-natuurlijk persoon. Voor een Vestiging: de Subjecttypering gevolgd door het Vestigingsnummer. 

## **Attribuutsoort Adres binnenland** 

> **Naam attribuutsoort** Adres binnenland 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** adresNederland 

> **Definitie attribuutsoort** De aanduiding van het adres waar het SUBJECT verblijft dan wel bereikbaar is. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 27-04-09 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om subjecten te kunnen zoeken op hun binnenlandse adres. Per subject kan dit immers verschillen (verblijfsadres, vestigingslocatie, bezoekadres, correspondentieadres, etcetera). Het kan zowel om een locatie-adres als een postbus-adres gaan. 

> **Domein attribuutsoort** Formaat: AN257 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het betreft een afleidbaar groepattribuutsoort met de volgende afleidbare gegevens van of bij een ADRESSEERBAAR OBJECT AANDUIDING: 

- Adresseerbaar object aanduiding typering; 

- WOONPLAATS.Woonplaatsnaam  (van de WOONPLAATS behorende bij de OPENBARE RUIMTE bij de ADRESSEERBAAR OBJECT AANDUIDING); 

- WOONPLAATS.Woonplaatsidentificatie  (van de WOONPLAATS behorende bij de ADRESSEERBAAR OBJECT AANDUIDING); 

- WOONPLAATS.Woonplaatsnaam  (van de WOONPLAATS behorende bij de ADRESSEERBAAR OBJECT AANDUIDING); 

- • ADRESSEERBAAR OBJECT AANDUIDING.Postcode dan wel SUBJECT.Postadres postcode; 

- Identificatiecode adresseerbaar object aanduiding; 

- WOONPLAATS.Woonplaatsidentificatie  (van de WOONPLAATS behorende bij de OPENBARE RUIMTE bij de ADRESSEERBAAR OBJECT AANDUIDING); 

- OPENBARE RUIMTE.Identificatiecode openbare ruimte (van de OPENBARE RUIMTE bij de  ADRESSEERBAAR OBJECT AANDUIDING); 

- GEMEENTELIJKE OPENBARE RUIMTE.Naam openbare ruimte (van de GEMEENTELIJKE OPENBARE RUIMTE bij de OPENBARE RUIMTE bij de  ADRESSEERBAAR OBJECT AANDUIDING); 

- GEMEENTELIJKE OPENBARE RUIMTE.Straatnaam (van de GEMEENTELIJKE OPENBARE RUIMTE bij de OPENBARE RUIMTE bij de  ADRESSEERBAAR OBJECT AANDUIDING); 

- • Huisnummer; 

- Huisletter; 

- Huisnummertoevoeging, 

gevolgd door de volgende afleidbare gegevens van SUBJECT: 

- Postadrestype; 

- Postbus- of antwoordnummer . 

## **Attribuutsoort Adres buitenland** 

|**Naam attribuutsoort**|Adres buitenland|
|---|---|
|**Herkomst attribuutsoort**|KING|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|adresBuitenland|
|**Definitie attribuutsoort**|De aanduiding van het adres waar het SUBJECT verblijft dan wel|
||bereikbaar is in het buitenland.|
|**Herkomst definitie attribuutsoort**|KING|
|**Datum opname attribuutsoort**|27-04-09|
|**Toelichting attribuutsoort**|Het betreft een afleidbaar gegeven dat is opgenomen om subjecten te|
||kunnen zoeken op hun eventuele buitenlandse adres.|
|**Domein attribuutsoort**|Formaat:<br>AN149|
||Waardenverzameling: alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Afleidbaar gegeven|
|**Regels attribuutsoort**|Het betreft een afleidbaar groepattribuutsoort met de volgende afleidbare|
||gegevens van het SUBJECT:|
||•<br>LAND.Landcode (van het LAND bij het SUBJECT)|
||•<br>LAND.Landnaam (van het LAND bij het SUBJECT)|
||•<br>Adres buitenland 1|
||•<br>Adres buitenland 2|
||•<br>Adres buitenland 3.|



## **Attribuutsoort KvK-nummer** 

## **Naam attribuutsoort** 

## KvK-nummer 

> **Herkomst attribuutsoort** NHR 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** kvkNummer **Definitie attribuutsoort** 

> **Definitie attribuutsoort** Landelijk uniek identificerend administratienummer van een MAATSCHAPPELIJKE ACTIVITEIT behorend bij een SUBJECT zoals toegewezen door de Kamer van Koophandel (KvK). 

> **Herkomst definitie attribuutsoort** KING op basis van GFO BG 

> **Datum opname attribuutsoort** 19 mei 2009 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om subjecten te kunnen zoeken op het KvK-nummer van hun eventuele maatschappelijke activiteit. 

> **Domein attribuutsoort** Formaat: AN8 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Voor een RECHTSPERSOON cq. haar specialisaties: het KvK-nummer van de MAATSCHAPPELIJKE ACTIVITEIT waarvan de RECHTSPERSOON eigenaar is (indien van toepassing). Voor een VESTIGING: het KvK-nummer van de MAATSCHAPPELIJKE ACTIVITEIT waarvoor de VESTIGING activiteiten uitoefent. 

## **Relatiesoort SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING op basis van GFO BG 

**Code relatiesoort** 

> **Definitie relatiesoort** Het adres waarop het SUBJECT in de regel schriftelijk bereikbaar is en dat gevormd wordt door de combinatie van de ADRESSEERBAAR OBJECT AANDUIDING met  de bijbehorende (GEMEENTELIJKE) OPENBARE RUIMTE en WOONPLAATS. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatie is de tegenhanger van ADRESSEERBAAR OBJECT AANDUIDING Is correspondentieadres van SUBJECT. Een correspondentieadres betreft het in de GBA opgenomen briefadres indien het SUBJECT een INGESCHREVEN PERSOON betreft en dit met de attribuutsoort INGESCHREVEN PERSOON .  Adresherkomst is aangegeven. Zie verder de toelichting bij laatstgenoemde attribuutsoort. 

> **Indicatie materiële historie** J indien het een GBA-briefadres betreft, anders N 

> **Indicatie formele historie** J indien het een GBA-briefadres betreft, anders N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een GBA-briefadres betreft, anders Gemeentelijk basisgegeven 

> **Regels relatiesoort** Zie de GBA indien het een ingeschreven natuurlijk persoon betreft, anders niet verplicht te registreren 

## **Relatiesoort SUBJECT heeft als correspondentieadres postadres in WOONPLAATS** 

|**Naam relatiesoort**|SUBJECT heeft als correspondentieadres postadres in WOONPLAATS|
|---|---|
|**Herkomst relatiesoort**|KING|
|**Code relatiesoort**||
|**Definitie relatiesoort**|De woonplaats die behoort bij het postadres van het SUBJECT|
|**Herkomst definitie relatiesoort**|KING|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|De relatie is de tegenhanger van WOONPLAATS is deel van|
||correspondentieadres zijnde postadres van SUBJECT.|
||Het relatiesoort maakt deel uit van het groepattribuutsoort Postadres.|
|**Indicatie materiële historie**|N|
|**Indicatie formele historie**|N|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|



**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** De relatie komt alleen voor in combinatie met een gevuld postbus- of antwoordnummer. 

## **Relatiesoort SUBJECT Is aangewezen belanghebbende bij WOZ-BELANG** 

> **Naam relatiesoort** SUBJECT Is aangewezen belanghebbende bij WOZ-BELANG 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.20b/01.30b 

**Definitie relatiesoort** 

De unieke aanduidingen van de WOZ-BELANGen waarbij de natuurlijk of niet-natuurlijk persoon als belanghebbende is aangewezen. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

KING op basis van de catalogus BRWOZ 

In de BRWOZ is dit gemodelleerd als de attribuutsoorten ‘Aangewezen belanghebbende (Burgerservicenummer)’ en ‘Aangewezen belanghebbende (FI-nummer)’ bij het objecttype WOZ-BELANG. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZ-BELANG heeft als aangewezen belanghebbende SUBJECT. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort SUBJECT heeft verblijfsadres in LAND** 

> **Naam relatiesoort** SUBJECT heeft verblijfsadres in LAND 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

## **Definitie relatiesoort** 

> **Definitie relatiesoort** Het LAND waarin het SUBJECT heeft aangegeven te (gaan) verblijven dan wel verblijft. 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 1 november 2008 

> **Toelichting relatiesoort** De relatiesoort maakt deel uit van de groepattribuutsoort Verblijf buitenland. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven indien het een ingeschreven natuurlijk of niet-natuurlijk persoon betreft, anders een gemeentelijk basisgegeven. 

> **Regels relatiesoort** - 

## **2.50. Terreindeel** 

## **Attribuutsoort Type terrein** 

**Naam attribuutsoort** 

Type terrein 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** type **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** IMGeo **Datum opname attribuutsoort** 

Specificatie van het soort terrein 

9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie IMGeo, CodeList TypeTerrein 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** 

Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Verharding** 

**Naam attribuutsoort** 

Verharding 

**Herkomst attribuutsoort Code attribuutsoort** - **XML-tag attribuutsoort** 

IMGeo 

verharding 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Mate waarin het terreindeel al of niet verhard is 

## IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie IMGeo, CodeList Verharding 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Identificatie terreindeel** 

> **Naam attribuutsoort** Identificatie terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** identificatie **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** object. 

> **Domein attribuutsoort** Formaat: 

Een unieke identificatie voor een terreindeel 

9 april 2007 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

> **Domein attribuutsoort** Formaat: AN25 Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (04) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status terreindeel** 

**Naam attribuutsoort** 

## Status terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** status **Definitie attribuutsoort** 

De status gekoppeld aan de levenscyclus van het terreindeel. 

|**Herkomst definitie attribuutsoort**|IMGeo||
|---|---|---|
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|In het IMGeo betreft dit de status||
|**Domein attribuutsoort**|Formaat:|A8|
||Waardenverzameling: Plan||
|||Bestaand|
|||Historie|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijke basisgegeven||
|**Regels attribuutsoort**|-||



In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

## **Attribuutsoort Naam terreindeel** 

> **Naam attribuutsoort** Naam terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** naam 

## **Definitie attribuutsoort** 

Benaming van het terreindeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: ScopedName. Waardenverzameling: - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Geometrie terreindeel** 

**Naam attribuutsoort** 

Geometrie terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

De minimaal tweedimensionale geometrische representatie van de omtrekken van een terreindeel 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een terreindeel. 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Zie de inwinningsregels zoals beschreven in het IMGeo bij Terreindeel. 

## **Attribuutsoort Relatieve hoogteligging terreindeel** 

> **Naam attribuutsoort** Relatieve hoogteligging terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** relatieveHoogteligging 

> **Definitie attribuutsoort** Aanduiding voor de relatieve hoogte van het terreindeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

> **Domein attribuutsoort** Formaat: N1 Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De objecten op maaiveldniveau moeten een gebiedsdekkend geheel vormen. 

## **Attribuutsoort Datum begin geldigheid terreindeel** 

## **Naam attribuutsoort** 

Datum begin geldigheid terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop het terreindeel is ontstaan. 

Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: Onvolledigedatum 

**Domein attribuutsoort** 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid terreindeel** 

> **Naam attribuutsoort** Datum einde geldigheid terreindeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het terreindeel ongeldig is geworden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid terreindeel’ kan in de registratie worden opgenomen. 

## **2.51. Verblijfsobject** 

## **Attribuutsoort Indicatie geconstateerd verblijfsobject** 

**Naam attribuutsoort** 

Indicatie geconstateerd verblijfsobject 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 56.02 

> **XML-tag attribuutsoort** geconstateerd 

**Definitie attribuutsoort** 

> **Definitie attribuutsoort** Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Verblijfsobjectstatus** 

> **Naam attribuutsoort** Verblijfsobjectstatus 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 56.32 

> **XML-tag attribuutsoort** status 

> **Definitie attribuutsoort** De fase van de levenscyclus van een VERBLIJFSOBJECT, waarin het betreffende VERBLIJFSOBJECT zich bevindt. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Hoogste bouwlaag verblijfsobject** 

**Naam attribuutsoort** 

Hoogste bouwlaag verblijfsobject 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.32 

> **XML-tag attribuutsoort** hoogsteBouwlaag **Definitie attribuutsoort** 

De ligging van de hoogste bouwlaag van het verblijfsobject gerekend ten opzichte van het straatpeil. 

> **Herkomst definitie attribuutsoort** GFO BG **Datum opname attribuutsoort Toelichting attribuutsoort** 

## 9 april 2007 

Voor de definitie van bouwlaag wordt verwezen naar NEN 2580 (2e druk, 1997): 'Een deel van een gebouw, dat bestaat uit een of meer ruimten, waarbij de bovenkanten van de afgewerkte vloeren van twee aan elkaar grenzende ruimten niet meer dan 1,5 meter in hoogte verschillen'. Onder straatpeil wordt verstaan: 

a. Voor een bouwwerk, waarvan de hoofdtoegang direct aan de weg grenst, de krachtens besluit van burgemeester en wethouders vastgestelde hoogte van de weg ter plaatse van de hoofdtoegang; b. Voor een bouwwerk, waarvan de hoofdtoegang niet direct aan de weg grenst: de hoogte van het terrein ter plaatse van de hoofdtoegang bij voltooiing van de bouw (Model-bouwverordening). 

De hoogste bouwlaag geeft van een verblijfsobject aan op welke bouwlaag van een pand zich de bovenste bouwlaag van het daarin aanwezige verblijfsobject bevindt. Het geeft dus niet aan uit hoeveel bouwlagen het verblijfsobject bestaat. Dit laatste kan berekend worden uit 'hoogste bouwlaag' en 'laagste bouwlaag' van het verblijfsobject. De bouwlaag op straatpeil heeft de waarde 0. 

Indien de hoogste bouwlaag onbekend is, wordt geen waarde ingevuld. Voorbeeld: een appartement op de zesde verdieping van een flatgebouw van tien verdiepingen (elf bouwlagen) heeft als hoogste bouwlaag 7. Daar het appartement zich uitstrekt over een verdieping, is ook de laagste bouwlaag gelijk aan 7. Indien het verblijfsobject (bijvoorbeeld een parkeergarage) ondergronds ligt, is de laagste bouwlaag bijvoorbeeld op bouwlaag -7 en de hoogste bouwlaag op bouwlaag - 1 (zes verdiepingen). 

**Domein attribuutsoort** 

Formaat: N3 Waardenverzameling: -99 tot +999 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Laagste bouwlaag verblijfsobject** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Laagste bouwlaag verblijfsobject 

GFO BG 

95.53 

laagsteBouwlaag 

De ligging van de laagste bouwlaag van het verblijfsobject gerekend ten opzichte van het straatpeil. 

GFO BG 

9 april 2007 

|**Toelichting attribuutsoort**|Voor de definitie van bouwlaag wordt verwezen naar NEN 2580 (2e druk,|
|---|---|
||1997): 'Een deel van een gebouw, dat bestaat uit een of meer ruimten,|
||waarbij de bovenkanten van de afgewerkte vloeren van twee aan elkaar|
||grenzende ruimten niet meer dan 1,5 meter in hoogte verschillen'.|
||Onder straatpeil wordt verstaan:|
||a. Voor een bouwwerk, waarvan de hoofdtoegang direct aan de weg|
||grenst, de krachtens besluit van burgemeester en wethouders|
||vastgestelde hoogte van de weg ter plaatse van de hoofdtoegang;|
||b. Voor een bouwwerk, waarvan de hoofdtoegang niet direct aan de weg|
||grenst: de hoogte van het terrein ter plaatse van de hoofdtoegang bij|
||voltooiing van de bouw (Model-bouwverordening).|
||De laagste bouwlaag geeft van een verblijfsobject aan op welke bouwlaag|
||van een pand zich de onderste bouwlaag van het daarin aanwezige|
||verblijfsobject bevindt. Het geeft dus niet aan uit hoeveel bouwlagen het|
||verblijfsobject bestaat. Dit laatste kan berekend worden uit 'hoogste|
||bouwlaag' en 'laagste bouwlaag' van het verblijfsobject.|
||De bouwlaag op straatpeil heeft de waarde 0.|
||Indien de laagste bouwlaag onbekend is, wordt geen waarde ingevuld.|
||Voorbeeld: een appartement op de zesde verdieping van een flatgebouw|
||van tien verdiepingen (elf bouwlagen) heeft als hoogste bouwlaag 7. Daar|
||het appartement zich uitstrekt over een verdieping, is ook de laagste|
||bouwlaag gelijk aan 7. Indien het verblijfsobject (bijvoorbeeld een|
||parkeergarage) ondergronds ligt, is de laagste bouwlaag bijvoorbeeld op|
||bouwlaag -7 en de hoogste bouwlaag op bouwlaag - 1 (zes|
||verdiepingen).|
|**Domein attribuutsoort**|Formaat:<br>N3|
||Waardenverzameling: -99 tot +999|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels attribuutsoort**|-|



## **Attribuutsoort Toegang bouwlaag verblijfsobject** 

|**Naam attribuutsoort**|Toegang bouwlaag verblijfsobject|
|---|---|
|**Herkomst attribuutsoort**|KING|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|toegangBouwlaag|



## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De ligging van de bouwlaag van het verblijfsobject, gerekend ten opzichte van het straatpeil, waarop zich de hoofdtoegang tot het verblijfsobject bevindt. 

KING 

> **Datum opname attribuutsoort** 9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: N3 Waardenverzameling: -99 tot +999 

> **Indicatie materiële historie** NeeJa 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Soort woonobject** 

**Naam attribuutsoort** 

Soort woonobject 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.78 

> **XML-tag attribuutsoort** soortWoonobject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Indeling van woonverblijven volgens het CBS. 

De definities van de verschillende soorten woonverblijven volgens het CBS zijn te vinden in de Handleiding voor de administratieve woningtelling, CBS, 1992. 

## _Woning_ 

Een woning is een tot bewoning bestemd gebouw dat, vanuit bouwtechnisch oogpunt gezien, blijvend is bestemd voor permanente bewoning door een particulier huishouden. 

- het tot bewoning bestemd gebouw dient zodanig te zijn gebouwd of verbouwd dat het voor particuliere bewoning geschikt is. 

- het tot bewoning bestemde gebouw dient te zijn voorzien van een eigen toegangsdeur die hetzij direct vanaf de openbare weg, hetzij via een gemeenschappelijke ruimte (zoals portiek, galerij, trappenhuis, corridor) 

toegang biedt tot de woonruimte. 

- het tot bewoning bestemde gebouw dient tenminste 14m2 aan verblijfsruimte te bevatten. 

- het tot bewoning bestemde gebouw dient te beschikken over een toilet en over een keukeninrichting die is bestemd voor de bereiding van complete maaltijden. 

## _Recreatiewoning_ 

Een recreatiewoning is een tot bewoning bestemd gebouw dat voldoet aan alle criteria die gelden voor woningen, maar waarvoor daarnaast tenminste een van de volgende criteria van toepassing is: 

- het tot bewoning bestemde gebouw is voor vakantiedoeleinden bestemd - het tot bewoning bestemde gebouw is gelegen op officieel voor recreatie aangewezen terrein. 

## _Wooneenheid_ 

Een wooneenheid is een deel van een tot bewoning bestemd gebouw dat, vanuit bouwtechnisch oogpunt, blijvend is bestemd voor permanente bewoning door een particulier huishouden en dat voldoet aan alle criteria die van toepassing zijn op woningen, behalve aan het vierde criterium vanwege het ontbreken van een keukeninrichting die bestemd is voor het bereiden van complete maaltijden en/of het ontbreken van een toilet, terwijl die ruimte bovendien gelegen is in een gebouw dat ter compensatie van deze aan de wooneenheid ontbrekende elementen gemeenschappelijke voorzieningen bevat. De operationele criteria voor wooneenheden zijn: 

- het deel van een tot bewoning bestemd gebouw dient zodanig te zijn gebouwd of verbouwd dat het voor particuliere bewoning geschikt is; - het deel van een tot bewoning bestemd gebouw dient te zijn voorzien van een eigen toegangsdeur die hetzij direct vanaf de openbare weg, hetzij via een gemeenschappelijke ruimte (zoals portiek, galerij, trappenhuis, corridor) toegang biedt tot de woonruimte; 

- het deel van een tot bewoning bestemd gebouw dient tenminste 14m2 aan verblijfsruimte te bevatten; 

- het gebouw waarin de wooneenheid gelegen is, dient te beschikken over een (gemeenschappelijke) toilet en over een (gemeenschappelijk) keukeninrichting die is bestemd voor de bereiding van complete maaltijden; 

- het gebouw waarin de wooneenheid gelegen is, is gebouwd of verbouwd met bestemming ‘bewoning door meerdere particuliere huishoudens’; 

- het deel van een tot bewoning bestemd gebouw bevindt zich niet in een bedrijfsgebouw voor de horeca of in een bijzonder woongebouw. 

## _Bijzonder woongebouw_ 

Een bijzonder woongebouw is een gebouwencomplex, gebouw of deel van een gebouw, dat volgens de bouw of verbouw blijvend bestemd is voor permanente bewoning door een institutioneel huishouden. 

## _De operationele criteria voor bijzondere woongebouwen zijn:_ 

- het gebouw of gebouwencomplex heeft een adres; 

- het gebouw of gebouwencomplex is bestemd voor permanente bewoning; 

- het gebouw of gebouwencomplex is in gebruik door een rechtspersoon; - deze rechtspersoon valt binnen een van de bedrijfsgroepen zoals vermeld in de ‘Handleiding voor de administratieve woningtelling’, 1992; - De rechtspersoon gebruikt het gebouw(encomplex) voor permanente huisvesting en bedrijfsmatige huishoudelijke verzorging van een verzameling personen. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: N1 Waardenverzameling: 1 = woning 2 = recreatiewoning 3 = wooneenheid 4 = bijzonder woongebouw 7 = overig woonverblijf 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Aantal kamers** 

## **Naam attribuutsoort** Aantal kamers 

> **Herkomst attribuutsoort** Gegevenswoordenboek WOZ (2002), overgenomen door KING 

> **Code attribuutsoort** 61.25 

> **XML-tag attribuutsoort** aantalKamers 

> **Definitie attribuutsoort** Het aantal kamers van het Verblijfsobject in de situatie tijdens de bouw. 

> **Herkomst definitie attribuutsoort** KING op basis van Gegevenswoordenboek WOZ (2002) 

> **Datum opname attribuutsoort** 1 november 2008 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie** 

Het attribuut maakt deel uit van het StUF-sectormodel en kan bijgehouden worden vanuit het WOZ-proces. Het betreft de situatie na oplevering. Een tot twee kamers verbouwde (van oorsprong) vier-kamerappartement wordt met vier kamers vermeld. Formaat: N2 Waardenverzameling: 00-99 Nee 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Ontsluiting verdieping** 

**Naam attribuutsoort** 

Ontsluiting verdieping 

> **Herkomst attribuutsoort** Gegevenswoordenboek WOZ (2002), overgenomen door KING 

> **Code attribuutsoort** 61.23 

> **XML-tag attribuutsoort** ontsluitingVerdieping 

## **Definitie attribuutsoort** 

Aanduiding van de manier waarop de desbetreffende bouwlaag van een object toegankelijk is gemaakt. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 1 februari 2008 **Toelichting attribuutsoort** 

Gegevenswoordenboek WOZ (2002) 

Het attribuut maakt deel uit van het StUF-sectormodel en kan bijgehouden worden vanuit het WOZ-proces. Zie verder het Gegevenswoordenboek WOZ 

|**Domein attribuutsoort**|Formaat:|AN3|
|---|---|---|
||Waardenverzameling:|T = trap|
|||R = roltrap|
|||L = lift|
|**Indicatie materiële historie**|J||
|**Indicatie formele historie**|N||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Relatiesoort VERBLIJFSOBJECT heeft als hoofdadres NUMMERAANDUIDING** 

**Naam relatiesoort** VERBLIJFSOBJECT heeft als hoofdadres NUMMERAANDUIDING **Herkomst relatiesoort** BAG **Code relatiesoort** 56.10 **Definitie relatiesoort** De identificatiecode nummeraanduiding waaronder het hoofdadres van een VERBLIJFSOBJECT, dat in het kader van de basisregistratie gebouwen als zodanig is aangemerkt, is opgenomen in de basisregistratie adressen. **Herkomst definitie relatiesoort** BAG **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** Het betreft het attribuutsoort ‘Aanduiding hoofdadres verblijfsobject’ in de BAG. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is hoofdadres van VERBLIJFSOBJECT. 

||De attribuutsoort maakt deel uit van de groepattribuutsoort BAG-|
|---|---|
||gegevens. Zie verder de toelichting in de BAG.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort VERBLIJFSOBJECT heeft als nevenadres(sen) NUMMERAANDUIDING** 

> **Naam relatiesoort** VERBLIJFSOBJECT heeft als nevenadres(sen) NUMMERAANDUIDING 

> **Herkomst relatiesoort** BAG 

> **Code relatiesoort** 56.11 

> **Definitie relatiesoort** De identificatiecodes nummeraanduiding waaronder nevenadressen van een VERBLIJFSOBJECT, die in het kader van de basisregistratie gebouwen als zodanig zijn aangemerkt, zijn opgenomen in de basisregistratie adressen. 

> **Herkomst definitie relatiesoort** BAG 

> **Datum opname relatiesoort** 9 april 2007 

## **Toelichting relatiesoort** 

> **Toelichting relatiesoort** Het betreft het attribuutsoort ‘Aanduiding nevenadressen verblijfsobject’ in de BAG. De relatie is de tegenhanger van het relatiesoort NUMMERAANDUIDING is nevenadres van VERBLIJFSOBJECT. De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort VERBLIJFSOBJECT maakt deel uit van één of meer PANDEN** 

> **Naam relatiesoort** VERBLIJFSOBJECT maakt deel uit van één of meer PANDEN 

> **Herkomst relatiesoort** BAG 

> **Code relatiesoort** 56.90 

> **Definitie relatiesoort** De unieke aanduidingen van de PANDEN waarvan het VERBLIJFSOBJECT onderdeel uitmaakt. 

> **Herkomst definitie relatiesoort** BAG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het attribuutsoort ‘Pandrelatering’ in de BAG. De relatie is de tegenhanger van het relatiesoort PAND heeft inliggend VERBLIJFSOBJECT. 

|**Toelichting relatiesoort**|Het betreft het attribuutsoort ‘Pandrelatering’ in de BAG.<br>De relatie is de tegenhanger van het relatiesoort PAND heeft inli<br>VERBLIJFSOBJECT.|
|---|---|
||De attribuutsoort maakt deel uit van de groepattribuutsoort BAG-|
||gegevens. Zie verder de toelichting in de BAG.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-M|



## **Indicatie authentiek** 

**Regels relatiesoort** 

Authentiek gegeven 

- 

## **Relatiesoort VERBLIJFSOBJECT heeft daarop INGESCHREVEN PERSOONen** 

> **Naam relatiesoort** VERBLIJFSOBJECT heeft daarop INGESCHREVEN PERSOONen 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** 08.11 

> **Definitie relatiesoort** De personen die ingeschreven zijn in de gemeente op het adres dat hoort bij het VERBLIJFSOBJECT 

> **Herkomst definitie relatiesoort** KING op basis van GBA 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van groep 11 (Adres) van categorie 08 (Verblijfplaats) in de GBA in de gevallen dat de personen verblijven in het verblijfsobject. De relatie is de tegenhanger van INGESCHREVEN PERSOON verblijft op VERBLIJFSOBJECT. Zie verder de toelichting in de GBA bij genoemd attribuutsoort. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding** Ja **strijdigheid/nietigheid** 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven **Regels relatiesoort** 

## **Relatiesoort VERBLIJFSOBJECT is huisvesting van HUISHOUDEN** 

> **Naam relatiesoort** VERBLIJFSOBJECT is huisvesting van HUISHOUDEN 

> **Herkomst relatiesoort** KING op basis van GFO BG 

> **Code relatiesoort** 96.01 

> **Definitie relatiesoort** Het VERBLIJFSOBJECT waarin één of meer HUISHOUDENs wonen. 

> **Herkomst definitie relatiesoort** KING op basis van GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

**Toelichting relatiesoort** 

Een huishouden is woonachtig in één verblijfs-object, standplaats of ligplaats. In één verblijfsobject kunnen nul, één of meer huishoudens wonen. 

De relatie is de tegenhanger van het relatiesoort HUISHOUDEN is gehuisvest in VERBLIJFSOBJECT. **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding** Nee **strijdigheid/nietigheid Indicatie kardinaliteit** 0-N **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** Niet verplicht te registreren. 

## **2.52. Verblijfstitel** 

## **Attribuutsoort Aanduiding verblijfstitel** 

**Naam attribuutsoort** 

Aanduiding verblijfstitel 

> **Herkomst attribuutsoort** GBA 

> **Code attribuutsoort** 10.39.10 

> **XML-tag attribuutsoort** aanduiding 

> **Definitie attribuutsoort** De code uit de Verblijfstiteltabel die aangeeft over welke verblijfsrechtelijke status de ingezetene beschikt. 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Zie de toelichting in de GBA. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Verblijfstitelomschrijving** 

**Naam attribuutsoort** 

Verblijfstitelomschrijving 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.88 

> **XML-tag attribuutsoort** omschrijving **Definitie attribuutsoort** 

Omschrijving van de verblijfsrechtelijke status van de ingeschrevene. GFO BG 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

1 maart 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: AN100 Waardenverzameling: Nee 

**Indicatie formele historie** 

Nee 

|**Aanduiding gebeurtenis**|Nee|
|---|---|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Regels attribuutsoort** 

## **Attribuutsoort Begindatum geldigheid verblijfstitel** 

|**Naam attribuutsoort**|Begindatum geldigheid verblijfstitel|
|---|---|
|**Herkomst attribuutsoort**|GFO BG|
|**Code attribuutsoort**|81.20|
|**XML-tag attribuutsoort**|tijdvakObject.beginObject|
|**Definitie attribuutsoort**|De datum waarop de verblijfstitel is ontstaan.|
|**Herkomst definitie attribuutsoort**|GFO BG|
|**Datum opname attribuutsoort**|1 maart 2009|
|**Toelichting attribuutsoort**|Het gaat hier om veranderingen in de lijst van codes en omschrijvingen.|
||Niet te verwarren met de datum waarop een natuurlijke persoon zijn of|
||haar verblijfstitel verkrijgt.|
|**Domein attribuutsoort**|Formaat:<br>Onvolledige datum|
||Waardenverzameling:|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|
|**Regels attribuutsoort**||



## **Attribuutsoort Einddatum geldigheid verblijfstitel** 

## **Naam attribuutsoort** 

Einddatum geldigheid verblijfstitel 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** tijdvakObject.eindObject 

> **Definitie attribuutsoort** De datum waarop de verblijfstitel is opgeheven. 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 1 maart 2009 

> **Toelichting attribuutsoort** Het gaat hier om veranderingen in de lijst van codes en omschrijvingen. Niet te verwarren met de datum waarop een natuurlijke persoon zijn of haar verblijfstitel verliest. 

> **Domein attribuutsoort** Formaat: Onvolledige datum Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

## **Relatiesoort VERBLIJFSTITEL hoort bij INGEZETENE** 

**Naam relatiesoort** 

VERBLIJFSTITEL hoort bij INGEZETENE 

> **Herkomst relatiesoort** KING/GFO 

> **Code relatiesoort** 39.10 

> **Definitie relatiesoort** De INGEZETENEN die beschikken over de VERBLIJFSTITEL. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 maart 2009 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

De relatiesoort is afgeleid van het GBA-attribuut Aanduiding verblijfstitel. Zie verder de toelichting in de GBA. 

Ja 

**Indicatie formele historie** 

Ja 

|**Aanduiding gebeurtenis**|Nee|
|---|---|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Ja|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|
|**Regels relatiesoort**||



## **2.53. Vestiging** 

## **Attribuutsoort Vestigingsnummer** 

**Naam attribuutsoort** 

Vestigingsnummer 

> **Herkomst attribuutsoort** NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

## vestigingsNummer 

Landelijk uniek identificerend administratienummer van een VESTIGING zoals toegewezen door de Kamer van Koophandel (KvK). 

KING op basis van GFO BG 

9 april 2007 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN12 Waardenverzameling: 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Groepattribuutsoort Handelsnamen** 

> **Naam attribuutsoort** Handelsnamen 

> **Herkomst attribuutsoort** NHR 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Datum opname attribuutsoort** 

De naam of de namen waaronder de vestiging handelt 9 april 2007 

## **Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: Handelsnaam Verkorte naam Volgorde. Zie verder de catalogus NHR. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Attribuutsoort Handelsnaam** 

|**Naam attribuutsoort**|Handelsnaam||
|---|---|---|
|**Herkomst attribuutsoort**|NHR||
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|handelsnaam||
|**Definitie attribuutsoort**|De naam waaronder de onderneming handelt.||
|**Datum opname attribuutsoort**|2 februari 2007||
|**Toelichting attribuutsoort**|Het attribuutsoort maakt deel uit van het groepattribuutsoort||
||Handelsnamen. Zie verder de toelichting in het NHR.||
|**Domein attribuutsoort**|Formaat:|AN200|
||Waardenverzameling: bij de KvK ingeschreven handelsnamen||
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Authentiek gegeven||



## **Attribuutsoort Verkorte naam** 

**Naam attribuutsoort** 

## Verkorte naam 

**Herkomst attribuutsoort** 

## NHR 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** handelsnaamVerkort **Definitie attribuutsoort** 

De door de Kamer van Koophandel bepaalde naam van de onderneming ten behoeve van adresseringsdoeleinden. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 2 februari 2009 **Toelichting attribuutsoort** 

KING op basis van GFO BG 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Handelsnamen. Zie verder de toelichting in het NHR. Formaat: AN45 Waardenverzameling: 

**Domein attribuutsoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Landelijk basisgegeven 

## **Attribuutsoort Volgorde** 

> **Naam attribuutsoort** Volgorde 

> **Herkomst attribuutsoort** NHR 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** volgorde **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** NHR 

{nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 2 februari 2009 **Toelichting attribuutsoort** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Handelsnamen. Zie verder de toelichting in het NHR. 

**Domein attribuutsoort** 

Formaat: N6 Waardenverzameling: 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Landelijk basisgegeven|



## **Groepattribuutsoort Activiteiten** 

**Naam attribuutsoort** 

Activiteiten 

**Herkomst attribuutsoort** 

NHR 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

Korte aanduiding van de uitgeoefende activiteit of activiteiten. 

## NHR 

2 februari 2009 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Indicatie hoofdactiviteit Activiteitcode Activiteit. 

Zie verder de catalogus NHR. 

**Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Indicatie hoofdactiviteit** 

**Naam attribuutsoort** 

Indicatie hoofdactiviteit 

**Herkomst attribuutsoort** 

## NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

activiteit.indicatieHoofdactiviteit 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** NHR **Datum opname attribuutsoort** 2 februari 2009 

{nog niet in NHR uitgewerkt} 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

Formaat: AN3 Waardenverzameling: Ja, Nee Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk  basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Activiteitcode** 

**Naam attribuutsoort** 

Activiteitcode 

**Herkomst attribuutsoort** 

NHR 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

activiteit.code 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Een door een standaardcodes weergegeven typeringen behorende bij een VESTIGING 

9 april 2007 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

Formaat: N15 Waardenverzameling: 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Activiteit** 

> **Naam attribuutsoort** Activiteit 

> **Herkomst attribuutsoort** NHR 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** activiteit.omschrijving **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** NHR 

> **Datum opname attribuutsoort** 2 februari 2009 

Eén van de activiteiten van de vestiging 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Activiteiten. Zie verder de toelichting in het NHR. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Landelijk  basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Typering hoofd/nevenvestiging** 

**Naam attribuutsoort** 

Typering hoofd/nevenvestiging 

> **Herkomst attribuutsoort** NHR 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

## typeringVestiging 

Indicatie welke vestiging de hoofdvestiging of de hoofdnederzetting is indien een onderneming meerdere vestigingen heeft. KING op basis van Catalogus NHR 

9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN15 Waardenverzameling: Hoofdvestiging, Nevenvestiging 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Datum aanvang** 

> **Naam attribuutsoort** Datum aanvang 

> **Herkomst attribuutsoort** NHR **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumAanvang 

> **Definitie attribuutsoort** {nog niet in NHR uitgewerkt 

> **Datum opname attribuutsoort** 2 februari 2009 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

1-1 

**Indicatie authentiek** 

Authentiek gegeven 

## **Attribuutsoort Datum beëindiging** 

|**Naam attribuutsoort**|Datum beëindiging||
|---|---|---|
|**Herkomst attribuutsoort**|NHR||
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|datumEinde||
|**Definitie attribuutsoort**|{nog niet in NHR uitgewerkt||
|**Datum opname attribuutsoort**|2 februari 2009||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Ja||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Authentiek gegeven||



## **Relatiesoort VESTIGING betreft uitoefening van activiteiten door MAATSCHAPPELIJKE ACTIVITEIT** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

VESTIGING betreft uitoefening van activiteiten door MAATSCHAPPELIJKE ACTIVITEIT 

KING op basis van NHR 

## **Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 

{nog niet in NHR uitgewerkt 

KING op basis van NHR 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Vestigingnummer(s) van de bijbehorende vestiging(en)’ bij het objecttype Maatschappelijke activiteit in het NHR. De relatie is de tegenhanger van MAATSCHAPPELIJKE  ACTIVITEIT Oefent activiteit uit in VESTIGING. Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** {nog niet in NHR uitgewerkt 

## **Relatiesoort VESTIGING heeft hoofdlocatie in of op BENOEMD OBJECT** 

> **Naam relatiesoort** VESTIGING heeft hoofdlocatie in of op BENOEMD OBJECT 

> **Herkomst relatiesoort** KING op basis van NHR **Code relatiesoort** 

> **Definitie relatiesoort** Het BENOEMD OBJECT waarin of waarop zich (het gedeelte van) de VESTIGING bevindt dat beschouwd wordt als hoofdlocatie voor de uitvoering van de activiteiten van deze VESTIGING 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Bezoekadres’ bij het objecttype Vestiging in het NHR v.w.b. benoemde objecten d.w.z. naast adresseerbare objecten ook overige gebouwde objecten en overige terreinen. De relatie is de tegenhanger van BENOEMD OBJECT is hoofdlocatie van VESTIGINGen. 

Zie verder de toelichting in het NHR bij genoemd attribuutsoort. 

||obje<br>obje<br>De r<br>VES<br>Zie|
|---|---|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|



## **Indicatie kardinaliteit** 

**Indicatie authentiek** 

Authentiek gegeven 

## **Regels relatiesoort** 

## **Relatiesoort VESTIGING heeft nevenlocatie in of op BENOEMD OBJECT** 

> **Naam relatiesoort** VESTIGING heeft nevenlocatie in of op BENOEMD OBJECT 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De BENOEMDe OBJECTen waarin zich de gedeelten van een VESTIGING bevinden die niet beschouwd worden als hoofdlocatie voor de uitvoering van de activiteiten van deze VESTIGING. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het NHR kent per vestiging slechts één adres, in het RSGB gemodelleerd met de relatie ‘VESTIGING heeft hoofdlocatie in of op BENOEMD OBJECT’. Het RSGB biedt daarnaast de mogelijkheid om ook andere locaties te benoemen waarin die vestiging ook haar activiteiten uitoefent. Dit moet niet verward worden met de hoofdvestiging en de nevenvestigingen van een maatschappelijke activiteit. Elke hoofd- en nevenvestiging (van een maatschappelijke activiteit) heeft minimaal een hoofdlocatie (van die vestiging). De relatie is de tegenhanger van BENOEMD OBJECT is nevenlocatie van VESTIGINGen. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-M 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort VESTIGING heeft als locatie-adres ADRESSEERBAAR OBJECTAANDUIDING** 

|**Naam relatiesoort**|VESTIGING heeft als locatie-adres ADRESSEERBAAR|
|---|---|
||OBJECTAANDUIDING|
|**Herkomst relatiesoort**|KING op basis van NHR|



## **Code relatiesoort** 

> **Definitie relatiesoort** De ADRESSEERBAAR OBJECTAANDUIDING bij het BENOEMD OBJECT waarin de VESTIGING (één van) haar lokatie(s) heeft en die bij inschrijving gekozen is als vestigingssadres. 

> **Datum opname relatiesoort** 1 maart 2009 

> **Toelichting relatiesoort** De vestiging kan er aldus voor kiezen zich op een hoofd- of op een nevenadres te laten inschrijven. De relatie is de tegenhanger van ADRESSEERBAAR OBJECTAANDUIDING is locatie-adres van VESTIGINGen. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Regels attribuutsoort** 

## **2.54. Waterdeel** 

## **Attribuutsoort Type waterdeel** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Type waterdeel 

IMGeo 

> **Code attribuutsoort** - **XML-tag attribuutsoort Definitie attribuutsoort** 

type 

Specificatie van het soort water 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Formaat: AN40 

Waardenverzameling: zie IMGeo, CodeList TypeWater Ja 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Type Infrastructuur** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Type Infrastructuur 

IMGeo 

- 

typeInfrastructuur 

Soort infrastructureel element 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie IMGeo, CodeList TypeInfrastructuur 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Identificatie waterdeel** 

**Naam attribuutsoort** 

Identificatie waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** identificatie **Definitie attribuutsoort** 

Een unieke identificatie voor een waterdeel 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort Domein attribuutsoort** 

## IMGeo 

9 april 2007 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

> **Domein attribuutsoort** Formaat: AN25 Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (03) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status waterdeel** 

**Naam attribuutsoort** 

Status waterdeel 

**Herkomst attribuutsoort Code attribuutsoort** - **XML-tag attribuutsoort Definitie attribuutsoort** 

## IMGeo 

## status 

De status gekoppeld aan de levenscyclus van het waterdeel. 

|**Herkomst definitie attribuutsoort**|IMGeo||
|---|---|---|
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|In het IMGeo betreft dit de status||
|**Domein attribuutsoort**|Formaat:|A8|
||Waardenverzameling: Plan||
|||Bestaand|
|||Historie|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijke basisgegeven||
|**Regels attribuutsoort**|-||



In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

## **Attribuutsoort Naam waterdeel** 

> **Naam attribuutsoort** Naam waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** naam 

## **Definitie attribuutsoort** 

## Benaming van het waterdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** - 

> **Domein attribuutsoort** Formaat: ScopedName. Waardenverzameling: - 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Geometrie waterdeel** 

**Naam attribuutsoort** 

Geometrie waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

De minimaal tweedimensionale geometrische representatie van de omtrekken van een waterdeel 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een waterdeel. 

Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Zie de inwinningsregels zoals beschreven in het IMGeo bij Waterdeel. 

## **Attribuutsoort Relatieve hoogteligging waterdeel** 

> **Naam attribuutsoort** Relatieve hoogteligging waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** relatieveHoogteligging 

> **Definitie attribuutsoort** Aanduiding voor de relatieve hoogte van het waterdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

> **Domein attribuutsoort** Formaat: N1 Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De objecten op maaiveldniveau moeten een gebiedsdekkend geheel vormen. 

## **Attribuutsoort Datum begin geldigheid waterdeel** 

## **Naam attribuutsoort** 

Datum begin geldigheid waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop het waterdeel is ontstaan. 

Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: OnvolledigeDatum 

**Domein attribuutsoort** 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid waterdeel** 

> **Naam attribuutsoort** Datum einde geldigheid waterdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** De datum waarop het waterdeel ongeldig is geworden. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid waterdeel’ kan in de registratie worden opgenomen. 

## **2.55. Wegdeel** 

## **Attribuutsoort Type weg** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Type weg 

IMGeo - 

type 

Specificatie van het soort weg 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Formaat: AN40 

Waardenverzameling: zie IMGeo, CodeList TypeWeg Ja 

Ja 

Nee 

Nee 

Nee 

Nee 

0-1 Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Type Infrastructuur** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

Type Infrastructuur 

IMGeo 

- 

typeInfrastructuur 

Soort infrastructureel element 

IMGeo 

9 april 2007 

**Toelichting attribuutsoort** 

|**Domein attribuutsoort**|Formaat:|AN40|
|---|---|---|
||Waardenverzameling: zie IMGeo, CodeList TypeInfrastructuur||
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Attribuutsoort Verharding** 

|**Naam attribuutsoort**|Verharding||
|---|---|---|
|**Herkomst attribuutsoort**|IMGeo||
|**Code attribuutsoort**|-||
|**XML-tag attribuutsoort**|verharding||
|**Definitie attribuutsoort**|Mate waarin het wegdeel al of niet verhard is||
|**Herkomst definitie attribuutsoort**|IMGeo||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|AN40|
||Waardenverzameling: zie IMGeo, CodeList Verharding||
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



## **Attribuutsoort Identificatie wegdeel** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Identificatie wegdeel 

IMGeo 

**Code attribuutsoort XML-tag attribuutsoort** 

- 

## identificatie 

**Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Een unieke identificatie voor een wegdeel 

## IMGeo 

9 april 2007 

In het IMGeo betreft dit de identificatie van het overeenkomstige geoobject. 

Formaat: AN25 Waardenverzameling: NL.IMGEO.xxxx. Het 1e deel is de landcode, het 2e deel is de code voor het sectormodel. Het derde deel is de combinatie van de (viercijferige) gemeentecode (volgens GBA tabel 33), de tweecijferige code voor het type geoobject (01) en een voor het betreffende objecttype binnen een gemeente unieke tiencijferige objectvolgnummer. 

||(vierc<br>33), d<br>objec<br>binne<br>objec|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijke basisgegeven|
|**Regels attribuutsoort**|-|



## **Attribuutsoort Status wegdeel** 

> **Naam attribuutsoort** Status wegdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** status 

> **Definitie attribuutsoort** De status gekoppeld aan de levenscyclus van het wegdeel. 

> **Herkomst definitie attribuutsoort** IMGeo 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## 9 april 2007 

In het IMGeo betreft dit de status van het overeenkomstige geo-object. 

> **Domein attribuutsoort** Formaat: A8 Waardenverzameling: Plan Bestaand Historie 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Naam wegdeel** 

|**Naam attribuutsoort**|Naam wegdeel||
|---|---|---|
|**Herkomst attribuutsoort**|IMGeo||
|**Code attribuutsoort**|-||
|**XML-tag attribuutsoort**|naam||
|**Definitie attribuutsoort**|Benaming van het wegdeel||
|**Herkomst definitie attribuutsoort**|IMGeo||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|-||
|**Domein attribuutsoort**|Formaat:|ScopedName.|
||Waardenverzameling: -||
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||



**Indicatie authentiek** 

**Regels attribuutsoort** 

## Gemeentelijke basisgegeven 

- 

## **Attribuutsoort Geometrie wegdeel** 

**Naam attribuutsoort** 

## Geometrie wegdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** geometrie **Definitie attribuutsoort** 

De minimaal tweedimensionale geometrische representatie van de omtrekken van een wegdeel 

**Herkomst definitie attribuutsoort** 

## KING 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

Het betreft de geometrie zoals gedefinieerd in het IMGeo bij een wegdeel. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: aanduiding van het type geometrie (Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RDstelsel. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Zie de inwinningsregels zoals beschreven in het IMGeo bij Wegdeel. 

## **Attribuutsoort Relatieve hoogteligging wegdeel** 

**Naam attribuutsoort Herkomst attribuutsoort** IMGeo **Code attribuutsoort** - **XML-tag attribuutsoort** relatieveHoogteligging **Definitie attribuutsoort** 

Relatieve hoogteligging wegdeel 

Aanduiding voor de relatieve hoogte van het wegdeel 

> **Herkomst definitie attribuutsoort** IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

> **Domein attribuutsoort** Formaat: N1 Waardenverzameling: gehele positieve en negatieve getallen in het bereik van -5 tot +5 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** De objecten op maaiveldniveau moeten een gebiedsdekkend geheel vormen. 

Weergegeven wordt de hoogteligging van de objecten ten opzichte van elkaar. Hiervoor wordt gebruik gemaakt van niveaus die aangeven of een object zich op maaiveldniveau (niveau 0) bevindt of op een onder- of bovenliggend niveau. Standaard wordt aan een object ‘niveau 0’ toegekend. Het niveau geeft geen informatie over de absolute hoogte van een object. 

## **Attribuutsoort Datum begin geldigheid wegdeel** 

> **Naam attribuutsoort** Datum begin geldigheid wegdeel 

> **Herkomst attribuutsoort** IMGeo 

> **Code attribuutsoort** - 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop het wegdeel is ontstaan. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** Het betreft het attribuutsoort objectBeginTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid wegdeel** 

**Naam attribuutsoort Herkomst attribuutsoort** IMGeo **Code attribuutsoort** - **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort Herkomst definitie attribuutsoort** KING **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

Datum einde geldigheid wegdeel 

De datum waarop het wegdeel ongeldig is geworden. 

Het betreft het attribuutsoort objectEindTijd van het overeenkomstige Geo-object in het IMGeo. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: OnvolledigeDatum 

**Domein attribuutsoort** 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid wegdeel’ kan in de registratie worden opgenomen. 

## **2.56. Wijk** 

## **Attribuutsoort Wijkcode** 

**Naam attribuutsoort** 

Wijkcode 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.90 

> **XML-tag attribuutsoort** wijkCode **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

De code behorende bij de naam van de wijk. 

**Toelichting attribuutsoort** 

De gehanteerde codering is de CBS-wijkcode. De wijkgrenzen worden in overleg tussen gemeente en CBS vastgesteld. Een unieke buurtcode ontstaat door combinatie van de gemeentecode (4 posities), de wijkcode (2 posities) en de buurtcode (2 posities). Formaat: N2 Waardenverzameling: Wijkcode conform CBS-tabel 

**Domein attribuutsoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijke basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Wijknaam** 

**Naam attribuutsoort** 

## Wijknaam 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 95.91 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

## wijkNaam 

De naam van de wijk, zoals die door het CBS wordt gebruikt. 

## GFO BG 

9 april 2007 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: alle alfanumerieke tekens zonder … 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Wijkgeometrie** 

> **Naam attribuutsoort** Wijkgeometrie 

> **Herkomst attribuutsoort** IMGeo **Code attribuutsoort** 

> **XML-tag attribuutsoort** geometrie 

**Definitie attribuutsoort** 

De tweedimensionale geometrische representatie van de omtrekken van de wijk. 

> **Herkomst definitie attribuutsoort** KING op basis van IMGeo 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De wijkgrenzen zijn zoveel mogelijk gebaseerd op sociaalgeografische kenmerken. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: alle binnen Nederland gelegen waarden van het RD-stelsel. 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|



## **Regels attribuutsoort** 

## **Attribuutsoort Datum begin geldigheid wijk** 

> **Naam attribuutsoort** Datum begin geldigheid wijk 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.20 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 **Toelichting attribuutsoort** 

De datum waarop de wijk is gecreëerd. 

In het GFO BG was de attribuutnaam ‘Ingangsdatum wijk’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. Formaat: OnvolledigeDatum 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid wijk** 

**Naam attribuutsoort** 

Datum einde geldigheid wijk 

> **Herkomst attribuutsoort** GFO BG 

> **Code attribuutsoort** 81.30 

> **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO BG 

> **Datum opname attribuutsoort** 9 april 2007 

De datum waarop een wijk is komen te vervallen. 

9 april 2007 

> **Toelichting attribuutsoort** In het GFO BG was de attribuutnaam ‘Einddatum wijk’. Vanwege naamsconventies binnen het stelsel van basisgegevens is voor een andere attribuutnaam gekozen. 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid wijk’ kan in de registratie worden opgenomen. 

## **Relatiesoort WIJK ligt in GEMEENTE** 

|**Naam relatiesoort**|WIJK ligt in GEMEENTE|
|---|---|
|**Herkomst relatiesoort**|GFO BG|
|**Code relatiesoort**|94.64|
|**Definitie relatiesoort**|De gemeente waarin de wijk is gelegen.|
|**Herkomst definitie relatiesoort**|GFO BG|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|Een gemeente bestaat uit een of meer wijken. Een wijk ligt in 1|
||gemeente.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort WIJK bestaat uit BUURTen** 

> **Naam relatiesoort** WIJK bestaat uit BUURTen 

> **Herkomst relatiesoort** GFO BG 

> **Code relatiesoort** 94.08 

> **Definitie relatiesoort** De wijk waarin de buurt is gelegen. 

> **Herkomst definitie relatiesoort** GFO BG 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Een wijk bestaat uit een of meer buurten. Een buurt ligt in 1 wijk. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **2.57. Woonplaats** 

## **Groepattribuutsoort BAG-gegevens** 

> **Naam attribuutsoort** BAG-gegevens 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 19 november 2008 **Toelichting attribuutsoort** 

De gegevens van de WOONPLAATS zoals die zijn opgenomen in de BasisRegistratie Adressen. 

Het groepatribuutsoort is toegevoegd teneinde de BAG-gegevens te kunnen onderscheiden van de andere gegevens en hen de metagegevens mee te kunnen geven zoals gespecificeerd in de catalogus BAG. 

Het groepattribuutsoort bestaat uit de volgende attribuutsoorten: 11.03 Woonplaatsidentificatie 11.70 Woonplaatsnaam 11.71 Woonplaatsgeometrie 11.72 Indicatie geconstateerde woonplaats 11.79 Woonplaatsstatus en de volgende relatiesoorten: WOONPLAATS heeft OPENBARE RUIMTE WOONPLAATS betreft ADRESSEERBAAR OBJECT AANDUIDING **Domein attribuutsoort** n.v.t **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum **Indicatie in onderzoek** Ja **Aanduiding** Nee **strijdigheid/nietigheid Indicatie kardinaliteit** 1-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

## **Attribuutsoort Woonplaatsidentificatie** 

**Naam attribuutsoort** 

Woonplaatsidentificatie 

**Herkomst attribuutsoort** 

## BAG 

**Code attribuutsoort XML-tag attribuutsoort** 

11.03 

identificatie 

De unieke aanduiding van een WOONPLAATS, zoals opgenomen in de landelijke woonplaatsentabel. 

## **Definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

9 april 2007 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. Nee 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit ***** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Woonplaatsnaam** 

**Naam attribuutsoort** 

Woonplaatsnaam 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.70 

> **XML-tag attribuutsoort** woonplaatsNaam 

> **Definitie attribuutsoort** De door het bevoegde gemeentelijke orgaan aan een WOONPLAATS 

De door het bevoegde gemeentelijke orgaan aan een WOONPLAATS toegekende benaming. 

|**Definitie attribuutsoort**|De door het<br>toegekende|
|---|---|
|**Datum opname attribuutsoort**|9 april 2007|
|**Toelichting attribuutsoort**|De attribuut|
||gegevens. Z|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit *****|1-1|



De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. Nee 

**Indicatie authentiek** 

Authentiek gegeven 

## **Attribuutsoort Woonplaatsgeometrie** 

**Naam attribuutsoort** 

Woonplaatsgeometrie 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.71 

> **XML-tag attribuutsoort** geometrie 

## **Definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie** 

De tweedimensionale geometrische representatie van het vlak dat wordt gevormd door de omtrekken van een woonplaats. 9 april 2007 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

Nee 

Nee 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit ***** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Indicatie geconstateerde woonplaats** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Indicatie geconstateerde woonplaats 

BAG 

**Code attribuutsoort** 

11.72 

> **XML-tag attribuutsoort** geconstateerd 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Indicatie materiële historie** 

Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. 

9 april 2007 

De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit ***** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Woonplaatsstatus** 

> **Naam attribuutsoort** Woonplaatsstatus 

> **Herkomst attribuutsoort** BAG 

> **Code attribuutsoort** 11.79 

> **XML-tag attribuutsoort** status 

> **Definitie attribuutsoort** De fase van de levenscyclus van een WOONPLAATS, waarin de betreffende WOONPLAATS zich bevindt. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting attribuutsoort** De attribuutsoort maakt deel uit van de groepattribuutsoort BAGgegevens. Zie verder de toelichting in de BAG. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Woonplaatsnaam NEN** 

**Naam attribuutsoort** 

> **Naam attribuutsoort** Woonplaatsnaam NEN 

> **Herkomst attribuutsoort** NEN 5825 (2002) **Code attribuutsoort** 

> **XML-tag attribuutsoort** woonplaatsNaamNen 

> **Definitie attribuutsoort** De door TNT Post gehanteerde naam van een woonplaats 

> **Herkomst definitie attribuutsoort** NEN 5825 (2002) 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het attribuut bevat een verkorte naam ten opziche van de officiele woonplaatsnaam zoals geregistreerd in de BAG. 

> **Domein attribuutsoort** Formaat: AN24 Waardenverzameling: woonplaatsnamen in de TNT Postcodetabel 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Datum begin geldigheid woonplaats** 

|**Naam attribuutsoort**|Datum begin geldigheid woonplaats|Datum begin geldigheid woonplaats|
|---|---|---|
|**Herkomst attribuutsoort**|KING||
|**Code attribuutsoort**|-||
|**XML-tag attribuutsoort**|ingangsdatumObject||
|**Definitie attribuutsoort**|De datum waarop de|woonplaats is ontstaan.|
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||



## **Regels attribuutsoort** 

## **Attribuutsoort Datum einde geldigheid woonplaats** 

## **Naam attribuutsoort** 

Datum einde geldigheid woonplaats 

|**Herkomst attribuutsoort**|KING||
|---|---|---|
|**Code attribuutsoort**|-||
|**XML-tag attribuutsoort**|einddatumObject||
|**Definitie attribuutsoort**|De datum waarop de|woonplaats is komen te vervallen.|
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|Alleen een datum die|gelijk is aan of die gelegen is na de datum zoals|
||opgenomen onder 'Datum begin geldigheid …’ kan in de registratie||
||worden opgenomen.||



## **Relatiesoort WOONPLAATS ligt in GEMEENTE** 

**Naam relatiesoort Herkomst relatiesoort** KING **Code relatiesoort** - **Definitie relatiesoort Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 

WOONPLAATS ligt in GEMEENTE 

De GEMEENTE waarin de WOONPLAATS is gelegen. 

9 april 2007 

**Toelichting relatiesoort** 

> **Toelichting relatiesoort** Een woonplaats zoals gedefinieerd in de BAG ligt altijd binnen één gemeente. Een aaneengesloten gedeelte van Nederland dat aangeduid wordt met dezelfde woonplaatsnaam maar dat doorsneden wordt door één of meer gemeentegrenzen wordt aldus geregistreerd als meerdere woonplaatsen. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort WOONPLAATS heeft OPENBARE RUIMTE** 

> **Naam relatiesoort** WOONPLAATS heeft OPENBARE RUIMTE 

> **Herkomst relatiesoort** KING op basis van BAG 

**Code relatiesoort Definitie relatiesoort** De binnen de WOONPLAATS gelegen OPENBARE RUIMTEn. **Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. De relatie is de tegenhanger van het attribuutsoort ‘Identificatie bijbehorende woonplaats’ bij de Openbare ruimte in de BAG cq. van het relatiesoort OPENBARE RUIMTE ligt in WOONPLAATS. Een openbare ruimte zoals gedefinieerd in de BAG ligt altijd binnen één woonplaats. 

Zie verder de toelichting in de BAG. 

||bijbe<br>relat<br>Een<br>woo<br>Zie|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-N|



**Indicatie authentiek** 

**Regels relatiesoort** 

Gemeentelijk basisgegeven 

- 

## **Relatiesoort WOONPLAATS betreft ADRESSEERBAAR OBJECT AANDUIDING** 

**Naam relatiesoort Herkomst relatiesoort Code relatiesoort Definitie relatiesoort** 

WOONPLAATS betreft ADRESSEERBAAR OBJECT AANDUIDING 

KING op basis van BAG 

- 

De ADRESSEERBAAR OBJECT AANDUIDING en van de objecten die gelegen zijn in de WOONPLAATS en waarvan de OPENBARE RUIMTe, waaraan de ADRESSEERBAAR OBJECT AANDUIDING is gerelateerd, gelegen is in een andere WOONPLAATS. KING 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** De relatiesoort maakt deel uit van de groepattribuutsoort BAG-gegevens. De relatie is de tegenhanger van het attribuutsoort ‘Identificatie bijbehorende woonplaats’ bij de NUMMERAANDUIDING in de BAG cq. van het relatiesoort ADRESSEERBAAR OBJECT AANDUIDING ligt in WOONPLAATS. Zie verder de toelichting in de BAG. 

||De relatie is de tegenhange<br>bijbehorende woonplaats’ bi<br>van het relatiesoort ADRES<br>WOONPLAATS.<br>Zie verder de toelichting in d|
|---|---|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|-|



## **Relatiesoort WOONPLAATS maakt deel uit van woonadreslocatie van INGESCHREVEN PERSOON** 

> **Naam relatiesoort** WOONPLAATS maakt deel uit van verblijfslocatie van INGESCHREVEN PERSOON 

> **Herkomst relatiesoort** KING op basis van GBA 

> **Code relatiesoort** - 

## **Definitie relatiesoort** 

> **Definitie relatiesoort** De personen die ingeschreven zijn op de WOONPLAATS indien het adres waarop deze personen zijn ingeschreven geen NUMMERAANDUIDING betreft. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van attribuutsoort 10.20 (Gemeentedeel) in de GBA in de gevallen dat de persoon niet ingeschreven kan worden op een verblijfsobject, stand- of ligplaats. De relatie is de tegenhanger van het relatiesoort INGESCHREVEN PERSOON verblijft op locatie in WOONPLAATS. De relatie wordt alleen geregistreerd indien de persoon niet verblijft in een verblijfsobject, stand- en ligplaats. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Ja 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Authentiek gegeven 

> **Regels relatiesoort** - 

## **Relatiesoort WOONPLAATS is deel van correspondentieadres zijnde postadres van SUBJECT** 

**Naam relatiesoort** 

WOONPLAATS is deel van correspondentieadres zijnde postadres van SUBJECT 

> **Herkomst relatiesoort** KING 

**Code relatiesoort Definitie relatiesoort** Van SUBJECTEN de postadressen die gelegen zijn in de WOONPLAATS **Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 9 april 2007 **Toelichting relatiesoort** De relatie is de tegenhanger van SUBJECT heeft als correspondientieadres postadres in WOONPLAATS. **Indicatie materiële historie** Ja **Indicatie formele historie** N **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee 

|**Indicatie in onderzoek**|Nee|
|---|---|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-N|
|**Indicatie authentiek**|Gemeentelijk basisgegeven|
|**Regels relatiesoort**|Niet verplicht te registreren|



## **2.58. WOZ-belang** 

## **Attribuutsoort Status belang** 

|**Naam attribuutsoort**|Status belang|
|---|---|
|**Herkomst attribuutsoort**|BR WOZ|
|**Code attribuutsoort**|15.89|
|**XML-tag attribuutsoort**|statusBelang|
|**Definitie attribuutsoort**|De fase van de levenscyclus van een BELANG.|
|**Datum opname attribuutsoort**|1 februari 2008|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Aanduiding eigenaar/gebruiker** 

**Naam attribuutsoort** 

Aanduiding eigenaar/gebruiker 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 41.10 

> **XML-tag attribuutsoort** aanduidingEigenaarGebruiker **Definitie attribuutsoort** 

De aanduiding of het genoemde subject eigenaar of gebruiker van het genoemde WOZ-object is, dan wel of deze eigenaargebruiker is. 1 februari 2008 

**Datum opname attribuutsoort Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 

## **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Datum begin geldigheid belang** 

|**Naam attribuutsoort**|Datum begin geldigheid belang|Datum begin geldigheid belang|
|---|---|---|
|**Herkomst attribuutsoort**|WOZ/KING||
|**Code attribuutsoort**|81.22||
|**XML-tag attribuutsoort**|tijdvakRelatie.beginRelatie||
|**Definitie attribuutsoort**|Een aanduiding op welk tijdstip een relatie is ontstaan.||
|**Datum opname attribuutsoort**|1 februari 2008||
|**Domein attribuutsoort**|Formaat:|OnvolledigeDatum|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||



## **Attribuutsoort Datum einde geldigheid belang** 

> **Naam attribuutsoort** Datum einde geldigheid belang 

> **Herkomst attribuutsoort** WOZ/KING 

> **Code attribuutsoort** 82.32 

> **XML-tag attribuutsoort** tijdvakRelatie.eindRelatie 

> **Definitie attribuutsoort** Een aanduiding op welk tijdstip een relatie is beëindigd. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Een aanduiding op welk tijdstip een relatie is beëindigd. 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Relatiesoort WOZ-BELANG betreft WOZ-OBJECT** 

> **Naam relatiesoort** WOZ-BELANG betreft WOZ-OBJECT 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.01a 

> **Definitie relatiesoort** De unieke aanduiding van het WOZ-OBJECT waarbij het WOZ-BELANG hoort. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerd WOZ-object’ bij het objecttype WOZ-BELANG. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZOBJECT heeft WOZ-BELANG. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-BELANG heeft als aangewezen belanghebbende SUBJECT** 

> **Naam relatiesoort** WOZ-BELANG heeft als aangewezen belanghebbende SUBJECT 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.20a/01.30a 

> **Definitie relatiesoort** De unieke aanduiding van de natuurlijk of niet-natuurlijk persoon of vestiging die als belanghebbende is aangewezen. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als de attribuutsoorten ‘Aangewezen belanghebbende (Burgerservicenummer)’ en ‘Aangewezen belanghebbende (FI-nummer)’ bij het objecttype WOZ-BELANG. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van SUBJECT Is aangewezen belanghebbende bij WOZ-BELANG. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **2.59. WOZ-deelobject** 

## **Attribuutsoort Nummer WOZ-deelobject** 

**Naam attribuutsoort** 

Nummer WOZ-deelobject 

**Herkomst attribuutsoort** 

Gegevenswoordenboek WOZ (2002), overgenomen door KING 11.71 

> **Code attribuutsoort** 11.71 

> **XML-tag attribuutsoort** nummerWOZDeelObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** Gegevenswoordenboek WOZ (2002) 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Toelichting attribuutsoort** Zie het Gegevenswoordenboek WOZ 

> **Domein attribuutsoort** Formaat: N6 Waardenverzameling: 0 - 999999 

> **Indicatie materiële historie** N 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Uniek identificatienummer voor het deelobject binnen een WOZ-object. 

## **Attribuutsoort Code WOZ-deelobject** 

**Naam attribuutsoort** 

Code WOZ-deelobject 

> **Herkomst attribuutsoort** Gegevenswoordenboek WOZ (2002), overgenomen door KING 

> **Code attribuutsoort** 61.15 

> **XML-tag attribuutsoort** codeWOZDeelObject **Definitie attribuutsoort** 

Aanduiding van het soort deelobject ten behoeve van een correcte interpretatie van de onderbouwing van de taxatie. Gegevenswoordenboek WOZ (2002) 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

1 februari 2008 

**Toelichting attribuutsoort** 

Zie het Gegevenswoordenboek WOZ 

> **Domein attribuutsoort** Formaat: AN4 Waardenverzameling: zie WOZ-tabel tabel "codering onderdelen WOZobjecten" 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** N 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status WOZ-deelobject** 

**Naam attribuutsoort** 

Status WOZ-deelobject 

> **Herkomst attribuutsoort** WOZ/KING 

> **Code attribuutsoort** 64.23 **XML-tag attribuutsoort Definitie attribuutsoort** 

statusWOZDeelObject 

De fase van de levenscyclus van een WOZ-DEELOBJECT, waarin het betreffende WOZ-DEELOBJECT zich bevindt. 

**Herkomst definitie attribuutsoort** 

Gegevenswoordenboek WOZ (2002) 

**Datum opname attribuutsoort** 

1 februari 2008 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## Formaat: 

Waardenverzameling: gevormd, niet actief, actief beëindigd ten onrechte opgevoerd 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|N|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|



## **Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Datum begin geldigheid deelobject** 

**Naam attribuutsoort** 

Datum begin geldigheid deelobject 

> **Herkomst attribuutsoort** WOZ/KING 

> **Code attribuutsoort** 81.21 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

Een aanduiding op welk tijdstip een deelobject is ontstaan. 

Formaat: OnvolledigeDatum 

## **Attribuutsoort Datum einde geldigheid deelobject** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort Datum opname attribuutsoort** 

Datum einde geldigheid deelobject 

WOZ/KING 

82.31 

einddatumObject 

Een aanduiding op welk tijdstip een deelobject is beëindigd. 1 februari 2008 

**Domein attribuutsoort Indicatie materiële historie Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Formaat: OnvolledigeDatum 

Nee 

Ja 

Nee Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Relatiesoort WOZ-DEELOBJECT is onderdeel van WOZ-OBJECT** 

**Naam relatiesoort** 

WOZ-DEELOBJECT is onderdeel van van WOZ-OBJECT 

> **Herkomst relatiesoort** WOZ/KING 

> **Code relatiesoort** 01.01a 

> **Definitie relatiesoort** De unieke aanduiding van het WOZ-OBJECT waarvan het WOZDEELOBJECT deel van uitmaakt. 

> **Herkomst definitie relatiesoort** KING op basis van het WOZ-gegevenswoordenboek 

> **Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

De unieke aanduiding van het WOZ-OBJECT waarvan het WOZDEELOBJECT deel van uitmaakt. 

In het WOZ-gegevenswoordenboek is dit gemodelleerd als het attribuutsoort ‘WOZ-objectnummer’ bij de entiteit ‘onderdelen voor onderbouwing taxatie WOZ-object’. In het RSGB wordt dit hergebruikt als relatiesoort. De relatie is de tegenhanger van WOZ-OBJECT bestaat uit WOZ-DEELOBJECT. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-DEELOBJECT bestaat uit BENOEMD OBJECT** 

> **Naam relatiesoort** WOZ-DEELOBJECT bestaat uit BENOEMD OBJECT 

> **Herkomst relatiesoort** KING 

> **Code relatiesoort** 56.01a 

> **Definitie relatiesoort** De unieke aanduiding van het BENOEMD OBJECT dat geheel of gedeeltelijk deel uitmaakt van het WOZ-DEELOBJECT. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde verblijfsobjecten, stand- en ligplaatsen’ bij het WOZ-object. In het RSGB wordt dit hergebruikt als relatiesoort vanuit WOZ-DEELOBJECT. De relatie is de tegenhanger van BENOEMD OBJECT bestaat uit één of meer WOZ-DEELOBJECTen. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-DEELOBJECT bestaat uit PAND** 

**Naam relatiesoort Herkomst relatiesoort** KING **Code relatiesoort** 55.01a **Definitie relatiesoort** 

WOZ-DEELOBJECT bestaat uit PAND 

De unieke aanduiding van het PAND dat geheel of gedeeltelijk deel uitmaakt van het WOZ-DEELOBJECT. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

KING op basis van de catalogus BRWOZ 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde panden’ bij het WOZ-object. In het RSGB wordt dit hergebruikt als relatiesoort vanuit WOZ-DEELOBJECT. De relatie is de tegenhanger van PAND bestaat uit één of meer WOZ-DEELOBJECTen. 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Gemeentelijk basisgegeven.|



**Regels relatiesoort** 

- 

## **2.60. WOZ-object** 

## **Attribuutsoort WOZ-objectnummer** 

|**Naam attribuutsoort**|WOZ-objectnummer|
|---|---|
|**Herkomst attribuutsoort**|BR WOZ|
|**Code attribuutsoort**|01.01|
|**XML-tag attribuutsoort**|wozObjectNummer|
|**Definitie attribuutsoort**|De unieke aanduiding van een WOZ-OBJECT.|
|**Datum opname attribuutsoort**|1 februari 2008|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven|



## **Attribuutsoort Locatie-omschrijving** 

**Naam attribuutsoort** 

Locatie-omschrijving 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 11.80 **XML-tag attribuutsoort Definitie attribuutsoort** 

aanduidingWOZobject.locatieomschrijving 

De aanvullende omschrijving van de ligging van een WOZ-OBJECT ten opzichte van een betrokken of het dichtstbijzijnde VERBLIJFSOBJECT, STANDPLAATS, LIGPLAATS, OVERIG GEBOUWD OBJECT, OVERIG TERREIN of OPENBARE RUIMTE. 

**Datum opname attribuutsoort** 

1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Geometrie WOZ-object** 

**Naam attribuutsoort** 

Geometrie WOZ-object 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.71 

> **XML-tag attribuutsoort** wozObjectGeometrie 

> **Definitie attribuutsoort** De minimaal tweedimensionale geometrische representatie van de omtrekken van een WOZ-OBJECT. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Status WOZ-object** 

**Naam attribuutsoort** 

Status WOZ-object 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.79 

> **XML-tag attribuutsoort** statusWozObject **Definitie attribuutsoort** 

De fase van de levenscyclus van een WOZOBJECT, waarin het betreffende WOZOBJECT zich bevindt. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Grondoppervlakte** 

> **Naam attribuutsoort** Grondoppervlakte 

> **Herkomst attribuutsoort** Gegevenswoordenboek WOZ (2002), overgenomen door KING 

> **Code attribuutsoort** 12.10 

> **XML-tag attribuutsoort** grondOppervlakte 

> **Definitie attribuutsoort** De oppervlakte grond in vierkante meters die behoort tot het WOZ-object. 

> **Herkomst definitie attribuutsoort** Gegevenswoordenboek WOZ (2002) 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Toelichting attribuutsoort** Zie het Gegevenswoordenboek WOZ 

> **Domein attribuutsoort** Formaat: N11 Waardenverzameling: 0 - 99999999999 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Gebruikscode** 

> **Naam attribuutsoort** Gebruikscode 

> **Herkomst attribuutsoort** Gegevenswoordenboek WOZ (2002), overgenomen door KING 

> **Code attribuutsoort** 12.20 

> **XML-tag attribuutsoort** gebruikscode 

## **Definitie attribuutsoort** 

Aanduiding van het feitelijk gebruik van een object zoals dat ten grondslag heeft gelegen aan de waardebepaling en voor zover relevant voor de afnemers, uitgedrukt in een code. 

> **Herkomst definitie attribuutsoort** Gegevenswoordenboek WOZ (2002) 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Toelichting attribuutsoort** Zie het Gegevenswoordenboek WOZ 

> **Domein attribuutsoort** Formaat: N2 Waardenverzameling: zie domeintabel in geg.wrdnboek WOZ 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1 - 1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Soort-object-code** 

**Naam attribuutsoort** 

Soort-object-code 

**Herkomst attribuutsoort Code attribuutsoort** 61.10 **XML-tag attribuutsoort** soortObjectCode 

Gegevenswoordenboek WOZ (2002), overgenomen door KING 

## **Definitie attribuutsoort** 

Aanduiding van het soort object ten behoeve van een correcte bepaling van de waarde. 

**Herkomst definitie attribuutsoort** 

Gegevenswoordenboek WOZ (2002) 

> **Datum opname attribuutsoort** 1 februari 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

Zie het Gegevenswoordenboek WOZ 

Formaat: N4 Waardenverzameling: overzicht soort-object op www.waarderingskamer.nl 

**Indicatie materiële historie** 

J 

**Indicatie formele historie Aanduiding gebeurtenis** 

N 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Vastgestelde waarde** 

> **Naam attribuutsoort** Vastgestelde waarde 

> **Herkomst attribuutsoort** KING 

> **Code attribuutsoort** 15.10 

> **XML-tag attribuutsoort** VastgesteldeWaarde.waarde 

> **Definitie attribuutsoort** Waarde van het WOZ-object op de laatst bekende peildatum zoals deze in het kader van de Wet WOZ is vastgesteld. 

> **Herkomst definitie attribuutsoort** KING o.b.v. BRWOZ 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat de waarde bevat op de meest actuele peildatum. 

> **Domein attribuutsoort** Formaat: N11 Waardenverzameling: gehele euro’s 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het attribuut wordt afgeleid van de Vastgestelde waarde op de laatst bekende Waardepeildatum in de aan het WOZ-object gerelateerde objecten WOZ-waarde. Indien het attribuut een waarde heeft dan heeft ook Waardepeildatum een waarde. 

## **Attribuutsoort Waardepeildatum** 

**Naam attribuutsoort** 

Waardepeildatum 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.20 

> **XML-tag attribuutsoort** vastgesteldeWaarde.waardepeildatum 

> **Definitie attribuutsoort** De laatstbekende datum waarnaar de waarde van het WOZ-object wordt bepaald. 

> **Herkomst definitie attribuutsoort** KING o.b.v. BRWOZ 

> **Datum opname attribuutsoort** 2 februari 2009 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat de laatstbekende peildatum bevat. 

> **Domein attribuutsoort** Formaat: Datum Waardenverzameling: alle datums op 1 januari van enig jaar 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het attribuut wordt afgeleid van de laatste bekende Waardepeildatum in de aan het WOZ-object gerelateerde objecten WOZ-waarde. Indien het attribuut een waarde heeft dan heeft ook Vastgestelde waarde een waarde. 

## **Attribuutsoort Datum begin geldigheid WOZ-object** 

**Naam attribuutsoort** 

Datum begin geldigheid WOZ-object 

> **Herkomst attribuutsoort** WOZ/KING 

> **Code attribuutsoort** 81.21 

> **XML-tag attribuutsoort** ingangsdatumObject 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort Domein attribuutsoort Indicatie materiële historie** 

Een aanduiding op welk tijdstip een object is ontstaan. 

1 februari 2008 

Formaat: OnvolledigeDatum Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Attribuutsoort Datum einde geldigheid WOZ-object** 

> **Naam attribuutsoort** Datum einde geldigheid WOZ-object 

> **Herkomst attribuutsoort** WOZ/KING 

> **Code attribuutsoort** 82.31 

> **XML-tag attribuutsoort** einddatumObject 

> **Definitie attribuutsoort** Een aanduiding op welk tijdstip een object is beëindigd. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

Een aanduiding op welk tijdstip een object is beëindigd. 

## **Relatiesoort WOZ-OBJECT heeft WOZ-belang** 

**Naam relatiesoort** 

WOZ-OBJECT heeft WOZ-BELANG 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.01b **Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 

De unieke aanduidingen van WOZ-BELANGen bij een WOZ-OBJECT. KING op basis van de catalogus BRWOZ 

30 november 2007 

**Toelichting relatiesoort** 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerd WOZ-object’ bij het objecttype WOZ-BELANG. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZBELANG betreft WOZ-OBJECT. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-OBJECT bevat KADASTRALE ONROERENDE ZAAK** 

> **Naam relatiesoort** WOZ-OBJECT bevat KADASTRALE ONROERENDE ZAAK 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 51.01a 

> **Definitie relatiesoort** De unieke aanduidingen van de KADASTRALE ONROERENDE ZAAKen opgenomen in de Basis Registratie Kadaster die geheel of gedeeltelijk deel uitmaken van het WOZ-OBJECT. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerde kadastrale objecten’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK behoort tot WOZ-OBJECT. Zie verder de toelichting in de BRWOZ. 

|**Indicatie materiële historie**|J|
|---|---|
|**Indicatie formele historie**|J|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-N|



**Indicatie authentiek** 

**Regels relatiesoort** 

Niet-authentiek landelijk basisgegeven. 

- 

## **Relatiesoort WOZ-OBJECT heeft WOZ-DEELOBJECT** 

> **Naam relatiesoort** WOZ-OBJECT heeft WOZ-DEELOBJECT 

> **Herkomst relatiesoort** WOZ/KING 

> **Code relatiesoort** 01.01b 

> **Definitie relatiesoort** De unieke aanduidingen van de WOZ-DEELOBJECTen waaruit het WOZ-OBJECT bestaat. 

> **Herkomst definitie relatiesoort** KING op basis van het WOZ-gegevenswoordenboek 

> **Datum opname relatiesoort** 30 november 2007 

> **Toelichting relatiesoort** In het WOZ-gegevenswoordenboek is dit gemodelleerd als het attribuutsoort ‘WOZ-objectnummer’ bij de entiteit ‘onderdelen voor onderbouwing taxatie WOZ-object’. In het RSGB wordt dit hergebruikt als relatiesoort. De relatie is de tegenhanger van WOZ-DEELOBJECT maakt deel uit van WOZ-OBJECT. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-OBJECT heeft WOZ-WAARDE** 

**Naam relatiesoort** 

> **Naam relatiesoort** WOZ-OBJECT heeft WOZ-WAARDE 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.01 

> **Definitie relatiesoort** De aan het WOZ-OBJECT gerelateerde WOZ-WAARDEn 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 2 februari 2009 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerd WOZ-object’ bij het objecttype Waarde. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZ-WAARDE hoort bij WOZ-OBJECT. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-OBJECT heeft aanduiding afgeleid van ADRESSEERBAAR OBJECT AANDUIDING** 

**Naam relatiesoort** 

> **Naam relatiesoort** WOZ-OBJECT heeft aanduiding afgeleid van ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.02a2 

> **Definitie relatiesoort** De ADRESSEERBAAR OBJECT AANDUIDING waarvan de locatie- 

De ADRESSEERBAAR OBJECT AANDUIDING waarvan de locatieaanduiding van het WOZ-object wordt afgeleid met behulp van het adres bij de ADRESSEERBAAR OBJECT AANDUIDING en de locatieomschrijving van het WOZ-object. 

## **Herkomst definitie relatiesoort** 

KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Adresseerbaar object voor aanduiding WOZ-object’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van ADRESSEERBAAR OBJECT AANDUIDING bepaalt nadere aanduiding van WOZ-OBJECT. 

Er is voor gekozen deze relatie te leggen naar de ADRESSEERBAAR OBJECT AANDUIDING zodat voor de WOZ-aanduiding ook gebruik gemaakt kan worden van de nevenadressen van benoemde objecten (naar analogie van het ingeschreven zijn van personen in de GBA op een nevenadres). 

Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** J 

**Indicatie formele historie** 

J 

## **Aanduiding gebeurtenis** 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **Relatiesoort WOZ-OBJECT ligt aan OPENBARE RUIMTE** 

**Naam relatiesoort Herkomst relatiesoort** BRWOZ/KING **Code relatiesoort** 11.01a **Definitie relatiesoort** 

WOZ-OBJECT ligt aan OPENBARE RUIMTE 

De unieke aanduiding van de OPENBARE RUIMTE waarvan de aanduiding van het WOZ-object wordt afgeleid met behulp van de locatieomschrijving. 

**Herkomst definitie relatiesoort** 

KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 30 november 2007 **Toelichting relatiesoort** 

In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Adresseerbaar object voor aanduiding WOZ-object’ bij het objecttype WOZ-OBJECT. In het RSGB wordt dit hergebruikt als relatiesoort. De relatie is de tegenhanger van OPENBARE RUIMTE heeft nabijgelegen WOZOBJECT. 

Zie verder de toelichting in de BRWOZ. 

**Indicatie materiële historie** 

J 

> **Indicatie formele historie** J 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **2.61. WOZ-waarde** 

## **Attribuutsoort Vastgestelde waarde** 

> **Naam attribuutsoort** Vastgestelde waarde 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.10 

> **XML-tag attribuutsoort** vastgesteldeWaarde 

> **Definitie attribuutsoort** Waarde van het WOZ-object zoals deze in het kader van de Wet WOZ is vastgesteld. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Waardepeildatum** 

> **Naam attribuutsoort** Waardepeildatum 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.20 

> **XML-tag attribuutsoort** waardepeildatum 

> **Definitie attribuutsoort** De datum waarnaar de waarde van het WOZ-object wordt bepaald. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

1-1 

**Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Toestandspeildatum** 

> **Naam attribuutsoort** Toestandspeildatum 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.25 

> **XML-tag attribuutsoort** toestandspeildatum 

> **Definitie attribuutsoort** Het in artikel 18 van de Wet WOZ bedoelde moment waarop de staat van de onroerende zaak in formele zin maatgevend is voor de waardebepaling. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Status beschikking** 

> **Naam attribuutsoort** StatusBeschikking 

> **Herkomst attribuutsoort** BR WOZ 

> **Code attribuutsoort** 15.99 

> **XML-tag attribuutsoort** beschikking.statusBeschikking 

**Definitie attribuutsoort** 

> **Definitie attribuutsoort** De fase van de levenscyclus van een WAARDE zoals deze tot uitdrukking komt in de juridische status van de WOZ-beschikking. 

> **Datum opname attribuutsoort** 1 februari 2008 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** 

Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Relatiesoort WOZ-WAARDE hoort bij WOZ-OBJECT** 

> **Naam relatiesoort** WOZ-WAARDE hoort bij WOZ-OBJECT 

> **Herkomst relatiesoort** BRWOZ/KING 

> **Code relatiesoort** 01.01 

> **Definitie relatiesoort** Het WOZ-OBJECT waaraan de WOZ-WAARDE gerelateerd is. 

> **Herkomst definitie relatiesoort** KING op basis van de catalogus BRWOZ 

> **Datum opname relatiesoort** 2 februari 2009 

> **Toelichting relatiesoort** In de BRWOZ is dit gemodelleerd als het attribuutsoort ‘Gerelateerd WOZ-object’ bij het objecttype Waarde. In het RSGB wordt dit hergebruikt als relatiesoort.  De relatie is de tegenhanger van WOZ-OBJECT heeft WOZ-WAARDE. Zie verder de toelichting in de BRWOZ. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie, Documentdatum 

> **Indicatie in onderzoek** Ja 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (N-1) 

> **Indicatie authentiek** Niet-authentiek landelijk basisgegeven. 

> **Regels relatiesoort** - 

## **2.62. Zakelijk recht** 

## **Attribuutsoort Kadaster identificatie zakelijk recht** 

**Naam attribuutsoort** 

Kadaster identificatie zakelijk recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Een door het Kadaster toegekende landelijk uniek nummer aan een recht. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Groepattribuutsoort Aandeel in recht** 

**Naam attribuutsoort** 

Aandeel in recht 

**Herkomst attribuutsoort** 

BRK 

## **Code attribuutsoort** 

**Definitie attribuutsoort Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

Het aandeel waarvoor de gerechtigde deelneemt in het recht. 

9 april 2007 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Teller 

Noemer 

**Indicatie materiële historie** 

Ja 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Ja 

Nee 

Ja: Documentidentificatie 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Attribuutsoort Teller** 

**Naam attribuutsoort** 

Teller 

**Herkomst attribuutsoort** 

BRK 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** AandeelRecht.teller **Definitie attribuutsoort** 

> **Datum opname attribuutsoort** 29 december 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

Het aantal delen waarvoor de gerechtigde deelneemt in het recht. 

Maakt deel uit van het groepattribuutsoort Aandeel in recht. Zie verder de toelichting in de BRK. Formaat: N8 Waardenverzameling: 1 ..n  waarbij n gelijk aan of kleiner is dan Noemer Nee 

## **Attribuutsoort Noemer** 

> **Naam attribuutsoort** Noemer 

> **Herkomst attribuutsoort** BRK 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** AandeelRecht.noemer 

> **Definitie attribuutsoort** Het totaal aantal delen waarvoor de gerechtigden deelnemen in het recht. 

> **Datum opname attribuutsoort** 29 december 2008 

> **Toelichting attribuutsoort** Maakt deel uit van het groepattribuutsoort Aandeel in recht. 

Maakt deel uit van het groepattribuutsoort Aandeel in recht. Zie verder de toelichting in de BRK. 

|**Domein attribuutsoort**|Formaat:|N8|
|---|---|---|
||Waardenverzameling:|1 .. 99.999.999|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Authentiek gegeven||



## **Attribuutsoort Ingangsdatum recht** 

> **Naam attribuutsoort** Ingangsdatum recht 

|**Herkomst attribuutsoort**|GFO BG||
|---|---|---|
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|ingangsdatumRecht||
|**Definitie attribuutsoort**|De datum waarop de|notarië|
||brondocument waar het zak||
|**Herkomst definitie attribuutsoort**|GFO BG||
|**Datum opname attribuutsoort**|1 mei 2008||
|**Toelichting attribuutsoort**|De attribuutsoort komt in de||
||sluiten op de huidige wijze v||
|**Domein attribuutsoort**|Formaat:|Onv|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



De datum waarop de notariële akte is ingeschreven of anderszins een brondocument waar het zakelijk recht op berust is ingeschreven. 

De attribuutsoort komt in de BRK niet voor maar is toegevoegd om aan te sluiten op de huidige wijze van gegevenslevering door het Kadaster. Formaat: 

OnvolledigeDatum 

## **Attribuutsoort Einddatum recht** 

> **Naam attribuutsoort** Einddatum recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumRecht 

> **Definitie attribuutsoort** De laatste dag waarop het recht volgens het brondocument, op grond waarvan het recht is opgevoerd, nog van toepassing zal zijn. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Indicatie betrokken in splitsing** 

|**Naam attribuutsoort**|Indicatie betrokken in splitsing|
|---|---|
|**Herkomst attribuutsoort**|BRK|
|**Code attribuutsoort**||
|**XML-tag attribuutsoort**|betrokkenInSplitsing|
|**Definitie attribuutsoort**|Een aanduiding die aangeeft dat het betrokken recht al dan niet is|
||betrokken bij een splitsing in appartementsrechten.|
|**Datum opname attribuutsoort**|9 april 2007|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Nee|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Relatiesoort ZAKELIJK RECHT is van AARD VERKREGEN RECHT** 

|**Naam relatiesoort**|ZAKELIJK RECHT is van AARD VERKREGEN RECHT|
|---|---|
|**Herkomst relatiesoort**|KING/BRK|
|**Code relatiesoort**||
|**Definitie relatiesoort**|Een verwijzing naar de AARD VERKREGEN RECHT dat van toepassing|
||is op het  ZAKELIJK RECHT|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|Het betreft het hergebruik als relatiesoort van het attribuutsoort|
||‘Aanduiding aard verkregen recht’ bij het objecttype ZAKELIJK RECHT in|
||de BRK.|
||Zie verder de toelichting in de BRK bij genoemd attribuutsoort.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentidentificatie|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Relatiesoort ZAKELIJK RECHT is van AARD RECHT VERKORT** 

> **Naam relatiesoort** ZAKELIJK RECHT is van AARD RECHT VERKORT 

> **Herkomst relatiesoort** KING/BRK **Code relatiesoort** 

> **Definitie relatiesoort** Een verwijzing naar de AARD RECHT VERKORT dat van toepassing is op het  ZAKELIJK RECHT 

> **Datum opname relatiesoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘Aanduiding aard recht verkort’ bij het objecttype ZAKELIJK RECHT in de BRK. Zie verder de toelichting in de BRK bij genoemd attribuutsoort. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

## **Relatiesoort ZAKELIJK RECHT betreft KADASTRALE ONROERENDE ZAAK** 

|**Naam relatiesoort**|ZAKELIJK RECHT betreft KADASTRALE ONROERENDE ZAAK|
|---|---|
|**Herkomst relatiesoort**|BRK|
|**Code relatiesoort**||
|**Definitie relatiesoort**|Een verwijzing naar de KADASTRALE ONROERENDE ZAAK waarop het|
||ZAKELIJK RECHT betrekking heeft.|
|**Datum opname relatiesoort**|9 april 2007|
|**Toelichting relatiesoort**|Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht .|
||betrokken onroerende zaak’ bij het objecttype RECHT in de BRK. De|
||relatie is de tegenhanger van KADASTRALE ONROERENDE ZAAK heeft|
||één of meer ZAKELIJK RECHT.|
||Zie verder de toelichting in de BRK bij genoemd attribuutsoort.|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Ja|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**|Ja: Documentidentificatie|
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1-1|
|**Indicatie authentiek**|Authentiek gegeven|



## **Relatiesoort ZAKELIJK RECHT heeft als gerechtigde RECHTSPERSOON** 

|**Naam relatiesoort**|ZAKELIJK RECHT heeft als gerechtigde RECHTSPERSOON|
|---|---|
|**Herkomst relatiesoort**|BRK|
|**Code relatiesoort**||
|**Definitie relatiesoort**|Een verwijzing naar een RECHTSPERSOON, ten name waarvan het|
||ZAKELIJK RECHT is gesteld.|
|**Toelichting relatiesoort**|Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht .|
||gerechtigde’ bij het objecttype RECHT in de BRK. De relatie is de|
||tegenhanger van RECHTSPERSOON is gerechtigde van ZAKELIJK|
||RECHT.|
||Zie verder de toelichting in de BRK bij genoemd attribuutsoort.|
|**Indicatie materiële historie**|Nee|



**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Authentiek gegeven 

Ja: Documentidentificatie 

## **Relatiesoort ZAKELIJK RECHT heeft ZAKELIJK RECHT AANTEKENINGen** 

**Naam relatiesoort** 

ZAKELIJK RECHT heeft ZAKELIJK RECHT AANTEKENINGen 

**Herkomst relatiesoort** 

KING op basis van BRK 

**Code relatiesoort** 

**Definitie relatiesoort** 

De ZAKELIJK RECHT AANTEKENINGen die geplaatst zijn bij het . ZAKELIJK RECHT 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 29 december 2008 

**Toelichting relatiesoort** 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘zakelijk recht . aantekening’ bij het objecttype ZAKELIJK RECHT in de BRK. De relatie is de tegenhanger van ZAKELIJK RECHT AANTEKENING behoort bij ZAKELIJK RECHT. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven **Regels relatiesoort** 

## **2.63. Zakelijk recht aantekening** 

## **Attribuutsoort Kadaster identificatie aantekening recht** 

> **Naam attribuutsoort** Kadaster identificatie aantekening recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** identificatie 

> **Definitie attribuutsoort** Een door het Kadaster toegekend landelijk uniek nummer aan een aantekening bij een ZAKELIJK RECHT. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Aard aantekening recht** 

**Naam attribuutsoort** 

Aard aantekening recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** aard 

**Definitie attribuutsoort** 

Een aanduiding die aangeeft van welke soort de aantekening bij het recht is. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

1-1 

**Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Beschrijving aantekening recht** 

> **Naam attribuutsoort** Beschrijving aantekening recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** omschrijving 

> **Definitie attribuutsoort** Een tekstuele toelichting inzake de aantekening bij het recht. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Attribuutsoort Begindatum aantekening recht** 

**Naam attribuutsoort** 

Begindatum aantekening recht 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

ingangsdatumObject 

Deze begindatum geeft aan wanneer een bepaalde aantekening bij een recht rechtsgeldig geworden is. 

**Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

2 februari 2009 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

De attribuutsoort komt niet voor in de BRK. De waarde wordt afgeleid van de datum ondertekening van het stuk waarin het feit genoemd is waarop de aantekening is gebaseerd. Formaat: Onvolledige datum Waardenverzameling: geldige, eventueel onvolledige datums Nee 

## **Indicatie formele historie** 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

## **Attribuutsoort Einddatum aantekening recht** 

**Naam attribuutsoort** 

Einddatum aantekening recht 

> **Herkomst attribuutsoort** BRK **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort** 

Deze einddatum geeft aan wanneer een bepaalde aantekening bij een recht niet langer meer rechtsgeldig is 1 mei 2008 

> **Datum opname attribuutsoort** 1 mei 2008 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Relatiesoort ZAKELIJK RECHT AANTEKENING behoort bij ZAKELIJK RECHT** 

**Naam relatiesoort** 

ZAKELIJK RECHT AANTEKENING behoort bij ZAKELIJK RECHT 

> **Herkomst relatiesoort** KING op basis van BRK **Code relatiesoort** 

> **Definitie relatiesoort** Het ZAKELIJK RECHT waarbij de AANTEKENING geplaatst is. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 november 2008 

**Toelichting relatiesoort** 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘zakelijk recht . aantekening’ bij het objecttype ZAKELIJK RECHT in de BRK. De relatie is de tegenhanger van ZAKELIJK RECHT heeft ZAKELIJK RECHT AANTEKENING en. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels relatiesoort** 

## **Relatiesoort ZAKELIJK RECHT AANTEKENING heeft betrokken RECHTSPERSOON** 

> **Naam relatiesoort** ZAKELIJK RECHT AANTEKENING heeft betrokken RECHTSPERSOON 

> **Herkomst relatiesoort** BRK **Code relatiesoort** 

> **Definitie relatiesoort** Een uniek nummer van de eventueel betrokken RECHTSPERSOON bij deze aantekening. 

> **Datum opname attribuutsoort** 9 april 2007 

> **Toelichting relatiesoort** Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht . 

Het betreft het hergebruik als relatiesoort van het attribuutsoort ‘recht . aantekening recht . betrokken persoon’ bij het objecttype RECHT in de BRK. De relatie is de tegenhanger van RECHTSPERSOON is betrokken bij ZAKELIJK RECHT AANTEKENING. Zie verder de toelichting in de BRK. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Ja: Documentidentificatie 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

## **Bijlage 1: Metagegevens** 

In deze bijlage specificeren we de metagegevens die het gevolg zijn van de declaraties van attribuutsoorten betreffende materiele en formele historie, aanduiding gebeurtenis, aanduiding brondocument, indicatie in onderzoek en aanduiding strijdigheid/nietigheid. aanzet 

## **Metagegevens betreffende materiële historie** 

## **Attribuutsoort Begindatum geldigheid gegevens** 

|**Naam attribuutsoort**|**Begindatum geldigheid gegevens**|**Begindatum geldigheid gegevens**|
|---|---|---|
|**Herkomst attribuutsoort**|KING||
|**Code attribuutsoort**|||
|**XML-tag attribuutsoort**|tijdvakGeldigheid.beginGeldigheid||
|**Definitie attribuutsoort**|De begindatum van een periode waarin een of||
||worden bijgehouden|over de entiteit een wijzigin|
|**Herkomst definitie attribuutsoort**|KING||
|**Datum opname attribuutsoort**|01-09-08||
|**Toelichting attribuutsoort**|betreft de materiele historie||
|**Domein attribuutsoort**|Formaat:|Datum/tijd (JJJJMMDD)|
||Waardeverzameling:|<br>Alle (on)geldige datums|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Ntb||
|**Regels attribuutsoort**|-||



De begindatum van een periode waarin een of meer gegevens die worden bijgehouden over de entiteit een wijziging hebben ondergaan. KING 

## **Attribuutsoort Einddatum geldigheid gegevens** 

## **Naam attribuutsoort** 

## **Einddatum geldigheid gegevens** 

> **Herkomst attribuutsoort** KING **Code attribuutsoort XML-tag attribuutsoort** 

tijdvakGeldigheid.eindeGeldigheid 

## **Definitie attribuutsoort** 

De einddatum van een periode waarin een of meer gegevens die worden bijgehouden over de entiteit een wijziging hebben ondergaan. KING 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

01-09-08 

|**Toelichting attribuutsoort**|betreft de materiele historie|betreft de materiele historie|
|---|---|---|
|**Domein attribuutsoort**|Formaat:|Datum/tijd (JJJJMMDD)|
||Waardeverzameling:|Alle (on)geldige datums|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Ntb||
|**Regels attribuutsoort**|-||



## **Metagegevens betreffende formele historie** 

## **Attribuutsoort Tijdstip registratie gegevens** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

## **Tijdstip registratie gegevens** 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

tijdstipRegistratie 

De datum en tijd waarop één of meer gegevens van de entiteit gelijktijdig zijn opgenomen in de registratie. 

KING 

> **Datum opname attribuutsoort** 01-09-08 **Toelichting attribuutsoort Domein attribuutsoort** 

betreft de formele historie 

Formaat: Datum/tijd (JJJJMMDDUUMMSS) Waardeverzameling: Alle geldige datums en tijdstippen gelegen op of voor de huidige datum en tijd 1-1 

**Indicatie kardinaliteit Indicatie authentiek** 

ntb 

**Regels attribuutsoort** 

- 

## **Metagegevens betreffende gebeurtenissen** 

## **Attribuutsoort metagegeven nog niet gedefinieerd en toegepast** 

**Naam attribuutsoort** 

**metagegeven nog niet gedefinieerd en toegepast** 

**Herkomst attribuutsoort** 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort Domein attribuutsoort** 

**Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

## **Metagegevens betreffende brondocumenten** 

## **Attribuutsoort Documentidentificatie** 

**Naam attribuutsoort** 

## **Documentidentificatie** 

**Herkomst attribuutsoort** 

BAG, GBA, BRK, BRWOZ 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## Brondocument.identificatie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een entiteit heeft plaatsgevonden 

## KING 

## 1-7-2008 

## **Toelichting attribuutsoort** 

De wijze waarop documenten geïdentificeerd worden en de naam die aan deze identificatie gegeven wordt, verschilt per basisregistratie: 

- BAG:  Documentnummer 

- BRK: Kadaster identificatie stuk; 

- GBA: Aktenummer (81.20) 

- NHR: n.v.t. 

- BRWOZ: Documentnummer 

**Domein attribuutsoort** 

**Indicatie kardinaliteit Indicatie authentiek** 

Formaat: AN20 Waardeverzameling: Alle bestaande alfanumerieke tekens 1-1 

Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Documentdatum** 

**Naam attribuutsoort** 

## **Documentdatum** 

**Herkomst attribuutsoort** 

BAG, GBA, BRWOZ 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

brondocument.datum 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

De datum waarop het brondocument is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van de entiteit heeft plaatsgevonden 

KING 

01-07-08 

**Toelichting attribuutsoort** 

De naam die aan deze attribuutsoort gegeven wordt, verschilt per basisregistratie: 

- BAG: Documentdatum 

- - BRK: n.v.t.; 

- - GBA: Documentdatum (82.20) 

- - NHR: n.v.t. - BRWOZ: Documentdatum 

- **Domein attribuutsoort** Formaat: Datum/tijd (JJJJMMDD) Waardeverzameling: Alle geldige datums en tijdstippen 

- **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Documentomschrijving** 

> **Naam attribuutsoort Documentomschrijving** 

**Herkomst attribuutsoort** 

GBA 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** brondocument.omschrijving **Definitie attribuutsoort** 

Beschrijving van het document waaraan de gegevens zijn ontleend of waaruit de gegevens zijn afgeleid 

> **Herkomst definitie attribuutsoort** GBA 

> **Datum opname attribuutsoort** 01-07-08 

**Toelichting attribuutsoort** 

De attribuutsoort komt alleen voor in de GBA onder de naam ‘Beschrijving document’ (82.30). 

**Domein attribuutsoort** 

Formaat: AN40 Waardeverzameling: Alle bestaande alfanumerieke tekens 0-1 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort AkteGemeente** 

> **Naam attribuutsoort AkteGemeente** 

> **Herkomst attribuutsoort** GBA **Code attribuutsoort** 

> **XML-tag attribuutsoort** brondocument.akteGemeente **Definitie attribuutsoort** 

De code uit de gemeentetabel die aangeeft in welke gemeente de akte in de registers van de burgerlijke stand in Nederland is opgenomen. 

## **Herkomst definitie attribuutsoort** 

## GBA 

> **Datum opname attribuutsoort** 30-3-2009 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** De attribuutsoort komt alleen voor in de GBA onder de naam ‘Registergemeente akte (81.10). 

> **Domein attribuutsoort** Formaat: N4 Waardeverzameling: Een codering conform de regels van de GBAgemeententabel 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Documentgemeente** 

**Naam attribuutsoort Herkomst attribuutsoort** 

## **Documentgemeente** 

## GBA 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** brondocument.gemeente **Definitie attribuutsoort** 

De code uit de gemeentetabel die aangeeft in welke gemeente de ontlening aan of de afleiding uit het document heeft plaatsgevonden. 9 april 2007 

**Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

De attribuutsoort komt alleen voor in de GBA onder de naam ‘Gemeente document (82.10). 

**Domein attribuutsoort** 

Formaat: N4 Waardeverzameling: Een codering conform de regels van de GBAgemeententabel 0-1 

**Indicatie kardinaliteit** 

**Indicatie authentiek** 

Niet authentiek landelijk basisgegeven 

## **Regels attribuutsoort** 

## **Metagegevens betreffende ‘in onderzoek’** 

## **Attribuutsoort Aanduiding gegevens in onderzoek** 

|**Naam attribuutsoort**|Aanduiding gegevens|in onderzoek|
|---|---|---|
|**Herkomst attribuutsoort**|GBA, BAG,BRK, NHR||
|**Code attribuutsoort**|||
|**Definitie attribuutsoort**|Een aanduiding waarmee wordt aangegeven dat een onderzoek wordt||
||uitgevoerd naar de juistheid van een of meerdere gegevens van het||
||betreffende object||
|**Datum opname attribuutsoort**|9 april 2007||
|**Toelichting attribuutsoort**|||
|**Domein attribuutsoort**|Formaat:|AN1|
||Waardenverzameling:|J, N|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Ja||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||
|**Indicatie authentiek**|Niet authentiek landelijk basisgegeven||



## **Metagegevens betreffende strijdigheid / nietigheid** 

## **Attribuutsoort Aanduiding strijdigheid / nietigheid** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Aanduiding strijdigheid / nietigheid 

GBA 

**Code attribuutsoort** 

**Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

De aanduiding dat één of meer gegevens van het object  strijdig met de openbare orde dan wel nietig zijn 

9 april 2007 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Formaat: AN1 Waardenverzameling: O (= onjuist) S (= strijdig met de openbare orde) 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Niet authentiek landelijk basisgegeven 

**==> picture [435 x 701] intentionally omitted <==**

