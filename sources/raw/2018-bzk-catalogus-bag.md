---
title: "Catalogus BAG 2018"
source: "https://imbag.github.io/catalogus/"
author: "Ministerie van Binnenlandse Zaken en Koninkrijksrelaties"
published: 2018-03-29
created: 2026-06-25
description: "Systeembeschrijving van de Basisregistratie Adressen en Gebouwen, vastgesteld door de minister van BZK."
tags:
  - "bag"
  - "basisregistraties"
---

# Catalogus BAG 2018

Systeembeschrijving van de Basisregistratie Adressen en Gebouwen

Deze website bevat de onlineversie van de Catalogus BAG 2018 zoals vastgesteld door de minister van Binnenlandse Zaken en Koninkrijksrelaties op 29 maart 2018.

## 1 Inleiding

Deze catalogus beschrijft hoe informatie over adressen en gebouwen moet worden vastgelegd voor landelijke uitwisseling. De catalogus beoogt uniformiteit in objectafbakening en bijhouding te bevorderen.

In 2018 ontstond deze catalogus na samenvoeging van de Catalogus BAG 2009 met gerelateerde documenten, inclusief wijzigingen voortvloeiend uit de aangepaste Wet basisregistratie adressen en gebouwen (ingangsdatum 1 juli 2018).

De catalogus bevat uitgangspunten en voorschriften voor eenduidige objectvastlegging, ontwerpprincipes, algemene principes, gegevenskwaliteit, objectgegevens en gegevensdefinities.

### 1.1 De Basisregistratie Adressen en Gebouwen

Sinds 2009 hebben gemeenten de wettelijke taak om basisgegevens over adressen en gebouwen bij te houden in de BAG.

De Basisregistratie Adressen functioneert als overzichtstabel van officiële adressen binnen de Nederlandse overheid. Drie objecten vormen gezamenlijk een adres: Woonplaats, Nummeraanduiding en Openbare ruimte. "Adressen worden daarbij aangemerkt als een vereenvoudigde officiële naamgeving van een beperkt aantal objecten."

Officiële adressen kunnen alleen aan drie adresseerbare objecttypen worden toegekend: Verblijfsobject, Ligplaats en Standplaats.

De Basisregistratie Gebouwen registreert alle gebouwen-gerelateerde objecten: Pand, Verblijfsobject, Ligplaats en Standplaats.

Na evaluatie door de Auditdienst Rijk (2013-2014) werden beide registraties samengevoegd tot één basisregistratie: de Basisregistratie Adressen en Gebouwen.

### 1.2 Doel

De BAG behoort tot het landelijk stelsel van basisregistraties, gericht op betere informatievoorziening in Nederland.

Het voornaamste doel is het uniek identificeren van adresseerbare objecten en panden, waarbij een duidelijke relatie ontstaat tussen adressering en object. Dit bevordert eenduidige relaties tussen verschillende registraties.

"Registratie in de BAG heeft overigens uitdrukkelijk uitsluitend een administratieve achtergrond en houdt geen legalisering of ander (rechts)gevolg in."

### 1.3 Gebruik

De BAG vormt de kern van de overheidsgegevenshuishouding en is verplicht te gebruiken. Dit verbetert consistentie van objecten in overheidsprocessen en maakt koppeling van gegevens mogelijk.

Een verplichting voor terugmelding bij twijfel over gegevensrechtmatigheid, gecombineerd met gebruiksplicht, fungeert als instrument om kwaliteit te vergroten.

## 5 Conceptueel model

Het conceptueel gegevensmodel toont de onderlinge relaties tussen objecttypen, attributen en hun samenhang.

Objecttypen met een schuingedrukte naam zijn abstracte objecttypen. Deze komen niet als concreet object voor in een BAG-product.

Deze abstracte typen vormen de basis waarvan alle BAG-objecttypen de eigenschappen overerven. Dit zorgt voor een coherente structuur in het gehele model.

## 6 Objecttypen

### 6.1 Woonplaats

Een Woonplaats is "een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente."

Attributen: identificatie [1], naam [1], geometrie [1], status [1], geconstateerd [1], documentdatum [1], documentnummer [1].

### 6.2 Openbare ruimte

Een Openbare ruimte is "een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen."

Voorbeelden zijn wegen, water, spoorbanen en landschappelijke gebieden.

Attributen: identificatie [1], naam [1], type [1], status [1], geconstateerd [1], documentdatum [1], documentnummer [1].

Relaties: ligt in gerelateerde woonplaats [1].

### 6.3 Nummeraanduiding

Een Nummeraanduiding is "een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats."

Attributen: identificatie [1], huisnummer [1], huisletter [0..1], huisnummertoevoeging [0..1], postcode [0..1], type adresseerbaar object [1], status [1], geconstateerd [1], documentdatum [1], documentnummer [1].

