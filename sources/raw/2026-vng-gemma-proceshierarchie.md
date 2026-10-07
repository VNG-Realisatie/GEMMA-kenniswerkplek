Procesarchitectuur Proceshiërarchie - GEMMA Online

Ga direct naar het tekstgedeelte
Ga direct naar zoeken
Ga direct naar de navigatie

GEMMA Online

- Inloggen

- Contact

- GEMMA Online
- Basisarchitectuur
- Bedrijfsarchitectuur
- Procesarchitectuur
- Procesarchitectuur Proceshiërarchie

# Procesarchitectuur Proceshiërarchie

Bekijk inhoudsopgave

## Inhoud

- 1 Typen processen

- 2 Samenstelling van processen

- 3 Specialisaties

- 4 Ketensamenwerking

## Typen processen[bewerken]

Bij het classificeren van bedrijfsprocessen maken we onderscheid tussen sturende processen, uitvoerende (primaire) processen en ondersteunende processen. Deze definiëren we als volgt:

Type Definitie Voorbeeld

Sturende processen De processen die zorgen voor het vormen van de strategie, en het programmeren en evalueren hiervan. Deze processen zijn door het voortbrengen van kaders en de doelen vooral gericht op het aansturen van de primaire processen van de gemeente. Deze processen hebben interne klanten. Het proces "Opstellen begroting".

Primaire Processen Processen die gericht zijn op het door de organisatie leveren van toegevoegde waarde aan haar omgeving. Het zijn processen waaraan de organisatie haar bestaansrecht ontleent. Deze lopen van klant (aanvraag) en/of samenleving (maatschappelijke behoefte) tot diezelfde klant (product) en/of samenleving (effect in de stad). Deze processen hebben externe klanten. Het proces "Behandelen vergunningaanvraag".

Ondersteunende processen Processen die resultaten voortbrengen die niet direct zichtbaar zijn voor de burger, maar essentiële ondersteuning leveren voor het effectief kunnen uitvoeren van de primaire processen, andere ondersteunende processen of de gehele organisatie. Deze processen hebben interne klanten. Het proces "Beheren archief en informatie".

## Samenstelling van processen[bewerken]

We kunnen processen op verschillende niveaus beschouwen; een proces op een hoger niveau is dan samengesteld uit ("aggregeert") een of meerdere processen op een lager niveau. Elk proces bestaat zo uit delen, en ieder procesdeel bestaat weer uit een nog kleiner geheel. Vergelijkbaar met een reeks Matroesjka-poppetjes, waar uit elk poppetje weer een kleiner poppetje tevoorschijn komt. Het hoogste niveau dat we in deze hiërarchie onderkennen is het klant-tot-klant- ofwel bedrijfsproces. Onderstaande figuur toont in een ArchiMate-diagram de niveaus die we in de GEMMA procesarchitectuur onderkennen:

BusinessProcess

Bedrijfsproces

BusinessProcess

Deelproces

BusinessProcess

Processtap

BusinessProcess

Handeling

AggregationRelationship

AggregationRelationship

AggregationRelationship

Deze svg is op 17-09-2026 11:31:33 CEST gegenereerd door ArchiMedes™ © 2016-2026 ArchiXL.

ArchiMedes 17-09-2026 11:31:33 CEST

Proceshiërarchie (uit model: GEMMA) - Toon SVG

We hanteren de volgende definities voor de niveaus:

Niveau Definitie Voorbeeld

Bedrijfsproces Een bedrijfsproces (ook wel genoemd klant-tot-klantproces) is een onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerde, geordende reeks deelprocessen, gerelateerd aan een interne of externe klant en gericht op het leveren van een dienst aan die klant. Het proces "Behandelen vergunningaanvraag".

Deelproces Een deelproces is een onder verantwoordelijkheid van één bedrijfsfunctie uitgevoerde, geordende reeks processtappen, gericht op het leveren van een deeldienst die een noodzakelijke of gewenste bijdrage levert aan een uiteindelijk aan de klant te leveren dienst. In de voorgaande versie van de procesarchitectuur werd dit niveau "werkproces" genoemd. Het deelproces "Intake vergunningaanvraag".

Processtap Een processtap is een onder verantwoordelijkheid van één persoon (rol) handmatig of geautomatiseerd uitgevoerde, geordende reeks handelingen gericht op het bijdragen aan de levering van een deeldienst. De processtap "Versturen ontvangstbevestiging".

Handeling Kleinst mogelijke eenheid van werk, uitgevoerd door één persoon of machine op één plek op één moment. De handeling "Opvragen adres uit de basisregistratie".

