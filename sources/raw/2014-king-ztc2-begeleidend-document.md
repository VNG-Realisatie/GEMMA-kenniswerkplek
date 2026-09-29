---
title: "GEMMA Zaaktypecatalogus 2 (ZTC2) — Begeleidend document v2.1"
source: "https://vng-realisatie.github.io/ImZTC/documenten/GEMMA_ZTC2_-_Begeleidend_document_v2.1.pdf"
source_page: "https://vng-realisatie.github.io/ImZTC/"
author: "KING Gemeenten"
published: 2014-07-01
created: 2026-06-27
description: "Begeleidend document bij de ZTC2: context, positionering, objecttypen en gebruik van de zaaktypecatalogus."
tags:
  - "Dienstverlening"
  - "Standaarden"
---

**GEMMA ZAAKTYPECATALOGUS 2 (VERSIE 2.1)** 

## **Begeleidend document** 

**==> picture [489 x 428] intentionally omitted <==**

**==> picture [103 x 52] intentionally omitted <==**

Opgesteld door KING Gemeenten Datum 1 juli 2014 Versie 2.1 

**==> picture [103 x 52] intentionally omitted <==**

## **Inhoud** 

|**1**|**Inleiding**|**Inleiding**|**4**|
|---|---|---|---|
|**2**|**De context van de Zaaktypecatalogus: van klant naar klant**||**5**|
||2.1|Producten en Dienstencatalogus (PDC)|5|
||2.2|(E-)Formulieren|6|
||2.3|GEMMA Referentieprocessen|7|
||2.4|Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ)|7|
||2.5|Standaard UitwisselingsFormaat Zaken (StUF-ZKN)|7|
||2.6|DSP of ZTC?|8|
|**3**|**Positionering van de Zaaktypecatalogus**||**9**|
||3.1|Producten- en DienstenCatalogus (PDC)|9|
||3.2|Formulieren|10|
||3.3|Referentieprocessen|10|
||3.4|Aansluiting op selectielijst|10|
|**4**|**Functie en gebruik van de Zaaktypecatalogus**||**12**|
||4.1|Functie|12|
||4.2|Het gebruik van de Zaaktypecatalogus|13|
|**5**|**Kenmerken van een zaaktype**||**17**|
||5.1|Vorm|17|
||5.2|Structuur op hoofdlijnen|17|
|**6**|**Beheer**||**21**|
||6.1|Sjablonen en modellen: KING|21|
||6.2|Referentiezaaktypen: KING|21|
||6.3|Generieke waardenlijsten, domeintabellen, etc.: KING / beheerders Catalogi|21|
||6.4|Inhoud: gemeente, sector, etc.|22|
||6.5|Validatie en landelijke publicatie van Zaaktypecatalogi: KING|22|
|**Bijlage 1: Sjabloon zaaktype**|||**24**|
|**Bijlage 2: Toelichting op het sjabloon**|||**31**|



**==> picture [103 x 52] intentionally omitted <==**

## **1 Inleiding** 

Gemeenten ontwikkelen zich tot de meest nabije overheid voor burgers, bedrijven en instellingen. Daarbij werken ze aan het verbeteren van hun publieke dienstverlening, de besturing, interne bedrijfsvoering en de ondersteunende informatievoorziening. 

Het is belangrijk om meer grip te krijgen op de processen: voor het behalen van gemeentelijke doelstellingen, het verbeteren van de dienstverlening of het verhogen van de efficiëntie en effectiviteit. Zaak- en procesgericht werken wordt hierbij als verbindend thema gezien. KING ondersteunt gemeenten bij deze ontwikkeling door middel van de GEMeentelijke Model Architectuur (GEMMA). De GEMMA-onderdelen geven kaders en richting voor het inrichten van gemeentelijke bedrijfs-  en informatiearchitectuur. Voor zaak- en procesgericht werken biedt KING onder andere de GEMMA Zaaktypecatalogus. 

Dit document beschrijft de visie van KING op de zaaktypecatalogus, de uitgangspunten, het gebruik, de opzet, en het informatiemodel van de GEMMA Zaaktypecatalogus 2. Deze documentversie (2.1) is de doorontwikkeling van versie 2.0 die tot stand gekomen is op basis van een brede review en bijdragen vanuit de Expertgroep ZTC van KING. Om de GEMMA Zaaktypecatalogus te kunnen verbeteren door het uitbrengen van nieuwe versies daarvan zonder de naam telkens te moeten veranderen, spreken we niet langer over ‘de ZTC 2.0’ maar over de ZTC2 (de 2[e] generatie zaaktypecatalogus) waarvan versie 2.1 nu voor ligt. 

De GEMMA Zaaktypecatalogus 2 bestaat uit de volgende onderdelen: 

- het Begeleidend document dat voor u ligt, 

- de Referentie-zaaktype-beschrijvingen (‘Bezwaar behandelen’, ‘Subsidieaanvraag behandelen’, etc.), die kunnen dienen als startpunt voor de uitwerking van eigen, daarvan afgeleide, zaaktypen, 

- een Sjabloon voor het specificeren van een zaaktype, ook te gebruiken voor ‘het goede gesprek’ over de vertaling van een proces naar een zaaktype en voor het registreren van het zaaktype in een applicatie, 

- een gedetailleerd informatiemodel (InformatieModel ZTC2), 

- de vertaling daarvan naar een uitwisselformaat (StUF-ZTC), 

- waardenlijsten voor de referentielijsten in IMZTC2 (i.c. ‘generieke documenttypen’), 

- een beschrijving van de wijze waarop de ZTC 2.0 beheerd wordt (het Beheermodel). 

## **Leeswijzer** 

- Hoofdstuk 2 vertrekt vanuit de vraag van ‘de klant’ en schetst welke (GEMMA)bouwstenen een bijdrage leveren aan het leveren van een antwoord op die vraag. 

- In hoofdstuk 3 wordt de relatie beschreven tussen de GEMMA Zaaktypecatalogus 2 en de andere (GEMMA-) bouwstenen. 

- In hoofdstuk 4n wordt nader ingegaan op de functie en het gebruik van de GEMMA Zaaktypecatalogus 2. 

- Hoofdstuk 5 beschrijft de vorm en structuur van de GEMMA Zaaktypecatalogus 2 op hoofdlijnen. 

- In hoofdstuk 6 wordt stilgestaan bij de verschillende producten en daarmee samenhangende beheeraspecten die de GEMMA Zaaktypecatalogus 2 met zich meebrengt. 

- In de bijlagen is het sjabloon, met een toelichting, opgenomen voor het specificeren van een zaaktype. 

**==> picture [103 x 52] intentionally omitted <==**

## **2 De context van de Zaaktypecatalogus: van klant naar klant** 

In deze paragraaf worden de bouwstenen beschreven die een rol spelen bij zaakgericht werken en zodoende van belang zijn voor de Zaaktypecatalogus. De bouwstenen zijn beschreven aan de hand van het logische verloop van een klantvraag: 

1. De klant zoekt het product dat voorziet in zijn behoefte/vraag; 

2. De klant bestelt het product; 

3. De overheid produceert het product, waarbij zij de klant op gezette tijden informeert over de voortgang; 

4. De overheid levert het product aan de klant; 

5. De overheid archiveert de gegevens over de bestelling, het productieproces en de levering. 

Het hierboven geschetste verloop sluit nauw aan bij dienstverleningsprocessen waarbij de ‘klant’ een burger of bedrijf is die een product vraagt en geleverd krijgt. Die ‘klant’ kan echter ook de samenleving zijn die - soms proactief, soms reactief - door de overheid wordt bediend: denk aan het beheer van de openbare ruimte (bijvoorbeeld het onderhouden van groenvoorzieningen) of het houden van toezicht en eventueel handhavend optreden (bijvoorbeeld toezicht op en handhaving van de parkeerverordening). In dergelijke gevallen is niet altijd sprake van het ‘zoeken’ of ‘bestellen’ van een product door een individuele klant. 

## **2.1 Producten en Dienstencatalogus (PDC)** 

Processen starten nooit spontaan, er is altijd een aanleiding voor. Bij processen die zich binnen overheidsorganisaties voltrekken, wordt die aanleiding vaak gevonden in wet- en regelgeving. De gemeente is beheerder van de openbare ruimte en dus verantwoordelijk voor het geven van toestemming voor het gebruik daarvan, bijvoorbeeld als er een evenement wordt georganiseerd. De gemeente is ook verantwoordelijk voor het registreren van haar bevolking en dient dus te worden geïnformeerd over de geboortes binnen de gemeentegrenzen. Uitkeringen worden, afhankelijk van de persoonlijke situatie, verstrekt door een gemeente of het UWV, etcetera. De verantwoordelijkheden, rechten en plichten omtrent al deze onderwerpen zijn door de overheid heel precies uitgewerkt in landelijke wetgeving en landelijke, regionale of lokale regelgeving. 

In de Producten- en Dienstencatalogi (PDC's) van overheidsorganisaties is deze wet- en regelgeving vertaald naar producten en diensten die de overheidsorganisaties leveren. 

Zo zal de organisator van een evenement een vergunning moeten vragen aan de overheid. En moet voor elk pasgeboren kind een geboorteakte worden gevraagd bij de burgerlijke stand. Iemand die aanspraak wil maken op een financiële ondersteuning van de overheid, vraagt een uitkering aan. 

Doorgaans zijn niet alle producten en diensten die overheidsorganisaties voortbrengen, terug te vinden in hun producten- en dienstencatalogus; veel overheidsorganisatie nemen alleen die producten en diensten op die door individuele burgers, bedrijven of instellingen kunnen worden aangevraagd of gemeld. Hierdoor blijven in de Producten- en Dienstencatalogi verschillende groepen producten en diensten buiten beeld: 

- Producten en diensten die de overheid proactief levert, zoals het voorinvullen van de belastingaangifte of het samenstellen en verstrekken van een pensioenoverzicht. 

- En, in het verlengde daarvan, producten en diensten die de overheid aan de maatschappij - het collectief - levert, zoals het aanleggen en onderhouden van een weg of het versterken van een waterkering, maar ook het beboeten van een fout- 

**==> picture [103 x 52] intentionally omitted <==**

parkeerder, het inspecteren van - de keuken in - een horecagelegenheid, het opsporen en beboeten van een illegale lozing van milieuverontreinigende stoffen. 

 Tot slot leveren overheidsorganisaties tal van producten en diensten aan de eigen - of een met de eigen organisatie samenwerkende - organisatie, zoals het inrichten van een werkplek, het vergoeden van declaraties, het verstrekken van adviezen, etc. 

Deze producten en diensten worden doorgaans niet opgenomen in een producten- en dienstencatalogus, terwijl de overheid wel degelijk processen uitvoert die dit soort producten en diensten voortbrengen. KING pleit ervoor de producten- en dienstencatalogi - van overheidsorganisaties uit te breiden met deze - nu nog onzichtbare - producten en diensten en deze te ontsluiten naar de relevante doelgroepen. Op deze manier heeft elke overheidsorganisatie op één plaats (in de PDC) alle producten en diensten inzichtelijk die door die organisatie worden voortgebracht. Producten- en Dienstencatalogus moet hier ruim worden opgevat; essentieel is dat de beschrijving van alle producten en diensten op één plaats plaatsvindt. Dit kan de PDC op de website van de organisatie zijn, maar ook een andere _registratie_ van waaruit de PDC op de website wordt gevoed. 

In het kader van Overheidsloket 2000 is een gemeentelijke producten- en dienstencatalogus (de vraaggerichte interactieve dienstencatalogus, VIND) ontwikkeld. In 2002 is het beheer en de doorontwikkeling daarvan belegd bij een commerciële partij. Sindsdien zijn er meerdere leveranciers opgestaan die, veelal geïntegreerd met een Content Management Systeem, een producten- en dienstencatalogus aanbieden. Er is dus niet één landelijk vastgestelde PDC met producten en diensten die door alle gemeenten worden gebruikt. 

Om toch een beeld te krijgen van het 'assortiment' producten en diensten dat door gemeenten wordt geleverd, kan worden gekeken naar de Uniforme ProductnamenLijst (UPL), die is samengesteld door het ICTU-programma Samenwerkende Catalogi. Deze lijst kent momenteel 513 unieke productnamen die op 1725 verschillende manieren in PDC's van gemeenten zijn aangetroffen. Ook hier gaat het 'slechts' om de producten en diensten die door individuele burgers, bedrijven of instellingen kunnen worden aangevraagd of gemeld. Deze lijsten zijn dus verre van compleet. 

## **2.2 (E-)Formulieren** 

Door het lezen van de Producten en Dienstencatalogi weet de lezer weliswaar welke rechten en plichten van toepassing zijn in het verkeer met de overheid, maar gebeurt er nog niets. 

Om daadwerkelijk toestemming te krijgen voor het organiseren van een evenement, een pasgeboren kind geregistreerd te krijgen of aanspraak te maken op een uitkering, zal een concrete vraag - of mededeling - moeten worden neergelegd bij de overheid. (E-)Formulieren zijn hierbij nodig. Zo komen vragen om een dienst op een eenduidige manier binnen en wordt het proces dat antwoord geeft op de vraag, in gang gezet. 

Voor de uitvoering van een proces zijn altijd gegevens nodig. Daarom wordt een vraag in een groot aantal gevallen bij de overheid ingediend in de vorm van een - fysiek of elektronisch - formulier. Waar dit niet gebeurt, bijvoorbeeld als de vraag aan de overheid wordt gesteld middels een brief of in een telefoongesprek, vult de overheid doorgaans zelf alsnog een formulier in. Dit om ervoor te zorgen dat elke procesgang start met alle gegevens die daarvoor benodigd zijn. 

KING heeft in samenwerking met gemeenten specificaties voor tientallen elektronische formulieren ontwikkeld. Daarnaast zijn er ook elektronische formulieren van andere organisaties zoals van het Omgevingsloket (Wabo) en van de Belastingdienst voor het aanvragen van Toeslagen. 

**==> picture [103 x 52] intentionally omitted <==**

## **2.3 GEMMA Referentieprocessen** 

Zodra de vraag naar een product of dienst de overheid - door middel van een formulier - heeft bereikt, start de overheid een proces om het gevraagde product of de gevraagde dienst te leveren. Dit betekent overigens niet dat er net zoveel soorten processen zijn als producten: de honderden producten en diensten die, bijvoorbeeld, door een gemeente worden geleverd, zijn te groeperen naar een beperkt aantal soorten processen. Denk bijvoorbeeld aan soorten processen voor het verlenen van vergunningen, het verstrekken van subsidies, etc. 

De vraag naar een product - bijvoorbeeld de vraag om een evenementenvergunning of een parkeervergunning - kan zo worden beantwoord door een proces uit te voeren conform een generiek procesmodel voor vergunningverlening. 

Natuurlijk is de uitwerking van zo'n generiek procesmodel begrensd tot het niveau dat alle processen waarin vergunningen worden geproduceerd, gemeenschappelijk hebben. Zo wordt in het generieke procesmodel voor het verlenen van vergunningen geen processtap of handeling beschreven voor het verifiëren van de tenaamstelling van het voertuig waarvoor een parkeervergunning is aangevraagd. En bevat het ook geen processtap of handeling die verifieert of op de datum waarvoor een evenementenvergunning wordt aangevraagd, wel voldoende politie, brandweer en hulpdiensten beschikbaar zijn. Dergelijke productspecifieke stappen / handelingen en de daaruit voortkomende informatie zijn in de generieke procesmodellen doorgaans geabstraheerd naar adviezen die externe specialisten - t.a.v. evenementen- of parkeervergunningen - leveren. 

KING werkt in samenwerking met gemeenten een tiental van deze Referentieprocessen (voorheen: e-Processen) uit. 

## **2.4 Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ)** 

In 2004 verscheen het Gemeenschappelijk Functioneel Ontwerp Zaken (GFO-Zaken), ontwikkeld door gemeenten en leveranciers onder auspiciën van VNG/EGEM. Het legde de basis voor het zaakgericht werken dat op dit moment door veel gemeenten en steeds meer andere overheidsorganisaties wordt geïmplementeerd. GFO-Zaken is in 2010 opgevolgd door het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ). 

Het RGBZ is een model van de informatie die een overheidsorganisatie nodig heeft om elk proces dat zij uitvoert, te registreren, regisseren en documenteren en die informatie uit te wisselen met derden (burgers, bedrijven, collega-overheden en intern). Het is een generiek - en dus enigszins abstract - model waarin voor het proces belangrijke informatie zoals betrokkenen, objecten, voortgang, dossier en uitkomst zijn gemodelleerd. 

Het RGBZ zorgt voor eenduidigheid in de communicatie over zaken door het hanteren van één taal: de gegevensstandaard. Het maakt bovendien duidelijk om welke gegevens het gaat. Het draagt hiermee bij aan het verbeteren van dienstverlening, bedrijfsvoering en informatiehuishouding. 

In de volgende hoofdstukken zal nog stil worden gestaan bij het RGBZ en de relatie met de zaaktypecatalogus. Het RGBZ is door KING samen met gemeenten ontwikkeld en wordt beheerd door KING. 