Relaties: ligt in gerelateerde woonplaats [0..1], ligt aan gerelateerde openbare ruimte [1].

### 6.4 Pand

Een Pand is "de kleinste, bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is."

Attributen: identificatie [1], geometrie [1], oorspronkelijk bouwjaar [1], status [1], geconstateerd [1], documentdatum [1], documentnummer [1].

### 6.5 Adresseerbaar object

Een Adresseerbaar object is "een (abstract) object waaraan adressen kunnen worden toegekend."

Dit omvat Standplaatsen, Ligplaatsen of Verblijfsobjecten.

Relaties: heeft als hoofdadres [1], heeft als nevenadres [0..*].

### 6.6 Ligplaats

Een Ligplaats is "een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object."

Attributen: identificatie [1], status [1], geometrie [1], geconstateerd [1], documentdatum [1], documentnummer [1].

### 6.7 Standplaats

Een Standplaats is "een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte."

Attributen: identificatie [1], status [1], geometrie [1], geconstateerd [1], documentdatum [1], documentnummer [1].

### 6.8 Verblijfsobject

Een Verblijfsobject is "de kleinste binnen een of meer panden gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte."

Attributen: identificatie [1], geometrie [1], gebruiksdoel [1..*], oppervlakte [1], status [1], geconstateerd [1], documentdatum [1], documentnummer [1].

Relaties: maakt deel uit van gerelateerd pand [1..*].

## 7 Attributen & relaties

### 7.1 Woonplaats

- **identificatie** (11.03): Unieke aanduiding van een woonplaats, 4 karakters (0001-9999). Authentiek, identificerend, geen materiële/formele historie.
- **naam** (11.70): Benaming van door gemeentebestuur aangewezen woonplaats, max. 80 karakters. Authentiek, onderzoekbaar, materiële en formele historie.
- **geometrie** (11.71): Tweedimensionale representatie van woonplaatsomtrek als vlak of multivlak. Authentiek, onderzoekbaar, materiële en formele historie.
- **status** (11.79): Levenscyclusfase van woonplaats (type StatusWoonplaats). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (11.72): Indicatie of woonplaats via feitelijke constatering zonder brondocument is opgenomen. Basisgegeven, materiële en formele historie.
- **documentdatum** (11.77): Datum vastgesteld brondocument voor opname/mutatie/verwijdering. Basisgegeven, materiële en formele historie.
- **documentnummer** (11.78): Unieke aanduiding brondocument binnen gemeente, max. 40 karakters. Basisgegeven, materiële en formele historie.

### 7.2 Openbare ruimte

- **identificatie** (11.01): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **naam** (11.10): Naam toegekend via formeel gemeentelijk besluit, max. 80 karakters. Authentiek, onderzoekbaar, materiële en formele historie.
- **type** (11.16): Aard van openbare ruimte (TypeOpenbareRuimte). Authentiek, onderzoekbaar, materiële en formele historie.
- **status** (11.19): Levenscyclusfase (StatusNaamgeving). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (11.11): Indicatie feitelijke constatering zonder brondocument. Basisgegeven, materiële en formele historie.
- **documentdatum** (11.17): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (11.18): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.
- **Relatie: ligt in gerelateerde woonplaats** (11.15): Openbare ruimte ligt in woonplaats. Kardinaliteit [1], authentiek, onderzoekbaar, materiële en formele historie.

### 7.3 Nummeraanduiding

- **identificatie** (11.02): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **huisnummer** (11.20): Toegekende nummering, 1-99999. Authentiek, onderzoekbaar, materiële en formele historie.
- **huisletter** (11.30): Toevoeging aan huisnummer (A-Z, a-z), maximaal 1 karakter. Kardinaliteit [0..1], authentiek, onderzoekbaar, materiële en formele historie.
- **huisnummertoevoeging** (11.40): Nadere toevoeging, max. 4 alfanumerieke karakters. Kardinaliteit [0..1], authentiek, onderzoekbaar, materiële en formele historie.
- **postcode** (11.60): Door PostNL vastgestelde code, formaat: 4 cijfers + 2 hoofdletters. Kardinaliteit [0..1], basisgegeven, onderzoekbaar, kan geen waarde hebben, materiële en formele historie.
- **type adresseerbaar object** (11.66): Aard object waaraan nummeraanduiding is toegekend (TypeAdresseerbaarObject). Authentiek, onderzoekbaar, materiële en formele historie.
- **status** (11.69): Levenscyclusfase (StatusNaamgeving). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (11.21): Indicatie feitelijke constatering. Basisgegeven, materiële en formele historie.
- **documentdatum** (11.67): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (11.68): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.
- **Relatie: ligt in gerelateerde woonplaats** (11.61): Woonplaats van adresseerbaar object. Kardinaliteit [0..1], authentiek, onderzoekbaar, materiële en formele historie.
- **Relatie: ligt aan gerelateerde openbare ruimte** (11.65): Openbare ruimte waaraan adresseerbaar object ligt. Kardinaliteit [1], authentiek, onderzoekbaar, materiële en formele historie.

