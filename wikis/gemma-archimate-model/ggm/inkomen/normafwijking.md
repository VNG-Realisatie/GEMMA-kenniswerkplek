<!-- gegenereerd door tools/ggm.py; hash: a4cd5a185fa09bc7b5a96e96e21bb47acd006b1ed09a13c3731d051bb2bd224d -->
# Normafwijking

Taakveld: Inkomen. Alleen objecttypen; letterlijke definities uit het GGM.

## Afwijkende maatregel

Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast.

Attributen: Bedrag, Code reden afwijking maatregel, Motivatie afwijking maatregel, Percentage.

GUID: `EAID_1BD0DD3A_888E_945B_4A20_276CADAE4D4C`

Relaties:

- refereert → Maatregel op uitkering (*Aggregation (shared)*, 1..1 → 1..1, `EAID_15977151_EC46_89CA_680B_276CADDFD8E5`)
- Maatregel generaliseert Afwijkende maatregel → Maatregel (*Generalization*,  → , `EAID_161E166F_377B_77CF_BF11_276CAE45C097`)

## Boete

Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen.

Attributen: Bedrag boete, Boetevorm, Reden boete, Voorwaarde boete.

GUID: `EAID_05E49616_803F_4C1B_9663_262C4A191DF9`

Relaties:

- Maatregel generaliseert Boete → Maatregel (*Generalization*,  → , `EAID_02D32D3B_1AFE_54E9_20D4_2632D33E000F`)

## Maatregel

Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven.

Attributen: Datum aanvang maatregel, Datum einde maatregel, Datum vaststelling maatregel, identificatie, Type maatregel.

GUID: `EAID_0B63B508_9F69_A5D7_4387_2632D2C24782`

## Maatregel op uitkering

Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen.

Attributen: Code reden maatregel, Motivatie vermindering maatregel, Percentage maatregel.

GUID: `EAID_032C6459_3922_4AEF_0D73_262C4A138E25`

Relaties:

- Maatregel generaliseert Maatregel op uitkering → Maatregel (*Generalization*,  → , `EAID_07EDB42A_2F9E_9557_14A9_2632D2E7753D`)

## Normafwijking

Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering.

Attributen: Datum vaststelling normafwijking, Datum vaststelling verwijtbaarheid, identificatie, Motivatie verwijtbaarheid, Recidive, Type normafwijking, Verwijtbaarheid.

GUID: `EAID_167FF4C9_6B66_EEDA_5189_262C4A139258`

Relaties:

- Normafwijking leidt tot Maatregel → Maatregel (*Aggregation (shared)*, 0..1 → 1..1, `EAID_03151107_A266_68F8_F5DE_2632D35E1D57`)