## **2.5 Standaard UitwisselingsFormaat Zaken (StUF-ZKN)** 

Waar een informatiemodel als het RGBZ de objecten, attributen en relaties uitwerkt die van belang zijn, zorgt het Standaard UitwisselingsFormaat (StUF) ervoor dat die gegevens ook kunnen worden uitgewisseld. De StUF-standaard voorziet in interactie tussen systemen, zodat die systemen elkaar kunnen informeren en bevragen en  gegevensmutaties uitgewisseld kunnen worden. Specifiek voor de interactie met betrekking tot de gegevens die in het RGBZ zijn gemodelleerd, is het sectormodel StUF-ZKN ontwikkeld. 

**==> picture [103 x 52] intentionally omitted <==**

KING beheert de StUF-standaard, de horizontale sectormodellen StUF-BG en StUF-ZKN en het verticale sectormodel StUF-EF. 

## **2.6 DSP of ZTC?** 

Gemeenten hebben (conform Artikel 18 uit de Archiefregeling) de zorg om te beschikken over een actueel, compleet en logisch samenhangend overzicht van de archiefbescheiden, geordend overeenkomstig de ten tijde van de vorming van het archief daarvoor geldende ordeningsstructuur. Om aan deze zorg te voldoen, werken veel gemeenten met een Documentstructuurplan (DSP) als ordeningsstructuur. 

Met de steeds verdere digitalisering van archiefbescheiden zijn meerdere ordeningen mogelijk dan met alleen papieren  documenten. Er kunnen overzichten gecreëerd worden op BSN, zaakobjecten, documenttypen, resultaattypen, archiefeigenschappen, zaaktypen en ga zo maar door. Verschillende leveranciers hebben hierop geanticipeerd door een DSP-tool  te leveren met informatie zoals de soorten betrokkenen en objecttypen uit de ZTC, maar ook diverse andere informatie zoals organisatiediagrammen, autorisatietabellen en applicatie-inventarisaties. 

Met de nieuwe versie van de ZTC is er een landelijke standaard opgeleverd die overheidsorganen kunnen gebruiken als kern van de ordeningsstructuur. Voor digitale archiefbescheiden biedt de ZTC (samen met het RGBZ) voldoende informatie om te voldoen aan de zorg van de geldende Archiefregeling. Voor archiefbescheiden die nog niet binnen de ZTC van de gemeente worden beheerd, is een specifieke ordeningsstructuur noodzakelijk. 

In de basis is er niets gewijzigd. Er wordt verwacht dat overheidsorganen een helder beleid hebben voor het ordenen en structureren van informatie (dus naast het eventueel hebben van een tool). Overheidsorganen die zaakgericht willen werken doen er goed aan om hier rekening mee te houden in hun beleid en ten minsten de volgende onderdelen daarin te verwerken: 

- Een beschrijving van de werkwijze, gebaseerd op het RGBZ; 

- Een beschrijving van het gebruik van zaaktypen, gebaseerd op de ZTC; 

- Een beschrijving van de zaaktypecatalogi die in gebruik zijn; 

- Een beschrijving van de beheerprocessen. 

**==> picture [103 x 52] intentionally omitted <==**

## **3 Positionering van de Zaaktypecatalogus** 

De ZTC is ook een bouwsteen, naast de hiervoor beschreven bouwstenen. Voordat naar het gebruik van de ZTC kan worden gekeken, is het wenselijk de samenhang te schetsen tussen de ZTC en de andere bouwstenen. Zie onderstaande schematische weergave. 

**==> picture [482 x 296] intentionally omitted <==**

## **3.1 Producten- en DienstenCatalogus (PDC)** 

Versie 1.0 van de ZTC ging uit van een 1:1-relatie tussen een zaaktype in de ZTC en een product of dienst in de PDC. Hoewel in de praktijk een zaaktype en een product vaak nauw verbonden zijn, is het niet altijd handig een 1:1-relatie tussen een zaaktype en een product of dienst te leggen. 

Zo kan één zaaktype volstaan voor het verstrekken van verschillende subsidieproducten als die allemaal volgens hetzelfde proces worden behandeld. Of kunnen in een PDC producten voorkomen die - al dan niet voortkomend uit wet- en regelgeving - verschillende namen hebben, maar in essentie hetzelfde product aanduiden; denk bijvoorbeeld aan het GBA-uittreksel en het ‘Bewijs van in leven zijn’. Tot slot streven overheidsorganisaties naar meer ‘vraaggestuurde’ dienstverlening (op basis van gebeurtenissen of omstandigheden). Daarbij worden meerdere producten die nodig zijn voor het geven van een antwoord op de vraag van de klant, behandeld in één (hoofd)zaak en gebundeld geleverd. Een voorbeeld daarvan is een integrale ‘Horecavergunning’ waarin naast de ‘Drank- en horecavergunning’ ook een ‘Exploitatievergunning’, ‘Terrasvergunning’, ‘Speelautomatenvergunning’ is opgenomen. 

Om die reden modelleert KING een 1:n-relatie tussen zaaktypen in de ZTC en producten in de PDC. Uiteraard kan daarmee nog steeds ook een 1:1-koppeling tussen zaaktypen en producten worden geïmplementeerd. 

**==> picture [103 x 52] intentionally omitted <==**

## **3.2 Formulieren** 

(e-)Formulieren zijn belangrijk voor - het starten van - zaken. De ontvangst van een ingevuld formulier markeert doorgaans de start van een zaak en voedt het proces met de gegevens die het nodig heeft. Denk bijvoorbeeld aan de gegevens over subjecten (initiator), (zaak)objecten (pand, perceel), gerelateerde zaken, et cetera. ‘Formulier’ moet hier overigens in brede zin worden opgevat: het kan gaan om een papieren formulier, een webformulier, maar ook om het scherm waarmee een baliemedewerker een zaak initieert. 

De relatie tussen formulier en product heeft KING vormgegeven als 1:n; één formulier kan worden gebruikt voor het aanvragen van één of meerdere producten. De relatie tussen formulier en zaaktype is als een n:1-relatie gemodelleerd: meerdere formulieren kunnen met één zaaktype behandeld worden. 

De voornaamste reden voor deze keuze is dat overheidsorganisaties die hun dienstverlening vraaggericht willen inrichten, op deze manier in staat worden gesteld om meerdere producten die horen bij een thema of levensgebeurtenis via één formulier te laten aanvragen en vanuit één zaaktype de behandeling te laten plaatsvinden of deze te coördineren. Onder zo’n ‘hoofdzaak’ kunnen deelzaken worden uitgevoerd waarmee de individuele producten worden voortgebracht (zie ook de toelichting op (hoofd)zaken en deelzaken in bijlage 2). 

## **3.3 Referentieprocessen** 

De GEMMA Referentieprocessen zijn ontwikkeld vanuit de overtuiging dat overheidsorganisaties weliswaar vele honderden verschillende producten produceren, maar dat de processen die deze producten voortbrengen grote overeenkomsten vertonen. Voor het afgeven van vergunningen wordt een proces doorlopen dat voor alle typen vergunningen vergelijkbaar is. Hetzelfde geldt voor het verstrekken van subsidies en uitkeringen. Natuurlijk, op detailniveau ziet de beoordeling van een aanvraag voor een parkeervergunning er anders uit dan de beoordeling van een aanvraag voor een omgevingsvergunning. Maar 'boven' dit detailniveau doorloopt elke vergunningaanvraag hetzelfde proces. 

Zaaktypen kunnen veel van deze details accommoderen en slaan zo de brug tussen het product - de parkeervergunning, de omgevingsvergunning - en het generieke Referentieproces. Zo kan de behandeling van een aanvraag voor een parkeervergunning via het zaaktype worden gerelateerd aan andere zaakobjecten (voertuig) dan een omgevingsvergunning (adres, pand, perceel). En helpen zaaktypen ook in het maken van onderscheid tussen de termijn van bijvoorbeeld 4 werkdagen voor het verlenen van een parkeervergunning en de 8 of 26 weken voor een omgevingsvergunning. Deze zaaktypen parametriseren zo dus een generiek Referentieproces. 

De relatie tussen zaaktype en Referentieproces wordt in de ZTC daarom gemodelleerd als n:1. 

## **3.4 Aansluiting op selectielijst** 

Zoals hierboven geschetst, is de ZTC2 toegesneden op en afgestemd met de bouwstenen van GEMMA. Ten opzichte van versie 1.0 resulteert dit vooral in een verbreding van de ZTC met elementen uit het RGBZ en elementen die van belang zijn voor de besturing van de juiste registratie van zaakgegevens. 

Maar hoe zit het met de relatie tussen de ZTC en de archivering van zaken? De GEMMA ZTC 1.0 heeft vaak wel een eerste aanzet gegeven voor archivering, maar speelt voor de archivering - te - vaak geen rol. Om die reden wordt in veel organisaties gewerkt met een ordeningsstructuurplan gebaseerd op een DSP, dat wordt beheerd met behulp van een DSP-tool. Dat de ZTC 1.0 onvoldoende geschikt is als leidraad voor archivering ligt niet zozeer aan de ZTC, maar aan de complexiteit van de Selectielijsten waarin regels zijn opgenomen voor de vorming, bewaring en 

**==> picture [103 x 52] intentionally omitted <==**

vernietiging van archiefbescheiden. De selectielijsten zijn nauwelijks ontworpen op geautomatiseerde selectie en waardering. 

Om beter in te kunnen spelen op het - conform de Selectielijsten - geautomatiseerd selecteren en waarderen van zaken, is in de ZTC2 het RESULTAATTYPE geflexibiliseerd. Tegelijkertijd werkt KING nauw samen met de Adviescommissie Archieven van de VNG om ook de Selectielijsten in de toekomst beter geschikt te maken voor, en aan te laten sluiten op, de behoefte zoveel mogelijk te kunnen archiveren op zaakniveau. Uitgangspunt is om de datums waarop dossiers in aanmerking komen voor vernietiging of overbrenging zoveel als mogelijk geautomatiseerd te kunnen bepalen. Op basis van de GEMMA Zaaktypecatalogus 2 kunnen zaken van een groot aantal zaaktypen geautomatiseerd worden geselecteerd en gewaardeerd conform de Selectielijsten. 

**==> picture [103 x 52] intentionally omitted <==**

## **4 Functie en gebruik van de Zaaktypecatalogus** 

De zaaktypecatalogus en de andere geschetste bouwstenen passen in en op elkaar.  Wat is de rol van de zaaktypecatalogus daarin en wat betekent dat voor het gebruik van de zaaktypecatalogus? 

## **4.1 Functie** 

Het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) is goed gedocumenteerd. In dit document wordt dus volstaan met het beschrijven van de relatie tussen RGBZ en de Zaaktypecatalogus (ZTC). 

In RGBZ wordt onderscheid gemaakt tussen de ZAAK en het ZAAKTYPE. 

De ZAAK in RGBZ registreert het verloop van een individuele procesgang: _de ZAAK startte op ddmm-jjjj met de ontvangst van een ZAAKDOCUMENT van DOCUMENTTYPE ... en leidde tot het verzenden van een ZAAKDOCUMENT van DOCUMENTTYPE ... ter bevestiging van de ontvangst en het zetten van de STATUS ... Op dd-mm-jjjj accepteerde de behandelende afdeling de ZAAK middels het zetten van de STATUS ... Vervolgens verzond MEDEWERKER ... op dd-mm-jjjj een ZAAKDOCUMENT van DOCUMENTTYPE ... met het verzoek om aanvullende informatie en vulde de attributen 'Indicatie opschorting' en 'Reden opschorting'_ . 

Dit is slechts een - smalle - greep uit de registratie die plaatsvindt tijdens de behandeling van een zaak. Alles dat gerelateerd aan de entiteit ZAAK wordt geregistreerd, is een feitenrelaas (registratie van de realisatie) van het verloop van een proces waarin een individuele vraag of melding wordt behandeld. 

Maar waar kan die feitelijke gang van zaken aan worden getoetst? De definitie van een zaak is immers: 

een _samenhangende_ hoeveelheid werk met een _gedefinieerde aanleiding_ en een _gedefinieerd resultaat_ , waarvan de _kwaliteit_ en _doorlooptijd_ bewaakt moeten worden. 

RGBZ voorziet in zo'n toetsingskader via het ZAAKTYPE. Daarin worden 'de kenmerken van groepen vergelijkbare zaken' vastgelegd. Denk bijvoorbeeld aan: 

- Kerngegevens over zaken van dit zaaktype 

- Relaties naar Producten en Diensten, Formulieren, Procesmodellen, Archief 

- Termijnen voor behandeling 

- Basisgegevens die kunnen/moeten worden vastgelegd 

- De statussen die worden bereikt 

- Besluiten die kunnen worden genomen 

- De mogelijke resultaten 

- Eventuele deel- en/of vervolgzaken 

Een ZAAK van een bepaald ZAAKTYPE kan zo worden geconfigureerd door het opgeven van waarden (parameters) die van toepassing zijn op alle zaken van dit ZAAKTYPE. Bijvoorbeeld door het instellen van een 'Doorlooptijd behandeling' van 3 weken voor het ZAAKTYPE 'Behandelen aanvraag collectevergunning' en van 8 weken voor het ZAAKTYPE 'Behandelen aanvraag omgevingsvergunning regulier'. Of in een ZAAKTYPE 'Behandelen evenementenvergunning' te configureren dat voor het zetten van de status 'Afgehandeld' te allen tijde een document met DOCUMENTTYPE 'Advies Brandweer' in het zaakdossier aanwezig moet zijn. Op deze manier geeft een ZAAKTYPE vorm en inhoud aan het toetsingskader voor de kwaliteit en doorlooptijd van alle zaken van dit ZAAKTYPE. 

**==> picture [103 x 52] intentionally omitted <==**

Maar waar worden dit soort parameters bijgehouden? Het RGBZ modelleert weliswaar zowel ZAAK als ZAAKTYPE, maar bevat geen concrete invulling van de waarden die een ZAAK van het ZAAKTYPE 'Behandelen aanvraag evenementenvergunning' mag/kan aannemen. 

Het antwoord op bovenstaande vraag luidt: in de Zaaktypecatalogus. De Zaaktypecatalogus vormt zo een twee-eenheid met het RGBZ en heeft als functie de parameters op te slaan die een ZAAKTYPE definiëren. KING kiest er daarom voor de Zaaktypecatalogus uit te breiden met alle elementen die samenhangen met het ZAAKTYPE zoals gemodelleerd in het RGBZ. 

Echter, het RGBZ richt zich met name op die gegevens die van belang zijn voor het informeren van betrokkenen over - het verloop van - de zaak en die nodig zijn om daarover, ook achteraf, verantwoording te kunnen afleggen. De GEMMA Zaaktypecatalogus 2 richt zich - ook - op elementen die van waarde zijn voor de juiste registratie van gegevens van de zaak, zoals in het hierboven geschetste voorbeeld waarin het advies van de Brandweer op een bepaald moment in het zaakdossier aanwezig moet zijn. Dergelijke ‘stuurparameters’ hebben geen plaats in het RGBZ, dat richt zich op het resultaat van deze 'sturing'. Zij zijn wel erg belangrijk voor een kwalitatief goed en soepel verloop van de zaak en zijn om die reden wel opgenomen in de GEMMA Zaaktypecatalogus 2. 

## **4.2 Het gebruik van de Zaaktypecatalogus** 

## **4.2.1. Ondersteuning van het** _**goede gesprek**_ **over zaakgericht werken** 

De ZTC2 is een uitstekend instrument om met elkaar te praten over zaak- en procesgericht werken. De praktijk leert namelijk dat de term 'zaak- en procesgericht werken' vrijwel iedereen wel bekend in de oren klinkt, maar dat de beelden die mensen erbij hebben sterk verschillen. Een gesprek voeren over de vertaling van een proces naar een zaaktype in de zaaktypecatalogus, maakt zaakgericht werken heel erg concreet en wijdt bovendien alle deelnemers in de terminologie van zaakgericht werken in. Opeens gaat het gesprek over rollen, doorlooptijden, statussen, documenten, besluiten en resultaten en probeert iedereen 'zijn' proces uit te drukken in die gemeenschappelijke taal. Het voeren van dit _goede gesprek_ ondersteunt KING met een sjabloon waarin de uitwerking van een zaaktype kan worden vastgelegd. 

## **4.2.2. Binnen een organisatie** 

Wanneer de ZTC2 op organisatieniveau wordt ingezet, is het een belangrijk hulpmiddel voor het leggen van verbanden tussen de bouwstenen die een rol spelen in het voortbrengen van producten en diensten. Denk bijvoorbeeld aan de samenhang tussen de Producten- en Dienstencatalogus (PDC), (elektronische) formulieren, zaaktypen, procesmodellen en/of -beschrijvingen en het archief. 

