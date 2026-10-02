<!-- gegenereerd door tools/ggm.py; hash: 745a69fc4891f768fa25d522722aabb567b942036c450f68f9b6f88b627ad1b5 -->
# HR

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

## Beoordeling

Beoordeling is het oordeel van de professional over het functioneren van een leerling

Attributen: datum, oordeel, omschrijving.

GUID: `EAID_2A0CC803_9017_4fad_99B5_9347623090F5`

Relaties:

- vastlegging → Document (*Usage*,  → , `EAID_FECC6A70_6D99_4103_AC80_81549EEC578A`)

## Declaratie

Een opgave van te vergoeden kosten.

Attributen: datumIndiening, datumDeclaratie, betreft, omschrijving, bedrag.

GUID: `EAID_E611CEB2_F4FA_49e2_AA6B_B380BC1918AC`

Relaties:

- soort declaratie → Declaratiesoort (*Association*, 0..* → 1..1, `EAID_53ABD040_F8F1_4d2c_AD7A_9A832A9649E1`)

## Declaratiesoort

Typering van een declaratie

Attributen: naam, omschrijving.

GUID: `EAID_9D4FB9DF_D68A_4503_96C0_272B6777A4FC`

## Dienstverband

De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst.

Attributen: datumStart, datumEinde, salaris, periodiek, schaal, urenPerWeek.

GUID: `EAID_63FF86E2_1BB0_48f6_8D95_3D82E8D2FA06`

Relaties:

- dienstverband conform functie → Functie (*Association*, 0..* → 1, `EAID_B3C69ADB_9237_4bde_937C_8A9B873AD176`)
- onderdeel van → OrganisatorischeEenheidHR (*Association*, 0..* → 1..*, `EAID_0F596F15_608B_4a1a_ADE6_D1053EF13FF8`)
- is op vestiging → VestigingVanZaakbehandelendeOrganisatie (*Association*, 0..* → 0..*, `EAID_DAE508E1_5EDF_4ff6_B108_E83324586885`)
- arbeidsovereenkomst → Document (*Usage*,  → , `EAID_BB3D43B2_D0C6_4bd8_98C7_A5DCD4EF7230`)

## Disciplinaire Maatregel

Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt.

Attributen: datumGeconstateerd, datumOpgelegd, omschrijving, reden.

GUID: `EAID_50F3F931_38F4_4ff0_8CE4_8A51056767E0`

Relaties:

- soort maatregel → SoortDisciplinaireMaatregel (*Association*, 0..* → 1..1, `EAID_48BA20B4_B020_400d_8936_9F8AD9650F3B`)

## Formatieplaats

Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar

Attributen: uren per week.

GUID: `EAID_81EFBDCE_E500_4090_A37A_D3F799517866`

Relaties:

- toegewezen aan → Dienstverband (*Association*, 0..* → 0..*, `EAID_C886E8C0_39ED_477b_A430_B7577E0A3238`)
- functie van formatieplaats → Functie (*Association*, 0..* → 1..*, `EAID_FA8E1AC6_EB2C_4a69_A5B1_7F05B3CE3168`)
- onderdeel van → OrganisatorischeEenheidHR (*Association*, 1 → 0..1, `EAID_B12C3E92_BEF7_4859_A882_A37444268D3C`)

## Functie

Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden

Attributen: Naam, Omschrijving, Taken, Schaal, Code.

GUID: `EAID_F29C11C1_477C_4b90_985C_43F94D08230A`

Relaties:

- gebaseerd op → NormProfiel (*Association*, 1 → 1, `EAID_631F8439_F29C_4a41_A8E3_4C52BBEA69A4`)

## Functiehuis

Model waarin functies van een organisatie worden beschreven.

Attributen: naam, omschrijving.

GUID: `EAID_D69EE16A_390C_4d6f_BC01_2B13FB3B22F1`

## GenotenOpleiding

Afgeronde opleiding, een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden

