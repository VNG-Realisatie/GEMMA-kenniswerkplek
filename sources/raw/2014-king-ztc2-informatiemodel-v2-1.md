---
title: "GEMMA Zaaktypecatalogus 2 (ZTC2) — Informatiemodel v2.1"
source: "KING / VNG Realisatie"
author: "KING (Arjan Kloosterboer, Mark van den Broek, Remko de Haas)"
published: 2014-07-01
created: 2026-06-18
description: "Informatiemodel voor zaaktypecatalogi: definieert CATALOGUS, ZAAKTYPE, STATUSTYPE, RESULTAATTYPE, ROLTYPE, EIGENSCHAP, INFORMATIEOBJECTTYPE, BESLUITTYPE en ZAAKOBJECTTYPE als configuratielaag bovenop het RGBZ."
tags:
  - "Dienstverlening"
  - "Standaarden"
  - "GEMMA"
---

**==> picture [171 x 86] intentionally omitted <==**

# **GEMMA ZAAKTYPECATALOGUS 2 (VERSIE 2.1)** 

# **Informatiemodel** 

**==> picture [489 x 428] intentionally omitted <==**

**==> picture [103 x 52] intentionally omitted <==**

## **VERSIE** 

|**Versie**<br>**Datum**|**Versie**<br>**Datum**|**Auteur(s)**<br>**Opmerkingen/veranderingen**|**Auteur(s)**<br>**Opmerkingen/veranderingen**||
|---|---|---|---|---|
|2.0|6-3-2013|Mark van den Broek<br>/ Arjan Kloosterboer<br>/ Remko de Haas|Versie 2 is een doorontwikkeling en –<br>vooral – uitbreiding op het – beperkte en<br>niet gedocumenteerde – informatiemodel<br>van versie 1.||
|2.1|1-7-2014|Arjan Kloosterboer|Materiële historie, desbetreffende<br>attribuutregels en, waar nog niet<br>aanwezig, Datum begin geldigheid en<br>Datum einde geldigheid toegevoegd zodat<br>ook versies van zaaktypen correct<br>gemodelleerd zijn.<br>De wijze van het specificeren van<br>zaaktypespecifieke eigenschappen<br>gewijzigd zodanig dat ook verwezen kan<br>worden naar een informatiemodel en een<br>XML-schema.<br>De term ‘document’ vervangen door<br>‘informatieobject’.<br>Mogelijk gemaakt dat in<br>uitzonderingsgevallen het archiefregime<br>van informatieobjecten van een ZAAK-<br>INFORMATIEOBJECTTYPE afwijkt van het<br>archiefregime van het ZAAKTYPE cq.<br>zaakdossiers van zaken van dat zaaktype.<br>Toelichting bij ZAAKTYPE aangescherpt<br>v.w.b. afbakening van een zaaktype.<br>Toelichtingen bij zaaktype-zaaktype-<br>relaties aangescherpt en domeinwaarden<br>van ‘Aard relatie’geharmoniseerd met<br>RGBZ.<br>Referentielijst ‘Informatieobjecttype-<br>omschrijving generiek’ toegevoegd.||



Zie bijlage 1 voor een specificatie per objecttype van de wijzigingen in de meest recente versie. 

2 

**==> picture [103 x 52] intentionally omitted <==**

## **Inhoud** 

|**1**|**Inleiding**|**Inleiding**|**4**|
|---|---|---|---|
|**2**|**Model op hoofdlijnen**||**5**|
|**3**|**Objecttypen**||**9**|
||3.1|Objecttype BESLUITTYPE|10|
||3.2|Objecttype CATALOGUS|11|
||3.3|Objecttype EIGENSCHAP|12|
||3.4|Objecttype INFORMATIEOBJECTTYPE|15|
||3.5|Objecttype RESULTAATTYPE|16|
||3.6|Objecttype ROLTYPE|19|
||3.7|Objecttype STATUSTYPE|20|
||3.8|Objecttype ZAAKOBJECTTYPE|21|
||3.9|Objecttype ZAAKTYPE|23|
|**4**|**Relatieklassen**||**27**|
||4.1|Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE|27|
||4.2|Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE ARCHIEFREGIME|28|
||4.3|Relatieklasse ZAAKTYPENRELATIE|29|
|**5**|**Referentielijst**||**30**|
||5.1|Referentielijst INFORMATIEOBJECTTYPE-OMSCHRIJVING GENERIEK|30|
|**6**|**Attribuut- en relatiesoorten**||**32**|
||6.1|Objecttypen|36|
||6.2|Relatieklassen|113|
||6.3|Referentielijst|118|
|**Bijlage**||**1: Wijzigingen ten opzichte van versie 2.0**|**121**|



3 

**1 Inleiding** 

**==> picture [103 x 52] intentionally omitted <==**

Zaakgericht werken wordt als een belangrijk thema gezien om meer grip te krijgen op processen, zowel voor dienstverlening als interne doelen, en de daarvoor relevante informatievoorziening. KING ondersteunt gemeenten bij deze ontwikkeling door middel van de GEMeentelijke Model Architectuur (GEMMA). De GEMMAonderdelen geven kaders en richting voor het inrichten van de gemeentelijke bedrijfsvoering  en informatiehuishouding. Voor zaak- en procesgericht werken biedt KING o.a. de GEMMA Zaaktypecatalogus. 

De visie van KING op de Zaaktypecatalogus, de uitgangspunten, het gebruik, de opzet, de inhoud en het beheer, beschrijft zij in het document ‘GEMMA Zaaktypecatalogus 2’. Een zaaktypecatalogus bevat de zaaktypen die onderscheiden worden binnen het domein waarop die catalogus gericht is. De ‘ZTC2’ geeft duidelijkheid over de kenmerken waarmee een zaaktype beschreven wordt. Welke kenmerken dit zijn, wat ze betekenen en hoe ze zich tot elkaar verhouden, is uitgewerkt in het Informatiemodel ZTC dat voor u ligt. Hiermee specificeren we de structuur van een catalogus met zaaktypen. 

4 

**==> picture [103 x 52] intentionally omitted <==**

## **2 Model op hoofdlijnen** 

Aan de hand van onderstaande afbeelding lichten we de informatie-structuur van de GEMMA Zaaktypecatalogus 2 op hoofdlijnen toe. De details vermelden we in de volgende hoofdstukken. Aan het einde van dit hoofdstuk is het model met attributen opgenomen. 

**==> picture [455 x 362] intentionally omitted <==**

Bij het ontwerp van de GEMMA Zaaktypecatalogus (ZTC) 2 is vooral gefocust op maximale aansluiting van de ZTC op het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) en op het definiëren van die extra elementen die geen plaats - horen te - hebben in RGBZ, maar wel van belang zijn voor de besturing van zaken en daarmee dicht aanliggen tegen de wijze waarop systemen zaakgericht werken ondersteunen. Ten opzichte van versie 1 is de zaaktypecatalogus dus ontwikkeld in de ‘breedte’: de ZTC2 bevat veel meer objecttypen en attributen dan versie 1. 

KING heeft onderkend dat er niet één landelijke zaaktypecatalogus kan bestaan waarin alle zaaktypen van alle overheidsorganisaties volledig uitgewerkt een plaats hebben of krijgen. Als gevolg van de ‘verbreding’ in versie 2 zijn er tal van elementen in de ZTC opgenomen die uitsluitend lokaal kunnen worden ingevuld. Het gevolg is dat er niet één, maar vele zaaktypecatalogi zullen ontstaan. 

Om aan die ontwikkeling tegemoet te komen, voorziet de ZTC2 in het objecttype CATALOGUS. Daarmee worden alle ZAAKTYPEN en daaraan gerelateerde objecten en attributen voor een specifiek domein gebundeld tot één geheel. Het domein waarop zo’n 

5 

**==> picture [103 x 52] intentionally omitted <==**

catalogus van toepassing is, kan sterk uiteenlopen. Er zullen catalogi zijn die met de ZAAKTYPEn van één overheidsorganisatie worden gevuld, maar ook catalogi worden ontwikkeld die veel breder reiken; denk aan een sectorale catalogus voor alle overheidsorganisaties die binnen een sector actief zijn of een ketencatalogus voor ketenpartners. Het informatiemodel van de ZTC2 voorziet daarom in een unieke identificatie van een CATALOGUS: de combinatie van het RSIN van de ‘eigenaar’ van de CATALOGUS en het Domein waarop de CATALOGUS van toepassing is. 

In één CATALOGUS worden op het hoogste niveau verschillende objecttypen onderscheiden. Het belangrijkst is natuurlijk het objecttype ZAAKTYPE; een zaaktypecatalogus definieert immers de verschillende ZAAKTYPEn die relevant zijn voor het domein waarop de CATALOGUS betrekking heeft en bepaalt zo de gegevens die worden vastgelegd van zaken van het ZAAKTYPE. Historie is in het model zodanig opgenomen dat versies van zaaktypen onderscheiden kunnen worden, met telkens bij elke versie van een zaaktype alle daarbij behorende waarden van het zaaktype en van de ‘onderliggende’ objecttypen zoals statustypen, informatieobjecttypen en resultaattypen. 

De CATALOGUS bevat, op hetzelfde niveau als het ZAAKTYPE, de objecttypen BESLUITTYPE  en INFORMATIEOBJECTTYPE (voorheen Documenttype). Deze objecttypen zijn zo te gebruiken in alle ZAAKTYPEn die in de CATALOGUS worden gedefinieerd. Omdat de waardenlijsten van deze objecttypen fors kunnen zijn, kan in elk ZAAKTYPE worden geconfigureerd welke BESLUITTYPEn en INFORMATIEOBJECTTYPEn relevant zijn voor zaken van het ZAAKTYPE. De objecttypen BESLUITTYPE en 

INFORMATIEOBJECTTYPE zijn - met kleine aanpassingen en aanvullingen - overgenomen uit het RGBZ. 

Binnen elk ZAAKTYPE zijn de objecttypen STATUSTYPE, ZAAKOBJECTTYPE, ROLTYPE, EIGENSCHAP en RESULTAATTYPE gemodelleerd. 

Het STATUSTYPE is overgenomen uit het RGBZ en wordt in de ZTC eveneens gemodelleerd binnen een ZAAKTYPE . De reden hiervoor is dat de herbruikbaarheid van STATUSTYPEn beperkt is; er is weliswaar een aantal generieke STATUSTYPEn denkbaar (bijvoorbeeld ‘Ontvangen’ of ‘Afgehandeld’), maar in een groot aantal gevallen krijgt een STATUSTYPE en de daarbij horende attributen een ZAAKTYPE-specifieke invulling. 

Het ZAAKOBJECTTYPE is een objecttype dat noch in het RGBZ, noch in de ZTC 1 voorkomt. Het objecttype is in de ZTC2 geïntroduceerd om vooraf - per ZAAKTYPE - de relatie tussen een ZAAK en de basis- en kerngegevens die relevant zijn voor ZAAKen van dat ZAAKTYPE inzichtelijk te maken en - belangrijker - registratie daarvan tijdens de behandeling van een ZAAK te kunnen afdwingen. Denk aan het niet kunnen zetten van een STATUS als niet eerst een relevant basis- of kerngegeven via ZAAKOBJECT is gerelateerd aan de zaak. 

Ook het ROLTYPE is een objecttype dat niet in het RGBZ of de ZTC 1 voorkomt. Het voorziet in de behoefte om per ZAAKTYPE een duidelijke typering te kunnen geven aan de BETROKKENEn die in een - door het ROLTYPE - bepaalde hoedanigheid ‘acteren’ in zaken van een bepaald ZAAKTYPE. Het ROLTYPE beoogt zo vooral ondersteuning te bieden aan het - via het ROLTYPE - onderscheiden van groepen BETROKKENEn en daarvoor specifieke functionaliteit aan te bieden. Denk bijvoorbeeld aan het instellen van autorisaties voor bepaalde ROLTYPEn, of het informeren van BETROKKENEn in één of meer ROLTYPEn over de voortgang van de behandeling van zaken van een bepaald ZAAKTYPE. 

6 

**==> picture [103 x 52] intentionally omitted <==**

De ZTC2 modelleert het objecttype EIGENSCHAP als objecttype bij een ZAAKTYPE. Een EIGENSCHAP is een voor het betreffende ZAAKTYPE specifiek gegeven dat voor de - besturing van de - behandeling van een zaak van dat ZAAKTYPE van groot belang is. Denk aan de EIGENSCHAP ‘Datum evenement’: dit gegeven is relevant voor de behandelaar van aanvragen voor een evenementenvergunning, bijvoorbeeld om evenementen te sorteren op datum en aanvragen voor evenement die de komende weken zijn gepland eerder te behandelen dan evenementen die pas over enkele maanden zullen plaatsvinden. 

Verder kent de ZTC2 bij een ZAAKTYPE het RESULTAATTYPE: een objecttype dat niet in het RGBZ voorkomt, maar wel al in de ZTC 1 werd geïntroduceerd. Het RGBZ kent overigens bij een zaak wel het attribuut Resultaatomschrijving  dat bij een fysieke zaak een waarde heeft die ontleend wordt aan de RESULTAATTYPEn bij het ZAAKTYPE van die zaak. Het is in de ZTC2 in meer detail gemodelleerd met het doel betere ondersteuning te bieden aan het correct en integraal kunnen archiveren van zaken van een bepaald ZAAKTYPE en daarbij geautomatiseerd te bepalen wat de datum is waarop een zaakdossier vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden. In uitzonderingsgevallen wijkt het archiefregime van een individueel informatieobject in een zaakdossier af van het archiefregime van de zaak als geheel. In het correct archiveren van dergelijke gevallen voorziet de relatie van RESULTAATTYPE naar ZAAKINFORMATIEOBJECT-TYPE. 

Dan resten nog de relaties tussen ZAAKTYPEn onderling. In de ZTC2 worden twee relatiesoorten onderscheiden: de relatie tussen een ZAAKTYPE en deel-ZAAKTYPEn en de relatie tussen (om andere redenen) gerelateerde ZAAKTYPEN. De tweede relatiesoort betreft de relatie tussen een ZAAKTYPE en de ZAAKTYPEn die een noodzakelijk vervolg zijn op het eerstgenoemde ZAAKTYPE, de relatie tussen een ZAAKTYPE en de ZAAKTYPEn die een bijdrage leveren aan de behandeling van het eerstgenoemde ZAAKTYPE en de relatie tussen een ZAAKTYPE en andere ZAAKTYPen waarop het eerstgenoemde ZAAKTYPE betrekking heeft. Al deze relaties maken het mogelijk om ZAAKTYPEn zuiver af te bakenen, overeenkomstig bedrijfsprocessen, en grip te behouden op samenhang en samenwerking tussen bedrijfsprocessen, binnen de eigen organisaties en tussen organisaties, teneinde een passend antwoord te verkrijgen op de aanleiding voor een zaak. 

7 

**==> picture [726 x 523] intentionally omitted <==**

**----- Start of picture text -----**<br>
8<br>**----- End of picture text -----**<br>


**==> picture [103 x 52] intentionally omitted <==**

## **3 Objecttypen** 

In dit hoofdstuk specificeren we de onderscheiden objecttypen naar de volgende aspecten. 

**Naam** De naam van het objecttype. **Mnemonic** De in StUF-BG gehanteerde afkorting voor de naam van het objecttype. Objecttypen met een mnemonic tussen (haakjes) worden (nog) niet als zelfstandige entiteit in StUF-BG gebruikt. **Herkomst** De basisregistratie of het informatiemodel waaraan het objecttype is ontleend dan wel ‘KING’ indien het een door KING Gemeenten toegevoegd objecttype betreft. **Definitie** De beschrijving van de betekenis van het objecttype. **Herkomst definitie** De basisregistratie of het informatiemodel waaruit de definitie is overgenomen dan wel een aanduiding die aangeeft uit welke bronnen de defintie is samengesteld. **Datum opname** De datum waarop het objecttype is opgenomen inhet informatiemodel. **Unieke aanduiding** De wijze waarop objecten (van dit type) uniek worden aangeduid. **Populatie** De beschrijving van de exemplaren van het gedefinieerde objecttype binnen het domein waarop het informatiemodel betrekking heeft. **Kwaliteitsbegrip** De waarborgen voor de juistheid van een object van het desbetreffende type. **Overzicht attributen** Hier worden de attribuutsoorten gespecificeerd die behoren tot het desbetreffende objecttype. Attribuutsoorten kunnen deel uit maken van een zgn. attribuutgroep. De tot een dergelijke groep behorende attribuutsoorten zijn inspringend vermeld. Van elk attribuutsoort wordt de naam, definitie, formaat en kardinaliteit vermeld. Zie hiervoor de uitleg aan het begin van hoofdstuk **Fout! Verwijzingsbron niet gevonden. Fout! Verwijzingsbron niet gevonden.** . 

**Overzicht relaties** Hier worden de relaties gespecificeerd die het desbetreffende objecttype heeft met andere objecttypen. Van elke relatiesoort wordt de relatienaam met kardinaliteiten en de definitie getoond. De relatiesoorten worden nader gespecificeerd in hoofdstuk **Fout! Verwijzingsbron niet gevonden. Fout! Verwijzingsbron niet gevonden.** . 

**Toelichting objecttype** Een inhoudelijke toelichting op het objecttype als geheel. 

9 

**==> picture [103 x 52] intentionally omitted <==**

## **3.1 Objecttype BESLUITTYPE** 

**Naam** BESLUITTYPE **Mnemonic** BST **Herkomst** KING **Definitie** Generieke aanduiding van de aard van een besluit **Herkomst definitie** KING **Datum opname** 1 juni 2008 **Unieke aanduiding** Unieke aanduiding van CATALOGUS in combinatie met Besluittypeomschrijving **Populatie** Alle besluittypen van de besluiten die het resultaat kunnen zijn van het zaakgericht werken van de behandelende organisatie(s). **Kwaliteitsbegrip** 

|**Overzicht attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Besluittype-omschrijving|Omschrijving van de aard van BESLUITen van|AN80|0 - 1|
||het BESLUITTYPE.|||
|Besluittype-omschrijving|Algemeen gehanteerde omschrijving van de|AN80|0 - 1|
|generiek|aard van BESLUITen van het BESLUITTYPE|||
|Besluitcategorie|Typering van de aard van BESLUITen van het|AN40|0 - 1|
||BESLUITTYPE.|||
|Reactietermijn|Het aantal dagen, gerekend vanaf de|N3|1 - 1|
||verzend- of publicatiedatum, waarbinnen|||
||verweer tegen een besluit van het besluittype|||
||mogelijk is.|||
|Publicatie-indicatie|Aanduiding of BESLUITen van dit|AN1|1 - 1|
||BESLUITTYPE gepubliceerd moeten worden.|||
|Publicatietekst|De generieke tekst van de publicatie van|AN1000|0 - 1|
||BESLUITen van dit BESLUITTYPE|||
|Publicatietermijn|Het aantal dagen, gerekend vanaf de|N3|0 - 1|
||verzend- of publicatiedatum, dat BESLUITen|||
||van dit BESLUITTYPE gepubliceerd moeten|||
||blijven.|||
|Toelichting|Een eventuele toelichting op dit|AN1000|0 - 1|
||BESLUITTYPE.|||
|Datum begin geldigheid|De datum waarop het BESLUITTYPE is|Onvolledig|1 - 1|
|besluittype|ontstaan.|eDatum||
|Datum einde geldigheid|De datum waarop het BESLUITTYPE is|Onvolledig|0 - 1|
|besluittype|opgeheven.|eDatum||



**Overzicht relaties** 

10 

**==> picture [103 x 52] intentionally omitted <==**

_Relatienaam met Definitie kardinaliteiten_ ZAAKTYPE  [1..*] De BESLUITTYPEn die relevant kunnen zijn voor ZAAKen van dit heeft relevant ZAAKTYPE BESLUITTYPE  [0..*] RESULTAATTYPE  [1..*] Het BESLUITTYPE van besluiten die gepaard gaan met resultaten leidt tot van het RESULTAATTYPE. BESLUITTYPE  [0..*] BESLUITTYPE  [1..*] De CATALOGUS waartoe dit BESLUITTYPE behoort. maakt deel uit van CATALOGUS  [1] BESLUITTYPE  [0..*] Het INFORMATIEOBJECTTYPE van informatieobjecten waarin wordt vastgelegd in besluiten van dit BESLUITTYPE worden vastgelegd. INFORMATIEOBJECTTYPE [0..*] 

## **Toelichting objecttype** 

Het betreft de indeling of groepering van besluiten naar hun aard, zoals bouwvergunning, ontheffing geluidhinder en monumentensubsidie 

## **3.2 Objecttype CATALOGUS** 

**Naam** CATALOGUS **Mnemonic** CAT **Herkomst** KING **Definitie** De verzameling van ZAAKTYPEn - incl. daarvoor relevante objecttypen - voor een Domein die als één geheel beheerd wordt. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Unieke aanduiding** Combinatie van Domein met RSIN. **Populatie Kwaliteitsbegrip** 

|**Overzicht attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Domein|Een afkorting waarmee wordt aangegeven|AN5|1 - 1|
||voor welk domein in een CATALOGUS|||
||ZAAKTYPEn zijn uitgewerkt.|||
|RSIN|Het door een kamer toegekend uniek|N9|1 - 1|
||nummer voor de INGESCHREVEN NIET-|||
||NATUURLIJK PERSOON die de eigenaar is van|||
||een CATALOGUS.|||
|Contactpersoon beheer naam De naam van de contactpersoon die||AN40|1 - 1|
||verantwoordelijk is voor het beheer van de|||



11 

**==> picture [103 x 52] intentionally omitted <==**

CATALOGUS. Contactpersoon beheer Het telefoonnummer van de contactpersoon AN20 0 - 1 telefoonnummer die verantwoordelijk is voor het beheer van de CATALOGUS. Contactpersoon beheer Het emailadres van de contactpersoon die AN254 0 - 1 emailadres verantwoordelijk is voor het beheer van de CATALOGUS. 

## **Overzicht relaties** 

_Relatienaam met Definitie kardinaliteiten_ ZAAKTYPE  [1..*] De CATALOGUS waartoe dit ZAAKTYPE behoort. maakt deel uit van CATALOGUS  [1] INFORMATIEOBJECTTYPE De CATALOGUS waartoe dit INFORMATIEOBJECTTYPE behoort. [1..*] maakt deel uit van CATALOGUS  [1] BESLUITTYPE  [1..*] De CATALOGUS waartoe dit BESLUITTYPE behoort. maakt deel uit van CATALOGUS  [1] 

## **Toelichting objecttype** 

Voor de inzet van de CATALOGUS in één uitvoerende organisatie (bijv. een gemeente) gaat KING ervan uit dat binnen de organisatie één CATALOGUS wordt gebruikt met alle ZAAKTYPEn van de organisatie. De unieke identificatie in dit voorbeeld wordt dan de combinatie van het Domein 'Gemeente', gevolgd door het RSIN van de betreffende gemeente. Standaardiserende organisaties zullen mogelijk meerdere catalogi willen publiceren en beheren. Denk aan een ministerie dat voor meerdere sectoren een CATALOGUS aanlegt. Via het Domein-attribuut krijgt zo elke CATALOGUS toch een unieke identificatie. 

KING bepaalt niet op voorhand welke waarden 'Domein' kan aannemen, maar registreert wel alle gebruikte waarden. 

## **3.3 Objecttype EIGENSCHAP** 

**Naam** EIGENSCHAP 

**Mnemonic** EIG **Herkomst** KING **Definitie** Een relevant inhoudelijk gegeven dat bij ZAAKen van dit ZAAKTYPE geregistreerd moet kunnen worden en geen standaard kenmerk is van een zaak. 

**Herkomst definitie** KING **Datum opname** 1 juli 2012 **Unieke aanduiding** Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met Eigenschapnaam 

**Populatie** 

12 

**==> picture [103 x 52] intentionally omitted <==**

|**Kwaliteitsbegrip**||||
|---|---|---|---|
|**Overzicht attributen**||||
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Eigenschapnaam|De naam van de EIGENSCHAP|AN20|1 - 1|
|Definitie|De beschrijving van de betekenis van deze|AN255|1 - 1|
||EIGENSCHAP|||
|Specificatie van eigenschap|Attribuutkenmerken van de eigenschap|Specificatie|0- 1|
|||van||
|||eigenschap||
|- Groep|Benaming van het object of groepattribuut|AN32|0 - 1|
||waarvan de EIGENSCHAP een inhoudelijk|||
||gegeven specificeert.|||
|- Formaat|Het soort tekens waarmee waarden van de|AN20|1 - 1|
||EIGENSCHAP kunnen worden vastgelegd.|||
|- Lengte|Het aantal karakters (lengte) waarmee|AN14|1 - 1|
||waarden van de EIGENSCHAP worden|||
||vastgelegd.|||
|- Kardinaliteit|Het aantal mogelijke voorkomens van|AN3|1 - 1|
||waarden van deze EIGENSCHAP bij een zaak|||
||van  het ZAAKTYPE.|||
|- Waardenverzameling|Een waarde die deze EIGENSCHAP kan|AN100|0 - N|
||hebben.|||
|Referentie naar eigenschap|Verwijzing naar de standaard waarin de|Referentie|0- 1|
||eigenschap is gespecificeerd|naar||
|||eigenschap||
|- Objecttype|De naam van het objecttype waarbij de|AN40|0 - 1|
||eigenschap is gemodelleerd in het|||
||informatiemodel waarvan het objecttype|||
||deel uit maakt.|||
|- Informatiemodel|De naam en de versie van het|AN80|0 - 1|
||informatiemodel waarin de eigenschap is|||
||gemodelleerd.|||
|- Namespace|De naam van het schema waarin de|AN200|1 - 1|
||eigenschap is opgenomen.|||
|- Schemalocatie|De locatie van het XML-schema behorend bij|AN200|1 - 1|
||de Namespace|||
|- X-path element|De naam van de eigenschap en het pad|AN255|0 - 1|
||daarnaar toe in het XML-schema behorend bij|||
||de namespace.|||
|- Entiteittype|De naam van de XML-constructie in het XML-|AN80|1 - 1|
||schema behorend bij de namespace die|||
||afgeleid is van de naam van het objecttype en|||
||waarin de eigenschap is opgenomen.|||
|Toelichting|Een toelichting op deze EIGENSCHAP en het|AN1000|0 - 1|
||belang hiervan voor zaken van dit ZAAKTYPE.|||
|Datum begin geldigheid|De datum waarop de EIGENSCHAP is|Onvolledig|1 - 1|
|eigenschap|ontstaan.|eDatum||
|Datum einde geldigheid|De datum waarop de EIGENSCHAP is|Onvolledig|0 - 1|
|eigenschap|opgeheven.|eDatum||