Voor organisaties die zaak- en procesgericht werken organisatiebreed implementeren, bewijst de zaaktypecatalogus bovendien goede diensten in het verschaffen van overzicht: elk soort proces dat in de organisatie wordt uitgevoerd is op een gestandaardiseerde wijze - op hoofdlijnen - beschreven via het bijbehorende zaaktype in de ZTC2. Daarmee legt de ZTC2 een universeel fundament voor het genereren en interpreteren van managementinformatie: voor elk soort proces bevat de ZTC2 immers _kritieke prestatie indicatoren_ (KPI's) in de vorm van voorgeschreven en gewenste doorlooptijden, mogelijke uitkomsten van zaken, de aanduiding van de voortgang van zaken via statustypen, etc. 

Ten slotte, en dit wordt door velen gezien als de belangrijkste functie, vervult de ZTC2 een belangrijke rol in de configuratie van geautomatiseerde systemen. Idealiter 'lezen' systemen de parameters van relevante zaaktypen uit de zaaktypecatalogus en configureren op basis daarvan de procesondersteuning binnen het systeem. Denk aan het verdelen van zaken naar de juiste 

**==> picture [103 x 52] intentionally omitted <==**

organisatorische eenheden en/of rollen, het op 'oranje' zetten van een zaak in de werkvoorraad van een behandelaar als de in het zaaktype geconfigureerde doorlooptijd dreigt te worden overschreden, het afdwingen van opname van de juiste documenten in het zaakdossier, et cetera. 

Veel zaak- en documentmanagementsystemen zijn al in staat de ZTC2 op deze wijze te gebruiken als configuratie-instrument. En ook in backofficeapplicaties wordt steeds vaker gebruik gemaakt van de zaaktypecatalogus voor de inrichting van de procesgang. 

De roep om verbreding van de zaaltypecatalogus komt met name vanuit dit laatste toepassingsgebied. Zowel gemeenten als hun leveranciers willen een zaaktypecatalogus die beter past op het RGBZ, zodat systemen die zaakgericht werken ondersteunen ook maximaal gebruik kunnen maken van de configuratieruimte die het RGBZ biedt. 

## **4.2.3. Binnen de gemeentelijke overheidslaag** 

Versie 1.0 van de Zaaktypecatalogus bevat 317 zaaktype-uitwerkingen die 1:1 zijn gekoppeld aan producten en diensten. Een fors aantal gemeenten heeft deze versie van de GEMMA Zaaktypecatalogus gebruikt om niet voor elk zaaktype 'het wiel opnieuw uit te vinden'. Er ging zo een zekere standaardiserende werking uit van de ZTC. 

Voor de doorontwikkeling naar versie 2.0 zag KING zowel een behoefte aan uitbreiding in de lengte (een zaaktypecatalogus met daarin een uitputtende lijst gestandaardiseerde zaaktypen voor gemeenten) als in de breedte (een  zaaktypecatalogus die de configuratieruimte van het RGBZ maximaal benut, maar geen uitputtende lijst gestandaardiseerde zaaktypen bevat). KING is na uitvoerig onderzoek tot de conclusie gekomen dat de verbreding die voor aansluiting van de zaaktypecatalogus op RGBZ nodig is, niet valt te combineren met een uitputtende lijst van in hoge mate gestandaardiseerde zaaktypen binnen één, door KING te ontwikkelen en beheren, catalogus voor gemeenten. 

Immers, met de verbreding van de zaaktypecatalogus moeten tal van procesmatige en vakinhoudelijke aspecten worden uitgewerkt in de zaaktypen. Zo legt een zaaktype vast welke Rollen relevant zijn, welke Statussen worden bereikt, welke Documenten kunnen ontstaan en in het dossier moeten worden opgenomen, welke Objecten kunnen of moeten worden gerelateerd, welke Eigenschappen relevant zijn, welke Besluiten kunnen worden genomen en welke Resultaten de zaak kan hebben. KING beschikt noch over de inhoudelijke expertise, noch over de capaciteit voor het ontwikkelen en beheren van zo’n _brede_ zaaktypecatalogus waarin alle zaaktypen van gemeenten zijn uitgewerkt. 

Zeker niet als in aanmerking wordt genomen dat niet alleen _verbreding_ van de zaaktypecatalogus gewenst is, maar ook _verlenging_ : versie 1.0 van de zaaktypecatalogus bevat ‘slechts’ 317 uitgewerkte zaaktypen. Dit zijn met name de zaaktypen die op initiatief van burgers, bedrijven en instellingen bij gemeenten kunnen worden aangevraagd. Dat aantal is overigens nog fors minder dan de 513 Uniforme Productnamen van de UPL die op 1725 verschillende manieren (Komt-VoorAls, KVA) in PDC’s van gemeenten zijn aangetroffen. Het is reëel te veronderstellen dat er - om te komen tot een volledige zaaktypecatalogus voor gemeenten - daarnaast nog zaaktypen moeten worden uitgewerkt voor enkele honderden ‘onzichtbare’ producten en diensten die niet voorkomen in de UPL of de KVA-lijst. Het gaat dan om de proactief geleverde producten en diensten, interne producten en diensten en producten en diensten die gemeenten en ketenpartners aan elkaar leveren. 

Ten slotte: met het verbreden van de ZTC is deze ook meerdimensionaal geworden. De hierboven geschetste relaties tussen een ZAAKTYPE en BESLUITTYPEn, DOCUMENTTYPEn, EIGENSCHAPpen, RESULTAATTYPEn, ROLTYPEn, STATUSTYPEn en ZAAKOBJECTTYPEn kunnen niet meer worden ‘gevangen’ in de twee dimensies van een spreadsheet waarin de ZTC 1.0 is vastgelegd. Om toch 

**==> picture [103 x 52] intentionally omitted <==**

een indicatie te krijgen van de omvang van de zaaktypecatalogus voor de overheidslaag Gemeenten, is de volgende rekensom gemaakt. 

Veronderstelling: een gemiddeld zaaktype omvat: 

- voor het Zaaktype: 32 attribuutsoorten en 12 relatiesoorten 

- 2 Besluittypen met elk 9 attribuutsoorten en 1 relatiesoort 

- 5 Documenttypen met elk 10 attribuutsoorten en 4 relatiesoorten 

- 2 Eigenschappen met elk 7 attribuutsoorten en 2 relatiesoorten 

- 4 Resultaattypen met elk 9 attribuutsoorten en 4 relatiesoorten 

- 5 Roltypen met elk 3 attribuutsoorten en 2 relatiesoorten 

- 5 Statustypen met elk 9 attribuutsoorten en 4 relatiesoorten 

- 3 Zaakobjecttypen met elk 3 attribuutsoorten en 4 relatiesoorten 

Voor het uitwerken van één zaaktype moeten dus zo’n 300 attribuut- en relatiesoorten worden beschreven. Voor het ‘opwerken’ van de 317 zaaktypen uit de ZTC 1.0 naar 2.0 zouden zo - zonder hergebruik van objecttypen en zonder versiebeheer van individuele objecttypen - een kleine 100.000 kenmerken van een waarde voorzien moeten worden. 

De ZTC2 focust daarom met name op een goed, conform RGBZ, gestandaardiseerde structuur van de zaaktypecatalogus en niet langer op het in de ZTC opnemen van zoveel mogelijk gestandaardiseerde zaaktypen. De ZTC2 is dus vooral een goed gestandaardiseerd Zaaktypecatalogussjabloon. Overigens betekent dit niet het einde van gestandaardiseerde zaaktypen: in het vervolg van dit hoofdstuk en in hoofdstuk 6 beschrijft KING haar visie daarop. 

## **4.2.4. Binnen een overheidskolom, sector, keten** 

In de voorgaande paragrafen van dit hoofdstuk is geschetst hoe de ZTC2 kan worden gebruikt binnen één overheidsorganisatie en binnen één overheidslaag (horizontaal, meer specifiek: gemeenten). De conclusie is dat een zaaktypecatalogus vooral toegevoegde waarde heeft op lokaal niveau, maar dat één brede zaaktypecatalogus met zaaktypen voor alle overheden in een overheidslaag niet te verenigen is met de verbreding van de ZTC. 

Met deze analyse en conclusie is nog niet de vraag beantwoord wat de waarde en functie van een zaaktypecatalogus is in de overheidskolom (verticaal, ook wel aangeduid als sectoren). Want waar de horizontale (binnen een overheidslaag) standaardisatie - onder meer als gevolg van de verbreding van de ZTC - een brug te ver is, ligt die verticale standaardisatie van zaaktypen meer onder handbereik. Binnen een kolom, sector of keten is immers wél de benodigde expertise aanwezig voor het uitwerken van de ‘eigen’ zaaktypen en zal het belang van gestandaardiseerde zaaktypen ook makkelijker worden onderkend, onder andere vanwege de noodzaak tot samenwerking binnen zo’n sector, kolom of keten. 

Overheidskolommen of sectoren worden gevormd door met elkaar samenwerkende organisaties binnen een gemeenschappelijk beleidsterrein. In optima forma hebben die organisaties doelen die ze gezamenlijk nastreven. Elk van de betrokken overheidsorganisaties draagt zijn steentje bij aan het bereiken van die doelen en realiseert zich dat die bijdrage moet worden ingepast in het grotere geheel. 

De ZTC2 vervult in deze verdeling van taken, bevoegdheden en werk tussen de verschillende betrokken organisaties een belangrijke rol. Elk van de doelen binnen een kolom/sector is verbonden aan een daarvoor verantwoordelijke organisatie; denk aan de intergemeentelijke sociale dienst voor zaken binnen het Werk en Inkomen domein, of de gemeente die het bevoegd gezag is voor het behandelen van een omgevingsvergunningaanvraag. Deze organisatie coördineert de (hoofd)zaak die daarbij hoort. De taken die door ketenpartners worden uitgevoerd - het uitbrengen van adviezen, het doen van onderzoek, etc. - zet de coördinerende organisatie uit in de vorm van 

**==> picture [103 x 52] intentionally omitted <==**

gerelateerde zaken onder de hoofdzaak. Voor de uitvoerende ketenpartners zijn dit uiteraard weer gewoon (hoofd)zaken, met de coördinerende organisatie als 'klant'. 

Het levert grote voordelen op als dit geheel van zaken door de samenwerkende ketenpartners gezamenlijk wordt uitgewerkt in een gemeenschappelijke Zaaktypecatalogus: 

- het leidt tot duidelijke afspraken over de verdeling van werk via goed op elkaar afgestemde zaaktypen die door de verschillende partners worden uitgevoerd; 

- de ketenpartners spreken dezelfde taal en worden aangespoord gezamenlijke afspraken te maken over de invulling van statustypen, documenttypen, etc.; 

- de zaaktypen in de gemeenschappelijke Zaaktypecatalogus kunnen - en moeten - worden beschouwd als de 'contracten' die de samenwerkende organisaties met elkaar hebben gesloten; 

- over de naleving van deze contracten kan eenvoudig worden gerapporteerd, semantiek en syntax zijn immers gelijkgeschakeld; 

- de zaakgerichte systemen van de verschillende ketenpartners worden optimaal op elkaar afgestemd als zij worden geconfigureerd vanuit één gemeenschappelijke zaaktypecatalogus. 

Dit samen uitwerken en delen van één zaaktypecatalogus hoeft niet direct groots en meeslepend op - bijvoorbeeld - landelijk niveau te worden gerealiseerd. De praktijk wijst uit dat klein beginnen, bijvoorbeeld op regionaal niveau met partijen die allemaal een gelijk belang hebben bij een goed functionerende ketensamenwerking, snel kan leiden tot een concrete invulling van zo'n keten-ZTC. Andere regio's kunnen de aldus uitgewerkte zaaktypecatalogus weer gebruiken als vertrekpunt voor 'hun' keten-ZTC; zo ontstaat een olievlekwerking en geleidelijke convergentie naar steeds meer bovenregionale gemeenschappelijkheid. Deze beweging is op dit moment waar te nemen in de ontwikkeling van de Regionale Uitvoeringsdiensten en hun ketensamenwerking met bevoegde gezagen. 

**==> picture [103 x 52] intentionally omitted <==**

## **5 Kenmerken van een zaaktype** 

## **5.1 Vorm** 

De GEMMA Zaaktypecatalogus 2 is niet langer een uitputtende lijst met gestandaardiseerde zaaktypen. De GEMMA Zaaktypecatalogus 2 is eerst en boven alles een sjabloon voor Zaaktypecatalogi die overheidsorganisaties, al dan niet met elkaar samenwerkend, kunnen gebruiken voor het vastleggen van hun eigen zaaktypen. 

Met het verbreden van de ZTC krijgt deze ook meer dimensies (statustypen, documenttypen, besluittypen, etc.) dan versie 1.0. De dimensies zijn uitgewerkt in de vorm van het Informatiemodel ZTC2 met bijbehorend uitwisselformaat (StUF-ZTC) waarmee de specificaties van zaajtypen kunnen worden gevalideerd. Dit heeft als bijkomend voordeel dat Zaaktypecatalogi eenvoudiger kunnen worden verwerkt in en door systemen, bijvoorbeeld bij het op elkaar afstemmen van specificaties van een zaaktype tussen een zaaksysteem en een taakspecifieke applicatie. 

## **5.2 Structuur op hoofdlijnen** 

Aan de hand van de afbeelding aan het einde van dit hoofdstuk wordt de informatie-structuur van de GEMMA Zaaktypecatalogus 2 op hoofdlijnen toegelicht. De details zijn uitgewerkt in het separate document ‘GEMMA Zaaktypecatalogus 2 – Informatiemodel’. De structuur op hoofdlijnen is vereenvoudigd in het sjabloon (bijlage 1). 

De GEMMA Zaaktypecatalogus (ZTC) 2 is, in tegenstelling tot versie 1.0, geen catalogus waarin alle denkbare zaaktypen van gemeenten en andere overheidsorganisaties zijn uitgewerkt. Bij het ontwerp van de ZTC2 is vooral gefocust op maximale aansluiting van de ZTC op het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) en op het definiëren van die extra elementen die geen plaats - horen te - hebben in RGBZ, maar wel van belang zijn voor de besturing van zaken en daarmee dicht aanliggen tegen de wijze waarop systemen zaakgericht werken ondersteunen. Ten opzichte van versie 1.0 is de GEMMA Zaaktypecatalogus 2 dus ontwikkeld in de ‘breedte’: de ZTC2 bevat veel meer objecttypen en attributen dan versie 1.0. 

Met deze verschuiving van de focus heeft KING onderkend dat er niet één landelijke zaaktypecatalogus kan bestaan waarin alle zaaktypen van alle overheidsorganisaties volledig uitgewerkt een plaats hebben of krijgen. Als gevolg van de ‘verbreding’ zijn er tal van elementen in de ZTC2 opgenomen die uitsluitend lokaal kunnen worden ingevuld. Het gevolg is dat er niet één, maar vele zaaktypecatalogi zullen ontstaan. 

Om aan die ontwikkeling tegemoet te komen, voorziet de ZTC2 in het objecttype CATALOGUS. Daarmee worden alle ZAAKTYPEN en daaraan gerelateerde objecten en attributen voor een specifiek domein gebundeld tot één geheel. Het domein waarop zo’n catalogus van toepassing is, kan sterk uiteenlopen. Er zullen catalogi zijn die met de ZAAKTYPEn van één overheidsorganisatie worden gevuld, maar ook catalogi worden ontwikkeld die veel breder reiken; denk aan een sectorale catalogus voor alle overheidsorganisaties die binnen een sector actief zijn of een ketencatalogus voor ketenpartners. Het informatiemodel van de ZTC 2 voorziet daarom in een unieke identificatie van een CATALOGUS: de combinatie van het RSIN van de ‘eigenaar’ van de CATALOGUS en het Domein waarop de CATALOGUS van toepassing is. 

In één CATALOGUS worden op het hoogste niveau verschillende objecttypen onderscheiden. Het belangrijkst is natuurlijk het objecttype ZAAKTYPE; een zaaktypecatalogus definieert immers de verschillende ZAAKTYPEn die relevant zijn voor het domein waarop de CATALOGUS betrekking 

**==> picture [103 x 52] intentionally omitted <==**

heeft en bepaalt zo de gegevens die worden vastgelegd van zaken van het ZAAKTYPE. Historie is in het model zodanig opgenomen dat versies van zaaktypen onderscheiden kunnen worden, met telkens bij elke versie van een zaaktype alle daarbij behorende waarden van het zaaktype en van de ‘onderliggende’ objecttypen zoals statustypen, informatieobjecttypen en resultaattypen. 

De CATALOGUS bevat, op hetzelfde niveau als het ZAAKTYPE, de objecttypen BESLUITTYPE  en INFORMATIEOBJECTTYPE (voorheen Documenttype). Deze objecttypen zijn zo te gebruiken in alle ZAAKTYPEn die in de CATALOGUS worden gedefinieerd. Omdat de waardenlijsten van deze objecttypen fors kunnen zijn, kan in elk ZAAKTYPE worden geconfigureerd welke BESLUITTYPEn en INFORMATIEOBJECTTYPEn relevant zijn voor zaken van het ZAAKTYPE. De objecttypen BESLUITTYPE en INFORMATIEOBJECTTYPE zijn - met kleine aanpassingen en aanvullingen - overgenomen uit het RGBZ. 

