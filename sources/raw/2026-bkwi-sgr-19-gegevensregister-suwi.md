---
title: "Gegevensregister SUWI 19.0 — Deel 1: Beschrijving en gegevensmodel"
source: "https://sgr.bkwi.nl/sgr/SGR-19.0/SGR%2019.0%20Deel%201%20Beschrijving%20en%20gegevensmodel.pdf"
author: "BKWI"
published:
created: 2026-06-27
description: "Conceptueel gegevensmodel en berichtenregister voor gegevensuitwisseling tussen UWV, SVB en gemeenten (260 klassen, 930 attributen)"
tags:
  - "Werk en Inkomen"
---

**Gegevensregister SUWI 19.0** _Bijlage XII bij artikel 6.2 van de Regeling SUWI, bedoeld in artikel 5.20 van het Besluit SUWI_ 

## Deel 1 

Beschrijving en gegevensmodel 

## **INHOUDSOPGAVE DEEL 1: BESCHRIJVING EN GEGEVENSMODEL** 

|**1.** <br>**2.** <br>**3.** <br>**4.**|**INLEIDING**<br>**5**|
|---|---|
||1.1 Het SUWI-Gegevensregister ....................................................................................................... 5<br>1.1.1<br>Het SUWI-Gegevensmodel .......................................................................................... 6<br>1.1.2<br>Het SUWI-Berichtenregister ......................................................................................... 7<br>1.1.3<br>XML-extensies op het SUWI-Gegevensmodel voor de definitie van SuwiML ........... 8<br>1.2 SGR/SuwiML .............................................................................................................................. 8<br>1.3 Verhouding ten opzichte van versie 18.0 .................................................................................... 9<br>1.4 Leeswijzer ................................................................................................................................... 9<br>**BERICHTENREGISTER**<br>**10**|
||2.1 Inleiding .................................................................................................................................... 10<br>2.2 Overzichtstabel .......................................................................................................................... 10<br>2.3 Partijen en uitwisselingsmomenten ........................................................................................... 11<br>**SYSTEMATIEK ITEMCHARTS**<br>**12**|
||3.1 Uitgangspunten .......................................................................................................................... 12<br>3.2 Rubrieken op de Itemcharts ....................................................................................................... 13<br>**CONCEPTUEEL GEGEVENSMODEL**<br>**15**|
||4.1 Verklaring systematiek .............................................................................................................. 15<br>4.2 Beschrijving SUWI-Gegevensmodel ........................................................................................ 16<br>4.3 Conceptueel gegevensdeelmodel Stamgegevens ...................................................................... 16<br>4.4 Conceptueel gegevensdeelmodel Arbeidsmarktkwalificaties ................................................... 18<br>4.5 Conceptueel gegevensdeelmodel Arbeidsgegevens .................................................................. 20<br>4.6 Conceptueel gegevensdeelmodel Arbeidsverleden ................................................................... 21<br>4.7 Conceptueel gegevensdeelmodel Uitkeringsgegevens .............................................................. 22<br>4.8 Conceptueel gegevensdeelmodel Arbeidstoeleidingsgegevens ................................................ 28<br>4.9 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Polisadministratie ........................ 33<br>4.10 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Rijksdienst voor het Wegverkeer<br>(RDW) 34<br>4.11 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Kadaster ....................................... 35<br>4.12 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Basisregistratie Personen (BRP) .. 36<br>4.13 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Dienst Uitvoering Onderwijs<br>(DUO) 38<br>4.14 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Belastingdienst ............................. 39<br>4.15 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit het Handelsregister (HR) ............. 40<br>4.16 Conceptueel gegevensdeelmodel van Verbeteren Uitwisseling Matchingsgegevens (VUM) .. 44<br>4.17 Conceptueel gegevensdeelmodel van de instrumentengidsen Dennis & Eva ........................... 49|



|4.18 Conceptueel gegevensdeelmodel Adresgegevens .....................................................................|52|
|---|---|
|4.19 Conceptueel gegevensdeelmodel SUWI-algemeen ..................................................................|53|
|**5.** **STANDAARDSTRUCTUREN**|**54**|
|5.1 Toelichting op de standaardstructuren ......................................................................................|54|
|5.2 Standaardstructuur Adres Nederland ........................................................................................|56|
|5.3 Standaardstructuur Adres Buitenland ........................................................................................|58|
|5.4 Standaardstructuur Bankrekeningnummer Buitenland .............................................................|59|
|5.5 Standaardstructuur Bedraggegevens .........................................................................................|60|
|5.6 Standaardstructuur Telefoonnummer ........................................................................................|61|
|5.7 Standaardstructuur Datum .........................................................................................................|62|
|5.8 Standaardstructuur Tijdstip .......................................................................................................|63|
|**6.** **NORMINSTANTIES EN BEHERENDE INSTANTIES**|**64**|
|6.1 Definitie norminstantie ..............................................................................................................|64|
|6.2 Overzicht norminstanties ...........................................................................................................|64|
|6.3 Definitie beherende instantie .....................................................................................................|65|
|**7.** **AANVULLENDE SUWIML-TAGS**|**66**|
|**BIJLAGE 1**<br>**OVERZICHT SGR-GEGEVENS- WETTELIJKE GRONDSLAG**|**67**|
|**BIJLAGE 2**<br>**TABEL BERICHTENINDEX**|**68**|
|**BIJLAGE 3A**<br>**OVERZICHT GEGEVENS GETOOND OP KLANTBEELD DIGITAAL**||
|**KLANTDOSSIER**|**69**|
|**BIJLAGE 3B**<br>**VERTALING IN BEGRIJPELIJKE TAAL VAN GEGEVENS OP**||
|**KLANTBEELD DIGITAAL KLANTDOSSIER**|**70**|



## **DEEL 2: ITEMCHARTS KLASSEN EN ATTRIBUTEN** 

## **1.  INLEIDING** 

## **1.1 Het SUWI-Gegevensregister** 

Het SUWI-Gegevensregister (SGR) is de standaard die binnen het SUWI-domein wordt gehanteerd voor het uitwisselen van gegevens tussen de SUWI-partijen. Het UWV, de SVB en de Burgemeester en Wethouders van de gemeenten werken samen om de inschakeling van uitkeringsgerechtigden en werkzoekenden in het arbeidsproces te bevorderen. Zij werken voorts samen met andere diensten en instellingen die werkzaamheden verrichten die verband houden met de uitoefening van hun taken. De samenwerking kan mede betrekking hebben op het uitwisselen van gegevens tussen de genoemde partijen _[1]_ . Het Inlichtingenbureau (IB) heeft daarin een dienstverlenende en coördinerende rol ten behoeve van gemeenten. 

In Artikel 6.2 van de Regeling SUWI is het Gegevensregister SUWI als volgt geformuleerd: 

In bijlage XII (‘Gegevensregister SUWI’) bij deze regeling is het Gegevensregister SUWI opgenomen, bedoeld in artikel 5.20 van het Besluit SUWI. 

- In bijlage XVIII (‘Gegevensregister IB’) bij deze regeling zijn gegevens opgenomen als bedoeld in artikel 5.24, tweede lid, van het Besluit SUWI, die door het IB worden verwerkt. 

## Vervolgens staat in de Regeling SUWI het volgende: 

## _Transparantie van gegevensleveringen en eenduidigheid in gegevensdefinities en technische standaarden; het SUWI Gegevensregister (SGR)_ 

Op hoofdlijnen bevat het SGR enerzijds een Conceptueel Gegevensmodel (object en gegevensdefinities van met de centrale voorziening uitgewisselde gegevens) en de technische standaarden. Anderzijds bevat het SGR een Berichtenregister. Het Berichtenregister geeft weer ten behoeve van welke wettelijke taak (doelbinding) welke gegevenssoorten (proportionaliteit) door wie (verantwoordelijke) aan wie (verwerker) met de centrale voorziening worden uitgewisseld. 

- Het SGR wordt aangepast wanneer tot daadwerkelijke levering wordt overgegaan. Het berichtenregister is publiek. 

De daadwerkelijke gegevenslevering vindt vervolgens plaats op basis van de gegevensdefinitie in het Conceptueel Gegevensmodel. Het SGR is als zodanig het referentiekader voor systeembouwers. 

## Scope: 

In het SGR worden alle gegevens vastgelegd die via de Gezamenlijke Elektronische Voorzieningen SUWI (GeVS) beschikbaar worden gesteld. Ook al worden de gegevens maar door één ketenpartij geleverd en gebruikt. Dit laatste geldt alleen voor de gegevens vanuit de Polisadministratie. 

## Het SGR dient aldus te bevatten: 

1. alle tussen de SUWI-partijen uit te wisselen gegevens (definitie en formaat); 

2. de berichten die worden uitgewisseld of de koppelvlakken (samenstelling, zendende en ontvangende partijen, condities); 

3. de vastlegging van een gemeenschappelijke taal voor elektronische gegevensuitwisseling, SuwiML. 

Het SGR kent de volgende onderdelen, die tezamen invulling geven aan de doelstelling zoals die in de Regeling SUWI is gedefinieerd: 

- het SUWI-Gegevensmodel; 

- het SUWI-Berichtenregister; 

- XML-extensies op het SUWI-Gegevensmodel voor de definitie van SuwiML. 

De technische beschrijving van SuwiML is in een aantal afzonderlijke documenten, zoals SuwiML-Berichtstandaard en SuwiML-Transactiestandaard, vastgelegd. Deze vormen samen met het SGR de standaard SGR/SuwiML. 

> _1_ Artikel 9, lid 1 van de Wet SUWI 

## **1.1.1 Het SUWI-Gegevensmodel** 

Het SUWI-Gegevensmodel geeft een eenduidige en ondubbelzinnige definitie van gegevens en hun betekenis ten behoeve van de uitwisseling en verwerking van informatie - zoals die gerepresenteerd wordt door deze gegevens - door de verschillende partijen. 

Het SUWI-Gegevensmodel is een conceptueel gegevensmodel, dat wordt weergegeven in de vorm van een UML-klassendiagram, met de definities van klassen, attributen en relaties. 

Een conceptueel gegevensmodel geeft een abstracte beschrijving van de werkelijkheid, in dit geval die van het SUWI-domein (het werkterrein van UWV, SVB en gemeenten) en een deel van de externe bronnen, waaruit de gegevens worden ontsloten, die nodig zijn voor de uitvoering van hun wettelijke taken. Het gezichtspunt van de beschrijving is dat van gemeenschappelijk gegevensgebruik door de SUWI-organisaties in het kader van de uitvoering van de wet SUWI. 

Het SUWI-Gegevensmodel bevat alle gegevensgroepen en –elementen die ten behoeve van de GeVS worden gebruikt, door de SUWI-partijen onderling worden uitgewisseld en die door de SUWI-partijen vanuit de externe bronnen worden ontsloten. Het SUWI-Gegevensmodel is toegankelijk gemaakt door het op te delen in een aantal thema’s: stamgegevens, arbeidsgegevens, uitkeringsgegevens, arbeidstoeleidinggegevens enz. Deze thema’s zijn op afzonderlijke diagrammen toegelicht. 

De systematiek van de diagrammen wordt beschreven in hoofdstuk 4.1. 

De verschillende klassen en attributen worden afzonderlijk beschreven op zogenaamde Itemcharts: 

- voor elke klasse is er een Itemchart met de unieke naam, de definitie van de klasse en een lijst van de gebruikte attributen; 

- voor elk attribuut is er een Itemchart met onder meer de unieke naam voor het gegeven, een definitie van de betekenis van het gegeven, een beschrijving van het waardebereik en de codering daarvan. Het waardebereik van een aantal gegevens is in aparte tabellen opgenomen. 

De systematiek van de Itemcharts wordt beschreven in hoofdstuk 3. 

## **Weergave** 

Het conceptueel gegevensmodel wordt afgebeeld in de vorm van een UML-klassendiagram, dat de samenhang weergeeft van de verschillende gegevens door ze in groepen te plaatsen (d.w.z. als klassen met attributen) en dat de samenhang tussen de verschillende klassen laat zien door middel van getekende relaties. Het SUWI-Gegevensmodel bestaat uit een groot aantal gegevens en hun definities en de vastlegging van de onderlinge samenhang. Een en ander wordt grafisch getoond in een aantal diagrammen. 

De gegevens geven aan hoe eigenschappen van objecten in de werkelijkheid worden vastgelegd; een gegevensdefinitie beschrijft een eigenschap, geeft het formaat aan van de waarde die de eigenschap kan hebben (bijvoorbeeld tekst, of datum), en waar dat van toepassing is het bereik van die waarden (dit gebeurt bijvoorbeeld in de vorm van een tabel). Naast de gegevens beschrijft het SGR ook de objecten waar die gegevens eigenschappen van zijn. Dit gebeurt in de vorm van klassen. 

Om hiervan een voorbeeld te geven nemen we 'Cliënt'. In de werkelijkheid van het SUWI-domein bestaat het object 'Cliënt' met eigenschappen zoals naam, geboortedatum en burgerservicenummer. De persoon die zich bij het UWV als werkzoekende heeft ingeschreven, is in het SUWI-domein zo'n object. In het SGR is dit in eerste instantie gemodelleerd als klasse CLIENT SUWI met de daarbij behorende attributen. In tweede instantie zijn – in het proces van de gegevensmodellering - de naamattributen, geboortedatum en burgerservicenummer in een aparte klasse NATUURLIJK PERSOON gezet. De klasse CLIENT SUWI is een bepaald type van NATUURLIJK PERSOON. Een ander type van NATUURLIJK PERSOON is KIND; ook KIND heeft een naam, geboortedatum en burgerservicenummer. Door de gemeenschappelijke gegevens (eigenschappen) in een aparte klasse te plaatsen kunnen ze hergebruikt worden en hoeven ze maar één keer te worden gedefinieerd. 

Het SGR bevat ongeveer 260 klassen en 930 attributen (exclusief Verbeteren Uitwisseling Matchingsgegevens (VUM) en instrumentengidsen Dennis & Eva); voor de overzichtelijkheid zijn ze 

geordend in een aantal submodellen. In die submodellen zijn de gegevens weer geordend naar deelaspecten als opleiding en werkervaring. Hiernaast is een aantal submodellen naar gebruiksdoel opgenomen. Deze submodellen geven een kijk (een view) op het totaal, waarin alleen die klassen getoond worden die voor een bepaald doel van belang zijn, bijvoorbeeld een bepaalde gegevensuitwisseling zoals een aanvraag voor een uitkering. 

De object- en gegevensdefinities, alsmede de ordening van de gegevens in het conceptueel gegevensmodel, zijn nadrukkelijk een representatie van de werkelijkheid. Het conceptueel gegevensmodel bevat daarmee nog geen blauwdruk voor systeembouw, maar dat model biedt wel een goed uitgangspunt voor bijvoorbeeld een databaseontwerp. Systeembouwers zullen op basis van de systeemeisen de gegevensdefinities uit het conceptueel gegevensmodel moeten vertalen naar de te gebruiken datastructuren voor een specifiek systeem. Het conceptueel gegevensmodel geeft een model van de werkelijkheid van de gegevensuitwisseling en -verwerking en het is geen direct model van een database. 

Wanneer een bestaand systeem niet voldoet aan het SGR, dan hoeft dat systeem niet integraal te worden aangepast. Waar een systeem (geautomatiseerd) gegevens uitwisselt (met andere systemen) in het SUWI-domein, dient het, voor die uitwisseling, uiteraard wél het SGR te volgen _._ 

## **1.1.2 Het SUWI-Berichtenregister** 

Het SUWI-Berichtenregister bevat een beschrijving van de berichten die in het SUWI-domein worden uitgewisseld. Onder een bericht wordt hier verstaan een gestructureerde set informatie (gegevens) die is samengesteld met het oog op uitwisseling door middel van de Suwinet-functionaliteiten Inkijk, Inlezen en Meldingen. De beschrijving bestaat uit een berichtindex, met de naam van het bericht, de partijen waartussen het wordt uitgewisseld, de uitwisselingsmomenten, en een opsomming van de gegevens die het maximaal kan bevatten. 

In het kader van de Wet Eenmalige Uitvraag van gegevens (WEU) is een overzicht met aanduiding van SGR-gegevens ten opzichte van de wettelijke grondslag beschikbaar. Dit met het doel voor zowel de burgers als de professionals, de gegevensuitwisselingen binnen de Gezamenlijke elektronische Voorziening SUWI (GeVS) zodanig transparant te maken dat inzichtelijk wordt op basis van welke wettelijke grondslag (doelbinding) welke gegevens (proportionaliteit) door wie (verantwoordelijke) aan wie (verwerker) worden geleverd en zodoende partijen aanspreekbaar te maken op naleving van de AVG (Algemene verordening gegevensbescherming). Daarbij wordt gebruik gemaakt van het overzicht waarbij op de X-as (horizontale as) de sociale wetten zijn gepositioneerd ten opzichte van, op de Y-as (verticale as), de gegevens. Op deze wijze wordt, indien als zodanig met een kruisje in de gezamenlijke cel aangegeven, per gegeven zichtbaar op basis van welke wettelijke grondslag(en) een gegeven wordt geleverd en gebruikt/geraadpleegd. Dit overzicht voegt enerzijds een extra (verticale) kolom op de X-as toe waarin per gegeven is aangegeven wie de bronhouder van of de verantwoordelijke voor dat gegeven is. Anderzijds is per wet aangegeven wie deze uitvoert. Met het laatste wordt tevens inzichtelijk wie de verwerker is. 

Het SUWI-Berichtenregister bevat tevens een overzicht van welke gegevens aan de klant worden getoond (het klantbeeld). Zodoende wordt de voortgang van de effectuering van het principe van éénmalige uitvraag en meermalig gebruik binnen het SUWI-domein eveneens transparant. 

## **1.1.3 XML-extensies op het SUWI-Gegevensmodel voor de definitie van SuwiML** 

Voor ieder gegeven (klasse of attribuut) is een SuwiML-tag opgenomen op de Itemchart. Dit betreft een XML-tag[2] , die als rubriek is opgenomen in de Itemcharts. Hiermee wordt elk gegeven in op XML gebaseerde gegevensuitwisselingen in het SUWI-domein uniek geïdentificeerd en gerelateerd aan de definities in het SGR. Daarnaast is er een aantal SuwiML-tags gedefinieerd die bepaalde relaties, of rollen van een klasse in een relatie, in de gegevens- en berichtenmodellen implementeren (Domicilieadres, Feitelijk adres e.d. als rollen van het standaardadres). Hiermee is het vocabulaire van de taal voor elektronische gegevensuitwisseling in het SUWI-domein, SuwiML, in het SGR vastgelegd. 

De overige onderdelen van SuwiML (het SuwiML-Basisschema, de SuwiML-Transactiestandaard en de SuwiML-Berichtstandaard) zijn in aparte componenten en documenten, los van het SGR-document, opgenomen. Het SGR en SuwiML vormen tezamen de uitwisselingsstandaard SGR/SuwiML. SuwiML is een standaard die in hoge mate wordt bepaald door ontwikkelingen in de techniek. Zij wordt vastgesteld in het domeingroepsoverleg of Managementoverleg afspraken en voorzieningen gegevensuitwisseling SUWI. 

## **1.2 SGR/SuwiML** 

Het SGR is de basis voor de elektronische gegevensuitwisseling in het SUWI-domein. Het bevat daarvoor de gegevensbeschrijvingen, formaten, en de logische structuur van de berichten. Op deze basis is voor de elektronische gegevensuitwisseling in het SUWI-domein een gemeenschappelijke taal ontwikkeld, aangeduid als SuwiML, onder gebruikmaking van XML en hierop gebaseerde standaarden. 

Doel SuwiML: 

_SuwiML heeft tot doel de elektronische gegevensuitwisseling tussen partijen in het SUWIdomein (UWV, SVB, gemeenten en IB_[3] _) te faciliteren. Dit betreft zowel het faciliteren van de ontwikkeling van de gegevensuitwisseling (het zo eenvoudig mogelijk maken van het definiëren en realiseren van berichten) als de ondersteuning van de operationele gegevensuitwisseling (het gebruik door systemen van SuwiML-schema’s bij het maken of verwerken van berichten). SuwiML biedt de basis voor een eenduidige en ondubbelzinnige definitie van de uit te wisselen gegevens en is een standaard voor de codering van gegevens en berichten bij elektronische gegevensuitwisseling._ 

Een groot deel van SuwiML wordt vastgelegd en gedefinieerd door middel van het SGR. De overige onderdelen zijn het SuwiML-Basisschema (de vertaling van de SGR-gegevens naar XML), de SuwiMLBerichtstandaard met richtlijnen voor het samenstellen van berichten en de SuwiMLTransactiestandaard met richtlijnen voor de verpakking van berichten, stuurgegevens voor berichten, het gebruik van onderliggende communicatieprotocollen en foutafhandeling. 

Daar waar gegevensuitwisseling plaatsvindt in het SUWI-domein, dienen de gegevens te voldoen aan het SGR en dient de elektronische gegevensuitwisseling conform SuwiML te zijn. Dit geldt tevens voor de vormgeving van berichten en transacties. Het SGR is van toepassing voor alle vormen van gestructureerde gegevensuitwisseling in het SUWI-domein. 

Voor de gegevensuitwisseling in het SUWI-domein wordt momenteel het gebruik van twee soorten van gestructureerde gegevensuitwisseling onderscheiden: 

- Suwinet-Inkijk, voor het online opvragen van gegevens 

- Suwinet-Inlezen, voor het automatisch inlezen van gegevens tussen applicaties. 

Voor beide vormen is de toepassing van SuwiML verplicht. 

> _2_ Voor XML wordt verwezen naar: Extensible Markup Language 1.0. W3C recommendation 10-february-1998. Archived at www.w3.org/TR/REC-xml. Tevens wordt verwezen naar: Extensible Markup Language (XML) 1.0 (Second edition): W3C recommendation 6-october-2000. Archived at www.w3.org/TR/REC-xml. 

> _3_ Dit betreft het IB als dienstverlenende partij in dit domein ten behoeve van de gemeenten. 

## **1.3 Verhouding ten opzichte van versie 18.0** 

De vorige versie 18.0 van het SGR bevat de gegevens die uitgewisseld zijn in het kader van de samenwerking binnen de keten Werk en Inkomen tot en met december 2022. 

In de periode van januari 2023 t/m december 2024 zijn er wijzigingsverzoeken op het SGR beoordeeld en goedgekeurd door de Werkgroep Gegevens & Berichten (WGB) onder toezicht van de Domeingroep Gegevens & Berichten (DGB). Daarbij werden er adviezen ter vaststelling meegegeven. De goedgekeurde wijzigingsverzoeken zijn in deze versie van het SGR verwerkt. 

De belangrijkste aanvullingen in versie 19.0 van het SGR worden hieronder weergegeven. 

- De nieuwe en aangepaste gegevens met betrekking tot de wijzigingen in de Loonaangifte 2024 en 2025; 

- De nieuwe en aangepaste gegevens met betrekking tot het Kadaster, de Rijksdienst voor het Wegverkeer (RDW) en de Kamer van Koophandel (KvK); 

- De nieuwe gegevens met betrekking tot Verbeteren Uitwisseling Matchingsgegevens (VUM); 

- De nieuwe gegevens met betrekking tot de instrumentengidsen Dennis & Eva; 

- Reguliere wijzigingsverzoeken; 

- Jaarlijks opschoning en onderhoud. 

Ten opzichte van de vorige versie is de wijze van datamodelleren gewijzigd in versie 19.0 van het SGR. In de vorige versie van het SGR werd het SUWI-Gegevensmodel vormgegeven in een EntiteitenRelatie-Diagram (ERD). In de nieuwe versie wordt gebruikgemaakt van een UML-klassendiagram. Ten opzichte van de vorige versie is de naamgeving van de entiteiten gewijzigd in klassen en de gegevenselementen gewijzigd in attributen. 

Sommige gegevens met betrekking tot VUM moeten nog worden geïmplementeerd in de praktijk. Met het Inlichtingenbureau zijn afspraken gemaakt om rekening te houden met de gegevens over VUM die in deze versie van het SGR staan vermeld. 

## **1.4 Leeswijzer** 

De overige hoofdstukken van dit deel 1 van het SGR hebben de volgende inhoud: 

Hoofdstuk 2 bevat de toelichting van het Berichtenregister. 

In hoofdstuk 3 wordt de systematiek van de Itemcharts beschreven. 

In hoofdstuk 4 wordt het conceptueel gegevensmodel gepresenteerd. 

In hoofdstuk 5 zijn standaardstructuren opgenomen. In Itemcharts wordt hiernaar verwezen. 

In hoofdstuk 6 wordt een uitleg gegeven over de begrippen norminstantie en beherende instantie, en wordt weergeven naar welke externe standaarden wordt verwezen vanuit de Itemcharts. 

In hoofdstuk 7 zijn aanvullende SuwiML-tags opgenomen. 

In de bijlagen zijn de volgende overzichtstabellen opgenomen: 

- 1. Overzicht SGR-gegevens – Wettelijke grondslag 

- 2. Berichtenindex 

- 3a. Overzicht gegevens getoond op klantbeeld Digitaal Klantdossier 

- 3b. Lijst van klantvriendelijke verklaring van gegevens die getoond zijn op klantbeeld. 

Deel 2 bevat alle Itemcharts. 

## **2. BERICHTENREGISTER** 

## **2.1 Inleiding** 

Dit hoofdstuk bevat de toelichting van het Berichtenregister. Het Berichtenregister wordt naast de Berichtenindex, uitgebreid met overzichtstabellen van SGR-gegevens ten opzichte van de wettelijke grondslag en het overzicht van gegevens die getoond zijn in het klantbeeld van Digitaal Klantdossier. Deze overzichtstabellen zijn in de bijlagen opgenomen, omdat deze overzichtstabellen een dynamisch karakter hebben en regelmatig aan wijzigingen onderhevig zijn. 

De Berichtenindex bestaat uit een overzichtstabel van het gegevensregister. Hierin is voor de uitgewisselde berichten in het SUWI-domein voor alle klassen en attributen aangegeven of het onderdeel uitmaakt van de bedoelde berichten. De Berichtenindex is gebaseerd op de berichtspecificaties in het Berichtenregister. Daarnaast wordt in dit hoofdstuk een overzicht opgenomen, waarin wordt weergegeven tussen welke partijen de uitwisseling plaatsvindt en op welke momenten de uitwisseling kan plaatsvinden. 

## **2.2 Overzichtstabel** 

In de overzichtstabellen zijn een horizontale as en een verticale as gebruikt. De verticale as bevat een overzicht van de klassen en attributen die behoren tot het gegevensregister. In de tabel wordt middels een ‘kruisje’ aangegeven of de klasse dan wel het attribuut deel uitmaakt van het betreffende onderwerp, hetzij een bepaalde wet, hetzij een bericht. Een leeg veld betekent dat het gegeven geen onderdeel uitmaakt van het betreffende onderwerp. 

In de toelichting van de bijbehorende overzichtstabel wordt aangegeven welke bijzonderheden er zijn van de invulling van het overzicht. 

## **2.3 Partijen en uitwisselingsmomenten** 

In de volgende tabel wordt voor de bronberichten (dossierberichten) uit de _berichtenindex_ weergegeven tussen welke partijen uitwisseling plaatsvindt. De uitwisseling vindt op elk moment plaats in het bedrijfsproces waarop een gebruiker of applicatie gegevens nodig heeft voor de uitvoering van een processtap. 

Op basis van deze bronberichten worden berichten-op-maat gemaakt, specifiek voor de geautoriseerde afnemer(s) of organisatie(s) op basis van de doelbinding en proportionaliteit. De berichten-op-maat voor bepaalde afnemer(s) zijn op te vragen bij BKWI en Inlichtingenbureau. 

|**Bericht**|**Leverende partij**|**Afnemende partij**|
|---|---|---|
|UWVWb Dossier Persoon|UWV WERKbedrijf|UWV, GSD, SVB, Nederlandse Arbeidsinspectie|
|UWV Dossier Arbeidsverleden|UWV|UWV, GSD, SVB, Nederlandse Arbeidsinspectie|
|UWV Dossier Reintegratie|UWV WERKbedrijf|UWV, GSD|
|UWV Dossier Loonheffingen|UWV|Nederlandse Arbeidsinspectie|
|UWV Dossier Inkomsten|UWV|UWV, GSD, SVB, Nederlandse Arbeidsinspectie, CAK,<br>Dienst Justis, DUO, IND|
|UWV Dossier<br>Werknemersverzekeringen|UWV|UWV, GSD, SVB, Nederlandse Arbeidsinspectie, CAK,<br>Dienst Justis, IND|
|UWV Dossier Aanvraag<br>Uitkering Status|UWV|UWV, GSD|
|SVB Dossier Persoon|SVB|UWV, GSD, SVB, CAK|
|Bijstandsregelingen|GSD & SVB|UWV, GSD, SVB, Dienst Justis, IND, Nederlandse<br>Arbeidsinspectie|
|GSD Dossier Reintegratie|GSD|UWV, GSD, SVB|
|BRP Dossier Persoon-sets|BRP|UWV, GSD, SVB, Nederlandse Arbeidsinspectie|
|PIVA Dossier Persoon|PIVA|GSD|
|DUO Dossier Persoon|DUO|UWV, GSD|
|DUO Dossier Studiefinanciering|DUO|UWV, GSD, SVB|
|Kadaster Dossier|Kadaster|GSD, SVB, Nederlandse Arbeidsinspectie|
|BD Dossier Persoon|BD (via IB)|GSD|
|RDW Dossier|RDW|UWV, GSD, SVB, Nederlandse Arbeidsinspectie|
|UWV Dossier Quotum<br>Arbeidsbeperkten|UWV|UWV, GSD|
|NHR Inschrijving|HR|GSD, Nederlandse Arbeidsinspectie, SVB, UWV|
|NHR Vestiging|HR|GSD, Nederlandse Arbeidsinspectie, SVB, UWV|
|NHR Zoeken|HR|GSD, Nederlandse Arbeidsinspectie, SVB, UWV|



De afnemende partijen zijn de geautoriseerde Suwinet-gebruiker of applicatie, op basis van de rol en regels in gemeenschappelijke gebruikersadministratie Suwinet. 

## **3. SYSTEMATIEK ITEMCHARTS** 

In dit hoofdstuk wordt beschreven hoe de Itemcharts zijn opgebouwd. 

De Itemcharts bieden een gestandaardiseerde beschrijving van de SUWI-gegevenselementen. Elke Itemchart beschrijft een klasse of attribuut door middel van een aantal kenmerken ofwel rubrieken. 

## **3.1 Uitgangspunten** 

Bij het beschrijven van de gegevens zijn de volgende uitgangspunten gehanteerd: 

De gegevensbeschrijvingen zijn in eerste instantie gebaseerd op internationale, nationale en vervolgens op sectorale standaarden. Pas als er geen bestaande standaard is voor een gegeven, die aansluit bij het gebruik van dat gegeven in het SUWI-domein, is een eigen beschrijving gemaakt. Voor de verschillende gehanteerde standaarden, zie Hoofdstuk 4 _Norminstanties en beherende instanties_ . 

In de gegevensbeschrijvingen staan soms woorden of groepen van woorden in hoofdletters weergegeven. Hiermee wordt een verwijzing aangegeven naar de beschrijving van een term (begrip), een standaardtabel, een standaardstructuur of een ander gegeven. 

Het onderscheid in gegevens, termen, standaardtabellen en standaardstructuren is gemaakt om de gegevensbeschrijvingen zo duidelijk en zo eenvoudig mogelijk te houden en om het beheer van de gegevensbeschrijvingen te vergemakkelijken. 

Een _term_ is een begrip dat gebruikt wordt in de beschrijving van bijvoorbeeld een gegeven, en niet al is beschreven als (samengesteld) attribuut, 

Een _standaardtabel_ beschrijft in feite een standaard waardebereik. Een standaard waardebereik is een waardebereik dat voor meerdere gegevens geldt of een waardebereik dat door een andere (norm)instantie wordt beheerd dan de SUWI-beheerorganisatie. 

Een _standaardstructuur_ geeft condities aan die gelden voor het gebruik van de samenstellende delen van een samengesteld gegeven of die gelden voor het waardebereik van enkelvoudige attributen. 

De relaties tussen de verschillende samengestelde attributen (klassen) worden weergegeven in UMLklassendiagram, zie hiervoor hoofdstuk 4. De relaties zijn niet in de Itemcharts opgenomen. De Itemcharts zijn pure gegevensbeschrijvingen. De klassen worden apart van de attributen beschreven. 

## **3.2 Rubrieken op de Itemcharts** 

De klassen en attributen worden door middel van de volgende rubrieken in de Itemcharts beschreven: 

1. _Naam_ 

De naam voldoet aan de volgende voorwaarden: 

- hij is uniek; 

- hij maakt, indien van toepassing, gebruik van ingeburgerde namen; 

- hij sluit zoveel mogelijk aan bij naamgeving zoals die voorkomt in wet- en regelgeving, zoals die wordt gehanteerd in bestaande normen of zoals die voorkomt in een andere Itemchart. 

## 2. _SuwiML-tag_ 

Een unieke identificatie van het gegeven, voor gebruik als codering van het gegeven in elektronische gegevensuitwisseling op basis van XML. 

3. _Formaat_ (alleen van toepassing bij attributen) 

   - Voor attributen is dit de aanduiding van de lengte en de set beschikbare karakters die geldt voor de waarde van het attribuut. 

Het formaat is aangegeven door middel van de volgende notatie, waarbij de cijfers slechts als voorbeeld dienen: 

N6 6 numerieke tekens, vaste lengte A3 3 alfabetische tekens, vaste lengte AN5 5 alfanumerieke tekens, vaste lengte N..9 maximaal 9 numerieke tekens A..6 maximaal 6 alfabetische tekens AN..35 maximaal 35 alfanumerieke tekens 

De numerieke tekens zijn de Arabische cijfers 0 tot en met 9. 

De alfabetische tekens zijn alle niet-numerieke tekens en betreffen de kleine letters, de hoofdletters en overige tekens (inclusief besturings- en/of speciale tekens). 

De alfanumerieke tekens zijn zowel de numerieke als de alfabetische tekens. 

Bij numerieke tekens is het formaat exclusief: 

- decimaal teken 

- positief/negatief teken 

- scheidingsteken voor drietallen 

## 4. _Definitie_ 

De unieke beschrijving van het item, die slechts op één manier is uit te leggen en die dient ter verduidelijking van de betekenis van het item. 

5. _Norm(instantie)_ 

De organisatie die verantwoordelijk is voor de normering van het item, dan wel de standaard, norm of conventie waarop de normering van het item is gebaseerd. 

6. _Waardebereik_ (alleen van toepassing bij attributen) De aanduiding voor de set met waarden die het attribuut mag aannemen. Deze is niet gevuld in gevallen waar het waardebereik niet van toepassing is (bij samengestelde attributen) of waarbij het waardebereik voor zich spreekt (bij enkelvoudige attributen zonder beperkingen op het waardebereik, anders dan aan gegeven door middel van de rubriek "Formaat"). 

Het waardebereik is op één van de volgende manieren beschreven: 

   - als opsomming (kleine tabellen) 

   - als verwijzing naar een standaardtabel 

   - als omschrijving van de toetsingsvoorwaarden (bijvoorbeeld bij aantallen van uren) 

7. _Attributen_ (alleen van toepassing bij klassen) De attributen waaruit de klasse maximaal is opgebouwd. 

8. _Structuur_ (alleen van toepassing bij attributen) De standaardstructuur die van toepassing is op het attribuut. Voor een samengesteld attribuut geeft de standaardstructuur de condities aan die gelden voor het gebruik van de samenstellende delen van het samengestelde attribuut. Voor enkelvoudige attributen beschrijft de standaardstructuur de condities die gelden voor het waardebereik. 

9. _Opmerkingen_ In deze rubriek staan de opmerkingen die in de andere rubrieken op generlei wijze zijn onder te brengen. 

## **4.  CONCEPTUEEL GEGEVENSMODEL** 

In dit hoofdstuk wordt het conceptueel gegevensmodel gepresenteerd. Het conceptueel gegevensmodel is voor de duidelijkheid onderverdeeld in een tiental deelmodellen: één voor elke van de acht hieronder genoemde gegevensclusters, een voor het adres en een voor de algemene procesgegevens. Per deelmodel wordt een globale beschrijving gegeven. 

## **4.1 Verklaring systematiek** 

De meeste deelmodellen gaan uit van de cliënt, de klasse CLIENT SUWI met het burgerservicenummer als sleutelgegeven. Met betrekking tot deze cliënt worden gegevens weergegeven. Deze gegevens zijn gegroepeerd in _klassen_ , weergegeven door middel van een rechthoek. 

Een _relatie_ in het model is aangegeven als een ononderbroken lijn. 

De _cardinaliteit_ van een relatie wordt als volgt aangegeven: 

- een n-kant van een relatie wordt aangegeven door het teken * bij de relatielijn aan de kant van de klasse die vaker kan voorkomen; 

- een 1-kant van een relatie is te herkennen aan het cijfer 1 bij de relatielijn aan de kant van de klasse die verplicht is. 

_Optionaliteit_ van een relatie wordt in het diagram aangegeven door middel van het cijfer 0 bij de relatielijn. Het cijfer 0 staat aangegeven aan de kant van de klasse die in de relatie optioneel is. Is een relatie niet optioneel, dan wordt dat aangegeven door het cijfer 1 als begin (1 of 1..*) in de relatielijn aan de kant van de klasse die verplicht is. 

Het onderscheid tussen _super- en subklassen_ wordt aangegeven door middel van een overervingsymbool (een pijl richting de superklasse). Een subklasse is een afgeleide vorm van een meer algemene superklasse. Een Postbusadres is bijvoorbeeld een subklasse van het type Adres Nederland. Het Postbusadres kan alle attributen van Adres Nederland overerven, en heeft daarbij nog eigen attributen. Een subklasse kan op haar beurt weer superklasse van andere subklassen zijn. 

## **4.2 Beschrijving SUWI-Gegevensmodel** 

