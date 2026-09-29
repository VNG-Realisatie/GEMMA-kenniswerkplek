---
title: "Catalogus Basisregistratie Kadaster"
source: "https://www.kadaster.nl/documents/1953498/2770003/BRK+Catalogus.pdf/ede17779-9298-c280-9997-788dd365a132?t=1628685375984"
source_page: "https://www.kadaster.nl/-/catalogus-brk"
author: "Het Kadaster"
published: 2020-12-10
created: 2026-06-25
description: "Systeembeschrijving van de Basisregistratie Kadaster, met wettelijk kader, authentieke gegevens en vertaling naar het informatiemodel IMKAD."
tags:
  - "brk"
  - "basisregistraties"
---

## **Catalogus Basisregistratie Kadaster** 

## **Datum** 

10 december 2020 

## **Versie** 

1.0 

## **Versiehistorie** 

|Versie|datum|auteur|omschrijving|
|---|---|---|---|
|1.0|10-12-2020|Het Kadaster|Publicatieversie – status definitief|



## **Inhoudsopgave** 

|**1**|**Inleiding ............................................................................................................................................... 3**|
|---|---|
|**2**|**Wat is de Basisregistratie Kadaster .................................................................................................. 3**|
|2.1|Het openbaar register en de Kadastrale registratie .............................................................................. 3|
|2.2|Stelsel Basisregistraties ........................................................................................................................ 4|
|2.3|Bijhouding van de Basisregistratie Kadaster ......................................................................................... 5|
|2.3.1|De brongegevens wijken af van de gegevens uit Basisregistraties ...................................................... 6|
|2.3.2|Onvolledigheid Basisregistratie Kadaster ............................................................................................. 6|
|2.3.3|Van onvolledig negatief naar een semi positief stelsel ......................................................................... 6|
|2.3.4|Verplicht gebruik door bestuursorganen bij de uitvoering van hun publieke taken ............................... 7|
|2.3.5|Verplicht gebruik van andere Basisregistraties in de praktijk ................................................................ 8|
|2.3.6|Dubbele authenticiteit ........................................................................................................................... 8|
|2.4|Authentieke gegevens in de BRK ......................................................................................................... 9|
|2.4.1|Dubbele authenticiteit schematisch uitgelegd ..................................................................................... 10|
|2.5|Gegevens in de BRK en hun authenticiteit ......................................................................................... 11|
|2.5.1|Gegevenstype Onroerende zaak ........................................................................................................ 12|
|2.5.2|Gegevenstype Recht .......................................................................................................................... 13|
|2.5.3|Gegevenstype Tenaamstelling ........................................................................................................... 15|
|2.5.5|Gegevenstype Kadastrale kaart .......................................................................................................... 17|
|2.6|Koppelingen van de BRK met andere basisregistraties ...................................................................... 17|
|**3**|**Gebeurtenissen ................................................................................................................................. 18**|
|3.1|Gebeurtenissen BRK .......................................................................................................................... 19|



**==> picture [110 x 86] intentionally omitted <==**

|3.1.1|Bijwerking op grond van een ingeschreven stuk ................................................................................. 19|
|---|---|
|3.1.2|Bijwerking op grond van een kadasterstuk ......................................................................................... 20|
|3.1.3|Bijwerking op grond van een relaas van bevindingen ......................................................................... 20|
|3.1.4|Terugmelding ...................................................................................................................................... 20|
|3.1.5|Beschikking ......................................................................................................................................... 21|
|3.1.6|Bezwaar en beroep ............................................................................................................................. 21|
|3.2|Gebeurtenissen WKPB ....................................................................................................................... 22|
|3.2.1|Inschrijving oorsponkelijk besluit Wkpb............................................................................................... 22|
|3.2.2|Inschrijving wijzigingsbesluit Wkpb ..................................................................................................... 22|
|3.2.3|Inschrijving beëindigingsbesluit en de vervallenverklaring Wkpb ........................................................ 23|
|3.2.4|Inschrijving van een herroepingsbesluit Wkpb .................................................................................... 23|
|3.2.5|Werkingsgebied Publiekrechtelijke Beperkingen WKPB ..................................................................... 24|
|3.2.6|Bezwaar en beroep ............................................................................................................................. 24|
|**4**|**Vertaling naar informatiemodel ....................................................................................................... 25**|
|4.1|Overzicht ............................................................................................................................................. 26|
|4.1.1|Domeinen ........................................................................................................................................... 27|
|4.2|Domein Kadastraal Object .................................................................................................................. 27|
|4.3|Domein Onroerende zaak ................................................................................................................... 28|
|4.4|Domein Zakelijk recht ......................................................................................................................... 29|
|4.5|Domein Persoon ................................................................................................................................. 30|
|4.6|Domein Stuk ....................................................................................................................................... 31|
|4.7|Domein Publiekrechtelijke beperking .................................................................................................. 32|
|4.8|Leeswijzer MIM modellen ................................................................................................................... 33|



**==> picture [69 x 16] intentionally omitted <==**

## **1 Inleiding** 

Deze catalogus voor de basisregistratie Kadaster is een catalogus in de zin van Artikel 48, lid 5 Kadasterwet en beschrijft de gegevens die in de basisregistratie Kadaster zijn opgenomen van: in de openbare registers ingeschreven stukken, perceelsgrenzen zoals aangewezen en gemeten in het veld, publiekrechtelijke beperkingen. De catalogus beschrijft het wettelijkkader van de gegevens in de registratie, samen met de gedetailleerde uitwerking van de gegevens in de basisregistratie Kadaster zoals beschreven in het informatiemodel Kadaster (IMKAD). Binnen het Kadaster is er onderscheid te maken tussen de openbare registers en de Kadastrale registratie. De openbare registers zijn een documentenregistratie waarin de ingeschreven stukken worden opgenomen. Dit zijn over het algemeen stukken die betrekking hebben op het overdragen en vestigen van zakelijke rechten op onroerende zaken en besluiten in het kader van de WKPB. Met de informatie die in deze ingeschreven stukken staat wordt de registratie bijgewerkt naar de nieuwe juiste stand. In deze registratie wordt vastgelegd wie, welke rechten heeft op een Kadastraal object. Het feit dat de Kadastrale registratie onderdeel is van het stelsel van basisregistraties als Basisregistratie Kadaster (BRK) betekent dat de registratie zowel privaatrechtelijk als publiekrechtelijk een rol vervult. Publiekrechtelijk is het de bron van verschillende authentieke gegevens. In hoofdstuk 2 wordt beschreven wat dit inhoudt voor de Kadastrale registratie. Daarnaast wordt ingegaan op de gegevens die binnen de BRK als authentiek zijn aangemerkt en hoe deze zich verhouden tot authentieke gegevens in andere registraties. In hoofdstuk 3 wordt beschreven welke gebeurtenissen zorgen voor de bijwerking van de BRK en van de BRKPB, de registratie voor publiekrechtelijke beperkingen. Hoofdstuk 4 beschrijft uit welke bouwblokken en onderdelen de BRK bestaat. Omdat de details daarvan uitputtend beschreven worden in het Informatiemodel Kadaster (IMKAD) wordt ook op hoofdlijnen beschreven hoe dat informatiemodel gelezen moet worden. 

## **2 Wat is de Basisregistratie Kadaster** 

Een basisregistratie is een door de overheid officieel aangewezen registratie met daarin gegevens van hoogwaardige kwaliteit, die door alle overheidsinstellingen verplicht en zonder nader onderzoek, worden gebruikt bij de uitvoering van publiekrechtelijke taken. 

De Basisregistratie Kadaster (BRK) bevat de registratie van onroerende zaken en zakelijke rechten en de kadastrale kaart. De BRK bevat informatie over percelen, eigendom, hypotheken, beperkte rechten (zoals opstal en vruchtgebruik) en leidingnetwerken. Op de kadastrale kaart zijn percelen, perceelnummer, oppervlakte, grenzen van het rijk, provincies en gemeenten te vinden. De BRK wordt bijgehouden door het Kadaster. 

## **2.1 Het openbaar register en de Kadastrale registratie** 

De informatie in de BRK is afkomstig uit- en wordt bijgewerkt op basis van, aan het Kadaster ter inschrijving aangeboden stukken. Deze ter inschrijving aangeboden stukken zijn de brondocumenten voor de registratie van informatie over eigendom, hypotheken, beperkte rechten, leidingnetwerken en publiekrechtelijke beperkingen. Deze stukken zijn te raadplegen in een openbaar register. Dit zijn over het algemeen stukken die betrekking hebben op het overdragen en vestigen van zakelijke rechten op onroerende zaken. De brondocumenten voor de informatie over de grenzen van percelen en hun ligging zijn de relazen van bevinding die worden opgesteld door de landmeters van het Kadaster. Dit zijn interne documenten die de grondslag vormen voor het opstellen van de Kadastrale Kaart. 

**==> picture [69 x 16] intentionally omitted <==**

Hoe de informatie in de BRK gerelateerd is aan de stukken uit het openbaar register is te zien in het informatiemodel in het domein Stuk (zie paragraaf 4.6). De registratie wordt in de kern beschreven in het domein Recht (zie paragraaf 4.4) met als basis de domeinen Kadastraal Object, Onroerende Zaak (paragraaf 4.3) en Persoon (paragraaf 4.5). 

Het raadplegen van de openbare registers verloopt via informatieproducten die gebaseerd zijn op de BRK. In deze producten is een referentie opgenomen naar de relevante stukken, die dan afzonderlijk kunnen worden opgevraagd en ingezien. 

## **2.2 Stelsel Basisregistraties** 

De Basisregistratie Kadaster (BRK) is onderdeel is van het stelsel van Basisregistraties, waarover u meer kunt lezen op de website van digitaleoverheid.nl. Daarom maakt de BRK ook gebruik van gegevens uit andere 

registraties. Over deze andere registraties kunt u in de via de volgende links meer informatie vinden: 

- Via de website van Rijksoverheid.nl over basisregistratie Personen (BRP): persoonsgegevens van Nederlanders in binnen- en buitenland; 

- Via de website van de Kamer van Koophandel in het handelsregister (HR): gegevens van alle bedrijven en rechtspersonen in Nederland; 

- Op de pagina BAG (Basisregistraties Adressen en Gebouwen): alle adressen en gebouwen in Nederland. 

In de onderstaande plaat (figuur 1) is te zien hoe de verschillende basisregistraties met elkaar samenhangen en welke authentieke en basisgegevens zij toevoegen aan het stelsel. 

**==> picture [356 x 321] intentionally omitted <==**

_Figuur 1: Overzicht stelsel basisregistraties_ _**(bron** : www.digitaleoverheid.nl_ _**)**_ 

**==> picture [69 x 16] intentionally omitted <==**

De stelselplaat gegevens hieronder (figuur 2) geeft een overzicht van veel voorkomende begrippen in de basisregistraties en de verbindingen daartussen. Zo is te zien dat het stelsel gegevens bevat van een persoon, voertuig of pand. Maar ook hoe gegevens met elkaar samenhangen, zoals dat een vestiging van een bedrijf gevestigd is op een adres en in een verblijfsobject. 

