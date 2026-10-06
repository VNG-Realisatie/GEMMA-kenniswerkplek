Wijzigen Administratienummer | RvIG

Overslaan en naar de inhoud gaan

Rijksdienst voor Identiteitsgegevens
Ministerie van Binnenlandse Zaken en Koninkrijksrelaties

Zoeken

Zoeken...

Zoeken

Handleiding Uitvoeringsprocedures HUP

#
Wijzigen Administratienummer

Het kan voorkomen dat een Administratienummer (A-nummer) moet worden gewijzigd, bijvoorbeeld omdat verschillende personen hetzelfde A-nummer hebben. Je moet onderzoek doen naar de oorzaak hiervan. Als er meerdere gemeenten bij betrokken zijn, overleg je met deze gemeente(n). In geval van een dubbelinschrijving (een persoon met meerdere persoonslijsten, zie procedure Dubbelinschrijving) voer je geen A-nummerwijziging uit.

Als verschillende personen hetzelfde A-nummer hebben, ken je aan alle betrokken personen een nieuw A-nummer toe. Dit geldt ook voor opgeschorte persoonslijsten. Je voert de onderstaande procedure uit. Naar aanleiding van deze wijziging worden Wa01-berichten naar de eventuele vorige bijhoudingsgemeenten, de geboortegemeente en de RNI gestuurd en wordt een Lg01-bericht naar de BRP-V gestuurd. De BRP-V meldt de wijziging van het A-nummer door middel van Wa11-berichten aan de relevante afnemers. Als een gerelateerde in een andere gemeente is ingeschreven, dan stuur je een kennisgeving van de A-nummerwijziging naar die gemeente.

Bij een vestiging vanuit het Caribisch deel van het Koninkrijk moet het A-nummer bij een eerste inschrijving worden overgenomen van de PIVA-PL, zie voor meer informatie Eerste inschrijving vanuit het Caribisch deel van Nederland. Bij een hervestiging vraag je de persoonslijst op uit de RNI. Dit A-nummer wijzig je niet. Het A-nummer uit de BRP is leidend.

Deze procedure wordt d.m.v. een actualisering uitgevoerd, nooit als correctieprocedure. Je wijzigt het A-nummer in de actuele categorie 01 Persoon van alle betrokken persoonslijsten. Het oude A-nummer neem je op in het element 20.10 Vorig A-nummer. Door deze actualisering ontstaat historie. Je neemt een nieuwe actuele categorie op. Hieronder volgen een aantal voorbeelden.

### Akte of document

Als documentomschrijving vul je de tekst “dubbel A-nummer” in.

### Ingangsdatum geldigheid

Hier vul je de datum in waarop het nieuwe A-nummer is toegekend, dit zal in de regel de systeemdatum zijn.

### Gevolgen voor andere persoonslijsten

Persoonslijsten van gerelateerden (ouders, kinderen en (vroegere) echtgenoten of geregistreerde partners) worden ook geactualiseerd.

Het A-nummer wordt in de betreffende categorie 02 Ouder1, 03 Ouder2, 05 Huwelijk/geregistreerd partnerschap of 09 Kind van alle gerelateerden gewijzigd. Door deze actualisering ontstaat historie. Je neemt een nieuwe actuele categorie op met als ingangsdatum geldigheid de datum waarop het nieuwe A-nummer is toegekend. Als omschrijving van het brondocument vul je de tekst “dubbel A-nummer” in. Actualiseer je de gerelateerdencategorie aan de hand van een Wa01-bericht, dan vul je hier de tekst “dubbel A-nummer, melding gemeente <gemeentecode>”. De gemeentecode ontleen je aan tabel 33 Gemeententabel.

Deze procedure wordt nooit als correctieprocedure uitgevoerd.

### Verwijsgegevens