Binnen elk ZAAKTYPE zijn de objecttypen STATUSTYPE, ZAAKOBJECTTYPE, ROLTYPE, EIGENSCHAP en RESULTAATTYPE gemodelleerd. 

Het STATUSTYPE is overgenomen uit het RGBZ en wordt in de ZTC eveneens gemodelleerd binnen een ZAAKTYPE . De reden hiervoor is dat de herbruikbaarheid van STATUSTYPEn beperkt is; er is weliswaar een aantal generieke STATUSTYPEn denkbaar (bijvoorbeeld ‘Ontvangen’ of ‘Afgehandeld’), maar in een groot aantal gevallen krijgt een STATUSTYPE en de daarbij horende attributen een ZAAKTYPE-specifieke invulling. 

Het ZAAKOBJECTTYPE is een objecttype dat noch in het RGBZ, noch in de ZTC 1 voorkomt. Het objecttype is in de ZTC2 geïntroduceerd om vooraf - per ZAAKTYPE - de relatie tussen een ZAAK en de basis- en kerngegevens die relevant zijn voor ZAAKen van dat ZAAKTYPE inzichtelijk te maken en - belangrijker - registratie daarvan tijdens de behandeling van een ZAAK te kunnen afdwingen. Denk aan het niet kunnen zetten van een STATUS als niet eerst een relevant basis- of kerngegeven via ZAAKOBJECT is gerelateerd aan de zaak. 

Ook het ROLTYPE is een objecttype dat niet in het RGBZ of de ZTC 1 voorkomt. Het voorziet in de behoefte om per ZAAKTYPE een duidelijke typering te kunnen geven aan de BETROKKENEn die in een - door het ROLTYPE - bepaalde hoedanigheid ‘acteren’ in zaken van een bepaald ZAAKTYPE. Het ROLTYPE beoogt zo vooral ondersteuning te bieden aan het - via het ROLTYPE - onderscheiden van groepen BETROKKENEn en daarvoor specifieke functionaliteit aan te bieden. Denk bijvoorbeeld aan het instellen van autorisaties voor bepaalde ROLTYPEn, of het informeren van BETROKKENEn in één of meer ROLTYPEn over de voortgang van de behandeling van zaken van een bepaald ZAAKTYPE. 

De ZTC2 modelleert het objecttype EIGENSCHAP als objecttype bij een ZAAKTYPE. Een EIGENSCHAP is een voor het betreffende ZAAKTYPE specifiek gegeven dat voor de - besturing van de - behandeling van een zaak van dat ZAAKTYPE van groot belang is. Denk aan de EIGENSCHAP ‘Datum evenement’: dit gegeven is relevant voor de behandelaar van aanvragen voor een evenementenvergunning, bijvoorbeeld om evenementen te sorteren op datum en aanvragen voor evenement die de komende weken zijn gepland eerder te behandelen dan evenementen die pas over enkele maanden zullen plaatsvinden. 

Verder kent de ZTC2 bij een ZAAKTYPE het RESULTAATTYPE: een objecttype dat niet in het RGBZ voorkomt, maar wel al in de ZTC 1 werd geïntroduceerd. Het RGBZ kent overigens bij een zaak wel het attribuut Resultaatomschrijving  dat bij een fysieke zaak een waarde heeft die ontleend wordt aan de RESULTAATTYPEn bij het ZAAKTYPE van die zaak. Het is in de ZTC2 in meer detail 

gemodelleerd met het doel betere ondersteuning te bieden aan het correct en integraal kunnen archiveren van zaken van een bepaald ZAAKTYPE en daarbij geautomatiseerd te bepalen wat de datum is waarop een zaakdossier vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden. In uitzonderingsgevallen wijkt het archiefregime van een individueel informatieobject in 

**==> picture [103 x 52] intentionally omitted <==**

een zaakdossier af van het archiefregime van de zaak als geheel. In het correct archiveren van dergelijke gevallen voorziet de relatie van RESULTAATTYPE naar ZAAK-INFORMATIEOBJECT-TYPE. Dan resten nog de relaties tussen ZAAKTYPEn onderling. In de ZTC2 worden twee relatiesoorten onderscheiden: de relatie tussen een ZAAKTYPE en deel-ZAAKTYPEn en de relatie tussen (om andere redenen) gerelateerde ZAAKTYPEN. De tweede relatiesoort betreft de relatie tussen een ZAAKTYPE en de ZAAKTYPEn die een noodzakelijk vervolg zijn op het eerstgenoemde ZAAKTYPE, de relatie tussen een ZAAKTYPE en de ZAAKTYPEn die een bijdrage leveren aan de behandeling van het eerstgenoemde ZAAKTYPE en de relatie tussen een ZAAKTYPE en andere ZAAKTYPen waarop het eerstgenoemde ZAAKTYPE betrekking heeft. Al deze relaties maken het mogelijk om ZAAKTYPEn zuiver af te bakenen, overeenkomstig bedrijfsprocessen, en grip te behouden op samenhang en samenwerking tussen bedrijfsprocessen, binnen de eigen organisaties en tussen organisaties, teneinde een passend antwoord te verkrijgen op de aanleiding voor een zaak. 

**==> picture [103 x 52] intentionally omitted <==**

**==> picture [665 x 509] intentionally omitted <==**

**==> picture [103 x 52] intentionally omitted <==**

## **6 Beheer** 

Het loslaten van de gedachte dat er één allesomvattende Zaaktypecatalogus kan bestaan waarin alle zaaktypen van en voor alle gemeenten - en andere overheidsorganisaties - zijn gestandaardiseerd, heeft uiteraard ook gevolgen voor het beheer. In plaats van één Zaaktypecatalogus zullen vele Zaaktypecatalogi ontstaan die op evenzoveel plaatsen moeten worden beheerd. Wie doet wat?  Hieronder volgt een overzicht. Eén en ander is nader uitgewerkt in het document ‘Beheermodel ZTC’. 

## **6.1 Sjablonen en modellen: KING** 

De nauwe relatie tussen RGBZ en het informatiemodel van de GEMMA Zaaktypecatalogus vereist dat het beheer van beide bouwstenen in één hand ligt. Alleen zo kan worden geborgd dat wijzigingen in het RGBZ ook leiden tot de benodigde aanpassingen in het Informatiemodel ZTC en vice versa. De ZTC is daarbij kaderstellend voor het RGBZ. 

KING zal zorg dragen voor het beheer van: 

- de beschrijving van objecten, attribuut- en relatiesoorten van de Zaaktypecatalogus (het Informatiemodel ZTC); 

- het uitwisselformaat voor zaaktypen (StUF-ZTC); 

- het tekstsjabloon voor de uitwerking van individuele zaaktypen. 

## **6.2 Referentiezaaktypen: KING** 

Op basis van de referentieprocessen uit de KING-procesarchitectuur 2.0 ontwikkelt KING een referentie-zaaktypecatalogus met referentie-zaaktypen. 

Een zaaktype uit de referentiecatalogus beschrijft de standaard onderdelen die in elk onderliggend zaaktype zouden moeten voorkomen. Een voorbeeld hiervan is het uitvoeren van handhaving. Binnen een gemeente is het mogelijk dat er op verschillende beleidsterreinen handhaving plaatsvindt. Het zaaktype ‘Handhaven’ uit de referentiecatalogus beschrijft het overkoepelende zaaktype van handhaving voor gemeenten, ongeacht het beleidsterrein. 

De referentiezaaktypen dienen als startpunt voor de uitwerking door gemeenten van eigen, daarvan afgeleide, zaaktypen. 

KING zal zorg dragen voor het beheer van: 

- de Referentiezaaktypecatalogus o.b.v. de Referentieprocesmodellen. 

## **6.3 Generieke waardenlijsten, domeintabellen, etc.: KING / beheerders Catalogi** 

Zowel het RGBZ als de ZTC definiëren objecttypen en attribuutsoorten waarvan de gegevenswaarden om (landelijk) beheer vragen, inclusief het beheer van meerdere versies. Dit geldt bijvoorbeeld voor de generieke omschrijvingen die zijn gedefinieerd voor objecttypen als BESLUITTYPE, INFORMATIEOBJECTTYPE, RESULTAATTYPE, ROLTYPE, et cetera. Die generieke omschrijvingen zijn er voor bedoeld om, ook als ‘lokaal’ een andere omschrijving wordt gehanteerd, gegevens tussen verschillende organisaties te kunnen uitwisselen op basis van die generieke omschrijving. KING beheert de in het RGBZ opgenomen domeinwaarden van attribuutsoorten en beheert de waardenlijsten die in het RGBZ gespecificeerd zijn. Een voorbeeld van het laatste zijn de benamingen van generieke documenttypen. Domeinwaarden van andere attribuutsoorten worden beheerd door de desbetreffende catalogi-beheerders. Een voorbeeld daarvan zijn de generieke statusomschrijvingen per zaaktype. 

**==> picture [103 x 52] intentionally omitted <==**

## **6.4 Inhoud: gemeente, sector, etc.** 

Het beheer van Zaaktypecatalogi waarin concrete zaaktypen zijn uitgewerkt, zal op vele plaatsen plaatsvinden. Een ZTC die uitsluitend wordt gebruikt voor één gemeente, zal moeten worden beheerd door de organisatie zelf. Daar waar met elkaar samenwerkende organisaties gezamenlijk een Zaaktypecatalogus gebruiken, ligt het in de rede het beheer bij één van die partijen onder te brengen. 

Dit laat overigens onverlet dat KING groot belang hecht aan - zo breed mogelijk - gestandaardiseerde zaaktypen. De uitwerking daarvan zal echter _bottom up_ moeten plaatsvinden door partijen die een gedeeld belang hebben bij die gestandaardiseerde zaaktypen. Een goed voorbeeld daarvan is hierboven al aangestipt: op initiatief van een provincie heeft een Regionale Uitvoeringsdienst samen met zijn opdrachtgevers een gemeenschappelijke zaaktypecatalogus uitgewerkt. Deze zaaktypecatalogus is door de provincie ter review voorgelegd aan de andere Regionale Uitvoeringsdiensten in de provincie. Inmiddels heeft deze zaaktypecatalogus zijn weg ook gevonden naar Regionale Uitvoeringsdiensten in andere provincies. Op deze wijze ontstaat de olievlek waarin een steeds groter worden groep organisaties gebruik maakt van een gemeenschappelijk uitgewerkte zaaktypecatalogus. 

KING zal zowel de _bottom up-_ als _top down-_ ontwikkeling van Zaaktypecatalogi actief stimuleren door vakverenigingen en beroepsgroepen (bijv. NvvB voor het Burgerzakendomein, VDP voor Publieksdiensten, VBWTN en Stadswerk voor Bouw- en Woningtoezicht, etc.) aan te moedigen zaaktypen uit te werken voor hun domein. Uiteraard worden ook andere belanghebbende partijen van harte uitgenodigd hieraan een bijdrage leveren. KING denkt daarbij bijvoorbeeld aan leveranciers met specialistische kennis over een domein, maar ook aan de expertise van bijvoorbeeld DSP-leveranciers t.a.v. dossiervorming en archivering. 

Deze decentrale uitwerking van Zaaktypecatalogi is voor iedereen nieuw. KING zal deze ontwikkeling - bijvoorbeeld in de afstemming met vakverenigingen en beroepsgroepen - zo goed mogelijk monitoren en inventariseren of daarbij behoefte is aan - procesmatige - ondersteuning. Als die behoefte bestaat, zal KING onderzoeken of daar met bijvoorbeeld een opleidingsaanbod of de ondersteuning van gespecialiseerde e-adviseurs invulling aan kan worden gegeven. 

## **6.5 Validatie en landelijke publicatie van Zaaktypecatalogi: KING** 

Het succes van Zaaktypecatalogi die een belangrijke standaardiserende werking nastreven - zoals een Zaaktypecatalogus voor een sector, keten of overheidslaag - staat of valt met kwaliteit en vindbaarheid. KING zal zorgen voor een ‘community’ waar alle catalogi kunnen worden gepubliceerd. Daarbij zal een onderscheid worden gemaakt tussen Zaaktypecatalogi die het bereik hebben van een sector, keten of overheidslaag en catalogi met een kleiner bereik. 

Catalogi die door een representatieve vertegenwoordiging van een landelijk publiek Domein (denk aan een vakvereniging of beroepsgroep) aan KING voor publicatie worden aangeboden, zullen onder aansturing van KING worden gevalideerd. In die validatie wordt uitsluitend de conformiteit van de betreffende catalogus getoets aan de - versie van - vigerende referentiemodellen (RGBZ, RSGB en IMZTC), standaarden (StUF-ZTC, StUF-ZKN en StUF-BG) en richtlijnen (bijv. de aanwijzingen van KING ten aanzien van ROLlen, Zaken en Deelzaken, et cetera). Over de kwaliteit van de inhoud van de catalogus kan KING geen oordeel vellen; KING beschikt niet op elk domein over de vakinhoudelijke expertise die daarvoor nodig is. Met betrekking tot de inhoud van een Zaaktypecatalogus zal KING daarom volstaan met het registreren van het gremium dat de catalogus ontwikkelde en voor validatie en publicatie aanbood, de deelnemers aan dat gremium en de contactpersoon die aanspreekpunt is voor ontwikkeling en beheer van de catalogus. Na validatie 

**==> picture [103 x 52] intentionally omitted <==**

- en verwerking van eventuele daaruit voortvloeiende aanpassingen - publiceert KING de catalogi die voldoen aan de conformiteitstoets op een herkenbare - ‘getoetst door KING’ - wijze. 

Ook catalogi die geen landelijk bereik hebben, of catalogi die niet door publieke partijen zijn ontwikkeld, kunnen desgevraagd door KING worden gepubliceerd. Daarop zal KING echter geen validatie uitvoeren, tenzij de aanbiedende organisatie daar expliciet om vraagt en bereid is de kosten van validatie voor haar rekening te nemen. 

Voor alle door KING te publiceren catalogi - gevalideerd of niet - geldt dat deze beheerd moeten worden. Indien KING signalen ontvangt dat een catalogus niet of onvoldoende wordt beheerd - bijvoorbeeld als wijzigingen in wet- en regelgeving niet leiden tot overeenkomstige aanpassingen in de zaaktypen van de catalogus - kan KING de publicatie van de catalogus staken. 

**==> picture [103 x 52] intentionally omitted <==**

## **Bijlage 1: Sjabloon zaaktype** 

Op de volgende pagina’s vermelden we het sjabloon voor het specificeren van een zaaktype. Een toelichting hierop vindt u in bijlage 2. De actuele versie van het sjabloon is als wijzigbaar document aanwezig op de website van KING. 

Het sjabloon kent de volgende indeling: 

- Procesgang (op hoofdlijnen) 

- Algemene gegevens 

- Publicatie (van indiening) 

- Planning 

- Statussen 

- Checklistitems bij status 

- Rollen en betrokkenen 

- Zaakobjecten 

- Eigenschappen 

- Zaakdocumenten 

- Besluiten 

- Resultaten en bewaartermijnen 

- Deelzaken 

- Vervolgzaken 

- Voorafgaande zaken 

- Zaken die een bijdrage leveren. 

**==> picture [103 x 52] intentionally omitted <==**

## **Zaaktype [Zaaktype-omschrijving]** 

Identificatie: [Zaaktype-identificatie] 

Versie datum: [Datum begin geldigheid versie van zaaktype] 

## **PROCESGANG (OP HOOFDLIJNEN)** 

**==> picture [454 x 73] intentionally omitted <==**

[voorbeeld; vervangen door figuur met procesgang van zaaktype] 

## **ALGEMENE GEGEVENS** 

|**ALGEMENE GEGEVENS**||
|---|---|
|**Zaaktype-omschrijving**<br>**generiek**||
|**Zaakcategorie**||
|**Doel**||
|**Aanleiding**||
|**Indicatie Intern of Extern**||
|**Handeling initiator**||
|**Onderwerp**||
|**Handeling behandelaar**||
|**Trefwoord**||
|**Archiefclassificatiecode**||
|**Vertrouwelijkheidaanduiding**|Maak keuze|
|**Producten/Dienst naam**||
|**URL (producten/dienst)**||
|**Formuliernaam**||
|**URL (formulier)**||
|**Procesnaam**||
|**URL (proces)**||
|**Verantwoordingsrelatie**||
|**Verantwoordelijke**||
|**Toelichting**||



## **PUBLICATIE (van indiening)** 

|**Publicatie-indicatie**|Maak keuze|
|---|---|
|**Publicatietekst**||



## **PLANNING** 

**Doorlooptijd behandeling** 

**==> picture [103 x 52] intentionally omitted <==**

|**Servicenorm behandeling**||
|---|---|
|**Opschorting/aanhouding**<br>**mogelijk**|Maak keuze|
|**Verlenging mogelijk**|Maak keuze|
|**Verlengingstermijn**||