13 

**==> picture [103 x 52] intentionally omitted <==**

## **Overzicht relaties** 

_Relatienaam met Definitie kardinaliteiten_ STATUSTYPE  [0..1] De EIGENSCHAPpen die verplicht een waarde moeten hebben heeft verplichte gekregen, voordat een STATUS van dit STATUSTYPE kan worden EIGENSCHAP  [0..*] gezet. RESULTAATTYPE  [0..*] De EIGENSCHAP die bepalend is voor het moment waarop de heeft voor Brondatum Archiefactietermijn start voor een ZAAK met een resultaat van dit archiefprocedure relevante RESULTAATTYPE. EIGENSCHAP  [0..1] EIGENSCHAP  [0..*] Het ZAAKTYPE van de ZAAKen waarvoor deze EIGENSCHAP van is van belang is. ZAAKTYPE  [1] 

## **Toelichting objecttype** 

Met standaard kenmerken van een zaak worden bedoeld de attributen die in het RGBZ gespecificeerd zijn bij ZAAK en bij de andere daarin opgenomen objecttypen. Deze kenmerken zijn generiek d.w.z. van toepassing op elke zaak, ongeacht het zaaktype. Niet voor elke zaak van elk zaaktype is dit voldoende informatie voor de behandeling van de zaak, de besturing daarvan en om daarover informatie uit te kunnen wisselen. Zo is voor het behandelen van een aanvraag voor een kapvergunning informatie nodig over de locatie, het type en de diameter van de te kappen boom. Het RGBZ bevat reeds de locatie-kenmerken. Boomtype en Stamdiameter zijn gegevens die specifiek zijn voor zaken van dit zaaktype, de zaaktypespecifieke eigenschappen. Een ander voorbeeld is de evenementdatum bij de behandeling van een aanvraag voor een evenementenvergunning. 

Met het specificeren van eigenschappen wordt ten eerste beoogd duidelijkheid te geven over de voor een zaaktype relevante eigenschappen en wordt ten tweede beoogd die eigenschappen zodanig te specificeren dat waarden van deze eigenschappen in StUF-ZKNberichten uitgewisseld kunnen worden. 

Met de attributen van het objecttype EIGENSCHAP wordt een zaaktypespecifieke eigenschap gespecificeerd. De attributen Eigenschapnaam en Definitie duiden de eigenschap. De eigenschap wordt gegevenstechnisch gespecificeerd met één van twee groepen attributen: a) Groep, Formaat, Lengte, Kardinaliteit en Waardenverzameling. Het attribuut ‘Groep’ maakt het mogelijk om eigenschappen te groeperen naar een object of een groepattribuut en, met een StUF-ZKN-bericht, de waarden van de bij een groep behorende eigenschappen voor meerdere objecten uit te wisselen (bijvoorbeeld een ‘kapvergunning’ voor meerdere bomen die ieder apart geduid worden). 

b) Objecttype, Informatiemodel, Namespace, Schemalocatie, X-path element en Entiteittype. Deze specificeren een eigenschap door te refereren naar een berichtenmodel en, bij voorkeur ook, een informatiemodel. De eigenschap wordt aldus ontleend aan een XML-schema (als onderdeel van een berichtenmodel) dat reeds bestaat of specifiek voor het zaaktype (of de zaaktypecatalogus) is opgesteld. Voor een goed begrip van de eigenschap is het dringend gewenst dat deze semantisch gespecificeerd is in een informatiemodel met het oog op eenduidig te interpreteren uitwisseling van waarden van de eigenschap.  Het betreft het informatiemodel dat opgesteld is voor het domein waarvoor de zaaktypen gespecificeerd worden en op basis waarvan het XML-schema is vervaardigd. 

De specificatie ad. a ondersteunt de mogelijkheid om waarden van deze eigenschappen, bij 

14 

**==> picture [103 x 52] intentionally omitted <==**

een specifieke zaak, uit te wisselen tussen applicaties ten behoeve van gebruik van deze gegevens door de gebruikers van deze applicaties. De gebruikers kunnen deze gegevens interpreteren, de uitwisselende applicaties kennen deze gegevens, zonder voorafgaande afspraken, niet zodanig dat zij daar betrouwbaar bewerkingen op kunnen baseren anders dan tonen en eventueel wijzigen en opslaan. 

De specificatie ad. b ondersteunt de mogelijkheid om waarden van deze eigenschappen, bij een specifieke zaak, uit te wisselen tussen applicaties die deze gegevens (willen) kennen teneinde daarop betrouwbaar bewerkingen te doen of te baseren (bijvoorbeeld uit de diameter, type en plaats van de boom afleiden of de vergunning verleend kan worden of niet). 

## **3.4 Objecttype INFORMATIEOBJECTTYPE** 

**Naam** INFORMATIEOBJECTTYPE **Mnemonic** DCT **Herkomst** KING **Definitie** Aanduiding van de aard van INFORMATIEOBJECTen zoals gehanteerd door de zaakbehandelende organisatie. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Unieke aanduiding** Unieke aanduiding van CATALOGUS in combinatie met Informatieobjecttypeomschrijving. **Populatie** 

|**Kwaliteitsbegrip**|betreft dit de waarborgen voor de juistheid van de in de|betreft dit de waarborgen voor de juistheid van de in de|registratie||
|---|---|---|---|---|
|**Overzicht attributen**|||||
|_Attribuutnaam_||_Definitie_|_Formaat_|_Kardi-_|
|||||_naliteit_|
|Informatieobjecttype-||Omschrijving van de aard van|AN80|1 - 1|
|omschrijving||informatieobjecten van dit|||
|||INFORMATIEOBJECTTYPE.|||
|Informatieobjecttype-||Algemeen gehanteerde omschrijving van het|INFORMA|0 - 1|
|omschrijving generiek||INFORMATIEOBJECTTYPE.|TIEOBJECT||
||||TYPE-||
||||OMSCHRIJ||
||||VING||
||||GENERIEK||
|Informatieobjectcategorie||Typering van de aard van informatieobjecten|AN80|1 - 1|
|||van dit INFORMATIEOBJECTTYPE.|||
|Informatieobjecttypetrefwoo||Trefwoord(en) waarmee informatieobjecten|AN30|0 - N|
|rd||van het INFORMATIEOBJECTTYPE kunnen|||
|||worden gekarakteriseerd.|||
|Vertrouwelijkheidaanduiding||Aanduiding van de mate waarin|AN20|0 - 1|
|||informatieobjecten van dit|||
|||INFORMATIEOBJECTTYPE voor de|||
|||openbaarheid bestemd zijn.|||
|Model||De URL naar het model / sjabloon dat wordt|anyURL|0 - N|
|||gebruikt voor de creatie van|||



15 

**==> picture [103 x 52] intentionally omitted <==**

Toelichting 

Datum begin geldigheid informatieobjecttype Datum einde geldigheid informatieobjecttype 

informatieobjecten van dit INFORMATIEOBJECTTYPE. Een eventuele toelichting op dit AN1000 0 - 1 INFORMATIEOBJECTTYPE. De datum waarop het Onvolledig 1 - 1 INFORMATIEOBJECTTYPE is ontstaan. eDatum De datum waarop het Onvolledig 0 - 1 INFORMATIEOBJECTTYPE is opgeheven. eDatum 

## **Overzicht relaties** 

## _Definitie_ 

_Relatienaam met kardinaliteiten_ ZAAKTYPE  [1..*] heeft relevant INFORMATIEOBJECTTYPE [0..*] 

De INFORMATIEOBJECTTYPEn die relevant kunnen zijn voor ZAAKen van dit ZAAKTYPE. 

De CATALOGUS waartoe dit INFORMATIEOBJECTTYPE behoort. 

INFORMATIEOBJECTTYPE De CATALOGUS waartoe dit INFORMATIEOBJECTTYPE behoort. [1..*] maakt deel uit van CATALOGUS  [1] BESLUITTYPE  [0..*] Het INFORMATIEOBJECTTYPE van informatieobjecten waarin wordt vastgelegd in besluiten van dit BESLUITTYPE worden vastgelegd. INFORMATIEOBJECTTYPE [0..*] De BESLUITTYPEn die in informatieobjecten van dit INFORMATIEOBJECTTYPE worden vastgelegd. 

## **Toelichting objecttype** 

‘Informatieobject’ is een generiekere term voor het veelgebruikte begrip ‘document’ dat beperkter van reikwijdte is. Een informatieobject kan van alles zijn, ongeacht aard en vorm: een tekstverwerkingsdocument, een papieren brief, een webpagina, een landkaart, een foto, een geluidsopname, een dataset, een blog, etcetera. En ook een digitaal ontvangen of gecreeerd informatieobject dat bestaat uit meerdere fysieke informatieobjecten, zoals een aanvraag (als tekstdocument) met bijbehorende tekening (CAD-formaat) en berekening (spreadsheet) of een email met bijlage(n). Net zoals dezelfde aanvraag op papier met bijlagen als één informatieobject beschouwd kan worden. De fysieke vorm van hetgeen ontvangen of gecreeerd is, is dus niet (alleen) bepalend voor de afbakening van dat wat als informatieobject beschouwd wordt. Voor de leesbaarheid hanteren we in toelichtingen in dit informatiemodel hier en daar wel de term ‘document’ waarmee we formeel ‘informatieobject’ bedoelen. Het INFORMATIEOBJECTTYPE betreft de typering van informatieobjecten naar hun aard zoals gehanteerd door de zaakbehandelende organisatie. Elk informatieobjecttype komt overeen met of valt binnen de generieke typering van informatieobjecten zoals landelijk gehanteerd, de informatieobjecttype-omschrijving generiek . Het informatieobjecttype stelt organisatie in staat hun eigen typering aan te houden en, d.m.v. de relatie naar Informatieobjecttypeomschrijving generiek, toch aan te kunnen sluiten op de landelijk gehanteerde typering generiek. 

**3.5 Objecttype RESULTAATTYPE** 

**Naam** RESULTAATTYPE 

16 

**==> picture [103 x 52] intentionally omitted <==**

**Mnemonic** RST **Herkomst** KING **Definitie** Het betreft de indeling of groepering van resultaten van zaken van hetzelfde ZAAKTYPE naar hun aard, zoals 'verleend', 'geweigerd', 'verwerkt', et cetera. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Unieke aanduiding** Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met de Resultaattypeomschrijving 

## **Populatie Kwaliteitsbegrip** 

|**Overzicht attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Resultaattypeomschrijving|Omschrijving van de aard van resultaten van|AN20|1 - 1|
||het RESULTAATTYPE.|||
|Resultaattypeomschrijving|Algemeen gehanteerde omschrijving van de|AN20|1 - 1|
|generiek|aard van resultaten van het RESULTAATTYPE.|||
|Selectielijstklasse|Verwijzing naar de, voor het archiefregime bij|AN500|0 - 1|
||het RESULTAATTYPE relevante, passage in de|||
||Selectielijst Archiefbescheiden van de voor|||
||het ZAAKTYPE verantwoordelijke|||
||overheidsorganisatie.|||
|Archiefnominatie|Aanduiding die aangeeft of ZAAKen met een|AN16|1 - 1|
||resultaat van dit RESULTAATTYPE blijvend|||
||moeten worden bewaard of (op termijn)|||
||moeten worden vernietigd .|||
|Archiefactietermijn|De termijn waarna het zaakdossier (de ZAAK|N4|1 - 1|
||met alle bijbehorende|||
||INFORMATIEOBJECTen) van een ZAAK met|||
||een resultaat van dit RESULTAATTYPE|||
||vernietigd of overgebracht (naar een|||
||archiefbewaarplaats) moet worden.|||
|Brondatum archiefprocedure|Aanduiding van de brondatum voor de start|AN20|1 - 1|
||van de Archiefactietermijn van het|||
||zaakdossier.|||
|Toelichting|Een toelichting op dit RESULTAATTYPE en het|AN1000|0 - 1|
||belang hiervan voor ZAAKen waarin een|||
||Resultaat van dit RESULTAATTYPE wordt|||
||geselecteerd.|||
|Datum begin geldigheid|De datum waarop het RESULTAATTYPE is|Onvolledig|1 - 1|
|resultaattype|ontstaan.|eDatum||
|Datum einde geldigheid|De datum waarop het RESULTAATTYPE is|Onvolledig|0 - 1|
|resultaattype|opgeheven.|eDatum||
|**Overzicht relaties**||||
|_Relatienaam met_|_Definitie_|||



17 

**==> picture [103 x 52] intentionally omitted <==**

## _kardinaliteiten_ 

RESULTAATTYPE  [0..*] bepaalt afwijkend archiefregime van ZAAK-INFORMATIEOBJECTTYPE  [0..*] 

RESULTAATTYPE  [0..*] heeft verplichte ZAAKOBJECTTYPE  [0..*] RESULTAATTYPE  [0..*] heeft verplichte ZAAK-INFORMATIEOBJECTTYPE  [0..*] RESULTAATTYPE  [0..*] heeft voor Brondatum archiefprocedure relevante EIGENSCHAP  [0..1] 

Informatieobjecten van een ZAAKINFORMATIEOBJECTTYPE bij zaken van een ZAAKTYPE waarvan, op grond van resultaten van een RESULTAATTYPE bij dat ZAAKTYPE,  de archiveringskenmerken afwijken van de archiveringskenmerken van het ZAAKTYPE. 

De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan ZAAKen van dit ZAAKTYPE voordat een resultaat van dit RESULTAATTYPE kan worden gezet. 

De INFORMATIEOBJECTTYPEn die verplicht aanwezig moeten zijn in het zaakdossier van ZAAKen van dit ZAAKTYPE voordat een resultaat van dit RESULTAATTYPE kan worden gezet. 

De EIGENSCHAP die bepalend is voor het moment waarop de Archiefactietermijn start voor een ZAAK met een resultaat van dit RESULTAATTYPE. 

RESULTAATTYPE  [1..*] Het ZAAKTYPE van ZAAKen waarin resultaten van dit is relevant voor RESULTAATTYPE bereikt kunnen worden. ZAAKTYPE  [1] RESULTAATTYPE  [1..*] Het BESLUITTYPE van besluiten die gepaard gaan met resultaten leidt tot van het RESULTAATTYPE. BESLUITTYPE  [0..*] 

## **Toelichting objecttype** 

Elke zaak heeft een resultaat. In een aantal gevallen valt dit resultaat samen met een besluit: ‘Evenementenvergunning verleend’, ‘Energiesubsidie geweigerd’, et cetera. Het komt echter ook voor dat zaken worden afgehandeld zonder dat er een besluit wordt genomen. Dit is bijvoorbeeld het geval bij aangiften (geboorte, verhuizing), meldingen (openbare ruimte), maar ook bij het intrekken van een aanvraag. Het resultaat van een zaak is van groot belang voor de archivering: het resultaattype bepaalt mede of de zaak en het bijbehorende dossier moeten worden vernietigd (na enige termijn) of blijvend bewaard moeten worden (en na enige termijn ‘overgebracht’ worden naar een archiefbewaarplaats). Met RESULTAATTYPE worden de mogelijke resultaten benoemd bij het desbetreffende zaaktype. Daarmee is het archiefregime bepaald voor het gehele zaakdossier: alle informatie over en documenten bij de zaken van het ZAAKTYPE. 

In uitzonderingsgevallen kan er sprake van zijn dat documenten van een bepaald INFORMATIEOBJECTTYPE in zaakdossiers bij zaken van het ZAAKTYPE een afwijkend archiefregime hebben ten opzichte van het zaakdossier. Privacy-gevoeligheid kan er reden voor zijn om documenten van een ZAAKINFORMATIEOBJECTTYPE eerder te vernietigen dan het zaakdossier als geheel. Specifieke wetgeving, zoals die voor de BAG, leidt er daarentegen toe dat een Omgevingsvergunning (activiteit bouwen) ten eeuwige dage bewaard moet blijven terwijl het zaakdossier na 20 jaar vernietigd dient te worden. De relatiesoort ‘RESULTAATTYPE bepaalt afwijkend archiefregime van ZAAK-INFORMATIEOBJECT-TYPE’ geeft de mogelijkheid deze uitzonderingsgevallen te documenteren. 

18 

**==> picture [103 x 52] intentionally omitted <==**

## **3.6 Objecttype ROLTYPE** 

## **Naam** ROLTYPE 

**Mnemonic** RLT **Herkomst** KING 

**Definitie** Generieke aanduiding van de aard van een ROL die een BETROKKENE kan uitoefenen in ZAAKen van een ZAAKTYPE. 

**Herkomst definitie** 

KING 

**Datum opname** 1 juli 2012 

**Unieke aanduiding** Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met de Roltypeomschrijving 

**Populatie** 

## **Kwaliteitsbegrip** 

## **Overzicht attributen** 

_Attribuutnaam Definitie Formaat Kardinaliteit_ Roltypeomschrijving Omschrijving van de aard van de ROL. AN20 1 - 1 Roltypeomschrijving generiek Algemeen gehanteerde omschrijving van de AN20 1 - 1 aard van de ROL. Soort betrokkene De (soort) betrokkene die een rol van dit AN80 1 - N roltype mag uitoefenen. Datum begin geldigheid De datum waarop het ROLTYPE is ontstaan. Onvolledig 1 - 1 roltype eDatum Datum einde geldigheid De datum waarop het ROLTYPE is opgeheven. Onvolledig 0 - 1 roltype eDatum 

## **Overzicht relaties** 

_Relatienaam met Definitie kardinaliteiten_ ROLTYPE  [1..*] De ROLTYPEn waarin BETROKKENEn een ROL kunnen uitoefenen in is van ZAAKen van dit ZAAKTYPE. ZAAKTYPE  [1] ROLTYPE  [1..*] De STATUSTYPEn die een betrokkene in een rol van dit ROLTYPE mag zetten mag zetten. STATUSTYPE  [0..*] 

## **Toelichting objecttype** 

Zowel in de GEMMA-procesarchitectuur, het RGBZ als de ZTC komt het begrip ‘rol’ voor. De interpretatie daarvan hebben we geharmoniseerd. 

Onder ‘rol’ verstaan we de aard van de bijdrage die een extern persoon, medewerker, afdeling, bedrijf e.d. levert aan de behandeling van een zaak cq. de uitvoering van een bedrijfsproces. Het gaat hierbij om ‘wat’ iemand doet,  niet om ‘wie’ het doet. Het gaat dus niet om functies van medewerkers binnen een organisatie maar om de taken die iemand uitvoert. Een rol kan in praktijksituaties dan ook toegewezen worden aan diverse functionarissen, afdelingen en externen. Ook kan het voor komen dat één medewerker meerdere rollen vervult of dat 

19 

**==> picture [103 x 52] intentionally omitted <==**

meerdere medewerkers samen één rol vervullen. 

Rolbenamingen zijn veelal specifiek voor het zaak- of procestype: subsidieaanvrager, inspecteur, juridisch adviseur, vergunningbehandelaar, bezwaarindiener, klager, etcetera. Om bij uitwisseling van zaak- en procesgegevens (binnen en tussen organisaties) te bereiken dat rolbenamingen juist geïnterpreteerd worden, hanteren we generieke rolbenamingen. Per zaaktype en proces kunnen deze verbijzonderd of zelfs uitgesplitst worden naar contextspecifieke benamingen. Waar gesproken wordt van ‘zaak’ bedoelen we zowel ‘hoofdzaak’ als ‘deelzaak’. 

## **3.7 Objecttype STATUSTYPE** 

|**Naam**|STATUSTYPE|STATUSTYPE|||
|---|---|---|---|---|
|**Mnemonic**|STT||||
|**Herkomst**|KING||||
|**Definitie**|Generieke aanduiding van de aard van een STATUS||||
|**Herkomst definitie**|KING||||
|**Datum opname**|1 juni|2008|||
|**Unieke aanduiding**|Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met||||
||het Statustypevolgnummer||||
|**Populatie**|||||
|**Kwaliteitsbegrip**|||||
|**Overzicht attributen**|||||
|_Attribuutnaam_||_Definitie_|_Formaat_|_Kardi-_|
|||||_naliteit_|
|Statustype-omschrijving||Een korte, voor de initiator van de zaak|AN80|1 - 1|
|||relevante, omschrijving van de aard van de|||
|||STATUS van zaken van een ZAAKTYPE.|||
|Statustype-omschrijving||Algemeen gehanteerde omschrijving van de|AN80|0 - 1|
|generiek||aard van STATUSsen van het STATUSTYPE|||
|Statustypevolgnummer||Een volgnummer voor statussen van het|N4|1 - 1|
|||STATUSTYPE binnen een zaak.|||
|Doorlooptijd status||De door de zaakbehandelende organisatie(s)|N3|0 - 1|
|||gestelde norm voor de doorlooptijd voor het|||
|||bereiken van statussen van dit STATUSTYPE|||
|||bij het desbetreffende ZAAKTYPE, vanaf het|||
|||bereiken van de voorafgaande status|||
|Checklistitem||Te controleren aandachtspunt|Checklistite|0 - N|
|||voorafgaand aan het bereiken van een|m||
|||status van het STATUSTYPE.|||
|- Itemnaam||De betekenisvolle benaming van het|AN30|1 - 1|
|||checklistitem|||
|- Vraagstelling||Een betekenisvolle vraag waaruit blijkt|AN255|1 - 1|
|||waarop het aandachtspunt gecontroleerd|||
|||moet worden.|||
|- Verplicht||Het al dan niet verplicht zijn van controle van|boolean|1 - 1|
|||het aandachtspunt voorafgaand aan het|||



20 

**==> picture [103 x 52] intentionally omitted <==**

||bereiken van de status van het gerelateerde|||
|---|---|---|---|
||STATUSTYPE.|||
|- Toelichting|Beschrijving van de overwegingen bij het|AN1000|0 - 1|
||controleren van het aandachtspunt|||
|Informeren|Aanduiding die aangeeft of na het zetten van|A1|1 - 1|
||een STATUS van dit STATUSTYPE de Initiator|||
||moet worden geïnformeerd over de|||
||statusovergang.|||
|Statustekst|De tekst die wordt gebruikt om de Initiator te|AN1000|0 - 1|
||informeren over het bereiken van een|||
||STATUS van dit STATUSTYPE bij het|||
||desbetreffende ZAAKTYPE.|||
|Toelichting|Een eventuele toelichting op dit STATUSTYPE.|AN1000|0 - 1|
|Datum begin geldigheid|De datum waarop het STATUSTYPE is|Onvolledig|1 - 1|
|statustype|ontstaan.|eDatum||
|Datum einde geldigheid|De datum waarop het STATUSTYPE is|Onvolledig|0 - 1|
|statustype|opgeheven.|eDatum||



## **Overzicht relaties** 

_Relatienaam met Definitie kardinaliteiten_ STATUSTYPE  [0..1] De informatieobjecten van de INFORMATIEOBJECTTYPEn van het heeft verplichte aan het STATUSTYPE gerelateerde ZAAKTYPE waarvoor geldt dat ZAAK-INFORMATIEOBJECTdeze verplicht aanwezig moeten zijn bij een zaak van het TYPE  [0..*] gerelateerde ZAAKTYPE voordat de status van dit STATUSTYPE kan worden gezet bij die zaak. STATUSTYPE  [0..1] De EIGENSCHAPpen die verplicht een waarde moeten hebben heeft verplichte gekregen, voordat een STATUS van dit STATUSTYPE kan worden EIGENSCHAP  [0..*] gezet. STATUSTYPE  [0..1] De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan heeft verplichte ZAAKen van het ZAAKTYPE voordat een STATUS van dit ZAAKOBJECTTYPE  [0..*] STATUSTYPE kan worden gezet. STATUSTYPE  [1..*] Het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE is van bereikt kunnen worden. ZAAKTYPE  [1] ROLTYPE  [1..*] De STATUSTYPEn die een betrokkene in een rol van dit ROLTYPE mag zetten mag zetten. STATUSTYPE  [0..*] 

## **Toelichting objecttype** 

Zaken van eenzelfde zaaktype doorlopen alle dezelfde statussen, tenzij de zaak voortijdig beeëindigd wordt. Met STATUSTYPE worden deze statussen benoemd bij het desbetreffende zaaktype. De attribuutsoort ‘Doorlooptijd status’ is niet bedoeld om daarmee voor een individuele zaak de statussen te plannen maar om geïnteresseerden informatie te verschaffen over de termijn waarop normaliter een volgende status bereikt wordt. 

**3.8 Objecttype ZAAKOBJECTTYPE** 

21 

**==> picture [103 x 52] intentionally omitted <==**

## **Naam** 

ZAAKOBJECTTYPE 

**Mnemonic** ZOT **Herkomst** KING **Definitie** De objecttypen van objecten waarop een zaak van het ZAAKTYPE betrekking kan hebben. 

## **Herkomst definitie** 

KING 

**Datum opname** 1 juli 2012 **Unieke aanduiding** Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met het Objecttype 

## **Populatie** 

## **Kwaliteitsbegrip** 

## **Overzicht attributen** 

|**zicht attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Objecttype|De naam van het objecttype waarop zaken|AN40|1 - 1|
||van het gerelateerde ZAAKTYPE betrekking|||
||hebben.|||
|Ander objecttype|Aanduiding waarmee wordt aangegeven of|AN1|1 - 1|
||het ZAAKOBJECTTYPE een ander, niet in RSGB|||
||en RGBZ voorkomend, objecttype betreft|||
|Relatieomschrijving|Omschrijving van de betrekking van het|AN80|1 - 1|
||Objecttype op zaken van het gerelateerde|||
||ZAAKTYPE.|||
|Datum begin geldigheid|De datum waarop het ZAAKOBJECTTYPE is|Onvolledig|1 - 1|
|zaakobjecttype|ontstaan.|eDatum||
|Datum einde geldigheid|De datum waarop het ZAAKOBJECTTYPE is|Onvolledig|0 - 1|
|zaakobjecttype|opgeheven.|eDatum||