Bij het wijzigen van een A-nummer stel je, indien van toepassing, de voorgaande woongemeente(n), de huidige bijhoudingsgemeente en de geboortegemeente op de hoogte. Deze gemeenten hebben gegevens (de persoonslijst of verwijsgegevens) van deze persoon en worden door een Wa-01 bericht op de hoogte gebracht van de A-nummer wijziging. Op grond van een Wa01-bericht actualiseert de vorige bijhoudingsgemeente, de geboortegemeente of de RNI het A-nummer in de verwijsgegevens van de betreffende persoon. Let daarbij op het volgende:

- Gebruik de historische categorieën 58 Verblijfplaats om te bepalen naar welke gemeenten een Wa01-bericht moet worden verstuurd.

- Als de huidige bijhoudingsgemeente tot de bedoelde gemeenten behoort, dan stuur je uiteraard geen Wa01-bericht.

- Komt een bepaalde bijhoudingsgemeente meerdere keren voor in de categorieën 58, dan stuur je slechts één bericht.

- Is een of meer van de hier bedoelde vroegere gemeenten betrokken geweest bij een herindeling en is die gemeente daarbij opgeheven, dan geldt het volgende. Als de opgeheven gemeente nu deel uitmaakt van de eigen gemeente, dan stuur je geen Wa01-bericht. Als de opgeheven gemeente nu deel uitmaakt van een andere gemeente, dan stuur je het Wa01-bericht naar die andere gemeente. Raadpleeg tabel 33 Gemeententabel om vast te stellen of een gemeente is opgeheven en zo ja, tot welke gemeente die opgeheven gemeente nu behoort.

- Je stuurt het Wa01-bericht ook naar de eventuele toevallige geboortegemeente met inachtneming van wat bij het vorige punt is vermeld.

- Staat de RNI vermeld in de historische categorieën 58, dan stuur je ook een Wa01-bericht naar de RNI.

- Het Wa01-bericht is ook aanleiding om de persoonslijsten van gerelateerden (ouders, kinderen en (vroegere) echtgenoten of geregistreerde partners) in categorie 02 Ouder1, 03 Ouder2, 05 Huwelijk/geregistreerd partnerschap of 09 Kind te wijzigen.

Door deze actualisering ontstaat historie. Je neemt een nieuwe actuele categorie op.

Wijzigen administratienummer

V18.1.1a

Categorie 01 Persoon

01.10
A-nummer
Nieuw toegekend A-nummer

01.20
Burgerservicenummer
Gevuld (ongewijzigd)

02.10
Voornamen
Sifan

02.20
Adellijke titel/predicaat

02.30
Voorvoegsel geslachtsnaam

02.40
Geslachtsnaam
Isik

03.10
Geboortedatum
20-04-1998

03.20
Geboorteplaats
0114 Emmen

03.30
Geboorteland
6030 Nederland

04.10
Geslachtsaanduiding
V

20.10
Vorig A-nummer
Vorig toegekend A-nummer

20.20
Volgend A-nummer

61.10
Aanduiding naamgebruik
E

82.10
Gemeente document
Eigen gemeente

82.20
Datum document
Systeemdatum

82.30
Beschrijving document
dubbel A-nummer

85.10
Ingangsdatum geldigheid
Systeemdatum

86.10
Datum van opneming
Systeemdatum

Categorie 51 Persoon

01.10
A-nummer
Gevuld

01.20
Burgerservicenummer
Gevuld

02.10
Voornamen
Sifan

02.20
Adellijke titel/predicaat

02.30
Voorvoegsel geslachtsnaam

02.40
Geslachtsnaam
Isik

03.10
Geboortedatum
20-04-1998

03.20
Geboorteplaats
0114 Emmen

03.30
Geboorteland
6030 Nederland

04.10
Geslachtsaanduiding
V

20.10
Vorig A-nummer

20.20
Volgend A-nummer

61.10
Aanduiding naamgebruik
E

81.10
Registergemeente akte
0144 Emmen

81.20
Aktenummer
10A0114

