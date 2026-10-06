De soorten gegevens | RvIG

Overslaan en naar de inhoud gaan

Rijksdienst voor Identiteitsgegevens
Ministerie van Binnenlandse Zaken en Koninkrijksrelaties

Zoeken

Zoeken...

Zoeken

Handleiding Uitvoeringsprocedures HUP

#
De soorten gegevens

## Wat kun je vinden op deze pagina?

- Algemene gegevens
- Administratieve gegevens
- Verwijsgegevens
- Technische gegevens
- Gegeven bij de persoonslijst

De gegevens op de persoonslijst zijn onderverdeeld in verschillende soorten die ieder hun eigen functie hebben:

- Algemene gegevens
- Administratieve gegevens
- Verwijsgegevens
- Technische gegevens
- Gegeven bij de persoonslijst

In één categorie kunnen meerdere soorten gegevens voorkomen. De gegevens in een groep binnen één categorie zijn altijd van dezelfde soort. In het Gegevenswoordenboek, van het LO BRP is in paragraaf 4.8 bij elk gegeven in elke categorie aangegeven welk soort gegeven het betreft.

## Algemene gegevens

Algemene gegevens vormen de belangrijkste gegevens van de BRP. Het gaat onder andere om het administratienummer (A-nummer), het burgerservicenummer (BSN), de naamgegevens, de geboortedatum, de nationaliteit, het adres van de ingeschreven persoon en de gegevens in verband met de uitvoering van de Kieswet, de Paspoortwet en de Wet op de Nederlandse identiteitskaart.

Algemene gegevens worden niet verwijderd of overschreven. Daarop zijn twee soorten uitzonderingen:

- de gegevens in categorie 12 Reisdocument en categorie 13 Kiesrecht;
- het verwijderen of overschrijven van gegevens bij Adoptie of Geslachtswijziging.

In andere gevallen ontstaat bij het corrigeren van algemene gegevens historie. In de door correctie ontstane historie wordt altijd in element 84.10 Indicatie onjuist de “O” opgenomen. Onjuiste categorieën mogen niet meer inhoudelijk worden gewijzigd.

### Toelichting bij voorbeelden:

Hieronder is er een onjuist gegeven opgenomen in een actuele categorie, dan corrigeer je die categorie. Door deze correctie ontstaat historie. Je neemt in de categorie die historisch wordt door deze procedure in element Indicatie onjuist de “O” op. In onderstaand voorbeeld is de gezagssituatie over een minderjarige persoon opgenomen (ouder1 en een derde hebben het gezag). Toen bleek dat niet ouder1, maar ouder2 samen met een derde belast was met het gezag, is dit gecorrigeerd.

Onjuist gegeven komt alleen voor in de actuele categorie

V3.1.1a

Categorie 11 Gezagsverhouding

32.10 Indicatie gezag minderjarige 2D

33.10 Indicatie curateleregister

82.10 Gemeente document Eigen gemeente

82.20 Datum document Systeemdatum

82.30 Beschrijving document uittreksel gezagsregister

85.10 Ingangsdatum geldigheid 29-11-2014

86.10 Datum van opneming Systeemdatum

Categorie 61 Gezagsverhouding

32.10 Indicatie gezag minderjarige 1D

33.10 Indicatie curateleregister

82.10 Gemeente document 0917 Heerlen

82.20 Datum document 14-12-2014

82.30 Beschrijving document uittreksel gezagsregister

84.10 Indicatie onjuist O Onjuist

85.10 Ingangsdatum geldigheid 29-11-2014

86.10 Datum van opneming 14-12-2014

Hieronder is er een onjuist gegeven opgenomen in een historische categorie, dan corrigeer je de betreffende categorie. Je voegt een nieuwe historische categorie toe. In onderstaand voorbeeld is de gezagssituatie over de ingezetene opgenomen (Ouder1 en Ouder2 hebben het gezag) en vervolgens is de gezagssituatie beëindigd. Toen bleek dat de ingangsdatum geldigheid in de historische categorie verkeerd was, is dit gecorrigeerd.

Onjuist gegeven komt alleen voor in een historische categorie

V3.1.1b

Categorie 11 Gezagsverhouding

32.10 Indicatie gezag minderjarige

33.10 Indicatie curateleregister

82.10 Gemeente document

82.20 Datum document

