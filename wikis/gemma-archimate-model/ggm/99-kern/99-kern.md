<!-- gegenereerd door tools/ggm.py; hash: 35a7719228edb90f44a727782b6768be880e68294e927c6d6f65cbad928400d4 -->
# 99 Kern

Taakveld: 99 Kern. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Foto | `EAID_7FE4B466_B051_4068_9ED1_6E60C3B2DBAD` | Afbeelding op een plat vlak vervaardigd door middel van fotografie | bestandsnaam, bestandstype, datumtijd, bestandsgrootte, pixelsX, pixelsY, locatie |
| Gebied | `EAID_0303A7A4_EF51_4262_AEE0_642FA5064807` | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | gebiedsAanduiding |
| Gebiedengroep | `EAID_85E3996B_578D_4313_B078_2773F98412D9` | Verzameling van gebieden |  |
| Lijn | `EAID_FAB83AD1_DC8C_4f78_B54F_33466EB9B139` | Denkbeeldige streep op de aardoppervlakte | lijnLocatie |
| Lijnengroep | `EAID_CD06432A_B69D_4ab2_A5B0_C4C3092835A0` | Verzameling van lijnen |  |
| Locatie | `EAID_79284529_B817_4e3f_BE51_AEAFC60BDE44` | De locatie beschrijft middels co√∂rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) | naam, hoogte, NEN3610ID |
| Periode | `EAID_137DECB4_F249_4039_B4F3_787852C4CB11` | bepaalde tijdsduur. | datumStart, datumEinde, omschrijving |
| Punt | `EAID_20437683_6777_4c7b_B44B_1E3A216239AA` | Plaats in de ruimte | puntLocatie |
| Puntengroep | `EAID_4C0C5DDB_E5BA_42a0_BA5B_65E2D433B16C` | Verzameling van punten |  |
| Video-opname | `EAID_435883D2_C399_4590_B4F5_B07111103484` | Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven. | datumtijd, lengte, videoformaat, bestandsgrootte |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Foto | Association | betreft | Erfgoed Object | 0..* → 0..* | `EAID_C48B4158_EAEB_4853_A5B2_0B8228A162C6` |  |
| Gebied | Generalization |  | Locatie |  →  | `EAID_055869D2_9B49_49d5_BB2A_87FD878FBEEF` |  |
| Gebiedengroep | Association | omvat | Gebied | 0..1 → 1..* | `EAID_D5C41A3E_F7C6_47ce_89E8_55CD70D5B20B` |  |
| Gebiedengroep | Generalization |  | Locatie |  →  | `EAID_9E2921AC_18D5_4701_BCCF_5D7435C5AEEB` |  |
| Lijn | Generalization |  | Locatie |  →  | `EAID_DD9A1AE6_546C_44d9_8890_217CF7DECA25` |  |
| Lijnengroep | Association | omvat | Lijn | 0..1 → 0..* | `EAID_17B63209_082A_486f_8C97_693197D5283D` |  |
| Lijnengroep | Generalization |  | Locatie |  →  | `EAID_103F7AEE_AE14_4696_B25B_02E714FB9F4E` |  |
| Punt | Generalization |  | Locatie |  →  | `EAID_CDCD16ED_13EB_4f40_AC5A_53E2816AC050` |  |
| Puntengroep | Association | omvat | Punt | 0..1 → 1..* | `EAID_15EBE58A_B543_4c88_9A5E_D4A42C45195A` |  |
| Puntengroep | Generalization |  | Locatie |  →  | `EAID_FFC33549_5CC9_42e5_B644_A416BFFCE43B` |  |
| Video-opname | Association | betreft | Erfgoed Object | 0..* → 0..* | `EAID_7F694517_2C91_4a32_84DC_5DC94540E4D3` |  |
| Video-opname | Association | betreft | Agendapunt | 0..1 → 0..* | `EAID_E4F4F868_574E_4ce6_98AB_87B446913522` |  |
