<!-- gegenereerd door tools/ggm.py; hash: 46f891c62151a1301dc6764fcd3a10f5c11606fdf91259e0cd325a5984e7577f -->
# 10 Dienstverlening

Taakveld: 10 Dienstverlening. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Aanvraagdata | `EAID_1F68C981_7E16_4368_8867_CA00AEB08A04` | Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM | veld, data |
| AanvraagOfMelding | `EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB` | Komt overeen met een VJV Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID | afgehandeld, kanaal, soort, datumAfhandeling, categorie, identificatie, onderwerp, status, subcategorie, datumAanmaak, categoriecode, datumBeginStatus, datumEindeStatus, hoofdcategorie, hoofdcategoriecode, onderwerpcode, statuscode, statusVolgorde, subcategoriecode |
| Afspraakstatus | `EAID_5AA9821A_A88A_480b_9950_70FE017593B3` | de toestand van de afspraak | status |
| Artikel | `EAID_F38E71BC_DDA2_4a9c_A438_C486EC4C4646` | Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk |  |
| Balieafspraak | `EAID_631FEEF1_88D3_4d18_ADB2_BF999068493E` | Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. | starttijdGepland, tijdAangemaakt, toelichting, tijdsduurGepland, wachttijdTotaal, eindtijdGepland, wachttijdVoorStartAfspraak, wachttijdNaStartAfspraak, werkelijkeTijdsduur, notitie |
| ExterneBron | `EAID_841FC453_80B3_4389_A91F_9498FDC629CF` | Bron buiten de eigen organisatie |  |
| Formuliersoort | `EAID_0567826D_81EE_4bbd_8D62_3073B74CDF11` | Bron: GEM_FORM ID: FORM_ID | naam, onderwerp, ingebruik |
| Formuliersoortveld | `EAID_E512AEFD_85FB_4b57_82FE_709221307861` | Bron: GEM_VELD ID: FORM_ID en VELD_NAAM | veldnaam, veldtype, helptekst, maxLengte, isVerplicht, label |
| Klantbeoordeling | `EAID_881F95F7_7096_49ab_B1CA_4D9FA93BB4A9` | goed- of afkeurende uitspraak; = mening, opvatting | ddBeoordeling, beoordeling, contactOpnemen, categorie, subCategorie, onderwerp, kanaal |
| Klantbeoordelingreden | `EAID_40394EFE_AD3E_4fd9_B9FC_AF73442AF625` | Reden voor de beoordeling | reden |
| MOR-AanvraagOfMelding | `EAID_A9B89FF7_BCED_49fc_97A4_2A98BCED5B17` | Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte | locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst |
| Onderwerp | `EAID_8D758F67_6085_4ac7_BFDC_8D97AB632A93` | Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID | naam, toelichting, isActief |
| ProductOfDienst | `EAID_4B871112_CB41_4bfb_BD43_117C63D31BB4` | Bron: QP_CALENDAR.CFM_SERVICES | naam, afhandeltijd, ingebruik |
| Telefoononderwerp | `EAID_48FE13A9_2204_4631_BAEE_E2D3B10E9A2D` | Onderwerp waarover het telefooncontact gaat | onderwerp |
| Telefoonstatus | `EAID_D8A82A45_03C3_44d5_AF32_3138A55B2E75` | ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon” DROPPEDCANCELED: “Opgehangen door systeem” ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ” CONNECTEDDIRECT: “Direct verbonden” CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap” AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap” DroppedBusy: “Opgehangen door systeem, te druk” REJECTED: “Geweigerd door systeem” Droppedoverload: “Opgehangen door systeem vanwege overbelasting” | contactConnectionState, status |
| Telefoontje | `EAID_EEB60E10_C244_4176_AB68_F0E30759269F` | De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen. | starttijd, eindtijd, totaleTijdsduur, trackID, totaleWachttijd, totaleSpreektijd, totaleOnHoldTijd, afhandeltijdNaGesprek, deltaISDNConnectie |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| AanvraagOfMelding | Association | ingediend door | Indiener | 0..* → 1..1 | `EAID_17617172_7EAE_4ad5_AD37_4EE2EE4E1F78` |  |
| AanvraagOfMelding | Association | heeft | AOMStatus | 1..1 → 1..* | `EAID_1BA529A4_6911_43a1_8342_7ADBDD69FBA5` |  |
| AanvraagOfMelding | Association | betreft | Onderwerp | 0..* → 1..* | `EAID_2762907E_CC1E_49e9_B376_C8F36F3A2EA0` |  |
| AanvraagOfMelding | Association | heeft data | Aanvraagdata | 1..1 → 0..* | `EAID_33411F61_D155_49df_9D6B_C945FDA65DF7` |  |
| AanvraagOfMelding | Association | kan leiden tot | Zaak | 0..1 → 0..* | `EAID_87F9EA19_0A1D_4c3f_ADCA_C8F48F216312` |  |
| AanvraagOfMelding | Association | aanvraag met  | Formuliersoort | 0..* → 0..1 | `EAID_B6781FDB_E6F4_4ecb_B251_A072A105B0F2` |  |
| AanvraagOfMelding | Association | heeft documenten | Document | 0..1 → 0..* | `EAID_BE9DCE55_00F0_4742_BAA8_DB992389C5C6` |  |
| AanvraagOfMelding | Association | melder | Rechtspersoon | 1..* → 0..1 | `EAID_D3F7C054_B676_41e3_B470_1FD8BFAFB232` |  |
| Aanvraagdata | Association | is conform | Formuliersoortveld | 0..* → 1..1 | `EAID_90D3BEFB_53DD_4577_ADC1_43654BC665DD` |  |
| Balieafspraak | Association | mondt uit in | Klantcontact | 0..1 → 0..1 | `EAID_744D06AC_B194_446e_8B69_DE9DED40C71B` |  |
| Balieafspraak | Association | met | Medewerker | 0..* → 0..1 | `EAID_8E658E97_A6B3_4c06_9C40_20A059C06BBD` |  |
| Balieafspraak | Association | heeft | Afspraakstatus | 0..* → 1..1 | `EAID_CCA3BF1D_D8A1_4c6d_8FFC_FB82A807A944` |  |
| Balieafspraak | Association | heeft betrekking op | Zaak | 0..* → 0..1 | `EAID_D1F86572_708B_42f8_B095_789694BB8DCB` |  |
| Balieafspraak | Association | betreft | ProductOfDienst | 0..* → 0..* | `EAID_DF44DEC9_F13A_4274_AA28_A1A1851B2B01` |  |
| Balieafspraak | Association | locatie | VestigingVanZaakbehandelendeOrganisatie | 0..* → 0..1 | `EAID_EB9B83F5_23DD_4cc8_B65A_EED41272722B` |  |
| Formuliersoort | Association | is aanleiding voor | Zaaktype | 0..* → 0..* | `EAID_0A5CA34A_9326_497e_ADC3_38787D073F36` |  |
| Formuliersoort | Association | heeft velden | Formuliersoortveld | 1..1 → 0..* | `EAID_FA630ACF_77F6_47a2_93B4_8FB6A9DF9A91` |  |
| Klantbeoordeling | Association | heeft | Klantbeoordelingreden | 1 → 0..* | `EAID_F56EF6BD_D1C5_48fc_80AC_EF42CD79FCC8` |  |
| MOR-AanvraagOfMelding | Generalization |  | AanvraagOfMelding |  →  | `EAID_868A0305_46EE_4dd7_99D3_35198598C18A` |  |
| Onderwerp | Association | hoofdonderwerp | Onderwerp | 0..* → 1..1 | `EAID_D378AE75_A54F_4dbd_A673_D6DFAF7CAD9F` |  |
| ProductOfDienst | Association | heeft | Klantbeoordeling | 1..* → 0..* | `EAID_75DA4113_4927_43d1_A910_B2ECE6D51B65` |  |
| Telefoononderwerp | Association | heeft | Klantcontact | 0..1 → 0..* | `EAID_29BC6916_A8BA_4b0f_A710_D461C86FE7E0` |  |
| Telefoononderwerp | Association | heeft | Telefoontje | 0..1 → 0..* | `EAID_E13676F2_69CF_4caa_8667_41E5E65FE315` |  |
| Telefoontje | Association | mondt uit in | Klantcontact | 0..1 → 0..* | `EAID_B6963309_6A66_4c0f_A90A_C36C517ED4AC` |  |
| Telefoontje | Association | heeft | Telefoonstatus | 0..* → 1..1 | `EAID_E471ACCA_15CE_4b2e_83BE_301BF0407150` |  |