**==> picture [385 x 221] intentionally omitted <==**

_Figuur 2 Stelselplaat gegevens_ 

## **2.3 Bijhouding van de Basisregistratie Kadaster** 

De basisregistratie wordt bijgehouden aan de hand van de wijzigingen van de privaatrechtelijke rechtstoestand. De bronnen voor deze wijzigingen zijn stukken, veelal notariële akten, die worden ingeschreven in de Openbare Registers. Deze zijn leidend, ook voor het gebruik in het kader van de uitvoering van publieke taken. Het kan echter voorkomen dat de informatie in de Openbare Registers afwijkt van informatie in de basisregistraties aanwezig is. Deze afwijkingen kunnen de volgende oorzaken hebben. 

- Het gegeven dat in een basisregistratie geregistreerd is, is niet meer actueel; 

- De basisregistratie heeft een fout gemaakt bij het overnemen van een gegeven uit het brondocument; 

- De notaris heeft de (authentieke) gegevens die in de akte zijn opgenomen niet uit de desbetreffende basisregistratie(s) overgenomen; 

- De gegevens worden niet op een uniforme manier in alle basisregistraties weergegeven. 

Indien er sprake is van afwijkingen dienen die te worden terug gemeld zodat de verschillen kunnen worden opgelost. De behandeling van terugmeldingen door overheden mag echter niet leiden tot strijd met de privaatrechtelijke situatie. In plaats daarvan moet worden uitgezocht waar de oorzaak van het verschil ligt. In de volgende paragrafen zullen de verschillende situaties nader worden beschreven als gevolg waarvan de feitelijke werkelijkheid kan afwijken van de Basisregistratie Kadaster. 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [438 x 218] intentionally omitted <==**

_Figuur 3: Openbare registers en de Basisregistratie Kadaster_ 

- 2.3.1 De brongegevens wijken af van de gegevens uit Basisregistraties 

   - Als de gegevens uit het brondocument afwijken van de authentieke gegevens uit een andere basisregistratie, worden de gegevens uit het brondocument aangehouden. Wanneer er verschillen blijken te zijn worden de afwijkende gegevens uit andere basisregistraties worden niet automatisch overgenomen. De reden daarvoor is te vinden in de wijziging van de Kadasterwet, de Organisatiewet Kadaster en enige andere wetten die verband houden met de aanwijzing van de kadastrale registratie, en de kadastrale kaart tot Basisregistratie Kadaster. Het zijn van basisregistratie heeft alleen betekenis voor publiekrechtelijk gebruik. De privaatrechtelijke rechtszekerheidsfunctie van de registratie verandert niet. 

- 2.3.2 Onvolledigheid Basisregistratie Kadaster 

Dat de BRK is aangewezen als basisregistratie doet niets af aan het feit dat er buiten de registers om rechten kunnen wijzigen door verjaring, erfopvolging, boedelmenging, of andere redenen. Bijvoorbeeld in het geval van erfopvolging wordt in de Basisregistratie Kadaster volstaan met de aan de Basisregistratie Personen (BRP) ontleende toevoeging “overleden” zonder vermelding van erfgenamen. Ten aanzien van perceelgrenzen speelt iets vergelijkbaars. Als er een verschil is tussen de fysieke en kadastrale grenzen moeten mensen zelf dat verschil achterhalen en hun eigen conclusie over mogelijke verjaring trekken. 

Dit soort situaties zijn een gevolg van het feit dat het Nederlands stelsel van vastgoedregistratie een “onvolledig negatief stelsel” is. Omdat onbekende verkrijgingen niet bij de uitgangspunten van een basisregistratie passen, wordt gezocht naar methoden om inschrijving van dergelijke wijzigingen in de Openbare Registers te bevorderen, zodat de Basisregistratie Kadaster op deze punten meer aansluit op de juridische werkelijkheid. Een voorbeeld hiervan is het bevorderen van het bij het Kadaster kosteloos inschrijven van verklaringen van erfrecht. 

- 2.3.3 Van onvolledig negatief naar een semi positief stelsel 

In de juridische literatuur wordt het Nederlandse stelsel semi-positief genoemd. Dit heeft te maken met een aantal maatregelen in ons stelsel, die ervoor zorgen dat het allemaal een stuk positiever uitpakt dan het in eerste instantie lijkt. 

**==> picture [69 x 16] intentionally omitted <==**

Op de eerste plaats zijn daarbij de derdenbeschermingsbepalingen van Boek 3 BW van belang. In Artikel 88 Burgerlijk Wetboek Boek 3 is voor registergoederen een bepaling opgenomen dat ondanks onbevoegdheid van de vervreemder een overdracht toch als geldig kan worden aangemerkt indien de derde-verkrijger te goeder trouw is (dus is afgegaan op de openbare registers van het kadaster) en de ongeldigheid niet voortvloeit uit beschikkingsonbevoegdheid van de vervreemder bij een vroegere overdracht. In het voorbeeld dat de koop wordt vernietigd op grond van bedrog, betekent dit dat ondanks de werking van het causale stelsel een derde verkrijger toch eigenaar wordt, mits te goeder trouw. 

Daarnaast kennen de Artikelen 24 - 26 Burgerlijk Wetboek Boek 3 beschermingsbepalingen in situaties dat derden uitgaan van de informatie die in de openbare registers is opgenomen. In dit kader is het onderscheid tussen openbare registers en BRK van belang. 

De openbare registers bevatten de brondocumenten: notariële akten, maar ook beslagen, rechterlijke uitspraken, besluiten van overheden en andere van belang zijnde documenten. In de derdenbeschermingsbepalingen van het BW wordt naar deze openbare registers verwezen. De BRK fungeert als toegangspoort voor deze openbare registers doordat de delen en nummers van de brondocumenten worden ontsloten. Verder bevat de BRK per kadastraal object de essentialia uit de brondocumenten. Bovendien is het een basisregistratie: ten aanzien van de authentieke gegevens uit deze registratie (zoals rechthebbenden, rechten, percelen) zijn andere overheden verplicht zich op deze gegevens te baseren zonder nader onderzoek. 

Vanuit een publiekrechtelijk perspectief zou men dus kunnen spreken over een positief stelsel: er is voor overheden geen noodzaak om de brondocumenten te raadplegen; men mag (of beter nog: dient) op de inhoud van de BRK af te gaan. Maar in het privaatrechtelijke domein heeft de BRK niet dezelfde juridische waarde als de openbare registers. 

Een tweede reden dat het Nederlandse stelsel semi-positief wordt genoemd is de verplichte notariële tussenkomst. De notaris zal steeds onderzoek doen in de openbare registers naar de feiten die van belang zijn voor het registergoed dat object is van een rechtshandeling. Ook doet hij uitgebreid onderzoek naar de beschikkingsbevoegdheid van vervreemders. Doordat zijn notariële akte vervolgens verplicht wordt ingeschreven in de openbare registers van het kadaster, wint ons stelsel aan betrouwbaarheid. 

Ten slotte wordt als derde reden opgevoerd dat de bewaarder in 1992 bij de inwerkingtreding van Boek 3 BW een waarschuwingsbevoegdheid heeft gekregen. Hij kan hiervan gebruik maken wanneer hij het sterke vermoeden heeft dat een ingeschreven feit niet tot stand kan komen (Artikel 19 Burgerlijk Wetboek Boek 3, lid 4). Dit is geen bevoegdheid tot weigering van de inschrijving, maar wel de mogelijkheid te waarschuwen. Van deze waarschuwingsbevoegdheid wordt gebruik gemaakt in bepaalde gevallen.1 

## 2.3.4 Verplicht gebruik door bestuursorganen bij de uitvoering van hun publieke taken 

Een van de belangrijkste kenmerken van een basisregistratie is de wettelijke plicht voor bestuursorganen om authentieke gegevens te gebruiken. (indien vaststaat dat de gegevensverzameling voldoende betrouwbaar is). Dit betekent dat Bestuursorganen de plicht hebben om bij hun besluitvorming de betreffende basisregistratie te raadplegen wat betreft de weergave van die authentieke gegevens. Zij dienen daarbij zelf alert te zijn op de aantekening «in onderzoek» bij een gegeven. Die aantekening duidt er op dat de beheerder na beëindiging van het onderzoek een beslissing neemt omtrent het gemelde gegeven, waarbij dat gegeven wordt aangepast of 

- 1 Bron: Onduidelijkheden rondom Inschrijving en Registratie (Ruben Roes en Jacques Vos) 

- WPNR 7180 

**==> picture [69 x 16] intentionally omitted <==**

ongewijzigd blijft. Bestuursorganen zijn in het stelsel van basisregistraties overigens niet verplicht om andere dan authentieke gegevens uit basisregistraties te gebruiken.” 

In Artikel 7l Kadasterwet is de consequentie beschreven van een van de grondbeginselen van het principe van een basisregistratie (eenmaal inwinnen en meervoudig gebruik van authentieke gegevens): de burger behoeft reeds in een basisregistratie opgeslagen gegevens niet nogmaals te verstrekken, behoudens in de in dit artikel genoemde uitzonderingsgevallen. 

## 2.3.5 Verplicht gebruik van andere Basisregistraties in de praktijk 

Het Kadaster is een bestuursorgaan en is daarom ook wettelijk verplicht de authentieke gegevens uit een andere basisregistratie over te nemen. Tegelijkertijd is het Kadaster ook wettelijk verplicht de gegevens uit de akte over te nemen. Door deze dubbele verplichting kunnen knelpunten ontstaan. 

Aangezien artikel 18 Kadasterwet (vermelding van persoonsgegevens) nog niet aan het stel van basisregistraties is aangepast kan de inschrijving van een notariële akte niet worden geweigerd wanneer de gegevens in de akte afwijken van de persoonsgegevens in een andere basisregistratie. In de meeste gevallen wordt de notaris wel verzocht te onderzoeken of hij de notariële akte kan verbeteren. 

Ook notarissen zijn bestuursorganen. Daarom moeten zij ook de basisregistraties raadplegen en de authentieke gegevens in hun akten op te nemen. Hierdoor kan de kans op ‘knelpunten’ aanzienlijk worden verminderd. In de praktijk blijkt echter dat dit nog niet altijd standaard gebeurt waardoor verschillen tussen de gegevens uit het brondocument en een andere basisregistratie kunnen ontstaan. Een dergelijk verschil heeft tot gevolg dat een koppeling tussen twee basisregistraties niet tot stand kan worden gebracht. 

In het voorbeeld van de persoonsgegevens komt er geen koppeling tot stand tussen de Basisregistratie Kadaster en de Basisregistratie Personen. Eventuele mutaties in de Basisregistratie Personen worden daardoor niet automatisch overgenomen in de Basisregistratie Kadaster. 

In artikel 7n Kadasterwet staat “Een bestuursorgaan meldt aan de Dienst, onder opgaaf van redenen, zijn gerede twijfel omtrent de juistheid van een in de basisregistratie kadaster opgenomen gegeven, dat krachtens deze wet als authentiek is aangemerkt _._ ” Het Kadaster neemt na ontvangst van een terugmelding een beslissing over een wijziging van het betreffende authentieke gegeven. Indien het Kadaster die beslissing niet binnen een dag na ontvangst van die melding heeft genomen, wordt in de basisregistratie kadaster, aangegeven dat het betreffende gegeven «in onderzoek» is. Het Kadaster stuurt een schriftelijke mededeling aan de belanghebbende indien de beslissing heeft geleid tot een wijziging van het betreffende authentieke gegeven. 