Attributen: datumStart, datumEinde, datumToewijzing, prijs, verrekenen.

GUID: `EAID_261363C5_1E00_4b6a_B570_2129DC044010`

Relaties:

- soort opleiding → Opleiding (*Association*, 0..* → 1..1, `EAID_B56E335E_B0BB_4876_939E_FD93B18E9768`)

## Geweldsincident

Een gebeurtenis met betrekking tot agressie en omvat het veroorzaken van verwondingen of schade bij mensen, dieren, of voorwerpen.

Attributen: datum, type, omschrijving.

GUID: `EAID_41AFF74F_ADBE_4f3f_AB2F_25027A70E573`

## Individueel Keuzebudget

Bedrag dat feitelijk beschikbaar gesteld wordt voor een individu om een bepaalde keus te kunnen maken

Attributen: datumStart, datumEinde, datumToekenning, bedrag.

GUID: `EAID_B64178F1_7D37_4a77_BEF7_97E8C9DDA4E8`

Relaties:

- besteding → KeuzebudgetBesteding (*Association*, 1..1 → 0..*, `EAID_DD7FF2ED_F806_4692_9334_1B5561305B9C`)
- heeft individueel keuzebudget → Werknemer (*Association*, 0..* → 1..1, `EAID_AEC374FB_B966_4408_9540_612BDB839919`)

## Inzet

Uren inzet die gepleegd wordt in een bepaalde periode op een organisatorische eenheid en het percentage dat ook daadwerkelijk wordt uitgevoerd.Dit kan afwijken van de contractuele uren.

Attributen: datumBegin, datumEinde, percentage, uren.

GUID: `EAID_532191CA_13CC_4500_93C9_54AB2862F38D`

Relaties:

- aantal volgens inzet → Dienstverband (*Association*, 1 → 0..*, `EAID_B365F23E_A00D_4fef_9EE3_A416614B00C6`)
- inzet voor functie → Functie (*Association*, 1 → 1, `EAID_BA44BA34_41E8_4faf_8D8E_7693BCC345B3`)
- inzet bij → OrganisatorischeEenheidHR (*Association*, 0..* → 1, `EAID_30F12B18_84AE_4b2a_A642_F2CD8D1AA505`)

## KeuzebudgetBesteding

De daadwerkelijk uitgave van een keuzebudget

Attributen: datum, bedrag.

GUID: `EAID_B9288D01_0B8F_4f8c_BAE1_AFD1B0EF6FDF`

Relaties:

- soort besteding → KeuzebudgetBestedingsoort (*Association*, 0..* → 1..1, `EAID_42E94BB7_BBBE_4cfd_BE12_83932898ADDA`)

## KeuzebudgetBestedingsoort

Typering van een keuzebudgetbesteding

Attributen: naam, omschrijving.

GUID: `EAID_A0051651_4772_436d_9553_B432BDCE3A52`

## NormProfiel

Normprofiel of Normfunctie:nGenerieke functie zoals beschreven in HR21. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden

Attributen: code, omschrijving, schaal.

GUID: `EAID_E1C6E98B_20B2_43b0_8EC1_5C0905B3A139`

Relaties:

- onderdeel van → Functiehuis (*Association*, 1..* → 1, `EAID_7BF736B1_C39A_4cd3_8C30_EB2A0FEA2980`)

## Onderwijsinstituut

Een instituut waar onderwijs wordt gegeven.

GUID: `EAID_59F3063A_13A6_4cbc_A387_045A6B126746`

Relaties:

- → NietNatuurlijkPersoon (*Generalization*,  → , `EAID_C571BFF8_D84B_481e_8A46_D9706B3AB3D1`)

## Opleiding

Een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden.

Attributen: naam, omschrijving, prijs, instituut.

GUID: `EAID_E07D60DE_CD26_4cef_A18B_6F72CC76C1B6`

Relaties:

- wordt gegeven door → Onderwijsinstituut (*Association*, 1..* → 1..*, `EAID_276851B1_EF8E_4e97_ABD2_AAB5A18AC50F`)

