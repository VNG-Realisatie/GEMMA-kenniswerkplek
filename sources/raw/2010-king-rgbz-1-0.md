---
title: "Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 1.0"
source: "KING / VNG Realisatie"
author: "KING (Kwaliteitsinstituut Nederlandse Gemeenten)"
published: 2010-09-01
created: 2026-06-18
description: "Informatiemodel voor zaakgerelateerde gegevens: definieert objecttypen, attributen en relaties voor zaakgericht werken (ZAAK, BETROKKENE, ROL, STATUS, DOCUMENT, BESLUIT, ZAAKOBJECT)."
tags:
  - "Dienstverlening"
  - "Standaarden"
  - "GEMMA"
---

**==> picture [440 x 444] intentionally omitted <==**

## **Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ)** 

onderdeel van de GEMeentelijke Model Architectuur (GEMMA) 

versie 1.0 (in gebruik) september 2010 

**==> picture [181 x 92] intentionally omitted <==**

Kwaliteitsinstituut Nederlandse Gemeenten (KING) Nassaulaan 12 Postbus 30435 2500 GK Den Haag T: 070 373 8017 F: 070 363 5682 www.KINGgemeenten.nl 

2 

## **Voorwoord** 

Zaakgericht werken is  in opkomst bij  gemeenten. Het biedt de mogelijkheid  om zowel  de dienstverlening aan de klant te verbeteren als de interne efficiëntie van de dienstverleningsprocessen. Ook kan het worden toegepast op andere zowel in- als externe activiteiten van een gemeente. Een eenduidig begrippenkader is noodzakelijk om binnen de gemeente  in  zaken  samen te werken.  Hiertoe  is  in  2004  door  de  VNG  het  GFO  Zaken uitgebracht. Ervaringen in het gebruik van het GFO Zaken en het uitbrengen in 2007 van het RSGB(asisgegevens) door EGEM i-teams deed de behoefte ontstaan aan een nieuwe versie. Dat is het RGBZ(aken) dat voor u ligt. 

Deze rapportage is het voorlopige eindresultaat van een werkgroep onder verantwoordelijkheid van EGEM i-teams. De werkgroep bestond uit de volgende vertegenwoordigers: 

- Charley Beekhuizen (gemeente Den Haag) 

- Arnold Berkhout (gemeente Alkmaar) 

- Timo ten Cate (Spécialité) 

- Corné Dekker (GovUnited) 

- Kees Duijvelaar (VNG) 

- Hans Goutier (ICTU–Kenniscentrum) 

- Ben de Jong (gemeente Amstelveen) 

- Arjan Kloosterboer (EGEM i-teams; opsteller rapportage) 

- Magda van Noordenburg (EGEM i-teams; werkgroepvoorzitter) 

- Elbert Raadsen (ICTU–Kenniscentrum) 

- Erik Vos (gemeente Haarlemmermeer) 

- Paul Wouters (EGEM i-teams, werkgroepsecretaris). 

## **Beheer** 

Deze rapportage is in september 2010 vastgesteld door de StUF-regiegroep. Commentaar op deze  versie  nemen we  in de normale  beheerprocedure  van het RGB  Zaken mee. KINGspecialisten beoordelen wijzigingsverzoeken en leggen ze ter advisering voor aan werkgroepen met  een  publiek-private  samenstelling. Iedere  belangstellende kan  wijzigingsverzoeken indienen. 

Per 1 januari 2010 is het beheer van het RGBZ overgenomen door KING, het KwaliteitsInstituut Nederlandse Gemeenten. 

Voor  vragen,  suggesties  of  opmerkingen  kunt  u  contact  opnemen  met  ons.  Zie  de contactgegevens op de voorgaande pagina. 

3 

## **Leeswijzer** 

De rapportage richt zich op iedereen die zich beroepsmatig bezighoudt met (het structureren van)  de  gemeentelijke  informatievoorziening,  het  zaakgericht  werken  en/of  het  tot  stand brengen en beheren van gegevensuitwisseling ten behoeve van het zaakgericht werken.. De  rapportage  is  opgebouwd  overeenkomstig  de  gebruikelijke  indeling  van  catalogi  voor basisregistraties. Allereerst beschrijven we in hoofdstuk 2 het RGB Zaken op hoofdlijnen en lichten we het referentiemodel nader toe. In paragraaf 2.1 gaan we in op de rol van het RGB Zaken binnen GEMMA. In paragraaf 2.2 vindt u een overzicht van het objectenmodel en de daarmee samenhangende aspecten. In de hoofdstukken 3 en 4 vindt u de specificaties van de elementen waaruit het RGB Zaken is opgebouwd: objecttypen (hoofdstuk 3), attribuutsoorten en relatiesoorten (hoofdstuk 4). Deze hoofdstukken zijn vooral als ‘naslagwerk’ bedoeld. 

4 

## **Samenvatting** 

Het model specificeert de gegevens en hun samenhang die gemeenten, daarmee samenwerkende organisaties en hun klanten minimaal nodig hebben om voldoende op de hoogte te zijn van lopende en afgeronde zaken. Op basis van het model kunnen betrokkenen bij,  en  geïnteresseerden  in  een  zaak  geïnformeerd  worden.  Dit  loopt  van  ex-  en  interne initiatoren van een zaak via medebehandelaars daarvan en belangstellenden in de publicatie van de zaak of het resultaat daarvan, tot management dat behoefte heeft aan sturingsinformatie. Met de gegevens in het model moet men ook (achteraf) een zaak kunnen verantwoorden, zowel inhoudelijk (is de zaak goed afgehandeld) als qua proces (is de zaak op de  juiste  wijze  afgehandeld),  en  desgewenst  de  (behandeling  van  de)  zaak  kunnen reconstrueren. 

Hieronder visualiseren we het RGB Zaken op hoofdlijnen. 

**==> picture [340 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
BETROKKENE<br>betreft<br>ZAAKOBJECT betreft<br>NATUURLIJK  andere<br>PERSOON<br>ZAAK<br>NIET-<br>NATUURLIJK<br>PERSOON<br>oefent uit<br>VESTIGING ROL BESLUIT<br>ORGANISA-<br>TORISCHE<br>EENHEID<br>MEDEWERKER<br>is relevant voor<br>STATUS DOCUMENT<br>is deelzaak van<br>betreft kan leiden tot<br>heeft<br>zet heeft<br>zet kan vast-<br>gelegd zijn als<br>**----- End of picture text -----**<br>


Afbeelding 1: RGBZ op hoofdlijnen 

Kenmerkend is de centrale positie van de ZAAK met daaraan gerelateerd de voor de ZAAK relevante  DOCUMENTen,  de  ZAAKOBJECTen  waarop  de  ZAAK  betrekking  heeft  en  de BETROKKENEn in hun ROLlen ten aanzien van de ZAAK. 

## **Doelen** 

Het RGBZ voorziet in standaarden zodat gemeenten en organisaties waarmee zij samenwerken hun  zaakgegevens  eenduidig  kunnen  vastleggen  en  onderling  over  de  zaak  kunnen communiceren. Het RGBZ vormt de grondslag voor de doorontwikkeling van de berichtenstandaard StUF-Zaken. 

## **Gebruik** 

Het RGBZ is voor ontwerpers en ontwikkelaars een handvat om te bepalen welke gegevens op welke wijze in bijvoorbeeld een zakenmagazijn moeten worden opgenomen. Het RGBZ is niet bedoeld als een uitputtend voorschrift. Als de gemeente bijvoorbeeld een zakenbeheersysteem wil inrichten, dan moet dat tenminste de gegevens bevatten die in het model zijn opgenomen, volgens de daarin vastgelegde specificaties. 

5 

## **Inhoudsopgave** 

|**1. Inleiding**<br>  <br>**.....................................................................................................................................**<br>**7**|
|---|
|**2. Afbakening**<br>  <br>**................................................................................................................................**<br>**9**|
|2.1. Relatie tot GEMMA<br>..............................................................................................................<br>9|
|2.2. Objectenmodel<br>...................................................................................................................<br>11|
|**3. De soorten van objecten van registratie**<br>**..............................................................................**<br>**15**|
|3.1. Besluit<br>................................................................................................................................<br>18<br>|
|3.2. Besluittype<br> <br>..........................................................................................................................<br>19<br>|
|3.3. Betrokkene<br>.........................................................................................................................<br>20|
|3.4. Document<br>...........................................................................................................................<br>25|
|3.5. Documenttype<br>....................................................................................................................<br>27|
|3.6. Enkelvoudig document<br>.......................................................................................................<br>28<br>|
|3.7. Medewerker<br> <br>.......................................................................................................................<br>30<br>|
|3.8. Object<br>.................................................................................................................................<br>32|
|3.9. Organisatorische eenheid<br>..................................................................................................<br>52|
|3.10. Rol<br>  <br>....................................................................................................................................<br>54<br>|
|3.11. Samengesteld document<br>.................................................................................................<br>56<br>|
|3.12. Status<br>...............................................................................................................................<br>57<br>|
|3.13. Statustype<br>........................................................................................................................<br>58<br>|
|3.14. Zaak<br>.................................................................................................................................<br>59|
|3.15. Zaakdocument<br>    <br>.................................................................................................................<br>61<br>|
|3.16. Zaakobject<br>     <br>........................................................................................................................<br>62<br>|
|3.17. Zaaktype<br>..........................................................................................................................<br>63|
|**4. Beschrijving van de attributen en relaties**<br>**..........................................................................**<br>**64**<br>|
|4.1.Besluit<br>    <br>................................................................................................................................<br>70<br>|
|4.2.Besluittype<br>  <br>..........................................................................................................................<br>79<br>|
|4.3.Betrokkene<br>.........................................................................................................................<br>86<br>|
|4.4. Document<br>...........................................................................................................................<br>88|
|4.5. Documenttype<br> <br>....................................................................................................................<br>97<br>|
|4.6. Enkelvoudig document<br>.....................................................................................................<br>103|
|4.7. Medewerker<br>.....................................................................................................................<br>110|
|4.8. Object<br>...............................................................................................................................<br>120|
|4.9. Organisatorische eenheid<br>................................................................................................<br>128|
|4.10. Rol<br>..................................................................................................................................<br>138|
|4.11. Samengesteld document<br>...............................................................................................<br>152|
|4.12. Status<br>.............................................................................................................................<br>153|
|4.13. Statustype<br>......................................................................................................................<br>158|
|4.14. Zaak<br>...............................................................................................................................<br>164|
|4.15. Zaakdocument<br>...............................................................................................................<br>191|
|4.16. Zaakobject<br>......................................................................................................................<br>195|
|4.17. Zaaktype<br>........................................................................................................................<br>197|
|**Bijlage 1: Dublin Core**<br>**.............................................................................................................**<br>**209**|



6 

## **1. Inleiding** 

In 2004 heeft de Vereniging van Nederlandse Gemeenten (VNG) het Gemeentelijk Functioneel Ontwerp Zaken uitgebracht. Een zaak is daarin gedefinieerd als: 

“ _een  samenhangende  hoeveelheid  werk  met  een  gedefinieerde  aanleiding  en  een gedefinieerd resultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden_ .” 

Met dit GFO Zaken werd een standaard gezet voor de centrale beschikbaarheid van basis- en sleutelgegevens over een zaak en het centraal kunnen ontsluiten van een zaak. Het GFO Zaken is in de daarop volgende jaren door een toenemend aantal gemeenten en leveranciers benut bij het verbeteren van de dienstverlening aan burgers en bedrijven. 

In 2007 heeft  EGEM i-teams versie 1.0 van het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) opgeleverd. Hierin zijn de landelijke basisregistraties ‘vertaald’ naar het model van de gemeentelijke gegevenshuishouding volgens het principe ‘eenmalig bijhouden, meervoudig gebruik’. 

Zaken en basisregistraties zijn aan elkaar gerelateerd: in elke (gegevens)catalogus van een basisregistratie is een hoofdstuk opgenomen met gebeurtenissen - zoals het verlenen van een bouwvergunning - die aanleiding geven tot wijzigingen in die basisregistratie. De activiteiten die een  gemeente  uitvoert  om  tot  die  wijziging  te  komen  vormen  gezamenlijk  een  zaak, bijvoorbeeld het behandelen van een bouwaanvraag. Een mutatie in een basisregistratie mag alleen doorgevoerd worden op basis van een besluit, zoals een bouwvergunning. Een dergelijk besluit  is  vastgelegd  in  een  document  dat  gedurende  de  behandeling  van  de  zaak geproduceerd wordt. 

Vanwege de nauwe relatie tussen beide modellen ontstond de behoefte om het GFO Zaken en het RSGB te verbinden. Dit hebben we in de periode december 2007 – maart 2009 gerealiseerd in een werkgroep met gemeentelijke ervaringsdeskundigen onder leiding van EGEM i-teams. Het heeft tevens geleid tot een actualisatie van het GFO Zaken met als belangrijkste toevoeging het ‘document’, Het resultaat is het voorliggende Referentiemodel Gemeentelijke Basisgegevens Zaken, kortweg het RGB Zaken, afgekort: RGBZ, dat het GFO Zaken vervangt. 

## **Informatiemodel RGBZ** 

Het model specificeert de gegevens en hun samenhang die gemeenten, daarmee samenwerkende organisaties en hun klanten minimaal nodig hebben om voldoende op de hoogte te zijn van lopende en afgeronde zaken. Het draagt bij aan: 

- het verbeteren van de dienstverlening aan de burger, 

- het ondersteunen van elektronische dienstverlening, 

- het verbeteren van de bedrijfsvoering van de gemeente, 

- betere mogelijkheden tot handhaving, en 

- betere mogelijkheden voor het opstellen van de politieke agenda, het volgen van de uitvoering daarvan en het verantwoorden van resultaten in het kader van het dualisme. 

De  specificaties  van  de  gegevens  vormen  de  vastlegging  van  afspraken  over  inhoud  en betekenis  van  die  gegevens.  Zij  waarborgen  het  eenduidig  gebruik  van  die  gegevens  en voorkomen verschil in interpretatie en verkeerde gevolgtrekkingen. Dit is des te meer van belang bij digitale communicatie waarin deze gegevens betrokken zijn. 

Om de zojuist genoemde bijdrage ook in praktische zin te kunnen leveren wordt het StUFsectormodel Zaken afgeleid van het RGBZ. Waar het RGBZ als informatiemodel de semantiek en structuur van de zaakgerelateerde gegevens beschrijft, geeft StUF-Zaken de berichtspecificaties voor (web-)services en gegegevensuitwisseling. 

7 

## **GEMMA** 

Het Referentiemodel Gemeentelijke Basisgegevens Zaken is onderdeel van de Gemeentelijke Model Architectuur (GEMMA) van EGEM i-teams. De inhoud is in lijn met de Nederlandse OverheidsReferentieArchitectuur (NORA). 

## **Werkwijze** 

Als werkgroep zijn we begonnen met het inventariseren van vraagpunten,  verandervoorstellen en verbeterpunten ten aanzien van het GFO Zaken, de zogeheten issues. Hierbij hebben we ook  leveranciers  van  zaakfunctionaliteit  betrokken.  In  meerdere  werkgroepbijeenkomsten hebben we deze issues bediscussieerd en hebben we het GFO Zaken  geleidelijk getransformeerd tot het RGB Zaken. Vervolgens hebben we een review van de conceptversie gehouden  onder  leveranciers  van  zaakfunctionaliteit  en  informatiemanagers  van  grote gemeenten. Tot slot is het StUF-sectormodel Zaken afgeleid van het RGBZ. Zowel review als ‘verStUFfing’ hebben geleid tot aanpassingen. 

## **Leeswijzer** 

In hoofdstuk 2 gaan we allereerst in op het werkingsgebied van het voorliggende model en op de afbakening die we daarbinnen gekozen hebben (par. 2.1). Vervolgens schetsen we het model op hoofdlijnen (par. 2.2). 

Het model is opgebouwd uit objecttypen en hun attribuut- en relatiesoorten. In hoofdstuk 3 specificeren we de objecttypen en in hoofdstuk 4 per objecttype de attribuut- en relatiesoorten. 

Naast  dit  hoofddocument  is  de  Verantwoordingsrapportage  beschikbaar  met  daarin  een toelichting op de totstandkoming van dit referentiemodel, een lijst van issues en besluiten daarover en de verschillen tussen het GFO Zaken en het RGBZ. 

Deze versie van het RGB Zaken is in september 2010 in de StUF-Regiegroep vastgesteld, tegelijk met de vaststelling van StUF-ZaKeN 3.10. 

8 

## **2. Afbakening** 

## **2.1. Relatie tot GEMMA** 

Door EGEM i-teams is begin 2009 de “GEMMA-procesarchitectuur” uitgebracht. De basisplaat zoals hieronder weergegeven toont de verschillende bouwstenen voor de dienstverleningsprocessen in samenhang. 

**==> picture [473 x 306] intentionally omitted <==**

Afbeelding 2: GEMMA-procesarchitectuur 

Het RGB Zaken richten we vooral op het, in het midden gevisualiseerde, Dienstverleningsmanagement: de rol die de verbindende schakel is tussen klantcontact (in verschillende kanalen) en behandelend of besluitend specialist en die de uitvoering van het dienstverleningsproces coördineert. Dit wil niet zeggen dat het RGBZ de rollen Klantcontact en Vakspecialist niet ondersteund. Integendeel, maar wel met de beperking dat het RGBZ niet gericht is op specifieke klantcontactinformatie en vakspecifieke informatie. Het RGBZ maakt het dus wel mogelijk dat de rollen Klantcontact, Vakspecialist en Dienstverleningsmanagement met elkaar communiceren over zaken, zowel binnengemeentelijk als met ketenpartners. Dit kan de indruk wekken dat we het RGBZ niet richten op de groep procesbouwstenen ‘Behandelen’. Dit is ten dele waar. Met het referentiemodel standaardiseren we wel de generieke gegevens over de behandeling van een zaak (zaakkenmerken, betrokkenen, documenten, voortgang) maar niet de vakspecifieke informatie. Deze verschilt immers per zaaktype. Evenmin modelleren we gegevens  die  wenselijk  zijn  voor  het  sturen  van  behandelaars  van  zaken  op  eenduidige afhandeling daarvan. Voor het model cq. de informatievoorziening over zaken is alleen de uitkomst van  deze  vorm  van  sturing  relevant..  Verder,  de procesarchitectuur  is  gericht op externe klanten van de gemeente (en daarmee samenwerkende organisaties). Het RGB Zaken richten we ook op interne klanten: medewerkers met een vraag die geclassificeerd wordt als 

9 

een verzoek om afhandeling van een zaak. Dat kan gaan van het verzoek tot opheffing van een computerstoring tot de vervaardiging van een bestemmingsplan. Eind 2009 bracht EGEM i-teams de GEMMA-informatie-architectuur uit. De onderstaande figuur visualiseert dit op hoofdlijnen. 

**==> picture [426 x 286] intentionally omitted <==**

Afbeelding 3: GEMMA-informatie-architectuur op hoofdlijnen 

Naar analogie van de bedrijfsarchitectuur richten we het RGB Zaken vooral op de twee midoffice-componenten Zakenbeheer en Beheer documentaire informatie. Dit wil niet zeggen dat het RGBZ niet ook gericht is op andere componenten. Dat is wel het geval zei het in generieke zin. 

Samengevat verwoorden we de gekozen afbakening als volgt: 

- Het adequaat kunnen informeren van betrokkenen bij, en geïnteresseerden in een zaak. Dit loopt  van  ex-  en  interne  initiatoren  van  een  zaak  via  medebehandelaars  daarvan  en belangstellenden in de publicatie van de zaak of het resultaat daarvan tot management dat behoefte heeft aan sturingsinformatie. 

- Het (ook achteraf) kunnen verantwoorden van de zaak, zowel inhoudelijk (is de zaak goed afgehandeld) als qua proces (is de zaak op de juiste wijze afgehandeld), en desgewenst kunnen reconstrueren van de (behandeling van de) zaak. 

Een andere belangrijke relatie binnen GEMMA is er met de GEMMA Zaaktypecatalogus. Waar het RGB Zaken de van zaaktypen uit te wisselen gegevens en hun semantiek specificeert, definieert de Zaaktypecatalogus de zaaktypen die in de gegevensuitwisseling betrokken kunnen zijn. 

Met  een  zaak  geeft de gemeente  invulling  aan  een  dienstverleningsproces.  Een  dergelijk proces heeft veelal betrekking op personen en/of objecten binnen het gemeentelijk grondgebied. Deze hebben we al eerder gemodelleerd in het Referentiemodel Stelsel van 

10 

Gemeentelijke Basisgegevens (RSGB). De relatie tussen beide referentiemodellen is dan ook evident.  Dit  visualiseren  we  in  onderstaande  figuur.  Kaderstellend  voor  de  gemeentelijke referentiemodellen zijn landelijke modellen, tot op heden, naast de NORA, alleen de catalogi van de landelijke basisregistraties. Binnen de gemeentelijke informatie-architectuur kennen we momenteel twee horizontale gegevensmodellen: het RSGB ('de  objecten  waarop de gemeentelijke taakuitoefening betrekking heeft') en het RGBZ ('de wijze waarop zij haar taken uitoefent met betrekking tot die objecten'). Deze modellen zijn op hun beurt kaderstellend voor eventuele verticale gegevensmodellen voor specifieke dienstverleningsprocessen of clusters daarvan. 

**==> picture [358 x 207] intentionally omitted <==**

Afbeelding 4: Gegevensmodellen in relatie tot elkaar 

## **2.2. Objectenmodel** 

In deze paragraaf lichten we het objectenmodel toe. Het model op hoofdlijnen is weergegeven in  de  samenvatting.  Op  de  laatste  pagina  van  deze  paragraaf  ziet  u  het  model  in  detail gevisualiseerd. 

We modelleren alleen de actuele situatie. De behoefte aan historie specificeren we met de desbetreffende metagegevens. 

## **Tekenwijze** 

