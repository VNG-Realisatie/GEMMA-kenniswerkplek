<!-- gegenereerd door tools/ggm.py; hash: 22fb767ca1941a333bec517df9edecc9cbb1c67f39b0c083f7d2aa0efa032544 -->
# 3 Economie

Taakveld: 3 Economie. Alleen objecttypen; letterlijke definities uit het GGM.

## Contact

Persoon waarmee communicatie plaatsvindt

Attributen: contactsoort, datum, tekst.

GUID: `EAID_3BF6985C_06AB_4cfc_9A0E_5CC37C224245`

Relaties:

- met → NatuurlijkPersoon (*Association*, 0..* → 0..*, `EAID_C836212C_BD57_42b6_B51D_E49EA2853F66`)
- bij → Vestiging (*Association*, 0..* → 0..1, `EAID_F74AC804_79E6_40a6_992F_C50B4F045C90`)

## Hotel

Gebouw waar je tegen betaling kunt logeren.

Attributen: aantalKamers.

GUID: `EAID_5805FA72_C0CE_43c1_A53F_B81166AEFDD4`

Relaties:

- heeft → Hotelbezoek (*Association*, 1 → 0..*, `EAID_7570B853_AEE4_4a58_A791_9FE8BE675DD6`)
- → Vestiging (*Generalization*,  → , `EAID_2480687F_FBAE_4e71_805B_0456E338F9D4`)

## Hotelbezoek

Verblijf in een hotel

Attributen: datumStart, datumEinde.

GUID: `EAID_669000E9_25D6_4346_B718_516CDB8B88B7`

## Verkooppunt

Locatie waar iets wordt verkocht

Attributen: winkelformule.

GUID: `EAID_8F05E7BA_E7ED_45d1_9626_C8D7FBDB2F1B`

Relaties:

- → Vestiging (*Generalization*,  → , `EAID_C9C1BB34_7A67_4b56_B6A0_1DCDF215AD43`)

## Werkgelegenheid

De vraag naar arbeid, te berekenen door de totale productie te delen door de arbeidsproductiviteit per persoon.

Attributen: aantalFulltimeMannen, aantalFulltimeVrouwen, aantalParttimeVrouwen, aantalParttimeMannen, grootteklasse.

GUID: `EAID_EB35F5B8_9289_49cc_8DF4_8BD20EC662A9`

## Winkelvloeroppervlak

Gemeten oppervlakte in vierkante meters van een winkel

Attributen: winkelvloeroppervlakte, WVOKlasse, bronWVO, leegstand, aantalKassa.

GUID: `EAID_0EABA880_434F_41c3_A41D_0002222AAC2A`
