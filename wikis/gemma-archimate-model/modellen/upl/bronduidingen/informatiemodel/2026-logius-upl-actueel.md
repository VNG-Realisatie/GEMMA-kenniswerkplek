---
id: 2026-logius-upl-actueel
type: bronduiding
model: upl
bronnen:
- 2026-logius-upl-actueel
- 2026-logius-upl-komt-voor-als
- 2026-logius-upl-thema
- 2026-logius-upl-sdg-informatiegebied
relevant: ja
korte_titel: UPL
bijgewerkt: '2026-10-11'
---

# Uniforme Productnamenlijst (UPL)

Bron: [origineel (csv)](../../../../../../sources/modellen/2026-logius-upl-actueel.csv) · [omzetting (json)](../../../../../../sources/modellen/2026-logius-upl-actueel.json) · [online](https://standaarden.overheid.nl/owms/oquery/UPL-actueel.csv)

## Samenvatting

Een vindplaats noemt de rij in de CSV (de kop is rij 1). Deze bronduiding duidt de lijst zelf en de drie aanvullende tabellen van Logius: [komt voor als](../../../../../../sources/modellen/2026-logius-upl-komt-voor-als.csv), [thema](../../../../../../sources/modellen/2026-logius-upl-thema.csv) en [SDG-informatiegebied](../../../../../../sources/modellen/2026-logius-upl-sdg-informatiegebied.csv). De aangevulde lijsten van GEMMA hebben een eigen bronduiding: [extern](2025-vng-upl-producten-en-diensten-extern.md) en [intern](2025-vng-upl-producten-en-diensten-intern.md).

**Wat de UPL is.** De Uniforme Productnamenlijst van Logius geeft één naam voor elk product of elke dienst van de overheid, zodat productinformatie van verschillende organisaties vindbaar en herbruikbaar wordt. Per naam geeft de lijst wie het levert (Rijk, provincie, waterschap, gemeente), voor wie (burger, bedrijf), of het onder de Dienstenwet of de SDG valt, of het autonomie of medebewind is, de soort (aanvraag, subsidie, melding, verplichting) en de wettelijke grondslag met een link naar de regeling (rij 1). De UPL is de echte bron; de lijsten van GEMMA zijn er een bewerking van.

**Bron én matchdoel.** De UPL is de enige bron die zegt welk aanbod gemeenten hebben, en is daarmee een bron voor de inhoud (brontype `informatiemodel`). Ze is ook een matchdoel: een UPL-product valt nooit weg, en de UPL-naam wordt een synoniem (ARCHITECTURE.md, sectie 2 en 3.4).

**Een UPL-item wordt altijd een dienst.** Wat de UPL noemt, is aanbod van de overheid aan een afnemer: in het model een dienst, met de UPL-naam als synoniem en de URI als vaste verwijzing. De lijst zegt niet wat het item is (er staan geen definities in); de naam, de definitie en de onderbouwing komen uit de bronnen voor de inhoud.

**Diensten met en zonder landelijke grondslag.** Een item met een grondslag in landelijke regelgeving (meestal medebewind, zoals verlof tot begraven op Wlb art. 11, rij 1277) wordt een dienst zoals elk element, met die grondslag. Een item zonder landelijke grondslag (vaak autonomie, met een VNG-model, een verordening of geen grondslag, zoals grafuitgifte op art. 11 van de model-beheersverordening, rij 469) blijft toch in het model: het noemt de grondslag in een VNG-model als die er is, en anders volgt een terugmelding. Zo'n dienst wordt niet uitgewerkt in processen, objecten of rollen, want die verschillen per gemeente (regel Wettelijke grondslag).

**Welke diensten voor gemeenten zijn.** Een item is voor gemeenten als de kolom Gemeente een X heeft; veel items hebben ook andere bestuurslagen (rij 1). Alleen die items komen in het model. De aangevulde lijst extern van GEMMA is afgeleid van de UPL voor gemeenten.

**De aanvullende tabellen.** *Komt voor als* geeft de namen waaronder een item bij organisaties voorkomt; dat zijn kandidaat-synoniemen en een hulp bij het matchen van een gemeentelijke productpagina. *Thema* en *SDG-informatiegebied* ordenen de items; de wiki gebruikt die indelingen nu niet.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| UniformeProductnaam | de uniforme naam van een product of dienst, met een URI | UPL-naam | rij 1, kolom A en B |
| Gemeente | X als het item door gemeenten wordt geleverd; ook Rijk, Provincie, Waterschap | bestuurslaag | rij 1, kolom C-F |
| Burger, Bedrijf | de doelgroep | — | rij 1, kolom G en H |
| Autonomie, Medebewind | of de gemeente het item uit eigen bevoegdheid levert of in uitvoering van hogere regelgeving | — | rij 1, kolom K en L |
| Aanvraag, Subsidie, Melding, Verplichting | de soort item | — | rij 1, kolom M-P |
| Grondslag, Grondslaglabel, Grondslaglink | de grondslag, met label en link naar de regeling; één rij per grondslag | — | rij 1, kolom Q-S |
| KomtVoorAls | een naam waaronder het item bij een organisatie voorkomt | — | komt voor als, rij 1 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| verlof tot begraven | heeft grondslag | Wet op de lijkbezorging art. 11 | rij 1277 |
| grafuitgifte | heeft grondslag | Model Beheersverordening begraafplaatsen art. 11 | rij 469 |
| paspoort | heeft grondslag | Paspoortwet art. 26 | rij 925 |

## Relevantie voor de architectuur

- **Diensten**: elk UPL-item voor gemeenten binnen de afbakening van een onderwerp wordt een dienst, met de UPL-naam als synoniem en de grondslag als relatie *is grondslag voor* vanuit het beleidskader (regel Wettelijke grondslag).
- **Volledigheid**: de UPL voor gemeenten is de lijst van het aanbod; een item dat binnen een onderwerp valt en nog geen dienst is, is een gat.
- **Synoniemen**: de UPL-naam en de namen uit *komt voor als* zijn synoniemen met context "UPL" (regel Naamvorm).
- **Terugmeldingen**: een afwijking van de UPL zelf (een ontbrekend item, een onjuiste grondslag) gaat naar Logius; een afwijking van de aanvulling van GEMMA naar de werkgroep procesarchitectuur.

## Citaten

> verlof tot begraven,…,Artikel 11 Wet op de lijkbezorging (rij 1277)

> grafuitgifte,…,Artikel 11 Model Beheersverordening begraafplaatsen (rij 469)