**==> picture [329 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tekensymboliek<br>1:N-relatie<br>OBJECTTYPE A OBJECTTYPE B<br>objecttype van basisregistratie objecttype niet in landelijke basisregistratie<br>of-of-relatie<br>OBJECTTYPE C generalisatie ('groep') van meer objecttypen;<br>N:M-relatie 1 of meer van laatstgenoemde objecttypen<br>maakt deel uit van een basisregistratie<br>altijd voorko- mende relatie komende relatie niet altijd voor-<br>**----- End of picture text -----**<br>


We brengen een **Tekensymboliek** objecttype  in  beeld met een rechthoek. De  naam  van  het 1:N-relatie **OBJECTTYPE A OBJECTTYPE B** objecttype  is  in  de rechthoek  vermeld. objecttype van basisregistratie objecttype niet in landelijke basisregistratie In  een  oranje  vlak staan de of-of-relatie objecttypen die deel uitmaken van enige **OBJECTTYPE C** generalisatie ('groep') van meer objecttypen; (catalogus van een) N:M-relatie 1 of meer van laatstgenoemde objecttypen maakt deel uit van een basisregistratie basisregistratie  (A). EGEM heeft de andere objecttypen toegevoegd. Een witte rechthoek visualiseert een objecttype 

11 

dat uit meerdere andere objecttypen is samengesteld. Dit is een zogenaamde generalisatie van objecttypen. Laatstgenoemde objecttypen zijn op hun beurt specialisaties van het gegeneraliseerde objecttype. Een gegeneraliseerd objecttype heeft een ‘vet’ kader (C) als één of  meer  van  de  specialisaties  daarvan  deel  uitmaken  van  enige  (catalogus  van  een) basisregistratie. In een blauw vlak staan de objecttypen die geen generalisaties zijn van andere objecttypen en geen deel uitmaken van enige (catalogus van een) basisregistratie (B). 

Tussen de objecttypen brengen we de drie soorten relaties als volgt in beeld: een 1:1-relatie (een lijn), een 1:N-relatie (een lijn met één ‘harkje’) en een N:M-relatie (een lijn met twee ‘harkjes’). Een relatie die deel uitmaakt van enige (catalogus van een) basisregistratie is ‘vetter’ gevisualiseerd dan relaties waarvoor dit niet geldt: de relaties die KING heeft toegevoegd. Een relatie veronderstelt dat een object van het ene objecttype altijd gerelateerd is aan dat van het andere objecttype. Wanneer dit niet het geval hoeft te zijn, dan ziet u dat aan het open rondje aan het uiteinde van de relatie(lijn). In het voorbeeld: een object van objecttype B is altijd gerelateerd aan een object van objecttype A, maar andersom hoeft dat niet het geval te zijn. Met een of-of-relatie tenslotte bedoelen we dat een object van – in dit geval – objecttype C een relatie kent met een object van één van beide gerelateerde objecttypen, hier objecttype A of B. 

## **Toelichting** 

Centraal in het referentiemodel staat het begrip ZAAK. Een ZAAK is “een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moet worden”. Een ZAAK  zoals  deze  door een initiator is ‘aangevraagd’, behandelen we desgewenst als meerdere min of meer onafhankelijke ‘deelzaken’. Elke deelzaak is op zich weer een ZAAK. Deze relateren we aan de ‘hoofdzaak’: de ZAAK zoals die geïnitieerd is. 

Kenmerken van groepen vergelijkbare zaken leggen we vast met het ZAAKTYPE. 

Elke zaak heeft ‘ergens betrekking op’. Dit modelleren we met de relatie naar OBJECT via ZAAKOBJECT als het een object van een type uit het RSGB of RGBZ betreft. Zo niet, dan leggen we dit vast met zaakgegevens. Soms heeft de ene zaak betrekking op een andere zaak, wat we modelleren met de relatie ‘ZAAK betreft andere ZAAK’. Denk bijvoorbeeld aan een bezwaar of beroep dat naar aanleiding van een beschikking wordt ingediend en dat als een separate zaak wordt afgehandeld. 

Een ZAAK wordt geïnitieerd door een BETROKKENE. Dit kan een externe persoon of bedrijf zijn: NATUURLIJK PERSOON, NIET NATUURLIJK PERSOON of VESTIGING. Ook kan het initiatief voor de ZAAK binnen de zaakbehandelende organisatie(s) liggen: ORGANISATORISCHE  EENHEID  of  MEDEWERKER.  De  belangrijkste  ROL  van  beide laatstgenoemde  objecttypen  is  evenwel  het  behandelen  van  zaken.  Met  de  relatie  van ORGANISATORISCHE EENHEID naar VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE geven we aan op welke locatie de ORGANISATORISCHE EENHEID van de zaakbehandelende organisatie haar activiteiten uitoefent. 

Het initiëren van zaken is één van de ROLlen van een BETROKKENE. In het algemeen betreft ROL de taken, rechten en/of verplichtingen die een specifieke BETROKKENE heeft ten aanzien van een specifieke ZAAK. 

Een zaak doorloopt een aantal STATUSsen. Een STATUS geeft aan in welke toestand een zaak zich bevindt. De STATUS maakt het mogelijk de voortgang van de zaak op hoofdlijnen te volgen. Wat de hoofdlijnen zijn wordt in belangrijke mate bepaald vanuit de belangen van de initiator van de zaak. Deze is veelal geïnteresseerd in mijlpalen, niet in de diverse stappen die 

12 

de behandelende organisatie(s) moet zetten om de zaak af te handelen. Daarnaast kan de STATUS gebruikt worden voor het genereren van management informatie. 

Een  zaak  heeft in de loop  van  de tijd meerdere statussen: de achtereenvolgens  bereikte mijlpalen. De STATUS is niet bedoeld om de behandeling van de zaak te plannen. Deze planning volgt uit de STATUSTYPE bij de ZAAK. 

Een STATUS wordt altijd gezet door een BETROKKENE in zijn of haar ROL bij de ZAAK. DOCUMENTen die relevant zijn voor het bereiken van een STATUS of voor de communicatie over die STATUS, kunnen aan die STATUS gerelateerd worden. 

De uitkomst van de zaak kan bij de zaak zelf worden vastgelegd. Mogelijke uitkomsten zijn dat de aanvraag is toegekend, dat de zaak is ingetrokken door de aanvrager of dat de zaak niet ontvankelijk is verklaard. Een zaak leidt in veel gevallen tot één of meer BESLUITen. Kenmerken van groepen vergelijkbare BESLUITen  leggen we vast met het BESLUITTYPE. Een besluit wordt veelal schriftelijk vastgelegd maar dit is niet noodzakelijk. Vandaar de optionele relatie naar DOCUMENT. 

Vormt een besluit veelal het eind van een zaak, een ander document vormt de start van een zaak. Meerdere documenten kunnen gedurende de behandeling relevant zijn voor een zaak. Omgekeerd kan een document relevant zijn voor meerdere zaken. De relatie tussen ZAAK en DOCUMENT modelleren we dan ook via ZAAKDOCUMENT. 

In veel gevallen zal een ontvangen of gecreëerd document ook daadwerkelijk als één (fysiek) document beschouwd worden: het ENKELVOUDIG DOCUMENT. Evenwel, een document dat door bijvoorbeeld de initiator van een zaak als één document wordt beschouwd, kan feitelijk uit meerdere  documenten  bestaan,  bijvoorbeeld  omdat  het  formaat  (.pdf,  .odt.  CAD-file  e.d.) verschilt of omdat de zaakbehandelende organisatie hoofdrapport en bijlagen ieder apart als ENKELVOUDIG  DOCUMENT  wil  beschouwen.  Een  dergelijke  groep  bij  elkaar  behorende documenten beschouwen we tevens als een document en modelleren we als SAMENGESTELD  DOCUMENT.  Het  objecttype  DOCUMENT is  aldus  telkens  of  een ENKELVOUDIG DOCUMENT (E D in het schema) of een SAMENGESTELD DOCUMENT (S D in  het  schema)  waarbij  de  laatstgenoemde  bestaat  uit  twee  of  meer  ENKELVOUDIGe DOCUMENTen. 

Kenmerken van groepen vergelijkbare DOCUMENTen leggen we vast met het DOCUMENTTYPE. 

13 

## **Referentiem odel Gem eentelijke Basisgegevens Zaken in schem a** 

**==> picture [407 x 391] intentionally omitted <==**

**----- Start of picture text -----**<br>
BETRO KKENE<br>SUBJECT<br>OBJECT<br>RECHTS-PERSOO N<br>NATUURLIJK<br>PERSOO N<br>betreft<br>NIET- andere<br>NATUURLIJK  hoort bij<br>PERSOO N ZAAKO BJECT ZAAK ZAAKDOCUM ENT<br>heeft<br>VESTIGING<br>VZO<br>oefent uit<br>DO CUMENT<br>ROL<br>EDC SDC<br>ORG ANISA-<br>TO RISCHE EENHEID<br>STATUS BESLUIT<br>M EDEW ERKER<br>hoort bij<br>STATUSTYPE ZAAKTYPE BESLUITTYPE DO CUM ENTTYPE<br>is verantwoordelijke voor<br>is is deelzaak van<br>is<br>betreft<br>heeft<br>kan leiden tot<br>zet<br>huisvest is van is relevant voor<br>zet kan vast- gelegd zijn als<br>is van<br>hoort bij is verant- oordelijk voor w Is contact- persoon voor is van is van<br>**----- End of picture text -----**<br>


14 

## **3. De soorten van objecten van registratie** 

In dit hoofdstuk specificeren we de onderscheiden objecttypen op dezelfde wijze als in het RSGB. De objecttypen worden naar de volgende aspecten gespecificeerd. 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

De naam van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende  basisregistratie  dan  wel,  indien  het  een  door  KING toegevoegd objecttype betreft, de door KING vastgestelde naam van het objecttype. 

De in StUF-BG gehanteerde afkorting voor de naam van het objecttype. Objecttypen met een mnemonic tussen (haakjes) worden (nog) niet als zelfstandige entiteit in StUF-BG gebruikt. 

De basisregistratie in wiens catalogus  het objecttype  is gespecificeerd (oftewel  de  basisregistratie  waar  het  objecttype  deel  van  uitmaakt). Deze specificatie  is toegevoegd t.o.v. de basisregistratie-catalogus aangezien het hier niet om een basisregistratie gaat maar wel duidelijk moet zijn in welke basisregistratie het objecttype voorkomt (indien van toepassing). 

- **(Code objecttype)** De  door  de  desbetreffende  basisregistratiehouder  aan  het  objecttype toegekende uniek code. Deze wordt hier niet vermeld aangezien deze gespecificeerd  is  in  de  desbetreffende  catalogus.  Voor  door  KING toegevoegde objecttypen is vooralsnog afgezien van het specificeren van deze code. 

- **(Afkorting objecttype)** 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

- **Datum opname objecttype** 

**Toelichting objecttype** 

- **(Relatie met semantische kern)** 

- De door de desbetreffende basisregistratiehouder gehanteerde afkorting van de naam van het objecttype. Deze wordt hier niet vermeld aangezien deze gespecificeerd is in de desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van het specificeren van deze afkorting. 

De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegd objecttype betreft, de door KING vastgestelde definitie van het objecttype. 

Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd objecttype betreft. 

De datum waarop het objecttype is opgenomen in het RSGB. 

Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de daarin  opgenomen  toelichting.  De  toelichting  wordt  dan  ook  alleen gegeven indien het een door KING toegevoegd objecttype betreft dan wel indien  een  toelichting  nodig  is,  aanvullend  op  de  toelichting  in  de desbetreffende catalogus. 

De door de desbetreffende basisregistratiehouder gehanteerde beschrijving van de wijze waarop het objecttype in relatie staat tot de semantische kern van het stelsel van basisregistraties. Deze wordt hier niet  vermeld  aangezien  deze  gespecificeerd  is  in  de  desbetreffende catalogus.  Voor  door  KING  toegevoegde  objecttypen  is  vooralsnog afgezien van het specificeren van deze relatie. 

15 

## **Unieke aanduiding objecttype** 

## **(Identificatie objecttype)** 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de wijze  waarop  daarin voorkomende  objecten  (van dit type) uniek in de registratie  worden  aangeduid.  Deze  aanduiding  wordt  dan  ook  alleen vermeld indien het een door KING toegevoegd objecttype betreft. 

De door de desbetreffende basisregistratiehouder gehanteerde vermelding door middel van welke aan het object zelf waarneembare eigenschappen deze uniek kan  worden  aangeduid  (‘wanneer  is  sprake  van  één exemplaar?’). Deze wordt hier niet vermeld aangezien deze gespecificeerd is in  de  desbetreffende catalogus. Voor door KING toegevoegde objecttypen is vooralsnog afgezien van deze vermelding. 

Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende basisregistratie voorhanden zijn. Deze beschrijving wordt dan ook alleen gegeven indien het een door KING toegevoegd objecttype betreft. 

Voor objecttypen die deel uitmaken van een basisregistratie betreft dit de waarborgen voor de juistheid van de in de registratie opgenomen objecten van  het  desbetreffende  type. Deze  beschrijving  wordt dan  ook  alleen gegeven indien het een door KING toegevoegd objecttype betreft. 

_Code Gegevensnaam Herkomst_ 

Hier  worden  de  attribuutsoorten  gespecificeerd  die  behoren  tot  het desbetreffende objecttype. In afwijking van hetgeen in de basisregistratiecatalogi gebruikelijk is, worden de attribuutsoorten gespecificeerd van het objecttype  en niet van  een  daarop te baseren bericht. ‘Relatie-attribuutsoorten’ komen dan ook niet voor; de desbetreffende relaties worden onder de attribuutsoorten gespecificeerd. Attribuutsoorten kunnen deel uit maken van een zgn. attribuutgroep. De tot een dergelijke groep behorende attribuutsoorten zijn inspringend vermeld. Een attribuutsoort kan gespecificeerd zijn bij het desbetreffende objecttype in de desbetreffende catalogus dan wel door KING toegevoegd zijn. In het eerste geval is de attribuutsoortcode opgenomen, voor zover dit gespecificeerd is in de desbetreffende catalogus. In de kolom ‘Herkomst’ is aangegeven in welke basisregistratiecatalogus dit attribuutsoort is gespecificeerd (indien van toepassing). Indien hier een basisregistratiecatalogus vermeld wordt terwijl het objecttype niet afkomstig is van dezelfde basisregistratie, dan betreft het een generalisatie van andere objecttypen en  is de attribuutsoort van toepassing op alle laatstgenoemde objecttypen (de zgn. specialisaties waaronder het objecttype  in  de  basisregistratie  waarbij  de  attribuutsoort  hoort)  en derhalve bij het eerstgenoemde objecttype (de generalisatie van de andere objecttypen) gemodelleerd. 

Een  bijzondere  situatie  doet  zich  voor  indien  het  objecttype een generalisatie is van andere objecttypen dan wel dat het een specialisatie betreft  van  een  ander  objecttype.   Bij  het  eerstgenoemde  objecttype worden de attribuutsoorten gespecificeerd die van toepassing zijn op alle specialisaties daarvan. Bij het andere objecttype worden om redenen van semantiek  cq.  leesbaarheid  tevens  genoemd  de  attribuutsoorten  die behoren tot de generalisatie van dit objecttype. 

De attribuutsoorten worden nader gespecificeerd in hoofdstuk 2. 

16 

## **Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype Herkomst_ In  afwijking  van  hetgeen  in  de  basisregistratiecatalogi  gebruikelijk  is, worden hier de relaties gespecificeerd die het desbetreffende objecttype heeft  met  andere  objecttypen.  Naar  analogie  van  de  specificatie  van attribuutsoorten  worden  bij  specialisaties  van  objecttypen  tevens  de relaties genoemd die behoren tot de generalisatie van dit objecttype. De relatiesoorten worden nader gespecificeerd in hoofdstuk 2. 

De tussen haken vermelde specificaties zijn derhalve niet opgenomen. Bij een objecttype dat deel  uit  maakt  van  een  basisregistratie  worden  slechts  een  beperkt  aantal  specificaties opgenomen met het oog op de onderhoudbaarheid van het model. Voor de niet vermelde specificaties wordt verwezen naar de specificatie van het objecttype in de catalogus van de desbetreffende basisregistratie. 

17 

## **3.1. Besluit** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

**Datum opname objecttype** 

**Toelichting objecttype** 

## BESLUIT 

## BSL 

## KING 

Een  na  overweging  of beraadslaging  vastgestelde  beslissing   voor  een individueel of concreet geval. 

KING op basis van de BESCHIKKING in het GFO Zaken 

## 1 juni 2008 

In het GFO Zaken kwam het objecttype BESCHIKKING voor. Aangezien dit een deelverzameling is van BESLUIT en er ook andere besluiten zijn dan beschikkingen, hanteren we hier de term ‘besluit’. Het gaat hierbij niet alleen om  besluiten  van  bestuursorganen,  inhoudende  een  publiekrechtelijke rechtshandeling, maar ook om andere besluiten, zoals bijvoorbeeld genomen op interne zaken. 

Een besluit wordt veelal schriftelijk vastgelegd maar dit is niet noodzakelijk. Omgekeerd kan het voorkomen dat in een DOCUMENT meerdere besluiten vastgelegd zijn.Vandaar de N:M-relatie naar DOCUMENT. Een besluit komt wel altijd voort uit een zaak. 

Indien  een  BESLUIT  een  beschikking  betreft,  is  er  sprake  van  een beschikkinghouder, bijvoorbeeld degene aan wie de vergunning verleend is. Dit is één van de betrokkkenen met een van toepassing zijnde rol bij de zaak waartoe het besluit behoort. 

## **Unieke aanduiding objecttype** 

**Populatie objecttype** 

## Besluitidentificatie 

Alle  besluiten  die  het  (tussen)resultaat  zijn  van  zaken  waarvoor  de zaakbehandelende organisatie(s) het zaakgericht werken heeft ingericht. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

_Code Gegevensnaam Herkomst_ 0014 Besluitidentificatie GFO Zaken 0004 Besluitdatum GFO Zaken 0003 Besluittoelichting GFO Zaken 0008 Ingangsdatum GFO Zaken 0009 Vervaldatum GFO Zaken Vervalreden KING 0013 Publicatiedatum GFO Zaken 0015 Verzenddatum GFO Zaken Uiterlijke reactiedatum KING _Relatienaam incl. gerelateerd objecttype Herkomst_ is uitkomst van ZAAK GFO Zaken kan vastgelegd zijn als DOCUMENT KING is van BESLUITTYPE KING 

18 

## **3.2. Besluittype** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

**Unieke aanduiding objecttype Populatie objecttype** 

## BESLUITTYPE 

## BST 

KING 

Generieke aanduiding van de aard van een besluit 

## KING 

## 1 juni 2008 

Het betreft de indeling of groepering van besluiten naar hun aard, zoals bouwvergunning, ontheffing geluidhinder en monumentensubsidie Besluittype-omschrijving 

Alle besluittypen van de besluiten die het resultaat kunnen zijn van het zaakgericht werken van de behandelende organisatie(s). 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|0002|Besluittype-omschrijving|GFO Zaken|
||Besluittype-omschrijving generiek|KING|
||Besluitcategorie|KING|
||Reactietermijn|KING|
||Publicatie-indicatie|KING|
||Publicatietekst|KING|
||Publicatietermijn|KING|
||Datum begin geldigheid besluittype|KING|
||Datum einde geldigheid besluittype|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|heeft|BESLUITen|KING|



19 

## **3.3. Betrokkene** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

**Definitie objecttype** 

## **Herkomst definitie objecttype** 

**Datum opname objecttype** 

## **Toelichting objecttype** 

## BETROKKENE 

## BTR 

## KING 

Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK. 

## KING 

## 1 juni 2008 

Het gaat hier om de  verzameling  van  mogelijke  betrokkenen  bij  zaken: natuurlijke personen  in  hun  hoedanigheid  als burger  dwz. niet  als medewerker van de zaakbehandelende organisatie(s), niet-natuurlijke personen, vestigingen (van maatschappelijke activiteiten van natuurlijke en niet-natuurlijke personen) waaronder de vestigingen van de zaakbehandelende organisatie(s), organisatorische eenheden van de zaakbehandelende organisatie(s) en medewerkers binnen die organisatorische eenheden. 

Grofweg bestaat dit uit twee groepen: enerzijds burgers en bedrijven die zaken  initieren  en  belanghebbende  zijn  bij  zaken  en  anderzijds  de organisatoriische  eenheden  en  medewerkers  van  de  zaakbehandelende organisatie(s). Evenwel, ook een medewerker van de zaakbehandelende organisatie(s) kan een zaak initieren, met name als het gaat om ‘interne’ zaken zoals bijvoorbeeld het opstellen van een bestemmingsplan. 

Indien  een  medewerker  van  een  vestiging  (van  een  maatschappelijke activiteit) die geen deel uit maakt van een zaakbehandelende organisatie, een zaak initieert (bijvoorbeeld een medewerker van een willekeurig bedrijf die een vergunning aanvraagt) dan is de betrokkene die vestiging, dus niet de  medewerker  daarvan.  Desbetreffende  medewerkergegevens  kunnen eventuieel wel geregistreerd worden als contactgegevens bij de rol die die vestiging speelt in die zaak. 

BETROKKENE heeft zelf amper attribuutsoorten, alleen afgeleide attribuutsoorten  voor  het  zoeken  van  betrokkenen.  De  attribuutsoorten bevinden zich vooral bij de specialisaties van het objecttype (‘subtypes’ zoals NATUURLIJK PERSOON). Deze werken we hieronder, in deze paragraaf, uit voor wat betreft de aan het RSGB ontleende objecttypen. 

NB. De betrokkene kwam ook voor in het GFO Zaken 2004 maar had daar een andere betekenis. Alleen de naam is overgenomen. 

## **Unieke aanduiding objecttype** 

Zie de unieke aanduidingen van de specialisaties die van dit objecttype deel uit maken. 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

_Code Gegevensnaam_ Naam Identificatie Adres binnenland 

_Herkomst_ 

20 

## Adres buitenland 

## **Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype_ oefent uit ROL 

_Herkomst_ KING 

## **Objecttype: NATUURLIJK PERSOON** 

## **Naam objecttype** 

## NATUURLIJK PERSOON 

**Herkomst objecttype Toelichting objecttype** 

## **Overzicht attributen** 

## RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een NATUURLIJK PERSOON die in het RGBZ gebruikt worden. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ INGESCHREVEN PERSOON . Burgerservicenummer ANDER NATUURLIJK PERSOON .  Nummer ander natuurlijk persoon INGESCHREVEN PERSOON . Verblijfsplaats ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode INGESCHREVEN PERSOON . Locatiebeschrijving WOONPLAATS . Woonplaatsnaam Voornamen Adellijke titel/predikaat ACADEMISCHE TITEL . Academische titelcode Voorvoegsels geslachtsnaam Geslachtsnaam Geslachtsaanduiding Aanduiding naamgebruik Geboortedatum Naam aanschrijving Aanhef aanschrijving Voorletters aanschrijving Voornamen aanschrijving Geslachtsnaam aanschrijving Overlijdensdatum SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING 

ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

21 

SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam SUBJECT . Telefoonnummer SUBJECT . Fax-nummer SUBJECT . Emailadres SUBJECT . Bank/girorekeningnummer SUBJECT . Subjecttypering 

## **Objecttype: NIET-NATUURLIJK PERSOON** 

**Naam objecttype** 

NIET-NATUURLIJK PERSOON 

**Herkomst objecttype Toelichting objecttype** 

## **Overzicht attributen** 

RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een NIET-NATUURLIJK PERSOON die in het RGBZ gebruikt worden. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ NNP-ID ANDER BUITENLANDS NIET-NATUURLIJK PERSOON .  Nummer ander buitenlands niet-natuurlijk persoon (Statutaire) Naam Datum aanvang Datum beëindiging SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 

22 

Adres buitenland 3 Land . Landnaam SUBJECT . Telefoonnummer SUBJECT . Fax-nummer SUBJECT . Emailadres SUBJECT . Bank/girorekeningnummer SUBJECT . Subjecttypering 

## **Objecttype: VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE** 

**Naam objecttype** 

VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE 

**Mnemonic objecttype Herkomst objecttype** 

VZO 

KING 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

Een  VESTIGING van  een  onderneming  of  rechtspersoon  zijnde  de zaakbehandelende organisatie. 

KING 

**Datum opname objecttype** 

17 mei 2010 

**Toelichting objecttype** 

Deze specialisatie ('subtype') van VESTIGING is opgenomen om binnen vestigingen onderscheid te kunnen maken tussen vestigingen van organisaties die zaken behandelen en vestigingen van andere organisaties. Alleen van vestigingen van zaakbehandelende organisaties leggen we de relatie naar organisatorische eenheden (en medewerkers) om op die manier uit te kunnen wisselen op welke locatie een organisatorische eenheid van een zaakbehandelende organisatie haar taken uitoefent. 

De specialisatie overerft alle attribuutsoorten en relatiesoorten van VESTIGING en kent zelf slechts één relatiesoort. 

Hieronder benoemen we de aan het RSGB ontleende gegevens  van een VESTIGING  zoals  die  in  het  RGBZ  gebruikt  worden.  Zie  voor  de specificaties van deze gegevens het RSGB. 

**Unieke aanduiding objecttype** 

**Populatie objecttype** 

SUBJECT.Subjecttypering gevolgd door het Vestigingsnummer 

De vestigingen van de organisatie die de zaken behandelt  en waarbinnen één  of  meer  organisatorische  eenheden  hun  activiteiten  uitvoeren  en betrokken zijn of waren bij één of meer zaken. 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

Code Gegevensnaam Herkomst Vestigingsnummer Handelsnaam Verkorte naam Datum aanvang Datum beëindiging 

Heeft als locatie-adres ADRESSEERBAAR OBJECTAANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

23 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam SUBJECT . Telefoonnummer SUBJECT . Fax-nummer SUBJECT . Emailadres SUBJECT . Bank/girorekeningnummer SUBJECT . Subjecttypering 

## **Overzicht relaties** 

_Relatienaam incl. gerelateerd objecttype_ huisvest ORGANISATORISCHE EENHEID 

_Herkomst_ KING 

24 

## **3.4. Document** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## DOCUMENT 

## DOC 

## KING 

Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon  bij  de  uitvoering  van  taken,  zijnde  een  ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT. 

KING, op basis van NEN 2082 

## 1 juni 2008 

Een document kan van alles zijn, ongeacht aard en vorm: een tekstverwerkingsdocument, een papieren brief, een webpagina, een landkaart, een foto, een geluidsopname, een dataset, een blog, etcetera. En ook een digitaal ontvangen of gecreeerd document dat bestaat uit meerdere fysieke documeten, zoals een aanvraag (als tekstdocument) met bijbehorende tekening (CAD-formaat) en berekening (spreadsheet) of een e- mail met bijlage(n). Net zoals dezelfde aanvraag op papier met bijlagen als één  document   beschouwd  kan  worden. De  fysieke  vorm  van  hetgeen ontvangen of gecreeerd is, is dus niet (alleen) bepalend voor de afbakening van dat wat als document beschouwd wordt. 

|ENKELVOUDIG<br>DOCUMENT|DOCUMENT<br>SAMENGESTELD<br>DOCUMENT<br>maakt<br>deel uit<br>~~van~~|
|---|---|



Een  document dat door bijvoorbeeld  de  initiator  van  een  zaak  als  één document wordt beschouwd, kan fysiek uit meerdere documenten bestaan. Een  dergelijke groep  documenten  kan  beschouwd worden als één document. Gezien de definitie kan er immers sprake zijn van het 'geheel van gegevens met een eigen identiteit' waarbij alleen de vorm er toe heeft geleid dat er drie fysieke documenten zijn ontvangen (tekstverwerkingsdocument, CAD-file en rekenblad). Evenzogoed zouden we het ontvangen materiaal kunnen beschouwen als drie afzonderlijke documenten. Ook kan het zijn dat een document dat fysiek dezelfde vorm heeft toch beschouwd wordt als bestaande  uit  meerdere  documenten,  bijvoorbeeld  een  document  met omvangrijke  bijlagen,  omdat  dit  beter  aansluit  bij  het  gebruik  er  van. Organisaties  gaan  hier  verschillend  mee  om.  Om  in  te  spelen  op  de verschillende beschouwingswijzen hebben we DOCUMENT zodanig gemodelleerd  dat  dit  dan  wel  een  zelfstandig  (fysiek)  document is,  het ENKELVOUDIG DOCUMENT, dan wel een groep van bij elkaar horende documenten, passend binnen de definitie, het SAMENGESTELD DOCUMENT. Een SAMENGESTELD DOCUMENT bestaat telkens uit twee of meer ENKELVOUDIGE DOCUMENTEN.  Organisaties  kunnen er voor kiezen alleen de eerste mogelijkheid, het DOCUMENT als ENKELVOUDIG DOCUMENT te implementeren. Wel moeten zij er mee rekening houden dat zij  van  andere  organisaties,  via  geautomatiseerde  berichtenuitwisseling, samengestelde documenten 'aangereikt' krijgen en deze transformeren tot enkelvoudige documenten. 

25 

DOCUMENT heeft een N:M-relatie naar ZAAK waarmee we aangeven dat een document relevant kan zijn voor meer dan één zaak. Dit modelleren we via het objecttype ZAAKDOCUMENT. Dit is bijvoorbeeld het geval bij zgn. samengestelde  brieven:  één  brief  waarin  meerdere  zaken  aanhangig gemaakt worden zoals een verzoek en een klacht. 

Door documenten te registreren en aan een zaak te relateren wordt het archief bij/van de zaak opgebouwd; alle documenten bij een zaak vormen tezamen met de zaakkenmerken het zaakdossier. Het zaakdossier modelleren we dus niet als apart objecttype. Evenmin modelleren we een zgn.  objectdossier.  Dit  betreft  immers  alle  zaken,  met  bijbehorende kenmerken  en  documenten,  eventueel  van  bepaalde  zaaktypen,  die gerelateerd zijn aan een bepaald OBJECT. 

We hebben er voor gekozen om documenten niet te modelleren indien zij niet  aan  een  zaak  gekoppeld  worden  d.w.z.  niet  tot  een  zaak  leiden. Dergelijke documenten zijn klaarblijkelijk zodanig onbelangrijk dat zij niet archiefwaardig zijn d.w.z. niet bewaard hoeven te worden om te voldoen aan wettelijke en/of administratieve eisen en/of maatschappelijke behoeften. Een document zoals hier bedoeld wordt een archiefstuk (in het engels 'record') zo gauw de zaakkenmerken aangeven dat alle daaraan gekoppelde documenten gearchiveerd dienen te zijn. 

## **Unieke aanduiding objecttype** Documentidentificatie 

## **Populatie objecttype** 

Alle documenten die op enigerlei wijze relevant zijn voor het tot een goed einde brengen van een zaak. Een document is in dit kader relevant indien: 

- het  door  een  behandelaar  van  de  zaak  gedeeld  wordt  met  andere betrokkenen  bij  de  zaak (de  ondergrens; een  document  wat het persoonlijke domein van de behandelaar van een zaak niet verlaat wordt in dit kader niet relevant geacht), 

- het van belang is voor voor de inhoudelijke verantwoording (is de zaak goed afgehandeld), procesverantwoording (is de zaak op de juiste wijze afgehandeld) en/of reconstructie van de zaak, en/of 

- bewaard moet worden om te voldoen aan wettelijke en/of administratieve eisen en/of maatschappelijke behoeften. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Documentidentificatie|Dublin Core|
||Documentcreatiedatum|Dublin Core|
||Documentontvangstdatum|KING|
||Documenttitel|Dublin Core|
||Documentbeschrijving|Dublin Core|
||Document verzenddatum|KING|
||Vertrouwelijkaanduiding|KING|
||Documentauteur|Dublin Core|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|is van|DOCUMENTTYPE|KING|
|betreft|ZAAKDOCUMENTen|KING|
|kan vastlegging zijn van BESLUITen||KING|



26 

## **3.5. Documenttype** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

## **Unieke aanduiding objecttype** 

## DOCUMENTTYPE 

## DCT 

## KING 

Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie 

## KING 

## 1 juni 2008 

Het betreft de typering van documenten naar hun aard zoals gehanteerd door de zaakbehandelende organisatie. Elk documentype komt overeen met of  valt  binnen  de  generieke  typering  van  documenten  zoals  landelijk gehanteerd, de  Documenttype-omschrijving generiek  . Het documenttype stelt organisatie in staat hun eigen typering aan te houden en, d.m.v. de relatie naar documenttype-omschrijving generiek, toch aan te kunnen sluiten op de landelijk gehanteerde typering generiek. 

Documenttype-omschrijving 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Documenttype-omschrijving|Dublin Core|
||Documenttype-omschrijving generiek|KING|
||Documentcategorie|Dublin Core|
||Documenttypetrefwoord|KING|
||Datum begin geldigheid documenttype|KING|
||Datum einde geldigheid documenttype|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|Heeft|DOCUMENTen|KING|



27 

## **3.6. Enkelvoudig document** 

**Naam objecttype** 

ENKELVOUDIG DOCUMENT 

**Mnemonic objecttype** 

## EDC 

**Herkomst objecttype** 

KING 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren. 

KING 

**Datum opname objecttype** 

## 1 oktober 2009 

**Toelichting objecttype** 

Een ENKELVOUDIG DOCUMENT is een specialisatie van DOCUMENT. Zie de toelichting bij dat objecttype. Bij de definitie is gebruik gemaakt van de beschrijving van 'component' in de MoReq2 (2008). In de dagelijkse praktijk staat 'enkelvoudig document' momenteel synoniem met 'document'. 

Het ENKELVOUDIG DOCUMENT kan deel uit maken van een SAMENGESTELD DOCUMENT, bijvoorbeeld omdat zich in dat samengesteld  document  andere  documenten  bevinden  met  een  ander bestandsformaat, vanwege de omvang van dat samengesteld document of omdat behandeling daartoe aanleiding geeft. 

Een ENKELVOUDIG DOCUMENT dat deel uit maakt van een SAMENGESTELD DOCUMENT kan aan andere ZAAKen gerelateerd zijn dan de ZAAK waaraan dat SAMENGESTELD DOCUMENT gerelateerd is, veelal omdat dat ENKELVOUDIG DOCUMENT relevant is voor meerdere ZAAKen. 

Documenten, vooral  die  van de  zaakbehandelende organisatie, worden soms gewijzigd of in opeenvolgende conceptversies vervaardigd. Het is uit oogpunt van  verantwoording  van  belang  de diverse  documentversies  te kennen. Hiertoe is bij de meeste van de attribuuttypen van ENKELVOUDIG DOCUMENT zowel materiële als formele historie als ‘Ja’ gedeclareerd. Dit impliceert dat voor deze attributen de waarden in de diverse versies van een enkelvoudig document opgevraagd kunnen worden. 

## **Unieke aanduiding objecttype** 

## DOCUMENT.Documentidentificatie 

**Populatie objecttype Kwaliteitsbegrip objecttype** 

Zie DOCUMENT 

**Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Documentformaat|Dublin Core|
||Documenttaal|Dublin Core|
||Documentversie|KING|
||Documentstatus|KING|
||Documentinhoud|KING|
||Documentlink|KING|
||Bestandsnaam|KING|
|Attributen van de generalisatie DOCUMENT:|||
||Documentidentificatie|Dublin Core|
||Documentcreatiedatum|Dublin Core|
||Documentontvangstdatum|KING|
||Documenttitel|Dublin Core|
||Documentbeschrijving|Dublin Core|



28 

||Document verzenddatum|KING|
|---|---|---|
||Vertrouwelijkaanduiding|KING|
||Documentauteur|Dublin Core|
|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
||maakt deel uit van SAMENGESTELD DOCUMENT|KING|
||Relaties van de generalisatie DOCUMENT:||
||is van DOCUMENTTYPE|KING|
||betreft ZAAKDOCUMENTen|KING|
||kan vastlegging zijn van BESLUITen|KING|



29 

## **3.7. Medewerker** 

## **Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## MEDEWERKER 

## MDW 

GFO Zaken 2004 

Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID. 

KING op basis van het GFO Zaken 2004 

## 1 juni 2008 

Alleen medewerkers van organisatorische eenheden van de organisatie(s) die zaken behandelen, worden hier bedoeld. Dus niet medewerkers van andere organisaties zoals de externe initiatoren van zaken. Overigens kan een dergelijke medewerker wel (interne) zaken initiëren. 

We beperken ons tot het aangeven welke medewerker betrokken is bij een zaak en welke gegevens van die medewerker vanuit het oogpunt van een zaak relevant zijn. 

In de hier toegepaste modellering heeft een medewerker slechts één functie en behoort hij/zij bij slechts één organisatorische eenheid. Dat betekent dat een medewerker die meerdere functies heeft en/of voor of bij meer dan één organisatorische eenheid werkt, meerdere keren kan voorkomen, met op onderdelen verschillende gegevenswaarden, zoals functie. 

MEDEWERKER is een specialisatie ('subtype') van BETROKKENE. 

**Unieke aanduiding objecttype** 

## **Populatie objecttype** 

Medewerkeridentificatie 

Alle medewerkers van organisatorische eenheden (van de zaakbehandelende  organisatie(s))  die  een  rol  kunnen  spelen  bij  de behandeling van geimplementeerde zaaktypen. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|0001|Medewerkeridentificatie|GFO Zaken|
|0003|Achternaam|GFO Zaken|
|0006|Datum uit dienst|GFO Zaken|
|9516|E-mailadres|GFO Zaken|
|0002|Functie|GFO Zaken|
|0410|Geslachtsaanduiding|GFO Zaken|
|0007|Medewerkertoelichting|GFO Zaken|
|0005|Roepnaam|GFO Zaken|
|9580|Telefoonnummer|GFO Zaken|
|0211|Voorletters|GFO Zaken|
|0004|Voorvoegsel achternaam|GFO Zaken|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|hoort bij|ORGANISATORISCHE EENHEID|GFO Zaken|
|is verantwoordelijk voor ORGANISATORISCHE EENHEID||GFO Zaken|
|is contactpersoon voor ORGANISATORISCHE EENHEID||GFO Zaken|
|is verantwoordelijke voor ZAAKTYPE||KING/GFO|



Relatiesoorten van de generalisatie BETROKKENE: 

30 

oefent uit ROL 

KING 

31 

## **3.8. Object** 

## **Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

## OBJECT 

## OBJ 

## KING 

Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen. KING 

## 22 mei 2009 

Een zaak kan op ‘van alles en nog wat’ betrekking hebben. Voor zover dit voorkomens  (objecten)  van  de  in  het  RSGB  of  RGBZ  onderscheiden objecttypen betreft, worden deze met OBJECT gemodelleerd en door middel van ZAAKOBJECT aan een zaak gerelateerd. Het OBJECT kent dan ook bijna evenzovele specialisaties (‘subtypen’) als dat er objecttypen in het RSGB  en  RGBZ  opgenomen  zijn.  Zie  ‘populatie  objecttype’  voor  de objecttypen die het betreft (alleen objecttypen op het laagste specialisatieniveau d.w.z. geen gegeneraliseerde objecttypen). 

Het OBJECT heeft dan ook amper attributen (alleen voor het zoeken van objecten  van  dit  objecttype).  De  overige  attributen  specificeren  we  per specialisatie (‘subtype’). Deze werken we hieronder, in deze paragraaf, uit. NB.  ZAAKOBJECT  vervangt,  en  is  een  uitbreiding  op,  de  objecttypen VERBLIJFSOBJECT,  KADASTRAAL  OBJECT  en  ADRES  van  het GFO Zaken 2004. 

## **Unieke aanduiding objecttype** 

## **Populatie objecttype** 

De unieke aanduiding van de desbetreffende specialisatie (‘subtype’) van het OBJECT. 

Objecten van de volgende objecttypen: ANDER NATUURLIJK PERSOON, ANDER BUITENLANDS NIET-NATUURLIJK PERSOON, APPARTEMENTSRECHT, BESLUIT, BUURT, ENKELVOUDIG DOCUMENT, GEMEENTE, GEMEENTELIJKE OPENBARE RUIMTE, HUISHOUDEN, INGESCHREVEN NIET-NATUURLIJK PERSOON, INGEZETENE, INRICHTINGSELEMENT, KADASTRAAL PERCEEL, KUNSTWERKDEEL, LIGPLAATS, MAATSCHAPPELIJKE ACTIVITEIT, MEDEWERKER, NIET-INGEZETENE, NUMMERAANDUIDING, OPENBARE RUIMTE, ORGANISATORISCHE EENHEID, OVERIGE ADRESSEERBAAR OBJECT AANDUIDING, OVERIG GEBOUWD OBJECT,  OVERIG  TERREIN,  PAND,  SAMENGESTELD  DOCUMENT, SPOORBAANDEEL, STANDPLAATS, STATUS, TERREINDEEL, VERBLIJFSOBJECT, VESTIGING, WATERDEEL, WEGDEEL, WIJK, WOONPLAATS, WOZ-DEELOBJECT, WOZ-OBJECT, WOZ-WAARDE, ZAKELIJK RECHT. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Identificatie|KING|
||Naam|KING|
||Adres binnenland|KING|
||Adres buitenland|KING|
||Kadastrale aanduiding|KING|
||Geometrie|KING|



32 

## **Overzicht relaties** 

Objecttype 

_Relatienaam incl. gerelateerd objecttype_ betreft ZAAKOBJECTen 

KING _Herkomst_ KING 

## **Objecttype: ANDER NATUURLIJK PERSOON** 

**Naam objecttype** 

ANDER NATUURLIJK PERSOON 

**Herkomst objecttype** 

RSGB 

**Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een ANDER NATUURLIJK PERSOON die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam_ 

_Herkomst_ 

Nummer ander natuurlijk persoon Geslachtsaanduiding Geboortedatum Naam aanschrijving Aanhef aanschrijving Voorletters aanschrijving Voornamen aanschrijving Geslachtsnaam aanschrijving Overlijdensdatum SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING 

ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam 

## **Objecttype: ANDER BUITENLANDS NIET-NATUURLIJK PERSOON** 

**Naam objecttype** 

**Herkomst objecttype** 

ANDER BUITENLANDS NIET-NATUURLIJK PERSOON RSGB 

33 

## **Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een ANDER BUITENLANDS NIET-NATUURLIJK PERSOON die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Nummer ander buitenlands niet-natuurlijk persoon (Statutaire) Naam Datum aanvang Datum beëindiging SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam 

## **Objecttype: APPARTEMENTSRECHT** 

> **Naam objecttype** APPARTEMENTSRECHT 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een APPARTEMENTSRECHT  die  in  het  RGBZ  gebruikt  worden  bij  deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Appartementsindex BRK KADASTRALE ONROERENDE ZAAK . Kadastrale identificatie KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding Kadastrale gemeentecode Sectie Perceelnummer Datum begin geldigheid kadastrale onroerende zaak Datum einde geldigheid kadastrale onroerende zaak 

## **Objecttype: BESLUIT** 

> **Naam objecttype** BESLUIT 

> **Herkomst objecttype** RGBZ 

> **Toelichting objecttype** Hieronder benoemen we de aan het RGBZ ontleende gegevens van een BESLUIT  die  in  het  RGBZ  gebruikt  worden  bij  deze  specialisatie  van OBJECT. Zie voor de specificaties van deze gegevens het RGBZ 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Besluitidentificatie Besluitdatum Ingangsdatum Vervaldatum BESLUITTYPE . Besluittype-omschrijving 

34 

BESLUITTYPE . Besluittype-omschrijving generiek 

## **Objecttype: BUURT** 

> **Naam objecttype** BUURT 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een BUURT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Buurtcode Buurtnaam Buurtgeometrie Datum begin geldigheid buurt Datum einde geldigheid buurt WIJK . Wijkcode GEMEENTE . Gemeentecode 

## **Objecttype: ENKELVOUDIG DOCUMENT** 

> **Naam objecttype** ENKELVOUDIG DOCUMENT 

> **Herkomst objecttype** RGBZ 

> **Toelichting objecttype** Hieronder benoemen we de aan het RGBZ ontleende gegevens van een ENKELVOUDIG DOCUMENT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RGBZ. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Documentidentificatie Documentcreatiedatum Documentontvangstdatum Documenttitel DOCUMENTTYPE . Documenttype-omschrijving DOCUMENTTYPE . Documenttype-omschrijving generiek 

## **Objecttype: GEMEENTE** 

> **Naam objecttype** GEMEENTE 

**Herkomst objecttype** 

RSGB 

**Toelichting objecttype** 

**Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een GEMEENTE die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ 

35 

Gemeentecode Gemeentenaam Gemeentegeometrie Datum begin geldigheid gemeente Datum einde geldigheid gemeente 

## **Objecttype: GEMEENTELIJKE OPENBARE RUIMTE** 

> **Naam objecttype** GEMEENTELIJKE OPENBARE RUIMTE 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een GEMEENTELIJKE OPENBARE RUIMTE die in het RGBZ gebruikt worden bij  deze  specialisatie  van  OBJECT.  Zie  voor  de  specificaties  van  deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ GEMEENTE . Gemeentecode Identificatiecode gemeentelijke openbare ruimte Naam openbare ruimte Type openbare ruimte Geometrie gemeentelijke openbare ruimte Datum begin geldigheid Gemeentelijke Openbare Ruimte Datum einde geldigheid Gemeentelijke Openbare Ruimte 

## **Objecttype: HUISHOUDEN** 

> **Naam objecttype** HUISHOUDEN 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een HUISHOUDEN die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Huishoudennummer Huishoudensoort Datum begin geldigheid huishouden Datum einde geldigheid huishouden GEBOUWD OBJECT . Identificatie BENOEMD TERREIN . Identificatie ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

36 

## **Objecttype: INGESCHREVEN NIET-NATUURLIJK PERSOON** 

## **Naam objecttype** 

INGESCHREVEN NIET-NATUURLIJK PERSOON 

**Herkomst objecttype Toelichting objecttype** 

## **Overzicht attributen** 

## RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een INGESCHREVEN NIET-NATUURLIJK PERSOON die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ NNP-ID Rechtsvorm (Statutaire) Naam Datum aanvang Datum beëindiging SUBJECT heeft als bezoekadres ADRESSEERBAAR OBJECT AANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam 

37 

## **Objecttype: INGEZETENE** 

## **Naam objecttype** 

## **Herkomst objecttype** 

## **Toelichting objecttype** 

## **Overzicht attributen** 

## INGEZETENE 

## RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een INGEZETENE die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Burgerservicenummer||
||INGESCHREVEN PERSOON . Verblijfsplaats||
||ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer||
||ADRESSEERBAAR OBJECT AANDUIDING . Huisletter||
||ADRESSEERBAAR OBJECT AANDUIDING .||
|Huisnummertoevoeging|||
||GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte||
||GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam||
||ADRESSEERBAAR OBJECT AANDUIDING . Postcode||
||INGESCHREVEN PERSOON . Locatiebeschrijving||
||WOONPLAATS . Woonplaatsnaam||
||Geslachtsaanduiding||
||Geboortedatum||
||Naam aanschrijving||
||Aanhef aanschrijving||
||Voorletters aanschrijving||
||Voornamen aanschrijving||
||Geslachtsnaam aanschrijving||
||Overlijdensdatum||
||SUBJECT heeft als correspondentieadres ADRESSEERBAAR||
|OBJECT AANDUIDING|||
||ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer||
||ADRESSEERBAAR OBJECT AANDUIDING . Huisletter||
||ADRESSEERBAAR OBJECT AANDUIDING .||
|Huisnummertoevoeging|||
||GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte||
||GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam||
||ADRESSEERBAAR OBJECT AANDUIDING . Postcode||
||WOONPLAATS . Woonplaatsnaam||
||SUBJECT . Postadres||
||Postadrestype||
||Postbus- of antwoordnummer||
||Postadres postcode||
||WOONPLAATS . Woonplaatsnaam||
||SUBJECT . Verblijf buitenland||
||Adres buitenland 1||
||Adres buitenland 2||
||Adres buitenland 3||
||Land . Landnaam||



38 

## **Objecttype: INRICHTINGSELEMENT** 

## **Naam objecttype** 

INRICHTINGSELEMENT 

**Herkomst objecttype** 

RSGB 

**Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een INRICHTINGSELEMENT  die  in  het  RGBZ  gebruikt  worden  bij  deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Inrichtingselementtype Identificatie inrichtingselement Geometrie inrichtingselement Naam inrichtingselement Datum begin geldigheid inrichtingselement Datum einde geldigheid inrichtingselement 

## **Objecttype: KADASTRAAL PERCEEL** 

**Naam objecttype Herkomst objecttype** 

KADASTRAAL PERCEEL 

RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een KADASTRAAL  PERCEEL  die  in  het  RGBZ  gebruikt  worden  bij  deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Deelperceelnummer Begrenzing perceel KADASTRALE ONROERENDE ZAAK . Kadastrale identificatie KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding Kadastrale gemeentecode Sectie 

Perceelnummer Datum begin geldigheid kadastrale onroerende zaak Datum einde geldigheid kadastrale onroerende zaak 

## **Objecttype: KUNSTWERKDEEL** 

> **Naam objecttype** KUNSTWERKDEEL 

**Herkomst objecttype** 

RSGB 

**Toelichting objecttype** 

**Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een KUNSTWERKDEEL die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Type kunstwerk 

39 

Identificatie kunstwerkdeel Geometrie kunstwerkdeel Naam kunstwerkdeel Datum begin geldigheid kunstwerkdeel Datum einde geldigheid kunstwerkdeel 

## **Objecttype: LIGPLAATS** 

## **Naam objecttype** 

## LIGPLAATS 

**Herkomst objecttype** 

## RSGB 

**Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een LIGPLAATS die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ BENOEMD TERREIN . Benoemd terrein Identificatie BENOEMD TERREIN . Geometrie BENOEMD TERREIN . Datum begin geldigheid benoemd terrein BENOEMD TERREIN . Datum einde geldigheid benoemd terrein ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

## **Objecttype: MAATSCHAPPELIJKE ACTIVITEIT** 

> **Naam objecttype** MAATSCHAPPELIJKE ACTIVITEIT 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een MAATSCHAPPELIJKE ACTIVITEIT die in het RGBZ gebruikt worden bij deze  specialisatie  van  OBJECT.  Zie  voor  de  specificaties  van  deze gegevens het RSGB. 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ KvK-nummer Datum aanvang Datum beëindiging Handelsnaam SUBJECT . Identificatie 

40 

## **Objecttype: MEDEWERKER** 

## **Naam objecttype** 

MEDEWERKER 

> **Herkomst objecttype** RGBZ **Toelichting objecttype** 

Hieronder benoemen we de aan het RGBZ ontleende gegevens van een MEDEWERKER die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RGBZ 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Medewerkeridentificatie Achternaam Datum uit dienst Functie Geslachtsaanduiding Voorletters Voorvoegsel achternaam ORGANISATORISCHE EENHEID . Organisatieidentificatie 

## **Objecttype: NIET-INGEZETENE** 

> **Naam objecttype** NIET-INGEZETENE 

**Herkomst objecttype Toelichting objecttype** 

**Overzicht attributen** 

## RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een NIET-INGEZETENE die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Burgerservicenummer INGESCHREVEN PERSOON . Verblijfsplaats ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode INGESCHREVEN PERSOON . Locatiebeschrijving WOONPLAATS . Woonplaatsnaam Geslachtsaanduiding Geboortedatum Naam aanschrijving Aanhef aanschrijving Voorletters aanschrijving Voornamen aanschrijving Geslachtsnaam aanschrijving Overlijdensdatum SUBJECT heeft als correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter 

41 

## ADRESSEERBAAR OBJECT AANDUIDING . 

Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE .  Straatnaam ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Postadres Postadrestype Postbus- of antwoordnummer Postadres postcode WOONPLAATS . Woonplaatsnaam SUBJECT . Verblijf buitenland Adres buitenland 1 Adres buitenland 2 Adres buitenland 3 Land . Landnaam 

## **Objecttype: NUMMERAANDUIDING** 

> **Naam objecttype** NUMMERAANDUIDING 

**Herkomst objecttype** 

RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een NUMMERAANDUIDING die  in het RGBZ gebruikt worden  bij  deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Indicatie hoofdadres ADRESSEERBAAR OBJECT AANDUIDING . Identificatiecode adresseerbaar object aanduiding ADRESSEERBAAR OBJECT AANDUIDING . Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging ADRESSEERBAAR OBJECT AANDUIDING . Postcode ADRESSEERBAAR OBJECT AANDUIDING . Datum begin geldigheid adresseerbaar object aanduiding ADRESSEERBAAR OBJECT AANDUIDING . Datum einde geldigheid adresseerbaar object aanduiding GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte WOONPLAATS . Woonplaatsnaam 

## **Objecttype: OPENBARE RUIMTE** 

> **Naam objecttype** OPENBARE RUIMTE 

> **Herkomst objecttype** RSGB 

42 

## **Toelichting objecttype** 

**Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een OPENBARE RUIMTE die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Identificatiecode openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE . Naam openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE . Type openbare ruimte GEMEENTELIJKE OPENBARE RUIMTE . Datum begin geldigheid Gemeentelijke Openbare Ruimte GEMEENTELIJKE OPENBARE RUIMTE . Datum einde geldigheid Gemeentelijke Openbare Ruimte WOONPLAATS . Woonplaatsnaam 

## **Objecttype: ORGANISATORISCHE EENHEID** 

> **Naam objecttype** ORGANISATORISCHE EENHEID 

> **Herkomst objecttype** RGBZ 

> **Toelichting objecttype** Hieronder benoemen we de aan het RGBZ ontleende gegevens van een ORGANISATORISCHE EENHEID die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RGBZ. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Organisatieidentificatie Datum ontstaan Datum opheffing Naam 

## **Objecttype: OVERIGE ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam objecttype** OVERIGE ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een OVERIGE  ADRESSEERBAAR  OBJECT AANDUIDING  die  in  het  RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ ADRESSEERBAAR OBJECT AANDUIDING . Identificatiecode adresseerbaar object aanduiding ADRESSEERBAAR OBJECT AANDUIDING . Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging ADRESSEERBAAR OBJECT AANDUIDING . Postcode ADRESSEERBAAR OBJECT AANDUIDING . Datum begin geldigheid adresseerbaar object aanduiding ADRESSEERBAAR OBJECT AANDUIDING . Datum einde 

43 

## geldigheid adresseerbaar object aanduiding 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte WOONPLAATS . Woonplaatsnaam 

## **Objecttype: OVERIG GEBOUWD OBJECT** 

**Naam objecttype** 

## OVERIG GEBOUWD OBJECT 

**Herkomst objecttype** 

RSGB 

**Toelichting objecttype** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een OVERIG GEBOUWD OBJECT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

## **Overzicht attributen** _Code Gegevensnaam Herkomst_ 

Overig gebouwd object locatie-aanduiding GEBOUWD OBJECT . Gebouwd object identificatie BENOEMD TERREIN . Gebouwd object puntgeometrie BENOEMD TERREIN . Datum begin geldigheid gebouwd object BENOEMD TERREIN . Datum einde geldigheid  gebouwd object ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

## **Objecttype: OVERIG TERREIN** 

> **Naam objecttype** OVERIG TERREIN 

**Herkomst objecttype** 

RSGB 

## **Toelichting objecttype** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een OVERIG TERREIN die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ 

BENOEMD TERREIN . Benoemd terrein Identificatie BENOEMD TERREIN . Geometrie BENOEMD TERREIN . Datum begin geldigheid benoemd terrein BENOEMD TERREIN . Datum einde geldigheid benoemd terrein ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

44 

## **Objecttype: PAND** 

**Naam objecttype Herkomst objecttype** 

## PAND 

## RSGB 

**Toelichting objecttype** 

**Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een PAND die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Pandidentificatie Pandgeometrie bovenaanzicht Datum begin geldigheid pand Datum einde geldigheid pand 

## **Objecttype: SAMENGESTELD DOCUMENT** 

## **Naam objecttype** 

SAMENGESTELD DOCUMENT 

> **Herkomst objecttype** RGBZ 

> **Toelichting objecttype** Hieronder benoemen we de aan het RGBZ ontleende gegevens van een SAMENGESTELD DOCUMENT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RGBZ. 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Documentidentificatie Documentcreatiedatum Documentontvangstdatum Documenttitel DOCUMENTTYPE . Documenttype-omschrijving DOCUMENTTYPE. Documenttype-omschrijving generiek 

## **Objecttype: SPOORBAANDEEL** 

## **Naam objecttype** SPOORBAANDEEL 

**Herkomst objecttype** 

## RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een SPOORBAANDEEL die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Type spoorbaan Identificatie spoorbaandeel Geometrie spoorbaandeel Naam spoorbaandeel Datum begin geldigheid spoorbaandeel Datum einde geldigheid spoorbaandeel 

45 

## **Objecttype: STANDPLAATS** 

## **Naam objecttype** 

STANDPLAATS 

**Herkomst objecttype** 

## RSGB 

## **Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een STANDPLAATS die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

## _Code Gegevensnaam Herkomst_ 

BENOEMD TERREIN . Benoemd terrein Identificatie BENOEMD TERREIN . Geometrie BENOEMD TERREIN . Datum begin geldigheid benoemd terrein BENOEMD TERREIN . Datum einde geldigheid benoemd terrein ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . 

Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

## **Objecttype: STATUS** 

> **Naam objecttype** STATUS 

**Herkomst objecttype** 

RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RGBZ ontleende gegevens van een STATUS  die  in  het  RGBZ  gebruikt  worden  bij  deze  specialisatie  van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Datum status gezet ZAAK .  Zaakidentificatie STATUSTYPE . Statustype-omschrijving STATUSTYPE . Statustypevolgnummer 

## **Objecttype: TERREINDEEL** 

> **Naam objecttype** TERREINDEEL 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een TERREINDEEL die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Type terrein 

46 

Identificatie terreindeel Geometrie terreindeel Naam terreindeel Datum begin geldigheid terreindeel Datum einde geldigheid terreindeel 

## **Objecttype: VERBLIJFSOBJECT** 

## **Naam objecttype** VERBLIJFSOBJECT 

**Herkomst objecttype** 

## RSGB 

## **Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een VERBLIJFSOBJECT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

## _Code Gegevensnaam Herkomst_ 

GEBOUWD OBJECT . Gebouwd object identificatie BENOEMD TERREIN . Gebouwd object puntgeometrie BENOEMD TERREIN . Datum begin geldigheid gebouwd object BENOEMD TERREIN . Datum einde geldigheid  gebouwd object ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging 

GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

## **Objecttype: VESTIGING** 

**Naam objecttype** 

**Herkomst objecttype** 

**Toelichting objecttype** 

**Overzicht attributen** 

## **Objecttype: WATERDEEL** 

**Naam objecttype** 

## WATERDEEL 

**Herkomst objecttype** 

## RSGB 

**Toelichting objecttype** 

**Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een WATERDEEL die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Type waterdeel 

47 

Identificatie waterdeel Geometrie waterdeel Naam waterdeel Datum begin geldigheid waterdeel Datum einde geldigheid waterdeel 

## **Objecttype: WEGDEEL** 

> **Naam objecttype** WEGDEEL 

> **Herkomst objecttype** RSGB **Toelichting objecttype** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een WEGDEEL die in  het RGBZ gebruikt worden  bij  deze  specialisatie  van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Type weg Identificatie wegdeel Geometrie wegdeel Naam wegdeel Datum begin geldigheid wegdeel Datum einde geldigheid wegdeel 

## **Objecttype: WIJK** 

> **Naam objecttype** WIJK 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een WIJK die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

**Overzicht attributen** 

_Code Gegevensnaam Herkomst_ Wijkcode Wijknaam Wijkgeometrie Datum begin geldigheid wijk Datum einde geldigheid wijk GEMEENTE . Gemeentecode 

## **Objecttype: WOONPLAATS** 

> **Naam objecttype** WOONPLAATS 

**Herkomst objecttype Toelichting objecttype** 

## RSGB 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een WOONPLAATS die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

48 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Woonplaatsidentificatie Woonplaatsnaam Woonplaatsgeometrie Datum begin geldigheid woonplaats Datum einde geldigheid woonplaats 

## **Objecttype: WOZ-DEELOBJECT** 

> **Naam objecttype** WOZ-DEELOBJECT 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een WOZ-DEELOBJECT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ Nummer WOZ-deelobject Code WOZ-deelobject Datum begin geldigheid deelobject Datum einde geldigheid deelobject WOZ-OBJECT . WOZ-objectnummer 

## **Objecttype: WOZ-OBJECT** 

> **Naam objecttype** WOZ-OBJECT 

> **Herkomst objecttype** RSGB 

> **Toelichting objecttype** Hieronder benoemen we de aan het RSGB ontleende gegevens van een WOZ-OBJECT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

> **Overzicht attributen** _Code Gegevensnaam Herkomst_ WOZ-objectnummer Locatie-omschrijving Geometrie WOZ-object Soort-object-code Datum begin geldigheid WOZ-object Datum einde geldigheid WOZ-object ADRESSEERBAAR OBJECT AANDUIDING .  Huisnummer ADRESSEERBAAR OBJECT AANDUIDING . Huisletter ADRESSEERBAAR OBJECT AANDUIDING . Huisnummertoevoeging GEMEENTELIJKE OPENBARE RUIMTE .  Naam openbare ruimte ADRESSEERBAAR OBJECT AANDUIDING . Postcode WOONPLAATS . Woonplaatsnaam 

49 

## **Objecttype: WOZ-WAARDE** 

## **Naam objecttype** 

WOZ-WAARDE 

**Herkomst objecttype** 

## RSGB 

**Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een WOZ-WAARDE die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Vastgestelde waarde Waardepeildatum WOZ-OBJECT . WOZ-objectnummer 

## **Objecttype: ZAKELIJK RECHT** 

## **Naam objecttype** 

## ZAKELIJK RECHT 

**Herkomst objecttype** 

## RSGB 

**Toelichting objecttype** 

## **Overzicht attributen** 

Hieronder benoemen we de aan het RSGB ontleende gegevens van een ZAKELIJK RECHT die in het RGBZ gebruikt worden bij deze specialisatie van OBJECT. Zie voor de specificaties van deze gegevens het RSGB. 

_Code Gegevensnaam Herkomst_ Kadaster identificatie zakelijk recht Ingangsdatum recht Einddatum recht 

AARD VERKREGEN RECHT . Aanduiding aard verkregen recht KADASTRALE ONROERENDE ZAAK . Kadastrale identificatie KADASTRALE ONROERENDE ZAAK . Kadastrale aanduiding Kadastrale gemeentecode Sectie 

Perceelnummer KADASTRAAL PERCEEL .  Deelperceelnummer APPARTEMENTSRECHT  . Appartementsindex SUBJECT . Identificatie 

50 

## **3.9. Organisatorische eenheid** 

**Naam objecttype** 

ORGANISATORISCHE EENHEID 

**Mnemonic objecttype** 

## OEH 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

## **Toelichting objecttype** 

GFO Zaken 2004 

Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken. 

KING op basis van het GFO Zaken 2004 

## 1 juni 2008 

Alleen organisatorische eenheden van de organisaties die zaken behandelen worden hier bedoeld (bijvoorbeeld afdelingen van gemeenten). Dus  niet  organisatorische  eenheden  van  andere  organisaties  zoals  de externe initiatoren van zaken (bijvoorbeeld de afdeling van een bedrijf die een vergunning aanvraagt). 

De organisatorische eenheid zoals hier bedoeld is gehuisvest binnen één fysieke  vestiging  van  de  organisatie.  Als  een  functioneel  afgebakend onderdeel  van de  organisatie  haar  activiteiten uitvoert in  meerdere vestigingen  dan  wordt  die  uitgewisseld  als  evenveel  organisatorische eenheden  als  die  vestigingen.  Door  de  relatie  naar VESTIGING  VAN ZAAKBEHANDELENDE ORGANISATIE en daarmee  via VESTIGING naar NIET  NATUURLIJK  PERSOON is  bekend  om  welke  zaakbehandelende organisatie het gaat. 

Een  organisatorische  eenheid  kan  zowel  groot  als  klein  zijn.  De  ene organisatorische eenheid mag andere organisatorische eenheden bevatten, maar dit wordt niet gemodelleerd. We beperken ons tot het aangeven welke organisatorische eenheid welke rol heeft in een zaak en welke gegevens daarvan vanuit het oogpunt van een zaak relevant zijn. 

ORGANISATORISCHE EENHEID  is  een  specialisatie  ('subtype') van BETROKKENE. 

## **Unieke aanduiding objecttype** 

## **Populatie objecttype** 

## Organisatieidentificatie 

De organisatorische eenheden van de zaakbehandelende organisatie die betrokken  zijn  bij  het  zaakgericht  werken  betreffende  geimplementeerde zaaktypen. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

_Code Gegevensnaam Herkomst_ 0001 Organisatieidentificatie GFO Zaken 8120 Datum ontstaan GFO Zaken 8130 Datum opheffing GFO Zaken 9516 E-mail adres GFO Zaken 9527 Faxnummer GFO Zaken 0002 Naam GFO Zaken 0003 Naam verkort GFO Zaken 0004 Omschrijving GFO Zaken 9580 Telefoonnummer GFO Zaken 0005 Toelichting GFO Zaken 

51 

|**Overzicht relaties**|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|---|---|---|
||bestaat uit MEDEWERKERs|GFO Zaken|
||heeft als verantwoordelijke MEDEWERKER|GFO Zaken|
||heeft als contactpersoon MEDEWERKER|GFO Zaken|
||is verantwoordelijke voor ZAAKTYPE|KING/GFO|
||is gehuisvest  in VESTIGING VAN ZAAKBEHANDELENDE||
||ORGANISATIE|KING|
||Relatiesoorten van de generalisatie BETROKKENE:||
||oefent uit ROL|KING|



52 

## **3.10. Rol** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## ROL 

## ROL 

## KING 

De taken, rechten en/of verplichtingen die een specifieke betrokkene heeft ten aanzien van een specifieke zaak. 

## KING 

## 1 juni 2008 

De  ROL  verbindt  de  zaak  met  de  daarbij  betrokken  personen  en organisaties. Het gaat daarbij om de aard van de betrokkenheid van zowel de, veelal externe, initiatoren van de zaak als de behandelaren van de zaak. De aard van de betrokkenheid is dan ook divers: aanvrager, behandelaar, medebehandelaar, belanghebbende, indiener namens een ander, etcetera. Het is overigens  niet ondenkbaar dat één betrokkene meer dan één rol heeft in één zaak. Bijvoorbeeld als aanvrager van de zaak en als beschikkinghouder van het besluit (zoals een vergunning) dat de uitkomst is van de zaak. 

Elke zaakbehandelende organisatie kan diverse rolbenamingen (Rolomschrijving) hanteren. Om bij uitwisseling van zaakgegevens tussen organisaties te  bereiken dat rolbenamingen juist geinterpreteerd worden, hebben  we  Rolomschrijving  generiek  toegevoegd. Dit  bevat de  landelijk gehanteerde rolbenamingen. 

Indien de betrokkene bij een zaak een natuurlijk persoon, niet-natuurlijk persoon of vestiging (van een niet zaakbehandelende organisatie) is, kan het gewenst zijn de contactpersoon te kennen namens die betrokkene in die zaak. Deze hebben we dan ook opgenomen in ROL. Tevens hebben we de gegevens opgenomen van het correspondentieadres waarop de  (externe) betrokkene (natuurlijk persoon,niet-natuurlijk persoon of vestiging van nietzaakbehandelende  organisatie) in  zijn  of  haar  rol  bij  de  zaak  heeft aangegeven schriftelijk te willen communiceren indien dit afwijkt van het correspondentie-adres zoals dat voor de betrokkene regulier geldt. 

## **Unieke aanduiding objecttype** 

## **Populatie objecttype** 

Combinatie van de unieke aanduidingen van de gerelateerde BETROKKENE en de gerelateerde ZAAK met de Rolomschrijving. 

Voor alle zaken de bij een zaak betrokkenen die van belang zijn voor het tot een goed einde brengen, de inhoudelijke verantwoording (is de zaak goed afgehandeld), procesverantwoording  (is de zaak op  de juiste  wijze afgehandeld) en/of reconstructie van de zaak. 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|0002|Rolomschrijving|GFO Zaken|
||Rolomschrijving generiek|KING|
|0003|Roltoelichting|GFO Zaken|
||Contactpersoon|KING|
||Contactpersoonnaam|KING|
||Contactpersoon functie|KING|
||Contactpersoon telefoonnummer|KING|
||Contactpersoon emailadres|KING|
||Afwijkend correspondentie postadres|KING|



53 

## **Overzicht relaties** 

|Postadrestype|KING|
|---|---|
|Postbus- of antwoordnummer|KING/GFO|
|Postadres postcode|KING|
|Afwijkend buitenlands correspondentieadres|KING|
|Adres buitenland 1|KING|
|Adres buitenland 2|KING|
|Adres buitenland 3|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|betreft ZAAK|KING|
|wordt uitgeoefend door BETROKKENE|KING|
|zet als betrokkene STATUS|KING|
|van BETROKKENE met als afwijkend binnenlands correspondentieadres||
|ADRESSEERBAAR OBJECT AANDUIDING|KING|
|Afwijkend correspondentie postadres||
|van BETROKKENE met afwijkend correspondentie postadres dat||
|zich bevindt in WOONPLAATS|KING|
|Afwijkend buitenlands correspondentieadres||
|van BETROKKENE met afwijkend buitenlands correspondentieadres dat||
|zich bevindt in LAND|KING|



54 

## **3.11. Samengesteld document** 

**Naam objecttype** 

SAMENGESTELD DOCUMENT 

**Mnemonic objecttype Herkomst objecttype** 

SDC 

KING 

**Definitie objecttype** 

**Herkomst definitie objecttype** 

Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden., 

KING 

**Datum opname objecttype** 

## 1 oktober 2008 

## **Toelichting objecttype** 

## **Unieke aanduiding objecttype** 

Een SAMENGESTELD DOCUMENT is een specialisatie van DOCUMENT. Zie de toelichting bij dat objecttype. 

DOCUMENT.Documentidentificatie 

**Populatie objecttype** 

Zie DOCUMENT 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|Attributen van de generalisatie DOCUMENT:||
|Documentidentificatie|Dublin Core|
|Documentcreatiedatum|Dublin Core|
|Documentontvangstdatum|KING|
|Documenttitel|Dublin Core|
|Documentbeschrijving|Dublin Core|
|Document verzenddatum|KING|
|Vertrouwelijkaanduiding|KING|
|Documentauteur|Dublin Core|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|omvat ENKELVOUDIGE DOCUMENTen|KING|
|Relaties van de generalisatie DOCUMENT:||
|is van DOCUMENTTYPE|KING|
|betreft ZAAKDOCUMENTen|KING|
|kan vastlegging zijn van BESLUITen|KING|



55 

## **3.12. Status** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype Toelichting objecttype** 

## STATUS 

## STA 

## GFO Zaken 2004 

Een  aanduiding  van  de  stand  van  zaken  van  een  zaak  op  basis  van betekenisvol behaald resultaat voor de initiator van de zaak. 

KING op basis van het GFO Zaken 2004 

## 1 juni 2008 

De STATUS maakt het mogelijk de voortgang van de zaak op hoofdlijnen te volgen. Wat de hoofdlijnen zijn wordt vooral bepaald vanuit de belangen van de  initiator van de  zaak  en verplichtingen  vanuit wet- en  regelgeving. De initiator is veelal geinteresseerd in mijlpalen, niet in de diverse stappen die de behandelende organisatie(s) moet(en) zetten om de zaak af te handelen. 

Een zaak heeft in de loop van de tijd meerdere statussen: de achtereenvolgens bereikte mijlpalen. De STATUS is in het RGBZ overigens niet bedoeld om de behandeling van de zaak te plannen, wel om deze te kunnen volgen. 

De  laatst  bereikte  status  is  uiteraard  de  meest  actuele  status.  Daarvoor bereikte statussen zien we niet als historische waarden van de laatst bereikte status maar als historische statussen. De gegevens van een bereikte status wijzigen dan ook niet, m.u.v. eventuele ambtelijke correcties. 

Daar het kan voorkomen dat bepaalde, voor de zaak relevante, documenten nadrukkelijk  gerelateerd  zijn  aan  het  bereiken  van  een  status  en/of  de communicatie daarover, hebben  we de (optionele) relatie van STATUS naar ZAAKDOCUMENT gemodelleerd. 

NB. In het GFO Zaken 2004 was in de definitie sprake van ‘de burger’. Hier hebben we gekozen voor het ruimere begrip ‘initiator van de zaak’ omdat ook organisatorische eenheden en medewerkers zaken kunnen initiëren. 

## **Unieke aanduiding objecttype** 

Unieke aanduiding van de gerelateerde ZAAK in combinatie met  de Datum status gezet. 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|0004<br>Datum status gezet|GFO Zaken|
|0003<br>Statustoelichting|GFO Zaken|
|Indicatie laatst gezette status|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|is gezet door betrokkene in zijn/haar ROL|KING|
|is van ZAAK|GFO Zaken|
|is van STATUSTYPE|KING|
|heeft daarvoor relevante ZAAKDOCUMENTen|KING|



56 

## **3.13. Statustype** 

**Naam objecttype** 

**Mnemonic objecttype Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

## STATUSTYPE 

## STT 

KING 

Generieke aanduiding van de aard van een STATUS 

## KING 

## 1 juni 2008 

Zaken van eenzelfde zaaktype doorlopen alle dezelfde statussen, tenzij de zaak voortijdig beeindigd wordt. Met STATUSTYPE worden deze statussen benoemd bij het desbetreffende zaaktype. 

De attribuutsoort ‘Doorlooptijd status’ is niet bedoeld om daarmee voor een individuele  zaak  de  statussen  te  plannen  maar  om  geïnteresseerden informatie te verschaffen over de termijn waarop normaliter een volgende status bereikt wordt. 

## **Unieke aanduiding objecttype** 

Combinatie van de unieke aanduiding van het gerelateerde ZAAKTYPE met het Statustypevolgnummer 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|0002|Statustype-omschrijving|GFO Zaken|
|0001|Statustypevolgnummer|GFO Zaken|
||Doorlooptijd status|KING|
||Statustype-omschrijving generiek|KING|
||Datum begin geldigheid statustype|KING|
||Datum einde geldigheid statustype|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|heeft STATUSsen||KING|
|is van|ZAAKTYPE|KING|



57 

## **3.14. Zaak** 

## **Naam objecttype** 

## **Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype** 

## **Herkomst definitie objecttype** 

**Datum opname objecttype** 

## **Toelichting objecttype** 

## ZAAK 

## ZAK 

## GFO Zaken 2004 

Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding  en  een  welgedefinieerd  eindresultaat,  waarvan  kwaliteit  en doorlooptijd bewaakt moeten worden. 

GFO Zaken 2004 

## 1 juni 2008 

De ZAAK vormt de kern van het zaakgericht werken. Wat in een individueel geval een zaak is, waar die begint en waar die eindigt, moet vooral bekeken worden vanuit het perspectief van de initiator van de zaak (burger, bedrijf, medewerker, etc.). Wat door hem of haar als het eindresultaat wordt gezien definieert de omvang en afbakening van de zaak. 

In  de  praktijk  kan  dit  tot  problemen  in  de  behandeling  leiden  als  de behandelende  organisatie(s)  niet  in  staat  is  om  in  één  zaak  naar  het gewenste eindresultaat toe te werken. Het staat organisaties vrij om een zaak in ‘deelzaken’ te behandelen. Ook een ‘deelzaak’ is een ZAAK. Deze is gerelateerd aan de ‘hoofdzaak’: de ZAAK die het gevolg is van het verzoek van de initiator. Door deze onderlinge relatering cq. clustering wordt het zaakgericht werken voor de behandelende organisatie(s) beheersbaar  èn blijft  het  mogelijk  de  initiator  van  de  zaak  vanuit  zijn  perspectief  te informeren. Het relateren van hoofd- en deelzaken modelleren we met de relatiesoort 'ZAAK is deelzaak van ZAAK' en de attribuutsoorten Zaakniveau en Deelzakenindicatie. 

Elke zaak heeft ‘ergens betrekking op’ wat we modelleren met de relatie naar  ZAAKOBJECT.  In  het  geval  dat  de  zaak  op  geen  van  de,  met ZAAKOBJECT bedoelde, objecten betrekking heeft, wordt het object van de zaak vastgelegd met de attribuutgroep ‘Ander zaakobject’. 

Soms heeft de ene zaak betrekking op een andere zaak, wat we modelleren met de relatie ‘ZAAK is gerelateerd aan ZAAK’. De aard van de betrekking cq. relatie is op te maken uit de zaaktypen van beider zaken. 

Ook heeft elke zaak één of meer betrokkenen, wat we modelleren via de ROL. 

Een  zaak,  met  eventuele  deelzaken,  al  hun  kenmerken,  alle  daaraan gerelateerde documenten en alle andere gerelateerde gegevens (via ROL, ZAAKOBJECT, etc.) vormen gezamenlijk het zaakdossier. Het zaakdossier modelleren we dus niet als apart objecttype. Evenmin modelleren we een zgn.  objectdossier.  Dit  betreft  immers  alle  zaken,  met  bijbehorende kenmerken  en  documenten,  eventueel  van  bepaalde  zaaktypen,  die gerelateerd zijn aan een bepaald OBJECT. 

## **Unieke aanduiding objecttype** 

## **Populatie objecttype** 

## Zaakidentificatie 

Alle zaken waarvoor de zaakbehandelende organisatie(s) het zaakgericht werken heeft ingericht. 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

_Code Gegevensnaam_ 0001 Zaakidentificatie 

_Herkomst_ GFO Zaken 

58 

## **Overzicht relaties** 

|0014|Einddatum|GFO Zaken|
|---|---|---|
|0012|Einddatum gepland|GFO Zaken|
|0002|Omschrijving|GFO Zaken|
||Kenmerken|KING|
||- 0020 Kenmerk|GFO Zaken|
||- 0021 Kenmerk bron|GFO Zaken|
|0016|Resultaatomschrijving|GFO Zaken|
|0017|Resultaattoelichting|GFO Zaken|
|0011|Startdatum|GFO Zaken|
|0003|Toelichting|GFO Zaken|
|0013|Uiterlijke einddatum afdoening|GFO Zaken|
||Zaakniveau|KING|
||Deelzakenindicatie|KING|
||Registratiedatum|KING|
||Publicatiedatum|KING|
||Archiefnominatie|KING|
||Datum vernietiging dossier|KING|
||Betalingsindicatie|KING|
||Laatste betaaldatum|KING|
||Opschorting|KING|
||- Indicatie opschorting|KING|
||- Reden opschorting|KING|
||Verlenging|KING|
||- Duur verlenging|KING|
||- Reden verlenging|KING|
||Ander zaakobject|KING|
||- Ander zaakobject omschrijving|KING|
||- Ander zaakobject aanduiding|KING|
||- Ander zaakobject lokatie|KING|
||- Ander zaakobject registratie|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|heeft betrekking op andere ZAAKen||GFO Zaken|
|is deelzaak van ZAAK||KING|
|heeft betrekking op ZAAKOBJECTen||KING|
|heeft betrokkenen in ROLlen||KING|
|heeft ZAAKDOCUMENTen||KING|
|heeft STATUSsen||GFO Zaken|
|kan leiden tot BESLUIT||KING|
|is van|ZAAKTYPE|KING|



59 

## **3.15. Zaakdocument** 

**Naam objecttype** 

ZAAKDOCUMENT 

**Mnemonic objecttype** 

ZDC 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype** 

KING 

Een DOCUMENT dat relevant is voor de behandeling van de ZAAK en/of gecreëerd is in het kader van de behandeling van de ZAAK. KING 

**Datum opname objecttype** 

**Toelichting objecttype** 

## **Unieke aanduiding objecttype** 

## 1 juni 2008 

Meerdere documenten kunnen relevant zijn voor een zaak en/of gedurende de  behandeling  daarvan  gecreëerd  zijn.  Omgekeerd  kan  een  document relevant zijn voor meerdere zaken. Zo ontstaan n:m-relaties tussen zaken en documenten. Aangezien er eigenschappen zijn die niet bij alleen ZAAK of alleen DOCUMENT behoren (zoals bijvoorbeeld de Registratiedatum) maar behoren  bij  de  unieke  combinatie  van  een  zaak  met  een  document, modelleren we deze relatie met ZAAKDOCUMENT: de verwijzing naar de documenten  die  bij  een  zaak  behoren  en  de  verwijzing  naar de  zaken waarvoor een document relevant is. 

Combinatie van de unieke aanduidingen van de gerelateerde ZAAK en het gerelateerde DOCUMENT. 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
||Zaakdocumenttitel|Dublin Core|
||Zaakdocumentbeschrijving|Dublin Core|
||Registratiedatum|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|betreft|ZAAK|KING|
|betreft|DOCUMENT|KING|
|is relevant voor STATUS||KING|



60 

## **3.16. Zaakobject** 

## **Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

## **Toelichting objecttype** 

## ZAAKOBJECT 

## ZOB 

KING 

Een OBJECT waarop de ZAAK betrekking heeft. 

## KING 

## 1 juni 2008 

Een zaak kan op ‘van alles en nog wat’ betrekking hebben. Voor zover dit voorkomens  (objecten)  van  de  in  het  RSGB  onderscheiden  objecttypen betreft,  worden  deze  met  OBJECT  gemodelleerd.  Aangezien  de  relatie tussen ZAAK en OBJECT van de aard N-M is en eigenschappen heeft, modelleren we deze relatie met ZAAKOBJECT. 

Indien een zaak op een ander object betrekking heeft dan vallend onder OBJECT, dan wordt dat vastgelegd met de desbetreffende attribuutgroep bij ZAAK. 

NB. OBJECT en ZAAKOBJECT vervangen, en zijn een uitbreiding op, de objecttypen VERBLIJFSOBJECT, KADASTRAAL OBJECT en ADRES van het GFO Zaken 2004. 

## **Unieke aanduiding objecttype** 

De unieke aanduiding van de zaak in combinatie met de desbetreffende specialisatie (‘subtype’) van OBJECT. 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

**Overzicht attributen** 

## **Overzicht relaties** 

|_Code_<br>_Gegevensnaam_|_Herkomst_|
|---|---|
|Relatie-omschrijving|KING|
|_Relatienaam incl. gerelateerd objecttype_|_Herkomst_|
|Is onderwerp van ZAAK|KING|
|betreft OBJECT|KING|



61 

## **3.17. Zaaktype** 

**Naam objecttype** 

**Mnemonic objecttype** 

**Herkomst objecttype** 

**Definitie objecttype** 

**Herkomst definitie objecttype Datum opname objecttype** 

**Toelichting objecttype** 

## **Unieke aanduiding objecttype** 

## ZAAKTYPE 

## ZKT 

KING 

Generieke aanduiding van de aard van een zaak 

## KING 

## 1 juni 2008 

Het  betreft  de  indeling  of  groepering  van  zaken  naar  hun  aard,  zoals “Behandelen aanvraag bouwvergunning” en “Behandelen aanvraag ontheffing  parkeren”.  Elk  zaaktype  komt overeen  met of  valt  binnen  de generieke typering van zaken zoals landelijk gehanteerd in de Zaaktypecatalogus, de Zaaktype-omschrijving generiek . Het zaaktype stelt organisatie  in  staat  hun  eigen  typering  aan  te  houden  en,  d.m.v.  de zaaktype-omschrijving generiek, toch aan te kunnen sluiten op de landelijk gehanteerde typering generiek. 

Zaaktype-omschrijving 

## **Populatie objecttype** 

## **Kwaliteitsbegrip objecttype** 

## **Overzicht attributen** 

## **Overzicht relaties** 

|_Code_|_Gegevensnaam_|_Herkomst_|
|---|---|---|
|0005|Zaaktype-omschrijving|GFO Zaken|
||Zaaktype-omschrijving generiek|KING|
|0006|Trefwoord|GFO Zaken|
||Doorlooptijd behandeling|KING|
||Servicenorm behandeling|KING|
||Archiefcode|KING|
||Vertrouwelijkaanduiding|KING|
||Publicatie-indicatie|KING|
||Zaakcategorie|KING|
||Publicatietekst|KING|
||Datum begin geldigheid zaaktype|KING|
||Datum einde geldigheid zaaktype|KING|
|_Relatienaam incl. gerelateerd objecttype_||_Herkomst_|
|betreft ZAAKen||KING|
|heeft STATUSTYPEn||KING|
|heeft verantwoordelijke ORGANISATORISCHE EENHEID||KING/GFO|
|heeft verantwoordelijke MEDEWERKER||KING/GFO|



62 

## **4. Beschrijving van de attributen en relaties** 

In  dit  hoofdstuk  worden  de  onderscheiden  attributen  en  relaties,  naar  analogie  van  de basisregistratie-catalogi verder te noemen attribuutsoorten en relatiesoorten, gespecificeerd, per objecttype, op basis van de voor basisregistratie-catalogi gebruikelijke wijze, als volgt. 

## **Specificatie attribuutsoort** 

**Naam attribuutsoort** 

De naam van de attribuutsoort zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde attribuutsoort betreft, de door KING vastgestelde naam van de attribuutsoort. 

De naam van de attribuutsoort wordt uniek gemaakt door voorafgaand aan de naam de afkorting van het objecttype op te nemen, waarop de attribuutsoort betrekking heeft. 

**Herkomst attribuutsoort** 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

De basisregistratie in wiens catalogus de attribuutsoort is gespecificeerd (oftewel de basisregistratie waar de attribuutsoort deel van uitmaakt). Deze  specificatie  is  toegevoegd  t.o.v.  de  basisregistratie-catalogus aangezien het hier niet om een basisregistratie gaat maar wel duidelijk moet zijn in welke basisregistratie de attribuutsoort voorkomt (indien van toepassing). 

De door de desbetreffende basisregistratiehouder aan de attribuutsoort toegekende uniek code. Voor door KING toegevoegde attribuutsoorten is vooralsnog afgezien van het specificeren van deze code. 

De naam van de attribuutsoort in de gestructureerde beschrijving van de attribuutsoort in het XML-formaat zoals gespecificeerd in de desbetreffende  catalogus. De  XML-tag  wordt dan  ook  alleen  vermeld indien het een door KING toegevoegde attribuutsoort betreft. 

De beschrijving van de betekenis van de attribuutsoort zoals gespecificeerd in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde attribuutsoort betreft, de door KING vastgestelde definitie van de attribuutsoort. 

Voor attribuutsoorten die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen  vermeld  indien  het een  door  KING  toegevoegde  attribuutsoort betreft. 

De datum waarop de attribuutsoort is opgenomen in het RSGB. 

Voor attribuutsoorten die deel uitmaken van een basisregistratie betreft dit de daarin opgenomen toelichting. De toelichting wordt dan ook alleen gegeven indien het een door KING toegevoegde attribuutsoort betreft dan wel indien een toelichting nodig is, aanvullend op de toelichting in de desbetreffende catalogus. 

63 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

## **Indicatie formele historie** 

Formaat: 

Formaat: Het aantal karakters (lengte) en het soort tekens waarmee waarden van deze attribuutsoort worden vastgelegd. Waardenverzameling: De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben (opsomming, bereik of verwijzing naar tabel). Voor attribuutsoorten die deel uitmaken van een basisregistratie betreft dit het daarin gespecificeerde domein. Het domein wordt dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft. Indien  de  waardenverzameling  in  een  dynamische  waardentabel  is opgenomen,  dan  wordt  de  naam van  het  desbettreffende  StUFtabelentiteittype  vermeld  en  wordt  in  de  'Toelichting  attribuutsoort' vermeld in welk document de waardenverzameling beheerd wordt. 

Indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de attribuutwaarde. Met het opnemen van deze indicatie zien we af van de specificatie van ‘historie-attributen’  bij  objecttypen,  zoals  bijvoorbeeld  ‘Datum  begin geldigheid gegevens’, zoals dat gebruikelijk is in sommige basisregistratiecatalogi.  Dergelijke  attributen  (meta-gegevens)  volgen logsicherwijs  uit  deze  indicatie.  Om  duidelijk  te  maken  om  welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

Indicatie  of  de  formele  historie  van  de  attribuutsoort te  bevragen  is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt). 