- 2.3.6 Dubbele authenticiteit 

Het stelsel van basisregistraties kan niet begrepen worden door alleen de wet te lezen en te analyseren.  Een puur juridische analyse zal snel tot de conclusie leiden dat verschillende wettelijke bepalingen tegenstrijdig zijn. Zo wordt bijvoorbeeld volgens de wet, de naam van een persoon zowel door de BRK alsook door de GBA als authentiek aangemerkt. Op het eerste gezicht valt dit niet te rijmen met één van de meest belangrijke uitgangspunten van het stelsel dat van één gegeven maar één authentieke versie mag bestaan. De dubbele authenticiteit kan echter soms wel een belangrijke functie hebben. Zo kan het bijvoorbeeld voorkomen dat een persoon (bijvoorbeeld een buitenlander) wel in de BRK staat maar niet in de BRP (Registratie van Niet Ingezetenen; RNI) geregistreerd is. Indien de persoonsgegevens alléén in de BRP authentiek waren, dan zou de authenticiteit voor de persoonsgegevens van een persoon die wel in de BRK maar niet in de BRP staan, in het geheel ontbreken. 

In de volgende paragraaf zal verder op de authentieke gegevens binnen de BRK worden ingegaan, waarbij ook wordt aangegeven welke gegevens ook authentiek in een andere basisregistratie zijn. 

**==> picture [69 x 16] intentionally omitted <==**

## **2.4 Authentieke gegevens in de BRK** 

In de wet van een basisregistratie ligt vast welke gegevens van de basisregistratie authentiek zijn. Ook kan een gegeven authentiek zijn doordat het via een algemene maatregel van bestuur (AMvB) als zodanig wordt aangemerkt. De authentieke gegevens in de basisregistraties zijn van hoogwaardige kwaliteit zodat deze zonder nader onderzoek bij de uitvoering van publiekrechtelijke taken te gebruiken zijn. 

Volgens artikel 7h Kadasterwet wordt een “authentiek gegeven” (afkomstig uit de BRK) in de BRK door middel van een kenmerk onderscheiden van de authentieke gegevens die uit een andere basisregistratie afkomstig zijn en van de niet-authentieke gegevens. In het informatiemodel is dit aangegeven met het metadata-element “Indicatie authentiek”. Daarnaast in dit document aangegeven welke gegevens authentiek zijn. 

In het onderstaande schema is aangegeven hoe in de Kadasterwet is beschreven welke gegevens in de BRK authentiek zijn. 

**==> picture [432 x 215] intentionally omitted <==**

## _Figuur 4: Authentieke gegevens in de Kadasterwet_ 

Ter referentie hieronder de artikelen die in bovenstaand diagram genoemd zijn. 

## **Artikel 48 Kadasterwet** 

**lid 2** De basisregistratie kadaster bevat: 

- a. de kadastrale aanduiding van onroerende zaken en van appartementsrechten; 

- b. naam, voornamen, adres, geboortedatum en burgerlijke staat van de eigenaar van, beperkt gerechtigde met betrekking tot, of beslaglegger op, een onroerende zaak of, ingeval die eigenaar, gerechtigde of beslaglegger een rechtspersoon is, de rechtsvorm; 

- c. de wettelijke benaming van de beperkte rechten waaraan een onroerende zaak is onderworpen, en van de beslagen die op die zaak of dat beperkte recht zijn gelegd, als ook, of die zaak of dat beperkte recht onder bewind staat of ten aanzien daarvan een beding als bedoeld in artikel 252 van Boek 6 van het Burgerlijk Wetboek is ingeschreven; 

- d. de kadastrale grootte van een perceel; 

**lid 3** De basisregistratie kadaster bevat voorts de landelijke kadastrale kaart. Die kaart is toegankelijk door middel 

van een coördinaat in het net van coördinaatpunten, bedoeld in artikel 52, of door middel van de kadastrale aanduiding van een perceel. De landelijke kadastrale kaart bevat: 

- a. de afbeelding van de kadastrale grenzen van een perceel, weergegeven in het net van coördinaatpunten, bedoeld in artikel 52; 

- b. de kadastrale aanduiding van een perceel; 

**==> picture [69 x 16] intentionally omitted <==**

- c. de rijksgrens en de grens van een provincie of gemeente; 

## **Artikel 7g Kadasterwet** 

**lid 3** Indien een authentiek gegeven of deel daarvan als bedoeld in artikel 7f, tweede of derde lid, of een gegeven als bedoeld in artikel 48, 85, 92 of 98a, krachtens een wet tot instelling van een andere basisregistratie dan de basisregistratie kadaster of topografie als authentiek wordt aangemerkt, geldt dat gegeven daarna als een uit die andere basisregistratie overgenomen authentiek gegeven. 

- 2.4.1 Dubbele authenticiteit schematisch uitgelegd 

In de praktijk blijken de verschillende wetten van de basisregistraties niet naadloos op elkaar aan te sluiten. Dit heeft tot gevolg dat een bepaald gegeven in meerdere basisregistraties authentiek kan zijn. In het onderstaande schema wordt dat uitgelegd. 

**==> picture [345 x 420] intentionally omitted <==**

**----- Start of picture text -----**<br>
Het fenomeen “dubbele authenticiteit”<br>theorie  praktijk<br>Van één bepaald gegeven bestaat  Diverse gegevens worden door meer dan één<br>slechts één authentieke versie.  basisregistratie als authentiek aangemerkt.<br>oorzaak<br>Elke basisregistratie heeft vanwege zijn<br>achtergrond en doelbinding zijn eigen<br>definitie. De gegevens kennen dus een sterk<br>situationeel aspect.<br>Voorbeeld:<br>- GBA:  woon adres<br>-<br>BAG: objectadres<br>Sommige gegevens zijn<br>echter wel vrij uniek zoals<br>de naam en de<br>geboortedatum.<br>Het kan lastig worden te duiden waar een<br>gegeven zijn authentieke karakter aan<br>ontleent.<br>consequentie<br>**----- End of picture text -----**<br>


_Figuur 5: Dubbele authenticiteit_ 

 BRK-PB 

**==> picture [69 x 16] intentionally omitted <==**

De publiekrechtelijke beperkingen in de BRK zijn geen authentieke gegevens. De BRK-PB registratie is wel sinds 01-04-2020 de centrale landelijke registratie voor publiekrechtelijke beperkingen volgens de WKPBOZ en als zodanig onderdeel van de BRK. 

## **2.5 Gegevens in de BRK en hun authenticiteit** 

Zoals hiervoor aangegeven zijn de gegevens in de BRK onder te verdelen in authentieke gegevens (in eigen of in een andere registratie of beiden) en niet authentieke gegevens. Sommige van de niet authentieke gegevens zijn echter alleen in de BRK geregistreerd. Deze gegevens worden ook wel basisgegevens genoemd. 

Hierna wordt aangegeven welke gegevens in de BRK op welke manier authentiek zijn. Daarnaast wordt 

doormiddel van een tabel aangegeven waar deze authentieke gegevens in het Informatie Model Kadaster (IMKAD) te vinden zijn. 

|(IMKAD)te vinden|zijn.|
|---|---|
|**Kleur**|**Verklaring**|
|**Groen**|Authentiek gegeven volgens BRK|
|**Geel**|Uit een andere basisregistratie overgenomen authentiek gegeven|
|**Oranje**|Een door zowel de BRK alsook door een andere basisregistratie als authentiek<br>aangemerkt authentiek gegeven|
|**Lichtblauw**|Niet-authentiekgegeven|



**==> picture [69 x 16] intentionally omitted <==**

## 2.5.1 Gegevenstype Onroerende zaak 

**==> picture [482 x 395] intentionally omitted <==**

_Figuur 6: Authenticiteit bij onroerende zaken_ 

In IMKAD zijn deze gegevens als volgt terug te vinden: 

|<br>Authentiek gegeven|<br>Objecttype|Attribuutsoort (data element)|
|---|---|---|
|Kadastrale gemeente|OnroerendeZaak|kadastraleAanduiding (kadastraleGemeente)|
|Sectie|OnroerendeZaak|kadastraleAanduiding (sectie)|
|Perceelnummer|OnroerendeZaak|kadastraleAanduiding (perceelnummer)|
|Kadastrale grootte|Perceel|kadastraleGrootte|
|Coördinaten|Perceel|plaatsCoordinaten|
|Cultuuraanduiding|OnroerendeZaak|aardCultuurBebouwd<br>aardCultuurOnbebouwd|
|Koopsom|OnroerendeZaak|koopsom|
|Indexnummer|OnroerendeZaak|kadastraleAanduiding<br>(appartementsrechtVolgnummer)|
|netwerknummer||-|



**==> picture [69 x 16] intentionally omitted <==**

2.5.2 Gegevenstype Recht 

**==> picture [421 x 519] intentionally omitted <==**

_Figuur 7: Authenticiteit bij rechten en verplichtingen_ 

**==> picture [69 x 16] intentionally omitted <==**

## In IMKAD zijn deze gegevens als volgt terug te vinden: 

|**Authentiek gegeven**|**Objecttype**<br>**Attribuutsoort (data element)**|**Objecttype**<br>**Attribuutsoort (data element)**|
|---|---|---|
|Eigendom|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Opstal|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Erfpacht|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Vruchtgebruik|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Gebruik en bewoning|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Appartementsrechtsplitsing|Appartementsrechtsplitsing||
|Zakelijkrecht als bedoeld…|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Oud-vaderlandse rechten|ZakelijkRecht|Aard (waardelijstAardZakelijkRecht)|
|Hypotheekrecht|ZekerheidsstellingHypothecair||
|Hoofdsom hypotheek|stukdeel|bedragZekerheidsstellingHypotheek|
|Rentevoethypotheek||Zie akte|
|Koopovereenkomst waarvan<br>de inschrijving resulteert in<br>koperbescherming volgens<br>artikel 7:3 BW|Aantekening|aard (waardelijstAardAantekening)|
|Koopovereenkomst of<br>voorovereenkomst tot koop<br>waarvan de inschrijving<br>resulteert in<br>koperbescherming volgens<br>artikel 10 Wvg|Aantekening|aard (waardelijstAardAantekening)|
|Vervallen van de<br>koopovereenkomst of<br>voorovereenkomst tot koop<br>die zijn ingeschreven op<br>grond van artikel 7:3 BW of<br>10 Wvg|Aantekening|aard (waardelijstAardAantekening)|
|Aandeel in een gemeenschap|GezamenlijkAandeel|aandeel (telller / noemer)|
|Erfpachtcanon|Erfpachtcanon||
|Mogelijkheid tot eenzijdige<br>opzegging hypotheekrecht|||
|Rangwisseling<br>hypotheekrecht|Aantekening|aard (waardelijstAardAantekening)|
|Naam van rechtsfeiten die<br>resulteren in een wijziging<br>van de hypotheeknemer|Stukdeel|aard (waardelijstAardStukdeel)|
|Aantekening met een<br>beschrijving van de inhoud<br>van een recht|Aantekening|aard (waardelijstAardAantekening)|
|Mandeligheid|Mandeligheid||
|Einddatumrecht|Aantekening|einddatumRecht|
|Voorwaardelijke verkrijging|Aantekening|aard (waardelijstAardAantekening)|
|Erfdienstbaarheid|Aantekening|aard (waardelijst AardAantekening)|



