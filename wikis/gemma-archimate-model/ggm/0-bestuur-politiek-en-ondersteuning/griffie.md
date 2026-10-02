<!-- gegenereerd door tools/ggm.py; hash: b2a4982c4c7efa145fc1d698357777a82f7ca972073f845ab351a6b69ac2655c -->
# Griffie

Taakveld: 0 Bestuur, Politiek en Ondersteuning. Alleen objecttypen; letterlijke definities uit het GGM.

## Aanwezige Deelnemer

iemand die meedoet aan eencollege- of raadsvergadering

Attributen: aanvangAanwezigheid, eindeAanwezigheid, rol, vertegenwoordigtOrganisatie, naam.

GUID: `EAID_F1E55DC7_0F33_40ea_8713_2E1AC3D7EE8D`

Relaties:

- is → Collegelid (*Association*, 0..1 → 0..1, `EAID_09E484E1_ACD5_4340_B916_371787D426CF`)
- is → NatuurlijkPersoon (*Association*, 0..1 → 0..1, `EAID_BE36E0F8_0D39_41ce_BE5D_9723DCE88E81`)

## Agendapunt

Een onderwerp dat in de vergadering wordt behandeld.

Attributen: nummer, titel, omschrijving.

GUID: `EAID_73FB5212_40ED_40dc_B837_36588840445A`

## Categorie

Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren

Attributen: naam.

GUID: `EAID_B9B82B25_5D7F_4d2b_84F9_4DF74525EEAD`

Relaties:

- heeft → Raadsstuk (*Association*, 0..1 → 0..*, `EAID_E5CC9977_A6A5_4d53_B7F5_394A7C56235C`)

## Collegelid

Iemand die behoort het college van burgemeester en wethouders

Attributen: voornaam, achternaam, titel, fractie, portefeuille, datumAanstelling, datumUittreding.

GUID: `EAID_7B9EDDFD_57F7_4ff2_938F_FDFA3B503DA8`

Relaties:

- → Ingezetene (*Generalization*,  → , `EAID_A589113E_6865_4318_9B25_A339169D7B02`)

## Dossier

Samenhangende set gegevens en informatie voor een specifiek doel

Attributen: naam.

GUID: `EAID_475E24C9_CC9A_49cc_AB80_8CA0221441E5`

Relaties:

- hoort bij → Raadsstuk (*Association*, 0..* → 0..*, `EAID_97901C7A_E07B_49af_828A_2F0E03C8E795`)

## Indiener

Persoon die meldiing of aanvraag doet

Attributen: naam, omschrijving.

GUID: `EAID_98CB3C6F_588B_479f_9A2B_F5D5362DD17C`

Relaties:

- is → Collegelid (*Association*, 0..1 → 0..1, `EAID_BAB2F0D0_9317_45c8_A353_9989968728B6`)
- is → Raadslid (*Association*, 0..1 → 0..1, `EAID_16819B21_09BC_4882_9D17_6BDA1FAE308F`)
- heeft → Raadsstuk (*Association*, 0..* → 1..*, `EAID_7E93A04F_3844_49ba_B1AB_F26D73012118`)
- is → Rechtspersoon (*Association*, 0..1 → 0..1, `EAID_CE20BFC0_F092_4cef_853B_695F355221B6`)

## Programma

Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te coördineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie.

Attributen: naam.

GUID: `EAID_CA56A59A_F855_4c19_89BE_578B12481EA0`

## Raadscommissie

Een raadscommissie binnen de Nederlandse gemeenteraad is een groep raadsleden die zich buigt over specifieke thema's of beleidsonderwerpen om de besluitvorming in de volledige raad voor te bereiden en te ondersteunen.

Attributen: naam.

GUID: `EAID_CB27D699_F82B_45ad_823A_B2B51BCAECBA`

Relaties:

- heeft → Vergadering (*Association*, 0..1 → 0..*, `EAID_84B35607_9C4D_47a2_B9E0_5C20A2C477FB`)

## Raadslid

Iemand die behoort de gemeenteraad

Attributen: voornaam, achternaam, titel, fractie, datumAanstelling, datumUittreding.

GUID: `EAID_5772BEBB_97FA_42a9_B70D_DB55EAD6D1EE`

Relaties:

- is → Aanwezige Deelnemer (*Association*, 0..1 → 0..1, `EAID_85F0446A_CB6B_456e_91A6_3CA8C45D2550`)
- is lid van → Raadscommissie (*Association*, 0..* → 0..*, `EAID_1DF94C0B_C6BD_4c7d_9AE2_5761713339DB`)
- → Ingezetene (*Generalization*,  → , `EAID_95BB643E_8174_4680_9551_3503B188F7AC`)

## Raadsstuk

Stuk dat door de gemeenteraad wordt behandeld

Attributen: datumRegistratie, datumPublicatie, datumExpiratie, besloten, typeRaadsstuk.

GUID: `EAID_440219A4_C64B_4eac_ADE5_E79ED6AA9BFE`

Relaties:

- → Document (*Abstraction*,  → , `EAID_37D02D26_7ADF_4bd4_8F62_682F2E943C29`)
- behandelt → Agendapunt (*Association*, 0..* → 0..*, `EAID_5A64B46B_96A6_4f1c_B92A_44B925160E61`)
- hoort bij → Programma (*Association*, 0..* → 0..*, `EAID_A06DA05F_8BC4_497b_8A7B_05774189434F`)
- heeft → Taakveld (*Association*, 0..* → 0..1, `EAID_E4D00870_1DF1_4693_909D_E94782A7BEF9`)
- wordt behandeld in → Vergadering (*Association*, 0..* → 0..*, `EAID_AA12C031_2ED2_4fde_911F_CFE585E81CB0`)

## Stemming

Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering

Attributen: resultaat, stemmingstype.

GUID: `EAID_331C4A0B_1505_4945_A0B0_DCD8703AB50F`

Relaties:

- hoort bij → Agendapunt (*Association*, 0..* → 0..1, `EAID_1C2E6D7B_B9F0_48a9_9EB6_C68727E25A65`)
- betreft → Raadsstuk (*Association*, 0..1 → 1, `EAID_6212E314_EC1D_4325_B5F1_06DFC208F360`)

## Taakveld

Een samenhangend geheel van activiteiten en taken en hangt onder een programma.

Attributen: naam.

GUID: `EAID_01E83CEC_D69D_47eb_9BAB_252AABADDD18`

## Vergadering

Een bijeenkomst van meerdere mensen (meestal van eenzelfde organisatie) die met elkaar spreken en/of afspraken maken over de gemeenschappelijke toekomst.

Attributen: eindtijd, starttijd, titel, locatie.

GUID: `EAID_257F4ABF_7CCD_453f_B2E8_5A6434383A9B`

Relaties:

- → Aanwezige Deelnemer (*Association*, 1..1 → 0..*, `EAID_29CBC16D_7D9B_469a_8641_EC4ABE5C3795`)
- heeft → Agendapunt (*Association*, 1 → 0..*, `EAID_4A5F49E9_B2F8_4ee3_AFE4_963CAF4FB6F4`)
- heeft verslag → Raadsstuk (*Association*, 0..1 → 0..1, `EAID_478BEE5A_22BB_4688_9AF4_5B6A29A16BAF`)
- betreft → Video-opname (*Association*, 1 → 0..*, `EAID_74669FE0_D963_4e2d_97C6_FE532ADE734E`)