## **Overzicht relaties** 

## _Definitie_ 

_Relatienaam met Definitie kardinaliteiten_ STATUSTYPE  [0..1] De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan heeft verplichte ZAAKen van het ZAAKTYPE voordat een STATUS van dit ZAAKOBJECTTYPE  [0..*] STATUSTYPE kan worden gezet. RESULTAATTYPE  [0..*] De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan heeft verplichte ZAAKen van dit ZAAKTYPE voordat een resultaat van dit ZAAKOBJECTTYPE  [0..*] RESULTAATTYPE kan worden gezet. ZAAKOBJECTTYPE  [0..*] Zaken van het ZAAKTYPE waarvoor objecten van dit is relevant voor ZAAKOBJECTTYPE relevant zijn. ZAAKTYPE  [1] 

## **Toelichting objecttype** 

Een zaak kan op ‘van alles en nog wat’ betrekking hebben. 

Voor zover dit voorkomens (objecten) van de in het RSGB of RGBZ onderscheiden objecttypen betreft, wordt met ZAAKOBJECTTYPE gespecificeerd op welke van de RSGB- en/of RGBZ- 

22 

**==> picture [103 x 52] intentionally omitted <==**

objecttypen zaken van het gerelateerde ZAAKTYPE betrekking kunnen hebben. Voor zover het andere objecten betreft, wordt met ZAAKOBJECTTYPE gespecificeerd welke andere typen objecten dit betreft. 

## **3.9 Objecttype ZAAKTYPE** 

**Naam** ZAAKTYPE **Mnemonic** ZKT **Herkomst** KING **Definitie** Het geheel van karakteristieke eigenschappen van zaken van eenzelfde soort **Herkomst definitie** KING o.b.v. RGBZ **Datum opname** 1 juli 2012 **Unieke aanduiding** Combinatie van de unieke aanduiding van CATALOGUS met Zaaktypeidentificatie **Populatie Kwaliteitsbegrip** 

|**Overzicht attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Zaaktype-identificatie|Unieke identificatie van het ZAAKTYPE binnen|N5|1 - 1|
||de CATALOGUS waarin het ZAAKTYPE|||
||voorkomt.|||
|Zaaktype-omschrijving|Omschrijving van de aard van ZAAKen van het|AN80|1 - 1|
||ZAAKTYPE.|||
|Zaaktype-omschrijving|Algemeen gehanteerde omschrijving van de|AN80|0 - 1|
|generiek|aard van ZAAKen van het ZAAKTYPE|||
|Zaakcategorie|Typering van de aard van ZAAKen van het|AN40|0 - 1|
||ZAAKTYPE.|||
|Doel|Een omschrijving van hetgeen beoogd is te|AN1000|1 - 1|
||bereiken met een zaak van dit zaaktype.|||
|Aanleiding|Een omschrijving van de gebeurtenis die leidt|AN1000|1 - 1|
||tot het starten van een ZAAK van dit|||
||ZAAKTYPE.|||
|Toelichting|Een eventuele toelichting op dit zaaktype.|AN1000|0 - 1|
|Indicatie Intern of Extern|Een aanduiding waarmee onderscheid wordt|AN6|1 - 1|
||gemaakt tussen ZAAKTYPEn die Intern|||
||respectievelijk Extern geïnitieerd worden.|||
|Handeling initiator|Werkwoord dat hoort bij de handeling die de|AN20|1 - 1|
||initiator verricht bij dit zaaktype. Meestal|||
||'aanvragen', 'indienen' of 'melden'.|||
|Onderwerp|Het onderwerp van ZAAKen van dit|AN80|1 - 1|
||ZAAKTYPE. In veel gevallen nauw gerelateerd|||
||aan de product- of dienstnaam uit de|||
||Producten- en Dienstencatalogus (PDC).|||
||Bijvoorbeeld: 'Evenementenvergunning',|||



23 

**==> picture [103 x 52] intentionally omitted <==**

||'Geboorte', 'Klacht'.|||
|---|---|---|---|
|Handeling behandelaar|Werkwoord dat hoort bij de handeling die de|AN20|1 - 1|
||behandelaar verricht bij het afdoen van|||
||ZAAKen van dit ZAAKTYPE. Meestal|||
||'behandelen', 'uitvoeren', 'vaststellen' of|||
||'onderhouden'.|||
|Doorlooptijd behandeling|De periode waarbinnen volgens wet- en|N3|1 - 1|
||regelgeving een ZAAK van het ZAAKTYPE|||
||afgerond dient te zijn.|||
|Servicenorm behandeling|De periode waarbinnen verwacht wordt dat|N3|0 - 1|
||een ZAAK van het ZAAKTYPE afgerond wordt|||
||conform de geldende servicenormen van de|||
||zaakbehandelende organisatie(s).|||
|Opschorting/aanhouding|Aanduiding die aangeeft of ZAAKen van dit|A1|1 - 1|
|mogelijk|ZAAKTYPE kunnen worden opgeschort en/of|||
||aangehouden.|||
|Verlenging mogelijk|Aanduiding die aangeeft of de Doorlooptijd|A1|1 - 1|
||behandeling van ZAAKen van dit ZAAKTYPE|||
||kan worden verlengd.|||
|Verlengingstermijn|De termijn in dagen waarmee de|N3|1 - 1|
||Doorlooptijd behandeling van ZAAKen van dit|||
||ZAAKTYPE kan worden verlengd.|||
|Trefwoord|Een trefwoord waarmee ZAAKen van het|AN30|0 - N|
||ZAAKTYPE kunnen worden gekarakteriseerd.|||
|Archiefclassificatiecode|De systematische identificatie van|AN20|0 - 1|
||zaakdossiers van dit ZAAKTYPE|||
||overeenkomstig logisch gestructureerde|||
||conventies, methoden en procedureregels.|||
|Vertrouwelijkheidaanduiding|Aanduiding van de mate waarin zaakdossiers|AN20|1 - 1|
||van ZAAKen van dit ZAAKTYPE voor de|||
||openbaarheid bestemd zijn.|||
|Verantwoordelijke|De (soort) organisatorische eenheid  of|AN50|1 - 1|
||(functie van) medewerker die|||
||verantwoordelijk is voor de uitvoering van|||
||zaken van het ZAAKTYPE.|||
|Publicatie-indicatie|Aanduiding of (het starten van) een ZAAK van|AN1|1 - 1|
||dit ZAAKTYPE gepubliceerd moet worden.|||
|Publicatietekst|De generieke tekst van de publicatie van|AN1000|0 - 1|
||ZAAKen van dit ZAAKTYPE.|||
|Product/Dienst|Het product of de dienst die door|Product/Di|1 - N|
||ZAAKen van dit ZAAKTYPE wordt|enst||
||voortgebracht.|||
|- Naam|De naam van het product of de dienst.|AN80|1 - 1|
|- Link|De URL naar de beschrijving van het product|anyURL|0 - 1|
||of de dienst.|||
|Formulier|Het formulier dat ZAAKen van dit|Formulier|0 - N|
||ZAAKTYPE initieert.|||
|- Naam|De naam van het formulier.|AN80|1 - 1|
|- Link|De URL naar het formulier.|anyURL|0 - 1|
|Referentieproces|Verwijzing naar een gelijknamig|Referentie|1 - 1|



24 

**==> picture [103 x 52] intentionally omitted <==**

||groepattribuutsoort.|proces||
|---|---|---|---|
|- Link|De URL naar de beschrijving van het|anyURL|0 - 1|
||Referentieproces.|||
|- Naam|De naam van het Referentieproces.|AN80|1 - 1|
|Verantwoordingsrelatie|De relatie tussen ZAAKen van dit ZAAKTYPE|AN40|0 - N|
||en de beleidsmatige en/of financiële|||
||verantwoording.|||
|Broncatalogus|De CATALOGUS waaraan het ZAAKTYPE|Broncatalo|0 - 1|
||is ontleend.|gus||
|- Domein|Het domein van de CATALOGUS waaraan het|AN30|1 - 1|
||ZAAKTYPE is ontleend.|||
|- RSIN|Het RSIN van de INGESCHREVEN NIET-|N9|1 - 1|
||NATUURLIJK PERSOON die beheerder is van|||
||de CATALOGUS waaraan het ZAAKTYPE is|||
||ontleend.|||
|Bronzaaktype|Het zaaktype binnen de CATALOGUS|Bronzaakty|0 - 1|
||waaraan dit ZAAKTYPE is ontleend.|pe||
|- Zaaktype-identificatie|De Zaaktype-identificatie van het|N5|1 - 1|
||bronzaaktype binnen de CATALOGUS.|||
|- Zaaktype-omschrijving|De Zaaktype-omschrijving van het|AN80|1 - 1|
||bronzaaktype, zoals gehanteerd in de|||
||Broncatalogus.|||
|Datum begin geldigheid|De datum waarop het ZAAKTYPE is ontstaan.|Onvolledig|1 - 1|
|zaaktype||eDatum||
|Versiedatum|De datum waarop de (gewijzigde) kenmerken|Datum|1 - 1|
||van het ZAAKTYPE geldig zijn geworden|(jjjjmmdd)||
|Datum einde geldigheid|De datum waarop het ZAAKTYPE is|Onvolledig|0 - 1|
|zaaktype|opgeheven.|eDatum||



## **Overzicht relaties** 

_Definitie_ 

_Relatienaam met Definitie kardinaliteiten_ ZAAKTYPE  [0..*] De ZAAKTYPEn van zaken die relevant zijn voor zaken van dit heeft gerelateerd ZAAKTYPE. ZAAKTYPE  [0..*] ZAAKTYPE  [1..*] De INFORMATIEOBJECTTYPEn die relevant kunnen zijn voor heeft relevant ZAAKen van dit ZAAKTYPE. INFORMATIEOBJECTTYPE [0..*] ZAAKTYPE  [1..*] De BESLUITTYPEn die relevant kunnen zijn voor ZAAKen van dit heeft relevant ZAAKTYPE BESLUITTYPE  [0..*] ZAAKTYPE  [0..*] De ZAAKTYPEn (van de hoofdzaken) waaronder ZAAKen van dit is deelzaaktype van ZAAKTYPE als deelzaak kunnen voorkomen. ZAAKTYPE  [0..*] ZAAKOBJECTTYPE  [0..*] Zaken van het ZAAKTYPE waarvoor objecten van dit is relevant voor ZAAKOBJECTTYPE relevant zijn. ZAAKTYPE  [1] RESULTAATTYPE  [1..*] Het ZAAKTYPE van ZAAKen waarin resultaten van dit 

25 

**==> picture [103 x 52] intentionally omitted <==**

is relevant voor RESULTAATTYPE bereikt kunnen worden. ZAAKTYPE  [1] EIGENSCHAP  [0..*] Het ZAAKTYPE van de ZAAKen waarvoor deze EIGENSCHAP van is van belang is. ZAAKTYPE  [1] ROLTYPE  [1..*] De ROLTYPEn waarin BETROKKENEn een ROL kunnen uitoefenen in is van ZAAKen van dit ZAAKTYPE. ZAAKTYPE  [1] STATUSTYPE  [1..*] Het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE is van bereikt kunnen worden. ZAAKTYPE  [1] ZAAKTYPE  [1..*] De CATALOGUS waartoe dit ZAAKTYPE behoort. maakt deel uit van CATALOGUS  [1] 

## **Toelichting objecttype** 

Het betreft de indeling of groepering van zaken naar hun aard, zoals “Behandelen aanvraag bouwvergunning” en “Behandelen aanvraag ontheffing parkeren”. Wat in een individueel geval een zaak is, waar die begint en waar die eindigt, wordt bekeken vanuit het perspectief van de initiator van de zaak (burger, bedrijf, medewerker, etc.). Het traject van (aan)vraag cq. aanleiding voor de zaak tot en met de levering van de producten/of diensten die een passend antwoord vormen op die aanleiding, bepaalt de omvang en afbakening van de zaak en daarmee van het zaaktype. Hiermee komt de afbakening van een zaaktype overeen met een bedrijfsproces: ‘van klant tot klant’. Dit betekent ondermeer dat onderdelen van bedrijfsprocessen geen zelfstandige zaken vormen. Het betekent ook dat een aanleiding die niet leidt tot de start van de uitvoering van een bedrijfsproces, niet leidt tot een zaak (deze wordt behandeld in het kader van een reeds lopende zaak). 

Zie ook de toelichtingen bij de relatiesoorten ‘ZAAKTYPE  is deelzaaktype van ZAAKTYPE’ en ‘ZAAKTYPE heeft gerelateerd ZAAKTYPE’ voor wat betreft zaaktypen van deelzaken respectievelijk gerelateerde zaken. 

26 

**==> picture [103 x 52] intentionally omitted <==**

## **4 Relatieklassen** 

In dit hoofdstuk specificeren we de onderscheiden Relatieklassen. Zie de inleidende tekst van hoofdstuk 3 voor de betekenis van de aspecten waarnaar de relatieklassen gespecificeerd zijn. 

## **4.1 Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE** 

**Naam** ZAAK-INFORMATIEOBJECT-TYPE 

|**Mnemonic**||||
|---|---|---|---|
|**Definitie**|Kenmerken van de relatie ZAAKTYPE heeft relevante|||
||INFORMATIEOBJECTTYPEn.|||
|**Overzicht Attributen**||||
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Volgnummer|Uniek volgnummer van het ZAAK-|N3|1 - 1|
||INFORMATIEOBJECT-TYPE binnen het|||
||ZAAKTYPE.|||
|Richting|Aanduiding van de richting van|AN20|1 - 1|
||informatieobjecten van het gerelateerde|||
||INFORMATIEOBJECTTYPE bij zaken van het|||
||gerelateerde ZAAKTYPE.|||



## **Overzicht relaties** 

## _Definitie_ 

_Relatienaam met Definitie kardinaliteiten_ RESULTAATTYPE  [0..*] Informatieobjecten van een ZAAKINFORMATIEOBJECTTYPE bij bepaalt afwijkend zaken van een ZAAKTYPE waarvan, op grond van resultaten van archiefregime van een RESULTAATTYPE bij dat ZAAKTYPE,  de archiveringskenmerken ZAAK-INFORMATIEOBJECTafwijken van de archiveringskenmerken van het ZAAKTYPE. TYPE  [0..*] 

De informatieobjecten van de INFORMATIEOBJECTTYPEn van het aan het STATUSTYPE gerelateerde ZAAKTYPE waarvoor geldt dat deze verplicht aanwezig moeten zijn bij een zaak van het gerelateerde ZAAKTYPE voordat de status van dit STATUSTYPE kan worden gezet bij die zaak. 

STATUSTYPE  [0..1] heeft verplichte ZAAK-INFORMATIEOBJECTTYPE  [0..*] 

RESULTAATTYPE  [0..*] heeft verplichte ZAAK-INFORMATIEOBJECTTYPE  [0..*] 

De INFORMATIEOBJECTTYPEn die verplicht aanwezig moeten zijn in het zaakdossier van ZAAKen van dit ZAAKTYPE voordat een resultaat van dit RESULTAATTYPE kan worden gezet. 

27 

**==> picture [103 x 52] intentionally omitted <==**

## **4.2 Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE ARCHIEFREGIME** 

## ZAAK-INFORMATIETOBJECT-TYPE ARCHIEFREGIME 

|||||
|---|---|---|---|
|**Naam**|ZAAK-INFORMATIETOBJECT-TYPE ARCHIEFREGIME|||
|**Mnemonic**|ZIA|||
|**Definitie**|Afwijkende archiveringskenmerken van informatieobjecten van een|||
||INFORMATIEOBJECTTYPE bij zaken van een ZAAKTYPE op|grond van||
||resultaten van een RESULTAATTYPE bij dat ZAAKTYPE|||
|**Overzicht Attributen**||||
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Selectielijstklasse|Verwijzing naar de voor het|AN500|0 - 1|
||ZAAKINFORMATIEOBJECTTYPE bij het|||
||RESULTAATTYPE relevante passage in de|||
||Selectielijst Archiefbescheiden van de voor|||
||het ZAAKTYPE verantwoordelijke|||
||overheidsorganisatie.|||
|Archiefnominatie|Aanduiding die aangeeft of|A16|1 - 1|
||informatieobjecten, van het|||
||INFORMATIEOBJECTTYPE bij zaken van het|||
||ZAAKTYPE met een resultaat van het|||
||RESULTAATTYPE, blijvend moeten worden|||
||bewaardof (op termijn) moeten worden|||
||vernietigd.|||
|Archiefactietermijn|De termijn waarna informatieobjecten, van|N4|1 - 1|
||het INFORMATIEOBJECTTYPE bij zaken van|||
||het ZAAKTYPE met een resultaat van het|||
||RESULTAATTYPE, vernietigd of overgebracht|||
||(naar een archiefbewaarplaats) moeten|||
||worden.|||
|**Overzicht relaties**||||



28 

**==> picture [103 x 52] intentionally omitted <==**

## **4.3 Relatieklasse ZAAKTYPENRELATIE** 

**Naam** ZAAKTYPENRELATIE **Mnemonic Definitie** Kenmerken van de relatie ZAAKTYPE heeft gerelateerde ZAAKTYPE. 

|**Overzicht Attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Aard relatie|Omschrijving van de aard van de relatie van|AN15|1 - 1|
||zaken van het ZAAKTYPE tot zaken van het|||
||andere ZAAKTYPE|||
|Toelichting|Een toelichting op de aard van de relatie|AN255|0 - 1|
||tussen beide ZAAKTYPEN.|||
|**Overzicht relaties**||||



29 

**==> picture [103 x 52] intentionally omitted <==**

## **5 Referentielijst** 

In dit hoofdstuk specificeren we de onderscheiden referentielijsten. Zie de inleidende tekst van hoofdstuk 3 voor de betekenis van de aspecten waarnaar de referentielijsten gespecificeerd zijn. 

## **5.1 Referentielijst INFORMATIEOBJECTTYPE-OMSCHRIJVING GENERIEK** 

**Naam** INFORMATIEOBJECTTYPE-OMSCHRIJVING GENERIEK 

**Mnemonic** DOG **Herkomst** KING **Definitie** Algemeen binnen de overheid gehanteerde omschrijvingen van de typen informatieobjecten 

**Herkomst definitie** KING **Datum opname** 1-1-2013 **Unieke aanduiding** Informatieobjecttype-omschrijving generiek 

|**Overzicht Attributen**||||
|---|---|---|---|
|_Attribuutnaam_|_Definitie_|_Formaat_|_Kardi-_|
||||_naliteit_|
|Informatieobjecttype-|Algemeen gehanteerde omschrijving van|AN80|1 - 1|
|omschrijving generiek|het type informatieobject.|||
|Definitie|Nauwkeurige beschrijving van het|AN255|1 - 1|
|informatieobjecttype-|generieke type informatieobject|||
|omschrijving generiek||||
|Herkomst|De naam van de waardenverzameling, of|AN12|1 - 1|
|informatieobjecttype-|van de beherende organisatie daarvan,|||
|omschrijving generiek|waaruit de waarde is overgenomen.|||
|Hierarchie|De plaats in de rangorde van het|AN80|1 - 1|
|informatieobjecttype-|informatieobjecttype.|||
|omschrijving generiek||||
|Opmerking|Zinvolle toelichting bij het|AN255|0 - 1|
|informatieobjecttype-|informatieobjecttype|||
|omschrijving generiek||||
|Datum begin geldigheid|De datum waarop de generieke|Onvolledig|1 - 1|
|informatieobjecttype-|omschrijving van toepassing is geworden.|eDatum||
|omschrijving generiek||||
|Datum einde geldigheid|De datum waarop de generieke|Onvolledig|0 - 1|
|informatieobjecttype-|omschrijving niet meer van toepassing is.|eDatum||
|omschrijving generiek||||



## **Toelichting referentielijst** 

Deze 'lijst' bevat de benamingen van de generieke informatieobjecttypen die in de informatieuitwisseling betrokken zijn. 

Het gaat telkens om een korte omschrijving van de aard van een informatieobject, ook wel 'documentnaam' genoemd, zoals deze landelijk binnen de overheid wordt toegepast op basis van 

30 

**==> picture [103 x 52] intentionally omitted <==**

de ZTC. 

De 'lijst' betreft dus geen informatieobjecttypen voor specifieke domeinen en ook geen organisatiespecifieke informatieobjecttypen. 

31 

**==> picture [103 x 52] intentionally omitted <==**

## **6 Attribuut- en relatiesoorten** 

In dit hoofdstuk specificeren we de onderscheiden attributen en relaties per objecttype, relatieklasse en referentielijst naar de volgende aspecten. 

## **Specificatie attribuutsoort** 

## **Naam** 

**Herkomst** 

**Code** 

## **XML-tag** 

**Definitie** 

**Herkomst definitie** 

**Datum opname** 

De naam van de attribuutsoort. 

De basisregistratie of het informatiemodel waaraan de attribuutsoort ontleend is dan wel ‘KING’ indien het een door KING Gemeenten toegevoegd attribuutsoort betreft. 

De in een basisregistratie of ander informatiemodel aan de attribuutsoort toegekende uniek code. Voor door KING toegevoegde attribuutsoorten is vooralsnog afgezien van het specificeren van deze code. 

De naam van de attribuutsoort in berichtstructureer die afgeleid is van het voorliggende informatiemodel. 

De beschrijving van de betekenis van de attribuutsoort. 

De basisregistratie of het informatiemodel waaruit de definitie is overgenomen dan wel een aanduiding die aangeeft uit welke bronnen de defintie is samengesteld. 

De datum waarop de attribuutsoort is opgenomen in het informatiemodel. 

**Formaat** 

**Waardenverzameling** 

Het aantal karakters (lengte) en het soort tekens waarmee waarden van deze attribuutsoort worden vastgelegd. 

De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben (opsomming, bereik of verwijzing naar tabel). Indien de waardenverzameling in een dynamische waardentabel is opgenomen, dan wordt de naam van de desbetreffende referentielijst vermeld. 

## **Indicatie materiële historie** 

Indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de attribuutwaarde. 

**Indicatie formele historie** 

## **Aanduiding gebeurtenis** 

Indicatie of de formele historie van de attribuutsoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt). 

Indicatie of bij een opname, mutatie of verwijdering van de attribuutwaarde de gebeurtenis aangeduid wordt  die aanleiding gaf tot verandering van de attribuutwaarde en zo ja, de specificatie van het metagegeven waarmee de gebeurtenis aangeduid wordt: Gebeurtenisomschrijving. Dit metagegeven specificeren we in een separataat document. 

32 

**==> picture [103 x 52] intentionally omitted <==**

## **Aanduiding brondocument** 

## **Indicatie in onderzoek** 

Indicatie of bij een opname, mutatie of verwijdering van de attribuutwaarde het brondocument aangeduid wordt op basis waarvan de verandering van de attribuutwaarde heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Documentsoort, Documenthouder. Deze metagegevens specificeren we in een separaat document. 

De indicatie of te bevragen is dat er twijfel is of is geweest aan de juistheid van de attribuutwaarde en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de attribuutwaarde. Dit metagegeven specificeren we in een separaat document. 

**Aanduiding** De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de **strijdigheid/nietigheid** openbare orde dan wel nietig is. Dit metagegeven specificeren we in een separaat document. 

## **Indicatie kardinaliteit** 

Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype:. 

0-1: is soms niet beschikbaar 

1-1: is altijd beschikbaar 0-N: is niet altijd beschikbaar, kan een opsomming zijn 1-N: is altijd beschikbaar, kan een opsomming zijn. Indien een attribuutsoort deel uit maakt van een groepsattribuutsoort, dan wordt de kardinaliteit vermeld van het attribuutsoort binnen de groepattribuutsoort. Voor de uiteindelijke kardinaliteit van het attribuutsoort moet ook rekening gehouden worden met de kardinaliteit van het groepsattribuutsoort. 

## **Indicatie authentiek** 

Aanduiding of het een authentiek gegeven (attribuutsoort) betreft. 

**Regels** Optionaliteitsregels of waardebeperkende regels voor de waarden van de attribuutsoort. 

**Toelichting** 

Een inhoudelijke toelichting op de attribuutsoort. 

## **Specificatie relatiesoort** 

Relatiesoorten specificeren we alleen bij het objecttype van waaruit de relatie ontspringt (zie de pijlrichting in het diagram), niet bij het gerelateerde objecttype. 

## **Naam** 

**Gerelateerd objecttype** 

De naam van de relatiesoort. 

Het objecttype waarop de relatie van toepassing is. 

33 

**==> picture [103 x 52] intentionally omitted <==**

## **Indicatie kardinaliteit** 

Deze indicatie geeft aan hoeveel keer waarden van deze relatiesoort (i.c. relaties) kunnen voorkomen bij een object van het betreffende objecttype:. 

0-1: is soms niet beschikbaar 

1-1: is altijd beschikbaar 

0-*: is niet altijd beschikbaar, kunnen meerdere relaties zijn 1-*: is altijd beschikbaar, kunnen meerdere relaties zijn 

*-*: is niet altijd beschikbaar, kunnen meerdere relaties zijn tussen objecten van hetzelfde objecttype. 

De kardinaliteit van de inverse relatie geven we tussen haken aan. Indien een relatiesoort deel uit maakt van een groepsattribuutsoort, dan wordt de kardinaliteit vermeld van de relatiesoort binnen de groepattribuutsoort. Voor de uiteindelijke kardinaliteit van de relatiesoort moet ook rekening gehouden worden met de kardinaliteit van het groepsattribuutsoort. 

## **Herkomst** 

## **Code** 

**Definitie** 

**Herkomst definitie** 

**Datum opname** 

**Indicatie materiële historie** 

**Indicatie formele historie** 

**Aanduiding brondocument** 

De basisregistratie of het informatiemodel waaraan de relatiesoort ontleend is dan wel ‘KING’ indien het een door KING Gemeenten toegevoegd relatiesoort betreft. 

De in een basisregistratie of ander informatiemodel aan de relatiesoort of overeenkomstige attribuutsoort toegekende uniek code. Voor door KING toegevoegde relatiesoorten is vooralsnog afgezien van het specificeren van deze code. 

De beschrijving van de betekenis van de relatiesoort. 