82.30 Beschrijving document

85.10 Ingangsdatum geldigheid 04-10-2017

86.10 Datum van opneming 01-11-2017

Categorie 61 Gezagsverhouding

32.10 Indicatie gezag minderjarige 12

33.10 Indicatie curateleregister

82.10 Gemeente document Eigen gemeente

82.20 Datum document Systeemdatum

82.30 Beschrijving document uittreksel gezagsregister

84.10 Indicatie onjuist

85.10 Ingangsdatum geldigheid 30-01-2014

86.10 Datum van opneming Systeemdatum

Categorie 61 Gezagsverhouding

32.10 Indicatie gezag minderjarige 12

33.10 Indicatie curateleregister

82.10 Gemeente document 0106 Assen

82.20 Datum document 24-02-2014

82.30 Beschrijving document uittreksel gezagsregister

84.10 Indicatie onjuist O Onjuist

85.10 Ingangsdatum geldigheid 29-01-2014

86.10 Datum van opneming 24-02-2014

Hieronder is in het voorbeeld een onjuist gegeven opgenomen in zowel een actuele als in een of meer historische categorieën, dan corrigeer je alle categorieën waarin dat gegeven voorkomt. Voor elke onjuiste categorie komt een nieuwe categorie in de plaats.

Als meerdere (historische) categorieën gecorrigeerd worden, moet of groep 81 Akte of groep 82 Document als volgt worden ingevuld:

- in de gecorrigeerde oudste categorie wordt het brondocument opgenomen aan de hand waarvan de gegevens gecorrigeerd zijn en
- in elke gecorrigeerde recentere categorie worden de brondocumentgegevens (groep 81 Akte of groep 82 Document) uit de onderliggende onjuiste categorie ongewijzigd overgenomen. Dit betreft categorieën met latere actualiseringen waarin het onjuiste gegeven wel gecorrigeerd moet worden maar waarbij het brondocument wat bij die latere actualisering hoort niet overschreven mag worden.

In onderstaand voorbeeld zijn al drie procedures uitgevoerd:

- de geboorte van een kind op 15-04-2002
- het aanvullen van gerelateerdengegevens op 20-06-2010
- het verwerken van een voornaamswijziging van het kind per 28-08-2012

Toen (uit een latere vermelding bij de geboorteakte) bleek dat de geslachtsnaam van het kind gecorrigeerd is vanaf geboortedatum, is de persoonslijst van de ouder ook gecorrigeerd. Omdat de onjuiste geslachtsnaam in zowel de actuele categorie als de twee historische categorieën voorkomt, zijn alle categorieën gecorrigeerd. Hierbij geldt dat de eerste correctie aan de hand van het brondocument (de geboorteakte) plaatsvindt. Bij de rest van de correcties zijn de gegevens in groep 81 Akte en 82 Document ongewijzigd overgenomen van de oorspronkelijke categorieën.

Onjuist gegeven komt voor in zowel de actuele als historische categorie(en)

V3.1.1c

Categorie 09 Kind

01.10 A-nummer Gevuld

01.20 Burgerservicenummer Gevuld

02.10 Voornamen Madelief

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Erikson

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte 0599

81.20 Aktenummer 10M1234

82.10 Gemeente document

82.20 Datum document

82.30 Beschrijving document

85.10 Ingangsdatum geldigheid 28-08-2012

86.10 Datum van opneming Systeemdatum

Categorie 59 Kind

01.10 A-nummer Gevuld

01.20 Burgerservicenummer Gevuld

02.10 Voornamen Madelief

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Dubbeldam

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte 0599

81.20 Aktenummer 10M1234

82.10 Gemeente document

82.20 Datum document

82.30 Beschrijving document

84.10 Indicatie onjuist/strijdigheid O Onjuist

85.10 Ingangsdatum geldigheid 28-08-2012

86.10 Datum van opneming 11-12-2012

Categorie 59 Kind

01.10 A-nummer Gevuld

01.20 Burgerservicenummer Gevuld

02.10 Voornamen Kim

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Erikson

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte

81.20 Aktenummer

82.10 Gemeente document 0637 Zoetermeer

82.20 Datum document 20-06-2010

82.30 Beschrijving document PL gerelateerde

84.10 Indicatie onjuist/strijdigheid

85.10 Ingangsdatum geldigheid 20-06-2010

