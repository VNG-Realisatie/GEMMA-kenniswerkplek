<!-- gegenereerd door tools/ggm.py; hash: 732301e56d5292e0318b6d00c9f41c633469d6dc518b3c0298a0b7124badb7c8 -->
# HR

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Beoordeling | `EAID_2A0CC803_9017_4fad_99B5_9347623090F5` | Beoordeling is het oordeel van de professional over het functioneren van een leerling | datum, oordeel, omschrijving |
| Declaratie | `EAID_E611CEB2_F4FA_49e2_AA6B_B380BC1918AC` | Een opgave van te vergoeden kosten. | datumIndiening, datumDeclaratie, betreft, omschrijving, bedrag |
| Declaratiesoort | `EAID_9D4FB9DF_D68A_4503_96C0_272B6777A4FC` | Typering van een declaratie | naam, omschrijving |
| Dienstverband | `EAID_63FF86E2_1BB0_48f6_8D95_3D82E8D2FA06` | De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst. | datumStart, datumEinde, salaris, periodiek, schaal, urenPerWeek |
| Disciplinaire Maatregel | `EAID_50F3F931_38F4_4ff0_8CE4_8A51056767E0` | Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt. | datumGeconstateerd, datumOpgelegd, omschrijving, reden |
| Formatieplaats | `EAID_81EFBDCE_E500_4090_A37A_D3F799517866` | Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar | uren per week |
| Functie | `EAID_F29C11C1_477C_4b90_985C_43F94D08230A` | Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | Naam, Omschrijving, Taken, Schaal, Code |
| Functiehuis | `EAID_D69EE16A_390C_4d6f_BC01_2B13FB3B22F1` | Model waarin functies van een organisatie worden beschreven. | naam, omschrijving |
| GenotenOpleiding | `EAID_261363C5_1E00_4b6a_B570_2129DC044010` | Afgeronde opleiding, een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden | datumStart, datumEinde, datumToewijzing, prijs, verrekenen |
| Geweldsincident | `EAID_41AFF74F_ADBE_4f3f_AB2F_25027A70E573` | Een gebeurtenis met betrekking tot agressie en omvat het veroorzaken van verwondingen of schade bij mensen, dieren, of voorwerpen. | datum, type, omschrijving |
| Individueel Keuzebudget | `EAID_B64178F1_7D37_4a77_BEF7_97E8C9DDA4E8` | Bedrag dat feitelijk beschikbaar gesteld wordt voor een individu om een bepaalde keus te kunnen maken | datumStart, datumEinde, datumToekenning, bedrag |
| Inzet | `EAID_532191CA_13CC_4500_93C9_54AB2862F38D` | Uren inzet die gepleegd wordt in een bepaalde periode op een organisatorische eenheid en het percentage dat ook daadwerkelijk wordt uitgevoerd.Dit kan afwijken van de contractuele uren. | datumBegin, datumEinde, percentage, uren |
| KeuzebudgetBesteding | `EAID_B9288D01_0B8F_4f8c_BAE1_AFD1B0EF6FDF` | De daadwerkelijk uitgave van een keuzebudget | datum, bedrag |
| KeuzebudgetBestedingsoort | `EAID_A0051651_4772_436d_9553_B432BDCE3A52` | Typering van een keuzebudgetbesteding | naam, omschrijving |
| NormProfiel | `EAID_E1C6E98B_20B2_43b0_8EC1_5C0905B3A139` | Normprofiel of Normfunctie:nGenerieke functie zoals beschreven in HR21. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | code, omschrijving, schaal |
| Onderwijsinstituut | `EAID_59F3063A_13A6_4cbc_A387_045A6B126746` | Een instituut waar onderwijs wordt gegeven. |  |
| Opleiding | `EAID_E07D60DE_CD26_4cef_A18B_6F72CC76C1B6` | Een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden. | naam, omschrijving, prijs, instituut |
| OrganisatorischeEenheidHR | `EAID_53B0C49F_1BDE_4fee_BB0B_0D82517177CC` | Specialisatie van de Organisatorische eenheid uit het RGBZ voor het HR domein. | naam, type |
| Relatie | `EAID_FE559B58_A6CD_4108_82BE_98E1AEBFD9BD` | Betrekking waarin personen, zaken, begrippen of grootheden van nature tot elkaar staan. |  |
| Rol | `EAID_BF424764_453D_46cc_817C_3A7BDC4134A7` | De rol van de medewerker, zoals afdelingshoofd of manager | datumBegin, datumEinde, omschrijving |
| Sollicitant | `EAID_131BDD67_2A31_43c5_9125_F12DE2D98D2D` | Persoon die werk zoekt |  |
| Sollicitatie | `EAID_3BD1368C_23F1_4f42_99DB_C81581A646A0` | Verzoek om in een functie te worden aangesteld. | datum |
| Sollicitatiegesprek | `EAID_1D4DA0E6_DA20_4ff7_A415_B937712C6F6D` | Onderhoud tussen sollicitant en werkgever met betrekking tot een sollicatie | datum, opmerkingen, volgendGesprek, aangenomen |
| SoortDisciplinaireMaatregel | `EAID_B0747DFC_DFC8_4ef2_8E1E_C2E8606036FC` | Typering van een disciplinaire maatregel | naam, omschrijving |
| Uren | `EAID_93165DEC_ECB7_4225_9484_E1727524A1B5` | Aantal besteedde uren aan een activiteit | aantal |
| Vacature | `EAID_DC978807_5F36_4148_B816_D6886D026DD8` | Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden. | datumOpengesteld, datumGesloten, intern, extern, deeltijd, vastedienst |
| Verlof | `EAID_D04135BF_C2F0_46dd_B332_F1BE36C358EF` | Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn. | datumtijdStart, datumtijdEinde, goedgekeurd, datumAanvraag, datumToekenning |
| Verlofsoort | `EAID_ED741EE1_E773_40e3_B0E6_8D9886EB792F` | Typering van verlof | naam, omschrijving |
| Verzuim | `EAID_610B18E6_B675_4cc0_A883_BAB9D384C668` | Een afwezigheid van een werknemer van werk. | datumtijdStart, datumtijdEinde |
| Verzuimsoort | `EAID_45900108_585D_45ec_A042_BF4928B7F6DC` | Typologie van verzuim | naam, omschrijving |
| Werknemer | `EAID_BBBB63AC_B546_409b_B6D4_53DB561253B7` | De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst. | naam, voornaam, geboortedatum, woonplaats |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Beoordeling | Usage | vastlegging | Document |  →  | `EAID_FECC6A70_6D99_4103_AC80_81549EEC578A` |  |
| Declaratie | Association | soort declaratie | Declaratiesoort | 0..* → 1..1 | `EAID_53ABD040_F8F1_4d2c_AD7A_9A832A9649E1` |  |
| Dienstverband | Association | onderdeel van | OrganisatorischeEenheidHR | 0..* → 1..* | `EAID_0F596F15_608B_4a1a_ADE6_D1053EF13FF8` |  |
| Dienstverband | Association | dienstverband conform functie | Functie | 0..* → 1 | `EAID_B3C69ADB_9237_4bde_937C_8A9B873AD176` |  |
| Dienstverband | Association | is op vestiging | VestigingVanZaakbehandelendeOrganisatie | 0..* → 0..* | `EAID_DAE508E1_5EDF_4ff6_B108_E83324586885` |  |
| Dienstverband | Usage | arbeidsovereenkomst | Document |  →  | `EAID_BB3D43B2_D0C6_4bd8_98C7_A5DCD4EF7230` |  |
| Disciplinaire Maatregel | Association | soort maatregel | SoortDisciplinaireMaatregel | 0..* → 1..1 | `EAID_48BA20B4_B020_400d_8936_9F8AD9650F3B` |  |
| Formatieplaats | Association | onderdeel van | OrganisatorischeEenheidHR | 1 → 0..1 | `EAID_B12C3E92_BEF7_4859_A882_A37444268D3C` |  |
| Formatieplaats | Association | toegewezen aan | Dienstverband | 0..* → 0..* | `EAID_C886E8C0_39ED_477b_A430_B7577E0A3238` |  |
| Formatieplaats | Association | functie van formatieplaats | Functie | 0..* → 1..* | `EAID_FA8E1AC6_EB2C_4a69_A5B1_7F05B3CE3168` |  |
| Functie | Association | gebaseerd op | NormProfiel | 1 → 1 | `EAID_631F8439_F29C_4a41_A8E3_4C52BBEA69A4` |  |
| GenotenOpleiding | Association | soort opleiding | Opleiding | 0..* → 1..1 | `EAID_B56E335E_B0BB_4876_939E_FD93B18E9768` |  |
| Individueel Keuzebudget | Association | heeft individueel keuzebudget | Werknemer | 0..* → 1..1 | `EAID_AEC374FB_B966_4408_9540_612BDB839919` |  |
| Individueel Keuzebudget | Association | besteding | KeuzebudgetBesteding | 1..1 → 0..* | `EAID_DD7FF2ED_F806_4692_9334_1B5561305B9C` |  |
| Inzet | Association | inzet bij | OrganisatorischeEenheidHR | 0..* → 1 | `EAID_30F12B18_84AE_4b2a_A642_F2CD8D1AA505` |  |
| Inzet | Association | aantal volgens inzet | Dienstverband | 1 → 0..* | `EAID_B365F23E_A00D_4fef_9EE3_A416614B00C6` |  |
| Inzet | Association | inzet voor functie | Functie | 1 → 1 | `EAID_BA44BA34_41E8_4faf_8D8E_7693BCC345B3` |  |
| KeuzebudgetBesteding | Association | soort besteding | KeuzebudgetBestedingsoort | 0..* → 1..1 | `EAID_42E94BB7_BBBE_4cfd_BE12_83932898ADDA` |  |
| NormProfiel | Association | onderdeel van | Functiehuis | 1..* → 1 | `EAID_7BF736B1_C39A_4cd3_8C30_EB2A0FEA2980` |  |
| Onderwijsinstituut | Generalization |  | NietNatuurlijkPersoon |  →  | `EAID_C571BFF8_D84B_481e_8A46_D9706B3AB3D1` |  |
| Opleiding | Association | wordt gegeven door | Onderwijsinstituut | 1..* → 1..* | `EAID_276851B1_EF8E_4e97_ABD2_AAB5A18AC50F` |  |
| OrganisatorischeEenheidHR | Generalization |  | OrganisatorischeEenheid |  →  | `EAID_7995B3F4_9366_472e_96A4_BCFBF6DFB7EB` |  |
| Relatie | Association | is kind van | Werknemer | 0..* → 1 | `EAID_F7CE1157_F7D4_4967_81D0_55F7619A680F` |  |
| Relatie | Generalization |  | NatuurlijkPersoon |  →  | `EAID_B8C56861_C624_4bb4_9DDC_F096ED47139C` |  |
| Rol | Association | hoort bij | OrganisatorischeEenheidHR | 0..* → 0..1 | `EAID_F1F6FACA_0A8D_4904_BA95_CF4984524E7C` |  |
| Sollicitant | Association | solliciteert op functie | Sollicitatie | 1..1 → 0..* | `EAID_7ED83E72_5019_47f5_84BF_5A3DC813EF67` |  |
| Sollicitant | Generalization |  | NatuurlijkPersoon |  →  | `EAID_0051D0C2_0529_422f_9F8F_34BD200A2C9B` |  |
| Sollicitatie | Association | op vacature | Vacature | 0..* → 1..1 | `EAID_69D5B4D8_4D23_4a03_AF7E_9DD4B3B0B439` |  |
| Sollicitatiegesprek | Association | in kader van | Sollicitatie | 0..* → 1..1 | `EAID_34310019_D4F3_4952_97C7_EE9936584868` |  |
| Sollicitatiegesprek | Association | doet sollicitatiegesprek | Werknemer | 0..* → 1..* | `EAID_5E83AD01_AAD7_4d8b_9F09_4180F84BF53B` |  |
| Sollicitatiegesprek | Association | kandidaat | Sollicitant | 0..* → 0..* | `EAID_BED7E9A7_0ECA_4b8b_8EF8_117D8668B970` |  |
| Uren | Association | aantal volgens inzet | Dienstverband | 1..1 → 0..* | `EAID_2F508CBE_E926_4a6d_B85C_401E0BBCDA2F` |  |
| Vacature | Association | vacature bij functie | Functie | 0..* → 1..1 | `EAID_8ACA644F_8D3A_4ab0_B755_24F44D39EEC1` |  |
| Vacature | Usage | vacaturetekst | Document |  →  | `EAID_512E1661_34DE_4e18_9A66_9C4D5B1238D1` |  |
| Verlof | Association | soort verlof | Verlofsoort | 0..* → 1..1 | `EAID_3EDEEC77_46DE_47eb_AD90_10AA60A69F0C` |  |
| Verzuim | Association | soort verzuim | Verzuimsoort | 0..* → 1..1 | `EAID_8B730311_4D6F_4d43_8A5B_8E099B4C421C` |  |
| Werknemer | Association | is partner van | Relatie | 1 → 0..1 | `EAID_04C60911_78B7_4a60_BF69_BF5722278217` |  |
| Werknemer | Association | Beoordeeld door | Beoordeling | 1..1 → 0..* | `EAID_24BF4DCE_5DDC_4c1b_92F0_EFADF4BE03B9` |  |
| Werknemer | Association | heeft | Rol | 1..* → 0..* | `EAID_58514271_87E3_4f5f_A3E4_AF251AA7D9C9` |  |
| Werknemer | Association | beoordeling van | Beoordeling | 1..1 → 0..* | `EAID_6357FC97_EE14_4c30_BCC3_6903DF51DA36` |  |
| Werknemer | Association | heeft maatregel | Disciplinaire Maatregel | 1..1 → 0..* | `EAID_68D387CF_74AA_4219_8B64_52D7FE6A8DC5` |  |
| Werknemer | Association | heeft verzuim | Verzuim | 1..1 → 0..* | `EAID_7702C4F6_A0C5_44d0_9857_96B1F62FD27F` |  |
| Werknemer | Association | dient in | Declaratie | 1..1 → 0..* | `EAID_89425B69_C330_426d_B0E5_9C8C5EF6310E` |  |
| Werknemer | Association | medewerker heeft dienstverband | Dienstverband | 1..1 → 1..* | `EAID_8AB912F9_CF51_4288_85FB_DC19C1E92659` |  |
| Werknemer | Association | heeft ondergaan | Geweldsincident | 0..* → 1..1 | `EAID_8AF83985_ABFC_4a38_95D3_CB368AA680BA` |  |
| Werknemer | Association | heeft verlof | Verlof | 1..1 → 0..* | `EAID_A4816678_4407_46e7_B5EC_2FEAB323A83A` |  |
| Werknemer | Association | heeft genoten | GenotenOpleiding | 1..1 → 0..* | `EAID_C14E8E75_F958_4d73_972F_E0E1FA74400A` |  |
| Werknemer | Association | solliciteert | Sollicitatie | 1..1 → 0..* | `EAID_D49B7ECE_0089_4d69_970C_8AB585251F66` |  |
| Werknemer | Generalization |  | Medewerker |  →  | `EAID_DC562D5C_370F_4e49_9D81_1454BD5D73BB` |  |
| Werknemer | Usage | personeelsdossier | Document |  →  | `EAID_1C8FDDB2_7138_41c4_B087_937A036EDB3E` |  |