De basisregistratie of het informatiemodel waaruit de definitie is overgenomen dan wel een aanduiding die aangeeft uit welke bronnen de defintie is samengesteld. 

De datum waarop de relatiesoort is opgenomen in het informatiemodel. 

Indicatie of de materiële historie van de relatiesoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de relatie. 

Indicatie of de formele historie van de relatiesoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de relatie (wanneer was de verandering bekend en is deze verwerkt). 

Indicatie of bij een opname, mutatie of verwijdering van de relatie het brondocument aangeduid wordt op basis waarvan de verandering van de relatie heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Documentsoort, Documenthouder. Deze metagegevens specificeren we in een separaat document. 

34 

**==> picture [103 x 52] intentionally omitted <==**

|**Indicatie in onderzoek**|De indicatie of te bevragen is dat er twijfel is of is geweest aan de|
|---|---|
||juistheid van de relatie en dat een onderzoek wordt of is uitgevoerd|
||naar de juistheid van de relatie. Dit metagegeven specificeren we in|
||een separaat document.|
|**Aanduiding**|De aanduiding of te bevragen is dat de relatie strijdig met de|
|**strijdigheid/nietigheid**|openbare orde dan wel nietig is. Dit metagegeven specificeren we in|
||een separaat document.|
|**Indicatie authentiek**|Aanduiding of de attribuutsoort waarvan de relatiesoort is afgeleid,|
||een authentiek gegeven (attribuutsoort) betreft.|
|**Regels**|Optionaliteitsregels of waardebeperkende regels voor de voorkomens|
||van de relatiesoort..|
|**Toelichting**|Een inhoudelijke toelichting op de relatiesoort.|



35 

**==> picture [103 x 52] intentionally omitted <==**

## **6.1 Objecttypen** 

## **6.1.1. Objecttype BESLUITTYPE** 

## **Attribuutsoort Besluittype-omschrijving** 

**Naam** Besluittype-omschrijving **Herkomst** GFO Zaken 2004 **Code** 0002 **XML-tag** omschrijving **Definitie** Omschrijving van de aard van BESLUITen van het BESLUITTYPE. **Herkomst definitie** GFO Zaken 2004, aangepast door KING **Datum opname** 1 juni 2008 **Formaat** AN80 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** - **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van het besluit, ook wel besluitnaam genoemd. Voorbeelden: Lichte bouwvergunning, Kapvergunning, Ontheffing geluidhinder en Monumentensubsidie. Het betreft de attribuutsoort Beschikkingomschrijving in het GFO Zaken 2004. 

## **Attribuutsoort Besluittype-omschrijving generiek** 

|**Naam**|Besluittype-omschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijvingGeneriek|
|**Definitie**|Algemeen gehanteerde omschrijving van de aard van BESLUITen|
||van het BESLUITTYPE|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|



36 

**==> picture [103 x 52] intentionally omitted <==**

historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van het besluit, ook wel besluitnaam genoemd, zoals deze landelijk wordt toegepast binnen de ZTC voor het domein waarvan het zaaktype is afgeleid. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Besluittype-omschrijving. 

## **Attribuutsoort Besluitcategorie** 

|**Naam**|Besluitcategorie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|categorie|
|**Definitie**|Typering van de aard van BESLUITen van het BESLUITTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN40|
|**Waardenverzameling**|gebaseerd op de AWB|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



## **Toelichting** 

Het gaat hier om de indeling van besluittypen naar categorieën zoals Vergunning, Ontheffing en Subsidie. 

## **Attribuutsoort Reactietermijn** 

|**Naam**|Reactietermijn|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|reactietermijn|
|**Definitie**|Het aantal dagen, gerekend vanaf de verzend- of|
||publicatiedatum, waarbinnen verweer tegen een besluit van het|
||besluittype mogelijk is.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|N3|
|**Waardenverzameling**|0-999 kalenderdagen|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



37 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

De telling begint bij de dag volgend op de verzend- of publicatiedatum.  Indien geen sprake is van een reactietermijn dan is de waarde nul. 

## **Attribuutsoort Publicatie-indicatie** 

|**Naam**|Publicatie-indicatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|publicatieIndicatie|
|**Definitie**|Aanduiding of BESLUITen van dit BESLUITTYPE gepubliceerd|
||moeten worden.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN1|
|**Waardenverzameling**|J, N|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



## **Toelichting** 

Het gaat hier niet alleen om de wettelijke verplichting tot publicatie maar ook om de eigen keuze van de organisatie die besluiten van dit type neemt. 

## **Attribuutsoort Publicatietekst** 

**Naam** Publicatietekst **Herkomst** KING **Code XML-tag** publicatieTekst **Definitie** De generieke tekst van de publicatie van BESLUITen van dit BESLUITTYPE **Herkomst definitie** KING **Datum opname** 1 juni 2008 **Formaat** AN1000 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee 

38 

**==> picture [103 x 52] intentionally omitted <==**

**Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

## **Attribuutsoort Publicatietermijn** 

**Naam** Publicatietermijn **Herkomst** KING **Code XML-tag** publicatieTermijn **Definitie** Het aantal dagen, gerekend vanaf de verzend- of publicatiedatum, dat BESLUITen van dit BESLUITTYPE gepubliceerd moeten blijven. **Herkomst definitie** KING **Datum opname** 1 juni 2008 **Formaat** N3 **Waardenverzameling** 0 - 999 kalenderdagen **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

De telling begint bij de dag volgend op de verzend- of publicatiedatum. 

## **Attribuutsoort Toelichting** 

|**Attribuutsoort Toelichting**||
|---|---|
|**Naam**|Toelichting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een eventuele toelichting op dit BESLUITTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



39 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een toelichting te geven op dit BESLUITTYPE. Hier kan bijvoorbeeld een beschrijving worden gegeven van de betekenis van het besluit voor - het verloop van - een ZAAKTYPE. 

## **Attribuutsoort Datum begin geldigheid besluittype** 

|**Naam**|Datum begin geldigheid besluittype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het BESLUITTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|29 mei 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van een gerelateerd|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het besluittype bestaat en toegepast kan worden. Dit vindt plaats met ingang van een versie van het zaaktype dat als eerste aan het besluittype wordt gerelateerd . 

## **Attribuutsoort Datum einde geldigheid besluittype** 

|**Naam**|Datum einde geldigheid besluittype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop het BESLUITTYPE is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|29 mei 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



40 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De datum is gelijk aan of gelegen na de datum zoals opgenomen onder 'Datum begin geldigheid besluittype’. De datum is gelijk aan de dag voor een Versiedatum van een gerelateerd zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het besluittype niet meer bestaat en niet meer toegepast kan worden. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het als laatste gerelateerde zaaktype. 

## **Relatiesoort maakt deel uit van** 

|**Naam**|maakt deel uit van|
|---|---|
|**Gerelateerd objecttype**|CATALOGUS|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De CATALOGUS waartoe dit BESLUITTYPE behoort.|
|**Herkomst definitie**|KING|
|**Datum opname**|28 januari 2013|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**||
|**Toelichting**||



## **Relatiesoort wordt vastgelegd in** 

|**Naam**|wordt vastgelegd in|
|---|---|
|**Gerelateerd objecttype**|INFORMATIEOBJECTTYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|Het INFORMATIEOBJECTTYPE van informatieobjecten waarin|
||besluiten van dit BESLUITTYPE worden vastgelegd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is aan de Versiedatum van de gerelateerde|
||zaaktypen.|



## **Toelichting** 

41 

**==> picture [103 x 52] intentionally omitted <==**

## **6.1.2. Objecttype CATALOGUS** 

## **Attribuutsoort Domein** 

|**Attribuutsoort Domein**||
|---|---|
|**Naam**|Domein|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|domein|
|**Definitie**|Een afkorting waarmee wordt aangegeven voor welk domein in|
||een CATALOGUS ZAAKTYPEn zijn uitgewerkt.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN5|
|**Waardenverzameling**|Hoofdletters|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



Voor de waardenverzameling wordt door KING een waardenlijst beheerd waarin wordt bijgehouden welke afkorting welk domein betreft. 

## **Attribuutsoort RSIN** 

|**Naam**|RSIN|
|---|---|
|**Herkomst**|KING op basis van NHR|
|**Code**||
|**XML-tag**|rsin|
|**Definitie**|Het door een kamer toegekend uniek nummer voor de|
||INGESCHREVEN NIET-NATUURLIJK PERSOON die de eigenaar is|
||van een CATALOGUS.|
|**Herkomst definitie**|NHR|
|**Datum opname**|1 juli 2012|
|**Formaat**|N9|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Ja|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Authentiek|
|**Regels**|-|
|**Toelichting**||



42 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Contactpersoon beheer naam** 

|**Naam**|Contactpersoon beheer naam|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|contactpersoonBeheerNaam|
|**Definitie**|De naam van de contactpersoon die verantwoordelijk is voor het|
||beheer van de CATALOGUS.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN40|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



## **Attribuutsoort Contactpersoon beheer telefoonnummer** 

|**Naam**|Contactpersoon beheer telefoonnummer|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|contactpersoonBeheerTelefoonnummer|
|**Definitie**|Het telefoonnummer van de contactpersoon die verantwoordelijk|
||is voor het beheer van de CATALOGUS.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



Het type is alfanumeriek zodat eventuele toevoegingen als 'bgg', 'zak' of 'mobiel' kunnen worden verwerkt. 

## **Attribuutsoort Contactpersoon beheer emailadres** 

43 

**==> picture [103 x 52] intentionally omitted <==**

**Naam** Contactpersoon beheer emailadres **Herkomst** KING **Code XML-tag** contactpersoonBeheerEmailadres **Definitie** Het emailadres van de contactpersoon die verantwoordelijk is voor het beheer van de CATALOGUS. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Formaat** AN254 **Waardenverzameling** conform RFC 5321 en RFC 5322 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** - **Toelichting** 

## **6.1.3. Objecttype EIGENSCHAP** 

## **Attribuutsoort Eigenschapnaam** 

|**Naam**|Eigenschapnaam|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|naam|
|**Definitie**|De naam van de EIGENSCHAP|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|



## **Toelichting** 

Het betreft de naam van het attribuut in het desbetreffende informatiemodel of, indien de eigenschap niet  aan een informatiemodel ontleend is, de semantische naam van de eigenschap (i.t.t. de elementnaam in een XML-schema). 

Indien eigenschappen gespecificeerd worden door te refereren naar een berichtenmodel cq. namespace, dan kan de eigenschap overeenkomen met een ComplexType (entiteittype). Daarmee wordt aangegeven dat alle elementen van dat entiteittype zaakspecifieke eigenschappen bij het zaaktype zijn. 

44 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Definitie** 

|**Attribuutsoort Definitie**||
|---|---|
|**Naam**|Definitie|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|definitie|
|**Definitie**|De beschrijving van de betekenis van deze EIGENSCHAP|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN255|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Eigenschappen vormen een krachtige en flexibele functionaliteit voor het registreren van relevante kenmerken voor ZAAKen van een specifiek ZAAKTYPE. Die kracht staat of valt echter met een heldere, eenduidige definitie van de EIGENSCHAP. Bijvoorbeeld: "De omtrek van de boom, gemeten op een hoogte van 1 meter boven het maaiveld." De definitie wordt, indien van toepassing, ontleend aan het informatiemodel waarin de eigenschap is gemodelleerd. 

## **Groepattribuutsoort Specificatie van eigenschap** 

|**Naam**|Specificatie van eigenschap|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|specificatie|
|**Definitie**|Attribuutkenmerken van de eigenschap|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attributen van deze groepattribuutsoort hebben geen|
||waarden indien één of meer attributen  van de|
||groepattribuutsoort ‘Referentie naar eigenschap’ van|
||waarden zijn voorzien. De attributen van de|
||groepattribuutsoort veranderen alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van|



45 

**==> picture [103 x 52] intentionally omitted <==**

het gerelateerde zaaktype. 

## **Toelichting** 

Met de ‘subattributen’ (van deze groepattribuutsoort) Groep, Formaat, Lengte, Kardinaliteit en Waardenverzameling wordt een eigenschap gedetailleerd gespecificeerd. Dit vindt alleen plaats als de eigenschap niet gespecificeerd is door middel van het groepattribuutsoort  ‘Referentie naar eigenschap’. 

## **Attribuutsoort 'Groep' van groepattribuutsoort 'Specificatie van eigenschap'** 

|**Naam**|Groep|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|groep|
|**Definitie**|Benaming van het object of groepattribuut waarvan de|
||EIGENSCHAP een inhoudelijk gegeven specificeert.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 december 2013|
|**Formaat**|AN32|
|**Waardenverzameling**|Letters, cijfers en liggende streepjes|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||



## **Toelichting** 

De attribuutsoort maakt het mogelijk om eigenschappen te groeperen naar een object of een groepattribuut en, met een StUF-ZKN-bericht, de waarden van de bij een groep behorende eigenschappen voor meerdere objecten uit te wisselen (bijvoorbeeld een ‘kapvergunning’ voor meerdere bomen die ieder apart geduid worden) . 

## **Attribuutsoort 'Formaat' van groepattribuutsoort 'Specificatie van eigenschap'** 

|**Naam**|Formaat|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|formaat|
|**Definitie**|Het soort tekens waarmee waarden van de EIGENSCHAP|
||kunnen worden vastgelegd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 december 2013|
|**Formaat**|AN20|
|**Waardenverzameling**|tekst|
||getal|
||datum (jjjjmmdd)|
||datum/tijd (jjjjmmdduummss)|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||



46 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** zie groep **Regels Toelichting** 

## **Attribuutsoort 'Lengte' van groepattribuutsoort 'Specificatie van eigenschap'** 

**Naam** Lengte **Herkomst** KING **Code XML-tag** lengte **Definitie** Het aantal karakters (lengte) waarmee waarden van de EIGENSCHAP worden vastgelegd. **Herkomst definitie** KING **Datum opname** 11 januari 2014 **Formaat** AN14 **Waardenverzameling** Als Formaat = tekst: 0-255 Als Formaat = getal: n,m (n: aantal cijfers geheel getal, m: aantal decimalen) Als Formaat = datum: 8 Als Formaat = datum/tijd: 14 **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** zie groep **Regels Toelichting** 

## **Attribuutsoort 'Kardinaliteit' van groepattribuutsoort 'Specificatie van eigenschap'** 

|**eigenschap'**||
|---|---|
|**Naam**|Kardinaliteit|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|kardinaliteit|
|**Definitie**|Het aantal mogelijke voorkomens van waarden van deze|
||EIGENSCHAP bij een zaak van  het ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN3|
|**Waardenverzameling**|gehele getallen groter dan 0|
||'N' voor ongelimiteerd|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|



47 

**==> picture [103 x 52] intentionally omitted <==**

|**Aanduiding gebeurtenis**|Nee|
|---|---|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||
|**Toelichting**||



## **Attribuutsoort 'Waardenverzameling' van groepattribuutsoort 'Specificatie van eigenschap'** 

|**Naam**|Waardenverzameling|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|waardeverzameling|
|**Definitie**|Een waarde die deze EIGENSCHAP kan hebben.|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN100|
|**Waardenverzameling**||
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - N|
|**Indicatie authentiek**|zie groep|
|**Regels**||



**Toelichting** 

Door middel van deze attribuutsoort kan een (reeks van) waarde(n) voor de EIGENSCHAP worden gedefinieerd. Bijvoorbeeld: 'J' en 'N'. 

## **Groepattribuutsoort Referentie naar eigenschap** 

|**Naam**|Referentie naar eigenschap|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|referentie|
|**Definitie**|Verwijzing naar de standaard waarin de eigenschap is|
||gespecificeerd|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|



48 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie authentiek Regels** 

Gemeentelijk kerngegeven 

De attributen van deze groepattribuutsoort hebben geen waarden indien één of meer attributen  van de groepattribuutsoort ‘Specificatie van eigenschap’ van waarden zijn voorzien. 

De attributen van de groepattribuutsoort veranderen alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Met de ‘subattributen’ (van deze groepattribuutsoort) Objecttype, Informatiemodel, Namespace, Schemalocatie, X-path element en Entiteittype   wordt een eigenschap gespecificeerd door te refereren naar een berichtenmodel cq. namespace en, bij voorkeur ook, een informatiemodel. Dit vindt alleen plaats als de eigenschap niet gespecificeerd is door middel van het groepattribuutsoort  ‘Specificatie van eigenschap’. 

Met de naam van de eigenschap zijn de metagegevens van de eigenschap (herkomst, formaat, waardenverzameling e.d.) te ontlenen aan het desbetreffende informatiemodel. 

De specificatie dwingt niet af dat er persé sprake moet zijn van een informatiemodel. Wel is een consequentie dat er een XML-schema is waarin de, bij een zaaktype te specificeren, eigenschap is opgenomen. Verwijzen naar zowel een informatie- als een berichtenmodel is evenwel een waarborg voor een robuuste gegevensuitwisseling. 

## **Attribuutsoort 'Objecttype' van groepattribuutsoort 'Referentie naar eigenschap'** 

|**Naam**|Objecttype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|objecttype|
|**Definitie**|De naam van het objecttype waarbij de eigenschap is|
||gemodelleerd in het informatiemodel waarvan het objecttype|
||deel uit maakt.|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN40|
|**Waardenverzameling**|Letters, cijfers, spaties en liggende streepjes|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||



**Toelichting** 

Het betreft het objecttype, in het desbetreffende informatiemodel, waarbij de eigenschap als attribuut is opgenomen cq. gemodelleerd. 

## **Attribuutsoort 'Informatiemodel' van groepattribuutsoort 'Referentie naar eigenschap'** 

**Naam** Informatiemodel 

49 

**==> picture [103 x 52] intentionally omitted <==**

**Herkomst** KING **Code XML-tag** informatiemodel **Definitie** De naam en de versie van het informatiemodel waarin de eigenschap is gemodelleerd. **Herkomst definitie** KING **Datum opname** 11 januari 2014 **Formaat** AN80 **Waardenverzameling** Letters, cijfers en liggende streepjes **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** zie groep **Regels Toelichting** 

Het betreft het informatiemodel waarin de eigenschap als attribuut is gemodelleerd. 

## **Attribuutsoort 'Namespace' van groepattribuutsoort 'Referentie naar eigenschap'** 

|**Naam**|Namespace|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|namespace|
|**Definitie**|De naam van het schema waarin de eigenschap is|
||opgenomen.|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN200|
|**Waardenverzameling**|Alle uri’s van gepubliceerde xml-schema’s|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||
|**Toelichting**||



Het XML-schema is afgeleid van het eerder gespecificeerde informatiemodel  waarin de eigenschap is opgenomen. Het betreft een reeds bestaand xml-schema of een specifiek voor de zaaktypecatalogus of het zaaktype opgesteld xml-schema. 

## **Attribuutsoort 'Schemalocatie' van groepattribuutsoort 'Referentie naar eigenschap'** 

**Naam** Schemalocatie 

50 

**==> picture [103 x 52] intentionally omitted <==**

|**Herkomst**|KING|
|---|---|
|**Code**||
|**XML-tag**|schemalocatie|
|**Definitie**|De locatie van het XML-schema behorend bij de Namespace|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN200|
|**Waardenverzameling**||
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||
|**Toelichting**||



Betreft de locatie van het XML-schema behorend bij de Namespace waarin het element cq. de eigenschap is gedefinieerd. 

## **Attribuutsoort 'X-path element' van groepattribuutsoort 'Referentie naar** 

## **eigenschap'** 

|**Naam**|X-path element|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|pathElement|
|**Definitie**|De naam van de eigenschap en het pad daarnaar toe in het|
||XML-schema behorend bij de namespace.|
|**Herkomst definitie**|KING|
|**Datum opname**|11 januari 2014|
|**Formaat**|AN255|
|**Waardenverzameling**|Alle elementen in het xml-schema zoals aangeduid met|
||Namespace.|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**||
|**Toelichting**||



Het element is de ‘XML-vertaling’ van de Eigenschap in het Informatiemodel en is opgenomen in het XML-schema dat onder Namespace genoemd is. 

Het voorzien in een waarde van deze attribuutsoort is optioneel. Indien geen waarde aanwezig is, dan zijn alle elementen die deel uit maken van de Namespace zaaktypespecifieke eigenschappen. Deze hoeven dan dus niet per element cq. per eigenschap gespecificeerd te worden. 

## **Attribuutsoort 'Entiteittype' van groepattribuutsoort 'Referentie naar** 

51 

**==> picture [103 x 52] intentionally omitted <==**

## **eigenschap'** 

**Naam** Entiteittype **Herkomst** KING **Code XML-tag** entiteittype **Definitie** De naam van de XML-constructie in het XML-schema behorend bij de namespace die afgeleid is van de naam van het objecttype en waarin de eigenschap is opgenomen. **Herkomst definitie** KING **Datum opname** 11 januari 2014 **Formaat** AN80 **Waardenverzameling** Alle complex types in het xml-schema zoals aangeduid met Namespace. **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** zie groep **Regels Toelichting** 

Het Entiteittype is de ‘XML-vertaling’ van het Objecttype in het Informatiemodel en naar een ComplexType in het XML-schema dat onder Namespace genoemd is. 

Voor een eenduidige referentie van de eigenschap in een XML-schema is veelal het complextype benodigd waarmee duidelijk wordt van welk object de eigenschap een kenmerk is. Bijvoorbeeld, de eigenschap ‘Oppervlakte’ kan een kenmerk zijn van de objecttypen Perceel en van Gebouw welke zich als complex types in hetzelfde XML-schema kunnen bevinden. 

## **Attribuutsoort Toelichting** 

|**Attribuutsoort Toelichting**||
|---|---|
|**Naam**|Toelichting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een toelichting op deze EIGENSCHAP en het belang hiervan voor|
||zaken van dit ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|



52 

**==> picture [103 x 52] intentionally omitted <==**

historie) op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

## **Attribuutsoort Datum begin geldigheid eigenschap** 

|**Naam**|Datum begin geldigheid eigenschap|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop de EIGENSCHAP is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2013|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van het gerelateerde|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer de eigenschap bij het zaaktype bestaat en toegepast kan worden. Dit vindt plaats met ingang van een versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Attribuutsoort Datum einde geldigheid eigenschap** 

|**Naam**|Datum einde geldigheid eigenschap|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop de EIGENSCHAP is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2013|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan of gelegen na de datum zoals opgenomen|
||onder 'Datum begin geldigheid eigenschap’.|
||De datum is gelijk aan de dag voor een Versiedatum van het|



53 

**==> picture [103 x 52] intentionally omitted <==**

gerelateerde zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer de eigenschap niet meer bestaat en niet meer toegepast kan worden bij het zaaktype. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Relatiesoort is van** 

**Naam** is van **Gerelateerd objecttype** ZAAKTYPE **Indicatie kardinaliteit** 1 **Herkomst** KING **Code Definitie** Het ZAAKTYPE van de ZAAKen waarvoor deze EIGENSCHAP van belang is. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels Toelichting** 

## **6.1.4. Objecttype INFORMATIEOBJECTTYPE** 

|**Attribuutsoort Informatieobjecttype-omschrijving**|**Attribuutsoort Informatieobjecttype-omschrijving**|
|---|---|
|**Naam**|Informatieobjecttype-omschrijving|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijving|
|**Definitie**|Omschrijving van de aard van informatieobjecten van dit|
||INFORMATIEOBJECTTYPE.|
|**Herkomst definitie**|KING op basis van de Dublin Core|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**||
|**Toelichting**||



Het gaat hier om een korte omschrijving van de aard van van gelijksoortige 

54 

**==> picture [103 x 52] intentionally omitted <==**

informatieobjecttypen, ook wel documentsoort genoemd. Voorbeelden: Bouwaanvraag, Kapvergunning, Taxatieverslag, Geboorte-akte. Het betreft het Dublin Core metadata-element ‘Subject’ met als toelichting: Typically, Subject will be expressed as keywords, key phrases, or classification codes that describe a topic of the resource. Recommended best practice is to select a value from a controlled vocabulary or formal classification scheme. Aan te bevelen is dus om aan te sluiten bij een (landelijke) domeinwaardencatalogus zoals gemodelleerd met informatieobjecttype-omschrijving generiek 

Let op dat het hier alleen om het onderwerp gaat; trefwoorden worden vastgelegd in Informatieobjecttypetrefwoord. 

|**Attribuutsoort Informatieobjecttype-omschrijving generiek**|**Attribuutsoort Informatieobjecttype-omschrijving generiek**|
|---|---|
|**Naam**|Informatieobjecttype-omschrijving generiek|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijvingGeneriek|
|**Definitie**|Algemeen gehanteerde omschrijving van het|
||INFORMATIEOBJECTTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|INFORMATIEOBJECTTYPE-OMSCHRIJVING GENERIEK|
|**Waardenverzameling**|zie referentielijst  INFORMATIEOBJECTTYPE-OMSCHRIJVING|
||GENERIEK|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van gelijksoortige documenten, ook wel documentnaam genoemd, zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Informatieobjecttype-omschrijving. De domeinwaarden zijn opgenomen in een specifieke referentielijst. De daarin aanwezige waarden zijn overgenomen uit de NEN2084 en aangevuld met voor de overheid (als geheel) relevante informatieobjecttypen. 

## **Attribuutsoort Informatieobjectcategorie** 

|**Naam**|Informatieobjectcategorie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|categorie|
|**Definitie**|Typering van de aard van informatieobjecten van dit|
||INFORMATIEOBJECTTYPE.|
|**Herkomst definitie**|KING op basis van de Dublin Core|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|



55 

**==> picture [103 x 52] intentionally omitted <==**

|**Waardenverzameling**|alle alfanumerieke tekens|
|---|---|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



## **Toelichting** 

Voorbeelden hiervan zijn ‘Vergunning’, ‘Subsidie-aanvraag’, ‘Onderzoeksrapport’, Besluit. Het betreft het Dublin Core metadata-element ‘Type’ met als toelichting: Type includes terms describing general categories, functions, genres, or aggregation levels for content. Recommended best practice is to select a value from a controlled vocabulary (for example, the DCMI Type Vocabulary (DCT)). To describe the physical or digital manifestation of the resource, use the Format element. 

Aan te bevelen is dus om te komen tot een (landelijke) domeinwaardenverzameling. 

## **Attribuutsoort Informatieobjecttypetrefwoord** 

