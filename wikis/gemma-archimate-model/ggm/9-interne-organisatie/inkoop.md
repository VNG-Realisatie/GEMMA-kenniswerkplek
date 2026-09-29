<!-- gegenereerd door tools/ggm.py; hash: 6fabc1078e39e35b838f69a3abff68e53e80634ffd7d0615d87036ad0971d1e8 -->
# Inkoop

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Aanbesteding | `EAID_44EC6082_2682_43c7_A52E_0AD05B06A046` | Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding | naam, tendernedKenmerk, status, datumStart, volgendeSluiting, type, procedure, digitaal, referentienummer, datumPublicatie, scoreMaximaal |
| Aanbesteding Inhuur | `EAID_01D90490_C76A_444a_BFCE_355AFC5FB012` | Aanbesteding voor inhuur van personen of diensten | datumVerzending, status, titel, type, publicatie, perceel, datumSluiting, aanvraagnummer, omschrijving, hoogsteTarief, laagsteTarief, datumOpeningKluis, datumCreatie, referentie, procedure, projectreferentie, projectnaam, aanvraagGesloten, fase |
| Aankondiging | `EAID_BB135B0E_A2C2_4681_BD91_30863F8B3D70` | Aankondiging van een Nationale of Europese aanbesteding | datum, naam, beschrijving, type, categorie |
| Aanvraag Inkooporder | `EAID_33E5EA10_F43A_4966_B9C1_875F0E2C1B52` | het betreft hier het formulier 'Aanvraag Inkooporder' | correspondentienummer, onderwerp, omschrijving, leveringOfDienst, wijzeVanInhuur, inhuurAnders, betalingOverMeerJaren, nettoTotaalBedrag, reactie, status |
| Categorie | `EAID_6CA060D0_C5AC_4b50_8B64_00DCAEA7EF48` | Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren | code, omschrijving |
| Contract | `EAID_9FBF9FB8_B28D_4733_8443_607B8498F446` | Bindende overeenkomst | contractRevisie, internContractID, internContractRevisie, status, groep, type, categorie, classificatie, voorwaarde, beschrijving, zoekwoorden, autorisatiegroep, opmerkingen, datumStart, datumEinde, datumCreatie |
| CPV-code | `EAID_6A4CF470_3B0E_4141_9DB6_C9E8A525CB49` | De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen. | code, omschrijving |
| FormulierInhuur | `EAID_B598FF22_CDD0_486f_B528_99421D0FA608` | Formulier ten behoeve van inhuur personeel | functienaamInhuur, datumIngangInhuur, akkoordHRAdviseur, akkoordFinancieelAdviseur |
| FormulierVerlengingInhuur | `EAID_1D87490A_9F07_424f_BE6F_5E9C11376B05` | Formulier ten behoeve van verlenging inhuur personeel | datumEindeNieuw, indicatieVerhogenInkooporder, indicatieRedenInhuurGewijzigd, toelichting |
| Gunning | `EAID_3FB9B466_D147_42d7_99D1_2D14A007D16C` | Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding Of voor levering personeel | datumGunning, bericht, datumVoorlopigeGunning, gegundePrijs, datumPublicatie |
| Inkooppakket | `EAID_170AF8F5_8952_407a_91C4_EAF910DE3304` | Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd. | code, naam, type |
| Inschrijving | `EAID_2902E8D6_FF16_45d6_A0A4_47E2857D2D19` | Inschrijving op een nationale of Europese aanbesteding | datum, prijs, score |
| Kandidaat | `EAID_75B4E818_5ECD_45c5_98F9_66F57FC6117E` | Iemand die een bepaalde baan of functie wil | datumIngestuurd |
| Kwalificatie | `EAID_AB2AED85_D2B0_45cf_9B1F_C6005E894494` | Kwalifificatie voor een nationale of europese aanbesteding | startGeldigheid, eindeGeldigheid |
| Leverancier | `EAID_EA7FE08E_34F7_45d2_BE2E_E4E3B8333BF3` | Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie | naam, nummer |
| Offerte | `EAID_BF21FFA3_3EA6_410a_BC65_7BE5547646B6` | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. | prijs, datumOfferte, naam, omschrijving |
| Offerteaanvraag | `EAID_1EF1AC66_9563_4cdd_AE78_0878D651907A` | Aanbesteding bij inschrijving | datumAanvraag, datumSluiting, naam, omschrijving |
| SelectietabelAanbesteding | `EAID_B2BD6C5B_460E_4f2a_9B78_3E101DAD8D6B` | Gebaseerd op het procedureoverzicht inkoop. Hierin kan de tabel met drempelbedragen en bijbehorende procedures worden opgeslagen | opdrachtcategorie, drempelbedragVanaf, drempelbedragTot, aanbestedingsoort, openbaar |
| StartformulierAanbesteden | `EAID_7694A657_22D8_4b00_AAE2_A78EF014B43A` | Formulier voor het starten van een aanbeseding | omschrijving, indicatorOverkoepelendProject, opdrachtsoort, opdrachtcategorie, indicatieEenmaligeLos, indicatieMeerjarigRepeterend, indicatieMeerjarigeRaamovereenkomst, toelichtingEenmaligOfRepeterend, indicatieAanvullendeOpdrachtLeverancier, toelichtingAanvullendeOpdracht, beoogdeLooptijd, beoogdeTotaleOpdrachtwaarde, indicatieBeoogdeAanbestedingOnderhands, indicatieBeoogdeProcKomtOvereen |
| Uitnodiging | `EAID_BB182A6F_6935_4702_ABEA_B96E32A40B02` | Een verzoek om iets bij te wonen. | datum, afgewezen, geaccepteerd |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Aanbesteding | Association | procesleider | Medewerker | 0..* → 0..1 | `EAID_083C9CF6_C21B_46b3_A933_1DDAFA9F771F` |  |
| Aanbesteding | Association | betreft | Zaak | 0..1 → 0..1 | `EAID_7E3E1D53_B929_4e16_946E_CFCC35BC2FD9` |  |
| Aanbesteding | Association | mondt uit | Gunning | 0..1 → 0..1 | `EAID_F4336DDB_05D3_439b_ACB5_62B9E010DA8A` |  |
| Aanbesteding | Usage |  | Document |  →  | `EAID_BE356FF7_ABE1_4853_B32E_947B14EC26E1` |  |
| Aanbesteding Inhuur | Association | mondt uit | Gunning | 1 → 0..1 | `EAID_27F22979_C7BD_47b1_B397_FB73EE85054D` |  |
| Aanbesteding Inhuur | Association | valt onder | CPV-code | 0..* → 1 | `EAID_64ABE717_2D93_476f_8084_A98C90BCAAEC` |  |
| Aanbesteding Inhuur | Association | eigenaar | Medewerker | 0..* → 0..1 | `EAID_BE6176A2_C180_4e8e_8CA5_83E21A1A70CC` |  |
| Aanbesteding Inhuur | Association | valt binnen | Categorie | 0..* → 1 | `EAID_FC1D9123_E562_4fe4_9DE1_20ABD602CF8F` |  |
| Aanbesteding Inhuur | Usage |  | Document |  →  | `EAID_E222FE00_25DF_45a1_9EA0_466D53792702` |  |
| Aankondiging | Association | mondt uit | Aanbesteding | 0..* → 0..1 | `EAID_AD975BE9_A0DA_49e6_A0C4_9569996A120F` |  |
| Aanvraag Inkooporder | Association | afhandeling | Zaak | 0..1 → 0..1 | `EAID_4ADD200D_6946_4adb_8500_FBB1F6291E81` |  |
| Aanvraag Inkooporder | Association | betreft | Leverancier | 0..* → 1 | `EAID_58461ED6_0889_4b28_8140_C1C120592AEE` |  |
| Aanvraag Inkooporder | Association | afgehandeld door | OrganisatorischeEenheid | 0..* → 1 | `EAID_6E0A612D_3FC1_4e4e_A882_307582C17A80` |  |
| Aanvraag Inkooporder | Association | betreft | Contract | 0..* → 1 | `EAID_8A886AB2_1EDA_4982_8EAD_4C7AC3A10631` |  |
| Aanvraag Inkooporder | Association | mondt uit in  | Inkooporder | 0..* → 0..1 | `EAID_AD817D28_F4F3_47c6_AB94_EE00A505B132` |  |
| Aanvraag Inkooporder | Association | ingediend bij | Medewerker | 0..* → 1 | `EAID_EBC91C89_CF15_49bc_A3BF_05673D182F65` |  |
| Aanvraag Inkooporder | Usage |  | Document |  →  | `EAID_0EB48345_AE35_4691_B63D_F1814734DCBD` |  |
| CPV-code | Association | valt onder | Aanbesteding | 1 → 0..* | `EAID_FA4F75BB_DBC5_47b3_90F1_0AC75F94E634` |  |
| Contract | Association | bevat | Tarief | 1 → 0..* | `EAID_530BD4D3_FF9D_47d6_BCA7_06BCD10417D1` |  |
| Contract | Association | bovenliggend | Contract | 0..* → 0..1 | `EAID_E09C6849_4665_4bfe_83BA_D220F55E1139` |  |
| Contract | Usage | vastlegging als contract | Document |  →  | `EAID_C645E918_6257_4a72_A084_A3FF0D6F3D59` |  |
| FormulierInhuur | Association | heeft | Kostenplaats | 0..* → 1 | `EAID_1F7EF4DB_E751_47a9_A960_CF2846AF6B3E` |  |
| FormulierInhuur | Association | mondt uit in | Aanbesteding Inhuur | 0..1 → 0..1 | `EAID_90C15984_859B_4665_A898_139D05C730D5` |  |
| FormulierInhuur | Association | aanvrager | Medewerker | 0..* → 1 | `EAID_CD6BDEB3_A2D0_48e6_9AF3_9269C7BAD5AB` |  |
| FormulierInhuur | Usage |  | Document |  →  | `EAID_016A253A_7D21_4e89_88A5_30B317D2DFEF` |  |
| FormulierVerlengingInhuur | Association | aanvrager | Medewerker | 0..* → 1 | `EAID_020F2F9A_BDA8_40a3_8E83_85752A9D1CE7` |  |
| FormulierVerlengingInhuur | Association | betreft | Inkooporder | 0..* → 1 | `EAID_5D27EFEE_7414_4083_B02C_A9F6D5F1D578` |  |
| FormulierVerlengingInhuur | Association | ingehuurd via | Leverancier | 0..* → 1 | `EAID_62481646_A5FD_404a_8716_91401BCA31F5` |  |
| FormulierVerlengingInhuur | Association | betreft | Medewerker | 0..* → 1 | `EAID_DE937028_151F_4bb6_B28A_4C0F5C7155C4` |  |
| FormulierVerlengingInhuur | Usage |  | Document |  →  | `EAID_5EA0C45F_50B0_43bb_9481_B6A2854026FF` |  |
| Gunning | Association | betreft | Inschrijving | 0..1 → 0..1 | `EAID_096607E3_510B_4140_8B76_A4F249EF45D4` |  |
| Gunning | Association | betreft | Kandidaat | 0..1 → 1 | `EAID_2412AD35_118A_4a10_92A6_B4381CC94130` |  |
| Gunning | Association | betreft | Offerte | 0..1 → 0..1 | `EAID_B59891C6_BF26_4dd2_8455_7F84D5AB50E7` |  |
| Gunning | Association | inhuur | Medewerker | 0..* → 0..1 | `EAID_BD37E6F0_5FCB_43c2_A915_1C3F4F2D8CE0` |  |
| Inkooppakket | Association | heeft | CPV-code | 0..* → 1..* | `EAID_EA2C3BC9_E303_4c1f_BF27_F0CBF17570AA` |  |
| Inschrijving | Association | betreft | Aanbesteding | 0..* → 1 | `EAID_DA41126D_D289_40bb_A36D_5625650CBE54` |  |
| Kandidaat | Association | betreft | NatuurlijkPersoon | 0..* → 1 | `EAID_C5DF9BC2_DA59_4e82_942B_E27F2E5E1E3F` |  |
| Kandidaat | Association | ingediend voor | Aanbesteding Inhuur | 0..* → 1 | `EAID_D92FDD25_BBD8_463d_B918_B7340DF94F75` |  |
| Kwalificatie | Association | betreft | Aanbesteding | 0..* → 1 | `EAID_0BBACB1A_E170_478c_9E82_56E273D340A2` |  |
| Leverancier | Association | heeft | Inschrijving | 1 → 0..* | `EAID_044ACFF3_A63F_4745_9BFB_CD7E5CB1A797` |  |
| Leverancier | Association | heeft | Kwalificatie | 1 → 0..* | `EAID_05D2D9C8_7433_4221_9EEF_612ACFFDC656` |  |
| Leverancier | Association | biedt aan | Kandidaat | 1 → 0..* | `EAID_6918E1EE_EC2B_45c6_BC35_693CEB3C30F1` |  |
| Leverancier | Association | heeft gekwalificeerd | Aanbesteding Vastgoed | 0..* → 0..* | `EAID_6BB295DA_4080_4b49_B3EF_07E52AE82C2A` |  |
| Leverancier | Association | gekwalificeerd | Categorie | 0..* → 0..* | `EAID_82CD954D_A9E0_4405_BE91_C15C3F01E6D6` |  |
| Leverancier | Association | contractant | Contract | 1 → 0..* | `EAID_A4596611_218A_45df_8EF8_096FCCD8114A` |  |
| Leverancier | Association | voert werk uit conform | Werkbon | 1..1 → 0..* | `EAID_BE21C646_CB3B_4d16_A3E0_F856269AE2A1` |  |
| Leverancier | Generalization |  | Rechtspersoon |  →  | `EAID_23019C72_EC24_499e_A2EF_58190937DFD5` |  |
| Offerte | Association | ingediend door | Leverancier | 0..* → 1 | `EAID_8E6F2106_48ED_4640_8D57_232E09A4B65F` |  |
| Offerte | Association | betreft | Aanbesteding | 0..* → 1 | `EAID_D42EDBD0_1347_4dbc_9A17_DFA3B4144BD7` |  |
| Offerteaanvraag | Association | betreft | Aanbesteding | 0..* → 1 | `EAID_11E96BA6_1358_47d9_A851_0EDC29AA3E2A` |  |
| Offerteaanvraag | Association | gericht aan | Leverancier | 0..* → 1 | `EAID_6F34B2D2_6257_4faa_87EE_E38F35C9B1A0` |  |
| StartformulierAanbesteden | Association | betreft | Zaak | 0..* → 0..1 | `EAID_03A7ECAA_181B_496d_A6F8_4C06D3F742F3` |  |
| StartformulierAanbesteden | Association | mondt uit | Aankondiging | 0..1 → 0..* | `EAID_B1AE1615_E4CD_4e14_B866_F6DD3F3837E8` |  |
| StartformulierAanbesteden | Association | mondt uit | Aanbesteding | 0..1 → 0..1 | `EAID_CE4355D8_EE82_4ce4_8B5B_7BD4769AA44E` |  |
| Uitnodiging | Association | gericht aan | Leverancier | 0..* → 1 | `EAID_235922D5_16F9_4ecb_A43A_0E2D7BE8D5DC` |  |
| Uitnodiging | Association | betreft | Aanbesteding Inhuur | 0..* → 1 | `EAID_263D659A_945D_42b7_97BB_2B96E51903C1` |  |