### 7.4 Pand

- **identificatie** (55.01): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **geometrie** (55.20): Minimaal tweedimensionale representatie bovenzicht omtrek (GM_Surface). Authentiek, onderzoekbaar, materiële en formele historie.
- **oorspronkelijk bouwjaar** (55.30): Jaar waarin pand als bouwkundig gereed is/wordt opgeleverd (Year). Authentiek, onderzoekbaar, materiële en formele historie.
- **status** (55.31): Levenscyclusfase (StatusPand). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (55.02): Indicatie feitelijke constatering. Basisgegeven, materiële en formele historie.
- **documentdatum** (55.97): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (55.98): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.

### 7.5 Adresseerbaar object

- **Relatie: heeft als hoofdadres** (100.51): Nummeraanduiding aangemerkt als hoofdadres. Kardinaliteit [1], authentiek, onderzoekbaar, materiële en formele historie.
- **Relatie: heeft als nevenadres** (100.52): Nummeraanduiding aangemerkt als nevenadres. Kardinaliteit [0..*], authentiek, onderzoekbaar, materiële en formele historie.

### 7.6 Ligplaats

- **identificatie** (58.01): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **status** (58.03): Levenscyclusfase (StatusPlaats). Authentiek, onderzoekbaar, materiële en formele historie.
- **geometrie** (58.20): Tweedimensionale representatie omtrek (GM_Surface). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (58.02): Indicatie feitelijke constatering. Basisgegeven, materiële en formele historie.
- **documentdatum** (58.97): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (59.98): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.

### 7.7 Standplaats

- **identificatie** (57.01): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **status** (57.03): Levenscyclusfase (StatusPlaats). Authentiek, onderzoekbaar, materiële en formele historie.
- **geometrie** (57.20): Tweedimensionale representatie omtrek (GM_Surface). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (57.02): Indicatie feitelijke constatering. Basisgegeven, materiële en formele historie.
- **documentdatum** (57.97): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (57.98): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.

### 7.8 Verblijfsobject

- **identificatie** (56.01): Unieke aanduiding via objectnummering. Authentiek, identificerend, geen materiële/formele historie.
- **geometrie** (56.20): Minimaal tweedimensionale representatie (PuntOfVlak). Authentiek, onderzoekbaar, materiële en formele historie.
- **gebruiksdoel** (56.30): Categorisering gebruiksdoelen volgens vergunning/constatering (Gebruiksdoel, kardinaliteit [1..*]). Authentiek, onderzoekbaar, identificerend, materiële en formele historie.
- **oppervlakte** (56.31): Gebruiksoppervlakte in hele vierkante meters (1-999999). Authentiek, onderzoekbaar, materiële en formele historie.
- **status** (56.32): Levenscyclusfase (StatusVerblijfsobject). Authentiek, onderzoekbaar, materiële en formele historie.
- **geconstateerd** (56.02): Indicatie feitelijke constatering. Basisgegeven, materiële en formele historie.
- **documentdatum** (56.97): Datum brondocument. Basisgegeven, materiële en formele historie.
- **documentnummer** (56.98): Unieke aanduiding brondocument, max. 40 karakters. Basisgegeven, materiële en formele historie.
- **Relatie: maakt deel uit van gerelateerd pand** (56.90): Panden waarvan verblijfsobject onderdeel uitmaakt. Kardinaliteit [1..*], authentiek, onderzoekbaar, materiële en formele historie.

### 7.9 Samengestelde attributen

**Objectnummering**: gemeentecode (4 karakters), objecttypecode (2 karakters), objectvolgnummer (10 karakters).

**PuntOfVlak**: Union-type, keuze tussen punt (GM_Point) of vlak (GM_Surface).

**VlakOfMultivlak**: Union-type, keuze tussen vlak (GM_Surface) of multivlak (GM_MultiSurface).

## 10 Objectafbakening

### 10.1 Inleiding

Dit hoofdstuk behandelt de regels voor herkenning van objecten in de BAG. Het beschrijft welke dingen uit de werkelijkheid door de BAG worden geregistreerd.

### 10.2 Toekenning van nummeraanduidingen

