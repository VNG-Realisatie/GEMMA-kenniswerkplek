<!-- gegenereerd door tools/ggm.py; hash: 85d902d23b5bf5dab55b8075ebfde38132fd640668b37404f56a80ddf7f60a4c -->
# Subsidies

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

## Betaalmoment

Moment waarop er een bepaald deel van de subsidie betaald moet worden.

Attributen: bedrag, datum, voorschot.

GUID: `EAID_E403A215_A367_4eef_8716_075AF54388D0`

## Rapportagemoment

Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd

Attributen: datum, naam, omschrijving, termijn.

GUID: `EAID_20CA8283_CE99_455c_BF4D_EAE3DF41AE5B`

Relaties:

- heeft → Document (*Association*, 0..1 → 0..*, `EAID_42130460_011F_4022_A09E_5F4EA114151E`)

## Sector

Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid.

Attributen: naam, omschrijving.

GUID: `EAID_DA4F9850_4CA0_4508_9D57_F631BC30B360`

## Subsidie

Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten

Attributen: niveau, deadlineIndiening, subsidiebedrag, coFinanciering, opmerkingen, status, accountantscontrole, datumStart, datumEinde, datumVerzendingEindeafrekening, gerealiseerdeProjectkosten, hoogteSubsidie, datumBehandeltermijn, datumSubsidievaststelling, subsidievaststellingBedrag, ontvangenBedrag, datumBewaartermijn, onderwerp, subsidiesoort, socialReturnVerplichting, socialReturnNagekomen, socialReturnBedrag, verantwoordenOp, uitgaandeSubsidie, prestatiesubsidie, doelstelling, opmerkingenVoorschotten.

GUID: `EAID_FD701A55_6865_44aa_9A73_C46E02481796`

Relaties:

- heeft → Document (*Association*, 0..* → 0..1, `EAID_F16D79F6_7D75_4c83_89DA_A23B7A8C2D49`)
- heeft → Kostenplaats (*Association*, 0..* → 0..1, `EAID_B1B2D83D_5165_43df_9248_9A0DCB724A53`)
- behandelaar → Medewerker (*Association*, 0..* → 0..1, `EAID_252FE487_E02D_428a_B92C_449A4AA49FCF`)
- heeft → Rapportagemoment (*Association*, 1 → 0..*, `EAID_8FD88F5F_A73E_4e67_A11A_D06E0AE70055`)
- verstrekker → Rechtspersoon (*Association*, 0..* → 0..1, `EAID_797A10EE_8097_4c6c_9BD9_FEECB4DEE86C`)
- valt binnen → Sector (*Association*, 0..* → 0..1, `EAID_CE46B10D_4FE2_495c_AAA4_6DA8D72633DC`)
- heeft → Taak (*Association*, 1 → 0..*, `EAID_98895123_3432_4228_916D_276992A55D90`)
- heeft → Zaak (*Association*, 0..1 → 0..1, `EAID_FD3717BB_474D_4f8f_98CB_329751FA5CBD`)

## Subsidieaanvraag

Aanvraag voor een subsidie

Attributen: datumIndiening, aangevraagdBedrag, ontvangstbevestiging, verwachteBeschikking, kenmerk.

GUID: `EAID_26C0D33A_B15A_4256_A5BF_5382A4E03539`

Relaties:

- betreft → Subsidie (*Association*, 1 → 1, `EAID_09E8842D_14B1_4275_A63F_92A4AA214791`)
- mondt uit → Subsidiebeschikking (*Association*, 1 → 0..1, `EAID_3A80E369_1CB1_413e_B9E7_CC54A4EAAFE6`)

## Subsidiebeschikking

Besluit over het al dan niet toekennen van een subsidie

Attributen: beschiktBedrag, ontvangen, kenmerk, internKenmerk, opmerkingen, besluit, beschikkingsnummer.

GUID: `EAID_F8BD6D83_D3F8_4dd3_B12E_22A991D1A0A2`

Relaties:

- betreft → Subsidie (*Association*, 0..1 → 1, `EAID_4DE143AC_298B_4ebd_BAA9_A19FCD1E9907`)

## Subsidiecomponent

Onderdeel van een subisidie met een eigen kostenplaats.

Attributen: toegekendBedrag, gereserveerdBedrag.

GUID: `EAID_DB093A73_BE89_462b_8FBA_19B2629072ED`

Relaties:

- heeft → Betaalmoment (*Association*, 1 → 1..*, `EAID_42A182B6_9541_4283_BA4F_E672ADC03C9D`)
- heeft → Kostenplaats (*Association*, 0..* → 1, `EAID_ABE367A4_534E_48b9_9240_627972C6AF1B`)

## Subsidieprogramma

Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang

Attributen: naam, omschrijving, datumStart, datumEinde, programmabegroting.

GUID: `EAID_8F1A719D_C89A_4194_8FF4_1F3E0F174D3D`

Relaties:

- verantwoordelijk voor → OrganisatorischeEenheid (*Association*, 0..* → 1, `EAID_01CEEBB3_B2BF_464b_9CB6_A92E0F454D7E`)
- gaat over → Subsidie (*Association*, 0..1 → 1..*, `EAID_F25E2F97_F385_4f6f_9D5F_9BE78A352254`)

## Taak

Een samenhangende set activiteiten in het kader van een subsidie.

Attributen: datumStart, datumEinde, termijn, taakomschrijving.

GUID: `EAID_156C82B1_2641_40c8_9E99_60031643C29A`

Relaties:

- projectleider → Rechtspersoon (*Association*, 0..* → 0..1, `EAID_2CDDCD51_E333_4b1a_9030_54231ACDC6C5`)