|**Naam**|Informatieobjecttypetrefwoord|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|trefwoord|
|**Definitie**|Trefwoord(en) waarmee informatieobjecten van het|
||INFORMATIEOBJECTTYPE kunnen worden gekarakteriseerd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN30|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - N|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



**Toelichting** 

**Attribuutsoort Vertrouwelijkheidaanduiding** 

|**Naam**|Vertrouwelijkheidaanduiding|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|vertrouwelijkAanduiding|



56 

**==> picture [103 x 52] intentionally omitted <==**

**Definitie** Aanduiding van de mate waarin informatieobjecten van dit INFORMATIEOBJECTTYPE voor de openbaarheid bestemd zijn. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Formaat** AN20 **Waardenverzameling** ZEER GEHEIM (indien kennisnemen door niet gerechtigden zeer ernstige schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) GEHEIM (indien kennisnemen door niet gerechtigden ernstige schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) CONFIDENTIEEL (indien kennisnemen door niet gerechtigden schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) VERTROUWELIJK (indien kennisnemen door niet gerechtigden nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) ZAAKVERTROUWELIJK (indien kennisnemen door anderen dan betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) INTERN (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) BEPERKT OPENBAAR (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties) OPENBAAR (in alle andere gevallen) 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|Deze attribuutsoort prevaleert boven de|
||Vertrouwelijkheidaanduiding van het ZAAKTYPE. Indien geen|
||Vertrouwelijkheidaanduiding voor het INFORMATIEOBJECTTYPE is|
||ingesteld, wordt deze bepaald door de|
||Vertrouwelijkheidaanduiding van het ZAAKTYPE.|
||De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|
|**Toelichting**||



57 

**==> picture [103 x 52] intentionally omitted <==**

Middels deze attribuutsoort kan worden vastgelegd in welke mate informatieobjecten van dit INFORMATIEOBJECTTYPE bestemd zijn voor de openbaarheid. Zo kan een ZAAK waarvoor in het ZAAKTYPE is vastgelegd dat de Vertrouwelijkheidaanduiding 'Openbaar' is, toch 

informatieobjecten bevatten die op basis van hun INFORMATIEOBJECTTYPE niet - samen met de openbare zaakinformatie - 'Openbaar' worden gemaakt. Denk bijvoorbeeld aan privacygevoelige informatie zoals een Bibob-advies. 

De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst bijzondere informatie (VIRBI). 

## **Attribuutsoort Model** 

|**Naam**|Model|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|model|
|**Definitie**|De URL naar het model / sjabloon dat wordt gebruikt voor de|
||creatie van informatieobjecten van dit INFORMATIEOBJECTTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|anyURL|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - N|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan eenzelfde Versiedatum|
||van de gerelateerde zaaktypen.|



## **Toelichting** 

Voor veel informatieobjecttypen worden standaardmodellen / -sjablonen gedefinieerd die worden gebruikt voor de creatie van nieuwe documenten. Deze attribuutsoort relateert dergelijke sjablonen aan - de creatie van documenten van - dit informatieobjecttype. 

## **Attribuutsoort Toelichting** 

|**Naam**|Toelichting|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een eventuele toelichting op dit INFORMATIEOBJECTTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|



58 

**==> picture [103 x 52] intentionally omitted <==**

**Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan eenzelfde Versiedatum van de gerelateerde zaaktypen. 

## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een toelichting te geven op dit INFORMATIEOBJECTTYPE. Hier kan bijvoorbeeld een beschrijving worden gegeven van de betekenis van het informatieobjecttype en de aard van de documenten die ertoe behoren. 

## **Attribuutsoort Datum begin geldigheid informatieobjecttype** 

|**Naam**|Datum begin geldigheid informatieobjecttype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het INFORMATIEOBJECTTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van een gerelateerd|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het informatieobjecttype bestaat en toegepast kan worden. Dit vindt plaats met ingang van een versie van het zaaktype dat als eerste aan het informatieobjecttype wordt gerelateerd. 

## **Attribuutsoort Datum einde geldigheid informatieobjecttype** 

|**Naam**|Datum einde geldigheid informatieobjecttype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop het INFORMATIEOBJECTTYPE is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|



59 

**==> picture [103 x 52] intentionally omitted <==**

**Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De datum is gelijk aan of gelegen na de datum zoals opgenomen onder 'Datum begin geldigheid informatieobjecttype’. De datum is gelijk aan de dag voor een Versiedatum van een gerelateerd zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het informatieobjecttype niet meer bestaat en niet meer toegepast kan worden. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het als laatste gerelateerde zaaktype. 

## **Relatiesoort maakt deel uit van** 

|**Naam**|maakt deel uit van|
|---|---|
|**Gerelateerd objecttype**|CATALOGUS|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De CATALOGUS waartoe dit INFORMATIEOBJECTTYPE behoort.|
|**Herkomst definitie**|KING|
|**Datum opname**|28 januari 2013|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**||
|**Toelichting**||



## **6.1.5. Objecttype RESULTAATTYPE** 

## **Attribuutsoort Resultaattypeomschrijving** 

|**Naam**|Resultaattypeomschrijving|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijving|
|**Definitie**|Omschrijving van de aard van resultaten van het RESULTAATTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|



60 

**==> picture [103 x 52] intentionally omitted <==**

## **Regels** 

- 

## **Toelichting** 

Het gaat hier om de benaming van resultaten (van uitvoering van zaken van het betreffende zaaktype) zoals de organisatie die hanteert. Deze kunnen afwijken van hetgeen standaard is voor het domein cq. de ZTC die voor dat domein is opgesteld. Aan te bevelen is zoveel mogelijk aan te sluiten bij die standaard zijnde de waarden in ‘Resultaattype-omschrijving generiek’. 

## **Attribuutsoort Resultaattypeomschrijving generiek** 

|**Naam**|Resultaattypeomschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijvingGeneriek|
|**Definitie**|Algemeen gehanteerde omschrijving van de aard van resultaten|
||van het RESULTAATTYPE.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van het resultaat, zoals deze landelijk wordt toegepast voor zaken van het betreffende ZAAKTYPE en is opgenomen in de ZTC voor het betreffende domein. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Resultaattypeomschrijving. 

Het gaat om resultaten zoals 'verleend', 'toegekend', 'afgewezen', 'verwerkt', 'gegrond', 'ongegrond', 'geweigerd', 'niet nodig', 'ontvankelijk', 'niet ontvankelijk', 'vastgesteld', 'niet vastgesteld'. 

## **Attribuutsoort Selectielijstklasse** 

|**Naam**|Selectielijstklasse|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|selectielijstklasse|
|**Definitie**|Verwijzing naar de, voor het archiefregime bij het|
||RESULTAATTYPE relevante, passage in de Selectielijst|
||Archiefbescheiden van de voor het ZAAKTYPE verantwoordelijke|
||overheidsorganisatie.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN500|
|**Waardenverzameling**|de aanduidingen van de passages cq. klassen in de gehanteerde|



61 

**==> picture [103 x 52] intentionally omitted <==**

||selectielijst.|
|---|---|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Bij gemeenten gaat het om de aanduidingen van de categorie in de Selectielijst waarin per categorie de archiefactietermijn wordt vermeld van de daartoe behorende soorten documenten. In niet-gemeentelijke selectielijsten wordt soms een ander begrip dan categorie gehanteerd. Vandaar dat we hier het begrip ‘klasse’ hanteren. 

## **Attribuutsoort Archiefnominatie** 

|**Naam**|Archiefnominatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|archiefnominatie|
|**Definitie**|Aanduiding die aangeeft of ZAAKen met een resultaat van dit|
||RESULTAATTYPE blijvend moeten worden bewaard of (op termijn)|
||moeten worden vernietigd .|
|**Herkomst definitie**|KING, o.b.v. Archiefwet 1995|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN16|
|**Waardenverzameling**|Blijvend bewaren|
||Vernietigen|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

De attribuutsoort specificeert het ‘archiefregime’ voor de zaakdossiers van het ZAAKTYPE waarvan de zaak het desbetreffende RESULTAATTYPE heeft. Het archiefregime van zaken van een ZAAKTYPE verschilt naar gelang het resultaat van die zaken. 

In het geval van vernietigen wordt het zaakdossier na enige tijd vernietigd. In het geval van blijvend bewaren wordt het zaakdossier na enige tijd overgebracht naar een archiefbewaarplaats (de in art. 12 van de Archiefwet 1995 bepaalde algemene termijn is 20 jaar). Door middel van de attribuutsoort Archiefactietermijn wordt gespecificeerd na verloop van hoeveel tijd wordt overgegaan tot vernietiging resp. overbrenging. 

62 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Archiefactietermijn** 

|**Naam**|Archiefactietermijn|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|archiefactietermijn|
|**Definitie**|De termijn waarna het zaakdossier (de ZAAK met alle|
||bijbehorende INFORMATIEOBJECTen) van een ZAAK met een|
||resultaat van dit RESULTAATTYPE vernietigd of overgebracht|
||(naar een archiefbewaarplaats) moet worden.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|N4|
|**Waardenverzameling**|0-9999 maanden|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Of sprake is van vernietigen of overbrengen (in het geval van blijvend bewaren) is vastgelegd met de attribuutsoort Archiefnominatie. 

De datum waarop de termijn start, is afhankelijk van de waarde van Brondatum archiefprocedure. Let op: de eenheid waarin de Archiefactietermijn wordt uitgedrukt, is gewijzigd naar maanden (in plaats van jaren, zoals was gedefinieerd in versie 1.0 van de Zaaktypecatalogus). Reden hiervoor is dat de archiefactietermijn in selectielijsten niet altijd is gesteld op gehele jaren. De algemene termijn voor overbrenging is 20 jaar cq. 240 maanden. 

## **Attribuutsoort Brondatum archiefprocedure** 

|**Naam**|Brondatum archiefprocedure|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|brondatumProcedure|
|**Definitie**|Aanduiding van de brondatum voor de start van de|
||Archiefactietermijn van het zaakdossier.|
|**Herkomst definitie**|ZTC 1.0, gewijzigd door KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|- 'afgehandeld': de termijn start op de datum waarop de zaak is|
||afgehandeld (ZAAK.Einddatum in het RGBZ),|
||- 'ingangsdatum besluit': de termijn start op de datum waarop het|
||besluit van kracht wordt (BESLUIT.Ingangsdatum in het RGBZ),|
||-  'vervaldatum besluit': de termijn start op de dag na de datum|
||waarop het besluit vervalt (BESLUIT.Vervaldatum in het RGBZ),|



63 

**==> picture [103 x 52] intentionally omitted <==**

- ‘eigenschap’: de termijn start op de datum die vermeld is in een zaaktype-specifieke eigenschap (zijnde een ‘datumveld’); -  'ander datumkenmerk': de termijn start op de datum die in een ander datumveld bij de zaak of bij een gerelateerde zaak (voorafgaand, volgend op of deelzaak)  is vastgelegd. **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** Als de waarde van deze attribuutsoort 'eigenschap' is, dient middels de relatiesoort ‘heeft voor Brondatum archiefprocedure relevante EIGENSCHAP’ te worden vastgelegd welke EIGENSCHAP de brondatum bevat. 

Als de waarde van deze attrIbuutsoort ‘ander datumkenmerk’ is, dient middels de attribuutsoort Toelichting te worden beschreven welk datumveld de brondatum bevat. De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Het betreft het ‘datumveld’ waarvan de daarin vermelde datum als startdatum van de Archiefactietermijn genomen moet worden. Meerdere datumvelden komen hiervoor in aanmerking. Deze specificeren we onder ‘Waardenverzameling’. In het geval van ‘ander datumkenmerk’ zal de einddatum van de archiefactietermijn bij een zaak handmatig bepaald moeten worden, in andere gevallen kan deze berekend worden. 

Let op: deze attribuutsoort had in de ZTC 1.0 de naam 'Ingang V-termijn'. 

## **Attribuutsoort Toelichting** 

|**Attribuutsoort Toelichting**||
|---|---|
|**Naam**|Toelichting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een toelichting op dit RESULTAATTYPE en het belang hiervan voor|
||ZAAKen waarin een Resultaat van dit RESULTAATTYPE wordt|
||geselecteerd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|



64 

**==> picture [103 x 52] intentionally omitted <==**

## **Regels** 

De attribuutsoort moet van een waarde voorzien zijn indien de attribuutsoort ‘Brondatum archiefprocedure’ de waarde ‘ander datumkenmerk’ heeft. 

De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Naast een toelichting op het resultaattype en het belang hiervan wordt hierin (tekstueel) aangegeven op basis van welk datumveld de brondatum voor de archiefprocedure  bepaald wordt indien dit een 'ander datumkenmerk' is zoals gespecificeerd bij ’Brondatum archiefprocedure’. 

## **Attribuutsoort Datum begin geldigheid resultaattype** 

|**Naam**|Datum begin geldigheid resultaattype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het RESULTAATTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van het gerelateerde|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het resultaattype bestaat en toegepast kan worden. Dit vindt plaats met ingang van een versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Attribuutsoort Datum einde geldigheid resultaattype** 

|**Naam**|Datum einde geldigheid resultaattype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop het RESULTAATTYPE is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||



65 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De datum is gelijk aan of gelegen na de datum zoals opgenomen onder 'Datum begin geldigheid resultaattype’. De datum is gelijk aan de dag voor een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het resultaattype niet meer bestaat en niet meer toegepast kan worden. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Relatiesoort bepaalt afwijkend archiefregime van** 

|**Naam**|bepaalt afwijkend archiefregime van|
|---|---|
|**Gerelateerd objecttype**|ZAAK-INFORMATIEOBJECT-TYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|Informatieobjecten van een ZAAKINFORMATIEOBJECTTYPE bij|
||zaken van een ZAAKTYPE waarvan, op grond van resultaten van|
||een RESULTAATTYPE bij dat ZAAKTYPE,  de|
||archiveringskenmerken afwijken van de archiveringskenmerken|
||van het ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2103|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**||
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Met deze relatiesoort kan een afwijkend archiefregime (t.o.v. het ZAAKTYPE als geheel) vastgelegd worden voor documenten van een ZAAKINFORMATIEOBJECTTYPE bij het ZAAKTYPE. Zie verder de toelichting bij RESULTAATTYPE. 

Kenmerken van deze relatiesoort (de t.o.v. het RESULTTAATTYPE afwijkende 

archiveringskenmerken) zijn gemodelleerd met de relatieklasse ZAAK-INFORMATIEOBJECT-TYPE ARCHIEFREGIME. 

## **Relatiesoort heeft verplichte** 

**Naam** heeft verplichte **Gerelateerd objecttype** ZAAKOBJECTTYPE **Indicatie kardinaliteit** 0..* **Herkomst** KING 

66 

**==> picture [103 x 52] intentionally omitted <==**

**Code Definitie** De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan ZAAKen van dit ZAAKTYPE voordat een resultaat van dit RESULTAATTYPE kan worden gezet. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De relatiesoort ontstaat en eindigt alleen (materiële historie) op een datum die gelijk is resp. een dag ligt voor een Versiedatum van het gerelateerd zaaktype. 

## **Toelichting** 

Met behulp van deze relatiesoort kan worden geconfigureerd dat bij het zetten van een resultaat van een bepaald RESULTAATTYPE een OBJECT van ZAAKOBJECTTYPE aan de ZAAK moet zijn gerelateerd. 

## **Relatiesoort heeft verplichte** 

|**Relatiesoort heeft verplichte**||
|---|---|
|**Naam**|heeft verplichte|
|**Gerelateerd objecttype**|ZAAK-INFORMATIEOBJECT-TYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De INFORMATIEOBJECTTYPEn die verplicht aanwezig moeten zijn|
||in het zaakdossier van ZAAKen van dit ZAAKTYPE voordat een|
||resultaat van dit RESULTAATTYPE kan worden gezet.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Met behulp van deze relatiesoort kan worden geconfigureerd dat bij het zetten van een resultaat van een bepaald RESULTAATTYPE een INFORMATIEOBJECT van INFORMATIEOBJECTTYPE in het zaakdossier aanwezig moet zijn. Denk aan een document van INFORMATIEOBJECTTYPE 'Besluit' als in een collectevergunningzaak een resultaat van ‘Resultaattypeomschrijving generiek’ wordt gezet met de waarde 'verleend' of 'geweigerd'. Als in die zaak een resultaat van 

‘Resultaattypeomschrijving generiek’ wordt gezet met de waarde 'niet nodig', is 'Besluit' geen verplicht informatieobjecttype, maar bijvoorbeeld wel het informatieobjecttype 'Mededeling' waarin de aanvrager wordt geïnformeerd over het niet nodig zijn van een vergunning. 

**Relatiesoort heeft voor Brondatum archiefprocedure relevante** 

67 

**==> picture [103 x 52] intentionally omitted <==**

|**Naam**|heeft voor Brondatum archiefprocedure relevante|
|---|---|
|**Gerelateerd objecttype**|EIGENSCHAP|
|**Indicatie kardinaliteit**|0..1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De EIGENSCHAP die bepalend is voor het moment waarop de|
||Archiefactietermijn start voor een ZAAK met een resultaat van dit|
||RESULTAATTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|Een relatie van deze relatiesoort moet aanwezig zijn en is alleen|
||aanwezig indien de attribuutsoort ‘Brondatum archiefprocedure’|
||de waarde ‘eigenschap’ heeft.|
||De gerelateerde EIGENSCHAP moet van het formaat ‘Datum’ of|
||‘Datum/tijd’ zijn.|
||De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Het datumveld dat bepalend is voor de start van de archiefactietermijn wordt gespecificeerd met de attribuutsoort ‘Brondatum archiefprocedure’. Indien dit een zaaktype-specifieke eigenschap is, dan wordt met deze relatie aangeduid om welke eigenschap het gaat. 

Denk bijvoorbeeld aan eigenschappen als 'Datum geboorte' bij een geboorteaangifte, 'Datum uit dienst' bij pensionering, et cetera. 

## **Relatiesoort is relevant voor** 

|**Relatiesoort is relevant voor**||
|---|---|
|**Naam**|is relevant voor|
|**Gerelateerd objecttype**|ZAAKTYPE|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|Het ZAAKTYPE van ZAAKen waarin resultaten van dit|
||RESULTAATTYPE bereikt kunnen worden.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**||
|**Toelichting**||



68 

**==> picture [103 x 52] intentionally omitted <==**

Niet elk RESULTAATTYPE is relevant voor ZAAKen van een ZAAKTYPE. Deze relatiesoort is opgenomen om bij een ZAAKTYPE vast te kunnen leggen welke deelverzameling RESULTAATTYPEn relevant kan zijn voor ZAAKen van dit ZAAKTYPE en behandelaren zo een overzichtelijke lijst met resultaattypen te kunnen presenteren. 

## **Relatiesoort leidt tot** 

**Naam** leidt tot **Gerelateerd objecttype** BESLUITTYPE **Indicatie kardinaliteit** 0..* **Herkomst** KING **Code Definitie** Het BESLUITTYPE van besluiten die gepaard gaan met resultaten van het RESULTAATTYPE. **Herkomst definitie** KING **Datum opname** 31 december 2012 **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De relatiesoort ontstaat en eindigt alleen (materiële historie) op een datum die gelijk is resp. een dag ligt voor een Versiedatum van het gerelateerd zaaktype. 

## **Toelichting** 

Een besluit is altijd het gevolg van, of gaat gepaard met het resultaat van een zaak. Met deze relatie worden deze verbanden op type-niveau gelegd. 

## **6.1.6. Objecttype ROLTYPE** 

## **Attribuutsoort Roltypeomschrijving** 

|**Naam**|Roltypeomschrijving|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijving|
|**Definitie**|Omschrijving van de aard van de ROL.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



69 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Roltypeomschrijving generiek** 

**Naam** Roltypeomschrijving generiek **Herkomst** KING **Code XML-tag** omschrijvingGeneriek **Definitie** Algemeen gehanteerde omschrijving van de aard van de ROL. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Formaat** AN20 **Waardenverzameling** Adviseur: Kennis in dienst stellen van de behandeling van (een deel van) een zaak. Behandelaar: De vakinhoudelijke behandeling doen van (een deel van) een zaak. Belanghebbende: Vanuit eigen en objectief belang rechtstreeks betrokken zijn bij de behandeling en/of de uitkomst van een zaak. Nb. De formulering is afgeleid van de belanghebbende in de AWB. Beslisser: Nemen van besluiten die voor de uitkomst van een zaak noodzakelijk zijn. Initiator: Aanleiding geven tot de start van een zaak. Nb. Indien het gaat om dienstverlening aan burgers en bedrijven wordt ook wel de term ‘klant’ gehanteerd. Met het oog op andere dan dienstverleningszaken is hier gekozen voor de meer algemene term. 

Klantcontacter: Het eerste aanspreekpunt zijn voor vragen van burgers en bedrijven in het kader van de dienstverlening door de organisatie aan burgers en bedrijven. Nb. Met betrekking tot het zaakgericht werken betreft dit veelal het verzorgen van de intake van een vraag naar een product of dienst, het informeren over de voortgang van de behandeling van de zaak en het leveren van de uitkomst van de zaak. Zaakcoördinator: Er voor zorg dragen dat de behandeling van de zaak in samenhang uitgevoerd wordt conform de daarover gemaakte afspraken. 

|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van de rol, zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Roltypeomschrijving. 

**Attribuutsoort Soort betrokkene** 

70 

**==> picture [103 x 52] intentionally omitted <==**

|**Naam**|Soort betrokkene|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|soortBetrokkene|
|**Definitie**|De (soort) betrokkene die een rol van dit roltype mag uitoefenen.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - N|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Deze attribuutsoort heeft primair een documentatiefunctie en beschrijft welke (soort) betrokkene(n) een ROL van dit ROLTYPE kunnen uitoefenen. 

## **Attribuutsoort Datum begin geldigheid roltype** 

|**Naam**|Datum begin geldigheid roltype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het ROLTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2013|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van het gerelateerde|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het roltype bestaat en toegepast kan worden bij het zaaktype. Dit vindt plaats met ingang van een versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Attribuutsoort Datum einde geldigheid roltype** 

**Naam** Datum einde geldigheid roltype 

71 

**==> picture [103 x 52] intentionally omitted <==**

**Herkomst** KING **Code XML-tag** einddatumObject **Definitie** De datum waarop het ROLTYPE is opgeheven. **Herkomst definitie** KING **Datum opname** 23 september 2013 **Formaat** OnvolledigeDatum **Waardenverzameling Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De datum is gelijk aan of gelegen na de datum zoals opgenomen onder 'Datum begin geldigheid roltype’. De datum is gelijk aan de dag voor een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het roltype niet meer bestaat en niet meer toegepast kan worden bij het zaaktype. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Relatiesoort is van** 

|**Relatiesoort is van**||
|---|---|
|**Naam**|is van|
|**Gerelateerd objecttype**|ZAAKTYPE|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De ROLTYPEn waarin BETROKKENEn een ROL kunnen uitoefenen|
||in ZAAKen van dit ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



Elke zaakbehandelende organisatie is vrij in het definiëren van ROLTYPEn die passen bij het zaakof procestype: subsidieaanvrager, adviesopsteller, inspecteur, juridisch adviseur, vergunningbehandelaar, bezwaarindiener, klager, etcetera. 

## **Relatiesoort mag zetten** 

**Naam** mag zetten **Gerelateerd objecttype** STATUSTYPE 

**==> picture [103 x 52] intentionally omitted <==**

|**Indicatie kardinaliteit**|0..*|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De STATUSTYPEn die een betrokkene in een rol van dit ROLTYPE|
||mag zetten.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Een status kan alleen gezet worden door een betrokkene, zijnde een organisatorische eenheid of medewerker, niet door een willekeurig andere betrokkene. 

## **6.1.7. Objecttype STATUSTYPE** 

|**Attribuutsoort Statustype-omschrijving**|**Attribuutsoort Statustype-omschrijving**|
|---|---|
|**Naam**|Statustype-omschrijving|
|**Herkomst**|GFO Zaken 2004|
|**Code**|0002|
|**XML-tag**|omschrijving|
|**Definitie**|Een korte, voor de initiator van de zaak relevante, omschrijving|
||van de aard van de STATUS van zaken van een ZAAKTYPE.|
|**Herkomst definitie**|GFO Zaken 2004, aangepast door KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



Het betreft de attribuutsoort Status.Statusomschrijving in het GFO Zaken 2004 met dien verstande dat deze nu van toepassing is per Statustype, d.w.z. voor alle daarbij te registreren Statussen, en niet per status bepaald kan worden. 

Voorbeelden hiervan zijn “Aanvraag ontvangen”, “Äanvraag ontvankelijk”, “Aanvraag in behandeling”, “Voorstel bij B&W” en “Aanvraag afgehandeld”. 

## **Attribuutsoort Statustype-omschrijving generiek** 

**Naam** Statustype-omschrijving generiek 

73 

**==> picture [103 x 52] intentionally omitted <==**

|**Herkomst**|KING|
|---|---|
|**Code**||
|**XML-tag**|omschrijvingGeneriek|
|**Definitie**|Algemeen gehanteerde omschrijving van de aard van STATUSsen|
||van het STATUSTYPE|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van de status zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Statustypeomschrijving. 

## **Attribuutsoort Statustypevolgnummer** 

|**Naam**|Statustypevolgnummer|
|---|---|
|**Herkomst**|GFO Zaken 2004|
|**Code**|0001|
|**XML-tag**|volgnummer|
|**Definitie**|Een volgnummer voor statussen van het STATUSTYPE binnen een|
||zaak.|
|**Herkomst definitie**|KING op basis van GFO Zaken 2004|
|**Datum opname**|1 juni 2008|
|**Formaat**|N4|
|**Waardenverzameling**|0001 - 9999|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Een zaak van een bepaald ZAAKTYPE doorloopt achtereenvolgens de statussen overeenkomstig de aan het ZAAKTYPE gerelateerde STATUSTYPEN. Het volgnummer legt de volgorde vast waarin de statussen doorlopen worden 

74 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Doorlooptijd status** 

|**Naam**|Doorlooptijd status|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|doorlooptijd|
|**Definitie**|De door de zaakbehandelende organisatie(s) gestelde norm voor|
||de doorlooptijd voor het bereiken van statussen van dit|
||STATUSTYPE bij het desbetreffende ZAAKTYPE, vanaf het bereiken|
||van de voorafgaande status|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|N3|
|**Waardenverzameling**|1-999 kalenderdagen|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

