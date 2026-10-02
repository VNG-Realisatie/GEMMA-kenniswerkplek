<!-- gegenereerd door tools/ggm.py; hash: 66cee49056c8ee0f9b360c52f81cf599c82cc3215ad39eb0b252e0b2b32bb6f4 -->
# 10 Dienstverlening

Taakveld: 10 Dienstverlening. Alleen objecttypen; letterlijke definities uit het GGM.

## Aanvraagdata

Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM

Attributen: veld, data.

GUID: `EAID_1F68C981_7E16_4368_8867_CA00AEB08A04`

Relaties:

- is conform → Formuliersoortveld (*Association*, 0..* → 1..1, `EAID_90D3BEFB_53DD_4577_ADC1_43654BC665DD`)

## AanvraagOfMelding

Komt overeen met een VJV Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID

Attributen: afgehandeld, kanaal, soort, datumAfhandeling, categorie, identificatie, onderwerp, status, subcategorie, datumAanmaak, categoriecode, datumBeginStatus, datumEindeStatus, hoofdcategorie, hoofdcategoriecode, onderwerpcode, statuscode, statusVolgorde, subcategoriecode.

GUID: `EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB`

Relaties:

- heeft data → Aanvraagdata (*Association*, 1..1 → 0..*, `EAID_33411F61_D155_49df_9D6B_C945FDA65DF7`)
- heeft → AOMStatus (*Association*, 1..1 → 1..*, `EAID_1BA529A4_6911_43a1_8342_7ADBDD69FBA5`)
- heeft documenten → Document (*Association*, 0..1 → 0..*, `EAID_BE9DCE55_00F0_4742_BAA8_DB992389C5C6`)
- aanvraag met  → Formuliersoort (*Association*, 0..* → 0..1, `EAID_B6781FDB_E6F4_4ecb_B251_A072A105B0F2`)
- ingediend door → Indiener (*Association*, 0..* → 1..1, `EAID_17617172_7EAE_4ad5_AD37_4EE2EE4E1F78`)
- betreft → Onderwerp (*Association*, 0..* → 1..*, `EAID_2762907E_CC1E_49e9_B376_C8F36F3A2EA0`)
- melder → Rechtspersoon (*Association*, 1..* → 0..1, `EAID_D3F7C054_B676_41e3_B470_1FD8BFAFB232`)
- kan leiden tot → Zaak (*Association*, 0..1 → 0..*, `EAID_87F9EA19_0A1D_4c3f_ADCA_C8F48F216312`)

## Afspraakstatus

de toestand van de afspraak

Attributen: status.

GUID: `EAID_5AA9821A_A88A_480b_9950_70FE017593B3`

## Artikel

Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk

GUID: `EAID_F38E71BC_DDA2_4a9c_A438_C486EC4C4646`

## Balieafspraak

Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.

Attributen: starttijdGepland, tijdAangemaakt, toelichting, tijdsduurGepland, wachttijdTotaal, eindtijdGepland, wachttijdVoorStartAfspraak, wachttijdNaStartAfspraak, werkelijkeTijdsduur, notitie.

GUID: `EAID_631FEEF1_88D3_4d18_ADB2_BF999068493E`

Relaties:

- heeft → Afspraakstatus (*Association*, 0..* → 1..1, `EAID_CCA3BF1D_D8A1_4c6d_8FFC_FB82A807A944`)
- mondt uit in → Klantcontact (*Association*, 0..1 → 0..1, `EAID_744D06AC_B194_446e_8B69_DE9DED40C71B`)
- met → Medewerker (*Association*, 0..* → 0..1, `EAID_8E658E97_A6B3_4c06_9C40_20A059C06BBD`)
- betreft → ProductOfDienst (*Association*, 0..* → 0..*, `EAID_DF44DEC9_F13A_4274_AA28_A1A1851B2B01`)
- locatie → VestigingVanZaakbehandelendeOrganisatie (*Association*, 0..* → 0..1, `EAID_EB9B83F5_23DD_4cc8_B65A_EED41272722B`)
- heeft betrekking op → Zaak (*Association*, 0..* → 0..1, `EAID_D1F86572_708B_42f8_B095_789694BB8DCB`)

## ExterneBron

Bron buiten de eigen organisatie

GUID: `EAID_841FC453_80B3_4389_A91F_9498FDC629CF`

