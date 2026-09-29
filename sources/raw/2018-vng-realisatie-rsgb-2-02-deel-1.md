**==> picture [226 x 113] intentionally omitted <==**

**==> picture [426 x 400] intentionally omitted <==**

## **Referentiemodel** 

## **Stelsel van Gemeentelijke Basisgegevens** Deel I: Beschrijving 

onderdeel van de GEMeentelijke Model Architectuur (GEMMA) 

versie 2.02 (in gebruik) april 2018 

## _Voorwoord_ 

Burgers en bedrijven hoeven (straks) nog maar één keer hun gegevens aan de overheid te verstrekken. Landelijke basisregistraties zorgen voor het meervoudig gebruik hiervan binnen de overheid. Vóór die tijd dienen gemeenten minimaal hun basisgegevens op orde te hebben. Vanwege het belang van een goede gegevenshuishouding heeft KING medio 2007 versie 1.0 uitgebracht van het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB). Daarmee speelden wij in op de  overheidsbrede invoering van het landelijk stelsel van basisregistraties. Tevens verving dit het GFO Basisgegevens. In het voorjaar van 2008 hebben we met versie 1.1. het toepassingsgebied van het RSGB vergroot met de Basisregistratie WOZ (Waardering Onroerende Zaken). Voortschrijdend inzicht, de eerste ervaringen met het RSGB, ontwikkelingen in de (catalogi van de) landelijke basisregistraties en het ontwikkelen van de berichtenstandaard StUF-BG hebben ons aanleiding gegeven versie 2.0 van het RSGB uit te brengen. Dit objecten- of gegevensmodel ondersteunt gemeenten bij het stroomlijnen van hun gegevenshuishouding en de daarop gerichte processen voor beheer en gebruik. Ook voorziet het in standaarden voor gegevensuitwisseling, zodat gemeenten een samenhangende informatievoorziening kunnen opzetten. In versie 2.02 zijn wijzigingen doorgevoerd naar aanleiding van de aanpassingen die zijn doorgevoerd in de catalogus BAG (versie 2009) en het Logisch Ontwerp GBA (versie LO3.7). Deze wijzigingen zijn te vinden in een separaat document. 

## **Beheer** 

De rapportage RSGB 2.0  is in mei 2009 vastgesteld door de StUF-regiegroep. Versie 2.02 betreft een patch m.b.t. Een aanpassing van niet-natuurlijke personen op verzoek van de StUF expertgroep. 

Het beheer van het RSGB is per 1 januari 2010 overgenomen door KING, het KwaliteitsInstituut Nederlandse Gemeenten. Voor vragen, suggesties of opmerkingen kunt u contact opnemen met ons. 

Commentaar op deze versie nemen we in de normale beheerprocedure van het RSGB mee. KING-specialisten beoordelen wijzigingsverzoeken en leggen ze ter advisering voor aan werkgroepen met een publiek-private samenstelling. Iedere belangstellende kan wijzigingsverzoeken indienen. 

**2** 

## **Leeswijzer** 

De rapportage richt zich op iedereen die zich beroepsmatig bezighoudt met (het structureren van) de gemeentelijke informatievoorziening, het inrichten en beheren van basisregistraties en/of het tot stand brengen en beheren van gegevensuitwisseling. De rapportage is opgebouwd overeenkomstig de gebruikelijke indeling van catalogi voor basisregistraties. Vanwege de omvang is zij in twee delen opgesplitst. Deel I beschrijft het RSGB op hoofdlijnen en licht het referentiemodel nader toe. In hoofdstuk 2 van deel I vindt u een overzicht van het objectenmodel en de daarmee samenhangende aspecten. In bijlage 1 lichten wij de wijzigingen toe ten opzichte van versie 1.1. In bijlage 2 geven we aan welke uit het GFO-BG afkomstige gegevens op welke wijze in het RSGB zijn opgenomen. In Deel II vindt u de specificaties van de componenten waaruit het RSGB is opgebouwd: objecttypen (hoofdstuk 1), attribuutsoorten en relatiesoorten (hoofdstuk 2). Dit deel is vooral als ‘naslagwerk’ bedoeld. 

**3** 

## **Samenvatting** 

De invoering van een overheidsbreed stelsel van basisregistraties is één van de meest ingrijpende ontwikkelingen waarmee gemeenten te maken hebben. Het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) biedt gemeenten en hun leveranciers houvast bij het invoeren en het gebruiken van deze gegevens. 

Dit objectenmodel voor de gemeentelijke basisgegevens presenteert de samenhang tussen basisregistraties op een logische wijze. Maar gemeenten hebben meer gegevens nodig voor hun werkprocessen dan nu in de landelijke basisregistraties beschikbaar zijn. Het binnengemeentelijk stelsel  is dan ook ‘rijker’ dan het landelijke stelsel. Dit referentiemodel is onderdeel van de GEMmeentelijke Model Architectuur (GEMMA) van KING. De inhoud is in lijn met de Nederlandse OverheidsReferentieArchitectuur (NORA). 

## **STELSEL VAN GEMEENTELIJKE BASISGEGEVENS OP HOOFDLIJNEN** 

**==> picture [420 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
ADRESSEERBAAR<br>OPENBARE<br>GEMEENTE WOONPLAATS OBJECT<br>RUIMTE<br>AANDUIDING<br>'straat' 'adres'<br>SUBJECT BENOEMD OBJECT<br>NATUURLIJK  verblijfsrelatie BENOEMD<br>TERREIN<br>PERSOON<br>huishouden<br>NIET-NATUURLIJK  MAATSCHAPPE- GEBOUWD<br>PERSOON LIJKE ACTIVITEIT OBJECT<br>RECHTSPERSOON<br>zakelijk recht KADASTRALE<br>ONROERENDE<br>ZAAK<br>VESTIGING<br>PAND<br>belanghebbende<br>WOZ-OBJECT<br>OVERIG GEO-<br>OBJECT<br>relatie<br>functionaris<br>**----- End of picture text -----**<br>


## **Inhoud** 

We hebben het RSGB gebaseerd op de Basisregistraties Adressen (BRA), Gebouwen (BGR), Personen (GBA), Bedrijven (NHR), Kadaster (BRK) en WOZ (BRWOZ) en op de grootschalige topografie die in het Informatiemodel Geografie (IMGeo) is gedefinieerd. We hebben dit aangevuld met gegevens van de voorloper van het referentiemodel, het GFO BasisGegevens uit 1998, waarbij het model bewust beperkt gehouden is. Het referentiemodel is opgebouwd uit: 

- objecttypen zoals ‘Verblijfsobject’ en ‘Ingeschreven persoon’; 

- attribuutsoorten  die  eigenschappen  van  deze  objecttypen  beschrijven  zoals  ‘Bruto inhoud’ en ‘Voornamen’; 

- relatiesoorten tussen deze objecttypen zoals ‘Ingeschreven persoon verblijft in Verblijfsobject’. 

**4** 

## **Doelen** 

Het referentiemodel draagt er aan bij dat gemeenten en daarmee samenwerkende organisaties in staat zijn om de kern van hun gegevenshuishouding, de basisgegevens, in samenhang eenmalig te onderhouden en meervoudig te gebruiken bij de uitoefening van hun taken. Het stroomlijnen van de processen voor het beheer van deze gegevens biedt kansen voor efficiencyverbetering. Meervoudig gebruik van gegevens, waarbij vertrouwd kan worden op de kwaliteit van deze gegevens, is bijvoorbeeld van groot belang voor een goede dienstverlening. Verder vormt het referentiemodel de grondslag voor de berichtenstandaard StUFB(asis)G(egevens). Leveranciers baseren hun software op deze standaard, zodat uitwisselbaarheid van basisgegevens wordt bereikt. Tot slot waarborgt het referentiemodel de uitwisseling van basisgegevens met het landelijk stelsel van basisregistraties en het benutten van dit stelsel in de gemeentelijke informatievoorziening. 

## **Invoering** 

Het is de bedoeling om het referentiemodel in de periode 2009 – 2010 geleidelijk in te voeren. KING verwacht dat leveranciers in die tijd hun software aanpassen aan de basisregistraties. Gedurende de genoemde periode zullen de versies van de berichtenstandaard StUF-BG op basis van het GFO-Basisgegevens en op basis van het RSGB naast elkaar bestaan, zodat een geleidelijke overgang mogelijk is. KING raadt gemeenten nadrukkelijk aan om de ontwikkeling van hun informatievoorziening te baseren op dit referentiemodel en niet alleen uit te gaan van één of meer (catalogi van) landelijke basisregistraties. Op deze manier kunnen gemeenten aansluiten bij het landelijk stelsel én wordt hun eigen informatievoorziening optimaal bediend. Het RSGB vult namelijk de gegevens uit het landelijke stelsel aan met gegevens die voor de gemeentelijke processen cruciaal zijn, maar niet in het landelijk stelsel worden geregistreerd. 

**5** 

## **Inhoudsopgave** 

**1. Inleiding...........................................................................................................7** 1.1. Aanleiding..........................................................................................................................7 1.2. Opzet.................................................................................................................................7 1.3. Invoering............................................................................................................................8 **2. Objectenmodel................................................................................................9** 2.1. Afbakening.........................................................................................................................9 2.2. Doelen..............................................................................................................................10 2.3. Toelichting........................................................................................................................10 2.4. Opbouw............................................................................................................................19 2.4.1. Metagegevens...........................................................................................................19 2.4.2. Historie......................................................................................................................20 2.4.3. Afleidbare gegevens..................................................................................................23 2.4.4. Domeinwaarden of tabel............................................................................................23 **Bijlage 1: Relatie tot GFO Basisgegevens....................................................24** 

**6** 

## **1. Inleiding** 

## **1.1. Aanleiding** 

De invoering van een stelsel van basisregistraties bij de gehele overheid is zonder twijfel een van de meest ingrijpende ontwikkelingen waar gemeenten mee te maken hebben. Onder het motto ‘De overheid vraagt niet naar de bekende weg’, is wettelijk vastgelegd dat burgers en bedrijven basisgegevens nog maar éénmaal aan de overheid hoeven te verstrekken. Alle overheidsorganisaties zijn verplicht deze gegevens te gebruiken. 

Voor gemeenten zijn de basisregistraties dáárom zo belangrijk, omdat zij niet alleen gebruiker ervan zijn, maar ook bronhouder van bijvoorbeeld de basisregistraties van Personen, Adressen en Gebouwen. De basisgegevens vormen nog maar het topje van de ijsberg van wat gemeenten aan gegevens nodig hebben om hun processen uit te voeren. Om grip te krijgen op de meervoudig gebruikte gegevens, heeft een aantal Voorhoedgemeenten onder leiding van EGEM medio 2007 versie 1.0 uitgebracht van het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB). Dit model was de opvolger van het ‘oude’ GFO-Basisgegevens van de Vereniging Nederlandse Gemeenten (VNG). In het voorjaar van 2008 hebben we met versie 1.1. het toepassingsgebied van het RSGB vergroot met de Basisregistratie WOZ (Waardering Onroerende Zaken). Daarmee speelden wij in op de overheidsbrede invoering van het landelijk stelsel van basisregistraties. Voortschrijdend inzicht, de eerste ervaringen met het RSGB, ontwikkelingen in de (catalogi van de) landelijke basisregistraties en het ontwikkelen van de berichtenstandaard StUF-BG hebben ons aanleiding gegeven versie 2.0 van het RSGB uit te brengen. 

## **1.2. Opzet** 

KING presenteert met dit stelsel een standaard om het gebruik van basisgegevens binnen gemeenten en daarmee samenwerkende organisaties te bevorderen. We spreken binnen gemeenten over één samenhangend stelsel van basisgegevens en niet over een basisregistratie. Deze laatste term is gereserveerd voor de landelijke basisregistraties. Dit landelijke stelsel vormt echter wel het uitgangspunt voor het gemeentelijke model. Versie 2.0 van het RSGB is gebaseerd op de volgende, al dan niet definitieve, versies van de catalogi en vergelijkbare beschrijvingen van basisregistraties: 