De zaakbehandelende organisatie(s) bepaalt zelf de hardheid van deze norm: verwachting, servicenorm of harde norm. 

De attribuutsoort kent materiële historie zodat bij aanpassing van de doorlooptijd van een statustype bij een zaaktype de ‘oude’ doorlooptijd van toepassing blijft voor afgeronde en onderhanden zaken van dat zaaktype. 

## **Groepattribuutsoort Checklistitem** 

|**Naam**|Checklistitem|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|checklistitem|
|**Definitie**|Te controleren aandachtspunt voorafgaand aan het bereiken|
||van een status van het STATUSTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|31 december 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0..*|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De groepattribuutsoort verandert alleen van waarde|
||(materiële historie) cq. één of meer van de subattributen|



75 

**==> picture [103 x 52] intentionally omitted <==**

veranderen van waarde op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Door één of meer checklistitems op te nemen bij een status, wordt een checklist verkregen met punten waaraan aandacht besteed moet worden teneinde die status te bereiken. 

## **Attribuutsoort 'Itemnaam' van groepattribuutsoort 'Checklistitem'** 

**Naam** Itemnaam **Herkomst** KING **Code XML-tag** checklistitem.naam **Definitie** De betekenisvolle benaming van het checklistitem **Herkomst definitie** KING **Datum opname** 31 december 2012 **Formaat** AN30 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** zie groep **Toelichting** 

## **Attribuutsoort 'Vraagstelling' van groepattribuutsoort 'Checklistitem'** 

**Naam** Vraagstelling **Herkomst** KING **Code XML-tag** checklistitem.vraag **Definitie** Een betekenisvolle vraag waaruit blijkt waarop het aandachtspunt gecontroleerd moet worden. **Herkomst definitie** KING **Datum opname** 31 december 2012 **Formaat** AN255 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** zie groep **Toelichting** 

76 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort 'Verplicht' van groepattribuutsoort 'Checklistitem'** 

**Naam** Verplicht **Herkomst** KING **Code XML-tag** checklistitem.verplicht **Definitie** Het al dan niet verplicht zijn van controle van het aandachtspunt voorafgaand aan het bereiken van de status van het gerelateerde STATUSTYPE. **Herkomst definitie** KING **Datum opname** 31 december 2012 **Formaat** boolean **Waardenverzameling** J, N **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** zie groep **Toelichting** 

**Attribuutsoort 'Toelichting' van groepattribuutsoort 'Checklistitem'** 

**Naam** Toelichting **Herkomst** KING **Code XML-tag** checklistitem.toelichting **Definitie** Beschrijving van de overwegingen bij het controleren van het aandachtspunt **Herkomst definitie** KING **Datum opname** 31 december 2012 **Formaat** AN1000 **Waardenverzameling** alle alfanumerieke tekens. **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** zie groep **Toelichting** 

## **Attribuutsoort Informeren** 

**Naam** Informeren **Herkomst** KING 

77 

**==> picture [103 x 52] intentionally omitted <==**

|**Code**||
|---|---|
|**XML-tag**|informeren|
|**Definitie**|Aanduiding die aangeeft of na het zetten van een STATUS van dit|
||STATUSTYPE de Initiator moet worden geïnformeerd over de|
||statusovergang.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|A1|
|**Waardenverzameling**|J, N|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

## **Attribuutsoort Statustekst** 

|**Attribuutsoort Statustekst**||
|---|---|
|**Naam**|Statustekst|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|statustekst|
|**Definitie**|De tekst die wordt gebruikt om de Initiator te informeren over|
||het bereiken van een STATUS van dit STATUSTYPE bij het|
||desbetreffende ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

## **Attribuutsoort Toelichting** 

**Naam** Toelichting 

78 

**==> picture [103 x 52] intentionally omitted <==**

|**Herkomst**|KING|
|---|---|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een eventuele toelichting op dit STATUSTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een toelichting te geven op dit STATUSTYPE. Hier kan bijvoorbeeld een beschrijving van het procesverloop worden gegeven dat voorafgaat aan het bereiken van deze status. 

## **Attribuutsoort Datum begin geldigheid statustype** 

|**Naam**|Datum begin geldigheid statustype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het STATUSTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van het gerelateerde|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het statustype bestaat en toegepast kan worden. Dit vindt plaats met ingang van een versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Attribuutsoort Datum einde geldigheid statustype** 

**Naam** Datum einde geldigheid statustype 

79 

**==> picture [103 x 52] intentionally omitted <==**

**Herkomst** KING **Code XML-tag** einddatumObject **Definitie** De datum waarop het STATUSTYPE is opgeheven. **Herkomst definitie** KING **Datum opname** 1 oktober 2009 **Formaat** OnvolledigeDatum **Waardenverzameling Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De datum is gelijk aan of gelegen na de datum zoals opgenomen onder 'Datum begin geldigheid statusType’. De datum is gelijk aan de dag voor een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het statustype niet meer bestaat en niet meer toegepast kan worden. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Relatiesoort heeft verplichte** 

|**Relatiesoort heeft verplichte**||
|---|---|
|**Naam**|heeft verplichte|
|**Gerelateerd objecttype**|ZAAK-INFORMATIEOBJECT-TYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De informatieobjecten van de INFORMATIEOBJECTTYPEn van het|
||aan het STATUSTYPE gerelateerde ZAAKTYPE waarvoor geldt dat|
||deze verplicht aanwezig moeten zijn bij een zaak van het|
||gerelateerde ZAAKTYPE voordat de status van dit STATUSTYPE|
||kan worden gezet bij die zaak.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

**Relatiesoort heeft verplichte** 

80 

**==> picture [103 x 52] intentionally omitted <==**

|**Naam**|heeft verplichte|
|---|---|
|**Gerelateerd objecttype**|EIGENSCHAP|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De EIGENSCHAPpen die verplicht een waarde moeten hebben|
||gekregen, voordat een STATUS van dit STATUSTYPE kan worden|
||gezet.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Deze relatiesoort definieert dat bij het zetten van een STATUS van dit STATUSTYPE de EIGENSCHAP een waarde moet hebben. Denk aan het verplicht invullen van de EIGENSCHAP 'Datum evenement' als in een evenementenvergunningzaak een STATUS van STATUSTYPE 'In behandeling genomen' wordt gezet. 

## **Relatiesoort heeft verplichte** 

|**Relatiesoort heeft verplichte**||
|---|---|
|**Naam**|heeft verplichte|
|**Gerelateerd objecttype**|ZAAKOBJECTTYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan|
||ZAAKen van het ZAAKTYPE voordat een STATUS van dit|
||STATUSTYPE kan worden gezet.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het gerelateerd zaaktype.|



## **Toelichting** 

Deze relatiesoort definieert welk(e) objecttype(n) verplicht moet(en) zijn gerelateerd aan een zaak voordat de STATUS van dit STATUSTYPE kan worden gezet. Denk aan het verplicht relateren van een LIGPLAATS, voordat een ZAAK van het ZAAKTYPE 'Ligplaatsvergunningaanvraag behandelen' de STATUS 'In behandeling genomen' kan bereiken. Op deze manier kan worden afgedwongen dat (basis)gegevens die cruciaal zijn voor het verloop van een zaak, op het juiste 

81 

**==> picture [103 x 52] intentionally omitted <==**

moment aan de zaak zijn gerelateerd. 

## **Relatiesoort is van** 

**Naam** is van **Gerelateerd objecttype** ZAAKTYPE **Indicatie kardinaliteit** 1 **Herkomst** KING **Code Definitie** Het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE bereikt kunnen worden. **Herkomst definitie** KING **Datum opname** 1 juni 2008 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid Indicatie authentiek** Gemeentelijk kerngegeven **Regels** 

## **Toelichting** 

De relatiesoort is vooral opgenomen teneinde betrokkenen te kunnen informeren wat de eerstvolgend te bereiken status in een zaak is en binnen welke termijn het bereiken van die status verwacht wordt. 

## **6.1.8. Objecttype ZAAKOBJECTTYPE** 

## **Attribuutsoort Objecttype** 

**Naam** Objecttype **Herkomst** KING **Code XML-tag** objecttype **Definitie** De naam van het objecttype waarop zaken van het gerelateerde ZAAKTYPE betrekking hebben. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Formaat** AN40 **Waardenverzameling** Indien Ander objecttype='N': ANDER NATUURLIJK PERSOON, ANDER BUITENLANDS NIETNATUURLIJK PERSOON, APPARTEMENTSRECHT, BESLUIT, BUURT, ENKELVOUDIG INFORMATIEOBJECT, GEMEENTE, GEMEENTELIJKE OPENBARE RUIMTE, HUISHOUDEN, INGESCHREVEN NIETNATUURLIJK PERSOON, INGEZETENE, INRICHTINGSELEMENT, KADASTRAAL PERCEEL, KUNSTWERKDEEL, LIGPLAATS, MAATSCHAPPELIJKE ACTIVITEIT, MEDEWERKER, NIETINGEZETENE, NUMMERAANDUIDING, OPENBARE RUIMTE, ORGANISATORISCHE EENHEID, OVERIGE ADRESSEERBAAR OBJECT AANDUIDING, OVERIG GEBOUWD OBJECT, OVERIG TERREIN, PAND, SAMENGESTELD INFORMATIEOBJECT, SPOORBAANDEEL, STANDPLAATS, STATUS, TERREINDEEL, VERBLIJFSOBJECT, VESTIGING, WATERDEEL, WEGDEEL, WIJK, WOONPLAATS, WOZDEELOBJECT, WOZ-OBJECT, WOZ-WAARDE, ZAKELIJK RECHT 

82 

**==> picture [103 x 52] intentionally omitted <==**

Indien Ander objecttype='J': alle alfanumerieke tekens 

|**Indicatie materiële historie**|Nee|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



Het kan een in het RGBZ of RSGB onderscheiden objecttype betreffen dan wel een ander objecttype. Als ‘Ander objecttype’ de waarde 'N' (Nee) heeft, dient de naam van een objecttype uit het RSGB of het RGBZ te worden gekozen. Als ‘Ander objecttype’ de waarde 'J' (Ja) heeft, dan heeft deze attribuutsoort de naam van een ander, niet in het RSGB en het RGBZ voorkomend, objecttype dat relevant is voor zaken van het gerelateerde ZAAKTYPE (bijv. 'WIPKIP' of ‘Handhavingsobject’). 

## **Attribuutsoort Ander objecttype** 

|**Naam**|Ander objecttype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|anderobject|
|**Definitie**|Aanduiding waarmee wordt aangegeven of het ZAAKOBJECTTYPE|
||een ander, niet in RSGB en RGBZ voorkomend, objecttype betreft|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1|
|**Waardenverzameling**|- J (Ja; het betreft een objecttype dat niet voorkomt in het RSGB|
||en RGBZ)|
||-N (Nee; het betreft een objecttype uit het RSGB of RGBZ).|



|**Indicatie materiële historie**|Ja|
|---|---|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

## **Attribuutsoort Relatieomschrijving** 

|**Naam**|Relatieomschrijving|
|---|---|
|**Herkomst**|KING|



83 

**==> picture [103 x 52] intentionally omitted <==**

|**Code**||
|---|---|
|**XML-tag**|relatieOmschrijving|
|**Definitie**|Omschrijving van de betrekking van het Objecttype op zaken van|
||het gerelateerde ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Het gaat hier om het duiden van het aard van de betrokkenheid van het objecttype bij zaken van het gerelateerde zaaktype en/of het belang van dat objecttype voor die zaken. 

## **Attribuutsoort Datum begin geldigheid zaakobjecttype** 

|**Naam**|Datum begin geldigheid zaakobjecttype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het ZAAKOBJECTTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2013|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan een Versiedatum van het gerelateerde|
||zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het zaakobjecttype bestaat en toegepast kan worden bij het zaaktype. Dit vindt plaats met ingang van een versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Attribuutsoort Datum einde geldigheid zaakobjecttype** 

|**Naam**|Datum einde geldigheid zaakobjecttype|
|---|---|
|**Herkomst**|KING|



84 

**==> picture [103 x 52] intentionally omitted <==**

|**Code**||
|---|---|
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop het ZAAKOBJECTTYPE is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2013|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan of gelegen na de datum zoals opgenomen|
||onder 'Datum begin geldigheid zaakobjecttype’.|
||De datum is gelijk aan de dag voor een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het zaakobjecttype niet meer bestaat en niet meer toegepast kan worden bij het zaaktype. Dit vindt alleen plaats bij een overgang naar een nieuwe versie van het zaaktype d.w.z. niet op tussenliggende datums. 

## **Relatiesoort is relevant voor** 

|**Relatiesoort is relevant voor**||
|---|---|
|**Naam**|is relevant voor|
|**Gerelateerd objecttype**|ZAAKTYPE|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|Zaken van het ZAAKTYPE waarvoor objecten van dit|
||ZAAKOBJECTTYPE relevant zijn.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|



## **Toelichting** 

‘Relevant’ wil in dit kader zeggen dat informatie over objecten van het Objecttype gebruikt wordt bij de behandeling van zaken van het betreffende zaaktype en/of dat die behandeling kan leiden tot het muteren van die informatie. 

Deze relatiesoort begrenst de objecttypen die kunnen worden gerelateerd aan zaken van dit zaaktype. Zo kunnen foutieve relaties zoveel als mogelijk worden voorkomen: in een zaak die de behandeling van een geboorteaangifte betreft, horen geen - directe - relaties te kunnen worden gelegd naar objecttypen als KUNSTWERKDEEL, MAATSCHAPPELIJKE ACTIVITEIT, et cetera 

## **6.1.9. Objecttype ZAAKTYPE** 

85 

**==> picture [103 x 52] intentionally omitted <==**

## **Attribuutsoort Zaaktype-identificatie** 

|**Naam**|Zaaktype-identificatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|identificatie|
|**Definitie**|Unieke identificatie van het ZAAKTYPE binnen de CATALOGUS|
||waarin het ZAAKTYPE voorkomt.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|N5|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|



## **Toelichting** 

Deze attribuutsoort identificeert een ZAAKTYPE uniek binnen de CATALOGUS waarin het ZAAKTYPE voorkomt, ook als daarin meerdere versies - onderscheiden door Datum begin geldigheid zaaktype en Datum einde geldigheid zaaktype - van een ZAAKTYPE voorkomen. 

## **Attribuutsoort Zaaktype-omschrijving** 

|**Naam**|Zaaktype-omschrijving|
|---|---|
|**Herkomst**|GFO Zaken 2004|
|**Code**|0005|
|**XML-tag**|omschrijving|
|**Definitie**|Omschrijving van de aard van ZAAKen van het ZAAKTYPE.|
|**Herkomst definitie**|GFO Zaken 2004, aangepast door KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|Binnen een CATALOGUS moet de Zaaktype-omschrijving uniek|
||zijn.|
||De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het betreft de gelijknamige attribuutsoort bij Zaak in het GFO Zaken 2004. 

86 

**==> picture [103 x 52] intentionally omitted <==**

Binnen een catalogus heeft elke zaaktype een unieke naam, de Zaaktype-omschrijving. 

## **Attribuutsoort Zaaktype-omschrijving generiek** 

|**Naam**|Zaaktype-omschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|omschrijvingGeneriek|
|**Definitie**|Algemeen gehanteerde omschrijving van de aard van ZAAKen van|
||het ZAAKTYPE|
|**Herkomst definitie**|KING, o.b.v. RGBZ|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|zoals vastgelegd in CATALOGUS.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het gaat hier om een korte omschrijving van de aard van de zaak, ook wel zaaknaam genoemd, zoals deze binnen een Domein wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Zaaktype-omschrijving. De domeinwaarden zijn opgenomen in de CATALOGUS van het betreffende Domein. 

## **Attribuutsoort Zaakcategorie** 

|**Attribuutsoort Zaakcategorie**||
|---|---|
|**Naam**|Zaakcategorie|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|zaakcategorie|
|**Definitie**|Typering van de aard van ZAAKen van het ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN40|
|**Waardenverzameling**|zie Zaaktypecatalogus|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



87 

**==> picture [103 x 52] intentionally omitted <==**

## **Toelichting** 

Het gaat hier om de indeling van zaaktypen naar categorieën zoals Behandelen vergunningaanvraag, Behandelen ontheffingaanvraag en Behandelen subsidie-aanvraag. 

## **Attribuutsoort Doel** 

|**Attribuutsoort Doel**||
|---|---|
|**Naam**|Doel|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|doel|
|**Definitie**|Een omschrijving van hetgeen beoogd is te bereiken met een zaak|
||van dit zaaktype.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een omschrijving te geven van het doel - het gedefinieerde resultaat uit de definitie van een zaak - dat wordt nagestreefd in ZAAKen van dit ZAAKTYPE. Denk aan het beoordelen van een vergunningaanvraag met het oogmerk daarover een besluit te nemen, het opmaken van een akte naar aanleiding van een aangifte, et cetera. 

## **Attribuutsoort Aanleiding** 

|**Attribuutsoort Aanleiding**||
|---|---|
|**Naam**|Aanleiding|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|aanleiding|
|**Definitie**|Een omschrijving van de gebeurtenis die leidt tot het starten van|
||een ZAAK van dit ZAAKTYPE.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|



88 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een omschrijving te geven van de gebeurtenis - de gedefinieerde aanleiding uit de definitie van een zaak - die leidt tot ZAAKen van dit ZAAKTYPE. Denk bij het uitwerken van deze attribuutsoort niet alleen aan de directe aanleiding - zoals een aanvraag, aangifte of melding -, maar ook aan indirecte aanleidingen. Zo kunnen aanvragen voor een vergunning of meldingen ook voortkomen uit een toezichtzaak. 

## **Attribuutsoort Toelichting** 

|**Attribuutsoort Toelichting**||
|---|---|
|**Naam**|Toelichting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een eventuele toelichting op dit zaaktype.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN1000|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld om een toelichting te geven op dit ZAAKTYPE. Hier kan bijvoorbeeld een beschrijving van het procesverloop op hoofdlijnen worden gegeven. 

## **Attribuutsoort Indicatie Intern of Extern** 

|**Attribuutsoort Indicatie**|**Intern of Extern**|
|---|---|
|**Naam**|Indicatie Intern of Extern|
|**Herkomst**|KING, o.b.v. ZTC 1.0|
|**Code**||
|**XML-tag**|indicatieInternOfExtern|
|**Definitie**|Een aanduiding waarmee onderscheid wordt gemaakt tussen|
||ZAAKTYPEn die Intern respectievelijk Extern geïnitieerd worden.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN6|
|**Waardenverzameling**|- ‘Intern’ (de aanleiding voor het starten voor de zaak ligt binnen|
||de zaakbehandelende organisatie)|
||- ‘Extern’ (de aanleiding voor het starten voor de zaak ligt buiten|



89 

**==> picture [103 x 52] intentionally omitted <==**

de zaakbehandelende organisatie) **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Middels deze attribuutsoort is het mogelijk onderscheid te maken tussen ZAAKTYPEn met een externe initiatie  - bijvoorbeeld bij het aanvragen van een omgevingsvergunning - en ZAAKTYPEn met een interne initiatie  - bijvoorbeeld bij het aanvragen van bijzonder verlof. Indien van beide sprake kan zijn, dan prevaleert de externe initiatie. 

## **Attribuutsoort Handeling initiator** 

|**Naam**|Handeling initiator|
|---|---|
|**Herkomst**|KING, o.b.v. ZTC 1.0|
|**Code**||
|**XML-tag**|handelingInitiator|
|**Definitie**|Werkwoord dat hoort bij de handeling die de initiator verricht bij|
||dit zaaktype. Meestal 'aanvragen', 'indienen' of 'melden'.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Er is een aantal opties mogelijk bij de naamgeving van de zaaktypen. Omdat elke gemeente haar eigen voorkeur hierin zal ontwikkelen en de lijst generiek is bedoeld, wordt onderstaand het IOBmodel gepresenteerd dat gemeenten kan helpen de eigen keuze te maken. Het IOB model is niet alleen bruikbaar voor het definiëren van namen voor zaaktypen, maar tevens voor het definiëren van producten en webformulieren. Daarnaast kan de tabel gebruikt worden voor het onderwerp in communicatie-uitingen zoals ontvangstbevestigingen. De letters IOB staan voor: 

I: handeling Initiator (van het zaaktype), d.w.z. de interne of externe klant, 

O: Onderwerp (het meest vergelijkbaar met ‘product’ uit de PDC), 

- B: handeling Behandelaar (van het zaaktype) van de eigen organisatie. 

90 

**==> picture [103 x 52] intentionally omitted <==**

I en B worden in de lijst weergegeven als werkwoorden. Een gemeente kan er voor kiezen één of beide werkwoorden te vervangen door het bijbehorende zelfstandig naamwoord. 'Aanvragen vergunning behandelen' kan zo bijvoorbeeld leiden tot het zaaktype met de naam 'Aanvraag vergunning'. 

Er zijn zaaktypen waarbij er geen duidelijke initiator is of waarbij de initiator impliciet in het zaaktype zit verweven. In zo'n geval is I niet gevuld. Voorbeeld: 'Opstellen bestemmingsplan'. Ook bij zaaktypen die met een vaste regelmaat voorkomen, bijvoorbeeld eenmaal per jaar, is geen I benoemd. Voorbeeld hierbij is 'Onroerend zaakbelasting heffen'. 

Als de gemeente de initiator is van een zaak bij derden, zoals het aanvragen van subsidie bij de provincie, zijn alleen I en O gevuld, B is dan leeg. In feite betreft het hier een zaak bij een andere organisatie, maar het kan voor een gemeente zinvol zijn de aanvraag bij derden als zaak te behandelen. 

Belangrijk: 

Er wordt geen voorkeur uitgesproken voor de wijze waarop het zaaktype zou moeten worden benoemd. Ook kan de naamgeving naar buiten toe (bijvoorbeeld in een PDC of op het webformulier op een internet site) afwijken omdat dit duidelijker is voor de burger. 

## **Attribuutsoort Onderwerp** 

|**Attribuutsoort Onderwerp**||
|---|---|
|**Naam**|Onderwerp|
|**Herkomst**|KING, o.b.v. ZTC 1.0|
|**Code**||
|**XML-tag**|onderwerp|
|**Definitie**|Het onderwerp van ZAAKen van dit ZAAKTYPE. In veel gevallen|
||nauw gerelateerd aan de product- of dienstnaam uit de|
||Producten- en Dienstencatalogus (PDC). Bijvoorbeeld:|
||'Evenementenvergunning', 'Geboorte', 'Klacht'.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Er is een aantal opties mogelijk bij de naamgeving van de zaaktypen. Omdat elke gemeente haar eigen voorkeur hierin zal ontwikkelen en de lijst generiek is bedoeld, wordt onderstaand het IOBmodel gepresenteerd dat gemeenten kan helpen de eigen keuze te maken. Het IOB model is niet alleen bruikbaar voor het definiëren van namen voor zaaktypen, maar tevens voor het definiëren van producten en webformulieren. Daarnaast kan de tabel gebruikt worden voor het onderwerp in communicatie-uitingen zoals ontvangstbevestigingen. De letters IOB staan voor: 

I: handeling Initiator (van het zaaktype), d.w.z. de interne of externe klant, 

## O: Onderwerp (het meest vergelijkbaar met ‘product’ uit de PDC), 

91 

**==> picture [103 x 52] intentionally omitted <==**

B: handeling Behandelaar (van het zaaktype) van de eigen organisatie. 

I en B worden in de lijst weergegeven als werkwoorden. Een gemeente kan er voor kiezen één of beide werkwoorden te vervangen door het bijbehorende zelfstandig naamwoord. 'Aanvragen vergunning behandelen' kan zo bijvoorbeeld leiden tot het zaaktype met de naam 'Aanvraag vergunning'. 

Er zijn zaaktypen waarbij er geen duidelijke initiator is of waarbij de initiator impliciet in het zaaktype zit verweven. In zo'n geval is I niet gevuld. Voorbeeld: 'Opstellen bestemmingsplan'. Ook bij zaaktypen die met een vaste regelmaat voorkomen, bijvoorbeeld eenmaal per jaar, is geen I benoemd. Voorbeeld hierbij is 'Onroerend zaakbelasting heffen'. 

Als de gemeente de initiator is van een zaak bij derden, zoals het aanvragen van subsidie bij de provincie, zijn alleen I en O gevuld, B is dan leeg. In feite betreft het hier een zaak bij een andere organisatie, maar het kan voor een gemeente zinvol zijn de aanvraag bij derden als zaak te behandelen. 

Belangrijk: 

Er wordt geen voorkeur uitgesproken voor de wijze waarop het zaaktype zou moeten worden benoemd. Ook kan de naamgeving naar buiten toe (bijvoorbeeld in een PDC of op het webformulier op een internet site) afwijken omdat dit duidelijker is voor de burger. 

## **Attribuutsoort Handeling behandelaar** 

|**Naam**|Handeling behandelaar|
|---|---|
|**Herkomst**|KING, o.b.v. ZTC 1.0|
|**Code**||
|**XML-tag**|handelingBehandelaar|
|**Definitie**|Werkwoord dat hoort bij de handeling die de behandelaar|
||verricht bij het afdoen van ZAAKen van dit ZAAKTYPE. Meestal|
||'behandelen', 'uitvoeren', 'vaststellen' of 'onderhouden'.|
|**Herkomst definitie**|KING, o.b.v. ZTC 1.0|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Er is een aantal opties mogelijk bij de naamgeving van de zaaktypen. Omdat elke gemeente haar eigen voorkeur hierin zal ontwikkelen en de lijst generiek is bedoeld, wordt onderstaand het IOBmodel gepresenteerd dat gemeenten kan helpen de eigen keuze te maken. Het IOB model is niet alleen bruikbaar voor het definiëren van namen voor zaaktypen, maar tevens voor het definiëren van producten en webformulieren. Daarnaast kan de tabel gebruikt worden voor het onderwerp in communicatie-uitingen zoals ontvangstbevestigingen. De letters IOB staan voor: 

I: handeling Initiator (van het zaaktype), d.w.z. de interne of externe klant, 

