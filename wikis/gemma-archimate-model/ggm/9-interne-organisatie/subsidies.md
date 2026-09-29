<!-- gegenereerd door tools/ggm.py; hash: 212a4d3055c2f84a57afc4747c0495e1a4395b8fcdd4f82bb5763c78fbbb98ab -->
# Subsidies

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Betaalmoment | `EAID_E403A215_A367_4eef_8716_075AF54388D0` | Moment waarop er een bepaald deel van de subsidie betaald moet worden. | bedrag, datum, voorschot |
| Rapportagemoment | `EAID_20CA8283_CE99_455c_BF4D_EAE3DF41AE5B` | Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd | datum, naam, omschrijving, termijn |
| Sector | `EAID_DA4F9850_4CA0_4508_9D57_F631BC30B360` | Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid. | naam, omschrijving |
| Subsidie | `EAID_FD701A55_6865_44aa_9A73_C46E02481796` | Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten | niveau, deadlineIndiening, subsidiebedrag, coFinanciering, opmerkingen, status, accountantscontrole, datumStart, datumEinde, datumVerzendingEindeafrekening, gerealiseerdeProjectkosten, hoogteSubsidie, datumBehandeltermijn, datumSubsidievaststelling, subsidievaststellingBedrag, ontvangenBedrag, datumBewaartermijn, onderwerp, subsidiesoort, socialReturnVerplichting, socialReturnNagekomen, socialReturnBedrag, verantwoordenOp, uitgaandeSubsidie, prestatiesubsidie, doelstelling, opmerkingenVoorschotten |
| Subsidieaanvraag | `EAID_26C0D33A_B15A_4256_A5BF_5382A4E03539` | Aanvraag voor een subsidie | datumIndiening, aangevraagdBedrag, ontvangstbevestiging, verwachteBeschikking, kenmerk |
| Subsidiebeschikking | `EAID_F8BD6D83_D3F8_4dd3_B12E_22A991D1A0A2` | Besluit over het al dan niet toekennen van een subsidie | beschiktBedrag, ontvangen, kenmerk, internKenmerk, opmerkingen, besluit, beschikkingsnummer |
| Subsidiecomponent | `EAID_DB093A73_BE89_462b_8FBA_19B2629072ED` | Onderdeel van een subisidie met een eigen kostenplaats. | toegekendBedrag, gereserveerdBedrag |
| Subsidieprogramma | `EAID_8F1A719D_C89A_4194_8FF4_1F3E0F174D3D` | Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang | naam, omschrijving, datumStart, datumEinde, programmabegroting |
| Taak | `EAID_156C82B1_2641_40c8_9E99_60031643C29A` | Een samenhangende set activiteiten in het kader van een subsidie. | datumStart, datumEinde, termijn, taakomschrijving |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Rapportagemoment | Association | heeft | Document | 0..1 → 0..* | `EAID_42130460_011F_4022_A09E_5F4EA114151E` |  |
| Subsidie | Association | behandelaar | Medewerker | 0..* → 0..1 | `EAID_252FE487_E02D_428a_B92C_449A4AA49FCF` |  |
| Subsidie | Association | verstrekker | Rechtspersoon | 0..* → 0..1 | `EAID_797A10EE_8097_4c6c_9BD9_FEECB4DEE86C` |  |
| Subsidie | Association | heeft | Rapportagemoment | 1 → 0..* | `EAID_8FD88F5F_A73E_4e67_A11A_D06E0AE70055` |  |
| Subsidie | Association | heeft | Taak | 1 → 0..* | `EAID_98895123_3432_4228_916D_276992A55D90` |  |
| Subsidie | Association | heeft | Kostenplaats | 0..* → 0..1 | `EAID_B1B2D83D_5165_43df_9248_9A0DCB724A53` |  |
| Subsidie | Association | valt binnen | Sector | 0..* → 0..1 | `EAID_CE46B10D_4FE2_495c_AAA4_6DA8D72633DC` |  |
| Subsidie | Association | heeft | Document | 0..* → 0..1 | `EAID_F16D79F6_7D75_4c83_89DA_A23B7A8C2D49` |  |
| Subsidie | Association | heeft | Zaak | 0..1 → 0..1 | `EAID_FD3717BB_474D_4f8f_98CB_329751FA5CBD` |  |
| Subsidieaanvraag | Association | betreft | Subsidie | 1 → 1 | `EAID_09E8842D_14B1_4275_A63F_92A4AA214791` |  |
| Subsidieaanvraag | Association | mondt uit | Subsidiebeschikking | 1 → 0..1 | `EAID_3A80E369_1CB1_413e_B9E7_CC54A4EAAFE6` |  |
| Subsidiebeschikking | Association | betreft | Subsidie | 0..1 → 1 | `EAID_4DE143AC_298B_4ebd_BAA9_A19FCD1E9907` |  |
| Subsidiecomponent | Association | heeft | Betaalmoment | 1 → 1..* | `EAID_42A182B6_9541_4283_BA4F_E672ADC03C9D` |  |
| Subsidiecomponent | Association | heeft | Kostenplaats | 0..* → 1 | `EAID_ABE367A4_534E_48b9_9240_627972C6AF1B` |  |
| Subsidieprogramma | Association | verantwoordelijk voor | OrganisatorischeEenheid | 0..* → 1 | `EAID_01CEEBB3_B2BF_464b_9CB6_A92E0F454D7E` |  |
| Subsidieprogramma | Association | gaat over | Subsidie | 0..1 → 1..* | `EAID_F25E2F97_F385_4f6f_9D5F_9BE78A352254` |  |
| Taak | Association | projectleider | Rechtspersoon | 0..* → 0..1 | `EAID_2CDDCD51_E333_4b1a_9030_54231ACDC6C5` |  |