**==> picture [69 x 16] intentionally omitted <==**

|Beslag|ZekerheidstellingInzakeBeslag||
|---|---|---|
|Kwalitatieve verplichting|Aantekening|aard (waardelijstAardAantekening)|
|Publiekrechtelijke<br>beperkingen|Aantekening|aard (waardelijstAardAantekening)|
|onderbewindstelling van een<br>grondstuk|Aantekening|aard (waardelijstAardAantekening)|



## 2.5.3 Gegevenstype Tenaamstelling 

**==> picture [476 x 268] intentionally omitted <==**

_Figuur 8: Authenticiteit bij tenaamstelling_ 

**==> picture [69 x 16] intentionally omitted <==**

## In IMKAD zijn deze gegevens als volgt terug te vinden: 

|In IMKAD zijn deze gegevens als|volgt terug te vinden:||
|---|---|---|
|**Authentiek gegeven**|**Objecttype**|**Attribuutsoort (data element)**|
|Natuurlijk persoon naam|GeregistreerdPersoon|naam (geslachtsnaam)<br>naam (vooorvoegselGeslachtsnaam)|
|Natuurlijk persoon voornaam|GeregistreerdPersoon|naam (Voornamen)|
|Natuurlijk persoon adres|Persoon|woonlocatie|
|Natuurlijk persoon<br>geboortedatum|GeregistreerdPersoon|geboorte (geboortedatum)|
|Natuurlijk persoon burgerlijke<br>staat|GeregistreerdPersoon|partnerschap|
|Natuurlijk persoon geslacht|GeregistreerdPersoon|geslachtsaanduiding|
|Natuurlijk persoon<br>geboorteplaats|GeregistreerdPersoon|geboorte (geboorteplaats)|
|Natuurlijk persoon<br>geboorteland|GeregistreerdPersoon|geboorte (geboorteland)|
|beschikkingsbevoegdheid|Aantekening|aard (waardelijstAardAantekening)|
|Rechtspersoon naam|Rechtspersoon|statutaireNaam|
|Rechtspersoon adres|Rechtspersoon|woonlocatie|
|Rechtspersoon zetel|Rechtspersoon|statutaireZetel|
|Rechtspersoon rechtsvorm|Rechtspersoon|rechtsvorm|
|Naam vereniging van<br>eigenaars|Rechtspersoon|statutaireNaam|
|Adres vereniging van<br>eigenaars|Persoon|woonlocatie|



- 2.5.4 Gegevenstype verwijzing naar brondocumenten 

**==> picture [486 x 113] intentionally omitted <==**

_Figuur 9: Authenticiteit bij verwijzing naar brondocumenten_ 

In IMKAD zijn deze gegevens als volgt terug te vinden: 

|**Authentiek gegeven**|**Objecttype**|**Attribuutsoort (data element)**|
|---|---|---|
|Stuk identificatienummer|TerInschrijvinAangebodenStuk|deelEnNummer|
|Tijdstip inschrijven stuk|TerInschrijvinAangebodenStuk|tijdstipAanbieding|
|Dagtekening van de<br>bijwerking||Wordt vermeld bij bevraging van Kol of<br>Kik inzage|
|Volgnummer van niet<br>ingeschreven stukken||Dit is het deel en nummer van het stuk<br>dat is ingeschreven in het register van<br>voorlopige aantekening (ook wel 4D).|



**==> picture [69 x 16] intentionally omitted <==**

- 2.5.5 Gegevenstype Kadastrale kaart 

**==> picture [439 x 84] intentionally omitted <==**

_Figuur 10: Authenticiteit bij de kadastrale kaart_ 

Deze gegevens worden overgenomen uit de BRK-Geo. Deze gegevenselementen zitten slechts gedeeltelijk ook in IMKAD en zijn als volgt terug te vinden: 

|in IMKAD en zijn als volgt terug|te vinden:||
|---|---|---|
|**Authentiek gegeven**|**Objecttype**|**Attribuutsoort (data element)**|
|Kadastrale grenzen|Kadastralegrens|Grenslijn|
|Kadastrale gemeente|Onroerendezaak|Kadastraleaanduiding<br>(kadastralegemeente)|
|Sectie|OnroerendeZaak|kadastraleAanduiding (sectie)|
|Peceelnummer|OnroerendeZaak|kadastraleAanduiding (perceelnummer)|
|Voorstelling van de omtrek<br>hoofd-of bijgebouw||-|



Over het product Kadastrale kaart kunt u meer lezen op de volgende website: https://www.pdok.nl/introductie//article/basisregistratie-kadaster-brk- 

## **2.6 Koppelingen van de BRK met andere basisregistraties** 

De BRK heeft koppelingen met de Basisregistratie Adressen en Gebouwen, het Handelsregister en de 

Basisregistratie Personen. Bij deze koppelingen doen zich twee situaties voor: 

1. een authentiek gegeven in de BRK is gelijk aan een authentiek gegeven in een andere basisregistratie, of 

2. een niet-authentiek gegeven in de BRK is wel authentiek in een andere basisregistratie. 

In de onderstaande tabellen wordt aangegeven voor welke gegevens dit het geval is. 

|of<br>2.<br>een niet-authentiek gegeven in de BRK is wel authentiek in een andere basisregistratie.<br>In de onderstaande tabellen wordt aangegeven voor welke gegevens dit het geval is.|of<br>2.<br>een niet-authentiek gegeven in de BRK is wel authentiek in een andere basisregistratie.<br>In de onderstaande tabellen wordt aangegeven voor welke gegevens dit het geval is.|of<br>2.<br>een niet-authentiek gegeven in de BRK is wel authentiek in een andere basisregistratie.<br>In de onderstaande tabellen wordt aangegeven voor welke gegevens dit het geval is.|
|---|---|---|
|Situatie 1: Authentieke BRK gegevens zijn ook Authentiek in een andere basisregistratie|||
|**BRK-BRP**|**BRK-HR**|**BRK-BAG**|
|-<br>naam|-<br>naam|-<br>adres|
|-<br>voornaam|-<br>zetel||
|-<br>adres|-<br>rechtsvorm||
|-<br>geboortedatum|||
|-<br>burgerlijke staat|||



|Situatie 2: Niet authentieke BRK gegevens zijn_wel_Authentiek in een_andere_basisregistratie|Situatie 2: Niet authentieke BRK gegevens zijn_wel_Authentiek in een_andere_basisregistratie|Situatie 2: Niet authentieke BRK gegevens zijn_wel_Authentiek in een_andere_basisregistratie|
|---|---|---|
|**BRK-BRP**|**BRK-HR**|**BRK-BAG**|
|-<br>geslacht|-<br>naam vereniging van<br>Eigenaars|-<br>voorstelling van de<br>omtrek hoofd- of<br>bijgebouw|
|-<br>geboorteplaats|-<br>adres Vereniging van<br>Eigenaars||
|-<br>geboorteland|||



**==> picture [69 x 16] intentionally omitted <==**

## **3 Gebeurtenissen** 

Het opnemen en wijzigen van gegevens in de BRK wordt bijwerking genoemd. Bijwerking vindt plaats door middel van bijhouding of vernieuwing. Bijwerking kan alleen op basis van ingeschreven stukken, kadasterstukken en relazen van bevindingen. Indien het kadaster gegevens uit deze stukken niet juist heeft overgenomen, kunnen bestuursorganen en belanghebbenden een terugmelding doen. Ook dat kan tot bijwerking leiden. Een beslissing tot bijwerking is een beschikking waartegen bezwaar of beroep kan  instellen. De BRK onderscheid hierbij de volgende gebeurtenissen: 

- bijwerking op grond van een ingeschreven stuk 

- bijwerking op grond van een kadasterstuk 

- bijwerking op grond van een relaas van bevindingen 

- terugmelding 

- beschikking 

- bezwaar en beroep 

In de paragraaf 3.1 worden deze gebeurtenissen nader beschreven. 

De bijwerking van de BRK met betrekking tot publiekrechtelijke beperkingen verloopt anders de inschrijving van notariële akten. Dit heeft de volgende achtergrond.[2] 

## **Wet kenbaarheid publiekrechtelijke beperkingen (Wkpb) en Kadasterwet** 

De oorspronkelijke Wet kenbaarheid publiekrechtelijke beperkingen (Wkpb) van 2007 is per 1 april 2020 gewijzigd. Gemeenten gaan, net als andere bestuursorganen, hun publiekrechtelijke beperkingen inschrijven in de BRK, en niet meer in aparte systemen. Bij deze wetswijziging is ook een aanpassing van de Kadasterwet vastgesteld, waardoor de wijze van authenticatie verandert. Daarmee is het mogelijk gemaakt om 

brondocumenten ter inschrijving in de openbare registers aan te bieden volgens een op de Wkpb afgestemde procedure. Het idee hierachter is dat een inhoudelijke controle door het Kadaster voor deze documenten niet nodig is, omdat de in te schrijven documenten formele besluiten van bestuursorganen betreffen. Vanwege de afwijkende werkwijze voor inschrijven en registreren van publiekrechtelijke beperkingen is er binnen de BRK een subsysteem gebouwd, de BRK-PB. 

## **Regeling Wkpb** 

De regeling kenbaarheid publiekrechtelijke beperkingen onroerende zaken is een nadere uitwerking van de wet Wkpb en de Kadasterwet en is sinds 1 april 2020 van kracht. In de regeling is opgenomen wat onder een brondocument dient te worden verstaan, uit welke registraties werkingsgebieden gekozen kunnen worden, op welke wijze handmatig ingetekende geometrie (ook wel ‘vrije contour’ of ‘contour’ genoemd) moet worden aangeboden, welke essentialia bij inschrijving van een beperking dienen te worden geregistreerd en welke mogelijkheden een bronhouder heeft als een gekozen werkingsgebied niet langer actueel is. 

De Wkpb bepaalt dat bestuursorganen die publiekrechtelijke beperkingenbesluiten nemen, de verplichting hebben tot inschrijving in de BRK-PB. Vanaf 2020 geldt dat dus ook voor gemeenten. Die inschrijving is onderdeel van een proces dat al lang voor de inschrijving van start is gegaan: het besluit wordt voorbereid, genomen en kenbaar gemaakt. Na de inschrijving kan een beperking nog wijzigen, beëindigd worden, of worden ingetrokken. Deze bijwerkingen ontstaan als gevolg van: 

- een herziening of intrekking van het oorspronkelijke besluit; 

- een beslissing in administratief beroep; 

> 2 Bron: Handboek Wkpb-beheer op https://www.kadaster.nl/-/stappenplan-beter-kenbaar-stap-4 