## **STATUSSEN** 

|**Status-**<br>**type-**<br>**volg-**<br>**nummer**|**Statustype-**<br>**omschrijving**|**Status-kenmerken**|
|---|---|---|
|||_Statustype-omschrijving generiek:_<br>_Doorlooptijd status:_<br>_Informeren:_ Maak keuze<br>_Statustekst:_ <br>_Toelichting:_<br>|
|||_Statustype-omschrijving generiek:_<br>_Doorlooptijd status:_<br>_Informeren:_ Maak keuze<br>_Statustekst:_ <br>_Toelichting:_<br>|



## **CHECKLISTITEMS BIJ STATUS** 

|**Status-**<br>**type-**<br>**volg-**<br>**nummer**|**Itemnaam**|**Vraagstelling**|**Verplicht**|**Toelichting**|
|---|---|---|---|---|
||||Maak keuze||
||||Maak keuze||
||||Maak keuze||



## **ROLLEN en BETROKKENEN** 

|**Roltypeomschrijving**|**Roltypeomschrijving**<br>**generiek**|**Betrokkenen**|**Mag zetten**<br>**Status(sen)**|
|---|---|---|---|
||Adviseur|||
||Behandelaar|||
||Belanghebbende|||
||Beslisser|||
||Initiator|||
||Klantcontacter|||



**==> picture [103 x 52] intentionally omitted <==**

Zaakcoördinator 

## **ZaakOBJECTEN** 

|**Objecttype**|**Ander**<br>**objecttype?**|**Verplicht**<br>**bij**<br>**Status**|**Verplicht**<br>**bij**<br>**Resultaat**|**Relatieomschrijving**|
|---|---|---|---|---|
||Maak keuze||||
||Maak keuze||||
||Maak keuze||||



## **EIGENSCHAPPEN** 

|**Eigenschapnaam**|**Eigenschap-kenmerken**|**Eigenschap-kenmerken**||
|---|---|---|---|
||_Definitie:_|||
||_Groep:_<br>_Formaat:_<br>_Lengte:_<br>_Kardinaliteit:_<br>_Waardenverzameling:_|_Objecttype:_<br>_Informatiemodel:_<br>_Namespace:_<br>_Schemalocatie:_<br>_X-path element:_<br>_Entiteittype:_||
||_Verplicht bij Status:_<br>_Toelichting:_|||
||_Definitie:_|||
||_Groep:_<br>_Formaat:_<br>_Lengte:_<br>_Kardinaliteit:_<br>_Waardenverzameling:_|_Objecttype:_<br>_Informatiemodel:_<br>_Namespace:_<br>_Schemalocatie:_<br>_X-path element:_<br>_Entiteittype:_||
||_Verplicht bij Status:_<br>_Toelichting:_|||



**==> picture [103 x 52] intentionally omitted <==**

## **ZAAKDOCUMENTEN** 

|**Volg-**<br>**nr**|**Documenttype-**<br>**omschrijving**|**Documenttype-kenmerken**|
|---|---|---|
|||_Documenttype-omschrijving generiek:_<br>_Documentcategorie:_Maak keuze<br>_Documenttypetrefwoord:_<br>_Vertrouwelijkheidaanduiding:_Maak keuze<br>_Richting:_Maak keuze<br>_Model:_<br>_Verplicht bij Status:_<br>_Verplicht bij Resultaat:_<br>_Toelichting:_|
|||_Documenttype-omschrijving generiek:_<br>_Documentcategorie:_Maak keuze<br>_Documenttypetrefwoord:_<br>_Vertrouwelijkheidaanduiding:_Maak keuze<br>_Richting:_Maak keuze<br>_Model:_<br>_Verplicht bij Status:_<br>_Verplicht bij Resultaat:_<br>_Toelichting:_|



## **BESLUITEN** 

|**BESLUITEN**||
|---|---|
|**Besluittype-**<br>**omschrijving**|**Besluittype-kenmerken**|
||_Besluittype-omschrijving generiek:_<br>_Besluitcategorie:_<br>_Reactietermijn:_<br>_Publicatie-indicatie:_Maak keuze<br>_Publicatietekst:_<br>_Publicatietermijn:_<br>_Documenttype:_<br>_Toelichting:_|



**==> picture [103 x 52] intentionally omitted <==**

_Besluittype-omschrijving generiek: Besluitcategorie: Reactietermijn: Publicatie-indicatie:_ Maak keuze _Publicatietekst: Publicatietermijn: Documenttype: Toelichting:_ 

## **RESULTATEN en BEWAARTERMIJNEN** 

|**Resultaattypeomschrijving**|**Resultaattype-kenmerken**|
|---|---|
||_Resultaattypeomschrijving generiek:_<br>_Selectielijstklasse:_<br>_Archiefnominatie:_V (Vernietigen)<br>_Archiefactietermijn:_<br>_Brondatum archiefprocedure:_<br>_Relevante Eigenschap Brondatum archiefprocedure:_<br>_Leidt tot BESLUIT(en):_<br>_Heeft verplichte ZAAKOBJECTTYPE:_<br>_Toelichting:_|
||_Resultaattypeomschrijving generiek:_<br>_Selectielijstklasse:_<br>_Archiefnominatie:_V (Vernietigen)<br>_Archiefactietermijn:_<br>_Brondatum archiefprocedure:_<br>_Relevante Eigenschap Brondatum archiefprocedure:_<br>_Leidt tot BESLUIT(en):_<br>_Heeft verplichte ZAAKOBJECTTYPE:_<br>_Toelichting:_|



_Voor specifieke zaakdocumenttypen (uitzonderingen):_ 

|**Resultaat-**<br>**typeom-**<br>**schrijving**|**Zaak-**<br>**doc-**<br>**volgnr**|**Documenttype**<br>**-omschrijving**|**Selectielijst-**<br>**klasse**|**Archief-**<br>**nominatie**|**Archief-**<br>**actie-**<br>**termijn**|
|---|---|---|---|---|---|
|||||||
|||||||



## **DEELZAKEN** 

**ZAAKTYPE: Toelichting** 

**==> picture [103 x 52] intentionally omitted <==**

## **VERVOLGZAKEN** 

**ZAAKTYPE: Toelichting** 

## **VOORAFGAANDE ZAKEN** 

**Zaaktype Toelichting** 

## **ZAKEN DIE EEN BIJDRAGE LEVEREN** 

**Zaaktype Toelichting** 

**==> picture [103 x 52] intentionally omitted <==**

## **Bijlage 2: Toelichting op het sjabloon** 

Met dit sjabloon wordt een ZAAKTYPE benoemd en gespecificeerd. Hieronder geven we een toelichting op de gegevens waarmee het zaaktype wordt gespecificeerd. Zie voor meer detail s over deze gegevens het Informatiemodel ZTC2. 

Met het benoemen van een zaaktype worden onder meer zaken van dit ZAAKTYPE afgebakend. Wat in een individueel geval een zaak is, waar die begint en waar die eindigt, moet vooral bekeken worden vanuit het perspectief van de initiator van de zaak (burger, bedrijf, medewerker, etc.). Het traject van (aan)vraag cq. aanleiding voor de zaak tot en met de levering van de producten/of diensten die een passend antwoord vormen op die aanleiding, bepaalt de omvang en afbakening van een zaak en daarmee van het ZAAKTYPE. Hiermee komt de afbakening van een zaak overeen met een bedrijfsproces: ‘van klant tot klant’ (intern dan wel extern). Dit betekent onder meer dat onderdelen van bedrijfsprocessen geen zelfstandige zaken vormen. Het betekent ook dat een aanleiding die niet leidt tot de start van de uitvoering van een bedrijfsproces, niet leidt tot een zaak (en wordt behandeld in het kader van een reeds lopende zaak). 

|**Gegeven**|**toelichting**|
|---|---|
|**Zaaktype**|Omschrijving van de aard van zaken van het ZAAKTYPE.<br>Binnen een catalogus heeft elke zaaktype een unieke naam cq. omschrijving.<br>Richtlijn voor de benaming van een zaaktype is ‘zelfstandig naamwoord + werkwoord’. Bijvoorbeeld:<br>‘Subsidieaanvraag behandelen’. Ook andere combinaties van ‘Handeling initiator’, ‘Onderwerp’ en ‘Handeling<br>behandelaar’ (zie verderop) zijn mogelijk mits dit binnen een catalogus consequent wordt toegepast.<br>Lengte: 80 letters en leestekens|
|**Identificatie**|Unieke aanduiding van het ZAAKTYPE. Deze bestaat uit de unieke aanduiding van de CATALOGUS gevolgd door de<br>identificatie van het ZAAKTYPE.:<br>-<br>Een afkorting (5 hoofdletters) voor het domein waarop de catalogus gericht is;<br>-<br>Het RSIN van de organisatie die de eigenaar is van de catalogus (het RSIN wordt uitgegeven door de<br>Kamers van Koophandel aan elke onderneming en samenwerkingsverband en bevat 9 cijfers);<br>-<br>De identificatie van het ZAAKTYPE binnen de CATALOGUS (1 tot 5 cijfers zonder voorloopnullen).<br>Om redenen van leesbaarheid wordt tussen het RSIN en het zaaknummer een liggend streepje geplaatst,<br>bijvoorbeeld ABCDE123456789-21<br>Lengte: 16 tot 20 tekens|
|**Versiedatum:**|De datum waarop de (gewijzigde) kenmerken van het ZAAKTYPE geldig zijn geworden.|



**==> picture [103 x 52] intentionally omitted <==**

## **ALGEMENE GEGEVENS** 

|**Gegeven**|**toelichting**|
|---|---|
|**Zaaktype-omschrijving generiek**|Algemeen gehanteerde omschrijving van de aard van zaken van het ZAAKTYPE. Het gaat hier om een korte<br>omschrijving van de aard van de zaak, ook wel zaaknaam genoemd, zoals deze binnen een domein wordt<br>toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Zaaktype-<br>omschrijving. De domeinwaarden zijn opgenomen in de CATALOGUS van het betreffende Domein.<br>Lengte: 80 letters en leestekens|
|**Zaakcategorie**|Typering van de aard van zaken van het ZAAKTYPE. Het gaat hier om de indeling van zaaktypen naar categorieën<br>zoals Behandelen vergunningaanvraag, Behandelen ontheffingaanvraag en Behandelen subsidie-aanvraag.<br>Lengte: 40 letters en leestekens|
|**Doel**|Een omschrijving van hetgeen beoogd is te bereiken met een zaak van dit zaaktype. Deze attribuutsoort heeft<br>vooral een documentatiefunctie en is bedoeld om een omschrijving te geven van het doel – dat geconcretiseerd<br>wordt met het “gedefinieerde resultaat” uit de definitie van ‘zaak’ - dat wordt nagestreefd met de behandeling van<br>zaken van dit ZAAKTYPE. Denk aan het nemen van een besluit op een ingediende vergunningaanvraag, het<br>opmaken van een akte naar aanleiding van een aangifte, et cetera.<br>Lengte: 1000 letters en leestekens|
|**Aanleiding**|Een omschrijving van de gebeurtenis die leidt tot het starten van een zaak van dit ZAAKTYPE. Deze attribuutsoort<br>heeft vooral een documentatiefunctie en is bedoeld om een omschrijving te geven van de gebeurtenis - de<br>“gedefinieerde aanleiding” uit de definitie van ‘zaak’ - die leidt tot zaken van dit ZAAKTYPE. Denk bij het<br>uitwerken van deze attribuutsoort niet alleen aan de directe aanleiding - zoals een aanvraag, aangifte of melding -<br>, maar ook aan indirecte aanleidingen. Zo kunnen aanvragen voor een vergunning of meldingen ook voortkomen<br>uit een toezichtzaak.<br>Lengte: 1000 letters en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

|**Indicatie Intern of Extern**|Een aanduiding waarmee onderscheid wordt gemaakt tussen zaken van ZAAKTYPEn die Intern respectievelijk<br>Extern geïnitieerd worden. Middels deze attribuutsoort is het mogelijk onderscheid te maken tussen zaken met<br>een externe initiatie (“Extern”) - bijvoorbeeld bij het aanvragen van een omgevingsvergunning - en zaken met<br>een interne initiatie (Intern) - bijvoorbeeld bij het aanvragen van bijzonder verlof. Indien van beide sprake kan<br>zijn dan prevaleert de externe aanleiding.<br>Waarden: Extern, Intern.  (Lengte: 6)|
|---|---|
|**Handeling initiator**|Werkwoord dat hoort bij de handeling die de initiator verricht bij dit zaaktype. Meestal 'aanvragen', 'indienen' of<br>'melden'.<br>Lengte: 20 letters en leestekens|
|**Onderwerp**|Het onderwerp van zaken van dit ZAAKTYPE. In veel gevallen nauw gerelateerd aan de product- of dienstnaam uit<br>de Producten- en Dienstencatalogus (PDC). Bijvoorbeeld: 'Evenementenvergunning', 'Geboorte', 'Klacht'.<br>Lengte: 80 letters en leestekens|
|**Handeling behandelaar**|Werkwoord dat hoort bij de handeling die de behandelaar verricht bij het afdoen van zaken van dit ZAAKTYPE.<br>Meestal 'behandelen', 'uitvoeren', 'vaststellen' of 'onderhouden'.<br>Lengte: 20 letters en leestekens|
|**Trefwoord**|Een of meer trefwoorden waarmee zaken van het ZAAKTYPE worden gekarakteriseerd.<br>Lengte: 30 letters en leestekens|
|**Archiefclassificatiecode**|De systematische identificatie van zaakdossiers van dit ZAAKTYPE overeenkomstig logisch gestructureerde<br>conventies, methoden en procedureregels. Een zaakdossier betreft alle informatie over een zaak (en daarvan deel<br>uit makende deelzaken) inclusief alle daarbij geregistreerde documenten. Met de archiefclassificatiecode wordt de<br>relatie gelegd naar de plaats van het zaakdossier in het gehanteerde archiveringsclassificatiestelsel, bijvoorbeeld<br>de ‘BasisArchiefCode (BAC)’. Vermeld wordt de classificatiecode in het gehanteerde archiveringsclassificatiestelsel,<br>gevolgd door een spatie en – tussen haakjes  - de gebruikelijke afkorting van de naam van het gehanteerde<br>classificatiestelsel.<br>Lengte: 30 tekens|



**==> picture [103 x 52] intentionally omitted <==**

|**Vertrouwelijkheidaanduiding**|Aanduiding van de mate waarin zaakdossiers van zaken van dit ZAAKTYPE voor de openbaarheid bestemd zijn.<br>Een zaakdossier betreft alle informatie over een zaak (en daarvan deel uit makende deelzaken) inclusief alle<br>daarbij geregistreerde documenten.<br>De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst bijzondere informatie<br>(VIRBI):<br>- ZEER GEHEIM (indien kennisnemen door niet gerechtigden zeer ernstige schade kan toebrengen aan het belang<br>van de Staat of zijn bondgenoten)<br>- GEHEIM (indien kennisnemen door niet gerechtigden ernstige schade kan toebrengen aan het belang van de Staat<br>of zijn bondgenoten)<br>- CONFIDENTIEEL (indien kennisnemen door niet gerechtigden schade kan toebrengen aan het belang van de Staat<br>of zijn bondgenoten)<br>- VERTROUWELIJK (indien kennisnemen door niet gerechtigden nadeel kan toebrengen aan het belang van één of<br>meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties)<br>- ZAAKVERTROUWELIJK (indien kennisnemen door anderen dan betrokkenen bij de zaak nadeel kan toebrengen aan<br>het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere<br>publiekrechtelijke organisaties)<br>- INTERN (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) nadeel kan<br>toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere<br>publiekrechtelijke organisaties)<br>- BEPERKT OPENBAAR (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende<br>organisatie(s) en betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende<br>organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties)<br>- OPENBAAR (in alle andere gevallen)<br>Lengte: 20 letters en leestekens|
|---|---|
|**Producten/Dienst naam**|De namen van de producten en/of diensten zoals deze worden aangeboden als uitkomst van de behandeling van<br>zaken van het ZAAKTYPE. Bijvoorbeeld een product uit de PDC of de UPL (Uniforme ProductenLijst).<br>Lengte: 80 letters en leestekens|
|**URL (producten/dienst)**|De URL naar de beschrijving van het product of de dienst. Bijvoorbeeld de URL naar een productbeschrijving in de<br>producten-en dienstencatalogus op de website.|
|**Formuliernaam**|De naam van het formulier dat zaken van dit ZAAKTYPE initieert.<br>Lengte: 80 letters en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