Binnen het SUWI-Gegevensmodel worden onder andere de volgende clusters onderscheiden. 

- **Stamgegevens** - de gegevens die de cliënt identificeren en objectief beschrijven. 

- **Arbeidsmarktkwalificaties** - de gegevens van een cliënt betreffende de positie op de arbeidsmarkt. 

- **Arbeidsgegevens** - huidige en historische gegevens betreffende arbeid. 

- **Uitkeringsgegevens** - de gegevens die de aanvraag van de uitkering, de uitkeringsverhouding en de grondslag van de uitkering betreffen. 

- **Arbeidstoeleidingsgegevens** - de gegevens met betrekking tot arbeidstoeleiding, inclusief de fasering en het trajectplan. 

- **Ontsluiting gegevens uit externe bronnen** - de gegevens die afkomstig zijn van de de Rijksdienst voor het Wegverkeer (RDW), het Kadaster, de Basisregistratie Personen (BRP), de Dienst Uitvoering Onderwijs (DUO), de Belastingdienst en het Handelsregister (HR). 

- **Verbeteren Uitwisseling Matchingsgegevens (VUM)** - de gegevens die worden gebruikt bij VUM. 

- **Instrumentengidsen Dennis & Eva** - de gegevens die worden gebruikt bij de instrumentengidsen Dennis & Eva. 

- **De basis adresmodellering** , die ten grondslag ligt aan alle adressen in het SUWIGegevensmodel. 

- **Algemene procesgegevens** . 

Het SUWI-Gegevensmodel wordt in het navolgende per cluster beschreven. 

## **4.3 Conceptueel gegevensdeelmodel Stamgegevens** 

De gegevenscategorie Stamgegevens bevat gegevens die de cliënt identificeren en objectief beschrijven. 

De identiteit van de cliënt wordt weergegeven in gegevens als naam, burgerservicenummer, geboortedatum en nationaliteit. Indien de cliënt niet over de Nederlandse nationaliteit beschikt worden ook gegevens vastgelegd over de gronden op basis waarvan de cliënt in Nederland mag verblijven en in aanmerking komt voor bemiddeling naar arbeid (vreemdelingendocument). 

Daarnaast worden van een cliënt de adresgegevens vastgelegd. Dit kan het adres volgens de Basisregistratie Personen (BRP) zijn, het zogenaamde ‘domicilieadres’, maar kan ook een hiervan afwijkend adres zijn, het ‘feitelijke adres’ of het ‘feitelijke adres buitenland’. Met behulp van het feitelijke adres kan het (tijdelijke) verblijfadres van de cliënt worden vastgelegd. 

Indien van toepassing worden gegevens over de leefsituatie van de cliënt vastgelegd: burgerlijke staat, gegevens over de eventuele (ex-)partner(s) en kind(eren) en over het huishouden waar de cliënt deel van uitmaakt. 

In de praktijk is van de hier genoemde klassen die rond een cliënt zijn vastgelegd, in ieder geval altijd het adres gevuld. De overige klassen zijn alleen gevuld indien dat van toepassing is, sommige alleen binnen een bepaalde kolom. 

**==> picture [452 x 675] intentionally omitted <==**

**----- Start of picture text -----**<br>
:0,,%I)05;%5G-%4;,%I<br>!"#$%FGG()%* PQQJ S%-G%9-$624;,%I2#.-G%5945; PQQJ !"#$%FGG()%*<br>:1-$. ,$-.II%<br>PQQJ >08-F-9-%24;,%I PQQJ<br>!+GG,-#..GI00,G*<br>PQQJ S%-G%9-$624;,%I PQQJ 12 "8IFB,-$=-572.-G7%#,%-;%2,%FBGI=0,8<br>PQQJ PQQJ<br>:0,,%I)05;%5G-%4;,%I2#.-G%5945;<br>PQQJ PQQJ<br>!"#$%FGG()%* !"#$%FGG()%*<br>C2&77-"#?K',$-.II% (&71#$6#%2%8#$-#%9<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 +45;.-;-57254487%#,.-6 12 3%;,472445=.99%5;%2#%.,I2IG.;-%<-545F-%,-57<br>12 +D5.88%, 12 3%;,472445=.99%5;%2G0%947%2GH"N2I"JO<br>12 3.,7%,I%,=-F%5.88%, 12 3%;,472#4I-I#%.,I2IG.;-%<-545F-%,-57<br>12 :0;%23@AD7%7%=%5I27%B%-8 12 3%;,472#4I-IG0%947%2GH"N2I"JO<br>12 :0;%27%#00,G%7%8%%5G% 12 :0;%2IG4G.I2%%5D0.;%,G0%I9472IG.;-%<-545F-%,-57<br>12 :0;%2A?I+D7%7%=%5I27%B%-8 J PQQJ 12 :0;%2G0%6%55-572#4I-I#%.,I2IG.;-%<-545F-%,-57<br>12 O%#00,G%;4G.8 12 >4G.82445=4572G0%6%55-57I)%,-0;%2IG.;-%<-545F-%,-57<br>12 O%#00,G%945; 12 >4G.82%-5;%2IG.;-%<-545F-%,-57<br>12 O%#00,G%)944GI 12 >4G.82%-5;%2G0%6%55-57I)%,-0;%2IG.;-%<-545F-%,-57<br>12 O%I94FBG 12 ?5;-F4G-%2445=.99%5;%2#%.,I2IG.;-%<-545F-%,-57<br>12 ?;%5G-<-F4G-%5.88%,2A?I+ 12 ?5;-F4G-%2,%FBG20)2IG.;-%<-545F-%,-57<br>12 ?5;-F4G-%2IG4,G6L49-<-F4G-%2=097%5I2>F" 12 ?5;-F4G-%2IG.;-%<-545F-%,-57<br>12 "8IFB,-$=-572IG4G.I2M4G..,9-$62A%,I005 12 ?5;-F4G-%2G0%6%55-572GH"N2I"JO<br>12 N-75-<-F45G2;%%92=452;%24FBG%,5448<br>12 ID5.88%,<br>12 I00,548%5<br>12 I00,=0%7I%9<br>12 ?5;-F4G-%2B45;9-FBG-57<br>12 I00,9%GG%,I<br>PQQJ<br>!"#$%FGG()%*<br>(8D$%1#%9'#%"#8D&#%9$%;"#8D&<br>!+GG,-#..GI00,G*<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* 12 >4G.82L44,IFB.L-572IFB%5;-572-59-FBG-57%5)9-FBG<br>0#%1 ,2-&%$- PQQJ J !"#$%&'()*+ PQQJ PQQJ<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 ?5;-F4G-%26-5;%,#-$I947 PQQR J 12 3456,%6%5-575.88%, !"#$%FGG()%*<br>12 3.,7%,9-$6%2IG44G (&2%122-1'&$"$6II%%755$-<br>12 :0;%2945;2;0%97,0%)<br>PQQR J 12 :0;%29%%<=0,8 !+GG,-#..GI00,G*<br>J 121212 >4G.820=%,9-$;%5?5;-F4G-%20=%,9-$;%5+<5%8%,I-5;-F4G-%23@A H%9%<0055.88%, F9-%5G 121212 :0;%2G()%2G%9%<0055.88%,?5;-F4G-%27%B%-82G%9%<0055.88%,?5;-F4G-%2=00,6%.,2G%9%<0055.88%,<br>PQQJ PQQR 12 H%9%<0052945;5.88%,<br>12 H%9%<0055.88%,<br>PQQJ<br>!"#$%FGG()%*<br>(;$8#6#$K$'9$9$=$%.'0#%1$-L#?."29 CD84-924;,%I2F9-%5G !"#$%FGG()%*<br>(&2%122-1'3452#"'21-$.<br>!+GG,-#..GI00,G* J PQQR<br>12 :0;%2945;2=%,#9-$<26-5; J J J !+GG,-#..GI00,G*<br>12 :0;%2L005I-G.4G-%26-5; 12 CD84-924;,%I<br>12 ?5;-F4G-%2=00,6%.,2%D84-924;,%I<br>12 ?5;-F4G-%2NFG?2%D84-924;,%I<br>PQQJ PQQJ PQQR PQQJ<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>@$-L"#?6.&#&$" A$9#&#52&#$L$B#?. C2&#I%2"#&$#& @-$$51$"#%9$%1I875$%&<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 :0;%2=%,#9-$<IG-G%9 12 :0;%2I00,G29%7-G-84G-%#%L-$I 12 :0;%2#-$N05;%,2M%;%,945;%,IFB4) 12 :0;%2I00,G2=,%%8;%9-57%5;0F.8%5G<br>12 >4G.82445=4572=%,#9-$<IG-G%9 12 >4G.82%-5;%27%9;-7B%-;29%7-G-84G-%#%L-$I 12 :0;%254G-0549-G%-G 12 >4G.82%-5;%27%9;-7B%-;2=,%%8;%9-57%5;0F.8%5G<br>12 >4G.82%-5;%2=%,#9-$<IG-G%9 12 M.88%,29%7-G-84G-%#%L-$I 12 :0;%2,%;%52=%,6,-$7-572M%;%,945;I%254G-0549-G%-G 12 ?5;-F4G-%24,#%-;2G0%7%IG445<br>12 :0;%2,%;%52=%,9-%I2M%;%,945;I%254G-0549-G%-G 12 M.88%,2=,%%8;%9-57%5;0F.8%5G<br>12 >4G.82445=457254G-0549-G%-G<br>12 >4G.82%-5;%254G-0549-G%-G<br>**----- End of picture text -----**<br>


**Figuur 1. Stamgegevens** 

## **4.4 Conceptueel gegevensdeelmodel Arbeidsmarktkwalificaties** 

De gegevenscategorie Arbeidsmarktkwalificaties bevat gegevens die aangeven hoe de cliënt is toegerust voor de arbeidsmarkt. 

Door middel van de klasse ‘arbeidsmarktkwalificaties’ worden zaken vastgelegd die betrekking hebben op de vaardigheden van de cliënt die nodig zijn om in het maatschappelijke leven goed te kunnen functioneren. Bijvoorbeeld de mate van mondelinge en schriftelijke taalbeheersing van het Nederlands. 

Er kunnen gegevens opgenomen zijn over opleidingen en cursussen die de cliënt gevolgd heeft of nog volgt. Hieronder vallen gegevens zoals opleidingsnaam, duur van de opleiding en of de opleiding succesvol is afgerond. 

Daarnaast kunnen gegevens over de werkervaring van de cliënt beschikbaar zijn, zoals de uitgeoefende beroepen en het aantal jaren ervaring daarin. 

In een aparte klasse worden gegevens over het eventuele rijbewijs van de cliënt geregistreerd. 

De genoemde klassen die betrekking hebben op de cliënt zijn alleen vastgelegd indien ze van toepassing zijn en sommige alleen binnen een bepaalde kolom. 

**==> picture [452 x 651] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>C3&DD-"#A7G,$-.II%<br>!+GG,-#..GI00,G*<br>12 +45;.-;-57254487%#,.-6<br>12 +N5.88%, !"#$%&GG()%*<br>12 3.,7%,I%,=-&%5.88%, !"#$%&G()*+<br>12 :0;%23@AN7%7%=%5I27%B%-8<br>!"#$%&GG()%* 12 :0;%27%#00,G%7%8%%5G% !+GG,-#..GI00,G*<br>,$-.II% 12 :0;%2A?I+N7%7%=%5I27%B%-8 12 3456,%6%5-575.88%,<br>12 J%#00,G%;4G.8<br>12 3.,7%,9-$6%2IG44G<br>12 J%#00,G%945;<br>!+GG,-#..GI00,G* 12 :0;%2945;2;0%97,0%)<br>12 "8I&B,-$=-572.-G7%#,%-;%2,%&BGI=0,8 12 J%#00,G%)944GI 12 :0;%29%%<=0,8<br>12 J%I94&BG<br>12 L4G.820=%,9-$;%5<br>12 ?;%5G-<-&4G-%5.88%,2A?I+<br>12 ?5;-&4G-%20=%,9-$;%5<br>12 ?5;-&4G-%2IG4,G6F49-<-&4G-%2=097%5I2LO" 12 +<5%8%,I-5;-&4G-%23@A<br>12 "8I&B,-$=-572IG4G.I2H4G..,9-$62A%,I005<br>12 L-75-<-&45G2;%%92=452;%24&BG%,5448<br>12 IN5.88%,<br>MNNP MNNP<br>12 I00,548%5<br>P<br>12 I00,=0%7I%9<br>12 ?5;-&4G-%2B45;9-&BG-57<br>12 I00,9%GG%,I<br>MNNO<br>PNNO<br>!"#$%&GG()%*<br>!"#$%&GG()%* L$5-3=.:I6<$&$%&#$<br>012G-$"3&#$<br>!+GG,-#..GI00,G*<br>!+GG,-#..GI00,G* 12 :0;%27%;,47I&08)%G%5G-%<br>12 L4G.82445=4572+CDN,%94G-% 12 L4G.82%-5;%2=4IG7%IG%9;%27%;,47I&08)%G%5G-%<br>12 L4G.82%-5;%2+CDN,%94G-% 12 "8I&B,-$=-5727%;,47I&08)%G%5G-%<br>12 C0%9-&BG-5727%;,47I&08)%G%5G-%<br>P<br>MNNO<br>MNNP<br>!"#$%&GG()%* !"#$%&GG()%*<br>;<"$#5#%= MNNO 0-4$#5.63-7&783"#9#:3&#$. MNNP !"#$%&GG()%* @#A4$8#A.<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>!+GG,-#..GI00,G*<br>1212 +45G492$4,%52I.&&%I=0924<7%,05;+45G492.,%520)9%-;-57 MNNO P 1212 :0;%2G449#%B%%,I-572805;%9-57:0;%2G449#%B%%,I-572I&B,-<G%9-$6 P MNNO 12 :0;%2I00,G2,-$#%F-$I<br>12 :0;%29%%,F%728#0<br>12 :0;%25-=%4.20)9%-;-57<br>12 :0;%2IG4G.I20)9%-;-57<br>12 :0;%2G-$;I#%I94720)9%-;-57 P<br>12 L4G.82445=4572=097%520)9%-;-57<br>12 L4G.82;-)9084 MNNO<br>12 L4G.82%-5;%2=097%520)9%-;-57<br>12 ?5;-&4G-%2#.-G%5945;I%20)9%-;-57 !"#$%&GG()%*<br>12 ?5;-&4G-%2;-)9084 *$-7$-?3-#%= !"#$%&GG()%*<br>12 C0%9-&BG-5720)9%-;-57 B$-I$<<br>!+GG,-#..GI00,G* MNNO P<br>12 +45G492$4,%52F%,6G4482-52#%,0%)<br>12 C0%9-&BG-572#%,0%)<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>;<"$#5#%=.%336GI%=$:I5$$-5 ;<"$#5#%=.%336G=$:I5$$-5 B$-I$<.%336GI%=$:I5$$-5 B$-I$<.%336G=$:I5$$-5<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 H44820)9%-;-572057%&0;%%,; 12 :0;%20)9%-;-57I5448 12 H4482#%,0%)2057%&0;%%,; 12 :0;%2#%,0%)I5448<br>12 ?5;-&4G-%20)9%-;-57I544824&G-%< 12 ?5;-&4G-%2#%,0%)I544824&G-%<<br>12 "8I&B,-$=-5720)9%-;-57I5448 12 "8I&B,-$=-572#%,0%)I5448<br>P MNNO P MNNO<br>**----- End of picture text -----**<br>


**Figuur 2. Arbeidsmarktkwalificaties** 

## **4.5 Conceptueel gegevensdeelmodel Arbeidsgegevens** 

De gegevenscategorie Arbeidsgegevens omvat historische en actuele gegevens over de werkzaamheden die de cliënt binnen en buiten één of meer arbeidsverhoudingen heeft verricht. 

Indien er sprake is van een arbeidsverhouding worden ook gegevens vastgelegd over de inkomsten uit deze arbeidsverhouding en de contactgegevens van de registrerende instantie. Sectorindeling vindt plaats op grond van de Werkloosheidswet (WW). Om redenen van compatibiliteit voor bestaande systemen zijn in het conceptueel gegevensdeelmodel nog aanwezig: zowel de oorspronkelijke indeling op basis van bedrijfsverenigingen (BV), als de latere indeling op basis van de sector beroepsen bedrijfsleven. 

Ook hier geldt dat de klassen alleen gevuld zijn indien ze van toepassing zijn op de cliënt en vaak alleen binnen een bepaalde kolom. 

**==> picture [452 x 479] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$$%&'()*+,%-../<br>!"#$%FGG()%*<br>!"#$%&'()*+<br>!"#$%FGG()%*<br>,--.'-.I$#012$."$0$% !+GGH-#..GI00HG*<br>12 3456H%6%5-575.88%H<br>!+GGH-#..GI00HG* 12 3.H7%H9-$6%2IG44G<br>12 +45G492BCD;47%524H#%-;I=%H9%;%5 12 J0;%2945;2;0%97H0%)<br>12 +45G492=%H9005;%2.H%524H#%-;I=%H9%;%5 12 J0;%29%%<=0H8<br>12 ?5;-F4G-%2N49<$44H2FF TUUV S 12 >4G.820=%H9-$;%5<br>12 ?5;-F4G-%2845G%9G0H7<0H<4-G 12 ?5;-F4G-%20=%H9-$;%5<br>12 ?5;-F4G-%2G0H7<0H<4-G 12 +<5%8%HI-5;-F4G-%23@A<br>12 H44H2BCD;47%524H#%-;I=%H9%;%5<br>12 A%HF%5G47%2$44H24H#%-;I=%H9%;%5<br>S<br>!"#$%FGG()%* !"#$%FGG()%*<br>C5"5D'()*+ =$0.#;K12$.$%#7#%7 TUUV<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !"#$%FGG()%*<br>12 J0;%2609082BJF? 12 3CD5.88%H 3.I$#012$.4560#%7 !"#$%FGG()%*<br>12 I4482609082BJF? TUUV 12 I44823C S TUUV 3.I$#019$.#50$<br>12 I4482609082BJF?2Q=%H60HGR !+GGH-#..GI00HG*<br>12 >4G.82445=45724H#%-;I=%HN0.;-57 !+GGH-#..GI00HG*<br>S 12 >4G.82%-5;%24H#%-;I=%HN0.;-57 12 >4G.82445=45724H#%-;I)%H-0;%<br>TUUV !"#$%FGG()%* S SUUV 12 >4G.82%-5;%24H#%-;I)%H-0;%<br>($8&5.'I$.5$91J'$%'I$0.#;K1"$2$% 12 L%8-;;%9;2445G492M%H6.H%52)%H2M%%6<br>!"#$%FGG()%* 12 ?5;-F4G-%2=%H)9-FNG2=%HG%6%H;2NOF<br>L-.&#;'()*+ TUUS !+GGH-#..GI00HG* S TUUV<br>12 J0;%2I%FG0H<br>!+GGH-#..GI00HG* S TUUV 12 I4482I%FG0H<br>TUUS 12 J0;%2)4HG-$2BJF? SUUV TUUV S<br>12 I4482)4HG-$2BJF?<br>SUUV<br>S<br>!"#$%FGG()%*<br>TUUV !"#$%FGG()%* B55%9$.#50$<br>30.$1<br>!"#$%FGG()%*<br>!+GGH-#..GI00HG*<br>?$1&#7#%7'()*+<br>12 3%;H472#H.G090052BC<br>!+GGH-#..GI00HG* TUUS TUUS 12 J0;%2G0%7%)4IG%29005#%94IG-57G4#%9<br>12 J0;%2=%IG-7-572BJF? TUUS S 12 >4G.82445=45729005)%H-0;%<br>12 I4482=%IG-7-572BJF? 3%G0%64;H%I2N00<;=%IG-7-57 1212 >4G.82%-5;%29005)%H-0;%?5;-F4G-%29005N%<<-57I60HG-572G0%7%)4IG<br>S J0HH%I)05;%5G-%4;H%I2N00<;=%IG-7-57<br>TUUV S S S<br>!"#$%FGG()%* !"#$%FGG()%*<br>!5%&-8&9$.155%@J-K0$"#%7 S *$.A7$2$.<br>TUUV !+GGH-#..GI00HG* TUUV TUUS !+GGH-#..GI00HG*<br>12 I4482F05G4FG)%HI005OD4<;%9-57 12 +45I9.-G-57I5.88%H23C<br>12 P45;%9I544820H745-I4G-%<br>**----- End of picture text -----**<br>


**Figuur 3. Arbeidsgegevens** 

## **4.6 Conceptueel gegevensdeelmodel Arbeidsverleden** 

De gegevenscategorie Arbeidsverleden omvat gegevens over het arbeidsverleden van de cliënt. 

Vanaf 1 januari 2005 is de wet Feitelijk Arbeidsverleden van kracht. In deze wet is geregeld dat voor de bepaling van de duur van een WW-uitkering wordt uitgegaan van het feitelijke arbeidsverleden van de cliënt vanaf het kalenderjaar 1998. 

Indien van toepassing worden gegevens over arbeidsverleden, inkomstenverhouding, arbeidsverhouding en werkgever vastgelegd. 

**==> picture [452 x 534] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%*<br>233-'3-.$#I01$-"$I$%<br>!"#$%&''()%*<br>,-.$#I01$-"$I$%<br>!+''H-#..'I00H'*<br>12 +45'492DNF;47%524H#%-;I=%H9%;%5<br>!+''H-#..'I00H'*<br>12 +45'492=%H9005;%2.H%524H#%-;I=%H9%;%5<br>12 +45'492$44H2<%-'%9-$624H#%-;I=%H9%;%5 Q NOOP 12 ?5;-&4'-%2G49<$44H2HH<br>12 +45'492$44H2<-&'-%<24H#%-;I=%H9%;%5<br>12 ?5;-&4'-%2845'%9B0H7<0H<4-'<br>12 ?5;-&4'-%254;%H205;%HB0%624H#%-;I=%H9%;%5<br>12 ?5;-&4'-%2B0H7<0H<4-'<br>12 ?5;-&4'-%2)%H-0;%524H#%-;I=%H9%;%527%C%5I'<br>12 I44H2DNF;47%524H#%-;I=%H9%;%5<br>NOOQ 12 A%H&%5'47%2$44H24H#%-;I=%H9%;%5 Q<br>NOOP<br>Q Q<br>!"#$$%&'()*+,%-../<br>!"#$%&''()%* !"#$%&''()%*<br>!"#$%&'()*+ +%4560&$%1$-758I#%9<br>!+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 3456H%6%5-575.88%H 12 +45;.-;-572-5608I'%5=%HG0.;-572C%H67%=%H<br>12 3.H7%H9-$6%2I'44' 12 J0;%2H%;%52%-5;%24H#%-;I=%HG0.;-57<br>12 J0;%2945;2;0%97H0%) Q NOOP 12 J0;%2H%;%52%-5;%2-5608I'%5=%HG0.;-572<9%JC%H6%H<br>12 J0;%29%%<=0H8 12 L4'.82445=4572-5608I'%5=%HG0.;-57<br>12 L4'.820=%H9-$;%5 12 L4'.82%-5;%2-5608I'%5=%HG0.;-57 !"#$%&''()%*<br>12 ?5;-&4'-%20=%H9-$;%5 12 A%HI05%%9I5.88%H NOOP J$-#5I$'3-.$#I01$-"$I$%<br>12 +<5%8%HI-5;-&4'-%23@A 12 N0975.88%H2-5608I'%5=%HG0.;-57<br>!+''H-#..'I00H'*<br>QOOP 12 +45'492DNF;47%52)%H-0;%24H#%-;I=%H9%;%5<br>12 +45'492=%H9005;%2.H%52)%H-0;%24H#%-;I=%H9%;%5<br>Q 12 J0;%2#4I-I24H#%-;I=%H9%;%5<br>12 L4'.82445=4572)%H-0;%24H#%-;I=%H9%;%5<br>!"#$%&''()%* 12 L4'.82%-5;%2)%H-0;%24H#%-;I=%H9%;%5<br>,I6#%#0&-3&#$1$'$$%7$#I 12 N0975.88%H2)%H-0;%24H#%-;I=%H9%;%5<br>NOOQ NOOP<br>Q !+''H-#..'I00H'* NOOP<br>12 L4'.82445=45724;8-5-I'H4'-%=%2%%5G%-;<br>12 L4'.82%-5;%24;8-5-I'H4'-%=%2%%5G%-;<br>12 ?5;-&4'-%2#90664;%24;8-5-I'H4'-%=%2%%5G%-;<br>12 ?5;-&4'-%254;%H205;%HB0%624H#%-;I=%H9%;%57%7%=%5I24;8-5-I'H4'-%=%2%%5G%-;<br>12 O005G%<<-57%55.88%H<br>12 L44824;8-5-I'H4'-%=%2%%5G%-;<br>12 +45I9.-'-57I5.88%H23N<br>NOOP<br>!"#$%&''()%*<br>!"#$%&''()%*<br>*$-49$1$-<br>,-.$#I01$-758I#%9<br>NOOQ<br>!+''H-#..'I00H'*<br>!+''H-#..'I00H'* QOOP Q 12 +45I9.-'-57I5.88%H23N<br>12 L4'.82445=45724H#%-;I=%HG0.;-57<br>12 M45;%9I544820H745-I4'-%<br>12 L4'.82%-5;%24H#%-;I=%HG0.;-57<br>**----- End of picture text -----**<br>


**Figuur 4. Arbeidsverleden** 

## **4.7 Conceptueel gegevensdeelmodel Uitkeringsgegevens** 

De gegevenscategorie Uitkeringsgegevens omvat de gegevens over historische en actuele gegevens betreffende één of meer uitkeringen van de cliënt. 

Van een uitkering kan zijn vastgelegd op grond van welke wet zij is toegekend en wat het uitkeringsbedrag is (inkomsten uitkering). Ook gegevens over de aanvraag van de uitkering en eventuele maatregelen die van toepassing zijn op de uitkering kunnen worden vastgelegd. 

Ten behoeve van het UWV is een bruto uitkeringsbedrag opgenomen en voor de gemeentelijke kolom (GSD) is een netto uitkeringsbedrag opgenomen. 

Zowel van de lopende, historische of aangevraagde uitkering kan worden vastgelegd wie de (aanvraag van de) uitkering in behandeling heeft of heeft gehad (contactpersoon/-afdeling en bovenliggende klassen). Daarnaast kan er nog een aantal specifieke gegevens zijn vastgelegd: gegevens over arbeidsongeschiktheid en werkloosheid. 

Alleen de van toepassing zijnde klassen zijn gevuld, en alleen bij betrokken kolommen. De specifieke gegevensset voor een aanvraag van de bijstandsuitkering op basis van de Participatiewet is vanwege de omvang geplaatst in een apart gegevensdeelmodel, dat hierna is opgenomen. 

Dit model is uitgebreid met specifieke uitkeringsgegevens van de gemeentelijke kolom, de gegevens met betrekking tot Bezwaar en Beroep en specifieke gegevens in het kader van de gegevensuitwisseling met de SVB. 

**==> picture [665 x 424] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%F''()%* !"#$$%&'()*+,%-../<br>!"#$%&G($G)*%+,*$%&-.I%$0, !"#$%F''()%*<br>.I%$0,-=L9?<br>!+'',-#..'I00,'*<br>12 304%25,#%-4I067%IF8-9'8%-4I9:5II%27%IF85'2)%,2%-64%2;5F8''-$42<+" !+'',-#..'I00,'*<br>12 304%25,#%-4I067%IF8-9'8%-4I9:5II% VPPX Q 12 C569,%9%6-676.==%,<br>12 304%2F5'%70,-%2=%4-IF8%2#%)%,9-67%6 12 C.,7%,:-$9%2I'55'<br>12 L5'.=2556?5672+"@9:5II% 12 304%2:564240%:7,0%)<br>12 L5'.=2%%,I'%2+"@457 12 304%2:%%F?0,= !"#$%F''()%*<br>12 L5'.=20?%,:-$4%6 9$"+I22G*$%&-.I%$0,<br>12 G64-F5'-%20?%,:-$4%6<br>12 +F6%=%,I-64-F5'-%2CBH !+'',-#..'I00,'* !"#$%F''()%*<br>!"#$%F''()%* Q VPPQ 12 L5'.=2%%,I'%2;%,9:00I8%-4I457 !308"33(-99<br>1"20&GI3(-3"#$%&G#$4$"+,*$%& 12 G64-F5'-%2+"2?00,5F7556425562%%,I'%2;%,9:00I8%-4I457<br>12 "=IF8,-$?-672,%4%62;%,9:00I8%-4 !+'',-#..'I00,'*<br>12!+'',-#..'I00,'*304%27,064I:5725,#%-4I#%)%,9'8%-4 VPPX Q 1212 304%2),%)%6I-0%6304%2,%4%62556?,5572<<<br>12 L5'.=2556?56727,064I:5725,#%-4I#%)%,9'8%-4 12 L5'.=2Q?%,=0%4%:-$9%R2556?5672),%)%6I-0%6<br>12 L5'.=2%-64%27,064I:5725,#%-4I#%)%,9'8%-4 12 L5'.=2?%,=0%4%:-$9%2%%,I'%2;%,9:00I8%-4I457<br>12 G64-F5'-%2556?.::-672+HH27%;%6I'<br>12 G64-F5'-%2556?.::-672+PI27%;%6I'<br>!"#$%F''()%* 12 G64-F5'-%2556?.::-672+P<27%;%6I'<br>567-"$(%G,"3,%$-82I($0G-9:;K! !"#$%F''()%* 12 G64-F5'-%2556?.::-672JO<+J@S27%;%6I'<br>12!+'',-#..'I00,'*L5'.=2%-64%2ALB2,%7-I',5'-%2?0:7%6I2<CDN+ VPPQ Q Q Q Q VPPX 1212!+'',-#..'I00,'*L5'.=2556?56725,#%-4I?%,80.4-67L5'.=2%-64%25,#%-4I?%,80.4-67 !"#$%&G8$"*2@&%0( VPPQ VPPQ 1212121212 G64-F5'-%2#%M;55,2;%,97%?%,I?%,9:5,-67G64-F5'-%2807%,2:0062#-$2564%,%2;%,97%?%,G64-F5'-%2?00,IF80'27%;%6I'G64-F5'-%2;%,97%?%,I?%,9:5,-67206'?567%6I0%:-F8'-672#%M;55,2;%,97%?%,I?%,9:5,-67<br>VPPX<br>VPPX VPPX<br>VPPX Q VPPX !308"33(-@%,+$"%0( !"#$%F''()%*<br>L%,+$"%0(G8$"*2@&%0( !"#$%F''()%* =$),2"-#$"2$4GB-$0-#$&"%IMGI$8$0 !"#$%F''()%* 12!+'',-#..'I00,'*304%2I'5'.I2556?,5572.-'9%,-67<br>1212!+'',-#..'I00,'*L5'.=2%-64%2:0067%,%:5'%%,4%2.-'9%,-672<<L5'.=2%-64%2?%,?0:7.-'9%,-672<< =4$)%M%$+$-($($8$0G-99-@%,+$"%0( !"#$%F''()%* VPPQ Q 1212121212!+'',-#..'I00,'*+56'5:2;%,9.,%62)%,2;%%927,064I:572.-'9%,-67L5'.=2556?5672.-'9%,-67I?%,80.4-67L5'.=2%-64%2=5L-=5:%2.-'9%,-67I4..,L5'.=2%-64%2.-'9%,-67I?%,80.4-67"=IF8,-$?-672,%4%62%-64%2.-'9%,-67I?%,80.4-67 VPPXVPPX VPPX 1212!+'',-#..'I00,'*304%2I%F'0,T55=2I%F'0, VPPX 121212121212 L5'.=2556?,5572.-'9%,-67L5'.=2556?5672)%,-04%2556?,5572.-'9%,-67L5'.=2%-64%2)%,-04%2556?,5572.-'9%,-67G64-F5'-%20?%,-7%2.-'9%,-67%6"=IF8,-$?-672,%4%62'%2:5'%2556?,5572.-'9%,-67I0%:-F8'-672)%,-04%2556?,5572.-'9%,-67<br>VPPX VPPX Q VPPX<br>!"#$%F''()%* Q VPPX VPPX !"#$%F''()%*<br>:"@,2-@%,+$"%0(G#$&"3( VPPX Q =ABC$,<br>!+'',-#..'I00,'* !"#$%F''()%* Q Q !+'',-#..'I00,'*<br>12 L5'.=2556?5672#,.'02.-'9%,-67I#%4,57 L%,+$"%0(G4$"%2&$ 12 304%2JO@;%'<br>12 L5'.=2%-64%2#,.'02.-'9%,-67I#%4,57 !"#$%F''()%*<br>12 304%2=.6'%%68%-4 VPPX Q !+'',-#..'I00,'* Q .20,3),4$"G220LB3M&$I%0(<br>12 304%2.-'9%,-67I)%,-04% 12 L5'.=2556?5672.-'9%,-67I)%,-04%<br>12 <55,4%#%4,57 12 L5'.=2%-64%2.-'9%,-67I)%,-04% !+'',-#..'I00,'*<br>12 G64-F5'-%2?%,):-F8'2?%,M%9%,42ON< 12 T55=2F06'5F')%,I006U@5F4%:-67<br>Q Q VPPX VPPX<br>!"#$%F''()%*<br>N$,,2-@%,+$"%0(G#$&"3( VPPX VPPX VPPX Q VPPQ Q VPPQ Q<br>1212!+'',-#..'I00,'*304%2=.6'%%68%-4304%2.-'9%,-67I)%,-04% F33,"$($I-G#,-@%,+$"%0( !"#$%F''()%* :$&"%IMG8$"$0%(%0( !"#$%F''()%* !"#$%F''()%* J3",%I-=L9? H$G,%(%0(-=L9? !"#$%F''()%*<br>121212 L5'.=2556?56726%''02.-'9%,-67I#%4,57L5'.=2%-64%26%''02.-'9%,-67I#%4,57<55,4%2#%4,57 121212!+'',-#..'I00,'*L5'.=2556?5672=55',%7%:2=#'2.-'9%,-67L5'.=2%-64%2=55',%7%:2=#'2.-'9%,-67H%,F%6'57%290,'-672.-'9%,-67 1212!+'',-#..'I00,'*CP@6.==%,T55=2CP VPPX VPPQ 1212!+'',-#..'I00,'*304%2)5,'-$2JO<GT55=2)5,'-$2JO<G Q VPPX 1212!+'',-#..'I00,'*304%2?%I'-7-672JO<GT55=2?%I'-7-672JO<G<br>VPPX<br>Q<br>!"#$%F''()%* !"#$%F''()%* !"#$%F''()%*<br>7$&$0-G33,"$($I-G#,-@%,+$"%0(-L9H 7$&$0-G33,"$($I-G#,-#%IG,30&-@%,+$"%0( K2I2G-=L9?<br>!+'',-#..'I00,'* !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 304%2,%4%62=55',%7%:2=#'2.-'9%,-672O<P 12 304%2,%4%62=55',%7%:2=#'2#-$I'5642.-'9%,-67 12 304%290:0=2JO<G<br>12 T55=290:0=2JO<G<br>12 T55=290:0=2JO<G2Q?%,90,'R<br>**----- End of picture text -----**<br>


**Figuur 5. Uitkeringsgegevens** 

**==> picture [672 x 429] intentionally omitted <==**

