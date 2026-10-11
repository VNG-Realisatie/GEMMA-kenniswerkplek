Ondersteunde Modelelementen - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# Gebruik modelelementen

Modelelementen zijn de bouwstenen van een informatiemodel. Het zijn de formele constructies waarmee concepten, eigenschappen en relaties uit de werkelijkheid worden vastgelegd in een model. Voorbeelden van modelelementen zijn objecttypen, attributen, relaties, datatypen en enumeraties. Samen bepalen zij de structuur, betekenis en samenhang van de informatie die in een domein wordt beschreven.

Het GGM bouwt voort op de modelelementen zoals gedefinieerd in de kern van het MIM (Metamodel Informatiemodellering). Door deze landelijke standaard als fundament te gebruiken, sluit het model naadloos aan bij bestaande afspraken en kunnen de verschillende onderdelen van het GGM eenduidig worden geïnterpreteerd. Daarbij voegt het GGM eigen uitbreidingen en conventies toe, zodat de modelelementen optimaal aansluiten bij de gemeentelijke context en ondersteunende tooling zoals de DDL-generator.

MIM is een toepassingensprofiel op UML (Unified Modelling Language), en dan met name op de Class-diagrammen. UML is een wereldwijd toegepaste standaard voor informatiemodelleren. Om deze reden verwijzen wij ook naar de gebruikte UML-modeltypen. Hierbij nemen we UML v2.5.1 als uitgangspunt.

## Modelelementen ondersteund door het GGM

### Kernelementen

In onderstaande tabel wordt getoond welke modelelementen uit de kern van MIM worden ondersteund, en wat de relatie ten opzichte van UML is.

MIM-modelelement
UML-equivalent
Ondersteuning GGM

Objecttype
Klasse
Volledig ondersteund

Attribuutsoort
Attribuut
Volledig ondersteund

Gegevensgroep
Geen UML-constructie*
Geen ondersteuning

Gegevensgroeptype
Geen UML-constructie*
Geen ondersteuning

Generalisatie
Generalisatie
Volledig ondersteund

Relatiesoort
Associatie
Volledig ondersteund

Relatiesoort
Aggregatie
Ondersteund, maar wordt voor database DDL als associatie beschouwd

Relatieklasse
Association Klasse
Geen ondersteuning**

Relatierol, Relatierol bron en doel
Rolnaam van een association end (UML)
Volledig ondersteund

Datatype
Datatype
Ondersteund (zie ook datatypes)

* In UML wordt dit meestal gemodelleerd met een klasse die als type fungeert voor een samengestelde eigenschap, of met een datatype.

Het verschil is dat een datatype in UML geen identiteit kent (waardoor het meer lijkt op een MIM-gegevensgroep), terwijl een klasse wél een eigen identiteit heeft.

** Als je een constructie wilt modelleren met een associatieklasse dan gebruik je voor het GGM een Objecttype/Klasse met associaties beide kanten op (koppetabelconstructie).

### Ondersteunde datatypes

Het GGM ondersteunt de volgende datatypes uit het MIM):

MIM-datatype
UML-equivalent
Ondersteuning GGM

Primitief Datatype
Primitive type
Ondersteund, zie tabel

Gestructureerd datatype
DataType
Volledig ondersteund, via verwijzing naar Klasse van het DataType

Data-element
Property
Volledig ondersteund als attribuut van de DataType Klasse

Enumeratie en Enumeratiewaarde*
Enumeration
Volledig ondersteund

Referentielijst en Referentielijstelement*
Geen directe UML-vertaling, veelal Enumeration
Geen ondersteuning

Codelijst*
Geen directe UML-vertaling, veelal Klasse
Geen ondersteuning

*Uitleg lijstsoorten: een enumeratie is een vaste, beperkte lijst van waarden die volledig in het informatiemodel zelf wordt gedefinieerd en nauwelijks verandert (bijv. geslacht: man, vrouw, onbekend). Een referentielijst is eveneens een gesloten set waarden, maar wordt extern beheerd door een bronorganisatie en in het model alleen gerefereerd (bijv. ISO-landcodes). Een codelijst ten slotte is een open of dynamische lijst waarvan de waarden in de tijd kunnen wisselen of groeien, vaak beheerd buiten het model (bijv. product- of gemeentecodes).

### Ondersteunde primitieve datatypes

In het GGM kunnen alle primitieve datatypes zoals gespecificeerd in het MIM woerden toegepast. Daarnaast is er een aantal datatypes dat als extensie op MIM kan worden toegepast. Deze worden in de volgende tabel getoond. Het GGM ondersteunt bovendien aanvullende namen voor verschillende primitieve datatypes, dit om compatibiliteit met oudere informatiemodellen te garanderen. Deze worden in de derde kolom van de tabel getoond.

MIM-primitieve
UML-equivalent
Door GGM ondersteunde varianten (case insensitive)

CharacterString
String
characterString, string, text, memo, char, varchar, character varying, string text, AN.. (alfanumeriek met lengte)

Integer
Integer
integer, int, number, short, long, N.. (numeriek met lengte)

Decimal
Real / Decimal
decimal, float, double, real, decimaal