- Catalogus BasisRegistratie Adressen (BRA versie 4.0; Vrom, 2-2006), 

- Catalogus Basis Gebouwen Registratie (BGR versie 4.0; Vrom, 2-2006), 

- Logisch Ontwerp GBA versie 3.6 (11-2007) en concept-versie 3.7 v.w.b. de relatie GBA – BAG, 

- Programma van eisen Handelsregister (HR; EZ, 6-2008 versie. 1.6) en de Gegevenscatalogus  Nieuw HandelsRegister (concept; VVKvK, 7-2008), 

- Catalogus BasisRegistratie Kadaster (BRK; Kadaster, 3-2009 versie. 1.0.4), 

- Catalogus Basisregistratie WOZ (BRWOZ; Waarderingskamer, 4-2008, versie 1.3) 

- en in aanvulling hierop het 

- GFO Basisgegevens (VNG, 1998). 

De basisregistratie Topografie is niet in het referentiemodel opgenomen. We zijn uitgegaan van grootschalige geo-objecten, met andere woorden de toekomstige Basisregistratie Grootschalige Topografie. Daarvoor gebruikten we het document: 

- Informatiemodel Geografie (concept IMGeo; Geonovum v/h Ravi, 3-2007 vs. 2.0). 

**7** 

Het model richt zich vooral op basisregistraties uit de eerste tranche van de inrichting van het stelsel. Pas wanneer er voldoende bekend is over een andere basisregistratie (tweede tranche en verder) wordt het model uitgebreid en aangepast. 

Het Referentiemodel Stelsel van Gemeentelijke Basisgegevens is onderdeel van de GEMmeentelijke Model Architectuur (GEMMA) van KING. De inhoud is in lijn met de Nederlandse OverheidsReferentieArchitectuur (NORA). 

## **1.3. Invoering** 

Toepassing van het referentiemodel heeft consequenties voor de gemeentelijke organisatie, haar processen, informatievoorziening, gegevenshuishouding en automatisering. Elke gemeente is autonoom in haar keuzes daarin en KING faciliteert de toepassing waar mogelijk. Het tempo van de invoering is vooral afhankelijk van het verwerken van het referentiemodel in de software die gemeenten gebruiken bij de uitvoering van hun taken. 

De software die gemeenten op dit moment gebruiken is vaak (mede) gebaseerd op het eerder genoemde GFO-Basisgegevens. In de jaren 2009 – 2010 passen leveranciers naar verwachting hun software aan op de in te voeren basisregistraties. Dit betekent (ook) een overgang van het GFO-BG naar dit referentiemodel. Om die te ondersteunen, brengt KING tegelijkertijd met het RSGB 2.0 een nieuwe versie van de berichtenstandaard StUF-BG uit. Tijdens deze periode – en mogelijkerwijs langer – bestaat er een StUF-BG-versie op basis van het GFOBasisgegevens (2.04) en een versie op basis van dit referentiemodel (3.10), waardoor een geleidelijke overgang mogelijk is. KING adviseert gemeenten om bij verdere ontwikkeling van hun informatievoorziening te anticiperen op deze overgang. Ze kunnen dan maatregelen treffen om er voor te zorgen dat in de overgangsperiode hun informatievoorziening overweg kan met beide versies van StUF. 

## **Méér dan de landelijke basisregistraties** 

Het referentiemodel is een vertaling en een uitbreiding van het landelijk stelsel van basisregistraties met het oog op de gemeentelijke informatiebehoefte. Op onderdelen verschilt het dan ook van het landelijk stelsel. Wel zijn de landelijke basisregistraties bijna volledig opgenomen in het referentiemodel. KING raadt gemeenten dringend aan om bij de ontwikkeling van hun informatievoorziening uit te gaan van het referentiemodel en niet alleen van één, of meer, catalogi van landelijke basisregistraties. Op die manier sluiten zij aan bij het landelijk stelsel én kunnen zij hun eigen informatievoorziening optimaal faciliteren. Daarnaast gaat KING er van uit dat de leveranciers van gemeentelijke software niet alleen anticiperen op de landelijke basisregistraties maar ook het referentiemodel en de daarop gebaseerde versie van StUF-BG in de software verwerken. 

**8** 

## **2. Objectenmodel** 

**==> picture [256 x 290] intentionally omitted <==**

In dit hoofdstuk bakenen we allereerst het stelsel van gemeentelijke basisgegevens af (paragraaf 2.1). We lichten het referentiemodel toe op basis van de objecttypen en hun relaties (paragraaf 2.3). We besteden ook bijzondere aandacht aan de doelen van dit stelsel (paragraaf 2.2) en aan de metagegevens (paragraaf 2.4). Het stelsel schetsen we in de nevenstaande figuur. 

## **2.1. Afbakening** 

Het stelsel van gemeentelijke basisgegevens is geen basisregistratie zoals bedoeld in het (landelijke) stelsel van basisregistraties. Het is de vertaling van dit stelsel naar de gemeentelijke informatievoorziening. Hierin is nadrukkelijk behoefte aan samenhang tussen de objecten en gegevens uit die basisregistraties èn behoefte aan specifieke gemeentelijke basisgegevens. Het RSGB is 

dan ook meer dan de optelsom van de landelijke basisregistraties. Dit is hieronder gevisualiseerd. Ook ondersteunt de gemeentelijke informatievoorziening diverse taakgebieden en bestaan er uiteenlopende informatiebehoeften. Voor sommige taakgebieden is, of wordt dit uitgewerkt in specifieke informatiemodellen. Deze zijn gerelateerd aan het stelsel van gemeentelijke basisgegevens doordat zij, waar dat zinvol is, een deel van deze objecten en gegevens bevatten. 

Het kan voorkomen dat dergelijke taakspecifieke modellen ook zijn gebaseerd op gegevensuitwisseling met niet-gemeentelijke ketenpartners, die op hun beurt weer andere sectormodellen toepassen. De specificaties daarin zouden kunnen afwijken van die in dit referentiemodel. Om dat te voorkomen, lijkt het wenselijk om objecten en gegevens waarvoor 