|**URL (formulier)**|De URL naar het formulier.|
|---|---|
|**Procesnaam**|De naam van het Referentieproces dat ten grondslag ligt aan dit ZAAKTYPE.<br>Lengte: 80 letters en leestekens|
|**URL (proces)**|De URL naar de beschrijving van het Referentieproces.|
|**Verantwoordingsrelatie**|De relatie tussen zaken van dit ZAAKTYPE en de beleidsmatige en/of financiële verantwoording. De zaken die<br>worden uitgevoerd leveren een bijdrage aan / of zijn een invulling van de taken van de organisatie. Met dit<br>attribuut kan de relatie worden gelegd naar de systemen / systematiek waarmee de organisatie rapporteert over<br>de uitvoering van deze taken. Gemeenten en provincie kunnen hier bijvoorbeeld de IV3-functie invullen die zaken<br>van dit ZAAKTYPE relateert aan de systematiek van de financiële verantwoording.<br>Lengte: 40 letters en leestekens|
|**Verantwoordelijke**|De (soort) organisatorische eenheid  of (functie van) medewerker die verantwoordelijk is voor de uitvoering van<br>zaken van het ZAAKTYPE. Afhankelijk van het niveau waarop het zaaktype gespecificeerd wordt, kan de<br>verantwoordelijke afdeling of medewerker nader geduid worden. Indien het om een zaaktype in een catalogus<br>voor een specifieke organisatie gaat, dan de naam van een Organisatorische eenheid of Medewerker<br>overeenkomstig het RGBZ.<br>Lengte: 50 letters en leestekens|
|**Toelichting**|Een eventuele toelichting op dit zaaktype. Deze attribuutsoort heeft vooral een documentatiefunctie en is bedoeld<br>om een toelichting te geven op (de behandeling van) zaken van dit ZAAKTYPE. Hier kan bijvoorbeeld een<br>beschrijving van het procesverloop op hoofdlijnen worden gegeven.<br>Lengte: 1000 letters en leestekens|



## **PUBLICATIE (van indiening)** 

|**Gegeven**|**toelichting**|
|---|---|
|**Publicatie-indicatie**|Aanduiding of (het starten van) een zaak van dit ZAAKTYPE gepubliceerd moet worden. Het gaat hier niet alleen<br>om de wettelijke verplichting tot publicatie maar ook om de eigen keuze van de organisatie die zaken van dit type<br>behandelt.<br>Mogelijke waarden: J, N.|



**==> picture [103 x 52] intentionally omitted <==**

|**Publicatietekst**|De generieke tekst van de publicatie van zaken van dit ZAAKTYPE.<br>Lengte: 1000 letters en leestekens|
|---|---|
|**PLANNING**||
|**Gegeven**|**toelichting**|
|**Doorlooptijd behandeling**|De periode (in kalenderdagen) waarbinnen volgens wet- en regelgeving een zaak van het ZAAKTYPE afgerond<br>dient te zijn. De startdatum van de zaak markeert de eerste dag. De uiterlijke einddatum van de zaak markeert<br>de laatste dag.<br>Mogelijke waarden: 1-999.|
|**Servicenorm behandeling**|De periode (in kalenderdagen) waarbinnen verwacht wordt dat een zaak van het ZAAKTYPE afgerond wordt<br>conform de geldende servicenormen van de zaakbehandelende organisatie(s). De startdatum van de zaak<br>markeert de eerste dag. De geplande einddatum van de zaak markeert de laatste dag.<br>Het spreekt voor zich dat deze periode niet langer mag zijn dan de periode van Doorlooptijd behandeling.<br>Mogelijke waarden: 1-999.|
|**Opschorting/aanhouding**<br>**mogelijk**|Aanduiding die aangeeft of zaken van dit ZAAKTYPE kunnen worden opgeschort en/of aangehouden.<br>Mogelijke waarden: J, N.|
|**Verlenging mogelijk**|Aanduiding die aangeeft of de Doorlooptijd behandeling van zaken van dit ZAAKTYPE kan worden verlengd.<br>Mogelijke waarden: J, N.|
|**Verlengingstermijn**|De termijn in dagen waarmee de Doorlooptijd behandeling van zaken van dit ZAAKTYPE kan worden verlengd. Het<br>is mogelijk dat de verlenging van de behandeltermijn aan wettelijke beperkingen gebonden is. Zo kan de<br>behandeling van een reguliere WABO-procedure één maal met 6 weken (42 dagen) worden verlengd.<br>Mogelijke waarden: 0-999.|



## **STATUSTYPEN** 

Een status is een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak. Het gaat hier dus om bereikte mijlpalen (‘wat is de laatst bereikte mijlpaal’), niet om een aanduiding van onderhanden werk (‘waar zijn we mee bezig’), vanuit het perspectief van de belanghebbende bij een zaak, niet vanuit de behandelaar. 

**==> picture [103 x 52] intentionally omitted <==**

|**Gegeven**|**toelichting**|
|---|---|
|**Statustypevolgnummer**|Een volgnummer voor statussen van het STATUSTYPE binnen een zaak van het ZAAKTYPE. Een zaak doorloopt<br>achtereenvolgens de te vermelden statussen. Het volgnummer legt de volgorde vast waarin de statussen<br>doorlopen worden.<br>Lengte: 4 cijfers|
|**Statustype-omschrijving**|Een korte, voor de initiator van de zaak relevante, omschrijving van de aard van de status van zaken van het<br>ZAAKTYPE. Daar een status een bereikte mijlpaal weergeeft, is een nadrukkelijke richtlijn voor de benaming van<br>een statustype ‘zelfstandig naamwoord + voltooid deelwoord’ waarbij de benaming correspondeert met de fase in<br>de zaak cq. het desbetreffende werkproces. Voorbeelden hiervan zijn “Zaak geregistreerd”, “Indieningsvereisten<br>getoetst”, “Inhoudelijk behandeld”, “Besluit vastgesteld” en “Zaak afgehandeld”<br>Lengte: 80 letters en leestekens|
|**Status-kenmerken:**||
|_Statustype-omschrijving generiek_|Algemeen gehanteerde omschrijving van de aard van statussen van het STATUSTYPE. Het gaat hier om een korte<br>omschrijving van de aard van de status zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de<br>zaakbehandelende organisatie(s) gehanteerde naam, de Statustypeomschrijving.<br>Lengte: 80 letters en leestekens|
|_Doorlooptijd status_|De door de zaakbehandelende organisatie(s) gestelde norm voor de doorlooptijd voor het bereiken van statussen<br>van dit STATUSTYPE, vanaf het bereiken van de voorafgaande status. De zaakbehandelende organisatie(s)<br>bepaalt zelf de hardheid van deze norm: verwachting, servicenorm of harde norm.<br>Mogelijke waarden: 1-999 kalenderdagen|
|_Informeren_|Aanduiding die aangeeft of na het zetten van een status van dit STATUSTYPE de Initiator moet worden<br>geïnformeerd over de statusovergang. Als wordt aangegeven dat de Initiator wordt geïnformeerd, kan de<br>attribuutsoort Statustekst worden gebruikt voor het specificeren van de tekst waarmee de Initiator wordt<br>geïnformeerd over de statusovergang.<br>Mogelijke waarden: J, N.|



**==> picture [103 x 52] intentionally omitted <==**

|_Statustekst_|De tekst die wordt gebruikt om de Initiator te informeren over het bereiken van een status van dit STATUSTYPE<br>bij het desbetreffende ZAAKTYPE.<br>Lengte: 1000 letters en leestekens|
|---|---|
|_Toelichting_|Een toelichting op dit STATUSTYPE. Deze attribuutsoort heeft vooral een documentatiefunctie. Wenselijk is  een<br>beschrijving van hetgeen bereikt is met het procesverloop dat leidt tot deze status. Het gaat daarbij om de stand<br>van zaken bij het bereiken van de status (voltooide deelwoorden), niet om een opsomming van activiteiten of<br>processtappen.<br>Lengte: 1000 letters en leestekens|



## **CHECKLISTitemS bij status** 

Dit betreft te controleren aandachtspunten voorafgaand aan het bereiken van een status van het STATUSTYPE. Per STATUSTYPE kunnen nul of meer checklistitems worden gespecificeerd. 

|**Gegeven**|**Toelichting**|
|---|---|
|||
|**Statustypevolgnummer**|Het volgnummer van het STATUSTYPE waarop het checklistitem van toepassing is.|
|**Itemnaam**|De betekenisvolle benaming van het checklistitem<br>Lengte: 30 letters en leestekens|
|**Vraagstelling**|Een betekenisvolle vraag waaruit blijkt waarop het aandachtspunt gecontroleerd moet worden.<br>Lengte: 255 letters en leestekens|
|**Verplicht**|Het al dan niet verplicht zijn van controle van het aandachtspunt voorafgaand aan het bereiken van de status van<br>het gerelateerde STATUSTYPE.<br>Mogelijke waarden: J, N.|
|**Toelichting**|Beschrijving van de overwegingen bij het controleren van het aandachtspunt<br>Lengte: 1000 letters en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

## **ROLLEN en BETROKKENEN** 

Een rol betreft de taken, rechten en/of verplichtingen die een specifieke betrokkene heeft ten aanzien van een zaak van het ZAAKTYPE. 

|**Gegeven**|**Toelichting**|
|---|---|
|**Roltypeomschrijving**|Omschrijving van de aard van de rol die een betrokkene kan uitoefenen in zaken van het ZAAKTYPE. Het gaat hier<br>om een rolomschrijving die geënt is op het specifieke van zaken van dit ZAAKTYPE. Dit in tegenstelling tot<br>‘Roltypeomschrijving generiek’.<br>Lengte: 20 letters en leestekens|
|**Roltypeomschrijving generiek**|Algemeen gehanteerde omschrijving van de aard van de rol zoals deze voor alle zaaktypen van toepassing is.<br>Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Roltypeomschrijving.<br>Waardenverzameling:<br>- Adviseur: Kennis in dienst stellen van de behandeling van (een deel van) een zaak.<br>- Behandelaar: De vakinhoudelijke behandeling doen van (een deel van) een zaak.<br>- Belanghebbende: Vanuit eigen en objectief belang rechtstreeks betrokken zijn bij de behandeling en/of de<br>uitkomst van een zaak. Nb. De formulering is afgeleid van de belanghebbende in de AWB.<br>- Beslisser: Nemen van besluiten die voor de uitkomst van een zaak noodzakelijk zijn.<br>- Initiator: Aanleiding geven tot de start van een zaak. Nb. Indien het gaat om dienstverlening aan burgers en<br>bedrijven wordt ook wel de term ‘klant’ gehanteerd. Met het oog op andere dan dienstverleningszaken is hier<br>gekozen voor de meer algemene term.<br>- Klantcontacter: Het eerste aanspreekpunt zijn voor vragen van burgers en bedrijven in het kader van de<br>dienstverlening door de organisatie aan burgers en bedrijven. Nb. Met betrekking tot het zaakgericht werken<br>betreft dit veelal het verzorgen van de intake van een vraag naar een product of dienst, het informeren over de<br>voortgang van de behandeling van de zaak en het leveren van de uitkomst van de zaak..<br>- Zaakcoördinator: Er voor zorg dragen dat de behandeling van de zaak in samenhang uitgevoerd wordt conform de<br>daarovergemaakte afspraken.|
|**Betrokkenen**|De (soort) betrokkene die een rol van dit ROLTYPE mag uitoefenen. Dit gegeven heeft primair een<br>documentatiefunctie.<br>Lengte: 80 letters en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

|**Mag zetten Status(sen)**|De STATUSTYPEn die een betrokkene in een rol van dit ROLTYPE mag zetten. Een status kan alleen gezet worden<br>door een betrokkene, zijnde een organisatorische eenheid of medewerker, niet door een willekeurig andere<br>betrokkene. Gebruik hierbij de statusvolgnummers.|
|---|---|



## **ZaakOBJECTEN** 

Het gaat hier om de typen van objecten waarop een zaak van het ZAAKTYPE betrekking kan hebben. Een zaak kan op ‘van alles en nog wat’ betrekking hebben.  Voor zover dit in het RSGB of RGBZ onderscheiden objecttypen betreft, wordt hier gespecificeerd op welke van de RSGB- en/of RGBZobjecttypen zaken van het gerelateerde ZAAKTYPE betrekking kunnen hebben. Voor zover het andere objecten betreft, wordt gespecificeerd welke andere typen objecten dit betreft. Voor alle duidelijkheid, het gaat dus niet om betrokkenen die een rol in de zaak hebben (die specificeren we bij ‘Rollen en betrokkenen’). 

|**Gegeven**|**Toelichting**|
|---|---|
|**Objecttype**|De naam van het objecttype waarop zaken van het gerelateerde ZAAKTYPE betrekking hebben.<br>Het kan een in het RGBZ of RSGB onderscheiden objecttype betreffen dan wel een ander objecttype. Als ‘Ander<br>objecttype’ de waarde 'N' (Nee) heeft, dient de naam van een objecttype uit het RSGB of het RGBZ te worden<br>gekozen. Als ‘Ander objecttype’ de waarde 'J' (Ja) heeft, dan heeft deze attribuutsoort de naam van een ander,<br>niet in het RSGB en het RGBZ voorkomend,  objecttype dat relevant is voor zaken van het gerelateerde<br>ZAAKTYPE (bijv. 'Wipkip' of ‘Handhavingsobject’).<br>Lengte: 40 letters en leestekens|
|**Ander objecttype?**|Aanduiding waarmee wordt aangegeven of het ZAAKOBJECTTYPE  een ander, niet in RSGB en RGBZ voorkomend,<br>objecttype betreft.<br>Mogelijke waarden:<br>- J (Ja; het betreft een objecttype dat niet voorkomt in het RSGB en RGBZ).<br>- N(Nee;het betreft een objecttype uit het RSGB of RGBZ).|
|**Verplicht bij Status**|STATUSTYPEn waarvoor geldt dat er een object van dit ZAAKOBJECTTYPE verplicht gerelateerd moet zijn aan een<br>zaak van dit ZAAKTYPE voordat die status kan worden gezet.<br>Gebruik voor de verwijzing het Statustypevolgnummer.|



**==> picture [103 x 52] intentionally omitted <==**

|**Verplicht bij Resultaat**|De RESULTAATTYPEn waarvoor geldt dat er verplicht een object van dit ZAAKOBJECTTYPE moet zijn gerelateerd<br>aan de zaak voordat een Resultaat van het RESULTAATTYPE kan worden gezet.|
|---|---|
|**Relatieomschrijving**|Omschrijving van de betrekking van objecten van het ZAAKOBJECTTYPE op zaken van het gerelateerde<br>ZAAKTYPE. Het gaat hier om het duiden van de aard van de betrokkenheid van het objecttype bij zaken van het<br>gerelateerde zaaktype en/of het belang van dat objecttype voor die zaken.<br>Lengte: 80 letters en leestekens|



## **EIGENSCHAPPEN** 

Dit betreft relevante inhoudelijk gegevens die bij Zaken van dit ZAAKTYPE geregistreerd moeten kunnen worden en geen standaard kenmerk zijn van een zaak. Met het laatste wordt bedoeld de attributen die in het RGBZ gespecificeerd zijn bij ZAAK en bij de andere daarin opgenomen objecttypen. Deze kenmerken zijn generiek d.w.z. van toepassing op elke zaak, ongeacht het zaaktype. Niet voor elke zaak van elk zaaktype is dit voldoende informatie voor – de besturing van – de behandeling van de zaak en om daarover informatie uit te kunnen wisselen. Zo is voor het behandelen van een aanvraag voor een kapvergunning informatie nodig over de locatie, het type en de diameter van de te kappen boom nodig. Het RGBZ bevat reeds de locatiekenmerken. Boomtype en Stamdiameter zijn gegevens die specifiek zijn voor zaken van dit zaaktype, de zaaktypespecifieke eigenschappen. Een ander voorbeeld is de evenementdatum bij de behandeling van een aanvraag voor een evenementenvergunning. 

Een zaaktypespecifieke eigenschap wordt op één van twee wijzen gespecificeerd: 

- 1) door het specificeren van de gegevenstechnische kenmerken van de eigenschap (m.b.v. Groep, Formaat, Lengte, Kardinaliteit en Waardenverzameling); 

2) door te refereren naar een berichtenmodel en, bij voorkeur ook, een informatiemodel (m.b.v. Objecttype, Informatiemodel, Namespace, Schemalocatie, X-path element en Entiteittype). De eigenschap wordt aldus ontleend aan een XML-schema (als onderdeel van een berichtenmodel) dat reeds bestaat of specifiek voor het zaaktype (of de zaaktypecatalogus of het desbetreffende domein) is opgesteld. 

|**Gegeven**|**toelichting**|
|---|---|
|**Eigenschapnaam**|De naam van de EIGENSCHAP. Bijvoorbeeld ‘Gevraagd subsidiebedrag’, ‘Boomdiameter’.<br>Lengte: 20 letters en leestekens|
|**Eigenschap-kenmerken:**||



**==> picture [103 x 52] intentionally omitted <==**

