<!-- gegenereerd door tools/ggm.py; hash: e5757e008ec55a97d2bc03e60c3d7f05040d24007e1fced298c99a17b17c4a48 -->
# Sport

Taakveld: 5 Sport, Cultuur en Recreatie. Alleen objecttypen; letterlijke definities uit het GGM.

## Belijning

Op of in het oppervlak van de verharding aangebrachte tekens ter geleiding, waarschuwing, regeling of informatie van het verkeer

Attributen: naam.

GUID: `EAID_9E01AD8B_D856_4a58_9CE1_06C70F628350`

## Bezetting

Aantal deelnemers aan een activiteit

GUID: `EAID_D9F56210_BF72_42e4_A1BC_AD7F683D55A0`

## Binnenlocatie

Locatie binnen een gebouw

Attributen: bouwjaar, vloeroppervlakte, klokurenOnderwijs, klokurenVerenigingen, onderhoudsstatus, onderhoudsniveau, geschatteKostenPerJaar, locatie, adres, sporthal, gymzaal, gemeentelijk.

GUID: `EAID_6508657D_7C3F_4261_B647_5D3B077A20F9`

Relaties:

- heeft → Belijning (*Association*, 0..* → 0..*, `EAID_D1CABCB9_BCC0_4288_96F7_C66C76C6D252`)
- heeft → Sportmateriaal (*Association*, 0..* → 0..*, `EAID_B86CBE10_CDA1_4945_BE76_236321765DCF`)
- is gevestigd in → Verblijfsobject (*Association*, 0..* → 0..1, `EAID_07B7AA32_6C85_4f64_88FC_B13D20D10B69`)
- is gevestigd in → Verblijfsobject (*Association*, 0..* → 0..1, `EAID_B8A7B3F7_4835_4e90_9EE3_B1A006D7FF55`)
- bedient → Wijk (*Association*, 0..* → 1, `EAID_ACAA8C5B_98C8_4040_9BF5_B0B95F43F945`)
- bedient → Wijk (*Association*, 0..* → 1, `EAID_C07B0FB7_C253_47a8_8D08_228AFC02EC08`)
- → Sportlocatie (*Generalization*,  → , `EAID_0D3EE350_90B3_41f5_B256_C15AA6192205`)
- inspectierapport → Document (*Usage*, 0..1 → 0..*, `EAID_20BD6184_0D82_41ea_AAAC_78C6AF1EDE66`)

## Onderhoudskosten

Kosten voor het onderhoud van iemand of iets, hetzij om te voorzien in de levensbehoeften van personen, hetzij voor de instandhouding en verzorging van zaken.

GUID: `EAID_5C8F7563_D1FF_4622_8565_F48A1BCAB9E3`

## Sportlocatie

Locatie waar de betreffende sport plaatsvindt

Attributen: naam.

GUID: `EAID_BE5E10D0_FD83_4b0a_B5D2_4A7EE6B9C53B`

## Sportmateriaal

Materieel om sport mee te beoefenen of ter odnersteuning van de sportuitvoering.

Attributen: naam.

GUID: `EAID_5B64A5F8_64B5_4d1b_BEDD_486ED2C2C493`

## Sportpark

Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport.

GUID: `EAID_FE1A2EF2_44FA_46fa_A583_7BAB858E17FD`

Relaties:

- ligt op → OverigBenoemdTerrein (*Association*, 0..1 → 1, `EAID_C32A50B9_89E5_48b5_93DD_DD21E01E2E4C`)
- heeft → Veld (*Association*, 0..1 → 0..*, `EAID_ADFCB89E_2296_4c77_B112_FD165DE4F164`)
- → Sportlocatie (*Generalization*,  → , `EAID_C9BFBD40_0BE4_4607_9509_98244DB5DE36`)

## Sportvereniging

Organisatievorm waarin sport bedreven kan worden

Attributen: naam, typeSport, binnensport, buitensport, email, adres, ledenaantal, aantalNormTeams.

GUID: `EAID_852AD372_B353_49c2_A4E7_F87D8AA96AD7`

Relaties:

- gebruikt → Sportlocatie (*Association*, 0..* → 0..*, `EAID_B5E7BB72_759A_457c_8CD9_6EDD0C20BFC5`)
- → NietNatuurlijkPersoon (*Generalization*,  → , `EAID_D1E2A784_6163_4a1f_87BA_6BE650606078`)

## Veld

Een stuk land dat speciaal voor het bedrijven van een veldsport gereedgemaakt is

GUID: `EAID_D1889096_CC76_48a8_A9DF_8151FFF1E0AC`

Relaties:

- heeft → Belijning (*Association*, 0..* → 0..*, `EAID_E0398E9C_B2DD_403a_98FC_EBB0A8851598`)
- ligt op → OverigBenoemdTerrein (*Association*, 0..1 → 1, `EAID_E803AA60_7038_4d6e_B5BA_2741116E7008`)