## O: Onderwerp (het meest vergelijkbaar met ‘product’ uit de PDC), 

92 

**==> picture [103 x 52] intentionally omitted <==**

B: handeling Behandelaar (van het zaaktype) van de eigen organisatie. 

I en B worden in de lijst weergegeven als werkwoorden. Een gemeente kan er voor kiezen één of beide werkwoorden te vervangen door het bijbehorende zelfstandig naamwoord. 'Aanvragen vergunning behandelen' kan zo bijvoorbeeld leiden tot het zaaktype met de naam 'Aanvraag vergunning'. 

Er zijn zaaktypen waarbij er geen duidelijke initiator is of waarbij de initiator impliciet in het zaaktype zit verweven. In zo'n geval is I niet gevuld. Voorbeeld: 'Opstellen bestemmingsplan'. Ook bij zaaktypen die met een vaste regelmaat voorkomen, bijvoorbeeld eenmaal per jaar, is geen I benoemd. Voorbeeld hierbij is 'Onroerend zaakbelasting heffen'. 

Als de gemeente de initiator is van een zaak bij derden, zoals het aanvragen van subsidie bij de provincie, zijn alleen I en O gevuld, B is dan leeg. In feite betreft het hier een zaak bij een andere organisatie, maar het kan voor een gemeente zinvol zijn de aanvraag bij derden als zaak te behandelen. 

Belangrijk: 

Er wordt geen voorkeur uitgesproken voor de wijze waarop het zaaktype zou moeten worden benoemd. Ook kan de naamgeving naar buiten toe (bijvoorbeeld in een PDC of op het webformulier op een internet site) afwijken omdat dit duidelijker is voor de burger. 

## **Attribuutsoort Doorlooptijd behandeling** 

|**Naam**|Doorlooptijd behandeling|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|doorlooptijd|
|**Definitie**|De periode waarbinnen volgens wet- en regelgeving een ZAAK|
||van het ZAAKTYPE afgerond dient te zijn.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|N3|
|**Waardenverzameling**|1-999 kalenderdagen|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

De periode is in kalenderdagen; zie voor een definitie van dit begrip de AWB. De startdatum van de zaak markeert de eerste dag. De uiterlijke einddatum van de zaak markeert de laatste dag. 

## **Attribuutsoort Servicenorm behandeling** 

|**Naam**|Servicenorm behandeling|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|servicenorm|
|**Definitie**|De periode waarbinnen verwacht wordt dat een ZAAK van het|
||ZAAKTYPE afgerond wordt conform de geldende servicenormen|



93 

**==> picture [103 x 52] intentionally omitted <==**

van de zaakbehandelende organisatie(s). **Herkomst definitie** KING **Datum opname** 1 juni 2008 **Formaat** N3 **Waardenverzameling** 1-999 kalenderdagen **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** Deze periode mag niet langer zijn dan de periode van Doorlooptijd behandeling. De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

De periode is in kalenderdagen; zie voor een definitie van dit begrip de AWB. De startdatum van de zaak markeert de eerste dag. De geplande einddatum van de zaak markeert de laatste dag. 

## **Attribuutsoort Opschorting/aanhouding mogelijk** 

|**Naam**|Opschorting/aanhouding mogelijk|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**||
|**Definitie**|Aanduiding die aangeeft of ZAAKen van dit ZAAKTYPE kunnen|
||worden opgeschort en/of aangehouden.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|A1|
|**Waardenverzameling**|J, N|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

## **Attribuutsoort Verlenging mogelijk** 

**Naam** Verlenging mogelijk **Herkomst** KING **Code** 

94 

**==> picture [103 x 52] intentionally omitted <==**

|**XML-tag**|verlengingmogelijk|
|---|---|
|**Definitie**|Aanduiding die aangeeft of de Doorlooptijd behandeling van|
||ZAAKen van dit ZAAKTYPE kan worden verlengd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|A1|
|**Waardenverzameling**|J, N|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

## **Attribuutsoort Verlengingstermijn** 

|**Naam**|Verlengingstermijn|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|verlengingstermijn|
|**Definitie**|De termijn in dagen waarmee de Doorlooptijd behandeling van|
||ZAAKen van dit ZAAKTYPE kan worden verlengd.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|N3|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|Mag alleen een waarde bevatten als Verlenging mogelijk de|
||waarde 'J' heeft.|
||De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het is mogelijk dat de verlenging van de behandeltermijn aan wettelijke beperkingen gebonden. Zo kan de behandeling van een reguliere WABO-procedure één maal met 6 weken (42 dagen) worden verlengd. 

## **Attribuutsoort Trefwoord** 

95 

**==> picture [103 x 52] intentionally omitted <==**

**Naam** Trefwoord **Herkomst** GFO Zaken 2004, aangepast door KING **Code** 0006 **XML-tag** trefwoord **Definitie** Een trefwoord waarmee ZAAKen van het ZAAKTYPE kunnen worden gekarakteriseerd. **Herkomst definitie** GFO Zaken 2004, aangepast door KING **Datum opname** 1 juni 2008 **Formaat** AN30 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0 - N **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Het betreft de gelijknamige attribuutsoort bij Zaak in het GFO Zaken 2004. 

## **Attribuutsoort Archiefclassificatiecode** 

|**Naam**|Archiefclassificatiecode|
|---|---|
|**Herkomst**|KING, op basis van NEN 2082|
|**Code**||
|**XML-tag**|archiefclassificatiecode|
|**Definitie**|De systematische identificatie van zaakdossiers van dit ZAAKTYPE|
||overeenkomstig logisch gestructureerde conventies, methoden|
||en procedureregels.|
|**Herkomst definitie**|KING, op basis van NEN 2082|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN20|
|**Waardenverzameling**|De classificatiecode in het gehanteerde|
||archiveringsclassificatiestelsel, gevolgd door een spatie en –|
||tussen haakjes  - de gebruikelijke afkorting van de naam van het|
||gehanteerde classificatiestelsel.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|
|**Toelichting**||



96 

**==> picture [103 x 52] intentionally omitted <==**

Een zaakdossier betreft alle informatie over een zaak (en daarvan deel uit makende deelzaken) inclusief alle daarbij geregistreerde documenten. Met de archiefclassificatiecode wordt de relatie gelegd naar de plaats van het zaakdossier in het gehanteerde archiveringsclassificatiestelsel. 

## **Attribuutsoort Vertrouwelijkheidaanduiding** 

**Naam Herkomst Code XML-tag Definitie** 

Vertrouwelijkheidaanduiding KING 

vertrouwelijkheidAanduiding Aanduiding van de mate waarin zaakdossiers van ZAAKen van dit ZAAKTYPE voor de openbaarheid bestemd zijn. 

**Herkomst definitie** KING **Datum opname** 1 juni 2008 **Formaat** AN20 **Waardenverzameling** 

ZEER GEHEIM (indien kennisnemen door niet gerechtigden zeer ernstige schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) 

GEHEIM (indien kennisnemen door niet gerechtigden ernstige schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) 

CONFIDENTIEEL (indien kennisnemen door niet gerechtigden schade kan toebrengen aan het belang van de Staat of zijn bondgenoten) 

VERTROUWELIJK (indien kennisnemen door niet gerechtigden nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) 

ZAAKVERTROUWELIJK (indien kennisnemen door anderen dan betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) INTERN (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publliekrechtelijke organisaties) 

BEPERKT OPENBAAR (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties) OPENBAAR (in alle andere gevallen) **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven 

97 

**==> picture [103 x 52] intentionally omitted <==**

## **Regels** 

De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Een zaakdossier betreft alle informatie over een zaak (en daarvan deel uit makende deelzaken) inclusief alle daarbij geregistreerde documenten. 

De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst bijzondere informatie (VIRBI). 

## **Attribuutsoort Verantwoordelijke** 

|**Naam**|Verantwoordelijke|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|Verantwoordelijke|
|**Definitie**|De (soort) organisatorische eenheid  of (functie van) medewerker|
||die verantwoordelijk is voor de uitvoering van zaken van het|
||ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|28 januari 2013|
|**Formaat**|AN50|
|**Waardenverzameling**|Indien het om een zaaktype in een catalogus voor een specifieke|
||organisatie gaat, dan de naam van een Organisatorische eenheid|
||of Medewerker overeenkomstig het RGBZ.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Afhankelijk van het niveau waarop het zaaktype gespecificeerd wordt, kan de verantwoordelijke afdeling of medewerker nader geduid worden. Als het gaat om een zaaktype voor een specifieke organisatie, dan wordt de afdeling of medewerker exact benoemd. 

## **Attribuutsoort Publicatie-indicatie** 

|**Naam**|Publicatie-indicatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|publicatieIndicatie|
|**Definitie**|Aanduiding of (het starten van) een ZAAK van dit ZAAKTYPE|
||gepubliceerd moet worden.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN1|
|**Waardenverzameling**|J, N|
|**Indicatie materiële historie**|Ja|



98 

**==> picture [103 x 52] intentionally omitted <==**

|**Indicatie formele historie**|Nee|
|---|---|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het gaat hier niet alleen om de wettelijke verplichting tot publicatie maar ook om de eigen keuze van de organisatie die zaken van dit type behandelt. 

## **Attribuutsoort Publicatietekst** 

|**Naam**|Publicatietekst|
|---|---|
|**Herkomst**|RGBZ|
|**Code**||
|**XML-tag**|Publicatietekst|
|**Definitie**|De generieke tekst van de publicatie van ZAAKen van dit|
||ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juni 2008|
|**Formaat**|AN1000|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

## **Groepattribuutsoort Product/Dienst** 

|**Naam**|Product/Dienst|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|Product_DienstGrp|
|**Definitie**|Het product of de dienst die door ZAAKen van dit ZAAKTYPE|
||wordt voortgebracht.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|



99 

**==> picture [103 x 52] intentionally omitted <==**

**Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1..* **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De groepattribuutsoort verandert alleen van waarde (materiële historie) cq. één of meer van de subattributen veranderen van waarde op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Met deze groepattribuutsoort kan de relatie worden gelegd naar één of meer producten en of diensten die met ZAAKen van dit ZAAKTYPE worden geleverd. Omdat aan een product- of dienstbeschrijving rechten kunnen worden ontleend, is het van belang dat bij - een versie van - een ZAAKTYPE is vastgelegd welke - versie van - een productbeschrijving van toepassing is op ZAAKen van dit ZAAKTYPE. 

## **Attribuutsoort 'Naam' van groepattribuutsoort 'Product/Dienst'** 

|**Naam**|Naam|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|naam|
|**Definitie**|De naam van het product of de dienst.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**|-|
|**Toelichting**||



## **Attribuutsoort 'Link' van groepattribuutsoort 'Product/Dienst'** 

|**Naam**|Link|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|link|
|**Definitie**|De URL naar de beschrijving van het product of de dienst.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|anyURL|
|**Waardenverzameling**|geldige URL van de product- of dienstbeschrijving|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|



100 

**==> picture [103 x 52] intentionally omitted <==**

|**Aanduiding brondocument**||
|---|---|
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**|-|
|**Toelichting**||



## **Groepattribuutsoort Formulier** 

|**Naam**|Formulier|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|formulier|
|**Definitie**|Het formulier dat ZAAKen van dit ZAAKTYPE initieert.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0..*|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De groepattribuutsoort verandert alleen van waarde|
||(materiële historie) cq. één of meer van de subattributen|
||veranderen van waarde op een datum die gelijk is aan een|
||Versiedatum van het zaaktype.|



## **Toelichting** 

Met deze groepattribuutsoort wordt de relatie gelegd naar het 'blanco' formulier / de formulierdefinitie waarmee ZAAKen van dit ZAAKTYPE worden geïnitieerd. Formulier moet in deze context in de ruimste zin van het woord worden opgevat; het kan zowel gaan om het sjabloon voor het papieren formulier als het e-formulier dat wordt gebruikt voor de webintake. Om die reden is de kardinaliteit 0-N: er kan per kanaal een ander formulier gedefinieerd zijn. De kardinaliteit per kanaal is 0-1. 

## **Attribuutsoort 'Naam' van groepattribuutsoort 'Formulier'** 

|**Naam**|Naam|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|naam|
|**Definitie**|De naam van het formulier.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||



101 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** zie groep **Regels** - **Toelichting** 

## **Attribuutsoort 'Link' van groepattribuutsoort 'Formulier'** 

|**Naam**|Link|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|link|
|**Definitie**|De URL naar het formulier.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|anyURL|
|**Waardenverzameling**|geldige URL van de product- of dienstbeschrijving.|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**|-|



## **Toelichting** 

Bijvoorbeeld de URL naar de PDF waarmee een aanvraag op papier kan worden ingediend of de URL naar een formulier waarmee de webintake plaatsvindt. 

## **Groepattribuutsoort Referentieproces** 

|**Naam**|Referentieproces|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|referentieproces|
|**Definitie**|Het Referentieproces dat ten grondslag ligt aan dit ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De groepattribuutsoort verandert alleen van waarde|
||(materiële historie) cq. één of meer van de subattributen|
||veranderen van waarde op een datum die gelijk is aan een|
||Versiedatum van het zaaktype.|



102 

**==> picture [103 x 52] intentionally omitted <==**

## **Toelichting** 

## **Attribuutsoort 'Naam' van groepattribuutsoort 'Referentieproces'** 

|**Naam**|Naam|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|naam|
|**Definitie**|De naam van het Referentieproces.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN80|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**|-|
|**Toelichting**||



## **Attribuutsoort 'Link' van groepattribuutsoort 'Referentieproces'** 

|**Naam**|Link|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|link|
|**Definitie**|De URL naar de beschrijving van het Referentieproces.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|anyURL|
|**Waardenverzameling**|geldige URL van de beschrijving van het Referentieproces.|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|zie groep|
|**Regels**|-|
|**Toelichting**||



## **Attribuutsoort Verantwoordingsrelatie** 

**Naam** Verantwoordingsrelatie **Herkomst** KING 

103 

**==> picture [103 x 52] intentionally omitted <==**

|**Code**||
|---|---|
|**XML-tag**|verantwoordingsrelatie|
|**Definitie**|De relatie tussen ZAAKen van dit ZAAKTYPE en de beleidsmatige|
||en/of financiële verantwoording.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN40|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - N|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

De ZAAKen die worden uitgevoerd leveren een bijdrage aan / of zijn een invulling van de taken van de organisatie. Met dit attribuut kan de relatie worden gelegd naar de systemen / systematiek waarmee de organisatie rapporteert over de uitvoering van deze taken. Gemeenten en provincie kunnen hier bijvoorbeeld de IV3-functie invullen die ZAAKen van dit ZAAKTYPE relateert aan de systematiek van de financiële verantwoording. 

## **Groepattribuutsoort Broncatalogus** 

|**Naam**|Broncatalogus|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|broncatalogus|
|**Definitie**|De CATALOGUS waaraan het ZAAKTYPE is ontleend.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0..1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De groepattribuutsoort verandert alleen van waarde|
||(materiële historie) cq. één of meer van de subattributen|
||veranderen van waarde op een datum die gelijk is aan een|
||Versiedatum van het zaaktype.|



## **Toelichting** 

Met deze groepattribuutsoort kan een relatie worden gelegd naar de CATALOGUS waaraan de configuratie van dit ZAAKTYPE is ontleend. Denk bijvoorbeeld aan het leggen van de relatie tussen het 'lokale' ZAAKTYPE 'Aanvraag Uittreksel GBA behandelen' en een specifiek voor de sector Burgerzaken ontwikkelde catalogus met alle zaaktypen voor Burgerzaken. De combinatie van deze 

104 

**==> picture [103 x 52] intentionally omitted <==**

groepattribuutsoort met de attribuutsoort Bronzaaktype-identificatie identificeert het zaaktype waarvan dit 'lokale' zaaktype is afgeleid uniek en stelt de beheerder van dit ZAAKTYPE in staat die relatie te bewaken. 

## **Attribuutsoort 'Domein' van groepattribuutsoort 'Broncatalogus'** 

|**Naam**|Domein|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**||
|**Definitie**|Het domein van de CATALOGUS waaraan het ZAAKTYPE is|
||ontleend.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN30|
|**Waardenverzameling**|alle alfanumerieke tekens|
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|-|
|**Toelichting**||



## **Attribuutsoort 'RSIN' van groepattribuutsoort 'Broncatalogus'** 

|**Naam**|RSIN|
|---|---|
|**Herkomst**|NHR|
|**Code**||
|**XML-tag**|rsin|
|**Definitie**|Het RSIN van de INGESCHREVEN NIET-NATUURLIJK PERSOON|
||die beheerder is van de CATALOGUS waaraan het ZAAKTYPE|
||is ontleend.|
|**Herkomst definitie**|NHR|
|**Datum opname**|1 juli 2012|
|**Formaat**|N9|
|**Waardenverzameling**||
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|
|**Aanduiding strijdigheid/nietigheid**|zie groep|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Authentiek|
|**Regels**|-|
|**Toelichting**||



105 

**==> picture [103 x 52] intentionally omitted <==**

## **Groepattribuutsoort Bronzaaktype** 

|**Naam**|Bronzaaktype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|bronzaaktype|
|**Definitie**|Het zaaktype binnen de CATALOGUS waaraan dit ZAAKTYPE is|
||ontleend.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0..1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De groepattribuutsoort verandert alleen van waarde|
||(materiële historie) cq. één of meer van de subattributen|
||veranderen van waarde op een datum die gelijk is aan een|
||Versiedatum van het zaaktype.|



## **Toelichting** 

- Met de combinatie van deze groepattribuutsoort en de groepattribuutsoort Broncatalogus, kan de relatie worden gelegd naar het zaaktype (de bron) dat de basis vormde voor dit ZAAKTYPE. Uitgangspunt is dat het zaaktype is afgeleid van de versie van het bronzaaktype zoals dat bestond ten tijde van de begindatum van het zaaktype. 

- Een voorbeeld is een zaaktype dat is overgenomen uit een landelijk gestandaardiseerde CATALOGUS en vervolgens enigszins is aangepast voor toepassing in de eigen organisatie. Door het vastleggen van deze relatie kunnen wijzigingen in het bronzaaktype worden gesignaleerd, geëvalueerd en mogelijk leiden tot aanpassing van het 'eigen' zaaktype. 

- Idealiter is een organisatiespecifiek zaaktypen ontleend aan een referentiecatalogus. Aangezien dat vooralsnog niet altijd het geval zal zijn heeft dit groepattribuutsoort de kardinaliteit 0-1. Dringend wordt aanbevolen dit groepattribuutsoort wel van waarden te voorzien. 

## **Attribuutsoort 'Zaaktype-identificatie' van groepattribuutsoort 'Bronzaaktype'** 

|**Naam**|Zaaktype-identificatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|identificatie|
|**Definitie**|De Zaaktype-identificatie van het bronzaaktype binnen de|
||CATALOGUS.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|N5|
|**Waardenverzameling**||
|**Indicatie materiële historie**|zie groep|
|**Indicatie formele historie**|zie groep|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|zie groep|



106 

**==> picture [103 x 52] intentionally omitted <==**

**Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** - **Toelichting** 

## **Attribuutsoort 'Zaaktype-omschrijving' van groepattribuutsoort 'Bronzaaktype'** 

**Naam** Zaaktype-omschrijving **Herkomst** KING **Code XML-tag** omschrijving **Definitie** De Zaaktype-omschrijving van het bronzaaktype, zoals gehanteerd in de Broncatalogus. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Formaat** AN80 **Waardenverzameling** alle alfanumerieke tekens **Indicatie materiële historie** zie groep **Indicatie formele historie** zie groep **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** zie groep **Aanduiding strijdigheid/nietigheid** zie groep **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** - **Toelichting** 

## **Attribuutsoort Datum begin geldigheid zaaktype** 

|**Naam**|Datum begin geldigheid zaaktype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop het ZAAKTYPE is ontstaan.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan de vroegste Versiedatum van het zaaktype.|
|**Toelichting**||



Met deze datum wordt aangegeven vanaf wanneer het zaaktype bestaat en toegepast kan 

107 

**==> picture [103 x 52] intentionally omitted <==**

## worden. 

## **Attribuutsoort Versiedatum** 

**Naam** Versiedatum **Herkomst** KING **Code XML-tag** versiedatum **Definitie** De datum waarop de (gewijzigde) kenmerken van het ZAAKTYPE geldig zijn geworden **Herkomst definitie** KING **Datum opname** 23 september 2013 **Formaat** Datum (jjjjmmdd) **Waardenverzameling Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De Versiedatum is gelijk aan of ligt na de Datum begin geldigheid zaaktype en is gelijk aan of ligt voor de Datum einde geldigheid zaaktype. 

## **Toelichting** 

Een versie van het zaaktype betreft alle kenmerken daarvan. Dus niet alleen van ZAAKTYPE zelf maar ook van alle ‘daaronder hangende’ objecttypen zoals STATUSTYPE, RESULTAATTYPE, et cetera. 

## **Attribuutsoort Datum einde geldigheid zaaktype** 

|**Naam**|Datum einde geldigheid zaaktype|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop het ZAAKTYPE is opgeheven.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 oktober 2009|
|**Formaat**|OnvolledigeDatum|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Nee|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De datum is gelijk aan of gelegen na de datum zoals opgenomen|
||onder 'Datum begin geldigheid zaaktype’.|



## **Toelichting** 

Met deze datum wordt aangegeven vanaf wanneer het zaaktype niet meer bestaat en niet meer 

108 

**==> picture [103 x 52] intentionally omitted <==**

toegepast kan worden. 

## **Relatiesoort heeft gerelateerd** 

**Naam** heeft gerelateerd **Gerelateerd objecttype** ZAAKTYPE **Indicatie kardinaliteit** 0..* **Herkomst** KING **Code Definitie** De ZAAKTYPEn van zaken die relevant zijn voor zaken van dit ZAAKTYPE. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De relatiesoort ontstaat en eindigt alleen (materiële historie) op een datum die gelijk is resp. een dag ligt voor een (en dezelfde) Versiedatum van het zaaktype en het gerelateerd zaaktype. 

## **Toelichting** 

Soms staan zaken niet op zich maar hebben zij onderlinge relaties. 

Zo kan een zaak van een bepaald ZAAKTYPEn een noodzakelijk vervolg zijn op een zaak van (een ander of hetzelfde) ZAAKTYPE dat eraan vooraf gaat. Denk aan een toezichtzaak die gepland wordt bij afronding van een vergunningzaak of een handhavingszaak die voortvloeit uit een toezichtzaak. 

In andere gevallen gaat het om de vraag van de ene organisatie aan een andere organisatie om een bijdrage te leveren aan een zaak van eerstgenoemde organisatie. Ook binnen organisaties komt dit voor tussen organisatie-onderdelen.. Het gaat er daarbij om dat een organisatieonderdeel of een externe organisatie wordt ingezet voor een gedeelte van de zaak waarbij voor dat onderdeel of die organisatie die inzet een zelfstandig bedrijfsproces is. Dat bedrijfsproces wordt derhalve uitgevoerd als zaak van een (ander) ZAAKTYPE. In dergelijke gevallen is sprake van gerelateerde zaken, en daarmee ZAAKTYPEN, waarbij de ene zaak een bijdrage levert aan de andere zaak. Kenmerkend is dat deze zaken verschillende aanleidingen hebben (in tegenstelling tot deelzaken bij eenzelfde hoofdzaak). Voor de in behandeling zijnde zaak is dat de ‘klantvraag’, voor de gerelateerde zaak is dat een verzoek vanuit de andere (cq. in behandeling zijnde) zaak. Let wel, als die inzet voor dat organisatie-onderdeel geen zelfstandig bedrijfsproces is, dan is geen sprake van een gerelateerde zaak noch van een deelzaak maar van uitvoering van een deel van de in behandeling zijnde zaak. 

De derde situatie waarin zaken relaties hebben, betreft gevallen waarbij de ene zaak betrekking heeft op, relevant is voor of onderwerp is van een andere zaak. Dit is vergelijkbaar met de relatie die aangeeft dat een zaak betrekking heeft op een zaakobject. Voorbeelden hiervan zijn de bezwaarzaak die betrekking heeft op de vergunningzaak. Het onderscheid met de hiervoor genoemde ‘vervolg-relatie’ is dat de ene zaak geen noodzakelijk d.w.z. te plannen vervolg op de andere zaak is. 

Met deze relatiesoort worden de relaties vastgelegd tussen de gerelateerde ZAAKTYPEn. Deze relatiesoort kent eigenschappen, zoals de aard van de relatie, die we modelleren met de relatieklasse ZAAKTYPENRELATIE. 

Zie ook de toelichting bij de relatiesoort ‘ZAAKTYPE  is deelzaaktype van ZAAKTYPE’ voor het onderscheid met (zaaktypen van) deelzaken. 

109 

**==> picture [103 x 52] intentionally omitted <==**

## **Relatiesoort heeft relevant** 

**Naam** heeft relevant **Gerelateerd objecttype** INFORMATIEOBJECTTYPE **Indicatie kardinaliteit** 0..* **Herkomst** KING **Code Definitie** De INFORMATIEOBJECTTYPEn die relevant kunnen zijn voor ZAAKen van dit ZAAKTYPE. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De relatiesoort ontstaat en eindigt alleen (materiële historie) op een datum die gelijk is resp. een dag ligt voor een Versiedatum van het zaaktype. 

## **Toelichting** 

Niet elk INFORMATIEOBJECTTYPE is relevant voor ZAAKen van een ZAAKTYPE. Zo is het INFORMATIEOBJECTTYPE met Informatieobjecttype-omschrijving generiek 'Oproepkaart' erg relevant voor zaaktypen die betrekking hebben op verkiezingen, maar bijvoorbeeld niet voor de melding openbare ruimte, omgevingsvergunning, subsidieaanvraag, et cetera. Deze relatiesoort is opgenomen om bij een ZAAKTYPE vast te kunnen leggen welke deelverzameling INFORMATIEOBJECTTYPEn relevant kan zijn voor ZAAKen van dit ZAAKTYPE en behandelaren zo een overzichtelijke lijst met informatieobjecttypen te kunnen presenteren. 

## **Relatiesoort heeft relevant** 