Met het opnemen van deze indicatie zien we af van de specificatie van ‘historie-attributen’  bij  objecttypen,  zoals  bijvoorbeeld  ‘Datum  wjziging gegevens’ en ‘Datum en tijdstip registratie gegevens’ zoals dat gebruikelijk is in sommige basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen logsicherwijs uit deze indicatie. Om duidelijk te maken om welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

## **Aanduiding gebeurtenis** 

Indicatie of bij een opname, mutatie of verwijdering van de attribuutwaarde de gebeurtenis aangeduid wordt  die aanleiding gaf tot verandering van  de attribuutwaarde  en zo  ja, de specificatie  van het metagegeven waarmee de gebeurtenis aangeduid wordt: Gebeurtenisomschrijving. Dit metagegeven specificeren we in bijlage 1. Met het opnemen van deze aanduiding zien we af van de specificatie van ‘gebeurtenis-attributen’  bij  objecttypen,  zoals  bijvoorbeeld  ‘Aanduiding gebeurtenis begin’, zoals dat gebruikelijk is in sommige basisregistratiecatalogi.  Dergelijke  attributen  (meta-gegevens)  volgen logsicherwijs  uit  deze  aanduiding.  Om  duidelijk  te  maken  om  welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

64 

**Aanduiding brondocument** 