**==> picture [69 x 16] intentionally omitted <==**

- een rechterlijke uitspraak; 

- het vervallen of wijzigen van een werkingsgebied omdat het bijbehorende object niet langer actueel is; 

- andere wijzigingen die relevant zijn voor de juridische werking van een beperkingenbesluit. 

Deze wijzigingen van het beperkingenbesluit leiden tot bijwerking van de BRK op basis van een ter inschrijving aangeboden stuk. De beëindiging van de registratie van een publiekrechtelijke beperking kan doormiddel van het inschrijven van een beëindigingsbesluit of door het toevoegen van een “Datum beëindiging” waardoor de beperking na het verstrijken van die datum wordt beëindigd. 

In paragraaf 3.2 worden deze wijzigingen nader beschreven. 

## **3.1 Gebeurtenissen BRK** 

Voor de bijwerking van de BRK op basis van de hier beschreven gebeurtenisen worden de actualiteitsnomen gevolgd zoals die zijn beschreven in het kwaliteitshandvest: 

De verwerkingstijd van aangeboden akten en hypotheekstukken is als volgt: 

   - Beslissen of stukken in de openbare registers ingeschreven kunnen worden: binnen 24 uur op werkdagen 

   - Bekend maken van stukken in de Basisregistratie Kadaster en registraties voor Schepen en Luchtvaartuigen (Signaleren): voor 9.00 uur volgende werkdag 

   - Volledige verwerking van stukken in de Basisregistratie Kadaster en registraties voor Schepen en Luchtvaartuigen: binnen 6 werkdagen 

   - Bekend maken van beslagen in de Basisregistratie Kadaster en registraties voor Schepen en Luchtvaartuigen (Signaleren): binnen 1 uur na aanbieding (m.b.t. aanbieding geldt: op werkdagen waarbij stukken tussen 9.00 uur en 15.00 uur worden ingeschreven) 

   - Een nieuwe grens, gebaseerd op een ingeschreven stuk, inmeten en bijwerken in de kadastrale registratie: binnen 3 maanden nadat de grens door de gezamenlijke belanghebbenden is aangewezen 

- 3.1.1 Bijwerking op grond van een ingeschreven stuk Beschrijving gebeurtenis: Het bijwerken van de BRK op basis van een ingeschreven stuk. 

Toelichting gebeurtenis: 

De stukken die ter inschrijving worden aangeboden bij het kadaster zijn over het algemeen notariële akten. Met de inschrijving van deze stukken in het openbaar register neemt de bijwerking van de BRK terstond een aanvang. Nadat een inschrijving heeft plaatsgevonden, wordt bij de gegevens in de BRK waarop de inschrijving betrekking heeft, een aantekening geplaatst dat er een stuk is ingeschreven. Hiervoor wordt bij het perceel en de rechthebbende melding gemaakt van het tijdstip en het stukidentificatienummer. De aantekening wordt achterwege gelaten als de bijwerking terstond plaatsvindt en verwijderd nadat de bijwerking is voltooid. 

Indien de inschrijving van een stuk tot gevolg heeft dat gegevens over de eigenaar, de beperkt gerechtigden, de kadastrale aanduiding, de grootte dan wel een gegeven als bedoeld in art. 48 lid 2 sub c Kadasterwet in de BRK worden gewijzigd of aangevuld, dan wordt bij deze gewijzigde of aangevulde gegevens verwezen naar het ingeschreven stuk. De verwijzing geschiedt door vermelding van het tijdstip en het stukidentificatienummer van het ingeschreven stuk. 

**==> picture [69 x 16] intentionally omitted <==**

3.1.2 Bijwerking op grond van een kadasterstuk Beschrijving gebeurtenis: Het bijwerken van de BRK op basis van een kadasterstuk. Toelichting gebeurtenis: Naar aanleiding van een klacht of bezwaar dan wel een fout ontdekt door het Kadaster zelf wordt een kadasterstuk aangemaakt. Op grondslag van dit stuk vindt bijwerking plaats. Indien het kadasterstuk tot gevolg heeft voor de bijwerking dat gegevens over de eigenaar, de beperkt gerechtigden, de kadastrale aanduiding, de grootte dan wel een gegeven als bedoeld in art. 48 lid 2 sub c Kadasterwet in de BRK worden gewijzigd of aangevuld, dan wordt bij deze gewijzigde of aangevulde gegevens verwezen naar het kadasterstuk. De verwijzing geschiedt door vermelding van de dagtekening van de bijwerking en het volgnummer van het kadasterstuk. 

3.1.3 Bijwerking op grond van een relaas van bevindingen Beschrijving gebeurtenis: Het bijwerken van de BRK mede dan wel geheel op basis van een relaas van bevindingen. Toelichting gebeurtenis: Wanneer de bijwerking plaatsvindt op grondslag van een ingeschreven stuk en ten behoeve van de bijwerking een meting noodzakelijk is, wordt van de meting een relaas van bevindingen opgesteld. De bijwerking vindt vervolgens plaats mede op grondslag van het relaas van bevindingen. In de overige gevallen waarvoor een relaas van bevindingen moet worden opgesteld, vindt bijwerking in zijn geheel plaats op grondslag van deze relaas van bevindingen. Indien het relaas van bevindingen tot gevolg heeft voor de bijwerking dat gegevens over de eigenaar, de beperkt gerechtigden, de kadastrale aanduiding, de grootte of een gegeven als bedoeld in art. 48 lid 2 sub c Kadasterwet in de BRK worden gewijzigd of aangevuld, wordt bij het gewijzigde of aangevulde gegeven verwezen naar het relaas van bevindingen. De verwijzing geschiedt door vermelding van de dagtekening van de bijwerking en het volgnummer van het relaas van bevindingen. 

3.1.4 Terugmelding Beschrijving gebeurtenis: Een bestuursorgaan of een belanghebbende meldt aan het Kadaster zijn gerede twijfel over de juistheid van een in de BRK opgenomen authentieke gegeven. Toelichting gebeurtenis: Het kadaster haalt de gegevens omtrent bijwerking uit brondocumenten. Dit zijn de hiervoor genoemde ingeschreven stukken, kadasterstukken en relazen van bevindingen. Er mag op worden vertrouwd dat het kadaster deze gegevens juist uit het brondocument overneemt. Bestuursorganen die veronderstellen dat de BRK een authentiek gegeven niet correct heeft overgenomen uit een brondocument, melden onder opgaaf van redenen hun gerede twijfel omtrent de juistheid van dit in de BRK opgenomen authentieke gegeven. Voor belanghebbenden bestaat er in zulke gevallen de mogelijkheid om onder opgaaf van redenen een verzoek tot herstel te doen. Het kadaster neemt na ontvangst van een terugmelding of een verzoek tot herstel binnen een dag een beslissing over wijziging van het betreffende authentieke gegeven. Deze beslissing is een besluit in de zin van de Algemene wet 

**==> picture [69 x 16] intentionally omitted <==**

## bestuursrecht (Awb). 

Als de beslissing vanwege de complexiteit niet binnen een dag na ontvangst kan worden genomen, dan zal het kadaster na het verstrijken van die dag de aantekening ‘in onderzoek’ plaatsen bij het betreffende gegeven in de BRK of in een afzonderlijk register indien het een authentiek gegeven betreft van de landelijke kadastrale kaart. 

Het besluit om de aantekening ‘in onderzoek’ te plaatsen is geen besluit in de zin van de Awb. Na afloop van het onderzoek neemt de BRK het besluit tot wijziging of handhaving van het authentieke gegeven en verwijdert de aantekening ‘in onderzoek’. Dit is wel een besluit in de zin van de Awb. 

Een andere situatie is wanneer een bestuursorgaan zijn gerede twijfel meldt over de juistheid van een authentiek gegeven dat uit een andere basisregistratie is overgenomen. Deze melding zendt de BRK onverwijld door aan de beheerder van de desbetreffende basisregistratie en doet hiervan mededeling aan het bestuursorgaan dat de melding heeft gedaan. Ook voor belanghebbenden bestaat in dit geval de mogelijkheid om onder opgaaf van redenen een verzoek tot herstel in te dienen. Echter dit verzoek van belanghebbenden is niet mogelijk, indien een authentiek gegeven is overgenomen uit de Basisregistratie Topografie of de registratie voor schepen of luchtvaartuigen. De BRK zendt deze melding ook onverwijld door aan de beheerder van de desbetreffende basisregistratie en doet hiervan mededeling aan de belanghebbende. 

Een terugmelding kan niet wanneer er onjuiste gegevens in het brondocument zelf staan, of als een brondocument ontbreekt. In dergelijke gevallen moet contact worden opgenomen met de opsteller van het document of zal men een brondocument moeten laten opstellen. Dit zal over het algemeen een notaris zijn. 

- 3.1.5 Beschikking Beschrijving gebeurtenis: Het nemen van een beschikking omtrent bijwerking. 

Toelichting gebeurtenis: De beslissing tot het wel of niet bijwerken van de BRK is een beschikking. De beschikking treedt in werking zonder dat het bekend is gemaakt en is daarmee een uitzondering op Artikel 3:40 Awb Tevens zijn de artikelen 4:7 en 4:8 Awb niet van toepassing. 

3.1.6 Bezwaar en beroep Beschrijving gebeurtenis: Het instellen van bezwaar tegen een beschikking inzake de bijwerking. Het instellen van beroep tegen een beslissing op bezwaar inzake de bijwerking. 

Toelichting gebeurtenis: Een belanghebbende kan tegen een beschikking inzake de bijwerking een bezwaar indienen, nadat de bijwerking is voltooid. Er kan geen bezwaar worden ingediend tegen een beschikking als bedoeld in artikel 71, 72 of 78 lid 1 Kadasterwet. Een belanghebbende kan tegen een beslissing op bezwaar inzake de bijwerking beroep instellen bij de rechtbank. 

**==> picture [69 x 16] intentionally omitted <==**

Wanneer bezwaar of beroep wordt ingesteld op een beschikking dat betrekking heeft op een wijziging van een authentiek gegeven dat is opgenomen in de BRK, moet het kadaster de aantekening ‘in onderzoek’ plaatsen bij het betreffende gegeven in de BRK of in een afzonderlijk register wanneer het een authentiek gegeven betreft van de landelijke kadastrale kaart. Als de beslissing op bezwaar of beroep strekt tot wijziging van het authentieke gegeven, wordt dit in de BRK verwerkt. De aantekening ‘in onderzoek’ wordt niet verwijderd voordat er onherroepelijk is beslist op het bezwaar of beroep. 

## **3.2 Gebeurtenissen WKPB** 

- 3.2.1 Inschrijving oorsponkelijk besluit Wkpb Beschrijving gebeurtenis: Het inschrijven van het oorspronkelijk besluit. 

Toelichting gebeurtenis: 

De eerste stap in het opleggen van een beperking is altijd het nemen van een initieel of oorspronkelijk besluit. Door of namens het bestuursorgaan is besloten om een publiekrechtelijke beperking op te leggen en dit besluit wordt vervolgens kenbaar gemaakt. De vakafdeling van het bestuursorgaan zal hiervoor een systematiek hebben ontwikkeld (aangetekende brief, huis-aan-huisblad, website) en die verandert niet door de wetswijziging Wkpb. 

