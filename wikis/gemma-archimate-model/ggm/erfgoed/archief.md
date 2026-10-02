<!-- gegenereerd door tools/ggm.py; hash: 4a1656ac195335cbe10b888237d0a58fad21dfb09a7efbe4c3e9940264a2d6a5 -->
# Archief

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

## Aanvraag

(officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.

Attributen: datumtijd.

GUID: `EAID_2F2A3590_9B34_4ec5_B0AE_B487ED241155`

Relaties:

- voor → Archiefstuk (*Association*, 0..* → 0..*, `EAID_6941BFAC_0A5F_49b1_92B2_0AD5EF8F7D88`)

## Archief

De bewaarplaats van belangrijke gegevens die zijn vastgelegd in documentvorm alsook de verzameling van documenten die voor een bepaald doel vervaardigd zijn.

Attributen: naam, omschrijving, openbaarheidsbeperking, archiefnummer.

GUID: `EAID_E09E5B44_4D39_455a_B0A5_390A63AC0C43`

Relaties:

- valt binnen → Archiefcategorie (*Association*, 0..* → 0..*, `EAID_6E5A130E_ADAA_49b7_B413_2D6E404039F6`)
- stamt uit → Periode (*Association*, 0..* → 1..*, `EAID_F50E960E_F058_49d1_BEE4_CDC528BE386F`)
- heeft → Rechthebbende (*Association*, 0..* → 0..1, `EAID_B592184C_6739_49fe_9E13_B8D972C049AA`)

## Archiefcategorie

Typologie van een archief conform landelijke indeling

Attributen: naam, omschrijving, nummer.

GUID: `EAID_66DB38CC_932D_462c_9791_C60237EA9B7A`

## Archiefstuk

Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transacties.(AAT)

Attributen: trefwoorden, openbaarheidsbeperking, inventarisnummer, omvang, beschrijving, uiterlijkeVorm.

GUID: `EAID_369E453B_4C3A_48dc_9619_C36232B339D9`

Relaties:

- is onderdeel van → Archief (*Association*, 0..* → 1..1, `EAID_2907D6A4_5E68_4260_888D_6A2F4DBED03F`)
- heeft → DigitaalBestand (*Association*, 1..1 → 0..*, `EAID_0520C4AE_A1CB_4bc1_A3C2_F5763CB45D1B`)
- heeft → Nadere Toegang (*Association*, 1..1 → 0..1, `EAID_BC9161A8_B949_418c_8460_7BE95515134F`)
- heeft → Ordeningsschema (*Association*, 0..* → 0..*, `EAID_93326F4C_59F0_4858_82A9_04FE93151B7F`)
- stamt uit → Periode (*Association*, 0..* → 1..*, `EAID_FBD7B308_2CAD_425e_ACCA_ADFE8C30993C`)
- heeft → Uitgever (*Association*, 0..* → 0..1, `EAID_2A8819BB_D6B0_4dbf_BE82_21CAD5A21361`)
- heeft → Vindplaats (*Association*, 0..* → 1..1, `EAID_2C2606E9_7715_4136_A6A2_67CBD99E13A6`)
- → Document (*Generalization*,  → , `EAID_6217449D_B1A2_4d75_9C2B_3722E27B287B`)
- → Erfgoed Object (*Generalization*,  → , `EAID_56A06DA3_0A4E_4b13_9A21_35FDCF6B91B9`)

## Auteur

De persoon die verantwoordelijk is voor de inhoud van een (digitaal) document

Attributen: datumGeboorte, datumOverlijden.

GUID: `EAID_BCAFBBCD_851E_4235_9D85_88EC71F2245B`

Relaties:

- → Historisch Persoon (*Generalization*,  → , `EAID_56BA52DC_84C6_4e49_9224_B1BFD1A6BD8B`)

## Bezoeker

Een persoon die iemand of iets bezoekt.

GUID: `EAID_066C9C37_0FAF_4239_8D7D_B7EBE42E4918`

Relaties:

- doet → Aanvraag (*Association*, 1..1 → 0..*, `EAID_1208CAFE_5505_4681_A175_BBF40F2DB352`)
- → NatuurlijkPersoon (*Generalization*,  → , `EAID_BCD2F6EC_CB32_488b_90B9_F2C29206D0EA`)

## Depot

Plaats waar iets bewaard wordt.

Attributen: naam, omschrijving.

GUID: `EAID_604A6143_DE7F_4950_B3D4_DFB88C7F4670`

Relaties:

- heeft → Stelling (*Association*, 1..1 → 0..*, `EAID_88AEF29B_D906_4ba5_B394_135C20D857EF`)

## DigitaalBestand

Bestand dat uitsluitend met behulp van besturingsprogrammatuur of toepassingsprogrammatuur geraadpleegd kunnen worden

Attributen: naam, omschrijving, mimetype, blob.

GUID: `EAID_FEFE9DBE_921F_4cc4_99C5_972A9C5F4C6E`

## Indeling

Onderwerpen groeperen in samenhangende categorieën.

Attributen: naam, nummer, omschrijving, indelingsoort.

GUID: `EAID_13119DEC_D451_4bec_BB37_7B1944ACCA9D`

Relaties:

- hoort bij → Archief (*Association*, 0..* → 1..1, `EAID_99BFEAAB_AEF8_424e_B567_5D1DC2F5EE15`)
- valt binnen → Archiefstuk (*Association*, 0..1 → 0..*, `EAID_9608D483_4A70_43a3_A08A_94E36A899845`)
- valt binnen → Indeling (*Association*, 1..1 → 0..*, `EAID_CF9A5227_0396_435a_8734_0980E5661383`)

## Index

Attributen: indexnaam, indexwaarde.

GUID: `EAID_C45E0D5D_3B2F_40a7_B12C_B6E910C516FA`

## Kast

Object met een permanent karakter dat dient om iets in te bergen en te beschermen.

Attributen: kastnummer.

GUID: `EAID_CA844994_4AAE_417f_82A3_31CA5432237A`

Relaties:

- heeft → Plank (*Association*, 0..1 → 0..*, `EAID_5A187491_2E2F_4344_A191_E6973A644E4E`)

## Nadere Toegang

De bevoegdheid om gegevens te raadplegen, bepaalde plaatsen te betreden of een bepaalde taak uit te oefenen.

GUID: `EAID_7A080605_07C5_4947_9B35_BC6EBE2041FA`

Relaties:

- wordt beschreven → Index (*Association*, 1..1 → 1..*, `EAID_3CABDAAA_CBFF_4baf_83F5_E5EDAEFA5A8F`)

## Ordeningsschema

Ordening om archief en collecties beter vindbaar en bruikbaar voor betrokkenen.

Attributen: naam, text.

GUID: `EAID_B61986A2_B8E7_4e69_AD55_E61771FDEEB4`

## Plank

Deel, plaat; stuk hout breder dan het dik is en langer dan breed.

Attributen: planknummer.

GUID: `EAID_D9693C25_0F66_4504_BE2B_4BBF66071026`

## Rechthebbende

Een rechthebbende is iemand die rechten heeft op een goed.

GUID: `EAID_9AE5BCE3_AD6D_4241_9651_823400E3745F`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_6732FBFE_815B_4a32_AF06_655F4A3CCEDB`)

## Stelling

Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia)

Attributen: stellingnummer.

GUID: `EAID_78DA1B42_4AF8_4650_81A0_7F2C3A450B3D`

Relaties:

- heeft → Kast (*Association*, 1..1 → 0..*, `EAID_0F2A93BC_D421_4e98_A566_CD5F2C347D4E`)

## Uitgever

Iemand die iets op de markt brengt; iemand die iets uitgeeft

GUID: `EAID_59CF7225_3D61_42e2_A399_7EB13450D97D`

Relaties:

- → Rechtspersoon (*Generalization*,  → , `EAID_3231E963_F0A1_46fd_A304_F2C9C8BBA8D5`)

## Vindplaats

Een plek waar men iets gevonden heeft.

GUID: `EAID_D7947186_4317_407b_A456_41DF5187E810`

Relaties:

- is te vinden in → Depot (*Association*, 0..* → 1..1, `EAID_5B6E5EE5_1ED8_40de_9294_B50BFAFC2A5F`)
- is te vinden in → Kast (*Association*, 0..* → 1..1, `EAID_00A89678_8013_45ef_B523_EAE54EADE361`)
- is te vinden in → Plank (*Association*, 0..* → 1..1, `EAID_17951F4C_9871_476b_AFB3_7B3848B3B93D`)
- is te vinden in → Stelling (*Association*, 0..* → 0..1, `EAID_E19D5B42_D3F7_4c43_9037_DA4531AFF728`)