**----- Start of picture text -----**<br>
5#-."%H"'3'D"%&"'( !"#$%FGG()%* !"#$%FGG()%* @%&)HH' O%7%4-48=0.9%H 53=.H123'$&%$%'"'( !"#$%FGG()%*<br>12121212121212121212121212!+GGH-#..GI00HG*G%9H382334K.55%49%2#%.HI2IG.9-%J-434F-%H-48G%9H382334K.55%49%2G0%538%2CP"N2H"QRG%9H382#3I-I#%.HI2IG.9-%J-434F-%H-48G%9H382#3I-IG0%538%2CP"N2H"QRD09%2IG3G.I2%%4F0.9%HG0%I5382IG.9-%J-434F-%H-48D09%2G0%7%44-482#3I-I#%.HI2IG.9-%J-434F-%H-48:3G.;2334K3482G0%7%44-48I)%H-09%2IG.9-%J-434F-%H-48:3G.;2%-49%2IG.9-%J-434F-%H-48:3G.;2%-49%2G0%7%44-48I)%H-09%2IG.9-%J-434F-%H-48?49-F3G-%2334K.55%49%2#%.HI2IG.9-%J-434F-%H-48?49-F3G-%2H%F=G20)2IG.9-%J-434F-%H-48?49-F3G-%2IG.9-%J-434F-%H-48?49-F3G-%2G0%7%44-482CP"N2H"QR 12!+GGH-#..GI00HG*?49-F3G-%27-49%H#-$I538!"#$%FGG()%* A"'. VPPQVPPX VPPQQ 1212121212121212121212121212121212121212!+GGH-#..GI00HG*!+GGH-#..GI00HG*";IF=H-$K-482.-G8%#H%-9%2H%F=GIK0H;+349.-9-482433;8%#H.-7+F4.;;%HG.H8%HI%HK-F%4.;;%HD09%2GOLF8%8%K%4I28%=%-;D09%28%#00HG%8%;%%4G%D09%2L?H+F8%8%K%4I28%=%-;S%#00HG%93G.;S%#00HG%5349S%#00HG%)533GIS%I53F=G?9%4G-J-F3G-%4.;;%H2L?H+?49-F3G-%2IG3HG7635-J-F3G-%2K058%4I2:T"";IF=H-$K-482IG3G.I2M3G..H5-$72L%HI004N-84-J-F34G29%%52K3429%23F=G%H433;HF4.;;%HH00H43;%4H00HK0%8I%5?49-F3G-%2=3495-F=G-48H00H5%GG%HI 03#--&="B$1@%&)HH' !"#$%FGG()%* Q VPPQVPPQQ D0HH%I)049%4G-%39H%IVPPQVPPXQQ :0;-F-5-%239H%IVPPX VPPX!"#$%FGG()%* @3&#'%& 1212VPPQ!+GGH-#..GI00HG*G%9H382I35902#347H%7%4-48:3G.;2H%7%4-483JIF=H-JGQ VPPQVPPQVPPQ VPPXVPPQ 12121212121212121212!+GGH-#..GI00HG*D09%28%;%%4G%2=.6%5-$7II5.-G-48N334833428%H%8-IGH%%H92)3HG4%HIF=3)D09%28%;%%4G%204G#-49-482=.6%5-$7N8%H%8-IGH%%H92)3HG4%HIF=3)D09%2H%9%4204G#-49-482=.6%5-$7N8%H%8-IGH%%H92)3HG4%HIF=3)D09%2I00HG2K%H#-4G%4-I:3G.;2=.6%5-$7II5.-G-48N334833428%H%8-IGH%%H92)3HG4%HIF=3):3G.;204G#-49-482=.6%5-$7N8%H%8-IGH%%H92)3HG4%HIF=3)O3492=.6%5-$7II5.-G-48N334833428%H%8-IGH%%H92)3HG4%HIF=3)O349204G#-49-482=.6%5-$7N8%H%8-IGH%%H92)3HG4%HIF=3)L533GI2=.6%5-$7II5.-G-48N334833428%H%8-IGH%%H92)3HG4%HIF=3)L533GI204G#-49-482=.6%5-$7N8%H%8-IGH%%H92)3HG4%HIF=3) ?-8%="B$C(%&%(")#&%%&.1I3&#'%&)D+3I !"#$%FGG()%* VPPQ 121212!+GGH-#..GI00HG*D09%2F5.IG%H2G-$@049%H%2G-$IG349:3G.;2#%G335#33HIG%55-482G-$@049%H%2G-$IG349";IF=H-$K-482I00HG270IG%42G-$@049%H%2G-$IG349 5I%D"H"%$%1(%(%*%')14"BIH'.%&%14"B)#3'. VPPX VPPX!"#$%FGG()%* VPPX<br>1212!+GGH-#..GI00HG*D09%2H%F=GIK0H;?4IF=H-$K-48I4.;;%H2U3;%H2K342U00)=349%5121212121212!+GGH-#..GI00HG*D09%2#-$@049%H2M%9%H5349%HIF=3)D09%243G-0435-G%-GD09%2H%9%42K%H7H-$8-482M%9%H5349I%243G-0435-G%-GD09%2H%9%42K%H5-%I2M%9%H5349I%243G-0435-G%-G:3G.;2334K348243G-0435-G%-G:3G.;2%-49%243G-0435-G%-G!"#$%FGG()%* J"(%'12%.&"BH !"#$%FGG()%* 03#"H'3="#%"# VPPQ Q 9%&$I33F+%.%'13'.%&)1.3'1"'3&2%".)*%&+H-."'( !"#$%FGG()%* VPPXVPPX Q 12121212121212!+GGH-#..GI00HG*G347H%7%4-484.;;%HG.H8%H5-$7%2IG33GD09%25349290%58H0%)D09%25%%JK0H;:3G.;20K%H5-$9%4?49-F3G-%20K%H5-$9%4+J4%;%HI-49-F3G-%2GOLQ !"#$%FGG()%* K="%'#15!9L VPPQQVPPQQQ VPPQ 121212!+GGH-#..GI00HG*D09%2K%IG-8-482NTC?D09%27050;2NTC?D09%2)3HG-$2NTC?VPPQ !"#$%FGG()%* 4&H' VPPX QQQ VPPX 1212!+GGH-#..GI00HG*D09%2I00HG20K%H-8%2-470;IG%4";IF=H-$K-4820K%H-8%2-470;IG%4 N*%&"(%1"'$HF)#%'1DHFIH'%'# !"#$%FGG()%* VPPX !"#$%FGG()%* OH&.%&"'( VPPX VPPXVPPX 12121212121212!+GGH-#..GI00HG*QD09%2IG3G.I2334KH3382.-G7%H-48:3G.;2334KH3382.-G7%H-48:3G.;2334K3482)%H-09%2334KH3382.-G7%H-48:3G.;2%-49%2)%H-09%2334KH3382.-G7%H-48?49-F3G-%20K%H-8%2.-G7%H-48%4";IF=H-$K-482H%9%42G%253G%2334KH3382.-G7%H-48P0%5-F=G-482)%H-09%2334KH3382.-G7%H-48VPPXVPPX :3'*&33(1-"#$%&"'( !"#$%FGG()%*VPPXVPPQ<br>Q VPPQ!"#$%FGG()%* :.&%) VPPQ QVPPQ D0HH%I)049%4G-%39H%I2=00J9K%IG-8-48G%@0%739H%I2=00J9K%IG-8-48VPPQ Q QQ 1212!+GGH-#..GI00HG*+34I5.-G-48I4.;;%H2GHI349%5I433;20H834-I3G-%!"#$%FGG()%* 9%&$(%*%& VPPX 12121212121212!+GGH-#..GI00HG*G%9H382334K3482K0H9%H-48G%9H382I35902K0H9%H-48D09%2H%9%42K0H9%H-48D09%2IG3G.I2K0H9%H-48:3G.;2#%I5.-G2K0H9%H-48:3G.;204=%HH0%)%5-$72K0H9%H-48?9%4G-J-F3G-%4.;;%H2K0H9%H-48<br>QQPPX VPPQ !"#$%FGG()%* ;HH'I%&"H.% VPPX<br>VPPQ Q Q Q Q VPPX 1212!+GGH-#..GI00HG*:3G.;2334K34823H#%-9IK%H=0.9-48:3G.;2%-49%23H#%-9IK%H=0.9-48 :&2%".)*%&+H-."'( !"#$%FGG()%* Q QPPX 1212121212!+GGH-#..GI00HG*G%9H382#H.G050042NHD09%2G0%8%)3IG%25004#%53IG-48G3#%5:3G.;2334K34825004)%H-09%:3G.;2%-49%25004)%H-09%?49-F3G-%25004=%JJ-48I70HG-482G0%8%)3IG<br>VPPX<br>!"#$%FGG()%*<br>4&-#H1-"#$%&"'()2%.&3( !"#$%FGG()%*<br>!+GGH-#..GI00HG* ?-")*%)#"'(<br>121212 :3G.;2334K3482#H.G02.-G7%H-48I#%9H38:3G.;2%-49%2#H.G02.-G7%H-48I#%9H38D09%2;.4G%%4=%-9 VPPQ 12!+GGH-#..GI00HG*D09%2H%53G-%2#%604%H2G0G2=.-IK%IG-48 VPPQ<br>1212 D09%2.-G7%H-48I)%H-09%C33H9%#%9H38 VPPX Q Q<br>1212121212!+GGH-#..GI00HG*D09%2;.4G%%4=%-9D09%2.-G7%H-48I)%H-09%:3G.;2334K34824%GG02.-G7%H-48I#%9H38:3G.;2%-49%24%GG02.-G7%H-48I#%9H38C33H9%2#%9H38 NI=%"."'()'33F1(%DH.%%&.0%##H1-"#$%&"'()2%.&3( !"#$%FGG()%*!"#$%FGG()%* VPPX Q 121212!+GGH-#..GI00HG*:3G.;2334K3482.-G7%H-48I)%H-09%:3G.;2%-49%2.-G7%H-48I)%H-09%?49-F3G-%2K%H)5-F=G2K%H@%7%H92ABC!"#$%FGG()%* NI=%"."'( Q !"#$%&"'()I%&"H.% !"#$%FGG()%* VPPX QPPX!"#$%FGG()%* :G;1&%=3#"% Q VPPX VPPXVPPXQ 1212121212!+GGH-#..GI00HG*+34G3526%H7.H%42)%H26%%728H049I5382.-G7%H-48:3G.;2334K3482.-G7%H-48IK%H=0.9-48:3G.;2%-49%2;3L-;35%2.-G7%H-48I9..H:3G.;2%-49%2.-G7%H-48IK%H=0.9-48";IF=H-$K-482H%9%42%-49%2.-G7%H-48IK%H=0.9-48 !"#$%&"'()*%&+H-."'( !"#$%FGG()%*VPPQQ VPPXVPPXVPPXVPPXVPPX Q 12!+GGH-#..GI00HG*D09%2NAF6%G!"#$%FGG()%* 5678%# Q VPPXQ 12!+GGH-#..GI00HG*M33;2F04G3FG)%HI004NF3J9%5-48Q KH'#3D#I%&)HH'C73H.%="'( VPPX !"#$%FGG()%*Q<br>121212!+GGH-#..GI00HG*D09%20)5%-9-48I433;?49-F3G-%20)5%-9-48I433;23FG-%J";IF=H-$K-4820)5%-9-48I433;Q NI=%"."'()'33F1H'(%DH.%%&. !"#$%FGG()%* VPPX 121212121212121212121212!+GGH-#..GI00HG*+34G352$3H%42I.FF%IK0523J8%H049+34G352.H%420)5%-9-48D09%25%%H6%82;#0D09%24-K%3.20)5%-9-48D09%2IG3G.I20)5%-9-48D09%2G-$9I#%I53820)5%-9-48:3G.;2334K3482K058%420)5%-9-48:3G.;29-)50;3:3G.;2%-49%2K058%420)5%-9-48?49-F3G-%2#.-G%45349I%20)5%-9-48?49-F3G-%29-)50;3P0%5-F=G-4820)5%-9-48 VPPX 1212!+GGH-#..GI00HG*:3G.;2334K3482+POFH%53G-%:3G.;2%-49%2+POFH%53G-%Q Q VPPQ 121212!+GGH-#..GI00HG*+34G352.H%42)%H26%%72#%IF=-7#33H2K00H23H#%-9:3G.;2334K3482#%IF=-7#33H2K00H23H#%-9:3G.;2%-49%2#%IF=-7#33H2K00H23H#%-9 4%)D+"$233&+%".1D="%'#1*HH&13&2%". !"#$%FGG()%*!"#$%FGG()%* VPPQ<br>!+GGH-#..GI00HG* O&"B)#%=="'(13&2%".)I="D+#<br>12 M33;20)5%-9-482048%F09%%H9 !+GGH-#..GI00HG*<br>VPPQ 1212121212 D09%2H%9%42%-49%2KH-$IG%55-4823H#%-9I)5-F=G2#-$IG349D09%2KH-$IG%55-4823H#%-9I)5-F=G2#-$IG349:3G.;2334K3482KH-$IG%55-4823H#%-9I)5-F=G:3G.;2%-49%2KH-$IG%55-4823H#%-9I)5-F=G?49-F3G-%2KH-$IG%55-4823H#%-9I)5-F=G<br>**----- End of picture text -----**<br>


## **Figuur 6. Aanvraag bijstandsuitkering** 

**==> picture [666 x 410] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$$%&'()*+,%-../ !"#$%F''()%* !"#$%F''()%*<br>!"#$%F''()%* H-#.I$.F#%0 C<%I2<<0G-#F1$2#%0<br>!"#$%FG()*+<br>!+'',-#..'I00,'* !+'',-#..'I00,'*<br>!+'',-#..'I00,'* 12 :0;%2,%94'-%2#%B05%,2'0'2C.-I=%I'-57 12 :0;%2I'4'.I2445=,4472.-'6%,-57<br>12 3456,%6%5-575.88%, Q NOOQ NOOQ Q 12 >4'.82445=,4472.-'6%,-57<br>12 3.,7%,9-$6%2I'44' 12 >4'.82445=4572)%,-0;%2445=,4472.-'6%,-57<br>12 :0;%2945;2;0%97,0%) 12 >4'.82%-5;%2)%,-0;%2445=,4472.-'6%,-57<br>1212 :0;%29%%<=0,8>4'.820=%,9-$;%5 NOOQ 1212 ?5;-F4'-%20=%,-7%2.-'6%,-57%5"8IFC,-$=-572,%;%52'%294'%2445=,4472.-'6%,-57<br>12 ?5;-F4'-%20=%,9-$;%5 Q NOOP 12 O0%9-FC'-572)%,-0;%2445=,4472.-'6%,-57<br>12 +<5%8%,I-5;-F4'-%23@A NOOP Q<br>!"#$%F''()%*<br>(6$7#8#$1$G0$0$I$%.G9#:;4%5$2$G9#:.F<%5<br>!"#$%F''()%*<br>(6$7#8#$1$G0$0$I$%.G@#:.F<%5G-#F1$2#%0 !+'',-#..'I00,'* NOOP<br>Q NOOP 12 :0;%2F9.I'%,23-$E05;%,%23-$I'45;<br>!+'',-#..'I00,'* 12 >4'.82#%'449#44,I'%99-5723-$E05;%,%23-$I'45; !"#$%F''()%*<br>12 +45'49260I'%5;%9%,I 12 "8IFC,-$=-572I00,'260I'%523-$E05;%,%23-$I'45; 9$."#..#%0G46G<<%I2<<0G-#F1$2#%0<br>12 :0;%24459%-;-572#%%-5;-7-572#-$I'45;2.-'6%,-57<br>12 :0;%2F94II-<-F4'-%23#E NOOP Q NOOP !+'',-#..'I00,'*<br>12 :0;%2#%I9-II-5720)2445=,4472.-'6%,-57<br>Q 12 :0;%2,%;%524<B-$E-572445=,4472.-'6%,-572LJM<br>12 >4'.82#%I9-II-5720)2445=,4472.-'6%,-57<br>12 >4'.82;47'%6%5-572#%I9-II-5720)2445=,4472.-'6%,-57<br>Q NOOP 12 >4'.82%-5;%2#%I9-I'%,8-$520)2445=,4472.-'6%,-57<br>!"#$%F''()%* !"#$%F''()%*<br>+%14A.F$%G#%I"4$5G46G@#:.F<%5G-#F1$2#%0 )#F1$2#%0.I$234-5#%0<br>!+'',-#..'I00,'* NOOP Q !+'',-#..'I00,'* Q Q<br>12 :0;%2I00,'20=%,-7%2-5608I'%5 12 +45'492B%,6.,%52)%,2B%%627,05;I9472.-'6%,-57<br>12 >4'.82445=4572.-'6%,-57I=%,C0.;-57 !"#$%F''()%* !"#$%F''()%*<br>12 >4'.82%-5;%284D-849%2.-'6%,-57I;.., (=>?$F Q NOOP H425$2#%0<br>!"#$%F''()%* 12 >4'.82%-5;%2.-'6%,-57I=%,C0.;-57<br>(6$7#8#$1$G0$0$I$%.GF$A#02<F#$?$F 12 "8IFC,-$=-572,%;%52%-5;%2.-'6%,-57I=%,C0.;-57 NOOP Q !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 :0;%2FGHB%' Q NOOP 12 3%;,472445=4572=0,;%,-57<br>!+'',-#..'I00,'* NOOP Q 12 3%;,472I49;02=0,;%,-57<br>12 :0;%2I00,'2,%8-7,4'-%=00,E-%5-57 12 :0;%2,%;%52=0,;%,-57<br>12 :0;%2I'4'.I2=0,;%,-57<br>Q 12 >4'.82#%I9.-'2=0,;%,-57<br>!"#$%F''()%* 12 >4'.8205C%,,0%)%9-$62=0,;%,-57<br>!"#$%F''()%* NOOP B$FF4G-#F1$2#%0.@$52<0 12 ?;%5'-<-F4'-%5.88%,2=0,;%,-57<br>+%14A.F$%G@#:.F<%5G-#F1$2#%0 !"#$%F''()%* !+'',-#..'I00,'* NOOQ<br>1212!+'',-#..'I00,'*3%;,472#%'449#44,27%I'%9;%2.-'6%,-573%;,472'0'4492-5608I'%52.-'6%,-57 NOOP NOOQ 121212!+'',-#..'I00,'*>4'.82445=4572.-'6%,-57I)%,-0;%>4'.82%-5;%2.-'6%,-57I)%,-0;%?5;-F4'-%2=%,)9-FC'2=%,E%6%,;2GIJ )#F1$2#%0.6$2#45$ Q NOOP 1212121212 :0;%28.5'%%5C%-;:0;%2.-'6%,-57I)%,-0;%>4'.82445=45725%''02.-'6%,-57I#%;,47>4'.82%-5;%25%''02.-'6%,-57I#%;,47J44,;%2#%;,47 !"#$%F''()%* I2<-5$ NOOQ<br>1212!+'',-#..'I00,'*:0;%2I00,'250,8#%;,47:0;%28.5'%%5C%-;!"#$%F''()%* B42A@$52<0 NOOP Q !+'',-#..'I00,'* 92-F4G-#F1$2#%0.@$52<0 !"#$%F''()%* 1212121212!+'',-#..'I00,'*:0;%2C007'%2#%I'..,9-$6%2#0%'%:0;%2,%F-;-=%'%,8-$5:0;%2I00,'2I45F'-%?5;-F4'-%2,%F-;-=%?5;-F4'-%2,0#..I'%2-5F4II02'0%7%)4I'<br>12 J44,;%2#%;,47 Q NOOP 12 >4'.82445=4572#,.'02.-'6%,-57I#%;,47 12 A4,6%'5.88%,2$.I'-'-%<br>12 >4'.82%-5;%2#,.'02.-'6%,-57I#%;,47<br>12 :0;%28.5'%%5C%-;<br>Q Q 12 :0;%2.-'6%,-57I)%,-0;%<br>!"#$%F''()%* 12 J44,;%#%;,47<br>(6$7#8#$1$G0$0$I$%.GCM*<br>1212!+'',-#..'I00,'*?5;-F4'-%2)4,'5%,'0%I9472+"JA%,F%5'47%2'0%7%6%5;%2+"J NOOP N<<F2$0$"GA@FG-#F1$2#%0 !"#$%F''()%*NOOP !"#$%F''()%* !"#$%F''()%*<br>F$5$%GA<<F2$0$"GA@FG@#:.F<%5G-#F1$2#%0 G$I4"0$%GA<<F2$0$"GA@FG@#:.F<%5G-#F1$2#%0<br>!+'',-#..'I00,'*<br>12 >4'.82445=4572844',%7%928#'2.-'6%,-57 !+'',-#..'I00,'* NOOP NOOQ !+'',-#..'I00,'*<br>12 >4'.82%-5;%2844',%7%928#'2.-'6%,-57 12 :0;%2,%;%52844',%7%928#'2#-$I'45;2.-'6%,-57 12 3%;,472=%,8-5;%,-572.-'6%,-5728#'2844',%7%9<br>12 A%,F%5'47%260,'-572.-'6%,-57<br>**----- End of picture text -----**<br>


**Figuur 7. Uitkeringsgegevens (vervolg)** 

**==> picture [667 x 419] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%F''()%* !"#$$%&'()*+,%-../ !"#$%F''()%*<br>,5%6-551'7#&4$-#%1 !"#$%F''()%* ,-.$#I01$023#4&3$#I'!"#$%&<br>!"#$%&'()*+<br>!+'',-#..'I00,'* QRRS T !+'',-#..'I00,'*<br>12 :0;%2I'4'.I2445=,4472.-'6%,-57 !+'',-#..'I00,'* 12 :0;%24,#%-;I057%IFB-6'B%-;I694II%27%IFB4'2)%,2%-5;%2C4FB''-$;2D+"<br>12 >4'.82445=,4472.-'6%,-57 12 3456,%6%5-575.88%, T QRRS 12 :0;%24,#%-;I057%IFB-6'B%-;I694II%<br>12 >4'.82445=4572)%,-0;%2445=,4472.-'6%,-57 12 3.,7%,9-$6%2I'44' 12 :0;%2F4'%70,-%28%;-IFB%2#%)%,6-57%5<br>12 >4'.82%-5;%2)%,-0;%2445=,4472.-'6%,-57 T 12 :0;%2945;2;0%97,0%) 12 >4'.82445=4572+"E694II%<br>12 ?5;-F4'-%20=%,-7%2.-'6%,-57%5 12 :0;%29%%<=0,8 12 >4'.82%%,I'%2+"E;47<br>12 "8IFB,-$=-572,%;%52'%294'%2445=,4472.-'6%,-57 12 >4'.820=%,9-$;%5<br>12 F0%9-FB'-572)%,-0;%2445=,4472.-'6%,-57 QRRS 12 ?5;-F4'-%20=%,9-$;%5<br>12 +<5%8%,I-5;-F4'-%23@A<br>!"#$%F''()%*<br>)#&4$-#%106$-3;7I#%1 !"#$%F''()%*<br>)#&4$-#%10=$-#;I$<br>!+'',-#..'I00,'*<br>,5%6-551'** !"#$%F''()%* T QRRS 1212 +45'492C%,6.,%52)%,2C%%627,05;I9472.-'6%,-57>4'.82445=4572.-'6%,-57I=%,B0.;-57 T QRRS 12!+'',-#..'I00,'*>4'.82445=4572.-'6%,-57I)%,-0;%<br>12 >4'.82%-5;%284I-849%2.-'6%,-57I;.., 12 >4'.82%-5;%2.-'6%,-57I)%,-0;%<br>!+'',-#..'I00,'* 12 >4'.82%-5;%2.-'6%,-57I=%,B0.;-57 12 ?5;-F4'-%2=%,)9-FB'2=%,O%6%,;2HPD<br>12 :0;%2),%)%5I-0%5 12 "8IFB,-$=-572,%;%52%-5;%2.-'6%,-57I=%,B0.;-57<br>12 :0;%2,%;%52445=,4472DD T<br>12 >4'.82J=%,80%;%9-$6%O2445=4572),%)%5I-0%5 QRRS<br>12 >4'.82=%,80%;%9-$6%2%%,I'%2C%,6900IB%-;I;47<br>12 ?5;-F4'-%2445=.99-572+AA27%C%5I'<br>12 ?5;-F4'-%2445=.99-572+LF27%C%5I' !"#$%F''()%*<br>12 ?5;-F4'-%2445=.99-572+LD27%C%5I' (89:$&<br>12 ?5;-F4'-%2445=.99-572GMD+GEN27%C%5I' T T<br>12 ?5;-F4'-%2#%OC44,2C%,67%=%,I=%,694,-57 !+'',-#..'I00,'*<br>12 ?5;-F4'-%2B07%,290052#-$245;%,%2C%,67%=%, 12 :0;%2GHEC%'<br>12 ?5;-F4'-%2=00,IFB0'27%C%5I'<br>12 ?5;-F4'-%2C%,67%=%,I=%,694,-57205'=457%5<br>12 F0%9-FB'-572#%OC44,2C%,67%=%,I=%,694,-57 QRRS<br>QRRS<br>!"#$%F''()%*<br><$0"#00#%1';='55%6-551'7#&4$-#%1 !"#$%F''()%*<br>!"#$%F''()%*<br>@55&-$1$"'A.&'7#&4$-#%1<br>!+'',-#..'I00,'* <$>:55-023-#?&<br>12 :0;%2#%I9-II-5720)2445=,4472.-'6%,-57 !+'',-#..'I00,'*<br>12 :0;%2,%;%524<C-$O-572445=,4472.-'6%,-572MDL T QRRT !+'',-#..'I00,'* QRRS T 12 >4'.82445=4572844',%7%928#'2.-'6%,-57<br>12 >4'.82#%I9-II-5720)2445=,4472.-'6%,-57 12 >4'.82;47'%6%5-572#%OC44,IFB,-<' 12 >4'.82%-5;%2844',%7%928#'2.-'6%,-57<br>12 >4'.82;47'%6%5-572#%I9-II-5720)2445=,4472.-'6%,-57 12 @%<%,%5'-%5.88%,2#%OC44,IFB,-<' 12 A%,F%5'47%260,'-572.-'6%,-57<br>12 >4'.82%-5;%2#%I9-I'%,8-$520)2445=,4472.-'6%,-57 T<br>QRRT<br>!"#$%F''()%* !"#$%F''()%* !"#$%F''()%* !"#$%F''()%*<br><$0"#00#%1';='.$-;$=023-#?& <$-;$=023-#?& <$0"#00#%1';='.$>:55-023-#?& B$I$%'A55&-$1$"'A.&'7#&4$-#%1')*C<br>!+'',-#..'I00,'* QRRT T !+'',-#..'I00,'* QRRT T !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 :0;%2#%I9-II-5720)2#%,0%)IFB,-<' 12 >4'.82;47'%6%5-572#%,0%)IFB,-<' 12 :0;%2#%I9-II-5720)2#%OC44,IFB,-<' 12 :0;%2,%;%52844',%7%928#'2.-'6%,-572MDL<br>12 >4'.82;47'%6%5-572#%I9-II-5720)2#%,0%)IFB,-<' 12 >4'.82;47'%6%5-572#%I9-II-5720)2#%OC44,IFB,-<'<br>**----- End of picture text -----**<br>


**Figuur 8. Uitkeringsgegevens (Bezwaar en Beroep)** 

**==> picture [684 x 411] intentionally omitted <==**

**----- Start of picture text -----**<br>
:0,,%I)05;%5G-%4;,%I2#.-G%5945;<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* RSSG RSSG !"#$%FGG()%*<br>:2#.;$.F#%6 G4F22-"#HLGH$-.II% H$-.II% :0,,%I)05;%5G-%4;,%I 01-$.<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G* RSSG U%-G%9-$624;,%I RSSG<br>12 :0;%2,%94G-%2#%J05%,2G0G2B.-I=%IG-57 1212 +45;.-;-57254487%#,.-6+I5.88%, 12 "8IFB,-$=-572.-G7%#,%-;%2,%FBGI=0,8 RSSGU%-G%9-$624;,%I2#.-G%5945;RSSG<br>RSSG 1212 3.,7%,I%,=-F%5.88%,:0;%23@AI7%7%=%5I27%B%-8 RSSG L08-F-9-%24;,%I RSSG<br>RSSG 1212 :0;%27%#00,G%7%8%%5G%:0;%2A?F+I7%7%=%5I27%B%-8 RSSG RSSG<br>12 P%#00,G%;4G.8<br>121212 P%#00,G%945;P%#00,G%)944GIP%I94FBG (F21#$3#%4%5#$-#%6 !"#$%FGG()%*<br>121212!+GG,-#..GI00,G*+45G492J%,6.,%52)%,2J%%627,05;I9472.-G6%,-57L4G.82445=4572.-G6%,-57I=%,B0.;-57L4G.82%-5;%284L-849%2.-G6%,-57I;.., )#FL$-#%6.;$-?I21#%6 !"#$%FGG()%*G RSST G 121212121212121212 ?;%5G-<-F4G-%5.88%,2A?F+?5;-F4G-%2IG4,G6J49-<-F4G-%2=097%5I2LQ""8IFB,-$=-572IG4G.I2M4G..,9-$62A%,I005N-75-<-F45G2;%%92=452;%24FBG%,5448FI5.88%,F00,548%5F00,=0%7I%9?5;-F4G-%2B45;9-FBG-57F00,9%GG%,I G RSSG 1212121212121212!+GG,-#..GI00,G*3%;,472445=.99%5;%2#%.,I2IG.;-%<-545F-%,-573%;,472445=.99%5;%2G0%947%2CD"N2F"GH3%;,472#4I-I#%.,I2IG.;-%<-545F-%,-573%;,472#4I-IG0%947%2CD"N2F"GH:0;%2IG4G.I2%%5I0.;%,G0%I9472IG.;-%<-545F-%,-57:0;%2G0%6%55-572#4I-I#%.,I2IG.;-%<-545F-%,-57L4G.82445=4572G0%6%55-57I)%,-0;%2IG.;-%<-545F-%,-57L4G.82%-5;%2IG.;-%<-545F-%,-57<br>12 L4G.82%-5;%2.-G6%,-57I=%,B0.;-57 12 L4G.82%-5;%2G0%6%55-57I)%,-0;%2IG.;-%<-545F-%,-57<br>12 "8IFB,-$=-572,%;%52%-5;%2.-G6%,-57I=%,B0.;-57 12 ?5;-F4G-%2445=.99%5;%2#%.,I2IG.;-%<-545F-%,-57<br>G RSST 1212 ?5;-F4G-%2,%FBG20)2IG.;-%<-545F-%,-57?5;-F4G-%2IG.;-%<-545F-%,-57<br>12 ?5;-F4G-%2G0%6%55-572CD"N2F"GH<br>!"#$%FGG()%*<br>RSSG G !"#$%FG()*+<br>@4%L-$L$%#%6 !"#$%FGG()%* 1212!+GG,-#..GI00,G*3456,%6%5-575.88%,3.,7%,9-$6%2IG44G 7$1-46.5I89$F$%F#$ !"#$%FGG()%*<br>12!+GG,-#..GI00,G*34565448 G 1212 :0;%2945;2;0%97,0%):0;%29%%<=0,8 12!+GG,-#..GI00,G*:0;%27%;,47IF08)%G%5G-%<br>1212 3456,%6%5-575.88%,3?: 1212 L4G.820=%,9-$;%5?5;-F4G-%20=%,9-$;%5 RSSG RSST 1212 L4G.82%-5;%2=4IG7%IG%9;%27%;,47IF08)%G%5G-%"8IFB,-$=-5727%;,47IF08)%G%5G-%<br>12 ?3+M 12 +<5%8%,I-5;-F4G-%23@A 12 D0%9-FBG-5727%;,47IF08)%G%5G-%<br>12 D%5448IG%99-57<br>12 O45;%5F0;%2?N" RSST<br>RSSG RSSG<br>!"#$%FGG()%*<br>0-C$#1.84-LFLN4"#3#54F#$.<br>!+GG,-#..GI00,G*<br>12 :0;%2G449#%B%%,I-572805;%9-57<br>G 12 :0;%2G449#%B%%,I-572IFB,-<G%9-$6<br>RSSG<br>GSST G<br>G<br>!"#$%FGG()%*<br>0<=G-$"4F#$ RSST<br>1212!+GG,-#..GI00,G*L4G.82445=4572+DOI,%94G-%L4G.82%-5;%2+DOI,%94G-% !"#$%FGG()%* F9"$#1#%6 F9"$#1#%6.%448GI%6$5I1$$-1 !"#$%FGG()%*<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 +45G492$4,%52I.FF%I=0924<7%,05; 12 M44820)9%-;-572057%F0;%%,;<br>12 +45G492.,%520)9%-;-57<br>12 :0;%29%%,J%728#0<br>12 :0;%25-=%4.20)9%-;-57<br>12 :0;%2IG4G.I20)9%-;-57<br>RSST 1212 :0;%2G-$;I#%I94720)9%-;-57L4G.82445=4572=097%520)9%-;-57 RSST G<br>12 L4G.82;-)9084 !"#$%FGG()%*<br>12 L4G.82%-5;%2=097%520)9%-;-57 F9"$#1#%6.%448G6$5I1$$-1<br>12 ?5;-F4G-%2#.-G%5945;I%20)9%-;-57<br>12 ?5;-F4G-%2;-)9084 !+GG,-#..GI00,G*<br>G G G 12 D0%9-FBG-5720)9%-;-57 1212 :0;%20)9%-;-57I5448?5;-F4G-%20)9%-;-57I544824FG-%<<br>12 "8IFB,-$=-5720)9%-;-57I5448<br>RSSG RSSG RSSG<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>A"$B#C#"#F$#F @$.5?#LC44-?$#1G5"#$%FG;II-G4-C$#1 MIC#"#F$#F<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 ?5;-F4G-%2#%,%-;B%-;2#%,0%)205;%,2%-7%525-=%4. 12 +45G492.,%52)%,2J%%62#%IFB-6#44,2=00,24,#%-; 12 :0;%2=%,=0%,8-;;%9<br>12 ?5;-F4G-%2#%,%-;B%-;2=%,,-FBG%5205,%7%984G-72J%,620<2)90%7%5;-%5IG 12 L4G.82445=4572#%IFB-6#44,2=00,24,#%-; 12 ?5;-F4G-%2#%,%-;B%-;2G%2=%,B.-N%5<br>12 ?5;-F4G-%2#%,%-;B%-;2N0%6%52#.-G%52#%,0%)IJ%5I 12 L4G.82%-5;%2#%IFB-6#44,2=00,24,#%-; 12 @%-IG-$;<br>12 ?5;-F4G-%2#%,%-;B%-;2=%,,-FBG%52NJ44,O=.-92J%,6<br>12 ?5;-F4G-%2-57%IFB,%=%52#-$2.-GN%5;#.,%4.I<br>**----- End of picture text -----**<br>


**Figuur 9. Eenmalige registratie op werkplein** 

## **4.8 Conceptueel gegevensdeelmodel Arbeidstoeleidingsgegevens** 

De arbeidstoeleidingsgegevens leggen informatie vast over de arbeidstoeleidingsrelatie van de cliënt met één of meer partijen (UWV en GSD) en de activiteiten die de toetreding van de cliënt tot de arbeidsmarkt moeten bevorderen. 

Bij de arbeidstoeleidingsgegevens worden zaken vastgelegd als de (mate van) beschikbaarheid van de cliënt voor arbeid, het beroep of de beroepen waarvoor de cliënt bemiddelbaar is en het perspectief van de cliënt op het verkrijgen van een baan. Er kunnen ook gegevens vastgelegd zijn over de bereidheid tot verhuizen, bereidheid tot werken in ploegendienst en de bereidheid tot het werken in een ander beroep. 

In de vorm van inschrijvingsgegevens bij UWV WERKbedrijf is onder meer raadpleegbaar wanneer de cliënt is ingeschreven bij de arbeidsvoorziening, waarom de cliënt is ingeschreven en eventueel wanneer en waarom de inschrijving is beëindigd. 

Het is mogelijk dat een cliënt hulp nodig heeft bij de toetreding tot de arbeidsmarkt. In dat geval kan er een trajectplan opgesteld worden waarin een aantal activiteiten staat benoemd om toetreding te vergemakkelijken. Over dit trajectplan kunnen gegevens beschikbaar zijn. 

Over een gedeeltelijke arbeidsongeschikte cliënt kunnen gegevens als de mogelijke werkbelasting beschikbaar zijn. 

Bij de arbeidstoeleiding wordt ook vastgelegd of de cliënt zelfstandig naar vacatures solliciteert en of de cliënt verwezen is naar vacatures. 

Verder zijn de gegevens in het kader van re-integratie in de eerstvolgende gegevensdeelmodellen weergegeven. 

Dit gegevensdeelmodel bevat de gegevens in het kader van Dienstverlening UWV WERKbedrijf en de gegevens in het kader van re-integratie GSD. 