86.10 Datum van opneming Systeemdatum

Categorie 59 Kind

01.10 A-nummer Gevuld

01.20 Burgerservicenummer Gevuld

02.10 Voornamen Kim

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Dubbeldam

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte

81.20 Aktenummer

82.10 Gemeente document 0637 Zoetermeer

82.20 Datum document 20-06-2010

82.30 Beschrijving document PL gerelateerde

84.10 Indicatie onjuist/strijdigheid O Onjuist

85.10 Ingangsdatum geldigheid 20-06-2010

86.10 Datum van opneming 20-06-2010

Categorie 59 Kind

01.10 A-nummer

01.20 Burgerservicenummer

02.10 Voornamen Kim

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Erikson

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte 0599

81.20 Aktenummer 10A1234

82.10 Gemeente document

82.20 Datum document

82.30 Beschrijving document

84.10 Indicatie onjuist/strijdigheid

85.10 Ingangsdatum geldigheid 15-04-2002

86.10 Datum van opneming Systeemdatum

Categorie 59 Kind

01.10 A-nummer

01.20 Burgerservicenummer

02.10 Voornamen Kim

02.20 Adellijke titel/predicaat

02.30 Voorvoegsel geslachtsnaam

02.40 Geslachtsnaam Dubbeldam

03.10 Geboortedatum 15-04-2002

03.20 Geboorteplaats 0599 Rotterdam

03.30 Geboorteland 6030 Nederland

81.10 Registergemeente akte 0599

81.20 Aktenummer 10A1234

82.10 Gemeente document

82.20 Datum document

82.30 Beschrijving document

84.10 Indicatie onjuist/strijdigheid O Onjuist

85.10 Ingangsdatum geldigheid 15-04-2002

86.10 Datum van opneming 18-04-2002

## Administratieve gegevens

Administratieve gegevens hebben betrekking op en geven achtergrondinformatie over algemene gegevens. Ze duiden bijvoorbeeld aan: aan welke brondocumenten de gegevens ontleend zijn, wanneer ze zijn ontleend, wanneer ze zijn opgenomen en of er een onderzoek naar de juistheid ervan is gedaan of gaande is. Andere administratieve gegevens zeggen iets over de inschrijving of over het niet verstrekken van gegevens.

Bij het corrigeren van administratieve gegevens ontstaat over het algemeen geen historie en de onjuiste gegevens kunnen overschreven of verwijderd worden. De uitzondering op dit uitgangspunt is, in het LO BRP in hoofdstuk 3 (Actualiseren) wordt, in voorkomende gevallen, bij de actualiseringsprocedure vermeld dat de wijziging niet tot historie leidt. Staat dit niet vermeldt bij een actualiseringsprocedure (zoals bijvoorbeeld bij actualiseringsprocedure 2.1.7.4 Wijziging in reden opnemen nationaliteit) dan moet wel historie aangemaakt worden. Uiteraard geldt dit niet voor categorieën die geen historie kennen: categorie 07 Inschrijving, categorie 12 Reisdocument en categorie 13 Kiesrecht.

## Verwijsgegevens

Een verwijzing is een van de persoonslijst afgeleide verzameling gegevens die verwijst naar een volgende gemeente van inschrijving. Bij het corrigeren van deze gegevens ontstaat historie, behalve bij de wijziging van groep 70 Geheim. Bij wijziging van de indicatie geheim verwijsgegevens ontstaat geen historie.

## Technische gegevens

Technische gegevens zijn uitsluitend in categorie 07, groep 80 Synchroniciteit, opgenomen en zijn bedoeld om de synchroniciteit tussen de persoonslijsten bij de gemeenten en die in de GBA-V te bewaken. Elke wijziging op de persoonslijst heeft een wijziging in groep 80 Synchroniciteit tot gevolg. Omdat het systeem van de gemeente dit automatisch doet, wordt dit niet gedaan door de medewerker BRP. Om deze reden maakt groep 80 Synchroniciteit geen deel uit van de procedures in deze handleiding.

## Gegeven bij de persoonslijst

Dit betreft de afnemersindicaties die in BRP-V bij de persoonslijst opgeslagen worden in categorie 14. Deze categorie komt wel voor bij een persoonslijst maar maakt daar geen deel van uit.

Scroll naar boven
