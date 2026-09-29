---
title: "digiGO Informatiemodel Woongebouwen (IMWO)"
source: "https://nl-digigo.github.io/imwo/functional-doc-1-0/1.0/h/v1/imwo-rapport.html"
author: "digiGO"
published: 2026-07-01
created: 2026-09-24
description: "Formeel conceptueel informatiemodel voor woning en woongebouw: uitwerking van het GEBORA-bedrijfsobjectenmodel (domein Bouwwerk) met ~200 objecttypen, definities en relaties, gebaseerd op IFC, CityGML, NEN 2660 en NEN 3610."
tags:
  - "Standaarden"
---

## Inleiding

### Achtergrond

De ketenpartners die in het Bestuursakkoord Digitale Gebouwde Omgeving afspraken gemaakt hebben over digitaal samenwerken hebben geconstateerd dat gegevens over woningen en woongebouwen veelal niet goed uitwisselbaar zijn doordat iedere ketenpartner eigen definities en informatiemodellen heeft. Daarom hebben ze besloten een woongebouwinformatiemodel te ontwikkelen dat een brug slaat tussen hun eigen architectuur en definities en die van hun ketenpartners. Hierdoor wordt het makkelijk om elkaars begrippen te vertalen, informatie uit te wisselen en uiteindelijk het hergebruik van informatie en samenwerking tussen ketenpartners te bevorderen. 

### Projectorganisatie

| Naam                    | Organisatie                                | Rol                  |
| ----------------------- | ------------------------------------------ | -------------------- |
| Robert Versteeg         | digiGO                                     | Projectleider        |
| Hein Corstens           | digiGO                                     | Informatiemodelleur  |
| Martijn van Glabbeek    | digiGO                                     | Product Owner GEBORA |
| Paul Strokap            | Neprom                                     | Projectgroeplid      |
| Henk Nijstad            | Aedes                                      | Projectgroeplid      |
| Willem Pel              | Ketenstandaard                             | Projectgroeplid      |
| Gert Koutstaal          | Ketenstandaard                             | Projectgroeplid      |
| Ruud Kathmann           | Waarderingskamer                           | Projectgroeplid      |
| Rolf Jonker             | Geonovum / gemeente Rotterdam              | Projectgroeplid      |
| Wiechert Eschbach       | Windesheim Hogeschool                      | Projectgroeplid      |
| Gerlof de Haan          | Vereniging van Nederlandse Gemeenten (VNG) | Projectgroeplid      |
| Marco Witschge          | Techniek Nederland                         | Projectgroeplid      |
| Jan Brinkkemper         | Aedes                                      | Projectgroeplid      |
| Aydemir Çetin           | NL Ingenieurs / BuildingSmart              | Projectgroeplid      |
| Daniël Carree           | Rijksvastgoedbedrijf                       | Projectgroeplid      |
| Jan Hendrik Nieuwenhuis | Rijksvastgoedbedrijf                       | Projectgroeplid      |
| Jeroen Pat              | Techniek Nederland                         | Projectgroeplid      |
| Martijn Nijkamp         | BNA                                        | Stuurgroeplid        |
| Joppe Duindam           | Bouwend Nederland                          | Stuurgroeplid        |
| Alfred Boersma          | Rijksvastgoedbedrijf                       | Stuurgroeplid        |
| Jonathan Bosman         | Ministerie van Binnenlandse Zaken          | Stuurgroeplid        |
| Remco van der Linden    | Techniek Nederland                         | Stuurgroeplid        |
| Maurits Cammeraat       | digiGO                                     | Stuurgroeplid        |
| Roger Tan               | digiGO                                     | Stuurgroeplid        |
| Theo Peters             | Vereniging van Nederlandse Gemeenten (VNG) | Stuurgroeplid        |
| Bart Molmans            | Techniek Nederland                         | Klankbordgroeplid    |
| Bob Spitz               | V-OA Architecten                           | Klankbordgroeplid    |
| Chandro Kandiah         | Ictu                                       | Klankbordgroeplid    |
| Fatih Cingir            | NEN                                        | Klankbordgroeplid    |
| Marcel de Meulmeester   | Rijksvastgoedbedrijf                       | Klankbordgroeplid    |
| Oeds de Meer            | SBB Ontwikkelen en Bouwen                  | Klankbordgroeplid    |
| Pim van Meer            | Neprom                                     | Klankbordgroeplid    |
| Paul Oude Luttighuis    | Ministerie van Binnenlandse Zaken          | Klankbordgroeplid    |
| Jan Pieter Redert       | NWWI                                       | Klankbordgroeplid    |
| Bert Beentjes           | Kadaster                                   | Klankbordgroeplid    |
| Thies Mesdag            | Kadaster                                   | Klankbordgroeplid    |

Ontologische ondersteuning: Marcel Krassenburg

### Doel

Het doel van BM20 is een uitwerking tot begrippenkader en conceptueel informatiemodel van de begrippen woning en woongebouw, die ketenpartners kunnen (her-)gebruiken binnen hun eigen context. Het informatiemodel heeft de functie van referentiemodel en kan als ‘canoniek model’ – als centraal vertaalhulpmiddel – ingezet worden.

### Scope

Het informatiemodel heeft betrekking op informatie, die door meerdere ketenpartners wordt hergebruikt. Informatie die uitsluitend relevant is voor één ketenpartner valt daarmee buiten de scope van deze maatregel.

### Uitgangspunten

Het IMWO is een onderdeel van de GEBouwde Omgeving Referentie Architectuur (GEBORA).IMWO is een uitwerking van het Bedrijfsobjectenmodel (domein Bouwwerk).

Het IMWO is een conceptueel informatiemodel, dat de betekenis en de structuur van de relevante informatie beschrijft, onafhankelijk van het ontwerp van en de implementatie in systemen. Het is gericht op communicatie tussen domein- en IT-experts. 

De huidige versie van IMWO beperkt zich tot de specificatie van  objecttypen en relaties. Attribuutsoorten en kardinaliteiten komen nog niet of nauwelijks aan de orde: de prioriteit is gelegd bij het grip krijgen op de breedte van het domein. Pas bij de uitwerking per subdomein zal er dieper gegaan worden.

Het IMWO heeft betrekking op woningen en woongebouwen als fysieke objecten, aangevuld met aan die objecten klevende gegevens over gebruik, eigendom, bestemming, etc. Het wordt gezien als een onderdeel van een breder model van de gebouwde omgeving. Daartoe worden de specifieke onderdelen over woningen en woongebouwen 'opgehangen' aan een algemene kapstok, een 'topmodel' voor de gebouwde omgeving.

Het model is primair ontwikkeld op basis van de internationale standaarden IFC en CityGML en de nationale standaarden NEN 2660 en NEN 3610. Voor specifieke onderdelen is gebruik gemaakt van specifieke standaarden. Zo wordt bijvoorbeeld als het gaat om zakelijke rechten uitgegaan van het informatiemodel Kadaster (IMKAD).

### Model als Linked Data

Het model wordt ook beschikbaar gesteld als Linked Data. Als voorbeeld is een versie opgenomen als RDF/SKOS Turtle-bestand: [imwo_skos.ttl](./ttl/imwo_skos.ttl). Deze representatie volgt de structuur van de submodellen, objecttypen en hun onderlinge relaties. Hierbij zijn onder andere de objecttypen als concepten uitgewerkt en de hiërarchische relaties vooralsnog vastgelegd met behulp van SKOS-relaties zoals `skos:broader` en `skos:narrower`. 

Het IMWO-project was er in eerste instantie op gericht een eerste versie te ontwikkelen van een inhoudelijk semantisch model en niet op een technisch volwaardige implementatie. De vertaling naar LD is nu nog een extra. In de volgende versie dient de aansluiting op LD volledig gerealiseerd te worden. Daarbij gaat het vooral om de vertaling van het conceptuele informatiemodel naar rdfs/owl.

### Status van IMWO 1.0

Met deze beleidsmaatregel is gepoogd in korte tijd het thema Woongebouw in de volle breedte te vatten in een redelijk diepgaand conceptueel informatiemodel. Een informatiemodel dat ook nog eens via een topmodel is ingebed in het nog bredere thema Gebouwde omgeving. Én dat relaties legt met een groot aantal relevante standaarden. Onze poging is door inspanningen en denkwerk van de projectgroep geslaagd. Dat wil niet zeggen dat IMWO 1.0 perfect is. Verre van dat: het is een eerste poging, waarin op diverse momenten ervoor gekozen is **iets** te formuleren in plaats van lang te dubben over de details van een definitie. Het resultaat van het project is het **begin** van een ontwikkeling naar een steeds completer en nauwkeuriger wordend model, dat standaarden verbindt en harmoniseert, gericht op verbetering van **semantische interoperabiliteit**.

## Methodologie

### Richtlijnen

Voor de definities heeft de projectgroep IMWO richtlijnen opgesteld. Op 27 januari 2026 zijn die door de stuurgroep IMWO vastgesteld. Doelstelling ervan is het bieden van een praktische handreiking voor het toepassen van NL-SBB binnen IMWO. Bij eventuele tegenstrijdigheden heeft NL-SBB voorrang op basis van het principe pas-toe-of-leg-uit. De richtlijnen zijn in Bijlage 3 te vinden.

### Semantiek

Het IMWO is in deze fase een **semantisch** informatiemodel. Dat houdt in dat begrippen en relaties gebaseerd zijn op **betekenis**. Begrippen worden, uitgaande van een aantal niet nader te definiëren begrippen, gedefinieerd in termen van elkaar. Hierdoor worden de relaties bepaald door de definities. Er is bijvoorbeeld een relatie tussen een Bouwwerk en een Gebouw: ieder Gebouw is een Bouwwerk (generalisatie). Een Gebouw wordt gedefinieerd als een Bouwwerk, waaraan iets toegevoegd wordt (zoals dat het afsluitbaar is en een verblijfsfunctie heeft). 

Het op deze wijze definiëren is geen triviale zaak en de definities in de huidige versie van IMWO dienen als een eerste aanzet gezien te worden, waaraan nog veel denk- en doewerk besteed zal moeten worden om tot een nauwkeurige versie 2.0 te komen.

Een bekend beeld kan het belang van semantisch modelleren verduidelijken. In figuur 1 is de zogenaamde ‘semiotische driehoek’ afgebeeld. Daarin betekenen de hoekpunten:
  -	dingen in de – fysieke of mentale – werkelijkheid, bijvoorbeeld een lantaarnpaal;
  -	begrippen van dingen in de werkelijkheid in ons hoofd, ontstaan door verwerking van observaties door de hersenen;
  -	vastlegging van begrippen in symbolen en termen, taalelementen, deze termen moeten de dingen in de werkelijkheid representeren.

De uitdaging van de informatiemodelleur is te komen tot een zo nauwkeurig mogelijke terminologie: het zo klein mogelijk maken van het verschil tussen begrippen en termen. Dit zal nooit voor 100% lukken: er is altijd een afweging tussen precisie en deugdelijkheid. Misschien ben je tevredener met een vaag beeld dat op een lantaarnpaal lijkt dan met een precies beeld dat helaas geen lantaarnpaal, maar een kapstok is!

### MIM

Het Metamodel voor Informatie Modellering ([MIM](https://docs.geostandaarden.nl/mim/mim/)) beschrijft de grondslagen voor informatiemodellering zodanig dat afstemming tussen en uitwisseling van informatiemodellen mogelijk wordt. MIM hanteert vier beschouwingsniveaus:
1.	Model van Begrippen (of ‘Begrippenkader’)

    Een model van begrippen wordt opgesteld voor gebruik door mensen, het bevat een lijst termen met definities van die termen en de relaties tussen de termen in natuurlijke taal. Doel is dat mensen binnen een domein elkaar beter begrijpen.
2.	Conceptueel informatiemodel

    Het conceptuele informatiemodel specificeert – nog steeds in natuurlijke taal - precies de betekenis van data en hun onderlinge betekenisrelaties, onafhankelijk van het ontwerp van en de implementatie in systemen. Dit informatiemodel dient als taal waarmee domeinexperts kunnen communiceren met informatieanalisten en verschaft een eenduidige interpretatie van die werkelijkheid ten behoeve van deze communicatie. Met conceptueel wordt niet bedoeld abstract of hoog over, de beschrijvingen van de informatie die beschikbaar is zijn heel precies en concreet.
3.	Logisch gegevensmodel

    Het logisch gegevensmodel is een model van de representatie van informatie over de werkelijkheid in digitale registraties en in de uitwisseling daartussen. Het slaat de brug tussen werkelijkheid en systemen maar beschrijft nog niet de implementatie in die systemen. Een dergelijk model wordt in een formele taal beschreven en wordt waar mogelijk gegenereerd vanuit het conceptueel model. Ook het logisch model is implementatieonafhankelijk en kan in meerdere technische modellen of formaten worden geïmplementeerd.
4.	Technisch gegevensmodel

    Het technisch gegevensmodel specificeert de structuur en eigenschappen van de technologie waarin de gegevens worden vastgelegd of uitgewisseld. Deze specificatie is sterk afhankelijk van de gebruikte opslagtechnologie zoals een specifieke database of de servicetechnologie zoals [xml], [gml], [SOAP], REST, [GeoJSON], [Linked-Data] e.d. De technische specificaties worden over het algemeen zoveel mogelijk gegenereerd uit het logisch informatiemodel. Deze specificaties worden opgesteld voor ‘machines’, te gebruiken door softwareontwikkelaars.

Het IMWO is primair een Conceptueel informatiemodel. Aan de specificatie van  objecttypen en relatiesoorten worden echter meer informele beschrijvingen toegevoegd, welke samen input voor een begrippenkader opleveren.

Het IMWO is nog geen volledig Conceptueel Informatiemodel: in deze fase is de beperking van de scope in de diepte gezocht teneinde een informatiemodel te verkrijgen dat het domein van de gebouwde woonomgeving zo breed mogelijk af te dekken. In concreto betekent dit dat het model zich beperkt tot specificatie van de objecttypen en de relaties ertussen en dat attributen van objecttypen en kardinaliteiten van relaties (betreft die relatie 0, 1 of veel objecttypen?) later nog uitgewerkt moeten worden.

### Federatief samenwerken - DSGO - DDD

Het Digitaal Stelsel Gebouwde Omgeving (DSGO) richt zich op partijen uit de gebouwde omgeving die in een digitale ketensamenwerking gegevens met elkaar uitwisselen Het DSGO is een federatief datastelsel: een stelsel van juridische, technische en semantische afspraken. gericht op het gemakkelijk, veilig en verantwoord kunnen delen en combineren van data tussen verschillende organisaties, zonder dat die data centraal hoeven te worden opgeslagen. De bronhouder blijft verantwoordelijk voor de beschikbaarheid en de kwaliteit van de data. Het is van belang dat deelnemers aan een federatief datastelsel weten wat voor data beschikbaar zijn en of deze data in hun behoefte voorzien. Er is met andere woorden een datacatalogus nodig. Aan deze catalogus ligt een specificatie van de data ten grondslag, ofwel de te zoeken data zijn beschreven in een informatiemodel. Dit model is opgebouwd rond een semantische kern, waarin de relevante gegevens gespecificeerd worden als termen met betekenis. Deze termen worden gerelateerd aan de gegevensspecificaties van de bronnen, waarbij rekening gehouden wordt met betekenisverschillen: waar nodig worden gegevensspecificaties vertaald, immers in het ene domein wordt een andere taal gesproken dan in het andere domein. Zo heeft men het in het domein van de overheidsbasisregistratie over ‘panden’, terwijl men elders over ‘gebouwen’ spreekt. Veel panden zijn gebouwen, maar niet allemaal. Komt nog bij dat er in subdomeinen weer verschillend gedacht wordt over wat een gebouw is. Dus: je kunt (of jouw systeem kan) een beeld in je eigen taal vormen van mogelijke combinaties van beschikbare gegevens in verschillende bronnen. Na juridische en technische afhandeling kun je ze naar je toe halen. Op analoge wijze kun je gegevens in andere bronnen ter mutatie aanbieden. Op deze wijze worden de kernfuncties van de semantische laag van het DSGO – toevoegen van betekenis, standaardisatie, federatieve ontsluiting en interoperabiliteit – ingevuld.

NB het semantisch datamodel plus de vertalingen wordt als service aangeboden; het is geen verplichting. Op veel datadiensten is het model niet van toepassing, immers DSGO kan voor álle soorten data gebruikt worden.

Door toepassing van het canonieke model is ook domain driven design mogelijk: per domein kunnen eigen terminologieën en gegevensmodellen aangehouden worden. Deze worden via de centrale voorziening met elkaar compatible gemaakt.

In figuur 2 wordt het voordeel van federatief samenwerken nog eens op een andere manier verduidelijkt: in een situatie zonder centrale vertaling moeten standaarden en andere schema's bilateraal aan elkaar gerelateerd worden. In een situatie mét centrale vertaling worden de gegevens per paar standaarden wel twee keer vertaald, maar over het geheel is het aantal vertalingen sterk gereduceerd (bij n schema's van orde n2 tot orde n)

### Mapping en matching

‘Mapping’ is letterlijk zoiets als het afbeelden van iets op iets anders (zoals het afbeelden van bebouwing op een landkaart). Als het gaat om informatiemodellen betreft dit het afbeelden van elementen van het ene model op het andere, ofwel het leggen van een – zo mogelijk – eenduidige relatie tussen objecttypen, attribuutsoorten en relaties in het ene model en het andere.

Een voorbeeld: in het ene model wordt een typologie van gebouwen opgezet door het objecttype Gebouw te voorzien van subtypen Woongebouw, Bijeenkomstgebouw, etc. In het andere model is er slechts één objecttype, Gebouw, dat een attribuutsoort gebouwType heeft, die verwijst naar een enumeratie van gebouwtypen als Woongebouw, Bijeenkomstgebouw, etc. De mapping van model 1 naar model 2 is dan dat ieder subtype van Gebouw uit model 1 verwijst naar een enumeratie-element in de enumeratie gebouwType van Gebouw uit model 2. In dit geval is de mapping symmetrisch, dus ook geldig in omgekeerde richting.

‘Matching’ gaat iets verder dan mapping, het voegt aan de mapping een oordeel toe, namelijk of het domein en het bereik van de afbeelding op elkaar ‘passen’. Zo kan het zijn dat er in één van beide typologieën bepaalde subtypes ontbreken. 
Voor de term ‘matching’ is ook de term ‘alignment’ (afstemming, harmonisatie) in zwang. De connotatie is wellicht iets anders: vaak wordt ‘wishful thinking’ toegepast door gelijkstelling van termen met ongeveer dezelfde betekenis. Dat is zeer gevaarlijk en de oorzaak van veel storingen in het huidige digitale tijdperk, waarin de toepassing van koppelingen op basis van ‘ongeveer’ leidt tot oncontroleerbare softwarekluwens. 

Een mapping is de basis voor een transformatie Als het gaat om informatiemodellen wordt een bredere interpretatie gehanteerd: het gaat om het transformeren van het ene model in het andere, zowel syntactisch als semantisch. Syntactische transformatie wordt ook wel conversie genoemd, semantische transformatie wordt ook wel translatie genoemd. Aan een transformatie kan een proces toegevoegd worden, dat de vertaling geautomatiseerd verzorgt.

Naast matching is er een andere vorm van interoperabiliteitsverhoging, de uitbreiding (‘extension’) van informatiemodellen (c.q. ontologieën). Daarbij wordt een element uit een model gerelateerd aan een element uit een ander model. Bijvoorbeeld kan het Objecttype Gebouw in een zekere gebouwregistratie, waarin per gebouw alle ruimten worden benoemd met hun functie, uitgebreid worden met de oppervlakte per ruimte. Het moge duidelijk zijn dat er vóór deze afstemming een mapping en een matching dienen plaats te vinden.

Voorbeeld van een mapping

| Kenmerk          | Model 1           | Mapping                         | IMWO              | Mapping                | Model 2 |
| ---------------- | ----------------- | ------------------------------- | ----------------- | ---------------------- | ------- |
| taal             | Space             | Space ↔ Ruimte                  | Ruimte            | Ruimte ↔ Ruimte        | Ruimte  |
| dimensionaliteit | 2D of 3D          | 2D → 3D (z=0), 3D ↔ 3D          | 3D                | 3D ↔ 3D                | 3D      |
| afbakening       | reëel of virtueel | reëel/virtueel ↔ reëel/virtueel | reëel of virtueel | reëel/virtueel ← reëel | reëel   |

De verzameling triples, die gezamenlijk een mapping (in de tabel de elementen van de kolom ‘mapping’) tussen twee modellen representeren wordt ‘linkset’ genoemd.

In het voorbeeld is te zien dat er informatie verloren kan gaan: in model 2 worden alleen reëel afgebakende ruimten geregistreerd. In IMWO en via IMWO in model 1 is iedere reëel afgebakende ruimte ‘reëel of virtueel’ afgebakend, dus je weet niet meer hoe een ruimte is afgebakend, terwijl bekend was dat de afbakening reëel was. Dit is op twee manieren op te lossen:
1.	IMWO zodanig uitbreiden dat duidelijk is wanneer een ruimte reëel, virtueel of ‘virtueel of reëel’(‘onbekend’) is afgebakend
2.	een domeinregistratie die daar behoefte aan heeft uitbreiden met een kenmerk ‘reëel’ voor de ruimten die vanuit model 2 komen.

Los hiervan bevat model 2 überhaupt geen virtueel afgebakende ruimten, dus die kunnen in ieder geval niet gedeeld worden. Wellicht is het handig aan ruimten die uit model 2 komen het metagegeven ‘reëel’ mee te geven.

Op het niveau van het begrippenkader mogen de relaties zwak zijn, op het niveau van het conceptuele en zeker het logische model dienen ze sterk te zijn. Pragmatiek is op dat niveau uit den boze.

Om betrouwbare koppelingen te realiseren dienen er in ieder geval adequate metadata te worden toegevoegd.

Bij de uitwerking kan voortgebouwd worden op voorwerk van [CROW](https://docs.crow.nl/ontology-alignment/whitepaper/). Verder zouden AI tools ingezet kunnen worden om mappings te analyseren en transformaties te definiëren. Hiertoe is nader onderzoek en experiment nodig.

### Canoniek informatiemodel

Een canoniek informatiemodel fungeert als een centraal model, waarnaar gegevens uit verschillende domeinen vertaald worden en vice versa. Hierdoor kan er communicatie tussen alle domeinen plaatsvinden zonder koppeling van elk domein aan elk ander domein. Belangrijkste kenmerken en doelen:

- Standaardisatie: Het definieert een vaste structuur, formaat en betekenis (semantiek) van objecttypen en hun relaties, onafhankelijk van een specifieke applicatie.
- Vermindering van complexiteit: In plaats van 'point-to-point'-integraties (waarbij elk systeem met elk ander systeem praat), vertaalt elk systeem zijn eigen data naar het centrale, canonieke formaat.
- Eén 'bron van waarheid': Het creëert een uniforme weergave over een compleet domein, hetgeen zorgt voor consistente communicatie.
- Herbruikbaarheid: de gespecificeerrde objecttypen zijn herbruikbaar en generiek. 

Voordelen

- Makkelijker schalen: Nieuwe systemen toevoegen is eenvoudiger, omdat ze alleen hoeven te koppelen aan het centrale model.
- Consistentie: Minder fouten door verschillende definities van dezelfde data.
- Onderhoudbaarheid: Wijzigingen in één systeem hebben minder impact op andere systemen. 
  
### Methode

De ontwikkeling van het IMWO vindt plaats in een iteratief proces van:
-	creatie: ontwikkeling van (deel-)modellen; daarbij kunnen uitwerkingen, bijvoorbeeld in de vorm van BIM-modellen beproefd worden;
-	verificatie: nagaan of uitwerkingen (bijvoorbeeld BIM-modellen) kunnen voldoen aan het informatiemodel;
-	validatie: nagaan of het model daadwerkelijk voldoet aan de behoeften van de gebruikers, enerzijds businessadviseurs, anderzijds IT-specialisten; dit kan leiden tot aanpassingen van het model en de werkwijze, maar vindt vooral aan het eind plaats in een marktbrede review.

### Opbouw van het informatiemodel

IMWO is opgebouwd deelmodellen op drie abstractieniveaus
1. Topmodel
2. Bouwwerken
3. Woonobjecten

De eerste twee niveaus betreffen de gebouwde omgeving als geheel en hebben ten doel de woonobjecten te zien als onderdeel van een groter geheel. Omgekeerd kunnen het Topmodel en het model Bouwwerken later in andere richtingen uitgebouwd worden, met name richting utiliteitsbouw, infrastructuur en  ruimten. Ook is er een uitbouw mogelijk richting aspectmodellen, denk aan modellen voor installaties, systems engineering en energie. 

In de diagrammen wordt de volgende legenda gehanteerd:

## Inventarisatie

### Overzicht ###

De volgende schema’s zijn betrokken in de inventarisatie:
|                                    |            |                               |                                   |
| :--------------------------------- | :--------- | :---------------------------- | :-------------------------------- |
| Aedes Informatiemodel Vastgoed 0.9 | GEBORA 1.0 | IMWOZ                         | NEN3610                           |
| Bbl                                | Geometrie  | IndoorGM                      | NEN-EN 15221-6                    |
| BIM Basis ILS                      | GeoSPARQL  | Inspire                       | NEN-EN-15804                      |
| BOT ontology                       | GGM        | ISO 19100-reeks               | NPR 4660                          |
| BRICK                              | IDS        | KIS Systematiek               | OmniClass                         |
| BIM Legal                          | IFC        | LADM                          | NLBE-SfB                          |
| CPR-2024                           | GIR        | LVG                           | OTL B&U                           |
| CIM                                | ILS O&E    | materiaalpaspoort             | Paspoorten: CB23, GABC NEN18216 … |
| CIMOW                              | ILS Spaces | meetinstructies voor taxaties | RVB IM                            |
| CityGML                            | ILS Woco   | MiniBIM                       | SAREF                             |
| COBIE                              | IMBAG      | MiniGIM                       | STABU                             |
| CORA                               | IMBOR      | FM-standaarden                | Uniclass                          |
| DBL                                | IMGEO      | NAA.KT                        | Unieke ObjectCodering             |
| DiCon                              | IMIBRO     | NEN2580                       | VERA                              |
| DICO                               | IMKAD      | NEN2660-1                     | VIVET                             |
| Dossier Bevoegd Gezag              | IMX-Geo    | NEN2660-2                     | VTH-flo                           |
| ETIM                               | IMVG       | NEN2699                       | Wkb-dossier                       |
|                                    |            | NEN2767                       | WWS                               |
|                                    |            |                               |                                   |

[***Bijlage 1***](#bijlage1) bevat per schema een korte beschrijving.

[***Bijlage 2***](#bijlage2) bevat (delen van) geïnventariseerde informatiemodellen als UML-bestand en bijbehorende definities.

### Landelijke Voorziening Gebouwgegevens (LVG) ###

In de inventarisatie is ook de Landelijke Voorziening Gebouwgegevens (LVG) opgenomen. Dit is een voorziening die nog in ontwikkeling is. De achtergrond is het streven van de ondertekenaars van het Bestuursakkoord Digitale Gebouwde Omgeving 2027 om de informatiepositie van gebouweigenaren te verbeteren door inzage in en eenvoudig delen van gebouwgegevens. De overheid wil een katalysator zijn om de beschikbaarheid van versnipperde data te verbeteren (denk aan BAG-data, energieprestatiedata, installatiedata, subsidies en energiegebruik).  Bij de realisatie van dit streven is het handhaven van privacy van de betrokken eigenaren en controle van de data-eigenaren over hun data uitgangspunt. Inzage in en delen van data is geen doel op zich, maar moet daadwerkelijk handelingsperspectief realiseren op het gebied van verduurzaming, (ver)bouwen en de funderingsproblematiek. Om daarin effectief te zijn moeten de gegevens op een veilige manier gedeeld kunnen worden met derden, zoals makelaars, energie-adviseurs en financiële instellingen. Applicatiebouwers moeten de gegevens kunnen ontsluiten voor toepassingen. 

LVG zal opereren volgens de principes van het Federatief Datastelsel van de overheid (FDS). LVG zal als betrouwbaar en schaalbaar knooppunt binnen het FDS functioneren. Verder zal aangesloten worden op GEBORA . Dit betekent dat de LVG-architectuur toekomstbestendig moet zijn en rekening moet houden met standaarden uit de bouwsector. 

Het FDS definieert de spelregels en afspraken over eigenaarschap, beheer en gebruik van data in federatieve samenwerkingen. Voor de LVG betekent dit dat bronhouders (Kadaster, RVO, gemeenten) onder een gezamenlijk governancekader opereren onder regie bijvoorbeeld BZK of Logius.

Via DSGO gaat LVG aansluiten op GIR. Hierdoor kunnen ook installateurs toegang krijgen tot de installatiedata. De regie blijft uiteraard bij de woningeigenaar. Regeling Gemeenschappelijke Bronontsluiting & Delen via Toestemming met Private Dienstverleners (GBO-DvTP)

Er is een onderzoek gedaan naar de informatiebehoefte in de eerste fase. Het gaat dan om de volgende gegevens:
- perceelsgegevens
- woninggegevens: 
- topografische gegevens
- nutsaansluitingen
- verkoopinformatie 
- WOZ waarde
- energielabel en onderliggende gegevens (EP-online)
- ISDE gegevens van de woning die bekend en beschikbaar zijn (RVO)
- installatiegegevens (GIR); 

### Stelselarchitectuur Gegevensvraag en -aanbod

LVG en IMWO zouden ingepast kunnen worden in de bij het Kadaster in ontwikkeling zijnde architectuur voor de koppeling van vraag naar en aanbod van gegevens. Zie onderstaande figuur. Ter toelichting: te onderscheiden zijn een **bronnenlaag**, de **integratielaag** van data uit Bronnen en Landelijke Voorzieningen bij het Kadaster en de verdere integratie met data uit bronnen van bronhouders buiten het Kadaster en uit de integratie van bronnen bij Kadaster, de **interpretatielaag** (in roze) met op de top de **UX** van een serie van handelingsperspectieven (Use cases). De samenhangende informatiemodellen worden gezien als een Planetenstelsel, waarvan IMWO één planeet is.

De invulling van de architectuur is nog volop in ontwikkeling. Onderstaande figuur geeft een beeld.

## Globaal model

Het informatiemodel wordt behandeld in [Model](#model). Voorafgaande daaraan wordt in dit hoofdstuk een globaal overzicht verschaft. Daarin wordt eerst een globaal overzicht gegevens van de belangrijkste objecttypen en hun relaties, gevolgd door een iets uitgebreider overzicht van de drie abstractieniveaus van IMWO: (1) Topmodel, (2) Model Bouwwerken en (3) Model Woonobjecten.

### Globaal globaal model

Het IMWO beschrijft de woningen en woongebouwen op drie abstractieniveaus:
1. Fysieke objecten

   Woningen en woongebouwen zijn fysieke objecten. Daarop kunnen een aantal algemene kenmerken en relaties gedefinieerd worden, die verder als patroon voor alle fysieke objecten toegepast kunnen worden. Zo heeft een fysiek object een geometrie, waarmee alle specifieke fysieke objecten, zoals woningen en woongebouwen, een geometrie hebben.
2. Bouwwerken

   Woongebouwen zijn gebouwen en ieder gebouw is een bouwwerk. Zoals ieder fysiek object heeft een bouwwerk een ruimtelijke component, het geheel van ruimten, die de functie van het bouwwerk mogelijk maken, en een reële component, het samenstel van bouwdelen, installaties en inventaris, dat ervoor zorgt, dat het bouwwerk op de plaats, waar het staat als constructief zelfstandig object blijft staan, zodat de functie ervan ondersteund blijft worden. Iedere bouwwerkcomponent kan onderverdeeld worden in bouwwerkcomponenten totdat een elementaire bouwwerkcomponent bereikt is.

3. Woonobjecten

   Woonobjecten zijn (BAG-)verblijfsobjecten met een woonfunctie. Het kunnen zelfstandige woningen zijn dan wel wooneenheden in een woongebouw.Een woonobject bestaat uit woonobjectruimten.
   

### Fysieke objecten

Alle fysieke objecten hebben een aantal kenmerken: ze hebben een functie, een geometrie en een toestand, en ze bevatten materie. In de gebouwde omgeving worden fysieke objecten altijd als een eenheid gezien van een ruimtelijk object en een reëel object. Als ruimtelijk object biedt het ruimte aan functies als verblijven en verplaatsen van mensen, goederen en voertuigen, als reëel object verzorgt het de begrenzing van ruimtelijke objecten met 'harde' materie. Als we deze twee typen fysieke objecten relateren aan het aardoppervlak spreken we van ruimtelijke resp. reële geo-objecten.

De fysieke objecten kunnen diverse onderlinge relaties hebben:
-	plan/realisatie
- deel/geheel ((de)compositie)
- raakvlak
- topologie (onderlinge nabijheid/ bereikbaarheid)
- functioneel/technisch (implementatie)

### Bouwwerken

Een bouwwerk is een gebouwd fysiek geo-object en bedoeld om ter plaatse te functioneren. Een bouwwerk ligt op een terrein. Omdat een bouwwerk een fysiek object is valt het ook uiteen in een ruimtelijke en een reële component. Deze componenten kunnen weer verder gedecomponeerd worden. Dit leidt tot ruimtelijke en reële subtypen. De reële componenten worden onderscheiden in bouwcomponenten (balken, vloeren, etc.), installatiecomponenten en (vaste) inventariscomponenten.

De bouwwerkcomponenten hebben onderlinge raakvlakken. Dit betreft uiteraard de begrenzing van ruimten door reële objecten zoals wanden en vloeren, maar ook kunnen ruimten onderling een ('virtueel') raakvlak hebben en hetzelfde geldt voor reële componenten (zoals een afdekking op een vloer). 

Een gebouw is een bouwwerk met enkele bijzondere kenmerken, en wel: het is overdekt en geheel of gedeeltelijk met wanden omsloten, betreedbaar en afsluitbaar, primair bedoeld voor het bieden van een afgeschermde omgeving voor het verblijf, gebruik, onderbrengen of beschermen van mensen, dieren of voorwerpen, of voor de productie van goederen.

### Woonobjecten

Een woongebouw is een gebouw, dat primair geschikt is voor woningen en/of wooneenheden. Het bevat woonobjecten, verblijfsobjecten met een woonfunctie. Er worden twee soorten woonobjecten onderscheiden: woningen (zelfstandige woonobjecten) en wooneenhedenobjecten (een zelfstandig geheel, bestaande uit onzelfstandige wooneenheden). 

Een woonobject is opgebouwd uit ruimtelijke componenten, te onderscheiden naar verblijfsruimten, verkeersruimten, technische ruimten en functieruimten (zoals bergruimten).

## Model {#model}

### Inleiding

***Toelichting***

In een tiental submodellen wordt hierna het informatiemodel weergegeven in een diagram en toegelicht. Per objecttype is er een specifcatie plus een beschrijving van de relaties ervan met andere objecttypen.

De objecttypespecificatie ziet er als volgt uit:

| Onderwerp | Specificatie |
| :----- | :----- |
| Schema | Aanduiding van de standaard of het model. In dit geval is dat altijd ‘IMWO’ |
| Model | Subschema van IMWO |
| Term | Naam van de term |
| Formele definitie | Exacte beschrijving van het begrip, waarbij alle termen, behalve de niet nader gedefinieerde, worden gespecificeerd in een formele relatie tot andere termen |
| Bron | Bron, waarop de formele definitie gebaseerd is |
| Eigenaar | Eigenaar van de formele definitie, in dit geval steeds digiGO |
| Synoniemen | Eventuele synoniemen |
| Begrip | Naam van het concept zoals dat in de praktijk gebruikt wordt |
| Begripsdefinitie | Informele definitie (door mensen redelijkerwijs te bevatten definitie) |
| Bronterm | Term, zoals in de bron gehanteerd |
| Brondefinitie | Definitie, zoals in de bron gebruikt |
| Bron | Bron waarop de brondfinitie gebaseerd is |
| Eigenaar | Veronderstelde eigenaar van de brondefinitie. |
| Bijzonderheden | Bijzonderheden, die bij de bron vermeld zijn|
| Voorbeelden | Voorbeelden bij de definitie van IMWO|
| Commentaar | Commentaar en vraagpunten vanuit IMWO |
| Identificatie | 'url'..... uuid |

De relaties worden als volgt gespecificeerd:

| Term | Relatiesoort | Relatienaam | Model | Objecttype| 
| :--- | :--- | :--- | :--- | :--- | 
| naam van het objecttype | generalisatie, aggregatie, etc. | nadere specificatie | indien van toepassing: ander submodel of ander schema | naam van het gerelateerd objecttype |
| | | | | |

NB Vaak komt het voor dat een objecttype in IMWO gezien zou kunnen worden als een subtype of equivalentietype van een objecttype in een standaard. Bijvoorbeeld zou een fysiek object in IMWO een subtype- of equivalentierelatie kunnen hebben met een fysiek object in NEN 2660. Dit is niet gebeurd, omdat eerst in aangetoond moet worden dat het inderdaad om precies dezelfde objecttypen gaat. Bovendien willen we de vrijheid hebben nuanceringen aan te brengen, gecombineerd met geschikte mappings.

### Topmodel

De top is hoofdzakelijk gebaseerd op de ‘regels voor informatiemodellering van de gebouwde omgeving’ \[NEN 2660-1\] en \[NEN 2660-2\], alsmede het basismodel geo-informatie \[NEN 3610\|. Er wordt een aantal abstracte begrippen gedefinieerd, die wel heel algemeen zijn, maar toch belangrijk, omdat ze als patroon toegepast worden bij concrete objecttypen. Zo kan een gebouw – bijvoorbeeld om vluchtroutes te bepalen – gepresenteerd én geregistreerd worden als een netwerk, een topologisch model.

In het topmodel staat staat het objecttype FysiekObject centraal. Een FysiekObject is een verbijzondering van het algemenere objecttype Entiteit, waarvan het belangrijk is dat die een aantal specifieke relaties kan hebben met andere Entiteit, met name de transitie van functionele naar technische entiteit.

In het kader van de gebouwde omgeving wordt (in NEN 2660) onderscheid gemaakt tussen functionele en technische entiteiten. Een functionele entiteit wordt beschreven in termen van haar werking, haar functies, het WAT. Deze wordt geïmplementeerd door één of meer technische entiteiten, die beschreven worden in termen van de interne structuur, het HOE. De tweeling functionele entiteit-technische entiteit lijkt erg op een tweeling uit de filosofie, waarin de essentie en de existentie van dingen tegenover elkaar gesteld worden.

Een ruimte heeft op grond van het bovenstaande een functionele en een technische component. Je kunt ook zeggen: je hebt functionele ruimten en technische ruimten, waarbij de functionele ruimten rollen spelen van de technische ruimten. Functionele ruimten vervullen functies. Een voorbeeld:

•	functionele ruimte wachtkamer k in gebouw g

•	voertUit: functie wachten (of wellicht beter:’wachten faciliteren’)

•	isRolVan: technische ruimte kamer k in gebouw g; isRolVan (of: isGespeeldDoor) is synomiem met isGeïmplementeerdDoor 

Er zijn verschillende typen functies, zoals:

•	gebruiksdoel

•	registratieve functie

•	juridische functie

•	geografische functie.

Het begrip functie kan dus breder opgevat worden dan alleen gebruiksdoel. Een functie van een kadastraal perceel zou bijvoorbeeld kunnen zijn: ‘zakelijke rechten faciliteren’. De functie van een WOZ-object: ‘belastingheffing faciliteren’.

Het is wenselijk voor IMWO en beter nog: voor de gebouwde omgeving, een meer uitgebreide functietaxonomie uit te werken. Hiernaast kunnen ook functiedecomposities voorkomen, immers er zijn ook samengestelde functies.

**Hamburgermodel**

Een technische entiteit is een ‘functievervuller’. Dit wordt toegepast in de GARM Hamburgermodel–methodiek (GARM: General AEC Reference Model; AEC: Architecture, Engineering, and Construction), ontwikkeld door Wim Gielingh. In die methodiek wordt een object (Product Definition Unit (PDU)) gedefinieerd door zowel functionele eisen als technische oplossingen. Zo’n object kan vergeleken worden met een hamburger, met een functionele top en een technische bodem. In het functionele object worden functionele, technische en operationele eisen gekoppeld die nodig zijn om te komen tot een keuze (bijvoorbeeld door afweging) voor een technische oplossing. Een technische oplossing heeft kenmerken die getoetst moeten worden aan de eisen van het functionele object. Een technische oplossing kan op haar beurt weer (met decompositie) worden opgedeeld in nieuwe functionele objecten.  Het hamburgermodel speelt een belangrijke rol in de systems engineeringmethodiek. [Leidraad SE 2013] 

In de gebouwde omgeving worden fysieke objecten altijd als een eenheid gezien van een ruimtelijk object en een reëel object. Als ruimtelijk object biedt het ruimte aan functies als verblijven en verplaatsen van mensen, goederen en voertuigen, als reëel object verzorgt het de begrenzing van ruimtelijke objecten met 'harde' materie.

Er wordt nadrukkelijk een onderscheid gemaakt tussen fysieke objecten sec en geo-objecten: een GeoObject wordt gezien als een FysiekObject met een vaste plaats ten opzichte van het aardoppervlak. Hiermee komen we in het domein van de geo-informatie, waarvoor in Nederland het basismodel voor geo-informatie (NEN 3610) de centrale standaard is. Hieraan is het IMWO-topmodel dan ook gekoppeld.  

### Bouwwerken

Een Bouwwerk wordt gedefinieerd als een door mensen vervaardigd ruimtelijk afgebakend fysiek samenhangend constructief zelfstandig object, verbonden met en steun vindend in de grond, samengesteld uit constructieve onderdelen, aangevuld met bouwkundige en/of installatietechnische onderdelen met een ter plaatse uit te oefenen functie. 

**Toelichting**

- ‘door mensen vervaardigd’, afgeleid uit diverse definities; dit kenmerk sluit natuurlijke objecten uit.

-	‘ruimtelijk afgebakend’: dit is wat in wetenschappelijke literatuur ‘discreet’ genoemd wordt

-	‘samenhangend’ (ook wel: ‘aaneengesloten’): de vorm bestaat uit één geheel. Je kunt elk punt in de figuur bereiken vanuit elk ander punt zonder de figuur te verlaten. [Wikipedia]

-	‘constructief zelfstandig’: het bouwwerk blijft binnen bepaalde normen onder alle omstandigheden in stand

-	Het in diverse Nederlandse definities voorkomende kenmerk ‘van enige omvang’ is weggelaten. Immers: wat is de minimale omvang? Een stenen in de grond verankerd bankje in een plantsoen kun je gevoeglijk een bouwwerk noemen.

-	‘verbonden met en steun vindend in de grond’: dit sluit verplaatsbare constructies uit; in Bbl en NEN 3610 staat "…direct of indirect met de bodem verbonden of daarin steun vindt". De ‘of’ is in een ‘en’ veranderd, immers een constructie die zonder steun met de grond is verbonden zou toch geen bouwwerk genoemd mogen worden. En de term ‘bodem’ is door ‘grond’ vervangen, omdat met ‘bodem’ veelal alleen de toplaag van de grond wordt bedoeld. Juist de ondergrond is natuurlijk van belang voor de fundering.

-	‘samengesteld uit bouwkundige en constructieve en installatietechnische onderdelen’: 

    •	Bouwkundige onderdelen zijn onderdelen die het bouwwerk vormgeven, indelen, beschermen of bruikbaar maken, maar niet primair bedoeld zijn om het bouwwerk te dragen of stabiliteit te geven, zoals binnenwanden die geen dragende functie hebben, kozijnen en binnen- of buitendeuren. De functie daarvan is gebruik, comfort, indeling, afwerking, uitstraling

    •	Constructieve onderdelen: dit zijn onderdelen die belastingen moeten opnemen en afvoeren naar de fundering of andere dragende elementen. Ze zorgen voor veiligheid, sterkte en stabiliteit. Voorbeelden zijn fundering en dragende wanden. Functie: het bouwwerk overeind houden en zorgen dat het veilig is.
    •	Installatietechnische onderdelen: dat zijn de met de bouwkundige en of constructieve onderdelen verbonden installaties.
-	‘met een ter plaatse uit te oefenen functie’: dit kenmerk komt in bijna alle geïnventariseerde definities voor (in het algemeen als ‘bedoeld om ter plaatse te functioneren’).

-	weggelaten: ’Of een ruimtelijk af te bakenen deel daarvan’; dit zou modellering van een deel van een groter bouwwerk (vleugel, segment, bouwdeel) als afzonderlijk bouwwerk mogelijk maken; een nieuwe term is dan toch te prefereren, bijvoorbeeld ‘deelbouwwerk’, en wel omdat de zelfstandigheid van het object een essentieel kenmerk van een bouwwerk is.

Belangrijke uitwerkingen in het submodel Bouwwerken zijn verder:

- bepaling van de geometrie en de bepaling van oppervlake en inhoud daarvan op basis van NEN 2580;
- de rubricering van de reële BouwwerkComponenten tot BouwwComponenten, InsgtallatieComponenten en InventarisComponenten
- de decompositie van het Bouwwerk in  Ruimtelijke Bouwwerk Componenten. De uitwerking daarvan gebeurt alleen voor woonobjecten (hierna). Bijzondere Ruimtelijke Componenten  zijn Verdiepingen en BrandCompartimenten.
- en uiteraard de specialisatie naar Gebouw.

Een Gebouw wordt gedefinieerd als een overdekt en geheel of gedeeltelijk met wanden omsloten, betreedbaar en afsluitbaar  Bouwwerk, primair bedoeld voor het bieden van een afgeschermde omgeving voor het verblijf, gebruik, onderbrengen of beschermen van mensen, dieren of voorwerpen, of voor de productie van goederen.

Toelichting:

-	Overdekt en omsloten: in lijn met Aedes IMV, NEN 3610 en BAG varianten.

-	Betreedbaar en afsluitbaar: overgenomen uit de BAG/Pand definitie (IMBAG).

-	Doelgericht gebruik: overeenstemming tussen alle bronnen (verblijf, opslag, productie, bescherming).

Voorbeelden zijn: woonhuis, appartementsgebouw, kantoorgebouw, school, ziekenhuis, winkelpand, fabriek, schuur, loods.

### Bouwcomponenten

De BouwComponenten worden in 14 klassen verdeeld. Daarbij wordt nauw aangesloten bij de ILS O&E en IFC.

### Woonobjecten

Een Woongebouw wordt gedefinieerd als Gebouw dat primair geschikt is voor woningen en/of wooneenheden. Een grondgebonden woning wordt veelal niet als een woongebouw gezien. Om die reden wordt een woonobject direct als onderdeel van een Bouwwerk gespecificeerd. 

Een WoonObject is een Verblijfsobject (á la BAG) met een woonfunctie. Er worden twee soorten woonobjecten onderscheiden: woningen (zelfstandige woonobjecten) en wooneenhedenobjecten (een zelfstandig geheel, bestaande uit onzelfstandige wooneenheden). De Woningen worden verder onderverdeeld in een aantal subtypen. Er bestaan diverse typologieën, waarvan het gewenst is deze nader te analyseren en vervolgens te trachten op een systematische wijze tot een eenduidige typologie te komen.

Voor de Wooneenheden is geen typologie opgesteld, maar ze zijn gerubriceerd naar doelgroep.

Een woonobject is opgebouwd uit WoonObjectRuimten, te onderscheiden naar BuitenRuimten en BinnerRuimten, die verder verdeeld worden in Verblijfsruimten, Bedruimten, Verkeersruimten, TechnischeRuimten, Functieruimten, SanitaireRuimten en LegeRuimten. Deze ruimtetypen kunnen worden tot Bbl-gebieden.

Een WoonObjectRuimte heeft een Functie (in de BAG een 'gebruiksdoel' en in het Bbl 'bouwkundige bestemming' genoemd). Deze kan afwijken van de feitelijke Functie (in de BAG: het 'geconstateerde gebruiksdoel'), vandaar dat er twee relaties tussen WoonObjectRuimte en Functie opgenomen zijn.

### Woonobjectruimten

De WoonObjectRuimten zijn verder geklassificeerd. Het gaat hier om een voorlopige oplossing, die aansluit bij ILS-Woco en MiniBIM, maar die nog niet geheel en al consistent is.

### Installaties

Het submodel voorInstallaties sluit aan bij het Gebouwinstallatieregister (GIR) en de daarin toegepaste standaarden. Verder is het objecttype Nutsaansluiting opgenomen om een relatie te leggen met de NutsSystemen. 

De Installaties zijn verder geklassificeerd volgens de NL-SfB-standaard.

### Slimme woningen en bouwwerken

Het submodel Slimme woning/slim bouwwerk sluit aan bij de Saref-standaard.

### Binnenruimtenetwerk

Het submodel Binnenruimtenetwerk sluit aan bij IndoorGML 2.0. Het gaat hier om een eerste schets, die nog getoets moet worden en waarbij de aansluiting bij IndoorGML nog gespeicificeerd moet worden.
Oorzaak: in eerste instantie was alleen IndoorGML 1.0 bekend, en dat wijkt af van IndoorGML 2.0.

### Juridische objecten

In het submodel Juridische objecten wordt vooral verwezen naar objecttypen in de relevante standaarden. Dit submodel is van belang voor de ontwikkeling van het LVG, dat gebaseerd zal worden op een view op het IMWO.

## Inhoud van model: objecttypen en relaties

### Top

#### AbstractConcept

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | AbstractConcept |
| Formele definitie | wiskundig Concept. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | abstract concept |
| Begripsdefinitie | wiskundig concept. |
| Bronterm | Abstract Concept |
| Brondefinitie | Concept dat een structuur en een afbakening vormt in een abstracte ruimte. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Identificatie | 98f70228-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| AbstractConcept | heeft relatie met | heeftRelatieMet | NEN2660 | Abstract concept |
| AbstractConcept | is specialisatie van | heeftTopTerm | TopModel | Concept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| AbstractConcept | is generalisatie van |  | TopModel | AbstracteRuimte |
| AbstractConcept | is generalisatie van |  | TopModel | Tijd |

#### AbstracteRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | AbstracteRuimte |
| Formele definitie | verzameling met een structuur |
| Bron | Wikipedia |
| Eigenaar | digiGO |
| Begrip | abstracte ruimte |
| Begripsdefinitie | Verzameling met een structuur |
| Bronterm | Geometrische entiteit |
| Brondefinitie | benoemd concept dat een daadwerkelijke of virtuele afbakening vormt in een concrete (fysieke, driedimensionale) ruimte die we in de werkelijkheid ervaren. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | We beperken ons tot de klassieke geometrie. |
| Voorbeelden | euclidische ruimte |
| Identificatie | 98f704d2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| AbstracteRuimte | heeft relatie met | heeftRelatieMet | NEN2660 | Geometrische entiteit |
| AbstracteRuimte | is specialisatie van |  | TopModel | AbstractConcept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| AbstracteRuimte | is generalisatie van |  | TopModel | GeometrischeRuimte |
| AbstracteRuimte | is generalisatie van |  | TopModel | TopologischeRuimte |

#### Activiteit

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Activiteit |
| Formele definitie | Entiteit bij een Object met een ruimtelijke en een tijdsdimensie die objecten transformeert |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | activiteit |
| Bronterm | Activiteit |
| Brondefinitie | Entiteit die plaatsvindt of kan plaatsvinden in een concrete ruimte-tijd. Een activiteit transformeert objecten en wordt uitgevoerd door een object. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Volgens de systeemkunde omvat een proces een serie transformaties tijdens de doorvoer van  een of meer fysieke objecten en/of informatieobjecten. Een proces kan binnen deze context worden beschouwd  als een set van samenhangende activiteiten om input (bijvoorbeeld planningen, specificaties, adviezen) om te  zetten in output (bijvoorbeeld inspecties, onderzoeksrapporten, handhavingsmaatregelen). |
| Voorbeelden | voetbalwedstrijd Ajax-Feyenoord |
| Identificatie | 98f718f5-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Activiteit | heeft relatie met | heeftRelatieMet | NEN2660 | Activiteit |
| Activiteit | heeft relatie met | transformeert | TopModel | Object |
| Activiteit | is specialisatie van |  | TopModel | Entiteit |
| Activiteit | is specialisatie van |  | NEN2660 | Entiteit |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Activiteit | is generalisatie van |  | TopModel | Functie |
| Activiteit | is gerelateerd aan | heeftRelatieMet | SlimmeWoning | Activering |
| Activiteit | is gerelateerd aan | heeftRelatieMet | TopModel | Activiteit |
| Activiteit | is gerelateerd aan | voertUit | TopModel | Object |
| Activiteit | is gerelateerd aan | heeftRelatieMet | SlimmeWoning | Observatie |

#### Concept

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Concept |
| Formele definitie | enkelplaatsig enkelvoudig ding |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | digiGO |
| Begrip | concept |
| Begripsdefinitie | ondeelbaar op zichzelf staand ding |
| Bronterm | TopConcept |
| Brondefinitie | Enkelplaatsig (unair) element dat existentieel onafhankelijk is. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Enkelplaatsig: cardinaliteit=1: i.t.t. een 'relatie': die is meerplaatsig; enkelvoudig: atomair: kan (op een bepaald niveau) niet verder onderverdeeld worden. |
| Commentaar | In NEN 2660:1 wordt dit 'Topconcept'genoemd, maar dat begrip wordt niet nader gedefinieerd.In NEN 2660-1 is een Concept verder een specialisatie van een element, 'een enkelvoudig ding dat lid kan zijn van een verzameling', met als extra eigenschap dat het 'existentieel onafhankelijk'is. Maar wat is 'existentieel onafhankelijk'? |
| Identificatie | 98f6d569-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Concept | heeft relatie met | heeftRelatieMet | NEN2660 | Concept |
| Concept | is specialisatie van |  | NEN2660 | Element |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Concept | is generalisatie van |  | NEN2660 | Abstract concept |
| Concept | is generalisatie van | heeftTopTerm | TopModel | AbstractConcept |
| Concept | is generalisatie van |  | NEN2660 | Concreet concept |
| Concept | is generalisatie van | heeftTopTerm | TopModel | ConcreetConcept |
| Concept | is gerelateerd aan | heeftRelatieMet | TopModel | Concept |

#### ConcreetConcept

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | ConcreetConcept |
| Formele definitie | in ruimte en tijd afgebakend Concept. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | digiGO |
| Begrip | concreet concept |
| Begripsdefinitie | in ruimte en tijd afgebakend concept. |
| Bronterm | Concreet Concept |
| Brondefinitie | Concept dat een manifestatie en een afbakening vormt in een concrete ruimte-tijd. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Voorbeelden | Fysieke objecten, zoals atomen, cellen, organismen, mensen en organisaties, bouwwerken, waterlichamen en planeten, maar ook conceptuele en symbolische concepten die zijn gegrond in de fysieke werkelijkheid. |
| Identificatie | 98f7085d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ConcreetConcept | heeft relatie met | heeftRelatieMet | NEN2660 | Concreet concept |
| ConcreetConcept | is specialisatie van | heeftTopTerm | TopModel | Concept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ConcreetConcept | is generalisatie van |  | TopModel | Entiteit |
| ConcreetConcept | is generalisatie van |  | TopModel | Gebeurtenis |
| ConcreetConcept | is generalisatie van |  | TopModel | Toestand |

#### Entiteit

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Entiteit |
| Formele definitie | ConcreetConcept dat op elk moment in de tijd een bepaalde toestand heeft. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | digiGO |
| Begrip | entiteit |
| Begripsdefinitie | concept dat op elk moment in de tijd een bepaalde toestand heeft. |
| Bronterm | Entiteit |
| Brondefinitie | Concreet Concept dat een manifestatie en een afbakening vormt in een concrete ruimte-tijd, en dat op elk moment in de tijd een bepaalde toestand heeft. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Een entiteit heeft een levenscyclus, want er is een tijdsdimensie.  Een entiteit heeft een unieke identiteit die constant blijft gedurende de levenscyclus. De levenscyclus van een entiteit is opgebouwd uit de reeks van toestanden van de desbetreffende entiteit, die elkaar in de tijd opvolgen  Inerne definitie is opgeschoonde externe definitie. |
| Voorbeelden | brug, voetbalwedstrijd |
| Identificatie | 98f70945-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Entiteit | heeft relatie met | isImplementatieVan | TopModel | Entiteit |
| Entiteit | heeft relatie met | isDeelVan | TopModel | Entiteit |
| Entiteit | heeft relatie met | heeftRelatieMet | NEN2660 | Entiteit |
| Entiteit | is specialisatie van |  | NEN2660 | Concreet concept |
| Entiteit | is specialisatie van |  | TopModel | ConcreetConcept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Entiteit | is generalisatie van |  | TopModel | Activiteit |
| Entiteit | is generalisatie van |  | NEN2660 | Activiteit |
| Entiteit | is generalisatie van |  | Ketenstandaard-Ruimte | Functionele entiteit |
| Entiteit | is generalisatie van |  | NEN2660 | Functionele entiteit |
| Entiteit | is generalisatie van |  | NEN2660 | Geplande entiteit |
| Entiteit | is generalisatie van |  | NEN2660 | Gerealiseerde entiteit |
| Entiteit | is generalisatie van |  | TopModel | Object |
| Entiteit | is generalisatie van |  | NEN2660 | Object |
| Entiteit | is generalisatie van |  | Ketenstandaard-Ruimte | Technische entiteit |
| Entiteit | is generalisatie van |  | NEN2660 | Technische entiteit |
| Entiteit | is gerelateerd aan | isImplementatieVan | TopModel | Entiteit |
| Entiteit | is gerelateerd aan | isDeelVan | TopModel | Entiteit |
| Entiteit | is gerelateerd aan | heeftRelatieMet | TopModel | Entiteit |
| Entiteit | is gerelateerd aan | isRealisatieVan | TopModel | Object |
| Entiteit | is gerelateerd aan | heeft | TopModel | Toestand |

#### Functie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Functie |
| Formele definitie | Activiteit met een doelgerichte output en een specifieke input. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | functie |
| Bronterm | Functie |
| Brondefinitie | De functie van een object is de activiteit die het uitvoert of kan uitvoeren, zodanig dat de output van die activiteit bijdraagt aan het doel dat de betrokken stakeholder wil bereiken. Het betreft de bijdrage die van de medewerkers of het voorwerp wordt verwacht voor het behalen van de ondernemingsresultaten, respectievelijk de systeemprestatie waar het voorwerp onderdeel van uitmaakt. Ook een functie (zeker mathematische) kent een input en een output, analoog aan activiteiten. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Het begrip Functie is niet in de taxonomie van NEN 2660 opgenomen, maar wordt alleen in de tekst genoemd als toelichting op het begrip Activiteit. |
| Identificatie | 98f71ad5-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Functie | is specialisatie van |  | TopModel | Activiteit |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Functie | is generalisatie van |  | MiniBIM | Bouwkundige of constructieve functie |
| Functie | is generalisatie van |  | Woonobjecten | WoonObjectRuimteFunctie |
| Functie | is gerelateerd aan | wordtBepaaldDoor | MiniBIM | Terrein |

#### FunctioneleRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | FunctioneleRuimte |
| Formele definitie | RuimtelijkGeoObject met een specifieke Functie |
| Bron | [NEN3610:2022] |
| Eigenaar | digiGO |
| Begrip | functionele ruimte |
| Begripsdefinitie | ruimtelijk geo-object met een specifieke functie |
| Bronterm | Functionele Ruimte |
| Brondefinitie | Ruimte met een specifieke functie |
| Bron | [NEN3610:2022] |
| Eigenaar | NEN |
| Identificatie | 98f7141e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FunctioneleRuimte | heeft relatie met | heeftRelatieMet | NEN3610 | Functionele ruimte |
| FunctioneleRuimte | is specialisatie van |  | NEN3610 | Functionele ruimte |
| FunctioneleRuimte | is specialisatie van |  | IMIBRO | Object |
| FunctioneleRuimte | is specialisatie van |  | TopModel | RuimtelijkGeoObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FunctioneleRuimte | is generalisatie van |  | IMIBRO | Functiezone |
| FunctioneleRuimte | is generalisatie van |  | IMIBRO | Gebruikzone |
| FunctioneleRuimte | is generalisatie van |  | Bouwwerken | Terrein |
| FunctioneleRuimte | is generalisatie van |  | IMIBRO | Toegangspunt |
| FunctioneleRuimte | is generalisatie van |  | Woonobjecten | WoonObject |

#### FysiekeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | FysiekeRuimte |
| Formele definitie | FysiekObject, bestaande uit voor bepaalde functies niet-belemmerende materie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | RuimtelijkObject; RuimtelijkGebied |
| Begrip | fysieke ruimte |
| Begripsdefinitie | fysiekObject, datruimte biedt aan bepaalde functies |
| Bronterm | RuimtelijkGebied |
| Brondefinitie | fysiek object dat een bepaald gebied omsluit, zoals een vertrek, rijbaan en rivier, dat wordt begrensd door reële objecten of andere ruimtelijke gebieden (bijvoorbeeld op basis van gebruik of conventie) en dat een voornamelijk vloeibare of gasvormige hoeveelheid materie bevat |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Voorbeelden | Gezonde lucht voor de functie 'menselijk verblijf'. Koper voor een elektriciteitsleiding |
| Commentaar | FysiekeRuimte' sluit als term het beste aan bij het beeld van de meeste mensen |
| Identificatie | 98f70da0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FysiekeRuimte | heeft relatie met | heeftRelatieMet | NEN2660 | Ruimtelijk gebied |
| FysiekeRuimte | is specialisatie van |  | TopModel | FysiekObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FysiekeRuimte | is generalisatie van |  | TopModel | RuimtelijkGeoObject |

#### FysiekObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | FysiekObject |
| Formele definitie | Object dat bestaat of kan bestaan binnen de fysieke 4D ruimte-tijd. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | digiGO |
| Begrip | fysiek object |
| Begripsdefinitie | object dat bestaat of kan bestaan binnen de fysieke 4D ruimte-tijd. |
| Bronterm | Fysiek Object |
| Brondefinitie | Object dat bestaat of kan bestaan binnen de fysieke 4D ruimte-tijd. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Een fysiek object vormt een manifestatie en een afbakening van materie en/of energie, en is (in)direct waarneembaar door de zintuigen.  Zie belangrijke opmerkingen in NEN 2660-1:220, par.9.5.2. |
| Voorbeelden | Een viaduct, een lichtmast, een pomp, een auto, een muur, een vertrek als fysische ruimte, een document als fysieke drager van een informatieobject |
| Identificatie | 98f70b0a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FysiekObject | heeft relatie met | heeftRelatieMet | NEN2660 | Fysiek object |
| FysiekObject | heeft relatie met | heeftTopologischeRelatieMet | TopModel | FysiekObject |
| FysiekObject | is specialisatie van |  | TopModel | Object |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FysiekObject | is generalisatie van |  | Bouwwerken | BouwwerkComponent |
| FysiekObject | is generalisatie van |  | TopModel | FysiekeRuimte |
| FysiekObject | is generalisatie van |  | TopModel | ReeelObject |
| FysiekObject | is gerelateerd aan | heeftTopologischeRelatieMet | TopModel | FysiekObject |

#### Gebeurtenis

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Gebeurtenis |
| Formele definitie | ConcreetConcept én overgang tussen twee Toestanden |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | gebeurtenis |
| Bronterm | Gebeurtenis |
| Brondefinitie | Concreet Concept dat een overgang tussen twee opeenvolgende toestanden van een entiteit (object of activiteit) vormt. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Identificatie | 98f71cd2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Gebeurtenis | heeft relatie met | heeftRelatieMet | NEN2660 | Gebeurtenis |
| Gebeurtenis | heeft relatie met | begint | TopModel | Toestand |
| Gebeurtenis | heeft relatie met | beEindigt | TopModel | Toestand |
| Gebeurtenis | is specialisatie van |  | NEN2660 | Concreet concept |
| Gebeurtenis | is specialisatie van |  | TopModel | ConcreetConcept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Gebeurtenis | is gerelateerd aan | heeftRelatieMet | TopModel | Gebeurtenis |

#### GeografischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | GeografischeRuimte |
| Formele definitie | Historisch of fysisch-geografisch samenhangend RuimtelijkGeoObject |
| Bron | [NEN3610:2022] |
| Eigenaar | digiGO |
| Begrip | geografische ruimte |
| Begripsdefinitie | historisch of fysisch-geografisch samenhangend ruimtelijk geoObject |
| Bronterm | Geografische Ruimte |
| Brondefinitie | Ruimte die bekendstaat onder een vanuit de historie of het gebruik bekende benaming of een fysisch-geografische samenhang, al dan niet met zijn omgeving, kent. |
| Bron | [NEN3610:2022] |
| Eigenaar | NEN |
| Voorbeelden | Noordoostpolder, Midden- Nederland, rivierengebied, Veluwe, Zuid-Limburg, kustgebied. |
| Identificatie | 98f71752-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GeografischeRuimte | heeft relatie met | heeftRelatieMet | NEN3610 | Geografische ruimte |
| GeografischeRuimte | is specialisatie van |  | TopModel | RuimtelijkGeoObject |

#### GeometrischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | GeometrischeRuimte |
| Formele definitie | AbstracteRuimte met afstandsrelaties tussen de elementen |
| Bron | Wikipedia, IMWO |
| Eigenaar | digiGO |
| Synoniemen | MetrischeRuimte, Geometrie |
| Begrip | geometrische ruimte |
| Begripsdefinitie | ruimte met afstandsrelaties tussen de elementen |
| Bronterm | Geometrische Ruimte |
| Brondefinitie | - |
| Voorbeelden | kubus |
| Identificatie | 98f706b5-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GeometrischeRuimte | is specialisatie van |  | TopModel | AbstracteRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | 0DRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | 1DRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | 2DRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | 3DRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | BrutoGeometrischeRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | NettoGeometrischeRuimte |
| GeometrischeRuimte | is generalisatie van |  | Bouwwerken | TarraGeometrischeRuimte |
| GeometrischeRuimte | is gerelateerd aan | bepaalt | Bouwwerken | BepalingsMethode |
| GeometrischeRuimte | is gerelateerd aan | heeft | Bouwwerken | BouwwerkComponent |

#### GeoObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | GeoObject |
| Formele definitie | FysiekObject met een vaste plaats ten opzichte van het aardoppervlak. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | geo-object |
| Begripsdefinitie | fysiek object met een vaste plaats ten opzichte van het aardoppervlak. |
| Bronterm | Geo-Object |
| Brondefinitie | Fenomeen in de werkelijkheid dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van de aarde |
| Eigenaar | NEN |
| Bijzonderheden | Van dit objecttype worden geen directe instanties gemaakt. Indien een object een geo-object is, is het altijd een instantie van een subklasse van GeoObject. |
| Identificatie | 98f71d9f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GeoObject | heeft relatie met | heeftRelatieMet | NEN3610 | Geo-object |
| GeoObject | heeft relatie met | heeftLocatie | LVG | Locatie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GeoObject | is generalisatie van |  | Bouwwerken | Bouwwerk |
| GeoObject | is generalisatie van |  | IMBAG | Pand |
| GeoObject | is generalisatie van |  | TopModel | ReeelGeoObject |
| GeoObject | is generalisatie van |  | TopModel | RuimtelijkGeoObject |
| GeoObject | is gerelateerd aan | heeftLocatie | Installaties | Installatie |
| GeoObject | is gerelateerd aan | heeftLocatie | LVG | KadastraalObject |
| GeoObject | is gerelateerd aan |  | IMKAD | PubliekRechtelijkeBeperking |
| GeoObject | is gerelateerd aan |  | IMKAD | PubliekRechtelijkeBeperking |

#### JuridischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | JuridischeRuimte |
| Formele definitie | RuimtelijkGeoObject waarop een juridisch instrument beleid of regelgeving toepast. |
| Bron | [NEN3610:2022] |
| Eigenaar | digiGO |
| Begrip | juridische ruimte |
| Begripsdefinitie | ruimtelijk geoObject waarop een juridisch instrument beleid of regelgeving toepast. |
| Bronterm | Juridische Ruimte |
| Brondefinitie | Ruimte waar een juridisch instrument beleid of regelgeving toepast. |
| Bron | [NEN3610:2022] |
| Eigenaar | NEN |
| Voorbeelden | benoeming van ruimten en gebieden in bijvoorbeeld omgevingsvisie, omgevingsverordening, waterschapsverordening, projectbesluit. |
| Identificatie | 98f71827-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| JuridischeRuimte | heeft relatie met | heeftRelatieMet | NEN3610 | Juridische ruimte |
| JuridischeRuimte | is specialisatie van |  | TopModel | RuimtelijkGeoObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| JuridischeRuimte | is generalisatie van |  | IMKAD | Perceel |
| JuridischeRuimte | is generalisatie van |  | VTH-FLo | VTH-OBJECT |
| JuridischeRuimte | is generalisatie van |  | IMKAD | Werkingsgebied |

#### Object

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Object |
| Formele definitie | Entiteit die bestaat of kan bestaan binnen een concrete ruimte-tijd. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | digiGO |
| Begrip | object |
| Begripsdefinitie | entiteit die bestaat of kan bestaan binnen een concrete ruimte-tijd. |
| Bronterm | Object |
| Brondefinitie | Entiteit die bestaat of kan bestaan binnen een concrete ruimte-tijd. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Een object voert activiteiten uit en wordt getransformeerd door een activiteit. |
| Voorbeelden | Het Bouwhuis (hoofdkantoor van Bouwend Nederland) |
| Identificatie | 98f70a2d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Object | heeft relatie met | voertUit | TopModel | Activiteit |
| Object | heeft relatie met | isRealisatieVan | TopModel | Entiteit |
| Object | heeft relatie met | heeft | INSPIRE | Netwerkverwijzing |
| Object | heeft relatie met | heeftRelatieMet | NEN2660 | Object |
| Object | is specialisatie van |  | TopModel | Entiteit |
| Object | is specialisatie van |  | NEN2660 | Entiteit |
| Object | is specialisatie van |  | NEN3610 | Geo-object |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Object | is generalisatie van |  | IMIBRO | FunctioneleRuimte |
| Object | is generalisatie van |  | NEN2660 | Fysiek object |
| Object | is generalisatie van |  | TopModel | FysiekObject |
| Object | is generalisatie van |  | NEN2660 | Informatieobject |
| Object | is generalisatie van |  | IMIBRO | ReeelObject |
| Object | is generalisatie van |  | IMIBRO | RegistratieveRuimte |
| Object | is gerelateerd aan | transformeert | TopModel | Activiteit |
| Object | is gerelateerd aan | heeftRelatieMet | TopModel | Object |

#### ReeelGeoObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | ReeelGeoObject |
| Formele definitie | FysiekObject dat zowel ReeelObject als GeoObject is |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | reëel geo-object |
| Begripsdefinitie | reëel object met een vaste plaats ten opzichte van het aardoppervlak |
| Bronterm | Reëel object |
| Brondefinitie | Geo-object dat zich geheel materieel manifesteert. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Bijzonderheden | Een reëel of fysiek object is een tastbaar begrensd object dat gekenmerkt wordt door zijn materiele samenstelling en structuur.' |
| Commentaar | In NEN 3610 staat dat het NEN 3610 reëel object overeenkomt met het NEN 2660 technisch reëel object. Dan wordt dus verondersteld dat een NEN 2660 een vaste plaats t.o.v. het aardoppervlak hebben; dat is maar de vraag. Verder blijkt uit de zin 'Een reëel of fysiek object is een tastbaar begrensd object dat gekenmerkt wordt door zijn materiele samenstelling en structuur.' dat reëel en fysiek als synoniemen gebruikt mogen worden. Dat isnin strijd met NEN 2660. |
| Identificatie | 98f70cbc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ReeelGeoObject | heeft relatie met | heeftRelatieMet | NEN3610 | Reeel object |
| ReeelGeoObject | is specialisatie van |  | TopModel | GeoObject |
| ReeelGeoObject | is specialisatie van |  | TopModel | ReeelObject |

#### ReeelObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | ReeelObject |
| Formele definitie | FysiekObject, bestaande uit ondoordringbare materie |
| Bron | [NEN 2660-2:2022] |
| Eigenaar | digiGO |
| Begrip | reëel object |
| Begripsdefinitie | vormvast of niet-vormvast fysiek object, bestaande uit materie |
| Bronterm | Reëel Object |
| Brondefinitie | Hoeveelheid materie. Fysiek object (vormvast of niet-vormvast) dat in de werkelijkheid tastbaar en zichtbaar is (of kan zijn), door de mens gemaakt of natuurlijk ontstaan. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Voorbeelden | Betonnen dragende wand in een woning. Isolatiemateriaal voor een elektriciteitsleiding |
| Identificatie | 98f70be8-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ReeelObject | heeft relatie met | heeftRelatieMet | NEN2660 | Reëel object |
| ReeelObject | is specialisatie van |  | TopModel | FysiekObject |
| ReeelObject | is specialisatie van |  | IMIBRO | Object |
| ReeelObject | is specialisatie van |  | NEN3610 | Reeel object |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ReeelObject | is generalisatie van |  | IMIBRO | Bouwlaag |
| ReeelObject | is generalisatie van |  | IMIBRO | Constructie |
| ReeelObject | is generalisatie van |  | TopModel | ReeelGeoObject |

#### RegistratieveRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | RegistratieveRuimte |
| Formele definitie | Op basis van wet- of regelgeving afgebakend RuimtelijkGeoObject dat als eenheid geldt van politiek- bestuurlijke verantwoordelijkheid of voor bedrijfsvoering. |
| Bron | [NEN3610:2022] |
| Eigenaar | digiGO |
| Begrip | registratieve ruimte |
| Begripsdefinitie | op basis van wet- of regelgeving afgebakend RuimtelijkGeoObject dat als eenheid geldt van politiek- bestuurlijke verantwoordelijkheid of voor bedrijfsvoering. |
| Bronterm | Registratieve Ruimte |
| Brondefinitie | Op basis van wet- of regelgeving afgebakende ruimte die als eenheid geldt van politiek- bestuurlijke verantwoordelijkheid of voor bedrijfsvoering. |
| Bron | [NEN3610:2022] |
| Eigenaar | NEN |
| Voorbeelden | gemeente Delft, postcodegebied 2345, politieregio Haaglanden, veiligheidsregio Gelderland-Midden, Nationaal Park De Hoge Veluwe, kadastraal perceel. |
| Identificatie | 98f71533-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RegistratieveRuimte | heeft relatie met | heeftRelatieMet | NEN3610 | Registratieve ruimte |
| RegistratieveRuimte | is specialisatie van |  | IMIBRO | Object |
| RegistratieveRuimte | is specialisatie van |  | NEN3610 | Registratieve ruimte |
| RegistratieveRuimte | is specialisatie van |  | TopModel | RuimtelijkGeoObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RegistratieveRuimte | is generalisatie van |  | IMIBRO | AdresseerbaarObject |

#### RuimtelijkGeoObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | RuimtelijkGeoObject |
| Formele definitie | FysiekObject dat zowel FysiekeRuimte als GeoObject is |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | FysiekeGeoRuimte |
| Begrip | ruimtelijk geo-object |
| Begripsdefinitie | fysiek object met een vaste plaats ten opzichte van het aardoppervlak. |
| Bronterm | VirtueleRuimte |
| Brondefinitie | geo-object dat zich geheel of gedeeltelijk niet-materieel manifesteert en dus slechts in abstracte en/of geregistreerde vorm bestaat |
| Bron | [NEN3610:2022] |
| Eigenaar | NEN |
| Identificatie | 98f70e83-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RuimtelijkGeoObject | heeft relatie met | heeftRelatieMet | NEN3610 | Virtuele ruimte |
| RuimtelijkGeoObject | is specialisatie van |  | TopModel | FysiekeRuimte |
| RuimtelijkGeoObject | is specialisatie van |  | TopModel | GeoObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RuimtelijkGeoObject | is generalisatie van |  | TopModel | FunctioneleRuimte |
| RuimtelijkGeoObject | is generalisatie van |  | TopModel | GeografischeRuimte |
| RuimtelijkGeoObject | is generalisatie van |  | TopModel | JuridischeRuimte |
| RuimtelijkGeoObject | is generalisatie van |  | TopModel | RegistratieveRuimte |

#### Tijd

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Tijd |
| Formele definitie | AbstractConcept, bestaande uit een eendimensionale lineair geordende continue verzameling. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Bronterm | Temporele entiteit |
| Brondefinitie | benoemd concept dat een daadwerkelijke of virtuele afbakening vormt in een concrete (fysieke, ééndimensionale) tijd die we in de werkelijkheid ervaren. |
| Identificatie | 98f70785-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Tijd | heeft relatie met | heeftRelatieMet | NEN2660 | Temporele entiteit |
| Tijd | is specialisatie van |  | TopModel | AbstractConcept |

#### Toestand

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | Toestand |
| Formele definitie | ConcreetConcept én Temporeel deel van een Entiteit |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | toestand |
| Bronterm | Toestand |
| Brondefinitie | Concreet Concept dat een temporeel deel van een entiteit (een object of activiteit) vormt gedurende een periode tussen twee gebeurtenissen. Een toestand is het geheel van omstandigheden of condities waarin een entiteit (object of activiteit) zich bevindt en wordt gekenmerkt door de relaties en eigenschappen (met hun waarde) van de entiteit gedurende deze periode. |
| Bron | [NEN 2660-1:2022] |
| Eigenaar | NEN |
| Identificatie | 98f71bc2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Toestand | heeft relatie met | heeft | TopModel | Entiteit |
| Toestand | heeft relatie met | heeftRelatieMet | NEN2660 | Toestand |
| Toestand | is specialisatie van |  | NEN2660 | Concreet concept |
| Toestand | is specialisatie van |  | TopModel | ConcreetConcept |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Toestand | is generalisatie van |  | SlimmeWoning | BouwwerkComponentToestand |
| Toestand | is gerelateerd aan | begint | TopModel | Gebeurtenis |
| Toestand | is gerelateerd aan | beEindigt | TopModel | Gebeurtenis |
| Toestand | is gerelateerd aan | heeftRelatieMet | TopModel | Toestand |

#### TopologischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Top |
| Term | TopologischeRuimte |
| Formele definitie | AbstracteRuimte  met een zodanige structuur dat er continue afbeeldingen (functies) op kunnen worden gedefinieerd. |
| Bron | Wikipedia |
| Eigenaar | digiGO |
| Synoniemen | Topologie |
| Begrip | topologische ruimte |
| Begripsdefinitie | ruimte  met een zodanige structuur dat er continue afbeeldingen (functies) op kunnen worden gedefinieerd. |
| Bronterm | Topologische Ruimte |
| Brondefinitie | - |
| Voorbeelden | netwerk |
| Identificatie | 98f705d0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TopologischeRuimte | is specialisatie van |  | TopModel | AbstracteRuimte |

### Bouwwerken

#### 0DRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | 0DRuimte |
| Formele definitie | nuldimensionale GeometrischeRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | punt |
| Begripsdefinitie | nuldimensionale ruimte |
| Identificatie | 98f71e77-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 0DRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

#### 1DRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | 1DRuimte |
| Formele definitie | eendimensionale GeometrischeRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | lijn |
| Begripsdefinitie | eendimensionale ruimte |
| Identificatie | 98f71f3e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 1DRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

#### 2DRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | 2DRuimte |
| Formele definitie | tweedimensionale GeometrischeRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | vlak |
| Begripsdefinitie | tweedimensionale ruimte |
| Identificatie | 98f71ff3-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 2DRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 2DRuimte | is gerelateerd aan | isAfgeleidVan | Bouwwerken | BouwwerkComponentOppervlakte |

#### 3DRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | 3DRuimte |
| Formele definitie | driedimensionale GeometrischeRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | volume |
| Begripsdefinitie | driedimensionale ruimte |
| Identificatie | 98f720a6-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 3DRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| 3DRuimte | is generalisatie van |  | Bouwwerken | BouwwerkComponentInhoud |
| 3DRuimte | is gerelateerd aan | isAfgeleidVan | Bouwwerken | BouwwerkComponentInhoud |

#### BepalingsMethode

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BepalingsMethode |
| Formele definitie | wettelijk of conventioneel vastgelegde methode om de GeometrischeRuimte van een BouwwerkComponent vast te stellen door te bepalen welke elementen wel of niet meetellen en hoe ze gemeten worden |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bepalingsmethode |
| Begripsdefinitie | wettelijk of conventioneel vastgelegde methode om de geometrie van een ruimtelijke of reële bouwwerkcomponent vast te stellen door te bepalen welke elementen wel of niet meetellen en hoe ze gemeten worden |
| Bronterm | bepalingsmethode |
| Brondefinitie | <geen definitie> |
| Bron | [NEN 2580] |
| Eigenaar | NEN |
| Bijzonderheden | Per soort ruimtehoeveelheid (lengte of oppervlakte of inhoud: BVO, NVO, BI, etc.) is er precies één bepalingsmethode. |
| Voorbeelden | Glaslijncorrectie' bij de bepaling van de verhuurbare vloeropprvlakte (VVO) |
| Identificatie | 98f72159-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BepalingsMethode | heeft relatie met | bepaalt | TopModel | GeometrischeRuimte |

#### BouwComplex

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BouwComplex |
| Formele definitie | bouwkundig samenhangende verzameling Bouwwerken op een Terrein |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwcomplex |
| Bronterm | complex |
| Brondefinitie | Functionele ruimte die een verzameling van één of meer gebouwen, constructies, verharding, water en begroeiing betreft die samen een eenheid vormen. |
| Bron | [IMIBRO] |
| Identificatie | 98f72234-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwComplex | heeft relatie met | staatOp | Bouwwerken | Terrein |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwComplex | is gerelateerd aan | isDeelVan | Bouwwerken | Bouwwerk |

#### BouwComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BouwComponent |
| Formele definitie | BouwwerkComponent met een bouwkundige Functie. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwcomponent |
| Bronterm | IfcBuiltElement |
| Brondefinitie | The built element comprises all elements that are primarily part of the construction of a built facility, i.e., its structural and space separating system. Built elements are all physically existent and tangible things. |
| Bron | IFC |
| Eigenaar | bsI |
| Identificatie | 98f7281a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwComponent | is specialisatie van |  | Bouwwerken | ReeleBouwwerkComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwComponent | is generalisatie van |  | BouwComponenten | Afwerking |
| BouwComponent | is generalisatie van |  | BouwComponenten | Balk |
| BouwComponent | is generalisatie van |  | BouwComponenten | Dak |
| BouwComponent | is generalisatie van |  | BouwComponenten | Deur |
| BouwComponent | is generalisatie van |  | BouwComponenten | Fundering |
| BouwComponent | is generalisatie van |  | BouwComponenten | Funderingspaal |
| BouwComponent | is generalisatie van |  | BouwComponenten | Hellingbaan |
| BouwComponent | is generalisatie van |  | BouwComponenten | Kolom |
| BouwComponent | is generalisatie van |  | BouwComponenten | OndersteuningsConstructie |
| BouwComponent | is generalisatie van |  | BouwComponenten | Oplegging |
| BouwComponent | is generalisatie van |  | BouwComponenten | Plaat |
| BouwComponent | is generalisatie van |  | BouwComponenten | Raam |
| BouwComponent | is generalisatie van |  | BouwComponenten | Reling |
| BouwComponent | is generalisatie van |  | BouwComponenten | Schoorsteen |
| BouwComponent | is generalisatie van |  | BouwComponenten | Trap |
| BouwComponent | is generalisatie van |  | BouwComponenten | VirtueleComponent |
| BouwComponent | is generalisatie van |  | BouwComponenten | Vliesgevel |
| BouwComponent | is generalisatie van |  | BouwComponenten | Vloer |
| BouwComponent | is generalisatie van |  | BouwComponenten | Wand |
| BouwComponent | is generalisatie van |  | BouwComponenten | Zonwering |

#### Bouwwerk

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Bouwwerk |
| Formele definitie | door mensen vervaardigd, discreet, samenhangend, constructief zelfstandig GeoObject, direct of indirect steunend in de grond, samengesteld uit constructieve onderdelen, aangevuld met bouwkundige en installatietechnische onderdelen, met een ter plaatse uit te oefenen Functie. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwwerk |
| Begripsdefinitie | door mensen vervaardigd ruimtelijk afgebakend fysiek samenhangend constructief zelfstandig object, verbonden met en steun vindend in de grond, samengesteld uit constructieve onderdelen, aangevuld met bouwkundige en/of installatietechnische onderdelen met een ter plaatse uit te oefenen functie. |
| Bronterm | Constructie |
| Brondefinitie | Gebouwd object dat direct of indirect met de bodem is verbonden en bedoeld is om ter plaatse te functioneren. |
| Bron | [NEN 3610: 2022] |
| Eigenaar | NEN |
| Bijzonderheden | definitie in de Ow: constructie van enige omvang van hout, steen, metaal of ander materiaal, die op de plaats van bestemming hetzij direct of indirect met de grond verbonden is, hetzij direct of indirect steun vindt in of op de grond, bedoeld om ter plaatse te functioneren, met inbegrip van de daarvan deel uitmakende bouwwerkgebonden installaties anders dan een schip dat wordt gebruikt voor verblijf van personen en dat is bestemd en wordt gebruikt voor de vaart; |
| Identificatie | 98f72bab-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Bouwwerk | heeft relatie met | isDeelVan | Bouwwerken | BouwComplex |
| Bouwwerk | heeft relatie met |  | RVB | Bouwlaag |
| Bouwwerk | heeft relatie met | ? | MiniBIM | BouwwerkPerceel |
| Bouwwerk | heeft relatie met | typeert | MiniBIM | BouwwerkType |
| Bouwwerk | heeft relatie met | heeft | Bouwwerken | BrandCompartiment |
| Bouwwerk | heeft relatie met | is deel van | Paspoorten | Complex |
| Bouwwerk | heeft relatie met | heeftRelatieMet | NEN3610 | Constructie |
| Bouwwerk | heeft relatie met | isDeelVan | Bouwwerken | ReeleBouwwerkComponent |
| Bouwwerk | heeft relatie met | isDeelVan | Bouwwerken | RuimtelijkeBouwwerkComponent |
| Bouwwerk | heeft relatie met | aggregeertTot | IMWO00 | Terrein |
| Bouwwerk | heeft relatie met | staatOp | Bouwwerken | Terrein |
| Bouwwerk | is specialisatie van |  | TopModel | GeoObject |
| Bouwwerk | is specialisatie van |  | IFC | IfcObjectType |
| Bouwwerk | is specialisatie van |  | IFC | IfcSpace |
| Bouwwerk | is specialisatie van |  | RVB | OmgevingsElement |
| Bouwwerk | is specialisatie van |  | RVB | VastgoedObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Bouwwerk | is generalisatie van |  | IMWO00 | Ander Bouwwerk |
| Bouwwerk | is generalisatie van |  | Paspoorten | Gebouw |
| Bouwwerk | is generalisatie van |  | Bouwwerken | Gebouw |
| Bouwwerk | is generalisatie van |  | RVB | Gebouw |
| Bouwwerk | is generalisatie van |  | AedesImVg | Gebouw |
| Bouwwerk | is generalisatie van |  | MiniBIM | Onderbouw |
| Bouwwerk | is generalisatie van |  | MiniBIM | Woning |
| Bouwwerk | is generalisatie van |  | MiniBIM | Woongebouw |
| Bouwwerk | is gerelateerd aan | aggregeertTot | IMWO00 | Bouwdeel |
| Bouwwerk | is gerelateerd aan | isDeelVan | IMWO00 | Bouwlaag |
| Bouwwerk | is gerelateerd aan | isDeelVan | MiniBIM | Brandcompartiment |
| Bouwwerk | is gerelateerd aan | ligtIn | MiniBIM | Buitenruimte |
| Bouwwerk | is gerelateerd aan | aggregeertTot | IMWO00 | Gebied |
| Bouwwerk | is gerelateerd aan | isDeelVan | MiniBIM | Ruimte |
| Bouwwerk | is gerelateerd aan |  | RVB | VastgoedComplex |
| Bouwwerk | is gerelateerd aan | betreft | MiniBIM | WOZ-Eigendomseenheid |
| Bouwwerk | is gerelateerd aan | ligtIn | MiniBIM | Zone |

#### BouwwerkComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BouwwerkComponent |
| Formele definitie | samenstellend deel van een Bouwwerk of een BouwwerkComponent |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwwerkcomponent |
| Begripsdefinitie | samenstellend deel van een Bouwwerk of een BouwwerkComponent |
| Identificatie | 98f72e11-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponent | heeft relatie met | heeft | SlimmeWoning | BouwwerkComponentToestand |
| BouwwerkComponent | heeft relatie met | heeft | TopModel | GeometrischeRuimte |
| BouwwerkComponent | heeft relatie met | heeft | Bouwwerken | RuimteHoeveelheid |
| BouwwerkComponent | is specialisatie van |  | TopModel | FysiekObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponent | is generalisatie van |  | Bouwwerken | ReeleBouwwerkComponent |
| BouwwerkComponent | is generalisatie van |  | Bouwwerken | RuimtelijkeBouwwerkComponent |
| BouwwerkComponent | is gerelateerd aan | van | Bouwwerken | Raakvlak |
| BouwwerkComponent | is gerelateerd aan | met | Bouwwerken | Raakvlak |

#### BouwwerkComponentInhoud

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BouwwerkComponentInhoud |
| Formele definitie | RuimteHoeveelheid van een 3DRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwwerkcomponentinhoud |
| Begripsdefinitie | inhoud van een bouwwerkcomponent |
| Identificatie | 98f72f2a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponentInhoud | heeft relatie met | isAfgeleidVan | Bouwwerken | 3DRuimte |
| BouwwerkComponentInhoud | is specialisatie van |  | Bouwwerken | 3DRuimte |
| BouwwerkComponentInhoud | is specialisatie van |  | Bouwwerken | RuimteHoeveelheid |

#### BouwwerkComponentOppervlakte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BouwwerkComponentOppervlakte |
| Formele definitie | RuimteHoeveelheid van een 2DRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bouwwerkcomponentoppervlakte |
| Begripsdefinitie | oppervlakte van een bouwwerkcomponent |
| Identificatie | 98f73080-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponentOppervlakte | heeft relatie met | isAfgeleidVan | Bouwwerken | 2DRuimte |
| BouwwerkComponentOppervlakte | is specialisatie van |  | Bouwwerken | RuimteHoeveelheid |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponentOppervlakte | is gerelateerd aan | teltOpTot | Bouwwerken | NEN2580OppervlakteCategorie |

#### BrandCompartiment

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BrandCompartiment |
| Formele definitie | verzameling aaneengesloten RuimtelijkeBouwwerkComponenten, bestemd als maximaal uitbreidingsgebied van brand, als geheel begrensd door een geheel van ReeleBouwwerkComponenten met een voorgeschreven Weerstand tegen BrandDoorslag en BrandOverslag (WBDBO). |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | brandcompartiment |
| Begripsdefinitie | gedeelte van een of meer bouwwerken bestemd als maximaal uitbreidingsgebied van brand. |
| Bronterm | Brandcompartiment |
| Brondefinitie | Gedeelte van een of meer bouwwerken bestemd als maximaal uitbreidingsgebied van brand. |
| Bron | [Bbl] |
| Eigenaar | MinVRO |
| Commentaar | Dat een brandcompartiment volgens het Bbl over meerdere bouwwerken kan lopen, begrijpik niet. |
| Identificatie | 98f73329-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BrandCompartiment | heeft relatie met | heeft | Bouwwerken | RuimtelijkeBouwwerkComponent |
| BrandCompartiment | is specialisatie van |  | Bouwwerken | RuimtelijkeBouwwerkComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BrandCompartiment | is gerelateerd aan | heeft | Bouwwerken | Bouwwerk |

#### BrutoGeometrischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | BrutoGeometrischeRuimte |
| Formele definitie | GeometrischeRuimte, bepaald door de buitengeometrie van de omhullende scheidingsconstructies. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7354d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BrutoGeometrischeRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

#### Gebouw

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Gebouw |
| Formele definitie | overdekt en geheel of gedeeltelijk met wanden omsloten betreedbaar en afsluitbaar Bouwwerk ten behoeve van verblijf van, gebruik door, onderbrengen van of beschermen van mensen, dieren of voorwerpen of de productie van goederen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | gebouw |
| Begripsdefinitie | overdekt en geheel of gedeeltelijk met wanden omsloten, betreedbaar en afsluitbaar  Bouwwerk, primair bedoeld voor het bieden van een afgeschermde omgeving voor het verblijf, gebruik, onderbrengen of beschermen van mensen, dieren of voorwerpen, of voor de productie van goederen. |
| Bronterm | Gebouw |
| Brondefinitie | Overdekte en geheel of gedeeltelijk met wanden omsloten constructie bedoeld voor het in een afgeschermde omgeving onderbrengen van mensen, dieren of voorwerpen of voor de productie van goederen. |
| Identificatie | 98f7375d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Gebouw | heeft relatie met | heeft | MiniBIM | Bovenbouw |
| Gebouw | heeft relatie met | is deel van | Paspoorten | Complex |
| Gebouw | heeft relatie met | isFysiekGescheidenVan | MiniBIM | Gebouw |
| Gebouw | heeft relatie met | heeftRelatieMet | NEN3610 | Gebouw |
| Gebouw | heeft relatie met | is van | Paspoorten | Gebouwsoort |
| Gebouw | heeft relatie met | heeft | MiniBIM | Lifthal |
| Gebouw | heeft relatie met | heeft | MiniBIM | Onderbouw |
| Gebouw | heeft relatie met | bevat | IMBAG | Pand |
| Gebouw | heeft relatie met | staatOp | MiniBIM | Plint |
| Gebouw | heeft relatie met | isDeelVan | Ketenstandaard-Ruimte | Ruimte |
| Gebouw | heeft relatie met | heeft | MiniBIM | Trappenhuis |
| Gebouw | heeft relatie met | heeftVerdieping | OTLBenU | Verdieping |
| Gebouw | heeft relatie met | heeft | Bouwwerken | Verdieping |
| Gebouw | heeft relatie met | bevat | Woonobjecten | WoonObject |
| Gebouw | is specialisatie van |  | Paspoorten | Bouwwerk |
| Gebouw | is specialisatie van |  | Bouwwerken | Bouwwerk |
| Gebouw | is specialisatie van |  | RVB | Bouwwerk |
| Gebouw | is specialisatie van |  | IMWO00 | Bouwwerk |
| Gebouw | is specialisatie van |  | NEN3610 | Constructie |
| Gebouw | is specialisatie van |  | Ketenstandaard-Ruimte | Functionele entiteit |
| Gebouw | is specialisatie van |  | NEN2660 | Fysiek object |
| Gebouw | is specialisatie van |  | BOT | Zone |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Gebouw | heeft als onderdeel |  | IMWO00 | DiscreetGebouw |
| Gebouw | heeft als onderdeel |  | IMWO00 | InpandigeRuimte |
| Gebouw | is generalisatie van |  | IMIBRO | Bouwlaag |
| Gebouw | is generalisatie van |  | IMIBRO | Pand |
| Gebouw | is generalisatie van |  | Woonobjecten | WoonGebouw |
| Gebouw | is gerelateerd aan | is deel van | Paspoorten | Element |
| Gebouw | is gerelateerd aan | isFysiekGescheidenVan | MiniBIM | Gebouw |
| Gebouw | is gerelateerd aan | heeftRelatieMet | Bouwwerken | Gebouw |
| Gebouw | is gerelateerd aan | heeftGebouw | OTLBenU | Kavel |

#### InstallatieComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | InstallatieComponent |
| Formele definitie | ReeleBouwwerkComponent die samenstellend deel is van een Installatie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | installatiecomponent |
| Identificatie | 98f7397a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| InstallatieComponent | heeft relatie met | heeftRelatieMet | GIR | Component |
| InstallatieComponent | heeft relatie met | isOnderdeelVan | Installaties | Installatie |
| InstallatieComponent | is specialisatie van |  | Bouwwerken | ReeleBouwwerkComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| InstallatieComponent | is generalisatie van |  | SlimmeWoning | Apparaat |

#### InventarisComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | InventarisComponent |
| Formele definitie | ReeleBouwwerkComponent die dient ter inrichting van het Bouwwerk |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | inventariscomponent |
| Identificatie | 98f73b7e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| InventarisComponent | is specialisatie van |  | Bouwwerken | ReeleBouwwerkComponent |

#### Materiaal

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Materiaal |
| Formele definitie | Materie die is bestemd om te worden verwerkt tot een product |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | materiaal |
| Brondefinitie | Natuurlijke of kunstmatig geproduceerde stof die is bestemd om te worden verwerkt tot een product |
| Bron | CB23 |
| Identificatie | 98f73ce4-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Materiaal | heeft relatie met | is van | Paspoorten | Materiaalsoort |
| Materiaal | heeft relatie met | isSamengesteldUit | NEN2660 | Materie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Materiaal | is gerelateerd aan | bestaatUit | NEN2767 | Bouwdeel |
| Materiaal | is gerelateerd aan | isVan | ILS-OenE | Bouwproduct |
| Materiaal | is gerelateerd aan | isVan | MiniBIM | Element |
| Materiaal | is gerelateerd aan | bestaatUit | Bouwwerken | Product |
| Materiaal | is gerelateerd aan | bevat | Paspoorten | ProductMateriaal |

#### NEN2580OppervlakteCategorie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | NEN2580OppervlakteCategorie |
| Formele definitie | Type BouwwerkComponentOppervlakte, zoals in NEN 2580 onderscheiden |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | NEN2580-oppervlaktecategorie |
| Begripsdefinitie | Type bouwwerkcomponentoppervlakte, zoals in NEN 2580 onderscheiden |
| Voorbeelden | Brutovloeroppervlakte (BVO), Gebuirksoppervlakte (GO), Nettovloeroppervlakte (NVO), Tarra-oppervlakte (TO), Verhuurbare vloeroppervlakte (VVO) |
| Identificatie | 98f73e3c-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| NEN2580OppervlakteCategorie | heeft relatie met | teltOpTot | Bouwwerken | BouwwerkComponentOppervlakte |

#### NettoGeometrischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | NettoGeometrischeRuimte |
| Formele definitie | GeometrischeRuimte, bepaald door de binnengeometrie van de omhullende scheidingsconstructies. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f73f81-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| NettoGeometrischeRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

#### Product

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Product |
| Formele definitie | geproduceerd ReeelObject, dat als ReeleBouwwerkComponent wordt ingezet |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | product |
| Identificatie | 98f740b3-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Product | heeft relatie met | behoortTot | ETIM | ETIM-klasse |
| Product | heeft relatie met | bestaatUit | Bouwwerken | Materiaal |
| Product | heeft relatie met | heeft | ETIM | ModellingClass |
| Product | heeft relatie met | heeft | ETIM | Waarde |
| Product | is specialisatie van |  | Bouwwerken | ReeleBouwwerkComponent |
| Product | is specialisatie van |  | Ketenstandaard-Ruimte | Technische entiteit |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Product | is generalisatie van |  | GIR | Component |

#### Raakvlak

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Raakvlak |
| Formele definitie | Samenstel van 0D, 1D en 2D FysiekeRuimten op de grens van twee FysiekObjecten. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | raakvlak |
| Begripsdefinitie | samenstel van punten, lijnen en vlakken op de grens van twee fysieke objecten |
| Bronterm | raakvlak |
| Brondefinitie | ruimtelijk object, typisch een dunne 2D fysieke ruimte (maar 0D of 1D kan ook), dat de verbinding legt tussen twee fysieke objecten of poorten van fysieke objecten waarlangs een statische of dynamische wisselwerking of interactie tussen die elementen kan plaatsvinden |
| Bron | [NEN 2660-2:2022] |
| Eigenaar | NEN |
| Identificatie | 98f741f0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Raakvlak | heeft relatie met | van | Bouwwerken | BouwwerkComponent |
| Raakvlak | heeft relatie met | met | Bouwwerken | BouwwerkComponent |
| Raakvlak | heeft relatie met | heeftRelatieMet | NEN2660 | Raakvlak |
| Raakvlak | is specialisatie van |  | NEN2660 | Ruimtelijk gebied |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Raakvlak | is gerelateerd aan | heeftRelatieMet | Bouwwerken | Raakvlak |

#### ReeleBouwwerkComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | ReeleBouwwerkComponent |
| Formele definitie | BouwwerkComponent, die een ReeelObject is |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | reële bouwwerkcomponent |
| Identificatie | 98f74347-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ReeleBouwwerkComponent | heeft relatie met | heeftRelatieMet | IFC | IfcBuiltElement |
| ReeleBouwwerkComponent | heeft relatie met | isDeelVan | Bouwwerken | ReeleBouwwerkComponent |
| ReeleBouwwerkComponent | is specialisatie van |  | Bouwwerken | BouwwerkComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ReeleBouwwerkComponent | is generalisatie van |  | Bouwwerken | BouwComponent |
| ReeleBouwwerkComponent | is generalisatie van |  | Bouwwerken | InstallatieComponent |
| ReeleBouwwerkComponent | is generalisatie van |  | Bouwwerken | InventarisComponent |
| ReeleBouwwerkComponent | is generalisatie van |  | Bouwwerken | Product |
| ReeleBouwwerkComponent | is gerelateerd aan | isDeelVan | Bouwwerken | Bouwwerk |
| ReeleBouwwerkComponent | is gerelateerd aan | isDeelVan | Bouwwerken | ReeleBouwwerkComponent |

#### RuimteHoeveelheid

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | RuimteHoeveelheid |
| Formele definitie | vastgesteld aantal eenheden van een geometrische grootheid |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | ruimtehoeveelheid |
| Begripsdefinitie | vastgesteld aantal eenheden van een geometrische grootheid |
| Identificatie | 98f7447c-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RuimteHoeveelheid | is generalisatie van |  | Bouwwerken | BouwwerkComponentInhoud |
| RuimteHoeveelheid | is generalisatie van |  | Bouwwerken | BouwwerkComponentOppervlakte |
| RuimteHoeveelheid | is gerelateerd aan | heeft | Bouwwerken | BouwwerkComponent |

#### RuimtelijkeBouwwerkComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | RuimtelijkeBouwwerkComponent |
| Formele definitie | BouwwerkComponent, die een FysiekeRuimte is |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | ruimtelijke bouwwerkcomponent |
| Identificatie | 98f745d8-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RuimtelijkeBouwwerkComponent | heeft relatie met | isDeelVan | Bouwwerken | RuimtelijkeBouwwerkComponent |
| RuimtelijkeBouwwerkComponent | is specialisatie van |  | Bouwwerken | BouwwerkComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| RuimtelijkeBouwwerkComponent | is generalisatie van |  | Bouwwerken | BrandCompartiment |
| RuimtelijkeBouwwerkComponent | is generalisatie van |  | JuridischeObjecten | GemeenschappelijkeRuimte |
| RuimtelijkeBouwwerkComponent | is generalisatie van |  | JuridischeObjecten | PrivéRuimte |
| RuimtelijkeBouwwerkComponent | is generalisatie van |  | Bouwwerken | Verdieping |
| RuimtelijkeBouwwerkComponent | is gerelateerd aan | over | IMKAD | AppartementsrechtSplitsing |
| RuimtelijkeBouwwerkComponent | is gerelateerd aan | isDeelVan | Bouwwerken | Bouwwerk |
| RuimtelijkeBouwwerkComponent | is gerelateerd aan | heeft | Bouwwerken | BrandCompartiment |
| RuimtelijkeBouwwerkComponent | is gerelateerd aan | isDeelVan | Bouwwerken | RuimtelijkeBouwwerkComponent |
| RuimtelijkeBouwwerkComponent | is gerelateerd aan | heeft | Bouwwerken | Verdieping |

#### TarraGeometrischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | TarraGeometrischeRuimte |
| Formele definitie | GeometrischeRuimte tussen BrutoGeometrischeRuimte en NettoGeometrischeRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Bijzonderheden | Equivalent met de GeometrischeRuimte van de omhullende scheidngsconstructie |
| Identificatie | 98f746f9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TarraGeometrischeRuimte | is specialisatie van |  | TopModel | GeometrischeRuimte |

#### Terrein

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Terrein |
| Formele definitie | FunctioneleRuimte, waarin Bouwwerken geplaatst zijn of kunnen worden. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | terrein |
| Brondefinitie | Door een fysiek voorkomen gekarakteriseerd zichtbaar begrensd stuk grond |
| Bron | [IMBAG] |
| Eigenaar | MinBZK |
| Bijzonderheden | Komt uit NEN 3610:2011; is in NEN 3610:2022 vervallen. Reden onbekend |
| Identificatie | 98f7482f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Terrein | heeft relatie met | wordtBepaaldDoor | MiniBIM | Functie |
| Terrein | heeft relatie met | wordtBepaaldDoor | MiniBIM | Rechtsorde |
| Terrein | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Terrein | is specialisatie van |  | TopModel | FunctioneleRuimte |
| Terrein | is specialisatie van |  | IFC | IfcGeographicElement |
| Terrein | is specialisatie van |  | IFC | IfcSpace |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Terrein | is gerelateerd aan | staatOp | Bouwwerken | BouwComplex |
| Terrein | is gerelateerd aan | aggregeertTot | IMWO00 | Bouwwerk |
| Terrein | is gerelateerd aan | staatOp | Bouwwerken | Bouwwerk |
| Terrein | is gerelateerd aan | aggregeertTot | IMWO00 | Buitenruimte |
| Terrein | is gerelateerd aan | typeert | MiniBIM | TerreinType |

#### Verdieping

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwwerken |
| Term | Verdieping |
| Formele definitie | verzameling van alle aaneengesloten RuimtelijkeBouwwerkComponenten tussen twee opeenvolgende horizontale scheidingsconstructies in een Bouwwerk. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | verdieping |
| Begripsdefinitie | totale ruimte tussen twee opeenvolgende vloeren of tussen vloer en dak in een bouwwerk. |
| Bronterm | storey |
| Brondefinitie | space between two consecutive floors or between a floor and a roof. |
| Bron | ISO 6707-1 |
| Eigenaar | ISO |
| Bijzonderheden | nader uit te werken: deelverdiepingen (zoals bij split-level) en marges (bij niet-borizontale verdiepingen), en samenstelling van verdiepingen (verdieping over meerdere lagen  met subverdiepingen); misschien nog toevoegen: 'bouwlaag', als referentie aan de reële componenten |
| Identificatie | 98f74965-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Verdieping | heeft relatie met | heeftRuimte | OTLBenU | Ruimte |
| Verdieping | heeft relatie met | heeft | Bouwwerken | RuimtelijkeBouwwerkComponent |
| Verdieping | is specialisatie van |  | Bouwwerken | RuimtelijkeBouwwerkComponent |
| Verdieping | is specialisatie van |  | BOT | Zone |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Verdieping | is gerelateerd aan | heeftVerdieping | OTLBenU | Gebouw |
| Verdieping | is gerelateerd aan | heeft | Bouwwerken | Gebouw |

### Bouwcomponenten

#### Afwerking

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Afwerking |
| Formele definitie | BouwComponent, vast verbonden met een andere  BouwComponent met de Functie Afdekken |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | afwerking |
| Begripsdefinitie | bouwcomponent die een deel van een andere bouwcomponent bedekt en volledig afhankelijk is van dat andere element. |
| Bronterm | Afwerking |
| Brondefinitie | Een bekleding is een element dat een deel van een ander element bedekt en volledig afhankelijk is van dat andere element. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f74c08-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Afwerking | heeft relatie met | heeftRelatieMet | IFC | IfcCovering |
| Afwerking | is specialisatie van |  | Bouwwerken | BouwComponent |
| Afwerking | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Afwerking | is specialisatie van |  | NL-SfB | Functioneel gebouwelement |
| Afwerking | is specialisatie van |  | IFC | IfcCovering |

#### Balk

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Balk |
| Formele definitie | langwerpige (binnen bepaalde marges) horizontaal gelegen BouwComponent met dragende Functie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | balk |
| Begripsdefinitie | doorgaans een horizontaal of bijna horizontaal constructieve component die in staat is om belastingen te weerstaan, voornamelijk door buigweerstand |
| Bronterm | Ligger |
| Brondefinitie | doorgaans een horizontaal of bijna horizontaal constructief element dat in staat is om belastingen te weerstaan, voornamelijk door buigweerstand |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f74d5a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Balk | is specialisatie van |  | Bouwwerken | BouwComponent |
| Balk | is specialisatie van |  | MiniBIM | Element |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Balk | is generalisatie van |  | MiniBIM | Constructieve balk |
| Balk | is gerelateerd aan | heeftRelatieMet | IFC | IfcBeam |

#### Dak

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Dak |
| Formele definitie | BouwComponent aan de bovenkant  van een Bouwwerk met de Functie de binnenruimte van de buitenruimte af te grenzen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | dak |
| Begripsdefinitie | bovenste, beschermende afsluiting van een bouwwerk |
| Bronterm | Dak |
| Brondefinitie | beschrijving van het totale dak |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f74eb0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Dak | is specialisatie van |  | Bouwwerken | BouwComponent |
| Dak | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Dak | is specialisatie van |  | IFC | IfcRoof |
| Dak | is specialisatie van |  | MiniBIM | Vloer |
| Dak | is specialisatie van |  | MiniBIM | Vloer |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Dak | is gerelateerd aan | heeftRelatieMet | IFC | IfcRoof |

#### Deur

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Deur |
| Formele definitie | BouwComponent als onderdeel van een Wand met de Functie gecontroleerde toegang te verschaffen aan mensen, goederen, dieren en voertuigen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | deur |
| Begripsdefinitie | beweegbare bouwcomponent, die toegang biedt tot een ruimte. |
| Bronterm | Deur |
| Brondefinitie | gebouwd element dat voornamelijk wordt gebruikt om gecontroleerde toegang te bieden voor mensen, goederen, dieren en voertuigen |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f74f93-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Deur | is specialisatie van |  | Bouwwerken | BouwComponent |
| Deur | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Deur | is specialisatie van |  | MiniBIM | Element |
| Deur | is specialisatie van |  | IFC | IfcDoor |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Deur | is generalisatie van |  | MiniBIM | Garagedeur |
| Deur | is generalisatie van |  | MiniBIM | Vluchtdeur |
| Deur | is generalisatie van |  | MiniBIM | Woningtoegangsdeur |
| Deur | is gerelateerd aan | isDeelVan | BinnenRuimteNetwerk | Deurvlak |
| Deur | is gerelateerd aan | heeftRelatieMet | IFC | IfcDoor |

#### Fundering

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Fundering |
| Formele definitie | BouwComponent onder een Bouwwerk met de Functie de belasting van het Bouwwerk over te dragen aan de ondergrond. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | fundering |
| Begripsdefinitie | onderdeel van de fundering van een constructie dat de belasting verspreidt en overdraagt aan de ondergrond |
| Bronterm | Fundering |
| Brondefinitie | Een funderingselement is een onderdeel van de fundering van een constructie dat de belasting verspreidt en overdraagt aan de ondergrond |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f752da-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Fundering | is specialisatie van |  | Bouwwerken | BouwComponent |
| Fundering | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Fundering | is specialisatie van |  | IFC | IfcFooting |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Fundering | is gerelateerd aan | heeftRelatieMet | IFC | IfcFooting |

#### Funderingspaal

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Funderingspaal |
| Formele definitie | langwerpige (binnen bepaalde marges) verticale BouwComponent die onderdeel is van een Fundering met de Functie een deel van de belasting van een Bouwwerk over te dragen naar de ondergrond. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | funderingspaal |
| Begripsdefinitie | slank constructie-element van hout, beton of staal, dat in de grond wordt gedreven, gespoten of anderszins ingebracht met als doel een belasting te dragen |
| Bronterm | Funderingspaal |
| Brondefinitie | slanke constructie-element van hout, beton of staal, dat in de grond wordt gedreven, gespoten of anderszins ingebracht met als doel een belasting te dragen |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f753a7-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Funderingspaal | is specialisatie van |  | Bouwwerken | BouwComponent |
| Funderingspaal | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Funderingspaal | is specialisatie van |  | IFC | IfcPile |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Funderingspaal | is gerelateerd aan | heeftRelatieMet | IFC | IfcPile |

#### Hellingbaan

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Hellingbaan |
| Formele definitie | plaatvormige BouwComponent met als Functie personen, geoderen en dieren te verplaatsen tussen Vloeren op verschillende hoogte in een Bouwwerk |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | hellingbaan |
| Begripsdefinitie | verticale doorgang die zorgt voor een circulatieroute voor personen tussen het ene vloerniveau en een ander vloerniveau op een andere hoogte. Deze kan een bordes bevatten als tussenliggende vloerplaat. |
| Bronterm | Hellingbaan |
| Brondefinitie | Een verticale doorgang die zorgt voor een circulatieroute voor personen tussen het ene vloerniveau en een ander vloerniveau op een andere hoogte. Deze kan een bordes bevatten als tussenliggende vloerplaat. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f7547a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Hellingbaan | is specialisatie van |  | Bouwwerken | BouwComponent |
| Hellingbaan | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Hellingbaan | is specialisatie van |  | IFC | IfcRamp |
| Hellingbaan | is specialisatie van |  | MiniBIM | Wand |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Hellingbaan | is gerelateerd aan | heeftRelatieMet | IFC | IfcRamp |

#### Kolom

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Kolom |
| Formele definitie | binnen bepaalde marges verticale BouwComponent met als Functie het gewicht van het bovenliggende deel van een Bouwwerk over te dragen aan onderliggende andere Bouwcomponenten. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | kolom |
| Begripsdefinitie | verticale structurele of architectonische kolom die vaak is uitgelijnd met een kruispunt van een structureel raster. In de meeste gevallen vertegenwoordigt het een verticale, of bijna verticale, structurele kolom die door middel van compressie het gewicht van de bovenliggende structuur overdraagt aan andere structurele elementen eronder. Het kan ook een dergelijke kolom vertegenwoordigen vanuit architectonisch oogpunt, in welk geval het een niet-dragend element kan zijn. |
| Bronterm | Kolom |
| Brondefinitie | verticale structurele of architectonische kolom die vaak is uitgelijnd met een kruispunt van een structureel raster. In de meeste gevallen vertegenwoordigt het een verticale, of bijna verticale, structurele kolom die door middel van compressie het gewicht van de bovenliggende structuur overdraagt aan andere structurele elementen eronder. Het kan ook een dergelijke kolom vertegenwoordigen vanuit architectonisch oogpunt, in welk geval het een niet-dragend element kan zijn. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75556-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Kolom | is specialisatie van |  | Bouwwerken | BouwComponent |
| Kolom | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Kolom | is specialisatie van |  | MiniBIM | Element |
| Kolom | is specialisatie van |  | IFC | IfcColumn |
| Kolom | is specialisatie van |  | IMIBRO | Panddeel |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Kolom | is generalisatie van |  | MiniBIM | Constructieve kolom |
| Kolom | is gerelateerd aan | heeftRelatieMet | IFC | IfcColumn |

#### OndersteuningsConstructie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | OndersteuningsConstructie |
| Formele definitie | BouwComponent met de Functie belastingen te dragen tussen of voorbij steunpunten. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | ondersteuningsconstructie |
| Begripsdefinitie | structureel element dat is ontworpen om belastingen over te brengen tussen steunpunten of voorbij steunpunten. |
| Bronterm | Component |
| Brondefinitie | structureel element dat is ontworpen om belastingen over te brengen tussen steunpunten of voorbij steunpunten. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75644-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| OndersteuningsConstructie | is specialisatie van |  | Bouwwerken | BouwComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| OndersteuningsConstructie | is gerelateerd aan | heeftRelatieMet | IFC | IfcMember |

#### Oplegging

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Oplegging |
| Formele definitie | BouwComponent met de Functie in een Bouwwerk belastingen van de bovenbouw naar de onderbouw over te brengen, en die doorgaans beweging (verplaatsing of rotatie) in één of meer vrijheidsgraden toelaat. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | oplegging |
| Begripsdefinitie | bouwproduct om belastingen van de bovenbouw naar de onderbouw over te brengen, en dat doorgaans beweging (verplaatsing of rotatie) in één of meer vrijheidsgraden toelaat. |
| Bronterm | Oplegging |
| Brondefinitie | Een oplegging wordt gewoonlijk gebruikt om belastingen van de bovenbouw naar de onderbouw over te brengen, en dat doorgaans beweging (verplaatsing of rotatie) in één of meer vrijheidsgraden toelaat. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75711-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Oplegging | heeft relatie met | heeftRelatieMet | IFC | IfcBearing |
| Oplegging | is specialisatie van |  | Bouwwerken | BouwComponent |
| Oplegging | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Oplegging | is specialisatie van |  | IFC | IfcBearing |

#### Plaat

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Plaat |
| Formele definitie | vlakke BouwComponent met een constante dikte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | plaat |
| Begripsdefinitie | vlak onderdeel met een constante dikte. |
| Bronterm | Plaat |
| Brondefinitie | Een plaat is vaak een vlak onderdeel met een constante dikte. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f757e2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Plaat | heeft relatie met | heeftRelatieMet | IFC | IfcPlate |
| Plaat | is specialisatie van |  | Bouwwerken | BouwComponent |
| Plaat | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Plaat | is specialisatie van |  | IFC | IfcPlate |

#### Raam

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Raam |
| Formele definitie | BouwComponent in een Opening in Wand of Dak van een Bouwwerk met de Functie het toelaten van natuurlijk licht en frisse lucht. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | raam |
| Begripsdefinitie | bouwelement dat voornamelijk wordt gebruikt om natuurlijk licht en frisse lucht toe te laten. Het omvat verticale openingen, maar ook horizontale openingen zoals dakramen of lichtkoepels |
| Bronterm | Raam |
| Brondefinitie | bouwelement dat voornamelijk wordt gebruikt om natuurlijk licht en frisse lucht toe te laten. Het omvat verticale openingen, maar ook horizontale openingen zoals dakramen of lichtkoepels |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75924-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Raam | heeft relatie met | heeftRelatieMet | IFC | IfcWindow |
| Raam | is specialisatie van |  | Bouwwerken | BouwComponent |
| Raam | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Raam | is specialisatie van |  | IFC | IfcWindow |
| Raam | is specialisatie van |  | MiniBIM | Kozijn |

#### Reling

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Reling |
| Formele definitie | BouwComponent in de vorm van een frame naast ruimten voor menselijke of voertuigcirculatie en bij bepaalde ruimteafscheidingen, losstaand of aan een Wand bevestigd,  met de Functie  ondersteuning en bescherming tegen vallen en botsen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | reling |
| Begripsdefinitie | frameconstructie die zich bevindt naast ruimtes voor menselijke of voertuigcirculatie en bij bepaalde ruimteafscheidingen, waar deze wordt gebruikt in plaats van muren of ter aanvulling van muren. Ontworpen als een optionele fysieke ondersteuning, of om letsel of schade te voorkomen, hetzij door vallen of botsing. |
| Bronterm | Reling |
| Brondefinitie | frameconstructie die zich bevindt naast ruimtes voor menselijke of voertuigcirculatie en bij bepaalde ruimteafscheidingen, waar deze wordt gebruikt in plaats van muren of ter aanvulling van muren. Ontworpen als een optionele fysieke ondersteuning, of om letsel of schade te voorkomen, hetzij door vallen of botsing. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75bca-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Reling | heeft relatie met | heeftRelatieMet | IFC | IfcRailing |
| Reling | is specialisatie van |  | Bouwwerken | BouwComponent |
| Reling | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Reling | is specialisatie van |  | IFC | IfcRailing |

#### Schoorsteen

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Schoorsteen |
| Formele definitie | (binnen bepaalde marges) verticale holle BouwComponent  met de Functie rookgassen en dampen veilig  naar buiten te leiden |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | schoorsteen |
| Begripsdefinitie | verticale, of nagenoeg verticale, onderdelen van de constructie van een gebouw en maken deel uit van de gebouwschil |
| Bronterm | Schoorsteen |
| Brondefinitie | Schoorstenen zijn doorgaans verticale, of nagenoeg verticale, onderdelen van de constructie van een gebouw en maken deel uit van de gebouwschil |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75ca1-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Schoorsteen | heeft relatie met | heeftRelatieMet | IFC | IfcChimney |
| Schoorsteen | is specialisatie van |  | Bouwwerken | BouwComponent |
| Schoorsteen | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Schoorsteen | is specialisatie van |  | IFC | IfcChimney |

#### Trap

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Trap |
| Formele definitie | BouwComponent met als Functie personen, geoderen en dieren te verplaatsen tussen Vloeren op verschillende hoogte in een Bouwwerk in de vorm van een reeks aaneengesloten traptreden al dan niet met tussenbordessen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | trap |
| Begripsdefinitie | verticale doorgang die het mogelijk maakt voor gebruikers om te lopen (stappen) van het ene vloerniveau naar een ander vloerniveau op een andere hoogte. Een trap kan een bordes bevatten als tussenliggende vloerplaat. |
| Bronterm | Trap |
| Brondefinitie | verticale doorgang die het mogelijk maakt voor gebruikers om te lopen (stappen) van het ene vloerniveau naar een ander vloerniveau op een andere hoogte. Een trap kan een bordes bevatten als tussenliggende vloerplaat. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75d68-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Trap | heeft relatie met | heeftRelatieMet | IFC | IfcStair |
| Trap | is specialisatie van |  | Bouwwerken | BouwComponent |
| Trap | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Trap | is specialisatie van |  | MiniBIM | Element |
| Trap | is specialisatie van |  | IFC | IfcStair |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Trap | is generalisatie van |  | MiniBIM | Hoofdtrap |
| Trap | is generalisatie van |  | MiniBIM | Vluchttrap |

#### VirtueleComponent

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | VirtueleComponent |
| Formele definitie | Denkbeeldige BouwComponent, die een  denkbeeldig, tijdelijk of voorlopig vlak, gebied of grens aanduidt. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | virtuele component |
| Begripsdefinitie | speciaal element dat wordt gebruikt om denkbeeldige, tijdelijke of voorlopige gebieden, volumes en grenzen aan te duiden. |
| Bronterm | Virtueel element |
| Brondefinitie | speciaal element dat wordt gebruikt om denkbeeldige, tijdelijke of voorlopige gebieden, volumes en grenzen aan te duiden. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75e43-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VirtueleComponent | heeft relatie met | heeftRelatieMet | IFC | IfcVirtualElement |
| VirtueleComponent | is specialisatie van |  | Bouwwerken | BouwComponent |

#### Vliesgevel

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Vliesgevel |
| Formele definitie | BouwComponent opgehangen aan de rand van de Vloer of het Dak van een Bouwwerk met de Functie scheiden van Binnenruimte en Buitenruimte. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | vliesgevel |
| Begripsdefinitie | buitenmuur van een gebouw die bestaat uit een samenstelling van componenten, opgehangen aan de rand van de vloer- of dakconstructie in plaats van dragend te zijn op een vloer |
| Bronterm | Vliesgevel |
| Brondefinitie | buitenmuur van een gebouw die bestaat uit een samenstelling van componenten, opgehangen aan de rand van de vloer- of dakconstructie in plaats van dragend te zijn op een vloer |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75f0f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Vliesgevel | heeft relatie met | heeftRelatieMet | IFC | IfcCurtainWall |
| Vliesgevel | is specialisatie van |  | Bouwwerken | BouwComponent |
| Vliesgevel | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Vliesgevel | is specialisatie van |  | IFC | IfcCurtainWall |

#### Vloer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Vloer |
| Formele definitie | BouwComponent met de functie een RuimtelijkeBouwwerkComponent aan de bovenkant of de onderkant te begrenzen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | VloerPlaat |
| Begrip | vloer |
| Begripsdefinitie | constructie-element dat een ruimte verticaal kan omsluiten. |
| Bronterm | Vloer |
| Brondefinitie | constructie-element dat een ruimte verticaal kan omsluiten. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f75fdc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Vloer | heeft relatie met | heeftRelatieMet | IFC | IfcSlab |
| Vloer | is specialisatie van |  | Bouwwerken | BouwComponent |
| Vloer | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Vloer | is specialisatie van |  | MiniBIM | Element |
| Vloer | is specialisatie van |  | IFC | IfcSlab |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Vloer | is generalisatie van |  | MiniBIM | Balkonvloer |
| Vloer | is generalisatie van |  | MiniBIM | Begaanbare dakvloer |
| Vloer | is generalisatie van |  | MiniBIM | Constructieve vloer |
| Vloer | is generalisatie van |  | MiniBIM | Constructieve vloer |
| Vloer | is generalisatie van |  | MiniBIM | Dak |
| Vloer | is generalisatie van |  | MiniBIM | Dak |
| Vloer | is generalisatie van |  | Ketenstandaard-Ruimte | Dakvloer |
| Vloer | is generalisatie van |  | MiniBIM | Funderingsvloer |
| Vloer | is generalisatie van |  | MiniBIM | Galerijvloer |

#### Wand

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Wand |
| Formele definitie | (binnen bepaalde marges)verticale BouwComponent met de Functie scheiding van RuimtelijkeBouwwerkComponenten in een Bouwwerk of tussen binnen- en buitemruimte. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | wand |
| Begripsdefinitie | verticale constructie die ruimtes kan begrenzen of onderverdelen. |
| Bronterm | Wand |
| Brondefinitie | Een wand vertegenwoordigt een verticale constructie die ruimtes kan begrenzen of onderverdelen. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f7609f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Wand | heeft relatie met | heeftRelatieMet | IFC | IfcWall |
| Wand | is specialisatie van |  | Bouwwerken | BouwComponent |
| Wand | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Wand | is specialisatie van |  | NEN2660 | Discreet object |
| Wand | is specialisatie van |  | MiniBIM | Element |
| Wand | is specialisatie van |  | IFC | IfcWall |
| Wand | is specialisatie van |  | IFC | IfcWall |
| Wand | is specialisatie van |  | NEN2660 | Technische entiteit |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Wand | is generalisatie van |  | MiniBIM | Binnenspouwblad |
| Wand | is generalisatie van |  | MiniBIM | Binnenwand |
| Wand | is generalisatie van |  | MiniBIM | Constructieve wand |
| Wand | is generalisatie van |  | MiniBIM | Gevelwand |
| Wand | is generalisatie van |  | MiniBIM | Grijsdak |
| Wand | is generalisatie van |  | MiniBIM | Groendak |
| Wand | is generalisatie van |  | MiniBIM | Hellingbaan |
| Wand | is gerelateerd aan | representeert | BinnenRuimteNetwerk | Verbinding |

#### Zonwering

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Bouwcomponenten |
| Term | Zonwering |
| Formele definitie | BouwComponent  met de Functie beschermen tegen zonlicht, natuurlijk licht of beperken van het zicht. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | zonwering |
| Begripsdefinitie | elementen die beschermen tegen zonlicht, natuurlijk licht of om het zicht te beperken. |
| Bronterm | Zonwering |
| Brondefinitie | Zonweringselementen zijn speciaal ontworpen om te beschermen tegen zonlicht, natuurlijk licht of om het zicht te beperken. |
| Bron | [ILS O&E] |
| Eigenaar | digiGO |
| Identificatie | 98f76165-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Zonwering | is specialisatie van |  | Bouwwerken | BouwComponent |
| Zonwering | is specialisatie van |  | ILS-OenE | Bouwproduct |
| Zonwering | is specialisatie van |  | IFC | IfcShadingDevice |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Zonwering | is gerelateerd aan | heeftRelatieMet | IFC | IfcShadingDevice |

### Woonobjecten

#### Arbeidsmigranten

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Arbeidsmigranten |
| Formele definitie | Doelgroep |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f76345-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Arbeidsmigranten | is specialisatie van |  | Woonobjecten | Doelgroep |

#### Asielzoekers

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Asielzoekers |
| Formele definitie | Doelgroep |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f76402-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Asielzoekers | is specialisatie van |  | Woonobjecten | Doelgroep |

#### BedRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BedRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie Verblijven |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f764ed-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BedRuimte | heeft relatie met | heeftRelatieMet | Bbl | bedruimte |
| BedRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |
| BedRuimte | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### BenedenWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BenedenWoning |
| Formele definitie | MeergezinsWoning met toegang op de begane grond ofwel Verdieping 0. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f76611-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BenedenWoning | is specialisatie van |  | Woonobjecten | MeergezinsWoning |

#### BewonersInZorgInstelling

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BewonersInZorgInstelling |
| Formele definitie | Doelgroep |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7681f-755e-11f1-8f93-00ffdb61c323 |

#### BinnenRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BinnenRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent die volledig begrensd is door ReeleBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | binnenruimte |
| Begripsdefinitie | ruimte die aan alle zijden volledig wordt begrensd door bouwkundige scheidingsconstructies |
| Bronterm | binnenruimte |
| Brondefinitie | ruimte die aan alle zijden volledig wordt begrensd door bouwkundige scheidingsconstructies |
| Bron | [NEN 2580] |
| Eigenaar | NEN |
| Identificatie | 98f769e0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BinnenRuimte | is specialisatie van |  | Woonobjecten | WoonObjectRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BinnenRuimte | is generalisatie van |  | Woonobjecten | BedRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | FunctieRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | LegeRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | SanitaireRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | TechnischeRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | VerblijfsRuimte |
| BinnenRuimte | is generalisatie van |  | Woonobjecten | VerkeersRuimte |
| BinnenRuimte | is gerelateerd aan | representeert | BinnenRuimteNetwerk | Knoop |

#### BovenWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BovenWoning |
| Formele definitie | MeerginsWoning op een Verdieping , bereikbaar via een binnenTrap met een al dan niet gemeenschappelijke toegang. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f76b2e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BovenWoning | is specialisatie van |  | Woonobjecten | MeergezinsWoning |

#### BuitenRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | BuitenRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent die niet volledig begrensd is door ReeleBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | buitenruimte |
| Begripsdefinitie | ruimte die gedeeltelijk wordt begrensd door bouwkundige scheidingsconstructies |
| Bronterm | gebouwgebonden buitenruimte |
| Brondefinitie | ruimte die door het deels ontbreken van uitwensige bouwkundige scheidingsconstructies permamnent in open verbinding staan met de bodem en/of de buitenlucht |
| Bron | [NEN 2580] |
| Eigenaar | NEN |
| Identificatie | 98f76c60-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BuitenRuimte | is specialisatie van |  | Woonobjecten | WoonObjectRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Balkon |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Carport |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Dakterras |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Galerij |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Loggia |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Patio |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Terras |
| BuitenRuimte | is generalisatie van |  | Woonobjecten | Tuin |

#### Doelgroep

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Doelgroep |
| Formele definitie | type personen waar een WoonEenheid qua functionaliteit specifiek gericht is |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f76da9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Doelgroep | is generalisatie van |  | Woonobjecten | Arbeidsmigranten |
| Doelgroep | is generalisatie van |  | Woonobjecten | Asielzoekers |
| Doelgroep | is generalisatie van |  | Woonobjecten | BewonersInZorginstelling |
| Doelgroep | is generalisatie van |  | Woonobjecten | Studenten |
| Doelgroep | is generalisatie van |  | Woonobjecten | Woongroepen |
| Doelgroep | is gerelateerd aan | heeftDoelGroep | Woonobjecten | WoonEenhedenObject |
| Doelgroep | is gerelateerd aan | heeftDoelgroep | Woonobjecten | WoonEenheid |

#### EengezinsWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | EengezinsWoning |
| Formele definitie | Woning in een Pand zonder andere Verblijfsobjecten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | eengezinswoning |
| Begripsdefinitie | verblijfsobject (vbo) waarvan de gebruiksfunctie in de BAG tenminste een woonfunctie heeft (evt. naast nadere gebruiksfuncties), die ligt in een pand zonder andere vbo's |
| Bronterm | eengezinswoning |
| Brondefinitie | verblijfsobject (vbo) waarvan de gebruiksfunctie in de BAG tenminste een woonfunctie heeft (evt. naast nadere gebruiksfuncties), die ligt in een pand zonder andere vbo's |
| Bron | [CBS] |
| Eigenaar | CBS |
| Identificatie | 98f76f3b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| EengezinsWoning | is specialisatie van |  | Woonobjecten | Woning |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| EengezinsWoning | is generalisatie van |  | Woonobjecten | HoekWoning |
| EengezinsWoning | is generalisatie van |  | Woonobjecten | TussenWoning |
| EengezinsWoning | is generalisatie van |  | Woonobjecten | TweeOnderEenKapWoning |
| EengezinsWoning | is generalisatie van |  | Woonobjecten | VrijstaandeWoning |

#### FunctieRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | FunctieRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie opbergen en stallen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | BergRuimte |
| Begrip | functieRuimte |
| Begripsdefinitie | ruimte voor opbergen en stallen van goederen en voertuigen |
| Bronterm | functieruimte |
| Brondefinitie | In een functiegebied gelegen ruimte. Een functiegebied is een gebruiksgebied of een gedeelte daarvan, waar de voor die gebruiksfunctie kenmerkende activiteiten anders dan het verblijven van personen plaatsvinden; |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Identificatie | 98f771b1-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FunctieRuimte | heeft relatie met | heeftRelatieMet | Bbl | functieruimte |
| FunctieRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| FunctieRuimte | is generalisatie van |  | Woonobjecten | BergRuimte |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Bijkeuken |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | ExterneBergRuimte |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Fietsenstalling |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Garage |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Garagebox |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Kast |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | KelderRuimte |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Opstelplaats |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | ParkeerPlaats |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | Stalling |
| FunctieRuimte | is generalisatie van |  | Woonobjecten | WasRuimte |

#### GalerijWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | GalerijWoning |
| Formele definitie | MeergezinsWoning met toegang vanuit een galerij |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7739f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GalerijWoning | is specialisatie van |  | Woonobjecten | MeergezinsWoning |

#### HoekWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | HoekWoning |
| Formele definitie | Eengezinswoning in een Gebouw met drie of meer eengezinswoningen met precies één aangrenzende eengezinswoning |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | EindWoning |
| Identificatie | 98f774de-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| HoekWoning | is specialisatie van |  | Woonobjecten | EengezinsWoning |

#### Hoofdtoegang

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Hoofdtoegang |
| Formele definitie | <to do> |
| Identificatie | 98f776ae-755e-11f1-8f93-00ffdb61c323 |

#### LegeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | LegeRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie bieden van ruimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | lege ruimte |
| Begripsdefinitie | ruimte ten behoeve van doorgang of ruimte-ervaring |
| Identificatie | 98f77994-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| LegeRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| LegeRuimte | is generalisatie van |  | Woonobjecten | OnbenoemdeRuimte |
| LegeRuimte | is generalisatie van |  | Woonobjecten | Trapgat |
| LegeRuimte | is generalisatie van |  | Woonobjecten | Vide |
| LegeRuimte | is generalisatie van |  | Woonobjecten | Vide |
| LegeRuimte | is generalisatie van |  | Woonobjecten | ZolderRuimte |

#### Maisonnette

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Maisonnette |
| Formele definitie | MeergezinsWoning met meerdere Verdiepingen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f77b2e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Maisonnette | is specialisatie van |  | Woonobjecten | MeergezinsWoning |

#### MeergezinsWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | MeergezinsWoning |
| Formele definitie | Woning in een pand met minimaal één ander WoonOobject |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | Appartement |
| Identificatie | 98f77c70-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| MeergezinsWoning | is specialisatie van |  | Woonobjecten | Woning |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | BenedenWoning |
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | BovenWoning |
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | GalerijWoning |
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | Maisonnette |
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | PortiekWoning |
| MeergezinsWoning | is generalisatie van |  | Woonobjecten | WoningBovenBedrijfsruimte |

#### PortiekWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | PortiekWoning |
| Formele definitie | MeergezinsWoning met toegang vanuit een gemeenschappelijk afsluitbaar trappenhuis, een centrale hal of een gesloten portiek. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f77da8-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| PortiekWoning | is specialisatie van |  | Woonobjecten | MeergezinsWoning |

#### SanitaireRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | SanitaireRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie persoonlijke hygiëne |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | sanitaire ruimte |
| Begripsdefinitie | ruimte voor persoonlijke hygiëne |
| Identificatie | 98f77ee9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| SanitaireRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| SanitaireRuimte | is generalisatie van |  | Woonobjecten | BadRuimte |
| SanitaireRuimte | is generalisatie van |  | Woonobjecten | ToiletRuimte |

#### Studenten

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Studenten |
| Formele definitie | Doelgroep |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7806b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Studenten | is specialisatie van |  | Woonobjecten | Doelgroep |

#### TechnischeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | TechnischeRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie plaatsen van apparatuur, noodzakelijk voor het functioneren van het Bouwwerk |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | technische ruimte |
| Begripsdefinitie | ruimte voor het plaatsen van de apparatuur, noodzakelijk voor het functioneren van het bouwwerk, waartoe in ieder geval behoort een meterruimte, een liftmachineruimte en een stookruimte; |
| Bronterm | technische ruimte |
| Brondefinitie | ruimte voor het plaatsen van de apparatuur, noodzakelijk voor het functioneren van het bouwwerk, waartoe in ieder geval behoort een meterruimte, een liftmachineruimte en een stookruimte; |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Identificatie | 98f7819f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TechnischeRuimte | heeft relatie met | heeftRelatieMet | Bbl | technische ruimte |
| TechnischeRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | InstallatieRuimte |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | KruipRuimte |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | LiftmachineRuimte |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | Liftschacht |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | MeterRuimte |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | Schacht |
| TechnischeRuimte | is generalisatie van |  | Woonobjecten | StookRuimte |

#### Toegangspunt

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Toegangspunt |
| Formele definitie | <to do> |
| Identificatie | 98f782f8-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Toegangspunt | heeft relatie met | hoortBij | IMIBRO | PandOfVerblijfsobject |
| Toegangspunt | is specialisatie van |  | IMIBRO | FunctioneleRuimte |

#### TussenWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | TussenWoning |
| Formele definitie | Eengezinswoning in een Gebouw met drie of meer eengezinswoningen met twee aangrenzende eengezinswoningen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f78446-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TussenWoning | is specialisatie van |  | Woonobjecten | EengezinsWoning |

#### TweeOnderEenkapWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | TweeOnderEenkapWoning |
| Formele definitie | Eengezinswoning  in een Gebouw met twee eengezinswoningen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7862b-755e-11f1-8f93-00ffdb61c323 |

#### VerblijfsRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | VerblijfsRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie Verblijven van personen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | verblijfsruimte |
| Begripsdefinitie | ruimte voor het verblijven van personen |
| Bronterm | verblijfsruimte |
| Brondefinitie | Een in een verblijfsgebied gelegen ruimte voor het verblijven van personen. |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Identificatie | 98f78858-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerblijfsRuimte | heeft relatie met | heeftRelatieMet | Bbl | verblijfsruimte |
| VerblijfsRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Atrium |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | BedrijfsRuimte |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | BedRuimte |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Huiskamer |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | KantoorRuimte |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Keuken |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Serre |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Slaapkamer |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | Woonkamer |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | WoonkamerKeuken |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | WoonkamerKeukenSlaapkamer |
| VerblijfsRuimte | is generalisatie van |  | Woonobjecten | WoonSlaapkamer |

#### VerkeersRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | VerkeersRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent met de Functie zich verplaatsen tussen RuimtelijkeBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | verkeersruimte |
| Begripsdefinitie | ruimte voor het bereiken van een andere ruimte |
| Bronterm | verkeersruimte |
| Brondefinitie | ruimte voor het bereiken van een andere ruimte, die niet ligt in een verblijfsgebied of in een functiegebied, een toiletruimte, een badruimte of een technische ruimte; |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Identificatie | 98f78c65-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerkeersRuimte | heeft relatie met | heeftRelatieMet | Bbl | verkeersruimte |
| VerkeersRuimte | is specialisatie van |  | Woonobjecten | BinnenRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Corridor |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Entree |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Gang |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Hal |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Lift |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Lifthal |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Lifthal |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Overloop |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Rooksluis |
| VerkeersRuimte | is generalisatie van |  | Woonobjecten | Trappenhuis |

#### VrijstaandeWoning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | VrijstaandeWoning |
| Formele definitie | Eengezinswoning in een Gebouw zonder andere Panden |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | vrijstaande woning |
| Begripsdefinitie | eengezinswoning in een gebouw zonder andere panden |
| Bronterm | VrijstaandeWoning |
| Brondefinitie | Eengezinswoning die los staat van (eventueel) aanwezige andere objecten. |
| Bron | [IMIBRO] |
| Eigenaar | Geonovum |
| Identificatie | 98f78ea4-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VrijstaandeWoning | is specialisatie van |  | Woonobjecten | EengezinsWoning |

#### Woning

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Woning |
| Formele definitie | WoonObject met eigen toegang en woonvoorzieningen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woning |
| Begripsdefinitie | verblijfsobject met gebruiksdoel woonfunctie |
| Bronterm | Woning (BAG) |
| Brondefinitie | Alle verblijfsobjecten met minimaal een woonfunctie en eventueel een of meer andere gebruiksfuncties worden als woning aangemerkt. |
| Bron | [CBS] |
| Eigenaar | CBS |
| Identificatie | 98f793fc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Woning | is specialisatie van |  | MiniBIM | Bouwwerk |
| Woning | is specialisatie van |  | Woonobjecten | WoonObject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Woning | is generalisatie van |  | Woonobjecten | EengezinsWoning |
| Woning | is generalisatie van |  | Woonobjecten | MeergezinsWoning |

#### WoningBovenBedrijfsRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoningBovenBedrijfsRuimte |
| Formele definitie | MeergezinsWoning op een Verdieping boven een VerblijfsObject met industrie-, kantoor- of winkelfunctie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7bac8-755e-11f1-8f93-00ffdb61c323 |

#### WoonEenhedenObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonEenhedenObject |
| Formele definitie | WoonObject met WoonEenheden en een gemeenschappelijke RuimtelijkeBouwwerkComponent |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7bc9e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonEenhedenObject | heeft relatie met | heeftDoelGroep | Woonobjecten | Doelgroep |
| WoonEenhedenObject | heeft relatie met | bevat | Woonobjecten | WoonEenheid |
| WoonEenhedenObject | is specialisatie van |  | Woonobjecten | WoonObject |

#### WoonEenheid

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonEenheid |
| Formele definitie | afzonderlijk deel in een WoonObject, bestaande uit één of meer WoonObjectRuimten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | wooneenheid |
| Begripsdefinitie | onzelfstandige woonruimte |
| Bronterm | wooneenheid |
| Brondefinitie | gedeelte van een woonfunctie voor kamergewijze verhuur voor afzonderlijke bewoning; |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Bijzonderheden | zie ook de CBS-definitie: Een wooneenheid is een deel van een voor woondoeleinden bestemd (gebruiksdoel is woonfunctie) verblijfsobject van gebruik dat, vanuit bouwtechnisch oogpunt gezien, blijvend is bestemd voor permanente bewoning door een particulier huishouden en dat voldoet aan alle criteria die van toepassing zijn op woningen. |
| Identificatie | 98f7bd7f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonEenheid | heeft relatie met | heeftDoelgroep | Woonobjecten | Doelgroep |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonEenheid | is gerelateerd aan | bevat | Woonobjecten | WoonEenhedenObject |

#### WoonGebouw

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonGebouw |
| Formele definitie | Bouwwerk met de Functie  het bieden van ruimte aan en voorzienoingen voor WoonObjecten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woongebouw |
| Begripsdefinitie | Gebouw dat primair geschikt is voor woningen en/of wooneenheden |
| Bronterm | Woongebouw |
| Brondefinitie | Pand met een constructie die primair geschikt voor bewoning. |
| Bron | [IMIBRO] |
| Eigenaar | Geonovum |
| Identificatie | 98f7be8b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonGebouw | heeft relatie met | heeftRelatieMet | Bbl | woongebouw |
| WoonGebouw | is specialisatie van |  | Bouwwerken | Gebouw |

#### Woongroepen

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | Woongroepen |
| Formele definitie | Doelgroep |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7bf5f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Woongroepen | is specialisatie van |  | Woonobjecten | Doelgroep |

#### WoonObject

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonObject |
| Formele definitie | VerblijfsObject met de Functie wonen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woning |
| Begripsdefinitie | verblijfsobject met gebruiksdoel woonfunctie |
| Bronterm | Woning (BAG) |
| Brondefinitie | Alle verblijfsobjecten met minimaal een woonfunctie en eventueel een of meer andere gebruiksfuncties worden als woning aangemerkt. |
| Bron | [CBS] |
| Identificatie | 98f7c02d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObject | heeft relatie met | heeftRelatieMet | Bbl | woonfunctie |
| WoonObject | heeft relatie met | bevat | Woonobjecten | WoonObjectRuimte |
| WoonObject | is specialisatie van |  | TopModel | FunctioneleRuimte |
| WoonObject | is specialisatie van |  | IMBAG | Verblijfsobject |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObject | is generalisatie van |  | Woonobjecten | Woning |
| WoonObject | is generalisatie van |  | Woonobjecten | WoonEenhedenObject |
| WoonObject | is gerelateerd aan | bevat | Bouwwerken | Gebouw |

#### WoonObjectRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonObjectRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent in een Bouwwerk met de Functie wonen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7c0fe-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObjectRuimte | heeft relatie met |  | Woonobjecten | WoonObjectRuimte |
| WoonObjectRuimte | heeft relatie met | heeftInherenteFunctie | Woonobjecten | WoonObjectRuimteFunctie |
| WoonObjectRuimte | heeft relatie met | heeftFeitelijkeFunctie | Woonobjecten | WoonObjectRuimteFunctie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObjectRuimte | is generalisatie van |  | Woonobjecten | BinnenRuimte |
| WoonObjectRuimte | is generalisatie van |  | Woonobjecten | BuitenRuimte |
| WoonObjectRuimte | is gerelateerd aan | bevat | Woonobjecten | WoonObject |
| WoonObjectRuimte | is gerelateerd aan |  | Woonobjecten | WoonObjectRuimte |

#### WoonObjectRuimteFunctie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjecten |
| Term | WoonObjectRuimteFunctie |
| Formele definitie | Functie van een WoonObjectRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f7c1c3-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObjectRuimteFunctie | is specialisatie van |  | TopModel | Functie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonObjectRuimteFunctie | is gerelateerd aan | heeftInherenteFunctie | Woonobjecten | WoonObjectRuimte |
| WoonObjectRuimteFunctie | is gerelateerd aan | heeftFeitelijkeFunctie | Woonobjecten | WoonObjectRuimte |

### Woonobjectruimten

#### Atrium

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Atrium |
| Formele definitie | centraal in een Bouwwerk gelegen VerblijfsRuimte tot op Dakhoogte met de Functies licht, lucht, verbijven en zich verplaatsen tussen andere RuimtelijkeBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | atrium |
| Begripsdefinitie | centrale binnenruimte in een gebouw, tot op dakhoogte |
| Bronterm | Atrium |
| Brondefinitie | Een centrale binnenruimte in een gebouw, omgeven door meerdere verdiepingen, ontworpen om natuurlijk licht binnen te laten en een gevoel van openheid te creëren. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Zijn er niet twee typen atria: binnen en buiten? En eigenlijk is een binnen-atrium toch gewoon een vide? |
| Identificatie | 98f7c289-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Atrium | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### Badruimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Badruimte |
| Formele definitie | SanitaireRuimte met de Functie baden en/of douchen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | Badkamer |
| Begrip | badruimte |
| Begripsdefinitie | ruimte  voor het nemen van baden en douches, inclusief de daarvoor benodigde voorzieningen en installaties. |
| Bronterm | Badruimte |
| Brondefinitie | Een ruimte in een gebouw met sanitair voor het nemen van baden en douches, inclusief voorzieningen zoals een badkuip, douchebak, wastafel en toilet, vaak voorzien van waterdichte materialen en afvoersystemen. De term badruimte komt vanuit het bouwbesluit. In de volksmond wordt de ruimte op plattegronden meestal aangeduid als badkamer. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f7c368-755e-11f1-8f93-00ffdb61c323 |

#### Balkon

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Balkon |
| Formele definitie | ongelijkvloers uitgebouwde BuitenRuimte met de Functie verblijven. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | balkon |
| Begripsdefinitie | niet gelijkvloerse uitbouw van een vloer met borstwering aan de gevel van een gebouw, vanuit het gebouw toegankelijk, ten behoeve van verblijf |
| Brondefinitie | Open uitbouw die niet gelijkvloers aan de gevel is aangebracht en waarvan het bovenvlak vanuit het gebouw toegankelijk is. |
| Bron | [IMIBRO] |
| Eigenaar | Geonovum |
| Identificatie | 98f7c63b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Balkon | is specialisatie van |  | Woonobjecten | BuitenRuimte |
| Balkon | is specialisatie van |  | IMIBRO | Panddeel |

#### BedrijfsRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | BedrijfsRuimte |
| Formele definitie | VerblijfsRuimte met de Functie verkopen, produceren, dienstverlenen en/of zorgverlenen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bedrijfsruimte |
| Begripsdefinitie | ruimte voor verkoop, productie, dienstverlening en/of zorgverlening |
| Bronterm | Bedrijfsruimte |
| Brondefinitie | Een enkele ruimte binnen een gebouw die is ontworpen voor commerciële of zakelijke activiteiten, zoals winkels, zorgverlening, fabrieken of werkplaatsen, meestal voorzien van specifieke infrastructuur en voorzieningen voor de betreffende bedrijfsactiviteiten. Niet te verwarren met kantoorruimten. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f7c714-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BedrijfsRuimte | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### BergRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | BergRuimte |
| Formele definitie | FunctieRuimte met de Functie opslaan van goederen en gereedschappen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bergruimte |
| Begripsdefinitie | ruimte binnen de woning en/of met toegang vanuit de woning. Vaak gebruikt voor het opslaan van goederen, gereedschappen, of andere items. |
| Bronterm | Bergruimte |
| Brondefinitie | Een ruimte binnen de schil van een woning en/of met toegang vanuit de woning. Vaak gebruikt voor het opslaan van goederen, gereedschappen, of andere items, vaak voorzien van planken, rekken of kasten voor organisatie. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f7e4fd-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BergRuimte | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Bijkeuken

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Bijkeuken |
| Formele definitie | FunctieRuimte met de Functie opslaan van voorraad, schoonmaakartikelen, wasmachines, drogers en andere huishoudelijke apparaten. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | bijkeuken |
| Begripsdefinitie | ruimte naast de keuken, voor het opslaan van voorraad, schoonmaakartikelen, wasmachines, drogers en andere huishoudelijke apparaten. |
| Bronterm | Bijkeuken |
| Brondefinitie | Een (kleine) ruimte naast de keuken, vaak gebruikt voor het opslaan van voorraad, schoonmaakartikelen, wasmachines, drogers en andere huishoudelijke apparaten. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f7e702-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Bijkeuken | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Carport

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Carport |
| Formele definitie | aan de bovenkant reëel begrensde BuitenRuimte naast een Bouwwerk met de Functie parkeren van een of enkele auto's |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | carport |
| Begripsdefinitie | overdekte parkeerplaats naast of onder een gebouw. |
| Bronterm | Carport |
| Brondefinitie | Een overdekte structuur naast een gebouw, met één of meer open zijden, ontworpen om voertuigen te beschermen tegen weersinvloeden zoals regen, sneeuw en zon. In tegenstelling tot een garage heeft een carport meestal geen muren of deuren. Carports kunnen vrijstaand zijn of aan een gebouw bevestigd worden. Onder carport vallen ook ander soortige overdekte (buiten) parkeervakken, zoals die in de plint (begane grond) van een appartementencomplex. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f7e7e9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Carport | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### Corridor

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Corridor |
| Formele definitie | langwerpige VerkeersRuimte in een gemeenschappelijke ruimte die toegang verschaft tot meerdere WoonObjecten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | corridor |
| Begripsdefinitie | gang in een gemeenschappelijke ruimte die toegang verschaft tot meerdere woonobjecten |
| Bronterm | Corridor |
| Brondefinitie | Een gang in een gemeenschappelijke ruimte die toegang verschaft tot meerdere gebruiksfuncties. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f7e8cd-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Corridor | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### Dakterras

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Dakterras |
| Formele definitie | niet geheel overdekte BuitenRuimte op een Dak met de Functie verblijven |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | dakterras |
| Begripsdefinitie | niet geheel overdekte buitenruimte, gelegen op de dakconstructie van de onderliggende verdieping |
| Bronterm | Dakterras |
| Brondefinitie | Een niet-geheel-overdekte buitenruimte, gelegen op de dakconstructie van de onderliggende bouwlaag. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f7e9a7-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Dakterras | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### Entree

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Entree |
| Formele definitie | VerkeersRuimte tussen ToegangsPunt en een andere VerkeersRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | entree |
| Begripsdefinitie | ruimte tussen de toegang van een woning of wooneenhedengroep en een andere verkeersruimte. |
| Brondefinitie | Ruimte tussen de toegangsdeur en een verkeersruimte. Deze ruimte is van toepassing op een gebouw en op een gebruiksfunctie. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | (1) Het lijkt me dat er onderscheid gemaakt moet worden tussen GebouwEntree en VboEntree (WoonObjectEntree) (2) Wat doe je met een entree die direct in een verblijfsruimte uitkomt? Noem je dat een 'gang'? |
| Identificatie | 98f8041d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Entree | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### ExterneBergRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | ExterneBergRuimte |
| Formele definitie | FunctieRuimte met de Functie opslaan van goederen en gereedschappen buiten de WoonObjectRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | externe bergruimte |
| Begripsdefinitie | uimte buiten de woning, binnen of buiten het woongebouw  voor het opslaan van goederen, gereedschappen, fietsen, of andere items met geen toegang vanuit de woning. |
| Bronterm | Berging inpandig/ Berging uitpandig |
| Brondefinitie | Een ruimte buiten de schil van de woning, maar binnen een gebouw met ook andere functies. Vaak gebruikt voor het opslaan van goederen, gereedschappen, fietsen, of andere items, vaak voorzien van planken, rekken of kasten voor organisatie. Toegang niet vanuit de woning. Een berging in een ander gebouw, is dus ook inpandig. Niet bestemd voor technische installaties./ Een al dan niet afgesloten ruimte buiten het gebouw. Losstaand of in een cluster met enkel bergingen. Vaak gebruikt voor het opslaan van goederen, gereedschappen, fietsen, of andere items, vaak voorzien van planken, rekken of kasten voor organisatie. Niet bestemd voor technische installaties. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Nader  uit te zoeken |
| Identificatie | 98f80670-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ExterneBergRuimte | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Fietsenstalling

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Fietsenstalling |
| Formele definitie | FunctieRuimte met de Functie parkeren van fietsen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | fietsenstalling |
| Begripsdefinitie | ruimte binnen of buiten een gebouw voor het parkeren van fietsen. |
| Bronterm | Fietsenstalling inpandig/ Fietsenstalling uitpandig |
| Brondefinitie | Een ruimte binnen een gebouw die bedoeld is voor het parkeren van fietsen./ Een al dan niet overdekte of afgesloten ruimte buiten het gebouw die bedoeld is voor het parkeren van fietsen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f820f1-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Fietsenstalling | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Galerij

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Galerij |
| Formele definitie | ongelijkvloerse langwerpige BuitenRuimte tegen een Bouwwerk die als VerkeersRuimte toegang verschaft tot meerdere WoonObjecten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | galerij |
| Begripsdefinitie | aan de buitenkant van een gebouw hangende open gang, gebruikt als verbindingsroute tussen verschillende delen van het gebouw toegsng verschaffend tot afzonderlijke verblijfsobjecten |
| Bronterm | Galerij |
| Brondefinitie | Een aan de buitenkant van een gebouw hangende open gang, gebruikt als verbindingsroute tussen verschillende delen van het gebouw. Deze verschaft toegang tot afzonderlijke gebruiksfuncties. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f8224f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Galerij | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### Gang

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Gang |
| Formele definitie | langwerpige VerkeersRuimte tussen andere WoonObjectRuimten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | gang |
| Begripsdefinitie | Een langwerpige doorgangsruimte, gebruikt als verbindingsroute tussen verschillende ruimten. |
| Bronterm | Gang |
| Brondefinitie | Een doorgangsruimte met lengte- breedte verhouding van 1:n. Bevindt zich binnen een gebouw, gebruikt als verbindingsroute tussen verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang wordt verleend tot een gebruiksfunctie. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Deze ruimte bevat geen deur waarmee toegang wordt verleend tot een gebruiksfunctie.': begrijp ik niet |
| Identificatie | 98f82340-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Gang | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### Garage

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Garage |
| Formele definitie | reëel begrensde FunctieRuimte met de Functie parkeren |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | garage |
| Begripsdefinitie | een van een garagedeur voorziene ruimte in of buiten het woongebouw voor het parkeren van voertuigen. |
| Bronterm | Garage inpandig/ Garage uitpandig |
| Brondefinitie | Een inpandige garage is een garage die deel uitmaakt van een gebouw. Deze ruimte is meestal direct toegankelijk vanuit het interieur van het gebouw, bijvoorbeeld via een deur die leidt naar een gang, keuken, of bijkeuken. De garage is voorzien van een garagedeur die naar buiten opent. Een garage is gebonden aan een enkele woning, niet te verwarren met parkeergarage./ Een uitpandige garage is een garage die geen deel uitmaakt van het gebouw. Deze ruimte is niet direct toegankelijk vanuit het interieur van het gebouw. De uitpandige garage is via de oprijlaan van de woonruimte te bereiken en daarom betreft het een aanhorigheid van de woonruimte. De garage is voorzien van een garagedeur die naar buiten opent. Een garage is gebonden aan een enkele woning, niet te verwarren met parkeergarage. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Nader  uit te zoeken |
| Identificatie | 98f827fc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Garage | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Garagebox

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Garagebox |
| Formele definitie | FunctieRuimte met de Functies parkeren en opslaan van goederen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | garagebox |
| Begripsdefinitie | afgesloten, individuele ruimte bedoeld voor het stallen van een voertuig of het opslaan van goederen. |
| Bronterm | Garagebox |
| Brondefinitie | Een garagebox is een afgesloten, individuele ruimte bedoeld voor het stallen van een voertuig of het opslaan van goederen. Garageboxen zijn voorzien van een garagedeur die op slot kan, vaak een kanteldeur of een roldeur. Deze boxen kunnen losstaand zijn of deel uitmaken van een groter complex met meerdere garageboxen. Een garagebox is een afzonderlijk object van een woonruimte als het een vrijstaande garagebox is die middels een afzonderlijk terrein bereikbaar is of als het een garagebox is die in de plint (begane grond) van een appartementencomplex zit. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Bijzonderheden | Garageboxen zijn voorzien van een afsluitbare garagedeur. De box kan deel uitmaken van een groter complex met meerdere garageboxen. |
| Identificatie | 98f83edc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Garagebox | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Hal

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Hal |
| Formele definitie | (binnen bepaalde marges) even lange als brede VerkeersRuimte tussen andere WoonObjectRuimten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | hal |
| Begripsdefinitie | Een ongeveer even brede als lange doorgangsruimte tussen verschillende ruimten. |
| Bronterm | Hal |
| Brondefinitie | Een doorgangsruimte met een nagenoeg gelijke lengte- breedte verhouding. Bevindt zich binnen een gebouw, gebruikt als verbindingsroute tussen verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang wordt verleend tot een gebruiksfunctie |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Deze ruimte bevat geen deur waarmee toegang wordt verleend tot een gebruiksfunctie.': begrijp ik niet |
| Identificatie | 98f84052-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Hal | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### Huiskamer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Huiskamer |
| Formele definitie | VerblijfsRuimte in een WoonEenhedenObject met als Functies ontmoeten, sociaal samenzijn, ontspannen, bezoek ontvangen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | huiskamer |
| Begripsdefinitie | centrale gemeenschappelijke ruimte in een wooneenhedengroep ten behoeve van ontmoeten, sociaal samenzijn, ontspannen, bezoek ontvangen |
| Bronterm | Huiskamer |
| Brondefinitie | Een verblijfsruimte in een gemeenschappelijk verblijfsgebied, meestal in een woongebouw. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f8415c-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Huiskamer | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### InstallatieRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | InstallatieRuimte |
| Formele definitie | TechnischeRuimte met de Functie ruimte bieden aan Installaties |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f8424e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| InstallatieRuimte | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### KantoorRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | KantoorRuimte |
| Formele definitie | VerblijfsRuimte met de Functie administreren, zakelijk dienstverlenen en verwerken van informatie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | kantoorruimte |
| Begripsdefinitie | ruimte voor administraite, zakelijke dienstverlening en informatieverwerking. |
| Bronterm | Kantoorruimte |
| Brondefinitie | Een enkele ruimte binnen een gebouw die specifiek is ontworpen voor kantoorwerkzaamheden. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f84343-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| KantoorRuimte | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### Kast

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Kast |
| Formele definitie | ingebouwde FunctieRuimte, grenzend aan en toegankelijk vanuit  een BinnenRuimte met de Functie opbergen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | kast |
| Begripsdefinitie | Een opbergruimte, behorende tot de aangrenzende ruimte, onderdeel uitmakend van de bouwconstructie. |
| Bronterm | Kast |
| Brondefinitie | Een opbergruimte, behorende tot de aangrenzende ruimte, onderdeel uitmakend van de bouwconstructie. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f845f4-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Kast | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### KelderRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | KelderRuimte |
| Formele definitie | geheel of gedeeltelijk ondergrondse FunctieRuimte |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | kelder |
| Begripsdefinitie | Een (deels) ondergrondse ruimte onder de begane grond van een gebouw, meestal gebruikt voor opslag, nutsvoorzieningen, wasruimte en soms leefruimte. De toegang is via een trap of luik. In de kelder kan een volwassen persoon rechtop staan. |
| Bronterm | Kelder |
| Brondefinitie | Een (deels) ondergrondse ruimte onder de begane grond van een gebouw, meestal gebruikt voor opslag, nutsvoorzieningen, wasruimte en soms leefruimte. De toegang is via een trap of luik. In de kelder kan een volwassen persoon rechtop staan. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f847f9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| KelderRuimte | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Keuken

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Keuken |
| Formele definitie | VerblijfsRuimte met de Functie bereiden van voedsel |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | keuken |
| Begripsdefinitie | ruimte voor het bereiden van voedsel |
| Bronterm | Keuken |
| Brondefinitie | Een ruimte binnen een gebouw die is ontworpen en uitgerust voor het bereiden van voedsel, voorzien van een keukenblok. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f849f0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Keuken | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### Kruipruimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Kruipruimte |
| Formele definitie | ondiepe TechnischeRuimte onder de Vloer van een Bouwwerk met de Functie het leggen van leidingen, kabels en isolatie. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | kruipruimte |
| Begripsdefinitie | ondiepe ruimte onder de vloer van een gebouw. |
| Bronterm | Kruipruimte |
| Brondefinitie | Een kruipruimte is een ondiepe, vaak ongebruikte ruimte onder de vloer van een gebouw. De ruimte heeft een vrije hoogte van minder dan 1,5 meter (cf. NEN2580) en staat direct in verbinding met de buitenlucht of de bodem. Deze ruimte, die meestal hoog genoeg is om in te kruipen maar te laag om rechtop te staan, wordt gebruikt voor het leggen van leidingen, kabels en isolatie. Meestal is deze niet verwarmd. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Bijzonderheden | De ruimte heeft een vrije hoogte van minder dan 1,5 meter (cf. NEN2580) en staat direct in verbinding met de buitenlucht of de bodem. Deze ruimte, die meestal hoog genoeg is om in te kruipen maar te laag om rechtop te staan, wordt gebruikt voor het leggen van leidingen, kabels en isolatie. |
| Identificatie | 98f84bfa-755e-11f1-8f93-00ffdb61c323 |

#### Lift

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Lift |
| Formele definitie | mobiele Verkeersruimte in een cabine in een Schacht die personen of goederen tussen verschillende Verdiepingen in een Bouwwerk verplaatst. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | lift |
| Begripsdefinitie | ruimte in een cabine in een schacht die personen of goederen tussen verschillende verdiepingen in een bouwwerk verplaatst. |
| Bronterm | Lift |
| Brondefinitie | een hijs- of hefwerktuig dat bepaalde niveaus bedient met behulp van een drager die langs starre, ten opzichte van het horizontale vlak meer dan 15 graden hellende geleiders beweegt, of een hijs- of hefwerktuig dat een vaste, ten opzichte van het horizontale vlak meer dan 15 graden hellende baan volgt zelfs indien het niet langs starre geleiders beweegt; |
| Bron | [Bbl] |
| Eigenaar | MinVro |
| Identificatie | 98f84df3-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Lift | is specialisatie van |  | MiniBIM | Transport |
| Lift | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### Lifthal

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Lifthal |
| Formele definitie | VerkeersRuimte die vanuit een andere Verkeersruimte toegang geeft tot een Lift. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | lifthal |
| Begripsdefinitie | voorruimte die vanuit een verkeersruimte toegang geeft tot een lift. |
| Bronterm | Lifthal |
| Brondefinitie | Een voorruimte die vanuit een verkeersruimte toegang geeft tot een lift. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f85000-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Lifthal | is specialisatie van |  | Woonobjecten | VerkeersRuimte |
| Lifthal | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Lifthal | is gerelateerd aan | heeft | MiniBIM | Gebouw |

#### LiftmachineRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | LiftmachineRuimte |
| Formele definitie | TechnischeRuimte waarin de liftmachines, aandrijvingen, regelapparatuur en veiligheidsvoorzieningen zich bevinden, vaak gelegen boven of naast de liftschacht. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | liftmachineruimte |
| Begripsdefinitie | aparte ruimte binnen een gebouw waarin de liftmachines, aandrijvingen, regelapparatuur en veiligheidsvoorzieningen zich bevinden, vaak gelegen boven of naast de liftschacht. |
| Bronterm | Liftmachineruimte |
| Brondefinitie | Een aparte ruimte binnen een gebouw waarin de liftmachines, aandrijvingen, regelapparatuur en veiligheidsvoorzieningen zich bevinden, vaak gelegen boven of naast de liftschacht. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f851d9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| LiftmachineRuimte | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### Liftschacht

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Liftschacht |
| Formele definitie | langwerpige verticale TechnischeRuimte met de Functie ruimte bieden aan één of meer Liften. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | liftschacht |
| Begripsdefinitie | verticale ruimte binnen een bouwwerk, gebruikt voor  liften |
| Bronterm | Liftschacht |
| Brondefinitie | De ruimte in een bouwkundige liftschacht. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f853f0-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Liftschacht | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### Loggia

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Loggia |
| Formele definitie | ingebouwde BuitenRuimte met de Functie verblijven. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | loggia |
| Begripsdefinitie | aan twee of drie zijden gesloten vanuit het gebouw toegankelijke buitenruimte met borstwering die zich binnen het gevelvlak bevindt. |
| Bronterm | Loggia |
| Brondefinitie | Een loggia is een inpandig balkon: een aan drie zijden gesloten buitenruimte die zich binnen het gevelvlak bevindt. De opening bevindt zich in de gevel. De loggia heeft een borstwering. Meestal bevindt de loggia zich op de verdieping. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f856cc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Loggia | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### MeterRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | MeterRuimte |
| Formele definitie | TechnischeRuimte met de Functie ruimte bieden aan meters voor gas, elektriciteit, water, of andere nutsvoorzieningen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | meterruimte |
| Begripsdefinitie | ruimte waar meters voor gas, elektriciteit, water, of andere nutsvoorzieningen worden geïnstalleerd en onderhouden, meestal toegankelijk voor nutsbedrijven voor het aflezen en onderhouden van de meters. |
| Bronterm | Meterruimte |
| Brondefinitie | Een ruimte binnen een gebouw waar meters voor gas, elektriciteit, water, of andere nutsvoorzieningen worden geïnstalleerd en onderhouden, meestal toegankelijk voor nutsbedrijven voor het aflezen en onderhouden van de meters. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f858bd-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| MeterRuimte | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### OnbenoemdeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | OnbenoemdeRuimte |
| Formele definitie | LegeRuimte zonder benoemde Functie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | onbenoemde ruimte |
| Begripsdefinitie | Een ruimte zonder beoogd gebruik die bij de toets aan het BBL, de vergunningsaanvraag Omgevingsplantoets (OPA) of de aanvraag Technische Activiteit (WKB) buiten beschouwing dient te worden gelaten. |
| Bronterm | Onbenoemde ruimte |
| Brondefinitie | Een ruimte zonder beoogd gebruik die bij de toets aan het BBL, de vergunningsaanvraag Omgevingsplantoets (OPA) of de aanvraag Technische Activiteit (WKB) buiten beschouwing dient te worden gelaten. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f85aca-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| OnbenoemdeRuimte | is specialisatie van |  | Woonobjecten | LegeRuimte |

#### Opstelplaats

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Opstelplaats |
| Formele definitie | aan de onderkant reëel maar verder virtueel begrensde FunctieRuimte met de Functie opstellen van huishoudelijke apparaten. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | opstelplaats |
| Begripsdefinitie | aangewezen ruimte waar bepaalde installaties, apparatuur of objecten worden geplaatst, te specificeren naar specifieke huishoudelijke apparaten. |
| Bronterm | Opstelplaats |
| Brondefinitie | Een opstelplaats is de aangewezen ruimte waar bepaalde installaties, apparatuur of objecten worden geplaatst, opgesteld. Wordt verder gespecificeerd voor koelkast, kooktoestel, vaatwasser, wasdroger en wasmachine. Dit is voor onbepaalde tijd en kan dus ook zeer lang zijn. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f8606b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Opstelplaats | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Overloop

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Overloop |
| Formele definitie | VerkeersRuimte, die andere WoonObjectRuimten met bovenste trede van een Trap verbindt. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | overloop |
| Begripsdefinitie | ruimte die andere ruimtes met de bovenkant van een trap verbindt. |
| Bronterm | Overloop |
| Brondefinitie | Een overgangsgebied die ruimtes met een trap verbindt. Niet gelegen op de onderste bouwlaag van een adres. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f8614c-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Overloop | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### ParkeerPlaats

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | ParkeerPlaats |
| Formele definitie | aan de onderkant reëel maar verder virtueel begrensde FunctieRuimte met de Functie parkeren |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | parkeerplaats |
| Bronterm | Parkeerplaats |
| Brondefinitie | Een parkeerplaats is een specifiek aangewezen plek, waar voertuigen tijdelijk geparkeerd of gestald kunnen worden. Te specificeren voor auto, bakfiets, motorfiets en scootmobiel |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f8621a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ParkeerPlaats | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Patio

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Patio |
| Formele definitie | gedeeltelijk door Wanden begrensde BuitenRuimte bij een WoonObject. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | patio |
| Begripsdefinitie | ruimte buiten een woning of gebouw, gedeeltelijk begrensd door buitenwanden van die woning of dat gebouw. |
| Bronterm | Patio |
| Brondefinitie | Een open binnenplaats of verharde ruimte buiten een gebouw, omringd door muren. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f862ff-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Patio | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### Rooksluis

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Rooksluis |
| Formele definitie | VerkeersRuimte tussen Trappenhuis en een andere VerkeersRuimte met de Functie het rookvrij houden van het Trappenhuis |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | rooksluis |
| Begripsdefinitie | voorruimte die vanuit een verkeersruimte toegang geeft tot een trappenhuis met als doel het trappenhuis rookvrij te houden. |
| Bronterm | Rooksluis |
| Brondefinitie | Een voorruimte die vanuit een verkeersruimte toegang geeft tot een trappenhuis met als doel het trappenhuis rookvrij te houden. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f8648e-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Rooksluis | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

#### Schacht

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Schacht |
| Formele definitie | langwerpige verticale TechnischeRuimte met de Functie ventilatie en/of ruimte bieden aan bekabeling of leidingen. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | schacht |
| Begripsdefinitie | verticale doorgang of ruimte binnen een bouwwerk, gebruikt voor ventilatie, bekabeling of leidingen. |
| Bronterm | Schacht |
| Brondefinitie | Een verticale doorgang of ruimte binnen een gebouw, gebruikt voor ventilatie, bekabeling of leidingen vaak voorzien van brandwerende materialen en afsluitingen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Bijzonderheden | Vaak voorzien van brandwerende materialen en afsluitingen. |
| Identificatie | 98f865e9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Schacht | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### Serre

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Serre |
| Formele definitie | VerblijfsRuimte, grotendeel bestaande uit beweegbare glazen ReeleBouwComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | serre |
| Begripsdefinitie | verblijfsruimte, die grotendeel bestaat uit beweegbare glazen afscheidingsconstructies van de buitenruimte. |
| Bronterm | Serre |
| Brondefinitie | Een serre is een verwarmde binnenruimte die als (semi) buitenruimte gebruikt kan worden en valt binnen de GO. Niet te verwarren met een loggia, dat is een onverwarmde verglaasde buitenruimte. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f87ffc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Serre | is specialisatie van |  | IMIBRO | Panddeel |
| Serre | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### Slaapkamer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Slaapkamer |
| Formele definitie | VerblijfsRuimte met de Functie slapen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | slaapkamer |
| Begripsdefinitie | ruimte om te slapen |
| Bronterm | Slaapkamer |
| Brondefinitie | Een ruimte binnen een gebouw die is ontworpen en bestemd voor slapen. Niet te verwarren met een bedruimte. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f881d9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Slaapkamer | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### Stalling

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Stalling |
| Formele definitie | FunctieRuimte met de Functie parkeren van gemotoriseerde voertuigen, niet zijnde auto's. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | stalling |
| Begripsdefinitie | afgesloten ruimte binnen of buiten het gebouw  voor het parkeren of opslaan van gemotoriseerde (vaak elektrische) voertuigen, niet zijnde auto's, zoals scootmobielen, scooters of elektrische fietsen |
| Bronterm | Stalling inpandig/ Stalling uitpandig |
| Brondefinitie | Een afgesloten ruimte binnen een gebouw die bedoeld is voor het parkeren of opslaan van gemotoriseerde (vaak elektrische) voertuigen, niet zijnde auto's. Bijvoorbeeld scootmobielen, scooters of elektrische fietsen./ Een al dan niet overdekte of afgesloten ruimte buiten het gebouw die bedoeld is voor het parkeren of opslaan van gemotoriseerde (vaak elektrische) voertuigen, niet zijnde auto's. Bijvoorbeeld scootmobielen, scooters of elektrische fietsen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f88340-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Stalling | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### StookRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | StookRuimte |
| Formele definitie | InstallatieRuimte voor een StookInstallatie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f884c6-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| StookRuimte | is specialisatie van |  | Woonobjecten | TechnischeRuimte |

#### Terras

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Terras |
| Formele definitie | niet geheel overdekte BuitenRuimte op de begane grond met de Functie verblijven |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | terras |
| Begripsdefinitie | niet geheel overdekte gelijkvloers gelegen buitenruimte bij een woning of woongebouw |
| Bronterm | Terras |
| Brondefinitie | Een aan de woning verbonden bestrate buitenruimte met directe verbinding met de bomen. Gelegen binnen de bouwconstructie zonder overstek, en dat zich op de onderste woonlaag van de eenheid bevindt. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f88619-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Terras | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### ToiletRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | ToiletRuimte |
| Formele definitie | SanitaireRuimte met de Functie het faciliteren van persoonlijke verzorging en het afvoeren van de daarbij vrijgekomen stoffen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | toiletruimte |
| Begripsdefinitie | Een ruimte binnen een gebouw waarin toiletten en wastafels zijn geïnstalleerd, bedoeld voor persoonlijke hygiëne, vaak voorzien van sanitair, ventilatie, en sanitaire voorzieningen. |
| Bronterm | Toiletruimte |
| Brondefinitie | Een ruimte binnen een gebouw waarin toiletten en wastafels zijn geïnstalleerd, bedoeld voor persoonlijke hygiëne, vaak voorzien van sanitair, ventilatie, en sanitaire voorzieningen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f8877d-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ToiletRuimte | is specialisatie van |  | Woonobjecten | SanitaireRuimte |

#### Trapgat

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Trapgat |
| Formele definitie | LegeRuimte tussen de ruimte voor een Trap en de Vide daarboven. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | trapgat |
| Begripsdefinitie | Open ruimte in de verdiepingsvloer, bestemd om een trap te plaatsen. |
| Bronterm | Trapgat |
| Brondefinitie | Open ruimte in de verdiepingsvloer, bestemd om een trap te plaatsen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Commentaar | Nader bekijken: een trapgat lijkt meer op een sparing (IfcOpeningElement) dan op een Woonobjectruimte |
| Identificatie | 98f888dd-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Trapgat | is specialisatie van |  | Woonobjecten | LegeRuimte |

#### Trappenhuis

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Trappenhuis |
| Formele definitie | VerkeersRuimte met Trappen en evntueel ook Liften met de Functie verplaatsen van personen en goederen tussen Verdiepingen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | trappenhuis |
| Begripsdefinitie | verkeersruimte met trappen en eventueel ook liften voor het verplaatsen van personen en goederen tussen verdiepingen |
| Bronterm | Trappenhuis |
| Brondefinitie | Een verticale doorgangsruimte binnen een gebouw die wordt gebruikt om tussen verschillende verdiepingen te reizen, voorzien van een trap of trappen en vaak ook een lift, met veiligheidsvoorzieningen en nooduitgangen. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f88a28-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Trappenhuis | is specialisatie van |  | Woonobjecten | VerkeersRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Trappenhuis | is gerelateerd aan | heeft | MiniBIM | Gebouw |

#### Tuin

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Tuin |
| Formele definitie | BuitenRuimte bij een WoonObject buiten de reële begrenzing van het Bouwwerk met de Functie verblijven |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | tuin |
| Begripsdefinitie | buitenruimte buiten de gevelconstructie, bedoeld voor recreatie, tuinieren, sociale activiteiten en visuele esthetiek. |
| Bronterm | Tuin |
| Brondefinitie | Een buitenruimte buiten de gevelconstructie, vaak aangelegd met planten, gazon, bestrating en/of andere landschapskenmerken, bedoeld voor recreatie, tuinieren, sociale activiteiten en visuele esthetiek. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f88b88-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Tuin | is specialisatie van |  | Woonobjecten | BuitenRuimte |

#### Vide

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Vide |
| Formele definitie | LegeRuimte ter hoogte van minimaal één Verdieping op een ruimte zonder reële begrenzing eronder met de Functie ruimtelijke ervaring |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | vide |
| Begripsdefinitie | open ruimte binnen een gebouw, zonder fysieke afscheiding met de bouwlaag eronder |
| Bronterm | Vide |
| Brondefinitie | Een open ruimte binnen een gebouw, zonder fysieke afscheiding met de bouwlaag eronder. Bestemd om een een ruimtelijk gevoel te creeren. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f88ce9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Vide | is specialisatie van |  | Woonobjecten | LegeRuimte |
| Vide | is specialisatie van |  | Woonobjecten | LegeRuimte |

#### WasRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | WasRuimte |
| Formele definitie | FunctieRuimte met de Functie wassen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | wasruimte |
| Begripsdefinitie | ruimte binnen een gebouw ten behoeve van het wassen van kleding met de daarvoor benodigde voorzieningen. |
| Bronterm | Wasruimte |
| Brondefinitie | Een ruimte binnen een gebouw, specifiek bestemd voor wasmachines, drogers en andere apparaten voor wasgoed , voorzien van wateraansluitingen, afvoer en ventilatie. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f88e3f-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WasRuimte | is specialisatie van |  | Woonobjecten | FunctieRuimte |

#### Woonkamer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | Woonkamer |
| Formele definitie | VerblijfsRuimte in een Woning met als Functies ontmoeten, sociaal samenzijn, ontspannen, bezoek ontvangen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woonkamer |
| Begripsdefinitie | centrale ruimte in een woning ten behoeve van ontmoeten, sociaal samenzijn, ontspannen, bezoek ontvangen |
| Bronterm | Woonkamer |
| Brondefinitie | Een centrale ruimte binnen een woning, meestal gebruikt voor ontspanning, entertainment en sociale activiteiten, ingericht met zitplaatsen, meubels, elektronica en decoratieve elementen, vaak verbonden met andere delen van de woning zoals de eetkamer en keuken. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f88fb7-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Woonkamer | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### WoonkamerKeuken

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | WoonkamerKeuken |
| Formele definitie | VerblijfsRuimte met de Functies van Woonkamer en Keuken gecombineerd. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woonkamer-keuken |
| Begripsdefinitie | ruimte met een gecombineerde functie van keuken en woonkamer. |
| Bronterm | Woonkamer-keuken |
| Brondefinitie | Ruimte met een gecombineerde functie van keuken en woonkamer. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f890a7-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonkamerKeuken | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### WoonkamerKeukenSlaapkamer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | WoonkamerKeukenSlaapkamer |
| Formele definitie | VerblijfsRuimte met de Functies van Keuken en Slaapkamer gecombineerd. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woonkamer-keuken-slaapkamer |
| Begripsdefinitie | ruimte met een gecombineerde functie van keuken, woonkamer en slaapkamer |
| Bronterm | Woonkamer-keuken-slaapkamer |
| Brondefinitie | Ruimte met een gecombineerde functie van keuken, woonkamer en slaapkamer. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f89180-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonkamerKeukenSlaapkamer | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### WoonSlaapkamer

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | WoonSlaapkamer |
| Formele definitie | VerblijfsRuimte met de Functies van Woonkamer en Slaapkamer gecombineerd. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | woon-slaapkamer |
| Begripsdefinitie | ruimte met een gecombineerde functie van woonkamer en slaapkamer. |
| Bronterm | woon-slaapkamer |
| Brondefinitie | Ruimte met een gecombineerde functie van woonkamer en slaapkamer. |
| Bron | [MiniBIM] |
| Eigenaar | Neprom |
| Identificatie | 98f89750-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WoonSlaapkamer | is specialisatie van |  | Woonobjecten | VerblijfsRuimte |

#### ZolderRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Woonobjectruimten |
| Term | ZolderRuimte |
| Formele definitie | LegeRuimte, direct gelegen onder het Dak. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | zolderruimte |
| Begripsdefinitie | Een toegankelijke ruimte binnen een gebouw, direct gelegen onder het dak. |
| Bronterm | Zolderruimte |
| Brondefinitie | Een toegankelijke ruimte binnen een gebouw, direct gelegen onder het dak. |
| Bron | [ILS-woco] |
| Eigenaar | Aedes |
| Identificatie | 98f89838-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ZolderRuimte | is specialisatie van |  | Woonobjecten | LegeRuimte |

### Installaties

#### AfvoerInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | AfvoerInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie afvoeren van vloeistoffen en vaste stoffen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | afvoerinstallatie |
| Begripsdefinitie | Installatie ten behoeve van het afvoeren van vloeistoffen en vaste stoffen |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Afvoeren |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f89902-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| AfvoerInstallatie | is specialisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |

#### AssetManagementInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | AssetManagementInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie besturen, signaliseren en monitoren van een Bouwwerk. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | assetmanagementsysteem |
| Begripsdefinitie | Installatie ten behoeve van besturen, signaliseren en monitoren van een bouwwerk. |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Asset Management Systeem |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f89b90-755e-11f1-8f93-00ffdb61c323 |

#### BeveiligingsInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | BeveiligingsInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie voorzien in veiigheid |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | beveiligingsinstallatie |
| Begripsdefinitie | Installatie ten behoeve van het voorzien in veiigheid |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Beveiliging |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f89c59-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BeveiligingsInstallatie | is specialisatie van |  | Installaties | ElektrotechnischeInstallatie |

#### BrandveiligheidsInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | BrandveiligheidsInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie brandbestrijding |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | brandveiligheidsinstallatie |
| Begripsdefinitie | Installatie ten behoeve van brandbestrijding |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Werktuigkundige brandveiligheid |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f89d16-755e-11f1-8f93-00ffdb61c323 |

#### CommunicatieInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | CommunicatieInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie voorzien in informatieoverdracht |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | communicatieinstallatie |
| Begripsdefinitie | Installatie ten behoeven van informatieoverdracht |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Communicatie |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f89f8a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| CommunicatieInstallatie | is specialisatie van |  | Installaties | ElektrotechnischeInstallatie |

#### ElektrotechnischeInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | ElektrotechnischeInstallatie |
| Formele definitie | elektrotechnische Installatie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | elektrotechnische installatie |
| Begripsdefinitie | elektrotechnische installatie |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a043-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ElektrotechnischeInstallatie | heeft relatie met | heeftRelatieMet | NL-SfB | Elektrotechnische installatie |
| ElektrotechnischeInstallatie | is specialisatie van |  | Installaties | Installatie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | AssetManagemetnInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | BeveiligingsInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | CommunicatieInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | EnergieVoorzieningsInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | GebouwManagementInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | TransportInstallatie |
| ElektrotechnischeInstallatie | is generalisatie van |  | Installaties | VerlichtingsInstallatie |

#### EnergievoorzieningInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | EnergievoorzieningInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie voorzien in energie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | energievoorzieninginstallatie |
| Begripsdefinitie | Installatie ten behoeve van de energievoorziening |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Energievoorziening gebruikersaansluitingen |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a0f8-755e-11f1-8f93-00ffdb61c323 |

#### GasDistribuitieInstalltie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | GasDistribuitieInstalltie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie distribueren van gassen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | gasdistributie-installtie |
| Begripsdefinitie | Installatie ten behoeve van de distributie van gassen |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Gassen |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a35b-755e-11f1-8f93-00ffdb61c323 |

#### GebouwManagementInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | GebouwManagementInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie beheren van bouwwerkfunctionaliteiten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | gebouwmanagementsysteem |
| Begripsdefinitie | Installatie ten behoeve van het beheren van bouwwerkfunctionaliteiten |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Gebouw management systeem |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a412-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GebouwManagementInstallatie | is specialisatie van |  | Installaties | ElektrotechnischeInstallatie |

#### Installatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | Installatie |
| Formele definitie | elektromechanische BouwwerkComponent met een voor het functioneren van een Bouwwerk of BouwwerkComponent noodzakelijke Functie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Synoniemen | BouwwerkInstallatie |
| Begrip | installatie |
| Begripsdefinitie | voor het functioneren van een bouwwerk of een gedeelte daarvan noodzakelijke voorziening van niet-bouwkundige aard |
| Bronterm | Bouwwerkinstallatie |
| Brondefinitie | voor het functioneren van een bouwwerk of een gedeelte daarvan noodzakelijke voorziening van niet-bouwkundige aard |
| Bron | [Bbl] |
| Eigenaar | minBZK |
| Identificatie | 98f8a63b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Installatie | heeft relatie met | bestaatUit | GIR | Component |
| Installatie | heeft relatie met | heeftLocatie | TopModel | GeoObject |
| Installatie | heeft relatie met | heeftRelatieMet | IFC | IfcDistributionSystem |
| Installatie | heeft relatie met | heeftRelatieMet | GIR | Installatie |
| Installatie | heeft relatie met | localiseert | GIR | Locatie |
| Installatie | heeft relatie met | sluitAanOp | Installaties | NutsAansluiting |
| Installatie | heeft relatie met | ligtIn | IMBAG | Verblijfsobject |
| Installatie | is specialisatie van |  | IMWO00 | Element |
| Installatie | is specialisatie van |  | NL-SfB | Functioneel gebouwelement |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Installatie | is generalisatie van |  | Installaties | ElektrotechnischeInstallatie |
| Installatie | is generalisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |
| Installatie | is gerelateerd aan | isDeelVan | GIR | Component |
| Installatie | is gerelateerd aan | heeftRelatieMet | Installaties | Installatie |
| Installatie | is gerelateerd aan | isOnderdeelVan | Bouwwerken | InstallatieComponent |
| Installatie | is gerelateerd aan | aggregeertTot | IMWO00 | Voorziening |

#### KoelInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | KoelInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie koelen van RuimtelijkeBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | koelinstallatie |
| Begripsdefinitie | Installatie met de Functie van RuimtelijkeBouwwerkComponenten |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Koeling |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a739-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| KoelInstallatie | is specialisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |

#### LuchtbehandelingsInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | LuchtbehandelingsInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie ventilatie van RuimtelijkeBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | luchtbehandelingsinstallatie |
| Begripsdefinitie | Installatie ten behoeva van ventilatie |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Luchtbehandeling |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8a960-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| LuchtbehandelingsInstallatie | is specialisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |

#### MeetEnRegelinstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | MeetEnRegelinstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie meten en regelen ten behoeve van het functioneren van Installaties |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | meet- en regelinstallatie |
| Begripsdefinitie | Installatie voor het meten en regelen ten behoeve van het functioneren van andere bouwwerkinstallties |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Meet- en regelinstallaties |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8aa0b-755e-11f1-8f93-00ffdb61c323 |

#### NutsAansluiting

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | NutsAansluiting |
| Formele definitie | fysieke verbinding tussen een NutsSysteem en een WoonObject |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | nutsaansluiting |
| Begripsdefinitie | fysieke verbinding tussen het distributienetwerk van nutsbedrijven en een woning |
| Identificatie | 98f8ac1a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| NutsAansluiting | heeft relatie met | sluitAanOp | Installaties | NutsSysteem |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| NutsAansluiting | is gerelateerd aan | sluitAanOp | Installaties | Installatie |
| NutsAansluiting | is gerelateerd aan | heeftAansluiting | IMBAG | Verblijfsobject |

#### NutsSysteem

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | NutsSysteem |
| Formele definitie | distributienetwerk van een Nutsbedrijf |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | nutssysteem |
| Begripsdefinitie | distributienetwerk van een Nutsbedrijf |
| Identificatie | 98f8ace9-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| NutsSysteem | is gerelateerd aan | sluitAanOp | Installaties | NutsAansluiting |

#### TransportInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | TransportInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie horizontaal, verticaal en diagonaal transport van mensen, dieren en goederen |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | transportinstallatie |
| Begripsdefinitie | Installatie ten behoeve van horizontaal, verticaal en diagonaal transport van mensen, dieren en goederen |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Transport |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8adaa-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| TransportInstallatie | is specialisatie van |  | Installaties | ElektrotechnischeInstallatie |

#### VerlichtingsInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | VerlichtingsInstallatie |
| Formele definitie | ElektrotechnischeInstallatie met de Functie verlichting |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | verlichtingsinstallatie |
| Begripsdefinitie | Installatie en behoeve van verlichting |
| Bronterm | INSTALLATIES ELEKTROTECHNISCH: Verlichting |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8b01b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerlichtingsInstallatie | is specialisatie van |  | Installaties | ElektrotechnischeInstallatie |

#### VerwarmingsInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | VerwarmingsInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie verwarming van RuimtelijkeBouwwerkComponenten |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | verwarmingsInstallatie |
| Begripsdefinitie | Installatie ten behoeve van de verwarming van ruimten in een bouwwerk |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Verwarming |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8b0d6-755e-11f1-8f93-00ffdb61c323 |

#### WaterInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | WaterInstallatie |
| Formele definitie | WerktuigbouwkundigeInstallatie met de Functie toevoer en behandeling van water |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | waterInstallatie |
| Begripsdefinitie | Installatie voor toevoer en behandeling van water |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG: Water |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8b308-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WaterInstallatie | is specialisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |
| WaterInstallatie | is specialisatie van |  | Installaties | WerktuigbouwkundigeInstallatie |

#### WerktuigbouwkundigeInstallatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Installaties |
| Term | WerktuigbouwkundigeInstallatie |
| Formele definitie | werktuigbouwkundige Installatie |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | werktuigbouwkundige Installatie |
| Begripsdefinitie | werktuigbouwkundige installatie |
| Bronterm | INSTALLATIES WERKTUIGBOUWKUNDIG |
| Bron | [NL/SfB] |
| Eigenaar | Ketenstandaard |
| Bijzonderheden | In NL/SfB zijn alleen installaties op één spcificatieniveau lager gedefinieerd |
| Identificatie | 98f8b3f1-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WerktuigbouwkundigeInstallatie | heeft relatie met | heeftRelatieMet | NL-SfB | Werktuigbouwkundige installatie |
| WerktuigbouwkundigeInstallatie | is specialisatie van |  | Installaties | Installatie |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | AfvoerInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | BrandVeiligheidsInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | GasDistributieInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | KoelInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | LuchtbehandelingsInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | MeetEnRegelInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | VerwarmingsInstalltie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | VerwarmingsInstalltie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | WaterInstallatie |
| WerktuigbouwkundigeInstallatie | is generalisatie van |  | Installaties | WaterInstallatie |

### Slimme woning

#### Activering

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | Activering |
| Formele definitie | fysieke Activiteit ter beheersing van een BouwwerkComponentToestand |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | activering |
| Begripsdefinitie | fysieke actie van een actuator ter aanpassing van de toestand in een ruimte of bouwcomponent |
| Bronterm | Actuation |
| Brondefinitie | A saref:Actuation is the act of carrying out a procedure to control the state of the world using an actuator. It links to an actuator to describe what made the actuation, and to the controlled feature, property, property of interest, state, or state of interest. Typically, its input is a property value or a state. An actuation of a state (OP saref:controls) should have a state as input (OP saref:hasInput). Respectively, an actuation of a property should have a property value as input. |
| Bron | [SAREF] |
| Eigenaar | SAREF |
| Voorbeelden | pomp opstarten |
| Identificatie | 98f8b62c-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Activering | heeft relatie met | heeftRelatieMet | TopModel | Activiteit |
| Activering | heeft relatie met | beheerst | SlimmeWoning | BouwwerkComponentToestand |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Activering | is gerelateerd aan | realiseert | SlimmeWoning | Actuator |

#### Actuator

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | Actuator |
| Formele definitie | Apparaat met de Functie het tot stan brengen van een Activering op basis van een input en regels. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | actuator |
| Begripsdefinitie | apparaat dat activeringen realiseert op basis van input en regels |
| Bronterm | Actuator |
| Brondefinitie | A device designed to control one or more properties or states of one or more features of interest. |
| Bron | [SAREF] |
| Eigenaar | SAREF |
| Identificatie | 98f8ba38-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Actuator | heeft relatie met | realiseert | SlimmeWoning | Activering |
| Actuator | heeft relatie met | madeExecution | SAREF | Actuation |
| Actuator | is specialisatie van |  | SlimmeWoning | Apparaat |
| Actuator | is specialisatie van |  | SAREF | Device |

#### Apparaat

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | Apparaat |
| Formele definitie | technisch FysiekObject met specifieke Functies |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | apparaat |
| Begripsdefinitie | technisch fysiek object om specifieke taken uit te voeren |
| Bronterm | device |
| Brondefinitie | A tangible object designed to accomplish a particular task. In order to accomplish this task, the device performs one or more functions. An instance of saref:Device represents one specific real world entity. |
| Bron | [SAREF] |
| Eigenaar | SAREF |
| Identificatie | 98f8befa-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Apparaat | heeft relatie met | heeftRelatieMet | SAREF | Device |
| Apparaat | is specialisatie van |  | Bouwwerken | InstallatieComponent |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Apparaat | is generalisatie van |  | SlimmeWoning | Actuator |
| Apparaat | is generalisatie van |  | SlimmeWoning | Sensor |

#### BouwwerkComponentToestand

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | BouwwerkComponentToestand |
| Formele definitie | fysieke Toestand van een BouwwerkComponent |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | fysieke toestand |
| Identificatie | 98f8c13a-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponentToestand | is specialisatie van |  | TopModel | Toestand |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| BouwwerkComponentToestand | is gerelateerd aan | beheerst | SlimmeWoning | Activering |
| BouwwerkComponentToestand | is gerelateerd aan | heeft | Bouwwerken | BouwwerkComponent |
| BouwwerkComponentToestand | is gerelateerd aan | observeert | SlimmeWoning | Observatie |

#### Observatie

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | Observatie |
| Formele definitie | Activiteit van een Sensor die resulteert in een schatting of berekening van een BouwwerkComponentToestand. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | observatie |
| Begripsdefinitie | activiteit van een Sensor die resulteert in een schatting of berekening van een de toestand in een ruimte of bouwcomponent |
| Bronterm | Observation |
| Brondefinitie | A saref:Observation is the act of carrying out a procedure to estimate or calculate a value of a property of a feature of interest, or a state of a feature of interest. It links to a sensor to describe what made the observation, and to the observed feature, property, property of interest, state, or state of interest. Typically, its result is a property value or a state. An observation of a state (OP saref:observes) should have a state as a result (OP saref:hasResult). Respectively, an observation of a property should have a property value as a result. |
| Bron | [SAREF] |
| Eigenaar | SAREF |
| Identificatie | 98f8c1f2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Observatie | heeft relatie met | heeftRelatieMet | TopModel | Activiteit |
| Observatie | heeft relatie met | observeert | SlimmeWoning | BouwwerkComponentToestand |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Observatie | is gerelateerd aan | realiseert | SlimmeWoning | Sensor |

#### Sensor

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Slimme woning |
| Term | Sensor |
| Formele definitie | Apparaat met de Functie het realiseren van een Observatie op basis van een input en vertaling daarvan. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Begrip | sensor |
| Begripsdefinitie | apparaat dat is ontworpen om een of meer eigenschappen of toestanden van een of meer kenmerken van belang te observeren en te meten. |
| Bronterm | Sensor |
| Brondefinitie | A device designed to observe and measure one or more properties or states of one or more features of interest. |
| Bron | [SAREF] |
| Eigenaar | SAREF |
| Identificatie | 98f8dfdc-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Sensor | heeft relatie met | realiseert | SlimmeWoning | Observatie |
| Sensor | heeft relatie met | madeExecution | SAREF | Observation |
| Sensor | is specialisatie van |  | SlimmeWoning | Apparaat |
| Sensor | is specialisatie van |  | SAREF | Device |

### Juridische objecten

#### GemeenschappelijkeRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Juridische objecten |
| Term | GemeenschappelijkeRuimte |
| Formele definitie | … |
| Identificatie | 98f92a49-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| GemeenschappelijkeRuimte | is specialisatie van |  | Bouwwerken | RuimtelijkeBouwwerkComponent |

#### PrivéRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Juridische objecten |
| Term | PrivéRuimte |
| Formele definitie | RuimtelijkeBouwwerkComponent,beschikbaar voor uitsluitend gebruik van de eigenaar van het betreffende AppartementsRecht. |
| Bron | IMWO |
| Eigenaar | digiGO |
| Identificatie | 98f8e2cf-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| PrivéRuimte | is specialisatie van |  | Bouwwerken | RuimtelijkeBouwwerkComponent |

### Binnenruimtenetwerk

#### Deurvlak

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Binnenruimtenetwerk |
| Term | Deurvlak |
| Identificatie | 98f92ce4-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Deurvlak | heeft relatie met | isDeelVan | BouwComponenten | Deur |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Deurvlak | is gerelateerd aan | representeert | BinnenRuimteNetwerk | Verbinding |

#### Knoop

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Binnenruimtenetwerk |
| Term | Knoop |
| Identificatie | 98f92ff2-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Knoop | heeft relatie met | representeert | Woonobjecten | BinnenRuimte |
| Knoop | heeft relatie met | representeert | BinnenRuimteNetwerk | VerbindingsRuimte |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Knoop | is gerelateerd aan | van | BinnenRuimteNetwerk | Verbinding |
| Knoop | is gerelateerd aan | naar | BinnenRuimteNetwerk | Verbinding |

#### Verbinding

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Binnenruimtenetwerk |
| Term | Verbinding |
| Identificatie | 98f9327b-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| Verbinding | heeft relatie met | representeert | BinnenRuimteNetwerk | Deurvlak |
| Verbinding | heeft relatie met | van | BinnenRuimteNetwerk | Knoop |
| Verbinding | heeft relatie met | naar | BinnenRuimteNetwerk | Knoop |
| Verbinding | heeft relatie met | representeert | BouwComponenten | Wand |

#### VerbindingsRuimte

| Veld | Waarde |
|---|---|
| Schema | IMWO |
| Model | Binnenruimtenetwerk |
| Term | VerbindingsRuimte |
| Identificatie | 98f935d4-755e-11f1-8f93-00ffdb61c323 |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerbindingsRuimte | heeft relatie met | heeftRelatieMet | IFC | IfcOpeningElement |

| Term | Relatiesoort | Relatienaam | Model | Object |
|---|---|---|---|---|
| VerbindingsRuimte | is gerelateerd aan | representeert | BinnenRuimteNetwerk | Knoop |

## Beheer en doorontwikkeling IMWO
*Samenvatting van het door Martijn van Glabbeek, product owner GEBORA, opgestelde Ontwikkelplan IMWO* 

### Beheer IMWO
IMWO 1.0 is een eerste bruikbare basisversie, die op termijn uitgroeit tot een Vocabulary Hub binnen het DSGO: partijen koppelen hun begrippen één keer aan de hub in plaats van voor elke uitwisseling een nieuwe vertaalsleutel te bouwen. Vier doelstellingen sturen het beheer:
1. continuiteit en versioning
2. permanente URI's en gratis viewer
3. doorontwikkeling op basis van jaarlijkse standaardenmapping
4. sectordraagvlak en adoptie.

De governance is opgezet conform BOMOS en kent vier lagen:

1. Product Owner GEBORA. Deze draagt eindverantwoordelijkheid, legt releasebesluiten voor aan de GEBORA Architectuurboard en is als agendadeelnemer aangesloten bij SDO-overleggen (NEN 2660, IFC, CityGML).
2. De Change Advisory Board (CAB) is het centrale adviesorgaan en komt tweemaal per jaar bijeen. Hij weegt alle Request Changes (RC's) langs drie assen: verbreding naar andere bouwwerktypen, verdieping van begrippen, en verbetering van tooling en toepassingsinfrastructuur. De CAB is samengesteld vanuit vier perspectieven: (1) Overheid / bevoegd gezag (2) Marktpartijen, (3)  Bouw, ontwerp en techniek  en (4) Kennis en onderzoek
3. Klankbordgroep (3-5 experts): deze geeft jaarlijks een reflectie op toekomstbestendigheid.
4. IMWO Adviseur: deze is verantwoordelijk voor de dagelijkse operatie.

Voor Request Changes (RC's) wordt een procedure ingericht.

Publicatie en tooling: elk begrip krijgt een stabiele, permanente URI (bijv. https://modellen.digigo.nu/imwo/def/Woongebouw); IMWO wordt als owl-bestand online raadpleegbaar via een gratis viewer.  Bij elke versie worden webtekst, functionele handleiding, technische handleiding en FAQ verstrekt.

Ten behoeve van sectordraagvlak, adoptie en toepassing komt er een Jaarlijkse IMWO-expertdag en vinden er presentaties plaats op branchedagen. Use cases worden geprioriteerd op basis van stuurgroepinput en IOP-programma. Softwareleveranciers zijn een prioritaire doelgroep voor vroege adoptie: één keer koppelen aan het IMWO ontsluit toegang tot de gehele sector. Communicatie via IMWO-pagina, digiGO-nieuwsbrief en vakconferenties.

### Doorontwikkeling IMWO

Er zijn drie assen voor doorontwikkeling:
1. Verdieping – logische datamodellen voor concrete toepassingen (BM13 vergunningscheck, BM15 Kadaster/LVG, installatieregistratie, DPP, WKB, BBL-alignment, European Core Vocabularies)
2. Verbreding – uitbreiding naar utiliteitsgebouwen (laaghangend fruit), GWW-sector, aansluiting Nationaal Semantisch Vlak (NORA/RVB)
3. Technologie – MCP-koppelvlakken voor AI-bevraagbaarheid; uitgroei tot volledig bevraagbare Vocabulary Hub via digiGO Hub (2027-2028)

## Bronnen
| Referentie          | Titel, auteur, datum                                                                                                                                                                                                                | link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Aedes-IMV]         | AEDES Informatiemodel vastgoed, versie 0.9, 2025?                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Bbl]               | Besluit bouwwerken leefomgeving https://wetten.overheid.nl/BWBR0041297                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Bbl-Praktijk]      | Ministerie van BZK,'Praktijkboek Besluit bouwwerken leefomgeving', Vakmedianet, 2001                                                                                                                                                | https://open.overheid.nl/overheid/openbaarmakingen/api/v0/attachment/ronl-1a2b0036-d4b1-4f7d-89b8-149fb26976c2                                                                                                                                                                                                                                                                                                                                                                         |
| [BIM Basis ILS]     | Beheerorganisatie BIM Basis ILS, 'BIM Basis ILS'                                                                                                                                                                                    |  https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [BIM Legal]         | Stichting platform BIM Legal, 'BIM Legal afsprakenset v1.0', 2025                                                                                                                                                                   | https://bimlegal.nl/wp-content/uploads/2026/01/2025-Afsprakenset-BIM-Legal-v1.1.pdf                                                                                                                                                                                                                                                                                                                                                                                                    |
| [BOT]               | Linked Building Data Community Group'Building Topology Ontology', 2021                                                                                                                                                              | https://w3c-lbd-cg.github.io/bot/                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [BRK]               | Kadaster,'Catalogus Basisregistratie Kadaster', 10-12-2020                                                                                                                                                                          | https://www.kadaster.nl/-/catalogus-brk                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [CBS]               | Begrippen                                                                                                                                                                                                                           | https://www.cbs.nl/nl-nl/onze-diensten/methoden/begrippen                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [CB23-lexicon]      | Platform CB'23,'Lexicon Circulaire bouw', versie 3.0, 24 april 2024                                                                                                                                                                 | https://platformcb23.nl/                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [CB23-pp]           | Platform CB'23,'Leidraad Paspoorten voor de bouw. Deel 1+2', juni 2023 (Public Draft)                                                                                                                                               | https://platformcb23.nl/                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [CIMOW]             | Geonovum,'Conceptueel Informatiemodel Omgevingswet', 9 januar 2026                                                                                                                                                                  | https://docs.geostandaarden.nl/dso/dso-cim-ow/                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [CityGML]           | OGC City Geography Markup Language (CityGML) Part 1: Conceptual Model Standard                                                                                                                                                      | https://docs.ogc.org/is/20-010/20-010.html#toc0                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [COBIE]             |                                                                                                                                                                                                                                     | https://nibs.org/nbims/v3/cobie/                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [digiGO e.a. 2025]  | Ketenstandaard, digiGO, Geonovum, CROW,'Naar een betrouwbaar   virtueel digitaal bouwwerkdossier', 2025?                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [EMSO]              | Geonovum,'DiS Geo : Eisen aan model samenhangende objectenregistratie', 16 juni 2021                                                                                                                                                | https://docs.geostandaarden.nl/disgeo/emso/                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [EMSO]              | Geonovum,'DiS Geo : Eisen aan model samenhangende objectenregistratie', Versie ter vaststelling 16 juni 2021                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [EP-Online]         | Rijksoverheid,'EP-online'; officiële landelijke database met energielabels en energieprestatie-indicatoren                                                                                                                          | www.ep-online.nl                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ETIM]              | ETIM International                                                                                                                                                                                                                  | https://www.etim-international.com/                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Gebora]            | digiGO: 'GEBORA: GEBouwde Omgeving Referentie Architectuur', https://www.digigo.nu/wat-is-gebora/                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GeboraCim 2025]    | digiGO,’GEBORA Conceptueel informatiemodel’, versie 1.0, 30-04-2025: https://www.digigo.nu/wp-content/uploads/2025/06/GEBORA-Conceptueel-Informatiemodel-1.0-ter-publicatie.pdf                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GeoSemantiek 2022] | Geonovum, 'Whitepaper semantische interoperabiliteit van geo-informatie', 2022                                                                                                                                                      | https://geonovum.github.io/semigeo/                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [GGM]               | Gemeentelijk Gegevensmodel                                                                                                                                                                                                          | https://www.gemeentelijkgegevensmodel.nl/v2.5.0/                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GIR-0]             | Installatiedata delen via GIR', presentatie digiGO, 2025                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GIR-1]             | GIR Documentatie                                                                                                                                                                                                                    | https://ketenstandaard.semantic-treehouse.nl/docs/api/GIR/                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [GIR-2]             | GIR Documentatie                                                                                                                                                                                                                    | https://ketenstandaard.semantic-treehouse.nl/docs/TNL/GIR/                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [IBRO-begrip]       | Geonovum,'Begrippenkader Integrale Bronregistratie Objecten', ;                                                                                                                                                                     | https://definities.geostandaarden.nl/ibro/id/begrippenkader/Samenhangende+Objectenregistratie+Gebouwen; https://definities.geostandaarden.nl/ibro/nl/index                                                                                                                                                                                                                                                                                                                             |
| [IBRO-LM 0.9.1]     | Geonovum.'Logische gegevensmodel Integrale brondregistratie objecten v 0.9.1.'                                                                                                                                                      | https://docs.geostandaarden.nl/ibro/vv-im-ibro-lm-20251105/#domein-gebouwen                                                                                                                                                                                                                                                                                                                                                                                                            |
| [IDS]               | BuildingSmart,'Information Delivery Specification (IDS)', https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/; https://github.com/buildingSMART/IDS/tree/development/Documentation        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IFC 4.3.2]         | BuildingSmart,'IFC 4.3.2.0 specification', 2025: https://ifc43-docs.standards.buildingsmart.org/  (inhoud is conform ISO 16739-1:2024)                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ILS-O&E-1]         | digiGO,'ILS Ontwerp & Engineering',                                                                                                                                                                                                 | https://www.digigo.nu/ilsen-en-richtlijnen/ils-ontwerp-en-engineering/                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ILS-O&E-2]         | digiGO, 'Handboek ILS Ontwerp & engineering 2.0 - Bouwproducten                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ILS-Spaces]        | Gemeente Rotterdam e.a., 'ILS voor ruimten in de Omgevingswet', maart 2025                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ILS-woco 3.0]      | Aedes, 'ILS-woco 3.0', 16 juli 2025                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IMBAG 2018]        | Ministerie van BZK,'Catalogus Basisregistratie Adressen en Gebouwen',  2018'                                                                                                                                                        | https://imbag.github.io/catalogus/                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [IMIBRO 1.0.0]      | Geonovum,'Conceptueel Informatiemodel Integrale Bronregistratie Objecten (IMIBRO) 1.0.0', vastgestelde versie 29 september 2025                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IMIBRO]            | Geonovum,'Conceptueel Informatiemodel Integrale Bronregistratie Objecten (IMIBRO). Een overzicht', 28 mei 2025, https://www.geonovum.nl/uploads/documents/Conceptueel-Informatiemodel-IMIBRO%20voor%20consultatie.pdf               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IMKAD]             | Kadaster,'Catalogus conceptueel model: IMKAD', 30 januari 2020                                                                                                                                                                      | https://developer.kadaster.nl/schemas/imkad/20200130/cat/index.html                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [IMVG]              | Geonovum,Ínformatiemodel vastgoedgebruik', werkversie 25 maart 2026                                                                                                                                                                 | https://geonovum.github.io/IMVG/                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [IMWOZ]             | Waarderingskamer,'Informatiemodel WOZ', ter vaststelling 01 januari 2026                                                                                                                                                            | https://www.waarderingskamer.nl/documenten/imwoz-models/IMWOZ-model-03.12/cat/index.html                                                                                                                                                                                                                                                                                                                                                                                               |
| [IMX-Geo]           | https://geonovum.github.io/IMX-Geo/                                                                                                                                                                                                 | zie nog meer documenten hierover op: https://www.geonovum.nl/geo-standaarden/imx-geo-semantisch-model-basis-en-kernregistraties                                                                                                                                                                                                                                                                                                                                                        |
| [IndoorGML]         | OGC,'IndoorGML 2.0 Part1-Conceptual Model, 2025                                                                                                                                                                                     | http://www.opengis.net/doc/IS/indoorgml/2.0                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ISDE]              | RVO,'ISDE:meldcodelijsten', 2025                                                                                                                                                                                                    | www.rvo.nl/sunsidies-financiering/isde/meldcodelijsten                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Ketenstandaard-Ruimte]              | Ketenstandaard,'Ruimtedefinities. Opzoeknaarhetlogische modelvan eenruimte.', presentatie 2025                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                  || [MIM 2024]          | Geonovum,’Metamodel Informatiemodellering (MIM)’, versie 1.2, 13 juni 2024                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [MiniBIM A]         | MiniBIM ILS deel A: Toelichting', v3.1-deel A', Comissie digitalisering Neprom/ Pim van Meer, Paul Strokap, 2025?                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [MiniBIM B]         | MiniBIM ILS ', v3.1-deel B', Comissie digitalisering Neprom/ Pim van Meer, Paul Strokap, 2025?                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NAA.K.T.1]         | NAA.K.T. Eenduidige materiaalbenaming', toelichting                                                                                                                                                                                 | https://www.digigo.nu/wp-content/uploads/2023/11/EenduidigeMateriaalbenaming_toelichting.pdf                                                                                                                                                                                                                                                                                                                                                                                           |
| [NAA.K.T.2]         | NAA.K.T. Eenduidige materiaalbenaming', infographic                                                                                                                                                                                 | https://www.digigo.nu/wp-content/uploads/2023/11/EenduidigeMateriaalbenaming_infographic.pdf                                                                                                                                                                                                                                                                                                                                                                                           |
| [NAA.K.T.3]         | NAA.K.T. Eenduidige materiaalbenaming', lijst                                                                                                                                                                                       | https://www.digigo.nu/wp-content/uploads/2024/07/EenduidigeMateriaalbenaming_lijst-v2.4.xlsm                                                                                                                                                                                                                                                                                                                                                                                           |
| [NEN 2580]          | NEN, 'NEN 2580:2007 nl. Oppervlakten en inhouden van gebouwen - Termen, definities en bepalingsmethoden', mei 2007                                                                                                                  | https://connect.nen.nl/Standard/Detail/113982?compId=14489&collectionId=0                                                                                                                                                                                                                                                                                                                                                                                                              |
| [NEN 2660-1]        | NEN,'Regels voor informatiemodellering van de gebouwde omgeving - Deel 1: Conceptuele modellen', 2022                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NEN 2660-2]        | NEN,'Regels voor informatiemodellering van de gebouwde omgeving - Deel 2: Praktische configuratie, extensie en implementatie van NEN 2660-1', 2022                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NEN 2699]          | NEN,'NEN 2699:2017. Investerings- en exploitatiekosten van onroerende zaken', 2017                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NEN 3610]          | NEN,'Basismodel geo-informatie - Termen, definities, relaties en algemene regels voor de uitwisseling van informatie over aan de aarde gerelateerde ruimtelijke objecten', 1 juni 2022;  https://www.nen.nl/nen-3610-2022-nl-296137 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NEN4660]           | Nederlandse praktijkrichtlijn  NEN, 'NPR 4660 (nl). Modellering van gebouwde omgeving en procesindustrie - Praktijkvoorbeelden voor toepassing van NEN 2660-1 en -2', januari 2026                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [NL/SfB]            | NL/SfB 2005, versiedatum 2019-12-23                                                                                                                                                                                                 | https://www.stabu.nl/standaarden/profile.aspx; https://ketenstandaard.nl/nlbe-sfb-facts/viewer/                                                                                                                                                                                                                                                                                                                                                                                        |
| [NTA8800:2025]      | NEN, 'Energieprestaties van gebouwen - Bepalingsmethode', 2025                                                                                                                                                                      | www.nen.nl/nya-8800-2025-nl-344705                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [OTL-B&U]           | digiGO/BIMW en Gobar Adviseurs,'Draaiboek OTL voor B&U sector. Randvoorwaarden en handleiding', 2024                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [OTL-richtlijnen]   | digiGO,'Richtlijnen voor OTL'en. digiGO technische documentatie', werkdocument 17 maart 2025                                                                                                                                        | https://nl-digigo.github.io/kadersinformatiemodellen/kader/                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [RBS]               | RVB BIM Specificatie, versie 1.1-c, april 2019                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RVB]               | Rijksvastgoedbedrijf,'Harmonisatie begrippen """"nstandhouden vastgoed v.1.0', MEMO 15-9-2022                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RVB-mode]          | UML-modellen 2024                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [SAREF]             | ETSI, 'SAREF: the Smart Applications REFerence ontology', 31-10-2024                                                                                                                                                                | https://saref.etsi.org/core/v4.1.1/                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [S4BLD]             | ETSI, 'SAREF4BLDG ontology and semantics', 24-04-2025                                                                                                                                                                               | https://saref.etsi.org/saref4bldg/v2.1.1/                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [SAREF-BLD]         | ETSI,' 103 410-3 V1.1.2 (2020-05). SmartM2M; Extension to SAREF; Part 3: Building Domain'                                                                                                                                           | https://www.etsi.org/deliver/etsi_ts/103400_103499/10341003/01.01.02_60/ts_10341003v010102p.pdf                                                                                                                                                                                                                                                                                                                                                                                        |
| [SEMIC Location]    | SEMIC Community,'Core Location Vocabulary'                                                                                                                                                                                          | https://semiceu.github.io/Core-Location-Vocabulary/releases/2.1.0                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [VTH-FLo]           | Ministerie van Infrastructuur en Waterstaat, 'Conceptueel Informatiemodel VTH Fysieke Leefomgeving', versie 1.0.0                                                                                                                   | https://digitaliseringvth.nl/bibliotheek/handlerdownloadfiles.ashx?idnv=3194110                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Windesheim 2024]   | Lectoraat Energietransitie Windesheim', Energetisch beter met BIM', 22-05-2024                                                                                                                                                      | https://objectstore.surf.nl/live/objectstore/9dacb26f-e9c1-47ad-9c15-44d09591d415/100610983_10074454_Rapport_Energetisch_Beter_met_BIM_20240522_met_bijlagen.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=8ea577ad65394dfeb2d62886e3056a36%2F20251227%2FNL%2Fs3%2Faws4_request&X-Amz-Date=20251227T201107Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=75b8513a461aba2c0a38a1b8fa041d24384e2a26c7a90592d474064f5de53cfb |
| [Wws]               | Woningwaarderingsstelsel                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Bijlage 1: Overzicht schema's {#bijlage1}

| Schema | Beschrijving | 
| :----- | :----- |
| Aedes IM Vastgoed |conceptueel informatiemodel volgens MIM |
| Bbl | Besluit bouwwerken leefomgeving: regels voor veiligheid, gezondheid, bruikbaarheid en duurzaamheid van bouwwerken. Een bouwwerk moet altijd voldoen aan die regels. |
| BIM Basis ILS | Specificatie van eenduidige afspraken over informatieuitwisseling over bouwwerken op basis van IFC. |
| BIM Legal | 3D-weergave van de juridische situatie van een gebouw en maken van splitsingstekeningen daaruit. |
| BOT ontology| ontologie voor Linked Data BIM-modellen |  
| BRICK |  open standaard voor semantische beschrijvingen van fysieke, logische en virtuele assets in gebouwen |
| CPR-2024 | Construction Products Regulation (Verordening Bouwproducten), EU 2024/3110, regelt de eisen, CE-markering en milieu-informatie voor alle bouwmaterialen die in de EU worden verhandeld, met een sterke nadruk op duurzaamheid en circulariteit. |
| CIM | Common Information Model, raamwerk voor beheerde elementen in een systeem. CIM betreft (1) informatietechnologie (2) elektriciteits-  en energiesystemen. 3. cybersecurity & data analytics |
| CIMOW | Conceptueel Informatiemodel Omgevingswet, de basis voor het Informatiemodel Omgevingswet (IMOW), dat weer de basis is voor het Digitaal Stelsel Omgevingswet (DSO), gekoppeld aan de Standaard officiële publicaties en Toepassingsprofielen voor omgevingsdocumenten (STOP/TPOD) |
| CityGML | City Geography Markup Language, standaard voor het opslaan en uitwisselen van virtuele 3D-stadsmodellen. |
| COBie | Construction-Operations Building information exchange, open dataformaat voor de publicatie van een subset van bouwinformatiemodellen (BIM) die zich richt op het leveren van gegevens over objecten, in tegenstelling tot geometrische informatie. |
| CORA | Corporatie Referentie Architectuur, met onder meer gegevensdomeinmodellen |
| DBL | EU Digital Building Logbook, integreert het Energielabel (EPC), het Building Renovation Passport, slimme paraatheid (Smart Readiness Indicator) en duurzaamheidsdata. |
| DiCon | Digital Construction Ontologies: Terminologie voor de weergave van gedigitaliseerde bouw- en renovatieprocessen |
| DICO | set afspraken met spelregels voor de elektronische uitwisseling van informatie tussen fabrikanten, groothandels, bouw-, onderhouds- en installatiebedrijven en woningcorporaties. | 
| Dossier Bevoegd Gezag | Wkb-opleverdossier |
| ETIM | nternationale standaard voor rubricering en classificatie van technische producten |
| GEBORA 1.0 | GEBouwde Omgeving Referentie Architectuur |
| Geometrie | Geometriestandaarden: IFC (IfcGeometryResource), veelal afgeleid van ISO 10303-42: geo-standaarden: ISO 19107 e.a.) …
| GeoSPARQL |  ontologie voor geo-informatie als uitbreiding op SPARQL met functionaliteit voor ruimtelijke vragen |
| GGM | Gemeentelijk Gegevensmodel | 
| GIR | Gebouwinstallatieregister |
| IDS | Information Delivery Specification, standaard voor het specificeren van objecten, classificaties, materialen, eigenschappen en waarden in een IFC-model |
| IFC | Industry Foundation Classes (ISO 16739), open standaard voor BIM | 
| ILS O&E | informatieleveringsspecificatie Ontwerp & Engineering |
| ILS Ruimten | informatieleveringsspecificatie voor ruimten in de Omgevingswet | 
| ILS Woco | informatieleveringsspecificatie voor woningcorporaties | 
| IMBAG | Informatiemodel Basisregistratie Adressen en Gebouwen |
| IMBOR | Informatiemodel Beheer Openbare Ruimte |
| IMGEO | Informatiemodel geo-informatie, uitbreiding op de BGT-inhoud |
| IMIBRO | Informatiemodel Integrale Bronregistratie Objecten, een integrale registratie van objecten in de fysieke ruimte | 
| IMKAD | Informatiemodel Kadaster |
| IMX-Geo | Semantisch model basis- en kernregistraties |
| IMVG | Informatiemodel Vastgoedgebruik |
| IMWOZ | Informatiemodel waardering onroerende zaken (WOZ) |
| IndoorGML | Open datamodel van de OGC voor ruimtelijke informatie binnenshuis, met name gericht op navigatie |
| Inspire | Europese standaard voor ruimtelijke informatie |
| ISO  ISO 19100-reeks | Internationale standaarden voor het vastleggen, uitwisselen en beheren van geo-informatie |
| KIS Systematiek | Gestructureerde vastlegging van specificaties op basis van standaarden als STABU, ETIM, DICO en NL-SfB |
| LADM | Land Administration Domain Model (ISO 19152) |
| LVG | Landelijke Voorziening Gebouwgegevens. Initiatief van de overheid om versnipperde data per gebouw samen te brengen en voor de eigenaar beschikbaar te maken |
| materiaalpaspoort | digitaal document met bouwinformatie voor circulair bouwen en hergebruik |
| meetinstructies voor taxaties | meetinstructie, gebaseerd op NEN 2580 |
| MiniBIM | minimale, eenduidige projectinformatie die nodig is voor vastgoedontwikkeling |
| MiniGIM | beschrijving van de minimale dataset voor een grondexploitatie (GREX) | 
| FM-standaarden | Facility managementstandaarden |
| NAA.KT | Naam, Kenmerk en Toepassing: uniforme classificatie van materialen in BIM |
| NEN2580 |  norm voor het eenduidig en objectief meten van oppervlakten en inhouden van gebouwen |
| NEN2660-1 |  raamwerk voor het ontwikkelen van samenhangende conceptuele modellen die betrekking hebben op het gebruik van, en de gehele levenscyclus van de gebouwde omgeving |
| NEN2660-2 | praktische invulling van NEN 2660-1 |
| NEN2699 | indeling van investeringskosten en exploitatiekosten van onroerende zaken |
| NEN2767 | methodiek voor de conditiemeting van beheerobjecten in de gebouwde omgeving |
| NEN3610 | basismodel geo-informatie |
| NEN-EN 15221-6 | Europese normen voor Facility Management |
| NEN-EN-15804 |  Europese norm voor de op de milieugerichte levenscyclusanalyse (LCA) gebaseerde milieuprestatie van bouwproducten |
| NLBE-SfB | geharmoniseerd classificatiesysteem Nederland en België |
| NPR 4660 | Praktijkrichtlijn bij NEN 2660 |
| OmniClass | classificatiesysteem voor de bouwsector |
| OTL B&U | objecttypenbibliotheek voor de B&U-sector |
| Paspoorten: CB23, GABC NEN18216 e.a. | digitale materiaal- en gebouwpaspoorten voor duurzaamheid en materialen |
| RVB IM | Informatiemodel Rijksvastgoedbedrijf |
| SAREF | The Smart Applications REFerence Ontology |
| STABU | gestandaardiseerde besteksystematiek voor de woning- en utiliteitsbouw | 
| Uniclass | uniform classificatiesysteem voor de bouwsector |
| Unieke ObjectCodering | sleutel om objecten (zoals gebouwen, percelen of netwerken) ondubbelzinnig te identificeren en registreren |
| VERA |  Volkshuisvesting Enterprise Referentie Architectuur |
| VIVET | programma voor Verbetering Informatie Voorziening Energietransitie |
| VTH-flo | Conceptueel Informatiemodel VTH Fysieke Leefomgeving |
| WWS | Woningwaarderingsstelsel van de Huurprijzenwet |

## Bijlage 2: Inventarisatie {#bijlage2}

### Diagrammen

### Overzicht

#### Toelichting

| Onderwerp | Specificatie |
| :----- | :----- |
| Schema | Aanduiding van de standaard of het model |
| Term | Termnaam |
| Definitie | Originele definitie, zodanig aangepast, dat alleen een zo beknopt mogelijke definiërende uitdrukking resteert. 
| Bron | [Verwijzing naar de bron] |
 | Context | Domein, waarbinnen de term gehanteerd wordt met de aangehaalde definitie |
 | Bijzonderheden | In de bron vermelde bijzonderheden. Soms is de definitie ingekort en wordt het verwijderde deel uit de definitie hier vermeld.|
 | Voorbeelden |In de bron genoemde voorbeelden|
 | Commentaar |Commentaar en vraagpunten vanuit IMWO|

*Context, bijzonderheden, voorbeelden en commentaar zijn in deze versie in de tabel weggelaten omwille van ruimte*.  

#### Inventarisatie van definities

| Schema                                                       | Naam                                                         | Definitie                                                    | Bron                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Aedes IM Vastgoed 0.9                                        | ander bouwwerk                                               |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | bouwdeel                                                     |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | bouwkundig element                                           |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | bouwlaag                                                     | Horizontale sectie van een gebouw, bovenop een constructieve  vloer of dak, die bestaat uit één of meer ruimten, toegankelijk is voor  mensen en een hoogte van minimaal 1,5 meter heeft. | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | bouwwerk                                                     | Constructie van enige omvang van hout, steen, metaal of ander  materiaal, die op de plaats van bestemming hetzij direct of indirect met de  grond verbonden is, hetzij direct of indirect steun vindt in of op de grond,  bedoeld om ter plaatse te functioneren” [BBL] | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | buitenruimte                                                 | Niet-volledig fysiek afgebakende ruimte die aan het bouwwerk  is gebonden. Ligt buiten de gesloten bouwstructuur en staat in direct contact  met de buitenlucht | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | eenheid                                                      |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | element                                                      |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | gebied                                                       | Afgebakende zone binnen een bouwwerk, waarin een specifieke  voorwaarde of juridische status geldt die beperkingen oplegt aan het  verwachte gebruik van die zone. | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | gebouw                                                       | Vrijstaande, overdekte en geheel of gedeeltelijk met wanden  omsloten toegankelijke ruimte(n), die direct of indirect met de grond is  verbonden en die primair bedoeld is voor gebruik, verblijf of opslag binnen  omsloten ruimten. | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | installatie                                                  |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | onderdeel                                                    |                                                              | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | ruimte                                                       | Door fysieke elementen afgebakend deel binnen een bouwwerk dat  bedoeld is voor een specifiek gebruik | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | subruimte                                                    | onderverdeling van een ruimte die bedoeld is voor een  specifiek gebruik | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | terrein                                                      | door een fysiek voorkomen gekarakteriseerd zichtbaar begrensd  stuk grond”     (BAG) | [Aedes-IMV]                                                  |
| Aedes IM Vastgoed 0.9                                        | voorziening                                                  |                                                              | [Aedes-IMV]                                                  |
| Bbl                                                          | aankleding                                                   | op of aan een constructieonderdeel bevestigd materiaal       | [Bbl}                                                        |
| Bbl                                                          | aansluitend terrein                                          | aan een bouwwerk grenzend onbebouwd gedeelte van een  bouwwerkperceel of openbaar toegankelijk gebied | [Bbl}                                                        |
| Bbl                                                          | achtererfgebied                                              | gebouwerf achter de lijn die het hoofdgebouw doorkruist op 1 m  achter de voorkant en van daaruit evenwijdig loopt met het aangrenzend  openbaar toegankelijk gebied, zonder het hoofdgebouw opnieuw te doorkruisen  of in het gebouwerf achter het hoofdgebouw te komen, waarbij als op een  perceel meer gebouwen aanwezig zijn die noodzakelijk zijn voor het verrichten  van de op grond van het omgevingsplan of een omgevingsvergunning voor een  omgevingsplanactiviteit op het perceel toegestane activiteiten of als het hoofdgebouw  geen woning is, maar op het perceel wel een of meer op de grond staande  woningen aanwezig zijn, voor het leggen van deze lijn bepalend is het  hoofdgebouw, de woning of een van de andere hiervoor bedoelde gebouwen,  waarvan de voorkant het dichtst is gelegen bij openbaar toegankelijk gebied; | [Bbl]                                                        |
| Bbl                                                          | airconditioningsysteem                                       | technisch bouwsysteem voor een vorm van inpandige  luchtbehandeling, waardoor de temperatuur wordt geregeld of kan worden  verlaagd | [Bbl}                                                        |
| Bbl                                                          | antennedrager                                                | antennemast of andere constructie bedoeld voor de bevestiging  van een antenne | [Bbl}                                                        |
| Bbl                                                          | antenne-installatie                                          | installatie bestaande uit een antenne, een antennedrager, de  bedrading en de in een of meer techniekkasten opgenomen apparatuur, met de  daarbij behorende bevestigingsconstructie | [Bbl}                                                        |
| Bbl                                                          | bedgebied                                                    | verblijfsgebied met een of meer bedruimten                   | [Bbl]                                                        |
| Bbl                                                          | bedreigd subbrandcompartiment                                | subbrandcompartiment waarin een brand begint                 | [Bbl}                                                        |
| Bbl                                                          | bedruimte                                                    | verblijfsruimte bestemd voor een of meer bedden bestemd voor  slapen of voor het verblijf van bedgebonden patiënten in die ruimte | [Bbl]                                                        |
| Bbl                                                          | beschermd subbrandcompartiment                               | gedeelte van een bouwwerk dat binnen de begrenzing van een  subbrandcompartiment ligt of daarmee samenvalt, dat meer bescherming biedt  tegen brand of rook dan een subbrandcompartiment | [Bbl}                                                        |
| Bbl                                                          | beschermde route                                             | buiten het subbrandcompartiment waar de vluchtroute begint  gelegen gedeelte van een vluchtroute | [Bbl}                                                        |
| Bbl                                                          | beschermde vluchtroute                                       | buiten een subbrandcompartiment gelegen gedeelte van een  vluchtroute die alleen voert door een verkeersruimte | [Bbl}                                                        |
| Bbl                                                          | bijbehorend bouwwerk                                         | uitbreiding van een hoofdgebouw of functioneel met een zich op  hetzelfde perceel bevindend hoofdgebouw verbonden, daar wel of niet tegen  aangebouwd gebouw, of ander bouwwerk, met een dak | [Bbl}                                                        |
| Bbl                                                          | bijna energieneutraal gebouw                                 | gebouw met een zeer hoge energieprestatie, waarbij de dicht  bij nul liggende of zeer lage hoeveelheid energie die is vereist in zeer  aanzienlijke mate wordt geleverd uit hernieuwbare bronnen die deels ter  plaatse of dichtbij wordt geproduceerd | [Bbl}                                                        |
| Bbl                                                          | bouwconstructie                                              | onderdeel van een bouwwerk voor het dragen van belastingen   | [Bbl}                                                        |
| Bbl                                                          | bouwschil                                                    | de geïntegreerde onderdelen die de binnenruimte van een gebouw  scheiden van de daar buiten gelegen onderdelen van de fysieke leefomgeving | [Bbl}                                                        |
| Bbl                                                          | bouwwerkinstallatie                                          | voor het functioneren van een bouwwerk of een gedeelte daarvan  noodzakelijke voorziening van niet-bouwkundige aard | [Bbl}                                                        |
| Bbl                                                          | bouwwerkperceel                                              | perceel dat als uitgangspunt dient bij het toetsen van een  bouwwerk aan de regels van dit besluit; | [Bbl]                                                        |
| Bbl                                                          | bouwwerkperceel                                              | perceel dat als uitgangspunt dient bij het toetsen van een  bouwwerk aan de regels van het Bbl | [Bbl}                                                        |
| Bbl                                                          | brandcompartiment                                            | Gedeelte van een of meer bouwwerken bestemd als maximaal  uitbreidingsgebied van brand. | [Bbl]                                                        |
| Bbl                                                          | brandcompartiment                                            | gedeelte van een of meer bouwwerken bestemd als maximaal  uitbreidingsgebied van brand | [Bbl}                                                        |
| Bbl                                                          | constructieonderdeel:                                        | onderdeel van een bouwwerk voor het voldoen van het bouwwerk  aan de technische eisen van de hoofdstukken 3 tot en met 5 van het Bbl | [Bbl}                                                        |
| Bbl                                                          | daknok                                                       | hoogste punt van een schuin dak                              | [Bbl}                                                        |
| Bbl                                                          | dakvoet                                                      | laagste punt van een schuin dak                              | [Bbl}                                                        |
| Bbl                                                          | extra beschermde vluchtroute                                 | buiten een brandcompartiment gelegen gedeelte van een  beschermde vluchtroute | [Bbl}                                                        |
| Bbl                                                          | functiegebied                                                | gebruiksgebied of een gedeelte daarvan, waar de voor die  gebruiksfunctie kenmerkende activiteiten anders dan het verblijven van  personen plaatsvinden; | [Bbl]                                                        |
| Bbl                                                          | functieruimte                                                | In een functiegebied gelegen ruimte.                         | [Bbl]                                                        |
| Bbl                                                          | gebouwerf                                                    | bebouwd of onbebouwd perceel, of een gedeelte daarvan, dat  direct is gelegen bij een hoofdgebouw en in feitelijk opzicht is ingericht  ten dienste van het gebruik van dat gebouw, waarbij het omgevingsplan die  inrichting niet verbiedt | [Bbl}                                                        |
| Bbl                                                          | gebruikseenheid                                              | NIET GEDEFINIEERD'                                           | [Bbl]                                                        |
| Bbl                                                          | gebruiksfunctie                                              | Gedeelten van een of meer bouwwerken die dezelfde  gebruiksbestemming hebben en die samen een gebruikseenheid vormen. | [Bbl]                                                        |
| Bbl                                                          | gebruiksgebied                                               | vrij indeelbaar gedeelte van een gebruiksfunctie waar voor de  gebruiksfunctie kenmerkende activiteiten plaatsvinden, dat bestaat uit een of  meer op dezelfde bouwlaag gelegen ruimten gelegen in een brandcompartiment  die niet door een dragende scheidingsconstructie van elkaar zijn gescheiden  en die geen toiletruimte, badruimte, technische ruimte of verkeersruimte  zijn, tenzij die ruimte zelf een functieruimte is; | [Bbl]                                                        |
| Bbl                                                          | hoofdgebouw                                                  | gebouw, of bouwkundig en functioneel te onderscheiden gedeelte  daarvan, dat noodzakelijk is voor het verrichten van andere activiteiten dan  bouwactiviteiten die op grond van het omgevingsplan of een  omgevingsvergunning voor een omgevingsplanactiviteit op het perceel zijn  toegestaan en, als meer gebouwen op het perceel aanwezig zijn, gelet op die  toegestane activiteiten het belangrijkst is | [Bbl}                                                        |
| Bbl                                                          | hoofdtoegang                                                 | toegang van een gebouw of een gebruiksfunctie die is bedoeld  om door een ieder te worden gebruikt om het gebouw of de gebruiksfunctie  binnen te gaan | [Bbl}                                                        |
| Bbl                                                          | inwendige scheidingsconstructie                              | constructie die de scheiding vormt tussen twee voor personen  toegankelijke besloten ruimten van een gebouw, met inbegrip van de op die  constructie aansluitende delen van andere constructies, voor zover die delen  van invloed zijn op het voldoen van die scheidingsconstructie aan een in dit  besluit gestelde eis; | [Bbl]                                                        |
| Bbl                                                          | inwendige scheidingsconstructie                              | constructie die de scheiding vormt tussen twee voor personen  toegankelijke besloten ruimten van een gebouw, met inbegrip van de op die  constructie aansluitende delen van andere constructies, voor zover die delen  van invloed zijn op het voldoen van die scheidingsconstructie aan een in dit  besluit gestelde eis | [Bbl}                                                        |
| Bbl                                                          | koelsysteem                                                  | technisch bouwsysteem met als doel het koelen van een ruimte  binnen een gebouw of gedeelte daarvan, door het toevoeren van koude of het  ontvochtigen van de lucht of een combinatie van beide | [Bbl}                                                        |
| Bbl                                                          | leefzone                                                     | gedeelte van een verblijfsgebied waarbij de ruimte gelegen  binnen 1 m van een uitwendige scheidingsconstructie, binnen 0,2 m van een  inwendige scheidingsconstructie en hoger gelegen dan 1,8 m boven de vloer  buiten beschouwing blijft; | [Bbl]                                                        |
| Bbl                                                          | leefzone                                                     | gedeelte van een verblijfsgebied waarbij de ruimte gelegen  binnen 1 m van een uitwendige scheidingsconstructie, binnen 0,2 m  van een inwendige scheidingsconstructie en hoger gelegen dan 1,8 m boven  de vloer buiten beschouwing blijft | [Bbl}                                                        |
| Bbl                                                          | lift                                                         | [lift voor personen als bedoeld in   artikel 1 van het Warenwetbesluit liften 2016](https://wetten.overheid.nl/jci1.3:c:BWBR0037650&artikel=1&g=2026-04-10&z=2026-04-10) | [Bbl}                                                        |
| Bbl                                                          | nevengebruiksfunctie                                         | gebruiksfunctie die ten dienste staat van een andere  gebruiksfunctie; | [Bbl]                                                        |
| Bbl                                                          | nooddeur                                                     | deur die alleen is bestemd om te vluchten                    | [Bbl}                                                        |
| Bbl                                                          | subbrandcompartiment                                         | gedeelte van een bouwwerk dat binnen de begrenzing van een  brandcompartiment ligt of daarmee samenvalt, voor beperking van verspreiding  van rook of verdere beperking van het uitbreidingsgebied van brand | [Bbl}                                                        |
| Bbl                                                          | systeem voor gebouwautomatisering en -controle               | systeem als bedoeld in artikel 2, onderdeel 3 bis, van de  herziene richtlijn energieprestatie van gebouwen | [Bbl}                                                        |
| Bbl                                                          | technisch bouwsysteem                                        | gebouwgebonden samenstelling van alle bestanddelen van een  installatie, waaronder de isolatiekenmerken daarvan, die is bedoeld voor  ruimteverwarming, ruimtekoeling, ventilatie, het voorzien van warmtapwater,  ingebouwde verlichting, gebouwautomatisering en -controle,  elektriciteitsopwekking ter plaatse, of een combinatie daarvan, met inbegrip  van systemen die gebruikmaken van energie uit hernieuwbare bronnen, van een  gebouw of een gedeelte daarvan | [Bbl}                                                        |
| Bbl                                                          | technische ruimte                                            | ruimte voor het plaatsen van de apparatuur, noodzakelijk voor  het functioneren van het bouwwerk, waartoe in ieder geval behoort een  meterruimte, een liftmachineruimte en een stookruimte; | [Bbl]                                                        |
| Bbl                                                          | tijdelijk bouwwerk                                           | bouwwerk met een instandhoudingstermijn van ten hoogste  15 jaar op dezelfde locatie; | [Bbl}                                                        |
| Bbl                                                          | toegankelijkheidssector                                      | voor personen met een functiebeperking zelfstandig bruikbaar  en toegankelijk gedeelte van een gebouw | [Bbl}                                                        |
| Bbl                                                          | trappenhuis                                                  | verkeersruimte waarin een trap ligt                          | [Bbl}                                                        |
| Bbl                                                          | uitwendige scheidingsconstructie                             | constructie die de scheiding vormt tussen een voor personen  toegankelijke besloten ruimte van een gebouw en de buitenlucht, de grond of  het water, inclusief de op die constructie aansluitende delen van andere  constructies, voor zover die delen van invloed zijn op het voldoen van die  scheidingsconstructie aan een in dit besluit gestelde eis; | [Bbl]                                                        |
| Bbl                                                          | uitwendige scheidingsconstructie                             | constructie die de scheiding vormt tussen een voor personen  toegankelijke besloten ruimte van een gebouw en de buitenlucht, de grond of  het water, inclusief de op die constructie aansluitende delen van andere  constructies, voor zover die delen van invloed zijn op het voldoen van die  scheidingsconstructie aan een in dit besluit gestelde eis | [Bbl}                                                        |
| Bbl                                                          | veiligheidsroute                                             | gedeelte van een extra beschermde vluchtroute dat voert door  een niet-besloten ruimte en aansluitend daarop door een ruimte die in de  vluchtrichting alleen kan worden bereikt vanuit een niet-besloten ruimte | [Bbl}                                                        |
| Bbl                                                          | veiligheidsvluchtroute                                       | gedeelte van een extra beschermde vluchtroute dat voert door  een niet-besloten ruimte en aansluitend daarop door een ruimte die alleen kan  worden bereikt vanuit niet-besloten ruimten | [Bbl}                                                        |
| Bbl                                                          | ventilatiesysteem                                            | technisch bouwsysteem, geen onderdeel uitmakend van een  verwarmings- of koelsysteem, dat verse lucht toevoert of verontreinigde  binnenlucht afvoert, of een combinatie daarvan | [Bbl}                                                        |
| Bbl                                                          | verblijfsgebied                                              | gebruiksgebied of een gedeelte daarvan voor het verblijven van  personen | [Bbl]                                                        |
| Bbl                                                          | verblijfsruimte                                              | Een in een verblijfsgebied gelegen ruimte voor het verblijven  van personen. | [Bbl]                                                        |
| Bbl                                                          | verkeersroute                                                | route die begint bij een doorgang van een ruimte, alleen voert  over vloeren, trappen of hellingbanen en eindigt bij de doorgang van een  andere ruimte | [Bbl}                                                        |
| Bbl                                                          | verkeersruimte                                               | ruimte voor het bereiken van een andere ruimte, die niet ligt  in een verblijfsgebied of in een functiegebied, een toiletruimte, een  badruimte of een technische ruimte; | [Bbl]                                                        |
| Bbl                                                          | verwarmingssysteem                                           | combinatie van de bestanddelen die nodig zijn voor een vorm  van inpandige luchtbehandeling, waardoor de temperatuur wordt verhoogd | [Bbl}                                                        |
| Bbl                                                          | vluchtroute                                                  | route die begint in ruimte voor personen, alleen voert over  vloeren, trappen of hellingbanen en eindigt op een veilige plaats, zonder dat  gebruik moet worden gemaakt van een lift | [Bbl}                                                        |
| Bbl                                                          | voor personen bestemde vloer of ruimte                       | vloer of ruimte waarvan het kenmerkende gebruik verbonden is  met de aanwezigheid van personen | [Bbl}                                                        |
| Bbl                                                          | voorerfgebied                                                | gebouwerf dat geen onderdeel is van het achtererfgebied      | [Bbl}                                                        |
| Bbl                                                          | warmtapwatersysteem                                          | technisch bouwsysteem waarin warmtapwater wordt opgewekt,  gedistribueerd of afgegeven | [Bbl}                                                        |
| Bbl                                                          | warmtegenerator                                              | onderdeel van een verwarmingssysteem dat nuttige warmte  genereert via een of meerdere van de volgende processen: (a) verbranding van  brandstof in een verbrandingstoestel;(b) joule-effect in de  verwarmingselementen van een verwarmingssysteem met elektrische weerstand;  en(c)opvangen van warmte uit de lucht, ventilatie afvoerlucht of een water-  of aardwarmtebron met een warmtepomp | [Bbl}                                                        |
| Bbl                                                          | wooneenheid                                                  | gedeelte van een woonfunctie voor kamergewijze verhuur voor  afzonderlijke bewoning; | [Bbl]                                                        |
| Bbl                                                          | woonfunctie                                                  | Gebruiksfunctie voor het wonen                               | [Bbl]                                                        |
| Bbl                                                          | woonfunctie voor gastouderopvang                             | woonfunctie voor  gastouderopvang als bedoeld in artikel 1.1, eerste lid, van de Wet  kinderopvang voor zover de opvang plaatsvindt op het woonadres van de  gastouder; | [Bbl]                                                        |
| Bbl                                                          | woonfunctie voor kamergewijze verhuur                        | niet-gemeenschappelijk deel van een woonfunctie waarin zich  vijf of meer wooneenheden bevinden. | [Bbl]                                                        |
| Bbl                                                          | woonfunctie voor particulier eigendom                        | woonfunctie die wordt gebouwd in particulier  opdrachtgeverschap of die wordt bewoond door de eigenaar; | [Bbl]                                                        |
| Bbl                                                          | woonfunctie voor verhuur                                     | woonfunctie, waarbij sprake is van huur van woonruimte als  bedoeld in artikel 232, eerste lid, van Boek 7 van het Burgerlijk Wetboek; | [Bbl]                                                        |
| Bbl                                                          | woonfunctie voor zorg                                        | woonfunctie waarbij aan de bewoners professionele zorg wordt  verleend met een vanuit het zorgaanbod georganiseerde koppeling tussen wonen  en zorg; | [Bbl]                                                        |
| Bbl                                                          | woongebouw                                                   | gebouw of gedeelte daarvan met alleen woonfuncties en  nevengebruiksfuncties daarvan, waarin meer dan een woonfunctie ligt die is  aangewezen op een gemeenschappelijke verkeersroute; | [Bbl]                                                        |
| Bbl?                                                         | subbrandcompartiment, beschermd subbrandcompartiment,  vluchtroute en extra beschermde vluchtroute | worden genoemd in ILS-Spaces (3.3.6)                         |                                                              |
| BIM Basis ILS                                                | ruimte                                                       | Ruimten zijn: volumes en oppervlakken, omsloten door  werkelijke fo heoretische grenzen, met een functie in een bouwwerk. | [BIM Basis ILS]                                              |
| BIM Basis ILS                                                | ruimte                                                       | volume of oppervlak dat gebruikt wordt als hulpmiddel in  verschillende processen gedurende de levenscyclus van een bouwwerk | [BIM Basis ILS]                                              |
| BIM Legal                                                    |                                                              |                                                              |                                                              |
| BOT                                                          | Building                                                     | An independent unit of the built environment with a  characteristic spatial structure, intended to serve at least one function or  user activity [ISO-12006]. A bot:Building is a part of the physical world or  a virtual world that is inherently both located in this world and having a 3D  spatial extent, is contained in a building site, and can contain one or more  storeys that are vertically connected. | [BOT]                                                        |
| BOT                                                          | Element                                                      | Constituent of a construction entity with a characteristic  technical function, form or position [[ISO-12006], 3.4.7]. | [BOT]                                                        |
| BOT                                                          | Interface                                                    | A generic concept to qualify the relationship of two or more  things in the world, where at least one is a building element or zone. | [BOT]                                                        |
| BOT                                                          | Site                                                         | A part of the physical world or a virtual world that is  inherently both located in this world and having a 3D spatial extent. It is  intended to contain or contains one or more buildings. | [BOT]                                                        |
| BOT                                                          | Space                                                        | A part of the physical world or a virtual world whose 3D  spatial extent is bounded actually or theoretically, and provides for certain  functions within the zone it is contained in. | [BOT]                                                        |
| BOT                                                          | Storey                                                       | A part of the physical world or a virtual world that is  inherently both located in this world and having a 3D spatial extent. A  bot:Storey is contained in one or more buildings, and is intended to contain  one or more spaces that are horizontally connected. Storeys of a building are  connected by means of vertical connections such as elevators and stairs. | [BOT]                                                        |
| BOT                                                          | Zone                                                         | A part of the physical world or a virtual world that is  inherently both located in this world and has a 3D spatial extent; | [BOT]                                                        |
| BRICK                                                        |                                                              |                                                              | https://brickschema.org/                                     |
| CBS                                                          | Eengezinswoning                                              | Een verblijfsobject (vbo) waarvan de gebruiksfunctie in de BAG  tenminste een woonfunctie heeft (evt. naast nadere gebruiksfuncties), die  ligt in een pand zonder andere vbo's. Hieronder vallen vrijstaande woningen,  aaneengeschakelde woningen, hoek-en tussenwoningen, voorzover niet gesplitst  of bestaande uit meerdere vbo's. | [CBS]                                                        |
| CBS                                                          | Huurwoningen                                                 | Woningen volgens de Basisregistratie Adressen en Gewbouwen  (BAG) die niet bewoond worden door de eigenaar van de woning of niet in  gebruik zijn als tweede woning. Hierbij gaat het om woningen waarvan het  aannemelijk is dat de woning bestemd is voor de huurmarkt. | [CBS]                                                        |
| CBS                                                          | Koopwoningen                                                 | Woningen volgens de Basisregistratie Adressen en Gewbouwen  (BAG) die eigendom zijn van de (toekomstige) bewoner(s) of in gebruik zijn  als tweede woning. Of waarbij de officiële partner van een overleden eigenaar  in de woning woont. | [CBS]                                                        |
| CBS                                                          | Meergezinswoning                                             | Een verblijfsobject (vbo) waarvan de gebruiksfunctie in de BAG  tenminste een woonfunctie heeft (evt. naast nadere gebruiksfuncties), die  ligt in een pand met minimaal nog één andere vbo. Hieronder vallen flats,  galerij-, portiek-, beneden- en bovenwoningen, appartementen en woningen  boven bedrijfsruimten. | [CBS]                                                        |
| CBS                                                          | Verzorgingshuis                                              | Woonvoorziening voor verzorging en begeleiding in een beschutte  woonomgeving (24-uursverblijf) van ouderen met lichamelijke en geestelijke  problemen en verminderde zelfredzaamheid. | [CBS]                                                        |
| CBS                                                          | Woning (BAG)                                                 | Alle verblijfsobjecten met minimaal een woonfunctie en eventueel een of  meer andere gebruiksfuncties worden als woning aangemerkt. | [CBS]                                                        |
| CBS                                                          | Woning (WOZ)                                                 | ingekort' Tot de woningen behoren die onroerende zaken die in  hoofdzaak (meer dan 70%) worden gebruikt voor woondoeleinden en die  onroerende zaken waarvan het gebruik volledig dienstbaar is aan  woondoeleinden. Objecten in aanbouw of leegstaande objecten met de bestemming  woondoeleinden zijn ook woningen. Tot de woningen behoren de volgende drie  klassen (met vermelding van de van toepassing zijnde gebruikscode): (i)  Woning dienend tot hoofdverblijf, (2) Woning met praktijkruimte, (3)  Recreatiewoningen en overige woningen. | [CBS]                                                        |
| CBS                                                          | Wooneenheid                                                  | Een wooneenheid is een deel van een voor woondoeleinden  bestemd (gebruiksdoel is woonfunctie) verblijfsobject van gebruik dat, vanuit  bouwtechnisch oogpunt gezien, blijvend is bestemd voor permanente bewoning  door een particulier huishouden en dat voldoet aan alle criteria die van  toepassing zijn op woningen. | [CBS]                                                        |
| CBS                                                          | Woonruimte                                                   | Onder een woonruimte verstaan we een huisvesting van  verschillende typen onderkomens waarin men permanent of voor langere tijd  onderdak heeft om in te leven, te slapen. Alle woningen vallen hieronder,  maar ook kantoren of andere niet-woningen die worden gebruikt als  (tijdelijke) woonruimte. Ook woonwagens en woonboten die bedoeld zijn voor  bewoning behoren tot de woonruimten (bewoonde stand- en ligplaatsen). | [CBS]                                                        |
| CBS                                                          | Woonterrein                                                  | Terrein dat voornamelijk voor het wonen bestemd is, incl.  primaire woonvoorzieningen. | [CBS]                                                        |
| CIMOW                                                        | Activiteit                                                   | Een activiteit is ieder menselijk handelen waarbij, of ieder  menselijk nalaten waardoor een verandering of effect in de fysieke  leefomgeving wordt of kan worden bewerkstelligd. | [CIMOW]                                                      |
| CIMWO                                                        | Gebied, Locatie,  Gebiedengroep, Ambtsgebied, Beperkingengebied, Bouw, Functie, e.a. | [CIMOW]                                                      |                                                              |
| CityGML                                                      | AbstractBuilding                                             | AbstractBuilding is an abstract superclass representing the  common attributes and associations of the classes Building and BuildingPart. | [CityGML]                                                    |
| CityGML                                                      | AbstractBuildingSubdivision                                  | AbstractBuildingSubdivision is the abstract superclass for  different kinds of logical building subdivisions. | [CityGML]                                                    |
| CityGML                                                      | AbstractCityObject                                           | Augments AbstractCityObject with properties defined in an ADE. | [CityGML]                                                    |
| CityGML                                                      | AbstractConstruction                                         | AbstractConstruction is the abstract superclass for objects  that are manufactured by humans from construction materials, are connected to  earth, and are intended to be permanent. A connection with the ground also  exists when the construction rests by its own weight on the ground or is  moveable limited on stationary rails or if the construction is intended to be  used mainly stationary. | [CityGML]                                                    |
| CityGML                                                      | AbstractConstructiveElement                                  | AbstractConstructiveElement is the abstract superclass for the  representation of volumetric elements of a construction. Examples are walls,  beams, slabs. | [CityGML]                                                    |
| CityGML                                                      | AbstractFeature                                              | AbstractFeature is the abstract superclass of all feature  types within the CityGML Conceptual Model. | [CityGML]                                                    |
| CityGML                                                      | AbstractFeatureWithLifespan                                  | AbstractFeatureWithLifespan is the base class for all CityGML  features. This class allows the optional specification of the real-world and  database times for the existence of each feature. | [CityGML]                                                    |
| CityGML                                                      | AbstractFillingElement                                       | AbstractFillingElement is the abstract superclass for  different kinds of elements that fill the openings of a construction | [CityGML]                                                    |
| CityGML                                                      | AbstractFurniture                                            | AbstractFurniture is the abstract superclass for the  representation of furniture objects of a construction. | [CityGML]                                                    |
| CityGML                                                      | AbstractInstallation                                         | AbstractInstallation is the abstract superclass for the  representation of installation objects of a construction. | [CityGML]                                                    |
| CityGML                                                      | AbstractLogicalSpace                                         | AbstractLogicalSpace is the abstract superclass for all types  of logical spaces. Logical space refers to spaces that are not bounded by  physical surfaces but are defined according to thematic considerations. | [CityGML]                                                    |
| CityGML                                                      | AbstractOccupiedSpace                                        | AbstractOccupiedSpace is the abstract superclass for all types  of physically occupied spaces. Occupied space refers to spaces that are  partially or entirely filled with matter. | [CityGML]                                                    |
| CityGML                                                      | AbstractPhysicalSpace                                        | AbstractPhysicalSpace is the abstract superclass for all types  of physical spaces. Physical space refers to spaces that are fully or  partially bounded by physical objects | [CityGML]                                                    |
| CityGML                                                      | AbstractSpace                                                | Specifies the degree of openness of a space.                 | [CityGML]                                                    |
| CityGML                                                      | AbstractSpaceBoundary                                        | AbstractSpaceBoundary is the abstract superclass for all types  of space boundaries. A space boundary is an entity with areal extent in the  real world. Space boundaries are objects that bound a Space. They also  realize the contact between adjacent spaces. | [CityGML]                                                    |
| CityGML                                                      | AbstractThematicSurface                                      | AbstractThematicSurface is the abstract superclass for all  types of thematic surfaces. | [CityGML]                                                    |
| CityGML                                                      | AnyFeature                                                   | AnyFeature is an abstract class that is the generalization of  all feature types. AnyFeature is an instance of the «metaclass» FeatureType  [cf. ISO 19109]. | [CityGML]                                                    |
| CityGML                                                      | Building                                                     | A free-standing, self-supporting construction that is roofed,  usually walled, and can be entered by humans and is normally designed to  stand permanently in one place. It is intended for human occupancy (for  example: a place of work or recreation), habitation and/or shelter of humans,  animals or things. | [CityGML]                                                    |
| CityGML                                                      | BuildingFurniture                                            | A BuildingFurniture is an equipment for occupant use, usually  not fixed to the building. [cf. ISO 6707-1] | [CityGML]                                                    |
| CityGML                                                      | BuildingInstallation                                         | A BuildingInstallation is a permanent part of a Building  (inside and/or outside) which has not the significance of a BuildingPart.  Examples are stairs, antennas, balconies or small roofs. | [CityGML]                                                    |
| CityGML                                                      | BuildingPart                                                 | A BuildingPart is a physical or functional subdivision of a  Building. It would be considered a Building, if it were not part of a  collection of other BuildingParts. | [CityGML]                                                    |
| CityGML                                                      | BuildingUnit                                                 | A BuildingUnit is a logical subdivision of a Building.  BuildingUnits are formed according to some homogeneous property like  function, ownership, management, or accessibility. They may be separately  sold, rented out, inherited, managed, etc | [CityGML]                                                    |
| CityGML                                                      | ClosureSurface                                               | ClosureSurface is a special type of thematic surface used to  close holes in volumetric objects. Closure surfaces are virtual  (non-physical) surfaces. | [CityGML]                                                    |
| CityGML                                                      | Construction                                                 | object that is manufactured by humans from construction  materials, is connected to earth, and is intended to be permanent. | [CityGML]                                                    |
| CityGML                                                      | Door                                                         | A Door is a construction for closing an opening intended  primarily for access or egress or both. [cf. ISO 6707-1] | [CityGML]                                                    |
| CityGML                                                      | Logical space                                                | space that is not bounded by physical surfaces but are defined  according to thematic considerations. | [CityGML]                                                    |
| CityGML                                                      | Logical space                                                | space that is not bounded by physical surfaces but are defined  according to thematic considerations. | [CityGML]                                                    |
| CityGML                                                      | Occupied space                                               | space that is partially or entirely filled with matter.      | [CityGML]                                                    |
| CityGML                                                      | Physical space                                               | space that is fully or partially bounded by physical objects. | [CityGML]                                                    |
| CityGML                                                      | Space                                                        | Entity of volumetric extent in the real world                | [CityGML]                                                    |
| CityGML                                                      | Storey                                                       | A Storey is typically a horizontal section of a Building.  Storeys are not always defined according to the building structure, but can  also be defined according to logical considerations | [CityGML]                                                    |
| CityGML                                                      | Window                                                       | A Window is a construction for closing an opening in a wall or  roof, primarily intended to admit light and/or provide ventilation. [cf. ISO  6707-1] | [CityGML]                                                    |
| COBie                                                        |                                                              |                                                              | [COBIE]                                                      |
| CORA                                                         |                                                              |                                                              |                                                              |
| Core Location Vocabulary                                     | Address                                                      |                                                              | [SEMIC Location]                                             |
| Core Location Vocabulary                                     | Geometry                                                     |                                                              | [SEMIC Location]                                             |
| Core Location Vocabulary                                     | Location                                                     |                                                              | [SEMIC Location]                                             |
| DICO                                                         |                                                              |                                                              |                                                              |
| DSO                                                          | wooneenheid                                                  |                                                              |                                                              |
| DSO? (of BBL?)                                               | woonfunctie voor kamergewijze verhuur                        | woonfunctie waarin zich 5 of meer wooneenheden bevinden.     |                                                              |
| Éen  digitale taal voor objecten?                            |                                                              |                                                              |                                                              |
| EMSO (=SOR)                                                  |                                                              |                                                              |                                                              |
| energie…                                                     |                                                              |                                                              | [Windesheim 2024]                                            |
| EP-Online                                                    |                                                              |                                                              | [EP-Online]                                                  |
| ETIM                                                         | ETIM-klasse (EC)                                             | Een groep producten met soortgelijke technische kenmerken.   |                                                              |
| ETIM                                                         | groep                                                        |                                                              |                                                              |
| ETIM                                                         | Kenmerk (EF)                                                 | Technische eigenschappen  van een product die binnen een klasse zijn vastgelegd. |                                                              |
| ETIM                                                         | Modelling Class (MC)                                         | Dit wordt gebruikt voor de  3D-modellering van producten, waardoor technische kenmerken direct gekoppeld  kunnen worden aan 3D-objecten in BIM-modellen |                                                              |
| ETIM                                                         | Technisch product                                            |                                                              |                                                              |
| ETIM                                                         | Waarde (EV)                                                  | De specifieke invulling van een kenmerk                      |                                                              |
| GEBORA 1.0                                                   | bouwwerk                                                     | constructie van menselijke hand die vast verbonden is met de  grond en bedoeld is voor een langdurig gebruik. | [Gebora]                                                     |
| GEBORA 1.0                                                   | functie                                                      | specifiek doel of beoogde gebruikstoepassing van een ruimte,  bouwwerk, of infrastructuur | [Gebora]                                                     |
| GEBORA 1.0                                                   | ruimte                                                       | specifiek afgebakend gebied binnen of buiten een bouwwerk dat  ontworpen en gebruikt wordt voor bepaalde functies. | [Gebora]                                                     |
| Gebouwdossier  (Wkb-opleverdossier, gemeentelijk dossier Ow)) | [digiGO e.a. 2025]                                           |                                                              |                                                              |
| Geometrie:  …alg. geometrische definities ('geometrie','solid' e.d.) | zie ook https://geonovum.github.io/semigeo/; en [GeoSemantiek 2022] |                                                              |                                                              |
| GeoSPARQL                                                    |                                                              |                                                              |                                                              |
| GGM                                                          |                                                              |                                                              | [GGM]                                                        |
| GIR                                                          | Component                                                    | Een Component is een onderdeel van een Installatie en  vertegenwoordigt een instantie van een Product. | [GIR-2]                                                      |
| GIR                                                          | Fabrikant                                                    | global location number'                                      |                                                              |
| GIR                                                          | Installatie                                                  | Een Installatie is een verzameling van Componenten die samen  een specifieke functie vervullen op een Locatie (bijv. een  Verblijfsobject). | [GIR-2]                                                      |
| GIR                                                          | Locatie                                                      | Een Locatie beschrijft waar de Installatie zich bevindt.     | [GIR-2]                                                      |
| GS1                                                          | Product                                                      | Een Product is een item geproduceerd door een Fabrikant      | [GIR-2]                                                      |
| Hpw-Puntensysteem?                                           |                                                              |                                                              |                                                              |
| IDE?                                                         |                                                              |                                                              | [ISDE]                                                       |
| IDS                                                          |                                                              |                                                              | [IDS]                                                        |
| IFC                                                          | IfcBeam                                                      | typically a horizontal, or nearly horizontal, structural  member that is capable of withstanding load primarily by resisting bending | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcBearing                                                   | Type of building element that is usually used to transmit  loads from superstructure to substructure, and usually allowing movement  (displacement or rotation) in one or more degrees of freedom | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcBuilding                                                  | structure that provides shelter for its occupants or contents  and stands in one place. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcBuildingStorey                                            | (nearly) horizontal aggregation of spaces that are vertically  bound. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcBuiltElement                                              | The built element comprises all elements that are primarily  part of the construction of a built facility, i.e., its structural and space  separating system. Built elements are all physically existent and tangible  things. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcChimney                                                   | typically vertical, or as near as vertical, parts of the  construction of a building and part of the building fabric. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcColumn                                                    | vertical structural or architectural member which often is  aligned with a structural grid intersection. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcCovering                                                  | A covering is an element which covers some part of another  element and is fully dependent on that other element. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcCurtainWall                                               | exterior wall of a building which is an assembly of  components, hung from the edge of the floor/roof structure rather than  bearing on a floor | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcDistributionElement                                       | a generalization of all elements that participate in a  distribution system. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcDistributionSystem                                        | a network designed to receive, store, maintain, distribute, or  control the flow of a distribution media | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcDoor                                                      | The door is a built element that is predominately used to  provide controlled access for people, goods, animals and vehicles | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcElement                                                   | a generalization of all components that make up a facility   | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcEntityClass                                               | Classificatie in Ifc van elementen en ruimten (entities).    | BuildingSmart                                                |
| IFC                                                          | IfcExternalSpatialElement                                    | external region at the building site:     - logically - for example, an  instance of IfcExternalSpatialElement could represent the air space around  the building without having an own shape representation, or     - physically - for example, an  instance of IfcExternalSpatialElement could represent the sloping ground  around the building to identify the part of the external building envelop  that is below ground. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcFacility                                                  | A Facility (derived from IfcSpatialStructureElement) may be an  IfcBuilding, an IfcBridge, an IfcRailway, an IfcRoad, an IfcMarineFacility  (or any other type of built facility defined in the future, such as  IfcTunnel). | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcFeatureElement                                            | generalization of all existence dependent elements which  modify the shape and appearance of the associated master element. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcFeatureElementSubtraction                                 | specialization of the general feature element, that represents  an existence dependent element which modifies the shape and appearance of the  associated master element | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcFooting                                                   | part of the foundation of a structure that spreads and  transmits the load to the soil | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcFurniture                                                 | Furniture defines complete furnishings such as a table, desk,  chair, or cabinet, which may or may not be permanently attached to a building  structure. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcGeograpphicElement                                        | generalization of all elements within a geographical landscape | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcInternalOrExternalEnum                                    | type of space boundaries in terms of either being inside the  building or outside the building. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcMaterial                                                  | homogeneous or inhomogeneous substance that can be used to  form elements (physical products or their components). | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcMaterialDefinition                                        | general supertype for all material related information items  in IFC that have common material related properties that may include  association of material with some shape parameters or assignments to  identified parts of a component. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcMember                                                    | a structural member designed to carry loads between or beyond  points of support | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcOpeningElement                                            | opening, recess or chase, all reflecting voids. It represents  a void within any element that has physical manifestation. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcPile                                                      | slender timber, concrete, or steel structural element, driven,  jetted, or otherwise embedded on end in the ground for the purpose of  supporting a load | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcPlate                                                     | planar and often flat part with constant thickness. A plate  may carry loads between or beyond points of support, or provide stiffening. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcProduct                                                   | an abstract representation of any object that relates to a  geometric or spatial context. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcRailing                                                   | The railing is a frame assembly adjacent to human or vehicle  circulation spaces and at some space boundaries where it is used in lieu of  walls or to complement walls | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcRamp                                                      | vertical passageway which provides a human circulation link  between one floor level and another floor level at a different elevation. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcRelAggregates                                             | special type of the general composition/decomposition (or  whole/part) relationship IfcRelDecomposes. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcRelSpaceBoundary                                          | the space boundary defines the physical or virtual delimiter  of a space by the relationship IfcRelSpaceBoundary to the surrounding  elements.            In the case of a physical space  boundary, the placement and shape of the boundary may be given, and the  building element, providing the boundary is referenced,       In the case of a virtual space  boundary, the placement and shape of the boundary may be given, and a virtual  element is referenced. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcRoof                                                      | covering of the top part of a building, it protects the  building against the effects of weather. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcShadingDevice                                             | Shading devices are purpose built devices to protect from the  sunlight, from natural light, or screening them from view. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSite                                                      | defined area of land, possibly covered with water, on which  the project construction is to be completed. A site may be used to erect,  retrofit or turn down building(s), or for other construction related  developments. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSlab                                                      | component of the construction that may enclose a space  vertically | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSpace                                                     | area or volume bounded actually or theoretically. Spaces are  areas or volumes that provide for certain functions within a building. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSpatialStructureElement                                   | A spatial structure element is the generalization of all  spatial elements that might be used to define a spatial structure. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSpatialZone                                               | non-hierarchical and potentially overlapping decomposition of  the project under some functional consideration. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcStair                                                     | vertical passageway allowing occupants to walk (step) from one  floor level to another floor level at a different elevation | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcSystem                                                    | an organized combination of related parts within an AEC  product, composed for a common purpose or function or to provide a service | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcVirtualElement                                            | special element used to provide imaginary, placeholder, or  provisional areas, volumes, and boundaries. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcWall                                                      | The wall represents a vertical construction that may bound or  subdivide spaces. | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcWindow                                                    | building element that is predominately used to provide natural  light and fresh air. It includes vertical opening but also horizontal opening  such as skylights or light domes | [IFC 4.3.2]                                                  |
| IFC                                                          | IfcZone                                                      | group of spaces, partial spaces or other zones.              | [IFC 4.3.2]                                                  |
| ILS O&E                                                      | Afwerking                                                    | Een bekleding is een element dat een deel van een ander  element bedekt en volledig afhankelijk is van dat andere element. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Bouwproduct                                                  | Bouwproducten kunnen zichtbare en niet-zichtbare objecten zijn  die tijdens een ontwerp en/of engineeringsproces worden toegepast om een  gebouw te ontwerpen en engineeren | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Component                                                    | structureel element dat is ontworpen om belastingen over te  brengen tussen steunpunten of voorbij steunpunten. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Dak                                                          | beschrijving van het totale dak                              | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Deur                                                         | gebouwd element dat voornamelijk wordt gebruikt om  gecontroleerde toegang te bieden voor mensen, goederen, dieren en voertuigen | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Distributiesysteem                                           | netwerk dat is ontworpen om een distributiemedium te  ontvangen, op te slaan, te onderhouden, te verdelen of de stroming ervan te  regelen. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Fundering                                                    | Een funderingselement is een onderdeel van de fundering van  een constructie dat de belasting verspreidt en overdraagt aan de ondergrond | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Funderingspaal                                               | slanke constructie-element van hout, beton of staal, dat in de  grond wordt gedreven, gespoten of anderszins ingebracht met als doel een  belasting te dragen | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Hellingbaan                                                  | Een verticale doorgang die zorgt voor een circulatieroute voor  personen tussen het ene vloerniveau en een ander vloerniveau op een andere  hoogte. Deze kan een bordes bevatten als tussenliggende vloerplaat. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Inrichting                                                   | Inrichting definieert complete inrichtingsstukken zoals een  tafel, bureau, stoel of kast, die al dan niet permanent aan een  gebouwstructuur bevestigd kunnen zijn. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Kolom                                                        | verticale structurele of architectonische kolom die vaak is  uitgelijnd met een kruispunt van een structureel raster. In de meeste  gevallen vertegenwoordigt het een verticale, of bijna verticale, structurele  kolom die door middel van compressie het gewicht van de bovenliggende  structuur overdraagt aan andere structurele elementen eronder. Het kan ook  een dergelijke kolom vertegenwoordigen vanuit architectonisch oogpunt, in  welk geval het een niet-dragend element kan zijn. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Ligger                                                       | doorgaans een horizontaal of bijna horizontaal constructief  element dat in staat is om belastingen te weerstaan, voornamelijk door  buigweerstand | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Oplegging                                                    | Een oplegging wordt gewoonlijk gebruikt om belastingen van de  bovenbouw naar de onderbouw over te brengen, en dat doorgaans beweging  (verplaatsing of rotatie) in één of meer vrijheidsgraden toelaat. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Plaat                                                        | Een plaat is vaak een vlak onderdeel met een constante dikte. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Positie                                                      | waar wordt een specifiek object gebruikt?                    | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Raam                                                         | bouwelement dat voornamelijk wordt gebruikt om natuurlijk  licht en frisse lucht toe te laten. Het omvat verticale openingen, maar ook  horizontale openingen zoals dakramen of lichtkoepels | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Reling                                                       | frameconstructie die zich bevindt naast ruimtes voor  menselijke of voertuigcirculatie en bij bepaalde ruimteafscheidingen, waar  deze wordt gebruikt in plaats van muren of ter aanvulling van muren.  Ontworpen als een optionele fysieke ondersteuning, of om letsel of schade te  voorkomen, hetzij door vallen of botsing. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Samenstelling                                                | vorm: verschil in opbouw of vorm.                            | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Schoorsteen                                                  | Schoorstenen zijn doorgaans verticale, of nagenoeg verticale,  onderdelen van de constructie van een gebouw en maken deel uit van de  gebouwschil | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Terrein                                                      | generalisatie van alle elementen binnen een geografisch  landschap | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Toepassing                                                   | functie: waarvoor wordt een specifiek object of systeem  gebruikt? (vanuit functie beredeneerd) | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Trap                                                         | verticale doorgang die het mogelijk maakt voor gebruikers om  te lopen (stappen) van het ene vloerniveau naar een ander vloerniveau op een  andere hoogte. Een trap kan een bordes bevatten als tussenliggende  vloerplaat. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Virtueel element                                             | speciaal element dat wordt gebruikt om denkbeeldige,  tijdelijke of voorlopige gebieden, volumes en grenzen aan te duiden. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Vliesgevel                                                   | buitenmuur van een gebouw die bestaat uit een samenstelling  van componenten, opgehangen aan de rand van de vloer- of dakconstructie in  plaats van dragend te zijn op een vloer | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Vloer                                                        | constructie-element dat een ruimte verticaal kan omsluiten.  | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Wand                                                         | Een wand vertegenwoordigt een verticale constructie die  ruimtes kan begrenzen of onderverdelen. | [ILS-O&E-2]                                                  |
| ILS O&E                                                      | Zonwering                                                    | Zonweringselementen zijn speciaal ontworpen om te beschermen  tegen zonlicht, natuurlijk licht of om het zicht te beperken. | [ILS-O&E-2]                                                  |
| ILS Spaces                                                   | Bebouwd terreinoppervlakte                                   |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Bebouwd terreinvolume                                        |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Bepalingsmethode                                             |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Bouwblok                                                     |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Dakruimte                                                    |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | eigendoms- en gebruikseenheid                                | het deel van een bouwwerk dat bij dezelfde “eigenaar” in  “eigendom” is en door dezelfde “gebruiker” in “gebruik” is en een zelfstandig  te gebruiken eenheid vormt.”. | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Functioneel ruimtelijk gebied                                | Ruimtelijk concept zoals “Woning”, “Woonkamer”, “Verdieping”,  “Perceel” of “Bouwwerk”. | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Gebouwgebonden buitenruimte                                  |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Geometrie literal                                            |                                                              |                                                              |
| ILS Spaces                                                   | Geometrie van ruimte…                                        | zie H 5'                                                     | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Geometrische entiteit                                        |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | KadastraalPerceel                                            |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Onder- en overbouwd  Terreinoppervlakte                      | [ILS-Spaces]                                                 |                                                              |
| ILS Spaces                                                   | Onder- en overbouwd  terreinvolume                           | [ILS-Spaces]                                                 |                                                              |
| ILS Spaces                                                   | Onderbouwd terreinoppervlakte                                |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Onderbouwd Terreinvolume                                     |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Overbouwd Terreinoppervlakte                                 |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Overbouwd terreinvolume                                      |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Tarra inhoud                                                 |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Technisch ruimtelijk gebied                                  | (afgeleid uit de tekst) Omplementatie van een Functioneel  ruimtelijk gebied met behulp van een Bepalingsmethode | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Terras                                                       |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Tuin                                                         |                                                              | [ILS-Spaces]                                                 |
| ILS Spaces                                                   | Verhuurbare  vloeroppervlakte (VVO)                          | [ILS-Spaces]                                                 |                                                              |
| ILS Spaces                                                   | Woongebouw                                                   | Gebouw of gedeelte daarvan met alleen woonfuncties en  nevengebruiksfuncties daarvan, waarin meer dan 1 woonfunctie ligt die is  aangewezen op een gemeenschappelijke verkeersroute | [ILS-Spaces]                                                 |
| ILS-woco                                                     | Atrium                                                       | Een centrale binnenruimte in een gebouw, omgeven door meerdere  verdiepingen, ontworpen om natuurlijk licht binnen te laten en een gevoel van  openheid te creëren. | [ILS-woco]                                                   |
| ILS-woco                                                     | Badruimte                                                    | Een ruimte in een gebouw met sanitair voor het nemen van baden  en douches, inclusief voorzieningen zoals een badkuip, douchebak, wastafel en  toilet, vaak voorzien van waterdichte materialen en afvoersystemen. De term  badruimte komt vanuit het bouwbesluit. In de volksmond wordt de ruimte op  plattegronden meestal aangeduid als badkamer. | [ILS-woco]                                                   |
| ILS-woco                                                     | Bedrijfsruimte                                               | Een enkele ruimte binnen een gebouw die is ontworpen voor  commerciële of zakelijke activiteiten, zoals winkels, zorgverlening,  fabrieken of werkplaatsen, meestal voorzien van specifieke infrastructuur en  voorzieningen voor de betreffende bedrijfsactiviteiten. Niet te verwarren met  kantoorruimten. | [ILS-woco]                                                   |
| ILS-woco                                                     | Bedruimte                                                    | Een verblijfsruimte voor 1 of meer bedden om te slapen, of  voor het verblijf van aan bed gebonden personen in deze ruimte. Denk aan een  slaapruimte in een crèche, hotelkamer of verpleegruimte in een ziekenhuis.  Niet te verwarren met slaapkamer. | [ILS-woco]                                                   |
| ILS-woco                                                     | Berging inpandig                                             | Een ruimte buiten de schil van de woning, maar binnen een  gebouw met ook andere functies. Vaak gebruikt voor het opslaan van goederen,  gereedschappen, fietsen, of andere items, vaak voorzien van planken, rekken  of kasten voor organisatie. Toegang niet vanuit de woning. Een berging in een  ander gebouw, is dus ook inpandig. Niet bestemd voor technische installaties. | [ILS-woco]                                                   |
| ILS-woco                                                     | Berging uitpandig                                            | Een al dan niet afgesloten ruimte buiten het gebouw. Losstaand  of in een cluster met enkel bergingen. Vaak gebruikt voor het opslaan van  goederen, gereedschappen, fietsen, of andere items, vaak voorzien van  planken, rekken of kasten voor organisatie. Niet bestemd voor technische  installaties. | [ILS-woco]                                                   |
| ILS-woco                                                     | Bergruimte                                                   | Een ruimte binnen de schil van een woning en/of met toegang  vanuit de woning. Vaak gebruikt voor het opslaan van goederen,  gereedschappen, of andere items, vaak voorzien van planken, rekken of kasten  voor organisatie. | [ILS-woco]                                                   |
| ILS-woco                                                     | Bijkeuken                                                    | Een (kleine) ruimte naast de keuken, vaak gebruikt voor het  opslaan van voorraad, schoonmaakartikelen, wasmachines, drogers en andere  huishoudelijke apparaten. | [ILS-woco]                                                   |
| ILS-woco                                                     | Cel                                                          | Een kleine afgesloten ruimte binnen een gebouw, vaak gebruikt  in gevangenissen, detentiecentra of politiebureaus voor het opsluiten van  individuen, met minimale voorzieningen voor comfort en veiligheid. | [ILS-woco]                                                   |
| ILS-woco                                                     | Entree                                                       | Ruimte tussen de toegangsdeur en een verkeersruimte. Deze  ruimte is van toeapssing op een gebouw en op een gebruiksfunctie. | [ILS-woco]                                                   |
| ILS-woco                                                     | Fietsenstalling inpandig                                     | Een ruimte binnen een gebouw die bedoeld is voor het parkeren  van fietsen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Fietsenstalling uitpandig                                    | Een al dan niet overdekte of afgesloten ruimte buiten het  gebouw die bedoeld is voor het parkeren van fietsen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Gang                                                         | Een doorgangsruimte met lengte- breedte verhouding van 1:n.  Bevindt zich binnen een gebouw, gebruikt als verbindingsroute tussen  verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang wordt  verleend tot een gebruiksfunctie. | [ILS-woco]                                                   |
| ILS-woco                                                     | Garage inpandig                                              | Een inpandige garage is een garage die deel uitmaakt van een  gebouw. Deze ruimte is meestal direct toegankelijk vanuit het interieur van  het gebouw, bijvoorbeeld via een deur die leidt naar een gang, keuken, of  bijkeuken. De garage is voorzien van een garagedeur die naar buiten opent.  Een garage is gebonden aan een enkele woning, niet te verwarren met  parkeergarage. | [ILS-woco]                                                   |
| ILS-woco                                                     | Garage uitpandig                                             | Een uitpandige garage is een garage die geen deel uitmaakt van  het gebouw. Deze ruimte is niet direct toegankelijk vanuit het interieur van  het gebouw. De uitpandige garage is via de oprijlaan van de woonruimte te  bereiken en daarom betreft het een aanhorigheid van de woonruimte. De garage  is voorzien van een garagedeur die naar buiten opent. Een garage is gebonden  aan een enkele woning, niet te verwarren met parkeergarage. | [ILS-woco]                                                   |
| ILS-woco                                                     | Garagebox                                                    | Een garagebox is een afgesloten, individuele ruimte bedoeld  voor het stallen van een voertuig of het opslaan van goederen. Garageboxen  zijn voorzien van een garagedeur die op slot kan, vaak een kanteldeur of een  roldeur. Deze boxen kunnen losstaand zijn of deel uitmaken van een groter  complex met meerdere garageboxen. Een garagebox is een afzonderlijk object  van een woonruimte als het een vrijstaande garagebox is die middels een  afzonderlijk terrein bereikbaar is of als het een garagebox is die in de plint  (begane grond) van een appartementencomplex zit. | [ILS-woco]                                                   |
| ILS-woco                                                     | Hal                                                          | Een doorgangsruimte met een nagenoeg gelijke lengte- breedte  verhouding. Bevindt zich binnen een gebouw, gebruikt als verbindingsroute  tussen verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang  wordt verleend tot een gebruiksfunctie | [ILS-woco]                                                   |
| ILS-woco                                                     | Kantoorruimte                                                | Een enkele ruimte binnen een gebouw die specifiek is ontworpen  voor kantoorwerkzaamheden. | [ILS-woco]                                                   |
| ILS-woco                                                     | Kast                                                         | Een opbergruimte, behorende tot de aangrenzende ruimte,  onderdeel uitmakend van de bouwconstructie. | [ILS-woco]                                                   |
| ILS-woco                                                     | Kelder                                                       | Een (deels) ondergrondse ruimte onder de begane grond van een  gebouw, meestal gebruikt voor opslag, nutsvoorzieningen, wasruimte en soms  leefruimte. De toegang is via een trap of luik. In de kelder kan een  volwassen persoon rechtop staan. | [ILS-woco]                                                   |
| ILS-woco                                                     | Keuken                                                       | Een ruimte binnen een gebouw die is ontworpen en uitgerust  voor het bereiden van voedsel, voorzien van een keukenblok. | [ILS-woco]                                                   |
| ILS-woco                                                     | Liftmachineruimte                                            | Een aparte ruimte binnen een gebouw waarin de liftmachines,  aandrijvingen, regelapparatuur en veiligheidsvoorzieningen zich bevinden,  vaak gelegen boven of naast de liftschacht. | [ILS-woco]                                                   |
| ILS-woco                                                     | Meterruimte                                                  | Een ruimte binnen een gebouw waar meters voor gas,  elektriciteit, water, of andere nutsvoorzieningen worden geïnstalleerd en  onderhouden, meestal toegankelijk voor nutsbedrijven voor het aflezen en  onderhouden van de meters. | [ILS-woco]                                                   |
| ILS-woco                                                     | Opstelplaats koelkast                                        | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld. In dit  geval specifiek een koelkast. Dit is voor onbepaalde tijd en kan dus ook zeer  lang zijn. | [ILS-woco]                                                   |
| ILS-woco                                                     | Opstelplaats kooktoestel                                     | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld. In dit  geval specifiek een kooktoestel. Dit is voor onbepaalde tijd en kan dus ook  zeer lang zijn. | [ILS-woco]                                                   |
| ILS-woco                                                     | Opstelplaats vaatwasser                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld. In dit  geval specifiek een vaatwasser. Dit is voor onbepaalde tijd en kan dus ook  zeer lang zijn. | [ILS-woco]                                                   |
| ILS-woco                                                     | Opstelplaats wasdroger                                       | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld. In dit  geval specifiek een wasdroger. Dit is voor onbepaalde tijd en kan dus ook  zeer lang zijn. | [ILS-woco]                                                   |
| ILS-woco                                                     | Opstelplaats wasmachine                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld. In dit  geval specifiek een wasmachine. Dit is voor onbepaalde tijd en kan dus ook  zeer lang zijn. | [ILS-woco]                                                   |
| ILS-woco                                                     | Overige ruimte                                               | Een algemene term die wordt gebruikt voor ruimtes binnenin een  gebouw die niet passen in andere categorieën. | [ILS-woco]                                                   |
| ILS-woco                                                     | Overloop                                                     | Een overgangsgebied die ruimtes met een trap verbindt. Niet  gelegen op de onderste bouwlaag van een adres. | [ILS-woco]                                                   |
| ILS-woco                                                     | Parkeerplaats auto                                           | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een auto. | [ILS-woco]                                                   |
| ILS-woco                                                     | Parkeerplaats bakfiets                                       | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een bakfiets. | [ILS-woco]                                                   |
| ILS-woco                                                     | Parkeerplaats motorfiets                                     | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een motorfiets. | [ILS-woco]                                                   |
| ILS-woco                                                     | Parkeerplaats scootmobiel                                    | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een scootmobiel. | [ILS-woco]                                                   |
| ILS-woco                                                     | Schacht                                                      | Een verticale doorgang of ruimte binnen een gebouw, gebruikt  voor ventilatie, bekabeling of leidingen vaak voorzien van brandwerende  materialen en afsluitingen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Serre                                                        | Een serre is een verwarmde binnenruimte die als (semi)  buitenruimte gebruikt kan worden en valt binnen de GO. Niet te verwarren met  een loggia, dat is een onverwarmde verglaasde buitenruimte. | [ILS-woco]                                                   |
| ILS-woco                                                     | Slaapkamer                                                   | Een ruimte binnen een gebouw die is ontworpen en bestemd voor  slapen. Niet te verwarren met een bedruimte. | [ILS-woco]                                                   |
| ILS-woco                                                     | Stalling inpandig                                            | Een afgesloten ruimte binnen een gebouw die bedoeld is voor  het parkeren of opslaan van gemotoriseerde (vaak elektrische) voertuigen,  niet zijnde auto's. Bijvoorbeeld scootmobielen, scooters of elektrische  fietsen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Stalling uitpandig                                           | Een al dan niet overdekte of afgesloten ruimte buiten het  gebouw die bedoeld is voor het parkeren of opslaan van gemotoriseerde (vaak  elektrische) voertuigen, niet zijnde auto's. Bijvoorbeeld scootmobielen,  scooters of elektrische fietsen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Technische ruimte                                            | Een ruimte binnen een gebouw waar technische installaties  worden geplaatst en onderhouden, zoals Verwarmingsinstallaties, ventilatie-  of airconditioningsystemen, datacenters, of telecomapparatuur. Niet te  gebruiken als meterruimte of liftmachineruimte. | [ILS-woco]                                                   |
| ILS-woco                                                     | Toiletruimte                                                 | Een ruimte binnen een gebouw waarin toiletten en wastafels  zijn geïnstalleerd, bedoeld voor persoonlijke hygiëne, vaak voorzien van  sanitair, ventilatie, en sanitaire voorzieningen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Trapgat                                                      | Open ruimte in de verdiepingsvloer, bestemd om een trap te  plaatsen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Trappenhuis                                                  | Een verticale doorgangsruimte binnen een gebouw die wordt  gebruikt om tussen verschillende verdiepingen te reizen, voorzien van een  trap of trappen en vaak ook een lift, met veiligheidsvoorzieningen en  nooduitgangen. | [ILS-woco]                                                   |
| ILS-woco                                                     | Vide                                                         | Een open ruimte binnen een gebouw, zonder fysieke afscheiding  met de bouwlaag eronder. Bestemd om een een ruimtelijk gevoel te  creeren. | [ILS-woco]                                                   |
| ILS-woco                                                     | Wasruimte                                                    | Een ruimte binnen een gebouw, specifiek bestemd voor  wasmachines, drogers en andere apparaten voor wasgoed , voorzien van  wateraansluitingen, afvoer en ventilatie. | [ILS-woco]                                                   |
| ILS-woco                                                     | Woonkamer                                                    | Een centrale ruimte binnen een woning, meestal gebruikt voor  ontspanning, entertainment en sociale activiteiten, ingericht met  zitplaatsen, meubels, elektronica en decoratieve elementen, vaak verbonden  met andere delen van de woning zoals de eetkamer en keuken. | [ILS-woco]                                                   |
| ILS-woco                                                     | Woonkamer-keuken                                             | Ruimte met een gecombineerde functie van keuken en woonkamer. | [ILS-woco]                                                   |
| ILS-woco                                                     | Woonkamer-keuken-slaapkamer                                  | Ruimte met een gecombineerde functie van keuken, woonkamer en  slaapkamer. | [ILS-woco]                                                   |
| ILS-woco                                                     | Zolderruimte                                                 | Een toegankelijke ruimte binnen een gebouw, direct gelegen  onder het dak. | [ILS-woco]                                                   |
| IMBAG                                                        | Adresseerbaar object                                         | Een Adresseerbaar object is een (abstract) object waaraan  adressen kunnen worden toegekend. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Ligplaats                                                    | Een Ligplaats is een door het bevoegde gemeentelijke orgaan  als zodanig aangewezen plaats in het water al dan niet aangevuld met een op  de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het  permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve  doeleinden geschikt drijvend object. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Nummeraanduiding                                             | Een Nummeraanduiding is een door het bevoegde gemeentelijke  orgaan als zodanig toegekende aanduiding van een verblijfsobject, een  standplaats of een ligplaats. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Openbare ruimte                                              | Een Openbare ruimte is een door het bevoegde gemeentelijke  orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die  binnen één woonplaats is gelegen. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Pand                                                         | Een Pand is de kleinste, bij de totstandkoming functioneel en  bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de  aarde is verbonden en betreedbaar en afsluitbaar is. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Standplaats                                                  | Een Standplaats is een door het bevoegde gemeentelijke orgaan  als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het  permanent plaatsen van een niet direct en niet duurzaam met de aarde  verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte  ruimte. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Verblijfsobject                                              | Een Verblijfsobject is de kleinste binnen een of meer panden  gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte  eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang  vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan  zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht  zelfstandig is. | [IMBAG 2018]                                                 |
| IMBAG                                                        | Woonplaats                                                   | Een Woonplaats is een door het bevoegde gemeentelijke orgaan  als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied  van de gemeente. | [IMBAG 2018]                                                 |
| IMBOR                                                        | nav LVG 15-10                                                |                                                              |                                                              |
| IMGEO                                                        |                                                              |                                                              |                                                              |
| IMIBRO                                                       | AdresseerbaarObject                                          | Een adresseerbaar object is een object waaraan formeel  adressen kunnen en moeten worden toegekend. | Gebaseerd op artikel 1 Wet basisregistratie adressen en gebouwen |
| IMIBRO                                                       | Afdak                                                        | Constructie aangebracht en vast verbonden aan de gevel van een  pand, gericht op beschutting tegen weersinvloeden. | EMSO                                                         |
| IMIBRO                                                       | Akkerbouw                                                    | Economische activiteiten waarbij het natuurlijke milieu wordt  aangepast ten behoeve van de productie van planten voor menselijk of dierlijk  gebruik. | EMSO                                                         |
| IMIBRO                                                       | Ambulancepost                                                | Opstelpunt voor voertuigen om medische hulpverleners te  vervoeren naar een plaats waar behoefte is aan spoedeisende hulp of om  slachtoffers of patiënten te vervoeren naar een ziekenhuis. | EMSO                                                         |
| IMIBRO                                                       | Balkon                                                       | Open uitbouw die niet gelijkvloers aan de gevel is aangebracht  en waarvan het bovenvlak vanuit het gebouw toegankelijk is. | EMSO                                                         |
| IMIBRO                                                       | Basisconstructie                                             | Panddeel wat de oorspronkelijke constructie betreft van het  pand waarin het panddeel is gelegen. | EMSO                                                         |
| IMIBRO                                                       | Bebouwingskern                                               | Geografische ruimte die gekenmerkt wordt door een concentratie  van gebouwen en die vanuit besluitvorming, historie of in de volksmond bekend  staat onder een bepaalde naam. | Gebaseerd op definitie Plaats in BRT                         |
| IMIBRO                                                       | Bedrijfsgebouw                                               | Pand waarvan de constructie zodanig is vormgegeven dat het  geschikt is voor het daarbinnen uitoefenen van specifieke bedrijfsmatige  activiteiten. | EMSO                                                         |
| IMIBRO                                                       | Benedenwoning                                                | Etagewoning of flatwoning op de begane grond met een voordeur  die op straat uitkomt. | EMSO                                                         |
| IMIBRO                                                       | BenoemdePlaats                                               | Door het bevoegde gemeentelijk orgaan als zodanig aangewezen  delen van een terrein en/of water waarvan het belang is daaraan een adres toe  te kennen en dat bedoeld is voor het permanent plaatsen van een niet direct  en niet duurzaam met de aarde verbonden object, het permanent afmeren van een  drijvend object of het permanent aanwezig zijn van publiek toegankelijke  technische voorzieningen. | Gebaseerd op artikel 1 Wet basisregistratie adressen en gebouwen |
| IMIBRO                                                       | BestuurlijkGebied                                            | Een bestuurlijk gebied is een registratieve ruimte die op  basis van wet- of regelgeving als eenheid geldt van bestuurlijke  verantwoordelijkheid. | EMSO                                                         |
| IMIBRO                                                       | Bibliotheek                                                  | Bewaarplaats voor boeken en andere media waarbij deze al dan  niet aan het publiek worden uitgeleend of ter inzage aangeboden. | EMSO                                                         |
| IMIBRO                                                       | Bijeenkomsten                                                | Activiteiten waarin grotere groepen bijeen worden gebracht  voor communicatieve doeleinden. | EMSO                                                         |
| IMIBRO                                                       | Bijgebouw                                                    | Pand dat constructief is opgezet om aan een woongebouw  ondersteunende opslagfaciliteiten te bieden. | EMSO                                                         |
| IMIBRO                                                       | Bioscoop                                                     | Publieke uitgaansgelegenheid die speciaal is bedoeld voor het  bekijken van films. | EMSO                                                         |
| IMIBRO                                                       | Boerderij                                                    | Pand dat zodanig constructief is vormgegeven dat daarbinnen  een combinatie van agrarische bedrijfsvoering en bewoning door de  bedrijfsvoerder kan plaatsvinden. | EMSO                                                         |
| IMIBRO                                                       | Bordes                                                       | Verhard oppervlak, eventueel verhoogd en/of uitgevoerd met  treden, grenzen aan een pand en primair bedoeld voor gebruik door voetgangers | EMSO                                                         |
| IMIBRO                                                       | Bouwlaag                                                     | Verzameling van ruimten die zijn gelegen op hetzelfde niveau  binnen een gebouw | [IBRO-LM 0.9.1]                                              |
| IMIBRO                                                       | Bovenwoning                                                  | Etagewoning of flatwoning op een etage die bereikbaar is via  een binnentrap met een mogelijk gemeenschappelijke voordeur die op straat  uitkomt of een eigen voordeur heeft die niet in een portiek uitkomt. | EMSO                                                         |
| IMIBRO                                                       | Brandweerkazerne                                             | Opstelpunt van materieel en manschappen ten behoeve van  brandbestrijding. | EMSO                                                         |
| IMIBRO                                                       | Brugwachtershuis                                             | Activiteiten gericht op het bedienen van de technische  voorzieningen die behoren bij een brug die geopend kan worden. | EMSO                                                         |
| IMIBRO                                                       | Bunker                                                       | Van oorsprong versterkt militair gebouw gericht op het  schuilen tegen beschietingen en bombardementen. | EMSO                                                         |
| IMIBRO                                                       | Buurt                                                        | Aaneengesloten gedeelte van een wijk, waarvan de grenzen zo  veel mogelijk gebaseerd zijn op topografische elementen. | GFO Basisgegevens                                            |
| IMIBRO                                                       | Buurtgebouw                                                  | Activiteitencentrum in een wijk, buurt of dorp waar  activiteiten plaatsvinden van en voor de bewoners hiervan. | EMSO                                                         |
| IMIBRO                                                       | Buurtschap                                                   | Lintbebouwing of  verspreid staande bebouwing in landelijk gebied met een zekere mate van  sociale samenhang die gezamenlijk een bebouwingskern vormen. |                                                              |
| IMIBRO                                                       | Celfunctie                                                   | Gebruiksfunctie voor dwangverblijf van personen.             | Bbl                                                          |
| IMIBRO                                                       | Cellen                                                       | Dwangverblijf van personen.                                  | EMSO                                                         |
| IMIBRO                                                       | Clubgebouw                                                   | Activiteiten gericht op het ten behoeve van leden of andere  deelnemers aan een groep verzorgen van ontspannende activiteiten of  samenkomsten. | EMSO                                                         |
| IMIBRO                                                       | Complex                                                      | Functionele ruimte die een verzameling van één of meer  gebouwen, constructies, verharding, water en begroeiing betreft die samen een  eenheid vormen. | EMSO                                                         |
| IMIBRO                                                       | Constructie                                                  | Gebouwd object dat direct of indirect met de bodem is  verbonden en bedoeld is om ter plaatse te functioneren. | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | Corridorflatwoning                                           | Flatwoning waarbij de voordeur uitkomt op een centraal binnen  de bouwmassa per etage gelegen loopgang dan wel op een centrale hal op de  etage. | EMSO                                                         |
| IMIBRO                                                       | Crematorium                                                  | Verbranding van lichamen van overledenen in een speciale oven. | EMSO                                                         |
| IMIBRO                                                       | Dakkapel                                                     | Uitbouw van het schuine dakvlak.                             | EMSO                                                         |
| IMIBRO                                                       | Deelkern                                                     | Ruimtelijk van omliggende  bebouwing te onderscheiden historische bebouwingskern, die is gelegen binnen  een andere bebouwingskern. |                                                              |
| IMIBRO                                                       | Detailhandel                                                 | Bedrijfsmatige levering van fysieke goederen voor persoonlijk  gebruik aan consumenten. | EMSO                                                         |
| IMIBRO                                                       | Dienstverlening                                              | Levering van niet-fysieke goederen door een persoon, instantie  of onderneming aan een andere partij. | EMSO                                                         |
| IMIBRO                                                       | Distributiecentrum                                           | Activiteiten gericht op het vanaf een geconcentreerde locatie  verspreiden van goederen door een bedrijf. | EMSO                                                         |
| IMIBRO                                                       | Doelgroepengebouw                                            | Pand met een constructieve opzet gericht op het tijdelijk of  permanent onderbrengen van grotere groepen personen voor zorg, onderwijs,  detentie of militaire doeleinden. | EMSO                                                         |
| IMIBRO                                                       | Eindwoning                                                   | Eengezinswoning die grenst aan een aanliggende woning en die  ligt op het begin of einde van de reeks woningen zonder (extra) bij de woning  behorende grond aan de zijkant van de woning. | EMSO                                                         |
| IMIBRO                                                       | Energiecentrale                                              | Pand met een constructie die het mogelijk maakt om daarbinnen  centraal energie op te wekken. | EMSO                                                         |
| IMIBRO                                                       | Energievoorziening                                           | Levering van elektriciteit en warmte aan consumenten en  bedrijven. | EMSO                                                         |
| IMIBRO                                                       | Erfconstructie                                               | Een met de aarde verbonden duurzaam en vrijstaand bouwwerk (op  het achtererf), waarvan de grondoppervlakte op basis van de maaiveld  geometrie kleiner is dan 5 m². | IMIBRO                                                       |
| IMIBRO                                                       | Fabriek                                                      | Bedrijfsgebouw dat constructief is vormgegeven zodat  daarbinnen op grote schaal stoffen of goederen geproduceerd kunnen worden. | EMSO                                                         |
| IMIBRO                                                       | Fabrieksschoorsteen                                          | Losstaand hoog stenen kanaal bedoeld voor het afvoeren van  verbrandingsgassen. | EMSO                                                         |
| IMIBRO                                                       | Fort                                                         | Naar alle zijden tegen vijandelijke aanvallen verdedigbaar  militair gebouw dat van oorsprong is ingericht om een eenheid militairen te  herbergen. | EMSO                                                         |
| IMIBRO                                                       | Functiezone                                                  | De grootst mogelijke clustering van (aaneengesloten) ruimten  met dezelfde functie en op dezelfde bouwlaag, die volledig binnen de  afbakening van een Pand (inclusief Panddelen) ligt. | IMIBRO                                                       |
| IMIBRO                                                       | FunctioneleRuimte                                            | Ruimte met een specifieke functie.                           | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | Galerijflatwoning                                            | Flatwoning waarbij de voordeur uitkomt op een aan de  buitenkant gelegen loopgang. | EMSO                                                         |
| IMIBRO                                                       | Garage                                                       | Bijgebouw met een constructie gericht op het kunnen stallen  van motorvoertuigen op meer dan twee wielen ter ondersteuning van een  woonfunctie. | EMSO                                                         |
| IMIBRO                                                       | Gasverdeelstation                                            | Drukverlaging van aardgas in een netwerk ten behoeve van  toevoer in een lokaal net. | EMSO                                                         |
| IMIBRO                                                       | Gebedsgebouw                                                 | Pand dat zodanig is ontworpen dat het primair geschikt is voor  het houden van religieuze bijeenkomsten. | EMSO                                                         |
| IMIBRO                                                       | Gebouw                                                       | Overdekte en geheel of gedeeltelijk met wanden omsloten  constructie bedoeld voor het in een afgeschermde omgeving onderbrengen van  mensen, dieren of voorwerpen of voor de productie van goederen. | nen 3610                                                     |
| IMIBRO                                                       | Gebruikzone                                                  | Een Gebruikzone is het samenstel van de grootst mogelijke  clustering van (aaneengesloten) ruimten op dezelfde bouwlaag binnen een Pand  (inclusief Panddelen), waarvoor geldt dat deze deel uit maakt van een  zelfstandige eenheid van gebruik. | IMIBRO                                                       |
| IMIBRO                                                       | Gehucht                                                      | Kleine bebouwingskern die bestaat uit een concentratie van  aaneengesloten bebouwing. | EMSO                                                         |
| IMIBRO                                                       | Gemaalgebouw                                                 | Pand dat is ingericht om de installaties te herbergen die  nodig zijn voor het van een lager naar een hoger niveau brengen van water. | EMSO                                                         |
| IMIBRO                                                       | Gemeentegebied                                               | Afgebakend gedeelte van het grondgebied van Nederland, onder  zeggenschap van een openbaar lichaam met diverse bestuurlijke taken,  ingesteld op basis van artikel 123 en 124 van de Grondwet, artikel 2:1  Burgerlijk Wetboek en artikel 3 van de Wet algemene regels herindeling. | Grondwet en Gemeentewet                                      |
| IMIBRO                                                       | Gemeentekantoor                                              | Directe dienstverlening vanuit een gemeente aan inwoners en  bedrijven. | EMSO                                                         |
| IMIBRO                                                       | GeografischeRuimte                                           | Ruimte die bekendstaat onder een vanuit de historie of het  gebruik bekende benaming of een fysisch-geografische samenhang, al dan niet  met zijn omgeving, kent. | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | GeoObject                                                    | Een fenomeen in de werkelijkheid dat direct of indirect is  geassocieerd met een locatie relatief ten opzichte van de aarde. | nen 3610                                                     |
| IMIBRO                                                       | GeschakeldeTweeOnderEenKapWoning                             | 2-onder-1-kapwoning waarbij de muren van aanbouwen  gedeeltelijk aan (aanbouwen van) andere woningen grenzen. | EMSO                                                         |
| IMIBRO                                                       | GeschakeldeWoning                                            | Eengezinswoning waarbij de muren of muren van aanbouwen  gedeeltelijk aan (aanbouwen van) andere woningen grenzen. | EMSO                                                         |
| IMIBRO                                                       | Gevangenis                                                   | Pand dat zodanig constructief is vormgegeven dat daarbinnen  personen in verzekerde bewaring kunnen worden gesteld om een gevangenisstraf  uit te zitten. | EMSO                                                         |
| IMIBRO                                                       | Gezondheidszorgfunctie                                       | Gebruiksfunctie voor medisch onderzoek, verpleging, verzorging  of behandeling. | Bbl                                                          |
| IMIBRO                                                       | Groothandel                                                  | Bedrijfsmatige levering van fysieke goederen aan  bedrijfsmatige afnemers. | EMSO                                                         |
| IMIBRO                                                       | Grossier                                                     | Activiteiten gericht op het in grote partijen inkopen van  goederen en deze als tussenhandelaar doorverkopen aan detailhandel of andere  professionele grootverbruikers. | EMSO                                                         |
| IMIBRO                                                       | Hangar                                                       | Bedrijfsgebouw met een omvang en constructie gericht op het  produceren, onderhouden of stallen van vliegtuigen en/of helikopters. | EMSO                                                         |
| IMIBRO                                                       | Horeca                                                       | Verstrekken van logies en/of bereide maaltijden, snacks en  dranken aan gasten voor onmiddellijke consumptie. | EMSO                                                         |
| IMIBRO                                                       | Hotel                                                        | Dienstverlening gericht op het met een commercieel oogmerk  aanbieden van overnachtingen. | EMSO                                                         |
| IMIBRO                                                       | Industrie                                                    | Met een hoge graad van mechanisering en automatisering  produceren van materiële goederen of artikelen. | EMSO                                                         |
| IMIBRO                                                       | Industriefunctie                                             | Gebruiksfunctie voor het bedrijfsmatig bewerken of opslaan van  materialen en goederen, of voor bedrijfsmatige agrarische doeleinden. | Bbl                                                          |
| IMIBRO                                                       | Industriekern                                                | Van openbare wegen voorziene bebouwingskern die voor het  grootste gedeelte bestaat uit gebouwen die gebruikt worden voor  bedrijfsmatige activiteiten. | EMSO                                                         |
| IMIBRO                                                       | Installatie                                                  | Constructie die een technisch samenhangend systeem betreft dat  een bepaald doel dient. | Gebaseerd op installatie in IMGeo 2.2                        |
| IMIBRO                                                       | Installatiegebouw                                            | Pand met een constructieve opbouw gericht op het binnen het  gebouw onderbrengen van specifieke technische installaties of voorzieningen. | EMSO                                                         |
| IMIBRO                                                       | InstitutioneelHuishouden                                     | Bedrijfsmatige huishoudelijke verzorging van een groep  personen. | EMSO                                                         |
| IMIBRO                                                       | Kantoor                                                      | Uitoefening van een bedrijf, beroep of dienst waarin geen  product wordt vervaardigd maar uitsluitend dienstverlening wordt bedreven. | EMSO                                                         |
| IMIBRO                                                       | Kantoorfunctie                                               | Gebruiksfunctie voor administratie.                          | Bbl                                                          |
| IMIBRO                                                       | Kantoorgebouw                                                | Pand met een constructieve opzet gericht op het daarbinnen  kunnen uitoefenen van administratieve werkzaamheden. | EMSO                                                         |
| IMIBRO                                                       | Kapel                                                        | Klein gebedsgebouw dat is vormgegeven om te kunnen fungeren  voor individuele bezinning. | EMSO                                                         |
| IMIBRO                                                       | Kas                                                          | Gebouw bestaande uit een structuur van meestal glas en metaal  die gebruikt wordt voor het commercieel kweken van planten in een beschermde  omgeving op een natuurlijke of kunstmatige ondergrond. | EMSO                                                         |
| IMIBRO                                                       | Kasteel                                                      | Versterkt en te verdedigen gebouw dat van oorsprong is bedoeld  voor bewoning. | EMSO                                                         |
| IMIBRO                                                       | Kazerne                                                      | Pand met een constructie gericht op het kunnen huisvesten van  militairen. | EMSO                                                         |
| IMIBRO                                                       | Kerkgebouw                                                   | Gebedsgebouw met een constructie gericht op het houden van  christelijke erediensten. | EMSO                                                         |
| IMIBRO                                                       | Klokkentoren                                                 | Toren bedoeld voor de ophanging van een uurwerk en/of  klokkenspel. | EMSO                                                         |
| IMIBRO                                                       | Klooster                                                     | Gebedsgebouw bedoeld voor huisvesting en eventueel het  voorzien in levensonderhoud van een geloofsgemeenschap. | EMSO                                                         |
| IMIBRO                                                       | Knoop                                                        | Vertegenwoordigt een belangrijke positie in het netwerk die  altijd voorkomt aan het begin of het einde van een verbinding. | D2.10.1 INSPIRE Data Specifications – Base Models – Generic Network Model |
| IMIBRO                                                       | Koelcel                                                      | Activiteiten gericht op het opzettelijk gekoeld houden ten  behoeve van de opslag van producten. | EMSO                                                         |
| IMIBRO                                                       | Kolom                                                        | Een verticaal, of bijna verticaal, constructiedeel dat door  compressie het gewicht van de constructie erboven overdraagt op andere  constructie-elementen eronder. | IMIBRO                                                       |
| IMIBRO                                                       | Kunst                                                        | Activiteiten waarin met behulp van vaardigheden en verbeelding  unieke creatieve producten worden gecreëerd. | EMSO                                                         |
| IMIBRO                                                       | Laadperron                                                   | Tegen het gebouw aangebrachte constructie die is bedoeld voor  het kunnen laden en lossen van voertuigen. | EMSO                                                         |
| IMIBRO                                                       | Laboratorium                                                 | Natuurwetenschappelijke werkplaats voor het maken of  onderzoeken van stoffen. | EMSO                                                         |
| IMIBRO                                                       | LatereAanbouw                                                | Panddeel wat een latere aanbouw (niet zijnde een serre) of  opbouw ten opzichte van de oorspronkelijke constructie van het gebouw betreft  waarin het panddeel is gelegen. | IMIBRO                                                       |
| IMIBRO                                                       | Logiesfunctie                                                | Gebruiksfunctie voor het bieden van recreatief verblijf of  tijdelijk onderdak aan personen. | Bbl                                                          |
| IMIBRO                                                       | Loods                                                        | Groot en hoog gebouw met veelal grote inrijdeuren bedoeld voor  het opslaan van handels- of industriële goederen. | EMSO                                                         |
| IMIBRO                                                       | Loopbrug                                                     | Constructie bedoeld voor het op hoogte verbinden van twee bij  elkaar liggende gebouwen zodat een oversteek van het ene naar het andere  gebouw kan plaatsvinden. | EMSO                                                         |
| IMIBRO                                                       | Magazijn                                                     | Tijdelijke opslag van goederen.                              | EMSO                                                         |
| IMIBRO                                                       | Maisonnette                                                  | Specifiek type flatwoning waarbij de woning zelf twee of meer  bouwlagen heeft en de voordeur uitkomt op een gemeenschappelijke loopgang, op  een gemeenschappelijk afsluitbaar trappenhuis, een centrale hal of gesloten  portiek. | EMSO                                                         |
| IMIBRO                                                       | Manege                                                       | Beoefening van het paardrijden in een besloten omgeving.     | EMSO                                                         |
| IMIBRO                                                       | Metrostation                                                 | Gebruiksgebied dat bedoeld is voor het in- en uitstappen in  metrovoertuigen. | EMSO                                                         |
| IMIBRO                                                       | Molen                                                        | Bedrijfsgebouw dat gekenmerkt wordt door het in een aan het  gebouw aanwezig zijn van een draaiend mechaniek waarbij wind wordt omgezet in  rotatie-energie van de op het gebouw aanwezige wieken. | EMSO                                                         |
| IMIBRO                                                       | Moskee                                                       | Gebedsgebouw met een constructie gericht op islamitische  geloofsuitoefening. | EMSO                                                         |
| IMIBRO                                                       | Multigebouw                                                  | Pand met een constructie gericht op het daarbinnen kunnen  vormen van meerdere op wonen en/of bedrijfsmatige activiteiten gerichte  gebruikseenheden. | EMSO                                                         |
| IMIBRO                                                       | Munitiedepot                                                 | Opslagplaats voor munitie en explosieven.                    | EMSO                                                         |
| IMIBRO                                                       | Museum                                                       | Activiteiten gericht op het bijeenbrengen en (ten minste voor  een gedeelte) voortdurend voor het publiek uitstallen van materiële en  immateriële getuigenissen van de mens en zijn omgeving. | EMSO                                                         |
| IMIBRO                                                       | Netwerk                                                      | Een verzameling netwerkelementen.                            | D2.10.1 INSPIRE Data Specifications – Base Models – Generic Network Model |
| IMIBRO                                                       | Netwerkelement                                               | Een element in een netwerk. Elk element in een netwerk biedt  een functie die van belang is in het netwerk. | D2.10.1 INSPIRE Data Specifications – Base Models – Generic Network Model |
| IMIBRO                                                       | Netwerkverwijzing                                            | Een verwijzing naar een netwerkelement.                      | D2.10.1 INSPIRE Data Specifications – Base Models – Generic Network Model |
| IMIBRO                                                       | Nummeraanduiding                                             | Door het bevoegde gemeentelijke orgaan als zodanig toegekende  aanduiding van een verblijfsobject of een benoemde plaats. | Artikel 1 Wet basisregistraties adressen en gebouwen, Catalogus BAG 2018 |
| IMIBRO                                                       | Object                                                       | Een fenomeen in de werkelijkheid dat direct of indirect is  geassocieerd met een locatie relatief ten opzichte van de aarde. | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | Observatorium                                                | Waarnemingen in de ruimte.                                   | EMSO                                                         |
| IMIBRO                                                       | Onderwijs                                                    | Activiteiten gericht op het overbrengen van kennis,  vaardigheden en attitudes met vooraf vastgelegde doelen. | EMSO                                                         |
| IMIBRO                                                       | Onderwijsfunctie                                             | Gebruiksfunctie voor het geven van onderwijs.                | Bbl                                                          |
| IMIBRO                                                       | OpenbaarLichaam                                              | Een openbaar lichaam is, in de bestuurlijke indeling van het  Koninkrijk der Nederlanden, een overheidsorganisatie met publiekrechtelijke  rechtspersoonlijkheid, die bepaalde taken uitvoert binnen een bepaald  ruimtelijk gebied of op een bepaald inhoudelijk gebied. | Wikipedia                                                    |
| IMIBRO                                                       | OpenbareRuimte                                               | Door het bevoegde gemeentelijke orgaan als zodanig aangewezen  en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen. | Artikel 1 Wet basisregistratie adressen en gebouwen          |
| IMIBRO                                                       | Opslag                                                       | Activiteiten gericht op het voor kortere of langere tijd  bewaren van goederen. | EMSO                                                         |
| IMIBRO                                                       | Opslagfunctie                                                | Ruimte voor het stallen en opslaan.                          | IMIBRO                                                       |
| IMIBRO                                                       | Overkapping                                                  | Afzonderlijk staande overdekking rustend op kolommen.        | EMSO                                                         |
| IMIBRO                                                       | Paleis                                                       | Ambtsverblijf dat een openbare of ceremoniële functie heeft. | EMSO                                                         |
| IMIBRO                                                       | Pand                                                         | Bouwwerk, dat overdekt is en een geheel of grotendeels met  wanden omsloten constructief zelfstandige eenheid vormt, bedoeld voor het in  een afgeschermde omgeving onderbrengen van mensen, dieren of voorwerpen of  voor de productie van goederen. Een pand bestaat uit minimaal één Panddeel  (type: basisconstructie). | [IMIBRO 1.0.0.]                                              |
| IMIBRO                                                       | Panddeel                                                     | Een Panddeel is een niet vrijstaand deel van (de constructie)  van een Pand dat wordt onderscheiden omdat het op een ander moment onderdeel  is geworden van dat Pand dan andere panddelen of omdat de aard van de  bouwkundige constructie voldoet aan bepaalde criteria. | IMIBRO                                                       |
| IMIBRO                                                       | Parkeergarage                                                | Open constructie die geheel of gedeeltelijk in gebruik is als  voorziening voor het parkeren van voertuigen. | EMSO                                                         |
| IMIBRO                                                       | Parkeergaragezone                                            | Openbare voorziening voor het parkeren van voertuigen.       | EMSO                                                         |
| IMIBRO                                                       | Peilmeetstation                                              | Meting van landelijke of regionale waterstanden via het  Monitoring Systeem Water met behulp van een Digitaal Niveau Meter (DNM). | EMSO                                                         |
| IMIBRO                                                       | Personeelshuisvesting                                        | Woonruimte die specifiek bedoeld is voor het onderbrengen van  personeel van een bepaalde organisatie. | EMSO                                                         |
| IMIBRO                                                       | Podiumkunst                                                  | Publieke uitgaansgelegenheid bedoeld voor vormen van kunst die  uitgevoerd worden op een podium in de aanwezigheid van publiek. | EMSO                                                         |
| IMIBRO                                                       | Politiebureau                                                | Dienstverlening door de politie aan de samenleving.          | EMSO                                                         |
| IMIBRO                                                       | Pompstation                                                  | Op- of doorpompen van vloeistoffen door middel van een  installatie. | EMSO                                                         |
| IMIBRO                                                       | Portiekflatwoning                                            | Flatwoning waarbij de voordeur uitkomt op een  gemeenschappelijk afsluitbaar trappenhuis, een centrale hal of een gesloten  portiek. | EMSO                                                         |
| IMIBRO                                                       | Portiekwoning                                                | Etagewoning waarbij de voordeur uitkomt in een open portiek. | EMSO                                                         |
| IMIBRO                                                       | Productverwerking                                            | Activiteiten gericht op het verwerken van een product tot een  ander product. | EMSO                                                         |
| IMIBRO                                                       | Provinciegebied                                              | Afgebakend gedeelte van het grondgebied van Nederland, onder  zeggenschap van een openbaar lichaam met diverse bestuurlijke taken,  ingesteld op basis van artikel 123 en 124 van de Grondwet, artikel 2:1  Burgerlijk Wetboek en artikel 13 van de Wet algemene regels herindeling | Grondwet en Provinciewet                                     |
| IMIBRO                                                       | Radarpost                                                    | Waarnemingen met behulp van radar om vliegtuigen en  scheepsbewegingen te observeren. | EMSO                                                         |
| IMIBRO                                                       | Rechtbank                                                    | Locatie van waaruit recht gesproken wordt.                   | EMSO                                                         |
| IMIBRO                                                       | Recreatie                                                    | Uitoefening van vormen van vrijetijdsbesteding die in  hoofdzaak geen lichamelijke beweging omvatten. | EMSO                                                         |
| IMIBRO                                                       | Recreatiegebouw                                              | Pand met een constructie die het mogelijk maakt dat daarbinnen  activiteiten kunnen plaatsvinden gericht op of ondersteunend aan sport,  cultuur of ontspanning. | EMSO                                                         |
| IMIBRO                                                       | Recreatiekern                                                | Bebouwingskern die voor het grootste gedeelte bestaat uit  gebouwen die gebruikt worden voor (verblijfs)recreatie. | EMSO                                                         |
| IMIBRO                                                       | ReeelObject                                                  | Geo-object dat zich geheel materieel manifesteert.           | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | RegistratieveRuimte                                          | Op basis van wet- of regelgeving afgebakende ruimte die als  eenheid geldt van politiek-bestuurlijke verantwoordelijkheid of voor  bedrijfsvoering. | NEN 3610:2022 nl                                             |
| IMIBRO                                                       | Religie                                                      | Activiteiten verbonden aan zingeving of het zoeken naar  betekenisvolle verbindingen, waarbij meestal een hogere macht, opperwezen of  god centraal staat. | EMSO                                                         |
| IMIBRO                                                       | Remise                                                       | Stallingsplaats voor trams en bussen in de nacht en andere  tijdstippen dat ze niet nodig zijn voor het vervoer van reizigers. | EMSO                                                         |
| IMIBRO                                                       | Rijksgebied                                                  | Het grondgebied van het Koninkrijk der Nederlanden           | EMSO                                                         |
| IMIBRO                                                       | Rioolgemaal                                                  | Activiteiten gericht op het binnen een rioolstelsel naar een  hoger peil brengen of over langere afstand transporteren van afvalwater. | EMSO                                                         |
| IMIBRO                                                       | Ruimte                                                       | Voor mensen toegankelijk deel van een gebouw, dat ten minste  aan de onderzijde en/of de bovenzijde wordt begrensd door een  scheidingsconstructie en dat een netto-hoogte heeft van tenminste 1,5 m. | [IBRO-begrip]                                                |
| IMIBRO                                                       | Schuur                                                       | Bijgebouw met een constructie gericht op het kunnen opslaan  van goederen ter ondersteuning van een woonfunctie. | EMSO                                                         |
| IMIBRO                                                       | Serre                                                        | Panddeel wat een serre betreft die al dan geen onderdeel  uitmaakt van de oorspronkelijke constructie van het pand waarin het panddeel  is gelegen. | EMSO                                                         |
| IMIBRO                                                       | Sport                                                        | Activiteiten gericht op lichamelijke oefeningen en ontspanning  waarbij vaardigheid, kracht en inzicht vereist worden. | EMSO                                                         |
| IMIBRO                                                       | Sportfunctie                                                 | Gebruiksfunctie voor het beoefenen van sport.                | Bbl                                                          |
| IMIBRO                                                       | Sportgebouw                                                  | Pand met een specifieke constructie die is bedoeld om het  mogelijk te maken om binnensporten te kunnen beoefenen. | EMSO                                                         |
| IMIBRO                                                       | Stal                                                         | Bedrijfsgebouw met een constructie gericht op het daarbinnen  onderbrengen van vee. | EMSO                                                         |
| IMIBRO                                                       | Station                                                      | Gebruiksgebied dat bedoeld is voor het in- en uitstappen in  treinen. | EMSO                                                         |
| IMIBRO                                                       | Strandpaviljoen                                              | Verstrekken van bereide maaltijden, snacks en dranken aan  gasten voor onmiddellijke consumptie vanuit een op het strand gelegen  voorziening. | EMSO                                                         |
| IMIBRO                                                       | Streek                                                       | Geografische ruimte met een culturele samenhang die vanuit de  historie of in de volksmond bekend staat onder een bepaalde naam. | Gebaseerd op Basisregistratie Topografie: Catalogus en  Productspecificaties (versie 1.2.0.1) |
| IMIBRO                                                       | Subbuurt                                                     | Een subbuurt is, zo mogelijk, een samenhangend sociaal geheel,  omsloten door natuurlijke grenzen (zoals brede wegen en waterlopen). Samen  vormen zij een Buurt. | Handboek Territoriale Indeling Rotterdam v8.0                |
| IMIBRO                                                       | Subbuurtdeel                                                 | Subbuurtdeel ontstaat als subbuurten te groot zijn voor  technisch en administratief beheer. Een subbuurtdeel is, zo mogelijk, een  samenhangend sociaal geheel, omsloten door natuurlijke grenzen (zoals brede  wegen en waterlopen). Samen vormen zij een Subbuurt. | Handboek Territoriale Indeling Rotterdam v8.0                |
| IMIBRO                                                       | Synagoge                                                     | Gebedsgebouw met een constructie gericht op joodse  geloofsuitoefening. | EMSO                                                         |
| IMIBRO                                                       | Techniek                                                     | Activiteiten waarin de ontwikkeling of het gebruik van  apparaten, machines en andere complexe voorwerpen centraal staat. | EMSO                                                         |
| IMIBRO                                                       | TechnischeFunctie                                            | Ruimte voor het plaatsen van technische voorzieningen.       | IMIBRO                                                       |
| IMIBRO                                                       | Telecommunicatie                                             | Activiteiten gericht op het in stand houden van voorzieningen  die benodigd zijn voor het op afstand met behulp van elektronische middelen  kunnen communiceren. | EMSO                                                         |
| IMIBRO                                                       | Tempel                                                       | Gebedsgebouw met een constructie gericht op  niet-abrahamitische geloofsuitoefening. | EMSO                                                         |
| IMIBRO                                                       | Toegangspunt                                                 | Een voorziening die vanaf de openbare weg, een erf of een  gedeelde verkeersruimte toegang geeft tot een object. | EMSO                                                         |
| IMIBRO                                                       | Toegangstrap                                                 | Buiten de gevel geplaatste trapconstructie die toegang biedt  tot een gebouw en vast verbonden is met dat gebouw. | EMSO                                                         |
| IMIBRO                                                       | Tol                                                          | Tolheffing ten behoeve van het gebruik van verkeers- of  waterwegen. | EMSO                                                         |
| IMIBRO                                                       | Toren                                                        | Pand met een constructie waarbij de verhouding van de hoogte  ten opzichte van lengte en breedte karakteristiek is voor de  verschijningsvorm. | EMSO                                                         |
| IMIBRO                                                       | Transformatorstation                                         | Transformeren van elektrische wisselspanning van hoge naar  lage spanning en andersom. | EMSO                                                         |
| IMIBRO                                                       | Tuinbouw                                                     | Op commerciële basis op intensieve wijze telen van groenten,  paddenstoelen, fruit, bloemen, planten, bomen, bollen of zaden. | EMSO                                                         |
| IMIBRO                                                       | Tussenwoning                                                 | Eengezinswoning waarbij de tussenmuren aan andere panden  grenzen en waarbij de woningen ten opzichte van elkaar in een gelijk vlak of  lijn liggen. | EMSO                                                         |
| IMIBRO                                                       | TweeOnderEenKapWoning                                        | Eengezinswoning waarvan het hoofdgebouw is verbonden met het  hoofdgebouw van één andere gelijksoortige en gelijkvormige woning (niet  zijnde een tussenwoning). | EMSO                                                         |
| IMIBRO                                                       | Uitkijktoren                                                 | Hoge open constructie die ontworpen is om vanuit een hoog punt  de wijde omgeving te kunnen bekijken en/of bewaken. | EMSO                                                         |
| IMIBRO                                                       | Veehouderij                                                  | Bedrijfsmatige activiteiten gericht op het houden van vee ten  behoeve van het verkrijgen van melk, eieren of vlees. | EMSO                                                         |
| IMIBRO                                                       | Veiligheidsregiogebied                                       | Afgebakend gedeelte van het grondgebied van Nederland, onder  zeggenschap van een openbaar lichaam met diverse bestuurlijke taken,  ingesteld op basis van artikel 9 van de Wet Veiligheidsregio’s | Wet Veiligheidsregio’s                                       |
| IMIBRO                                                       | Veiling                                                      | Activiteiten gericht op het op grote schaal openbaar verkopen  van goederen. | EMSO                                                         |
| IMIBRO                                                       | Verbinding                                                   | Netwerkelement dat twee posities met elkaar verbindt en een  homogeen pad in het netwerk voorstelt. De verbonden posities kunnen worden  voorgesteld als knopen. | D2.10.1 INSPIRE Data Specifications – Base Models – Generic Network Model |
| IMIBRO                                                       | Verblijfsobject                                              | Een clustering van gebruikzones die samen een zelfstandige  gebruikseenheid vormen. | IMIBRO                                                       |
| IMIBRO                                                       | Verkeersfunctie                                              | Ruimte bestemd voor het bereiken van een andere ruimte.      | IMIBRO                                                       |
| IMIBRO                                                       | Verkeerstoren                                                | Punt van waaruit verkeersregulatie te land, ter zee of in de  lucht plaatsvindt. | EMSO                                                         |
| IMIBRO                                                       | Vestingsgebouw                                               | Pand met een constructie die het mogelijk maakt om aanvallen  van buiten het gebouw te kunnen weerstaan. | EMSO                                                         |
| IMIBRO                                                       | Viskwekerij                                                  | Vorm van aquacultuur, waarbij vissen op een commerciële manier  worden gekweekt voor consumptie. | EMSO                                                         |
| IMIBRO                                                       | Voertuigen                                                   | Bedrijfsmatige stalling of opstelpunt van voertuigen.        | EMSO                                                         |
| IMIBRO                                                       | Voertuigenstalling                                           | Pand met een constructie gericht op het bedrijfsmatig kunnen  stallen van voertuigen. | EMSO                                                         |
| IMIBRO                                                       | VrijstaandeWoning                                            | Eengezinswoning die los staat van (eventueel) aanwezige andere  objecten. | EMSO                                                         |
| IMIBRO                                                       | Vuurtoren                                                    | Toren bedoeld als drager van een ter oriëntatie van schepen  dienend licht. | EMSO                                                         |
| IMIBRO                                                       | Wasstraat                                                    | Dienstverlening in de vorm van mechanische reiniging van de  buitenzijde van voertuigen. | EMSO                                                         |
| IMIBRO                                                       | Watertoren                                                   | Toren die oorspronkelijk is bedoeld voor de opslag van  drinkwater in een bovenin het gebouw gelegen waterreservoir. | EMSO                                                         |
| IMIBRO                                                       | Werf                                                         | Werkplaats waar schepen worden gebouwd of hersteld.          | EMSO                                                         |
| IMIBRO                                                       | Wijk                                                         | Aaneengesloten gedeelte van het grondgebied van een gemeente,  waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaalgeografische  kenmerken. | GFO Basisgegevens                                            |
| IMIBRO                                                       | Winkelfunctie                                                | Gebruiksfunctie voor het verhandelen van materialen, goederen  of diensten. | Bbl                                                          |
| IMIBRO                                                       | Wonen                                                        | Permanent verblijf van personen voor niet bedrijfsmatige  activiteiten. | EMSO                                                         |
| IMIBRO                                                       | Woonfunctie                                                  | Gebruiksfunctie voor het wonen.                              | Bbl                                                          |
| IMIBRO                                                       | Woongebouw                                                   | Pand met een constructie die primair geschikt voor bewoning. | EMSO                                                         |
| IMIBRO                                                       | Woonkern                                                     | Van openbare wegen voorziene bebouwingskern die voor het  grootste gedeelte bestaat uit gebouwen die gebruikt worden voor wonen. | EMSO                                                         |
| IMIBRO                                                       | Woonplaats                                                   | Door het bevoegde gemeentelijke orgaan als zodanig aangewezen  en van een naam voorzien gedeelte van het grondgebied van de gemeente. | Artikel 1 Wet basisregistratie adressen en gebouwen          |
| IMIBRO                                                       | Ziekenhuis                                                   | Onderzoek, behandeling en verpleging van patiënten in het  kader van professionele gezondheidszorg. | EMSO                                                         |
| IMIBRO                                                       | Zorg                                                         | Bieden van lichamelijke of geestelijke hulp of aandacht.     | EMSO                                                         |
| IMIBRO                                                       | Zorgcomplex                                                  | Alle bij een ziekenhuis / zorginstellingslocatie behorende  begroeiing, verharding en gebouwen. | IMIBRO                                                       |
| IMIBRO                                                       | Zwembadzone                                                  | Openbaar toegankelijke zwemactiviteiten.                     | EMSO                                                         |
| IMKAD                                                        | Appartementsrecht                                            | aandeel in goederen die in een splitsing zijn betrokken, dat  de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van  het gebouw die blijkens hun inrichting bestemd zijn of worden om als  afzonderlijk geheel te worden gebruikt | [IMKAD]                                                      |
| IMKAD                                                        | AppartementsrechtSplitsing                                   | het in appartementsrechten gesplitste Zakelijk recht van 1 of  meer kadastrale objecten. | [IMKAD]                                                      |
| IMKAD                                                        | BeperkingsGebied                                             | geen                                                         | [IMKAD]                                                      |
| IMKAD                                                        | KadastraalObject                                             | goed waarvoor bij overdracht of vestiging van rechten  inschrijving in de openbare registers van het Kadaster is vereist | [IMKAD]                                                      |
| IMKAD                                                        | KadastraleGrens                                              | de weergave van een grens op de kadastrale kaart die door de  dienst van het Kadaster tussen percelen vastgesteld wordt, op basis van  inlichtingen van belanghebbenden en met gebruikmaking van de aan de  kadastrale kaart ten grondslag liggende bescheiden die in elk geval de  landmeetkundige gegevens bevatten van hetgeen op die kaart wordt weergegeven | [IMKAD]                                                      |
| IMKAD                                                        | LocatieKadastraalObject                                      | aanduiding voor de locatie van het Kadastraal object in  Nederland. | [IMKAD]                                                      |
| IMKAD                                                        | Mandeligheid                                                 | het ontstaan van een gemeenschappelijk eigendom van een  onroerende zaak, van eigenaars van twee of meer erven, doordat de bestemming  van het gemeenschappelijk nut is vastgelegd in een tussen de eigenaars  opgemaakte notariële akte en dat deze akte is ingeschreven in de openbare  registers. | [IMKAD]                                                      |
| IMKAD                                                        | ObjectLocatieBinnenland                                      | aanduiding voor de locatie van het Kadastraal object in  Nederland. | [IMKAD]                                                      |
| IMKAD                                                        | OnroerendeZaak                                               | de grond, de niet gewonnen delfstoffen, de met de grond  verenigde beplantingen, alsmede de gebouwen en werken die duurzaam met de  grond zijn verenigd, hetzij rechtstreeks, hetzij door vereniging met andere  gebouwen of werken | [IMKAD]                                                      |
| IMKAD                                                        | OnroerendeZaakBeperking                                      | OnroerendeZaakBeperking                                      | [IMKAD]                                                      |
| IMKAD                                                        | Perceel                                                      | begrensd deel van het Nederlands grondgebied dat kadastraal  geïdentificeerd is en met kadastrale grenzen begrensd is. | [IMKAD]                                                      |
| IMKAD                                                        | PubliekrechtelijkeBeperking                                  | PubliekrechtelijkeBeperking                                  | [IMKAD]                                                      |
| IMKAD                                                        | WerkingsGebied                                               | geen                                                         | [IMKAD]                                                      |
| IMKAD                                                        | ZakelijkRecht                                                | absoluut recht op een kadastraal object dat tegenover iedereen  te handhaven is. | [IMKAD]                                                      |
| IMVG                                                         |                                                              |                                                              | [IMVG]                                                       |
| IMWOZ                                                        | Waarde                                                       | De op grond van de Wet WOZ vastgestelde waarde van het  WOZ-object naar de genoemde waardepeildatum. | [IMWOZ]                                                      |
| IMWOZ                                                        | WOZDeelobject                                                | Fysieke onderdelen van het WOZ-object die bij de taxatie of de  onderbouwing van de taxatie afzonderlijk meegenomen worden. | [IMWOZ]                                                      |
| IMWOZ                                                        | WOZObject                                                    | De onroerende zaak waarvan op grond van de Wet WOZ de waarde  moet worden bepaald en vastgesteld. | [IMWOZ]                                                      |
| IndoorGML                                                    | CellBoundary                                                 | Explicit boundary of cell space, to which we may assign  additional properties such as material, texture, etc. | [IndoorGML]                                                  |
| IndoorGML                                                    | CellSpace                                                    | The basic unit of indoor space, such as room and corridor, the  union of which makes the entire indoor space | [IndoorGML]                                                  |
| IndoorGML                                                    | Edge                                                         | Adjacency or connectivity relationship between nodes, which is  defined as 1-dimensional topological primitive in ISO 19107. | [IndoorGML]                                                  |
| IndoorGML                                                    | GeneralSpace                                                 | A type of NavigableSpace such as rooms, lobbies, kitchen,  etc., where agents can stay or use for a longer period of time and can serve  as starting and target cell in navigation. | [IndoorGML]                                                  |
| IndoorGML                                                    | NavigableBoundary                                            | A type of CellBoundary, which agents can pass through.       | [IndoorGML]                                                  |
| IndoorGML                                                    | NavigableSpace                                               | A cell space in which users cannot move                      | [IndoorGML]                                                  |
| IndoorGML                                                    | Node                                                         | Space abstraction of cell space in dual space to a point or  virtual point, which is defined as 0-dimensional topological primitive in ISO  19107. | [IndoorGML]                                                  |
| IndoorGML                                                    | NonNavigableBoundary                                         | A type of CellBoundary, which does not allow passage.        | [IndoorGML]                                                  |
| IndoorGML                                                    | NonNavigableSpace                                            | A cell space in which users can move freely                  | [IndoorGML]                                                  |
| IndoorGML                                                    | ObjectSpace                                                  | A type of NonNavigableSpace containing objects that make it  non-navigable | [IndoorGML]                                                  |
| IndoorGML                                                    | Route                                                        | A path to navigate between two nodes                         | [IndoorGML]                                                  |
| IndoorGML                                                    | TransferSpace                                                | A type of NavigableSpace that provides passages between  GeneralSpaces | [IndoorGML]                                                  |
| Informatiemodel  Funderingen                                 |                                                              |                                                              |                                                              |
| INREV                                                        |                                                              |                                                              |                                                              |
| Inspire?                                                     |                                                              |                                                              |                                                              |
| ISDE  (RVO-energie)                                          |                                                              |                                                              |                                                              |
| ISO19117                                                     |                                                              |                                                              |                                                              |
| Ketenstandaard                                               | Fysieke ruimte                                               | Een fysieke ruimte is een afgebakend gebied die materieel en  tastbaar begrensd is. Het is dus de ‘lucht’ tussen de vloeren en wanden. | presentatie Ketenstandaard nov. 26                           |
| KIS'(Ketenstandaard)                                         |                                                              |                                                              |                                                              |
| Land Administration Domain  Model (LADM)                     | LA_Parcel                                                    |                                                              |                                                              |
| LandInfra                                                    | CondominiumUnit                                              |                                                              |                                                              |
| LandInfra                                                    | Landparcel                                                   |                                                              |                                                              |
| LandInfra                                                    | Site                                                         |                                                              |                                                              |
| LVG                                                          | Aansluiting                                                  |                                                              |                                                              |
| LVG                                                          | Maatregel                                                    |                                                              |                                                              |
| LVG                                                          | MaatregelCategorie                                           |                                                              |                                                              |
| LVG                                                          |                                                              | zie ook IMVG'                                                |                                                              |
| materiaalpaspoort                                            |                                                              |                                                              |                                                              |
| meetinstructies  voor taxaties                               |                                                              |                                                              |                                                              |
| MiniBIM                                                      | Afnemer                                                      | (Beoogd) eigenaar.                                           | WOZ                                                          |
| MiniBIM                                                      | Atrium                                                       | Een centrale binnenruimte in een gebouw, omgeven door meerdere  verdiepingen, ontworpen om natuurlijk licht binnen te laten en een gevoel van  openheid te creëren. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Badruimte                                                    | Een ruimte in een gebouw met sanitair voor het nemen van baden  en douches, inclusief voorzieningen zoals een badkuip, douchebak, wastafel en  toilet, vaak voorzien van waterdichte materialen en afvoersystemen. De term  badruimte komt vanuit het bouwbesluit. In de volksmond wordt de ruimte op  plattegronden meestal aangeduid als badkamer. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Balkon                                                       | Een platform aan de buitenkant van een gebouw, vaak  ondersteund door balken of kolommen en voorzien van een balustrade voor  veiligheid, bedoeld voor recreatie of buitenactiviteiten, niet zijnde  verkeersruimten. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | BaseQuantities                                               | De basis-afmetingen van objecten zoals lengte, breedte, inhoud  etc. | BIPM                                                         |
| MiniBIM                                                      | Bedrijfsruimte                                               | Een enkele ruimte binnen een gebouw die is ontworpen voor  commerciële of zakelijke activiteiten, zoals winkels, zorgverlening,  fabrieken of werkplaatsen, meestal voorzien van specifieke infrastructuur en  voorzieningen voor de betreffende bedrijfsactiviteiten. Niet te verwarren met  kantoorruimten. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Bedruimte                                                    | Een verblijfsruimte voor 1 of meer bedden om te slapen, of  voor het verblijf van aan bed gebonden personen in deze ruimte. Denk aan een  slaapruimte in een crèche, hotelkamer of verpleegruimte in een ziekenhuis.  Niet te verwarren met slaapkamer. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Bepalingsmethode                                             | Wijze van meten.                                             | NEN 2580:2007 nl (o.a.)                                      |
| MiniBIM                                                      | Berging inpandig                                             | Een ruimte buiten de schil van de woning, maar binnen een  gebouw met ook andere functies. Vaak gebruikt voor het opslaan van goederen,  gereedschappen, fietsen, of andere items, vaak voorzien van planken, rekken  of kasten voor organisatie. Toegang niet vanuit de woning. Een berging in een  ander gebouw, is dus ook inpandig. Niet bestemd voor technische installaties. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Berging uitpandig                                            | Een al dan niet afgesloten ruimte buiten het gebouw. Losstaand  of in een cluster met enkel bergingen. Vaak gebruikt voor het opslaan van  goederen, gereedschappen, fietsen, of andere items, vaak voorzien van  planken, rekken of kasten voor organisatie. Niet bestemd voor technische  installaties. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Bergruimte                                                   | Een ruimte binnen de schil van een woning en/of met toegang  vanuit de woning. Vaak gebruikt voor het opslaan van goederen,  gereedschappen, of andere items, vaak voorzien van planken, rekken of kasten  voor organisatie. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Bijkeuken                                                    | Een (kleine) ruimte naast de keuken, vaak gebruikt voor het  opslaan van voorraad, schoonmaakartikelen, wasmachines, drogers en andere  huishoudelijke apparaten. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Bouwwerk                                                     | De ruimtelijke demarcatie van een bouwkundig en constructief  zelfstandige eenheid of een afsluitbaar deel van die eenheid. | VORM                                                         |
| MiniBIM                                                      | BouwwerkNummer                                               | Unieke nummering van bouwwerken.                             | VORM                                                         |
| MiniBIM                                                      | Bouwwerkperceel                                              | Perceel dat als uitgangspunt dient bij het toetsen van een  bouwwerk aan het BBL, de vergunningsaanvraag Omgevingsplantoets (OPA) of de  aanvraag Technische Activiteit (WKB). | BBL                                                          |
| MiniBIM                                                      | BouwwerkType                                                 | Enumeratie van bouwwerken.                                   | BBL/SOR                                                      |
| MiniBIM                                                      | Brandcompartiment                                            | Gedeelte van een of meer bouwwerken bestemd als maximaal  uitbreidingsgebied van brand. | BBL                                                          |
| MiniBIM                                                      | Buitenruimte                                                 | Een deel van een Bouwwerkperceel of een deel van een Bouwwerk  buiten de thermische schil dat permanent in open verbinding staat met de  bodem en/of de buitenlucht en toegankelijk is voor mensen of voor het stallen  van (motor)voertuigen. | NEN 2580:2007nl                                              |
| MiniBIM                                                      | BuitenruimteSoort                                            | Groepering van buitenruimten naar functie.                   | NEN 2580:2007nl                                              |
| MiniBIM                                                      | BuitenruimteType                                             | Enumeratie van buitenruimten.                                | Aedes/Geonovum                                               |
| MiniBIM                                                      | Carport                                                      | Een overdekte structuur naast een gebouw, met één of meer open  zijden, ontworpen om voertuigen te beschermen tegen weersinvloeden zoals  regen, sneeuw en zon. In tegenstelling tot een garage heeft een carport  meestal geen muren of deuren. Carports kunnen vrijstaand zijn of aan een  gebouw bevestigd worden. Onder carport vallen ook ander soortige overdekte  (buiten) parkeervakken, zoals die in de plint (begane grond) van een  appartementencomplex. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Categorie                                                    | Enumeratie van marktsegmenten.                               | VORM                                                         |
| MiniBIM                                                      | Cel                                                          | Een kleine afgesloten ruimte binnen een gebouw, vaak gebruikt  in gevangenissen, detentiecentra of politiebureaus voor het opsluiten van  individuen, met minimale voorzieningen voor comfort en veiligheid. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Corridor                                                     | Een gang in een gemeenschappelijke ruimte die toegang  verschaft tot meerdere gebruiksfuncties. | MiniBIM                                                      |
| MiniBIM                                                      | Dakterras                                                    | Een niet-geheel-overdekte buitenruimte, gelegen op de  dakconstructie van de onderliggende bouwlaag. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | EenheidNummer                                                | Unieke nummering van WOZ-objecten in een bouwwerk.           | VORM                                                         |
| MiniBIM                                                      | Eigendomseenheid                                             | Een onroerende zaak (b.v. woning) inclusief het perceel  (kavel) en externe panden (schuur, berging, garage etc) waarvoor een  WOZ-waarde wordt vastgesteld. | WOZ                                                          |
| MiniBIM                                                      | Elementen                                                    | Fysieke objecten die een Ruimte afbakenen en/of voor de  condities zorgen waardoor een beoogd gebruik mogelijk gemaakt wordt of die  een bouwkundige of constructieve functie vervullen. | VORM                                                         |
| MiniBIM                                                      | Entree                                                       | Ruimte tussen de toegangsdeur en een verkeersruimte. Deze  ruimte is van toeapssing op een gebouw en op een gebruiksfunctie. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Enumeratie                                                   | Waardelijst.                                                 | NEN 3610:2022 nl                                             |
| MiniBIM                                                      | Fietsenstalling inpandig                                     | Een ruimte binnen een gebouw die bedoeld is voor het parkeren  van fietsen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Fietsenstalling uitpandig                                    | Een al dan niet overdekte of afgesloten ruimte buiten het  gebouw die bedoeld is voor het parkeren van fietsen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Galerij                                                      | Een aan de buitenkant van een gebouw hangende open gang,  gebruikt als verbindingsroute tussen verschillende delen van het gebouw. Deze  verschaft toegang tot afzonderlijke gebruiksfuncties. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Gang                                                         | Een doorgangsruimte met lengte- breedte verhouding van 1:n.  Bevindt zich binnen een gebouw, gebruikt als verbindingsroute tussen  verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang wordt  verleend tot een gebruiksfunctie. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Garage inpandig                                              | Een inpandige garage is een garage die deel uitmaakt van een  gebouw. Deze ruimte is meestal direct toegankelijk vanuit het interieur van  het gebouw, bijvoorbeeld via een deur die leidt naar een gang, keuken, of  bijkeuken. De garage is voorzien van een garagedeur die naar buiten opent.  Een garage is gebonden aan een enkele woning, niet te verwarren met  parkeergarage. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Garage uitpandig                                             | Een uitpandige garage is een garage die geen deel uitmaakt van  het gebouw. Deze ruimte is niet direct toegankelijk vanuit het interieur van  het gebouw. De uitpandige garage is via de oprijlaan van de woonruimte te  bereiken en daarom betreft het een aanhorigheid van de woonruimte. De garage  is voorzien van een garagedeur die naar buiten opent. Een garage is gebonden  aan een enkele woning, niet te verwarren met parkeergarage. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Garagebox                                                    | Een garagebox is een afgesloten, individuele ruimte bedoeld  voor het stallen van een voertuig of het opslaan van goederen. Garageboxen  zijn voorzien van een garagedeur die op slot kan, vaak een kanteldeur of een  roldeur. Deze boxen kunnen losstaand zijn of deel uitmaken van een groter  complex met meerdere garageboxen. Een garagebox is een afzonderlijk object  van een woonruimte als het een vrijstaande garagebox is die middels een  afzonderlijk terrein bereikbaar is of als het een garagebox is die in de plint  (begane grond) van een appartementencomplex zit. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Gebied                                                       | Een zone in een Bouwwerk waarbinnen een bepaalde conditie  voorgeschreven wordt of een rechtsorde geldt en die beperkingen oplegt aan  het beoogd gebruik binnen dat Gebied. | VORM                                                         |
| MiniBIM                                                      | GebiedsSoort                                                 | Groepering van gebieden naar functie.                        | BBL (o.a.)                                                   |
| MiniBIM                                                      | GebiedsType                                                  | Enumeratie van gebieden.                                     | VORM                                                         |
| MiniBIM                                                      | Gebruiksbestemming                                           | Toegestaan gebruik van een gebruikseenheid: het gebruik.     | BBL                                                          |
| MiniBIM                                                      | Gebruikseenheid                                              | een gebruikseenheid is het kleinste, afgebakende stuk vastgoed  of benoemd terrein met een gebruiksfunctie dat wordt verhuurd, verkocht en/of  onderhouden of verkocht is. | CORA                                                         |
| MiniBIM                                                      | Gebruiksfunctie                                              | Gedeelten van een bouwwerk die dezelfde gebruiksbestemming  hebben en die samen een gebruikseenheid vormen: het object. | BBL                                                          |
| MiniBIM                                                      | Gemeenschappelijk verblijfsgebied                            | Gemeenschappelijke verblijfsgebied ten dienste van meerdere  gebruiksfuncties (gebruikseenheden). | BBL                                                          |
| MiniBIM                                                      | Gemeenschappelijke ruimte                                    | Gemeenschappelijke ruimten ten dienste van meerdere  gebruiksfuncties (gebruikseenheden), b.v. corridor, entreehal. | BBL                                                          |
| MiniBIM                                                      | Groepsruimte                                                 | Een verblijfsruimte in een kinderdagverblijf.                | MiniBIM                                                      |
| MiniBIM                                                      | Hal                                                          | Een doorgangsruimte met een nagenoeg gelijke lengte- breedte  verhouding. Bevindt zich binnen een gebouw, gebruikt als verbindingsroute  tussen verschillende ruimtes. Deze ruimte bevat geen deur waarmee toegang  wordt verleend tot een gebruiksfunctie | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Huiskamer                                                    | Een verblijfsruimte in een gemeenschappelijk verblijfsgebied,  meestal in een woongebouw. | MiniBIM                                                      |
| MiniBIM                                                      | IfcEntityClass                                               | Classificatie in Ifc van elementen en ruimten (entities).    | BuildingSmart                                                |
| MiniBIM                                                      | IfcSpace                                                     | Een IfcSpace is een ruimtelijk element in Ifc.               | BuildingSmart                                                |
| MiniBIM                                                      | IfcZone                                                      | Een IfcZone is een groepering van één of meerdere IfcSpace in  Ifc. | BuildingSmart                                                |
| MiniBIM                                                      | Kadastraalperceel                                            | Een begrensd deel van het Nederlands grondgebied dat  kadastraal geïdentificeerd is en met kadastrale grenzen begrensd is. | Kadaster                                                     |
| MiniBIM                                                      | Kantoorruimte                                                | Een enkele ruimte binnen een gebouw die specifiek is ontworpen  voor kantoorwerkzaamheden. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Kast                                                         | Een opbergruimte, behorende tot de aangrenzende ruimte,  onderdeel uitmakend van de bouwconstructie. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Kelder                                                       | Een (deels) ondergrondse ruimte onder de begane grond van een  gebouw, meestal gebruikt voor opslag, nutsvoorzieningen, wasruimte en soms  leefruimte. De toegang is via een trap of luik. In de kelder kan een  volwassen persoon rechtop staan. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Keuken                                                       | Een ruimte binnen een gebouw die is ontworpen en uitgerust  voor het bereiden van voedsel, voorzien van een keukenblok. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Kruipruimte                                                  | Een kruipruimte is een ondiepe, vaak ongebruikte ruimte onder  de vloer van een gebouw. De ruimte heeft een vrije hoogte van minder dan 1,5  meter (cf. NEN2580) en staat direct in verbinding met de buitenlucht of de  bodem. Deze ruimte, die meestal hoog genoeg is om in te kruipen maar te laag  om rechtop te staan, wordt gebruikt voor het leggen van leidingen, kabels en  isolatie. Meestal is deze niet verwarmd. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Lifthal                                                      | Een voorruimte die vanuit een verkeersruimte toegang geeft tot  een lift. | MiniBIM                                                      |
| MiniBIM                                                      | Liftmachineruimte                                            | Een aparte ruimte binnen een gebouw waarin de liftmachines,  aandrijvingen, regelapparatuur en veiligheidsvoorzieningen zich bevinden,  vaak gelegen boven of naast de liftschacht. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Liftschacht                                                  | De ruimte in een bouwkundige liftschacht.                    | MiniBIM                                                      |
| MiniBIM                                                      | Loggia                                                       | Een loggia is een inpandig balkon: een aan drie zijden gesloten buitenruimte die zich binnen het gevelvlak bevindt. De opening bevindt  zich in de gevel. De loggia heeft een borstwering. Meestal bevindt de loggia zich op de verdieping. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Meterruimte                                                  | Een ruimte binnen een gebouw waar meters voor gas,  elektriciteit, water, of andere nutsvoorzieningen worden geïnstalleerd en  onderhouden, meestal toegankelijk voor nutsbedrijven voor het aflezen en  onderhouden van de meters. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Nevengebruiksfunctie                                         | Een gebruiksfunctie die ten dienste staat van een andere  gebruiksfunctie. | BBL                                                          |
| MiniBIM                                                      | Objecttype                                                   | Groepering op hoogste abstractieniveau van gelijksoortige data  met overerfbare eigenschappen naar onderliggende subtypen. | -                                                            |
| MiniBIM                                                      | Onbenoemde ruimte                                            | Een ruimte zonder beoogd gebruik die bij de toets aan het BBL,  de vergunningsaanvraag Omgevingsplantoets (OPA) of de aanvraag Technische  Activiteit (WKB) buiten beschouwing dient te worden gelaten. | MiniBIM                                                      |
| MiniBIM                                                      | Opstelplaats auto                                            | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een auto. Dit is voor onbepaalde tijd en  kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats bakfiets                                        | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een bakfiets. Dit is voor onbepaalde tijd  en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats fiets hoog                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een fiets. Hoog, dus deze mag met tillen  of ander hulpmiddel te plaatsen zijn. Binnen de geldende regels. Dit is voor  onbepaalde tijd en kan dus ook zeer lang zijn. | MiniBIM                                                      |
| MiniBIM                                                      | Opstelplaats fiets laag                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een fiets. Laag, dus deze moet zonder  tillen of ander hulpmiddel te plaatsen zijn. Dit is voor onbepaalde tijd en  kan dus ook zeer lang zijn. | MiniBIM                                                      |
| MiniBIM                                                      | Opstelplaats koelkast                                        | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een koelkast. Dit is voor onbepaalde tijd  en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats kooktoestel                                     | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een kooktoestel. Dit is voor onbepaalde  tijd en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats motorfiets                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een motorfiets. Dit is voor onbepaalde  tijd en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats scooter                                         | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een scooter. Dit is voor onbepaalde tijd  en kan dus ook zeer lang zijn. | MiniBIM                                                      |
| MiniBIM                                                      | Opstelplaats scootmobiel                                     | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een scootmobiel. Dit is voor onbepaalde  tijd en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats vaatwasser                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een vaatwasser. Dit is voor onbepaalde  tijd en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats wasdroger                                       | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een wasdroger. Dit is voor onbepaalde tijd  en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Opstelplaats wasmachine                                      | Een opstelplaats is de aangewezen ruimte waar bepaalde  installaties, apparatuur of objecten worden geplaatst, opgesteld of  geparkeerd. In dit geval specifiek een wasmachine. Dit is voor onbepaalde  tijd en kan dus ook zeer lang zijn. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Orientatie                                                   | Hoofdrichting van een element, een ruimte of een buitenruimte. | Aedes                                                        |
| MiniBIM                                                      | Overige buitenruimte                                         | Een algemene term die wordt gebruikt voor ruimtes buiten een  gebouw die niet passen in andere categorieën. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Overige ruimte                                               | Een algemene term die wordt gebruikt voor ruimtes binnenin een  gebouw die niet passen in andere categorieën. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Overloop                                                     | Een overgangsgebied die ruimtes met een trap verbindt. Niet  gelegen op de onderste bouwlaag van een adres. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Parameter                                                    | Een parameter is een meetbare eigenschap waarmee een object  beschreven wordt. | -                                                            |
| MiniBIM                                                      | Parkeergarage niet-openbaar                                  | Een niet-openbare parkeergarage is een gebouwde  parkeervoorziening met meerdere parkeerplaatsen, soms verdeeld over meerdere  verdiepingen en kan zowel bovengronds als ondergronds (parkeerkelder) zijn.  Alleen toegankelijk voor specifieke gebruikers, zoals bewoners of werknemers.  Hoofdzakelijk bestemd voor vaste gebruikers zonder vaste parkeerplaats  (zwerfplek). | MiniBIM                                                      |
| MiniBIM                                                      | Parkeergarage openbaar                                       | Een openbare parkeergarage is een gebouwde parkeervoorziening  met meerdere parkeerplaatsen, soms verdeeld over meerdere verdiepingen en kan  zowel bovengronds als ondergronds (parkeerkelder) zijn. Toegankelijk voor het  algemene publiek, vaak tegen betaling, en bedoeld voor kort- of langparkeren.  Te gebruiken door meer dan 20 % niet-vaste gebruikers. Niet-vaste gebruikers  is hier algemeen publiek. | MiniBIM                                                      |
| MiniBIM                                                      | Parkeergarage stallingsgarage                                | Een stallingsgarage is een gebouwde parkeervoorziening met  meerdere parkeerplaatsen, soms verdeeld over meerdere verdiepingen en kan  zowel bovengronds als ondergronds (kelder) zijn. Gebruikt voor langdurig  stallen van voertuigen (bijvoorbeeld campers of oldtimers), vaak veilig en  bewaakt, en kan zowel openbaar als niet-openbaar zijn. Hoofdzakelijk bestemd  voor vaste gebruikers met vaste parkeerplaats met maximaal 80  parkeerplaatsen. | MiniBIM                                                      |
| MiniBIM                                                      | Parkeerplaats fiets hoog                                     | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een fiets, bovenin een rek. | [MiniBIM]                                                    |
| MiniBIM                                                      | Parkeerplaats fiets laag                                     | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een fiets, onderin een rek of op vloerniveau. | [MiniBIM]                                                    |
| MiniBIM                                                      | Parkeerplaats scooter                                        | Een parkeerplaats is een specifiek aangewezen plek, waar  voertuigen tijdelijk geparkeerd of gestald kunnen worden. In dit geval  specifiek een scooter. | [MiniBIM]                                                    |
| MiniBIM                                                      | Parkeerterrein                                               | Een parkeerterrein is een open, meestal verharde locatie die  speciaal is ingericht voor het parkeren van voertuigen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Patio                                                        | Een open binnenplaats of verharde ruimte buiten een gebouw,  omringd door muren. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | PMC                                                          | Standaardisatie van woningtypen en huurklassen: PMC (Product  Markt Combinatie). | NCB                                                          |
| MiniBIM                                                      | Rooksluis                                                    | Een voorruimte die vanuit een verkeersruimte toegang geeft tot  een trappenhuis met als doel het trappenhuis rookvrij te houden. | MiniBIM                                                      |
| MiniBIM                                                      | Ruimte                                                       | Een deel van een Bouwwerk met een beoogd gebruik (min. 1),  afgebakend door Fysieke Elementen. | VORM                                                         |
| MiniBIM                                                      | RuimteNummer                                                 | Unieke nummering van ruimten binnen een gebied.              | VORM                                                         |
| MiniBIM                                                      | RuimteSoort                                                  | Groepering van ruimten naar functie.                         | BBL                                                          |
| MiniBIM                                                      | RuimteType                                                   | Enumeratie van ruimten.                                      | Aedes                                                        |
| MiniBIM                                                      | Schacht                                                      | Een verticale doorgang of ruimte binnen een gebouw, gebruikt  voor ventilatie, bekabeling of leidingen vaak voorzien van brandwerende  materialen en afsluitingen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Serre                                                        | Een serre is een verwarmde binnenruimte die als (semi)  buitenruimte gebruikt kan worden en valt binnen de GO. Niet te verwarren met  een loggia, dat is een onverwarmde verglaasde buitenruimte. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Slaapkamer                                                   | Een ruimte binnen een gebouw die is ontworpen en bestemd voor  slapen. Niet te verwarren met een bedruimte. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Stalling inpandig                                            | Een afgesloten ruimte binnen een gebouw die bedoeld is voor  het parkeren of opslaan van gemotoriseerde (vaak elektrische) voertuigen,  niet zijnde auto's. Bijvoorbeeld scootmobielen, scooters of elektrische  fietsen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Stalling uitpandig                                           | Een al dan niet overdekte of afgesloten ruimte buiten het  gebouw die bedoeld is voor het parkeren of opslaan van gemotoriseerde (vaak  elektrische) voertuigen, niet zijnde auto's. Bijvoorbeeld scootmobielen,  scooters of elektrische fietsen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Subruimte                                                    | Een virtuele onderverdeling van een Ruimte, op basis van  beoogd gebruik (max. 1). | VORM                                                         |
| MiniBIM                                                      | Technische ruimte                                            | Een ruimte binnen een gebouw waar technische installaties  worden geplaatst en onderhouden, zoals Verwarmingsinstallaties, ventilatie-  of airconditioningsystemen, datacenters, of telecomapparatuur. Niet te  gebruiken als meterruimte of liftmachineruimte. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Terras                                                       | Een aan de woning verbonden bestrate buitenruimte met directe  verbinding met de bomen. Gelegen binnen de bouwconstructie zonder overstek,  en dat zich op de onderste woonlaag van de eenheid bevindt. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Terrein                                                      | Een deel van een stuk grond met een bepaalde functie of waar  een bepaalde rechtsorde geldt. | VORM                                                         |
| MiniBIM                                                      | TerreinType                                                  | Enumeratie van terreinen.                                    | VORM                                                         |
| MiniBIM                                                      | Thermische rekenzone                                         | Een thermische rekenzone is een opdeling van een bouwwerk ten  behoeve van energieberekeningen. | NTA 8800:2024 nl                                             |
| MiniBIM                                                      | Toiletruimte                                                 | Een ruimte binnen een gebouw waarin toiletten en wastafels  zijn geïnstalleerd, bedoeld voor persoonlijke hygiëne, vaak voorzien van  sanitair, ventilatie, en sanitaire voorzieningen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Trapgat                                                      | Open ruimte in de verdiepingsvloer, bestemd om een trap te  plaatsen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Trappenhuis                                                  | Een verticale doorgangsruimte binnen een gebouw die wordt  gebruikt om tussen verschillende verdiepingen te reizen, voorzien van een  trap of trappen en vaak ook een lift, met veiligheidsvoorzieningen en  nooduitgangen. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Tuin                                                         | Een buitenruimte buiten de gevelconstructie, vaak aangelegd  met planten, gazon, bestrating en/of andere landschapskenmerken, bedoeld voor  recreatie, tuinieren, sociale activiteiten en visuele esthetiek. | MiniBIM                                                      |
| MiniBIM                                                      | Uitgeefbaar                                                  | De grond waarop gebouwd zal worden met bijbehorend erf.      | Gebiedseconomie                                              |
| MiniBIM                                                      | Vide                                                         | Een open ruimte binnen een gebouw, zonder fysieke afscheiding  met de bouwlaag eronder. Bestemd om een een ruimtelijk gevoel te  creeren. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Wasruimte                                                    | Een ruimte binnen een gebouw, specifiek bestemd voor  wasmachines, drogers en andere apparaten voor wasgoed , voorzien van  wateraansluitingen, afvoer en ventilatie. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | WoningType                                                   | Enumeratie van woningtypen.                                  | -                                                            |
| MiniBIM                                                      | Woonkamer                                                    | Een centrale ruimte binnen een woning, meestal gebruikt voor  ontspanning, entertainment en sociale activiteiten, ingericht met  zitplaatsen, meubels, elektronica en decoratieve elementen, vaak verbonden  met andere delen van de woning zoals de eetkamer en keuken. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Woonkamer-keuken                                             | Ruimte met een gecombineerde functie van keuken en woonkamer. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Woonkamer-keuken-slaapkamer                                  | Ruimte met een gecombineerde functie van keuken, woonkamer en  slaapkamer. | ILS-woco 3.0a                                                |
| MiniBIM                                                      | Woon-slaapkamer                                              | Ruimte met een gecombineerde functie van woonkamer en  slaapkamer. | MiniBIM                                                      |
| MiniBIM                                                      | WOZ-object                                                   | Eigendomseenheid: gebruikseenheid (woning) inclusief het  perceel (kavel) en externe panden (schuur, berging, garage etc). | WOZ                                                          |
| MiniBIM                                                      | Zolderruimte                                                 | Een toegankelijke ruimte binnen een gebouw, direct gelegen  onder het dak. | ILS-woco 3.0a                                                |
| MiniGIM                                                      | Bebouwd oppervlak                                            |                                                              |                                                              |
| MiniGIM                                                      | Bebouwing                                                    |                                                              |                                                              |
| MiniGIM                                                      | Parkeerplaats - privaat                                      |                                                              |                                                              |
| MiniGIM                                                      | Perceel                                                      |                                                              |                                                              |
| MiniGIM                                                      | Verblijfsobject gebruiksfunctie                              |                                                              |                                                              |
| MSCI                                                         |                                                              |                                                              |                                                              |
| NAA.K.T                                                      | Kenmerk                                                      | roepnaam van het materiaal dat je toe wilt passen            | [NAA.K.T.1]                                                  |
| NAA.K.T                                                      | Naam                                                         | materiaalgroepen die we in de bouw toepassen                 | [NAA.K.T.1]                                                  |
| NAA.K.T                                                      | Toepassing                                                   |                                                              | [NAA.K.T.1]                                                  |
| NEN2580                                                      | afstand                                                      | lengtemaat, gemeten langs de kortste verbindingslijn tussen  twee punten | [NEN 2580]                                                   |
| NEN2580                                                      | bebouwde terreinoppervlakte                                  | oppervlakte binnen de buitenomtrek van een gebouw ter hoogte  van het maaiveld, voor zover deze oppervlakte binnen de terreinoppervlakte is  gelegen | [NEN 2580]                                                   |
| NEN2580                                                      | bijzondere gemeenschappelijke ruimte                         | gemeenschappelijke ruimte waarvan het gemeenscahppelijk zijn  slechts wordt bepaald door het door die ruimte voeren van een route die  toegang geeft tot, het verlaten mogelijk maakt van, of het vluchten mogelijk  maakt uit, een andere gfebruiksfunctie | [NEN 2580]                                                   |
| NEN2580                                                      | binnenruimte                                                 | ruimte die aan alle zijden volledig wordt begrensd door  bouwkundige scheidingsconstructies | [NEN 2580]                                                   |
| NEN2580                                                      | bouwlaag                                                     | deel van een gebouw, dat bestaat uit één of meer ruimten,  waarbij de bovenkanten van de afgewerkte vloeren of van het maaiveld van twee  aan elkaar grenzende ruimten niet meer dan 1,5 m in hoogte verschillen | [NEN 2580]                                                   |
| NEN2580                                                      | Bruto inhoud                                                 | De bruto-inhoud van een ruimte of een groep van ruimten is het  product van de BVO, vermeerderd met de oppervlakten van vides en schalmgaten,  die elk afzonderlijk groter zijn dan of gelijk aan 4 m2, en de brutohoogte. | [NEN 2580]                                                   |
| NEN2580                                                      | brutohoogte                                                  | loodrechte afstand tussen de bovenkant van een afgewerkte  vloer of het aansluitende terrein en de bovenzijde van de afgewerkte vloer  van een daarboven gelegen ruimte of de bovenkant van de dakconstructie | [NEN 2580]                                                   |
| NEN2580                                                      | Brutovloeroppervlakte                                        | De BVO van een ruimte of van een groep van ruimten is de  oppervlakte, gemeten op vloerniveau langs de buitenomtrek van de opgaande  scheidingsconstructies, die de desbetreffende ruimte of groep van ruimten  omhullen | [NEN 2580]                                                   |
| NEN2580                                                      | BVO                                                          | brutovloeroppervlakte                                        | [NEN 2580]                                                   |
| NEN2580                                                      | gebouwgebonden buitenruimte                                  | ruimte die door het deels ontbreken van uitwensige bouwkundige  scheidingsconstructies permamnent in open verbinding staan met de bodem en/of  de buitenlucht | [NEN 2580]                                                   |
| NEN2580                                                      | gebouwinstallatie                                            | installatie die voldoet aan de volgende criteria: de  installatie is vast verbonden met het gebouw, het tot stand brengen van de  installatie is nauw verweven met de bouwkundige werkzaamheden, de installatie  is overwegend gericht op het scheppen van de juiste omstandigheden voor het  verblijven of werken in het gebouw, de instllatie is niet gericht op het  produceren van goederen en/of diensten door het bedrijf | [NEN 2580]                                                   |
| NEN2580                                                      | gebruikseenheid                                              |                                                              | [NEN 2580]                                                   |
| NEN2580                                                      | gebruiksfunctie                                              | gedeelten van een of meer bouwwerken op een perceel of  standplaats, die dezelfde gebruiksbestemming hebben en die tezamen  eengenruikseenheid vormen | [NEN 2580]                                                   |
| NEN2580                                                      | gebruiksinhoud                                               | geheel van ruimten voor één gebruiker of gebruikersgroep     | [NEN 2580]                                                   |
| NEN2580                                                      | gebruiksoppervlakte                                          | oppervlakte van een ruimte of een groep van ruimten, gemeten  op vloerniveau, tussen de opgaande scheidingsconstructies, die de  desbetreffende ruimte of groep van ruimten omhullen | [NEN 2580]                                                   |
| NEN2580                                                      | gemeenschappelijke ruimte                                    | ruimte, die ten dienste staat van twee of meer  gebruiksfuncties | [NEN 2580]                                                   |
| NEN2580                                                      | GO                                                           | gebruiksoppervlakte                                          | [NEN 2580]                                                   |
| NEN2580                                                      | installatieoppervlakte                                       | De installatie oppervlakte is de netto vloeroppervlakte van de  ruimten voor alle gebouwinstallaties | [NEN 2580]                                                   |
| NEN2580                                                      | IO                                                           | installatieoppervlakte                                       | [NEN 2580]                                                   |
| NEN2580                                                      | logiesfunctie                                                | gebruiksfunctie voor het bieden van recreatief verblijf of  tijdelijk onderdak aan mensen | [NEN 2580]                                                   |
| NEN2580                                                      | logiesgebouw                                                 | gebouw of gedeelte van een gebouw, waarin twee of meer  logiesuncties liggen, die zijn aangewezen op één of meer gemeenschappelijke  verkeersroutes | [NEN 2580]                                                   |
| NEN2580                                                      | netto inhoud                                                 | De netto-inhoud van een ruimte of een groep van ruimten is het  product van de NVO, vermeerderd met de oppervlakten van vides en schalmgaten,  die elk afzonderlijk groter zijn dan of gelijk aan 4 m2, en de netto-hoogte. | [NEN 2580]                                                   |
| NEN2580                                                      | netto-hoogte                                                 | loodrechte afstand tussen de bovenkant van een afgewerkte  vloer of het aansluitende terrein en de onderkant van een daarboven aanwezig  plafond, vloer of dak, waarbij incidentele constructiedelen buitenbeschouwing  worden gelaten | [NEN 2580]                                                   |
| NEN2580                                                      | nettovloeroppervlakte                                        | De netto vloeroppervlakte van een ruimte of van een groep  ruimten is de oppervlakte, gemeten op vloerniveau, tussen de begrenzende  opgaande scheidingsconstructies van de afzonderlijke ruimten | [NEN 2580]                                                   |
| NEN2580                                                      | niet-overdekte gebouwgebonden buitenruimte                   | gebouwgebonden buitenruimte die, of een deel daarvan dat, niet  overdekt is in de zin van de overdekte gebouwgebonden buitenruimte | [NEN 2580]                                                   |
| NEN2580                                                      | nuttige oppervlakte                                          | dat deel van de NVO dat direct gericht is op de doelstelling en het gebruik van het  gebouw of een deel daarvan. | [NEN 2580]                                                   |
| NEN2580                                                      | NVO                                                          | nettovloeroppervlakte                                        | [NEN 2580]                                                   |
| NEN2580                                                      | Onbebouwd, Overbouwd en  onderbouwd Terrein-     Volume      | [NEN 2580]                                                   |                                                              |
| NEN2580                                                      | onbebouwde terreinoppervlakte                                | gedeelte van de terreinoppervlakte dat niet als bebouwde  terreinoppervlakte wordt aangemerkt | [NEN 2580]                                                   |
| NEN2580                                                      | onderbouwde terreinoppervlakte                               | de som van de oppervlakten van de delen van een gebouw, die  zich geheel onder het niveau van het maaiveld bevinden en daar niet mee  gelijk liggen of erboven uitsteken, voor over deze oppervlakte binnen de  terreinoppervlakte is gelegen. | [NEN 2580]                                                   |
| NEN2580                                                      | ondergeschikt bouwdeel                                       | bouwdeel van beperkte  afmetingen, dat buiten de hoofdmassa van het gebouw uitsteekt | [NEN 2580]                                                   |
| NEN2580                                                      | overbouwde terreinoppervlakte                                | som van de oppervlakten van de delen van een gebouw, die zich  geheel boven het niveau van het maaiveld bevinden en daar niet mee gelijk  liggen, voor zover deze oppervlakte binnen de terreinoppervlakte is gelegen | [NEN 2580]                                                   |
| NEN2580                                                      | overdekte gebouwgebonden buitenruimte                        | gebouwgebonden buitenruimte die, of een deel daarvan dat,  overdekt is, waarbij de breedte van de verticale projectie op het horizontale  vlak minimaal de helft is van de netto-hoogte en ten mimste gelijk is aan  0,75 m | [NEN 2580]                                                   |
| NEN2580                                                      | ruimte                                                       | voor mensen toegankelijk deel van een gebouw, dat ten minste  aan de onderzijde en/of de bovenzijde wordt begrensd door een  scheidingsconstructie en dat een netto-hoogte heeft van tenminste 1,5 m. | [NEN 2580]                                                   |
| NEN2580                                                      | ruimte of voorziening voor horizontaal verkeer               | ruimte of vooriening voor de verkeersafwikkeling per bouwlaag | [NEN 2580]                                                   |
| NEN2580                                                      | ruimte of voorziening voor verticaal verkeer                 | ruimte of vooriening voor de verkeersafwikkeling tussen de  bouwlagen van een gebouw | [NEN 2580]                                                   |
| NEN2580                                                      | tarra-oppervlakte                                            | De tarra-oppervlakte van een ruimte, van een groep van ruimten  of van een gebouw is gelijk aan het verschil van de bruto vloeroppervlakte en  de netto vloeroppervlakte van respectievelijk de desbetreffende ruimte, groep  van ruimten of het gebouw | [NEN 2580]                                                   |
| NEN2580                                                      | Terreininhoud voor de  buitenruimte (=TerreinVolume?)        | [NEN 2580]                                                   |                                                              |
| NEN2580                                                      | terreinoppervlakte                                           | oppervlakte van een door kadastrale of andere grenzen bepaald  perceel, voor zover dit is bestemd of gebruikt voor de plaatsing van één of  meer gebouwen met het daarbij behorende niet te bebouwen terreingedeelte | [NEN 2580]                                                   |
| NEN2580                                                      | TO                                                           | tarra-oppervlakte                                            | [NEN 2580]                                                   |
| NEN2580                                                      | trap                                                         | opeeenvolging van tredevlakken die het mogelijk maken om te  voet hoogteverschillen tussen twee vloeren te overbruggen | [NEN 2580]                                                   |
| NEN2580                                                      | verhuurbare vloeroppervlakte                                 | De verhuurbare oppervlakte van een ruimte of een groep van  ruimten is de oppervlakte, gemeten op vloerniveau, tussen de opgaande  scheidingsconstructies, die de desbetreffende ruimte of groep van  binnenruimten omhullen vermeerderd met de glaslijncorrectie. | [NEN 2580]                                                   |
| NEN2580                                                      | verkeersruimte of verkeersvoorziening                        | ruimte of voorziening binnen een ruimte die dient voor de  verkeersafwikkelling | [NEN 2580]                                                   |
| NEN2580                                                      | verticaal-verkeersoppervlakte                                | De verticale verkeersoppervlakte is de netto vloeroppervlakte  die wordt ingenomen door alle tot een gebouw behorende binnenruimten en  voorzieningen voor verticaal verkeer | [NEN 2580]                                                   |
| NEN2580                                                      | vrije hoogte                                                 | verticale afstand tussen de bovenkant van een afgewerkte vloer  of het maaiveld en de onderkant van het laagste, daarboven gelegen  constructie-onderdeel | [NEN 2580]                                                   |
| NEN2580                                                      | VV                                                           | verticaal-verkeersoppervlakte                                | [NEN 2580]                                                   |
| NEN2580                                                      | VVO                                                          | Verhuurbare vloeroppervlakte                                 | [NEN 2580]                                                   |
| NEN2580                                                      | woonfunctie                                                  | Gebruiksfunctie voor het wonen.                              | [NEN 2580]                                                   |
| NEN2580                                                      | woongebouw                                                   | gebouw of gedeelte van een gebouw, waarin twee of meer  woonfuncties liggen, die zijn aangewezen op één of meer gemeenschappelijke  verkeersroutes | [NEN 2580]                                                   |
| NEN2660-1                                                    | Abstract concept                                             | concept dat een structuur en een afbakening vormt in een  abstracte ruimte. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Activiteit                                                   | Entiteit die plaatsvindt of kan plaatsvinden in een concrete  ruimte-tijd. Een activiteit transformeert objecten, en wordt uitgevoerd door  een object | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Concept                                                      | enkelplaatsig (unair) element dat existentieel onafhankelijk  is. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Concreet concept                                             | Concept dat een manifestatie en een afbakening vormt in een  concrete ruimte-tijd, en dat op ieder moment in de tijd een bepaalde toestand  heeft. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Ding                                                         | iets wat waarneembaar of voorstelbaar is op het desbetreffende  conceptueel niveau of metaniveau. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Element                                                      | enkelvoudig ding dat lid kan zijn van een verzameling.       | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Entiteit                                                     | Concept dat een manifestatie en een afbakening vormt in een  concrete ruimte-tijd, en dat op ieder moment in de tijd een bepaalde toestand  heeft. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Fysiek object                                                | Object dat bestaat of kan bestaan binnen de fysieke 4D  ruimte-tijd. Een fysiek object vormt een manifestatie en een afbakening van  materie en/of energie, en is (in)direct waarneembaar door de zintuigen. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Gebeurtenis                                                  | Concreet Concept dat een overgang tussen twee opeenvolgende  toestanden van een entiteit (object of activiteit) vormt. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Geometrische entiteit                                        | benoemd concept dat een daadwerkelijke of virtuele afbakening  vormt in een concrete (fysieke, driedimensionale) ruimte die we in de  werkelijkheid ervaren. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Informatieobject                                             | Object dat een beschrijving vormt van een ding in de  werkelijkheid | [NEN2660-1]                                                  |
| NEN2660-1                                                    | materie                                                      | chemische stof; zuivere stof, chemische verbinding of mengsel  waaruit reële objecten zijn gemaakt | [NEN2660-2]                                                  |
| NEN2660-1                                                    | Object                                                       | Entiteit die bestaat of kan bestaan binnen een concrete  ruimte-tijd. Een object voert een activiteit uit, en wordt getransformeerd  door een activiteit | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Relatie                                                      | meerplaatsig (n-air) element dat een structureel verband of  betrekking tussen n (twee of meer) Dingen beschrijft, waarbij elk Ding een  bepaalde rol speelt (of een bepaalde plaats heeft) binnen de Relatie | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Rol                                                          | existentieel afhankelijk ding dat de relatieve positie van één  Ding binnen een Relatie benoemt. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Ruimte                                                       | geometrische entiteit                                        | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Temporele entiteit                                           | benoemd concept dat een daadwerkelijke of virtuele afbakening  vormt in een concrete (fysieke, ééndimensionale) tijd die we in de  werkelijkheid ervaren. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Toestand                                                     | Concreet Concept dat een temporeel deel van een entiteit (een  object of activiteit) vormt gedurende een periode tussen twee  gebeurtenissen. | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Top concept                                                  | Het meest generieke concept                                  | [NEN2660-1]                                                  |
| NEN2660-1                                                    | Verzameling                                                  | meervoudig Ding dat bestaat uit de elementen die lid zijn van  de Verzameling. | [NEN2660-1]                                                  |
| NEN2660-2                                                    | discreet object                                              | reëel object dat bestaat uit een aaneengesloten hoeveelheid  vormvaste materie, primair bijeengehouden door interne krachten  (zwaartekracht of elektromagnetische kracht) | [NEN2660-2]                                                  |
| NEN2660-2                                                    | functionele entiteit                                         | entiteit waarbij het gaat om het externe gedrag waarbij de  uitvoer bijdraagt aan doelstellingen van belanghebbenden  geïmplementeerd/gespeeld door een of meer technische entiteiten | [NEN2660-2]                                                  |
| NEN2660-2                                                    | geplande entiteit                                            | entiteit die nog niet bestaat in de fysieke werkelijkheid,  maar die in de mentale of conceptuele werkelijkheid voorkomt | [NEN2660-2]                                                  |
| NEN2660-2                                                    | gerealiseerde entiteit                                       | entiteit die bestaat of heeft bestaan in de fysieke  werkelijkheid | [NEN2660-2]                                                  |
| NEN2660-2                                                    | hoeveelheid bulkmaterie                                      | reëel object dat bestaat uit een aaneengesloten hoeveelheid  niet-vormvaste materie, primair bijeengehouden door externe krachten  (zwaartekracht of opsluiting) | [NEN2660-2]                                                  |
| NEN2660-2                                                    | materie                                                      | chemische stof. zuivere stof, chemische verbinding of mengsel  waaruit reële objecten zijn gemaakt | [NEN2660-2]                                                  |
| NEN2660-2                                                    | raakvlak                                                     | ruimtelijk object, typisch een dunne 2D fysieke ruimte (maar  0D of 1D kan ook), dat de verbinding legt tussen twee fysieke objecten of  poorten van fysieke objecten waarlangs een statische of dynamische  wisselwerking of interactie tussen die elementen kan plaatsvinden | [NEN2660-2]                                                  |
| NEN2660-2                                                    | reëel object                                                 | hoeveelheid materie. Fysiek object (vormvast of niet-vormvast)  dat in de werkelijkheid tastbaar en zichtbaar is (of kan zijn), door de mens  gemaakt of natuurlijk ontstaan. | [NEN2660-2]                                                  |
| NEN2660-2                                                    | ruimtelijk gebied                                            | fysiek object dat een bepaald gebied omsluit, zoals een  vertrek, rijbaan en rivier, dat wordt begrensd door reële objecten of andere  ruimtelijke gebieden (bijvoorbeeld op basis van gebruik of conventie) en dat  een voornamelijk vloeibare of gasvormige hoeveelheid materie bevat | [NEN2660-2]                                                  |
| NEN2660-2                                                    | technische entiteit                                          | entiteit waarbij het gaat om de technische eigenschappen, die  functionele entiteiten implementeert of speelt | [NEN2660-2]                                                  |
| NEN2699                                                      | Bedrijfsinstallaties                                         | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Binnenwandafbouw/binnenwandafwerking                         | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Bouwkundige werken t.b.v. bedrijfsinstallaties               | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Bouwkundige werken t.b.v. losse inrichtingen                 | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | bouwwerk                                                     | elke constructie van enige omvang van hout, steen, metaal of  ander materiaal,die op de plaats van de bestemming hetzij direct of indirect  met de grondverbonden is, hetzij direct of indirect steun vindt in of op de  grond | [NEN2699]                                                    |
| NEN2699                                                      | Dakafbouw/dakafwerking                                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | element                                                      | fysiek onderdeel of een verzameling van fysieke onderdelen van  een gebouw,gekenmerkt door het zich gedragen overeenkomstig de vereiste  functioneleprestatie, in het bijzonder gebruikt in de elementenmethode | [NEN2699]                                                    |
| NEN2699                                                      | elementencluster                                             | groep van elementen met bepaalde bij elkaar behorende  kenmerken | [NEN2699]                                                    |
| NEN2699                                                      | Fundering                                                    | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | gebouw                                                       | elk bouwwerk dat een voor mensen toegankelijke overdekte  geheel ofgedeeltelijk met wanden omsloten ruimte vormt | [NEN2699]                                                    |
| NEN2699                                                      | Gevelafbouw/gevelafwerking                                   | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Grondvoorzieningen                                           | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties in het terrein                                  | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | installaties t.b.v. bedrijfsinstallaties                     | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties t.b.v. losse inrichtingen                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties: elektra: communicatie, beveiliging             | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties: elektra: energievoorziening, verlichting       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties: Wtb: klimaatinstallaties                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Installaties: Wtb: vloeistof en gasinstallaties              | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Inventaris                                                   | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Omheining en afwerking                                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | onroerende zaak                                              | gebied(en), bouwwerk(en) met bouwwerkgebonden terrein(en)    | [NEN2699]                                                    |
| NEN2699                                                      | Opstallen (gebouwtjes, overkappingen, enz.)                  | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Plafonds binnen/buiten                                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Skelet                                                       | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | technische oplossing                                         | deel van een element dat zich onderscheidt in  verschijningsvorm, materiaalen/of uitvoeringswijze | [NEN2699]                                                    |
| NEN2699                                                      | Terrein                                                      | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Terreininrichting                                            | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Transportinstallaties                                        | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Trappen en hellingbanen                                      | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Vaste inrichtingen en voorzieningen                          | -                                                            | [NEN2699]                                                    |
| NEN2699                                                      | Vloerafbouw/vloerafwerking                                   | -                                                            | [NEN2699]                                                    |
| NEN2767                                                      | Areaal Portefeuille                                          |                                                              |                                                              |
| NEN2767                                                      | Beheerobject                                                 | afgebakende eenheid van  een bovenliggend netwerk, een objectenportefeuille, een complex of een areaal  die bestaat uit een samenhangend geheel van elementen met een of meer  autonome gebruiksfuncties, |                                                              |
| NEN2767                                                      | Bouwdeel                                                     | zelfstandig en  aanwijsbaar deel van een element, onderscheiden naar samenstelling of  constructiewijze, bestaande uit één of meer componenten waaraan technische  eigenschappen en een onderhoudshistorie kunnen worden gerelateerd |                                                              |
| NEN2767                                                      | Complex                                                      | verzameling van bij  elkaar behorende beheerobjecten, waarbij deze verzameling een specifieke  functie vervult |                                                              |
| NEN2767                                                      | Component                                                    | zelfstandige onderdeel  van een bouwdeel dat rechtstreeks het resultaat is van productie |                                                              |
| NEN2767                                                      | Element                                                      | aanwijsbaar deel van een  beheerobject dat uitsluitend op basis van de verlangde functie wordt  onderscheiden en bestaat uit één of meerdere bouwdelen |                                                              |
| NEN2767                                                      | Materiaal                                                    |                                                              |                                                              |
| NEN3610                                                      | adres                                                        |                                                              |                                                              |
| NEN3610                                                      | constructie                                                  | Gebouwd object dat direct of indirect met de bodem is  verbonden en bedoeld is om ter plaatse te functioneren. | [NEN3610:2022]                                               |
| NEN3610                                                      | functionele ruimte                                           | Ruimte met een specifieke functie                            | [NEN3610:2022]                                               |
| NEN3610                                                      | gebouw                                                       | Overdekte en geheel of gedeeltelijk met wanden omsloten  constructie bedoeld voor het in een afgeschermde omgeving onderbrengen van  mensen, dieren of voorwerpen of voor de productie van goederen. | [NEN3610:2022]                                               |
| NEN3610                                                      | geografische indentificatie                                  |                                                              |                                                              |
| NEN3610                                                      | geografische ruimte                                          | Ruimte die bekendstaat onder een vanuit de historie of het  gebruik bekende benaming of een fysisch-geografische samenhang, al dan niet  met zijn omgeving, kent. | [NEN3610:2022]                                               |
| NEN3610                                                      | geometrie                                                    |                                                              |                                                              |
| NEN3610                                                      | geoObject                                                    | fenomeen in de werkelijkheid dat direct of indirect is  geassocieerd met een locatie relatief ten opzichte van de aarde | [NEN3610:2022]                                               |
| NEN3610                                                      | juridische ruimte                                            | Ruimte waar een juridisch instrument beleid of regelgeving  toepast. | [NEN3610:2022]                                               |
| NEN3610                                                      | locatie                                                      |                                                              |                                                              |
| NEN3610                                                      | reëel object                                                 | Geo-object dat zich geheel materieel manifesteert.           | [NEN3610:2022]                                               |
| NEN3610                                                      | registratieve ruimte                                         | Op basis van wet- of regelgeving afgebakende ruimte die als  eenheid geldt van politiek- bestuurlijke verantwoordelijkheid of voor  bedrijfsvoering. | [NEN3610:2022]                                               |
| NEN3610                                                      | ruimte                                                       |                                                              |                                                              |
| NEN3610                                                      | virtuele ruimte                                              | geo-object dat zich geheel of gedeeltelijk niet-materieel  manifesteert en dus slechts in abstracte en/of geregistreerde vorm bestaat | [NEN3610:2022]                                               |
| NLBE-SfB                                                     |                                                              |                                                              |                                                              |
| NL-SfB                                                       | ADMINISTRATIEVE,  COMMERCIËLE en BESCHERMENDE VOORZIENINGEN  | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | AFBOUW                                                       |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | AFWERKINGEN                                                  |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | AGRARISCHE EN INDUSTRIËLE  VOORZIENINGEN                     | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | ALGEMENE en OVERIGE  VOORZIENINGEN                           | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Appartementen, studio's, flats                               |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | CIVIELTECHNISCHE  VOORZIENINGEN                              | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Familiepensions                                              |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Functioneel gebouwelement                                    |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | FUNDERINGEN                                                  |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | GEMEENSCHAPPELIJKE  WOONVOORZIENINGEN                        | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | GEZONDHEID en SOCIALE  VOORZIENINGEN                         | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | HISTORISCHE WOONGEBOUWEN                                     |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Hotels                                                       |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH                               | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Centrale  elektrotechnische voorzieningen | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Asset Management Systeem     | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Beveiliging                  | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Communicatie                 | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Energievoorziening gebruikersaansluitingen | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Gebouw management systeem    | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Transport                    | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  ELEKTROTECHNISCH: Verlichting                  | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG                             | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Afvoeren                   | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Gassen                     | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Koeling                    | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Luchtbehandeling           | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Meet- en regelinstallaties | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Verwarming                 | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Water                      | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | INSTALLATIES  WERKTUIGBOUWKUNDIG: Werktuigkundige brandveiligheid | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Kosthuizen voor  specifieke doelgroep                        | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | LOSSE INVENTARIS                                             |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Maisonnettes, duplexwoningen                                 |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Motels                                                       |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | ONDERWIJS-, WETENSCHAPS-  EN INFORMATIEVOORZIENINGEN         | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Overige aangepaste  woningen, hiervoor niet genoemd          | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Overige  gemeenschappelijke woonvoorzieningen, hiervoor niet genoemd | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Overige seriematige  woningen, hiervoor niet genoemd         | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | OVERIGE WOONVOORZIENINGEN                                    |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | PLANOLOGISCHE GEBIEDEN                                       |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | PROJECT TOTAAL                                               |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | RECREATIEVE VOORZIENINGEN                                    |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | RELIGIEUZE VOORZIENINGEN                                     |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Ruimtelijke voorziening                                      |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | RUWBOUW                                                      |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Sociale woningen                                             |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | TERREIN                                                      |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | TIJDELIJK en/of MOBIELE  WOONVOORZIENINGEN                   | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | VASTE VOORZIENINGEN                                          |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen met 1 verdieping                                    |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen met 2 of 3 verdiepingen                             |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen met 4 of meer  verdiepingen                         | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Woningen van conciërges,  bewakers                           | [NL/SfB]                                                     |                                                              |
| NL-SfB                                                       | Woningen voor alleenstaanden                                 |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen voor bejaarden                                      |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen voor gehandicapten                                  |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | Woningen zonder verdieping                                   |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | WONINGEN, aangepast                                          |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | WONINGEN, niet seriematig                                    |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | WONINGEN, seriematig                                         |                                                              | [NL/SfB]                                                     |
| NL-SfB                                                       | WOONVOORZIENINGEN                                            |                                                              | [NL/SfB]                                                     |
| NPR 4660                                                     | EtageRuimte                                                  | niet gedefinieerd'                                           |                                                              |
| NPR 4660                                                     | Gebouw                                                       | niet gedefinieerd'                                           |                                                              |
| NPR 4660                                                     | InpandigeRuimte                                              | niet gedefinieerd'                                           |                                                              |
| NTA8800                                                      |                                                              |                                                              | [NTA8800:2025]                                               |
| Omgevingswet                                                 | bouwwerk                                                     | constructie van enige  omvang van hout, steen, metaal of ander materiaal, die op de plaats van  bestemming hetzij direct of indirect met de grond verbonden is, hetzij direct  of indirect steun vindt in of op de grond, bedoeld om ter plaatse te  functioneren, met inbegrip van de daarvan deel uitmakende bouwwerkgebonden  installaties anders dan een schip dat wordt gebruikt voor verblijf van  personen en dat is bestemd en wordt gebruikt voor de vaart; |                                                              |
| Omgevingswet                                                 | gebouw                                                       | bouwwerk dat een voor  mensen toegankelijke overdekte geheel of gedeeltelijk met wanden omsloten  ruimte vormt; |                                                              |
| OmniClass  (ISO 12006-2)                                     |                                                              |                                                              |                                                              |
| OTL B&U                                                      | BouwkundigElement                                            | Bouwkundig element is een element in een gebouw behorende bij  de discipline bouwkunde, verbonden aan NL-Sfb code 1*.** t/m 4*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | BouwkundigObject                                             | Bouwkundig object is een object in een gebouw behorende bij de  discipline bouwkunde, verbonden aan NL-Sfb code 1*.** t/m 4.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | BouwkundigOnderdeel                                          | Bouwkundig onderdeel is een onderdeel van een  bouwkundigelement, verbonden aan NL-Sfb code 1*.** t/m 4*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | Gebouw                                                       | Een constructie voor het huisvesten van mensen of activiteiten | [OTL-B&U]                                                    |
| OTL B&U                                                      | InstallatieObject                                            | Installatie object is een element in een gebouw behorende bij  de installatietechniek, verbonden aan NL-Sfb code 5*.** t/m 6*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | InstallatieOnderdeel                                         | Installatie onderdeel is onderdeel van een installatieysteem,  verbonden aan NL-Sfb code 5*.** t/m 6*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | InstallatieSysteem                                           | Installatie systeem is een systeem van onderdelen in een  gebouw behorende bij de installatietechniek, verbonden aan NL-Sfb code 5*.**  t/m 6*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | InventarisObject                                             | Inventaris object is een element in een gebouw behorende bij  de inventaris, verbonden aan NL-Sfb code 7*.** t/m 9*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | Kavel                                                        | Een afgebakend stuk land, mogelijk bedekt met water, waarop  één of meerdere gebouwen kunnen staan. | [OTL-B&U]                                                    |
| OTL B&U                                                      | Ruimte                                                       | Een vertegenwoordiging van een gebied of volume dat feitelijk  (door wanden of vloeren) of theoretisch (door een bepaalde functie) beperkt  is. | [OTL-B&U]                                                    |
| OTL B&U                                                      | TerreinObject                                                | Terrein object is een element bij een gebouw behorende bij het  terrein, verbonden aan LN-Sfb code 9*.** | [OTL-B&U]                                                    |
| OTL B&U                                                      | Verdieping                                                   | Een horizontale verzameling van ruimtes, welke verticaal is  begrensd. | [OTL-B&U]                                                    |
| Paspoort-CB23                                                | Bouwproduct                                                  | Product dat is vervaardigd of bewerkt voor opname in  bouwwerken | [CB23-lexicon], NEN-EN 15804:2012+A2:2019 en. Duurzaamheid van bouwwerken  – Milieuverklaringen van producten – Basisregels voor de productgroep  bouwproducten. |
| Paspoort-CB23                                                | Bouwwerk                                                     | gebouwde of te bouwen constructie die bestaat uit elementen  en/of bouwproducten en die één geheel vormt en een specifieke functie vervult | [CB23-lexicon]; Platform CB’23 (2019). Framework Circulair Bouwen.  Raamwerk voor eenduidig taalgebruik en heldere kaders. Delft: Platform CB’23. |
| Paspoort-CB23                                                | Complex                                                      |                                                              |                                                              |
| Paspoort-CB23                                                | Element                                                      | (abstract) onderdeel van een (bouw)werk dat uitsluitend op  basis van een verlangde functie wordt onderscheiden | [CB23-lexicon]; Platform CB’23 (2019). Framework Circulair Bouwen.  Raamwerk voor eenduidig taalgebruik en heldere kaders. Delft: Platform CB’23. |
| Paspoort-CB23                                                | Gebied                                                       |                                                              |                                                              |
| Paspoort-CB23                                                | Gebouw                                                       |                                                              |                                                              |
| Paspoort-CB23                                                | Grondstof                                                    | ruwe, onbewerkte stof die kan worden omgezet in een materiaal | [CB23-lexicon]; NPR 8313-1:2021 nl. Circulaire kantoor- en leeromgeving –  Deel 1: Definities. Geraadpleegd via:  https://data.nen.nl/skosmos/docs/nl/page/82d54e6e-feaf-46b2-87fe-801fb347f09b. |
| Paspoort-CB23                                                | Materiaal                                                    | Natuurlijke of kunstmatig geproduceerde stof die is bestemd om  te worden verwerkt tot een product. | [CB23-lexicon];NTA 8220:2017 nl. Methode voor het beoordelen van  elektrisch materieel op brandrisico. Geraadpleegd via:  https://data.nen.nl/skosmos/docs/nl/page/71b234b1-2409-4791-82fa-c4ba8cb34e35 |
| Paspoort-CB23                                                | Schaalniveau                                                 | indeling van een bouwwerk (en soms zijn omgeving) in logische  eenheden op basis van bijvoorbeeld grootte en/of functie | [CB23-lexicon]; NEN 2660:1996 nl. Ordeningsregels voor gegevens in de  bouw – Termen, definities en algemene regels. |
| PLANON?                                                      | n.a.v. RVB                                                   |                                                              |                                                              |
| RBS                                                          | Binnenruimte                                                 | niet expliciet gedefinieerd'                                 | [RBS]                                                        |
| RBS                                                          | Bouwbesluit brandcompartimentering                           | (beschermd) (sub)Brandcompartiment volgens vigerend  bouwbesluit | [RBS]                                                        |
| RBS                                                          | Bouwbesluit Gebruiksfunctie                                  | Gebruiksfunctie volgens vigerend bouwbesluit.                | [RBS]                                                        |
| RBS                                                          | Bouwbesluit Gebruiksgebied                                   | Gebruiksgebied volgens vigerend bouwbesluit                  | [RBS]                                                        |
| RBS                                                          | Bouwbesluit vluchtroute                                      | Vluchtroute volgens vigerend bouwbesluit                     | [RBS]                                                        |
| RBS                                                          | Bouwlaag                                                     | Groepering van alle bouwwerkelementen die bij een te  onderscheiden verdieping van het bouwwerk behoren. | [RBS]                                                        |
| RBS                                                          | Bouwlaagoppervlakobject                                      | het geometrische IFC-object dat expliciet de verzameling  weergeeft van de bij een bouwlaag behorende bouwwerkelementen. | [RBS]                                                        |
| RBS                                                          | Buitenruimte                                                 | niet expliciet gedefinieerd'                                 | [RBS]                                                        |
| RBS                                                          | Ruimte                                                       | Driedimensionaal IFC-object dat in beginsel begrensd is door  de haar omhullende materiële bouwwerkelementen (wanden, vloeren etc.) en in  haar vorm op deze omhullende elementen aansluit. Een ruimte is hetzij een  binnenruimte, hetzij een buitenruimte. | [RBS]                                                        |
| RBS                                                          | Ruimtedeel                                                   | niet gedefinieerd'                                           | [RBS]                                                        |
| RBS                                                          | Terrein                                                      | De topografische site van een project                        | [RBS]                                                        |
| RBS                                                          | Zone                                                         | Groepering van ruimten of ruimtedelen                        | [RBS]                                                        |
| RVB                                                          | ACTIVITEIT                                                   | Een ACTIVITEIT is het geheel van werkzaamheden dat in het  kader van planning en beheersing wordt onderscheiden. | [RVB]                                                        |
| RVB                                                          | BOUWDEEL                                                     | Een BOUWDEEL is een uit materiaal bestaand INWENDIG ELEMENT  dat invulling geeft aan één of meer verlangde functies en tevens kan worden  onderscheiden naar materiële samenstelling of constructiewijze. | [RVB]                                                        |
| RVB                                                          | BOUWWERK                                                     | Een BOUWWERK is een OMGEVINGSELEMENT zijnde een constructie  van enige omvang van hout, steen, metaal of ander materiaal, die op de plaats  van bestemming hetzij direct of indirect met de grond verbonden is, hetzij  direct of indirect steun vindt in of op de grond, bedoeld om ter plaatse te  functioneren, met inbegrip van de daarvan deel uitmakende bouwwerkgebonden  installaties. | [RVB]                                                        |
| RVB                                                          | COMPLEX                                                      | VASTGOEDCOMPLEX                                              | [RVB]                                                        |
| RVB                                                          | CONDITIE                                                     | De CONDITIE is de (technische) toestand of  staat waarin het BOUWDEEL verkeert. | [RVB]                                                        |
| RVB                                                          | ELEMENT                                                      | BOUWDEEL                                                     | [RVB]                                                        |
| RVB                                                          | GEBOUW                                                       | Een GEBOUW is een BOUWWERK dat betreedbaar  en afsluitbaar is. | [RVB]                                                        |
| RVB                                                          | INWENDIG ELEMENT                                             | Een INWENDIG ELEMENT is het kleinste binnen een  OMGEVINGSELEMENT fysiek herkenbare RUIMTELIJK OBJECT dat het RVB wenst te  onderscheiden. | [RVB]                                                        |
| RVB                                                          | OMGEVINGSELEMENT                                             | Een OMGEVINGSELEMENT is het kleinste in de buitenruimte  (boven, op of onder het aardoppervlak) fysiek herkenbare RUIMTELIJK OBJECT  dat het RVB wenst te onderscheiden. | [RVB]                                                        |
| RVB                                                          | PAND                                                         | GEBOUW                                                       | [RVB]                                                        |
| RVB                                                          | RUIMTE                                                       | Een RUIMTE is een uit lege ruimte bestaand  INWENDIG ELEMENT dat voor mensen toegankelijk is, ten minste aan de  onderzijde en/of de bovenzijde wordt begrensd door BOUWDELEN en een netto-  hoogte heeft van ten minste 1,5     m. | [RVB]                                                        |
| RVB                                                          | RUIMTELIJK OBJECT                                            | Een RUIMTELIJK OBJECT is iets dat een  vorm, afmeting en positie heeft ten opzichte van het aardoppervlak. | [RVB]                                                        |
| RVB                                                          | VASTGOEDCOMPLEX                                              | Een VASTGOEDCOMPLEX is een verzameling van één of meer  OMGEVINGSELEMENTEN die het RVB als een functioneel of administratief  samenhangend geheel beschouwt. | [RVB]                                                        |
| RVB                                                          | VASTGOEDPORTEFEUILLE                                         | De VASTGOEDPORTEFEUILLE is de verzameling van alle  OMGEVINGSELEMENTEN die het RVB in eigendom, gebruik of beheer heeft of waarin  vermogen wordt belegd. | [RVB]                                                        |
| SAREF                                                        | Actuation                                                    | A saref:Actuation is the act of carrying out a procedure to  control the state of the world using an actuator. It links to an actuator to  describe what made the actuation, and to the controlled feature, property,  property of interest, state, or state of interest. Typically, its input is a  property value or a state. An actuation of a state (OP saref:controls) should  have a state as input (OP saref:hasInput). Respectively, an actuation of a  property should have a property value as input. | [SAREF]                                                      |
| SAREF                                                        | Actuator                                                     | A device designed to control one or more properties or states  of one or more features of interest. | [SAREF]                                                      |
| SAREF                                                        | Building                                                     | A building represents a structure that provides shelter for  its occupants or contents and stands in one place. The building is also used  to provide a basic element within the spatial structure hierarchy for the  components of a building project (together with site, storey, and space). | [S4BLD]                                                      |
| SAREF                                                        | BuildingDevice                                               | A tangible object designed to accomplish a particular task in  a building. | [S4BLD]                                                      |
| SAREF                                                        | BuildingObject                                               | An object in the building that can be controlled by devices, such as a  door or a window that can be automatically opened or closed by an  actuator. | [S4BLD]                                                      |
| SAREF                                                        | BuildingSpace                                                | An entity used to define the physical spaces of the building.  A building space contains devices or building objects. | [S4BLD]                                                      |
| SAREF                                                        | Device                                                       | A tangible object designed to accomplish a particular task. In  order to accomplish this task, the device performs one or more functions. An  instance of saref:Device represents one specific real world entity. | [SAREF]                                                      |
| SAREF                                                        | FeatureOfInterest                                            | A feature of interest represents any real world entity from  which a property or a state may be targeted, such as observed and controlled.  An instance of saref:FeatureOfInterest represents one specific real world  entity. | [SAREF]                                                      |
| SAREF                                                        | Function                                                     | Logical groups of commands that devices support to accomplish  their tasks. | [SAREF]                                                      |
| SAREF                                                        | Observation                                                  | A saref:Observation is the act of carrying out a procedure to  estimate or calculate a value of a property of a feature of interest, or a  state of a feature of interest. It links to a sensor to describe what made  the observation, and to the observed feature, property, property of interest,  state, or state of interest. Typically, its result is a property value or a  state. An observation of a state (OP saref:observes) should have a state as a  result (OP saref:hasResult). Respectively, an observation of a property  should have a property value as a result. | [SAREF]                                                      |
| SAREF                                                        | PhysicalObject                                               | Any Object that has a proper space region.                   | [S4BLD]                                                      |
| SAREF                                                        | Property                                                     | Identifiable qualities of features of interest that can be  target of devices, such as observed or controlled. A property can apply to  different features of interest. | [SAREF]                                                      |
| SAREF                                                        | Sensor                                                       | A device designed to observe and measure one or more  properties or states of one or more features of interest. | [SAREF]                                                      |
| SAREF                                                        | State                                                        | Identifiable conditions that features of interest are or may  be in, and that can be target of devices, such as observed and controlled. A  state can apply to different features of interest. | [SAREF]                                                      |
| STABU                                                        |                                                              |                                                              |                                                              |
| TRAIL  (Ketenstandaard)                                      |                                                              |                                                              |                                                              |
| Unieke  codering van objecten                                |                                                              |                                                              |                                                              |
| VERA                                                         |                                                              |                                                              |                                                              |
| VIVET                                                        |                                                              |                                                              |                                                              |
| VTH-Flo                                                      | ACTIVITEIT                                                   | Type van menselijk handelen (of menselijk nalaten) waarbij, of  waardoor een verandering of effect in de fysieke leefomgeving wordt of kan  worden bewerkstelligd. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | ACTIVITEITUITVOERING                                         | Menselijk handelen (of menselijk nalaten) waarbij, of waardoor  een verandering of effect in de fysieke leefomgeving wordt of kan worden  bewerkstelligd. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | ADRESSEERBAAR OBJECT                                         | Een object waaraan formeel adressen kunnen en moeten worden  toegekend: een verblijfsobject, standplaats of ligplaats. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | ANDER GEO-OBJECT                                             | Een fenomeen in de werkelijkheid, met een directe referentie  naar een plaats op het aardoppervlak, niet zijnde een andere specialisatie  van GEO-OBJECT | [VTH-FLo]                                                    |
| VTH-Flo                                                      | GEO-OBJECT                                                   | Fenomeen in de werkelijkheid dat direct of indirect is  geassocieerd met een plaats relatief ten opzichte van de aarde | [VTH-FLo]                                                    |
| VTH-Flo                                                      | KADASTRALE ONROERENDE ZAAK                                   | De grond, de niet gewonnen delfstoffen, de met de grond  verenigde beplantingen, alsmede de gebouwen en werken die duurzaam met de  grond zijn verenigd, hetzij rechtstreeks, hetzij door vereniging met andere  gebouwen of werken. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | PAND                                                         | Kleinste bij de totstandkoming functioneel en bouwkundig-  constructief zelfstandige eenheid die direct en duurzaam met de aarde is  verbonden en betreedbaar en afsluitbaar is. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | TOPOGRAFISCH OBJECT                                          | Een grootschalig topografisch object zoals vastgelegd in de  BGT. | [VTH-FLo]                                                    |
| VTH-Flo                                                      | VTH-OBJECT                                                   | Een ruimtelijk object of samenstelling daarvan waarvoor wet-  en regelgeving ten aanzien van de fysieke leefomgeving van toepassing is en  dat relevant is te onderscheiden vanuit het oogpunt van de uitvoering van  vergunningverlening, toezicht en/of handhaving. | [VTH-FLo]                                                    |
| Wwoz                                                         | WozObject,no checken'                                        | Grootste eenheid die bij  dezelfde "eigenaar" in "eigendom" is, die bij dezelfde  gebruiker in gebruik is, die een zelfstandige te gebruiken eenheid vormt en  die naar de omstandigheden beoordeeld, één geheel vormt. |                                                              |
| WWS                                                          | Overige ruimte                                               |                                                              | [Wws]                                                        |
| WWS                                                          | Ruimte                                                       |                                                              | [Wws]                                                        |
| WWS                                                          | Vertrek                                                      |                                                              | [Wws]                                                        |
| WWS                                                          | Woonruimte                                                   | ( woonruimte welke een zelfstandige woning vormt) woonruimte  als bedoeld in artikel 7:234 van het Burgerlijk Wetboek, welke wordt bewoond  door maximaal twee personen of welke wordt bewoond door drie of meer personen  die een duurzame gemeenschappelijke huishouding hebben. Onder woonruimte  welke een zelfstandige woning vormt, wordt in dit besluit niet mede begrepen  een woonwagen of een combinatie van een standplaats en een woonwagen.” | [Wws]                                                        |