Boolean
Boolean
boolean, bool, ja/nee, ja nee, ja/neen, yes no, indic, stdindjn

Date
Date
date, datum

DateTime
DateTime
datetime, datumtijd

Time
Time
time, tijd

URI
String (gespecialiseerd)
uri, url, link

Bedrag (Extensie op MIM)
Class / DataType (specifiek)
bedrag, currency, monetair, geldbedrag

Email (Extensie op MIM)
Class / DataType (specifiek)
email, e-mail

Blob (Extensie op MIM)
Class / DataType (specifiek)
blob

Onvolledige datum (Extensie op MIM)
Class / DataType (specifiek)
onvolledigedatum, onvolledige_datum

GM_Point (Extensie op MIM)
Class (geo-objecttype)
GM_Point, punt, point, coordinate, coördinaat, geopunt, coordinaat, gml, locatie, spatial, geometrie

Blob (Extensie op MIM)
DataType (binary)
blob, binary, byte

GUID (Extensie op MIM)
DataType (identifier)
guid

GM_… (Geofamilie) (Extensie op MIM)
Class (geo-objecttypen)
alle GM-namen die beginnen met GM_ (bijv. GM_Curve, GM_Surface, GM_Solid), plus hun varianten

### Ondersteuning overige modelelementen

Naast de basis-modelelementen ondersteunt het GGM ook aanvullende elementen die belangrijk zijn voor modelintegriteit en interoperabiliteit:

MIM-modelelement
UML-equivalent
Ondersteuning in GGM

Constraint
Constraint (UML-construct op Class, Attribute of Association)
Beperkt: nog niet systematisch ondersteund, kan worden opgenomen maar wordt niet vertaald naar DDL's of Linked Data.

Keuze
GeneralizationSet met disjoint/complete of Union Class
Beperkt: conceptueel aanwezig, maar GGM vertaalt keuzes meestal naar optionele attributen of enumeraties.

Relatierol
Association End Role
Volledig: rollen worden als relatierol gemodelleerd in GGM en EA (naam + multipliciteit).

Relatierol bron
Association End (source end)
Volledig: bronzijde van associaties is herkenbaar en wordt ondersteund.

Relatierol doel
Association End (target end)
Volledig: doelzijde van associaties is herkenbaar en wordt ondersteund.

Externe koppeling
Dependency of Association naar extern model
GGM kent zelf geen Externe koppelingen, maar kan wel datamodellen integreren op basis van Externe koppelingen. In dit geval zijn externe koppelingen juist noodzakelijk.

Informatiemodel
Model / Package
Volledig: GGM zelf is een MIM-informatiemodel, gerepresenteerd als Package-structuur.

Domein
Package
Volledig: GGM-domeinen worden als packages uitgewerkt, incl. release-tag.

Extern
Package (met stereotype «extern»)
GGM kent zelf geen Externe elementen zoals packages, maar kan wel datamodellen integreren op basis van Externe koppelingen. In dit geval zijn externe koppelingen juist noodzakelijk.

View
Package of Diagram met subset van elementen
Beperkt: views worden niet systematisch uitgewerkt in GGM, maar wel als diagrammen toegepast.

## Regels modelelementen

Veel regels voor het gebruik van modelelementen staan expliciet of impliciet beschreven in het MIM. Voor het gebruik van het GGM is een aantal regels van speciaal belang. Deze staan in deze paragraaf beschreven.

Ontwerpregel m1: Voeg altijd definities toe

- Definities zijn belangrijk om de betekenis van je modelelementen te kunnen begrijpen

- Definities zijn verplicht bij: Objecttypes en Enumeraties

- Voeg definities toe aan attributen en enumeratiewaarden als de betekenis niet direct uit de naam voortvloeit.

Ontwerpregel m2: Naamgeving is verplicht

- Naamgeving is verplicht bij: Objecttypes, Enumeraties en attribuutsoorten

- Naamgeving voor associaties is optioneel

Ontwerpregel m3: Attributen hebben altijd een datatype uit de lijst ondersteunde datatypes

- Alle attributen hebben een datatype uit de lijst ondersteunde datatypes

- Als het een primitief datatype is komt deze uit de lijst ondersteunde primitieve datatypes

- Als het geen primitief datatype is wordt altijd verwezen naar een Enumeratie of Objecttype in scope van het model

Ontwerpregel m4: Objecttypen hebben altijd tenminste 1 attribuut

- Alle objecttypen hebben tenminste 1 attribuut

- De attributen kunnen ook door overerving (generalisatie) worden verkregen

Ontwerpregel m5: Enumeraties hebben altijd tenminste 1 enumeratiewaarde

- Lege enumeraties hebben geen betekenis

Ontwerpregel m6: Relatietypen en generalisaties hebben altijd een begin- en eindpunt

- Alle relaties zijn verbonden aan twee objecttypen

- Voor associaties kan dat hetzelfde objecttype zijn

- Voor generalisaties en aggregaties zijn dat altijd verschillende objecttypen

Ontwerpregel m7: Kardinaliteit is verplicht

- Alle relaties kennen aan het beginpunt en aan het eindpunt een kardinaliteit

- Als geen kardinaliteit is opgegeven wordt dat opgevat als kardinaliteit 1