|_Definitie_|De beschrijving van de betekenis van deze EIGENSCHAP. Eigenschappen vormen een krachtige en flexibele<br>functionaliteit voor het registreren van relevante kenmerken voor zaken van een specifiek ZAAKTYPE. Die kracht<br>staat of valt echter met een heldere, eenduidige definitie van de EIGENSCHAP. Bijvoorbeeld: "De omtrek van de<br>boom in centimeters, gemeten op een hoogte van 1 meter boven het maaiveld."<br>Lengte: 255 letters en leestekens|De beschrijving van de betekenis van deze EIGENSCHAP. Eigenschappen vormen een krachtige en flexibele<br>functionaliteit voor het registreren van relevante kenmerken voor zaken van een specifiek ZAAKTYPE. Die kracht<br>staat of valt echter met een heldere, eenduidige definitie van de EIGENSCHAP. Bijvoorbeeld: "De omtrek van de<br>boom in centimeters, gemeten op een hoogte van 1 meter boven het maaiveld."<br>Lengte: 255 letters en leestekens|
|---|---|---|
|**_Specificatie van eigenschap:_**|Met de hiertoe behorende gegevens wordt een eigenschap gedetailleerd gespecificeerd.Dit vindt alleen plaats als<br>de eigenschap niet gespecificeerd is door middel van‘Referentie naar eigenschap’.||
|_- Groep_||Benaming van het object of groepattribuut waarvan de EIGENSCHAP een inhoudelijk gegeven specificeert.<br>Bijvoorbeeld: “subsidie”, “boom”.<br>Lengte: 32 letters, cijfers en leestekens|
|_- Formaat_||Het soort tekens waarmee waarden van de EIGENSCHAP kunnen worden vastgelegd.<br>Waardenverzameling: tekst, getal, datum (jjjjmmdd), datum/tijd (jjjjmmdduummss). Lengte: 20|
|_- Lengte_||Het aantal karakters (lengte) waarmee waarden van de EIGENSCHAP worden vastgelegd.<br>Waardenverzameling: Als Formaat = tekst: 0-255, Als Formaat = getal: n,m (n: aantal cijfers geheel getal, m:<br>aantal decimalen), Als Formaat=datum: 8, Als Formaat=datum/tijd: 14.  Lengte: 14|
|_- Kardinaliteit_||Het aantal mogelijke voorkomens van waarden van deze EIGENSCHAP bij een zaak van het ZAAKTYPE.<br>Waardenverzameling: gehele getallen groter dan 0, 'N' voor ongelimiteerd.  Waardenverzameling: gehele<br>getallen groter dan 0 en'N'voor ongelimiteerd. Lengte: 3|
|_- Waardenverzameling_||De - verzameling van - waarden die gegevens van deze EIGENSCHAP kunnen hebben. Door middel van deze<br>attribuutsoort kan een (reeks van) waarde(n) voor de EIGENSCHAP worden gedefinieerd. Bijvoorbeeld: 'Ja' en<br>'Nee'.  Lengte: 100|
|**_Referentie naar eigenschap:_**|Met de hiertoe behorende gegevens wordt een eigenschap benoemd door middel van een verwijzing naar de<br>standaard (berichtenmodel cq. namespace en, bij voorkeur ook, een informatiemodel) waarin de eigenschap is<br>gespecificeerd. Dit vindt alleen plaats als de eigenschap niet gespecificeerd is door middel van ‘Specificatie van<br>eigenschap’.||
|_- Objecttype_||De naam van het objecttype waarbij de eigenschap is gemodelleerd in het informatiemodel waarvan het<br>objecttype deel uit maakt.<br>Lengte: 40letters, cijfers en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

|_- Informatiemodel_|_- Informatiemodel_|De naam en de versie van het informatiemodel waarin de eigenschap is gemodelleerd.<br>Lengte:80letters, cijfers en leestekens|
|---|---|---|
|_- Namespace_||De naam van het XML-schema waarin de eigenschap is opgenomen.<br>Lengte: 200letters, cijfers en(bepaalde)leestekens|
|_- Schemalocatie_||De locatie van het XML-schema behorend bij de Namespace.<br>Lengte: 200letters, cijfers en(bepaalde)leestekens|
|_- X-path element_||De naam van de eigenschap en het pad daarnaar toe in het XML-schema behorend bij de namespace.<br>Lengte: 255letters, cijfers en(bepaalde)leestekens|
|_- Entiteittype:_||De naam van de XML-constructie in het XML-schema behorend bij de namespace die afgeleid is van de naam<br>van het objecttype en waarin de eigenschap is opgenomen.<br>Lengte:80letters, cijfers en(bepaalde)leestekens|
|_Verplicht bij Status_|STATUSTYPEn bij het ZAAKTYPE waarvoor geldt dat de EIGENSCHAP verplicht van een waarde voorzien moet zijn<br>voordat die status kan worden gezet.<br>Gebruik voor de verwijzing het Statustypevolgnummer.||
|_Toelichting_|Een toelichting op deze EIGENSCHAP en het belang hiervan voor zaken van dit ZAAKTYPE.<br>Lengte: 1000 letters en leestekens||



## **ZAAKDOCUMENTEN** 

Dit betreft de specificatie van typen van documenten die relevant kunnen zijn voor zaken van dit ZAAKTYPE.  We hebben hier, omwille van de begrijpelijkheid, gekozen voor de term ‘document’ waar we formeel van ‘informatieobject’ zouden moeten spreken. ‘Informatieobject’ is een generiekere term voor het veelgebruikte begrip ‘document’ dat beperkter van reikwijdte is. Een informatieobject kan van alles zijn, ongeacht aard en vorm: een tekstverwerkingsdocument, een papieren brief, een webpagina, een landkaart, een foto, een geluidsopname, een dataset, een blog, etcetera. En ook een digitaal ontvangen of gecreeerd informatieobject dat bestaat uit meerdere fysieke informatieobjecten, zoals een aanvraag (als tekstdocument) met bijbehorende tekening (CAD-formaat) en berekening (spreadsheet) of een email met bijlage(n). Net zoals dezelfde aanvraag op papier met bijlagen als één informatieobject beschouwd kan worden. De fysieke vorm van hetgeen ontvangen of gecreeerd is, is dus niet (alleen) bepalend voor de afbakening van dat wat als informatieobject beschouwd wordt. 

**==> picture [103 x 52] intentionally omitted <==**

|**Gegeven**|**Toelichting**|
|---|---|
|**Volgnummer**|Uniek volgnummer  van het zaakdocumenttype binnen het ZAAKTYPE.<br>Het volgnummer is alleen voor documentatiedoeleinden. Het wordt gebruikt om binnen een ZAAKTYPE te kunnen<br>verwijzen naar een zaakdocumenttype en om zaakdocumenttypen in schema’s te kunnen vermelden.|
|**Documenttype-omschrijving**|Omschrijving van de aard van documenten van dit Documenttype.  Het gaat hier om een korte omschrijving van de<br>aard van gelijksoortige documenten, ook wel documentsoort genoemd. Voorbeelden: Bouwaanvraag,<br>Kapvergunning, Taxatieverslag, Geboorte-akte.<br>Aan te bevelen is dus om aan te sluiten bij een (landelijke) domeinwaardencatalogus zoals gemodelleerd met<br>Documenttypeomschrijving generiek. Het is minimaal noodzakelijk dat een Zaakdocument dat in een CATALOGUS<br>bij meerdere ZAAKTYPEn voor komt, in al die vermeldingen dezelfde Documenttype-omschrijving heeft.<br>Let op dat het hier alleen om het onderwerp gaat; trefwoorden worden vastgelegd in Documenttypetrefwoord.<br>Lengte: 80 letters en leestekens|
|**Documenttype-kenmerken**||
|_Documentcategorie_|Typering van de aard van documenten van dit Documenttype.<br>Voorbeelden hiervan zijn ‘Vergunning’, ‘Subsidie-aanvraag’, ‘Onderzoeksrapport’, Besluit. Aan te bevelen is dus om<br>te komen tot een (landelijke) domeinwaardenverzameling.<br>Lengte: 80 letters en leestekens|
|_Documenttype-omschrijving_<br>_generiek_|Algemeen gehanteerde omschrijving van het Documenttype. Het gaat hier om een korte generieke omschrijving<br>van de aard van gelijksoortige documenten, ook wel documentnaam genoemd, zoals deze landelijk wordt<br>toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de<br>Documenttype-omschrijving. De domeinwaarden zijn opgenomen in een specifieke referentiewaardenlijst als<br>onderdeel van de ZTC2. De daarin aanwezige waarden zijn overgenomen uit de NEN2084 en aangevuld met voor<br>de overheid (als geheel) relevante documenttypen.<br>Lengte: 80 letters en leestekens|
|_Documenttypetrefwoord_|Trefwoord(en) waarmee documenten van het Documenttype kunnen worden gekarakteriseerd.<br>Lengte: 30 letters en leestekens|
|_Vertrouwelijkheidaanduiding_|Aanduiding van de mate waarin documenten van dit Documenttype voor de openbaarheid bestemd zijn.<br>Met dit gegeven kan worden gespecificeerd in welke mate documenten van dit Documenttype bestemd zijn voor<br>de openbaarheid. Zo kan een zaak waarvoor in het ZAAKTYPE is vastgelegd dat de Vertrouwelijkheidaanduiding<br>'Openbaar'is, toch documenten bevatten die op basis van hun Documenttype niet-samen met de openbare|



**==> picture [103 x 52] intentionally omitted <==**

||zaakinformatie - 'Openbaar' worden gemaakt. Denk bijvoorbeeld aan privacygevoelige informatie zoals een Bibob-<br>advies.<br>De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst bijzondere informatie<br>(VIRBI).<br>- ZEER GEHEIM (indien kennisnemen door niet gerechtigden zeer ernstige schade kan toebrengen aan het belang<br>van de Staat of zijn bondgenoten)<br>- GEHEIM (indien kennisnemen door niet gerechtigden ernstige schade kan toebrengen aan het belang van de Staat<br>of zijn bondgenoten)<br>- CONFIDENTIEEL (indien kennisnemen door niet gerechtigden schade kan toebrengen aan het belang van de Staat<br>of zijn bondgenoten)<br>- VERTROUWELIJK (indien kennisnemen door niet gerechtigden nadeel kan toebrengen aan het belang van één of<br>meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties)<br>- ZAAKVERTROUWELIJK (indien kennisnemen door anderen dan betrokkenen bij de zaak nadeel kan toebrengen aan<br>het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere<br>publiekrechtelijke organisaties)<br>- INTERN (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende organisatie(s) nadeel kan<br>toebrengen aan het belang van één of meer zaakbehandelende organisaties, betrokkenen bij de zaak en/of andere<br>publiekrechtelijke organisaties)<br>- BEPERKT OPENBAAR (indien kennisnemen door anderen dan medewerkers van de zaakbehandelende<br>organisatie(s) betrokkenen bij de zaak nadeel kan toebrengen aan het belang van één of meer zaakbehandelende<br>organisaties, betrokkenen bij de zaak en/of andere publiekrechtelijke organisaties)<br>- OPENBAAR (in alle andere gevallen).<br>Deze attribuutsoort prevaleert boven de Vertrouwelijkheidaanduiding van het ZAAKTYPE. Indien geen<br>Vertrouwelijkheidaanduiding voor het Documenttype is ingesteld, wordt deze bepaald door de<br>Vertrouwelijkheidaanduiding van het ZAAKTYPE.<br>Lengte: 20 letters en leestekens|
|---|---|
|_Richting_|Aanduiding van de verzendrichting van documenten van dit Zaakdocumenttype binnen zaken van dit ZAAKTYPE.<br>Waardenverzameling:'Inkomend','Intern','Uitgaand'. Lengte 20.|



**==> picture [103 x 52] intentionally omitted <==**

|_Model_|De URL naar het model / sjabloon dat wordt gebruikt voor de creatie van documenten van dit Documenttype.<br>Voor veel documenttypen worden standaardmodellen / -sjablonen gedefinieerd die worden gebruikt voor de<br>creatie van nieuwe documenten. Deze attribuutsoort relateert dergelijke sjablonen aan - de creatie van<br>documenten van-dit Documenttype.|
|---|---|
|_Verplicht bij Status_|Het STATUSTYPE van de eerste status bij het ZAAKTYPE waarvoor geldt dat er een document van dit<br>Documenttype verplicht aanwezig moeten zijn in het zaakdossier van een zaak voordat die status kan worden<br>gezet.<br>Gebruik voor de verwijzing het Statustypevolgnummer.|
|_Verplicht bij Resultaat_|De RESULTAATTYPEn van resultaten waarvoor geldt dat er verplicht een document van dit Documenttype in het<br>zaakdossier van zaken van het ZAAKTYPE aanwezig moet zijn voordat zo’n  resultaat kan worden gezet.|
|_Toelichting_|Een eventuele toelichting op dit Documenttype. Dit gegeven heeft vooral een documentatiefunctie. Hier kan<br>bijvoorbeeld een beschrijving worden gegeven van de betekenis van het documenttype en de aard van de<br>documenten die ertoe behoren.<br>Lengte: 1000 letters en leestekens|



## **BESLUITEN** 

Dit betreft typen van besluiten (BESLUITTYPEn) die relevant kunnen zijn voor zaken van dit ZAAKTYPE. 

|**Gegeven**|**toelichting**|
|---|---|
|**Besluittype-omschrijving**|Omschrijving van de aard van besluiten van het BESLUITTYPE. Het gaat hier om een korte omschrijving van de<br>aard van het besluit, ook wel besluitnaam genoemd. Voorbeelden: Lichte bouwvergunning, Kapvergunning,<br>Ontheffing geluidhinder en Monumentensubsidie.<br>Lengte: 80 letters en leestekens|
|**Besluittype-kenmerken:**||



**==> picture [103 x 52] intentionally omitted <==**

|_Besluittype-omschrijving generiek_|Algemeen gehanteerde omschrijving van de aard van besluiten van het BESLUITTYPE. Het gaat hier om een korte<br>omschrijving van de aard van het besluit, ook wel besluitnaam genoemd, zoals deze landelijk wordt toegepast.<br>Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Besluittype-<br>omschrijving.<br>Lengte: 80 letters en leestekens|
|---|---|
|_Besluitcategorie_|Typering van de aard van besluiten van het BESLUITTYPE. Het gaat hier om de indeling van besluittypen naar<br>categorieën zoals Vergunning, Ontheffing en Subsidie.<br>Waardenverzameling: gebaseerd op de AWB. Lengte: 40|
|_Reactietermijn_|Het aantal kalenderdagen, gerekend vanaf de verzend- of publicatiedatum, waarbinnen verweer tegen een besluit<br>van het besluittype mogelijk is. De telling begint bij de dag volgend op de verzend- of publicatiedatum.  Indien<br>geen sprake is van een reactietermijn dan is de waarde nul.<br>Mogelijke waarden: 0-999 kalenderdagen|
|_Publicatie-indicatie_|Aanduiding of besluiten van dit BESLUITTYPE gepubliceerd moeten worden. Het gaat hier niet alleen om de<br>wettelijke verplichting tot publicatie maar ook om de eigen keuze van de organisatie die besluiten van dit type<br>neemt.<br>Mogelijke waarden: J, N.|
|_Publicatietekst_|De generieke tekst van de publicatie van besluiten van dit BESLUITTYPE.<br>Lengte: 1000 letters en leestekens|
|_Publicatietermijn_|Het aantal kalenderdagen, gerekend vanaf de verzend- of publicatiedatum, dat besluiten van dit BESLUITTYPE<br>gepubliceerd moeten blijven. De telling begint bij de dag volgend op de verzend- of publicatiedatum.<br>Mogelijke waarden: 0-999 kalenderdagen|
|_Documenttype_|De Documenttype-omschrijving van het ZAAKDOCUMENTTYPE waarin besluiten van dit BESLUITTYPE worden<br>vastgelegd.|
|_Toelichting_|Een eventuele toelichting op dit BESLUITTYPE. Deze attribuutsoort heeft vooral een documentatiefunctie. Hier kan<br>bijvoorbeeld een beschrijving worden gegeven van de betekenis van het besluit voor - het verloop van - een<br>ZAAKTYPE.<br>Lengte: 1000 letters en leestekens|



**==> picture [103 x 52] intentionally omitted <==**

## **RESULTATEN en BEWAARTERMIJNEN** 

Hiermee worden de mogelijke resultaten benoemd bij zaken van het ZAAKTYPE. Dit is iets anders dan de uitkomst van een zaak in de vorm van een geleverd product of dienst. Een resultaat wordt dan ook in procedurele zin benoemd (hoe is de zaak geëindigd), niet in inhoudelijke zin. Elke zaak heeft een resultaat. In een aantal gevallen valt dit resultaat samen met een besluit: ‘Evenementenvergunning verleend’, ‘Energiesubsidie geweigerd’, et cetera. Het komt echter ook voor dat zaken worden afgehandeld zonder dat er een besluit wordt genomen. Dit is bijvoorbeeld het geval bij aangiften (geboorte, verhuizing), meldingen (openbare ruimte), maar ook bij het intrekken van een aanvraag. 

