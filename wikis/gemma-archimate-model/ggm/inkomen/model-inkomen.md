<!-- gegenereerd door tools/ggm.py; hash: 772f8fa642d576fb6bb9cabca5a6b56baffab7ed7fcf61c203f4f351a666ce32 -->
# Model Inkomen

Taakveld: Inkomen. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Component | `EAID_F4FD02F2_9FFA_4a35_BA32_B4CDE4002E7A` | Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen. | bedrag, begindatumBetrekkingop, eindatumBetrekkingop, debetCredit, rekeningNummer, grootboekcode, grootboekomschrijving, kostenplaats, groep, omschrijving, toelichting, groepcode |
| ComponentSoort | `EAID_3372192D_4773_46b2_BDA5_C98B220F8954` | *ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort. | regelingcode, regeling, kolom, kolomcode, componentcode, omschrijving |
| Huisvestingsoort | `EAID_8D999BE8_96AB_8418_B94F_289754CE1336` | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, soorthuisvestingCode |
| Inkomensvoorziening | `EAID_07784236_3AA6_45e5_8253_7D088C4020B0` | Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving | ingangsdatum, einddatum, toekenningsdatum, bedrag, eenmalig, groep, administratieveEinddatum, administratieveStartdatum, betalingsmomentcode, code, datumToekenning, indicatieBlokkering, indicatieStudietoeslag, indicatieUitkeringSplitsen, indicatieUitkeringsspecificatie, versterkkingsvorm, verwerktTotEnMetDatum |
| Inkomensvoorzieningsoort | `EAID_AF18E7D3_279D_4323_B785_6C75B4701430` | Typering van een inkomensvoorziening | naam, omschrijving, wet, vergoeding, vergoedingscode, regeling, regelingscode, code |
| RedenBlokkering | `EAID_88B0A7AB_53E6_4bc1_8D99_9BE896AB8418` | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenBlokkeringCode |
| RedenInstroom | `EAID_8D999BE8_96AB_8418_99A2_CB86335AFB97` | De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenInstroomCode, CBS-code, CBS-omschrijving |
| RedenUitstroom | `EAID_99A2CB86_335A_FB97_9C8F_47170B1699EC` | De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering beëindigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenUitstroomCode, CBS-code, CBS-omschrijving |
| Regeling | `EAID_C25455F3_FEB0_4c6d_9AA4_3B027718BEE3` | Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert. | startdatum, einddatum, toekenningsdatum, omschrijving |
| Regelingsoort | `EAID_14D3C960_5EF2_433c_8E1C_B493974280E2` | Typologie van een regeling | naam, omschrijving |
| UitkeringsRun | `EAID_F787184D_3AA8_4132_96C4_23A363C3C1B7` | Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking. | datumRun, periodeRun, soortRun, frequentie |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Component | Association | is van soort | ComponentSoort | 1..* → 1..1 | `EAID_0D2A4E08_7DF5_4545_A877_D564CB67BE55` |  |
| Component | Association | heeft | UitkeringsRun | 1..* → 1..1 | `EAID_7A6BF11D_7F34_468f_A1AA_73D96DDD51D3` |  |
| Inkomensvoorziening | Association | redenUitstroom | RedenUitstroom | 1 → 0..* | `EAID_070894C5_A7FF_41c1_9B45_49DB985F037C` |  |
| Inkomensvoorziening | Association | redenInstroom | RedenInstroom | 1 → 1..* | `EAID_124D9BBB_6EDF_4877_892B_FC37C49240C5` |  |
| Inkomensvoorziening | Association | redenBlokkering | RedenBlokkering | 1 → 0..* | `EAID_3929A5E7_EB95_4337_972C_2AF8AD5BB30B` |  |
| Inkomensvoorziening | Association | soortHuisvesting | Huisvestingsoort | 1 → 0..* | `EAID_A4221BE3_623E_4ecc_AAB1_1D5944526B6F` |  |
| Inkomensvoorziening | Association | is opgebouwd uit | Component | 1..1 → 1..* | `EAID_C9BD5B6D_0EF1_49c6_9ABC_82F1C4E9AC06` |  |
| Inkomensvoorzieningsoort | Association | is soort voorziening | Inkomensvoorziening | 1..1 → 0..* | `EAID_CA3F2F05_2D8A_4e33_A4ED_A35C7D2D5B1F` |  |
| Regeling | Association | is regelingsoort | Regelingsoort | 0..* → 1..1 | `EAID_AE5918D8_03E0_4a58_8902_F4FC44321626` |  |