Het is van groot belang dat alle essentialia in het besluit zijn opgenomen, anders kan inschrijving niet plaatsvinden en is de beperking formeel en feitelijk niet te handhaven. 

Die essentialia betreffen: 

- _de grondslag_ : de wet of het wetsartikel waar de beperking op gebaseerd is; 

- _het bestuursorgaan_ dat het brondocument of de beslissing in administratief beroep of rechterlijke uitspraak aanbiedt; 

- _het werkingsgebied_ : de locatie waarop de beperking betrekking heeft verbeeld door een opsomming van objecten of een kaart. Die eerste kunnen zijn: percelen uit de BRK, objecten uit de BAG en objecten uit de BGT. Het werkingsgebied dient eenduidig te zijn en niet voor interpretatie vatbaar; 

- _een ingangsdatum_ van de beperking, deze kan samenvallen met de datum van de kenbaarheid; 

- een eventuele _beëindigingsdatum_ van de beperking. 

Bij inschrijving wordt de publiekrechtelijke beperking geregistreerd in de BRK-PB onder een kadastereigen identificatienummer, terwijl het brondocument in de openbare registers wordt opgenomen met een registeridentificatie bestaande uit deel, nummer en reeks. 

- 3.2.2 Inschrijving wijzigingsbesluit Wkpb Beschrijving gebeurtenis: Inschrijving van een wijzigingsbesluit 

Toelichting gebeurtenis: Het wijzigingsbesluit is altijd terug te herleiden naar het oorspronkelijke besluit. Het kent vele denkbare varianten: het vergroten of verkleinen van het werkingsgebied, 

**==> picture [69 x 16] intentionally omitted <==**

het wijzigen van voorwaarden waaronder de beperking kan worden opgeheven, het verlengen van een beperkingentermijn etc. 

Bij inschrijving van een wijzigingsbesluit wordt de bestaande registratie van de desbetreffende publiekrechtelijke beperking in de BRK-PB bijgewerkt, terwijl het brondocument in de openbare registers wordt opgenomen met een registeridentificatie bestaande uit deel, nummer en reeks. 

- 3.2.3 Inschrijving beëindigingsbesluit en de vervallenverklaring Wkpb Beschrijving gebeurtenis: Inschrijving van een beëindigingsbesluit of een vervallenverklaring 

Toelichting gebeurtenis: 

Een beëindigingsbesluit is een besluit waarmee een opgelegde publiekrechtelijke beperking in zijn geheel wordt beëindigd, bijvoorbeeld omdat aan de voorwaarden voor beëindiging zoals opgenomen in het oorspronkelijke besluit is voldaan. Met het beëindigingsbesluit wordt een vóorkomen aan de levenscyclus van de beperking toegevoegd. 

Een bijzonder vorm van een beëindigingsbesluit is de _vervallenverklaring_ . Dit is een verklaring door of namens het bestuursorgaan waarmee een opgelegde publiekrechtelijke beperking wordt beëindigd in situaties dat de vakwet niet voorziet in een beëindigingsbesluit. Dit kan bijvoorbeeld plaatsvinden bij het aanwijzen van een provinciaal monument op grond waarvan de opgelegde beperking als gemeentelijk monument eindigt. 

Bij inschrijving van een beëindigingsbesluit of een vervallenverklaring wordt de bestaande registratie de publiekrechtelijke beperking in de BRK-PB bijgewerkt, terwijl het brondocument in de openbare registers wordt opgenomen met een registeridentificatie bestaande uit deel, nummer en reeks. 

- 3.2.4 Inschrijving van een herroepingsbesluit Wkpb Beschrijving gebeurtenis: Inschrijving van een herroepingsbesluit 

Toelichting gebeurtenis: Soms is het nodig om een beperking uit de registratie te verwijderen omdat deze ten onrechte is opgevoerd. Denk aan beperkingen die van onjuiste attribuutgegevens (bijvoorbeeld een verkeerde objectaanduiding) zijn voorzien. Ook een onjuist brondocument dat per abuis is ingeschreven kan een aanleiding zijn om een beperking te herroepen. Tot slot kan het beperkende besluit van een bronhouder zijn herroepen door een hoger bevoegd gezag – dit is uitsluitend mogelijk als de vakwet hierin voorziet – of door een rechterlijke uitspraak. Het verwijderen van dergelijke beperkingen wordt ‘herroepen’ genoemd. 

Bij inschrijving van een herroepingsbesluit wordt bij de bestaande publiekrechtelijke beperking de ‘Datum beëindiging’ gelijkgesteld aan ‘Datum in werking’ registratie, terwijl het brondocument in de openbare registers wordt opgenomen met een registeridentificatie bestaande uit deel, nummer en reeks. De doorlooptijd van de beperking wordt hiermee met terugwerkende kracht op nul 

**==> picture [69 x 16] intentionally omitted <==**

dagen gezet. Een en ander laat onverlet dat de ten onrechte geregistreerde beperking in een informatieproduct van het Kadaster terecht gekomen kan zijn. En hoewel deze beperking na herroepen alleen nog zichtbaar is voor de bronhouder in het beheerportaal is het voor iedereen mogelijk om via kadastrale recherche te laten achterhalen in welk tijdvak deze beperking in de BRK-PB opgenomen is geweest en kennis te nemen van de inhoud. 

## 3.2.5 Werkingsgebied Publiekrechtelijke Beperkingen WKPB 

_3.2.5.1 Werkingsgebied Publiekrechtelijke Beperkingen WKPB - BRK, BAG, BGT_ Beschrijving gebeurtenis: Het wijzigen van het werkingsgebied van een publiekrechtelijke beperking (BRK, BAG, BGT) 

Toelichting gebeurtenis: Het werkingsgebied van een publiekrechtelijke beperking kan gebaseerd zijn op een object uit de Basisregistratie Topografie, de Basisregistratie Adressen en Gebouwen. Wanneer een dergelijk object niet meer actueel is (percelen die gesplitst worden, BAG- of BGT-objecten die vervallen), dan kan dit door de bronhouder ambtshalve worden aangepast zonder dat daar een nieuwe inschrijving voor hoeft te worden gedaan. 

_3.2.5.2 Werkingsgebied Publiekrechtelijke Beperkingen WKPB - Contouren_ Beschrijving gebeurtenis: Het wijzigen van het werkingsgebied van een publiekrechtelijke beperking met een contour (GML-bestanden). 

Toelichting gebeurtenis: Het werkingsgebied van een publiekrechtelijke beperking kan gebaseerd zijn op een door de bronhouder geleverde handmatig ingetekende geometrie (‘contour’). Als die contour wijzigt (bijv. een bodemverontreiniging wordt kleiner, of een Natura2000-gebied wordt groter) dan dient de bronhouder een GML van de contour van het totale werkingsgebied opnieuw (met de wijziging er in verwerkt) aan te bieden. Deze wordt als nieuw stuk aan de bestaande registratie van de publiekrechtelijke beperking toegevoegd. Een raadpleger beschikt dan altijd over de complete actuele contour. 

3.2.6 Bezwaar en beroep Beschrijving gebeurtenis: Het instellen van bezwaar tegen de bijwerking. 

Het instellen van beroep tegen een beslissing op bezwaar inzake de bijwerking. 

Toelichting gebeurtenis: Een belanghebbende kan tegen de bijwerking een bezwaar indienen, nadat de bijwerking is voltooid. 

Een belanghebbende kan tegen een beslissing op bezwaar inzake de bijwerking beroep instellen bij de rechtbank. 

Wanneer bezwaar of beroep wordt ingesteld dat betrekking heeft op een wijziging van een authentiek gegeven dat is opgenomen in de BRK, moet het kadaster de aantekening ‘in onderzoek’ plaatsen bij het betreffende gegeven in de BRK of in 

**==> picture [69 x 16] intentionally omitted <==**

een afzonderlijk register wanneer het een authentiek gegeven betreft van de landelijke kadastrale kaart. Als de beslissing op bezwaar of beroep strekt tot wijziging van het authentieke gegeven, wordt dit in de BRK verwerkt. De aantekening ‘in onderzoek’ wordt niet verwijderd voordat er onherroepelijk is beslist op het bezwaar of beroep. 

## **4 Vertaling naar informatiemodel** 

De gedetailleerde uitwerking van de gegevens in de basisregistratie Kadaster is beschreven in het informatiemodel Kadaster (IMKAD). In dit model wordt aangegeven welke informatie in de basisregistratie Kadaster is opgenomenen laat zien hoe de wettelijke begrippen zijn omgezet naar objecttypen met attribuutsoorten en relaties tussen de objecttypen. 

Het IMKAD model beweegt mee met de ontwikkeling van wetgeving en inzichten over de registratie. Daarom is het model niet in detail in dit document opgenomen. Het volledige IMKAD model en een toelichting daarop wordt gepubliceerd op de website van het Kadaster onder https://www.kadaster.nl/imkad. 

**==> picture [439 x 322] intentionally omitted <==**

**----- Start of picture text -----**<br>
Release: 2.3.1 FINAL Draft Gebaseerd op Business object OnroerendeZaak: CDMKAD 20200701 Legend «Objecttype» Stukdeel _VoorkomenOR 0..* 1..*«Relatierol»0..* omvat «Objecttype» _Stuk _VoorkomenOR<br>Business object TeboekgesteldeZaakBusiness object Zakelijk RechtBusiness object Tenaamstelling en Zekerheidsrecht Niet getoond in dit diagram: relaties met Stukdeel. Zie diagram Alleen stukdeel. «Relatiesoort»isAanvullingOp<br>Business object AantekeningBusiness object PersoonBusiness object Stuk en StukdeelBusiness object Publiekrechtelijke beperking «Objecttype» Kadasterstuk TerInschrijvingAangebodenStuk «Objecttype» 1 heeft 0..* KadasterVerzoek «Objecttype» _VoorkomenOR<br>«featureType» GeoObject<br>RegistratiefGebied «featureType» «Static liskov» «Objecttype» Aantekening _VoorkomenOR 0..*0..* betrokkenPersoonaantekeningRecht<br>0..* 0..* aantekeningZekerheidsstelling 0..* _Zekerheidsstelling «Objecttype» _VoorkomenOR<br>0..*<br>0..*<br>aantekeningKadastraalObject _VoorkomenOR<br>rustOpObject ZekerheidsstellingHypothecair «Objecttype» ZekerheidsstellingInzakeBeslag «Objecttype» 0..* heeftBeslaglegger 1..* «Objecttype» _Persoon<br>0..* heeftHypotheeknemer<br>0..* 1..*<br>PubliekrechtelijkeBeperking «Objecttype» «Static liskov» _KadastraalObject «Objecttype» 0..1 1 0..1 rustOp+is belastend voor«Relatierol» 0..1 1..* ZakelijkRecht «Objecttype» _VoorkomenOR 0..*1 isBevanperktTot 0..*0..* Tenaamstelling «Objecttype» _VoorkomenOR 0..2..** tenNameVan 1 0..* postlocatie 0..1 _AdresLocatie «Objecttype» _VoorkomenOR<br>OnroerendeZaakFiliatie «Objecttype» OnroerendeZaakBeperking «Objecttype»leidtTot11..* 0..* beperkt 0..* 0..11 _OnroerendeZaak «Objecttype» _VoorkomenNEN3610 _TeboekgesteldeZaak «Objecttype»1..* heeftHoofdzaak«Relatiesoort» isBelastMet0..* +is belast met«Relatierol» 0..* Mandeligheid «Objecttype» _VoorkomenOR isBestemdTot1..*0..1 isBetrokkenBijisOntstaanUit1..*0..1 _AppartementsrechtSplitsing 2..*0..1«Objecttype» _VoorkomenOR betreftTenaamstelling0..* TenaamstellingFiliatie 1 «Objecttype»ontstaanVanuit0..* GezamenlijkAandeel geldtVoor«Objecttype»0..1 _VoorkomenOR 0..* woonlocatie 0..1 ObjectlocatieBinnenland «Generalisatie» _Objectlocatie «Objecttype»«Objecttype»<br>0..* ontstaanUitOZ<br>Hoofdsplitsing «Objecttype» Ondersplitsing «Objecttype» SpiegelsplitsingAfkoopErfpacht «Objecttype» SpiegelsplitsingOndersplitsing «Objecttype»<br>«Objecttype» Perceel Appartementsrecht «Objecttype» Leidingnetwerk «Objecttype»<br>0..1 0..1<br>perceelLinks perceelRechts<br>_VoorkomenNEN3610<br>KadastraleGrens «Objecttype»<br>**----- End of picture text -----**<br>