Verblijfsobjecten, standplaatsen en ligplaatsen hebben een hoofdadres en kunnen nevenadressen krijgen. Nevenadressen mogen alleen worden toegekend wanneer meerdere relevante toegangen aanwezig zijn met wezenlijke betekenis, zoals een leveranciersingang. Een nevenadres is een eigenschap van het gehele object, niet van gedeelten ervan.

### 10.3 Vaststelling van openbare ruimten

De vaststelling volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan. Bij nummeraanduidingen aan buitenlandse openbare ruimten registreert de gemeente deze alsof zij in de betreffende woonplaats zijn gelegen.

### 10.4 Indeling in woonplaatsen

De indeling volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan.

### 10.5 Afbakening van ligplaatsen

De afbakening volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan. Het daadwerkelijk gebruik van de plaats in het water is niet relevant voor afbakening.

### 10.6 Afbakening van panden

De bronhouder deelt een bouwkundige constructie op in bouwwerken en toetst elk afzonderlijk aan de panddefinitie.

**Bouwkundig-constructief zelfstandigheid:** Een bouwwerk is zelfstandig indien sloping geen aangrenzende constructies doet instorten. Elk bouwwerk in een serie gelijkvormige nabijgelegen constructies geldt als zelfstandig. Doorgangen tussen bouwwerken blijven buiten beschouwing bij zelfstandigheidsbeoordeling.

**Functioneel zelfstandigheid:** Een pand huisvest bij totstandkoming nul, een of meer complete verblijfsobjecten. Later kunnen verblijfsobjecten zich over meerdere panden uitstrekken.

**Directe verbinding met aarde:** Een pand moet directe constructieve verbinding hebben. Gestapelde panden zijn alleen mogelijk bij onderlinge bouwkundige zelfstandigheid.

**Duurzame verbinding met aarde:** Bouwwerken die naar aard en constructie verplaatsbaar zijn, kunnen geen pand zijn. Verplaatsbaarheid betekent dat onderdelen zonder scheiding kunnen worden aangevoerd of afgevoerd.

**Omsloten en dicht:** Een pand moet volledig door wanden omsloten zijn met dichte dakconstructie. Beweegbare delen (deuren, ramen, lichtkappen) gelden niet als permanente openingen.

**Betreedbaar:** Een pand moet voor mensen toegankelijk zijn en voldoende stahoogte bieden. Het moet verticale toegangsdeuren hebben.

**Kleinste eenheid:** Een pand moet ondeelbaar zijn en mag niet in kleinere pandeenheden kunnen worden opgedeeld.

**Uitzonderingen:** Bunkers worden pas afgebakend bij ingebruikname. Hobbykassen worden niet afgebakend. Militaire objecten worden niet afgebakend wanneer Minister van Defensie dit aangeeft.

### 10.7 Afbakening van standplaatsen

De afbakening volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan. Het daadwerkelijk gebruik van het terrein is niet relevant.

### 10.8 Afbakening van verblijfsobjecten

De bronhouder deelt panden of pandreeksen in ruimten en toetst elk aan de verblijfsobjectdefinitie. Dit gebeurt van binnenuit, waar de binnenste eigen toegang bepaalt waar een verblijfsobject begint.

**Binnenruimten binnen panden:** Een verblijfsobject bestaat uit een of meer binnenruimten binnen panden, conform NEN 2580:2007-definitie. Het verblijfsobject moet volledig omsloten zijn door wanden en dichte plafond-/dakconstructie en vloer.

**Aaneengesloten samenhangend gebruik:** Een eenheid moet ruimtelijk samenhangend zijn en exclusief alle vereiste basisvoorzieningen hebben.

Minimaal vereiste basisvoorzieningen per gebruiksdoel:
- Bijeenkomst, cel, gezondheid, kantoor, onderwijs, sport, winkel: water, toilet
- Logies: keuken, douche, toilet
- Industrie, overig: geen
- Wonen: keuken, douche, toilet

**Ontsluiting:** Het verblijfsobject moet via eigen afsluitbare toegangen ontsloten zijn: vanaf openbare weg, via eigen erf of via gedeelde verkeersruimte.

**Grootte en stahoogte:** Het verblijfsobject is voor mensen toegankelijk met voldoende stahoogte.

**Afsluitbare toegang:** Alle verblijfsobjecttoegang moet afsluitbaar zijn voor exclusief gebruik.

**Onderwerp goederenrechtelijke handelingen:** Ruimten die niet onderwerp kunnen zijn van transacties (hotelkamer, verzorgingshuiskamer, cel) gelden niet als verblijfsobject.

**Ondersteunend gebruik:** Exclusief ondersteunende ruimten (kelderbox bij flat) worden niet afgebakend.

**Kleinste eenheid:** Een verblijfsobject moet ondeelbaar zijn zonder opdeelbare subeenheden.