## OrganisatorischeEenheidHR

Specialisatie van de Organisatorische eenheid uit het RGBZ voor het HR domein.

Attributen: naam, type.

GUID: `EAID_53B0C49F_1BDE_4fee_BB0B_0D82517177CC`

Relaties:

- → OrganisatorischeEenheid (*Generalization*,  → , `EAID_7995B3F4_9366_472e_96A4_BCFBF6DFB7EB`)

## Relatie

Betrekking waarin personen, zaken, begrippen of grootheden van nature tot elkaar staan.

GUID: `EAID_FE559B58_A6CD_4108_82BE_98E1AEBFD9BD`

Relaties:

- is kind van → Werknemer (*Association*, 0..* → 1, `EAID_F7CE1157_F7D4_4967_81D0_55F7619A680F`)
- → NatuurlijkPersoon (*Generalization*,  → , `EAID_B8C56861_C624_4bb4_9DDC_F096ED47139C`)

## Rol

De rol van de medewerker, zoals afdelingshoofd of manager

Attributen: datumBegin, datumEinde, omschrijving.

GUID: `EAID_BF424764_453D_46cc_817C_3A7BDC4134A7`

Relaties:

- hoort bij → OrganisatorischeEenheidHR (*Association*, 0..* → 0..1, `EAID_F1F6FACA_0A8D_4904_BA95_CF4984524E7C`)

## Sollicitant

Persoon die werk zoekt

GUID: `EAID_131BDD67_2A31_43c5_9125_F12DE2D98D2D`

Relaties:

- solliciteert op functie → Sollicitatie (*Association*, 1..1 → 0..*, `EAID_7ED83E72_5019_47f5_84BF_5A3DC813EF67`)
- → NatuurlijkPersoon (*Generalization*,  → , `EAID_0051D0C2_0529_422f_9F8F_34BD200A2C9B`)

## Sollicitatie

Verzoek om in een functie te worden aangesteld.

Attributen: datum.

GUID: `EAID_3BD1368C_23F1_4f42_99DB_C81581A646A0`

Relaties:

- op vacature → Vacature (*Association*, 0..* → 1..1, `EAID_69D5B4D8_4D23_4a03_AF7E_9DD4B3B0B439`)

## Sollicitatiegesprek

Onderhoud tussen sollicitant en werkgever met betrekking tot een sollicatie

Attributen: datum, opmerkingen, volgendGesprek, aangenomen.

GUID: `EAID_1D4DA0E6_DA20_4ff7_A415_B937712C6F6D`

Relaties:

- kandidaat → Sollicitant (*Association*, 0..* → 0..*, `EAID_BED7E9A7_0ECA_4b8b_8EF8_117D8668B970`)
- in kader van → Sollicitatie (*Association*, 0..* → 1..1, `EAID_34310019_D4F3_4952_97C7_EE9936584868`)
- doet sollicitatiegesprek → Werknemer (*Association*, 0..* → 1..*, `EAID_5E83AD01_AAD7_4d8b_9F09_4180F84BF53B`)

## SoortDisciplinaireMaatregel

Typering van een disciplinaire maatregel

Attributen: naam, omschrijving.

GUID: `EAID_B0747DFC_DFC8_4ef2_8E1E_C2E8606036FC`

## Uren

Aantal besteedde uren aan een activiteit

Attributen: aantal.

GUID: `EAID_93165DEC_ECB7_4225_9484_E1727524A1B5`

Relaties:

- aantal volgens inzet → Dienstverband (*Association*, 1..1 → 0..*, `EAID_2F508CBE_E926_4a6d_B85C_401E0BBCDA2F`)

## Vacature

Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden.

Attributen: datumOpengesteld, datumGesloten, intern, extern, deeltijd, vastedienst.

GUID: `EAID_DC978807_5F36_4148_B816_D6886D026DD8`

Relaties:

