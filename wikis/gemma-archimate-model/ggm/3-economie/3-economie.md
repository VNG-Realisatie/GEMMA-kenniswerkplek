<!-- gegenereerd door tools/ggm.py; hash: 63c18d24db5b5f92bfb21d91a1a82cdbff59b9a3436e8481ffdc53668c956676 -->
# 3 Economie

Taakveld: 3 Economie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Contact | `EAID_3BF6985C_06AB_4cfc_9A0E_5CC37C224245` | Persoon waarmee communicatie plaatsvindt | contactsoort, datum, tekst |
| Hotel | `EAID_5805FA72_C0CE_43c1_A53F_B81166AEFDD4` | Gebouw waar je tegen betaling kunt logeren. | aantalKamers |
| Hotelbezoek | `EAID_669000E9_25D6_4346_B718_516CDB8B88B7` | Verblijf in een hotel | datumStart, datumEinde |
| Verkooppunt | `EAID_8F05E7BA_E7ED_45d1_9626_C8D7FBDB2F1B` | Locatie waar iets wordt verkocht | winkelformule |
| Werkgelegenheid | `EAID_EB35F5B8_9289_49cc_8DF4_8BD20EC662A9` | De vraag naar arbeid, te berekenen door de totale productie te delen door de arbeidsproductiviteit per persoon. | aantalFulltimeMannen, aantalFulltimeVrouwen, aantalParttimeVrouwen, aantalParttimeMannen, grootteklasse |
| Winkelvloeroppervlak | `EAID_0EABA880_434F_41c3_A41D_0002222AAC2A` | Gemeten oppervlakte in vierkante meters van een winkel | winkelvloeroppervlakte, WVOKlasse, bronWVO, leegstand, aantalKassa |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Contact | Association | met | NatuurlijkPersoon | 0..* → 0..* | `EAID_C836212C_BD57_42b6_B51D_E49EA2853F66` |  |
| Contact | Association | bij | Vestiging | 0..* → 0..1 | `EAID_F74AC804_79E6_40a6_992F_C50B4F045C90` |  |
| Hotel | Association | heeft | Hotelbezoek | 1 → 0..* | `EAID_7570B853_AEE4_4a58_A791_9FE8BE675DD6` |  |
| Hotel | Generalization |  | Vestiging |  →  | `EAID_2480687F_FBAE_4e71_805B_0456E338F9D4` |  |
| Verkooppunt | Generalization |  | Vestiging |  →  | `EAID_C9C1BB34_7A67_4b56_B6A0_1DCDF215AD43` |  |
