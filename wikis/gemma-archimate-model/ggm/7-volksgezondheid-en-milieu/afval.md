<!-- gegenereerd door tools/ggm.py; hash: 4b1898aca004af787ff2c7426e947790c349d357c73b25f4eb7ab503bfd746af -->
# Afval

Taakveld: 7 Volksgezondheid en Milieu. Alleen objecttypen; letterlijke definities uit het GGM.

## Categorie

Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren

Attributen: code, naam, omschrijving.

GUID: `EAID_9EC6B40B_0C87_4453_B567_E0D3572F86AF`

## Container

Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen

Attributen: sensorID, containercode.

GUID: `EAID_7D3D98F0_664C_4605_9D95_F68C88ECBA9A`

Relaties:

- soort → Containertype (*Association*, 0..* → 0..1, `EAID_A3FEE3DD_1148_4a7e_A133_1DAA02D2F1EA`)
- geschikt voor → Fractie (*Association*, 0..* → 1, `EAID_36405EF9_1834_4820_AC14_E948C8E501CA`)
- heeft → Locatie (*Association*, 0..* → 1, `EAID_B6A165E1_F6F2_447a_83F3_8786CC50D691`)
- heeft → Vulgraadmeting (*Association*, 1 → 0..*, `EAID_B9EFC41B_C77E_43e5_80BE_886D1F7FF6A7`)

## Containertype

Typologie van container

Attributen: naam, omschrijving.

GUID: `EAID_0A7769C7_FE3E_45eb_A644_22E5CB207B42`

## Fractie

Onderdeel, deeltje

Attributen: naam, omschrijving.

GUID: `EAID_80A7D18F_7C7E_4ee6_9F07_055559BCEF9F`

## Locatie

Locaties die worden aangedaan tijdens het rijden van een route. Dit kunnen adressen zijn en/of GML-punten met een x- en y-coordinaat. Avalex hanteert op het moment van schrijven alleen adressen, ook voor de containers.

Attributen: locatiePunt, locatiecode, adresaanduiding.

GUID: `EAID_7F4E17A3_0EC2_4bee_B4E0_BFA26D653EB9`

## Melding

De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend

Attributen: illegaal, 24uurs, datumtijd, omschrijving, meldingnummer.

GUID: `EAID_8A02DCF5_E568_4d45_96A2_FD4FB53F414C`

Relaties:

- hoofdcategorie → Categorie (*Association*, 0..* → 1, `EAID_72EEDB98_89E2_489f_853E_374200CC5BD7`)
- subcategorie → Categorie (*Association*, 0..* → 1, `EAID_BE8CFC8D_1A0C_4356_8D5A_24D839958662`)
- betreft → Containertype (*Association*, 0..* → 0..1, `EAID_FFAAF721_5ED0_4e5b_B5F7_D041D8517D00`)
- betreft → Fractie (*Association*, 0..* → 0..1, `EAID_0C4C7705_5F76_417a_B326_E721AFB72ADB`)
- betreft → Locatie (*Association*, 0..* → 1, `EAID_7F1E6990_018A_436c_9813_1F75AB62D3C7`)
- → AanvraagOfMelding (*Generalization*,  → , `EAID_C07BC087_AB8A_46f4_81C6_255300BCD9DF`)

## Milieustraat

Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil.

Attributen: naam, omschrijving, adresaanduiding.

GUID: `EAID_1638F2AF_F1E8_4360_BA47_D975F2135168`

Relaties:

- inzamelpunt van → Fractie (*Association*, 0..* → 0..*, `EAID_8F27C588_2ED1_4d02_85C1_E3560A0C898D`)

## Ophaalmoment

Een stop die een vuilniswagen maakt tijdens het doen van een rit. Bijgehouden wordt de gewichtstoename van de lading

Attributen: gewichtstoename, tijdstip.

GUID: `EAID_9079F098_1084_4484_ACCC_6C6C07043193`

Relaties:

- gelost → Container (*Association*, 0..* → 0..1, `EAID_99AE0490_31AD_4cde_9104_15B00595495C`)
- gestopt op → Locatie (*Association*, 0..* → 1, `EAID_90CF5882_E7C6_47d8_BC38_F44A69FF7F31`)

## Pas