_Figuur 11 Informatiemodel Kadaster zonder stukdeel_ 

Het informatiemodel volgt de modelleringsstandaard van het Metamodel voor Informatie Modellen (MIM). Dit metamodel is een verzameling van bouwstenen c.q. modelelementen die gebruikt mogen worden om een informatiemodel mee op te stellen. Het is dus de modelleertaal waarin het informatiemodel IMKAD is uitgedrukt. In paragraaf 4.8 is een korte leeswijzer voor informatiemodellen volgens de MIM standaard opgenomen. Als eerste introductie wordt in de volgende paragafen op een vereenvoudigde wijze schematisch weergegeven hoe de informatie uit de Basisregistratie Kadaster is gemodelleerd in het informatiemodel Kadaster (IMKAD). 

**==> picture [69 x 16] intentionally omitted <==**

Met de modellen in dit hoofdstuk is op hoofdlijnen te zien hoe de Basisregistratie Kadaster is opgebouwd. De belangrijkste objecten en hun onderlinge relaties worden weergegeven. Hierbij is ook aangegeven waar de authentieke gegevens zich bevinden. 

## **4.1 Overzicht** 

In het onderstaande schema staan de relaties tussen de belangrijkste obejcten in de BRK weergeven. Het Stuk wordt ingeschreven in het Openbaar Register en is de basis voor de bijwerking van de BRK maar is feitelijk geen onderdeel van de BRK. Omdat de objecten in de BRK op een Stuk zijn gebaseerd, of er in genoemd worden, is het wel opgenomen in het model. 

**==> picture [455 x 315] intentionally omitted <==**

_Figuur 12 Informatiemodel BRK_ 

In Figuur 12 wordt de kern van de BRK weergegeven. Het centrale object is het Kadastraal object. 

- **Kadastraal Object** (Perceel, Appartementsrecht, Netwerk) 

- **Zakelijk recht** (eigendom of beperkt recht) 

- **Tenaamstelling** 

- **Zekerheidsstelling** (Beslag of Hypotheek) 

- **Aantekening** 

- **Persoon** (Natuurlijk persoon, Niet natuurlijk persoon) 

- **Stuk** (Ter inschrijving aangeboden stuk, Kadaster stuk) 

- **Stukdeel** 

- **Locatie Kadastraal Object** 

- **Objectlocatie Binnenland** 

- **Onroerende zaak beperking** 

- **Publiekrechtelijke beperking** 

**==> picture [69 x 16] intentionally omitted <==**

Uitgeschreven in tekst is het model in Figuur 12 als volgt te lezen: 

- Een **Zakelijk recht** (eigendom) rust op een **Kadastraal Object** heeft een **Tenaamstelling** ten name van een **Persoon** . 

- Een **Zakelijk recht** is belast met een **Zakelijk recht** (beperkt recht). 

- Een **Aantekening** (betreft een) aantetekening **Kadastraal Object,** een aantekening Recht ( **Tenaamstelling** ) of een Aantekening **Zekerheidsstelling** 

- Een **Zekerheidsstelling** rust op een **Kadastraal Object** en heeft een hypotheeknemer **Persoon** of een beslaglegger **Persoon** . 

- Een **Zekerheidsstelling** is een **Zekerheidsstelling Inzake Beslag** (beslag) of een **Zekerheidsstelling Hypothecair** (hypotheek). 

- Een **Locatie Kadastraal Object** betreft een **Objectlocatie Binnenland** (adres) heeft een **Kadstraal object.** 

- Een **publiekrechtelijke beperking** leidt tot een **Onroerende zaak beperking** 

- Een **Onroerende zaak beperking** beperkt een **Onroerende zaak** 

- Een **Stuk** omvat **Stukdelen** 

- (niet in het diagram): 

   - Een Zakelijk recht is gebaseerd op een Stukdeel 

   - Een Aantekening is gebaseerd op een Stukdeel 

   - Een Kadastraal Object is gebaseerd op een Stukdeel 

   - `o` Een Tenaamstelling is gebaseerd op een Stukdeel `o` Een Zekerheidsstelling is gebaseerd op een Stukdeel 

## 4.1.1 Domeinen 

Het informatiemodel is onderverdeeld in samenhangende delen, ook wel domeinen genoemd. Er zijn verschillende kleuren gebruikt om de domeinen uit elkaar te houden. In de volgende paragrafen wordt per domein besproken wat de belangrijkste objecttypen zijn. Ook wordt aangegeven welke identificerende en authentieke gegevens in dat domein worden vastgelegd. 

## **4.2 Domein Kadastraal Object** 