Het resultaat van een zaak is van groot belang voor de archivering: het resultaattype bepaalt mede of de zaak en het bijbehorende dossier moeten worden vernietigd (na enige termijn) of blijvend bewaard moeten worden (en na enige termijn ‘overgebracht’ worden naar een archiefbewaarplaats). Het archiefregime wordt voor het gehele zaakdossier per resultaattype bepaald met de kenmerken in de eerstvolgende tabel. In bijzondere gevallen is het mogelijk dat voor (documenten van) een specifiek documenttype in het zaakdossier een ander archiefregime geldt. Deze uitzonderingsgevallen worden gespecificeerd in de tweede tabel. 

|**Gegeven**|**Toelichting**|
|---|---|
|**Resultaattypeomschrijving**|Omschrijving van de aard van resultaten van het RESULTAATTYPE. Het gaat hier om de benaming van resultaten<br>(van uitvoering van zaken van het betreffende zaaktype) zoals de organisatie die hanteert. Deze kunnen afwijken<br>van hetgeen standaard is voor het domein cq. de ZTC die voor dat domein is opgesteld. Aan te bevelen is zoveel<br>mogelijk aan te sluiten bij die standaard zijnde de waarden in ‘Resultaattype-omschrijving generiek’.<br>Lengte: 20 tekens|
|**Resultaattype-kenmerken:**||
|_Resultaattypeomschrijving generiek_|Algemeen gehanteerde omschrijving van de aard van resultaten van het RESULTAATTYPE. Het gaat hier om een<br>korte omschrijving van de aard van het resultaat, zoals deze landelijk wordt toegepast voor zaken van het<br>betreffende ZAAKTYPE en is opgenomen in de ZTC voor het betreffende domein. Deze kan afwijken van de door<br>de zaakbehandelende organisatie(s) gehanteerde naam, de Resultaattypeomschrijving. Het gaat om resultaten<br>zoals 'verleend', 'toegekend', 'afgewezen', 'verwerkt', 'gegrond', 'ongegrond', 'geweigerd', 'niet nodig',<br>'ontvankelijk', 'niet ontvankelijk', 'vastgesteld', 'niet vastgesteld'.<br>Lengte: 20 tekens|



**==> picture [103 x 52] intentionally omitted <==**

|_Selectielijstklasse_|Verwijzing naar de voor het archiefregime bij het RESULTAATTYPE relevante passage in de selectielijst van de<br>voor het ZAAKTYPE verantwoordelijke overheidsorganisatie. Bij gemeenten gaat het om de aanduidingen van de<br>categorie in de Selectielijst waarin per categorie de bewaartermijn wordt vermeld van de daartoe behorende<br>soorten documenten. In niet-gemeentelijke selectielijsten wordt soms een ander begrip dan categorie gehanteerd.<br>Waardenverzameling: de aanduidingen van de passages cq. klassen in de gehanteerde selectielijst.<br>Lengte: 500 tekens|
|---|---|
|_Archiefnominatie_|Aanduiding die aangeeft of dossiers van zaken met een resultaat van dit RESULTAATTYPE blijvend moeten worden<br>bewaard of (op termijn) moeten worden vernietigd. De vermelding specificeert het ‘archiefregime’ voor de<br>zaakdossiers van het ZAAKTYPE waarvan een zaak het desbetreffende RESULTAATTYPE heeft. Het archiefregime<br>van zaken van een ZAAKTYPE verschilt naar gelang het resultaat van die zaken.<br>In het geval van vernietigen wordt het zaakdossier na enige tijd vernietigd. In het geval van blijvend bewaren<br>wordt het zaakdossier na enige tijd overgebracht naar een archiefbewaarplaats (de in art. 12 van de Archiefwet<br>1995 bepaalde algemene termijn is 20 jaar). Door middel van het gegeven Archiefactietermijn wordt<br>gespecificeerd na verloop van hoeveel tijd wordt overgegaan tot vernietiging resp. overbrenging.<br>Waardenverzameling:‘Blijvend bewaren’,‘Vernietigen’.|
|_Archiefactietermijn_|De termijn, in maanden, waarna het zaakdossier (de zaak met alle bijbehorende documenten) van een zaak met<br>een resultaat van dit RESULTAATTYPE vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden.<br>Of sprake is van vernietigen of overbrengen (in het geval van blijvend bewaren) wordt gespecificeerd met het<br>gegeven ‘Archiefnominatie’.<br>De datum waarop deze termijn start, is afhankelijk van de waarde van ‘Brondatum archiefprocedure’.<br>De algemene termijn voor overbrenging is 20 jaar cq. 240 maanden. Lengte: 4 cijfers.|



**==> picture [103 x 52] intentionally omitted <==**

|_Brondatum archiefprocedure_|Brondatum voor de start van de Archiefactietermijn van het zaakdossier.<br>Het betreft het ‘datumveld’ waarvan de daarin vermelde datum als startdatum van de Archiefactietermijn<br>genomen moet worden. Meerdere datumvelden komen hiervoor in aanmerking. Dit geeft de volgende<br>waardenverzameling:<br>- 'afgehandeld': de termijn start op de datum waarop de zaak is afgehandeld (ZAAK.Einddatum in het RGBZ),<br>- 'ingangsdatum besluit': de termijn start op de datum waarop het besluit van kracht wordt (BESLUIT.Ingangsdatum<br>in het RGBZ),<br>-  'vervaldatum besluit': de termijn start op de dag na de datum waarop het besluit vervalt (BESLUIT.Vervaldatum in<br>het RGBZ),<br>- ‘eigenschap’: de termijn start op de datum die vermeld is in een zaaktype-specifieke eigenschap (zijnde een<br>‘datumveld’);<br>-  'ander datumkenmerk': de termijn start op de datum die in een ander datumveld bij de zaak of bij een<br>gerelateerde zaak (voorafgaand, volgend op of deelzaak)  is vastgelegd.<br>In het geval van ‘ander datumkenmerk’ zal de einddatum van de archiefactietermijn bij een specifieke zaak<br>handmatig bepaald moeten worden, in andere gevallen kan deze berekend worden.|
|---|---|
|_Relevante Eigenschap Brondatum_<br>_archiefprocedure_|De EIGENSCHAP die bepalend is voor het moment waarop de Archiefactietermijn start voor een zaak met een<br>resultaat van dit RESULTAATTYPE.<br>Het datumveld dat bepalend is voor de start van de bewaartermijn wordt gespecificeerd met de attribuutsoort<br>‘Brondatum archiefprocedure’. Indien dit een zaaktype-specifieke eigenschap is, dan wordt met dit gegeven<br>aangeduid om welke eigenschap het gaat. Denk bijvoorbeeld aan eigenschappen als 'Datum geboorte' bij een<br>geboorteaangifte, 'Datum uit dienst' bij pensionering, et cetera.<br>Waardenverzameling: één van de hiervoor gespecificeerde Eigenschapnamen.<br>Lengte: 20 letters en leestekens|
|_Leidt tot BESLUIT(en):_|Het BESLUITTYPE van besluiten die gepaard gaan met resultaten van het RESULTAATTYPE.|
|_Heeft verplicht(e)_<br>_ZAAKOBJECTTYPE(n):_|De objecten van ZAAKOBJECTTYPEn die verplicht gerelateerd moeten zijn aan zaken van dit ZAAKTYPE voordat<br>een resultaat van dit RESULTAATTYPE kan worden gezet.|



**==> picture [103 x 52] intentionally omitted <==**

|_Toelichting_|Een toelichting op dit RESULTAATTYPE en het belang hiervan voor zaken waarin een Resultaat van dit<br>RESULTAATTYPE wordt geselecteerd. Naast een toelichting op het resultaattype en het belang hiervan wordt<br>hierin (tekstueel) aangegeven op basis van welk datumveld de brondatum voor de archiefprocedure  bepaald<br>wordt indien dit een ‘ander datumkenmerk’  is zoals gespecificeerd bij ’Brondatum archiefprocedure’.<br>Lengte: 1000 tekens|
|---|---|
|Voor specifieke zaakdocumenttypen worden met onderstaande specificaties de eventuele afwijkingen gespecificeerd van het archiefregime van het<br>zaakdossier.||
|**Gegeven**|**Toelichting**|
|_Resultaattypeomschrijving_|Eén van de, in de voorafgaande tabel genoemde, Resultaattype-omschrijvingen waarbij een afwijkend<br>archiefregime geldt voor een specifiek documenttype.|
|_Zaakdocument-volgnummer_|Het unieke volgnummer  van het Zaakdocumenttype, zoals vermeld in de specificatie van zaakdocumenten,<br>waarvoor het afwijkende archiefregime geldt.|
|_Documenttype-omschrijving_|De Documenttype-omschrijving van het Zaakdocumenttype, zoals vermeld in de specificatie van<br>zaakdocumenten, waarvoor het afwijkende archiefregime geldt.|
|_Selectielijstklasse_|Verwijzing naar de voor het Zaakdocumenttype bij het RESULTAATTYPE relevante passage in de selectielijst van<br>de voor het ZAAKTYPE verantwoordelijke overheidsorganisatie. Bij gemeenten gaat het om de aanduidingen van<br>de categorie in de Selectielijst waarin per categorie de bewaartermijn wordt vermeld van de daartoe behorende<br>soorten documenten. In niet-gemeentelijke selectielijsten wordt soms een ander begrip dan categorie gehanteerd.<br>Waardenverzameling: de aanduidingen van de passages cq. klassen in de gehanteerde selectielijst.<br>Lengte: 500 tekens|



**==> picture [103 x 52] intentionally omitted <==**

|_Archiefnominatie_|Aanduiding die aangeeft of documenten van het Zaakdocumenttype bij een zaak met een resultaat van dit<br>RESULTAATTYPE blijvend moeten worden bewaard of (op termijn) moeten worden vernietigd. De vermelding<br>specificeert het ‘archiefregime’ voor documenten, van een specifiek Zaakdocumenttype, in zaakdossiers van het<br>ZAAKTYPE waarvan een zaak het desbetreffende RESULTAATTYPE heeft.<br>In het geval van vernietigen wordt het document na enige tijd vernietigd. In het geval van blijvend bewaren<br>wordt het document na enige tijd overgebracht naar een archiefbewaarplaats (de in art. 12 van de Archiefwet<br>1995 bepaalde algemene termijn is 20 jaar). Door middel van het gegeven Archiefactietermijn wordt<br>gespecificeerd na verloop van hoeveel tijd wordt overgegaan tot vernietiging resp. overbrenging.<br>Waardenverzameling:‘Blijvend bewaren’,‘Vernietigen’.|
|---|---|
|_Archiefactietermijn_|De termijn, in maanden, waarna documenten, van het Zaakdocumenttype, bij een zaak met een resultaat van dit<br>RESULTAATTYPE vernietigd of overgebracht (naar een archiefbewaarplaats) moeten worden.<br>Of sprake is van vernietigen of overbrengen (in het geval van blijvend bewaren) wordt gespecificeerd met het<br>gegeven ‘Archiefnominatie’.<br>De datum waarop deze termijn start, is afhankelijk van de waarde van ‘Brondatum archiefprocedure’ bij het<br>RESULTAATTYPE in de voorafgaande tabel.<br>De algemene termijn voor overbrenging is 20 jaar cq. 240 maanden. Lengte: 4 cijfers.|



## **DEELZAKEN** 

Een zaak van een (ander) zaaktype kan als deelzaak uitgevoerd worden van een zaak van het voorliggende zaaktype. Voor elke zaak geldt, hoofdzaak of deelzaak, dat de afbakening van een zaak overeen komt met een bedrijfsproces: ‘van klant tot klant’. Onderdelen van bedrijfsprocessen vormen geen zelfstandige zaken. Van deelzaken is alleen sprake als voor de gewenste producten en/of diensten, naar aanleiding van de klantvraag, separate bedrijfsprocessen zijn voorzien. Kenmerkend voor die bedrijfsprocessen is dat ze dezelfde aanleiding hebben: de klantvraag (niet te verwarren met de vraag vanuit de behandeling van een zaak om daaraan op een specifiek aspect een bijdrage te leveren; zie ‘bijdragezaken’ verderop). Met de ‘hoofdzaak’ wordt gecoördineerd dat de optelsom van de te leveren producten en diensten beantwoord aan de oorspronkelijke klantvraag. 

|**Gegeven**|**Toelichting**|
|---|---|
|Zaaktype|De Zaaktype-omschrijving van een zaak van een (ander) ZAAKTYPE die als deelzaak van het voorliggende<br>ZAAKTYPE behandeld kan worden.|



**==> picture [103 x 52] intentionally omitted <==**

Toelichting Een beschrijving van de situatie waarin sprake kan zijn van genoemd zaaktype als deelzaak van het voorliggende zaaktype. 

## **VERVOLGZAKEN** 

De situatie kan zich voordoen dat bij afronding van een zaak de start van een volgende zaak gepland moet worden. Bijvoorbeeld een hercontrole(zaak) bij afronding van een controlezaak waarin weg te nemen strijdigheden geconstateerd zijn. Door de zaaktypen van dergelijke zaken te specificeren, wordt een keten van zaken verkregen waarmee de opeenvolging van onderling afhankelijke bedrijfsprocessen bewaakt kan worden. Voor alle duidelijkheid, het betreft alleen te plannen zaken, niet zaken die mogelijkerwijs een vervolg kunnen zijn op de voorliggende zaak maar waarvan de start niet bewaakt hoeft te worden. Een voorbeeld van het laatste is een bezwaarzaak als reactie op een besluit dat vastgesteld is in een vergunningzaak. Bij afronding van de vergunningzaak hoeft het starten van de bezwaarzaak niet bewaakt te worden. Dat een bezwaarzaak betrekking heeft op een vergunningzaak wordt, bij het bezwaarzaaktype, vermeld onder ‘voorafgaande zaken’. 

|**Gegeven**|**Toelichting**|
|---|---|
|Zaaktype|De Zaaktype-omschrijving van een zaak van een (ander) ZAAKTYPE dat mogelijkerwijs gepland moet worden bij<br>afronding van een zaak van het voorliggende ZAAKTYPE.|
|Toelichting|Een beschrijving van de situatie waarin sprake kan zijn van het plannen van genoemd zaaktype.|



## **VOORAFGAANDE ZAKEN** 

Er kan sprake zijn van de situatie dat de ene zaak betrekking heeft op een andere zaak: eerder in behandeling genomen en/of afgeronde zaken die aanleiding geven tot het verzoeken om een nieuwe zaak. Bijvoorbeeld een ‘bezwaarzaak’ waaraan een ‘vergunningzaak’ vooraf ging. Voor zover relevant worden deze situaties gespecificeerd waarmee inzicht ontstaat in relaties tussen zaken van bepaald ZAAKTYPEN. 

|**Gegeven**|**Toelichting**|
|---|---|
|Zaaktype|De Zaaktype-omschrijving van een zaak van een (ander) ZAAKTYPE waarop een zaak van het voorliggende<br>ZAAKTYPE betrekking heeft.|
|Toelichting|Een beschrijving van de situatie waarin sprake kan zijn het betrekking hebben op genoemd ZAAKTYPE.|



**==> picture [103 x 52] intentionally omitted <==**

## **ZAKEN die een bijdrage leveren** 

Een kan sprake zijn dat gedurende de behandeling van een zaak een organisatie-onderdeel of een externe organisatie wordt ingezet voor een gedeelte van de zaak waarbij voor dat onderdeel of die organisatie die inzet een zelfstandig bedrijfsproces is. Dat bedrijfsproces wordt derhalve uitgevoerd als zaak van een bepaald zaaktype. In dergelijke gevallen is sprake van gerelateerde zaken waarbij de ene zaak een bijdrage levert aan de andere zaak. Kenmerkend is dat deze zaken verschillende aanleidingen hebben. Voor de in behandeling zijnde zaak is dat de klantvraag, voor de gerelateerde zaak is dat een verzoek vanuit de andere zaak. Let wel, als die inzet voor dat organisatie-onderdeel geen zelfstandig bedrijfsproces is, dan is geen sprake van een gerelateerde zaak noch van een deelzaak maar van uitvoering van een deel van de in behandeling zijnde zaak. 

|**Gegeven**|**Toelichting**|
|---|---|
|Zaaktype|De Zaaktype-omschrijving van een zaak van een ander ZAAKTYPE waarin een bijdrage geleverd wordt aan de<br>behandeling van een zaak van het voorliggende ZAAKTYPE.|
|Toelichting|Een beschrijving van de situatie waarin sprake kan zijn van zaken van genoemd ZAAKTYPE die een bijdrage<br>leveren.|



**==> picture [170 x 86] intentionally omitted <==**

**==> picture [103 x 52] intentionally omitted <==**

**KWALITEITSINSTITUUT NEDERLANDSE GEMEENTEN** 

**NASSAULAAN 12 2514 JS  DEN HAAG** 

**POSTBUS 30435 2500 GK  DEN HAAG** 

**T 070 373 80 08 F 070 363 56 82** 

**INFO@KINGGEMEENTEN.NL WWW.KINGGEMEENTEN.NL** 