Deze indeling geldt voor drie de typen processen sturend, uitvoerend en ondersteunend. Voor elk niveau geldt dat we spreken van een proces wanneer we het hebben over een logisch samenhangende "eenheid" activiteiten. Het onderkennen van dergelijke eenheden is zinvol voor het vergelijkbaar maken (zowel binnen alsook tussen gemeenten) van processen; voor het toewijzen aan rollen/afdelingen; voor het coherent kunnen aansturen; voor het kunnen toepassen van procesbouwstenen; en voor het kunnen uitbesteden van logische eenheden werk aan (keten)partners. Uitbesteding op het niveau van deelprocessen ligt het meest voor de hand, maar ook het uitbesteden van een geheel bedrijfsproces is mogelijk.

Op een aantal plaatsen in de procesarchitectuur spreken we van clusters van bedrijfsprocessen, bijvoorbeeld een cluster van bedrijfsprocessen die gerelateerd zijn aan personeelszaken. Het betreft dan een groepering van bedrijfsprocessen die bij elkaar horen omdat ze op hetzelfde 'thema' betrekking hebben.

## Specialisaties[bewerken]

Naast het onderkennen van aggregatieniveaus kunnen we ook specialisaties onderkennen. We moeten deze twee niet met elkaar verwarren. Waar het bij aggregaties gaat om het onderkennen dat een proces uiteenvalt in stukjes, gaat het bij specialisaties om het onderkennen van gemeenschappelijkheden en verbijzonderingen (dat is dus geen extra niveau in bovenstaande "ladder"). Zo zijn de processen "Behandelen evenementenvergunningaanvraag" en "Behandelen omgevingsvergunningaanvraag" specialisaties van het (generieke) proces "Behandelen vergunningaanvraag". Het bedrijfsproces "Behandelen omgevingsvergunningaanvraag" kan zelf ook weer twee specialisaties kennen: een reguliere en een uitgebreide variant. Onderstaande figuur toont dit voorbeeld in een ArchiMate-diagram.

BusinessProcess

Behandelen evenementen-
vergunningaanvraag

BusinessProcess

Behandelen omgevings-
vergunningaanvraag

BusinessProcess

Behandelen
vergunningaanvraag

BusinessProcess

Behandelen omgevings-
vergunningaanvraag
regulier

BusinessProcess

Behandelen omgevings-
vergunningaanvraag
uitgebreid

SpecializationRelationship

SpecializationRelationship

SpecializationRelationship

SpecializationRelationship

Deze svg is op 16-09-2026 20:17:05 CEST gegenereerd door ArchiMedes™ © 2016-2026 ArchiXL.

ArchiMedes 16-09-2026 20:17:05 CEST

Proceshiërarchie - specialisatie (open view in nieuw venster)

Het onderkennen van specialisaties is zinvol om gelijkvormigheid te onderstrepen. Gelijkvormigheid in de uitvoering van processen heeft als voordeel dat het de kans op fouten verkleint en de doelmatigheid vergroot, onder meer door de mogelijkheid van generieke geautomatiseerde ondersteuning. Teruggrijpend op het voorbeeld: het behandelen van een evenementenvergunningaanvraag zal op grotendeels gelijke wijze worden uitgevoerd als het behandelen van een omgevingsvergunningaanvraag, conform het generieke stramien van het behandelen van om het even welk type vergunningaanvraag. Wellicht kan voor het afhandelen van beide typen vergunningaanvragen ook hetzelfde softwarepakket gebruikt worden.

In de procesarchitectuur kijken we op generiek niveau naar de processen, en zoeken daarin naar genericiteit en overeenkomsten tussen de processen. In een producten-en-dienstencatalogus staan alle te leveren diensten; dat zijn er veel meer dan dat er processen zijn. Dat komt omdat meerdere diensten met hetzelfde proces geleverd kunnen worden. Voor zover er kleine verschillen in de procesgang zijn bij gerelateerde diensten, kunnen we specialisatie toepassen.

## Ketensamenwerking[bewerken]

Er is sprake van ketensamenwerking wanneer een gemeente bij de uitvoering van een klant-tot-klantproces afhankelijk is van een andere organisatie (een waterschap, provincie, ...), of andersom. Dit kan onder meer zijn omdat die andere organisatie een advies moet geven of ergens mee moet instemmen. Vanuit procesperspectief betekent dit dat twee bedrijfsprocessen, van twee organisaties, elkaar raken. We doelen hier op situaties waarbij er geen overkoepelende aansturing is; elke overheid heeft en houdt zijn eigen verantwoordelijkheid. Bijvoorbeeld: als een gemeente en een waterschap samenwerken in het kader van een omgevingswetvergunningaanvraag, dan hebben beide organisaties hun eigen verantwoordelijkheid; daar verandert niets aan door de samenwerking. Ketensamenwerking draait daarom vooral om vertrouwen bij het maken en nakomen van afspraken.