In het onderstaande diagram is te zien dat een **Kadastraal object** een generalisatie is van **Onroerende zaak** en **Teboekgestelde zaak** . Een Kadastraal object is een registergoed waarvoor bij overdracht of vestiging van rechten inschrijving in de openbare registers van het Kadaster is vereist volgens het burgerlijk wetboek (Artikel 10 Burgerlijk Wetboek Boek 3). Een kadastraal object is een Onroerende zaak of een Teboekgestelde zaak. Teboekgestelde zaken zijn geen onderdeel van de BRK maar worden wel door het Kadaster geregistreerd. Een Kadastraal Object wordt geïdentificeerd met een identificatie attribuut. 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [440 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
LocatieBinnenland<br>**----- End of picture text -----**<br>


_Figuur 13 Overzicht domein Kadastraal Object_ 

Een Kadastraal Object is gekoppeld aan een Locatie Binnenland en er rusten een of meer zakelijke rechten op. Ook kan er een zekerheidsstelling op rusten, dit is dit meestal een recht van hypotheek. Bijzonderheden kunnen vastgelegd zijn in de aantekeningen die van toepassing zijn op het Kadastraal object. 

De gegevens van de locatie binnenland betreffen de adresgegevens zoals die zijn opgenomen in de akte. Wanneer deze overeenkomen met een adres in de bag wordt een koppeling gelegd waardoor mutaties van een gekoppeld adres in de BAG doorwerkt in de registratie in de BRK. Als de koppeling niet lukt dan wordt het adres geregistreerd zoals vermeld in de akte ten tijde van de registratie. De koppeling met de BAG is overigens alleen mogelijk voor onroerende zaken met een BAG verblijfsobject, waarbij de koppeling wordt gebaseerd op de zogenaamde nummeraanduiding van het verblijfsobject. Percelen zonder een BAG verblijfsobject, zoals weilanden en onbebouwde percelen, hebben geen adresgegevens. 

## **4.3 Domein Onroerende zaak** 

Het domein Onroerende zaak groepeert de **Percelen** , **Appartemenstrechten** en **Leidingnetwerken** als **Onroerende Zaak** . De authentieke gegevens in dit domein zijn de _Kadastrale aanduiding_ van de Onroerende Zaak en de _Kadastrale grootte_ en de _coordinaten_ van een Perceel. De Koopsom en cultuuraanduiding, bebouwd en onbebouwd zijn belangrijke niet authentieke gegevens in dit domein. 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [461 x 222] intentionally omitted <==**

_Cursief_ = authentiek, 

Onderstreept _=_ identificerend 

_Figuur 14 Overzicht domein Onroerende zaak_ 

## **4.4 Domein Zakelijk recht** 

Het domein Zakelijk Recht beschrijft de samenhang tussen de **Kadastrale Objecten** en de **Zakelijke Rechten** en de **Tenaamstelling** daarvan aan een **Persoon** en de **Zekerheidsstellingen** die kunnen rusten op een KadastraalObject. Ook andere zaken die van invloed zijn op de rechtstoestand van het Kadastrale object horen bij dit domein, zoals **Aantekening** , **Erfpachtcanon** , **Mandeligheid** . 

Een groot deel van de authentieke gegevens opgesomd in paragraaf 2.5.2 behoren tot dit domein. Deze authentieke gegevens zijn voor een deel als apart objecttype gemodelleerd zoals _Erfpachtcanon_ , _Mandeligheid_ en _Gezamenlijk Aandeel_ . Andere gegevens zijn als kenmerk (aard) van het objecttype Zakelijk Recht gemodelleerd, zoals _eigendom_ en _beperkte rechten_ zoals erfpacht, vruchtgebruik, gebruik en bewoning. Ook wordt sommige informatie die van belang is voor de rechtstoestand van een Zakelijk Recht als Aantekening geregistreerd. Dit zijn onder andere de authentieke gegevens _einddatum recht_ , _voorwaardelijke verkrijging_ en _erfdienstbaarheid_ . Dit betreft bovendien de zaken die een beperking betreffen, zoals een _publiekrechtelijke beperking_ en een _kwalitatieve verplichting_ . 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [461 x 267] intentionally omitted <==**

_Figuur 15 Overview Zakelijk recht_ 

## **4.5 Domein Persoon** 

Binnen het domein Persoon komt de problematiek met betrekking tot de dubbele authenticiteit naar voren. De persoonsgegevens kunnen afkomstig zijn uit verschillende bronnen. In eerste instantie worden ze overgenomen uit het ter inschrijving aangeboden stuk. 

Als in de akte een NatuurlijkPersoon is genoemd, dan wordt gekeken of de persoon gekoppeld kan worden met de Basisregistratie Personen (BRP). Als de persoon gevonden wordt in de BRP dan wordt daarmee een koppeling gelegd. Mutaties van een gekoppelde persoon in de BRP werken dan door in zijn registratie in de BRK. Als de koppeling niet lukt dan wordt de persoon geregistreerd zoals overgenomen uit de akte. In het eerste geval is de actualiteit van het persoonsgeven nagenoeg gelijk aan de actualteit van de BRP. In het tweede geval is de actualteit gelijk aan de inschrijvingsdatum van de akte. 

Als in de akte een NietNatuurlijkpersoon is genoemd dan wordt gekeken of de persoon gekoppeld kan worden met een Handelsregister (HR) persoon. Als deze koppeling lukt wordt in de BRK bij deze persoon het Kamer van Koophandel nummer en het RSIN nummer vastgelegd. Deze koppeling wordt alleen op het moment van inschrijven gelegd, wat betekent dat de BRK niet wordt bijgewerkt op basis van mutaties bij het HR. De koppeling is een sleutel om het HR te bevragen. De actualteit is gelijk aan de inschrijvingsdatum van de akte. 

In dit schema is zichtbaar in welke soorten personen in de BRK voorkomen. Ten eerste N **atuurlijke Personen** en **Niet Natuurlijke Personen** . Deze personen worden vervolgens uitgewerkt volgens het gegevensmodel van 

respectievelijk de BRP met het object Geregistreerd Persoon en met gegevensmodel van het HR met het object Rechtspersoon. 

Binnen de BRK komen de personen in verschillende rollen voor, als rechthebbende bij een tenaamstelling of een hypotheek of beslag of als Persoon waarop een aantekening van toepassing is. 

Van een Natuurlijke persoon zijn de _geslachtsnaam, voornaam, voorvoegsel geslachtsnaam, geboortedatum,_ 

_geboorteland, geslachtsaanduiding_ en het _partnerschap_ authentieke gegevens. Van de niet natuurlijk persoon zijn de _StatutaireNaam, StatutaireZetel_ en de _Rechtsvorm_ authentiek. Verder worden de woonlocatie en de postlocatie van een persoon vastgelegd. 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [476 x 227] intentionally omitted <==**

**==> picture [119 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cursief  = authentiek,<br>Onderstreept = identificerend<br>**----- End of picture text -----**<br>


_Figuur 16 Overzicht domein Persoon_ 

## **4.6 Domein Stuk** 

De brondocumenten die aan de basis van de BRK liggen, zijn gemodelleerd in de begrippen Stuk en Stukdeel. Ieder stuk heeft tenminste een stukdeel, waarin de gegevens (rechtsfeiten) zijn beschreven op basis waarvan de BRK wordt bijgewerkt. Dit betreft gegevens zoals persoon, zakelijk recht, zekerheidsstelling, tenaamstelling, appartementsrecht en onroerende zaak. Een voorbeeld van een dergelijk rechtsfeit is de overdracht, waarin wordt beschreven dat een bepaald recht wordt overgedragen van de ene persoon naar de andere persoon. In de BRK wordt dan de tenaamstelling van de eerste persoon (vervreemder) beëindigd en die van de tweede persoon (verkrijger) opgevoerd. 

Er zijn twee soorten stukken die leiden tot een bijwerking van de BRK: 

1. **Ter inschrijving aangeboden stukken** meestal notariële akten, zoals: akte van levering, akte van appartementssplitsing, hypotheekakte enz. 

2. Interne (correctie) stukken worden verwerkt met een **Kadasterstuk** . 

Ook hierbij bepaalt het stukdeel welke bijwerking er plaats vindt. De soorten stukdelen zijn te vinden in de waardelijst aardStukdeel. 

**==> picture [69 x 16] intentionally omitted <==**

**==> picture [437 x 236] intentionally omitted <==**

**==> picture [119 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cursief  = authentiek,<br>Onderstreept = identificerend<br>**----- End of picture text -----**<br>


_Figuur 17 Overzicht domein Stuk_ 

Binnen het domein Stuk zijn _deel en nummer_ en het _tijdstip aanbieding stuk_ van het **Ter inschrijving Aangeboden Stuk** authentieke gegevens. Voor de meeste objecten uit IMKDAD is vastgelegd op basis van welke stukdelen die zijn ontstaan en in welke stukdelen ze worden vermeld. Op die manier zijn deze objecten te relateren aan de stukken die zijn ingeschreven in het openbaar register. 

## **4.7 Domein Publiekrechtelijke beperking** 

**==> picture [411 x 203] intentionally omitted <==**

Onderstreept = identificerend _Figuur 18 Overzicht domein Publiekrechtelijke beperking_ 

**==> picture [69 x 16] intentionally omitted <==**

Het domein Publiekrechtelijke beperking heeft geen authentieke gegevens. Het gebied van een publiekrechtelijke beperking ( **Beperikingsgebied** ) wordt aangeduid als een BGT object, een BAG object, een BRK object, of een vrije contour. In de levering van gegevens uit de BRK wordt bepaald welke **Onroerende zaken** geheel of gedeeltelijk samenvallen met **werkingsgebieden** van Publiekrechtelijke beperkingen. 

## **4.8 Leeswijzer MIM modellen** 

Als handreiking voor het lezen van het informatiemodel zoals gepubliceerd op https://www.kadaster.nl/imkad worden hier de belangrijkste concepten uit het MIM kort toegelicht. 

## **Objecttype** 

Een objecttype is een groep van gelijksoortige objecten. 

Om duidelijk te maken wat wordt bedoeld kijken we eerst naar het begrip ‘object’. 

_Definitie Object_ 

_Een ding, een tastbaar iets, in de werkelijkheid, zoals daarnaar gekeken wordt vanuit een bepaald domein. Toelichting:_ Het wordt veelal als niet politiek correct beschouwd mensen als objecten te zien. In dit kader, de informatievoorziening, beschouwen we evenwel natuurlijke en niet-natuurlijke personen wel als objecten. ‘Tastbaar’ moet hierbij ruim geïnterpreteerd worden. Het gaat niet alleen om fysiek herkenbare objecten zoals auto’s, gebouwen en mensen, ook om zogenaamde virtuele objecten waarover binnen het domein door betrokkenen gecommuniceerd wordt zoals kadastrale percelen, (maatschappelijke) activiteiten en processen. Hoe een ‘tastbaar iets’ als een object beschouwd wordt, hangt af van het domein waarvoor dat ‘tastbaar iets’ relevant is. Zo wordt de gebouwde omgeving in het ene domein beschouwd als een verzameling gebouwen terwijl een ander domein daarin panden onderscheidt. Een object is voor een domein relevant als eigenschappen (kenmerken) daarvan van belang zijn voor het functioneren van dat domein. 

## _Definitie Objecttype_ 

_De typering van een groep objecten (in de werkelijkheid) die binnen een domein relevant zijn en als gelijksoortig worden beschouwd._ 

_Toelichting_ Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het type ‘natuurlijk persoon’. In een ander domein, ‘de volksmond’, noemen we dit ‘mens’ wat ook een objecttype is. In weer een ander domein is Jan van het type ‘vergunninghouder’ en Piet en Marie niet, omdat aan hen (nog) nooit een vergunning verleend is. 

Objecttypen zijn een abstractie van de werkelijkheid waarmee we de werkelijkheid zo getrouw mogelijk beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie. Daartoe is veelal een interpretatie nodig (van die werkelijkheid c.q. die objecttypen) naar eenheden die in een registratie vastgelegd kunnen worden (records, entiteiten e.d.) op basis van andere overwegingen. 

## **Attribuutsoort** 

Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip ‘gegeven’. 

## _Definitie Gegeven_ 

_De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend._ 

_Toelichting:_ Gegevens zijn de objectief waarneembare neerslag of registratie van feiten op een bepaald medium, zodanig dat deze gegevens uitgewisseld en voor langere tijd bewaard kunnen worden. Dat kan op papier, in digitale vorm, et cetera. Met deze gegevens wordt een model (een selectief deel dus) van de werkelijkheid vastgelegd in de tijd. Ofschoon de werkelijkheid nooit stilstaat, kan deze door het vastleggen van de gegevens toch worden bevroren. 

**==> picture [69 x 16] intentionally omitted <==**

Voorbeelden van gegevens zijn de waardes ‘Jan’ en ‘man’ betreffende de naam en het geslacht van een object van het type Persoon. Merk op dat een gegeven zonder duidelijkheid over het type gegeven (naam, geslacht e.d.) geen informatie biedt. Een gegeven wordt ook wel attribuut genoemd. 

_Definitie Attribuutsoort_ 

_De typering van gelijksoortige gegevens die voor een objecttype van toepassing is._ 

_Toelichting_ Een gegeven met stereotype attribuutsoort is een kenmerk van een object. 

Attribuutsoorten worden ook wel kenmerken of eigenschappen genoemd. Aan elk objecttype worden nul, één of meer _«_ Attribuutsoort _»_ en toegekend. In een informatiemodel worden alleen voor het domein relevante attribuutsoorten opgenomen bij een objecttype. 

_Bijvoorbeeld: we kunnen definiëren dat 'persoonsnaam' en 'geslachtsaanduiding' attribuutsoorten zijn die van toepassing zijn voor het objecttype 'persoon'. Wanneer ‘oogkleur’ niet relevant is voor het domein, wordt deze niet gemodelleerd._ 

**==> picture [249 x 116] intentionally omitted <==**

_Figuur 19: Voorbeeld van Objecttype met attribuutsoorten_ 

In Figuur 8 is een objecttype Perceel te zien met zijn attribuutsoorten. Als bij een attribuutsoort [0..1] is weegegeven dan betekent dit dat een attribuut van dat soort 0 tot 1 keer kan voorkomen bij een object van dat type. Of meer algemeen als ergens [n..m] staat betekent dit dat het attribuutsoort n tot m keer kan voorkomen. In het voorbeeld hierboven komt de attribuutsoort perceelnummerRotatie 0 of 1 keer voor bij een perceel. De samenhang tussen objecttypen is te zien in de vorm van verbindingspijlen (relaties) die van het ene Objecttype naar het andere wijzen. In de modellen zijn drie soorten relaties te zien: 

**==> picture [102 x 67] intentionally omitted <==**

**==> picture [313 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
Gerichte relatie van bron naar doel.<br>-- Toelichting --<br>Een Zekerheidsstelling heeft een relatie met de naam “rustOpObject” die wijst<br>naar nul of één KadastraalObject<br>«Objecttype»<br>_KadastraalObject<br>1 rustOpObject<br>«Objecttype»<br>_Zekerheidsstelling<br>**----- End of picture text -----**<br>


**==> picture [69 x 16] intentionally omitted <==**

**==> picture [68 x 64] intentionally omitted <==**

Gerichte relatie waarbij het doel een onderdeel is van het bron object (compositie). -- Toelichting -- 

Een Stuk heeft een compositie relatie met de naam “omvat” die wijst naar één of meer Stukdelen. Ofwel een Stuk omvat altijd een of meer stukdelen. 

**==> picture [304 x 58] intentionally omitted <==**

**==> picture [59 x 59] intentionally omitted <==**

Generalisatie relatie, het doel objecttype is een generalisatie van het bron objecttype. 

-- Toelichting -- Een Zekerheidsstelling is een generalisatie van een ZekerheidsstellingHypothecair en een ZekerheidsstellingInzakeBeslag. Of andersom beschreven een ZekerheidsstellingHypothecair is een specialisatie van een Zekerheidsstelling. 

**==> picture [174 x 174] intentionally omitted <==**

