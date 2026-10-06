---
id: 2025-rvig-logisch-ontwerp-brp-2025q1
titel: Logisch Ontwerp BRP Versie 2025.Q1
uitgever: RvIG (Rijksdienst voor Identiteitsgegevens) / Ministerie van BZK
datum: '2025-01-01'
versie: ''
pad: sources/raw/2025-rvig-logisch-ontwerp-brp-2025q1.md
hash: 5f72a3c568b0b0eee8b93c8159cfc1bdb99cece39414963b99951afa7c4be185
tags:
- standaarden
brontype: informatiemodel
beschrijving: 'Formele systeemspecificatie van de Basisregistratie Personen: gegevenswoordenboek,
  categorieën, bijhouding, verstrekkingen en berichtenverkeer.'
url: https://www.rvig.nl/sites/default/files/2024-12/Logisch%20Ontwerp%20BRP%202025.Q1.pdf
url_pagina: https://www.rvig.nl/lo-brp
opgehaald: '2026-06-25'
---

# Logisch Ontwerp BRP Versie 2025.Q1

## Samenvatting
Het Logisch Ontwerp BRP (LO BRP) van RvIG, onderdeel van het ministerie van BZK, is de functionele en technische systeembeschrijving waar de Wet BRP, het Besluit BRP en de Regeling BRP naar verwijzen. Het beschrijft de bijhouding van de persoonslijst door gemeenten en de registratie niet-ingezetenen, de verstrekkingen vanuit BRP-V (autorisatietabel, spontane, selectie- en ad-hoc-verstrekking), het gegevenswoordenboek (categorieën, groepen, elementen, landelijke tabellen), het berichtenboek en de stelselcomponenten, met als bijlagen de dienstverleningsafspraken en de conversiegeschiedenis. De inhoud van de landelijke tabellen is niet opgenomen. Versie 2025.Q1, in werking per 1 januari 2025, vervangt 2024.Q3; er verschijnt in principe vier keer per jaar een nieuwe versie. Delen zonder grijze achtergrond in de bron vormen de systeembeschrijving; de rest is toelichting.

## Trefwoorden
LO BRP, Logisch Ontwerp, basisregistratie personen, bevolkingsregister, persoonslijst, PL, verwijzing, inschrijving, vervolginschrijving, verhuizing, adreswijziging, emigratie, immigratie, geboorte, overlijden, huwelijk, partnerschap, ouder, kind, nationaliteit, reisdocument, kiesrecht, verblijfstitel, gezag, A-nummer, burgerservicenummer, BSN, opschorting, blokkering, correctie, onderzoek, protocollering, niet-ingezetenen, RNI, afnemer, autorisatietabel, afnemersindicatie, spontane verstrekking, selectie, ad hoc verstrekking, BRP-V, TMV, terugmeldvoorziening, IKP, WALAA, adreskwaliteit, berichtendienst, gegevenswoordenboek, categorie, groep, element, rubriek, landelijke tabellen, BRP API, bewoning

## Begrippen
| Begrip | Regel | Soort |
|---|---|---|
| Afnemer | 377 | definitie |
| Reisdocument | 379 | definitie |
| Statuswijzigingen persoonslijst, PL-status | 521 | regeling |
| Opschorting bijhouding (groep 07.67) | 939 | regeling |
| Blokkering | 963 | regeling |
| Correcties | 969 | regeling |
| Vervolginschrijving | 631 | regeling |
| Wijziging van het A-nummer | 1055 | regeling |
| Wijziging van het burgerservicenummer | 1077 | regeling |
| Actualiseren verblijfplaats | 2107 | regeling |
| Onderzoekprocedure | 2867 | regeling |
| Protocolplicht | 3150 | regeling |
| Autorisatietabel | 3899 | regeling |
| BRP-Verstrekkingsvoorziening (BRP-V) | 4461 | regeling |
| Afnemersindicatie | 4481 | regeling |
| Spontane gegevensverstrekking | 4519 | regeling |
| Selectie | 4579 | regeling |
| Ad hoc gegevensverstrekking | 4615 | regeling |
| Persoonslijst | 4899 | definitie |
| Verwijzing | 4941 | regeling |
| Categorieën (opsomming 01/51 tot 17) | 5207 | regeling |
| Groepen | 5335 | regeling |
| Elementen | 5618 | regeling |
| Landelijke tabellen | 6130 | regeling |
| Bewoning op een adres (categorie AX) | 7468 | definitie |
| Terugmeldvoorziening (TMV) | 16519 | regeling |
| Informatieknooppunt (IKP) | 16682 | regeling |