## Formuliersoort

Bron: GEM_FORM ID: FORM_ID

Attributen: naam, onderwerp, ingebruik.

GUID: `EAID_0567826D_81EE_4bbd_8D62_3073B74CDF11`

Relaties:

- heeft velden → Formuliersoortveld (*Association*, 1..1 → 0..*, `EAID_FA630ACF_77F6_47a2_93B4_8FB6A9DF9A91`)
- is aanleiding voor → Zaaktype (*Association*, 0..* → 0..*, `EAID_0A5CA34A_9326_497e_ADC3_38787D073F36`)

## Formuliersoortveld

Bron: GEM_VELD ID: FORM_ID en VELD_NAAM

Attributen: veldnaam, veldtype, helptekst, maxLengte, isVerplicht, label.

GUID: `EAID_E512AEFD_85FB_4b57_82FE_709221307861`

## Klantbeoordeling

goed- of afkeurende uitspraak; = mening, opvatting

Attributen: ddBeoordeling, beoordeling, contactOpnemen, categorie, subCategorie, onderwerp, kanaal.

GUID: `EAID_881F95F7_7096_49ab_B1CA_4D9FA93BB4A9`

Relaties:

- heeft → Klantbeoordelingreden (*Association*, 1 → 0..*, `EAID_F56EF6BD_D1C5_48fc_80AC_EF42CD79FCC8`)

## Klantbeoordelingreden

Reden voor de beoordeling

Attributen: reden.

GUID: `EAID_40394EFE_AD3E_4fd9_B9FC_AF73442AF625`

## MOR-AanvraagOfMelding

Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte

Attributen: locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst.

GUID: `EAID_A9B89FF7_BCED_49fc_97A4_2A98BCED5B17`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_868A0305_46EE_4dd7_99D3_35198598C18A`)

## Onderwerp

Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID

Attributen: naam, toelichting, isActief.

GUID: `EAID_8D758F67_6085_4ac7_BFDC_8D97AB632A93`

Relaties:

- hoofdonderwerp → Onderwerp (*Association*, 0..* → 1..1, `EAID_D378AE75_A54F_4dbd_A673_D6DFAF7CAD9F`)

## ProductOfDienst

Bron: QP_CALENDAR.CFM_SERVICES

Attributen: naam, afhandeltijd, ingebruik.

GUID: `EAID_4B871112_CB41_4bfb_BD43_117C63D31BB4`

Relaties:

- heeft → Klantbeoordeling (*Association*, 1..* → 0..*, `EAID_75DA4113_4927_43d1_A910_B2ECE6D51B65`)

## Telefoononderwerp

Onderwerp waarover het telefooncontact gaat

Attributen: onderwerp.

GUID: `EAID_48FE13A9_2204_4631_BAEE_E2D3B10E9A2D`

Relaties:

- heeft → Klantcontact (*Association*, 0..1 → 0..*, `EAID_29BC6916_A8BA_4b0f_A710_D461C86FE7E0`)
- heeft → Telefoontje (*Association*, 0..1 → 0..*, `EAID_E13676F2_69CF_4caa_8667_41E5E65FE315`)

## Telefoonstatus

ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon” DROPPEDCANCELED: “Opgehangen door systeem” ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ” CONNECTEDDIRECT: “Direct verbonden” CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap” AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap” DroppedBusy: “Opgehangen door systeem, te druk” REJECTED: “Geweigerd door systeem” Droppedoverload: “Opgehangen door systeem vanwege overbelasting”

Attributen: contactConnectionState, status.

GUID: `EAID_D8A82A45_03C3_44d5_AF32_3138A55B2E75`

## Telefoontje

De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen.

Attributen: starttijd, eindtijd, totaleTijdsduur, trackID, totaleWachttijd, totaleSpreektijd, totaleOnHoldTijd, afhandeltijdNaGesprek, deltaISDNConnectie.

GUID: `EAID_EEB60E10_C244_4176_AB68_F0E30759269F`

Relaties:

- mondt uit in → Klantcontact (*Association*, 0..1 → 0..*, `EAID_B6963309_6A66_4c0f_A90A_C36C517ED4AC`)
- heeft → Telefoonstatus (*Association*, 0..* → 1..1, `EAID_E471ACCA_15CE_4b2e_83BE_301BF0407150`)