**==> picture [670 x 432] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%* !"#$$%&'()*+,%-../ !"#$%&''()%*<br>F5C*G*)F*) !"#$%&''()%* 0,86E%*M?*,484F4F?F,8$.IK$I@ABCF3%*M;<br>+G*F,)$-.I0<br>!+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 @0=%27%H70%H5-==%K !+''H-#..'I00H'* 12 @0=%2-6I&GH-$AH%=%62RSP2STCU#%=H-$A<br>1212 B6=-&4'-%2#%H%-=G%-=2'%27%HG.-F%6C%-I'-$= 12121212 L46?H%?%6-686.55%HL.H8%HK-$?%2I'44'@0=%2K46=2=0%K8H0%)@0=%2K%%A70H5 N NMMP 12121212 @0=%2H%=%62%-6=%2-6I&GH-$7-682RSP2STCU#%=H-$A34'.52%-6=%28%K=-8G%-=I'%H5-$62-6I&GH-$7-682RSP2STCU#%=H-$A34'.52%-6=%2-6I&GH-$7-682RSP2STCU#%=H-$A34'.52-6I&GH-$7-682RSP2STCU#%=H-$A<br>LMMN 12 34'.5207%HK-$=%6<br>12 B6=-&4'-%207%HK-$=%6<br>12 +A6%5%HI-6=-&4'-%2LCD<br>!"#$%&''()%* LMMP<br>1F86E*LC((%EF*3$6G*F,)$?55%$(%CF*3<br>12!+''H-#..'I00H'*+46'4K2.H%62)%H2N%%?2#%I&G-?#44H2700H24H#%-= LMMN N !"#$%&''()%* JGFK*C*G*)F*)<br>1212 34'.5244674682#%I&G-?#44H2700H24H#%-=34'.52%-6=%2#%I&G-?#44H2700H24H#%-= N 12!+''H-#..'I00H'*B6=-&4'-%2#%H%-=G%-=2#%H0%)206=%H2%-8%626-7%4.<br>12 B6=-&4'-%2#%H%-=G%-=27%HH-&G'%6206H%8%K54'-82N%H?20A2)K0%8%6=-%6I'<br>LMMN N NMMP N 12 B6=-&4'-%2#%H%-=G%-=2F0%?%62#.-'%62#%H0%)IN%6I<br>12 B6=-&4'-%2#%H%-=G%-=27%HH-&G'%62FN44HI7.-K2N%H?<br>!"#$%&''()%* 1%5, LMMN N !+''H-#..'I00H'*!"#$%&''()%* !"#$%FG()*F N LMMN 12 B6=-&4'-%2-68%I&GH%7%62#-$2.-'F%6=#.H%4.I<br>12!+''H-#..'I00H'*@0=%27%I'-8-682VRSB 1212 34'.5244674682+9:;H%K4'-%34'.52%-6=%2+9:;H%K4'-% 1F86E*LC((%EF*3$6G*F,)$?55%$CF2*33FG*,4 !"#$%&''()%*<br>1212 @0=%2?0K052VRSB@0=%2)4H'-$2VRSB LMMN N N LMMP 12!+''H-#..'I00H'*34'.52%-6=%2)%H-0=%26-%'2#%5-==%K#44H<br>12 B6=-&4'-%2=-H%&'2#%5-==%K#44H<br>!"#$%&''()%*<br>K%*M8)FGG*,4$(%CF*387G*6E)<br>12!+''H-#..'I00H'*@0=%2H%=%62%-6=%27H-$I'%KK-6824H#%-=I)K-&G'2#-$I'46= !%CF*382(%L)LG(G*;*6()*F8 !"#$%&''()%*<br>12121212 @0=%27H-$I'%KK-6824H#%-=I)K-&G'2#-$I'46=34'.52446746827H-$I'%KK-6824H#%-=I)K-&G'34'.52%-6=%27H-$I'%KK-6824H#%-=I)K-&G'B6=-&4'-%27H-$I'%KK-6824H#%-=I)K-&G' LMMN N N LMMN 1212!+''H-#..'I00H'*@0=%2'44K#%G%%HI-682506=%K-68@0=%2'44K#%G%%HI-682I&GH-A'%K-$?<br>!"#$%&''()%*<br>HFC5=G5,)IF44*,4 T;54-K24=H%I2&K-%6'<br>12!+''H-#..'I00H'*34'.52446746828%#0.N06'F%88-68 LMMN N<br>12 34'.52%-6=%28%#0.N06'F%88-68<br>!"#$%&''()%*<br>!"#$%&''()%* "%(MF6)7G(,<br>!+''H-#..'I00H'* 1F2*33FG*,4 N LMMN 12!+''H-#..'I00H'*34'.5244674682'H4$%&')K46<br>121212121212 34'.52#%5-==%K-6834'.527%HN-$F-682644H274&4'.H%B6=-&4'-%2)K44'I-68"5I&GH-$7-682H%I.K'44'2#%5-==%K-68"5I&GH-$7-682I00H'2&06'4&'2#%5-==%K-68"5I&GH-$7-682I'4'.I2#%5-==%K-68 LMMP N LMMP LMMN 12121212121212 34'.52%-6=%28%)K46=2'H4$%&')K4634'.52%-6=%2'H4$%&')K4634'.52A-646&-%K%24=5-6-I'H4'-%7%24AG46=%K-6834'.5206'7468I'2H%-6'%8H4'-%)K4634'.527%HF06=%62#H-%A28%%62&06'4&'H4452H%-6'%8H4'-%&04&G"5I&GH-$7-682#%I&G-?#44HG%-=2H%-6'%8H4'-%'H4$%&'<br>12 "5I&GH-$7-682K0&4'-%2H%-6'%8H4'-%'H4$%&'<br>N 12 "5I&GH-$7-682H%=%62%-6=%2'H4$%&')K46<br>12 "5I&GH-$7-682I00H'2H%-6'%8H4'-%4&'-7-'%-'<br>N<br>LMMN LMMP LMMP<br>!"#$%&''()%* !"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>IF%L4F?F% K(6()=%F +5,)(6)7F%855,9:(;3FG*,4 LMMP !;87%((L$LG(,)$2F)$.IK$I@ABCF3%*M;<br>!+''H-#..'I00H'* !+''H-#..'I00H'* !+''H-#..'I00H'* LMMP LMMN !+''H-#..'I00H'*<br>12 +46IK.-'-68I6.55%H2LP N N 12 +46'4K24H#%-=I.H%6274&4'.H%254J-544K2)%H2N%%? LMMN LMMP 12 H4452&06'4&')%HI006I;4A=%K-68 12 @0=%2'()%24AI)H44?2?K46'2RSP2STCU#%=H-$A<br>12 Q46=%KI644520H846-I4'-% 1212 +46'4K24H#%-=I.H%6274&4'.H%25-6-544K2)%H2N%%?H445274&4'.H% LMMP LMMN 1212 34'.52'-$=2446746824AI)H44?2?K46'2RSP2STCU#%=H-$A34'.52'-$=2%-6=%24AI)H44?2?K46'2RSP2STCU#%=H-$A<br>LMMN 1212 H.55%H274&4'.H%"5I&GH-$7-682&06'H4&'I00H'274&4'.H%2OLMMNO T;54-K24=H%I2&06'4&')%HI0064A=%K-68 LMMP 12 "5I&GH-$7-68206=%HN%H)24AI)H44?2?K46'2RSP2STCU#%=H-$A<br>12 "5I&GH-$7-682I00H'274&4'.H% !"#$%&''()%*<br>-)(,3((%3$@:2(*G$(3%F8<br>LMMP<br>!+''H-#..'I00H'*<br>12 T;54-K24=H%I<br>12 B6=-&4'-%2700H?%.H2%;54-K24=H%I<br>12 B6=-&4'-%2VRSB2%;54-K24=H%I<br>**----- End of picture text -----**<br>


## **Figuur 10. Arbeidstoeleidingsgegevens** 

**==> picture [643 x 381] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$$%&'()*+,%-../<br>!"#$%&''()%*<br>:)"#$&+;,-K<br>!"#$%&''()%*<br>!+'',-#..'I00,'* !"#$%&''()%* B'#(##$C?D%&+3"#$%&'#()#$"$*+,-.+-I012#3("45<br>12 FA5G,%G%5-585.BB%, ."%"#+3"#$%&'#()#$"$*+,-.+-I012#3("45<br>12 F.,8%,7-$G%2I'AA' !+'',-#..'I00,'*<br>12 304%27A54240%78,0%) !+'',-#..'I00,'* 12 304%2&05&7.I-%206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>12 304%27%%?60,B 12 "BI&J,-$6-582-5?0,BA'-%2600,2,%N-5'%8,A'-%#%4,-$? 12 304%2I'A'.I206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>12 @A'.B206%,7-$4%5 12 "BI&J,-$6-582B0'-6%,-582AA5)AG24-%5I'6%,7%5-5829:;2:K=L#%4,-$? 12 @A'.B206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>12 H54-&A'-%206%,7-$4%5 12 "BI&J,-$6-5826-I-%2G7A5' 12 "BI&J,-$6-58206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>12 +?5%B%,I-54-&A'-%2F=I 12 "BI&J,-$6-5826-I-%29:;2:K=L#%4,-$? 12 "BI&J,-$6-582,%4%5206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>12 "BI&J,-$6-582600,8%I&J-%4%5-I 12 C0%7-&J'-58206%,%%5G0BI'24-%5I'6%,7%5-5829:;2:K=L#%4,-$?<br>Q OPPR OPPR<br>QPPR OPPQ OPPQ OPPQ<br>!"#$%&''()%* !"#$%&''()%* OPPR<br>678+(#)9&"# !"#$%&'#()#$"$*+,-.+-I012#3("45 !"#$%&''()%*<br>!+'',-#..'I00,'* !+'',-#..'I00,'* :?$&9=&L#(%??$@A953#)"$*<br>1212 @A'.B2AA56A582+CDN,%7A'-%@A'.B2%-54%2+CDN,%7A'-% Q OPPR 121212 304%2,%4%52%-54%24-%5I'6%,7%5-5829:;2:K=L#%4,-$?@A'.B2AA56A5824-%5I'6%,7%5-5829:;2:K=L#%4,-$?@A'.B2%-54%24-%5I'6%,7%5-5829:;2:K=L#%4,-$? Q OPPR 12!+'',-#..'I00,'*LAAB2&05'A&')%,I005MNA?4%7-58<br>12 =%?%,%5'-%5.BB%,24-%5I'6%,7%5-5829:;2:K=L#%4,-$? OPPQ<br>Q<br>OPPR<br>OPPR OPPR<br>!"#$%&''()%* !"#$%&''()%*<br>-#(C"$%&(ED#$&+,-.+-I012#3("45 1$#)LE$&+C)9$&%"&E9&"#<br>OPPQ !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 304%2,%4%52%-54%2N%,G-5I',.B%5'29:;2:K=L#%4,-$? 12 304%2,%4%52%-54%2G5%7).5'2G7A5'<br>!"#$%&''()%* 12 @A'.B2AA56A582N%,G-5I',.B%5'29:;2:K=L#%4,-$? 12 304%2'()%2G5%7).5'2G7A5'<br>7(94#=&L)9$ 12 @A'.B2%-54%2N%,G-5I',.B%5'29:;2:K=L#%4,-$? 12 @A'.B2AA56A582G5%7).5'2G7A5'<br>12 "BI&J,-$6-582,%4%52-5O%'2N%,G-5I',.B%5'29:;2:K=L#%4,-$? 12 @A'.B2%-54%2G5%7).5'2G7A5'<br>1212!+'',-#..'I00,'*@A'.B2AA56A582',A$%&')7A5@A'.B2%-54%28%)7A542',A$%&')7A5 12 "BI&J,-$6-582N%,G-5I',.B%5'29:;2:K=L#%4,-$? 1212 "BI&J,-$6-582G5%7).5'2G7A5'"BI&J,-$6-582,%4%52A?B%74%52G5%7).5'2G7A5'<br>12 @A'.B2%-54%2',A$%&')7A5 OPPQ<br>12 @A'.B2?-5A5&-%7%2A4B-5-I',A'-%6%2A?JA54%7-58<br>12 @A'.B205'6A58I'2,%-5'%8,A'-%)7A5<br>12 @A'.B26%,O054%52#,-%?28%%52&05'A&' OPPR<br>121212 LAAB2,%-5'%8,A'-%&0A&J"BI&J,-$6-582#%I&J-G#AA,J%-42,%-5'%8,A'-%',A$%&'"BI&J,-$6-58270&A'-%2,%-5'%8,A'-%',A$%&' BL)?%%"$*+C$#)LE$&+C)9$&%"&E9&"# !"#$%&''()%*<br>12 "BI&J,-$6-582,%4%52%-54%2',A$%&')7A5 !+'',-#..'I00,'*<br>12 "BI&J,-$6-582I00,'2,%-5'%8,A'-%A&'-6-'%-' 12 304%2A&'0,20)70II-582G5%7).5'2G7A5'<br>12 304%2,%4%52%-54%20)70II-582G5%7).5'2G7A5'<br>12 304%2I'A'.I20)70II-582G5%7).5'2G7A5'<br>12 @A'.B20)70II-582G5%7).5'2G7A5'<br>12 "BI&J,-$6-5820)70II-582G5%7).5'2G7A5'<br>12 C0%7-&J'-5820)70II-582G5%7).5'2G7A5'<br>**----- End of picture text -----**<br>


**Figuur 11. Arbeidstoeleidingsgegevens (Dienstverlening UWV WERKbedrijf)** 

**==> picture [526 x 428] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$$%&'()*+,%-../<br>!"#$%&GG()%*<br>!"#$%&'()*+<br>!+GG,-#..GI00,G*<br>12 3456,%6%5-575.88%,<br>12 3.,7%,9-$6%2IG44G<br>12 :0;%2945;2;0%97,0%)<br>12 :0;%29%%<=0,8<br>12 L4G.820=%,9-$;%5<br>12 ?5;-&4G-%20=%,9-$;%5<br>12 +<5%8%,I-5;-&4G-%23@A !"#$%&GG()%*<br>!1%&02&3$I411%56078$"#%9<br>P !+GG,-#..GI00,G*<br>NOOQ 12 N4482&05G4&G)%,I005FM4<;%9-57<br>POOQ NOOQ<br>!"#$%&GG()%* !"#$%&GG()%*<br>,-.'I$"0&#$ ,I:$#84;$I<19$%<br>!+GG,-#..GI00,G* P NOOP !+GG,-#..GI00,G*<br>12 L4G.82445=4572+BCM,%94G-% 12 :0;%24,#%-;I=%,807%5<br>12 L4G.82%-5;%2+BCM,%94G-%<br>P P !"#$%&GG()%*<br>=1$"'I$#%&$9I0&#$;11IL#$%#%9<br>!+GG,-#..GI00,G*<br>NOOP<br>NOOQ 12 :0;%2;0%92,%-5G%7,4G-%=00,G-%5-57<br>!"#$%&GG()%*<br>?$#%&$9I0&#$;11IL#$%#%9<br>!+GG,-#..GI00,G*<br>12 :0;%2G()%2,%-5G%7,4G-%=00,G-%5-572HIL<br>12 L4G.82445=4572,%-5G%7,4G-%=00,G-%5-57 !"#$%&GG()%*<br>12 L4G.82%-5;%27%)945;2,%-5G%7,4G-%=00,G-%5-57 .11%@14&$%4A:4#8#$<br>12 L4G.82%-5;%2,%-5G%7,4G-%=00,G-%5-57<br>12 L4G.82%-5;%2=%,9%57;%2#%I9-IG%,8-$52,%-5G%7,4G-%=00,G-%5-57 NOOP NOOP !+GG,-#..GI00,G*<br>12 L4G.82-57%#,.-6548%2,%-5G%7,4G-%=00,G-%5-57 12 A%,&%5G47%29005O44,;%2G%520)G-&JG%2=452LMC<br>12 L4G.82-5548%2,%-5G%7,4G-%=00,G-%5-57<br>12 L4G.82=00,90)-7%2G0%6%55-572,%-5G%7,4G-%=00,G-%5-57<br>12 "8I&J,-$=-572,%-5G%7,4G-%=00,G-%5-57<br>12 "8I&J,-$=-572G()%2,%-5G%7,4G-%=00,G-%5-57<br>12 @%7-IG,4G-%5.88%,2,%-5G%7,4G-%=00,G-%5-572HIL<br>12 B0%9-&JG-572,%-5G%7,4G-%=00,G-%5-57<br>**----- End of picture text -----**<br>


**Figuur 12. Arbeidstoeleidingsgegevens (Re-integratie GSD)** 

