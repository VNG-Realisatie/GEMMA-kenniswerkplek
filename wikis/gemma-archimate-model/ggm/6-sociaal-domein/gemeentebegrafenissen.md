<!-- gegenereerd door tools/ggm.py; hash: 7fca4932a69fa420ee9e5eb43fd6faa33b918e720e2e7321f1ef3a38e6c38238 -->
# Gemeentebegrafenissen

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Gemeentebegrafenis | `EAID_F2DBE01F_7535_4f26_9DF2_081EF8632F36` | Teraardebestelling onder verantwoordelijjkheid van de gemeente. | melder, begrafeniskosten, gemeentelijkeKosten, verhaaldBedrag, datumBegrafenis, datumAfgedaan, datumGemeld, inkoopordernummer, doodsoorzaak, achtergrondMelding, urenGemeente, datumRuimingGraf |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Gemeentebegrafenis | Association | heeft | NatuurlijkPersoon | 0..1 → 1..1 | `EAID_1A5D69CD_5B2F_4164_8535_0652847B151E` |  |