84.10
Indicatie onjuist/strijdigheid

85.10
Ingangsdatum geldigheid
20-04-1998

86.10
Datum van opneming
21-04-1998

Wijzigen administratienummer in verwijsgegevens

V18.1.1b

Categorie 21 Verwijzing

01.10
A-nummer uitgeschreven persoon
Nieuw toegekend A-nummer

01.20
Burgerservicenummer uitgeschreven persoon
Gevuld (ongewijzigd)

02.10
Voornamen uitgeschreven persoon
Elisa Maria

02.20
Adellijke titel/predicaat uitgeschreven persoon

02.30
Voorvoegsel geslachtsnaam uitgeschreven persoon
van

02.40
Geslachtsnaam uitgeschreven persoon
Boot

03.10
Geboortedatum uitgeschreven persoon
22-05-1980

03.20
Geboorteplaats uitgeschreven persoon
0856 Uden

09.10
Gemeente waarheen uitgeschreven of toevallige geboorte
0917 Heerlen

09.20
Datum uitschrijving
18-08-2024

70.10
Indicatie geheim verwijsgegevens
0

85.10
Ingangsdatum geldigheid
Systeemdatum

86.10
Datum van opneming
Systeemdatum

Categorie 71 Verwijzing

01.10
A-nummer uitgeschreven persoon
Gevuld

01.20
Burgerservicenummer uitgeschreven persoon
Gevuld

02.10
Voornamen uitgeschreven persoon
Gevuld (ongewijzigd)

02.20
Adellijke titel/predicaat uitgeschreven persoon
Elisa Maria

02.30
Voorvoegsel geslachtsnaam uitgeschreven persoon

02.40
Geslachtsnaam uitgeschreven persoon
van

03.10
Geboortedatum uitgeschreven persoon
Boot

03.20
Geboorteplaats uitgeschreven persoon
22-05-1980

09.10
Gemeente waarheen uitgeschreven of toevallige geboorte
0856 Uden

09.20
Datum uitschrijving
0917 Heerlen

70.10
Indicatie geheim verwijsgegevens
0

84.10
Indicatie onjuist

85.10
Ingangsdatum geldigheid
18-08-2024

86.10
Datum van opneming
18-08-2024

Wijzigen administratienummer bij gerelateerden

V18.1.1c

Categorie 09 Kind

01.10
A-nummer
Nieuw toegekend A-nummer

01.20
Burgerservicenummer
Gevuld (ongewijzigd)

02.10
Voornamen
Femke

02.20
Adellijke titel/predicaat

02.30
Voorvoegsel geslachtsnaam

02.40
Geslachtsnaam
Smit

03.10
Geboortedatum
26-02-2002

03.20
Geboorteplaats
0546 Leiden

03.30
Geboorteland
6030 Nederland

81.10
Registergemeente akte

81.20
Aktenummer

82.10
Gemeente document
Eigen gemeente

82.20
Datum document
Systeemdatum

82.30
Beschrijving document
dubbel A-nummer, melding gemeente 0622

85.10
Ingangsdatum geldigheid
Datum toekenning A-nummer

86.10
Datum van opneming
Systeemdatum

89.10
Registratie betrekking

Categorie 59 Kind

01.10
A-nummer
Gevuld

01.20
Burgerservicenummer
Gevuld

02.10
Voornamen
Femke

02.20
Adellijke titel/predicaat

02.30
Voorvoegsel geslachtsnaam

02.40
Geslachtsnaam
Smit

03.10
Geboortedatum
26-02-2002

03.20
Geboorteplaats
0546 Leiden

03.30
Geboorteland
6030 Nederland

81.10
Registergemeente akte
0546 Leiden

81.20
Aktenummer
10B0237

84.10
Indicatie onjuist/strijdigheid

85.10
Ingangsdatum geldigheid
26-02-2002

86.10
Datum van opneming
26-02-2002

89.10
Registratie betrekking

Scroll naar boven