**==> picture [678 x 434] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>(&-%<--I<'&$"$B33%%LAA$I<br>!+GG,-#..GI00,G*<br>12 :0;%2G()%2G%9%<0055.88%,<br>12 ?5;-&4G-%27%B%-82G%9%<0055.88%,<br>12 ?5;-&4G-%2=00,6%.,2G%9%<0055.88%,<br>12 J%9%<0052945;5.88%,<br>12 J%9%<0055.88%, LMMN J%9%<0055.88%,<br>&05G4&G)%,I005<br>LMMP<br>J%9%<0055.88%,<br>&9-%5G N<br>!"#$%&GG()%* !"#$%&GG()%*<br>,-%.I--0'I$#%&$0I-&#$&I-1$2& LMMN ,-%.I--0'I$#%&$0I-&#$.33I4#$%#%0<br>!+GG,-#..GI00,G* !"#$$%&'()*+,%-../ !+GG,-#..GI00,G*<br>12 >4G.82445=,4472,%-5G%7,4G-%)945 !"#$%&GG()%* 12 +45G4924457%=,447;%2,%-5G%7,4G-%=00,D-%5-57<br>12 >4G.82#%I&B-66-572B%,#%00,;%9-572+" !"#$%&'()*+ 12 >4G.82445=,4472,%-5G%7,4G-%=00,D-%5-57<br>12 >4G.8205G=457IG#%=%IG-7-572;00,=%,C-$D-572NF> 12 >4G.824<7%B45;%9;2445=,4472,%-5G%7,4G-%=00,D-%5-57<br>1212 >4G.82=%,D%5;-572445=,4472,%-5G%7,4G-%=-I-%G4482,%-5G%7,4G-%#%;,-$< LMMP N 12!+GG,-#..GI00,G*3456,%6%5-575.88%, N LMMP 1212 >4G.82%-5;%2,%;%9-$6%2#%I9-IG%,8-$52445=,4472,%-5G%7,4G-%=00,D-%5-57>4G.82-5G,%66-572445=,4472,%-5G%7,4G-%=00,D-%5-57<br>12 "8I&B,-$=-572,%;%520)IG%99%52,%-5G%7,4G-%=-I-% 12 3.,7%,9-$6%2IG44G 12 >4G.8205G=457IG2445=,4472,%-5G%7,4G-%=00,D-%5-57<br>12 "8I&B,-$=-572I00,G2=00,;,4&BG2,%-5G%7,4G-%G,4$%&G 12 :0;%2945;2;0%97,0%) 12 >4G.8205G=457IG205G#,%6%5;%27%7%=%5I<br>12 :0;%29%%<=0,8 12 >4G.820)=,447205G#,%6%5;%27%7%=%5I<br>12 >4G.820=%,9-$;%5 12 >4G.82.-G%,IG%205G=457IG205G#,%6%5;%27%7%=%5I<br>N N 1212 ?5;-&4G-%20=%,9-$;%5+<5%8%,I-5;-&4G-%23@A 1212 "8I&B,-$=-5724457%=,447;%2,%-5G%7,4G-%=00,D-%5-57"8I&B,-$=-572G()%2445=,47%,2,%-5G%7,4G-%=00,D-%5-57<br>N N N LMMP<br>LMMN LMMN LMMP<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>5I-1$2&6"-% 7I#18&$""#%0'I$#%&$0I-&#$ !3A6"$&$I#%0'--%.I--0'I$#%&$0I-&#$.33I4#$%#%0<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 >4G.82445=4572G,4$%&G)945 12 >4G.82445=4572=,-$IG%99-572,%-5G%7,4G-% 12 ?5;-&4G-%205G=457IG205G#,%6%5;%27%7%=%5I<br>12 >4G.82%-5;%27%)945;2G,4$%&G)945 12 >4G.82%-5;%2=,-$IG%99-572,%-5G%7,4G-% 12 "8I&B,-$=-57205G#,%6%5;%27%7%=%5I<br>1212 >4G.82%-5;%2G,4$%&G)945>4G.82<-545&-%9%24;8-5-IG,4G-%=%24<B45;%9-57 12 "8I&B,-$=-572,%;%52=,-$IG%99-572,%-5G%7,4G-% LMMP LMMN<br>121212 >4G.8205G=457IG2,%-5G%7,4G-%)945>4G.82=%,D05;%52#,-%<27%%52&05G4&GG4482,%-5G%7,4G-%&04&B ,I?$#<8.$I@3L<#%0 !"#$%&GG()%* ($2&3I'?$I3$68:'$%'?$<I#1B8"$.$% !"#$%&GG()%*<br>12121212 "8I&B,-$=-572#%I&B-6#44,B%-;2,%-5G%7,4G-%G,4$%&G"8I&B,-$=-57290&4G-%2,%-5G%7,4G-%G,4$%&G"8I&B,-$=-572,%;%52%-5;%2G,4$%&G)945"8I&B,-$=-572I00,G2,%-5G%7,4G-%4&G-=-G%-G N LMMN 1212!+GG,-#..GI00,G*>4G.82445=45724,#%-;I=%,B0.;-57>4G.82%-5;%24,#%-;I=%,B0.;-57 LMMP N 1212!+GG,-#..GI00,G*:0;%2I%&G0,G4482I%&G0,<br>N<br>!"#$%&GG()%* !"#$%&GG()%*<br>N LMMP +%4$&'36"$#<#%0 LMMN N =$#%&$0I-&#$.33I4#$%#%0<br>N N N N !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12121212 ?5;-&4G-%2-5D%G20)9%-;-57>4G.82445=4572=097%520)9%-;-57>4G.82%-5;%2=097%520)9%-;-57J0%9-&BG-5720)9%-;-57 12121212 :0;%2G()%2,%-5G%7,4G-%=00,D-%5-572NF>>4G.82445=4572,%-5G%7,4G-%=00,D-%5-57>4G.82%-5;%27%)945;2,%-5G%7,4G-%=00,D-%5-57>4G.82%-5;%2,%-5G%7,4G-%=00,D-%5-57 D$.$I-%2#$I'I$#%&$0I-&#$.33I4#$%#%0 !"#$%&GG()%*<br>!"#$%&GG()%* 121212 >4G.82%-5;%2=%,9%57;%2#%I9-IG%,8-$52,%-5G%7,4G-%=00,D-%5-57>4G.82-57%#,.-6548%2,%-5G%7,4G-%=00,D-%5-57>4G.82-5548%2,%-5G%7,4G-%=00,D-%5-57 N LMMN 12!+GG,-#..GI00,G*G44829%=%,45&-%,2,%-5G%7,4G-%=00,D-%5-57<br>LMMN )#&.-"'I$#%&$0I-&#$&I-1$2& 12 >4G.82=00,90)-7%2G0%6%55-572,%-5G%7,4G-%=00,D-%5-57<br>12 "8I&B,-$=-572,%-5G%7,4G-%=00,D-%5-57<br>!+GG,-#..GI00,G* 12 "8I&B,-$=-572G()%2,%-5G%7,4G-%=00,D-%5-57<br>12 >4G.8205G=457IG28%9;-572.-G=492,%-5G%7,4G-%G,4$%&G26945G 12 @%7-IG,4G-%5.88%,2,%-5G%7,4G-%=00,D-%5-572NF><br>LMMP LMMP 12 >4G.82.-G=492,%-5G%7,4G-%G,4$%&G26945G 12 J0%9-&BG-572,%-5G%7,4G-%=00,D-%5-57<br>!"#$%&GG()%* !"#$%&GG()%* LMMP N N<br>=-663I&-0$'I$#%&$0I-&#$&I-1$2& =$#%&$0I-&#$6I3<L2& !"#$%&GG()%* LMMN<br>1212!+GG,-#..GI00,G*>4G.82#%00,;%9-572,4))0,G47%2,%-5G%7,4G-%G,4$%&G>4G.8205G=457IG2,4))0,G47%2,%-5G%7,4G-%G,4$%&G 1212!+GG,-#..GI00,G*>4G.82IG4G.I2C-$D-7-572,%-5G%7,4G-%),0;.&G"8I&B,-$=-572,%;%524<C-$D-572,%-5G%7,4G-%),0;.&G !+GG,-#..GI00,G* (9:;$& LMMN C$8"#88#%0'36'--%0$.I--0<$'I$#%&$0I-&#$.33I4#$%#%0 !"#$%&GG()%*<br>12 "8I&B,-$=-572#%=-5;-572,4))0,G47%2,%-5G%7,4G-%G,4$%&G 12 "8I&B,-$=-572,%-5G%7,4G-%),0;.&G 12 :0;%2FHIC%G !+GG,-#..GI00,G*<br>12 "8I&B,-$=-572I00,G2,4))0,G47%2,%-5G%7,4G-%G,4$%&G2OLMMNO 1212 "8I&B,-$=-572IG4G.I2,%-5G%7,4G-%),0;.&GJ0%9-&BG-572,%;%524<C-$D-572,%-5G%7,4G-%),0;.&G 1212 >4G.82#%I9-II-5720)24457%=,447;%2,%-5G%7,4G-%=00,D-%5-57"8I&B,-$=-572,%;%524<C-$D-572,%-5G%7,4G-%=00,D-%5-57<br>12 "8I&B,-$=-572IG4G.I24457%=,447;%2,%-5G%7,4G-%=00,D-%5-57<br>12 J0%9-&BG-572#%I9-II-5720)24457%=,447;%2,%-5G%7,4G-%=00,D-%5-57<br>**----- End of picture text -----**<br>


**Figuur 13. Arbeidstoeleidingsgegevens (Re-integratie UWV)** 

## **4.9 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Polisadministratie** 

Met de introductie van Polisadministratie bij het UWV zijn er gegevens die betrekking hebben op de loonaangifte bij de Belastingdienst in het SGR gedefinieerd. In dit gegevensdeelmodel worden deze gegevens weergegeven. Het gaat dan bijvoorbeeld om gegevens over de loonbelasting, administratieve eenheid, inkomstenverhouding, inkomstenopgave en inkomstenperiode. 

**==> picture [453 x 558] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%*<br>2(*+$,(3-(-(I("F4(I(*+"-3+"#$%FG("$)-.I(<br>!+GGH-#..GI00HG*<br>12 C5G.@255865892)%H-04%<br>121212 C5G.@2%-84%2)%H-04%F55H255865892)%H-04%F55H2%-84%2)%H-04% !"#$%FG(")(*+$,( !"#$%FGG()%*<br>!+GGH-#..GI00HG*<br>VPPX 12 304%255H425H#%-4I6%H70.4-89<br>VPP\ 1212 304%23+"304%23+"2-8J%8%H<br>!"#$%FGG()%* 12 304%2;5I%2-84%J-892<=L<br>!"#$%FG("$)-.I( 12 304%2-8F-4%8G%J%2-8?0@IG%86%H@-84%H-89<br>12 304%2-86J0%426%HA%?%H-89I)J-F7G<br>!+GGH-#..GI00HG* 12 304%2J008#%J5IG-89G5#%J<br>12 +58G5J2F08GH5FG.H%82)%H2N%%? 12 304%2)H%@-%?0HG-89<br>12 +58G5J2LBM459%82-8?0@IG%80)956% 12 304%2H%4%829%%82#-$G%JJ-8925.G0<br>12 +58G5J26%HJ0084%2.H%8 12 304%2I00HG2-8?0@IG%86%H70.4-89<br>12 N%4H592558N5I2-827%G2F.@.J5G-%6%2)H%@-%J0082+<;27%HA-%8 12 304%2G()%25H#%-4IF08GH5FG<br>12 N%4H592558N5I2-827%G2F.@.J5G-%6%2)H%@-%J0082+<;27009 12 304%26%HA%?%H-89II-G.5G-%2LB<<br>12 N%4H592558N5I2-827%G2F.@.J5G-%6%2)H%@-%J0082+<;2J559 12 C5G.@255865892-8?0@IG%8)%H-04%<br>12 N%4H592558N5I2-827%G2F.@.J5G-%6%2)H%@-%J0082+<;2.-G?%H-89 12 C5G.@2%-84%2-8?0@IG%8)%H-04%<br>12 N%4H592558N5I2-827%G2F.@.J5G-%6%2)H%@-%J0082<7? 12 D84-F5G-%25586H5592J008?0IG%8600H4%%J25H#%-4I9%7584-F5)G%2N%H?8%@%H<br>12 N%4H592F08GH5FGJ008 12 D84-F5G-%25586H5592J008?0IG%8600H4%%J27%H)J55GI%825H#%-4I9%7584-F5)G%2N%H?8%@%H<br>12 N%4H592%OGH52)%H-04%2I5J5H-I 12 D84-F5G-%25586H5592J008?0IG%8600H4%%J20.4%H%2N%H?8%@%H<br>1212 N%4H5929%4-;;%H%8G-%%H4%2)H%@-%2<7?N%4H5929%4-;;%H%8G-%%H4%2)H%@-%2<+"O<D+2-8?0@IG%80)956% 1212 D84-F5G-%25586H5592J008?0IG%8600H4%%J240%J9H0%)2#58%85;I)H55?2%82IF70J-89I#%J%@@%H4%8D84-F5G-%25586.JJ-8920)2.-G?%H-89 !"#$%FGG()%* >.G+$".4+G(+G<br>1212121212121212 N%4H5929%80G%82A%%459%85;GH%?N%4H5929%I)55H42J%6%8IJ00)H%9%J-89N%4H592-89%70.4%82#-$4H59%2L6NN%4H592-89%70.4%82J008#%J5IG-89O)H%@-%260J?I6%HA%?%H-89N%4H592-82.-G?%H-892#%9H%)%82#%G55J4%25J-@%8G5G-%N%4H592J%6%8IJ00)6%HJ0;?0HG-892G0%9%)5IGN%4H592J0082#%J5IG260J9%8I2G5#%J2#-$A084%H%2#%J08-89%8N%4H592J0082-829%J4 1212121212121212 D84-F5G-%25H#%-4I06%H%%8?0@IG2600H208#%)55J4%2G-$4D84-F5G-%24%%J85@%2G-$4I)55H;084ID84-F5G-%2$55H.H%880H@D84-F5G-%2J0082-8FJ.I-%;2<+F"GH2.-G?%H-89D84-F5G-%2J0082-I2I@%4%J2+"<2%8O0;2+D"2600H25JJ%%8IG5584%D84-F5G-%20)H0%)06%H%%8?0@IGD84-F5G-%2)%HI08%%JIJ%8-8928-%G2-82J008D84-F5G-%2)H%@-%?0HG-8925H#%-4I9%7584-F5)G%2N%H?8%@%H 121212121212!+GGH-#..GI00HG*304%2#-$A084%H2G%4%HJ584%HIF75)304%285G-085J-G%-G304%2H%4%826%H?H-$9-892G%4%HJ584I%285G-085J-G%-G304%2H%4%826%HJ-%I2G%4%HJ584I%285G-085J-G%-GC5G.@25586589285G-085J-G%-GC5G.@2%-84%285G-085J-G%-G<br>1212 N%4H592J0082J008#%J5IG-89O)H%@-%260J?I6%HA%?%H-89%8N%4H592J0082.-G206%HN%H? 1212 D84-F5G-%2)H%@-%?0HG-89240%J9H0%)2#58%85;I)H55?2%82IF70J-89I#%J%@@%H4%8D84-F5G-%2)H%@-%?0HG-8927%H)J55GI%825H#%-4I9%7584-F5)G%2N%H?8%@%H VPP\<br>12 N%4H5928-%G2-829%J42.-G9%?%%H42J008 12 D84-F5G-%2)H%@-%?0HG-892-824-%8IG28%@%825H#%-4I9%7584-F5)G%2N%H?8%@%H<br>121212 N%4H5920)#0.N25H#%-4I600HN55H4%8#%4H59N%4H5920)9%#0.N42H%F7G2%OGH52)%H-04%2I5J5H-IN%4H5920)9%#0.N42H%F7G265?58G-%G0%IJ59 121212 D84-F5G-%2)H%@-%?0HG-892$089%H%2N%H?8%@%HD84-F5G-%2)H%@-%?0HG-8920.4%H%2N%H?8%@%HD84-F5G-%2)H%@-%?0HG-8920.4%H%2N%H?8%@%HI !"#$%FGG()%* ;4+("G35<=!<br>121212121212121212 N%4H5920)85@%25H#%-4I600HN55H4%8#%4H59N%4H592)H%@-%2+0;N%4H592)H%@-%2+<;27%HA-%8N%4H592)H%@-%2+<;27009N%4H592)H%@-%2+<;2J559N%4H592)H%@-%2+<;2.-G?%H-89N%4H592558N5I2F.@.J5G-%;2)H%@-%J0082P="N%4H592)H%@-%J0082<+"ODB+O<H+N%4H592)H%@-%J0082<+"O<H+ 121212121212121212 D84-F5G-%2)H%@-%6H-$IG%JJ-892@5H9-85J%25H#%-4D84-F5G-%2).#J-%?H%F7G%J-$?%2558IG%JJ-892600H208#%)55J4%2G-$4D84-F5G-%2H%9%J@5G-925H#%-4I)5GH008D84-F5G-%2IF7H-;G%J-$?%25H#%-4I06%H%%8?0@IGD84-F5G-%2G-$4%J-$?%27%;;-89I?0HG-89D84-F5G-%265?58G-%#088%82G0%9%)5IGD84-F5G-%26%H60%H2658N%9%24%2D870.4-89I)J-F7G-9%D84-F5G-%26%HA%?%H42<+"O<D+D84-F5G-%26%HA%?%H42<< 12121212121212!+GGH-#..GI00HG*N58?H%?%8-898.@@%HN.H9%HJ-$?%2IG55G304%2J584240%J9H0%)304%2J%%;60H@C5G.@206%HJ-$4%8D84-F5G-%206%HJ-$4%8+;8%@%HI-84-F5G-%2NRQ VPPX >.G11*4+9#32(*F$$" !"#$%FGG()%*<br>12 N%4H592)H%@-%2I%FG0H;084I 12 D84-F5G-%26%HA%?%H42L< !+GGH-#..GI00HG*<br>12 N%4H592)H%@-%2P=" 12 D84-F5G-%2N5F7G9%J420.4%2H%9%J-89 12 +584.-4-892855@9%#H.-?<br>12 N%4H592)H%@-%2<+"O<H+ 12 D84-F5G-%2J0087%;;-89I?0HG-892G0%9%)5IG 12 +M8.@@%H<br>2(*+$,(3-(-(I("FI*..- !"#$%FGG()%* 1212 N%4H592)H%@-%2<<2+<=N%4H592)H-6%9%#H.-?25.G0 VPP\ 1212 N.H9%HI%H6-F%8.@@%H304%2NRQM9%9%6%8I29%7%-@<br>+"#$%FG("$)-.I( 12 N%4H592H%F7GIGH%%?I2#%G55J4%25J-@%8G5G-% VPPX 12 304%29%#00HG%9%@%%8G%<br>1212!+GGH-#..GI00HG*C5G.@255865892)%H-04%C5G.@2%-84%2)%H-04% VPPX VPPX 12121212 N%4H592H%8G%M2%8O0;2?0IG%8600H4%%J2)%HI08%%JIJ%8-89N%4H59265?58G-%G0%IJ59N%4H5926%H90%4-892H%-I?0IG%8208#%J5IGN%4H5926%H90%4-892L6N !"#$%FG("I(*0$1,+"- !"#$%FGG()%* VPP\ X 12121212 304%2QDB+M9%9%6%8I29%7%-@H%#00HG%45G.@H%#00HG%J584H%#00HG%)J55GI<br>12 N%4H5926%HH%?%84%25H#%-4I?0HG-89 !+GGH-#..GI00HG* 12 H%IJ5F7G<br>12 N%4H5926%HIGH%?G%25586.JJ-8920)2.-G?%H-892N%H?8%@%HI6%HA%?%H-89 12 +584.-4-892-8?0@IG%86%H70.4-892N%H?9%6%H 12 D4%8G-;-F5G-%8.@@%H2QDB+<br>12 N%4H592N%H?9%6%HI7%;;-892LB< 12 304%2H%4%82%-84%25H#%-4I6%H70.4-89 12 D84-F5G-%2IG5HG?N5J-;-F5G-%260J9%8I2CP"<br>12121212 N%4H592N%H?9%6%HI#-$4H59%2?-84%H0)6589N%4H592N%H?8%@%HI#-$4H59%2)H-6%9%#H.-?25.G0N%4H592<<2)H%@-%2N5F7G9%J4;084I2-8?0@IG%80)956%C5G.@255865892-8?0@IG%80)956% XPP\ X 12121212 304%2H%4%82%-84%2-8?0@IG%86%H70.4-892;J%ON%H?%HC5G.@255865892-8?0@IG%86%H70.4-89C5G.@2%-84%2-8?0@IG%86%H70.4-89Q%HI08%%JI8.@@%H X VPPX !"#$%FGG()%* 4$$".."-+:G(2(*F$$" 12121212 "@IF7H-$6-892IG5G.I2G5G..HJ-$?2Q%HI008L-98-;-F58G24%%J265824%25F7G%H855@BM8.@@%HB00H85@%8<br>12 C5G.@2%-84%2-8?0@IG%80)956% 12 B0J98.@@%H2-8?0@IG%86%H70.4-89 12 B00H60%9I%J<br>12 N%4H592#H.G0J0082LB 12 D84-F5G-%27584J-F7G-89<br>X 12 B00HJ%GG%HI<br>!"#$%FGG()%*<br>5(6G$*3*+F+6$-*$()3+"#$%FG("$)-.I( XPP\ !"#$%FGG()%* =%-G%J-$?254H%I2)%HI008254@-8-IGH5G-%6%2%%87%-4 !"#$%FGG()%*<br>!+GGH-#..GI00HG* VPP\ VPPX 2(*F$$" VPP\ =%-G%J-$?254H%I VPP\ ?,*(F<br>121212 N%4H592558N5I2F.@.J5G-%;2)H%@-%J0082I%FG0H;084IN%4H592)H%@-%2I%FG0H;084I304%2I%FG0H2H-I-F09H0%) VPPX VPP\ X VPPX VPP\ 12!+GGH-#..GI00HG*"@IF7H-$6-892.-G9%#H%-4%2H%F7GI60H@ VPPXVPPXVPP\ 30HH%I)084%8G-%54H%I230HH%I)084%8G-%54H%I2#.-G%8J584=%-G%J-$?254H%I2J008558)%HI008254@-8-IGH5G-%6%2%%87%-49-;G% VPPXVPPXVPP\ X<br>5(6G$*37(*$()F83("37(,*+9:F4(I(" 1212!+GGH-#..GI00HG*304%2I%FG0HG55@2I%FG0H!"#$%FGG()%*VPP\ X X 121212!+GGH-#..GI00HG*C5G.@255865892I%FG0H2H-I-F09H0%)C5G.@2%-84%2I%FG0H2H-I-F09H0%)304%2I%FG0H2H-I-F09H0%) 5(6G$*3*+F+6$-*$() !"#$%FGG()%* VPP\ VPPX 12121212!+GGH-#..GI00HG*C5G.@25586589254@-8-IGH5G-%6%2%%87%-4C5G.@2%-84%254@-8-IGH5G-%6%2%%87%-4D84-F5G-%2#J0??54%254@-8-IGH5G-%6%2%%87%-4D84-F5G-%2854%H2084%HA0%?25H#%-4I6%HJ%4%89%9%6%8I254@-8-IGH5G-%6%2%%87%-4 ?,%+"+FG*.G+(I(3(("0(+, !"#$%FGG()%* VPP\VPP\ X VPP\ =%-G%J-$?254H%I254@-8-IGH5G-%6%2%%87%-430HH%I)084%8G-%54H%I254@-8-IGH5G-%6%2%%87%-4VPP\ VPP\ VPP\XPP\ 12!+GGH-#..GI00HG*C5G.@25586589254H%I ?,*(F0$1,+"- !"#$%FGG()%*X<br>12 S0087%;;-89%88.@@%H VPP\ VPP\ 12 C5G.@2%-84%254H%I<br>VPPX 12 G55@254@-8-IGH5G-%6%2%%87%-4 !"#$%FGG()%* !"#$%FGG()%* 12 [0%J-F7G-892H%4%825;N-$?%842NRQM54H%I<br>VPPX 12 +58IJ.-G-89I8.@@%H2NB A+-("*+F+6$,*.-(* 5B8C(G<br>!"#$%FGG()%*<br>F(%$(,F7(NC..*,0(+, VPP\ VPPX X VPP\ !+GGH-#..GI00HG* X X !+GGH-#..GI00HG*<br>12 C5G.@255865892%-9%8H-I-F04H59%H 12 304%2LLMN%G<br>12!+GGH-#..GI00HG*C5G.@2558658929%@0%4I#%AN55H47%-4 VPP\ X 12 C5G.@2%-84%2%-9%8H-I-F04H59%H X X<br>12 C5G.@2%-84%29%@0%4I#%AN55H47%-4 X<br>VPP\ VPPX VPPX VPPX X VPPX X XPP\ 2*(%+()(*6("G.-(3+",+I+,1((4 !"#$%FGG()%*<br>!"#$%FGG()%*<br>1212!+GGH-#..GI00HG*304%25589-;G%;H%R.%8G-%254@-8-IGH5G-%6%2%%87%-4C5G.@2558658925589-;G%;H%R.%8G-%254@-8-IGH5G-%6%2%%87%-4 ?."-+:G(:*(H1("G+(3.,%+"+FG*.G+(I(3(("0(+, ")60J9%H 121212!+GGH-#..GI00HG*C5G.@255865892)H%@-%)%HF%8G59%2-84-6-4.%%JC5G.@2%-84%2)H%@-%)%HF%8G59%2-84-6-4.%%JQH%@-%)%HF%8G59%2-84-6-4.%%J<br>12 C5G.@2%-84%25589-;G%;H%R.%8G-%254@-8-IGH5G-%6%2%%87%-4 B00H9589%H<br>VPP\ VPP\ VPP\ VPP\ VPP\<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* !"#$%!&$''()"*+%,#(-../<br>G.+44+FF(%("G3F1*F(."6( ?:,*.60G)4+60G D$$*GN(GG+"-F*(4.G+( !"#$%FGG()%*<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG* @(60GF)(*F$$"<br>12 304%2;5-JJ-II%@%8G2I.HI%58F% 12 C5G.@2558658925;4H5F7G)J-F7G 12 C5G.@2600HGA%GG-89IH%J5G-% !+GGH-#..GI00HG*<br>121212 304%2H%4%82%-84%2;5-JJ-II%@%8G2I.HI%58F%C5G.@255865892;5-JJ-II%@%8G2I.HI%58F%2UVPPXYC5G.@2%-84%2;5-JJ-II%@%8G2I.HI%58F% 12 C5G.@2%-84%25;4H5F7G)J-F7G 1212 Q%HF%8G59%2J008I0@206%H9%95582-820)60J9%HS0087%;;-89%88.@@%H 121212 C5G.@20)H-F7G-892H%F7GI)%HI008"@IF7H-$6-892H%F7GI60H@2T584%JIH%9-IG%H"@IF7H-$6-892IG5G.I2H%F7GI)%HI008<br>12 G55@2H%F7GI)%HI008<br>12 "@IF7H-$6-892IG5G.G5-H%2A%G%J<br>12 304%2H%F7GI60H@<br>12 C5G.@255865892IG5G.G5-H%2A%G%J<br>**----- End of picture text -----**<br>


**Figuur 14. Ontsluiting gegevens uit Polisadministratie** 

## **4.10 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Rijksdienst voor het Wegverkeer (RDW)** 

In dit gegevensdeelmodel worden de gegevens die noodzakelijk zijn bij het uitvoeren van de vermogenstoets voor de Participatiewet en de fraudeonderzoeken van de sociale recherche weergegeven. Het gaat dan bijvoorbeeld om gegevens zoals het kenteken, de kenmerken, het eigenaarschap en de verzekeringsgegevens van een voertuig. 

**==> picture [453 x 567] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%*<br>;3#0"A0%(&$33#2"J4()*#12@($0*1*#1<br>!+GGH-#..GI00HG*<br>12 S-67-?-F47G2;%%92=472;%24F:G%H7445<br>UVVP<br>P !"#$%FGG()%*<br>!"#$%FGG()%* !"#$%FGG()%* K0"#4""&420()(J33##>55(&<br>12121212!+GGH-#..GI00HG*34G.52447=4762:47;%9I744534G.52%-7;%2:47;%9I7445A47;%9I7445@0960H;% !"#$%FGG()%* 6"#4()$#""5 PVVX P 1212121212!+GGH-#..GI00HG*34G.52447=4762=%IG-6-7634G.52%-7;%2=%IG-6-76L7;-F4G-%20):%??-762=%IG-6-76@%IG-6-76I7.55%H2A47;%9IH%6-IG%H@%IG-6-76I=0967.55%H2B45%H2=472B00):47;%9 I($0*1*#123#4(&#(5*#1 UVVPUVVP F0HH%I)07;%7G-%4;H%I2=%IG-6-76N%H0%84;H%I2=%IG-6-76 PP !"#$%FGG()%*UVVP !4&($ UVVP UVVPPP +;H%I2=%HH%8%H-76I544GIF:4))-$2C3M+;H%I26%=0954F:G-6;%UVVP 1212!+GGH-#..GI00HG*F0;%2=%HH%8%H-76I544GIF:4))-$2C3MO4452=%HH%8%H-76I544GIF:4))-$2C3M I(&N(G(&*#1$5""0$A?"%%*+ PVVX P K%9%?0077.55%H2=%HH%8%H-76I544GIF:4))-$2C3MK%9%?0077.55%H26%=0954F:G-6;% UVVX 1212121212!+GGH-#..GI00HG*F0;%2G()%2G%9%?0077.55%HL7;-F4G-%26%:%-52G%9%?0077.55%HL7;-F4G-%2=00H8%.H2G%9%?0077.55%HK%9%?0072947;7.55%HK%9%?0077.55%H UVVP<br>UVVX 12 C3M2#%;H-$?I7.55%H UVVP UVVP PVVX<br>A47;%9G207;%H UVVP F0HH%I)07;%7G-%4;H%I F(@3)5"A?0*14( !"#$%FGG()%* P !"#$%FGG()%* I(&N(G(&*#1<br>P T%-G%9-$824;H%I<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>!"#$%FGG()%* 12 F0;%26%=0954F:G-6;% 12 F0;%2I00HG2;%88-76<br>7#4(&#(5*#189#$0())*#1 12 O44526%=0954F:G-6;% 12 34G.52447=4762=%HH%8%H-76<br>!+GGH-#..GI00HG* P 1212 34G.52%-7;%2=%HH%8%H-76I09-I7.55%H<br>12 N0%8$44H2;%)07%H-762$44HIG.8<br>12 F0;%2H%;%72-7IF:H-$=-76207;%H7%5-76G-7IG%99-76 !"#$%FGG()%* UVVP UVVP UVVP UVVP<br>12 F0;%2H%;%72.-GIF:H-$=-76207;%H7%5-76G-7IG%99-76 I*(02I"0>>&)*+G2:(&$33#<br>1212121212 F0;%2G()%207;%H7%5-76G-7IG%99-7634G.52447=476207;%H7%5-7634G.52%-7;%207;%H7%5-7634G.52-7IF:H-$=-76207;%H7%5-76G-7IG%99-76L7;-F4G-%2%F0705-IF:24FG-%? 121212!+GGH-#..GI00HG*34G.52447=4762O-%G2O4G..H9-$82I%HI00734G.52%-7;%2O-%G2O4G..H9-$82I%HI00734G.52.-GIF:H-$=-762O-%G2O4G..H9-$82I%HI007 12!+GGH-#..GI00HG*"5IF:H-$=-762.-G6%#H%-;%2H%F:GI=0H5 !"#$%FGG()%* :(&$33#<br>1212121212 L7;-F4G-%2?4-99-II%5%7G207;%H7%5-76G-7IG%99-76L7;-F4G-%20):%??-76207;%H7%5-76G-7IG%99-76L7;-F4G-%2I.HI%47F%207;%H7%5-76G-7IG%99-76"5IF:H-$=-762IG4G.G4-H%2H%G%9L7IF:H-$=-76I7.55%H2845%H2=472800):47;%9 1212121212 T-Q7.55%HC%F:GI)%HI07%72%72S45%7P%H8-76I=%H#47;%72L7?0H54G-%2O.55%H34G.52447=4762IG4G.G%734G.5248G%2IG4G.G%7O445 UVVP 6"#4()""&$G(#0(G(# !"#$%FGG()%*P<br>12 "5IF:H-$=-762H%F:GI=0H52A47;%9IH%6-IG%H !+GGH-#..GI00HG*<br>UVVP 12 B%7G%8%72=0%HG.-6<br>!"#$%FGG()%* UVVP P<br>I3(&0>*1@(&%)*A?0*#1(##(5(&<br>UVVX<br>UVVP<br>!"#$%FGG()%*<br>UVVP !"#$%&"G()*+G(H-. UVVX UVVP<br>UVVP UVVP<br>!+GGH-#..GI00HG* !"#$%FGG()%*<br>!"#$%FGG()%* !"#$%FGG()%* 12 34G.52H%6-IGH4G-%2447I)H48%9-$8:%-; K0"0>$2?"#4()""&$G(#0(G(#<br>H(A?0$%(&$33# I"0>>&)*+G2:(&$33# 12 K-$;2447=4762447I)H48%9-$8:%-;<br>12 34G.52%-7;%2447I)H48%9-$8:%-; !+GGH-#..GI00HG*<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* 12 34G.52447=4762)%-9)%H-0;%2447I)H48%9-$8:%-; 12 F0;%2IG4G.I2:47;%944HI8%7G%8%7<br>1212 34G.520)H-F:G-762H%F:GI)%HI007"5IF:H-$=-762H%F:GI=0H52A47;%9IH%6-IG%H 1212 +47;.-;-76274456%#H.-8+Q7.55%H UVVX 12 34G.52%-7;%2)%-9)%H-0;%2447I)H48%9-$8:%-; 12 34G.52H%6-IGH4G-%2IG4G.I2:47;%944HI8%7G%8%7<br>12 "5IF:H-$=-762IG4G.I2H%F:GI)%HI007 12 N.H6%HI%H=-F%7.55%H P<br>12 O4452H%F:GI)%HI007 12 F0;%2NCIQ6%6%=%7I26%:%-5<br>12 "5IF:H-$=-762IG4G.G4-H%2H%G%9 12 F0;%26%#00HG%6%5%%7G%<br>12 F0;%2H%F:GI=0H5 12 F0;%2IL@+Q6%6%=%7I26%:%-5<br>12 34G.52447=4762IG4G.G4-H%2H%G%9 12 L%#00HG%;4G.5<br>12 L%#00HG%947;<br>12 L%#00HG%)944GI<br>12 L%I94F:G<br>12 L;%7G-?-F4G-%7.55%H2IL@+<br>12 L7;-F4G-%2IG4HG8P49-?-F4G-%2=096%7I23R" UVVX P P P<br>12 "5IF:H-$=-762IG4G.I2O4G..H9-$82I%HI007<br>12 S-67-?-F47G2;%%92=472;%24F:G%H7445 !"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>12 @Q7.55%H I3(&0>*1 H($)"1 P -(>&G""&4(&<br>12 @00H745%7<br>12 @00H=0%6I%9 !+GGH-#..GI00HG* P UVVX !+GGH-#..GI00HG* UVVX P !+GGH-#..GI00HG*<br>12 L7;-F4G-%2:47;9-F:G-76 12 +47G492H-G)944GI%72=0%HG.-6 12 34G.52H%6-IGH4G-%2#%I946 12 O4452;%.HP44H;%H<br>12 @00H9%GG%HI 12 N%;H462NIJ 12 30II-%HC%?%H%7G-% 12 L;%7G-?-F4G-%7.55%H<br>!"#$%FGG()%* 12 N%;H462F4G4906.I2=0%HG.-6<br>D(>&*#1 12 NH%%;G%2=0%HG.-6<br>12 F4G%60H-%2OOLGOFO2=0%HG.-6<br>!+GGH-#..GI00HG* UVVX P 12 F4G%60H-%2OOLGOFO2=0%HG.-62G0%=0%6-76<br>!"#$%FGG()%* ;)*(#02K=.9 12 34G.52%-7;%26%9;-6:%-;2+IB 121212 F0;%2F94II-?-F4G-%2=0%HG.-6F0;%2I00HG2#H47;IG0?F0;%2I00HG2=0%HG.-6 I(&$0&(GG*#1$@33&C(?3>42@3(&0>*1 !"#$%FGG()%*<br>12121212121212!+GGH-#..GI00HG*N478H%8%7-767.55%HN.H6%H9-$8%2IG44GF0;%2947;2;0%96H0%)F0;%29%%?=0H534G.520=%H9-$;%7L7;-F4G-%20=%H9-$;%7+?7%5%HI-7;-F4G-%2NCI UVVP 1212121212!+GGH-#..GI00HG*F0;%2IG4G.I2=0%HG.-634G.52447=4762IG4G.I2=0%HG.-634G.52%-7;%2IG4G.I2=0%HG.-6@0H-628%7G%8%72=0%HG.-6@096%7;28%7G%8%72=0%HG.-6 K0"0>$2@3(&0>*1 !"#$%FGG()%* UVVX P 12121212121212121212 34G.52%%HIG%2-7IF:H-$=-762=0%HG.-62-7G%H74G-0744934G.52%%HIG%2-7IF:H-$=-762=0%HG.-6274G-07449A00?;89%.H2=0%HG.-6B%7G%8%72=0%HG.-6M%76G%2=0%HG.-6J4II429%%62=0%HG.-6J4N-5.5254II42=0%HG.-6J%H82=0%HG.-6J0G0HF0;%2=0%HG.-6O4452?4#H-847G2=0%HG.-6 P UVVP 12121212!+GGH-#..GI00HG*34G.52447=4762=%HIGH%88-76I=00H#%:0.;2=0%HG.-634G.52%-7;%2=%HIGH%88-76I=00H#%:0.;2=0%HG.-6K-$;IG-)2447=4762=%HIGH%88-76I=00H#%:0.;2=0%HG.-6K-$;IG-)2%-7;%2=%HIGH%88-76I=00H#%:0.;2=0%HG.-6<br>12 O%=%789%.H2=0%HG.-6<br>B())(&$0"#42@3(&0>*1 !"#$%FGG()%* 121212 I944GI250G0HF0;%2=0%HG.-6K()%2=0%HG.-6M-%9#4I-I2=0%HG.-6 I3(&0>*1@(&%)*A?0*#1(# !"#$%FGG()%*<br>!+GGH-#..GI00HG* P P 12 I%-9;4G.52447I)H48%9-$8:%-; !+GGH-#..GI00HG*<br>1212 F0;%2G%99%HIG47;%%7:%-;2=0%HG.-6K%99%HIG47;2=0%HG.-6 12 I%-9G-$;2447I)H48%9-$8:%-; P UVVX 1212 34G.52447=4762=0%HG.-6=%H)9-F:G-76%734G.52%-7;%2=0%HG.-6=%H)9-F:G-76%7<br>12 K-$;IG-)2447=4762=0%HG.-6=%H)9-F:G-76%7<br>12 K-$;IG-)2%-7;%2=0%HG.-6=%H)9-F:G-76%7<br>**----- End of picture text -----**<br>


**Figuur 15. Ontsluiting gegevens uit Rijksdienst voor het Wegverkeer** 

## **4.11 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Kadaster** 

In dit gegevensdeelmodel worden de gegevens uit het Kadaster, die noodzakelijk zijn bij het uitvoeren van de vermogenstoets voor de Participatiewet en de fraudeonderzoeken van de sociale recherche weergegeven. Het gaat bijvoorbeeld om gegevens over de eigendom van de cliënt in de vorm van een onroerende zaak en andere gegevens over een onroerende zaak, zoals de kadastrale aanduiding, zakelijk recht, aantekening kadastraal object, etc. 

**==> picture [453 x 561] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%*<br>01#"$+2"1"#(3&1 !"#$%FGG()%*<br>H*#33*31#"$<br>!"#$%FGG()%* !"#$%FGG()%*<br>G()"&*+H-.I 4&5"$*#67*6#""#1+31#"$+86)*"&(3&1 !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>!+GGH-#..GI00HG* OPPF OPPY !+GGH-#..GI00HG* 1212 =08%27%3%%6G%?-IGH-FG 1212 +J68.-8-672#-$24.-I6.33%HJ.-IK%GG%H<br>12 9J6;H%;%6-676.33%H 12 +8H%IH%7%K2F2#.-G%6KJ68 12 C%3%%6G%8%%K 12 J.-I6.33%H<br>121212 9.H7%HK-$;%2IGJJG=08%2KJ68280%K7H0%)=08%2K%%L50H3 121212 +8H%IH%7%K2G2#.-G%6KJ68+8H%IH%7%K2H2#.-G%6KJ68?JG.32JJ65J672J8H%I2#.-G%6KJ68 121212 C%3%%6G%6JJ3@8%6G-L-FJG-%F08%26.33%HJJ68.-8-67@8%6G-L-FJG-%F08%25%H#K-$L)KJJGI 121212 J.-I6.33%HG0%50%7-67OJJ320)%6#JH%2H.-3G%LGHJJG6JJ3<br>121212 ?JG.3205%HK-$8%6@68-FJG-%205%HK-$8%6+L6%3%HI-68-FJG-%29AB 121212 ?JG.325%HGH%;25J62%-KJ68DJ682J8H%I2#.-G%6KJ68DJ682IJJH6JJH25%HGH0;;%6 121212 D0FJG-%03IF4H-$5-67B0IGF08%N006)KJJGI6JJ3 1212 N006#00G5%HI-$M-672NOPPFQN006IJ7%65%HI-$M-67<br>OPPF<br>OPPF !"#$%FGG()%*<br>>3K"()?K+#"7@*<br>!"#$%FGG()%*<br>9)5"&1%: !+GGH-#..GI00HG*<br>!"#$%FGG()%*<br>4&#%"#"&1"+;33K 12 ?JG.32%-68%2MJ;%K-$;2H%F4G<br>OPPF OPPY 12 "3IF4H-$5-672MJ;%K-$;2H%F4G<br>OPPF OPPY !+GGH-#..GI00HG*<br>12 9%8HJ72;00)I03<br>12 =08%2G()%206H0%H%68%2MJJ; !"#$%FGG()%*<br>!"#$%FGG()%* 1212 @68-FJG-%23%%H27%H%F4G-78%6RJJH2JJ6;00) B.#K-%;H%F4G%K-$;%2#%)%H;-672G 03&*"K"&)&5+K313$*#33(+%8?"7*<br>!"#$%%& 12 "3IF4H-$5-672;J8JIGHJJK20#$%FG OPPF OPPY !+GGH-#..GI00HG*<br>12!+GGH-#..GI00HG*"3IF4H-$5-672.-G7%#H%-8%2H%F4GI50H3 OPPF=0HH%I)068%6G-%J8H%IOPPF !"#$%FGG()%* 01#"$ OPPY 06H0%H%68%D0FJG-%MJJ; OPPF 1212 ?JG.32%-68%2JJ6G%;%6-672;J8JIGHJJK20#$%FG"3IF4H-$5-672JJ6G%;%6-672;J8JIGHJJK20#$%FG<br>OPPF OPPF OPPF<br>?03-F-K-%2J8H%I OPPF<br>OPPF OPPF<br>OPPF<br>B.#K-%;H%F4G%K-$;%2#%)%H;-672F<br>!"#$%FGG()%* !"#$%FGG()%*<br>23*66#()?K+!"#$%%& OPPY A"*#%KK"&<br>B"#$%%&C8"$*66#$%#533&<br>12!+GGH-#..GI00HG*+J68.-8-6726JJ37%#H.-; OPPF FPPY !"#$%FGG()%* OPPF<br>12 +U6.33%H !"#$%FGG()%* 2)"*+23*66#()?K+!"#$%%& OPPF<br>1212 9.H7%HI%H5-F%6.33%H=08%29ABU7%7%5%6I27%4%-3 H"#"7@*)51" !+GGH-#..GI00HG* OPPF<br>12 =08%27%#00HG%7%3%%6G% 12 ?JG.32JJ65J672O-%G2OJG..HK-$;2B%HI006 !"#$%FGG()%*<br>12 =08%2B@T+U7%7%5%6I27%4%-3 OPPF F F OPPF 12 ?JG.32%-68%2O-%G2OJG..HK-$;2B%HI006 D"7@*$B"#$%%&<br>12 C%#00HG%8JG.3 12 ?JG.32.-GIF4H-$5-672O-%G2OJG..HK-$;2B%HI006<br>12 C%#00HG%KJ68 12 X-U6.33%H !+GGH-#..GI00HG*<br>12 C%#00HG%)KJJGI 12 A%F4GI)%HI06%62%62LJ3%6I%H;-67I5%H#J68%62@6L0H3JG-%2O.33%H 12 ?JG.320)H-F4G-672H%F4GI)%HI006<br>12 C%IKJF4G 12 ?JG.32JJ65J672IGJG.G%6 12 "3IF4H-$5-672H%F4GI50H32JJ68%KIH%7-IG%H<br>12 @8%6G-L-FJG-%6.33%H2B@T+ 12 ?JG.32J;G%2IGJG.G%6 12 "3IF4H-$5-672IGJG.I2H%F4GI)%HI006<br>12 @68-FJG-%2IGJHG;IJK-L-FJG-%250K7%6I2?V" 12 OJJ3 12 OJJ32H%F4GI)%HI006<br>12 "3IF4H-$5-672IGJG.I2OJG..HK-$;2B%HI006 12 "3IF4H-$5-672IGJG.GJ-H%2M%G%K<br>12 L-76-L-FJ6G28%%K25J628%2JF4G%H6JJ3 12 =08%2H%F4GI50H3<br>12 TU6.33%H OPPF 12 ?JG.32JJ65J672IGJG.GJ-H%2M%G%K<br>12 T00H6J3%6<br>12 T00H50%7I%K !"#$%FGG()%* OPPF OPPF<br>12 @68-FJG-%24J68K-F4G-67 4&1"#&":)&5CI&$*"(()&5<br>12 T00HK%GG%HI<br>!+GGH-#..GI00HG*<br>12 90%;$JJH28%)06%H-672$JJHIG.;<br>1212 =08%2H%8%62-6IF4H-$5-672068%H6%3-67P-6IG%KK-67=08%2H%8%62.-GIF4H-$5-672068%H6%3-67P-6IG%KK-67 OPPF OPPF =313$*#3("+33&16)1)&5 !"#$%FGG()%*<br>121212 =08%2G()%2068%H6%3-67P-6IG%KK-67?JG.32JJ65J672068%H6%3-67?JG.32%-68%2068%H6%3-67 07*)"F"+@GB%*@""K !"#$%FGG()%* 12!+GGH-#..GI00HG*=08%2;J8JIGHJK%27%3%%6G%<br>!"#$%FGG()%* 12121212 ?JG.32-6IF4H-$5-672068%H6%3-67P-6IG%KK-67@68-FJG-%2%F0603-IF42JFG-%L@68-FJG-%2LJ-KK-II%3%6G2068%H6%3-67P-6IG%KK-67@68-FJG-%20)4%LL-672068%H6%3-67P-6IG%KK-67 1212!+GGH-#..GI00HG*@68-FJG-%2JFG-%5%24()0G4%%;?JG.32JJ65J6724()0G4%%; 12121212 SJ8JIGHJJK2)%HF%%K6.33%HSJ8JIGHJK%27%3%%6G%6JJ3SJ8JIGHJK%2I%FG-%T0K76.33%H2SJ8JIGHJJK2J))JHG%3%6GIH%F4G2NOPPFQ<br>N3&1"($&33: 12 @68-FJG-%2I.HI%J6F%2068%H6%3-67P-6IG%KK-67<br>12 "3IF4H-$5-672IGJG.GJ-H%2M%G%K<br>!+GGH-#..GI00HG* JJ68%KG2068%H 12 @6IF4H-$5-67I6.33%H2;J3%H25J62;00)4J68%K<br>12 ?JG.32JJ65J6724J68%KI6JJ3 12 "3IF4H-$5-672H%F4GI50H32JJ68%KIH%7-IG%H<br>12 ?JG.32%-68%24J68%KI6JJ3 OPPY F<br>12 JJ68%KI6JJ3<br>12 T0K70H8%<br>**----- End of picture text -----**<br>


**Figuur 16. Ontsluiting gegevens uit Kadaster** 

## **4.12 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Basisregistratie Personen (BRP)** 

In dit gegevensdeelmodel worden de gegevens uit de Basisregistratie Personen (BRP) die noodzakelijk zijn bij de uitvoering van wettelijke taken door UWV, GSD, SVB en Nederlandse Arbeidsinspectie weergegeven. Het gaat om de gegevens over de natuurlijk persoon en de adresgegevens van de natuurlijk persoon die geregistreerd staan in de BRP. 

**==> picture [453 x 571] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%* 9+#**+*)#"$ 1)#"$.=")"#8*&) !"#$%FGG()%* !"#$%FGG()%* H-)"#.I<br>1212121212121212!+GGH-#..GI00HG*+:68.-8-672#-$24.-I6.33%HF.-I<%GG%HF.-I6.33%HF.-I6.33%HG0%50%7-67G::320)%6#:H%2H.-3G%HGH::G6::3N006#00G5%HI-$J-672OLMMNON006I:7%65%HI-$J-67 121212121212121212!+GGH-#..GI00HG*?08%27%3%%6G%=-IGH-FGC%3%%6G%8%%<C%3%%6G%6::398%6G-L-F:G-%F08%26.33%H::68.-8-6798%6G-L-F:G-%F08%25%H#<-$L)<::GID0F:G-%03IF4H-$5-67B0IGF08%N006)<::GI6::3 LMMV LMMV!"#$%FGG()%* 1)#"$ LMMV LMMNLMMNLMMNLMMNP%-G%<-$;2:8H%I2#.-G%6<:68?0HH%I)068%6G-%:8H%I=03-F-<-%2:8H%I LMMNLMMNLMMN 12!+GGH-#..GI00HG*"3IF4H-$5-672.-G7%#H%-8%2H%F4GI50H3!"#$%FGG()%* !"#$%%& LMMN 1212!+GGH-#..GI00HG*!+GGH-#..GI00HG*=:G.32::65:672L:3-<-%H%F4G%<-$;%2#%GH%;;-67=:G.32::65:672L:3-<-%H%F4G%<-$;%2#%GH%;;-67!"#$%FGG()%* H-)"#.0<br>LMMN<br>!"#$%FGG()%* !"#$%FGG()%*<br>!"#$%FGG()%* =*+--#8(?H.!"#$%%& G(&)<br>H&2"$+#-L+-#""#).*)#"$.L-(+"&8*&)<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12!+GGH-#..GI00HG*+8H%IH%7%<2N2#.-G%6<:68 =03-F-<-%2:8H%I 1212 +:68.-8-6726::37%#H.-;+P6.33%H 12 968-F:G-%2;-68%H#-$I<:7<br>121212121212 +8H%IH%7%<2R2#.-G%6<:68+8H%IH%7%<2S2#.-G%6<:68=:G.32::65:672:8H%I2#.-G%6<:68=:G.325%HGH%;25:62%-<:68D:682:8H%I2#.-G%6<:68D:682I::H6::H25%HGH0;;%6 LMMV 121212121212 @.H7%HI%H5-F%6.33%H?08%2@ABP7%7%5%6I27%4%-3?08%27%#00HG%7%3%%6G%?08%2B9T+P7%7%5%6I27%4%-3C%#00HG%8:G.3C%#00HG%<:68 LMMVLMMV H@"#(2".(&G%&"&)" !"#$%FGG()%*<br>12 C%#00HG%)<::GI<br>12 C%I<:F4G !+GGH-#..GI00HG*<br>LMMV !"#$%FGG()%* A"#L8(?3J8**+$ LMMVLMMVLMMV ?0HH%IP%-G%<-$;+8H%I@.-G%6<:68)068%6G-%:8H%I 1212121212 98%6G-L-F:G-%6.33%H2B9T+968-F:G-%2IG:HG;I:<-L-F:G-%250<7%6I2=U""3IF4H-$5-672IG:G.I2G:G..H<-$;2B%HI006H-76-L-F:6G28%%<25:628%2:F4G%H6::3TP6.33%H LMMV LMMV12 !"#$%FGG()%*=:G.32::65:672L:3-<-%H%F4G%<-$;%2#%GH%;;-67<br>1*&2(3+".*)#"$4%-)(&2.!KA1 !"#$%FGG()%* LMMN LMMV LMMV LMMV LMMN 121212 T00H6:3%6T00H50%7I%<968-F:G-%24:68<-F4G-67 N LMMN !*#+&"# N<br>12!+GGH-#..GI00HG*?08%2%-<:6825:62-6IF4H-$5-67 LMMN 12 T00H<%GG%HI LMMN LMMV<br>1212 =:G.32::65:672:8H%I40.8-672B9T+=:G.325:62-6IF4H-$5-6720)2%-<:68 1*&2(3+".*)#"$4%-)(&2.56! !"#$%FGG()%* N LMMN<br>LMMV 12!+GGH-#..GI00HG*?08%2::67-LG%2:8H%I40.8-672@AB LMMN LMMN F-G"8(?HI2"#"2($+#""#).J*#+&"#$L4*J !"#$%FGG()%*<br>12 ?08%27%3%%6G%25:62-6IF4H-$5-67 LMMN !+GGH-#..GI00HG*<br>1212 =:G.32::65:672:8H%I40.8-672@AB=:G.325:62-6IF4H-$5-672#-$27%3%%6G% LMMN LMMN LMMV 121212 ?08%27%3%%6G%24.I%<-$;II<.-G-67Q::67::627%H%7-IGH%%H82):HG6%HIF4:)?08%27%3%%6G%206G#-68-6724.I%<-$;Q7%H%7-IGH%%H82):HG6%HIF4:)?08%2H%8%6206G#-68-6724.I%<-$;Q7%H%7-IGH%%H82):HG6%HIF4:)<br>12 ?08%2I00HG25%H#-6G%6-I<br>6"($)%L-C"&+ !"#$%FGG()%* LMMN 121212 =:G.324.I%<-$;II<.-G-67Q::67::627%H%7-IGH%%H82):HG6%HIF4:)=:G.3206G#-68-6724.I%<-$;Q7%H%7-IGH%%H82):HG6%HIF4:)D:6824.I%<-$;II<.-G-67Q::67::627%H%7-IGH%%H82):HG6%HIF4:)<br>!+GGH-#..GI00HG* 12 D:68206G#-68-6724.I%<-$;Q7%H%7-IGH%%H82):HG6%HIF4:)<br>1212 ?08%2#%J-G2#.-G%6<:68I2H%-I80F.3%6G?08%2-640.8-6728:62I%<25%H3-II-672G%8%H<:68I2H%-I80F.3%6G N 1212 B<::GI24.I%<-$;II<.-G-67Q::67::627%H%7-IGH%%H82):HG6%HIF4:)B<::GI206G#-68-6724.I%<-$;Q7%H%7-IGH%%H82):HG6%HIF4:)<br>12 ?08%2I-76::<26-%G25%HIGH%;;%62G%8%H<:68I2H%-I80F.3%6G<br>12 ?08%2I00HG2G%8%H<:68I2H%-I80F.3%6G<br>12 =:G.32%-68%27%<8-74%-82G%8%H<:68I2H%-I80F.3%6G<br>121212 =:G.32-640.8-6728:62I%<25%H3-II-672G%8%H<:68I2H%-I80F.3%6G=:G.32.-G7-LG%2G%8%H<:68I2H%-I80F.3%6GG.33%H2G%8%H<:68I2H%-I80F.3%6G LMMN !"#$%FGG()%* 78("&+.9:;K LMMN !"#$%FGG()%* =*+(%&*8(+"(+<br>LMMV !+GGH-#..GI00HG*<br>LMMN !+GGH-#..GI00HG* LMMN 12 ?08%2#-$J068%H2G%8%H<:68%HIF4:)<br>12 @:6;H%;%6-676.33%H LMMV 12 ?08%26:G-06:<-G%-G<br>12 @.H7%H<-$;%2IG::G 12 ?08%2H%8%625%H;H-$7-672G%8%H<:68I%26:G-06:<-G%-G<br>!"#$%FGG()%* 1212 ?08%2<:68280%<7H0%)?08%2<%%L50H3 N 1212 ?08%2H%8%625%H<-%I2G%8%H<:68I%26:G-06:<-G%-G=:G.32::65:6726:G-06:<-G%-G<br>M"2(+(C*+("L"G(?$ 12 =:G.3205%H<-$8%6 12 =:G.32%-68%26:G-06:<-G%-G<br>12 968-F:G-%205%H<-$8%6<br>!+GGH-#..GI00HG* 12 +L6%3%HI-68-F:G-%2@AB<br>1212 ?08%2I00HG2<%7-G-3:G-%#%I-$I=:G.32%-68%27%<8-74%-82<%7-G-3:G-%#%I-$I LMMN N N !"#$%FGG()%*<br>12 G.33%H2<%7-G-3:G-%#%I-$I O(+-8*+--#<br>N LMMV !+GGH-#..GI00HG*<br>LMMN 12 ?08%2:8%<<-$;%2G-G%<Q)H%8-;::G<br>!"#$%FGG()%*<br>KCC(2#*+(" N<br>LMMN 12!+GGH-#..GI00HG*=:G.325%IG-7-672-62G%8%H<:68 LMMV LMMN LMMN !"#$%FGG()%* H@"#8(?)"&<br>12 =:G.325%IG-7-6720)2%-<:68<br>12 D:6825:6I::H2-67%IF4H%5%6 !+GGH-#..GI00HG*<br>12 ?08%27%3%%6G%205%H<-$8%6<br>12 =:G.3205%H<-$8%6<br>K&$L4#(?@(&2$2"2"@"&$.56! !"#$%FGG()%* LMMN LMMN N LMMN LMMN 1212 D:68205%H<-$8%6B<::GI205%H<-$8%6<br>!+GGH-#..GI00HG*<br>12 ?08%27%3%%6G%2I::H2B%HI006I;::HG2J-F42#%5-68G<br>12 ?08%2B%HI006I;::HG250<<%8-727%F065%HG%%H8 LMMN<br>12 ?08%2H%8%620)IF40HG-672#-$40.8-672B%HI006I<-$IG<br>12 =:G.32%%HIG%2-6IF4H-$5-672@AB<br>12 =:G.320)IF40HG-672#-$40.8-672B%HI006I<-$IG LMMN LMMN LMMV<br>LMMN LMMN !"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>A"#L8(?3$+(+"8 D"N*2$@"#4%-)(&2 K&$L4#(?@(&2$2"2"@"&$.!KA1<br>LMMV LMMV !+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 ?08%25%H#<-$LIG-G%< 12 ?08%27%J:723-68%H$:H-7% 12 ?08%2%-<:682I::H2C%J-6I;::HG2J-F42#%5-68G<br>!"#$%FGG()%* !"#$%FGG()%* 12 =:G.32::65:6725%H#<-$LIG-G%< 12 968-F:G-%2F.H:G%<%IG%<<-67 12 ?08%2C%J-6I;::HG250<<%8-727%F065%HG%%H8<br>A"#(3(L*+(".6=K 6=KB)""8&"C"# 12 =:G.32%-68%25%H#<-$LIG-G%< 12 =:G.320)IF40HG-672#-$40.8-672B%HI006I<-$IG<br>12 ?08%2H%8%620)IF40HG-672#-$40.8-672B%HI006I<-$IG<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 =:G.325%H-L-F:G-%2AG9 12 ?08%2AG9P8%%<6%3%H<br>12 "3IF4H-$5-6725%H-L-F:G-%2AG9 12 "3IF4H-$5-6725%H8H:72AG9P8%%<6%3%H<br>**----- End of picture text -----**<br>


**Figuur 17. Ontsluiting gegevens uit Basisregistratie Personen (BRP)** 

**==> picture [428 x 668] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%%& !"#$%&GG()%*<br>9:0IG":.I0$I0<br>!"#$%&GG()%* MNNO MNNP<br>9:077%.I;()<$%HGG" !+GG,-#..GI00,G*<br>!+GG,-#..GI00,G* F7G$.I;(H*$%$*IH0%$$%#)B:%0"$%H6>:B !"#$%&GG()%* 1212 L05%2#-$7045%,2N%5%,=345%,I&C3)L05%243G-043=-G%-G<br>1212 +345.-5-462433:6%#,.-8+F4.::%, !+GG,-#..GI00,G* MNNP 1212 L05%2,%5%42;%,8,-$6-462N%5%,=345I%243G-043=-G%-GL05%2,%5%42;%,=-%I2N%5%,=345I%243G-043=-G%-G<br>1212 <.,6%,I%,;-&%4.::%,L05%2<ABF6%6%;%4I26%C%-: 1212 L05%26%:%%4G%2C.D%=-$8II=.-G-46O334633426%,%6-IG,%%,52)3,G4%,I&C3)L05%26%:%%4G%204G#-45-462C.D%=-$8O6%,%6-IG,%%,52)3,G4%,I&C3) 1212 93G.:2334;346243G-043=-G%-G93G.:2%-45%243G-043=-G%-G MNNP<br>12 L05%26%#00,G%6%:%%4G% 12 L05%2,%5%4204G#-45-462C.D%=-$8O6%,%6-IG,%%,52)3,G4%,I&C3)<br>12 L05%2B@G+F6%6%;%4I26%C%-: 12 L05%2I00,G2;%,#-4G%4-I MNNP MNNP<br>12 H%#00,G%53G.: 12 93G.:2C.D%=-$8II=.-G-46O334633426%,%6-IG,%%,52)3,G4%,I&C3)<br>1212 H%#00,G%=345H%#00,G%)=33GI MNNO MNNP 1212 93G.:204G#-45-462C.D%=-$8O6%,%6-IG,%%,52)3,G4%,I&C3)L3452C.D%=-$8II=.-G-46O334633426%,%6-IG,%%,52)3,G4%,I&C3) !"#$%&G$()*$*$+$"H !"#$%&GG()%*<br>1212 H%I=3&CG@5%4G-?-&3G-%4.::%,2B@G+ 1212 L345204G#-45-462C.D%=-$8O6%,%6-IG,%%,52)3,G4%,I&C3)B=33GI2C.D%=-$8II=.-G-46O334633426%,%6-IG,%%,52)3,G4%,I&C3) MNNO MNNO !+GG,-#..GI00,G* MNNO<br>12 @45-&3G-%2IG3,G8D3=-?-&3G-%2;0=6%4I29I" 12 B=33GI204G#-45-462C.D%=-$8O6%,%6-IG,%%,52)3,G4%,I&C3) 12 +345.-5-462045%,70%8 !"#$%&GG()%*<br>12 ":I&C,-$;-462IG3G.I2N3G..,=-$82B%,I004 12 93G.:2334;3462045%,70%8 5$IH#G678$"0<br>12 J-64-?-&34G25%%=2;3425%23&CG%,433: MNNP MNNP MNNP 12 93G.:2%-45%2045%,70%8<br>12 GF4.::%, !+GG,-#..GI00,G*<br>12 G00,43:%4 MNNO 12 L05%2#%7-G2#.-G%4=345I2,%-I50&.:%4G<br>12 G00,;0%6I%= MNNP MNNO 12 L05%2-4C0.5-4625342D%=2;%,:-II-462N%5%,=345I2,%-I50&.:%4G<br>12 @45-&3G-%2C345=-&CG-46 MNNP 12 L05%2I-6433=24-%G2;%,IG,%88%42N%5%,=345I2,%-I50&.:%4G<br>12 G00,=%GG%,I MNNO MNNO MNNO 1212 L05%2I00,G2N%5%,=345I2,%-I50&.:%4G93G.:2%-45%26%=5-6C%-52N%5%,=345I2,%-I50&.:%4G<br>MNNO MNNP 12 93G.:2-4C0.5-4625342D%=2;%,:-II-462N%5%,=345I2,%-I50&.:%4G<br>12 93G.:2.-G6-?G%2N%5%,=345I2,%-I50&.:%4G<br>ONNP 12 N.::%,2N%5%,=345I2,%-I50&.:%4G<br>MNNO<br>MNNP<br>MNNP<br>O MNNO MNNO<br>MNNP<br>MNNO<br>!"#$%&GG()%*<br>!"#$%&GG()%* MNNO =$.#I*>$I#)*$*$+$"H<br>-.I$"0)1234 !+GG,-#..GI00,G* MNNO !"#$%&GG()%*<br>!+GG,-#..GI00,G* 12 93G.:26%=5-6C%-526%6%;%4I MNNO ?$%@.I;AH0I0$.<br>12 <348,%8%4-464.::%,<br>1212 <.,6%,=-$8%2IG33GL05%2=345250%=6,0%) MNNO MNNO 12!+GG,-#..GI00,G*L05%2;%,#=-$?IG-G%=<br>12 L05%2=%%?;0,: MNNO MNNO 12 93G.:2334;3462;%,#=-$?IG-G%=<br>12 93G.:20;%,=-$5%4 MNNO 12 93G.:2%-45%2;%,#=-$?IG-G%=<br>12 @45-&3G-%20;%,=-$5%4<br>12 +?4%:%,I-45-&3G-%2<AB<br>O MNNO MNNO MNNO<br>MNNP<br>MNNO MNNO<br>MNNP MNNP !"#$%&GG()%*<br>!";7IH0)*$*$+$" MNNO<br>!"#$%&GG()%* MNNO<br>?$%@.I;AB.::0H !+GG,-#..GI00,G*<br>MNNP MNNP MNNO 12 L05%204$.-IG2IG,-$5-62:%G20)%4#3,%20,5%<br>MNNO<br>MNNO MNNO<br>!"#$%&GG()%*<br>!+$%.I;#$" MNNO<br>!+GG,-#..GI00,G* MNNO<br>12 L05%26%:%%4G%20;%,=-$5%4 !"#$%&GG()%* MNNO !"#$%&GG()%*<br>12 93G.:20;%,=-$5%4 C#8I"IH0%:0I$+$)*$*$+$"H)D5< MNNO !B":8$)*$*$+$"H)D5<<br>12 L34520;%,=-$5%4 MNNO MNNO MNNO<br>12 B=33GI20;%,=-$5%4 !+GG,-#..GI00,G*<br>MNNO MNNO 12 93G.:20)43:%26%6%;%4I2<AB<br>MNNO MNNO MNNO<br>MNNO MNNO<br>!"#$%&GG()%* MNNO MNNO<br>=$&:*H+$%>G7#I"* MNNO<br>MNNO<br>!+GG,-#..GI00,G* MNNO MNNO MNNO<br>12 L05%26%7362:-45%,$3,-6%<br>12 @45-&3G-%2&.,3G%=%IG%==-46 MNNO<br>MNNO MNNO<br>!"#$%&GG()%* !"#$%&GG()%*<br>C(0$ NG678$"0I"#I6:0I$<br>!+GG,-#..GI00,G* MNNO !+GG,-#..GI00,G*<br>12 L05%2,%6-IG%,6%:%%4G%238G% 12 L05%2334;.==%45250&.:%4G<br>12 +8G%4.::%, !"#$%&GG()%*<br>D%G"#G678$"0<br>!+GG,-#..GI00,G*<br>12 L05%26%:%%4G%2#,0450&.:%4G<br>12 ":I&C,-$;-462#,0450&.:%4G<br>12 93G.:2#,0450&.:%4G<br>**----- End of picture text -----**<br>


**Figuur 18. Ontsluiting gegevens uit Basisregistratie Personen (BRP): administratieve gegevens** 

## **4.13 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Dienst Uitvoering Onderwijs (DUO)** 

In dit gegevensdeelmodel worden de gegevens uit Dienst Uitvoering Onderwijs (DUO) die noodzakelijk zijn bij de uitvoering van wettelijke taken door UWV en GSD weergegeven. Het gaat om de gegevens over de natuurlijk persoon en de opleidingsgegevens (deelname en resultaat) die geregistreerd staan bij DUO. 

**==> picture [453 x 538] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>'"#*)B)C22*<br>!"#$%%& 0"$1(*22*+%3(")4)&5+5"#"5)$*#""#4+6-7 0"$1(*22*+"829"&<br>!+GG,-#..GI00,G*<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>RSST O RSSO RSSO 12 =08%2),07,J33J<br>12 "3I&4,-$5-672.-G7%#,%-8%2,%&4GI50,3 12 =08%2LJI%20)<%-8-672?C" 12 =08%2,%I.<GJJG2%NJ3%6<br>12 =08%2%NJ3%6068%,8%%<<br>12 =08%2I00,G2DJJ,8%80&.3%6G 12 ?JG.32,%I.<GJJG2%NJ3%6<br>12 =08%2,%I.<GJJG2%NJ3%6068%,8%%<<br>12 FJJ,2JL7%<%782%NJ3%6<br>RSST O !"#$%&GG()%* 12 J&0,%2%NJ3%6068%,8%%<<br>I&A%14+%3(")4)&5+<%(5"&$+6-7<br>RSSO<br>!+GG,-#..GI00,G*<br>!"#$%&GG()%* 12 =08%26-5%J.20)<%-8-672?C"<br>!"#$%&GG()%* >0I? 12 =08%20)<%-8-672?C"<br>O<br>?2*11#();=+!"#$%%& 12 =08%20)<%-8-67IG%<I%<2?C"<br>!+GG,-#..GI00,G* RSSO 12 GJJ320)<%-8-672?C"<br>!"#$%&GG()%*<br>!+GG,-#..GI00,G* 12 9A@GH6.33%, 12 GJJ320)<%-8-672?C"2-6G%,6JG-06JJ<<br>'()"&*+,-.I<br>12 +J68.-8-6726JJ37%#,.-; 12 GJJ320)<%-8-672;0,G2?C"<br>12 +H6.33%, RSSO 12 "3I&4,-$5-672IG.8-%7%#-%8<br>!+GG,-#..GI00,G*<br>12 9.,7%,I%,5-&%6.33%, 12 "3I&4,-$5-672IG.8-%H-640.8<br>12 9J6;,%;%6-676.33%, RSST !"#$%&GG()%*<br>12 =08%29ABH7%7%5%6I27%4%-3 12 "3I&4,-$5-672IG.8-%H.-GIG,003<br>12 =08%27%#00,G%7%3%%6G% 12 9.,7%,<-$;%2IGJJG 6""(&29"+%3(")4)&5+5"#"5)$*#""#4+@);+6-7 O O<br>12 =08%2B@N+H7%7%5%6I27%4%-3 12 =08%2<J68280%<7,0%) !"#$%&GG()%* O<br>12 =08%2<%%L50,3 7&4"#:);$%<"#""&=%9$* !+GG,-#..GI00,G*<br>12 Q%#00,G%8JG.3<br>12 ?JG.3205%,<-$8%6 12 +J68.-8-672<%%,$JJ,<br>12 Q%#00,G%<J68<br>12 Q%#00,G%)<JJGI 1212 @68-&JG-%205%,<-$8%6+L6%3%,I-68-&JG-%29AB RSSO RSST 12!+GG,-#..GI00,G*?JG.32-6I&4,-$5-6720)<%-8-67 RSST RSSO 1212 =08%2-6I&4,-$5-67I50,3=08%2068%,D-$I50,3 RSSO<br>12 Q%I<J&4G<br>12 ?JG.32.-GI&4,-$5-6720)<%-8-67 12 ?JG.32JJ65J6728%%<6J3%20)<%-8-67<br>12 @8%6G-L-&JG-%6.33%,2B@N+ 12 ?JG.32%-68%28%%<6J3%20)<%-8-67 !"#$%&GG()%*<br>12 @68-&JG-%2IGJ,G;DJ<-L-&JG-%250<7%6I2?C" ,*14)"(2$*<br>12 =08%2I%%,D%723#0<br>12 "3I&4,-$5-672IGJG.I2GJG..,<-$;2B%,I006<br>12 J-76-L-&J6G28%%<25J628%2J&4G%,6JJ3 !"#$%&GG()%* O O !+GG,-#..GI00,G*<br>12 NH6.33%, ,*14)"B)&2&C)"#)&5 RSST RSST 12 JG.8-%<JIG2%%64%-8<br>12 N00,6J3%6 12 JG.8-%<JIG2ODJJ,G%<br>12 N00,50%7I%< O RSSO !+GG,-#..GI00,G* !"#$%&GG()%* !"#$%&GG()%*<br>12 @68-&JG-%24J68<-&4G-67 12 9%8,J72JJ65.<<%68%2#%.,I2IG.8-%L-6J6&-%,-67 I&A%14+<2= >"#%"3$3#2=*);=%<"#""&=%9$*<br>12 N00,<%GG%,I<br>12 9%8,J72JJ65.<<%68%2G0%<J7%2LM"J2N"OP<br>12 9%8,J72#JI-I#%.,I2IG.8-%L-6J6&-%,-67 !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 9%8,J72#JI-IG0%<J7%2LM"J2N"OP 12 "3I&4,-$5-6725J; 12 +J6GJ<2.,%62#%,0%)I),J;G-$;50,3-67<br>12 =08%2IGJG.I2%%6H0.8%,G0%I<J72IG.8-%L-6J6&-%,-67 12 =08%26-5%J.20)<%-8-672?C" 12 ?JG.32JLI<.-G%62#%,0%)I),J;G-$;05%,%%6;03IG<br>12 =08%2G0%;%66-672#JI-I#%.,I2IG.8-%L-6J6&-%,-67 12 ?JG.32JJ65J672#%,0%)I),J;G-$;50,3-67<br>12 ?JG.32JJ65J672G0%;%66-67I)%,-08%2IG.8-%L-6J6&-%,-67 12 ?JG.32%-68%2#%,0%)I),J;G-$;50,3-672D%,;%<-$;<br>12 ?JG.32%-68%2IG.8-%L-6J6&-%,-67 12 @?2<%%,#%8,-$L<br>12 ?JG.32%-68%2G0%;%66-67I)%,-08%2IG.8-%L-6J6&-%,-67 12 =08%20)<%-8-67I068%,8%%<<br>12 @68-&JG-%2JJ65.<<%68%2#%.,I2IG.8-%L-6J6&-%,-67 12 "3I&4,-$5-6720)<%-8-67I068%,8%%<<br>12 @68-&JG-%2,%&4G20)2IG.8-%L-6J6&-%,-67<br>12 @68-&JG-%2IG.8-%L-6J6&-%,-67<br>12 @68-&JG-%2G0%;%66-672LM"J2N"OP<br>**----- End of picture text -----**<br>


**Figuur 19. Ontsluiting gegevens uit Dienst Uitvoering Onderwijs** 

## **4.14 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit Belastingdienst** 

In dit gegevensdeelmodel worden de gegevens die ontsloten zijn bij de Belastingdienst weergegeven. Het gaat om de gegevens over inkomsten, vermogen op de bankrekening en heffingskortingen die noodzakelijk zijn voor de uitvoering van de wettelijke taken van GSD. 

**==> picture [452 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>!"#$%&GG()%*<br>8"99)&2$3%#*)&2<br>>;*??#()@3+!"#$%%& !"#$%&GG()%*<br>01"#)2"+)&3%4$*"&+5%46%&"&* !"#$%&GG()%*<br>!+GG,-#..GI00,G*<br>!+GG,-#..GI00,G* H)2&;;(+I&()5A*)&2"&=?#";?<br>12 9%8,J724%LL-67I;0,G-672.-G2500,<0)-7%2JJ6I<J7<br>12 +J68.-8-6726JJ37%#,.-; !"#$%&GG()%* !+GG,-#..GI00,G*<br>12 +I6.33%, '()"&*+H-.I 12 =08%2I00,G205%,-7%2-6;03IG%6 NOOP NOOQ 12 9%8,J72),%3-%4%LL-67250<;I5%,C%;%,-67 NOOP NOOP !+GG,-#..GI00,G*<br>12 9.,7%,I%,5-&%6.33%, NOOP NOOQ 12 "3I&4,-$5-67205%,-7%2-6;03IG%6 12 =08%2I00,G24%LL-67I;0,G-6729%<JIG-678-%6IG 12 =08%2IGJG.I2I-76JJ<<br>12 =08%29ABI7%7%5%6I27%4%-3 !+GG,-#..GI00,G* 12 =08%2I00,G2,%&4G20)24%LL-67I;0,G-67<br>12 =08%27%#00,G%7%3%%6G% 12 9J6;,%;%6-676.33%, 12 ?JG.32#%I&4-;;-672#%<JIG-678-%6IG<br>12 =08%2B@J+I7%7%5%6I27%4%-3 12 9.,7%,<-$;%2IGJJG<br>12 O%#00,G%8JG.3 12 =08%2<J68280%<7,0%)<br>12 O%#00,G%<J68 12 =08%2<%%L50,3<br>12 O%#00,G%)<JJGI 12 ?JG.3205%,<-$8%6 !"#$%&GG()%*<br>12 O%I<J&4G 12 @68-&JG-%205%,<-$8%6 :;&3#"3"&)&2<br>12 @8%6G-L-&JG-%6.33%,2B@J+ 12 +L6%3%,I-68-&JG-%29AB !"#$%&GG()%*<br>1212 @68-&JG-%2IGJ,G;LJ<-L-&JG-%250<7%6I2?M""3I&4,-$5-672IGJG.I2DJG..,<-$;2B%,I006 NOOP NOOQ 7"#4%2"&$5%46%&"&* !"#$%&GG()%* NOOP NOOQ 1212!+GG,-#..GI00,G*9J6;6JJ39J6;,%;%6-676.33%, NOOP NOOQ !+GG,-#..GI00,G* 0&*1;&2"&+#"&*"+=;&3#"3"&)&2<br>12 G-76-L-&J6G28%%<25J628%2J&4G%,6JJ3 12 9@= 12 9%8,J7206G5J67%62,%6G%2#J6;,%;%6-67<br>12 JI6.33%,<br>12 @9+D 12 HJJ,206G5J67%62,%6G%<br>12 J00,6J3%6<br>12 N%6JJ3IG%<<-67<br>12 J00,50%7I%< 12 FJ68%6&08%2@G"<br>12 @68-&JG-%24J68<-&4G-67<br>12 J00,<%GG%,I NOOP<br>NOOQ<br>!"#$%&GG()%*<br>H;(<%+=;&3#"3"&)&2<br>!"#$%&GG()%*<br>!"#$%%&<br>!+GG,-#..GI00,G*<br>12 9%8,J72IJ<802#J6;,%;%6-67<br>!+GG,-#..GI00,G*<br>12 ?JG.32,%;%6-67JLI&4,-LG<br>12 "3I&4,-$5-672.-G7%#,%-8%2,%&4GI50,3<br>**----- End of picture text -----**<br>


**Figuur 20. Ontsluiting gegevens uit Belastingdienst** 

## **4.15 Conceptueel gegevensdeelmodel Ontsluiting gegevens uit het Handelsregister (HR)** 

In dit gegevensdeelmodel worden de gegevens die ontsloten worden uit het Handelsregister (HR) weergegeven. Het gaat om de gegevens over de Niet Natuurlijk Persoon met de verschillende rechtsvormen, zoals rechtspersoon, samenwerkingsverband en eenmanszaak met meerdere eigenaren, maatschappelijke activiteiten, ondernemingen en de al dan niet commerciële vestigingen die noodzakelijk zijn voor de uitvoering van wettelijke taken van keten Werk en Inkomen. 

**==> picture [453 x 563] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>;H#+7%# =H+..#F)34';%#*""7 ;%#*""7 F)3B"78%#%'#%01+*+"%*+H78<br>STTU U 12!+GGH-#..GI00HG*+469.-9-68264458%#H.-= 12!+GGH-#..GI00HG*"5IFKH-$7-682.-G8%#H%-9%2H%FKGI70H5 U STTU 12!+GGH-#..GI00HG*A09%2H%9%62%-69%2-6I0;7%6G-% STTU<br>12 +F6.55%H 12 A09%2#-$M069%H%2H%FKGIG0%IG469<br>12 @.H8%HI%H7-F%6.55%H<br>12 A09%2@JHF8%8%7%6I28%K%-5 STTU U U U STTV<br>!"#$%FGG()%* 12 A09%28%#00HG%8%5%%6G%<br>65%#F)38%7 12 A09%2H:G+F8%8%7%6I28%K%-5 !"#$%FGG()%* !"#$%FGG()%*<br>12 M%#00HG%94G.5 ;%#*""7'#%01+*5"#$ -%2"7%#)7(<br>!+GGH-#..GI00HG* 12 M%#00HG%;469<br>12 A09%28%5%%6G%207%H;-$9%6 STTU U 12 M%#00HG%);44GI !+GGH-#..GI00HG* !+GGH-#..GI00HG* !"#$%FGG()%*<br>12 34G.5207%H;-$9%6 12 M%I;4FKG 12 "5IFKH-$7-682H%FKGI70H52N469%;IH%8-IG%H 12 :9%6G-C-F4G-%29%)0G @%01+*2%#*""7')7'"2#)01+)7(<br>1212 O469207%H;-$9%6H;44GI207%H;-$9%6 1212 :9%6G-C-F4G-%6.55%H2H:G+:69-F4G-%2IG4HG=L4;-C-F4G-%270;8%6I23N" 12 G0;;%9-8%26445 1212 A09%2IG4G.I29%)0GIG.=234G.529%)06%H-68 !+GGH-#..GI00HG* !"#$%FGG()%*<br>12 "5IFKH-$7-682IG4G.I2L4G..H;-$=2H%HI006 12 30%;2H%FKGI70H5 <"$$H78)+H)#'4H2)+HHF<br>121212 O-86-C-F46G29%%;274629%24FKG%H6445GF6.55%HG00H645%6 N%%CG24;I2%-8%644H =)%+'=H+..#F)34';%#*""7 !"#$%FGG()%* !"#$%FGG()%* 12!+GGH-#..GI00HG*A09%2F055469-G4-H2=4)-G44;<br>12 G00H70%8I%; !+GGH-#..GI00HG* CH$%7M%#4)7(*5%#NH78 U STTV 12 @%9H482F055469-G4-H2=4)-G44;<br>1212 :69-F4G-%2K469;-FKG-68G00H;%GG%HI U 12121212 34G.5244674682L-%G2L4G..H;-$=2H%HI00634G.52%-69%2L-%G2L4G..H;-$=2H%HI00634G.52.-GIFKH-$7-682L-%G2L4G..H;-$=2H%HI006I-F6.55%H 1212!+GGH-#..GI00HG*"5IFKH-$7-682IG4G.I2I45%6L%H=-68I7%H#469+46G4;2F055469-G4-H%27%660G%6 U STTU !"#$%FGG()%* -..#<br>!"#$%FGG()%* 12121212 J%FKGI)%HI06%62%62O45%6L%H=-68I7%H#469%62:6C0H54G-%2L.55%H34G.5244674682IG4G.G%634G.524=G%2IG4G.G%6L445 A%7$H7*BHH4'$%+'$%%#8%#% !"#$%FGG()%* %)(%7H#%7 1212!+GGH-#..GI00HG*34G.52%-69%29..H:69-F4G-%206#%)44;9%29..H<br>IHH+*01H22%F)34%'H0+)5)+%)+ !"#$%FGG()%*<br>!+GGH-#..GI00HG* F.)+%7FH78*%'5%77""+*01H2'(%(%5%7*<br>1212121212 34G.5244674682544GIFK4))%;-$=%24FG-7-G%-G34G.52%-69%2544GIFK4))%;-$=%24FG-7-G%-GL4452544GIFK4))%;-$=%24FG-7-G%-G:6IFKH-$7-68I6.55%H2?45%H27462?00)K469%;:69-F4G-%2-6F-9%6G%%;2.-G;%6%624H#%-9I=H4FKG%6 STTU 1212121212!+GGH-#..GI00HG*34G.520)H-FKG-682H%FKGI)%HI006"5IFKH-$7-682H%FKGI70H52N469%;IH%8-IG%H"5IFKH-$7-682IG4G.I2H%FKGI)%HI006L4452H%FKGI)%HI006"5IFKH-$7-682IG4G.G4-H%2M%G%; @%01+*2%#*""7 !"#$%FGG()%* STTU 678%#7%$)7(9:7*+%FF)7( !"#$%FGG()%*1212!+GGH-#..GI00HG*O469274620)H-FKG-68O469274627%IG-8-68 F.)+%7FH78*%'5%77""+*01H2 !"#$%FGG()%* UU F.)+%7FH78*%'#%()*+#H+)%'(%(%5%7* STTU!"#$%FGG()%* STTU 12121212121212!+GGH-#..GI00HG*:69-F4G-%2K00C97%IG-8-682-62#.-G%6;469"5IFKH-$7-682H%FKGI70H52#.-G%6;469R%G%;34G.524=G%20)H-FKG-6834G.52%%HIG%2-6IFKH-$7-682#.-G%6;46934G.52C0H5%%;2#.-G%6;469IA09%2H%FKGI70H52F4G%80H-%2#.-G%6;469STTU<br>12 A09%2H%FKGI70H5<br>12 34G.5244674682IG4G.G4-H%2M%G%; !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>U U STTU STTV STTV STTU 1212 @0%=$44H29%)06%H-682$44HIG.=A09%2H%9%62-6IFKH-$7-682069%H6%5-68B-6IG%;;-68 1212 @.-G%6;469I2-6IFKH-$C26.55%HO4692H%8-IGH4G-%<br>U 12 A09%2H%9%62.-GIFKH-$7-682069%H6%5-68B-6IG%;;-68 12 "5IFKH-$7-682#.-G%6;469I2H%8-IG%H<br>12 A09%2G()%2069%H6%5-68B-6IG%;;-68<br>STTU P46-C%IG%%HG2M-FK24;I 12 34G.5244674682069%H6%5-68 STTU<br>U U U STTU STTU STTU 1212 34G.52%-69%2069%H6%5-6834G.52-6IFKH-$7-682069%H6%5-68B-6IG%;;-68<br>12 :69-F4G-%2%F0605-IFK24FG-%C<br>12 :69-F4G-%2C4-;;-II%5%6G2069%H6%5-68B-6IG%;;-68<br>12 :69-F4G-%20)K%CC-682069%H6%5-68B-6IG%;;-68<br>H0IG;0F4G-% 12 :69-F4G-%2I.HI%46F%2069%H6%5-68B-6IG%;;-68<br>12 "5IFKH-$7-682IG4G.G4-H%2M%G%;<br>STTV X0H9G2.-G8%0%C%692-6 H0IG;0F4G-% @%M0%=;0F4G-% 1212 :6IFKH-$7-68I6.55%H2=45%H27462=00)K469%;"5IFKH-$7-682H%FKGI70H52N469%;IH%8-IG%H<br>!"#$%FGG()%* CF:LH0+)5)+%)+ STTU !"#$%FGG()%* @%M0%=;0F4G-% !"#$%FGG()%*<br>G0+)5)+%)+%7'7)%+'0"$$%#0)%F% STTU STTU J%#4BH$%'2%#*"7%7<br>12!+GGH-#..GI00HG*:69-F4G-%2K00C94FG-7-G%-G 5%*+)()7( X006;0F4G-% STTU STTU U U !+GGH-#..GI00HG*<br>12 "5IFKH-$7-682O@:FF09% !+GGH-#..GI00HG* 12 A09%2=;4II%2L%H=M45%2)%HI06%62G0G44;<br>12 O@:FF09% 12 "5IFKH-$7-6824FG-7-G%-G X0H9G28%;%-92746.-G X0H9G2.-G8%0%C%692-6 N469%;G2069%H 1212 H%-;94G.52L%H=M45%2)%HI06%6+46G4;2L%H=M45%2)%HI06%62G0G44;<br>STTV STTU 12 +46G4;2L%H=M45%2)%HI06%629%%;G-$9<br>12 +46G4;2L%H=M45%2)%HI06%6270;G-$9<br>U STTV STTU STTU STTU STTU STTU STTU STTU !"#$%F%'#%()*+#H+)% !"#$%FGG()%* STTUSTTU STTU<br>!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>=)%+L0"$$%#0)%F%'5%*+)()7( <"$$.7)0H+)%(%(%5%7* I"0H+)% !+GGH-#..GI00HG* STTU STTV<br>!+GGH-#..GI00HG* STTU !+GGH-#..GI00HG* 1212 34G.5244674682H%8-IGH4G-%34G.52%-69%2H%8-IGH4G-% !"#$%FGG()%*<br>12 L44526-%GFF055%HF-%;%27%IG-8-68 STTU 1212 :69-F4G-%24C8%IFK%H59Q0%70%8-68249H%I STTU STTU STTU !+GGH-#..GI00HG* HH78%F*7HH$<br>STTU STTU 12 34G.5244674682K469%;I6445<br>H0IG;0F4G-% 12 34G.52%-69%2K469%;I6445<br>12 N469%;I6445<br>@%M0%=;0F4G-% 12 G0;80H9%<br>STTU STTU STTV STTV STTV<br>!"#$%FGG()%* N469%;G2069%H<br>?%*+)()7( STTV :I2%%62.-G0%C%6-682746<br>!+GGH-#..GI00HG* STTV STTV<br>12 A09%2G()%27%IG-8-68 U<br>12 34G.52446746827%IG-8-68 !"#$%FGG()%*<br>!"#$%FGG()%* 12 34G.52%-69%27%IG-8-68 <"$$%#0)%F%'5%*+)()7(<br>G0+)5)+%)+%7'0"$$%#0)%F%'5%*+)()7( 12 G%IG-8-68I6.55%H<br>!+GGH-#..GI00HG* STTV STTV STTV<br>12 :69-F4G-%2-5)0HG%%HG O4 5%68%70%8925 %G<br>12 :69-F4G-%2%P)0HG%%HG<br>STTU U<br>**----- End of picture text -----**<br>


**Figuur 21. Ontsluiting gegevens uit het Handelsregister: maatschappelijke activiteit** 

**==> picture [450 x 275] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%* !"#$%&''()%*<br>!"#$%F'()(*)(+,-.-%(.-/F' 0%)2(1(*)(7".-)/-"(<br>!+'',-#..'I00,'* @AAB @AAB !+'',-#..'I00,'*<br>12 304%2,%4%52%-54%2-5I067%5'-% 12 ;:'.<2::57:5=2,%=-I',:'-%<br>12 304%2#-$8054%,%2,%&9'I'0%I':54 12 ;:'.<2%-54%2,%=-I',:'-%<br>!"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>3+,41'./F()"F7 34).(/F+(*5/F*6(-/1"F7 0/"11"..(2(F-<br>!+'',-#..'I00,'* !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 ?54-&:'-%2I&9.64I:5%,-5= 12 ;:'.<2::57:5=2I.,I%:5&% 12 ;:'.<2::57:5=2>:-66-II%<%5'<br>12 ;:'.<2%-54%2I.,I%:5&% 12 ;:'.<2%-54%2>:-66-II%<%5'<br>12 "<I&9,-$7-5=2,%4%52%-54%2I.,I%:5&% 12 ?54-&:'-%2>:-66-II%<%5'<br>12 "<I&9,-$7-5=2I':'.I2I.,I%:5&%27:52#%':6-5=<br>12 ;..,2I.,I%:5&%27:52#%':6-5=<br>12 ?54-&:'-%2-I27%,6%5=4<br>12 304%2I':'.I2-5I067%5'-%<br>**----- End of picture text -----**<br>


**Figuur 22. Ontsluiting gegevens uit het Handelsregister: bijzondere rechtstoestand** 

**==> picture [452 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%F''()%*<br>!"#$%"&'%(<br>!+'',-#..'I00,'*<br>12 34%5'-6-F7'-%24%)0'<br>12 804%2I'7'.I24%)0'I'.92<br>12 :7'.;24%)05%,-5<<br>!"#$%F''()%*<br>!"#$%F''()%* !"#$%F''()%* !"#$%%&<br>)**&&"+"%'%( NI-52<,0%)I$77,,%9%5-5<@0.4%,<br>)**&,-.+ 1%-2"33'%( !"#$%F''()%*<br>!+'',-#..'I00,'* 4'"-54*-..&6'7+58"&,$$%<br>!+'',-#..'I00,'* !+'',-#..'I00,'* HIIJ HIIJ<br>12 804%2=7I'I'%>>-5<<br>12 ?0%9$77, 12 804%2,%4%5205'@%66-5< !+'',-#..'I00,'*<br>12 :7'.;2775=75<2A-%'2A7'..,>-$92B%,I005<br>12 :7'.;2%-54%2A-%'2A7'..,>-$92B%,I005<br>12 :7'.;2.-'IF@,-$=-5<2A-%'2A7'..,>-$92B%,I005<br>12 C-D5.;;%,<br>!"#$%F''()%*<br>NI-52<,0%)I$77,,%9%5-5<@0.4%, 12 N%F@'I)%,I05%52%52F7;%5G%,9-5<I=%,#754%523560,;7'-%2A.;;%,<br>I%,-"00'%(<br>12 :7'.;2775=75<2I'7'.'%5<br>HIIJ HIIJ 12 :7'.;279'%2I'7'.'%5<br>12 A77;<br>**----- End of picture text -----**<br>


**Figuur 23. Ontsluiting gegevens uit het Handelsregister: deponering** 

**==> picture [454 x 318] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>?1%"")*F8;6:G)-44# D%HG%<%4?00H7-<%H2#%IG..H7%H2H%F>GI)%HI004 HG-%"")-."#$%FG K(G)F+G6."#$%F4#1)F- B1>F%11*<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 +847.-7-4<2488=<%#H.-@ MNNL L 12 907%2#%;0%<72=%G2847%H%2)%HI04%4 12 647-F8G-%28:?-$@%472884I)H8@%5-$@>%-7I#%7-4< L MNNL 12 A%7H8<2<%)588GIG2@8)-G885<br>12 +N4.==%H 12 907%2#%;0%<7>%-72#%IG..H7%H 12 907%2#%;0%<7>%-72:.4FG-048H-I2#.-G%45847I2H%F>G 12 A%7H8<2<%IG0HG2@8)-G885<br>12 A.H<%HI%H;-F%4.==%H 12 907%2=04-IG-IF>%2#%IG..H7%H 12 907%2#%;0%<7>%-72;%H%::%488H2;05<%4I2#.-G%45847I2H%F>G 12 A%7H8<2=88GIF>8))%5-$@2@8)-G885<br>12 907%2AFGN<%<%;%4I2<%>%-=<br>121212 907%2<%#00HG%<%=%%4G%907%2G6D+N<%<%;%4I2<%>%-=H%#00HG%78G.= :"7*FG;)G$2%G*F8;G6."#$%F4#1)F- !"#$%FGG()%* MNNL MNNL !"#$%FGG()%*<br>12 H%#00HG%5847 !+GGH-#..GI00HG* HG>G);%G6(4*01$2%<br>1212 H%#00HG%)588GIH%I58F>G 12 907%2#%;0%<7>%-7 !+GGH-#..GI00HG*<br>121212121212121212 67%4G-:-F8G-%4.==%H2G6D+647-F8G-%2IG8HG@?85-:-F8G-%2;05<%4I2CI""=IF>H-$;-4<2IG8G.I2J8G..H5-$@2G%HI004O-<4-:-F84G27%%52;8427%28F>G%H488=DN4.==%HD00H48=%4D00H;0%<I%5647-F8G-%2>8475-F>G-4<D00H5%GG%HI B%%:GMNNL B%%:G !+GGH-#..GI00HG* !"#$%FG(G)("**F#+ !"#$%FGG()%* !"#$%FGG()%* /G01$2%F+3G /G(4*01$2%F+3G51#3G*-)G+F-%G) !"#$%FGG()%*MNNL L MNNL 1212!+GGH-#..GI00HG*647-F8G-%2-I2IG8G.G8-H907%2G()%2;05=8F>G!"#$%FGG()%* =4*01$2% MNNL L L MNNL 12121212 A%7H8<2#%)%H@-4<2-42<%57647-F8G-%20)<8;%2B847%5IH%<-IG%H270%4647-F8G-%20;%H-<%2;05=8F>G"=IF>H-$;-4<20;%H-<%2;05=8F>G!"#$%FGG()%*MNNLL<br>B%%:G 1212 3.4FG-%G-G%5647-F8G-%2IG8G.G8-H%2G-G%5 MNNL HG>G);F#+6F#621#3G*F#+<br>12 907%2:.4FG-% !+GGH-#..GI00HG*<br>MNNO B%%:G2#%GH%@@-4<20) 1212 A%7H8<2#%)%H@-4<2-42<%57907%2I00HG2>847%5-4<<br>B%%:G<br>C00H<br>!"#$%FGG()%* MNNO<br>L L MNNO =G-%F+F#+<br>!"#$%FGG()%* :G)-44# LL 1212!+GGH-#..GI00HG*907%2G()%2;%IG-<-4<C8G.=2884;84<2;%IG-<-4< O8=%4<%;0%<72=%G<br>12!+GGH-#..GI00HG*"=IF>H-$;-4<2.-G<%#H%-7%2H%F>GI;0H= L L B%%:G B%%:G!"#$%FGG()%* MNNL !+GGH-#..GI00HG* @1#->)1;G*F8;G65A !"#$%FGG()%* MNNO 1212 C8G.=2%-47%2;%IG-<-4<D%IG-<-4<I4.==%H MNNO<br>L MNNL !"#$%F4#1)F-67F894#3G)G6)G$2%-%4G-%1#3 1212 907%2#%;0%<7>%-72884I)H8@%5-$@%2#-$2I8=%4?%H@-4<I;%H#847A%7H8<2#%)%H@-4<<br>!+GGH-#..GI00HG* 12 647-F8G-%20;%H-<%2#%)%H@-4< MNNL MNNL<br>MNNL 12 907%2#%;0%<7>%-72#%?-47;0%H7%H 12 647-F8G-%2>8475-F>G-4< !4)0G*G6)G+F-%)1%FG !"#$%FGG()%* MNNL<br>!"#$%FGG()%*<br>HG>G);F#+6F#6)G$2%-21#3G*F#+ !+GGH-#..GI00HG*<br>MNNL 12 C8G.=2884;84<2H%<-IGH8G-%<br>!+GGH-#..GI00HG* MNNL 12 C8G.=2%-47%2H%<-IGH8G-%<br>12 907%2#%)%H@-4<2-42H%F>GI>847%5-4<<br>**----- End of picture text -----**<br>


**Figuur 24. Ontsluiting gegevens uit het Handelsregister: functievervulling** 

**==> picture [452 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%%&<br>!"#$%&GG()%*<br>NOOP ()*'+ !"#$%&GG()%*<br>,$%--*.&/012'*+""3<br>NOOP !+GGH-#..GI00HG*<br>12 +645.-5-482466:8%#H.-=<br>NOOP NOOP 12 +>4.::%H<br>?%L0%=65H%I B0IG65H%I 12 ?.H8%HI%HK-&%4.::%H<br>12 @05%2?AB>8%8%K%4I28%9%-:<br>NOOQ NOOQ 12 @05%28%#00HG%8%:%%4G%<br>12 @05%2B3C+>8%8%K%4I28%9%-:<br>?%L0%=65H%I !"#$%&GG()%* !"#$%&' R004N0&6G-% 1212 D%#00HG%56G.:D%#00HG%N645<br>NOOP !+GGH-#..GI00HG* NOOP P 1212 D%#00HG%)N66GID%IN6&9G<br>12 345-&6G-%2678%I&9%H:5 12 35%4G-7-&6G-%4.::%H2B3C+<br>NOOP 12 ;0%K0%8-48265H%I NOOP 12 345-&6G-%2IG6HG=F6N-7-&6G-%2K0N8%4I2GH"<br>@0HH%I)045%4G-%65H%I NOOP NOOP NOOP 1212 ":I&9H-$K-482IG6G.I2I6G..HN-$=2B%HI004J-84-7-&64G25%%N2K6425%26&9G%H466:<br>12 C>4.::%H<br>12 C00H46:%4<br>?%L0%=N0&6G-%<br>12 C00HK0%8I%N<br>?%L0%=N0&6G-% ?%L0%=N0&6G-% 12 345-&6G-%29645N-&9G-48<br>12 C00HN%GG%HI<br>B0IGN0&6G-% B0IGN0&6G-% B0IGN0&6G-%<br>POOQ POOQ NOOP NOOP NOOQ NOOQ NOOQ NOOQ<br>!"#$%&GG()%* '(")*'+),,#-(./*!"#$%%& !"#$%&GG()%* NOOQ<br>7$$%+#5$66'.&/0'1$#%&8&%'&% !"#$%&GG()%* 9'+%&:&3:<br>4'#5%+6'*+""3<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* J6:%48%K0%852:%G<br>12 G6G.:2664K6482:66GI&96))%N-$=%26&G-K-G%-G !+GGH-#..GI00HG* 12 @05%2G()%2K%IG-8-48<br>12 G6G.:2%-45%2:66GI&96))%N-$=%26&G-K-G%-G 12 G6G.:20)H-&9G-482H%&9GI)%HI004 12 G6G.:2664K6482K%IG-8-48<br>1212 I66:2:66GI&96))%N-$=%26&G-K-G%-G34I&9H-$K-48I4.::%H2M6:%H2K642M00)9645%N 1212 ":I&9H-$K-482H%&9GIK0H:2O645%NIH%8-IG%H":I&9H-$K-482IG6G.I2H%&9GI)%HI004 1212 G6G.:2%-45%2K%IG-8-48C%IG-8-48I4.::%H NOOQ<br>12 345-&6G-%2-4&-5%4G%%N2.-GN%4%426H#%-5I=H6&9G%4 12 I66:2H%&9GI)%HI004<br>12 ":I&9H-$K-482IG6G.G6-H%2L%G%N<br>12 @05%2H%&9GIK0H:<br>12 G6G.:2664K6482IG6G.G6-H%2L%G%N<br>**----- End of picture text -----**<br>


**Figuur 25. Ontsluiting gegevens uit het Handelsregister: locatie** 

**==> picture [452 x 290] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%F''()%*<br>=,0;)*K"("2("#$%F%)"F%.*K<br>LMMN<br>12!+''H-#..'I00H'*?0;%2H%;%72%-7;%2-7I0<9%7'-% !"#$%%&<br>12 ?0;%2#-$>07;%H%2H%F6'I'0%I'47; 9,"%29.%33(I,012+"(F))* !"#$%F''()%* LMMN<br>12!+''H-#..'I00H'*34'.5244794782=-%'2=4'..H<-$@2D%HI007 !"#$%F''()%* 8*%4,*K,*6 L)(:"I"2("6,F%(.%," !"#$%F''()%*<br>12!+''H-#..'I00H'*34'.5244794782I4-<<-II%5%7'!"#$%F''()%* L.,II,FF":"*% LMMN N 1212121212 34'.52%-7;%2=-%'2=4'..H<-$@2D%HI00734'.52.-'IF6H-$9-782=-%'2=4'..H<-$@2D%HI007N-F7.55%HG%F6'I)%HI07%72%72H45%7B%H@-78I9%H#47;%72C7I0H54'-%2=.55%H34'.5244794782I'4'.'%7 N LMMN 1212!+''H-#..'I00H'*?0;%2447<%-;-78207'#-7;-78C7;-F4'-%2<-J.-;4'-% LMMN LMMN 1212!+''H-#..'I00H'*34'.5244794782H%8-I'H4'-%34'.52%-7;%2H%8-I'H4'-%<br>12 34'.52%-7;%2I4-<<-II%5%7' 12 34'.524@'%2I'4'.'%7<br>12 C7;-F4'-%2I4-<<-II%5%7' 12 =445<br>N<br>!"#$%F''()%*<br>7.',%..I LMMN 9..:I);"2-"**))%F#$.' !"#$%F''()%*<br>!+''H-#..'I00H'*<br>1212 A%;H4828%)<44'I'2@4)-'44<A%;H4828%I'0H'2@4)-'44< !"#$%F'"(F))* !"#$%F''()%* LMMN 12!+''H-#..'I00H'*C7;-F4'-%2#%<%88-78I544'IF64))-$25%'29%H47;%H<-$@2@4)-'44<<br>12 A%;H482544'IF64))%<-$@2@4)-'44< 12!+''H-#..'I00H'*34'.520)H-F6'-782H%F6'I)%HI007 +(,-..%("#$%"I,01"2("#$%F'"(F))* !"#$%F''()%* N<br>12!+''H-#..'I00H'*A%;H482@0I'%720)H-F6'-78!"#$%F''()%* 8'(,#$%,*6 121212121212 "5IF6H-$9-782H%F6'I90H52:47;%<IH%8-I'%H"5IF6H-$9-782I'4'.I2H%F6'I)%HI007=4452H%F6'I)%HI007"5IF6H-$9-782I'4'.'4-H%2>%'%<?0;%2H%F6'I90H534'.5244794782I'4'.'4-H%2>%'%< N LMMN 12!+''H-#..'I00H'*?0;%2I'H.F'..H N LMMN !+''H-#..'I00H'*!"#$%F''()%* 5"("*,6,*6<br>121212 34'.524@'%20)H-F6'-7834'.524@'%2I'4'.'%7B-$>-8-7834'.52%%HI'%2-7IF6H-$9-782:47;%<IH%8-I'%H LMMN N 1212 34'.52-784782I'4'.'%7?0;%2H%F6'I#%90%8;6%-;<br>12 34'.520)H-F6'-78<br>+34I,"1("#$%"I,01"2("#$%F'"(F))* !"#$%F''()%* N N 8-"(,6"2'(,-..%("#$%"I,01"2("#$%F'"(F))* !"#$%F''()%*<br>LMMN !+''H-#..'I00H'*<br>!+''H-#..'I00H'* LMMN LMMN 12 =-%.B28%5%<;%2H%F6'I90H5<br>12 ?0;%2).#<-%@H%F6'%<-$@%2H%F6'I90H5 12 ?0;%209%H-8%2)H-944'H%F6'%<-$@%2H%F6'I90H5<br>LMMO LMMO N<br>?)::3*,#.%,"6"6"-"*F !"#$%F''()%* A%>0%@<0F4'-% D0I'<0F4'-%<br>LMMN<br>LMMN LMMN LMMN<br>!"#$%F''()%* !"#$%F''()%*<br>C)#.%," @=AB.#%,-,%",%<br>!+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 C7;-F4'-%24I8%IF6%H5; 12 C7;-F4'-%2600I;4F'-9-'%-'<br>12 O0%90%8-7824;H%I 12 "5IF6H-$9-782HACFF0;%<br>12 HACFF0;%<br>**----- End of picture text -----**<br>


**Figuur 26. Ontsluiting gegevens uit het Handelsregister: rechtspersoon** 

**==> picture [452 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>!"#$%&''()%* A2'I9I$#B%12""I%6'%%F+*12')%F*F+* 4'D$9I') ;%$+9$$I91%'0'?""++L..'I<br>(""I%6'%%F+*1"+9'I+'.F+*<br>QRRS 12!+''H-#..'I00H'*L6'.:2<00H'N%''-482045%H4%:-48 12!+''H-#..'I00H'*L6'.:2<00H'N%''-482<%I'-8-48 12!+''H-#..'I00H'*LNO 1212!+''H-#..'I00H'*=05%2'()%2'%B%70044.::%H345-&6'-%28%9%-:2'%B%70044.::%H<br>QRRT 12 345-&6'-%2<00HC%.H2'%B%70044.::%H<br>QRRS QRRS 12 ;%B%70042B6454.::%H<br>QRRS QRRT 12 ;%B%70044.::%H<br>!"#$%&''()%*<br>I6:%48%<0%852:%' 3"..L+F#$%F'*'*'2'+) QRRS<br>QRRT QRRT QRRS !"#$%&''()%*<br>QRRS QRRS ;%$+9$$I91@-.$F01$9I')<br>J%N0%CB0&6'-% !"#$%&''()%* QRRT<br>!"#$%&''()%* (')%F*F+* !+''H-#..'I00H'*<br>!"#$%F' QRRS 12 OA:6-B265H%I<br>QRRS QRRT !+''H-#..'I00H'* 12 345-&6'-%2<00HC%.H2%A:6-B265H%I<br>12!+''H-#..'I00H'*345-&6'-%2678%I&9%H:5 F0I'B0&6'-% 1212 =05%2'()%2<%I'-8-48L6'.:2664<6482<%I'-8-48 QRRS 12 345-&6'-%2ILM32%A:6-B265H%I<br>12 ;0%<0%8-48265H%I QRRS QRRT 1212 L6'.:2%-45%2<%I'-8-48?%I'-8-48I4.::%H QRRT !"#$%&''()%*<br>S QRRS C"I.'0'1I'*F)%I$%F' 4'I56$.'17'I)"+'+ !"#$%&''()%*<br>!+''H-#..'I00H'*<br>12 L6'.:2664<6482H%8-I'H6'-% !+''H-#..'I00H'*<br>12 L6'.:2%-45%2H%8-I'H6'-% 12 =05%2CB6II%2D%HCN6:%2)%HI04%42'0'66B<br>QRRS QRRS 1212 F%-B56'.:2D%HCN6:%2)%HI04%4+64'6B2D%HCN6:%2)%HI04%42'0'66B<br>HF'%-#"..'I#F'0'12')%F*F+* !"#$%&''()%* 3"..'I#F'0'12')%F*F+* !"#$%&''()%* 3I2%%42.-'0%7%4-482<64 QRRS 1212 +64'6B2D%HCN6:%2)%HI04%425%%B'-$5+64'6B2D%HCN6:%2)%HI04%42<0B'-$5<br>!+''H-#..'I00H'* QRRT QRRS<br>12 @66:24-%'A&0::%H&-%B%2<%I'-8-48<br>!"#$%&''()%*<br>S S QRRT QRRT G645%B'2045%H QRRS 8$+9'0)+$$.<br>!+''H-#..'I00H'*<br>QRRT QRRS M0H5'2.-'8%0%7%452-4 QRRS QRRS QRRS 12 L6'.:2664<64829645%BI466:<br>:#%F2F%'F%'+1+F'%1#"..'I#F'0' !"#$%&''()%* :#%F2F%'F%'+1#"..'I#F'0'12')%F*F+* !"#$%&''()%* !"#$%!&$''()"*+%,#(-../ QRRT 1212 L6'.:2%-45%29645%BI466:G645%BI466:<br>2')%F*F+* !"#$%&''()%* 12 ?0B80H5%<br>!+''H-#..'I00H'* S A+9'I+'.F+*N=+)%'00F+* QRRT<br>12!+''H-#..'I00H'*":I&9H-$<-4826&'-<-'%-' 1212 345-&6'-%2-:)0H'%%H'345-&6'-%2%H)0H'%%H' !+''H-#..'I00H'* G645%B'2045%H<br>12 J0%C$66H25%)04%H-482$66HI'.C<br>12 =05%2H%5%42-4I&9H-$<-482045%H4%:-48P-4I'%BB-48<br>12 =05%2H%5%42.-'I&9H-$<-482045%H4%:-48P-4I'%BB-48<br>12 =05%2'()%2045%H4%:-48P-4I'%BB-48 S<br>12 L6'.:2664<6482045%H4%:-48<br>12 L6'.:2%-45%2045%H4%:-48<br>12 L6'.:2-4I&9H-$<-482045%H4%:-48P-4I'%BB-48<br>!"#$%&''()%* 12 345-&6'-%2%&040:-I&926&'-%7<br>;<=-$#%F2F%'F% 12 345-&6'-%276-BB-II%:%4'2045%H4%:-48P-4I'%BB-48<br>12 345-&6'-%20)9%77-482045%H4%:-48P-4I'%BB-48<br>!+''H-#..'I00H'* 12 345-&6'-%2I.HI%64&%2045%H4%:-48P-4I'%BB-48<br>12 345-&6'-%2900756&'-<-'%-' 12 ":I&9H-$<-482I'6'.'6-H%2N%'%B<br>12 ":I&9H-$<-482IJ3A&05% 12 34I&9H-$<-48I4.::%H2C6:%H2<642C00)9645%B<br>12 IJ3A&05% 12 ":I&9H-$<-482H%&9'I<0H:2G645%BIH%8-I'%H<br>QRRS<br>**----- End of picture text -----**<br>


**Figuur 27. Ontsluiting gegevens uit het Handelsregister: vestiging** 

## **4.16 Conceptueel gegevensdeelmodel van Verbeteren Uitwisseling Matchingsgegevens (VUM)** 

In dit gegevensdeelmodel worden de gegevens die worden gebruikt bij Verbeteren Uitwisseling Matchingsgegevens (VUM) weergegeven. VUM zorgt voor meer transparantie in het werkzoekendenen vacaturebestand over regio- en organisatiegrenzen heen. Op die manier zorgt VUM ervoor dat de juiste werkzoekende snel, goed en duurzaam gekoppeld kan worden aan de juiste vacature. 

Het gaat om de gegevens over onder andere werkzoekende, vacature, arbeidsmarktkwalificatie en werkgever. 

Hieronder is aangegeven wat de bedoeling is van de verschillende kleuren in dit gegevensdeelmodel. 

- De klassen in het oranje betekenen dat de gegevenselementen vanuit het algemene gedeelte van het SGR specifiek voor VUM op maat zijn gemaakt. 

- De klassen in het blauw betekenen dat de gegevenselementen specifiek voor VUM zijn gecreëerd. 

- De klassen in het groen betekenen dat de gegevenselementen voor VUM zijn overgenomen uit het algemene gedeelte van het SGR. 

**==> picture [453 x 653] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%* !"#$%&''()%*<br>!"#$)*+("G ,FG)#-.)IF#0<br>!+'',-#..'I00,'* !+'',-#..'I00,'*<br>121212 +:8':B2C%,6.,%82)%,2C%%62M:N-M::B+:8':B2C%,6.,%82)%,2C%%62M-8-M::B389-&:'-%26:8'00,'-$9%8 1212 F09%2'()%2:,#%-9I&08',:&'F09%2'()%20=%,%%860MI'<br>OPPQ<br>OPPN<br>!"#$%&''()%*<br>!"#$%"#&'((")<br>!+'',-#..'I00,'* OPPQ<br>12 304%25%,50%,6-44%7<br>12 894-&:'-%2#%I&;-<#::,2500,2.-'50%,-9=2>%,<<br>12 894-&:'-%2#%I&;-<#::,2500,2>009?>%,<5%,<%%, !"#$%&''()%*<br>!"#$%F"$"G("<br>!+'',-#..'I00,'*<br>12 3425%,670%6%89%<br>!"#$%&''()%* ;8"<*1*8*)"*) 1212 389-&:'-%2#%I&;-6#::,;%-92&08':&'<%<%=%8I389-&:'-%2L4?@,%<-I',:'-% !"#$%&''()%*<br>!+'',-#..'I00,'* 12 A%,I008B-$6%2),%I%8':'-% !"1-(#"2<br>12 F09%2,%<-0I',::B OPPN !+'',-#..'I00,'*<br>1212 4:'.M2::8=:8<2#%I&;-6#::,2=00,2C%,64:'.M2%-89%2#%I&;-6#::,2=00,2C%,6 N OPPQ 1212 F95%#:9,%IG?L<br>12 389-&:'-%208,%<%BM:'-<2C%,620J2)B0%<%89-%8I'<br>!"#$%&''()%* N<br>=F1*8*)"*)<br>!+'',-#..'I00,'*<br>12 I%M-99%B-8<I)0I'&09% OPPN N<br>12 O:N-M:B%2,%-I:JI':89 !"#$%&''()%*<br>12 O:N-M:B%2,%-I'-$9 3".)F#41"#F"5264"G<br>N OPPQ 1"(#*+728"I"G<br>!+'',-#..'I00,'*<br>12 F09%2HI3<br>!"#$%&''()%*<br>>*24--G4?"#$<br>N N<br>!+'',-#..'I00,'*<br>12 389-&:'-%2::8):II-8<2C%,60M<%=-8< OPPN<br>12 389-&:'-%2#%<%B%-9-8<<br>12 389-&:'-%2C%,6=:,-:'-%<br>!"#$%&''()%*<br>9"0*(("8*G:21"#F"5<br>!"#$%&''()%* OPPQ<br>@FF#$"A#28-G(<br>12!+'',-#..'I00,'*L:89%8&09%23H" OPPQ N OPPQ<br>!"#$%&''()%* OPPN N<br>@-$I--#(*:M"*(<br>!+'',-#..'I00,'* B#1"*(20-#$)$?-8*7*.-)*" !"#$%&''()%* !"#$"#I-#*G: !"#$%&''()%* !"#$%&''()%* 9"#F"5<br>1212 L::M2=:6=::,9-<;%-9M0%B-&;'-8<2=:6=::,9-<;%-9 OPPQ 12!+'',-#..'I00,'*F09%2C%,6@2%829%868-=%:.2C%,670%6%89% 12!+'',-#..'I00,'*+:8':B2$:,%82C%,67::M2-82#%,0%) OPPQ N<br>12 4:'.M2::8=:8<2C%,67::M;%9%8<br>N OPPN 12 4:'.M2%-89%2C%,67::M;%9%8<br>12 L::M20,<:8-I:'-%<br>!"#$%&''()%* 12 M0%B-&;'-8<2C%,6%,=:,-8<<br>C--81"M""#2*G: N<br>!+'',-#..'I00,'*<br>1212 F09%28-=%:.2'::B#%;%%,I-8<2B%7%8F09%28-=%:.2'::B#%;%%,I-8<2B.-I'%,%8 OPPQ N N<br>12 F09%28-=%:.2'::B#%;%%,I-8<2M089%B-8<<br>12 F09%28-=%:.2'::B#%;%%,I-8<2I&;,-J'%B-$6 !"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>12 F09%2'::B OPPQ F*+1"?*+2 9"#F"52G--04FG:".F(""#( 9"#F"52G--04:".F(""#(<br>N<br>!+'',-#..'I00,'* !+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 F09%2I00,'2,-$#%C-$I 12 L::M2#%,0%)208<%&09%%,9 12 F09%2#%,0%)I8::M<br>N<br>!"#$%&''()%*<br>E"(#-:2.F05")"G)*" N N<br>!+'',-#..'I00,'* OPPQ<br>12 M0%B-&;'-8<2<%9,:<I&0M)%'%8'-%<br>OPPQ<br>OPPQ<br>!"#$%&''()%*<br>H58"*(*G: !"#$%&''()%*<br>!"#$%&''()%* !"#$%&''()%* ,A#2A2<br>E"(#-:2.F05")"G)*"4FG:".F(""#( E"(#-:2.F05")"G)*" !+'',-#..'I00,'*<br>:".F(""#( 12 F09%28-=%:.20)B%-9-8< !+'',-#..'I00,'*<br>!+'',-#..'I00,'* 12 F09%2I':'.I20)B%-9-8< 12 4:'.M2::8=:8<2=0B<%82&.,I.I<br>12 L::M2<%9,:<I&0M)%'%8'-%208<%&09%%,9 !+'',-#..'I00,'* 12 4:'.M2::8=:8<2=0B<%820)B%-9-8< 12 4:'.M2&%,'-J-&::'<br>12 F09%2<%9,:<I&0M)%'%8'-% 12 4:'.M29-)B0M: 12 4:'.M2%-89%2=0B<%82&.,I.I<br>12 4:'.M2%-89%2=0B<%820)B%-9-8< 12 389-&:'-%2&%,'-J-&::'<br>OPPQ 1212 389-&:'-%29-)B0M:L::M20)B%-9-8<I-8I'-'..' 1212 L::M2&.,I.IL::M20)B%-9-8<I-8I'-'..'<br>!"#$%&''()%* 12 M0%B-&;'-8<20)B%-9-8< 12 M0%B-&;'-8<2&.,I.I<br>GG)"#"22"<br>!+'',-#..'I00,'*<br>12 L::M2-8'%,%II%<br>!"#$%&''()%* !"#$%&''()%*<br>H58"*(*G:2G--04FG:".F(""#( H58"*(*G:2G--04:".F(""#(<br>!+'',-#..'I00,'* !+'',-#..'I00,'*<br>12 L::M20)B%-9-8<208<%&09%%,9 12 F09%20)B%-9-8<I8::M<br>**----- End of picture text -----**<br>


**Figuur 48. VUM: werkzoekendeprofiel** 

**==> picture [453 x 673] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%*<br>9F/G541+--F:""F4G3<br>!+''H-#..'I00H'*<br>12 =:'.;2::89:8L25%H6H::;D%4%8<br>!"#$%&''()%* 12 =:'.;2%-84%25%H6H::;D%4%8<br>!"#"$%&$'()&*+&+&,&-*$ ,G#$-F./GF-G012.G3 NOOQ 12 ";I&DH-$9-8L2:H#%-4I900H5::H4%8<br>,'-$(&$.&)/+&,&)$012-$ /G4F56718G+G3 12 F:<:H-I-84-&:'-%<br>,&)(&)$314+&.&)/4$56$7&4$ NOOP<br>(1'+)'8$9:()&*9" !+''H-#..'I00H'*<br>Q 12 304%2FG?<br>!"#$%&''()%* 1@%I'-L-8LI:4H%I !"#$%&''()%* NOOQ !"#$%&''()%*<br>94FG1 NOOQ NOOQ (GF)*G+GF Q A-3$F"#$+-F?<br>130HH%I)084%8'-%:4H%I !+''H-#..'I00H'* !"#$%&''()%* Q !+''H-#..'I00H'*<br>NOOQ NOOQ 12 N:84%<I8::;20HL:8-I:'-% Q !"#"$%FG Q 12 304%2'()%2:H#%-4I&08'H:&'<br>1I%H6<0&:'-%:4H%I !+''H-#..'I00H'* 12 304%2'()%209%H%%860;I' BGF-G013""?.-3*G#-4GGF4 !"#$%&''()%*<br>NOOQ NOOQ 12 304%25%H672%824%868-9%:.2;-8-;::<<br>12 =:'.;2I<.-'-8L29:&:'.H% !+''H-#..'I00H'*<br>12 ?=2@:&:'.H% !"#$%&''()%* 12 C::;2#%H0%)208L%&04%%H4<br>12 ?84-&:'-%2A=B7H%L-I'H:'-% Q BGF-G0<br>!"#$%&''()%* !"#$%&''()%* 12 C::;29:&:'.H%<br>(G/"4FG1 ,-885#5$"$5G:56;G 12 C.;;%H29:&:'.H%<br>12 ";I&DH-$9-8L29:&:'.H% Q<br>!+''H-#..'I00H'* NOOQ Q !+''H-#..'I00H'* QOOP NOOP Q !"#$%&''()%*<br>12 34I%#:4H%I 12 34F0<<-&-':'-%5-$H% BGF-G013""?.*G#-4GGF4<br>12 JBA<br>!+''H-#..'I00H'*<br>NOOP 12 304%2#%H0%)I8::;<br><""8/G=GGF153* !"#$%&''()%* Q (GF)GF+"F53* !"#$%&''()%*<br>!+''H-#..'I00H'* Q !+''H-#..'I00H'*<br>12 304%28-9%:.2'::<#%D%%HI-8L2<%H%8 12 +:8':<2$:H%825%H6H::;2-82#%H0%)<br>12 304%28-9%:.2'::<#%D%%HI-8L2<.-I'%H%8 NOOP 12 =:'.;2::89:8L25%H6H::;D%4%8<br>12 304%28-9%:.2'::<#%D%%HI-8L2;084%<-8L NOOP 12 =:'.;2%-84%25%H6H::;D%4%8<br>12 304%28-9%:.2'::<#%D%%HI-8L2I&DH-O'%<-$6 12 C::;20HL:8-I:'-%<br>12 304%2'::< 12 L0%<-&D'-8L25%H6%H9:H-8L<br>Q Q<br>Q !"#$%&''()%*<br>!"#$%&''()%* Q C56/G:561<br>!")+""F45*=G54 NOOP<br>!+''H-#..'I00H'*<br>!+''H-#..'I00H'* 12 304%2I00H'2H-$#%5-$I<br>12 C::;29:69::H4-LD%-4 NOOP<br>12 L0%<-&D'-8L29:69::H4-LD%-4 NOOQ<br>!"#$%&''()%*<br>!GF+-GF?544G8<br>>G4F"*1#-?0G$G3$5G !"#$%&''()%* QQ NOOP 1212!+''H-#..'I00H'*304%29%H90%H;-44%<?84-&:'-%2#%I&D-6#::H2900H2.-'90%H-8L25%H6<br>!+''H-#..'I00H'* NOOP Q 12 ?84-&:'-%2#%I&D-6#::H2900H2500875%H69%H6%%H<br>12 L0%<-&D'-8L2L%4H:LI&0;)%'%8'-%<br>!"#$%&''()%*<br>D8GE5/585$G5$<br>NOOQ<br>!+''H-#..'I00H'*<br>Q 12 304%2H%L-0I'H::<<br>!"#$%&''()%* !"#$%&''()%* 12 =:'.;2::89:8L2#%I&D-6#::H2900H25%H6<br>>G4F"*1#-?0G$G3$5G.-3*G#-4GGF4 >G4F"*1#-?0G$G3$5G 12 =:'.;2%-84%2#%I&D-6#::H2900H25%H6<br>*G#-4GGF4 12 ?84-&:'-%208H%L%<;:'-L25%H620O2)<0%L%84-%8I'<br>!+''H-#..'I00H'*<br>12 C::;2L%4H:LI&0;)%'%8'-%208L%&04%%H4 !+''H-#..'I00H'* Q<br>12 304%2L%4H:LI&0;)%'%8'-%<br>NOOP<br>NOOP NOOQ<br>!"#$%&''()%*<br>@08G5453* !"#$%&''()%* !"#$%&''()%*<br>A%F1%1 (GF)$564G3<br>!+''H-#..'I00H'*<br>12 304%28-9%:.20)<%-4-8L !+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 304%2I':'.I20)<%-4-8L 12 =:'.;2::89:8L290<L%82&.HI.I 12 +:8':<25%H6.H%82)%H25%%62;:M-;::<<br>12 =:'.;2::89:8L290<L%820)<%-4-8L 12 =:'.;2&%H'-O-&::' 12 +:8':<25%H6.H%82)%H25%%62;-8-;::<<br>12 =:'.;24-)<0;: 12 =:'.;2%-84%290<L%82&.HI.I 12 ?84-&:'-%26:8'00H'-$4%8<br>12 =:'.;2%-84%290<L%820)<%-4-8L 12 ?84-&:'-%2&%H'-O-&::'<br>12 ?84-&:'-%24-)<0;: 12 C::;2&.HI.I<br>12 C::;20)<%-4-8LI-8I'-'..' 12 C::;20)<%-4-8LI-8I'-'..'<br>12 L0%<-&D'-8L20)<%-4-8L 12 L0%<-&D'-8L2&.HI.I<br>!"#$%&''()%* !"#$%&''()%*<br>@08G5453*13""?.-3*G#-4GGF4 @08G5453*13""?.*G#-4GGF4<br>!+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 C::;20)<%-4-8L208L%&04%%H4 12 304%20)<%-4-8LI8::;<br>**----- End of picture text -----**<br>


**Figuur 59. VUM: vacature** 

**==> picture [450 x 356] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>!"#$%<br>!"#$%&GG()%* !"#$%&GG()%*<br>!"#$%&'$"$#()*" !"#$%&+,-.$*()*"<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 304%25%6%%7G% 12 ?;74%7&04%2<C"<br>12 8-IGH-&G 12 ?;74I7;;6<br>12 9%6%%7G%4%%: 12 ?0&;G-%06I&@H-$L-752#.-G%7:;74<br>12 9%6%%7G%7;;6 12 A0IG&04%2#.-G%7:;74<br>12 <4%7G-=-&;G-%&04%27.66%H;;74.-4-75 12 D%5-07;;62#.-G%7:;74<br>12 <4%7G-=-&;G-%&04%2L%H#:-$=):;;GI 12 B007):;;GI7;;62#.-G%7:;74<br>12 ?0&;G-%06I&@H-$L-75<br>12 A0IG&04%<br>12 B007):;;GI7;;6<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>/.#)).)"#$% 01%.+,%)"#$% !*.211#"*,33$#)"#$% /.#)).)"#$%&+,-.$*()*" !"#$%&GG()%*<br>01%.+,%)"#$%&+,-.$*()*"<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>!+GGH-#..GI00HG*<br>12 +;74.-4-752#-$2@.-I7.66%H 12 A0IG#.I7.66%H 12 +7GG00H47.66%H 12 N.-I7.66%H2#.-G%7:;74<br>12 A0IG#.I7.66%H2#.-G%7:;74<br>12 N.-I:%GG%H 12 CGH;;G7;;62#.-G%7:;74<br>12 N.-I7.66%H<br>12 N.-I7.66%HG0%L0%5-75<br>12 F;;620)%7#;H%2H.-6G%<br>12 CGH;;G7;;6<br>12 B007#00GL%HG-$H-75<br>12 B007G;5%7L%HG-$H-75<br>**----- End of picture text -----**<br>


**Figuur 30. VUM: adres** 

**==> picture [450 x 270] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>!"#$'("$")*" 8(),-9,:"#4(();0-6*"32)% !"#$%"&"#<br>!+''H-#..'I00H'* !+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 :;2<%H=L0%=%56% MOO JOOL 12 H4482&05'4&')%HI005IC4G6%7-59 JOOL M 12 3456%7I544820H945-I4'-%<br>12 :56-&4'-%2#%I&?-=#44H?%-62&05'4&'9%9%@%5I<br>12 :56-&4'-%2A;BCH%9-I'H4'-% M M<br>12 D%HI0057-$=%2)H%I%5'4'-%<br>JOOL<br>!"#$%&''()%*<br>+,-)*--#*./01-23.-*#"4<br>M JOOL<br>!+''H-#..'I00H'*<br>12 NC84-7246H%I JOOL<br>!"#$%&''()%*<br>+,-)*--#*<br>5"3"6(())711"#<br>M<br>JOOL<br>!+''H-#..'I00H'*<br>12 F%7%G0055.88%H<br>**----- End of picture text -----**<br>


**Figuur 31. VUM: contactgegevens** 

**==> picture [449 x 449] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>!"#$%&&'(&)&*$'+,-(<br>!+GG,-#..GI00,G*<br>!"#$%&GG()%* 12 304%2,%I.;G55G2-<;066%<<br>!"#$%&&'(&)&* 12 L5G.=2G-$42-<;066%<<br>12 L5G.=2G-$42.-G;066%<<br>!+GG,-#..GI00,G* OPPQ 12 M%#,.-N%,I<55=<br>12 304%2&5G%60,-%2789:4%%;<%=%, 12 @F:54,%I<br>12 304%2IG5G.I2G0%65<62789 R 12 G5<4%<&04%2@F:54,%I<br>12 304%2IG5G.I2789:4%%;<5=%<br>12 L5G.=255<?5<62789:4%%;<5=%<br>12 L5G.=2%-<4%2789:4%%;<5=% R<br>12 @<4-&5G-%2G0%65<62789 !"#$%&GG()%*<br>12 A55=2789:4%%;<%=%, R .+'/!"#$%&&'(&)&*<br>12 BC@A OPPQ<br>!+GG,-#..GI00,G*<br>R R<br>12 304%2,0;2789:4%%;<%=%,<br>12 L5G.=255<?5<62,0;2789:4%%;<%=%,<br>12 L5G.=2%-<4%2,0;2789:4%%;<%=%,<br>OPPQ OPPQ OPPQ<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>!"#$<+&=231-& !"#$'&>&*-(,5231-& 0+(12314&*5++(6$27%&'-(,<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>12 304%2G()%2789:L0%N5&G-% 12 304%2G()%2789:;%?%,-<6I5&G-% 12 A55=2&0<G5&G)%,I00<H:5I4%;-<6<br>12 G5<4%<&04%2@F:54,%I<br>R R<br>OPPQ OPPQ<br>!"#$%&GG()%* !"#$%&GG()%*<br>812(%22*% 812(%22*%/;$)2-'/2%*&5<br>9&'&7++((:))&*<br>!"#$%&GG()%* !+GG,-#..GI00,G*<br>!"#$231-& !+GG,-#..GI00,G* 12 O:=5-;254,%I<br>12 J%;%I00<<.==%,<br>!+GG,-#..GI00,G*<br>12 L5G.=2G-$42789:5&G-%<br>12 @L2789:L0%N5&G-%<br>12 @F:54,%I<br>12 G5<4%<&04%2@F:54,%I<br>12 "=I&M,-$?-<620<4%,N%,)2789:5&G-%<br>**----- End of picture text -----**<br>


**Figuur 32. VUM: procesgegevens** 

## **4.17 Conceptueel gegevensdeelmodel van de instrumentengidsen Dennis & Eva** 

In dit gegevensdeelmodel worden de gegevens die worden gebruikt bij de instrumentengidsen Dennis & Eva weergegeven. Dennis is een instrumentengids binnen de arbeidsmarktregio’s en helpt de werkgeversdienstverlening te verbeteren. Eva is een instrumentengids voor professionals binnen de gemeenten en ondersteunt om mensen te begeleiden naar werk of duurzame participatie. Organisaties vullen Dennis & Eva zelf met lokale en regionale instrumenten. Deze zijn vervolgens zichtbaar in alle instrumentengidsen, net als landelijke instrumenten. Zo ondersteunen Dennis & Eva beide kanten van het proces om inwoners naar werk, scholing of participatie te begeleiden. 

Het gaat om de gegevens over onder andere instrumenten, aanbieders van instrumenten, beheerders van instrumenten en uitvoeringslocaties. 

De adresgegevenselementen zijn overgenomen uit het algemene gedeelte van het SGR en in het grijs weergegeven in dit gegevensdeelmodel. 

**==> picture [451 x 463] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%*<br>C(%+03".#:D38$(,(0<br>!+'',-#..'I00,'*<br>12 C0:%2G%,D;46:I&F4)'%B%;<br>12 34452G%,D;46:I&F4)'%B%;<br>12 A;.B2G%,D;46:I&F4)'%B%;<br>12 P0,'%205I&F,-$N-6B2G%,D;46:I&F4)'%B%;2K=LL?@<br>12 "5I&F,-$N-6B2G%,D;46:I&F4)'%B%;2K=LL?@<br>12 H0%;-&F'-6B264452G%,D;46:I&F4)'%B%;<br>=LLQ<br>=LLQ<br>!"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>=I$-7(%I",#07:3$I( !"#$%&G("$ 4I"+<br>!+'',-#..'I00,'* !+'',-#..'I00,'* =LLQ !+'',-#..'I00,'*<br>=LL? 1212 34452;0&4'-%C0:%2'()%2.-'N0%,-6BI;0&4'-% =LLQ 1212 34452-6I',.5%6'77892-6I',.5%6' 1212 34452;-6D7NO2;-6D<br>12 86:-&4'-%2.-'N0%,-6BI;0&4'-%24&'-%I2K=LL?@ 12 86:-&4'-%2).#;-&4'-%2-6I',.5%6'<br>12 H0%;-&F'-6B2.-'N0%,-6BI;0&4'-%2K=LL?@ ? 1212 94'.52%-6:%2).#;-&4'-%2-6I',.5%6'2K=LL?@A;.B2-6I',.5%6'<br>1212 C0:%2#%,%-D2-6I',.5%6'94'.52446N46B2).#;-&4'-%2-6I',.5%6'2K=LL?@ ? !"#$%&''()%* ?I.(7<br>!"#$%&''()%* A.%(# =LL? =LLQ =LL? 1212!+'',-#..'I00,'*34452446#-%:%,77892446#-%:%,!"#$%&''()%* A3"2I(.(% ? =LLQ 1212121212 86:-&4'-%2;46:%;-$D2-6I',.5%6'86:-&4'-%2,%B-0644;2-6I',.5%6'86:-&4'-%2;0D44;2-6I',.5%6'34452#%,%-D2-6I',.5%6'86:-&4'-%2&05);%%'2K=LL?@ ? =LLQ 121212!+'',-#..'I00,'*34452N-:%0A;%.'%;2N-:%034452446#-%:%,2N-:%0<br>=LLQ =LLQ =LLQ !"#$%&''()%* 17*"073.<br>!"#$%&''()%* =LLQ !+'',-#..'I00,'*<br>B7"$3:$8(%#77" 12 34452:0G6;04:<br>12 7NO290G6;04:<br>!+'',-#..'I00,'* =LLQ<br>12 34452&06'4&')%,I006 ?<br>1212 H%;%I0066.55%,2&06'4&')%,I0062K=LL?@M54-;4:,%I2&06'4&')%,I0062K=LL?@ =LLQ !"#$%&''()%*<br>12 C0:%2'()%2&06'4&')%,I0062,%;4'-%2K=LL?@ @(,I#$%3$I(:7.(<br>12 "5I&F,-$N-6B2&06'4&')%,I0062K=LL?@ =LLQ<br>!+'',-#..'I00,'*<br>=LLQ 12 N%B-I',4'-%&0:%<br>12 N%B-I',4'-%&0:%;4#%;2K=LL?@<br>!"#$%&''()%* 12 86:-&4'-%2G%%,B%N%62K=LL?@<br>17(0,%7(8<br>!+'',-#..'I00,'* =LLQ<br>12 C0:%2:0%;B,0%)<br>12 34452:0%;B,0%)<br>!"#$%&''()%*<br>;%7(8#-7%G<br>!+'',-#..'I00,'*<br>1I("#$-(%23". !"#$%&''()%* !"#$%&G("$)*(%+,(-(%#.I("#$-(%0("I", !"#$%&''()%* !"#$%&G("$)*(%+"(G(%#.I("#$-(%0("I", !"#$%&''()%* =LLQ 1212 C0:%2B,0%)IN0,534452B,0%)IN0,5<br>1212!+'',-#..'I00,'*C0:%2:-%6I'N%,#46:34452:-%6I'N%,#46: =LLQ 1212!+'',-#..'I00,'*"5I&F,-$N-6B2D0,'2-6I',.5%6'86:-&4'-%2:0%;B,0%),%B-I'%, 1212!+'',-#..'I00,'*A45%6N4''-6B2-6I',.5%6'"5I&F,-$N-6B2:0%;2-6I',.5%6' =LLQ K03"$+("G(%+ !"#$%&''()%*<br>12 86:-&4'-%2'-$:%;-$D%2,%B%;-6B 12 "5I&F,-$N-6B24465%;:-6I',.&'-%I2K=LL?@<br>=LLQ 12 86:-&4'-%2;%%,G%,D',4$%&' 12 "5I&F,-$N-6B206:%,I&F%-:%6:%2446)4D2K=LL?@ !+'',-#..'I00,'*<br>1212!+'',-#..'I00,'*C0:%2;%%I'-$:IB,0%)34452;%%I'-$:IB,0%) 4((5$I6.#,%7(8 !"#$%&''()%* =LLQ =LLQ 121212 "5I&F,-$N-6B2446N,44B"5I&F,-$N-6B2-6I',.5%6'"5I&F,-$N-6B2N00,G44,:%6 12121212121212 "5I&F,-$N-6B2N00,G44,:%62:%%;645%2K=LL?@H0%;-&F'-6B2:0%;B,0%)2K=LL?@"5I&F,-$N-6B2I45%6G%,D-6BI)4,'6%,I2K=LL?@"5I&F,-$N-6B2G%,D4II),4D%62K=LL?@+46'4;2.,%62-6'%6I-'%-'2)%,2G%%D2K=LL?@"5I&F,-$N-6B2446N.;;%6:%2-6I0,54'-%2K=LL?@H0%;-&F'-6B2-6'%6I-'%-'2K=LL?@ =LLQ =LLQ 1212 C0:%2D;46'D%65%,D34452D;46'D%65%,D =I$-7(%I",#-7%G !"#$%&''()%*<br>1212 9..,2',4$%&'2K=LL?@C0:%2%%6F%-:2:..,2',4$%&'2K=LL?@ =LLQ !+'',-#..'I00,'*<br>=LLQ 12 H0%;-&F'-6B2:..,2',4$%&'2K=LL?@ ?LLQ 12 C0:%2.-'N0%,-6BIN0,5<br>!"#$%&''()%* 12 J%:,4B2'0'44;2D0I'%62K=LL?@ 12 34452.-'N0%,-6BIN0,5<br>9(:$7%)I"#$%&G("$ 12 H0%;-&F'-6B2D0I'%62K=LL?@<br>1212!+'',-#..'I00,'*"5I&F,-$N-6B2AJ8L&0:%AJ8L&0:% =LLQ 1212 9..,'2',4$%&'2-62.,%62K=LL?@"5I&F,-$N-6B2G%,DG-$O%2-6I',.5%6' ? !"#$%&''()%* L(77%.(0I",<br>!+'',-#..'I00,'*<br>=LLQ 1212 +.'%.,2#%00,:%;-6B2K=LL?@M54-;4:,%I24.'%.,2#%00,:%;-6B<br>12 +;B%5%6%2I&0,%<br>12 H0%;-&F'-6B24;B%5%6%2I&0,%2K=LL?@<br>12 N%I.;'44'2I&0,%<br>12 H0%;-&F'-6B2,%I.;'44'2I&0,%2K=LL?@<br>12 7-'N0%,-6B2I&0,%<br>12 H0%;-&F'-6B2.-'N0%,-6B2I&0,%2K=LL?@<br>12 94'.52'-$:2#%00,:%;-6B<br>**----- End of picture text -----**<br>


**Figuur 33. Instrumentengidsen Dennis & Eva** 

**==> picture [454 x 555] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%* !"#$%&GG()%*<br>!"#$%&G("$.*GI(01"I 21(&3#4(%1,5$<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G* !"#$%&GG()%*<br>6(3(%7G*G("$<br>12 34452-6IG,.5%6G205B%N-6B 12 F-G%;26-%.MI#%,-&IG<br>12 A;.B2-6IG,.5%6G205B%N-6B 12 "6:%,G-G%;26-%.MI#%,-&IG2<=LL?@ !+GG,-#..GI00,G*<br>12121212 "5I&I,-$N-6B2-6IG,.5%6G205B%N-6B2<=LL?@F-G%;2-6IG,.5%6G205B%N-6B2<=LL?@7JO2-6IG,.5%6G205B%N-6B2<=LL?@7JO2;0B02<=LL?@ ? =LLO 12121212 86I0.:26-%.MI#%,-&IGF%4I%,26-%.MI#%,-&IG2<=LL?@94G.52446N46B2).#;-&4G-%26-%.MI#%,-&IG2<=LL?@94G.52%-6:%2).#;-&4G-%26-%.MI#%,-&IG2<=LL?@ ? ?LLO 121212 94G.52G-$:2446B%544DG94G.52G-$:2B%M-$N-B:2<=LL?@94G.52G-$:2N%,M-$:%,:2<=LL?@<br>12 L,-54-,%2D;%.,2<=LL?@ 12 94G.52).#;-&4G-%26-%.MI#%,-&IG ?LLO<br>12 A%&.6:4-,%2D;%.,2<=LL?@ 12 86:-&4G-%2).#;-&4G-%26-%.MI#%,-&IG2<=LL?@<br>=LLO =LLO =LLO ?<br>!"#$%&GG()%*<br>!"#$%&G("$<br>!+GG,-#..GI00,G*<br>12 34452-6IG,.5%6G<br>? 12 77892-6IG,.5%6G<br>12 86:-&4G-%2).#;-&4G-%2-6IG,.5%6G<br>!"#$%&GG()%* 12 94G.52%-6:%2).#;-&4G-%2-6IG,.5%6G2<=LL?@<br>)*"$+,$-(%#**" P%G006:%2",B46-I4G-%I 12 A;.B2-6IG,.5%6G<br>12 C0:%2#%,%-D2-6IG,.5%6G<br>!+GG,-#..GI00,G* 12 94G.52446N46B2).#;-&4G-%2-6IG,.5%6G2<=LL?@<br>12 34452&06G4&G)%,I006 12 86:-&4G-%2;46:%;-$D2-6IG,.5%6G<br>12 F%;%G0066.55%,2&06G4&G)%,I0062<=LL?@ =LLO 12 86:-&4G-%2,%B-0644;2-6IG,.5%6G<br>12 H54-;4:,%I2&06G4&G)%,I0062<=LL?@ 12 86:-&4G-%2;0D44;2-6IG,.5%6G<br>12 C0:%2G()%2&06G4&G)%,I0062,%;4G-%2<=LL?@ =LLO 12 34452#%,%-D2-6IG,.5%6G<br>12 "5I&I,-$N-6B2&06G4&G)%,I0062<=LL?@ 12 86:-&4G-%2&05);%%G2<=LL?@<br>=LLO =LLO<br>=LLO ?=LLO<br>P%G006:%2B%#-%:%6<br>!"#$%&GG()%*<br>!"#$%&G("$.4(5(%("8(.*%I+"1#+$1( ?<br>!+GG,-#..GI00,G* =LLO<br>12 34452-6IG,.5%6G2#%I%,%6:%20,B46-I4G-%<br>12 A;.B20,B46-I4G-%<br>12 C0:%2G()%20,B46-I4G-%<br>=LLO =LLO =LLO<br>+&G-%N%2B%#-%:%6<br>"5N4GG%2#%I&I-D#4,%2B%#-%:%6<br>"5N4GG%2#%I&I-D#4,%2B%#-%:%62B%5%%6G%<br>!"#$%&GG()%* !"#$%&GG()%*<br>9+"8(:1;7(.-+%$1; L%4(18#G+%7$%(I1*<br>Q%I&I-D#4,%2B%#-%<br>!+GG,-#..GI00,G*<br>12 344524,#%-:I54,DG,%B-0<br>12 C0:%24,#%-:I54,DG,%B-0<br>?<br>!"#$%&GG()%* ?<br><(I1*"+:(.-+%$1; =LLO<br>=LLO =LLO =LLO ?LLO ?LLO ?LLO<br>!"#$%&GG()%* !"#$%&GG()%*<br>?(G(("$( ?(41(8<br>!+GG,-#..GI00,G* !+GG,-#..GI00,G*<br>!"#$%&GG()%* ?LLO 12 34452B%5%%6G% 12 34452B%#-%:<br>=+G("3(%71"I 12 C0:%2B%5%%6G% 12 C0:%2G()%2B%#-%:<br>=LLO<br>?<br>?<br>=LLO<br>!"#$%&GG()%*<br>9*7+:(.-+%$1; !"#$%&GG()%*<br>=LLO @1;7<br>!+GG,-#..GI00,G*<br>12 34452M-$D<br>**----- End of picture text -----**<br>


**Figuur 34. Instrumentengidsen Dennis & Eva** 

**==> picture [453 x 322] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&''()%*<br>!"#$%<br>!"#$%&''()%* !"#$%&''()%*<br>!"#$%&'$"$#()*" !"#$%&+,-.$*()*"<br>!+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 30&4'-%05I&6H-$7-89 12 348;%8&0;%2L?"<br>12 :0I'&0;% 12 348;I8445<br>12 <008)=44'I8445 12 30&4'-%05I&6H-$7-892#.-'%8=48;<br>12 :0I'&0;%2#.-'%8=48;<br>12 @%9-084452#.-'%8=48;<br>12 <008)=44'I84452#.-'%8=48;<br>!"#$%&''()%*<br>!"#$%&''()%* !"#$%&''()%* !"#$%&''()%* !"#$%&''()%*<br>3.#)).)"#$%&+,-.$*()*"<br>3.#)).)"#$% 20%.+,%)"#$% !*./00#"*,11$#)"#$% 20%.+,%)"#$%&+,-.$*()*"<br>!+''H-#..'I00H'*<br>!+''H-#..'I00H'* !+''H-#..'I00H'* !+''H-#..'I00H'* !+''H-#..'I00H'*<br>12 B.-I8.55%H2#.-'%8=48;<br>12 B.-I8.55%H 12 :0I'#.I8.55%H 12 +8'A00H;8.55%H 12 :0I'#.I8.55%H2#.-'%8=48;<br>12 ?'H44'84452#.-'%8=48;<br>12 B.-I8.55%H'0%70%9-89<br>12 C44520)%8#4H%2H.-5'%<br>12 ?'H44'8445<br>**----- End of picture text -----**<br>


**Figuur 35. Instrumentengidsen Dennis & Eva** 

## **4.18 Conceptueel gegevensdeelmodel Adresgegevens** 

In dit gegevensdeelmodel worden de basismodellering van een adres weergegeven. 

Een adres is een Nederlands of een buitenlands adres. Een Nederlands adres kan een straatadres, een postbusadres of een antwoordnummeradres zijn. Bij een buitenlands adres wordt een straatadres en een postbusadres onderscheiden. 

Deze basismodellering wordt gebruikt voor alle adressen in het SUWI-Gegevensmodel. 

**==> picture [451 x 221] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%!&$''()"*+%,#(-../<br>!"#$%F''()%*<br>'&("#&")*&+,-&$."II*&+<br>!+''H-#..'I00H'*<br>12 90%:$;;H28%)06%H-672$;;HI'.:<br><0HH%I)068%6'-%;8H%I2#.-'%6>;68 12 <08%2H%8%62-6IF4H-$5-672068%H6%3-67=-6I'%>>-67<br>12 <08%2H%8%62.-'IF4H-$5-672068%H6%3-67=-6I'%>>-67<br>!"#$%F''()%* IJJO IJJO !"#$%F''()%* 12 <08%2'()%2068%H6%3-67=-6I'%>>-67<br>!"#$%%& <0HH%I)068%6'-%;8H%I 0(#"$ 12 ?;'.32;;65;672068%H6%3-67<br>12 ?;'.32%-68%2068%H6%3-67<br>!+''H-#..'I00H'* IJJO IJJO 12 ?;'.32-6IF4H-$5-672068%H6%3-67=-6I'%>>-67<br>12 "3IF4H-$5-672.-'7%#H%-8%2H%F4'I50H3 M%-'%>-$:2;8H%I 12 @68-F;'-%2%F0603-IF42;F'-%A<br>IJJO IJJO IJJO IJJO 1212 @68-F;'-%2A;->>-II%3%6'2068%H6%3-67=-6I'%>>-67@68-F;'-%20)4%AA-672068%H6%3-67=-6I'%>>-67<br>M%-'%>-$:2;8H%I2#.-'%6>;68 12 @68-F;'-%2I.HI%;6F%2068%H6%3-67=-6I'%>>-67<br>IJJO IJJO 12 "3IF4H-$5-672I';'.';-H%2B%'%><br>?03-F->-%2;8H%I 12 @6IF4H-$5-67I6.33%H2:;3%H25;62:00)4;68%><br>12 "3IF4H-$5-672H%F4'I50H32C;68%>IH%7-I'%H<br>IJJO IJJO<br>O O<br>O O<br>!"#$%F''()%*<br>0(#"$1%2(*&+<br>!+''H-#..'I00H'*<br>12 ?;'.32;;65;672;8H%I<br>12 ?;'.32%-68%2;8H%I<br>OJJL 12 D0%>-F4'-672H%8%62;AE-$:%6829FGH;8H%I OJJL<br>**----- End of picture text -----**<br>


**Figuur 36. Adresmodellering in relatie tot Persoon of Onderneming/Instelling** 

**==> picture [452 x 282] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%&GG()%*<br>!"#$%<br>!"#$%&GG()%* !"#$%&GG()%*<br>!"#$%&.$"$#,-+" !"#$%&'()*$+,-+"<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 A06%2<%9%%5G% 12 3456%5&06%278"<br>12 B-IGH-&G 12 3456I5449<br>12 C%9%%5G%6%%= 12 30&4G-%09I&:H-$;-5<2#.-G%5=456<br>12 C%9%%5G%5449 12 L0IG&06%2#.-G%5=456<br>12 76%5G-D-&4G-%&06%25.99%H4456.-6-5< 12 ?%<-054492#.-G%5=456<br>12 76%5G-D-&4G-%&06%2;%H#=-$D)=44GI 12 @005)=44GI54492#.-G%5=456<br>12 30&4G-%09I&:H-$;-5<<br>12 L0IG&06%<br>12 @005)=44GI5449<br>!"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%* !"#$%&GG()%*<br>/*#--*-"#$% 01%*'(%-"#$% !+*211#"+(33$#-"#$% /*#--*-"#$%&'()*$+,-+" 01%*'(%-"#$%&'()*$+,-+"<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 +456.-6-5<2#-$2:.-I5.99%H 12 L0IG#.I5.99%H 12 +5GG00H65.99%H 12 N.-I5.99%H2#.-G%5=456 12 L0IG#.I5.99%H2#.-G%5=456<br>12 N.-I=%GG%H 12 8GH44G54492#.-G%5=456<br>12 N.-I5.99%H<br>12 N.-I5.99%HG0%;0%<-5<<br>12 F44920)%5#4H%2H.-9G%<br>12 8GH44G5449<br>12 @005#00G;%HG-$H-5<2IJOOLM<br>12 @005G4<%5;%HG-$H-5<<br>**----- End of picture text -----**<br>


**Figuur 37. Adresgegevens** 

## **4.19 Conceptueel gegevensdeelmodel SUWI-algemeen** 

In dit gegevensdeelmodel worden de algemene procesgegevens weergegeven die binnen Suwinet van belang zijn. 

In dit gegevensdeelmodel is vastgelegd: 

- welke partijen betrokken zijn bij het arbeidstoeleidingstraject voor een bepaalde cliënt (UWV en GSD); 

- welke vestiging en welke contactpersoon/-afdeling per partij voor de betrokken cliënt bij de arbeidstoeleiding betrokken is. De contactgegevens omvatten: adres, telefoonnummer en e- mail adres van de contactpersoon/-afdeling; 

- wanneer de cliënt zich voor dienstverlening heeft gemeld bij het UWV WERKbedrijf en wanneer er een intake voor werk en/of inkomen heeft plaatsgevonden. 

**==> picture [450 x 427] intentionally omitted <==**

**----- Start of picture text -----**<br>
!"#$%FGG()%* !"#$%FGG()%* !"#$%FGG()%*<br>)$.'6..I6(A?4.%3(.6I"# 12324()*+, )$I..$.6I"#<br>!+GGH-#..GI00HG* !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 TRL=-@2=4H%I 12 304%2?0@0L289:; 12 +=74.-4-762#-$2G.-I7.LL%H<br>12 ;74-F=G-%2500H?%.H2%RL=-@2=4H%I 12 <==L2?0@0L289:; 12 I.-I@%GG%H<br>12 ;74-F=G-%289:;2%RL=-@2=4H%I 12 <==L2?0@0L289:;2A5%H?0HGB 12 I.-I7.LL%H<br>12 I.-I7.LL%HG0%50%6-76<br>MNNV O 12 <==L20)%7#=H%2H.-LG%<br>12 8GH==G7==L<br>MNNV<br>TRL=-@2=4H%I2F07G=FG)%HI007 12 :007#00G5%HJ-$O-762LMNNOP<br>=N4%@-76 !"#$%FGG()%* 12 :007J=6%75%HJ-$O-76<br>MNNO -.I$%0()*+,<br>!"#$%FGG()%* MNNV MNNO !+GGH-#..GI00HG*<br>;2'$.K$="I#22'>?.@6"3%'& 12 304%2)=HG-$289:;<br>O 12 <==L2)=HG-$289:;<br>!+GGH-#..GI00HG*<br>12 <==L2F07G=FG)%HI007QR=N4%@-76 O !"#$%<br>O 30HH%I)074%7G-%=4H%I !"#$%FGG()%*<br>MNNO MNNO MNNV<br>56I"#(7"6"I3.'6<br>MNNO<br>U%O0%?=4H%I<br>!+GGH-#..GI00HG*<br>S%@%N0077.LL%H<br>F07G=FG)%HI0072=N4%@-76 MNNO 12 304%26%L%%7G%<br>MNNV 12 C-IGH-FG<br>12 D%L%%7G%4%%@<br>!"#$%FGG()%* 30HH%I)074%7G-%=4H%I 12 D%L%%7G%7==L<br>O<br>P=X7.LL%H !"#$%&%'&()*+, O MNNO 12 ;4%7G-N-F=G-%F04%27.LL%H==74.-4-76<br>F07G=FG)%HI0072=N4%@-76 12 ;4%7G-N-F=G-%F04%25%H#@-$N)@==GI<br>!+GGH-#..GI00HG* 12 F0F=G-%0LIFGH-$5-76<br>12 304%25%IG-6-76289:; U%O0%?=4H%I 12 H0IGF04%<br>MNNV MNNV 12 <==L25%IG-6-76289:; 12 :007)@==GI7==L<br>O MNNO<br>!"#$%FGG()%*<br>)$.'6..I6($"3"@22''944"I<br>!+GGH-#..GI00HG* !"#$%FGG()%* !"#$%FGG()%*<br>12 304%2G()%2G%@%N0077.LL%H -2#$89#.6I"# 5'$:22I6'944"I.6I"#<br>12 ;74-F=G-%26%G%-L2G%@%N0077.LL%H<br>12 ;74-F=G-%2500H?%.H2G%@%N0077.LL%H !+GGH-#..GI00HG* !+GGH-#..GI00HG*<br>12 S%@%N0072@=747.LL%H 12 H0IG#.I7.LL%H 12 +7GJ00H47.LL%H<br>12 S%@%N0077.LL%H<br>**----- End of picture text -----**<br>


## **Figuur 38. Algemene procesgegeven** 

## **5. STANDAARDSTRUCTUREN** 

## **5.1 Toelichting op de standaardstructuren** 

In dit hoofdstuk worden de standaardstructuren gepresenteerd waarnaar wordt verwezen in het SGR. De standaardstructuren zijn oorspronkelijk afkomstig uit het STUCON-register. 

Standaardstructuren worden op onderstaande wijze beschreven: 

## 1. _Naam_ 

De naam moet achtereenvolgens aan de volgende voorwaarden voldoen: 

- de naam is uniek; 

- er wordt gebruik gemaakt van algemeen ingeburgerde namen. 

## 2. _Omschrijving_ 

   - Verduidelijking en definiëring van de structuur in de Nederlandse taal met eventueel gebruikmaking van het termenregister. 

3. _Formaat_ 

Het formaat wordt aangegeven door middel van de volgende notatie, waarin de cijfers slechts als voorbeeld dienen: 

|N6|6 numerieke tekens, vaste lengte|
|---|---|
|A3|3 alfabetische tekens, vaste lengte|
|AN5|5 alfanumerieke tekens, vaste lengte|
|N..9|maximaal 9 numerieke tekens|
|A..6|maximaal 6 alfabetische tekens|
|AN..35|maximaal 35 alfanumerieke tekens|



Bij standaardstructuren die zijn samengesteld uit meerdere attributen wordt in plaats van deze notatie vermeld: “Zie samenstellende delen”. 

De numerieke tekens zijn de Arabische cijfers 0 tot en met 9. 

De alfabetische tekens zijn alle niet-numerieke tekens en betreffen de kleine letters, de hoofdletters en overige tekens (inclusief besturings- en/of speciale tekens). 

De alfanumerieke tekens zijn zowel de numerieke als de alfabetische tekens. 

Bij numerieke tekens is het formaat exclusief: 

- decimaal teken 

- positief/negatief teken 

- scheidingsteken voor drietallen. 

## 4. _Structuur_ 

Bevat de beschrijvingen van te volgen structurele voorwaarden wanneer verschillende attributen samenhangend gehanteerd worden. 

Voor het beschrijven van de samenstelling geldt de volgende syntax: 

<naam1> = <naam2> + <naam3> + ... + <naam n> 

<naam1> is de naam van de standaardstructuur, de namen 2 t/m n zijn de namen van de samenstellende attributen. 

In de samenstelling kunnen voorts de volgende symbolen worden gebruikt: 

{} iteratie van hetgeen zich tussen de accolades bevindt, 

[ | ] groepering met daarbinnen minimaal twee groepen, gescheiden door "|",  waarbij òf de ene òf de andere groep geldt, 

() optionele gegevens; deze gegevens komen 0 of 1 maal voor, 

*..* commentaar. 

Voorbeeld: 

STANDAARD ADRES NEDERLAND  = * straatadres * 

(  LOCATIEOMSCHRIJVING  ) + STRAATNAAM  + [  HUISNUMMER  + (  HUISNUMMERTOEVOEGING ) | WOONBOOTVERWIJZING  |  WOONWAGENVERWIJZING  ] + POSTCODE  + PLAATSNAAM  + (  GEMEENTENAAM  ) 

De standaardstructuren geven de complete samenstelling van een structuur weer. Een aantal van de samenstellende attributen hoeft geen enkele relatie met andere componenten (klassen, attributen e.d.) te hebben. Voor de volledigheid zijn beschrijvingen van deze elementen wel opgenomen. Dergelijke elementen zijn aangegeven in de samenstelling van een standaardstructuur door middel van de tekst "* structuurelement *". 

## _Opmerkingen_ 

Hierin zijn opmerkingen opgenomen die in de andere rubrieken op generlei wijze onder te brengen zijn. 

## **5.2 Standaardstructuur Adres Nederland** 

**Omschrijving** Standaardstructuur voor een Nederlands adres, gebaseerd op het "Besluit standaardadressering" van de Minister van Binnenlandse Zaken d.d. 22 februari 1988 en neergelegd in de NEN 5825. 

**Formaat** 

Zie samenstellende delen. 

**Structuur** Afhankelijk van het soort adres bevat de structuur de attributen zoals hieronder aangegeven: 

STANDAARD ADRES NEDERLAND  = * straatadres * 

(  LOCATIEOMSCHRIJVING  ) + 

STRAATNAAM  + 

[  HUISNUMMER  + (  HUISNUMMERTOEVOEGING  ) 

- |  WOONBOOTVERWIJZING  |  WOONWAGENVERWIJZING  ] + 

POSTCODE  + 

WOONPLAATSNAAM  + 

(  GEMEENTENAAM  ) 

## **of** 

STANDAARD ADRES NEDERLAND  = * postbusadres * 

(  LOCATIEOMSCHRIJVING  ) + 

POSTBUSNUMMER  + 

POSTCODE  + 

WOONPLAATSNAAM  + 

(  GEMEENTENAAM  ) 

## **of** 

STANDAARD ADRES NEDERLAND  = * antwoordnummeradres * 

(  LOCATIEOMSCHRIJVING  ) + 

ANTWOORDNUMMER  + 

POSTCODE  + WOONPLAATSNAAM  + 

(  GEMEENTENAAM  ) 

## **of** 

STANDAARD ADRES NEDERLAND  = * verkort adres * 

(  LOCATIEOMSCHRIJVING  ) + 

[  HUISNUMMER  + (  HUISNUMMERTOEVOEGING  ) 

|  WOONBOOTVERWIJZING  |  WOONWAGENVERWIJZING  ] + POSTCODE 

- **Opmerkingen** 1. Gebruikmaking van de LOCATIEOMSCHRIJVING  kan om verschillende redenen wenselijk dan wel noodzakelijk zijn. Het HUISNUMMER kan ontbreken of men wil niet-uiterlijk waarneembare kenmerken, zoals toevoegingen voor nadere differentiatie achter de voordeur, vermelden. 

- 2. De attributen WOONBOOTVERWIJZING  en WOONWAGENVERWIJZING dienen uitsluitend te worden gebruikt indien de woonboot respectievelijk de woonwagen niet voorzien is van de gebruikelijke huisnummeraanduiding. 

- 3. Een DOMICILIEADRES  kan geen postbusadres en ook geen antwoordnummeradres zijn. 

- 4. Een VERBLIJFADRES kan geen antwoordnummeradres zijn. 

## **5.3 Standaardstructuur Adres Buitenland** 

**Omschrijving** Standaardstructuur voor een buitenlands adres. **Formaat** Zie samenstellende delen. 

**Structuur** Afhankelijk van het soort adres bevat de structuur de attributen zoals hieronder beschreven: 

STANDAARD ADRES BUITENLAND  = * straatadres * 

- (  LOCATIEOMSCHRIJVING BUITENLAND  ) + 

- (  STRAATNAAM BUITENLAND  ) + 

- (  HUISNUMMER BUITENLAND  ) + 

- ( [ POSTCODE BUITENLAND  |  REGIONAAM BUITENLAND  ] ) + 

WOONPLAATSNAAM BUITENLAND  + 

- [  LANDENCODE ISO  |  LANDSNAAM  ] 

of 

STANDAARD ADRES BUITENLAND  = * postbusadres * 

- (  LOCATIEOMSCHRIJVING BUITENLAND ) + 

POSTBUSNUMMER BUITENLAND  + 

- ( [ POSTCODE BUITENLAND  |  REGIONAAM BUITENLAND ] ) + 

WOONPLAATSNAAM BUITENLAND  + 

- [  LANDENCODE ISO  |  LANDSNAAM  ] 

LANDENCODE ISO dient in principe altijd in STANDAARD ADRES BUITENLAND te worden opgenomen. Indien voor een bepaald land (nog) geen code in ISO 3166 staat vermeld, moet LANDSNAAM  worden ingevuld. 

POSTCODE BUITENLAND heeft de voorkeur boven REGIONAAM BUITENLAND. Pas als er geen POSTCODE BUITENLAND bekend is, mag REGIONAAM BUITENLAND worden ingevuld. 

**Opmerkingen** Er bestaat geen geldige afspraak in Nederland voor een standaardstructuur voor buitenlandse adressen. 

## **5.4 Standaardstructuur Bankrekeningnummer Buitenland** 

**Omschrijving** Standaardstructuur voor een BANKREKENINGNUMMER BUITENLAND. 

**Formaat** 

Zie samenstellende delen. 

**Structuur** STANDAARD BANKREKENINGNUMMER BUITENLAND  = 

[ ( IBAN + BIC ) | ( IBAN + BANKNAAM) | ( BANKREKENINGNUMMER BUITENLAND + BIC ) | ( LANDENCODE ISO + BANKREKENINGNUMMER BUITENLAND + BANKNAAM) ] 

**Norminstantie:** 

CGM 

**Opmerkingen -** 

## **5.5 Standaardstructuur Bedraggegevens** 

## **Omschrijving** 

## **Formaat** 

## **Structuur** 

Standaardstructuur voor gegevens die betrekking hebben op een bedrag. 

Zie samenstellende delen. 

STANDAARD BEDRAGGEGEVENS  = 

   - (  CODE MUNTEENHEID ) + 

   - WAARDE BEDRAG  + 

   - (  CODE PERIODE EENHEID GELDIGHEID BEDRAG ) 

1. WAARDE BEDRAG 

Er zijn geen voorloopnullen. 

2. Indien bij een waarde van een bedrag geen munteenheid  wordt opgegeven dan wordt de munteenheid beschouwd als EUR (euro). 

Conform de TABEL MUNTEENHEDEN  geldt voor de Euro een CODE KLEINERE MUNTEENHEID  = 2. Dit betekent dat een bedrag in dat geval altijd in **eurocenten** wordt weergegeven. 

Oorspronkelijk in euro vastgelegde bedragen dienen ten behoeve van de communicatie volgens STANDAARD BEDRAGGEGEVENS met 100 te worden vermenigvuldigd. 

3. CODE PERIODE EENHEID GELDIGHEID BEDRAG geeft aan dat een bedrag betrekking heeft op een bepaalde periode (bijvoorbeeld een brutoloon per uur of per week of per maand, etc.). 

## **Opmerkingen** 

Als bij een waarde van een bedrag een munteenheid wordt aangegeven (door middel van CODE MUNTEENHEID), dan houd wel rekening met de positie waar het decimaalteken (het aantal cijfers achter de komma) wordt geplaatst. 

In de TABEL MUNTEENHEDEN wordt door middel van CODE KLEINERE MUNTEENHEID aangegeven of een bedrag een komma heeft voor het derde (3), tweede (2) of het eerste (1) cijfer van rechts, of dat het geen komma (0) heeft. 

Norminstantie: ISO4217: 2001 

## **5.6 Standaardstructuur Telefoonnummer** 

**Omschrijving** Standaardstructuur voor attributen die een Nederlands telefoonnummer beschrijven. **Formaat** AN..15 

**Structuur** STANDAARD TELEFOONNUMMER = 

TELEFOON LANDNUMMER  +  TELEFOONNUMMER 

**Norminstantie** SGR 

**Opmerkingen** Het formaat van STANDAARDSTRUCTUUR TELEFOONNUMMER is AN..15 (alfanumeriek met maximaal 15 posities), zodat deze standaard voor alle mogelijk voorkomende telefoonnummers in Nederland en buitenland kan gelden. 

Op dit moment geldt voor de Nederlandse telefoonnummers de maximale lengte van 11 posities, zonder het Telefoon landnummer. Het formaat van telefoonnummers in buitenland is maximaal 15 posities, gebaseerd op Recommendation E.164 van ITU (International Telecommunication Union. 

## **5.7 Standaardstructuur Datum** 

## **Omschrijving** 

**Formaat** 

Standaardstructuur voor attributen die een datum beschrijven. 

N8 

- **Structuur** 1. De datum is in ISO 8601 gedefinieerd als een bepaalde dag van een kalenderjaar, weergegeven door het volgnummer binnen een kalendermaand binnen dat jaar. Het kalenderjaar is daarbij het jaar volgens de Gregoriaanse kalender, die in 1582 werd ingevoerd om een fout in de Juliaanse kalender te corrigeren. 

   2. De schrijfwijze in numerieke vorm van datum luidt: EEJJMMDD. 

De numerieke inhoud moet voldoen aan: 

- EE =  00 t/m 99 

- - JJ =  00 t/m 99 - MM =  00 indien DD, EE en JJ ook 00 zijn =  01 t/m 12 

- - DD =  00 indien MM, EE en JJ ook 00 zijn 

=  01 t/m 28 

=  29 behalve wanneer MM=02 én JJ geen 4- voud of MM=02 én JJ=00 én EEJJ geen 400-voud =  30 behalve wanneer MM = 02 =  31 behalve wanneer MM = 02, 04, 06, 09 of 

11 

Deze schrijfwijze voldoet aan ISO 8601 (Complete representation, basic format). 

3. Als de datum niet van toepassing is, dan wordt standaardwaarde 00000000 ingevuld. 

**Opmerkingen** Geen. 

## **5.8 Standaardstructuur Tijdstip** 

## **Omschrijving** 

## **Formaat** 

Standaardstructuur voor attributen die een moment van de dag, in uren, minuten, seconden en delen van een seconde aangeven. 

N8 

## **Structuur** 

De schrijfwijze van dit tijdstip in numerieke vorm luidt: HHMMSSDD 

De numerieke inhoud moet voldoen aan: 

- HH = 00 t/m 23 - MM = 00 t/m 59 - SS = 00 t/m 59 - DD = 00 t/m 99 

## **Opmerkingen** 

Deze schrijfwijze is inhoudelijk conform ISO 8601 (Complete representation, basic format). In de ISO 8601 is de schrijfwijze: HHMMSS,DD. 

De standaardstructuur  STANDAARD TIJDSTIP  gaat, net als de ISO 8601, uit van de 24-uurs notatiewijze. 

In de praktijk komt het vaak voor dat in een gegevensuitwisseling een tijdstip minder precies hoeft te worden doorgegeven dan tot in honderdsten van een seconde. Afhankelijk van de mate van precisie geldt voor de onderdelen MM, SS en DD in  STANDAARD TIJDSTIP de default-waarde "00". 

Voorbeeld: 9 uur en 48 minuten wordt volgens de standaard doorgegeven als: 09480000. 

## **6. NORMINSTANTIES EN BEHERENDE INSTANTIES** 

## **6.1 Definitie norminstantie** 

Op elke Itemchart van een klasse of attribuut is een norminstantie vermeld. Het gaat hier in beginsel om de organisatie die verantwoordelijk is voor de normering van het gegeven of de conventie waarop deze normering is gebaseerd. 

Dit kan zijn een internationale of nationale standaardiseringorganisatie, een externe organisatie die een bepaalde standaard onderhoudt of een organisatie binnen het SUWI-domein die primaire eigenaar is van het gegeven, en uitdien hoofde een rol vervult bij de definiëring van het gegeven. Voor gegevens waarvoor geen geschikte norminstantie aan te wijzen is, en voor gegevens binnen het SUWI-domein die een kolomoverstijgend belang hebben, vervult het SGR zelf die rol. 

Het beleid ten aanzien van het aanwijzen van een norminstantie is als volgt: 

1. In eerste instantie is de authentieke bron voor het gegeven ook de norminstantie. 

2. Is deze niet voorhanden dan wordt gezocht of er voor een gegeven een bruikbare en geaccepteerde internationale of nationale norm (NEN/ISO-norm) aanwezig is. 

3. Is deze er niet, of niet geschikt, en heeft meer dan één partij het gegeven nodig in het primaire proces, dan wordt de definitie door de partijen gezamenlijk vastgesteld onder coördinatie van het BKWI. Het SGR wordt dan aangegeven als norminstantie. 

4. Vervolgens wordt binnen de SUWI-partijen gekeken waar het gegeven binnen het primaire proces gebruikt wordt. Is dit duidelijk bij één partij, dan wordt deze partij norminstantie voor het gegeven. 

## **6.2 Overzicht norminstanties** 

Momenteel kent het SGR de volgende categorieën standaarden en daarbij onderkende norminstanties: 

- Formele standaarden van organisaties die zich specifiek bezighouden met internationale en nationale standaardisering: 

   - ISO: International Organisation for Standardization; 

   - NEN: Nederlands Normalisatie-instituut. 

- SGR als standaard binnen het SUWI-domein en als norminstantie voor genoemde gegevenscategorieën. 

- Standaarden en conventies op het niveau van de kolommen binnen het SUWI-domein: 

   - CGM (Canoniek Gegevensmodel): standaard onder verantwoordelijkheid van UWV; 

   - GFO/GGR (Gemeenschappelijk Functioneel Ontwerp/Gemeentelijk Gegevens Register): dit betreft standaarden die in het verleden ontwikkeld zijn voor het gemeentelijke domein, maar die thans niet meer worden onderhouden. Hiervoor is derhalve feitelijk momenteel geen norminstantie beschikbaar in bedoelde zin; 

- Externe partijen met voor de gegevensuitwisseling bepalende standaarden: 

   - 

   - Rijksdienst voor Identiteitsgegevens - Basisregistratie Personen 

- Kadaster - Basisregistratie Kadaster 

- Kamer van Koophandel - Handelsregister 

- Rijksdienst Wegverkeer - Basisregistratie Voertuigen 

- Dienst Uitvoering Onderwijs 

- Belastingdienst 

- Centraal Bureau voor de Statistiek 

## **6.3 Definitie beherende instantie** 

Voor een aantal tabellen en gegevens in het SGR wordt het waardebereik beheerd door een instantie. Doorgaans is dit ook de norminstantie voor de betrokken gegevens. In dit kader wordt de aanduiding beherende instantie gebruikt. 

## **7. AANVULLENDE SUWIML-TAGS** 

Op iedere Itemchart in het SGR wordt de SuwiML-tag van het betreffend gegeven vermeld. Hiernaast zijn er nog tags die niet op een Itemchart vermeld staan. 

Het gaat hier onder meer om de naam van de rol die een klasse in een relatie heeft, waarbij het onderkennen van die rol kenmerkend is voor die relatie. We zien bijvoorbeeld drie relaties tussen PERSOON en ADRES. ADRES heeft in elke relatie een andere rol, achtereenvolgens DOMICILIEADRES, FEITELIJK ADRES en CORRESPONDENTIEADRES. Deze rolinstanties van ADRES hebben een eigen SuwiML-tag gekregen. 

Een aantal voorbeelden extra tags is opgenomen in de volgende tabel: 

|**Naam**|**Soort**|**SuwiML-tag**|
|---|---|---|
|Domicilieadres<br>Feitelijk adres<br>Correspondentieadres<br>Postadres<br>Bezoekadres<br>Bezoekadres hoofdvestiging<br>Correspondentieadres<br>hoofdvestiging<br>Garant<br>Onderhoudsplichtige<br>Rekeninghouder<br>Schuldenaar<br>Begunstigde|Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie ADRES<br>Rolinstantie PERSOON<br>Rolinstantie PERSOON<br>Rolinstantie PERSOON<br>Rolinstantie PERSOON<br>Rolinstantie PERSOON|Domicilieadres<br>Feitelijkadres<br>Correspondentieadres<br>Postadres<br>Bezoekadres<br>BezoekadresHoofdvestiging<br>CorrespondentieadresHoofdvestiging<br>Garant<br>Onderhoudsplichtige<br>Rekeninghouder<br>Schuldenaar<br>Begunstigde|



## **BIJLAGE 1 OVERZICHT SGR-GEGEVENS - WETTELIJKE GRONDSLAG** 

## **BIJLAGE 2 TABEL BERICHTENINDEX** 

## **BIJLAGE 3A OVERZICHT GEGEVENS GETOOND OP KLANTBEELD DIGITAAL KLANTDOSSIER** 

## **BIJLAGE 3B VERTALING IN BEGRIJPELIJKE TAAL VAN GEGEVENS OP KLANTBEELD DIGITAAL KLANTDOSSIER** 