- vacature bij functie → Functie (*Association*, 0..* → 1..1, `EAID_8ACA644F_8D3A_4ab0_B755_24F44D39EEC1`)
- vacaturetekst → Document (*Usage*,  → , `EAID_512E1661_34DE_4e18_9A66_9C4D5B1238D1`)

## Verlof

Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn.

Attributen: datumtijdStart, datumtijdEinde, goedgekeurd, datumAanvraag, datumToekenning.

GUID: `EAID_D04135BF_C2F0_46dd_B332_F1BE36C358EF`

Relaties:

- soort verlof → Verlofsoort (*Association*, 0..* → 1..1, `EAID_3EDEEC77_46DE_47eb_AD90_10AA60A69F0C`)

## Verlofsoort

Typering van verlof

Attributen: naam, omschrijving.

GUID: `EAID_ED741EE1_E773_40e3_B0E6_8D9886EB792F`

## Verzuim

Een afwezigheid van een werknemer van werk.

Attributen: datumtijdStart, datumtijdEinde.

GUID: `EAID_610B18E6_B675_4cc0_A883_BAB9D384C668`

Relaties:

- soort verzuim → Verzuimsoort (*Association*, 0..* → 1..1, `EAID_8B730311_4D6F_4d43_8A5B_8E099B4C421C`)

## Verzuimsoort

Typologie van verzuim

Attributen: naam, omschrijving.

GUID: `EAID_45900108_585D_45ec_A042_BF4928B7F6DC`

## Werknemer

De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst.

Attributen: naam, voornaam, geboortedatum, woonplaats.

GUID: `EAID_BBBB63AC_B546_409b_B6D4_53DB561253B7`

Relaties:

- Beoordeeld door → Beoordeling (*Association*, 1..1 → 0..*, `EAID_24BF4DCE_5DDC_4c1b_92F0_EFADF4BE03B9`)
- beoordeling van → Beoordeling (*Association*, 1..1 → 0..*, `EAID_6357FC97_EE14_4c30_BCC3_6903DF51DA36`)
- dient in → Declaratie (*Association*, 1..1 → 0..*, `EAID_89425B69_C330_426d_B0E5_9C8C5EF6310E`)
- medewerker heeft dienstverband → Dienstverband (*Association*, 1..1 → 1..*, `EAID_8AB912F9_CF51_4288_85FB_DC19C1E92659`)
- heeft maatregel → Disciplinaire Maatregel (*Association*, 1..1 → 0..*, `EAID_68D387CF_74AA_4219_8B64_52D7FE6A8DC5`)
- heeft genoten → GenotenOpleiding (*Association*, 1..1 → 0..*, `EAID_C14E8E75_F958_4d73_972F_E0E1FA74400A`)
- heeft ondergaan → Geweldsincident (*Association*, 0..* → 1..1, `EAID_8AF83985_ABFC_4a38_95D3_CB368AA680BA`)
- is partner van → Relatie (*Association*, 1 → 0..1, `EAID_04C60911_78B7_4a60_BF69_BF5722278217`)
- heeft → Rol (*Association*, 1..* → 0..*, `EAID_58514271_87E3_4f5f_A3E4_AF251AA7D9C9`)
- solliciteert → Sollicitatie (*Association*, 1..1 → 0..*, `EAID_D49B7ECE_0089_4d69_970C_8AB585251F66`)
- heeft verlof → Verlof (*Association*, 1..1 → 0..*, `EAID_A4816678_4407_46e7_B5EC_2FEAB323A83A`)
- heeft verzuim → Verzuim (*Association*, 1..1 → 0..*, `EAID_7702C4F6_A0C5_44d0_9857_96B1F62FD27F`)
- → Medewerker (*Generalization*,  → , `EAID_DC562D5C_370F_4e49_9D81_1454BD5D73BB`)
- personeelsdossier → Document (*Usage*,  → , `EAID_1C8FDDB2_7138_41c4_B087_937A036EDB3E`)