## Verwijst naar
Wet BRP, Besluit BRP en Regeling BRP (regel 441; Wet BRP en Besluit BRP staan als `2026-rijk-wet-brp-bwbr0033715` en `2026-rijk-besluit-brp-bwbr0034306` in `sources/index/`). Wet GBA en Logisch Ontwerp GBA/RNI als voorgangers (regel 383-385). AVG (regel 397; `2016-eu-avg-geconsolideerd`). Artikel 3.14 Wet BRP (regel 377). Wet BRP-bepaling over privacy, inzage en correctie (regel 3136).

## Inhoud

Tekst: `sources/raw/2025-rvig-logisch-ontwerp-brp-2025q1.md`, 164690 woorden. Regel = regelnummer in die tekst.

| Kop | Regel | Woorden |
|---|---|---|
| **Inhoud** | 15 | 1045 |
| **Lijst met figuren** | 303 | 627 |
| **Lijst met tabellen** | 309 | 439 |
| **Overzicht wijzigingen** | 315 | 108 |
| **1 Algemene inleiding** | 343 | 0 |
| **1.1 Begrippen en definities** | 345 | 247 |
| **1.2 Het Logisch Ontwerp BRP** | 381 | 139 |
| **1.3 Plaatsbepaling Logisch Ontwerp BRP** | 389 | 115 |
| **1.4 Inhoud Logisch Ontwerp BRP** | 399 | 302 |
| **1.5 Beschrijving BRP** | 431 | 41 |
| **1.5.1 Wet- en regelgeving BRP** | 441 | 47 |
| **1.5.2 Stelselarchitectuur** | 447 | 1036 |
| **1.6 Statuswijzigingen van persoonslijsten in de Basisregistratie Personen** | 521 | 572 |
| **2 Bijhouding** | 579 | 0 |
| **2.1 Algemeen** | 581 | 635 |
| **2.1.2 Vervolginschrijving** | 631 | 656 |
| **2.1.3 Actualiseren** | 687 | 0 |
| **2.1.4 Actualiseren persoon** | 993 | 0 |
| **2.1.5 Actualiseren ouder1** | 1155 | 11 |
| **2.1.6 Actualiseren ouder2** | 1397 | 10 |
| **2.1.7 Actualiseren nationaliteit** | 1629 | 0 |
| 04.88 Deelnemer | 1731 | 0 |
| Tevens mag aanvullend de volgende groep worden opgenomen: | 1741 | 34 |
| **2.1.8 Actualiseren huwelijk/geregistreerd partnerschap** | 1785 | 10 |
| **2.1.9 Actualiseren overlijden** | 1925 | 0 |
| 06.88 Deelnemer | 1963 | 72 |
| **2.1.10 Actualiseren inschrijving** | 1975 | 0 |
| 07.67 Opschorting | 2063 | 18 |
| 07.68 Opname | 2071 | 0 |
| De volgende groep wordt gewijzigd: | 2085 | 0 |
| 07.70 Geheim | 2087 | 0 |
| 07.87 PK-conversie | 2093 | 0 |
| **2.1.11 Actualiseren verblijfplaats** | 2107 | 0 |
| **2.1.12 Actualiseren kind** | 2263 | 10 |
| **2.1.13 Actualiseren verblijfstitel** | 2471 | 0 |
| **2.1.14 Actualiseren gezagsverhouding** | 2515 | 10 |
| **2.1.15 Actualiseren reisdocument** | 2593 | 10 |
| ~~**2.1.15.6 Teruggave Nederlands reisdocument**~~ | 2647 | 38 |
| ~~**2.1.15.82**~~ **.1.15.7 Verwijderen van reisdocumentgegevens** | 2665 | 103 |
| ~~**2.1.15.92**~~ **.1.15.8 Correctie van ten onrechte opgenomen gegevens** | 2673 | 26 |
| **2.1.16 Actualiseren kiesrecht** | 2677 | 10 |
| **2.1.17 Actualiseren verwijzing** | 2737 | 0 |
| **2.1.18 Actualiseren akte en document** | 2823 | 0 |
| **2.1.19 Actualiseren ingangsdatum geldigheid** | 2849 | 78 |
| **2.1.20 Onderzoekprocedure en correcties** | 2867 | 0 |
| **2.1.21 Actualiseren bijzondere PL-situaties** | 2974 | 0 |
| **2.1.22 Actualiseren landelijke tabellen** | 3084 | 0 |
| **2.1.23 Privacyprocedures** | 3132 | 0 |
| _Herleidbare verstrekkingen_ | 3174 | 157 |
| _Niet-herleidbare verstrekkingen_ | 3182 | 356 |
| **2.1.24 Synchroniciteitsselectie** | 3364 | 167 |
| **2.2 Specifiek ingezetenen** | 3378 | 0 |
| **2.2.1 Eerste inschrijving** | 3380 | 0 |
| **2.2.2 Intergemeentelijke infrastructurele wijzigingen** | 3474 | 124 |
| **2.3 Specifiek niet-ingezetenen** | 3550 | 0 |
| **2.3.1 Eerste inschrijving** | 3552 | 0 |
| PL’en van nooit-ingezetenen | 3732 | 37 |
| PL’en van voormalig ingezetenen | 3736 | 28 |
| **2.3.2 Actualiseren van gegevens van niet-ingezetenen** | 3740 | 0 |
| PL van een nooit-ingezetene | 3746 | 11 |
| PL van een voormalig ingezetene | 3750 | 69 |
| **3 Verstrekkingen** | 3897 | 0 |
| **3.1 De autorisatietabel** | 3899 | 0 |
| **Verstrekkingsbeperking** (Rubriek 35.95.13) | 3935 | 229 |
| **Afnemersverstrekkingen ad hoc** (Rubriek 35.95.63) | 4015 | 26 |
| **Adresvraagbevoegdheid** (Rubriek 35.95.66) | 4019 | 274 |
| • | 4307 | 0 |
| **3.2 Afnemerssystemen** | 4395 | 0 |
| **3.3 BRP-Verstrekkingsvoorziening** | 4461 | 0 |
| **3.3.1 Inleiding** | 4463 | 7 |
| **3.3.2 Doelstelling van BRP-V** | 4467 | 75 |
| **3.3.3 Plaats van BRP-V in het BRP-stelsel** | 4471 | 0 |
| _BRP-V als ontvanger van gegevens_ | 4473 | 78 |
| _BRP-V als verstrekker van gegevens_ | 4477 | 25 |
| **3.3.4 Plaatsen en verwijderen van afnemersindicaties** | 4481 | 109 |
| 14.40 Afnemer | 4501 | 0 |
| 14.85 Geldigheid | 4503 | 0 |
| 14.85 Geldigheid | 4509 | 0 |
| **3.3.5 Spontane gegevensverstrekking** | 4519 | 183 |
| **3.3.6 Selectie** | 4579 | 17 |
| **3.3.7 Ad hoc gegevensverstrekking** | 4615 | 20 |
| **3.3.8 Verstrekking op basis van plaatsing van een afnemersindicatie** | 4721 | 230 |
| **3.3.9 (Mee)verstrekking van de groepen procedure en onjuist** | 4739 | 185 |
| **3.3.10 Meeverstrekken van verificatie en RNI-deelnemergegevens** | 4811 | 125 |
| **3.3.11 Niet verstrekken van gegevens van levenloos geboren kinderen** | 4855 | 135 |
| **3.3.12 Protocollering** | 4861 | 255 |
| **4 Gegevenswoordenboek** | 4873 | 0 |
| **4.1 Inleiding** | 4875 | 139 |
| **4.2 De BRP-gegevens** | 4883 | 44 |
| **4.2.1 De persoonslijst** | 4899 | 307 |
| **4.2.2 De verwijzing** | 4941 | 94 |
| **4.2.3 De afnemersindicatie** | 4955 | 76 |
| **4.2.4 De landelijke tabellen** | 4965 | 130 |
| **4.2.5 Afgeleide gegevens** | 4977 | 524 |
| **4.2.6 Aanduiding van de gegevens** | 4997 | 307 |
| **4.2.7 Soorten gegevens** | 5021 | 187 |
| **4.2.8 Het coderen dan wel omvormen van een gegeven** | 5053 | 83 |
| Vervolgens geldt: | 5075 | 153 |
| **4.3 Toelichting op gebruikte begrippen** | 5141 | 80 |
| **4.4 Beschrijving van de categorieën** | 5207 | 0 |
| **4.5 Beschrijving van de groepen** | 5335 | 2483 |
| **4.6 Beschrijving van de elementen** | 5618 | 5746 |
| Voorwaarden | 6076 | 1322 |
| **4.7 Beschrijving van de landelijke tabellen** | 6130 | 218 |
| Autorisatietabel | 6245 | 980 |
| **4.8 Beschrijving persoonslijst en verwijzing als ingezetene of overleden ingezetene** | 6442 | 0 |
| Elem.nr. Soort Rubrieknaam | 6538 | 89 |
| Elem.nr. Soort Rubrieknaam | 6563 | 162 |
| Elem.nr. Soort Rubrieknaam | 6629 | 49 |
| Elem.nr. Soort Rubrieknaam | 6639 | 100 |
| Elem.nr. Soort Rubrieknaam | 6679 | 114 |
| Elem.nr. Soort Rubrieknaam | 6716 | 72 |
| Elem.nr. Soort Rubrieknaam | 6739 | 97 |
| Elem.nr. Soort Rubrieknaam | 6765 | 63 |
| Elem.nr. Soort Rubrieknaam | 6792 | 79 |
| **4.9 Beschrijving persoonslijst en verwijzing van voormalig ingezetene** | 6817 | 0 |
| Elem.nr. Soort Rubrieknaam | 6914 | 92 |
| Elem.nr. Soort Rubrieknaam | 6941 | 162 |
| Elem.nr. Soort Rubrieknaam | 7009 | 36 |
| Elem.nr. Soort Rubrieknaam | 7030 | 103 |
| Elem.nr. Soort Rubrieknaam | 7072 | 114 |
| Elem.nr. Soort Rubrieknaam | 7109 | 72 |
| Elem.nr. Soort Rubrieknaam | 7132 | 97 |
| Elem.nr. Soort Rubrieknaam | 7158 | 63 |
| Elem.nr. Soort Rubrieknaam | 7185 | 74 |
| Elem.nr. Soort Rubrieknaam | 7218 | 27 |
| Elem.nr. Soort Rubrieknaam | 7224 | 79 |
| **4.10 Beschrijving persoonslijst en verwijzing nooit-ingezetene** | 7249 | 0 |
| Elem.nr. Soort Rubrieknaam | 7285 | 92 |
| Elem.nr. Soort Rubrieknaam | 7337 | 27 |
| Elem.nr. Soort Rubrieknaam | 7356 | 73 |
| Elem.nr. Soort Rubrieknaam | 7398 | 74 |
| Elem.nr. Soort Rubrieknaam | 7431 | 27 |
| Elem.nr. Soort Rubrieknaam | 7437 | 79 |
| **4.11 Beschrijving van de afgeleide gegevens** | 7462 | 0 |
| **5 Berichtenboek** | 8135 | 0 |
| **5.1 Berichten algemeen** | 8137 | 0 |
| 1. _**Zoeken op**_ ~~_**het eerste deel**_~~ _**een gedeelte van de rubriekwaarde**_ | 8764 | 87 |
| _Voor datums geldt:_ | 8768 | 72 |
| _Voor alle overige rubrieken geldt:_ | 8776 | 67 |
| 2. _**Zoeken zonder onderscheid tussen hoofdletters en kleine letters (case insenstive)**_ | 8780 | 18 |
| 3. _**Zoeken zonder diakritische tekens**_ | 8784 | 259 |
| **Datum beëindiging tabelregel** (8 posities, numeriek) | 9101 | 560 |
| • **BL** (Berichtlengte) | 9239 | 0 |
| 5 tekens | 9241 | 554 |
| **5.2 Berichten in verband met de bijhouding** | 9483 | 0 |
| 1. **Geboortegemeente** | 9984 | 316 |
| 4. **Gemeente eerste inschrijving** | 10000 | 317 |
| 1. **Huidige gemeente van inschrijving** | 10368 | 28 |
| 2. **Gemeente met verwijsgegevens** | 10372 | 568 |
| 3. **Minister van Justitie** | 10452 | 411 |
| **5.3 Berichten in verband met verstrekkingen** | 11932 | 0 |
| 1. **BRP-V** | 12010 | 419 |
| 1. **BRP-V** | 12060 | 37 |
| 1. **Afnemer** | 12092 | 371 |
| 1. **Afnemer** | 12284 | 18 |
| 2. **BRP-V** | 12288 | 329 |
| 1. **Afnemer** | 12360 | 150 |
| URI: {basis_url}/bewoningen | 12906 | 0 |
| Method: POST | 12908 | 15 |
| **5.4 Overige berichten** | 14100 | 0 |
| 1. **RvIG** | 14214 | 25 |
| 2. **Gemeente, RNI, BRP-V, BvBSN en afnemer** | 14222 | 122 |
| **5.5 Alternatieve media** | 14418 | 0 |
| **Inhoudelijke aspecten CSV-bestand** | 14654 | 121 |
| _Koprecord:_ | 14668 | 1 |
| _Gegevensrecord persoon 1_ | 14672 | 69 |
| _Gegevensrecord persoon 2_ | 14688 | 87 |
| **6 Stelselcomponenten** | 14706 | 0 |
| **6.1 Inleiding** | 14708 | 28 |
| **6.2 Berichtendienst (Turbo)sPd-interface** | 14712 | 0 |
| 5000 (𝑑𝑒 𝑚𝑎𝑥𝑖𝑚𝑎𝑙𝑒 𝑙𝑒𝑛𝑔𝑡𝑒)−(13+17+5)(𝑑𝑒 𝑣𝑎𝑠𝑡𝑒 ℎ𝑒𝑎𝑑𝑒𝑟) | 14985 | 134 |
| 1072 S **Mailbox is leeg** (No entries). | 16176 | 39 |
| **6.3 Terugmeldvoorziening (TMV)** | 16519 | 0 |
| **6.4 BRP Verstrekkingsvoorziening** | 16529 | 0 |
| BRP-V bevat geen verwijsgegevens. | 16573 | 199 |
| **6.5 Informatieknooppunt (IKP)** | 16682 | 0 |
| **6.6 Web Applicatie Landelijke Aanpak Adreskwaliteit (WALAA)** | 16702 | 0 |
| ~~**6.7 Gezagsmodule**~~ | 16708 | 95 |
| A Beheereisen en dienstverleningsafspraken | 16712 | 0 |
| **A.1 Inleiding** | 16714 | 86 |
| **A.2 Autorisatie en toegang** | 16726 | 0 |
| **A.3 Kwaliteit van de dienstverlening** | 16782 | 0 |
| _Prioriteit hoog:_ | 16927 | 20 |
| _Prioriteit overig:_ | 16931 | 42 |
| **A.4 Continuïteit, betrouwbaarheid en beheer** | 16998 | 67 |
| **A.5 Statistiek, gebruiksgegevens en protocollering** | 17066 | 0 |
| **A.6 Beheer** | 17078 | 0 |
| _Voldoen aan het gebruikersprofiel_ | 17094 | 340 |
| **A.7 Beheereisen Berichtendienst** | 17301 | 0 |
| B Conversies | 17393 | 0 |
| **B.1 Inleiding** | 17395 | 185 |
| **B.2 Historisch overzicht** | 17399 | 421 |
| ~~1 januari 2024: Vaste koppeling BAG-BRP (LO BRP 2024.Q1)~~ | 17453 | 552 |
| **B.3 Conversie PK-gegevens (tot 1-10-1994)** | 17517 | 0 |
| 01/02/03/05/09.02.10 Voornamen | 17655 | 258 |
| 01/02/03/05/09.02.30 Voorvoegsel geslachtsnaam | 17683 | 117 |
| 01/02/03/05/09.02.40 Geslachtsnaam | 17697 | 122 |
| 01/02/03/05/09.03.10 Geboortedatum | 17705 | 107 |
| 01/02/03/05/09.03.20 Geboorteplaats | 17713 | 107 |
| 01/02/03/05/09.03.30 Geboorteland | 17727 | 107 |
| 01.04.10 Geslachtsaanduiding | 17741 | 64 |
| 01.61.10 Aanduiding naamgebruik | 17745 | 37 |
| 01/02/03/05/09.81.10 Registergemeente akte | 17749 | 48 |
| 01/02/03/05/09.81.20 Aktenummer | 17753 | 48 |
| 01/02/03/04/05/09/11/12/13.82.10 Gemeente document | 17757 | 71 |
| 01/02/03/04/05/09/11/12/13.82.20 Datum document | 17769 | 41 |
| 01/02/03/04/05/09/11/12/13.82.30 Beschrijving document | 17775 | 183 |
| 01/02/03/04/05/08/09/10/11/12.85.10 Ingangsdatum geldigheid | 17793 | 202 |
| 04.05.10 Nationaliteit | 17809 | 31 |
| 04.63.10 Reden verkrijging Nederlandse nationaliteit | 17813 | 32 |
| 04.64.10 Reden verlies Nederlandse nationaliteit | 17817 | 24 |
| 04.65.10 Aanduiding bijzonder Nederlanderschap | 17821 | 45 |
| 05.06.10 Datum huwelijkssluiting | 17825 | 18 |
| 05.06.20 Plaats huwelijkssluiting | 17829 | 18 |
| 05.06.30 Land huwelijkssluiting | 17833 | 18 |
| 05.07.10 Datum huwelijksontbinding | 17837 | 18 |
| 05.07.20 Plaats huwelijksontbinding | 17841 | 18 |
| 05.07.30 Land huwelijksontbinding | 17845 | 18 |
| 05.07.40 Reden huwelijksontbinding | 17849 | 18 |
| 06.08.10/20/30 Datum/Plaats/Land overlijden | 17853 | 8 |
| 07.66.20 Datum ingang blokkering PL | 17857 | 5 |
| 07.67.10/20 Datum/Omschrijving reden opschorting bijhouding | 17861 | 5 |
| 07.68.10 Datum eerste inschrijving GBA | 17865 | 13 |
| 07.69.10 Gemeente waar de PK zich bevindt | 17869 | 50 |
| 07.70.10 Indicatie geheim | 17873 | 17 |
| 07.87.10 PK-gegevens volledig meegeconverteerd | 17879 | 35 |
| 08.09.10 Gemeente van inschrijving | 17883 | 32 |
| 08.09.20 Datum inschrijving | 17889 | 61 |
| 08.10.10 Functie adres | 17895 | 25 |
| 08.10.20 Gemeentedeel | 17899 | 17 |
| 08.10.30 Datum aangifte adreshouding | 17903 | 20 |
| 08.11.10 Straatnaam | 17907 | 24 |
| 08.11.20 Huisnummer | 17911 | 43 |
| 08.11.30 Huisletter | 17917 | 25 |
| 08.11.40 Huisnummertoevoeging | 17921 | 25 |
| 08.11.50 Aanduiding bij huisnummer | 17927 | 27 |
| 08.11.60 Postcode | 17933 | 29 |
| 08.12.10 Locatiebeschrijving | 17939 | 35 |
| 08.13.10/20 Land waarnaar vertrokken/Datum vertrek uit Nederland | 17945 | 8 |
| 08.14.10 Land vanwaar ingeschreven | 17949 | 53 |
| 08.14.20 Datum vestiging in Nederland | 17953 | 49 |
| 08.72.10 Omschrijving van de aangifte adreshouding | 17957 | 12 |
| 08.75.10 Indicatie document | 17961 | 5 |
| 10.39.10/20 Aanduiding/Datum einde verblijfstitel | 17965 | 5 |
| 11.32.10 Indicatie gezag minderjarige | 17969 | 22 |
| 11.33.10 Indicatie curateleregister | 17973 | 16 |
| 12.35.10 Soort Nederlands reisdocument | 17977 | 22 |
| Mogelijke aantekeningen: | 17981 | 47 |
| 12.35.20 Nummer Nederlands reisdocument | 17991 | 22 |
| 12.35.30 Datum uitgifte Nederlands reisdocument | 17995 | 31 |
| 12.35.40 Autoriteit van afgifte Nederlands reisdocument | 17999 | 31 |
| 12.35.50 Datum einde geldigheid Nederlands reisdocument | 18003 | 129 |
| 13.38.10 Aanduiding uitgesloten kiesrecht | 18013 | 30 |
| 13.38.20 Einddatum uitsluiting kiesrecht | 18017 | 34 |
| 14.40.10 Afnemersindicatie | 18021 | 13 |
| **B.4 Initiële vulling sofinummer (1-7-1995)** | 18027 | 0 |
| **B.5 Toevoegen geregistreerd partnerschap (1-1-1998)** | 18174 | 199 |
| **B.6 Wijzigingen burgerlijke stand en ingangsdatum verblijfstitel (1-2-2001)** | 18206 | 243 |
| 11.32.10 Indicatie gezag minderjarige | 18232 | 169 |
| 10.39.30 Ingangsdatum Verblijfstitel | 18248 | 72 |
| **B.7 Batchprocedure vulling burgerservicenummer (26-11-2007)** | 18252 | 0 |
| **B.8 Wijzigingen vanwege Modernisering GBA (26-11-2007)** | 18485 | 16 |
| 07.70.10 Indicatie geheim, | 18495 | 11 |
| 07.80.10 Versienummer | 18499 | 19 |
| 07.80.20 Datumtijdstempel | 18503 | 19 |
| **B.9 Wijzigingen in verband met de BAG (1-11-2009)** | 18507 | 0 |
| 08.11.10 Straatnaam | 18509 | 21 |
| 08.11.15 Naam openbare ruimte | 18513 | 21 |
| 08.11.20 Huisnummer | 18517 | 21 |
| 08.11.30 Huisletter | 18521 | 21 |
| 08.11.40 Huisnummertoevoeging | 18525 | 21 |
| 08.11.60 Postcode | 18529 | 21 |
| 08.11.70 Woonplaatsnaam | 18533 | 21 |
| 08.11.80 Identificatiecode verblijfplaats | 18537 | 296 |
| 08.11.90 Identificatiecode nummeraanduiding | 18551 | 21 |
| **B.10 Wijzigingen in verband met de RNI (6-1-2014)** | 18555 | 67 |
| **B.11 Conversieprocedure nationaliteitsgegevens (31-1-2015)** | 18577 | 0 |
| **B.12 Conversieprocedure reisdocumenten (31-1-2015)** | 18765 | 0 |
| **B.13 Conversieprocedure buitenlands persoonsnummer (8-10-2016)** | 18806 | 0 |
| **B.14 Inkorting straatnaam volgens de NEN-norm (8-10-2016)** | 18862 | 0 |
| 08.11.10 Straatnaam | 18864 | 166 |
| **B.15 Registratie levenloos geboren kinderen (1-2-2019)** | 18870 | 12 |
| **B.16 Gezagsverhouding vullen vanuit een tabel (4-10-2020)** | 18878 | 33 |
| **B.17 Toevoegen bereikbaarheidsgegevens arbeidsmigranten (22-10-2022)** | 18906 | 64 |
| **B.18 Toevoegen kiesrechtgegevens (01-07-2023)** | 18940 | 22 |
| **B.19 Vaste koppeling BAG-BRP (01-01-2024)** | 18950 | 392 |
| **B.20 Toevoegen informatierubrieken BRP API (22-04-2024)** | 18978 | 156 |
| **B.21 Toevoegen informatiecategorie BRP API (01-07-2024)** | 19046 | 22 |
| **B.22 Toevoegen informatierubrieken BRP API (01-01-2025)** | 19056 | 16 |