Indicatie of bij een opname, mutatie of verwijdering van de attribuutwaarde het brondocument aangeduid wordt op basis waarvan de verandering van de attribuutwaarde heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Documentsoort, Documenthouder. Deze metagegevens specificeren we in bijlage 1. 

Met het opnemen van deze aanduiding zien we af van de specificatie van ‘brondocument-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Documentnummer mutatie …’ en ‘Soort document ingang geldigheid’, zoals dat gebruikelijk is in sommige basisregistratiecatalogi. Dergelijke attributen (meta-gegevens) volgen logsicherwijs uit deze aanduiding. Om duidelijk te maken om welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

**Indicatie in onderzoek** 

De indicatie of te bevragen  is dat er twijfel is of is geweest aan de juistheid  van  de  attribuutwaarde  en  dat  een  onderzoek  wordt  of  is uitgevoerd naar de juistheid van de attribuutwaarde. Dit metagegeven specificeren we in bijlage 1. 

Met het opnemen van deze indicatie zien we af van de specificatie van ‘onderzoek-attributen’  bij  objecttypen,  zoals  bijvoorbeeld  ‘Aanduiding gegevens in onderzoek’ zoals dat gebruikelijk is in sommige basisregistratiecatalogi.  Dergelijke  attributen  (meta-gegevens)  volgen logsicherwijs  uit  deze  indicatie.  Om  duidelijk  te  maken  om  welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

> **Aanduiding strijdigheid/nietigheid** De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de openbare orde dan wel nietig is. Dit metagegeven specificeren we in bijlage 1. 

Met het opnemen van deze aanduiding zien we af van de specificatie van ‘strijdigheid/nietigheid-attributen’ bij objecttypen, zoals bijvoorbeeld ‘Aanduiding strijdigheid / nietigheid’ zoals dat gebruikelijk is in sommige basisregistratiecatalogi.  Dergelijke  attributen  (meta-gegevens)  volgen logsicherwijs  uit  deze  aanduiding.  Om  duidelijk  te  maken  om  welke attribuutsoort in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

**Indicatie kardinaliteit** 

Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype:. 

- 0-1: is soms niet beschikbaar 

- 1-1: is altijd beschikbaar 

0-N: is niet altijd beschikbaar, kan een opsomming zijn 

- 1-N: is altijd beschikbaar, kan een opsomming zijn. 

Indien een attribuutsoort deel uit maakt van een groepsattribuutsoort, dan wordt de kardinaliteit vermeld van het attribuutsoort binnen de groepattribuutsoort. Voor de uiteindelijke kardinaliteit van het attribuutsoort moet ook rekening gehouden worden met de kardinaliteit van het groepsattribuutsoort. 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Aanduiding of het een authentiek gegeven (attribuutsoort) betreft. 

Optionaliteitsregels of waardebeperkende regels zoals gespecificeerd in de desbetreffende catalogus. De regels worden dan ook alleen vermeld indien het een door KING toegevoegde attribuutsoort betreft.. 

65 

## **Specificatie relatiesoort** 

## **Naam relatiesoort** 

## **Herkomst relatiesoort** 

## **Code relatiesoort** 

## **Definitie relatiesoort** 

## **Herkomst definitie relatiesoort** 

## **Datum opname relatiesoort** 

## **Toelichting relatiesoort** 

## **Indicatie materiële historie** 

De naam van de relatiesoort zoals afgeleid is van de overeenkomstige attribuutsoort in de catalogus van de desbetreffende basisregistratie dan wel, indien het een door KING toegevoegde relatiesoort betreft, de door KING vastgestelde naam van de relatiesoort. 

De basisregistratie in wiens catalogus de attribuutsoort is gespecificeerd waarvan de relatiesoort is afgeleid (oftewel de basisregistratie waar de relatiesoort impliciet deel van uitmaakt). 

De door de desbetreffende basisregistratiehouder aan de overeenkomstige attribuutsoort toegekende uniek code. Voor door KING toegevoegde attribuutsoorten is vooralsnog afgezien van het specificeren van deze code. 

De beschrijving van de betekenis van de relatiesoort zoals afgeleid van de definitie van de overeenkomstige attribuutsoort in de catalogus van de desbetreffende  basisregistratie  dan  wel,  indien  het  een  door  KING toegevoegde relatiesoort betreft, de door KING vastgestelde definitie van de relatiesoort. 

Voor een relatiesoort waarvan het overeenkomstige attribuutsoort deel uitmaakt van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft. 

De datum waarop de relatiesoort is opgenomen in het RSGB. 

Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit de daarin opgenomen toelichting bij de overeenkomstige attribuutsoort. De toelichting wordt dan ook alleen gegeven indien het een door KING toegevoegde relatiesoort betreft dan wel indien een toelichting nodig is, aanvullend op de toelichting in de desbetreffende catalogus. 

Indicatie  of  de  materiële  historie  van  de  relatiesoort  te  bevragen  is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de relatie. 

Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit de  daarin,  bij  de  overeenkomstige  attribuutsoorten,  gespecificeerde indicatie. De indicatie wordt dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft. 

In  sommige  basisregistratiecatalogi  is  het  gebruikelijk  de  materiële historie te specificeren met specifieke ‘historie-attributen’. Van dergelijke attribuutsoorten  zien  we  hier  af.  Om  duidelijk  te  maken  om  welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

66 

**Indicatie formele historie** 

Indicatie of de formele historie van de relatiesoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de relatie (wanneer was de verandering bekend en is deze verwerkt). Voor relatiesoorten die deel uitmaken van een basisregistratie betreft dit de daarin, bij de overeenkomstige attribuutsoort, gespecificeerde indicatie. De indicatie wordt dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft. 

In sommige basisregistratiecatalogi is het gebruikelijk de formele historie te specificeren met specifieke ‘historie-attributen’. Van dergelijke attribuutsoorten  zien  we  hier  af.  Om  duidelijk  te  maken  om  welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

## **Aanduiding gebeurtenis** 

Indicatie of bij een opname, mutatie of verwijdering van de relatie de gebeurtenis aangeduid wordt  die aanleiding gaf tot verandering van de relatie  en  zo  ja,  de  specificatie  van  het  metagegeven  waarmee  de gebeurtenis aangeduid wordt: Gebeurtenisomschrijving. Dit metagegeven specificeren we in bijlage 1. 

In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te specificeren met specifieke ‘gebeurtenis-attributen’. Van dergelijke attribuutsoorten  zien  we  hier  af.  Om  duidelijk  te  maken  om  welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

**Aanduiding brondocument** 

**Indicatie in onderzoek** 

Indicatie of bij een opname, mutatie of verwijdering van de relatie het brondocument aangeduid wordt op basis waarvan de verandering van de relatie heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Documentsoort, Documenthouder. Deze metagegevens specificeren we in bijlage 1. In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te specificeren  met  specifieke  ‘brondocument-attributen’.  Van  dergelijke attribuutsoorten  zien  we  hier  af.  Om  duidelijk  te  maken  om  welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

De indicatie of te bevragen  is dat er twijfel is of is geweest aan de juistheid van de relatie en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de relatie. Dit metagegeven specificeren we in bijlage 1. In sommige basisregistratiecatalogi is het gebruikelijk deze indicatie te specificeren  met  specifieke  ‘in-onderzoek-attributen’.  Van  dergelijke attribuutsoorten  zien  we  hier  af.  Om  duidelijk  te  maken  om  welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de indicatie. 

> **Aanduiding strijdigheid/nietigheid** De aanduiding of te bevragen is dat de relatie strijdig met de openbare orde dan wel nietig is. Dit metagegeven specificeren we in bijlage 1. In sommige basisregistratiecatalogi is het gebruikelijk deze aanduiding te specificeren met specifieke ‘strijdigheid/nietigheid-attributen’. Van dergelijke attribuutsoorten zien we hier af. Om duidelijk te maken om welke attribuutsoorten in welke basisregistratie het gaat, geven we dit aan in de aanduiding. 

67 

## **Indicatie kardinaliteit** 

Deze indicatie geeft aan hoeveel keer waarden van deze relatiesoort (i.c. relaties) kunnen voorkomen bij een object van het betreffende objecttype:. 

0-1: is soms niet beschikbaar 

1-1: is altijd beschikbaar 

0-N: is niet altijd beschikbaar, kunnen meerdere relaties zijn 

1-N: is altijd beschikbaar, kunnen meerdere relaties zijn N-M: is niet altijd beschikbaar, kunnen meerdere relaties zijn tussen objecten van hetzelfde objecttype. 

De kardinaliteit van de inverse relatie geven we tussen haken aan. 

Indien een relatiesoort deel uit maakt van een groepsattribuutsoort, dan wordt de kardinaliteit vermeld van de relatiesoort binnen de groepattribuutsoort. Voor de uiteindelijke kardinaliteit van de relatiesoort moet  ook  rekening  gehouden  worden  met  de  kardinaliteit  van  het groepsattribuutsoort. 

## **Indicatie authentiek** 

**Regels relatiesoort** 

Aanduiding of de attribuutsoort waarvan de relatiesoort is afgeleid, een authentiek gegeven (attribuutsoort) betreft. 

Optionaliteitsregels of waardebeperkende regels zoals gespecificeerd in de desbetreffende catalogus. De regels worden dan ook alleen vermeld indien het een door KING toegevoegde relatiesoort betreft.. 

68 

## **4.1. Besluit** 

## **Attribuutsoort Besluitidentificatie** 

**Naam attribuutsoort** 

Besluitidentificatie 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0014 

**XML-tag attribuutsoort Definitie attribuutsoort** 

identificatie 

Identificatie van het besluit. 

**Herkomst definitie attribuutsoort** 

GFO Zaken 2004 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

Het betreft de identificatie of ook wel nummer dat aan het besluit is toegekend door de organisatie die het besluit heeft genomen. Het betreft de attribuutsoort Beschikkingidentificatie in het GFO Zaken 2004. 

Formaat: AN50 

Waardenverzameling: 1e 4 posities: gemeentecode van de gemeente die verantwoordelijk  is  voor  de  genomen  besluit;; pos.  5 – 50:  alle  alfanumerieke  tekens  m.u.v. diacrieten 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Besluitdatum** 

## **Naam attribuutsoort** 

Besluitdatum 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

GFO Zaken 2004 0004 datumBeslissing 

De beslisdatum (AWB) van het besluit. 

69 

## **Herkomst definitie attribuutsoort** 

## GFO Zaken 2004 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

1 juni 2008 

Het betreft de attribuutsoort Beschikkingsdatum in het GFO Zaken 2004. 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Besluittoelichting** 

> **Naam attribuutsoort** Besluittoelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0003 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Toelichting bij het besluit. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** De (samenvatting van de) toelichting op het besluit zoals veelal vermeld in de besluittekst. Het betreft de attribuutsoort Beschikkingtoelichting in het GFO  Zaken 2004. 

**Domein attribuutsoort Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee 

Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

70 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** - 

0-1 

Gemeentelijk basisgegeven 

## **Attribuutsoort Ingangsdatum** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Ingangsdatum 

GFO Zaken 2004 

0008 

ingangsdatumWerking 

Ingangsdatum van de werkingsperiode van het besluit. 

GFO Zaken 2004 

1 juni 2008 

Het betreft de attribuutsoort Ingangsdatum (van BESCHIKKING)  in het GFO Zaken 2004. 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

## Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

1-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Vervaldatum** 

> **Naam attribuutsoort** Vervaldatum 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0009 

> **XML-tag attribuutsoort** einddatumWerking 

71 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Datum waarop de werkingsperiode van het besluit eindigt. 

GFO Zaken 2004 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

De werkingsperiode is inclusief de opgeven datum. 

Het betreft de attribuutsoort  Vervaldatum (van  BESCHIKKING)  in het GFO Zaken 2004. 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

## Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Vervalreden** 

**Naam attribuutsoort** 

Vervalreden 

**Herkomst attribuutsoort** 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

vervalreden 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De omschrijving die aangeeft op grond waarvan het besluit is of komt te vervallen. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

De attribuutsoort geeft aan wat de reden is van het vervallen van het besluit op de vervaldatum. Het kan zijn dat het besluit slechts voor een beperkte periode geldig is. Dan zal de vervaldatum veelal al bij de creatie van  het  besluit  bekend  zijn.  Het  kan  ook  zijn  dat  het  besluit  later ingetrokken  is, bijvoorbeeld  vanwege  gewijizigde  omstandigheden  (de betrokkene op wie het besluit van toepassing is, is overleden) of vanwege een toegekend bezwaar. In die gevallen is er veelal een gerelateerde zaak die onder meer tot gevolg heeft dat het besluit ingetrokken is. 

72 

> **Domein attribuutsoort** Formaat: X40 Waardenverzameling: Besluit met tijdelijke werking Besluit ingetrokken door overheid Besluit ingetrokken o.v.v. belanghebbende 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Publicatiedatum** 

> **Naam attribuutsoort** Publicatiedatum 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0013 

> **XML-tag attribuutsoort** datumPublicatie 

> **Definitie attribuutsoort** Datum waarop het besluit gepubliceerd wordt. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het betreft de attribuutsoort Publicatiedatum (van BESCHIKKING) in het GFO Zaken 2004. 

> **Domein attribuutsoort** Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

73 

## **Regels attribuutsoort** 

- 

## **Attribuutsoort Verzenddatum** 

## **Naam attribuutsoort** 

Verzenddatum 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0015 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

datumVerzending 

Datum waarop het besluit verzonden is. 

GFO Zaken 2004 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

1 juni 2008 

Het betreft de attribuutsoort Verzenddatum (van BESCHIKKING) in het GFO Zaken 2004. 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

**Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Uiterlijke reactiedatum** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Uiterlijke reactiedatum 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

datumUiterlijkeReactie 

De datum tot wanneer verweer tegen het besluit mogelijk is. 

## KING 

1 juni 2008 

74 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

De reactiedatum valt op zich af te leiden met behulp van andere attributen zoals Besluittype.Reactietermijn en Besluitdatum. De reactiedatum is hier als  attribuutsoort  opgenomen  om  deze  datum  expliciet  te  kunnen communiceren. Zodoende hoeven partijen niet telkens deze datum zelf af te leiden (rekening houdend met weekend- en feestdagen) en hoeven zij niet te beschikken over de desbetreffende besluittype-attributen. 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

0-1 

Gemeentelijk basisgegeven 

Afleidbaar gegeven (uit BESLUITTYPE.Reactietermijn en BESLUIT.Besluitdatum) 

## **Relatiesoort BESLUIT is uitkomst van ZAAK** 

## **Naam relatiesoort** 

BESLUIT is uitkomst van ZAAK 

**Herkomst relatiesoort** 

**Code relatiesoort** 

KING op basis van GFO Zaken 2004 

## RES 

**Definitie relatiesoort Herkomst definitie relatiesoort** 

Aanduiding van de ZAAK waarbinnen het BESLUIT genomen is. 

## KING 

**Datum opname relatiesoort Toelichting relatiesoort** 

1 juni 2008 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

75 

## **Regels relatiesoort** 

- 

## **Relatiesoort BESLUIT kan vastgelegd zijn als DOCUMENT** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

BESLUIT kan vastgelegd zijn als DOCUMENT 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

Aanduiding van het (de) DOCUMENT(en) waarin het BESLUIT beschreven is. 

KING 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** Besluiten 

Besluiten worden veelal schriftelijk vastgelegd maar kunnen ook mondeling genomen zijn. Deze relatie verwijst naar het document waarin het besluit op schrift gesteld is, indien van toepassing.  Mogelijkerwijs is het besluit in meerdere afzonderlijke documenten vastgelegd of zijn in één document meerdere besluiten vastgelegd. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-M; N-M-relatie) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort BESLUIT is van BESLUITTYPE** 

> **Naam relatiesoort** BESLUIT is van BESLUITTYPE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Aanduiding van de aard van het BESLUIT. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

76 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

77 

## **4.2. Besluittype** 

## **Attribuutsoort Besluittype-omschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Besluittype-omschrijving 

GFO Zaken 2004 

**Code attribuutsoort** 

0002 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

omschrijving 

Omschrijving van de aard van BESLUITen van het BESLUITTYPE. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

Het gaat hier om een korte omschrijving van de aard van het besluit, ook wel besluitnaam genoemd. Voorbeelden: Lichte bouwvergunning, Kapvergunning, Ontheffing geluidhinder en Monumentensubsidie. Het betreft de attribuutsoort Beschikkingomschrijving in het GFO Zaken 2004. 

Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Besluittype-omschrijving generiek** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Besluittype-omschrijving generiek 

KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** omschrijvingGeneriek **Definitie attribuutsoort** 

Algemeen gehanteerde omschrijving van de aard van BESLUITen van het BESLUITTYPE 

**Herkomst definitie attribuutsoort** 

KING 

78 

## **Datum opname attribuutsoort** 

1 juni 2008 

**Toelichting attribuutsoort** 

Het gaat hier om een korte omschrijving van de aard van het besluit, ook wel besluitnaam genoemd, zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Besluittype-omschrijving. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Besluitcategorie** 

> **Naam attribuutsoort** Besluitcategorie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** categorie 

> **Definitie attribuutsoort** Typering van de aard van BESLUITen van het BESLUITTYPE. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het gaat hier om  de  indeling  van  besluittypen  naar categorien  zoals Vergunning, Ontheffing en Subsidie, 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: gebaseerd op de AWB 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

79 

## **Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Reactietermijn** 

## **Naam attribuutsoort** 

## **Herkomst attribuutsoort** 

Reactietermijn 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

reactietermijn 

Het  aantal  dagen,  gerekend  vanaf  de  verzend-  of  publicatiedatum, waarbinnen verweer tegen een besluit van het besluittype mogelijk is. KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

De telling begint bij de werkdag volgend op de verzend- of publicatiedatum. 

Formaat: N3 

Waardenverzameling: 0-999 werkdagen 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Publicatie-indicatie** 

> **Naam attribuutsoort** Publicatie-indicatie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** publicatieIndicatie **Definitie attribuutsoort** 

Aanduiding of BESLUITen van dit BESLUITTYPE gepubliceerd moeten worden. 

80 

## **Herkomst definitie attribuutsoort** 

## KING 

## **Datum opname attribuutsoort** 

## 1 juni 2008 

**Toelichting attribuutsoort** 

Het gaat hier niet alleen om de wettelijke verplichting tot publicatie maar ook om de eigen keuze van de organisatie die besluiten van dit type neemt. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1 Waardenverzameling: J, N 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Publicatietekst** 

> **Naam attribuutsoort** Publicatietekst 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** publicatieTekst 

> **Definitie attribuutsoort** De generieke tekst van de publicatie van BESLUITen van dit BESLUITTYPE 

**Herkomst definitie attribuutsoort** 

KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

81 

## **Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Publicatietermijn** 

## **Naam attribuutsoort** 

## **Herkomst attribuutsoort** 

Publicatietermijn 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

## publicatieTermijn 

Het aantal dagen, gerekend vanaf de verzend- of publicatiedatum, dat BESLUITen van dit BESLUITTYPE gepubliceerd moeten blijven. 

KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

De telling begint bij de werkdag volgend op de verzend- of publicatiedatum. 

Formaat: N3 

Waardenverzameling: 0 - 999 werkdagen 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis Aanduiding brondocument** 

Nee 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum begin geldigheid besluittype** 

> **Naam attribuutsoort** Datum begin geldigheid besluittype 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop het BESLUITTYPE is ontstaan. 

> **Herkomst definitie attribuutsoort** KING 

82 

## **Datum opname attribuutsoort** 

29 mei 2009 

## **Toelichting attribuutsoort** 

Met  deze  datum  wordt  aangegeven  vanaf  wanneer  het  besluittype bestaat en toegepast kan worden. 

## **Domein attribuutsoort** 

OnvolledigeDatum 

Formaat: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

1-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Datum einde geldigheid besluittype** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum einde geldigheid besluittype 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

einddatumObject 

De datum waarop het BESLUITTYPE is opgeheven. 

## KING 

29 mei 2009 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Met deze datum wordt aangegeven vanaf wanneer het besluittype niet meer bestaat en niet meer toegepast kan worden. Formaat: OnvolledigeDatum 

Nee 

## **Indicatie formele historie** 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

83 

## **Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen  onder  'Datum  begin  geldigheid  besluittype’  kan  in  de registratie worden opgenomen. 

## **Relatiesoort BESLUITTYPE heeft BESLUITen** 

> **Naam relatiesoort** BESLUITTYPE heeft BESLUITen 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Verwijzing naar de BESLUITen van dit BESLUITTYPE. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

84 

## **4.3. Betrokkene** 

Zie het RSGB voor de attribuutsoorten van de aan het RSGB ontleende specialisaties van BETROKKENE 

## **Relatiesoort BETROKKENE oefent uit ROL** 

> **Naam relatiesoort** BETROKKENE oefent uit ROL 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De ROLlen die BETROKKENE heeft in de zaken waarin BETROKKENE een ROL speelt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** Een betrokkene kan vele rollen hebben in diverse zaken. Voor externe betrokkenen  zal  het  veelal  gaan  om  de  rol  als  aanvrager,  direct betrokkene of geïnteresseerde. Medewerkers van de zaakbehandelende organisatie(s) oefenen (tevens) rollen uit ter behandeling van de zaak. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Objecttype VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE** 

## **Relatiesoort VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE huisvest ORGANISATORISCHE EENHEID** 

> **Naam relatiesoort** VESTIGING  VAN   ZAAKBEHANDELENDE  ORGANISATIE  huisvest ORGANISATORISCHE EENHEID 

> **Herkomst relatiesoort** KING 

**Herkomst relatiesoort Code relatiesoort** 

> **Definitie relatiesoort** De ORGANISATORISCHE EENHEID die haar activiteiten uitvoert in de VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE 

85 

## **Herkomst definitie relatiesoort** 

## KING 

**Datum opname relatiesoort Toelichting relatiesoort** 

## 17 mei 2010 

Met deze relatiesoort wordt voor vestigingen van de organisatie die zaken behandelt  gemodelleerd  welke  organisatorische  eenheden  (afdelingen e.d.) binnen die vestiging c.q. op die locatie werkzaam zijn. Aangezien de relatie alleen gemodelleerd is voor de VESTIGING VAN ZAAKBEHANDELENDE  ORGANISATIEs worden  binnen  het  RGBZ organisatorische eenheden en hun medewerkers niet uitgewisseld voor organisaties  die  alleen  op  andere  wijze  betrokken  zijn  bij  zaken bijvoorbeeld de aanvrager van een vergunning. 

## **Indicatie materiële historie** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1 -N (vice versa 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

86 

## **4.4. Document** 

## **Attribuutsoort Documentidentificatie** 

## **Naam attribuutsoort** 

Documentidentificatie 

**Herkomst attribuutsoort** 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## identificatie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Een binnen een gegeven context ondubbelzinnige referentie naar het document. 

KING op basis van de Dublin Core 

## 1 juni 2008 

Het gaat om een uniek kenmerk gevormd door een reeks letters of cijfers, dat het document  identificeert Het betreft  het Dublin  Core  metadataelement ‘Identifier’ met als toelichting: Recommended best practice is to identify the resource by means of a string or number conforming to a formal identification system. Formal identification systems include but are not limited to the Uniform Resource Identifier (URI) (including the Uniform Resource  Locator (URL)),  the  Digital  Object Identifier (DOI), and  the International Standard Book Number (ISBN).. 

Formaat: AN40 

Waardenverzameling: 1e 4 posities: gemeentecode van de gemeente die het document in haar registratie heeft opgenomen; pos.  5 – 40:  alle  alfanumerieke  tekens  m.u.v. diacrieten 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documentcreatiedatum** 

> **Naam attribuutsoort** Documentcreatiedatum 

**Herkomst attribuutsoort** 

KING op basis van de Dublin Core 

87 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## creatiedatum 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Een datum of een gebeurtenis in de levenscyclus van het document. 

KING op basis van de Dublin Core 

1 juni 2008 

Deze datum verwijst gewoonlijk naar de creatie van het document. Het betreft  het  Dublin  Core  metadata-element  ‘Date’  met  als  toelichting: Typically, Date will be associated with the creation or availability of the resource. Recommended best practice for encoding the date value is defined in a profile of ISO 8601 (W3CDTF) and includes (among others) dates of the form YYYY-MM-DD. 

Formaat: Datum (JJJJMMDD) 

Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit** 1-1 

Nee 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documentontvangstdatum** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Documentontvangstdatum 

KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** ontvangstdatum **Definitie attribuutsoort** 

De datum waarop het DOCUMENT ontvangen is. 

**Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## 1 juni 2008 

Het gaat hier om de datum waarop het document ontvangen is door de zaakbehandelende organisatie(s), dus niet door een specifieke afdeling of medewerker daarvan. 

88 

## **Domein attribuutsoort** 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op, voor of na de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Verplicht te registreren voor documenten die van buiten de zaakbehandelende organisatie(s) ontvangen zijn 

## **Attribuutsoort Documenttitel** 

> **Naam attribuutsoort** Documenttitel 

> **Herkomst attribuutsoort** KING op basis van de Dublin Core **Code attribuutsoort** 

> **XML-tag attribuutsoort** titel 

> **Definitie attribuutsoort** De naam waaronder het document formeel bekend is. 

> **Herkomst definitie attribuutsoort** KING op basis van de Dublin Core 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het betreft het Dublin Core metadata-element ‘Title’ met als toelichting: Typically, Title will be a name by which the resource is formally known. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

89 

## **Attribuutsoort Documentbeschrijving** 

## **Naam attribuutsoort** 

## **Herkomst attribuutsoort** 

Documentbeschrijving 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

beschrijving 

Een generieke beschrijving van de inhoud van het document. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

KING op basis van de Dublin Core 

1 juni 2008 

Het  betreft  het  Dublin  Core  metadata-element  ‘Description’  met  als toelichting: Examples of Description include, but are not limited to, an abstract, table  of contents, reference to a  graphical  representation of content, or free-text account of the content. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Document verzenddatum** 

> **Naam attribuutsoort** Document verzenddatum 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** verzenddatum **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

De datum waarop het DOCUMENT verzonden is. 

1 juni 2008 

90 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

Het gaat hier om de verzenddatum zoals deze op het document vermeld is (indien  van  toepassing),  voor  zowel inkomende als uitgaande documenten. 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op, voor of na de huidige datum en tijd Nee 

**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Vertrouwelijk aanduiding** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Vertrouwelijk aanduiding 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

vertrouwelijkAanduiding 

Aanduiding van de mate waarin het DOCUMENT voor de openbaarheid bestemd is. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst  bijzondere informatie (VIRBI). 

91 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN20|
||Waardenverzameling: ZEER  GEHEIM  (indien  kennisnemen  door  niet||
|||gerechtigden zeer ernstige schade kan|
|||toebrengen aan het belang van de Staat of|
|||zijn bondgenoten)|
|||GEHEIM (indien kennisnemen door niet|
|||gerechtigden ernstige schade kan toebrengen|
|||aan het belang van de Staat of zijn|
|||bondgenoten)|
|||CONFIDENTIEEL (indien kennisnemen door niet|
|||gerechtigden schade kan toebrengen aan het|
|||belang van de Staat of zijn bondgenoten)|
|||VERTROUWELIJK (indien kennisnemen door niet|
|||gerechtigden nadeel kan toebrengen aan het|
|||belang van één of meer zaakbehandelende|
|||organisaties, betrokkenen bij de zaak en/of|
|||andere publliekrechtelijke organisaties)|
|||ZAAKVERTROUWELIJK (indien kennisnemen|
|||door anderen dan betrokkenen bij de zaak|
|||nadeel kan toebrengen aan het belang van|
|||één of meer zaakbehandelende organisaties,|
|||betrokkenen bij de zaak en/of andere|
|||publliekrechtelijke organisaties)|
|||INTERN (indien kennisnemen door anderen dan|
|||medewerkers van de zaakbehandelende|
|||organisatie(s) nadeel kan toebrengen aan het|
|||belang van één of meer zaakbehandelende|
|||organisaties, betrokkenen bij de zaak en/of|
|||andere publliekrechtelijke organisaties)|
|||BEPERKT OPENBAAR (indien kennisnemen door|
|||anderen dan medewerkers van de|
|||zaakbehandelende<br>organisatie(s)|
|||betrokkenen bij de zaak nadeel kan|
|||toebrengen aan het belang van één of meer|
|||zaakbehandelende organisaties, betrokkenen|
|||bij  de  zaak  en/of andere  publliekrechtelijke|
|||organisaties)|
|||OPENBAAR (in alle andere gevallen)|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



92 

## **Attribuutsoort Documentauteur** 

## **Naam attribuutsoort** 

Documentauteur 

## **Herkomst attribuutsoort** 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

auteur 

De persoon of organisatie die in de eerste plaats verantwoordelijk is voor het creëren van de inhoud van het document. 

KING op basis van de Dublin Core 

1 juni 2008 

Het  kan  zowel  een  medewerker  of organisatorische  eenheid  van  de zaakbehandelende organisatie betreffen als een externe  partij (persoon of organisatie). 

Het betreft het Dublin Core metadata-element ‘Creator’ met als toelichting: Examples of Creator include a person, an organization, or a service. Typically, the name of a Creator should be used to indicate the entity. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort DOCUMENT is van DOCUMENTTYPE** 

> **Naam relatiesoort** DOCUMENT is van DOCUMENTTYPE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Aanduiding van de aard van het DOCUMENT. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

93 

## **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort DOCUMENT betreft ZAAKDOCUMENTen** 

## **Naam relatiesoort** 

DOCUMENT betreft ZAAKDOCUMENTen 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De ZAAKen waaraan het DOCUMENT is gerelateerd. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

De relatie van DOCUMENT naar ZAAK loopt via het relatie-objecttype ZAAKDOCUMENT.  Met  de  relatiesoort  ‘DOCUMENT  betreft  ZAAKDOCUMENTen’ geven we aan welke ZAAKDOCUMENTen afgeleid zijn van het DOCUMENT. 

## **Indicatie materiële historie** 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

94 

## **Regels relatiesoort** 

Indien het DOCUMENT een SAMENGESTELD DOCUMENT betreft of een ENKELVOUDIG DOCUMENT betreft dat geen deel uit maakt van een SAMENGESTELD DOCUMENT, dan dient minimaal één relatie naar een  ZAAKDOCUMENT  gelegd  te  zijn.  Indien  het  DOCUMENT  een ENKELVOUDIG  DOCUMENT  betreft  dat  deel  uit  maakt  van  een SAMENGESTELD DOCUMENT, dan heeft dit DOCUMENT geen relatie naar  het  ZAAKDOCUMENT  waaraan  het  DOCUMENT  zijnde  het SAMENGESTELD DOCUMENT gerelateerd is . 

## **Relatiesoort DOCUMENT kan vastlegging zijn van BESLUIT** 

**Naam relatiesoort** 

DOCUMENT kan vastlegging zijn van BESLUIT 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

> **Definitie relatiesoort** Aanduiding van het BESLUIT waarvan het DOCUMENT de beschrijving bevat. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** Zie de toelichting bij de tegenhanger van deze relatiesoort: BESLUIT kan vastgelegd zijn als DOCUMENT. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-M; N-M-relatie) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

95 

## **4.5. Documenttype** 

## **Attribuutsoort Documenttype-omschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Documenttype-omschrijving 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

omschrijving 

Omschrijving van de aard van DOCUMENTen van dit DOCUMENTTYPE. 

KING op basis van de Dublin Core 

1 juni 2008 

Het gaat hier om een korte omschrijving van de aard van het document, ook wel documentsoort genoemd. Voorbeelden: Bouwaanvraag, Kapvergunning, Taxatieverslag, Geboorte-akte.. 

Het betreft het Dublin Core metadata-element ‘Subject’ met als toelichting:  Typically,  Subject  will  be  expressed  as  keywords,  key phrases, or classification codes that describe a topic of the resource. Recommended  best  practice  is  to  select  a  value  from  a  controlled vocabulary or formal classification scheme. 

Aan te bevelen is dus om aan te sluiten bij een (landelijke) domeinwaardencatalogus zoals gemodelleerd met documenttypeomschrijvijng generiek 

Let op dat het hier alleen om het onderwerp gaat; trefwoorden worden vastgelegd in Documenttypetrefwoord. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documenttype-omschrijving generiek** 

> **Naam attribuutsoort** Documenttype-omschrijving generiek 

> **Herkomst attribuutsoort** KING 

96 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

omschrijvingGeneriek 

Algemeen gehanteerde omschrijving van het DOCUMENTTYPE 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

## KING 

1 juni 2008 

Het gaat hier om een korte omschrijving van de aard van een document, ook wel documentnaam genoemd, zoals deze landelijk wordt toegepast. Deze  kan  afwijken  van  de  door  de  zaakbehandelende  organisatie(s) gehanteerde naam, de Documenttype-omschrijving. De domeinwaardenzijn opgenomen in een specifieke tabel. De desbetreffende waarden zijn vermeld in het document 'RGBZ domeintabellen'. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: zie DTG-tabel. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documentcategorie** 

## **Naam attribuutsoort** 

> **Naam attribuutsoort** Documentcategorie 

> **Herkomst attribuutsoort** KING op basis van de Dublin Core **Code attribuutsoort** 

> **XML-tag attribuutsoort** categorie 

> **Definitie attribuutsoort** Typering van de aard van DOCUMENTen van dit DOCUMENTTYPE. 

> **Herkomst definitie attribuutsoort** KING op basis van de Dublin Core 

> **Datum opname attribuutsoort** 1 juni 2008 

1 juni 2008 

97 

## **Toelichting attribuutsoort** 

Voorbeelden hiervan zijn ‘Vergunning’, ‘Subsidie-aanvraag’, ‘Onderzoeksrapport’, Besluit. 

Het betreft het Dublin Core metadata-element ‘Type’ met als toelichting: Type includes terms describing general categories, functions, genres, or aggregation levels for content. Recommended best practice is to select a value  from  a  controlled  vocabulary  (for  example,  the  DCMI  Type Vocabulary (DCT)). To describe the physical or digital manifestation of the resource, use the Format element. 

Aan te bevelen is dus om te komen tot een (landelijke) domeinwaardencatalogus. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documenttypetrefwoord** 

> **Naam attribuutsoort** Documenttypetrefwoord 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** trefwoord 

> **Definitie attribuutsoort** Trefwoord(en)  waarmee  DOCUMENTen  van  het  DOCUMENTTYPE kunnen worden gekarakteriseerd. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN30 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

98 

## **Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum begin geldigheid documenttype** 

## **Naam attribuutsoort** 

Datum begin geldigheid documenttype 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** ingangsdatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 oktober 2009 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

De datum waarop het DOCUMENTTYPE is ontstaan. 

Met deze datum wordt aangegeven vanaf wanneer het documenttype bestaat en toegepast kan worden. Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid documenttype** 

> **Naam attribuutsoort** Datum einde geldigheid documenttype 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumObject 

99 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

De datum waarop het DOCUMENTTYPE is opgeheven. 

## KING 

**Datum opname attribuutsoort** 

1 oktober  2009 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

**Indicatie materiële historie** 

Met deze datum wordt aangegeven vanaf wanneer het documenttype niet meer bestaat en niet meer toegepast kan worden. Formaat: OnvolledigeDatum 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

**Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek Regels attribuutsoort** 

Gemeentelijk basisgegeven 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen  onder  'Datum  begin  geldigheid  documenttype’  kan  in  de registratie worden opgenomen. 

## **Relatiesoort DOCUMENTTYPE heeft DOCUMENTen** 

## **Naam relatiesoort** 

DOCUMENTTYPE heeft DOCUMENTen 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

Verwijzing naar de DOCUMENTENen van dit DOCUMENTTYPE 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

100 

**Indicatie authentiek Regels relatiesoort** 

Gemeentelijk basisgegeven 

- 

101 

## **4.6. Enkelvoudig document** 

## **Attribuutsoort Documentformaat** 

## **Naam attribuutsoort** 

Documentformaat 

**Herkomst attribuutsoort** 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

formaat 

De digitale manifestatie van het ENKELVOUDIG DOCUMENT. 

KING op basis van de Dublin Core 

1 juni 2008 

Het gaat hier om het bestandsoort van het enkelvoudig document, zoals ‘pdf’, ‘odf’, ‘xml’, ‘gml’, etc. Het betreft het Dublin Core metadata-element ‘Format’ met als toelichting: Typically, Format will include the media-type or  dimensions  of  the  resource.  Format  may  be  used  to  identify  the software, hardware, or other equipment needed to display or operate the resource. Examples of dimensions include size and duration. Recommended  best  practice  is  to  select  a  value  from  a  controlled vocabulary (for example, the list of Internet Media Types (MIME) defining computer media formats). 

Formaat: AN10 

Waardenverzameling: bestaande bestandsformaatbenamingen 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Het  Documentformaay  moet  van  een  waarde  voorzien  zijn  indien Bestandsnaam geen  waarde  heeft  of  indien  uit  de  waarde van Bestandsnaam geen geldig Documentformaat af te leiden is. 

## **Attribuutsoort Documenttaal** 

> **Naam attribuutsoort** Documenttaal 

> **Herkomst attribuutsoort** KING op basis van de Dublin Core **Code attribuutsoort** 

102 

## **XML-tag attribuutsoort** 

taal 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

Een taal van de intellectuele inhoud van het ENKELVOUDIG DOCUMENT 

KING op basis van de Dublin Core 

1 juni 2008 

Het  betreft  het  Dublin  Core  metadata-element  ‘Language’  met  als toelichting: Recommended best practice is to use RFC 3066 (RFC3066), which, in conjunction with ISO 639 (ISO639), defines two- and three-letter primary language tags with optional subtags. Examples include “en” or “eng” for English, “akk" for Akkadian, and “en-GB” for English used in the United Kingdom. 

Formaat: AN20 

Waardenverzameling: nader te bepalen (zie toelichting) 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Nee 

Nee 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Documentversie** 

> **Naam attribuutsoort** Documentversie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** versie 

**Definitie attribuutsoort** 

Aanduiding van de bewerkingsfase van het ENKELVOUDIG DOCUMENT 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het gaat hier om een versienummer zoals ‘0.2’ en 1.0’. Ofschoon we er voor gekozen hebben om zowel dit attribuuttype als het attribuuttype  Documentstatus  optioneel  te  verklaren, ware  het  aan  te bevelen bij elk documemt in ieder geval één van beide attributen van een waarde te voorzien. 

**Domein attribuutsoort** 

Formaat: 

AN5 

Waardenverzameling: alle alfanumerieke tekens m.u.v. diacrieten 

103 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Attribuutsoort Documentstatus** 

## **Naam attribuutsoort** 

Documentstatus 

**Herkomst attribuutsoort** 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

status 

Aanduiding van de stand van zaken van een ENKELVOUDIG DOCUMENTDOCUMENT. 

KING 

**Datum opname attribuutsoort** 

1 juni 2008 

**Toelichting attribuutsoort** 

Het  gaat  hier  om  aanduidingen  zoals  ‘in  bewerking’,  ‘concept’  en ‘definitief’.  Dus niet ‘afgehandeld’. Immers, zaken worden afgehandeld, documenten niet. Wel spelen documenten daarbij een rol. 

Ofschoon we er voor gekozen hebben om zowel dit attribuuttype als het attribuuttype  Documentversie  optioneel  te  verklaren, ware  het  aan  te bevelen  bij  elk  enkelvoudig  documemt in  ieder geval  één  van  beide attributen van een waarde te voorzien. 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN20|
||Waardenverzameling:|alle a|
|**Indicatie materiële historie**|Ja||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|0-1||



Waardenverzameling: alle alfanumerieke tekens m.u.v. diacrieten 

104 

## **Indicatie authentiek** 

Gemeentelijk basisgegeven 

## **Regels attribuutsoort** 

## **Attribuutsoort Documentinhoud** 

> **Naam attribuutsoort** Documentinhoud 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** inhoud **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

Datgene wat in een ENKELVOUDIG DOCUMENT wordt meegedeeld. 

Het  gaat  hier  om  de  inhoud  van  het  enkelvoudig  document  (in  het spraakgebruik  ‘het  document’)  in  het  formaat  zoals  vastgelegd  in Documentformaat. Veelal  gaat het om de  tekst van  een  enkelvoudig document (bijvoorbeeld in pdf-formaat). Het kan bijvoorbeeld ook een afbeelding (in bijvoorbeeld jpg-formaat) of een kaart (in bijvoorbeeld gmlformaat) betreffen. 

De  mogelijkheid  bestaat  dat  de  documentinhoud  in  een  (al  dan  niet separaat) bestand wordt uitgewisseld of dat er alleen verwezen wordt naar de locatie waar zich de documentinhoud bevindt. Hiertoe zijn de attribuutsoorten Bestandsnaam respectievelijk Documentlink opgenomen. **Domein attribuutsoort** Formaat: desbetreffend Documentformaat Waardenverzameling: n.v.t. **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** - 

105 

## **Attribuutsoort Documentlink** 

## **Naam attribuutsoort** 

Documentlink 

## **Herkomst attribuutsoort** 

## KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

## link 

De URL waarmee de documentinhoud op te vragen is. 

## KING 

## 22 mei 2009 

Vanwege vooral technische belemmeringen kan het voorkomen dat de attribuutsoort Documentinhoud geen waarde heeft d.w.z. dat de inhoud van het document ('het document' in het spraakgebruik) niet uitgewisseld wordt. Het attribuutsoort Documentlink verwijst dan naar de locatie waar de documentinhoud ('het document') zich bevindt en schept de mogelijkheid de documentinhoud ('het document') op te vragen. Een meer structurelere wijze om de documentinhoud op te vragen, is uiteraard met behulp van de Documentidentificatie. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: URL 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Bestandsnaam** 

> **Naam attribuutsoort** Bestandsnaam 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** bestandsnaam **Definitie attribuutsoort** 

De  naam  van  het  fysieke  bestand  waarin  de  documentinhoud  is vastgelegd. 

106 

## **Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

## 1 november 2009 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

Veelal zal de Documentinhoud uitgewisseld worden in de vorm van een fysiek bestand. De naam daarvan valt af te leiden uit de combinatie van Documenttitel en Documentformaat, gescheiden door een punt. Niet altijd is de zender van een bericht waarin het beoogd is de documentinhoud te leveren, in staat het formaat te bepalen. In dat geval wordt expliciet de naam van het bestand genoemd waarin zich de documentinhoud bevindt. De voorwaarde is dat de ontvanger uit de bestandsnaam het formaat kan afleiden. 

Formaat: AN255 

Waardenverzameling: alle in fysieke bestandsnamen toegestane tekens 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven **Regels attribuutsoort** 

Afleidbaar  uit  de  combinatie  van  Documenttitel  en  Documentformaat, gescheiden door een punt, mits beide attributen van een waarde zijn voorzien. Zo niet, dan is het attribuut Bestandsnaam van een waarde voorzien. Uit de bestandsnaam moet een geldig Documentformaat af te leiden zijn (laatste posities na de laatste punt in de bestandsnaam). Zo niet dan dient Documentformaat van een waarde te zijn voorzien. 

## **Relatiesoort ENKELVOUDIG DOCUMENT maakt deel uit van SAMENGESTELD DOCUMENT** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

ENKELVOUDIG  DOCUMENT  maakt  deel  uit  van  SAMENGESTELD DOCUMENT 

KING 

**Code relatiesoort** 

> **Definitie relatiesoort** De  verwijzing  naar  het  SAMENGESTELD  DOCUMENT  waarvan  het ENKELVOUDIG DOCUMENT met nog andere ENKELVOUDIGe DOCUMENTen, deel uitmaakt. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 1 juni 2008 

**Toelichting relatiesoort** 

Het gaat hier om enkelvoudige documenten die gezamenlijk eensamengesteld document vormen. De minimale groepsgrootte is twee. Zie verder de toelichting bij het objecttype en bij het objecttype Document. 

107 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 2-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

Indien een enkelvoudig document deel uit maakt van een samengesteld document, dan is het enkelvoudig document niet aan de zaak gerelateerd waaraan het samengesteld document gerelateerd is cq. het is via het samengesteld  document  aan  een  zaak  gerelateerd.  Wel  kan  het enkelvoudig document aan andere zaken gerelateerd zijn waarvoor het relevant is. 

108 

## **4.7. Medewerker** 

## **Attribuutsoort Medewerkeridentificatie** 

**Naam attribuutsoort** 

Medewerkeridentificatie 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0001 

**XML-tag attribuutsoort** 

identificatie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Een korte unieke aanduiding van de medewerker. 

KING op basis van GFO Zaken 2004 

1 juni 2008 

De zaakbehandelende organisatie(s) kan hier zelf een classificatie voor definiëren. 

Formaat: AN24 

Waardenverzameling: 1e 4 posities: gemeentecode van de gemeente zijnde de zaakbehandelende organisatie; pos.  5 – 24:  classificatie  bestaande  uit  alle alfanumerieke tekens m,u.v. diacrieten 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek** 

**Regels attribuutsoort** 

Nee 

1-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Achternaam** 

**Naam attribuutsoort** 

Achternaam 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0003 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

achternaam 

De  achternaam  zoals  de  medewerker  die  in  het  dagelijkse  verkeer gebruikt. 

GFO Zaken 2004 

109 

## **Datum opname attribuutsoort** 

1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort is overeenkomstig het attribuutsoort NatuurlijkPersoon.Geslachtsnaam  met dien verstande dat, in afwijking daarop, eventueel voorkomende voorvoegsels niet in de geslachtsnaam zijn opgenomen (zie attribuutsoort Voorvoegsel achternaam).. 

## **Domein attribuutsoort** 

Formaat: AN200 

Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 01-01-09 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum uit dienst** 

## **Naam attribuutsoort** 

Datum uit dienst 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0006 

> **XML-tag attribuutsoort** datumUitDienst **Definitie attribuutsoort** 

Een aanduiding van de datum waarop de arbeidsplaatsvervulling eindigt. 

**Herkomst definitie attribuutsoort** 

GFO-Personeel 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

1 juni 2008 

> **Domein attribuutsoort** Formaat: datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

110 

## **Indicatie kardinaliteit** 

0-1 

## **Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort E-mail adres** 

## **Naam attribuutsoort** 

E-mail adres 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

9516 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

emailadres 

Elektronisch postadres waaronder de medewerker in de regel bereikbaar is. 

GFO Zaken 2004 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

Het attribuutsoort is overeenkomstig het attribuutsoort Subject.Emailadres. 

Formaat: AN254 

Waardenverzameling: alle bestaande alfanumerieke tekens waarin zich, evenwel niet aan het begin en aan het eind, een ‘@’ moet bevinden. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

0-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Functie** 

> **Naam attribuutsoort** Functie 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0002 

> **XML-tag attribuutsoort** functie 

111 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

**Indicatie materiële historie Indicatie formele historie** 

De aanduiding van de taken, rechten en plichten die de medewerker heeft of heeft gehad binnen de zaakbehandelende organisatie. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

Van dit attribuut wordt (materiele) historie vastgelegd aangezien het van belang is in welke hoedanigheid de medewerker een rol in een zaak heeft vervuld. 

Formaat: AN50 Waardenverzameling: alle alfanumerieke tekens Ja 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Geslachtsaanduiding** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

**Code attribuutsoort** 

Geslachtsaanduiding 

GFO Zaken 2004 0410 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

geslachtsaanduiding 

Een aanduiding die aangeeft of de persoon een man of een vrouw is, of dat het geslacht nog onbekend is. 

GFO Zaken 2004 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

1 juni 2008 

Het attribuutsoort is overeenkomstig het attribuutsoort NatuurlijkPersoon.Geslachtsaanduiding Formaat: A1 Waardenverzameling: M:  Man V: Vrouw O: Onbekend 

Nee 

**Indicatie formele historie** 

**Aanduiding gebeurtenis** 

Nee Nee 

112 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Medewerkertoelichting** 

## **Naam attribuutsoort** 

> **Naam attribuutsoort** Medewerkertoelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0007 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Toelichting bij en/of over de medewerker. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 

Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens Nee Nee Nee Nee Nee 

**Indicatie materiële historie Indicatie formele historie** 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** - 

Nee 

0-1 Gemeentelijk basisgegeven 

## **Attribuutsoort Roepnaam** 

**Naam attribuutsoort Herkomst attribuutsoort Code attribuutsoort** 

Roepnaam GFO Zaken 2004 0005 

113 

## **XML-tag attribuutsoort** 

## roepnaam 

**Definitie attribuutsoort Herkomst definitie attribuutsoort** GFO Zaken 2004 **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

Naam waarmee de werknemer wordt aangesproken. 

> **Domein attribuutsoort** Formaat: AN30 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Telefoonnummer** 

> **Naam attribuutsoort** Telefoonnummer 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 9580 

> **XML-tag attribuutsoort** telefoonnummer 

> **Definitie attribuutsoort** Telefoonnummer waaronder de medewerker in de regel bereikbaar is. 

> **Herkomst definitie attribuutsoort** GFO-Basisgegevens 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort is overeenkomstig het attribuutsoort Subject.Telefoonnummer. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle bestaande alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

114 

> **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Voorletters** 

## **Naam attribuutsoort** 

Voorletters 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0211 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## voorletters 

De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen. 

GFO-Basisgegevens 

1 juni 2008 

Het attribuutsoort is overeenkomstig het attribuutsoort NatuurlijkPersoon.VoorlettersAanschrijving. 

Formaat: AN20 

Waardenverzameling: 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Voorvoegsel achternaam** 

> **Naam attribuutsoort** Voorvoegsel achternaam 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0004 

> **XML-tag attribuutsoort** voorvoegselAchternaam 

115 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), voorvoegseltabel, en door een spatie van de geslachtsnaam is gescheiden. 

GFO-Basisgegevens 

> **Datum opname attribuutsoort** 1 juni 2008 

**Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN10 Waardenverzameling: voorvoegseltabel GBA (tabel 36) 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels attribuutsoort** 

## **Relatiesoort MEDEWERKER hoort bij ORGANISATORISCHE EENHEID** 

> **Naam relatiesoort** MEDEWERKER hoort bij ORGANISATORISCHE EENHEID 

> **Herkomst relatiesoort** GFO Zaken 2004 **Code relatiesoort** 

> **Definitie relatiesoort** De ORGANISATORISCHE EENHEID waarvan de MEDEWERKER deel uitmaakt of deel heeft uitgemaakt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** Van deze relatie wordt (materiele) historie vastgelegd aangezien het van belang is in welke hoedanigheid de medewerker een rol in een zaak heeft vervuld. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

116 

## **Indicatie kardinaliteit** 

**Indicatie authentiek** 

**Regels relatiesoort** 

1-1 (vice versa: 0-N) 

Gemeentelijk basisgegeven 

- 

## **Relatiesoort MEDEWERKER is verantwoordelijk voor ORGANISATORISCHE EENHEID** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

MEDEWERKER is verantwoordelijk voor ORGANISATORISCHE EENHEID 

GFO Zaken 2004 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De ORGANISATORISCHE EENHEID waarvoor de MEDEWERKER uit hoofde  van  zijn  of  haar  functie  zorgt  (of  zorgde)  dat  deze  goed functioneert en daar rekenschap van geeft. 

KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

Van deze relatie wordt (materiele) historie vastgelegd aangezien het van belang is in welke hoedanigheid de medewerker een rol in een zaak heeft vervuld. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels relatiesoort** 

## **Relatiesoort MEDEWERKER is contactpersoon voor ORGANISATORISCHE EENHEID** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

