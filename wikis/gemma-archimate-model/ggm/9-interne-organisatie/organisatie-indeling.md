<!-- gegenereerd door tools/ggm.py; hash: 8996aa7b2e23dfe16be528ba3f9ccff83c74204b4bbfc6cf9b240eac802ef803 -->
# Organisatie-indeling

Taakveld: 9 Interne Organisatie. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Programma | `EAID_0E19C86B_9088_41bd_9DD0_15094426570E` | Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te co√∂rdineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie. | naam |
| Project | `EAID_7087D528_7024_4569_876A_C4605A00546D` | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. |  |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Programma | Association | binnen programma | Plan | 0..1 → 0..* | `EAID_60B21789_9C53_450d_80BD_78FED8978AFD` |  |
| Project | Association | heeft | Kostenplaats | 0..* → 0..* | `EAID_B73281DC_36F6_447b_A7F0_EC6A1EC333F3` |  |