klein kaartje met je naam en soms je foto erop, dat je toegang geeft tot bepaalde diensten

Attributen: pasnummer, adresaanduiding.

GUID: `EAID_F6D7A83B_30BC_44f4_91E2_74C04DCE87AE`

Relaties:

- geldig voor → Milieustraat (*Association*, 0..* → 1..*, `EAID_DEE1498F_CA3E_4bd2_9B38_E77E31049F0B`)
- uitgevoerde storting → Storting (*Association*, 1 → 0..*, `EAID_5614D2DC_1440_4241_9399_33073E5A1E4C`)

## Prijsafspraak

Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten.

Attributen: datumStart, datumEinde, titel.

GUID: `EAID_21BBA828_AAE0_4785_9E44_45C1B866C882`

Relaties:

- heeft → Prijsregel (*Association*, 1 → 0..*, `EAID_FDDDA9A7_05A7_4fc6_A28F_9A131CAD0BAD`)

## Prijsregel

Een *prijsregel* is een **regel die aangeeft hoe de prijs van een product, dienst of prestatie wordt vastgesteld of toegepast**, bijvoorbeeld binnen een declaratie- of tariefstructuur.

Attributen: bedrag, credit.

GUID: `EAID_E79C6C20_3D05_49fb_96ED_105B5CD0ABA5`

Relaties:

- betreft → Fractie (*Association*, 1..* → 1, `EAID_7E95D3E7_7C41_4873_9BC8_6BE07BD58617`)

## Rit

Verplaatsing van een wegvoertuig over een wegpad

Attributen: starttijd, eindtijd, ritcode.

GUID: `EAID_832DA9A0_0E64_4d41_8266_38418B095919`

Relaties:

- heeft → Ophaalmoment (*Association*, 1 → 0..*, `EAID_616888E8_12DB_4385_9F2A_EEABBBE80C6E`)
- volgens → Route (*Association*, 0..* → 0..1, `EAID_27329A36_5B92_44c6_8A47_EE43404FD628`)
- uitgevoerd met → Vuilniswagen (*Association*, 0..* → 1, `EAID_F197BB35_77DD_4309_A8B7_D910A033AE6C`)

## Route

Routes die gereden worden om bepaalde fracties vuilnis op te halen. Routes gaan langs locaties, waar afhankelijk van de routesoort een containers, bepaalde plekken of adressen worden aangedaan. huis-aan-huis: er worden locaties met adressen aangedaan illegale dumping, grofvuil: er worden locaties aangedaan (evt met adres) containters: er worden locaties met containers aangedaan

Attributen: routecode, routesoort, geometrie.

GUID: `EAID_55A58838_3877_4e76_B5BF_26C68FAD463D`

Relaties:

- ophalen → Fractie (*Association*, 0..* → 1, `EAID_C09F3E43_5B6A_460b_AD49_C26FE2DCFF78`)
- gaat langs → Locatie (*Association*, 0..1 → 0..*, `EAID_33F2F523_1BA7_4b83_A62D_19A8622465F5`)

## Storting

Activiteit, inhoudende a. het zich ontdoen van stoffen

Attributen: datumtijd, gewicht.

GUID: `EAID_15910FE7_D323_45ff_AA7F_CE3C636CE953`

Relaties:

- fractie → Fractie (*Association*, 0..* → 1..*, `EAID_9F46337A_7B77_464b_AAF3_E339F6D1E39A`)
- bij → Milieustraat (*Association*, 0..* → 1, `EAID_C3B463D6_BCFB_414c_9FDF_C5BFCDC7BC1B`)

## Vuilniswagen

Een vrachtwagen die gebruikt wordt om afval in te zamelen bij bedrijven en huishoudens (huisvuil)

Attributen: code, type, kenteken.

GUID: `EAID_9A422266_783E_4f48_9B12_F442C1B22A45`

Relaties:

- geschikt voor → Containertype (*Association*, 0..* → 1..*, `EAID_F27204F9_AFF0_431a_A5C8_66A1A1736ED1`)

## Vulgraadmeting

Mate waarin een (afval)container gevuld is

Attributen: tijdstip, vulgraad, vullingGewicht.

GUID: `EAID_3650DB98_AC7B_46c0_A607_C54D69E38E42`