Ketensamenwerking wordt soms aangeduid als "ketenproces", een proces op een hoger niveau dan de eigen bedrijfsprocessen. Hoewel dat in de discussie over samenwerking zinvol kan zijn, is het belangrijk om te begrijpen dat die uitspraak vanuit de procesarchitectuur gezien niet correct is. Wanneer we ketensamenwerking in ArchiMate willen modelleren, doen we dat niet als een proces dat uit andere processen is samengesteld (dus met een aggregatierelatie, zoals in de hierboven beschreven proceshiërarchie) maar als een bedrijfsinteractie waarin de bedrijfsprocessen van de betrokken organisaties samenkomen.

Dat is anders dan wanneer een gemeente een deelproces of processtap uitbesteedt aan een derde partij; in dat geval is er sprake van een "gewone" klant-leverancierrelatie. Daarbij behoudt de uitbestedende partij de eindverantwoordelijkheid over het gehele bedrijfsproces. Voorbeelden van uitbesteding zijn het inschakelen van een taxatiebureau, deurwaarder of accountant voor specifieke taken.

Onderstaand ArchiMate-diagram toont het verschil tussen ketensamenwerking zoals hierboven beschreven (links) en samenwerking in een uitbestedingsrelatie (rechts):

BusinessInteraction

Ketensamenwerking

BusinessProcess

Bedrijfsproces 1

BusinessProcess

Bedrijfsproces 2

BusinessRole

Verantwoordelijke
organisatie 1

BusinessRole

Verantwoordelijke
organisatie 2

BusinessRole

Verantwoordelijke
organisatie 1

BusinessProcess

Bedrijfsproces 1

BusinessProcess

Deelproces 1A

BusinessRole

Uitvoerende organisatie 1

BusinessRole

Uitvoerende organisatie 2

BusinessRole

Uitvoerende organisatie 1

BusinessProcess

Deelproces 1B

BusinessProcess

Deelproces 1C

BusinessRole

Uitvoerende organisatie 2

ServingRelationship

ServingRelationship

AssignmentRelationship

AssignmentRelationship

AssignmentRelationship

AggregationRelationship

AggregationRelationship

AggregationRelationship

AssignmentRelationship

AssignmentRelationship

AssignmentRelationship

AssignmentRelationship

AssignmentRelationship

Deze svg is op 17-09-2026 11:31:34 CEST gegenereerd door ArchiMedes™ © 2016-2026 ArchiXL.

ArchiMedes 17-09-2026 11:31:34 CEST

Ketensamenwerking (open view in nieuw venster)

Ketensamenwerking wordt steeds belangrijker en heeft behoorlijke impact op de procesarchitectuur. Meer hierover is beschreven onder Impact van ketensamenwerking.

Een samenhangende set Diensten, Bedrijfsobjecten en/of Representaties die onder in een Overeenkomst beschreven voorwaarden kan worden afgenomen.

De betekenis die mensen geven aan gegevens in een context.

Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst.

Afkorting van Gemeentelijke Modelarchitectuur. De referentiearchitectuur voor Nederlandse gemeenten, die beschrijft hoe gemeentelijke processen, informatiesystemen, gegevens en infrastructuur samenhangen, en richting geeft aan inrichting en ontwikkeling van de gemeentelijke informatievoorziening.

Onderdeel van de bedrijfsarchitectuur met principes en afspraken voor het inrichten van bedrijfsprocessen.

Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een Product of Dienst.

Een prestatie die een dienstverlener levert aan een dienstafnemer.

Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn.

Een door de overheid officieel aangewezen registratie met daarin gegevens van hoogwaardige kwaliteit, die door alle overheidsinstellingen verplicht en zonder nader onderzoek, worden gebruikt bij de uitvoering van publiekrechtelijke taken.

Breed toepasbaar en herbruikbaar.

Overgenomen van "https://www.gemmaonline.nl/index.php?title=Procesarchitectuur_Proceshiërarchie&oldid=218521"

Deze pagina is voor het laatst bewerkt op 17 nov 2025 om 15:00.

Categorie:

- Procesarchitectuur

Terug naar boven