MEDEWERKER is contactpersoon voor ORGANISATORISCHE EENHEID 

GFO Zaken 2004 

**Code relatiesoort** 

> **Definitie relatiesoort** De ORGANISATORISCHE EENHEID waarvoor MEDEWERKER anderen desgevraagd  in  contact  brengt  met  (andere)  medewerkers  van  deze ORGANISATORISCHE EENHEID. 

**Herkomst definitie relatiesoort** 

KING 

117 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort MEDEWERKER is verantwoordelijke voor ZAAKTYPE** 

**Naam relatiesoort Herkomst relatiesoort Code relatiesoort** 0008 **Definitie relatiesoort** 

MEDEWERKER is verantwoordelijke voor ZAAKTYPE 

KING op basis van GFO Zaken 2004 

De  MEDEWERKER  die  verantwoordelijk  is  voor  ZAAKen  van  het ZAAKTYPE. 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

KING op basis van het GFO Zaken 2004 

De relatiesoort is afgeleid van de  attribuutsoort Verantworordelijke bij Zaak in het GFO Zaken 2004. 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

118 

## **4.8. Object** 

## **Attribuutsoort Identificatie** 

## **Naam attribuutsoort** 

Identificatie 

**Herkomst attribuutsoort** 

## KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort** 

## identificatie 

**Definitie attribuutsoort** 

De unieke identificatie van het OBJECT 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

## KING 

## 29 mei 2009 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

Het betreft een afleidbaar gegeven dat is opgenomen om objecten te kunnen zoeken op hun identificatie. Deze is immers voor de verschillende specialisaties anders gespecificeerd. 

Formaat: 

AN50 

Waardenverzameling: de unieke aanduidingen van de objecttypen zijnde de specialisaties. 

**Indicatie materiële historie** 

## Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

**Indicatie kardinaliteit** 

1-1 

**Indicatie authentiek Regels attribuutsoort** 

## Afleidbaar gegeven 

Per  specialisatie  is  dit  de  unieke  aanduiding  van  het  desbetreffende objecttype. 

## **Attribuutsoort Naam** 

> **Naam attribuutsoort** Naam 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** naam 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

De benaming van het OBJECT indien dit een SUBJECT of specialisatie daarvan is. 

KING 

119 

## **Datum opname attribuutsoort** 

29 mei 2009 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om OBJECTEN zijnde subjecten te kunnen zoeken op hun benaming. Het betreft het overeenkomstige gegeven bij SUBJECT in het RSGB. 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

**Regels attribuutsoort** 

Zie voor de afleiding van dit gegeven ten eerste het overeenkomstige attribuutsoort  bij  SUBJECT  in  het  RSGB.  Verder  betreft  het  alle attribuutsoorten met de term 'naam' in de naam attribuutsoort voorzover genoemd in de specificaties van de objecttypen zijnde specialisaties van OBJECT in paragraaf 3.9. 

## **Attribuutsoort Adres binnenland** 

> **Naam attribuutsoort** Adres binnenland 

**Herkomst attribuutsoort** 

KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** adresBinnenland **Definitie attribuutsoort** 

De  aanduiding  van  het  adres  van  het  OBJECT  indien  dit  adres  in Nederland gelegen  is. 

**Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

## 27-04-09 

**Toelichting attribuutsoort** 

Het betreft een afleidbaar gegeven dat is opgenomen om objecten te kunnen zoeken op hun binnenlandse adres. Deze is immers voor de verschillende specialisaties anders gespecificeerd. 

Bij SUBJECTen of de specialisaties daarvan betreft dit het adres waar het SUBJECT verblijft dan wel bereikbaar is. 

**Domein attribuutsoort** 

Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

120 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Zie  voor  de  afleiding  van  dit  gegeven  v.w.b.  (specialisaties  van) SUBJECT het overeenkomstige attribuutsoort bij SUBJECT in het RSGB. Voor de specialisaties van OBJECT die een specialisatie betreffen van het BENOEMD OBJECT in het RSGB betreft het een groepattribuutsoort met de volgende afleidbare gegevens van of bij een ADRESSEERBAAR OBJECT AANDUIDING zijnde het hoofdadres: 

   - Adresseerbaar object aanduiding typering; 

   - WOONPLAATS.Woonplaatsnaam (van de WOONPLAATS behorende bij de OPENBARE RUIMTE bij de ADRESSEERBAAR OBJECT AANDUIDING); 

   - WOONPLAATS.Woonplaatsidentificatie (van de WOONPLAATS behorende bij de ADRESSEERBAAR OBJECT AANDUIDING); 

   - WOONPLAATS.Woonplaatsnaam (van de WOONPLAATS behorende bij de ADRESSEERBAAR OBJECT AANDUIDING); 

   - ADRESSEERBAAR OBJECT AANDUIDING.Postcode dan wel SUBJECT.Postadres postcode; 

   - Identificatiecode adresseerbaar object aanduiding; 

   - WOONPLAATS.Woonplaatsidentificatie (van de WOONPLAATS behorende bij de OPENBARE RUIMTE bij de ADRESSEERBAAR OBJECT AANDUIDING); 

   - OPENBARE RUIMTE.Identificatiecode openbare ruimte (van de OPENBARE  RUIMTE  bij  de   ADRESSEERBAAR  OBJECT AANDUIDING); 

   - GEMEENTELIJKE OPENBARE RUIMTE.Naam openbare ruimte (van de GEMEENTELIJKE OPENBARE RUIMTE bij de OPENBARE  RUIMTE  bij  de   ADRESSEERBAAR  OBJECT AANDUIDING); 

   - GEMEENTELIJKE  OPENBARE  RUIMTE.Straatnaam  (van  de GEMEENTELIJKE  OPENBARE  RUIMTE  bij  de  OPENBARE RUIMTE bij de  ADRESSEERBAAR OBJECT AANDUIDING); 

   - • Huisnummer; 

   - Huisletter; 

   - Huisnummertoevoeging, 

- en, indien het een OVERIG GEBOUWD OBJECT betreft tevens: 

   - OVERIG GEBOUWD OBJECT . Overig gebouwd object locatieaanduiding. 

Voor een HUISHOUDEN, NUMMERAANDUIDING, OVERIGE ADRESSEERBAAR OBJECTAANDUIDING en WOZ-OBJECT betreft het dezefde als de zojuist bij de ADRESSEERBAAR OBJECT AANDUIDING genoemde gegevens, voor het WOZ-object aangevuld met de Locatieomschrijving. 

121 

## **Attribuutsoort Adres buitenland** 

## **Naam attribuutsoort** 

Adres buitenland 

**Herkomst attribuutsoort** 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

adresBuitenland 

De aanduiding van het adres waar specialisaties van het OBJECT zijnde een  SUBJECT  dan  wel  een  specialisatie  daarvan,  verblijft  dan  wel bereikbaar is in het buitenland. 

KING 

> **Datum opname attribuutsoort** 29 mei 2009 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

Het betreft een afleidbaar gegeven dat is opgenomen om OBJECTEN zijnde subjecten te kunnen zoeken op hun eventuele buitenlandse adres. Het betreft het overeenkomstige gegeven bij SUBJECT in het RSGB. 

Waardenverzameling: alle alfanumerieke tekens 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven **Regels attribuutsoort** 

Zie voor de afleiding van dit gegeven het overeenkomstige attribuutsoort bij SUBJECT in het RSGB. 

## **Attribuutsoort Kadastrale aanduiding** 

## **Definitie attribuutsoort** 

Kadastrale aanduiding 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** kadastraleAanduiding **Definitie attribuutsoort** 

De kadastrale aanduiding van het OBJECT 

**Herkomst definitie attribuutsoort** 

KING 

122 

## **Datum opname attribuutsoort** 

## 29 mei 2009 

**Toelichting attribuutsoort** 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om objecten, indien van toepassing, te kunnen zoeken op hun kadastrale aanduiding. 

> **Domein attribuutsoort** Formaat: AN30 Waardenverzameling: 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Voor de objecttypen APPARTEMENTSRECHT, KADASTRAAL 

Voor de objecttypen APPARTEMENTSRECHT, KADASTRAAL PERCEEL  en   ZAKELIJK  RECHT  betreft  dit  een  groepattribuutsoort bestaande uit: 

- KADASTRALE ONROERENDE ZAAK . Kadastrale gemeentecode 

- KADASTRALE ONROERENDE ZAAK . Sectie 

- KADASTRALE ONROERENDE ZAAK . Perceelnummer 

- KADASTRAAL PERCEEL . Deelperceelnummer 

- APPARTEMENTSRECHT .  Appartementsindex. 

- Voor andere objecttypen is dit niet van toepassing. 

## **Attribuutsoort Geometrie** 

> **Definitie attribuutsoort** Geometrie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** geometrie 

> **Definitie attribuutsoort** De  minimaal  tweedimensionale  geometrische  representatie  van  het OBJECT. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 29 mei 2009 

> **Toelichting attribuutsoort** Het betreft een afleidbaar gegeven dat is opgenomen om objecten, indien van toepassing, ruimtelijk te kunnen zoeken.. 

> **Domein attribuutsoort** Formaat: GML Waardenverzameling: punt-, lijn- en vlakgeometrie 

> **Indicatie materiële historie** Nee 

123 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Afleidbaar gegeven 

> **Regels attribuutsoort** Het betreft voor de specialisatie cq. het objecttype: 

- APPARTEMENTSRECHT: de KADASTRAAL PERCEEL . Plaatscoordinaten perceel van het KADASTRAAL PERCEEL waarop het appartementencomplex staat waarvan het APPARTEMENTSRECHT  deel uit maakt; 

- BUURT: Buurtgeometrie; 

- GEMEENTE: Gemeentegeometrie; 

- GEMEENTELIJKE  OPENBARE  RUIMTE:  Geometrie  gemeentelijke openbare ruimte ; 

- HUISHOUDEN: 

   - de BENOEMD  TERREIN  . Geometrie  van de  LIGPLAATS of STANDPLAATS waarop het HUISHOUDEN gehuisvest is, dan wel 

   - de GEBOUWD OBJECT . Puntgeometrie van het VERBLIJFSOBJECT waarin  het HUISHOUDEN gehuisvest is; 

- INRICHTINGSELEMENT:  Geometrie inrichtingselement; 

- KADASTRAAL PERCEEL:  Plaatscoördinaten perceel; 

- KUNSTWERKDEEL:  Geometrie kunstwerkdeel; 

- LIGPLAATS: de BENOEMD TERREIN . Geometrie; 

- NUMMERAANDUIDING: 

   - de BENOEMD  TERREIN  . Geometrie  van de  LIGPLAATS of STANDPLAATS waarvan de NUMMERAANDUIDING het hoofdof nevenadres is, dan wel 

   - de GEBOUWD OBJECT . Puntgeometrie van het VERBLIJFSOBJECT  waarvan  de  NUMMERAANDUIDING  het hoofd- of nevenadres is; 

- OPENBARE RUIMTE: dat deel van de GEMEENTELIJKE OPENBARE RUIMTE . Geometrie gemeentelijke openbare ruimte dat zich bevindt binnen de WOONPLAATS (o.b.v. de Woonplaatsgeometrie) waarin de OPENBARE RUIMTE gelegen is; 

- OVERIGE ADRESSEERBAAR OBJECT AANDUIDING: 

- de BENOEMD TERREIN . Geometrie van het OVERIG BENOEMD TERREIN waarvan de OVERIGE ADRESSEERBAAR OBJECT AANDUIDING het adres is, dan wel 

- • de  GEBOUWD  OBJECT  .  Puntgeometrie  van  het  OVERIG GEBOUWD OBJECT waarvan de OVERIGE ADRESSEERBAAR OBJECT AANDUIDING het adres is; 

- • OVERIG GEBOUWD OBJECT: de GEBOUWD OBJECT . Puntgeometrie; 

124 

- OVERIG TERREIN:  de BENOEMD TERREIN . Geometrie; 

- PAND:  Pandgeometrie bovenaanzicht; 

- SPOORBAANDEEL: Geometrie spoorbaandeel; 

- STANDPLAATS: de BENOEMD TERREIN . Geometrie; 

- TERREINDEEL: Geometrie terreindeel; 

- VERBLIJFSOBJECT:  de  GEBOUWD OBJECT . Puntgeometrie; 

- VESTIGING:  de  BENOEMD  TERREIN  .  Geometrie  dan  wel  de GEBOUWD OBJECT . Puntgeometrie van het BENOEMD OBJECT waarin de VESTIGING haar hoofdlokatie heeft; 

- WATERDEEL: Geometrie waterdeel: 

- WEGDEEL: Geometrie wegdeel; 

- WIJK: Wijkgeometrie 

- WOONPLAATS: Woonplaatsgeometrie) 

- WOZ-DEELOBJECT: de WOZ-OBJECT . Geometrie WOZ-object van het WOZ-OBJECT waarvan het WOZ-DEELOBJECT onderdeel uitmaakt; 

- WOZ-OBJECT:  Geometrie WOZ-object; 

- ZAKELIJK RECHT: 

   - de KADASTRAAL PERCEEL .  Plaatscoordinaten perceel van het KADASTRAAL  PERCEEL  waarop  het ZAKELIJK RECHT betrekking heeft, dan wel 

   - de KADASTRAAL PERCEEL .  Plaatscoordinaten perceel van het KADASTRAAL PERCEEL waarop het appartementencomplex staat waarvan het APPARTEMENTSRECHT  deel uit maakt waarop het ZAKELIJK RECHT betrekking heeft; 

## en voor: 

- ANDER NATUURLIJK PERSOON, 

- INGEZETENE, en 

- NIET-INGEZETENE 

de BENOEMD  TERREIN . Geometrie dan wel  de  GEBOUWD OBJECT . Puntgeometrie van het ADRESSEERBAAR OBJECT waarin de natuurlijk persoon verblijft; 

Voor andere objecttypen is dit niet van toepassing. 

## **Attribuutsoort Objecttype** 

## **Definitie attribuutsoort** 

**Herkomst attribuutsoort** 

## Objecttype 

KING 

**Code attribuutsoort** 

## **XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

## typering 

Het onderscheid van een OBJECT naar haar specialisatiies. 

## KING 

1 oktober 2009 

125 

## **Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

Het betreft een afleidbaar gegeven dat is opgenomen om bij uitwisseling van gegevens van het objecttype OBJECT aan te kunnen geven welke specialisatie daarvan het betreft. 

Formaat: AN3 

Waardenverzameling: de mnemonics van de desbetreffende objecttypen uit RSGB en RGBZ 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

1-1 

Afleidbaar gegeven 

De waarde van het gegeven wordt bepaald door de mnemonic van het objjecttype zoals vermeld in de specificaties van het RSGB en het RGBZ. 

## **Relatiesoort OBJECT betreft ZAAKOBJECTen** 

## **Naam relatiesoort** 

OBJECT betreft ZAAKOBJECTen 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 22 mei 2009 

De ZAAKen die via het ZAAKOBJECT betrekking hebben op het OBJECT 

**Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels relatiesoort** 

126 

## **4.9. Organisatorische eenheid** 

## **Attribuutsoort Organisatieidentificatie** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Organisatieidentificatie 

GFO Zaken 2004 

**Code attribuutsoort** 

0001 

**XML-tag attribuutsoort** 

identificatie 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Een korte identificatie van de organisatorische eenheid. 

GFO Zaken 2004 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

De  zaakbehandelende  organisatie  kan  hiervoor  zelf  een  classificatie definiëren. 

Formaat: AN24 

Waardenverzameling: 1e 4 posities: gemeentecode van de gemeente zijnde de zaakbehandelende organisatie; pos.  5 – 24:  classificatie  bestaande  uit  alle alfanumerieke tekens m.u.v. diacrieten 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek** 

**Regels attribuutsoort** 

Nee 

1-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Datum ontstaan** 

## **Naam attribuutsoort** 

Datum ontstaan 

**Herkomst attribuutsoort** 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 8120 

> **XML-tag attribuutsoort** ingangsdatumObject 

> **Definitie attribuutsoort** De datum waarop de organisatorische eenheid is ontstaan. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

GFO Zaken 2004 

127 

## **Datum opname attribuutsoort** 

1 juni 2008 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum opheffing** 

## **Naam attribuutsoort** 

Datum opheffing 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 8130 

> **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

De datum waarop de organisatorische eenheid is opgeheven. 

GFO Zaken 2004 

**Datum opname attribuutsoort** 

1 juni 2008 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle  geldige  datums  zowel  op,  voor  of  na  de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

128 

## **Indicatie authentiek** 

## **Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort E-mail adres** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort Domein attribuutsoort** 

E-mail adres 

GFO Zaken 2004 

9516 

emailadres 

Elektronisch postadres waaronder de organisatorische eenheid in de regel bereikbaar is. 

GFO Zaken 2004 

1 juni 2008 

Het attribuutsoort is overeenkomstig het attribuutsoort Subject.Emailadres. 

Formaat: AN254 

Waardenverzameling: alle bestaande alfanumerieke tekens waarin zich, evenwel niet aan het begin en aan het eind, een ‘@’ moet bevinden. 

## **Indicatie materiële historie** 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

Nee 

Nee 

Nee 

Nee 

Nee 

0-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Faxnummer** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

Faxnummer 

GFO Zaken 2004 

9527 

faxnummer 

Faxnummer waaronder de organisatorische eenheid in de regel bereikbaar is. 

129 

## **Herkomst definitie attribuutsoort** 

## GFO Zaken 2004 

## **Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

1 juni 2008 

Het  attribuutsoort   is  overeenkomstig  het  attribuutsoort  Subject.FAXnummer. 

Het type is alfanumeriek zodat eventuele toevoegingen als 'bgg', 'zak' of 'mobiel' kunnen worden verwerkt. 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

Formaat: AN20 Waardenverzameling: alle bestaande alfanumerieke tekens. 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

**Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** 

Nee 

0-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Naam** 

## **Naam attribuutsoort** 

## Naam 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

> **Code attribuutsoort** 0002 

> **XML-tag attribuutsoort** naam **Definitie attribuutsoort** 

naam 

De feitelijke naam van de organisatorische eenheid. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN50 Waardenverzameling: classificatie 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

130 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek Regels attribuutsoort** - 

1-1 

Gemeentelijk basisgegeven 

## **Attribuutsoort Naam verkort** 

> **Naam attribuutsoort** Naam verkort 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0003 

> **XML-tag attribuutsoort** naamVerkort **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

Een verkorte naam voor de organisatorische eenheid. 

Deze verkorte naam kan bijvoorbeeld hiërarchisch worden opgebouwd en dan worden gebruikt ten behoeve van management informatie. Formaat: AN25 Waardenverzameling: alle alfanumerieke tekens Nee 

## **Indicatie materiële historie** 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Omschrijving** 

> **Naam attribuutsoort** Omschrijving 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0004 

> **XML-tag attribuutsoort** omschrijving **Definitie attribuutsoort** 

Een omschrijving van de organisatorische eenheid. 

131 

## **Herkomst definitie attribuutsoort** 

GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels attribuutsoort** 

## **Attribuutsoort Telefoonnummer** 

> **Naam attribuutsoort** Telefoonnummer 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 9580 

> **XML-tag attribuutsoort** telefoonnummer 

> **Definitie attribuutsoort** Telefoonnummer waaronder de organisatorische eenheid in de regel bereikbaar is. 

**Herkomst definitie attribuutsoort** 

GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort is overeenkomstig het attribuutsoort Subject.Telefoonnummer. 

Het type is alfanumeriek zodat eventuele toevoegingen als 'bgg', 'zak' of 'mobiel' kunnen worden verwerkt. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle bestaande alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

132 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Toelichting** 

> **Naam attribuutsoort** Toelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0005 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Toelichting bij de organisatorische eenheid. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort ORGANISATORISCHE EENHEID bestaat uit MEDEWERKERS** 

**Naam relatiesoort** 

ORGANISATORISCHE EENHEID bestaat uit MEDEWERKERS 

**Herkomst relatiesoort Code relatiesoort** 

GFO Zaken 2004 

**Definitie relatiesoort** 

De  MEDEWERKERs  die  deel  uitmaken  en  hebben  gemaakt  van  de ORGANISATORISCHE EENHEID. 

133 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** Van deze relatie wordt (materiele) historie vastgelegd aangezien het van belang is in welke hoedanigheid medewerkers rollen in zaken hebben vervuld. 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ORGANISATORISCHE EENHEID heeft als verantwoordelijke MEDEWERKER** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

ORGANISATORISCHE EENHEID heeft als verantwoordelijke MEDEWERKER 

GFO Zaken 2004 

**Code relatiesoort** 

**Definitie relatiesoort** 

## **Herkomst definitie relatiesoort** 

De  MEDEWERKER  die  uit  hoofde  van  zijn  of  haar functie  zorgt  (of zorgde) dat de ORGANISATORISCHE EENHEID goed functioneert en daar rekenschap van geeft. 

KING 

> **Datum opname relatiesoort** 1 juni 2008 

**Toelichting relatiesoort** 

Van deze relatie wordt (materiele) historie vastgelegd aangezien het van belang  is  in  welke  hoedanigheid  medewerker  rollen  in  zaken  heeft vervuld. 

**Indicatie materiële historie** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

134 

## **Regels relatiesoort** 

- 

## **Relatiesoort ORGANISATORISCHE EENHEID heeft als contactpersoon MEDEWERKER** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

ORGANISATORISCHE EENHEID heeft als contactpersoon MEDEWERKER GFO Zaken 2004 

**Code relatiesoort** 

> **Definitie relatiesoort** De  MEDEWERKER  die  anderen  desgevraagd  in  contact  brengt  met (andere) medewerkers van deze ORGANISATORISCHE EENHEID. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ORGANISATORISCHE EENHEID is verantwoordelijke voor ZAAKTYPE** 

**Naam relatiesoort** 

**Herkomst relatiesoort Code relatiesoort Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

**Datum opname relatiesoort** 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

ORGANISATORISCHE EENHEID is verantwoordelijke voor ZAAKTYPE 

KING op basis van GFO Zaken 2004 

0008 

De ORGANISATORISCHE EENHEID die verantwoordelijk is voor ZAAKen van het ZAAKTYPE. 

KING op basis van het GFO Zaken 2004 

1 juni 2008 

De relatiesoort is afgeleid van de  attribuutsoort Verantworordelijke bij Zaak in het GFO Zaken 2004. 

Nee 

**Indicatie formele historie** 

Nee 

135 

## **Aanduiding gebeurtenis** 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-1) **Indicatie authentiek** 

Gemeentelijk basisgegeven 

## **Regels relatiesoort** 

## **Relatiesoort ORGANISATORISCHE EENHEID is gehuisvest in VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

ORGANISATORISCHE  EENHEID  is  gehuisvest  in  VESTIGING  VAN ZAAKBEHANDELENDE ORGANISATIE 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE waar de ORGANISATORISCHE EENHEID haar activiteiten uitvoert. 

KING 

> **Datum opname relatiesoort** 17 mei 2010 **Toelichting relatiesoort** 

Met deze relatiesoort wordt voor organisatorische eenheden (afdelingen e.d.) van de organisatie die zaken behandelt gemodelleerd binnen welke vestiging van die organisatie c.q. op welke locatie die organisatorische eenheid werkzaam is. 

## **Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

136 

## **4.10. Rol** 

## **Attribuutsoort Rolomschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Rolomschrijving 

GFO Zaken 2004 

**Code attribuutsoort** 

0002 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

omschrijving 

Omschrijving van de aard van de rol. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

Het is afgeleid van de attribuutsoort Betrokkene.Rolomschrijving in het GFO Zaken 2004. 

Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

Ja 

**Indicatie formele historie** 

Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 **Indicatie authentiek** 

> **Regels attribuutsoort** - 

Gemeentelijk basisgegeven 

## **Attribuutsoort Rolomschrijving generiek** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Rolomschrijving generiek 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

rolomschrijvingGeneriek 

Algemeen gehanteerde benaming van de aard van de ROL 

KING 

22-05-09 

137 

## **Toelichting attribuutsoort** 

Het gaat hier om de benaming van een rol bij een zaak zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde benaming, de Rolomschrijving. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: Belanghebbende Gemachtigde Initiator Overig Uitvoerder Verantwoordelijke 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Bij een ZAAK kan maximaal één ROL met als Rolomschrijving generiek 'Initiator' voorkomen. 

Bij een ZAAK kan maximaal één ROL met als Rolomschrijving generiek 'Verantwoordelijke' voorkomen. 

## **Attribuutsoort Roltoelichting** 

> **Naam attribuutsoort** Roltoelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0003 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Toelichting bij de rol. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het is afgeleid van de attribuutsoort Betrokkene.Roltoelichting in het GFO Zaken 2004. 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

138 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Groepattribuutsoort Contactpersoon** 

## **Naam attribuutsoort** 

Contactpersoon 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

contactpersoon 

De gegevens van de persoon die anderen desgevraagd in contact brengt met  medewerkers  van  de  BETROKKENE,  een   NIET-NATUURLIJK PERSOON  of  VESTIGING  zijnde,  of  met  BETROKKENE  zelf,  een NATUURLIJK PERSOON  zijnde, vanuit het belang van BETROKKENE in haar ROL bij een ZAAK,. 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## 1 juni 2008 

Het gaat om gegevens van contactpersonen van externe betrokkenen zoals bijvoorbeeld van het bedrijf dat een vergunning aanvraagt en de persoon die als aanvrager van een vergunning een andere persoon als conatctpersoon heeft aangemeld. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

- Contactpersoonnaam 

- Contactpersoon functie 

- Contactpersoon telefoonnummer - Contactpersoon emailadres **Domein attribuutsoort** Formaat: n.v.t. Waardenverzameling: **Indicatie materiële historie** Ja **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee 

139 

## **Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

De attribuutgroep komt bij een rol niet voor indien de betrokkene een organisatorische eenheid of medewerker is. 

## **Attribuutsoort Contactpersoonnaam** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Contactpersoonnaam 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

contactpersoon/naam 

De opgemaakte naam van de contactpersoon namens de BETROKKENE. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Contactpersoon. Formaat: AN40 Waardenverzameling: alle alfanumerieke tekens 

**Domein attribuutsoort Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Contactpersoon functie** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

Contactpersoon functie 

KING 

contactpersoon/functie 

De aanduiding van de taken, rechten en plichten die de contactpersoon heeft binnen de organisatie van BETROKKENE. 

140 

## **Herkomst definitie attribuutsoort** 

## KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Contactpersoon. 

> **Domein attribuutsoort** Formaat: AN50 

Formaat: AN50 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Contactpersoon telefoonnummer** 

> **Naam attribuutsoort** Contactpersoon telefoonnummer 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** contactpersoon/telefoonnummer 

> **Definitie attribuutsoort** Telefoonnummer waaronder de contactpersoon in de regel bereikbaar is. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Contactpersoon. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

141 

## **Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Contactpersoon emailadres** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Contactpersoon emailadres 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

contactpersoon/emailadres 

Elektronich postadres waaronder de contactpersoon in de regel bereikbaar is. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Contactpersoon. 

Formaat: AN80 

Waardenverzameling: alle bestaande alfanumerieke tekens waarin zich, evenwel niet aan het begin en aan het eind, een ‘@’ moet bevinden. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek Regels attribuutsoort** - 

Gemeentelijk basisgegeven 

## **Groepattribuutsoort Afwijkend correspondentie postadres** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Afwijkend correspondentie postadres 

KING 

**Code attribuutsoort XML-tag attribuutsoort** 

afwijkendCorrespondentiePostadres 

142 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

De gegevens die tezamen een postbusadres of antwoordnummeradres vormen waarvan BETROKKENE, geen ORGANISATORISCHE EENHEID  en  MEDEWERKER  ziinde,  heeft  aangegeven  schriftelijk bereikbaar te zijn in verband met zijn/haar ROL in de  ZAAK en dat afwijkt van de reguliere correspondentiegegevens van BETROKKENE. 

KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

1 juni 2008 

Zoals uit de defintie moge blijken, zijn de gegevens alleen voorzien van een  waarde  indien  de  betrokkene  over  de  zaak  via  een  ander correspondentieadres wil cpmmuniceren dan het correspondentieadres zoals dat van betrokkene bekend is. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Postadrestype Postbus- of antwoordnummer 

Postadres postcode 

en het volgende relatiesoort: 

ROL van BETROKKENE met correspondentie postadres dat zich bevindt in WOONPLAATS. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels attribuutsoort** 

De  relatie  is  alleen  aanwezig  indien  de  gegevens  afwijken  van  het correspondentiepostadres van BETROKKENE. 

Indien  de  relatie  aanwezig  is  dan  is  het  groepsattributen Afwijkend buitenlands correspondentie adres niet van een waarde voorzien en is de relatiesoort  'ROL  bij  BETROKKENE  met  als  afwijkend  binnenlands correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING' niet aanwezig. 

## **Attribuutsoort Postadrestype** 

> **Naam attribuutsoort** Postadrestype 

> **Herkomst attribuutsoort** KING 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

afwijkendCorrespondentiePostadres/sub.type 

Aanduiding van het soort postadres 

143 

## **Herkomst definitie attribuutsoort** 

## KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

Door middel van de aanduiding wordt duidelijk of de waarde van het gegeven ‘Postbus- of antwoordnummer’ een postbus- of een antwoordnummer betreft. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort afwijkend correspondentie postadres. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: A1 Waardenverzameling: A: Antwoordnummer P: Postbusnummer 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Postbus- of antwoordnummer** 

> **Naam attribuutsoort** Postbus- of antwoordnummer 

> **Herkomst attribuutsoort** KING op basis van GFO BG 

> **Code attribuutsoort** 11.80 / 94.86 

> **XML-tag attribuutsoort** afwijkendCorrespondentiePostadres/sub.Nummer 

> **Definitie attribuutsoort** De numerieke aanduiding zoals deze door de Nederlandse PTT is vastgesteld voor postbusadressen en antwoordnummeradressen. 

> **Herkomst definitie attribuutsoort** KING op basis van GFO 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

In combinatie met postadrestype wordt duidelijk of de waarde van het gegeven een postbus- of een antwoordnummer betreft. Het attribuutsoort maakt deel uit van het groepattribuutsoort Afwijkend correspondentie postadres. 

> **Domein attribuutsoort** Formaat: N5 Waardenverzameling: 1 - 99999 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

144 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - 

**Regels attribuutsoort** 

## **Attribuutsoort Postadres postcode** 

## **Naam attribuutsoort** 

Postadres postcode 

**Herkomst attribuutsoort** 

KING op basis van GFO 

> **Code attribuutsoort** 11.60 

> **XML-tag attribuutsoort** afwijkendCorrespondentiePostadres/sub.postcode **Definitie attribuutsoort** 

De officiële Nederlandse PTT codering, bestaande uit een numerieke woonplaatscode en een alfabetische lettercode. 

**Herkomst definitie attribuutsoort** 

NEN 5825 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

1 juni 2008 

De postcode is opgebouwd uit een woonplaatscode en een lettercode. Het Besluit Standaardadressering zegt hierover: 

Woonplaatscode: een door de PTT ontworpen 4-cijferige code die een unieke aanduiding vormt voor alle woonplaatsen in Nederland. Lettercode: twee alfabetische tekens in hoofdletters. 

De combinatie woonplaatscode/lettercode vormt de cijfer/lettercombinatie van een aantal besteladressen die algemeen bekend staan als postcode. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort afwijkend correspondentie postadres. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN6 Waardenverzameling: 1000AA – 9999ZZ 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

145 

- 

## **Regels attribuutsoort** 

## **Groepattribuutsoort Afwijkend buitenlands correspondentieadres** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

Afwijkend buitenlands correspondentieadres 

KING 

afwijkendBuitenlandsAdres 

De gegevens van het adres in het buitenland waarop BETROKKENE in zijn/haar ROL in de ZAAK in de regel schriftelijk bereikbaar is  indien dat afwijkt van het reguliere buitenlandse correspondentieadres van BETROKKENE 

## 1 juni 2008 

Zoals uit de defintie moge blijken, zijn de gegevens alleen voorzien van een waarde indien de betrokkene over de zaak via een ander buitenlands correspondentieadres wil cpmmuniceren dan het buityenlands correspondentieadres zoals dat van betrokkene bekend is. 

Het groepattribuut is afgeleid van groep SUBJECT . Verblijf buitenland in het RSGB. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

Adres buitenland 1 

Adres buitenland 2 Adres buitenland 3 en de volgende relatiesoort: 

ROL van BETROKKENE met correspondentie postadres dat zich bevindt in LAND. 

