<!-- gegenereerd door tools/ggm.py; hash: 697ecaff776e493f27d53d04fa11fa46ef0e12c99e8698ed321e520c2a089dc9 -->
# Mobiliteit

Taakveld: 2 Verkeer, Vervoer en Waterstaat. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Stremming | `EAID_999725EE_737F_410e_906B_9865EBED3597` | Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident | naam, datumStart, datumEinde, datumAanmelding, status, datumWijziging, geschiktVoorPublicatie, delenToegestaan, locatie, hinderklasse, aantalGehinderden |
| Strooidag | `EAID_E2448A6D_3AE0_4884_AD5C_215A9E7166DE` | Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid | datum, minimumtemperatuur, tijdMinimumtemperatuur, maximumtemperatuur, tijdMaximumtemperatuur |
| Strooiroute | `EAID_73090FF8_12FD_471e_80FD_DBFB2FF97D7B` | Traject waarop het strooien plaatsvindt | route |
| StrooirouteUitvoering | `EAID_B825D33A_6DCE_4263_A031_E6E92C4EE86B` | De route die uiteindelijk is gevolgd voor het strooien | route, geplandStart, geplandEinde, werkelijkeStart, werkelijkEinde |
| Verkeersbesluit | `EAID_3F83DAA3_C37F_42b2_8D35_D75B840172F8` | Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. | referentienummer, datumBesluit, datumStart, titel, straat, postcode, huisnummer, datumEinde |
| Verkeerstelling | `EAID_DBE739FD_EBC4_4650_8A2B_714294A63A73` | Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid. | tijdVanaf, tijdTot, aantal |
| VLogInfo | `EAID_E4EEBD4D_A41E_4c9d_8099_CDA45BFF0056` | V-log is een open standaard voor datalogging van een verkeersregelinstallatie. | tijdstip, snelheid, startgroen, eindegroen, verkeerWilGroen, wachttijd, detectieVerkeer |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Stremming | Association | betreft | Wegdeel | 0..* → 0..* | `EAID_57DDEB5B_14C5_427e_AA0F_F730E65A4D0A` |  |
| StrooirouteUitvoering | Association | volgens | Strooiroute | 0..* → 1 | `EAID_5D16A414_E379_4c92_8D49_24D7B0D2BE18` |  |
| StrooirouteUitvoering | Association | uitvoering op | Strooidag | 0..* → 0..1 | `EAID_C5D894AE_7CD9_4d0e_9FCB_306AF2F5A4BA` |  |
| VLogInfo | Association | gegenereerd door | Sensor | 0..* → 0..1 | `EAID_0FDD5ACC_8DFF_4160_B713_ADBE554DAD6B` |  |
| VLogInfo | Association | gegenereerd door | Paal | 0..* → 0..1 | `EAID_AAF78D58_50E2_4312_84C4_882D2B56C890` |  |
| VLogInfo | Association | gegenereerd door | Kast | 0..* → 0..1 | `EAID_EF57AC68_D09C_4941_A675_6A6B3FF10C6C` |  |
| Verkeersbesluit | Association | is vastgelegd in | Document | 1 → 1 | `EAID_343A1C67_34DE_442e_B097_C38C395339B1` |  |