|**Relatiesoort heeft relevant**||
|---|---|
|**Naam**|heeft relevant|
|**Gerelateerd objecttype**|BESLUITTYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De BESLUITTYPEn die relevant kunnen zijn voor ZAAKen van dit|
||ZAAKTYPE|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een Versiedatum|
||van het zaaktype.|



## **Toelichting** 

Niet elk BESLUITTYPE is relevant voor ZAAKen van een ZAAKTYPE. Zo is het BESLUITTYPE met Besluittype-omschrijving generiek 'Handhavingsbesluit' erg relevant voor zaaktypen die 

110 

**==> picture [103 x 52] intentionally omitted <==**

betrekking hebben op handhaving, maar bijvoorbeeld niet voor behandelen van een aanvraag voor een reisdocument of een melding geslachtsnaamwijziging, et cetera. Deze relatiesoort is opgenomen om bij een ZAAKTYPE vast te kunnen leggen welke deelverzameling BESLUITTYPEn relevant kan zijn voor ZAAKen van dit ZAAKTYPE en behandelaren zo een overzichtelijke lijst met besluittypen te kunnen presenteren. 

## **Relatiesoort is deelzaaktype van** 

|**Naam**|is deelzaaktype van|
|---|---|
|**Gerelateerd objecttype**|ZAAKTYPE|
|**Indicatie kardinaliteit**|0..*|
|**Herkomst**|KING|
|**Code**||
|**Definitie**|De ZAAKTYPEn (van de hoofdzaken) waaronder ZAAKen van dit|
||ZAAKTYPE als deelzaak kunnen voorkomen.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De relatiesoort ontstaat en eindigt alleen (materiële historie) op|
||een datum die gelijk is resp. een dag ligt voor een (en dezelfde)|
||Versiedatum van het zaaktype en het gerelateerd zaaktype.|



## **Toelichting** 

Niet altijd is het mogelijk om een aanleiding, die in de ogen van de initiator daarvan als één samenhangend geheel beschouwd wordt, als één zaak binnen de organisatie te behandelen. Dit doet zich voor als de gewenste producten en diensten in verschillende bedrijfsprocessen vervaardigd worden d.w.z. voor elk gewenst product of dienst, of groep daarvan, is een zelfstandig bedrijfsproces voorzien. In dat geval kan de zaakbehandelende organisatie de aangevraagde zaak behandelen in meerdere ‘deelzaken’ die ieder op zich weer een zaak vormen voor één bedrijfsproces. Kenmerkend voor die bedrijfsprocessen cq. deelzaken is dat ze dezelfde aanleiding hebben: de klantvraag. 

Met de ‘hoofdzaak’ wordt gecoördineerd dat de optelsom van de te leveren producten en diensten beantwoord aan de oorspronkelijke klantvraag. Voor de initiator is en blijft de zaak als geheel (de ‘hoofdzaak’) relevant. De zaakbehandelende organisatie richt zich meer op de uitvoering van de deelzaken en de coördinatie daartussen (de ‘hoofdzaak’). 

De relatiesoort brengt het verband aan tussen een bedrijfsproces cq. ZAAKTYPE, waarvan zaken (ook) als deelzaken uitgevoerd kunnen worden, en de desbetreffende ZAAKTYPEN van de hoofdzaken en definieert de ZAAKTYPEn van de ’hoofdzaken’ waarbij een zaak van dit ZAAKTYPE als deelzaak kan voorkomen. 

Zie ook de toelichting bij de relatiesoort ‘ZAAKTYPE heeft gerelateerd ZAAKTYPE’ voor het onderscheid met (zaaktypen van) gerelateerde zaken. 

## **Relatiesoort maakt deel uit van** 

|**Naam**|maakt deel uit van|
|---|---|
|**Gerelateerd objecttype**|CATALOGUS|
|**Indicatie kardinaliteit**|1|
|**Herkomst**|KING|
|**Code**||



111 

**==> picture [103 x 52] intentionally omitted <==**

**Definitie** De CATALOGUS waartoe dit ZAAKTYPE behoort. **Herkomst definitie** KING **Datum opname** 1 juli 2012 **Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** - **Toelichting** 

112 

**==> picture [103 x 52] intentionally omitted <==**

## **6.2 Relatieklassen** 

## **6.2.1. Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE** 

## **Attribuutsoort Volgnummer** 

|**Naam**|Volgnummer|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|volgnummer|
|**Definitie**|Uniek volgnummer van het ZAAK-INFORMATIEOBJECT-TYPE|
||binnen het ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|21 februari 2013|
|**Formaat**|N3|
|**Waardenverzameling**|Getal van 1 t/m 999|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het volgnummer is alleen voor documentatiedoeleinden. Het wordt gebruikt om binnen een zaaktype te kunnen verwijzen naar een document en om documenten in schema’s te kunnen vermelden. 

## **Attribuutsoort Richting** 

|**Attribuutsoort Richting**||
|---|---|
|**Naam**|Richting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|richting|
|**Definitie**|Aanduiding van de richting van informatieobjecten van het|
||gerelateerde INFORMATIEOBJECTTYPE bij zaken van het|
||gerelateerde ZAAKTYPE.|
|**Herkomst definitie**|KING|
|**Datum opname**|1 juli 2012|
|**Formaat**|AN20|
|**Waardenverzameling**|'Inkomend', 'Intern', 'Uitgaand'|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|



113 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Voor een juiste behandeling van informatieobjecten van een INFORMATIEOBJECTTYPE is het van belang te weten langs welke route / met welk (gebruiks)doel ze in het zaakdossier zijn opgenomen. Zo is het, met het oog op de verantwoording van rechtmatig handelen, verstandig documenten die 'van buiten' kwamen of documenten die 'naar buiten' zijn verzonden zodanig in het zaakdossier op te slaan, dat de authenticiteit kan worden aangetoond. 

## **6.2.2. Relatieklasse ZAAK-INFORMATIEOBJECT-TYPE** 

## **ARCHIEFREGIME** 

## **Attribuutsoort Selectielijstklasse** 

|**Naam**|Selectielijstklasse|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|selectielijstklasse|
|**Definitie**|Verwijzing naar de voor het ZAAKINFORMATIEOBJECTTYPE bij het|
||RESULTAATTYPE relevante passage in de Selectielijst|
||Archiefbescheiden van de voor het ZAAKTYPE verantwoordelijke|
||overheidsorganisatie.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2013|
|**Formaat**|AN500|
|**Waardenverzameling**|de aanduidingen van de passages cq. klassen in de gehanteerde|
||selectielijst.|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

Bij gemeenten gaat het om de aanduidingen van de categorie in de Selectielijst waarin de archiefactietermijn wordt vermeld van de daartoe behorende soorten documenten die overeenkomen met het INFORMATIEOBJECTTYPE bij het ZAAKTYPE. In niet-gemeentelijke selectielijsten wordt soms een ander begrip dan categorie gehanteerd. Vandaar dat we hier het begrip ‘klasse’ hanteren. 

## **Attribuutsoort Archiefnominatie** 

114 

**==> picture [103 x 52] intentionally omitted <==**

|**Naam**|Archiefnominatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|archiefnominatie|
|**Definitie**|Aanduiding die aangeeft of informatieobjecten, van het|
||INFORMATIEOBJECTTYPE bij zaken van het ZAAKTYPE met een|
||resultaat van het RESULTAATTYPE, blijvend moeten worden|
||bewaardof (op termijn) moeten worden vernietigd.|
|**Herkomst definitie**|KING, o.b.v. Archiefwet 1995|
|**Datum opname**|23 september 2013|
|**Formaat**|A16|
|**Waardenverzameling**|Blijvend bewaren|
||Vernietigen|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||gerelateerde zaaktype.|



## **Toelichting** 

De attribuutsoort specificeert het ‘archiefregime’ voor de informatieobjecten van het INFORMATIEOBJECTTYPE bij het ZAAKTYPE waarvan de zaak het desbetreffende RESULTAATTYPE heeft. Het archiefregime van informatieobjecten van een INFORMATIEOBJECTTYPE bij het ZAAKTYPE kan in bijzondere gevallen afwijken van het archiefregime voor de zaakdossiers bij het ZAAKTYPE. 

In het geval van vernietigen wordt het document bij de zaak na enige tijd vernietigd. In het geval van blijvend bewaren wordt dat document na enige tijd overgebracht naar een archiefbewaarplaats (de in art. 12 van de Archiefwet 1995 bepaalde algemene termijn is 20 jaar). Door middel van de attribuutsoort Archiefactietermijn wordt gespecificeerd na verloop van hoeveel tijd wordt overgegaan tot vernietiging resp. overbrenging. 

## **Attribuutsoort Archiefactietermijn** 

|**Naam**|Archiefactietermijn|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|archiefactietermijn|
|**Definitie**|De termijn waarna informatieobjecten, van het|
||INFORMATIEOBJECTTYPE bij zaken van het ZAAKTYPE met een|
||resultaat van het RESULTAATTYPE, vernietigd of overgebracht|
||(naar een archiefbewaarplaats) moeten worden.|
|**Herkomst definitie**|KING|
|**Datum opname**|23 september 2013|
|**Formaat**|N4|
|**Waardenverzameling**|0-9999 maanden|
|**Indicatie materiële historie**|Ja|



115 

**==> picture [103 x 52] intentionally omitted <==**

**Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1 - 1 **Indicatie authentiek** Gemeentelijk kerngegeven **Regels** De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het gerelateerde zaaktype. 

## **Toelichting** 

Het archiefregime i.c. de vernietigings-- of overbrengingstermijn van informatieobjecten van een INFORMATIEOBJECTTYPE bij het ZAAKTYPE, kan in bijzondere gevallen afwijken van het archiefregime voor de zaakdossiers bij het ZAAKTYPE. Of sprake is van vernietigen of overbrengen (in het geval van blijvend bewaren) van een document van een specifiek INFORMATIEOBJECTTYPE bij een zaak van het ZAAKTYPE, is vastgelegd met de attribuutsoort Archiefnominatie. Met de attribuutsoort Archiefactietermijn wordt de desbetreffende termijn gespecificeerd. De algemene termijn voor overbrenging is 20 jaar cq. 240 maanden. 

De datum waarop de termijn start, is afhankelijk van de waarde van Brondatum archiefprocedure van RESULTAATTYPE. 

## **6.2.3. Relatieklasse ZAAKTYPENRELATIE** 

## **Attribuutsoort Aard relatie** 

|**Naam**|Aard relatie|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|aardRelatie|
|**Definitie**|Omschrijving van de aard van de relatie van zaken van het|
||ZAAKTYPE tot zaken van het andere ZAAKTYPE|
|**Herkomst definitie**|KING|
|**Datum opname**|21 februari 2013|
|**Formaat**|AN15|
|**Waardenverzameling**|- "vervolg" (een  zaak van het ZAAKTYPE is een te plannen vervolg|
||op een zaak van het andere ZAAKTYPE);|
||- "bijdrage" (een zaak van het ZAAKTYPE levert een bijdrage aan|
||het bereiken van de uitkomst van een zaak van het andere|
||ZAAKTYPE);|
||- “onderwerp” (een zaak van het ZAAKTYPE heeft|
||betrekking op een zaak van het andere ZAAKTYPE of een|
||zaak van het andere ZAAKTYPE is relevant voor of is|
||onderwerp van een  zaak van het ZAAKTYPE).|
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|1 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|



116 

**==> picture [103 x 52] intentionally omitted <==**

## **Regels** 

De attribuutsoort verandert alleen van waarde (materiële historie) op een datum die gelijk is aan een Versiedatum van het zaaktype. 

## **Toelichting** 

Zie de toelichtingen bij de relatiesoort ‘ZAAKTYPE heeft gerelateerd ZAAKTYPE’. 

## **Attribuutsoort Toelichting** 

|**Attribuutsoort Toelichting**||
|---|---|
|**Naam**|Toelichting|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|toelichting|
|**Definitie**|Een toelichting op de aard van de relatie tussen beide|
||ZAAKTYPEN.|
|**Herkomst definitie**|KING|
|**Datum opname**|21 februari 2013|
|**Formaat**|AN255|
|**Waardenverzameling**||
|**Indicatie materiële historie**|Ja|
|**Indicatie formele historie**|Nee|
|**Aanduiding gebeurtenis**|Nee|
|**Aanduiding brondocument**||
|**Indicatie in onderzoek**|Nee|
|**Aanduiding strijdigheid/nietigheid**|Nee|
|**Indicatie kardinaliteit**|0 - 1|
|**Indicatie authentiek**|Gemeentelijk kerngegeven|
|**Regels**|De attribuutsoort verandert alleen van waarde (materiële|
||historie) op een datum die gelijk is aan een Versiedatum van het|
||zaaktype.|



## **Toelichting** 

Het betreft een beschrijving van de situaties waarin de desbetreffende relatie zich kan voordoen. 

117 

**==> picture [103 x 52] intentionally omitted <==**

## **6.3 Referentielijst** 

## **6.3.1. Referentielijst INFORMATIEOBJECTTYPE-OMSCHRIJVING** 

## **GENERIEK** 

**Referentiegegeven Informatieobjecttype-omschrijving generiek** 

**Naam** Informatieobjecttype-omschrijving generiek **Herkomst** KING **Code XML-tag** omschrijving **Definitie** Algemeen gehanteerde omschrijving van het type informatieobject. **Herkomst definitie** KING **Datum opname** 1-1-2013 **Formaat** AN80 **Indicatie kardinaliteit** 1 - 1 **Toelichting** 

**Referentiegegeven Definitie informatieobjecttype-omschrijving generiek** 

**Naam** Definitie informatieobjecttype-omschrijving generiek **Herkomst** KING **Code XML-tag** definitie **Definitie** Nauwkeurige beschrijving van het generieke type informatieobject **Herkomst definitie** KING **Datum opname** 1-1-2013 **Formaat** AN255 **Indicatie kardinaliteit** 1 - 1 **Toelichting** 

## **Referentiegegeven Herkomst informatieobjecttype-omschrijving generiek** 

|**Naam**|Herkomst informatieobjecttype-omschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|herkomst|
|**Definitie**|De naam van de waardenverzameling, of van de beherende|
||organisatie daarvan, waaruit de waarde is overgenomen.|
|**Herkomst definitie**|KING|
|**Datum opname**|1-1-2013|
|**Formaat**|AN12|
|**Indicatie kardinaliteit**|1 - 1|
|**Toelichting**||



De kern van de waardenverzameling is overgenomen van de norm NEN2084 (herkomst: NEN2084). Deze is aangevuld met door KING als zinvol beoordeelde waarden (herkomst: KING). 

## **Referentiegegeven Hierarchie informatieobjecttype-omschrijving generiek** 

118 

**==> picture [103 x 52] intentionally omitted <==**

|**Naam**|Hierarchie informatieobjecttype-omschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|hierarchie|
|**Definitie**|De plaats in de rangorde van het informatieobjecttype.|
|**Herkomst definitie**|KING|
|**Datum opname**|1-1-2013|
|**Formaat**|AN80|
|**Indicatie kardinaliteit**|1 - 1|



## **Toelichting** 

Het betreft hier de plaats van het informatieobjecttype in of ten opzichte van de hierarchie van de informatieobjecttypen in de NEN2084. Een informatieobjecttype met een herkomst anders dan de NEN2084 komt pas vanaf niveau 2 in de hierarchie voor. Anders gezegd, de NEN2084 bepaalt de hoofdstructuur van de hierarchie. 

## **Referentiegegeven Opmerking informatieobjecttype-omschrijving generiek** 

|**Naam**|Opmerking informatieobjecttype-omschrijving generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|opmerking|
|**Definitie**|Zinvolle toelichting bij het informatieobjecttype|
|**Herkomst definitie**|KING|
|**Datum opname**|1-1-2013|
|**Formaat**|AN255|
|**Indicatie kardinaliteit**|0 - 1|
|**Toelichting**||



Het betreft vooral toelichting over het correct kunnen gebruiken van de informatieobjecttypen. Een voorbeeld is het op enig moment vervangen zijn van een informatieobjecttype door een ander informatieobjecttype d.w.z. het van naam veranderd zijn van het informatieobjecttype. 

## **Referentiegegeven Datum begin geldigheid informatieobjecttype-omschrijving generiek** 

|**generiek**||
|---|---|
|**Naam**|Datum begin geldigheid informatieobjecttype-omschrijving|
||generiek|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|ingangsdatumObject|
|**Definitie**|De datum waarop de generieke omschrijving van toepassing is|
||geworden.|
|**Herkomst definitie**|KING|
|**Datum opname**|1-1-2013|
|**Formaat**|OnvolledigeDatum|
|**Indicatie kardinaliteit**|1 - 1|
|**Toelichting**||



Met deze datum wordt aangegeven vanaf wanneer de generieke omschrijving toegepast kan worden. 

## **Referentiegegeven Datum einde geldigheid informatieobjecttype-omschrijving generiek** 

**Naam** Datum einde geldigheid informatieobjecttype-omschrijving 

119 

**==> picture [103 x 52] intentionally omitted <==**

||generiek|
|---|---|
|**Herkomst**|KING|
|**Code**||
|**XML-tag**|einddatumObject|
|**Definitie**|De datum waarop de generieke omschrijving niet meer van|
||toepassing is.|
|**Herkomst definitie**|KING|
|**Datum opname**|1-1-2013|
|**Formaat**|OnvolledigeDatum|
|**Indicatie kardinaliteit**|0 - 1|
|**Toelichting**||
|Met deze datum wordt|aangegeven vanaf wanneer de generieke omschrijving niet meer|
|toegepast kan worden.||



Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid’ kan in de registratie worden opgenomen. 

120 

**==> picture [103 x 52] intentionally omitted <==**

## **Bijlage 1: Wijzigingen ten opzichte van versie 2.0** 

In deze bijlage sommen we de structurele wijzigingen op die doorgevoerd zijn in versie 2.1 ten opzichte van versie 2.0 van de ZTC2. We doen dit per objecttype, relatieklasse en referentielijst, in alfabetische volgorde. Zie voor de wijzigingen in detail de versie van dit document met gemarkeerde wijzigingen. 

BESLUITTYPE: 

   - Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuutsoorten met uitzondering van de attribuutsoorten ‘Besluittype-omschrijving’, ‘Datum begin geldigheid besluittype’ en ‘Datum einde geldigheid besluittype’. 

   - Regel toegevoegd bij de attribuutsoorten ‘Datum begin geldigheid besluittype’ en ‘Datum einde geldigheid besluittype’. 

   - Indicatie materiële historie gewijzigd en regel toegevoegd bij de relatiesoort ‘BESLUITTYPE wordt vastgelegd in DOCUMENTINFORMATIEOBJECTTYPE’. 

- CATALOGUS: 

   - Definitie van de attribuutsoort ‘RSIN’ aangescherpt. 

   - Indicatie materiële historie en Indicatie formele historie gewijzigd van de attribuutsoort ‘RSIN’. 

EIGENSCHAP: 

- Indicatie materiële historie gewijzigd en regel toegevoegd bij de attribuutsoort ‘Definitie’. 

- De groepattribuutsoort ‘Specificatie van eigenschap’ toegevoegd. 

- De attribuutsoorten ‘Formaat’, ‘Lengte’, ‘Kardinaliteit’ en ‘Waardenverzameling’ onderdeel gemaakt van de groepattribuutsoort ‘Specificatie van eigenschap’. 

- De attribuutsoort ‘Groep’ toegevoegd aan de groepattribuutsoort ‘Specificatie van eigenschap’. 

- Definitie van de attribuutsoorten ‘Kardinaliteit’ en ‘Waardenverzameling’ aangescherpt. 

- Toegevoegd de groepattribuutsoort ‘Referentie naar eigenschap’ met de subattribuutsoorten ‘Objecttype’, ‘Informatiemodel’, ‘Namespace’, ‘Schemalocatie’, ‘X-path element’ en ‘Entiteittype’. 

- Indicatie materiële historie gewijzigd, kardinaliteit gewijzigd (naar 0..1) en regel toegevoegd (m.b.t. materiële historie) bij de attribuutsoort ‘Toelichting’ 

- De ‘historie-attribuutsoorten’ ‘Datum begin geldigheid eigenschap’ en ‘Datum einde geldigheid eigenschap’ toegevoegd. 

INFORMATIEOBJECTTYPE: 

- Naam van het objecttype DOCUMENTTYPE gewijzigd in INFORMATIEOBJECTTYPE. 

- Bij alle attribuut- en relatiesoorten de term ‘document’ vervangen door ‘informatieobject’. 

- Waardenverzameling van de attribuutsoort ‘DocumentInformatieobjecttypeomschrijving generiek’ gewijzigd zodat deze verwijst naar een referemtielijst die onderdeel uitmaakt van het informatiemodel ZTC2 (en niet meer RGBZ). 

- Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuutsoorten met uitzondering van de attribuutsoorten ‘Informatieobjecttype-omschrijving’, ‘Datum begin geldigheid Informatieobjecttype’ en ‘Datum einde geldigheid Informatieobjecttype’. 

121 

**==> picture [103 x 52] intentionally omitted <==**

- Regel toegevoegd bij de attribuutsoorten ‘Datum begin geldigheid Informatieobjecttype’ en ‘Datum einde geldigheid Informatieobjecttype’. 

- INFORMATIEOBJECTTYPE-OMSCHRIJVING GENERIEK: 

   - Referentielijst toegevoegd. 

RESULTAATTYPE: 

- Definitie van de attribuutsoort ‘Selectielijstklasse’ aangescherpt. 

- Formaat van de attribuutsoort ‘Archiefnominatie’ gewijzigd (in AN16). 

- Regels gewijzigd en toegevoegd bij de attribuutsoort ´Brondatum archiefprocedure´. 

- Van de attribuutsoort ‘Toelichting’ de kardinaliteit gewijzigd in 0..1 en regels toegevoegd. 

- Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuut- en relatiesoorten met uitzondering van de attribuutsoorten ‘Resultaattype-omschrijving’, ‘Datum begin geldigheid Resultaattype’ en ‘Datum einde geldigheid Resultaattype’ en de relatiesoort ‘RESULTAATTYPE is relevant voor ZAAKTYPE’. 

- Regel toegevoegd bij de attribuutsoorten ‘Datum begin geldigheid Resultaattype’ en ‘Datum einde geldigheid Resultaattype’. 

- Tweede regel toegevoegd bij de relatiesoort ‘RESULTAATTYPE heeft voor Brondatum archiefprocedure relevante EIGENSCHAP’ 

- Relatiesoort ‘RESULTAATTYPE bepaalt afwijkend archiefregime van ZAAKINFORMATIEOBJECT-TYPE’ toegevoegd. 

## ROLTYPE: 

   - Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuut- en relatiesoorten met uitzondering van de attribuutsoort ‘Roltype-omschrijving’ en de relatiesoort ‘ROLTYPE is van ZAAKTYPE’. 

   - De ‘historie-attribuutsoorten’ ‘Datum begin geldigheid roltype’ en ‘Datum einde geldigheid roltype’ toegevoegd. 

- STATUSTYPE: 

   - Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuut- en relatiesoorten met uitzondering van de attribuutsoorten ‘Statustype-omschrijving’, ‘Doorlooptijd status’, ‘Datum begin geldigheid Statustype’ en ‘Datum einde geldigheid Statustype’, de attribuutsoorten die deel uit maken van een groepattribuutsoort en de relatiesoort ‘STATUSTYPE is van ZAAKTYPE’. 

   - Regel toegevoegd m.b.t. materiële historie bij de attribuutsoorten ‘Doorlooptijd status’, ‘Datum begin geldigheid Statustype’ en ‘Datum einde geldigheid Statustype’. 

## ZAAK-INFORMATIEOBJECT-TYPE: 

- Naam van de relatieklasse ZAAK-DOCUMENT-TYPE gewijzigd in ZAAKINFORMATIEOBJECT-TYPE. 

- Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuutsoorten 

- Relatiesoort ‘RESULTAATTYPE bepaalt afwijkend archiefregime van ZAAKINFORMATIEOBJECT-TYPE’ toegevoegd. 

## ZAAK-INFORMATIEOBJECT-TYPE ARCHIEFREGIME: 

- Relatieklasse toegevoegd. 

ZAAKOBJECTTYPE: 

122 

**==> picture [103 x 52] intentionally omitted <==**

- Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij de attribuutsoorten ‘Ander objecttype’ en ‘Relatie-omschrijving’. 

- De ‘historie-attribuutsoorten’ ‘Datum begin geldigheid zaakobjecttype’ en ‘Datum einde geldigheid zaakobjecttype’ toegevoegd. 

## ZAAKTYPE: 

- Indicatie materiële historie gewijzigd en regel toegevoegd m.b.t. materiële historie bij alle attribuut- en relatiesoorten met uitzondering van de attribuutsoorten ‘Zaaktype-identificatie’, ‘Datum begin geldigheid zaaktype’ en ‘Datum einde geldigheid zaaktype’, de attribuutsoorten die deel uit maken van een groepattribuutsoort en de relatiesoort ‘ZAAKTYPE maakt deel uit van CATALOGUS’. 

- Tweede regel toegevoegd bij attribuutsoort ‘Zaaktype-omschrijving’. 

- Bij de attribuutsoort ‘Datum begin geldigheid zaaktype’ de definitie aangescherpt en een regel toegevoegd m.b.t. materiële historie. 

- Attribuutsoort ‘Versiedatum’ toegevoegd. 

- Regel toegevoegd m.b.t. materiële historie bij de attribuutsoort ‘Datum einde geldigheid zaaktype’. 

## ZAAKTYPENRELATIE: 

- Van de attribuutsoort ‘Aard relatie’ de waardenverzameling en de indicatie materiële historie gewijzigd en een regel toegevoegd m.b.t. materiële historie. 

- Van de attribuutsoort ‘Toelichting’ de kardinaliteit (in 0-1) en de indicatie materiële historie gewijzigd en een regel toegevoegd m.b.t. materiële historie. 

123 

**==> picture [103 x 52] intentionally omitted <==**

**==> picture [170 x 86] intentionally omitted <==**

**KWALITEITSINSTITUUT NEDERLANDSE GEMEENTEN** 

**NASSAULAAN 12 2514 JS  DEN HAAG** 

**POSTBUS 30435 2500 GK  DEN HAAG** 

**T 070 373 80 08 F 070 363 56 82** 

**INFO@KINGGEMEENTEN.NL WWW.KINGGEMEENTEN.NL** 

124 