De attribuutsoorten zijn gespecificeerd in het RSGB bij het objecttype SUBJECT. Hieronder specificeren we alleen de relatiesoort. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** De  relatie  is  alleen  aanwezig  indien  de  gegevens  afwijken  van  het buitenlands correspondentieadres van BETROKKENE. Indien  de  relatie  aanwezig  is  dan  is  het groepsattributen   Afwijkend correspondentie postadres  niet van een waarde voorzien en is de relatie 'ROL bij BETROKKENE met als afwijkend binnenlands correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING' niet aanwezig. 

146 

## **Relatiesoort ROL betreft ZAAK** 

> **Naam relatiesoort** ROL betreft ZAAK 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De ZAAK waarin de ROL uitgeoefend wordt. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 1-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ROL wordt uitgeoefend door BETROKKENE** 

**Naam relatiesoort Herkomst relatiesoort** KING **Code relatiesoort** 

ROL wordt uitgeoefend door BETROKKENE 

> **Definitie relatiesoort** De BETROKKENE die de ROL heeft in de desbetreffende ZAAK.. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

**Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

147 

## **Aanduiding strijdigheid/nietigheid** Nee 

## **Indicatie kardinaliteit** 

**Indicatie authentiek Regels relatiesoort** 

1-1 (vice versa: 0-N) 

Gemeentelijk basisgegeven 

Indien van de ROL de Roltype-omschrijving generiek 'Verantwoordelijke' is, dan kan de relatie alleen liggen naar de specialisatie ORGANISATORISCHE EENHEID of MEDEWERKER van BETROKKENE. 

## **Relatiesoort ROL zet als betrokkene STATUS** 

## **Naam relatiesoort** 

ROL zet als betrokkene STATUS 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

> **Definitie relatiesoort** De BETROKKENE die in zijn/haar ROL in een ZAAK heeft geregistreerd dat STATUSsen in die ZAAK bereikt zijn. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 01-06-08 

> **Toelichting relatiesoort** Alléén een medewerker (of organisatorische eenheid) die een rol heeft in een zaak, mag een status zetten voor die zaak. 

> **Indicatie materiële historie** Nee 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** De relatie kan alleen aanwezig zijn indien de Betrokkene bij de Rol een Organisatorische Eenheid of een Medewerker is. 

## **ROL bij BETROKKENE met als afwijkend binnenlands correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING** 

> **Naam relatiesoort** ROL bij BETROKKENE met als afwijkend binnenlands correspondentieadres ADRESSEERBAAR OBJECT AANDUIDING 

> **Herkomst relatiesoort** KING op basis van GFO BG 

**Code relatiesoort** 

148 

## **Definitie relatiesoort** 

## **Herkomst definitie relatiesoort** 

Het adres waarop BETROKKENE in zijn/haar ROL in de ZAAK in de regel schriftelijk bereikbaar is,  indien dat afwijkt van het reguliere binnenlandse correspondentieadres van BETROKKENE, en dat gevormd wordt door de combinatie van de ADRESSEERBAAR OBJECT AANDUIDING met  de bijbehorende (GEMEENTELIJKE) OPENBARE RUIMTE en WOONPLAATS. 

KING 

> **Datum opname relatiesoort** 1 juni 2008 

**Toelichting relatiesoort** 

Zoals uit de defintie moge blijken, is de relatie alleen aanwezig indien de betrokkene  over  de  zaak  via  een  ander  correspondentieadres  wil cpmmuniceren dan het correspondentieadres zoals dat van betrokkene bekend is. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Nee 

Nee 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

0-1 (vice versa: 0-N) 

**Indicatie authentiek** 

**Regels relatiesoort** 

De  relatie  is  alleen  aanwezig  indien  de  gegevens  afwijken  van  het binnenlands correspondentieadres van BETROKKENE. 

Indien de relatie  aanwezig is dan zijn de groepsattributen  Afwijkend correspondentie  postadres  en   Afwijkend  buitenlands  correspondentie adres niet van een waarde voorzien. 

## **Relatiesoort ROL van BETROKKENE met afwijkend correspondentie postadres dat zich bevindt in WOONPLAATS** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

ROL van BETROKKENE met afwijkend correspondentie postadres dat zich bevindt in WOONPLAATS 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De woonplaats die behoort bij het afwijkende correspondentie postadres van de betrokkene in zijn/haar rol bij de zaak 

KING 

> **Datum opname relatiesoort** 1 mei 2008 

**Toelichting relatiesoort** 

Het  relatiesoort  maakt  deel  uit  van  het  groepattribuutsoort  afwijkend crrespondentie postadres. 

149 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (binnen de groepattribuutsoort) (vice versa: 0-N) **Indicatie authentiek** 

## **Regels relatiesoort** 

## **Relatiesoort ROL van BETROKKENE met afwijkend buitenlands correspondentieadres dat zich bevindt in LAND** 

**Naam relatiesoort** 

> **Naam relatiesoort** ROL van BETROKKENE met afwijkend buitenlands correspondentieadres dat zich bevindt in LAND 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Het LAND dat behoort bij het afwijkend buitenlandse correspondentieadres van de betrokkene in zijn/haar rol bij de zaak 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 22-05-09 

> **Toelichting relatiesoort** Het  relatiesoort  maakt  deel  uit  van  het  groepattribuutsoort  Afwijkend buitenlands correspondentieadres. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (binnen groepattribuutsoort) (vice versa: 0-N) **Indicatie authentiek** 

## **Regels relatiesoort** 

150 

## **4.11. Samengesteld document** 

## **Relatiesoort SAMENGESTELD DOCUMENT omvat ENKELVOUDIGe DOCUMENTen** 

**Naam relatiesoort** 

**Herkomst relatiesoort** 

SAMENGESTELD DOCUMENT omvat ENKELVOUDIGe DOCUMENTen KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De ENKELVOUDIGe DOCUMENTen die deel uit maken van het SAMENGESTELD DOCUMENT. 

KING 

**Datum opname relatiesoort Toelichting relatiesoort** 

**Indicatie materiële historie** 

1 oktober 2009 

Zie  de  definitie  van  het  objecttype  en  verder  de  toelichting  bij  het objecttype Document. 

Ja 

**Indicatie formele historie Aanduiding gebeurtenis** 

Ja 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

**Indicatie authentiek** 

2-N (vice versa: 0-1) 

Gemeentelijk basisgegeven 

**Regels relatiesoort** 

151 

## **4.12. Status** 

## **Attribuutsoort Datum status gezet** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

Datum status gezet 

GFO Zaken 2004 0004 

datumStatusGezet 

De datum waarop de zaak de status heeft verkregen. 

GFO Zaken 2004 

1 juni 2008 

Op één dag kan een zaak meerdere statussen doorlopen. Om te kunnen bepalen wat de laatst gezette status is of in welke volgorde de statussen bereikt zijn, wordt de datum tot op de minuut vastgelegd. 

Formaat: Datum (JJJJMMDDUUMM) Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Status toelichting** 

## **Naam attribuutsoort** 

Statustoelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0003 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Een, voor de initiator van de zaak relevante, toelichting op de status van een zaak. 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort** 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

152 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Indicatie laatst gezette status** 

> **Naam attribuutsoort** Indicatie laatst gezette status 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** indicatieLaatsteStatus 

> **Definitie attribuutsoort** Aanduding of het de laatst bekende bereikte status betreft. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 oktober 2009 

> **Toelichting attribuutsoort** Dit afleidbaar gegeven is toegevoegd omdat het bepalen van de laatst bekende status anderds alleen te doen is op basis van analyse van alle statussen van de zaak. 

> **Domein attribuutsoort** Formaat: AN1 Waardenverzameling: J, N 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Afleidbaar gegeven 

153 

## **Regels attribuutsoort** 

Het gegeven is afleidbaar uit de historie van de attribuutsoort Datum status gezet van van alle statussen bij de desbetreffende zaak. 

## **Relatiesoort STATUS is gezet door betrokkene in zijn/haar ROL** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

STATUS is gezet door betrokkene in zijn/haar ROL 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De BETROKKENE die in zijn/haar ROL in een ZAAK heeft geregistreerd dat de STATUS in die ZAAK bereikt is. 

KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

Een status kan alleen gezet worden door een betrokkene, zijnde een organisatorische  eenheid  of  medewerker,  die  een  rol  heeft  in  de desbetreffende zaak, niet door een willekeurig andere betrokkene. Nee 

**Indicatie materiële historie** 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Ja 

Nee 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

**Indicatie authentiek** 

**Regels relatiesoort** 

1-1 (vice versa: 0-N) 

Gemeentelijk basisgegeven 

De relatie kan alleen liggen naar een Rol waarbij de Betrokkene een Organisatorische eenheid of Medewerker is terwijl de Rol hoort bij de Zaak waarop de Status betrekking heeft. 

## **Relatiesoort STATUS is van ZAAK** 

> **Naam relatiesoort** STATUS is van ZAAK 

**Herkomst relatiesoort** 

GFO Zaken 2004 

**Code relatiesoort** 

**Definitie relatiesoort** 

De ZAAK waarin de STATUS bereikt is. 

**Herkomst definitie relatiesoort** 

KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

**Indicatie materiële historie** 

Ja 

154 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort STATUS is van STATUSTYPE** 

> **Naam relatiesoort** STATUS is van STATUSTYPE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Aanduiding van de aard van de STATUS. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort STATUS heeft daarvoor relevante ZAAKDOCUMENTen** 

**Naam relatiesoort Herkomst relatiesoort** 

STATUS heeft daarvoor relevante ZAAKDOCUMENTen KING 

**Code relatiesoort** 

155 

## **Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De  bij  de  desbetreffende  ZAAK  behorende  ZAAKDOCUMENTen  die relevant  zijn  (geweest)  voor  het  bereiken  van  de  STATUS  en/of  de communicatie daarover. 

KING 

**Datum opname relatiesoort** 

22-05-09 

**Toelichting relatiesoort** 

Op zich zou uit de documentdatum (van de documenten bij de zaak) en de statusdatum afgeleid kunnen worden welke zaakdocumenten een rol gespeeld  hebben  ten  aanzien  van  een  status.  Evenwel,  njet  in  alle gevallen gaat dit op. Zo kunnen er documenten zijn die weliswaar voor de statusdatum  gecreeerd  zijn  maar  geen  rol  hebben  gespeeld  bij  het bereiken van die status. En over het bereikt hebben van de status kan gecommuniceerd zijn waarbij de desbetreffende documenten een creatiedatum hebben na de statusdatum. Deze relatiesoort biedt zaakbehandelende organisaties de mogelijkheid desgewenst dergelijke zaakdocumenten te relateren aan een bereikte status. 

De relatiesoort is de tegenhanger van 'ZAAKDOCUMENT is relevant voor STATUS'. 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument** 

Nee 

Nee 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek Regels relatiesoort** 

0-N (vice versa: 0-1) Gemeentelijk basisgegeven 

Alleen die zaakdocumenten kunnen gerelateerd zijn die gerelateerd zijn aan de desbetreffende zaak. 

156 

## **4.13. Statustype** 

## **Attribuutsoort Statustype-omschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Statustype-omschrijving 

GFO Zaken 2004 

**Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

0002 

omschrijving 

Een korte, voor de initiator van de zaak relevante, omschrijving van de aard van de STATUS van zaken van een ZAAKTYPE. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

Het betreft de attribuutsoort Status.Statusomschrijving in het GFO Zaken 2004 met dien verstande dat deze nu van toepassing is per Statustype, d.w.z.  voor  alle  daarbij  te  registreren  Statussen,  en  niet  per  status bepaald kan worden. 

Voorbeelden hiervan zijn “Aanvraag ontvangen”, “Äanvraag ontvankelijk”, “Aanvraag in behandeling”, “Voorstel bij B&W” en “Aanvraag afgehandeld”. 

**Domein attribuutsoort** 

Formaat: AN80 

Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Statustypevolgnummer** 

> **Naam attribuutsoort** volgnummer 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0001 

> **XML-tag attribuutsoort** volgnummer 

> **Definitie attribuutsoort** Een volgnummer voor de status binnen een zaak. 

157 

## **Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

KING op basis van GFO Zaken 2004 

1 juni 2008 

Een zaak doorloopt achtereenvolgens een aantal statussen. Het volgnummer legt de volgorde vast waarin de statussen doorlopen zijn. Formaat: N4 Waardenverzameling: 0001 - 9999 

Nee 

> **Indicatie formele historie** Nee 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Doorlooptijd status** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Doorlooptijd status 

KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** doorlooptijd **Definitie attribuutsoort** 

De  door  de  zaakbehandelende  organisatie(s)  gestelde  norm  voor  de doorlooptijd voor het bereiken van STATUSsen van dit STATUSTYPE bij het desbetreffende ZAAKTYPE. 

## **Herkomst definitie attribuutsoort** 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

1 juni 2008 

De zaakbehandelende organisatie(s) bepaalt zelf de hardheid van deze norm: verwachting, servicenorm of harde norm. 

Formaat: N3 (in dagen) Waardenverzameling: 1-999 werkdagen 

Ja 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

158 

## **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Statustype-omschrijving generiek** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Statustype-omschrijving generiek 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

omschrijvingGeneriek 

Algemeen gehanteerde omschrijving van de aard van STATUSsen van het STATUSTYPE 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

## KING 

1 juni 2008 

Het gaat hier om een korte omschrijving van de aard van de status zoals deze  landelijk  wordt  toegepast.  Deze  kan  afwijken  van  de  door  de zaakbehandelende  organisatie(s)  gehanteerde  naam,  de  Statustypeomschrijving. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

Waardenverzameling: alle alfanumerieke tekens 

## **Attribuutsoort Datum begin geldigheid statustype** 

> **Naam attribuutsoort** Datum begin geldigheid statustype 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

159 

## **XML-tag attribuutsoort** 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

## ingangsdatumObject 

De datum waarop het STATUSTYPE is ontstaan. 

## KING 

1 oktober 2009 

Met deze datum wordt aangegeven vanaf wanneer het statustype bestaat en toegepast kan worden. 

Formaat: OnvolledigeDatum 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum einde geldigheid statustype** 

## **Naam attribuutsoort** 

Datum einde geldigheid statustype 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** einddatumObject **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

De datum waarop het STATUSTYPE is opgeheven. 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

1 oktober 2009 

Met deze datum wordt aangegeven vanaf wanneer het statustype niet meer bestaat en niet meer toegepast kan worden. Formaat: OnvolledigeDatum 

**Domein attribuutsoort Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee 

160 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen  onder  'Datum  begin  geldigheid  statusType’  kan  in  de registratie worden opgenomen. 

## **Relatiesoort STATUSTYPE heeft STATUSsen** 

> **Naam relatiesoort** STATUSTYPE heeft STATUSsen 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Verwijzing naar de STATUSsen van dit STATUSTYPE. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort STATUSTYPE is van ZAAKTYPE** 

> **Naam relatiesoort** STATUSTYPE is van ZAAKTYPE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 

Het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE bereikt kunnen worden. 

KING 

1 juni 2008 

161 

**Toelichting relatiesoort Indicatie materiële historie** Nee **Indicatie formele historie** Nee **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 1-1 (vice versa: 1-N) **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** - 

162 

## **4.14. Zaak** 

## **Attribuutsoort Zaakidentificatie** 

**Naam attribuutsoort** 

Zaakidentificatie 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0001 

**XML-tag attribuutsoort** 

identificatie 

**Definitie attribuutsoort** 

Een identificatie van de zaak. 

**Herkomst definitie attribuutsoort** 

GFO Zaken 2004 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## 1 juni 2008 

Deze identificatie kan zowel intern als extern worden gebruikt om snel te kunnen refereren aan een bepaalde zaak. Formaat: AN40 

Waardenverzameling: 1e 4 posities: gemeentecode van de gemeente die verantwoordelijk is voor de behandeling van de zaak; 

pos.  5 – 40:  alle  alfanumerieke  tekens  m.u.v. diacrieten 

## **Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Einddatum** 

## **Naam attribuutsoort** 

Einddatum 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0014 

> **XML-tag attribuutsoort** einddatum 

> **Definitie attribuutsoort** De datum waarop de uitvoering van de zaak afgerond is. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

163 

## **Datum opname attribuutsoort** 

## 1 juni 2008 

> **Toelichting attribuutsoort** De periode waarin de zaak is uitgevoerd is inclusief de opgegeven datum. 

**Domein attribuutsoort** 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

## **Indicatie materiële historie** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Einddatum gepland** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

Einddatum gepland 

GFO Zaken 2004 

0012 

einddatumGepland 

De  datum  waarop  volgens  de  planning  verwacht  wordt  dat  de  zaak afgerond wordt. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

De periode is inclusief de opgegeven datum. 

De  datum  kan  berekend  worden  op  basis  van  de  Startdatum  en Zaaktype.servicenormBehandeling. 

## **Domein attribuutsoort** 

Formaat: Datum (JJJJMMDD) 

Waardenverzameling: Alle geldige datums gelegen op,, voor of na de huidige datum en tijd 

## **Indicatie materiële historie** 

Ja 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Ja 

Nee 

Nee 

Nee 

164 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek** 

**Regels attribuutsoort** 

0-1 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Omschrijving** 

## **Naam attribuutsoort** 

Omschrijving 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0002 

> **XML-tag attribuutsoort** omschrijving **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Deze 

Een korte omschrijving van de zaak. 

Deze omschrijving beschrijft de individuele zaak daar waar Zaaktype.zaaktype-omschrijving de aard van de zaak beschrijft. Bijvoorbeeld, bij een zaaktype ‘Behandelen aanvraag bouwvergunning’ geeft de omschrijving aan waarop de bouwvergunning betrekking heeft, bijvoorbeeld ‘Uitbreiden van de woning aan de achterzijde’. 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Groepattribuutsoort Kenmerken** 

> **Naam attribuutsoort** Kenmerken 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

165 

## **XML-tag attribuutsoort** 

## kenmerk 

## **Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

Identificatie-gegevens over de zaak in andere administraties 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

Dit groepsattribuut beschrijft identificerende gegevens waaronder de zaak in andere administraties is opgenomen. Aangezien de zaak in meerdere andere administraties kan voorkomen, kan deze gegevensgroep meerdere malen voorkomen. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: - Kenmerk - Kenmerk bron **Domein attribuutsoort** Formaat: n.v.t Waardenverzameling: **Indicatie materiële historie** Nee **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Kenmerk** 

> **Naam attribuutsoort** Kenmerk 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0020 

> **XML-tag attribuutsoort** kenmerk/kenmerk 

> **Definitie attribuutsoort** Identificeert uniek de zaak in een andere administratie. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Het attribuutsoort maakt deel uit van het groepattribuutsoort Kenmerken 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

166 

## **Indicatie formele historie** 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - 

**Regels attribuutsoort** 

## **Attribuutsoort Kenmerk bron** 

## **Naam attribuutsoort** 

Kenmerk bron 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0021 

> **XML-tag attribuutsoort** kenmerk/bron **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

De aanduiding van de administratie waar het kenmerk op slaat. 

Het attribuutsoort maakt deel uit van het groepattribuutsoort Kenmerken. 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

167 

## **Attribuutsoort Resultaatomschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Resultaatomschrijving 

GFO Zaken 2004 

**Code attribuutsoort** 

0016 resultaat/omschrijving 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort** GFO Zaken 2004 **Datum opname attribuutsoort** 1 juni 2008 

Een korte omschrijving wat het resultaat van de zaak inhoudt. 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Resultaattoelichting** 

**Naam attribuutsoort** 

Resultaattoelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0017 

> **XML-tag attribuutsoort** resultaat/toelichting **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: 

Een toelichting op wat het resultaat van de zaak inhoudt. 

Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

168 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Startdatum** 

## **Naam attribuutsoort** 

Startdatum 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

**Code attribuutsoort** 

0011 

**XML-tag attribuutsoort** 

startdatum 

**Definitie attribuutsoort** 

De datum waarop met de uitvoering van de zaak is gestart. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort Domein attribuutsoort** 

GFO Zaken 2004 

1 juni 2008 

> **Domein attribuutsoort** Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op, voor of na de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

169 

## **Attribuutsoort Toelichting** 

> **Naam attribuutsoort** Toelichting 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0003 

> **XML-tag attribuutsoort** toelichting 

> **Definitie attribuutsoort** Een toelichting op de zaak. 

> **Herkomst definitie attribuutsoort** GFO Zaken 2004 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Uiterlijke einddatum afdoening** 

## **Naam attribuutsoort** 

Uiterlijke einddatum afdoening 

> **Herkomst attribuutsoort** GFO Zaken 2004 

> **Code attribuutsoort** 0013 

> **XML-tag attribuutsoort** uiterlijkeEinddatum **Definitie attribuutsoort** 

De laatste datum waarop volgens wet- en regelgeving de zaak afgerond dient te zijn. 

**Herkomst definitie attribuutsoort** 

GFO Zaken 2004, aangepast door KING 

> **Datum opname attribuutsoort** 1 juni 2008 

**Toelichting attribuutsoort** 

De periode is inclusief de opgegeven datum. 

De  datum  kan  berekend  worden  op  basis  van  de  Startdatum  en Zaaktype.doorlooptijdBehandeling. 

170 

## **Domein attribuutsoort** 

Formaat: Datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op,, voor of na de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Zaakniveau** 

## **Naam attribuutsoort** 

Zaakniveau 

## **Herkomst attribuutsoort** 

KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** zaakniveau **Definitie attribuutsoort** 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 22 mei 2009 **Toelichting attribuutsoort** 

Het niveau van een ZAAK in de hierarchie van hoofdzaak met deelzaken. 

## 22 mei 2009 

Met het attribuutsoort kan afgeleid worden of de desbetreffende zaak een zgn. hoofdzaak  is (zaakniveau 1) dan wel een deelzaak daarvan of een deelzaak  van  een  andere  deelzaak. Uit oogpunt van  beheersing  van complexiteit gaan we vooralsnog uit van een hierarchie van maximaal drie niveau's: hoofdzaak, deelzaken en deeldeelzaken. 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|N1|
||Waardenverzameling:|1, 2 en 3|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||



171 

## **Indicatie authentiek** 

## **Regels attribuutsoort** 

## Gemeentelijk basisgegeven 

De hoofdzaaj heeft waarde 1. Een daarvan deel uit makende deelzaak heeft  waarde  2.  Een  van  één  van  die  deelzaken  deel  uitmakende deeldeelzaak heeft waarde 3. 

## **Attribuutsoort Deelzakenindicatie** 

> **Naam attribuutsoort** Deelzakenindicatie 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** deelzakenIndicatie 

> **Definitie attribuutsoort** De aanduiding of een ZAAK behandeld wordt in deelzaken. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 22 mei 2009 

> **Toelichting attribuutsoort** Het betreft zowel voor een zgn hoofdzaak als voor een zgn. deelzaak de indicatie of er sprake is van deelzaken respectievelijk deeldeelzaken. 

> **Domein attribuutsoort** Formaat: A1 Waardenverzameling: J, N 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Een  (deel)zaak  waaraan  (deel)deelzaken  gerelateerd  zijn,  heeft  de 

Een  (deel)zaak  waaraan  (deel)deelzaken  gerelateerd  zijn,  heeft  de waarde 'J”. Een (deel)zaak waarvoor dit niet geldt, heeft de waarde 'N'. 

## **Attribuutsoort Registratiedatum** 

> **Naam attribuutsoort** Registratiedatum 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** registratiedatum **Definitie attribuutsoort** 

De  datum  waarop  de  zaakbehandelende  organisatie  de  ZAAK  heeft geregistreerd 

172 

## **Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

1 juni 2008 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Publicatiedatum** 

> **Naam attribuutsoort** Publicatiedatum 

> **Herkomst attribuutsoort** KING 

## **Code attribuutsoort** 

> **XML-tag attribuutsoort** publicatiedatum **Definitie attribuutsoort** 

Datum waarop (het starten van) de zaak gepubliceerd is of wordt. 

**Herkomst definitie attribuutsoort** 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

1 juni 2008 

Niet alleen besluiten worden gepuibliceerd, bij sommige zaaktypen is het wettelijk  verplicht  of  gebruikelijk  om  het  starten  van  een  zaak  te publiceren, zoals het in behandeling nemen van een aanvraag voor een bouwvergunning. 

Formaat: 

datum 

Waardenverzameling: Alle geldige datums gelegen op, voor of na de huidige datum en tijd 

## **Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

173 

## **Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

- 

## **Attribuutsoort Archiefnominatie** 

## **Naam attribuutsoort** 

Archiefnominatie 

**Herkomst attribuutsoort** 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

## archiefnominatie 

Indicatie of het zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) gearchiveerd dient te worden 

## KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

## 1 juni 2008 

Of een zaak gearchiveerd moet worden hangt af van het zaaktype, het resultaat van de zaak en eventuele andere gerelateerde zaken. 

Formaat: AN1 Waardenverzameling: J, N 

Ja 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Datum vernietiging dossier** 

> **Naam attribuutsoort** Datum vernietiging dossier 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** datumVernietigingDossier 

174 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

De datum waarop het, al dan niet gearchiveerde, zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) vernietigd mag worden. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

## **Indicatie materiële historie** 

## 1 juni 2008 

Met vernietigen wordt hier vooral bedoeld dat het zaakdossier uit het archief verwijderd wordt.  De datum waarop dit mag plaatsvinden hangt af van de datums van besluiten die het gevolg zijn van de zaak, van het zaaktype,  van  het  resultaat  van  de  zaak  en  van  eventuele  andere gerelateerde zaken. 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op, voor of na de huidige datum en tijd 

Nee 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

**Indicatie kardinaliteit** 

0-1 

**Indicatie authentiek** 

Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Betalingsindicatie** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Betalingsindicatie 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

betalingsIndicatie 

Indicatie of de, met behandeling van de zaak gemoeide, kosten betaald zijn door de desbetreffende betrokkene. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

Het gaat hier om kosten zoals leges. 

Idealiter  wordt  deze  informatie  alleen  geregistreerd  in  een  financiele administratie. Dit vereist minimaal het opnemen van de Zaakidentificatie daarin. 

175 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN12 Waardenverzameling: N,v.t. (Nog) niet Gedeeltelijk Geheel 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Laatste betaaldatum** 

## **Naam attribuutsoort** 

Laatste betaaldatum 

**Herkomst attribuutsoort** 

KING 

**Code attribuutsoort XML-tag attribuutsoort** laatsteBetaaldatum **Definitie attribuutsoort** 

De datum waarop de meest recente betaling is verwerkt van kosten die gemoeid zijn met behandeling van de zaak. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

KING 

1 juni 2008 

De te betalen kosten kunnen in één keer maar ook in gedeeltes betaald worden. De attribuutsoort geeft alleen de datum weer waarop de laatste betaling is verwerkt. Idealiter wordt deze informatie alleen geregistreerd in een financiele administratie. Dit vereist minimaal het opnemen van de Zaakidentificatie daarin. 

Zie ook de attribuutsoort ‘Betalingsindicatie’. 

## **Domein attribuutsoort** 

Formaat: datum/tijd (JJJJMMDDHHMM) Waardenverzameling: Alle geldige datums en tijdstippen gelegen op of voor de huidige datum en tijd 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Nee 

176 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek** 

0-1 Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Opschorting** 

## **Naam attribuutsoort** 

## **Herkomst attribuutsoort** 

Opschorting 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

## opschorting 

Gegevens omtrent het tijdelijk opschorten van de behandeling van de ZAAK 

## KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

1 juni 2008 

Groepattribuutsoort, bestaande uit: 

Indicatie opschorting Reden opschorting 

## **Domein attribuutsoort** 

**Indicatie materiële historie** 

Formaat: n.v.t. Waardenverzameling: 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Indicatie opschorting** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Indicatie opschorting KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

opschorting/indicatie 

177 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

Aanduiding of de behandeling  van de ZAAK tijdelijk is opgeschort. 

KING 

> **Datum opname attribuutsoort** 1 juni 2008 

**Toelichting attribuutsoort** 

Maakt deel uit van groepattribuutsoort Opschorting 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: A1 Waardenverzameling: J, N 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

**Aanduiding brondocument** 

Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Reden opschorting** 

## **Naam attribuutsoort** 

Reden opschorting 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

opschorting/reden 

Omschrijving van de reden voor het opschorten van de behandeling van de zaak. 

KING 

> **Datum opname attribuutsoort** 1 juni 2008 

**Toelichting attribuutsoort** 

Maakt deel uit van groepattribuutsoort Opschorting 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

178 

## **Indicatie kardinaliteit** 

## 0-1 

**Indicatie authentiek** 

**Regels attribuutsoort** 

## Gemeentelijk basisgegeven 

Indien het attribuutsoort 'Indicatie opschorting' de waarde 'J' heeft dan heeft ook dit attribuutsoort een waarde. 

## **Attribuutsoort Verlenging** 

## **Naam attribuutsoort** 

## **Herkomst attribuutsoort** 

Verlenging 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort** 

**Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

verlenging 

Gegevens omtrent het verlengen van de doorlooptijd van de behandeling van de ZAAK 

## KING 

**Datum opname attribuutsoort** 

## **Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

1 juni 2008 

Groepattribuutsoort, bestaande uit: Duur verlenging Reden verlenging 

Formaat: n.v.t. Waardenverzameling: 

Ja 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

**Indicatie kardinaliteit** 

0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Duur verlenging** 

**Naam attribuutsoort Herkomst attribuutsoort Code attribuutsoort** 

Duur verlenging 

KING 

**XML-tag attribuutsoort** 

verlenging/duur 

179 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

Het aantal werkbare dagen waarmee de doorlooptijd van de behandeling van  de  ZAAK  is  verlengd  (of  verkort)  ten  opzichte  van  de  eerder gecommuniceerde doorlooptijd. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

1 juni 2008 

Maakt deel uit van groepattribuutsoort Verlenging 

Formaat: N3 

Waardenverzameling: zowel positieve als negatieve getallen 

**Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels attribuutsoort** 

## **Attribuutsoort Reden verlenging** 

> **Naam attribuutsoort** Reden verlenging 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** verlenging/reden 

> **Definitie attribuutsoort** Omschrijving van de reden voor het verlengen van de behandeling van de zaak. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Maakt deel uit van groepattribuutsoort Verlenging 

> **Domein attribuutsoort** Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Maakt deel uit van groepattribuutsoort Verlenging 

180 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit Indicatie authentiek** 

1-1 

Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

## **Groepattribuutsoort Ander zaakobject** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Ander zaakobject 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

anderZaakobject 

Aanduiding van het object (of de objecten) waarop de ZAAK betrekking heeft indien dat object (of die objecten) niet aangeduid kan worden met de relatie ‘heeft betrekking op ZAAKOBJECT’. 

## KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

1 juni 2008 

Het gaat hier om objecten  die  niet benoemd  zijn  als  ZAAKOBJECT. Bijvoorbeeld de invalidenparkeerplaats waarvoor een parkeervergunning verleend is.  Het kan om zowel ruimtelijke als andere objecten gaan. In het eerste geval verschaft het attribuuttype Zaakobjectlokatie inzicht in de ligging. 

Het betreft een groepattribuutsoort dat bestaat uit de volgende attribuutsoorten: 

- Ander zaakobject omschrijving 

- Ander zaakobject aanduiding 

- Ander zaakobject lokatie 

- Ander zaakobject registratie **Domein attribuutsoort** Formaat: n.v.t. Waardenverzameling: **Indicatie materiële historie** Ja **Indicatie formele historie** Ja **Aanduiding gebeurtenis** Nee **Aanduiding brondocument** Nee **Indicatie in onderzoek** Nee **Aanduiding strijdigheid/nietigheid** Nee **Indicatie kardinaliteit** 0-N **Indicatie authentiek** Gemeentelijk basisgegeven 

181 

## **Regels attribuutsoort** 

Indien deze groepattribuutsoort niet van een waarde is voorzien, dan moet er minimaal sprake zijn van één relatie ‘ZAAK heeft betrekking op ZAAKOBJECTen’, één relatie ‘ZAAK heeft betrekking op andere ZAAKen’ of één relatie ‘ZAAK is deelzaak van ZAAK’.. 

## **Attribuutsoort Ander zaakobject omschrijving** 

> **Naam attribuutsoort** Ander zaakobject omschrijving 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** AnderZaakobject/omschrijving 

> **Definitie attribuutsoort** Een korte omschrijving van de aard van het zaakobject. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Voorbeelden  hiervan  zijn  ‘Invalidenparkeerplaats’,  ín-  of  uitritlokatie’ lantaarnpaal, speelplek of -tuig en chemische opslagtank. 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven - **Regels attribuutsoort** 

## **Attribuutsoort Ander zaakobject aanduiding** 

> **Naam attribuutsoort** Ander zaakobject aanduiding 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** anderZaakobject/aanduiding 

> **Definitie attribuutsoort** Een identificerende beschrijving van het zaakobject. 

> **Herkomst definitie attribuutsoort** KING 

182 

