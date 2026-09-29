<!-- gegenereerd door tools/ggm.py; hash: 23a07ba0e17fafc2fc07c0e177a0b7ac9ae5ea06bc1455a8f82221d6f16efb46 -->
# Generiek Jeugd en Wmo

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| AOM_AanvraagWmoJeugd | `EAID_BE7C28C6_0922_4c6a_A953_3D598D991AB5` | *AOM_AanvraagWmoJeugd* is een objecttype in het gegevensmodel voor Wmo en Jeugd dat een **aanvraagtraject voor ondersteuning onder de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert. | clientReactie, datumBeschikking, datumEersteAfspraak, datumPlanVastgesteld, datumStartAanvraag, datumEinde, deskundigheid, doorloopmethodiek, maximaleDoorlooptijd, redenAfsluiting |
| AOMMeldingWmoJeugd | `EAID_0FA25A4F_DF7F_4feb_9460_19D054E874F8` | *AOMMeldingWMOJeugd* is een objecttype in het gemeentelijk gegevensmodel dat een **melding van een situatie of hulpvraag binnen het kader van de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert. | aanmelder, aanmeldingDoor, aanmeldingDoorLandelijk, aanmeldwijze, redenAfsluiting, isClientOpDeHoogte, deskundigheid, vervolg, onderzoekswijze, verwezen |
| Beperking | `EAID_F110608E_9C6A_4d66_BDCB_F4B2465E3CFD` | Een stoornis of conditie ‚ lichamelijk, zintuiglijk en-of geestelijk ‚ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt. | duur, categorie, commentaar, wet |
| Beperkingscategorie | `EAID_4E835898_6623_457f_99B4_C688D465F720` | Een categorisering van beperkingen | code, wet |
| Beperkingscore | `EAID_5EDE0349_8865_4b90_9A18_235C5AA660C4` | Getalsmatige duiding van een beperking | score, commentaar, wet |
| Beperkingscoresoort | `EAID_6B63630A_8A30_454d_B8C4_252D4C30A3BF` | Typering van beperkingscores | vraag, wet |
| Beschikking | `EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836` | In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift. | datumAfgifte, code, grondslagen, commentaar, wet |
| Beschikkingsoort | `EAID_FD14E04F_26A1_42ba_8E47_5F43AF539877` | Typering van een beschikking |  |
| Beschikte Voorziening | `EAID_975C3DA3_930A_49d8_B54F_2A560DC2AD5A` | Een voorziening waarover een beschikking is gedaan. | omvang, eenheid, frequentie, wet, code, datumStart, datumEinde, leveringsvorm, status, redenEinde, datumEindeOorspronkelijk |
| Budgetuitputting | `EAID_679162ED_0B45_4fb2_B16E_421C25A107F5` | Overzicht van de te verwachte inkomsten en uitgaven over een bepaalde periode | datum, uitgenutBedrag |
| Declaratie | `EAID_5E542F35_E413_49c4_8FB7_335B6BE9667A` | Een opgave van te vergoeden kosten. | declaratieBedrag, datumDeclaratie, declaratieStatus |
| Declaratieregel | `EAID_F73F6BFE_9CFE_4497_80E3_CADAA344CF69` | Een *declaratieregel* is de **administratieve regel** waarin het **volume van één product of geleverde prestatie** binnen een bepaalde declaratieperiode voor één cliënt wordt vastgelegd. | code, bedrag, datumStart, datumEinde |
| Leefgebied | `EAID_C55180D9_A5C3_4859_BD88_7686F5384157` | Gebied waarin alle activiteiten van een inwoner zich kunnen afspelen | naam |
| Levering | `EAID_F0CE97B6_3004_4424_A0AA_5034BC0144D1` | Levering van zorg door leverancier. Is in het geval van resultaatverplichting steeds: 1 stuk In PxQ uren maal tarief | eenheid, frequentie, omvang, code, datumStart, datumStop, stopreden |
| Leveringsvorm | `EAID_F35DA519_FA0C_48ae_9EFC_C4EBEC4BF144` | Zorg die onder de Wlz, de Zvw-Wijkverpleging of de Wmo 2015 valt, kan aan personen als zorg in natura (zin) worden geleverd of bekostigd worden uit een persoonsgebonden budget (pgb). | naam, wet, leveringsvormCode |
| Melding Eigen bijdrage | `EAID_A9D093FB_B3D1_46e5_B263_6C4D61F0C5D1` | Aangifte van de evetuele eigen bijdrage | datumStart, datumStop |
| PGB-Toekenning | `EAID_84FE9B56_158D_4b65_BCC1_5FE29D071FCC` | Betreft alleen toegekende voorzieningen met als leveringsvorm PGB Opgebouwd op basis van het TKB (Toekenninsgbericht) aan het SVB, en het BAB-bericht (budgetafsluiting). zie: https://istandaarden.nl/istandaarden/ipgb | datumToekenning, budget, datumEinde |
| Score | `EAID_5A367DA9_DE05_4b3b_954D_24271FD4FB76` | Het aantal behaalde punten | datum |
| Scoresoort | `EAID_653EA248_1547_4f8b_B026_B44FEEC711B2` | Typologie van score | niveau |
| Tarief | `EAID_57F01465_EE56_4c33_9BD9_8DB351A2C530` | Hoogte van een bedrag voor een bepaald product of dient | datumStart, datumEinde, bedrag, wet, eenheid |
| Team | `EAID_909A4134_4697_481e_9110_6386D0F6CAAD` | Een groep personen die door middel van samenwerking een gezamenlijk doel nastreeft, waarbij de teamleden afhankelijk van elkaar zijn om het doel te bereiken. | naam, omschrijving |
| Toewijzing | `EAID_01ECE551_A7B0_4b99_B6E7_F654D6AC15D5` | Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd. zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html | toewijzingnummer, datumToewijzing, datumStartToewijzing, datumEindeToewijzing, redenWijziging, omvang, commentaar, eenheid, frequentie, datumAanschaf, code, wet |
| Verplichting Wmo Jeugd | `EAID_EC0FB9CB_B407_49b4_8FCF_8837E7A72DA9` | *Verplichting Wmo Jeugd* is de wettelijke plicht van gemeenten om inwoners ondersteuning, hulp of zorg te bieden wanneer zij dat nodig hebben op grond van de Wet maatschappelijke ondersteuning (Wmo) en de Jeugdwet. | budgetsoortgroep, Budgetsoort, Feitelijke Einddatum, verplichtingsoort, Periodiciteit, Einddatumgepland, Jaar |
| Verzoek om Toewijzing | `EAID_9F392B0B_1654_4b4e_9261_F0A90DA1F7BD` | Verzoek tot toewijzing dat vanuit leverancier (via H10-portal) aan de gemeente wordt gestuurd. Zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html | referentieAanbieder, beschikkingsnummer, datumIngangBeschikking, datumIngangToewijzing, datumEindeToewijzing, volume, eenheid, frequentie, verwijzer, raamcontract, commentaar, datumOntvangst, soortVerwijzer |
| Voorziening | `EAID_EAAF2F59_6BC0_4243_B126_A8E604B32C5E` | Middel om services/maatregelen in te vullen. | productcode, naam, omschrijving, wet, code, afhandelwijze |
| Voorzieningsoort | `EAID_462E3982_56C3_4442_BE2F_2C23A7ED6015` | Typering van een voorziening | naam, omschrijving, wet, code, productcode, productcategoriecode, productcategorie |
| Zelfredzaamheidmatrix | `EAID_6C27D3D1_FBCE_4504_AF1E_48B4A4CB02EA` | Een geordend systeem waarbij aan elf domeinen van het dagelijks leven (zoals inkomen en dagbesteding; zie figuur) een waarde voor zelfredzaamheid wordt toegekend. | naam, omschrijving, datumStartGeldigheid, datumEindeGeldigheid |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| AOMMeldingWmoJeugd | Association | heeft | Client | 0..* → 1 | `EAID_90F004CE_1EA4_4ba4_A30A_593E8594B53B` |  |
| AOMMeldingWmoJeugd | Generalization |  | AanvraagOfMelding |  →  | `EAID_0CEC8537_F433_4820_9751_314BF07A728F` |  |
| AOM_AanvraagWmoJeugd | Association | heeft | Client | 0..* → 1 | `EAID_16B5C6F2_2668_4586_9717_DAEB205D9712` |  |
| AOM_AanvraagWmoJeugd | Association | leidt_tot | Beschikking | 0..1 → 0..* | `EAID_810BB1B8_B632_4c4c_86B2_51E6D96C0719` |  |
| AOM_AanvraagWmoJeugd | Generalization |  | AanvraagOfMelding |  →  | `EAID_9EEE5F0F_F0F9_4cc2_B73E_7B2DD855E6C5` |  |
| Beperking | Association | is een | Beperkingscategorie | 0..* → 0..1 | `EAID_9E12F959_DACD_493e_B131_B39A1E11F932` |  |
| Beperking | Association | is gebaseerd op | Beschikking | 0..* → 0..1 | `EAID_B351492B_CB3B_40e7_8893_75B45A6AA17F` |  |
| Beperking | Association |  | Beperkingscore | 0..1 → 0..* | `EAID_E5350C4D_69A4_497a_AF09_7E7F03542AC6` |  |
| Beperkingscore | Association | is een | Beperkingscoresoort | 0..* → 0..1 | `EAID_FEC3267E_6981_45d1_95F5_2F3F0BFDADA3` |  |
| Beschikking | Association |  | Client | 0..* → 1 | `EAID_0607E9E7_5520_4f88_A75B_C39FA879B947` |  |
| Beschikking | Association | heeft voorzieningen | Beschikte Voorziening | 1..1 → 1..* | `EAID_2692726B_3EC8_43f0_A1EF_492B29B6AF55` |  |
| Beschikking | Association | toewijzing | Toewijzing | 1 → 0..* | `EAID_3C8D1B70_4F90_4ac7_A839_BE567A7ECCC5` |  |
| Beschikking | Association | betreft | AOMMeldingWmoJeugd | 0..* → 0..* | `EAID_5B5C392C_F0CC_4507_B808_11EE4495DD73` |  |
| Beschikte Voorziening | Association | is voorziening | Voorziening | 0..* → 1..1 | `EAID_21C88910_836E_4469_B652_8359A6183C8C` |  |
| Beschikte Voorziening | Association | Toegewezen Product | Toewijzing | 1..* → 0..1 | `EAID_3B93901B_8280_44f1_8D68_F27250F93A89` |  |
| Beschikte Voorziening | Association | heeft | Leveringsvorm | 0..* → 1..1 | `EAID_650953B3_10A4_4a3e_A10F_D9D839FE0701` |  |
| Declaratie | Association | Ingediend door | Leverancier | 0..* → 1..1 | `EAID_CC023CF5_CF29_43e1_8F6A_F1B4614306D2` |  |
| Declaratieregel | Association | betreft | Client | 0..* → 1..1 | `EAID_D2A64BBB_CF64_4e28_9FF7_5BB5A5122207` |  |
| Declaratieregel | Association | is voor | Beschikking | 0..* → 1..1 | `EAID_E9CC210C_B151_47b6_A5BA_AC4E849EB25E` |  |
| Declaratieregel | Association | valt binnen | Declaratie | 0..* → 1..1 | `EAID_F136689A_92FE_4e0d_973C_2636E57C7825` |  |
| Levering | Association | geleverde prestatie | Beschikking | 0..* → 0..1 | `EAID_1AB8DE4C_D59A_4be0_BB17_4337950922D9` |  |
| Levering | Association | prestatie voor | Client | 0..* → 0..1 | `EAID_49E9E9A9_6284_4b72_A74F_9FC297060B71` |  |
| Levering | Association | geleverde zorg | Toewijzing | 0..* → 0..1 | `EAID_83C1A430_8D5D_484e_8D45_00CD5B692BCB` |  |
| Levering | Association | voorziening | Voorziening | 0..* → 1 | `EAID_986099D4_182A_4e44_8E8E_4975940E3376` |  |
| Melding Eigen bijdrage | Association | betreft | Beschikking | 0..* → 1 | `EAID_068E75CF_3D2D_4964_8957_A322D8902B08` |  |
| PGB-Toekenning | Association | betreft | Budgetuitputting | 1 → 0..* | `EAID_3AEC63D7_A2AC_4b1c_B7FE_9A02050D9D81` |  |
| PGB-Toekenning | Association | betreft | Beschikte Voorziening | 0..* → 1 | `EAID_521168CE_11F7_4535_9176_B3112230C519` |  |
| Score | Association | hoogte score | Scoresoort | 0..* → 1..1 | `EAID_5E95CEAC_D815_4ec4_9D75_A27E0E0FBA3A` |  |
| Score | Association | score bij leeggebied | Leefgebied | 0..* → 1..1 | `EAID_B620036D_4786_442c_B36C_82307BAB6EE5` |  |
| Tarief | Association | heeft | Leverancier | 0..* → 1..1 | `EAID_FA64AD6E_C1D7_467a_8DCA_B830A678F036` |  |
| Toewijzing | Association | levert voorziening | Leverancier | 0..* → 0..1 | `EAID_65B6883C_78DF_48b7_BC4E_C6FDCC1B9E2A` |  |
| Toewijzing | Association | is op basis van | Declaratieregel | 1..1 → 0..* | `EAID_7D705C7A_3508_43e3_B862_6C76A6FC5BA5` |  |
| Verplichting Wmo Jeugd | Association |  | AOM_AanvraagWmoJeugd | 1 → 0..1 | `EAID_486398C8_20C1_48d7_8475_A5BE1C06DB0D` |  |
| Verplichting Wmo Jeugd | Association | heeft | Client | 1 → 0..1 | `EAID_58333E4E_8EE0_430f_9451_1F2C0086D94A` |  |
| Verplichting Wmo Jeugd | Association |  | Beschikte Voorziening | 1 → 0..1 | `EAID_624544D9_080C_43d0_8CE8_2FF792248E35` |  |
| Verplichting Wmo Jeugd | Association | Verplichting aan | Leverancier | 1 → 0..1 | `EAID_AD790AA5_3D88_40c9_9FE7_A7EDDBF66C7E` |  |
| Verplichting Wmo Jeugd | Generalization |  | Inkooporder |  →  | `EAID_64F4A773_5E68_4ae8_8065_4E814C9663A0` |  |
| Verzoek om Toewijzing | Association | betreft | Voorziening | 0..* → 1 | `EAID_05C3C815_25CE_4342_A356_FA5E9120A124` |  |
| Verzoek om Toewijzing | Association | leverancier | Leverancier | 0..* → 1 | `EAID_7A1CE4C1_6A3D_4ddd_88EA_F9FE9398E13F` |  |
| Verzoek om Toewijzing | Association | betreft | Client | 0..* → 1 | `EAID_D2F0539A_1C19_499f_A58B_9EB002936CCB` |  |
| Verzoek om Toewijzing | Association | leidt tot | Beschikking | 0..* → 0..1 | `EAID_EE14C3D4_EB6B_475f_9445_08C464180657` |  |
| Voorziening | Association | valt binnen | Voorzieningsoort | 0..* → 1..1 | `EAID_517568B0_A13C_4f0f_8C5E_6E01CD68358B` |  |
| Voorziening | Association | heeft | Tarief | 1..1 → 1..* | `EAID_A9B9419C_C849_441a_86D8_3AC45CE560D3` |  |
| Zelfredzaamheidmatrix | Association | onderkent scores | Scoresoort | 1..* → 1..* | `EAID_6B0F940E_3386_401a_AC21_169514BAAAB4` |  |
| Zelfredzaamheidmatrix | Association | onderkent leefgebiieden | Leefgebied | 1..* → 1..* | `EAID_CA494862_38C0_4098_8995_1953CABDDBF3` |  |