**==> picture [263 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
Landelijke basisregistratiemodellen<br>GBA BAG BRK . . .<br>Horizontale domein<br>gegevensmodellen<br>RSGB RGBZ . . . . .<br>Verticale sectorale<br>gegevensmodellen<br>**----- End of picture text -----**<br>


**==> picture [147 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
Landelijke basisregistratiemodellen<br>**----- End of picture text -----**<br>


**9** 

dit geldt en die uitgewisseld worden tussen sectoren, op te nemen (en te specificeren) in het landelijk stelsel van basisregistraties. Door deze (gewijzigde) specificaties over te nemen in het referentiemodel ontstaat er weer harmonie tussen de informatiemodellen op de diverse niveaus en binnen de verschillende sectoren. 

## **2.2. Doelen** 

De gemeentelijke gegevenshuishouding omvat een diversiteit aan objecten, gegevens daarvan en relaties daartussen. In de praktijk mondt dit uit in een groot aantal eilanden met eigen specificaties die uitwisseling, koppeling, meervoudig en ‘gemeentebreed’ gebruik van gegevens belemmeren. Eenduidigheid is daarom dringend gewenst. De kern hiervan zijn de gemeentelijke basisgegevens. Dit referentiemodel specificeert het objecten- of gegevensmodel van deze basisgegevens. Dat is in 1998 gebeurd in het GFO-Basisgegevens. Het RSGB kunt u beschouwen als een herziening daarvan op basis van hedendaagse inzichten, met name de komst van het landelijk stelsel van basisregistraties. 

Het RSGB wil eraan bijdragen dat gemeenten en daarmee samenwerkende organisaties de kern van hun gegevenshuishouding, de basisgegevens, eenmalig onderhouden en meervoudig gebruiken. De achterliggende doelen zijn: 

- het eenduidig onderhouden van basisgegevens door gemeenten; 

- uitwisseling  van  basisgegevens  mogelijk  te  maken,  door  leveranciers  hun  software daarop te laten baseren; en 

- het waarborgen van het uitwisselen met, en het benutten van, het landelijk stelsel van basisregistraties. 

## **Houvast** 

Dit gegevensmodel vormt geen grondslag voor een (relationele) database. Het staat partijen – gemeenten, leveranciers – vrij om een eigen technische realisatievorm te kiezen. Die kan bijvoorbeeld bestaan uit meerdere databases. De essentie van het referentiemodel is vooral om eenduidig aan te geven welke gegevens kunnen worden ontleend aan het Stelsel van Gemeentelijke Basisgegevens: welke informatievragen kunt u stellen die ook kunnen worden beantwoord? Denk bijvoorbeeld aan ruimtelijke relaties tussen objecten. Uit het model kunt u afleiden over welke ruimtelijke relaties u informatie kunt krijgen, ongeacht of deze relaties administratief zijn vastgelegd, of gegenereerd worden met behulp van GIS-analysetechnieken. Veel informatievragen zullen voortkomen uit softwarecomponenten die bepaalde taken van de gemeente ondersteunen, en aan softwarecomponenten die delen van het stelsel ondersteunen. Om deze componenten te kunnen laten samenwerken, hebben we het referentiemodel uitgewerkt in een nieuwe versie van de berichtenstandaard StUF-BG, waarin we services of berichten definiëren. 

Ten slotte biedt het referentiemodel gemeenten houvast als zij zelf databases en software willen ontwikkelen en helpt het hen bij het selecteren van softwarecomponenten en databases van leveranciers. Het is raadzaam om aan – potentiële – leveranciers steeds te vragen of zij hun database baseren op het referentiemodel en of zij de berichten ondersteunen die op basis van het referentiemodel zijn gespecificeerd. 

## **2.3. Toelichting** 

In deze paragraaf lichten we het objectenmodel toe. Het model op hoofdlijnen is weergegeven in de samenvatting. Het is gebaseerd op de modellen van de diverse basisregistraties. We wijken niet af van deze modellen, maar in sommige gevallen zijn we gedetailleerder of hebben 

**10** 

we bepaalde gegevens niet overgenomen. Verder hebben we de modellen aangevuld en met elkaar verbonden, om te kunnen voldoen aan de gemeentelijke behoefte aan basisgegevens. We modelleren alleen de actuele situatie. De behoefte aan historie specificeren we met de desbetreffende metagegevens. 

## **Tekenwijze** 

We brengen een **Tekensymboliek** objecttype in beeld met een rechthoek. De naam van het 1:N-relatie **OBJECTTYPE A OBJECTTYPE B** objecttype is in de rechthoek vermeld. In een oranje vlak objecttype van basisregistratie objecttype niet in landelijke basisregistratie staan de of-of-relatie objecttypen die deel uitmaken van enige **OBJECTTYPE C** generalisatie ('groep') van meer objecttypen; (catalogus van een) N:M-relatie 1 of meer van laatstgenoemde objecttypen basisregistratie (A). maakt deel uit van een basisregistratie KING heeft de andere objecttypen toegevoegd. Een witte rechthoek visualiseert een objecttype dat uit meerdere andere objecttypen is samengesteld. Dit is een zogenaamde generalisatie van objecttypen. Laatstgenoemde objecttypen zijn op hun beurt specialisaties van het gegeneraliseerde objecttype. Een gegeneraliseerd objecttype heeft een ‘vet’ kader (C) als één of meer van de specialisaties daarvan deel uitmaken van enige (catalogus van een) basisregistratie. In een blauw vlak staan de objecttypen die geen generalisaties zijn van andere objecttypen en geen deel uitmaken van enige (catalogus van een) basisregistratie (B). Tussen de objecttypen brengen we de drie soorten relaties als volgt in beeld: een 1:1-relatie (een lijn), een 1:N-relatie (een lijn met één ‘harkje’) en een N:M-relatie (een lijn met twee ‘harkjes’). Een relatie die deel uitmaakt van enige (catalogus van een) basisregistratie is ‘vetter’ gevisualiseerd dan relaties waarvoor dit niet geldt: de relaties die KING heeft toegevoegd. Een relatie veronderstelt dat een object van het ene objecttype altijd gerelateerd is aan dat van het andere objecttype. Wanneer dit niet het geval hoeft te zijn, dan ziet u dat aan het open rondje aan het uiteinde van de relatie(lijn). In het voorbeeld: een object van objecttype B is altijd gerelateerd aan een object van objecttype A, maar andersom hoeft dat niet het geval te zijn. Met een of-of-relatie tenslotte bedoelen we dat een object van – in dit geval – objecttype C een relatie kent met een object van één van beide gerelateerde objecttypen, hier objecttype A of B. 

## **Basisregistratie-objecten** 

De volgende objectenmodellen vormen de kern van het objectenmodel: de Basisregistraties van Adressen en Gebouwen (de BAG: BRA en BGR), de Basisregistratie Personen (GBA en RNI), de Basisregistratie Ondernemingen en Rechtspersonen (het NHR oftewel Nieuw Handelsregister), de Basisregistratie Kadaster (de BRK), de BasisRegistratie WOZ (de BRWOZ) en de Basisregistratie Grootschalige Topografie (GBKN) cq. het Informatiemodel Geografie (IMGeo). 

Het gaat om de objecttypen: WOONPLAATS, OPENBARE RUIMTE, NUMMERAANDUIDING (onderdeel van ADRESEERBAAR OBJECT AANDUIDING), VERBLIJFSOBJECT (onderdeel van GEBOUWD OBJECT), STANDPLAATS, LIGPLAATS (beide onderdeel van BENOEMD TERREIN), PAND, INGEZETENE (PERSOON in BRP-termen, hier onderdeel van NATUURLIJK PERSOON), INGESCHREVEN NIET-NATUURLIJK PERSOON (onderdeel van 

**11** 

NIET-NATUURLIJK PERSOON), MAATSCHAPPELIJKE ACTIVITEIT, VESTIGING, KADASTRALE ONROERENDE ZAAK, ZAKELIJK RECHT, WOZ-OBJECT, WOZ-BELANG, WOZ-WAARDE en de geo-objecttypen: WEGDEEL, WATERDEEL, TERREINDEEL, SPOORBAANDEEL, KUNSTWERKDEEL en INRICHTINGSELEMENT. 

## **Adressen, gebouwen en terreinen** 

KING heeft de GEMEENTE als objecttype toegevoegd, omdat zij het bestuurlijke gebied is waarbinnen de betreffende ruimtelijke objecten liggen. 

Binnen een gemeente bevinden zich één of meer WOONPLAATSen, maar een woonplaats bevindt zich altijd binnen één gemeente. 

Binnen elke woonplaats bevinden zich één of meer OPENBARE RUIMTEn die in de BAG zijn gedefinieerd. Aangezien een openbare ruimte, zoals een straat, zich kan uitstrekken over meerdere woonplaatsen is GEMEENTELIJKE OPENBARE RUIMTE toegevoegd. De OPENBARE RUIMTE is nu dát deel van de gemeentelijke openbare ruimte dat zich binnen één woonplaats bevindt. 

De CBS-indeling in WIJKen en BUURTen hebben we eveneens toegevoegd. De geometrie is één van de te registreren gegevens. Een belangrijk voordeel hiervan is dat management­ informatie geografisch in beeld gebracht kan worden. 

Aan een OPENBARE RUIMTE kunnen ADRESSEERBARE OBJECT AANDUIDINGen gerelateerd zijn. In de meeste gevallen gaat het om NUMMERAANDUIDINGen die de BAG onderscheidt. Soms is het noodzakelijk om ook andere adressen vast te stellen, bijvoorbeeld van terreinen die geen stand- en ligplaatsen zijn en eventueel van gebouwen die geen verblijfsobjecten zijn. Een dergelijke OVERIGE ADRESSEERBAAR OBJECT AANDUIDING wordt weliswaar officieel vastgesteld, maar maakt geen deel uit van de BAG. 

De BGR onderscheidt gebouwde objecten als VERBLIJFSOBJECTen en terreinen als STANDen LIGPLAATSen. In het RSGB hebben we voor het onderscheid in gebouwen (GEBOUWD OBJECT) en terreinen (BENOEMD TERREIN) gekozen. Met de verblijfsobjecten wordt immers niet de hele gebouwde omgeving, voor zover zinvol, gemodelleerd. Vandaar dat we het OVERIG GEBOUWD OBJECT hebben toegevoegd. Dit geeft, in combinatie met de verblijfsobjecten, gemeenten de mogelijkheid om het deel van de gebouwde omgeving dat zij relevant vinden adequaat te registreren. Een OVERIG GEBOUWD OBJECT kan op één van drie manieren een adres krijgen: 

- door gebruik te maken van een ‘BAG-adres’ (NUMMERAANDUIDING), aangevuld met een locatieomschrijving; 

- door een officieel adres vast te stellen dat niet in de BAG wordt geregistreerd (OVERIGE ADRESSEERBAAR OBJECTAANDUIDING); 

- door de ligging ten opzichte van een OPENBARE RUIMTE aan te geven met een locatieomschrijving. 

Gemeenten hebben de behoefte om naast stand- en ligplaatsen ook andere afgebakende terreinen te registreren en een officieel (niet-authentiek) adres te geven. Hiervoor hebben we het OVERIG TERREIN toegevoegd. In combinatie met de stand- en ligplaatsen kunnen 

**12** 

## **DETAILLERING ADRESSEN, GEBOUW EN EN TERREINEN** 

**==> picture [430 x 608] intentionally omitted <==**

**----- Start of picture text -----**<br>
GEMEENTE<br>ontstaan uit /<br>overgegaan in<br>WOONPLAATS<br>GEMEENTELIJKE<br>OPENBARE  WIJK<br>RUIMTE<br>betreft 1 of meer OPENBARE<br>RUIMTE<br>BUURT<br>ADRESSEERBAAR OBJECT AANDUIDING<br>OVERIGE<br>ADRESSEERBAAR  NUMMER-<br>OBJECT  AANDUIDING<br>AANDUIDING<br>straatadres<br>officieel adres officieel adres<br>locatie-adres<br>nevenadres hoofdadres hoofdadres nevenadres hoofdadres<br>OVERIG<br>VERBLIJFS-<br>GEBOUWD  STANDPLAATS LIGPLAATS OVERIG TERREIN<br>OBJECT<br>OBJECT<br>ADRESSEERBAAR OBJECT<br>GEBOUWD OBJECT BENOEMD TERREIN<br>ontstaan uit / ligt in ontstaan uit /<br>overgegaan in BENOEMD OBJECT overgegaan in<br>zonder verblijfsobject ligt in<br>PAND<br>ligt in<br>ligt in<br>ligt in andere<br>ligt aan<br>**----- End of picture text -----**<br>


**13** 

gemeenten dan alle terreinen registreren waaraan zij een officieel adres willen toekennen. VERBLIJFSOBJECT, STANDPLAATS en LIGPLAATS hebben we gegeneraliseerd naar ADRESSEERBAAR OBJECT teneinde aan te sluiten bij de terminologie van de BAG. GEBOUWD OBJECT en BENOEMD TERREIN hebben we gegeneraliseerd naar BENOEMD OBJECT  omdat veel relaties de groepering van al deze objecttypen betreffen. 

VERBLIJFSOBJECTen maken deel uit van PANDen (gevisualiseerd met de ligt-in-relatie). Maar niet elk pand bevat verblijfsobjecten. Voor dergelijke panden hebben we een optionele relatie toegevoegd tussen PAND en BUURT om van de panden die niet aan VERBLIJFSOBJECTen worden gerelateerd, duidelijk te maken binnen welke buurt (en daarmee gemeente) zij vallen, bijvoorbeeld omdat een gemeente eigenaren van dergelijke panden wil aanschrijven. Overigens valt de relatie tussen een pand als bijgebouw van een verblijfsobject zijnde een hoofdgebouw af te leiden via de relaties van beide objecten met het WOZ-object. 

## **Topografie** 

Een deel van de geschetste objecttypen heeft betrekking op fysieke ruimtelijke objecten of geo-objecten zoals VERBLIJFSOBJECT en PAND. De andere geo-objecten benoemen we hier onafhankelijk van elkaar, zoals hiernaast is geschetst. 

## **OVERIGE GEO-OBJECTEN** 

|WEGDEEL||WATERDEEL||TERREINDEEL|
|---|---|---|---|---|
||||||
|SPOORBAAN-<br>DEEL||KUNSTWERK-<br>DEEL||INRICHTINGS-<br>ELEMENT|



## **Kadaster** 

Het objectenmodel van het stelsel van basisregistraties kent een n:m-relatie tussen enerzijds onroerende zaken (onderdeel van de BasisRegistratie Kadaster) en anderzijds verblijfsobjecten en stand- en ligplaatsen. Een onroerende zaak is de groepering van kadastrale percelen, appartementsrechten en leidingnetwerk. Alleen de eerste twee zijn zodanig belangrijk voor de gemeentelijke informatievoorziening dat die in het referentiemodel zijn opgenomen. Het KADASTRAAL PERCEEL en het APPARTEMENTSRECHT vormen gezamenlijk de KADASTRALE ONROERENDE ZAAK. Om aan te sluiten bij de toegevoegde objecttypen (OVERIG GEBOUWD OBJECT en OVERIG TERREIN) hebben we de relatie met 

## **DETAILLERING KADASTRALE ONROERENDE ZAKEN EN RECHTEN** 

**==> picture [440 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
KADASTRALE ONROERENDE ZAAK heeft als voornaamste zakelijk gerechtigde  RECHTSPERSOON<br>KADASTRAAL  APPARTEMENTS-<br>PERCEEL RECHT<br>ZAKELIJK RECHT<br>NATUURLIJK<br>PERSOON<br>ligt binnen<br>is ondergrond van app.complex met<br>ZAK. RECHT<br>is hoofd- ontstaan uit / AANTEKENING is van<br>perceel bij  overgegaan in<br>mandelige<br>is deel van appartementencomplex  NIET-NATUURLIJK<br>KAD. ONR. ZAAK  met als vereniging van eigenaars PERSOON<br>HISTORIE<br>RELATIE<br>BENOEMD  heeft KAD. ONR. ZAAK<br>OBJECT AANTEKENING is van<br>heeft<br>**----- End of picture text -----**<br>


**14** 

adresseerbare objecten vormgegeven als een verplichte relatie tussen BENOEMD OBJECT en KADASTRALE ONROERENDE ZAAK. 

Verder hebben we een 1:n-relatie toegevoegd tussen kadastrale percelen onderling (‘ligt binnen’). Een geheel perceel beschikt over geometrie (de perceelgrens), voor deelpercelen is dit niet het geval. Door deze relatie is van deelpercelen vast te leggen bij welke gehele percelen zij qua ligging horen. Op analoge wijze hebben we van de BRK afgeleid de ‘liggings-relaties’ tussen appartementsrechten en kadastrale percelen (‘is ondergrond van …’) via de zgn. appartementscomplexen. Op deze wijze is van elke kadastrale onroerende zaak vast te leggen om welk deel van het gemeentelijk grondgebied het gaat. Tot slot hebben we de voornaamste zakelijk gerechtigde (een RECHTSPERSOON) van een KADASTRALE ONROERENDE ZAAK toegevoegd. 

Het ZAKELIJK RECHT legt van elke kadastrale onroerende zaak vast welke RECHTSPERSOON (of RECHTSPERSOONen) daarop zakelijke rechten uitoefent. 

## **De WOZ** 

Centraal in dit gedeelte van het obejctenmodel staat het WOZ-OBJECT zoals dat in de BRWOZ voorkomt. Dit heeft relaties naar de KADASTRALE ONROERENDE ZAAKen (percelen en appartementsrechten) die tot het WOZ-object behoren, naar de zgn. WOZ-BELANGen, naar de WOZ-WAARDEn en naar de WOZ-DEELOBJECTen waaruit het is samengesteld. 

Het WOZ-DEELOBJECT betreft een element van een WOZ-OBJECT; meerdere WOZdeelobjecten (bijvoorbeeld de woning, de losstaande schuur en de grond) vormen gezamenlijk een WOZ-object en/of onderbouwen de waarde ervan nader (bijvoorbeeld de waarde-invloed van bodemverontreiniging). Voor een WOZ-deelobject geldt telkens één van de volgende situaties: 

- het komt overeen met een benoemd object (gebouwd object, benoemd terrein) of is een gedeelte daarvan, 

- het komt overeen met een pand of is een gedeelte daarvan of 

- het is geen van beide, het WOZ-deelobject betreft geen gebouwd object, pand, benoemd terrein of gedeelte daarvan; een voorbeeld hiervan is een bouwkavel waarop nog geen bouwvergunning verleend is. 

Het is bovendien zo dat een WOZ-deelobject nooit overeen kan komen met meer dan één (deel van een) benoemd object of pand. En, indien een WOZ-deelobject een relatie heeft met een pand, dan kan het alleen gaan om panden waarbinnen geen verblijfsobjecten afgebakend zijn, zoals garages en schuren bij woningen, en gedeelten van panden die niet afgebakend zijn als verblijfsobject, zoals een niet-afsluitbare parkeergarage onder een appartementencomplex. 

Door middel van het objecttype WOZ-BELANG leggen we vast welk subject als belanghebbende eigenaar is aangewezen, welk subject als belanghebbende gebruiker is aangewezen en eventueel welke "derden" zich bekend maken als "medebelanghebbenden". 

WOZ-objecten moeten voorzien kunnen worden van een voor de belanghebbende begrijpelijke aanduiding van de locatie waar het WOZ-object zich bevindt: de WOZ-object-aanduiding. In het gangbare spraakgebruik gaat het om een begrijpelijk adres voor het WOZ-object. Uitgangspunt van het RSGB is dat we voor de aanduiding van het WOZ-object gebruik maken van de adressen van de benoemde objecten waaraan het WOZ-object via zijn WOZ-deelobjecten is gerelateerd. Veelal is de WOZ-aanduiding eenduidig af te leiden uit deze 

**15** 

**==> picture [156 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
DETAILLERING WOZ-objecttypen<br>**----- End of picture text -----**<br>


**==> picture [481 x 599] intentionally omitted <==**

**----- Start of picture text -----**<br>
BENOEMD OBJECT<br>GEBOUWD OBJECT BENOEMD TERREIN<br>OVERIG<br>VERBLIJFS- OVERIG<br>GEBOUWD  STANDPLAATS LIGPLAATS<br>OBJECT TERREIN<br>OBJECT<br>ADRESSEERBAAR<br>OBJECT<br>AANDUIDING<br>PAND<br>NUMMER-<br>AANDUIDING<br>OVERIGE<br>WOZ- ADRESSEERBAAR<br>KADASTRALE  DEELOBJECT OBJECT<br>ONROERENDE  AANDUIDING<br>ZAAK<br>KADASTRAAL<br>PERCEEL<br>behoort tot<br>OPENBARE<br>WOZ-OBJECT<br>RUIMTE<br>APPARTEMENTS ligt aan<br>RECHT<br>heeft<br>ZAKELIJK<br>WOZ-BELANG WOZ-WAARDE<br>RECHT<br>heeft als<br>aangewezen<br>belang-<br>hebbende<br>INGESCHREVEN<br>NIET-NATUURLIJK  VESTIGING<br>ANDER<br>INGEZETENE NIET- NATUURLIJK  PERSOON<br>INGEZETENE<br>PERSOON<br>ANDER<br>INGESCHREVEN PERSOON<br>BUITENLANDS<br>NIET-NATUURLIJK<br>PERSOON<br>NATUURLIJK PERSOON<br>NIET-NATUURLIJK<br>PERSOON<br>RECHTSPERSOON<br>SUBJECT<br>ligt in<br>bestaat uit<br>maakt deel uit van straatadres van<br>heeft aanduiding  afgeleid van<br>heeft<br>heeft<br>**----- End of picture text -----**<br>


**16** 

relaties. Om ook in andere gevallen een WOZ-object van de aanduiding te kunnen voorzien, hebben we relatiesoorten toegevoegd van WOZ-OBJECT naar ADRESSEERBAAR OBJECT AANDUIDING en naar OPENBARE RUIMTE. 

## **Subjecten** 

Het SUBJECT is de verzameling van RECHTSPERSOONen: NATUURLIJKe PERSOONen en NIET-NATUURLIJKe PERSOONen, en VESTIGINGen. Deze benamingen wijken af van de door SBG gehanteerde terminologie. Dit doen we om verwarring tussen de begrippen persoon en natuurlijke persoon in het spraakgebruik te voorkomen. 

## **Natuurlijk persoon** 

Een NATUURLIJK PERSOON kan een INGESCHREVEN PERSOON zijn, of een ANDER NATUURLIJK PERSOON. En een ingeschreven persoon kan op zijn beurt weer een INGEZETENE of een NIET-INGEZETENE zijn. Een INGEZETENE is de persoon zoals de GBA die benoemd (als onderdeel van de BasisRegistratie Personen). De twee andere typen natuurlijke personen hebben we toegevoegd, omdat 

ook deze personen van belang zijn voor het uitoefenen van de gemeentelijke taken. Met de niet-ingezetenen lopen we vooruit op de invoering van de Registratie Niet-Ingezetenen als onderdeel van de BasisRegistratie Personen. De combinatie met de ingezetenen omvat daarmee alle personen die woonachtig zijn in Nederland, of die in het buitenland wonen, maar zijn ingeschreven als (niet-)ingezetene. Alle andere personen die relevant zijn voor de gemeentelijke taakuitoefening wonen in het buitenland en hebben we als ANDER BUITENLANDS NATUURLIJK PERSOON gemodelleerd. We onderscheiden twee groepen relaties tussen ingeschreven personen: OUDER-KIND-RELATIE en HUWELIJK/GEREGISTREERDPARTNERSCHAP-RELATIE. 

Een INGESCHREVEN PERSOON verblijft gewoonlijk in of op een ADRESSEERBAAR OBJECT (VERBLIJFSOBJECT, STAND- of LIGPLAATS). Is de verblijfsrelatie onbekend dan wordt de verblijfplaats, indien mogelijk, omschreven door een combinatie van de WOONPLAATS waarin de ingeschrevene verblijft met een zogenaamde nadere adresaanduiding. Is dit niet mogelijk dan resteert het registreren van een correspondentieadres of van een buitenlands adres, als de ingeschrevene in het buitenland verblijft. Aangezien een natuurlijk persoon zich kan inschrijven op een nevenadres wordt zijn of haar inschrijvingsadres bepaald door de relatie naar NUMMERAANDUIDING. 

Het correspondentieadres hebben we toegevoegd aan NATUURLIJK PERSOON. Dit kan zijn een (relatie met een) OVERIGE ADRESSEERBAAR OBJECTAANDUIDING (een NUMMERAANDUIDING of ander officieel adres) of een postadres (postbus of antwoordnummer) dat zich in een WOONPLAATS bevindt. Zowel correspondentie-adres als buitenlands adres gelden dus ook voor de ANDER BUITENLANDS NATUURLIJK PERSOON. 

Eén of meer ingeschreven personen kunnen gezamenlijk een HUISHOUDEN vormen dat is gehuisvest in of op een ADRESSEERBAAR OBJECT. Daarin respectievelijk daarop kunnen zich meerdere HUISHOUDENs bevinden. 

**17** 

## **DETAILLERING SUBJECTEN** 

**==> picture [465 x 643] intentionally omitted <==**

**----- Start of picture text -----**<br>
SUBJECT<br>RECHTSPERSOON<br>NATUURLIJK PERSOON NIET-NATUURLIJK<br>PERSOON<br>ANDER<br>ANDER<br>BUITENLANDS<br>NATUURLIJK<br>NIET-NATUURLIJK<br>PERSOON<br>PERSOON<br>INGESCHREVEN PERSOON<br>INGESCHREVEN<br>NIET-<br>INGEZETENE NIET-NATUURLIJK  VESTIGING<br>INGEZETENE<br>PERSOON<br>FUNCTIONARIS<br>MAATSCHAPPE-<br>HUISHOUDEN- LIJKE ACTIVITEIT<br>RELATIE<br>heeft als bezoekadres<br>HUISHOUDEN<br>WOONPLAATS<br>NUMMER-<br>AANDUIDING<br>is hoofdlocatie van<br>OVERIGE<br>ADRESSEERBA<br>ADRESSEERBAAR OBJECT is nevenlocatie van AR OBJECT<br>AANDUIDING<br>GEBOUWD OBJECT BENOEMD TERREIN ADRESSEERBAAR<br>OBJECT<br>BENOEMD OBJECT AANDUIDING<br>RELATIE<br>HUWELIJK /  OUDER-KIND- is eigenaar van<br>PARTNERSCHAP REISDOCUMENT oefent activiteit uit in<br>verblijft op locatie in<br>verblijft in of op heeft als locatie-adres<br>heeft als inschrijvingsadres<br>heeft als correspondentie-adres (postadres in)<br>**----- End of picture text -----**<br>


**18** 

## **Ondernemingen en rechtspersonen** 

Voor ondernemingen en rechtspersonen gaan we uit van het model van het NHR. Hierin worden binnen- en buitenlandse NIET-NATUURLIJKE PERSOONen geregistreerd die staan ingeschreven bij de Kamer van koophandel: de INGESCHREVEN NIET-NATUURLIJK PERSOON. Daaraan hebben we toegevoegd de ANDER NIET NATUURLIJK PERSOON. Dit zijn buitenlandse niet-natuurlijke personen die niet zijn ingeschreven bij de Kamer van Koophandel, en om die reden geen deel uitmaken van het NHR, maar die wel relevant zijn voor de gemeente. 

De FUNCTIONARIS-relatie geeft aan welke rechtspersonen namens de niet-natuurlijke persoon rechtshandelingen kunnen verrichten. Een functionaris kan dus zowel een natuurlijk als een niet-natuurlijk persoon zijn. 

Elke RECHTSPERSOON kan eigenaar zijn van één MAATSCHAPPELIJKE ACTIVITEIT, die hij uitoefent in één of meer VESTIGINGen. Gezien de eigenschappen van een VESTIGING beschouwen we dit objecttype in het RSGB als één van de subtypen van SUBJECT. 

Het NHR kent per VESTIGING slechts één VERBLIJFSOBJECT als locatie voor de activiteiten van die VESTIGING. Voor de gemeente kan het relevant zijn te weten in welke andere gebouwde objecten en/of benoemde terreinen de vestiging haar activiteiten verder uitoefent. Daarom hebben we een relatie ten behoeve van nevenlocaties toegevoegd. Daarnaast hebben we beide vestigingslocatierelaties, voor hoofd- en nevenlocaties, uitgebreid tot alle benoemde objecten (dus ook het OVERIG GEBOUWD OBJECT,STANDPLAATS, LIGPLAATS en OVERIG TERREIN). Dit is een aanvulling op het NHR. Aangezien een vestiging zich kan inschrijven op een nevenadres wordt het vestigingsadres bepaald door de relatie naar ADRESSEERBAAR OBJECT AANDUIDING. 

Evenals bij NATUURLIJK PERSOON hebben we het correspondentieadres toegevoegd aan de NIET-NATUURLIJK PERSOON en aan de VESTIGING. Dit kan een NUMMERAANDUIDING of OVERIGE ADRESSEERBAAR OBJECTAANDUIDING zijn, of een postadres. NIETNATUURLIJK PERSOON en VESTIGING kennen tevens een buitenlands adres. Aangezien ook een NATUURLIJK PERSOON een correspondentie-adres en een buitenlands adres kent, hebben we deze gegevens gemodelleerd als kenmerken van SUBJECT. 

## **2.4. Opbouw** 

Het gegevensmodel is opgebouwd uit objecttypen, attribuut- en relatiesoorten. In deze paragraaf gaan we in op een aantal aspecten hiervan. 

## **2.4.1. Metagegevens** 

Objecttypen, attribuut- en relatiesoorten specificeren we door middel van metagegevens. Zij zijn van essentieel belang zijn voor de werking van het landelijk stelsel van basisregistraties en dus voor het RSGB. Als bijvoorbeeld niet bekend is of een bepaald gegeven nog wel geldig is, dan is de kwaliteit van het functioneren van de overheid in het geding. 

De algemene definitie van metagegeven is: een gegeven over een gegeven of over een aggregatie van gegevens. 

Enerzijds gaat het om de betekenis van een gegeven zoals naam, definitie en domein, en anderzijds om de wijze waarop de waarde van een gegeven is bepaald (het proces) en wat uit die waarde afgeleid mag worden. Een voorbeeld van het laatste is het metagegeven ‘Status = 

**19** 

“in onderzoek”’ bij het gegeven “CORNELIS STEENMANS woont op het adres HONDSDRAFLAAN 30 te EINDHOVEN”. De gebruiker weet nu dat het woonadres van Cornelis Steenmans wellicht niet juist is en dat het wordt onderzocht. 

Het is raadzaam eenduidig om te gaan met metagegevens. In deel II definiëren we deze gegevens waarvan we in de volgende tabel een overzicht geven. 

|**Objecttype**|**Attribuutsoort**|**Relatiesoort**|
|---|---|---|
|Naam objecttype|Naam attribuutsoort|Naam relatiesoort|
|Mnemonic objecttype|Herkomst attribuutsoort|Herkomst relatiesoort|
|Herkomst objecttype|Code attribuutsoort|Code relatiesoort|
|Definitie objecttype|XML-tag attribuutsoort||
|Herkomst definitie objecttype|Definitie attribuutsoort|Definitie relatiesoort|
|Datum opname objecttype|Herkomst definitie attribuutsoort|Herkomst definitie relatiesoort|
|Toelichting objecttype|Datum opname attribuutsoort|Datum opname relatiesoort|
|Unieke aanduiding objecttype|Toelichting attribuutsoort|Toelichting relatiesoort|
|Populatie objecttype|Domein attribuutsoort||
|Kwaliteitsbegrip objecttype|Indicatie materiële historie|Indicatie materiële historie|
|Overzicht attributen|Indicatie formele historie|Indicatie formele historie|
|Overzicht relaties|Aanduiding gebeurtenis|Aanduiding gebeurtenis|
||Aanduiding brondocument|Aanduiding brondocument|
||Indicatie in onderzoek|Indicatie in onderzoek|
||Aanduiding strijdigheid/nietigheid|Aanduiding strijdigheid/nietigheid|
||Indicatie kardinaliteit|Indicatie kardinaliteit|
||Indicatie authentiek|Indicatie authentiek|
||Regels attribuutsoort|Regels relatiesoort|



**Overzicht metagegevens** 

## **2.4.2. Historie** 

Het aspect tijd speelt een belangrijke rol in het gebruik van de informatie uit (basis)registraties. Afnemers hebben eigen rechtsprocedures en moeten kunnen herleiden wanneer attribuutwaarden als bekend mochten worden verondersteld. Als bijvoorbeeld besluiten ter discussie worden gesteld, is het juridisch van belang te achterhalen op basis van welke attribuutwaarden zo’n besluit genomen is. Als onjuiste attribuutwaarden zijn gebruikt, is het relevant te weten of de juiste attribuutwaarden tijdens de besluitvorming al bekend waren. 

## **Tijdslijnen** 

Er spelen twee tijdslijnen een rol bij het herleiden van attribuutwaarden: 

**20** 

- Wanneer  is  iets  gebeurd,  in  de  werkelijkheid  of  volgens  opgave  (wanneer  zijn  de opgenomen  gegevens  geldig)?  Dit  valt  binnen  de  tijdlijn  van  de  aangehouden werkelijkheid. 

- Vanaf wanneer wist de overheid (als collectief van organisaties) dat de gegevens bekend waren?  Dit  valt  binnen  de  tijdlijn  van  het  administratieproces  of  de  administratieve werkelijkheid. 

In de rapportage 'Architectuur van het stelsel' (Stroomlijning BasisGegevens, 2006) wordt geadviseerd om beide tijdslijnen te registreren, om de attribuutwaarden van een bepaald moment te kunnen reconstrueren. Dit advies hebben we overgenomen. In de diverse basisregistraties wordt hieraan op verschillende wijzen invulling gegeven. Wij hebben er voor gekozen om in deze tijdslijnen op eenduidige wijze te voorzien met de attribuutsoorten ‘datum begin geldigheid object’ en ‘datum einde geldigheid object’ en het metagegeven ‘indicatie materiële historie’ respectievelijk het metagegeven ‘indicatie formele historie’. In sommige gevallen hebben we de beide attribuutsoorten onder specifieke namen opgenomen, zoals de geboortedatum en de overlijdensdatum van een natuurlijk persoon. De metagegevens specificeren we als volgt: 

- Indicatie materiële historie: indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de attribuutwaarde. Materiële historie impliceert  dat  actuele,  historische  en  eventuele  toekomstige  attribuutwaarden  te bevragen zijn 

- Indicatie formele historie: indicatie of de formele historie van de attribuutsoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt). 

## **Periode van geldigheid** 

De materiële historie heeft betrekking op een individuele attribuutsoort of de groep van attribuutsoorten die tegelijkertijd, als gevolg van een gebeurtenis, wijzigen (bijvoorbeeld de woonadresgegevens van een natuurlijk persoon als gevolg van een verhuizing). Ofschoon het mogelijk lijkt om de periode tussen het ontstaan en het beëindigen van een object af te leiden uit de reeks aan perioden van de materiële historie van de attribuutsoorten van dat object, hebben we er in het referentiemodel voor gekozen om beide op te nemen. Zo wordt het ontstaan en het beëindigen van een object expliciet opvraagbaar. En in sommige gevallen worden attribuutwaarden van een object al geregistreerd voordat het object feitelijk bestaat. Bijvoorbeeld in de BAG de gegevens van de nieuwbouwvergunning bij het pand dat waarschijnlijk gebouwd gaat worden. 

De periode die gemarkeerd wordt door de ‘datum begin geldigheid object’ en de ‘datum einde geldigheid object’ geeft aldus de periode aan waarin het object in de werkelijkheid heeft bestaan met de kenmerken die noodzakelijk zijn om van het in de werkelijkheid bestaan te kunnen spreken. Een persoon bestaat bijvoorbeeld pas in de werkelijkheid als deze als baby het lichaam van de moeder heeft verlaten. De materiële historie markeert de periode waarin de waarde(n) van één of meer attribuutsoorten van het object geldig zijn of waren. Waar mogelijk en verantwoord hebben we de materiële (en ook de formele) historie opgenomen voor de groep van alle attribuutsoorten van een objectsoort. Bij veel objecttypen is dit niet mogelijk omdat we de (materiële) historie van de landelijke basisgegevens willen onderscheiden van de historie van de gemeentelijke basisgegevens. Zo gaat de afstemming niet verloren met de landelijke basisregistratie over deze basisgegevens. Ook komt het voor dat een basisregistratie zelf al groepen van attribuutsoorten met eigen historiekenmerken 

**21** 

onderscheid. Dit is het geval in de BRP (GBA) voor bijvoorbeeld de groep (daar ‘categorie’ genaamd) ‘verblijfplaats’. 

## **Oude gegevens corrigeren** 

Een bijzonder geval van historie is het aanbrengen van correcties op attribuutwaarden uit het verleden. Dit gaat zowel om de administratieve werkelijkheid (‘wanneer hadden we wat kunnen weten?’) als de feitelijke cq. aangenomen werkelijkheid (‘wat dachten we dat de feitelijke waarde was op een bepaald moment en wat weten we daar nu over?’). Besluiten en daarop gebaseerde acties worden genomen op basis van de op een bepaald moment bekende (vermeende) werkelijkheid. Het is dus van belang om later te kunnen achterhalen wat die (vermeende) werkelijkheid was, en wat op een later moment de werkelijkheid bleek te zijn. Met de eerder genoemde historie-kenmerken is het mogelijk om correcties op deze wijze te registreren (zie onderstaande figuur). 

**==> picture [471 x 109] intentionally omitted <==**

Omgaan met correctie van gegevens (Bron: Architectuur van het stelsel; SBG, augustus 2006) 

## **Materiële en/of formele historie-indicatie?** 

Niet bij elke attribuutsoort (of groep van attribuutsoorten) hebben we beide metagegevens opgenomen. Soms zelfs geen van beide. Voor landelijke basisgegevens hebben we de specificaties in de desbetreffende catalogi gevolgd. Voor gemeentelijke basisgegevens hebben we grofweg de volgende regels gehanteerd: 

- in de situatie zoals hiervoor beschreven, waarin historische (en eventueel toekomstige) gegevenswaarden gecorrigeerd moeten kunnen worden en er ook voor de gecorrigeerde waarde inzicht is vanaf wanneer deze geldig is, zijn beide indicaties van toepassing; 

- indien er behoefte is aan inzicht in alle waarden (naast de huidige waarde ook historische en eventueel toekomstige waarden) van een attribuutsoort en tevens aan eenduidigheid over de datum vanaf wanneer een wijziging van de attribuutwaarde bekend was, dan zijn eveneens  beide  indicaties  van  toepassing;  deze  situatie  impliceert  dat  correcties aangebracht kunnen worden oftewel houdt de eerstgenoemde situatie in zich. 

- indien alleen de huidige waarde (in de werkelijkheid) relevant is en het niet relevant is vanaf wanneer deze waarde geldig is, dan zijn geen van beide indicaties van toepassing; 

- indien het relevant is en redelijkerwijs een aanname gedaan kan worden vanaf wanneer een  (huidige,  historische  of  eventueel  toekomstige)  waarde  geldig  is  maar het  niet relevant is te weten wanneer die waarde bekend was, dan is alleen de indicatie materiële historie van toepassing; er is in deze situatie dus geen inzicht of een waarde wellicht gecorrigeerd is; 

- indien redelijkerwijs zelden of nooit een aanname gedaan kan worden wanneer zich de wijziging in de werkelijkheid voordeed op basis waarvan de waarde gewijzigd is maar het wel relevant zou zijn vanaf wanneer de waarde-wijziging bekend was, dan zou alleen de indicatie formele historie van toepassing zijn. Evenwel, bij het eventueel doorvoeren van correcties in de historie ontstaat desinformatie (stel: vandaag is bekend geworden dat de 

**22** 

waarde over een periode ergens in 2002/2003 anders was; formele historie-datum is dan vandaag terwijl de huidige waarde een andere is dan de waarde in genoemde periode). Aangezien het opnemen van historie veronderstelt dat die gecorrigeerd kan worden, hebben we deze combinatie van historie-indicaties niet opgenomen voor die situaties. Een andere situatie doet zich voor als de eenmaal vastgestelde waarde nooit wijzigt en tevens niet gecorrigeerd kan of mag worden, Indien het voor een dergelijk attribuutsoort niet relevant is wanneer de waarde in de werkelijkheid is ontstaan en de waarde niet gelijktijdig ontstaat bij het ontstaan van het object, dan hebben we geen materiële maar wel formele historie opgenomen, mits het laatste relevant is. Een voorbeeld hiervan is … Een derde situatie doet zich voor als de attribuutsoort een datum is, bijvoorbeeld de overlijdensdatum van een persoon. De waarde van de attribuutsoort is tevens de datum van de materiële historie. Als hierop correcties plaats kunnen vinden, dan hebben we eveneens geen materiële maar wel formele historie opgenomen. 

Deze regels geven inzicht in de wijze waarop de combinaties van beide historie-indicaties bij een attribuut- of relatiesoort geïnterpreteerd moeten worden. 

## **2.4.3. Afleidbare gegevens** 

Het RSGB bevat onder andere zogenaamde afgeleide gegevens: gegevens die afleidbaar zijn uit andere attribuut- en/of relatiesoorten. Dit lijkt op redundantie. Toch hebben we deze gegevens daar opgenomen waar er ten eerste vraag is naar het afgeleide gegeven en ten tweede het gegeven niet eenvoudig af te leiden is (er moet sprake zijn van enige mate van complexiteit). Wel  hebben we het aantal afgeleide gegevens zo beperkt mogelijk gehouden. Een voorbeeld is de 'Datum vestiging in Nederland' van een Ingeschreven persoon. De afleiding van dit gegeven is niet triviaal. Door het als afleidbaar gegeven op te nemen kan het opgevraagd worden zonder dat de historie of andere gegevens van het object opgevraagd hoeven te worden om daaruit dit gegeven af te leiden. 

## **2.4.4. Domeinwaarden of tabel** 

In bijvoorbeeld het GFO Basisgegevens werd veel gewerkt met codetabellen om de mogelijke waarden van een attribuutsoort te specificeren. In bepaalde catalogi van basisregistraties, zoals die van de BAG, is hiervan geheel afgezien. De mogelijke waarden van een attribuutsoort zijn daarin als domeinwaarden van de attribuutsoort gespecificeerd. In het RSGB hebben we bij het laatste zoveel mogelijk aangesloten. Alleen als sprake is van dynamiek in de domeinwaarden hebben we een 'tabel-objecttype' opgenomen. Dit betreft de situaties waarin domeinwaarden kunnen veranderen en/of het aantal domeinwaarden kan toe- of afnemen. Een voorbeeld is het objecttype LAND. 

**23** 

## **Bijlage 1: Relatie tot GFO Basisgegevens** 

In dit referentiemodel hebben we het GFO BasisGegevens niet compleet overgenomen. Zie voor de motivering hiervan bijlage 1 van het RSGB versie 1.0. Hieronder geven we per gegevensgroep (in het GFO BG) aan welke gegevens wel en welke niet zijn overgenomen. 

Onderstaande tabel geeft de overeenkomsten en verschillen weer van het GFO-BG ten opzichte van het RSGB. De object- en gegevenstypen die deel uit maken van het RSGB, maar niet in het GFO-BG waren opgenomen, staan niet vermeld. 

De eerste kolom vermeldt de onderscheiden gegevensgroepen (vet gedrukt) en gegevens in het GFO-BG. In de tweede kolom staat het objecttype uit het RSGB, dat overeenkomt met de GFO-BG-gegevensgroep, dan wel het objecttype waarbij het gegeven is opgenomen. In de derde kolom staat een toelichting, als die nodig is. 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|**Academische Titel**|ACADEMISCHE||
|*Academische titel van een<br>natuurlijk persoon|TITEL||
|Academische titelcode|||
|Omschrijving academische<br>titel|||
|Positie academische titel t.o.v.<br>naam|||
|**Adellijke Titel/Predikaat**|NATUURLIJK<br>PERSOON|De attribuutsoorten van de GBA zijn<br>aangehouden, waardoor de GFO-BG-<br>gegevens niet één op één overeenkomen.|
|*Adellijke titel/predikaat van<br>een natuurlijk persoon|NATUURLIJK<br>PERSOON||
|Adellijke titel of predikaat<br>(code)|NATUURLIJK<br>PERSOON||
|Omschrijving adellijke titel|NATUURLIJK<br>PERSOON||
|Soort adellijke titel/predikaat|NATUURLIJK<br>PERSOON||
|**Adres**|ADRESSEERBAA<br>R OBJECT<br>AANDUIDING|Alleen gemodelleerd als Locatie-adres (in<br>de terminologie van het GFO-BG) dus niet<br>als Postadres. Betreft alleen officiële<br>adressen.|
|*Correspondentieadres|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|*Inschrijvingsadres|VERBLIJFSOB­<br>JECT,<br>STANDPLAATS en<br>LIGPLAATS<br>TERREIN|Gemodelleerd als 'verblijft in of op'.|



**24** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|Postcode|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Woonplaatsnaam|WOONPLAATS||
|**Adresfiliatie**|-|Niet opgenomen aangezien de filiatie van<br>GEBOUWD OBJECT  en BENOEMD<br>TERREIN bepalend is.|
|*Adresfiliatie is ontstaan uit<br>locatieadres|-||
|*Adresfiliatie is overgegaan in<br>locatieadres|-||
|Filiatiecode locatieadres|-||
|**Bestemmingsgebied**|-|Het Bestemmingsgebied is niet opgenomen<br>met het oog op de ontwikkelingen rondom<br>Imro en DURP waarbij sprake zou kunnen<br>zijn van een geografische registratie van<br>bestemmingen.|
|*Bestemming van een<br>kadastraal object|-||
|*Bestemming van een overig<br>bouwwerk|-||
|*Bestemming van een<br>verblijfsobject|-||
|Bestemmingsplanherziening|-||
|Naam bestemmingsplan|-||
|Omschrijving<br>bestemmingsgebied|-||
|Omschrijving planologische<br>bestemming|GEBOUWD<br>OBJECT||
|**Bouwwerk**|-|Bebouwing is in de BGR anders<br>gemodelleerd, het niveau Bouwwerk komt<br>niet meer voor.|
|*Gebouw is onderdeel van<br>bouwwerk|-||
|*Overig bouwwerk is<br>onderdeel van bouwwerk|-||
|Bouwwerknummer|-||
|**Buurt**|BUURT||
|*Buurt bij een locatieadres|BUURT|De relatie is verlegd naar GEBOUWD<br>OBJECT en BENOEMD TERREIN|
|*Buurt in een wijk|BUURT||
|Buurtcode|BUURT||
|Buurtnaam|BUURT||
|Einddatum buurt|BUURT||
|Ingangsdatum buurt|BUURT||
|**Filiatie kadastraal object**|KADASTRALE||
|*Filiatie kadastraal object is<br>ontstaan uit kadastraal object|ONROERENDE<br>ZAAK HISTORIE||
|*Filiatie kadastraal object is<br>overgegaan in kadastraal<br>object|RELATIE||
|Filiatiecode kadastraal object|||
|**Filiatie verblijfsobject**|BENOEMD<br>OBJECT|Gemodelleerd als n:m-relatie van het object<br>zelf.|
|*Filiatie verblijfsobject is<br>ontstaan uit verblijfsobject|||
|*Filiatie verblijfsobject is<br>overgegaan in verblijfsobject|||



**25** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|Filiatiecode verblijfsobject|||
|**Gebouw**|-|Bebouwing is in de BGR anders<br>gemodelleerd, het niveau Gebouw komt niet<br>meer voor.|
|*Gebouw is onderdeel van<br>bouwwerk|-||
|*Pand is onderdeel van<br>gebouw|-||
|Gebouwnummer|-||
|**Gemeente**|GEMEENTE||
|*Gemeente van inschrijving|INGESCHREVEN<br>PERSOON||
|*Gemeente waarin<br>locatieadres ligt|-|Gemodelleerd naar GEBOUWD OBJECT,<br>LIGPLAATS en STANDPLAATS via<br>WOONPLAATS, OPENBARE RUIMTE en<br>ADRESSEERBAAR OBJECT<br>AANDUIDING.|
|*Wijk in een gemeente|GEMEENTE||
|Einddatum gemeente|GEMEENTE||
|Gemeente waarin overgegaan|GEMEENTE||
|Gemeentecode|GEMEENTE||
|Gemeentenaam|GEMEENTE||
|Ingangsdatum gemeente|GEMEENTE||
|**Huishouden**|HUISHOUDEN||
|*Huishouden heeft<br>huishoudenrelaties|HUISHOUDEN||
|*Huishouden is gehuisvest in<br>WOZ-object|HUISHOUDEN|Relatie is niet gelegd naar het WOZ-object<br>maar naar het VERBLIJFSOBJECT,<br>LIGPLAATS en STANDPLAATS.|
|Grootte huishouden|HUISHOUDEN||
|Huishoudennummer|HUISHOUDEN||
|Soort huishouden|HUISHOUDEN||
|**Huishoudenrelatie**|HUISHOUDENREL<br>ATIE||
|*Huishouden heeft<br>huishoudenrelaties|HUISHOUDENREL<br>ATIE||
|*Huishoudenrelatie is een<br>natuurlijk persoon|HUISHOUDENREL<br>ATIE|Relatie is gelegd naar INGESCHREVEN<br>PERSOON|
|Einddatum huishoudenrelatie|HUISHOUDENREL<br>ATIE||
|Huishoudenrelatiecode|HUISHOUDENREL<br>ATIE|metagegeven|
|Ingangsdatum<br>huishoudenrelatie|HUISHOUDENREL<br>ATIE|metagegeven|
|**Huwelijk/Geregistreerd**<br>**partnerschap**|HUWELIJK /<br>GEREGISTREERD<br>PARTNERSCHAP|Uitgegaan is van de GBA, alle<br>desbetreffende gegevens zijn overgenomen.|
|*Huwelijk/partnerschap<br>bestaat uit|||



**26** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Land<br>huwelijkssluiting/aangaan<br>geregistreerd partnerschap|||
|*Land ontbinding<br>huwelijk/geregistreerd<br>partnerschap|||
|Datum<br>huwelijkssluiting/aangaan<br>geregistreerd partnerschap|||
|Datum inschrijving vonnis<br>ontbinding<br>huwelijk/geregistreerd|||
|Datum ontbinding<br>huwelijk/geregistreerd<br>partnerschap|||
|Plaats<br>huwelijkssluiting/aangaan<br>geregistreerd partnerschap|||
|Plaats ontbinding<br>huwelijk/geregistreerd<br>partnerschap|||
|Reden ontbinding<br>huwelijk/geregistreerd<br>partnerschap|||
|Soort verbintenis|||
|**Kadastraal object**|KADASTRALE<br>ONROERENDE<br>ZAAK||
|*Bestemming van een<br>kadastraal object|-|Gemodelleerd vanuit GEBOUWD OBJECT.|
|*Filiatie kadastraal object is<br>ontstaan uit kadastraal object|KADASTRALE<br>ONROERENDE<br>ZAAK||
|*Filiatie kadastraal object is<br>overgegaan in kadastraal<br>object|KADASTRALE<br>ONROERENDE<br>ZAAK||
|*Kadastraal object bij een<br>overig bouwwerk|-|Overig Bouwwerk is vervallen, zie toelichting<br>aldaar.|
|*Kadastraal object bij een<br>verblijfsobject|KADASTRALE<br>ONROERENDE<br>ZAAK|Relatie is gemodelleerd naar GEBOUWD<br>OBJECT, LIGPLAATS en STANDPLAATS.|
|*Kadastraal object bij een<br>WOZ-object|KADASTRALE<br>ONROERENDE<br>ZAAK||
|*Locatieadres van een<br>kadastraal object|KADASTRALE<br>ONROERENDE<br>ZAAK|Relatie naar adres loopt via GEBOUWD<br>OBJECT, LIGPLAATS en STANDPLAATS.|



**27** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Publiekrechtelijke beperking<br>rust op kadastraal object|-|Publiekrechtelijke Beperking is niet<br>opgenomen, zie toelichting aldaar.|
|*Voornaamste zakelijk<br>gerechtigde|KADASTRALE<br>ONROERENDE<br>ZAAK||
|*Zakelijk recht rust op<br>kadastraal object|KADASTRALE<br>ONROERENDE<br>ZAAK||
|Aanduiding indicatie mogelijk|-|Zie opmerking bij Publiekrechtelijke<br>Beperking.|
|Centroïd x-coördinaat<br>kadastraal object|KADASTRAAL<br>PERCEEL||
|Centroïd y-coördinaat<br>kadastraal object|||
|Centroïd z-coördinaat<br>kadastraal object|||
|Einddatum kadastraal object|KADASTRAAL<br>OBJECT||
|Indicatie oppervlakte geschat|KADASTRAAL<br>PERCEEL|Gegeventype ‘Aanduiding soort grootte’.|
|Indicatie vervallen|KADASTRAAL<br>OBJECT|Gegeventype ‘Vervallen o.b.v. stuk’.|
|Ingangsdatum kadastraal<br>object|KADASTRAAL<br>OBJECT||
|Kadastraal object index letter|KADASTRAAL<br>PERCEEL en<br>APPARRTEMENT<br>SRECHT|Via Kadastrale onroerende zaak typering|
|Kadastraal object index<br>nummer|KADASTRAAL<br>PERCEEL en<br>APPARRTEMENT<br>SRECHT||
|Kadastraal perceelnummer|KADASTRAAL<br>OBJECT||
|Kadastrale gemeentecode|KADASTRAAL<br>OBJECT||
|Kadastrale sectie|KADASTRAAL<br>OBJECT||
|Omschrijving deelperceel|KADASTRAAL<br>PERCEEL||
|Oppervlakte kadastraal object|KADASTRAAL<br>PERCEEL||
|**Land**|LAND||
|*Geboorteland|NATUURLIJK<br>PERSOON||



**28** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Land<br>huwelijkssluiting/aangaan<br>geregistreerd partnerschap|PARTNER-<br>RELATIE||
|*Land ontbinding<br>huwelijk/geregistreerd<br>partnerschap|PARTNER-<br>RELATIE||
|*Land overlijden|INGESCHREVEN<br>PERSOON||
|*Land van emigratie|INGESCHREVEN<br>PERSOON||
|*Land van immigratie|INGESCHREVEN<br>PERSOON||
|*Land waarin postadres ligt|SUBJECT||
|Einddatum land|LAND|Zie opmerking hierboven.|
|Ingangsdatum land|LAND||
|Landcode|LAND||
|Landnaam|LAND||
|**Locatieadres**|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|*Adresfiliatie is ontstaan uit<br>locatieadres|-|Niet opgenomen aangezien de filiatie van<br>BENOEMD OBJECTbepalend is.|
|*Adresfiliatie is overgegaan in<br>locatieadres|-||
|*Buurt bij een locatieadres|BENOEMD<br>OBJECT|De relatie naar BUURT is verlegd naar<br>genoemd objecttype.|
|*Gemeente waarin<br>locatieadres ligt|WOONPLAATS|Relatie verloopt via OPENBARE RUIMTE<br>en WOONPLAATS.|
|*Hoofdadres van een WOZ-<br>object|ADRESSEERBAA<br>R OBJECT<br>AANDUIDING|Ook via BENOEMD OBJECT.|
|*Locatieadres van een<br>kadastraal object|GEBOUWD<br>OBJECT,<br>LIGPLAATS en<br>STANDPLAATS|De relatie naar KADASTRAAL OBJECT is<br>verlegd naar genoemde objecttypen.|
|*Locatieadres van een overig<br>bouwwerk|OVERIG<br>GEBOUWD<br>OBJECT|Overig Bouwwerk komt niet meer voor. In de<br>relatie is voorzien d.m.v. het OVERIG<br>GEBOUWD OBJECT|
|*Locatieadres van een<br>verblijfsobject|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|*Nevenadres van een WOZ-<br>object|-|WOZ-object kent slechts één WOZ-adres..|
|*Verblijfs/vestigingsadres|VERBLIJFSOBJEC<br>T, LIGPLAATS EN<br>STANDPLAATS|De relatie is verlegd naar genoemde<br>objecttypen.|
|*Wijk bij een locatieadres|BUURT|De relatie verloopt via BENOEMD OBJECT<br>en BUURT.|



**29** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|Aanduiding bij huisnummer|-|Maakt geen deel meer uit van een officieel<br>adres.|
|Centroïd x-coördinaat<br>locatieadres|GEBOUWD<br>OBJECT||
|Centroïd y-coördinaat<br>locatieadres|GEBOUWD<br>OBJECT||
|Centroïd z-coördinaat<br>locatieadres|-|Maakt vooralsnog geen deel uit van de<br>BAG.|
|Einddatum locatieadres|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Huisletter|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Huisnummer|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Huisnummertoevoeging|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Ingangsdatum locatieadres|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING||
|Locatieadresnummer|ADRESSEER­<br>BAAR OBJECT<br>AANDUIDING|Identificatiecode adresseerbaar object<br>aanduiding|
|Locatieomschrijving|OVERIG<br>GEBOUWD<br>OBJECT|De Locatieomschrijving maakt geen deel uit<br>van een officieel adres. Wel kan het bij het<br>OVERIG GEBOUWD OBJECT worden<br>gebruikt om de ligging ervan t.o.v. een<br>officiële ADRESSEERBAAR OBJECT<br>AANDUIDING of een OPENBARE RUIMTE<br>aan te geven.|
|Straatcode|(GEMEENTELIJKE<br>) OPENBARE<br>RUIMTE|Identificatiecode (gemeentelijke) openbare<br>ruimte|
|Straatnaam|GEMEENTELIJKE<br>OPENBARE<br>RUIMTE||
|**Nationaliteit**|NATIONALITEIT||
|*Code van een nationaliteit|||
|Einddatum nationaliteit|||
|Ingangsdatum nationaliteit|||
|Nationaliteit (code)|||
|Omschrijving nationaliteit|||



**30** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|**Natuurlijk persoon**|NATUURLIJK<br>PERSOON en<br>specialisaties<br>daarvan||
|*Academische titel van een<br>natuurlijk persoon|NATUURLIJK<br>PERSOON||
|*Adellijke titel/predikaat van<br>een natuurlijk persoon|NATUURLIJK<br>PERSOON||
|*Geboorteland|INGESCHREVEN<br>PERSOON||
|*Gemeente van inschrijving|INGESCHREVEN<br>PERSOON||
|*Huishoudenrelatie is een<br>natuurlijk persoon|INGESCHREVEN<br>PERSOON||
|*Huwelijk/partnerschap<br>bestaat uit|INGESCHREVEN<br>PERSOON||
|*Identiteitsbewijs van een<br>natuurlijk persoon|INGESCHREVEN<br>PERSOON||
|*Inschrijvingsadres|INGESCHREVEN<br>PERSOON||
|*Kind heeft moeder|INGESCHREVEN<br>PERSOON||
|*Kind heeft vader|INGESCHREVEN<br>PERSOON||
|*Land overlijden|INGESCHREVEN<br>PERSOON||
|*Land van emigratie|INGESCHREVEN<br>PERSOON||
|*Land van immigratie|INGESCHREVEN<br>PERSOON||
|*Nationaliteit van een natuurlijk<br>persoon|INGESCHREVEN<br>PERSOON||
|*Ouder heeft kind|INGESCHREVEN<br>PERSOON||
|*Verblijfstitel van een natuurlijk<br>persoon|INGESCHREVEN<br>PERSOON||
|A-nummer|INGESCHREVEN<br>PERSOON||
|Aanduiding bijzonder<br>Nederlanderschap|INGESCHREVEN<br>PERSOON||
|Aanduiding naamgebruik|NATUURLIJK<br>PERSOON||
|Burgerlijke staat|HUWELIJK /<br>GEREGISTREERD<br>PARTNERSCHAP||
|Datum inschrijving in<br>gemeente|INGESCHREVEN<br>PERSOON||



**31** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|Datum opschorting bijhouding|INGESCHREVEN<br>PERSOON|metagegeven|
|Datum overlijden|NATUURLIJK<br>PERSOON||
|Datum verkrijging verblijfstitel|INGEZETENE||
|Datum verlies verblijfstitel|INGEZETENE||
|Datum vertrek uit Nederland|INGESCHREVEN<br>PERSOON||
|Datum vestiging in Nederland|INGESCHREVEN<br>PERSOON||
|Geboortedatum|NATUURLIJK<br>PERSOON||
|Geboorteplaats|INGESCHREVEN<br>PERSOON||
|Geslachtsaanduiding|NATUURLIJK<br>PERSOON||
|Geslachtsnaam|NATUURLIJK<br>PERSOON||
|Indicatie curateleregister|INGEZETENE||
|Indicatie geheim|INGESCHREVEN<br>PERSOON||
|Indicatie gezag minderjarige|INGEZETENE||
|Omschrijving reden<br>opschorting bijhouding|INGESCHREVEN<br>PERSOON||
|Plaats overlijden|INGESCHREVEN<br>PERSOON||
|Voorletters|NATUURLIJK<br>PERSOON||
|Voornamen|NATUURLIJK<br>PERSOON||
|Voorvoegsel geslachtsnaam|NATUURLIJK<br>PERSOON||
|**Nevenvestiging**|VESTIGING||
|*Nevenvestiging|VESTIGING|Attribuutsoort ‘Typering<br>hoofd/nevenvestiging’.|
|**Niet-natuurlijk persoon**|NIET-<br>NATUURLIJK<br>PERSOON,<br>MAATSCHAPPELI<br>JKE ACTIVITEIT<br>en VESTIGING||
|*Hoofdactiviteit|MAATSCHAPPELI<br>JKE ACTIVITEIT<br>en VESTIGING|Gegeventype ‘NACE-code’.|
|*Nevenactiviteit|MAATSCHAPPELI<br>JKE ACTIVITEIT<br>en VESTIGING|Gegeventype ‘NACE-code’.|



**32** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Nevenvestiging|VESTIGING|Attribuutsoort ‘Typering<br>hoofd/nevenvestiging’.|
|*Rechtsvorm van een niet-<br>natuurlijk persoon|NIET-<br>NATUURLIJK<br>PERSOON||
|Aantal werkzame mannen<br>fulltime|-||
|Aantal werkzame mannen<br>parttime|-||
|Aantal werkzame vrouwen<br>fulltime|-||
|Aantal werkzame vrouwen<br>parttime|-||
|Datum einde niet-natuurlijk<br>persoon|INGESCHREVEN<br>NIET-<br>NATUURLIJK<br>PERSOON||
|Datum ontbinding niet-<br>natuurlijk persoon|INGESCHREVEN<br>NIET-<br>NATUURLIJK<br>PERSOON||
|Datum oprichting niet-<br>natuurlijk persoon|INGESCHREVEN<br>NIET-<br>NATUURLIJK<br>PERSOON||
|Handelsnaam|MAATSCHAPPELI<br>JKE ACTIVITEIT<br>en VESTIGING||
|Handelsregisternummer|MAATSCHAPPELI<br>JKE ACTIVITEI|KvK-nummer|
|Indicatie faillissement|-||
|Indicatie hoofdvestiging|VESTIGING|Attribuutsoort ‘Typering<br>hoofd/nevenvestiging’.|
|Indicatie surséance van<br>betaling|-||
|Soort niet-natuurlijk persoon|-||
|Statutaire naam /<br>Vennootschapsnaam|NIET-<br>NATUURLIJK<br>PERSOON||
|Zaaknaam|MAATSCHAPPELI<br>JKE ACTIVITEIT<br>en VESTIGING|Het NHR kent de handelsnaam.|
|**Niet-woonobject**|GEBOUWD<br>OBJECT||
|Aantal parkeerplaatsen|-||
|Frontbreedte|-||



**33** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|**Ouder-Kind**|OUDER-KIND-<br>RELATIE||
|*Kind heeft moeder|OUDER-KIND-<br>RELATIE||
|*Kind heeft vader|OUDER-KIND-<br>RELATIE||
|*Ouder heeft kind|OUDER-KIND-<br>RELATIE||
|Einddatum familierechtelijke<br>betrekking|OUDER-KIND-<br>RELATIE||
|Ingangsdatum<br>familierechtelijke betrekking|OUDER-KIND-<br>RELATIE||
|**Overig bouwwerk**|OVERIG<br>GEBOUWD<br>OBJECT||
|*Bestemming van een overig<br>bouwwerk|GEBOUWD<br>OBJECT||
|*Kadastraal object bij een<br>overig bouwwerk|GEBOUWD<br>OBJECT||
|*Locatieadres van een overig<br>bouwwerk|OVERIG<br>GEBOUWD<br>OBJECT||
|*Overig bouwwerk behoort tot<br>WOZ-object|OVERIG<br>GEBOUWD<br>OBJECT||
|*Overig bouwwerk is<br>onderdeel van bouwwerk|-|Zie opmerking bij Bouwwerk.|
|Omschrijving overig bouwwerk|-||
|Overig-bouwwerknummer|GEBOUWD<br>OBJECT||
|Type overig bouwwerk|OVERIG<br>GEBOUWD<br>OBJECT||
|**Pand**|PAND|De definitie en daarmee de afbakening van<br>een PAND is anders dan die in het GFO-<br>BG.|
|*Pand is onderdeel van<br>gebouw|-|Zie opmerking bij Gebouw.|
|*Verblijfsobject is onderdeel<br>van pand|PAND||
|Hoogste bouwlaag pand|PAND||
|Laagste bouwlaag pand|PAND||
|Pandnummer|PAND||
|**Persoonlijk identiteitsbewijs**|REISDOCUMENT||
|*Identiteitsbewijs van een<br>natuurlijk persoon|||
|*Soort identiteitsbewijs|||
|Nummer identiteitsbewijs|||



**34** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|**Persoonlijke nationaliteit**|INGESCHREVEN<br>PERSOON||
|*Code van een nationaliteit|INGESCHREVEN<br>PERSOON||
|*Nationaliteit van een natuurlijk<br>persoon|INGESCHREVEN<br>PERSOON||
|Datum verkrijging nationaliteit|INGESCHREVEN<br>PERSOON||
|Datum verlies nationaliteit|INGESCHREVEN<br>PERSOON||
|**Postadres**|-|Is niet meer als separaat objecttype<br>gemodelleerd.|
|*Land waarin postadres ligt|SUBJECT||
|Adres buitenland (1)|SUBJECT||
|Adres buitenland (2)|||
|Adres buitenland (3)|||
|Adres buitenland (4)|-||
|Antwoordnummer|SUBJECT||
|Postbusnummer|SUBJECT||
|**Publiekrechtelijke beperking**|-||
|*Code van een<br>publiekrechtelijke beperking|-||
|*Publiekrechtelijke beperking<br>rust op kadastraal object|-||
|Einddatum publiekrechtelijke<br>beperking|-||
|Ingangsdatum<br>publiekrechtelijke beperking|-||
|Vindplaats document|-||
|**SBI-codering**|-|Overeenkomstig het NHR niet separaat<br>gemodelleerd.|
|*Hoofdactiviteit|-||
|*Nevenactiviteit|-||
|SBI-code|VESTIGING|Gegeventype‘NACE-code’.|
|SBI-omschrijving|VESTIGING|Gegeventype‘NACE-code’.|
|**Soort identiteitsbewijs**|REISDOCUMENT||
|*Soort identiteitsbewijs|SOORT||
|Identiteitsbewijs (code)|||
|Omschrijving identiteitsbewijs|||
|**Soort publiekrechtelijke**<br>**beperking**|-||
|*Code van een<br>publiekrechtelijke beperking|-||
|Publiekrechtelijke beperking<br>code|-||
|Publiekrechtelijke beperking<br>omschrijving|-||
|**Soort rechtsvorm**|-|Overeenkomstig het NHR niet separaat<br>gemodelleerd.|



**35** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Rechtsvorm van een niet-<br>natuurlijk persoon|-||
|Rechtsvormcode|NIET-<br>NATUURLIJK<br>PERSOON||
|Rechtsvormomschrijving|NIET-<br>NATUURLIJK<br>PERSOON||
|**Soort zakelijk recht**|AARD<br>VERKREGEN<br>RECHT|Overeenkomstig de BRK niet separaat<br>gemodelleerd.|
|*Code van een zakelijk recht|AARD<br>VERKREGEN<br>RECHT||
|Aanduiding erfdienstbaarheid|-||
|Zakelijk recht omschrijving|AARD<br>VERKREGEN<br>RECHT||
|Zakelijk-rechtcode|AARD<br>VERKREGEN<br>RECHT||
|**Subject**|SUBJECT||
|*Correspondentieadres|SUBJECT||
|*Eigenaar|-|Gemodelleerd via ZAKELIJK RECHT.|
|*Gebruiker|-|Gemodelleerd als relatie met<br>VERBLIJFSOBJECT, STANDPLAATS EN<br>LIGPLAATS voor INGESCHREVEN<br>PERSOON en via VESTIGING voor NIET-<br>NATUURLIJK PERSOON.|
|*Subject heeft zakelijk recht|SUBJECT||
|*Verblijfs/vestigingsadres|INGESCHREVEN<br>PERSOON||
|*Voornaamste zakelijk<br>gerechtigde|RECHTSPERSOO<br>N||
|Aanvulling Sofi-nummer|NIET-<br>NATUURLIJK<br>PERSOON|NNP-ID|
|Bank/girorekeningnummer|SUBJECT||
|E-mail adres|SUBJECT||
|Faxnummer|SUBJECT||
|Sofi-nummer|-|Wel: BurgerServiceNummer (bij<br>INGESCHREVEN PERSOON) en NNP-ID<br>(bij NIET-NATUURLIJK PERSOON).|
|Subjectnummer AKR|-||
|Telefoonnummer|SUBJECT||



**36** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|**Verblijfsobject**|VERBLIJFS­<br>OBJECT|In sommige gevallen kan dit een OVERIG<br>GEBOUWD OBJECT of BENOEMD<br>TERREIN zijn aangezien de definitie van<br>verblijfsobject verschilt tussen de BGR en<br>het GFO-BG.|
|*Bestemming van een<br>verblijfsobject|GEBOUWD<br>OBJECT||
|*Filiatie verblijfsobject is<br>ontstaan uit verblijfsobject|BENOEMD<br>OBJECT||
|*Filiatie verblijfsobject is<br>overgegaan in verblijfsobject|BENOEMD<br>OBJECT||
|*Kadastraal object bij een<br>verblijfsobject|BENOEMD<br>OBJECT||
|*Locatieadres van een<br>verblijfsobject|BENEOEMD<br>OBJECT||
|*Verblijfsobject behoort tot<br>WOZ-object|BENOEMD<br>OBJECT||
|*Verblijfsobject is onderdeel<br>van pand|VERBLIJFS­<br>OBJECT|n:m-relatie (in de BGR) i.p.v. een n:1-relatie<br>(in het GFO-BG).|
|Aan/uitbouw|-||
|Aantal ruimten|-||
|Bebouwde terreinoppervlakte|-||
|Bouwjaar|PAND||
|Bouwjaarklasse|-||
|Bouwkundige bestemming<br>actueel|GEBOUWD<br>OBJECT||
|Bouwkundige bestemming<br>oorspronkelijk|-||
|Bouwtechnische<br>kwaliteitsaanduiding|-||
|Bruto inhoud|GEBOUWD<br>OBJECT||
|Bruto vloeroppervlak|-||
|Centroïd x-coördinaat<br>verblijfsobject|GEBOUWD<br>OBJECT||
|Centroïd y-coördinaat<br>verblijfsobject|GEBOUWD<br>OBJECT||
|Centroïd z-coördinaat<br>verblijfsobject|-||
|Datum aanvang bouw|PAND|Metagegeven van Pandstatus|
|Datum bouw gereed|PAND|Metagegeven van Pandstatus|
|Datum sloop|PAND|Metagegeven van Pandstatus|
|Gemiddelde breedte<br>verblijfsobject|-||
|Gemiddelde hoogte<br>verblijfsobject|-||
|Gemiddelde lengte<br>verblijfsobject|-||



**37** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|Hoogste bouwlaag<br>verblijfsobject|VERBLIJFS­<br>OBJECT||
|Laagste bouwlaag<br>verblijfsobject|VERBLIJFS­<br>OBJECT||
|Lifttype|-||
|Monumentaanduiding|-||
|Onbebouwde<br>terreinoppervlakte|-||
|Onderhoudstoestand|-||
|Renovatiejaar|-||
|Verblijfsobjectnummer|BENOEMD<br>OBJECT||
|Verblijfsobjecttype|VERBLIJFS­<br>OBJECT|Betreft het gegeventype Gebruiksdoel in de<br>BGR.|
|**Verblijfstitel**|-|Overeenkomstig de GBA niet separaat<br>gemodelleerd.|
|*Verblijfstitel van een natuurlijk<br>persoon|INGEZETENE||
|Aanduiding verblijfstitel|INGEZETENE||
|Einddatum verblijfstitel|INGEZETENE||
|Ingangsdatum verblijfstitel|INGEZETENE||
|Verblijfstitelomschrijving|INGEZETENE||
|**Wijk**|WIJK||
|*Buurt in een wijk|WIJK||
|*Wijk bij een locatieadres|BENOEMD<br>OBJECT|Relatie loopt via BUURT.|
|*Wijk in een gemeente|WIJK||
|Einddatum wijk|WIJK||
|Ingangsdatum wijk|WIJK||
|Wijkcode|WIJK||
|Wijknaam|WIJK||
|**Woonobject**|VERBLIJFS­<br>OBJECT||
|Aantal woonlagen|-||
|Aantal woonvertrekken|-||
|Bereikbaarheid<br>hoofdwoonvertrek|-||
|Binnenwerkse kernoppervlakte|-||
|Soort woonobject|-||
|Woonoppervlakte|-||
|**WOZ-object**|WOZ-OBJECT||
|*Eigenaar|WOZ-BELANG||
|*Gebruiker|WOZ-BELANG||
|*Hoofdadres van een WOZ-<br>object|WOZ-OBJECT||
|*Huishouden is gehuisvest in<br>WOZ-object|-|Gemodelleerd naar VERBLIJFSOBJECT.|
|*Kadastraal object bij een<br>WOZ-object|WOZ-OBJECT||



**38** 

|**Gegevensgroep resp.**<br>**gegeven in GFO-BG**|**Objecttype waarbij**<br>**de gegevensgroep**<br>**resp. het gegeven is**<br>**opgenomen**|**Opmerking**|
|---|---|---|
|*Nevenadres van een WOZ-<br>object|-||
|*Overig bouwwerk behoort tot<br>WOZ-object|WOZ-OBJECT|Relatie naar OVERIG GEBOUWD OBJECT<br>via WOZ-DEELOBJECT|
|*Verblijfsobject behoort tot<br>WOZ-object|WOZ-OBJECT|Via WOZ-DEELOBJECT|
|Activiteit feitelijk|-||
|Huurprijs|-||
|Huurprijs (euro)|-||
|Peildatum huurprijs|-||
|Vastgestelde waarde|-||
|Vastgestelde waarde (euro)|WOZ-WAARDE||
|Waardepeildatum|WOZ-WAARDE||
|WOZ-objectnummer|WOZ-OBJECT||
|**Zakelijk recht**|ZAKELIJK RECHT||
|*Code van een zakelijk recht|ZAKELIJK RECHT||
|*Subject heeft zakelijk recht|ZAKELIJK RECHT||
|*Zakelijk recht rust op<br>kadastraal object|ZAKELIJK RECHT||
|Einddatum zakelijk recht|ZAKELIJK RECHT||
|Indicatie zakelijk recht met<br>meer zaken verkregen|KADASTRALE<br>ONROERENDE<br>ZAAK||
|Ingangsdatum zakelijk recht|ZAKELIJK RECHT||
|Koopjaar zakelijk recht|-||
|Koopsom zakelijk recht|-||
|Koopsom zakelijk recht (euro)|KADASTRALE<br>ONROERENDE<br>ZAAK||
|Noemer aandeel zakelijk recht|ZAKELIJK RECHT||
|Teller aandeel zakelijk recht|ZAKELIJK RECHT||



**39** 