## **Datum opname attribuutsoort** 

1 juni 2008 

## **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek Regels attribuutsoort** 

Gemeentelijk basisgegeven 

Indien deze attribuutsoort niet van een waarde is voorzien, dan moet de attribuutsoort ‘Zaakobjectlokatie’ van een waarde voorzien zijn. 

## **Attribuutsoort ander zaakobject lokatie** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Ander zaakobject lokatie 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

anderZaakobject/lokatie 

De minimaal tweedimensionale geometrische representatie van de ligging of de omtrek van het zaakobject. 

KING 

**Datum opname attribuutsoort** 

**Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

1 juni 2008 

Dit betreft zaakobjecten  zijnde ruimtelijke  objecten. Dit kunnen  zowel punt-, lijn- als vlakobjecten zijn. Daarvan wordt met dit attribuutsoort de geometrie (‘een kaartje’) vastgelegd. 

Formaat: GML 

Waardenverzameling: aanduiding  van het type geometrie (Punt, Lijn., Vlak, MultiVlak), gevolgd door coördinatenparen binnen de in Nederland gelegen waarden van het RD-stelsel 

## **Indicatie materiële historie** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

183 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Indien deze attribuutsoort niet van een waarde is voorzien, dan moet de attribuutsoort ‘Zaakobjectaanduiding’ van een waarde voorzien zijn. 

## **Attribuutsoort Ander zaakobject registratie** 

> **Naam attribuutsoort** Ander zaakobject registratie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** anderZaakobject/registratie 

> **Definitie attribuutsoort** De naam van de registratie waarin gegevens van het ANDER ZAAKOBJECT worden beheerd. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN50 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort ZAAK heeft betrekking op andere ZAAKen** 

> **Naam relatiesoort** ZAAK heeft betrekking op andere ZAAKen 

> **Herkomst relatiesoort** GFO Zaken 2004, aangepast door KING **Code relatiesoort** 

> **Definitie relatiesoort** De andere ZAAKen die het onderwerp zijn van de ZAAK. 

> **Herkomst definitie relatiesoort** KING 

184 

**Datum opname relatiesoort** 

**Toelichting relatiesoort** 

## **Indicatie materiële historie** 

## 1 juni 2008 

Het gaat hier om eerder in behandeling genomen en/of afgeronde zaken die aamleiding geven tot het verzoeken om een nieuwe zaak. Bijvoorbeeld in het geval van een bezwaar (nieuwe  zaak) tegen een besluit dat is genomen in een andere zaak. 

Ja 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 0-M; N-M-relatie ) 

> **Indicatie authentiek** Gemeentelijk basisgegeven **Regels relatiesoort** 

Indien  deze  relatiesoort  niet  voorkomt  bij  een  zaak,  dan  moet  de attribuutsoort ‘Ander zaakobject’ van een waarde voorzien zijn dan wel moet er minimaal sprake zijn van één relatiesoort ‘ZAAK heeft betrekking op ZAAKOBJECTen’ of één relatiesoort ‘ZAAK is deelzaak van ZAAK’. 

## **Relatiesoort ZAAK is deelzaak van ZAAK** 

## **Naam relatiesoort** 

ZAAK is deelzaak van ZAAK 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

## **Herkomst definitie relatiesoort** 

De  verwijzing  naar  de  ZAAK,  waarom  verzocht  is  door  de  initiator daarvan, die door de zaakbehandelende organisatie is opgedeeld in twee of meer separaat te behandelen zaken waarvan de onderhavige zaak er één is. 

KING 

**Datum opname relatiesoort** 

**Toelichting relatiesoort** 

## **Indicatie materiële historie** 

1 juni 2008 

Niet altijd is het mogelijk om een zaak, die in de ogen van de initiator daarvan als één samenhangend geheel beschouwd wordt, als één zaak binnen de organisatie te behandelen. In dat geval kan de zaakbehandelende  organisatie  de  aangevraagde  zaak  opsplitsen  in meerdere ‘deelzaken’ die ieder op zich weer een zaak vormen. Voor de initiator is en blijft de zaak als geheel relevant. De zaakbehandelende organisatie richt zich meer op de deelzaken. De relatiesoort brengt het verband  aan  tussen  al  deze  zaken  zodat  alle  betrokkenen  juist  en doelgericht geinformeerd zijn. 

Ja 

**Indicatie formele historie** 

Ja 

**Aanduiding gebeurtenis** 

Nee 

185 

## **Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

## Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa : 0-N) **Indicatie authentiek Regels relatiesoort** 

Gemeentelijk basisgegeven 

De relatie vanuit een zaak mag niet verwijzen naar detzelfde zaak d.w.z. moet verwijzen naar een andere zaak. 

Indien  deze  relatiesoort  niet  voorkomt  bij  een  zaak,  dan  moet  de attribuutsoort ‘Ander zaakobject’ van een waarde voorzien zijn dan wel moet er minimaal sprake zijn van één relatiesoort ‘ZAAK heeft betrekking op  ZAAKOBJECTen’  of  één  relatiesoort  ‘ZAAK  heeft  betrekking  op andere ZAAK’. 

## **Relatiesoort ZAAK heeft betrekking op ZAAKOBJECTen** 

## **Naam relatiesoort** 

**Herkomst relatiesoort Code relatiesoort Definitie relatiesoort** 

ZAAK heeft betrekking op ZAAKOBJECTen 

KING 

Het OBJECT of de OBJECTen die het onderwerp zijn van de ZAAK. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 

**Toelichting relatiesoort** 

Het gaat hier om de relatie naar de in het RSGB gespecificeerde objecten waarop  een  zaak  betrekking  kan  hebben  via  het  relatie-objecttype ZAAKOBJECT.  Bijvoorbeeld,  bij  een  zaak  van  zaaktype  ‘Behandelen aanvraag  bouwvergunning’  met  als  Omschrijving  ‘Uitbreiden  van  de woning aan de achterzijde’ betreft het de relatie naar het object zijnde het verblijfsobject  dat  correspondeert  met  genoemde  woning  (met  het bijbehorende adres). Ook kan een zaak betrekking hebben op personen, bijvoorbeeld bij een verhuizing van een gezin. De initiator van de zaak (in zijn rol als betrokkene) is bijvoorbeeld het 'gezinshoofd'. De objecten waarop de zaak betrekking heeft zijn alle gezinsleden waaronder het gezinshoofd, 

## **Indicatie materiële historie** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

186 

## **Regels relatiesoort** 

Indien  deze  relatiesoort  niet  voorkomt  bij  een  zaak,  dan  moet  de attribuutsoort ‘Ander zaakobject’ van een waarde voorzien zijn dan wel moet er minimaal sprake zijn van één relatiesoort ‘ZAAK heeft betrekking op andere ZAAKen’ of één relatiesoort ‘ZAAK is deelzaak van ZAAK’. 

## **Relatiesoort ZAAK heeft betrokkenen in ROLlen** 

**Naam relatiesoort Herkomst relatiesoort** 

ZAAK heeft betrokkenen in ROLlen 

KING 

**Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 1 juni 2008 

De ROLlen die door betrokkenen worden uitgeoefend in de ZAAK. 

**Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAK heeft ZAAKDOCUMENTen** 

> **Naam relatiesoort** ZAAK heeft ZAAKDOCUMENTen 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De DOCUMENTen die aan de ZAAK zijn gerelateerd 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

187 

## **Aanduiding gebeurtenis** 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAK heeft STATUSsen** 

> **Naam relatiesoort** ZAAK heeft STATUSsen 

> **Herkomst relatiesoort** GFO Zaken 2004 

**Code relatiesoort** 

**Definitie relatiesoort Herkomst definitie relatiesoort Datum opname relatiesoort** 

De STATUSsen die bereikt zijn gedurende de behandeling van de ZAAK. KING 1 juni 2008 

## **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAK kan leiden tot BESLUIT** 

> **Naam relatiesoort** ZAAK kan leiden tot BESLUIT 

> **Herkomst relatiesoort** KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De  BESLUITen  die  in  het  kader  van  de  behandeling  van  de  ZAAK genomen zijn. 

188 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAK is van ZAAKTYPE** 

> **Naam relatiesoort** ZAAK is van ZAAKTYPE 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** Aanduiding van de aard van de ZAAK. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

189 

## **4.15. Zaakdocument** 

## **Attribuutsoort Zaakdocumenttitel** 

## **Naam attribuutsoort** 

Zaakdocumenttitel 

**Herkomst attribuutsoort** 

KING op basis van de Dublin Core 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

**Indicatie materiële historie** 

titel 

De naam waaronder het document binnen de zaak bekend is. 

KING op basis van de Dublin Core 

1 juni 2008 

Het betreft het Dublin Core metadata-element ‘Title’ met als toelichting: Typically, Title will be a name by which the resource is formally known. De naam zal veelal gelijk zijn aan of afgeleid zijn van de generieke naam van het document (bij DOCUMENT). 

Formaat: AN200 Waardenverzameling: alle alfanumerieke tekens 

Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Zaakdocumentbeschrijving** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Zaakdocumentbeschrijving 

KING op basis van de Dublin Core 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

beschrijving 

Een op de zaak gerichte beschrijving van de inhoud van het document. KING op basis van de Dublin Core 

1 juni 2008 

190 

## **Toelichting attribuutsoort** 

Het  betreft  het  Dublin  Core  metadata-element  ‘Description’  met  als toelichting: Examples of Description include, but are not limited to, an abstract, table  of contents, reference to a  graphical  representation of content, or free-text account of the content. 

De beschrijving zal veelal gelijk zijn aan of afgeleid zijn van de generieke beschrijving van de inhoud van het document (bij DOCUMENT). 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Document registratiedatum** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Document registratiedatum 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

registratiedatum 

De datum waarop de zaakbehandelende organisatie het DOCUMENT heeft geregistreerd bij de ZAAK. 

KING 

**Datum opname attribuutsoort** 

1 juni 2008 

**Toelichting attribuutsoort** 

**Domein attribuutsoort** 

## **Indicatie materiële historie** 

Formaat: datum (JJJJMMDD) Waardenverzameling: Alle geldige datums gelegen op of voor de huidige datum en tijd 

Nee 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek** 

Nee 

Nee 

Nee 

Nee 

191 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort ZAAKDOCUMENT betreft ZAAK** 

> **Naam relatiesoort** ZAAKDOCUMENT betreft ZAAK 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De ZAAK waaraan het ZAAKDOCUMENT het DOCUMENT relateert. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 1-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAKDOCUMENT betreft DOCUMENT** 

**Naam relatiesoort** 

ZAAKDOCUMENT betreft DOCUMENT 

**Herkomst relatiesoort Code relatiesoort** 

KING 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort Datum opname relatiesoort** 

Het DOCUMENTdat door het ZAAKDOCUMENT aan de ZAAK wordt gerelateerd. 

KING 

1 juni 2008 

**Toelichting relatiesoort** 

192 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAKDOCUMENT is relevant voor STATUS** 

**Naam relatiesoort** 

ZAAKDOCUMENT is relevant voor STATUS 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort** 

De  bij  de  desbetreffende  ZAAK  behorende  STATUS  waarvoor  het ZAAKDOCUMENT relevant is (geweest) met het oog op het bereiken van die STATUS en/of de communicatie daarover. 

KING 

**Datum opname relatiesoort** 

## 22-05-09 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

De relatiesoort is de tegenhanger van 'STATUS heeft daarvoor relevante ZAAKDOCUMENTen'. Zie verder de toelichting bij die relatiesoort. 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

**Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

**Indicatie kardinaliteit** 

**Indicatie authentiek Regels relatiesoort** 

0-1 (vice versa: 0-N) 

## Gemeentelijk basisgegeven 

Alleen  die  status  kan  gerelateerd  zijn  die  gerelateerd  is  aan  de desbetreffende zaak. 

193 

## **4.16. Zaakobject** 

## **Attribuutsoort Relatie-omschrijving** 

## **Naam attribuutsoort** 

Relatie-omschrijving 

> **Herkomst attribuutsoort** KING 

**Code attribuutsoort** 

> **XML-tag attribuutsoort** omschrijving 

> **Definitie attribuutsoort** Omschrijving van de betrekking tussen de ZAAK en het OBJECT 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 22 mei 2009 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN80 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Relatiesoort ZAAKOBJECT is onderwerp van ZAAK** 

> **Naam relatiesoort** ZAAKOBJECT is onderwerp van ZAAK 

> **Herkomst relatiesoort** KING **Code relatiesoort** 

> **Definitie relatiesoort** De ZAAK die via het ZAAKOBJECT betrekking hebben op een OBJECT. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

194 

## **Aanduiding gebeurtenis** 

Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels relatiesoort** 

- 

## **Relatiesoort ZAAKOBJECT betreft OBJECT** 

## **Naam relatiesoort** 

ZAAKOBJECT betreft OBJECT 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort Definitie relatiesoort** Het OBJECT waarop een ZAAK via het ZAAKOBJECT betrekking heeft **Herkomst definitie relatiesoort** KING **Datum opname relatiesoort** 22 mei 2009 

**Toelichting relatiesoort** 

> **Indicatie materiële historie** Ja 

> **Indicatie formele historie** Ja 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

195 

## **4.17. Zaaktype** 

## **Attribuutsoort Zaaktype-omschrijving** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Zaaktype-omschrijving 

GFO Zaken 2004 

**Code attribuutsoort** 

0005 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

**Domein attribuutsoort** 

omschrijving 

Omschrijving van de aard van ZAAKen van het ZAAKTYPE. 

GFO Zaken 2004, aangepast door KING 

1 juni 2008 

Het betreft de gelijknamige  attribuutsoort bij Zaak  in het GFO Zaken 2004. 

Formaat: AN80 

Waardenverzameling: alle alfanumerieke tekens 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Zaaktype-omschrijving generiek** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Zaaktype-omschrijving generiek 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

omschrijvingGeneriek 

Algemeen gehanteerde omschrijving van de aard van ZAAKen van het ZAAKTYPE 

KING 

**Datum opname attribuutsoort** 

1 juni 2008 

196 

## **Toelichting attribuutsoort** 

Het gaat hier om een korte omschrijving van de aard van de zaak, ook wel zaaknaam genoemd, zoals deze landelijk wordt toegepast. Deze kan afwijken van de door de zaakbehandelende organisatie(s) gehanteerde naam, de Zaaktype-omschrijving. De domeinwaarden zijn opgenomen in een specifieke tabel. De desbetreffende waarden zijn afgeleid van de Zaaktypecatalogus en vermeld in het document 'RGBZ domeintabellen'. 

## **Domein attribuutsoort** 

Formaat: AN80 Waardenverzameling: zie ZTG-tabel . 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 **Indicatie authentiek** 

> **Regels attribuutsoort** - 

Gemeentelijk basisgegeven 

## **Attribuutsoort Trefwoord** 

## **Naam attribuutsoort** 

Trefwoord 

**Herkomst attribuutsoort** 

GFO Zaken 2004 

> **Code attribuutsoort** 0006 

> **XML-tag attribuutsoort** trefwoord **Definitie attribuutsoort** 

Een trefwoord waarmee ZAAKen van het ZAAKTYPE kunnen worden gekarakteriseerd. 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 1 juni 2008 

GFO Zaken 2004, aangeoast door KING 

**Toelichting attribuutsoort** 

Het betreft de gelijknamige  attribuutsoort bij Zaak  in het GFO Zaken 2004. 

**Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN30 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

197 

## **Indicatie kardinaliteit** 

## 0-N 

**Indicatie authentiek** 

**Regels attribuutsoort** 

Gemeentelijk basisgegeven 

- 

## **Attribuutsoort Doorlooptijd behandeling** 

**Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Doorlooptijd behandeling 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort Toelichting attribuutsoort** 

## **Domein attribuutsoort** 

**Indicatie materiële historie** 

## doorlooptijd 

De periode waarbinnen volgens wet- en regelgeving een ZAAk van het ZAAKTYPE afgerond dient te zijn. 

## KING 

## 1 juni 2008 

De periode is in werkbare dagen; zie voor een definitie van dit begrip […]. De  startdatum  van  de  zaak  markeert  de  eerste  dag.  De  uiterlijke einddatum van de zaak markeert de laatste dag. . 

Formaat: N3 (in werkbare dagen) Waardenverzameling: 1-999 

Nee 

**Indicatie formele historie Aanduiding gebeurtenis Aanduiding brondocument Indicatie in onderzoek Aanduiding strijdigheid/nietigheid Indicatie kardinaliteit** 1-1 **Indicatie authentiek Regels attribuutsoort** - 

Nee 

Nee 

Nee Nee 

Nee 

Gemeentelijk basisgegeven 

## **Attribuutsoort Servicenorm behandeling** 

> **Naam attribuutsoort** Servicenorm behandeling 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** servicenorm 

198 

## **Definitie attribuutsoort** 

## **Herkomst definitie attribuutsoort** 

De periode waarbinnen verwacht wordt dat een ZAAk van het ZAAKTYPE afgerond wordt coform de geldende servicenormen van de zaakbehandelende organisatie(s). 

KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

De periode is in werkbare dagen; zie voor een definitie van dit begrip […]. De  startdatum  van  de  zaak  markeert  de  eerste  dag.  De  geplande einddatum van de zaak markeert de laatste dag. 

**Domein attribuutsoort** 

Formaat: N3 (in werkbare dagen) Waardenverzameling: 1-999 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** Deze  periode  mag  niet  langer  zijn  dan  de  periode  van  Doorlooptijd behandeling. 

## **Attribuutsoort Archiefcode** 

> **Naam attribuutsoort** Archiefcode 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** archiefcode 

> **Definitie attribuutsoort** De  systematische  identificatie  van  zaakdossiers  van  dit  ZAAKTYPE overeenkomstig logisch gestructureerde conventies, methoden en procedureregels. 

> **Herkomst definitie attribuutsoort** KING, op basis van NEN 2082. 

> **Datum opname attribuutsoort** 1 juni 2008 

> **Toelichting attribuutsoort** Een zaakdossier betreft alle informatie over een zaak (en daarvan deel uit makende deelzaken) inclusief alle daarbij geregistreerde documenten. 

> **Domein attribuutsoort** Formaat: AN20 Waardenverzameling: alle alfanumerieke tekens m..u.v. diacrieten 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

199 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Vertrouwelijk aanduiding** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Vertrouwelijk aanduiding 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

vertrouwelijkAanduiding 

Aanduiding  van  de  mate  waarin  zaakdossiers  van  ZAAKen  van  dit ZAAKTYPE voor de openbaarheid bestemd zijn. 

KING 

**Datum opname attribuutsoort Toelichting attribuutsoort** 

## 1 juni 2008 

Een zaakdossier betreft alle informatie over een zaak (en daarvan deel uit makende deelzaken) inclusief alle daarbij geregistreerde documenten. De domeinwaarden zijn afgeleid van het Besluit voorschrift informatiebeveiliging rijksdienst  bijzondere informatie (VIRBI). 

200 

## **Domein attribuutsoort** 

||||
|---|---|---|
|**Domein attribuutsoort**|Formaat:|AN20|
||Waardenverzameling: ZEER  GEHEIM  (indien  kennisnemen  door  niet||
|||gerechtigden zeer ernstige schade kan|
|||toebrengen aan het belang van de Staat of|
|||zijn bondgenoten)|
|||GEHEIM (indien kennisnemen door niet|
|||gerechtigden ernstige schade kan toebrengen|
|||aan het belang van de Staat of zijn|
|||bondgenoten)|
|||CONFIDENTIEEL (indien kennisnemen door niet|
|||gerechtigden schade kan toebrengen aan het|
|||belang van de Staat of zijn bondgenoten)|
|||VERTROUWELIJK (indien kennisnemen door niet|
|||gerechtigden nadeel kan toebrengen aan het|
|||belang van één of meer zaakbehandelende|
|||organisaties, betrokkenen bij de zaak en/of|
|||andere publliekrechtelijke organisaties)|
|||ZAAKVERTROUWELIJK (indien kennisnemen|
|||door anderen dan betrokkenen bij de zaak|
|||nadeel kan toebrengen aan het belang van|
|||één of meer zaakbehandelende organisaties,|
|||betrokkenen bij de zaak en/of andere|
|||publliekrechtelijke organisaties)|
|||INTERN (indien kennisnemen door anderen dan|
|||medewerkers van de zaakbehandelende|
|||organisatie(s) nadeel kan toebrengen aan het|
|||belang van één of meer zaakbehandelende|
|||organisaties, betrokkenen bij de zaak en/of|
|||andere publliekrechtelijke organisaties)|
|||BEPERKT OPENBAAR (indien kennisnemen door|
|||anderen dan medewerkers van de|
|||zaakbehandelende<br>organisatie(s)|
|||betrokkenen bij de zaak nadeel kan|
|||toebrengen aan het belang van één of meer|
|||zaakbehandelende organisaties, betrokkenen|
|||bij  de  zaak  en/of andere  publliekrechtelijke|
|||organisaties)|
|||OPENBAAR (in alle andere gevallen)|
|**Indicatie materiële historie**|Nee||
|**Indicatie formele historie**|Nee||
|**Aanduiding gebeurtenis**|Nee||
|**Aanduiding brondocument**|Nee||
|**Indicatie in onderzoek**|Nee||
|**Aanduiding strijdigheid/nietigheid**|Nee||
|**Indicatie kardinaliteit**|1-1||
|**Indicatie authentiek**|Gemeentelijk basisgegeven||
|**Regels attribuutsoort**|-||



201 

## **Attribuutsoort Publicatie-indicatie** 

## **Naam attribuutsoort** 

Publicatie-indicatie 

**Herkomst attribuutsoort** 

KING 

## **Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort** 

publicatieIndicatie 

Aanduiding of (het starten van) een ZAAK van dit ZAAKTYPE gepubliceerd moet worden. 

KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

Het gaat hier niet alleen om de wettelijke verplichting tot publicatie maar ook  om  de  eigen  keuze  van  de  organisatie  die  zaken  van  dit  type behandelt. 

**Domein attribuutsoort** 

Formaat: AN1 Waardenverzameling: J, N 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Zaakcategorie** 

> **Naam attribuutsoort** Zaakcategorie 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** zaakcategorie 

> **Definitie attribuutsoort** Typering van de aard van ZAAKen van het ZAAKTYPE. 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 

1 juni 2008 

202 

## **Toelichting attribuutsoort** 

Het  gaat  hier  om  de  indeling  van  zaaktypen  naar  categorien  zoals Behandelen  vergunningaanvraag,  Behandelen  ontheffingaanvraag  en Behandelen subsidie-aanvraag., 

> **Domein attribuutsoort** Formaat: AN40 Waardenverzameling: zie Zaaktypecatalogus 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels attribuutsoort** - 

## **Attribuutsoort Publicatietekst** 

> **Naam attribuutsoort** Publicatietekst 

> **Herkomst attribuutsoort** KING **Code attribuutsoort** 

> **XML-tag attribuutsoort** publicatietekst 

> **Definitie attribuutsoort** De generieke tekst van de publicatie van ZAAKen van dit ZAAKTYPE 

> **Herkomst definitie attribuutsoort** KING 

> **Datum opname attribuutsoort** 1 juni 2008 **Toelichting attribuutsoort** 

> **Domein attribuutsoort** Formaat: AN1000 Waardenverzameling: alle alfanumerieke tekens 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

203 

- 

## **Regels attribuutsoort** 

## **Attribuutsoort Datum begin geldigheid zaaktype** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort Code attribuutsoort** 

Datum begin geldigheid zaaktype 

## KING 

**XML-tag attribuutsoort Definitie attribuutsoort Herkomst definitie attribuutsoort** KING **Datum opname attribuutsoort** 29 mei 2009 **Toelichting attribuutsoort** 

ingangsdatumObject 

De datum waarop het ZAAKTYPE is ontstaan. 

Met deze datum wordt aangegeven vanaf wanneer het zaaktype bestaat en toegepast kan worden. 

**Domein attribuutsoort** 

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

## **Attribuutsoort Datum einde geldigheid zaaktype** 

## **Naam attribuutsoort** 

**Herkomst attribuutsoort** 

Datum einde geldigheid zaaktype 

KING 

**Code attribuutsoort** 

**XML-tag attribuutsoort Definitie attribuutsoort** 

**Herkomst definitie attribuutsoort Datum opname attribuutsoort** 

einddatumObject 

De datum waarop het ZAAKTYPE is opgeheven. 

## KING 

29 mei 2009 

**Toelichting attribuutsoort** 

Met deze datum wordt aangegeven vanaf wanneer het zaaktype niet meer bestaat en niet meer toegepast kan worden. 

204 

## **Domein attribuutsoort** 

> **Domein attribuutsoort** Formaat: OnvolledigeDatum 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

**Regels attribuutsoort** 

Alleen een datum die gelijk is aan of die gelegen is na de datum zoals opgenomen onder 'Datum begin geldigheid zaaktype’ kan in de registratie worden opgenomen. 

## **Relatiesoort ZAAKTYPE betreft ZAAKen** 

## **Naam relatiesoort** 

ZAAKTYPE betreft ZAAKen 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

**Herkomst definitie relatiesoort Datum opname relatiesoort Toelichting relatiesoort** 

Verwijzing naar de ZAAKen van dit ZAAKTYPE. 

KING 

1 juni 2008 

**Indicatie materiële historie** 

Nee 

**Indicatie formele historie** 

**Aanduiding gebeurtenis** 

**Aanduiding brondocument** 

**Indicatie in onderzoek** 

Nee Nee Nee Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

205 

## **Relatiesoort ZAAKTYPE heeft STATUSTYPEn** 

## **Naam relatiesoort** 

ZAAKTYPE heeft STATUSTYPEn 

**Herkomst relatiesoort** 

KING 

**Code relatiesoort** 

**Definitie relatiesoort** 

De  STATUSTYPEn  die  bereikt  kunnen  worden  bij  behandeling  van ZAAKen van het ZAAKTYPE. 

> **Herkomst definitie relatiesoort** KING 

> **Datum opname relatiesoort** 1 juni 2008 **Toelichting relatiesoort** 

De relatiesoort is vooral opgenomen teneinde  betrokkenen te kunnen informeren wat de eerstvolgend te bereiken status in een zaak is en binnen welke termijn het bereiken van die status verwacht wordt. 

## **Indicatie materiële historie** 

Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 1-N (vice versa: 1-1) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** - 

## **Relatiesoort ZAAKTYPE heeft verantwoordelijke ORGANISATORISCHE EENHEID** 

## **Naam relatiesoort** 

**Herkomst relatiesoort** 

**Code relatiesoort** 

ZAAKTYPE heeft verantwoordelijke ORGANISATORISCHE EENHEID 

KING op basis van GFO Zaken 2004 

0008 

> **Definitie relatiesoort** De verantwoordelijk ORGANISATORISCHE EENHEID voor ZAAKen van het ZAAKTYPE. 

**Herkomst definitie relatiesoort** 

**Datum opname relatiesoort** 

**Toelichting relatiesoort** 

**Indicatie materiële historie** 

KING op basis van het GFO Zaken 2004 

1 juni 2008 

De relatiesoort is afgeleid van de attribuutsoort Verantwoordelijke bij Zaak in het GFO Zaken 2004. 

Nee 

**Indicatie formele historie** 

Nee 

**Aanduiding gebeurtenis** 

Nee 

206 

## **Aanduiding brondocument** 

Nee 

**Indicatie in onderzoek** 

Nee 

**Aanduiding strijdigheid/nietigheid** 

Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien een relatie van deze soort voorkomt, kan er geen relatie van de soort  ZAAKTYPE heeft verantwoordelijke MEDEWERKER voorkomen. 

## **Relatiesoort ZAAKTYPE heeft verantwoordelijke MEDEWERKER** 

> **Naam relatiesoort** ZAAKTYPE heeft verantwoordelijke MEDEWERKER 

> **Herkomst relatiesoort** KING op basis van GFO Zaken 2004 

> **Code relatiesoort** 0008 

> **Definitie relatiesoort** De verantwoordelijk MEDEWERKER voor ZAAKen van het ZAAKTYPE. 

> **Herkomst definitie relatiesoort** KING op basis van het GFO Zaken 2004 

> **Datum opname relatiesoort** 1 juni 2008 

> **Toelichting relatiesoort** De relatiesoort is afgeleid van de  attribuutsoort Verantworordelijke bij Zaak in het GFO Zaken 2004. 

> **Indicatie materiële historie** Nee 

> **Indicatie formele historie** Nee 

> **Aanduiding gebeurtenis** Nee 

> **Aanduiding brondocument** Nee 

> **Indicatie in onderzoek** Nee 

> **Aanduiding strijdigheid/nietigheid** Nee 

> **Indicatie kardinaliteit** 0-1 (vice versa: 0-N) 

> **Indicatie authentiek** Gemeentelijk basisgegeven 

> **Regels relatiesoort** Indien een relatie van deze soort voorkomt, kan er geen relatie van de soort ZAAKTYPE heeft verantwoordelijke ORGANISATORISCHE EENHEID voorkomen. 

207 

## **Bijlage 1: Dublin Core** 

Een deel van de attribuut- en relatiesoorten van documenten hebben we ontleend aan de Dublin Core 'standaard' (zie “Information and documentation — The Dublin Core metadata element set”; ISO, 2003).  In deze bijlage geven we  we aan hoe de Dublin Core metadata element set zich verhoudt tot de in het RGBZ opgenomen attribuut- en relatiesoorten. 

||**Dublin Core**|**RGBZ**|
|---|---|---|
|**Element**|**Contributor**|-|
||Definitie: An entity responsible for making<br>contributions to the content of the resource|Opmerking: niet overgenomen in het RGBZ<br>aangezien voor zaakgericht werken de<br>creator vooral van belang is.|
|**Element**|**Creator**|DOCUMENT . Documentauteur|
||Definitie: An entity primarily responsible for<br>making the content of the resource||
|**Element**|**Date**|DOCUMENT . Documentcreatiedatum|
||Definitie: A date of an event in the lifecycle of<br>the resource||
|**Element**|**Description**|DOCUMENT . Documentbeschrijving<br>ZAAKDOCUMENT . Zaakdocument-<br>beschrijving|
||Definitie: An account of the content of the<br>resource|Opmerking: het betreft de (korte) beschrijving<br>van de inhoud van het document in het<br>algemeen resp. de (korte) beschrijving van de<br>inhoud van het document in relatie tot de<br>zaak waaraan het document gerelateerd is.|
|**Element**|**Format**|ENKELVOUDIG DOCUMENT .<br>Documentformaat|
||Definitie: The physical or digital manifestation<br>of the resource|Opmerking: het betreft de aanduiding van de<br>bestandsoort van het digitale bestand waarin<br>het document is vastgelegd, zoals .pdf|
|**Element**|**Identifier**|DOCUMENT . Documentidentificatie|
||Definitie: An unambiguous reference to the<br>resource within a given context||
|**Element**|**Language**|ENKELVOUDIG DOCUMENT .Documenttaal|
||Definitie: A language of the intellectual<br>content of the resource||
|**Element**|**Publisher**|-|
||Definitie: An entity responsible for making the<br>resource available|Opmerking: niet in het RGBZ opgenomen<br>aangezien de waarde van dit gegeven<br>samenhangt met de organisatie waarbinnen<br>het document gecreëerd is.|
|**Element**|**Relation**|-|
||Definitie: A reference to a related resource|Opmerking: niet in het RGBZ opgenomen in<br>de overweging dat dit onvoldoende relevant<br>is voor zaakgericht werken. Daarin verwijzen|



208 

||**Dublin Core**|**RGBZ**|
|---|---|---|
|||immers zaken naar elkaar, daar waar van<br>toepassing.|
|**Element**|**Source**|-|
||Definitie: A reference to a resource from<br>which the present resource is derived|Opmerking: zie opmerking bij 'Relation'.|
|**Element**|**Subject**|DOCUMENTTYPE .Documenttype-<br>omschrijving|
||Definitie: A topic of the content of the<br>resource|Opmerking: het betreft de omschrijving van<br>de aard van het document, niet van de<br>specifieke inhoud. De Dublin Core spreekt<br>over 'keywords' uit een 'classification<br>scheme'.|
|**Element**|**Title**|DOCUMENT . Documenttitel<br>ZAAKDOCUMENT . Zaakdocumenttitel|
||Definitie: A name given to the resource|Opmerking: het betreft de naam waaronder<br>het document in het algemeen bekend is<br>resp. de naam die aan het document binnen<br>de zaak gegeven is.|
|**Element**|**Type**|DOCUMENTTYPE . Documentcategorie|
||Definitie: The nature or genre of the content<br>of the resource|Opmerking: het betreft de categorisering van<br>de waarden van 'Subject' cq. ' Documenttype-<br>omschrijving'.|



209 

