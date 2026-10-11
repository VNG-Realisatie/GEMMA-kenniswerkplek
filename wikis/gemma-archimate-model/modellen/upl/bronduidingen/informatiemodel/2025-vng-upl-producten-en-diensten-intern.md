---
id: 2025-vng-upl-producten-en-diensten-intern
type: bronduiding
model: upl
bronnen:
- 2025-vng-upl-producten-en-diensten-intern
relevant: ja
korte_titel: UPL-lijst intern
bijgewerkt: '2026-10-11'
---

# Uniforme productenlijst sturende en ondersteunende producten en diensten

Bron: [tekst](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-intern.md) · [origineel (xlsx)](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-intern.xlsx) · [omzetting (json)](../../../../../../sources/modellen/2025-vng-upl-producten-en-diensten-intern.json) · [online](https://www.gemmaonline.nl/images/gemma/4/46/Standaard_producten_en_dienstenlijst_intern_basis_UPL.zip)

## Samenvatting

Regelnummers verwijzen naar de tekst van deze bron.

De interne producten- en dienstenlijst van de GEMMA-procesarchitectuur noemt de producten en diensten die een gemeente voor zichzelf levert: sturend (bestuur en beleid) en ondersteunend (bedrijfsvoering). Ze is opgesteld en vastgesteld in de expertgroep GEMMA procesarchitectuur en afgestemd met de UPL (regel 242-244), maar is geen deel van de [UPL van Logius](2026-logius-upl-actueel.md): de namen zijn eigen namen, meestal werkwoordelijk ("213a-onderzoek uitvoeren"), zonder URI. Net als de [lijst extern](2025-vng-upl-producten-en-diensten-extern.md) staat ze op GEMMA Online en is ze toch een bron voor de inhoud, met brontype `informatiemodel`.

Wat de lijst per product geeft (kolomkop, regel 7): een nummer, de naam, een geabstraheerde schrijfwijze, tot twee grondslagen, het type (sturend of ondersteunend), het GEMMA-domein, het SCOPAFIJTH-gebied (security, communicatie, organisatie, personeel, algemene zaken, financiën, informatievoorziening, juridisch, technologie, huisvesting) en of het generiek of specifiek is. De toegestane waarden staan in de toelichtingstabel (regel 227-240). Definities of beschrijvingen staan er niet in.

Voor de wiki is de lijst de tegenhanger van de lijst extern voor het interne aanbod: een product of dienst uit deze lijst is aanbod aan een interne afnemer, en het SCOPAFIJTH-gebied en het GEMMA-domein (Bestuur, Ondersteuning) zijn de ouders in de indelingen. Nog geen onderwerp van de wiki gebruikt de lijst.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| UniformeProduct-dienstnaam | de naam van een intern product of een interne dienst | — | regel 7 |
| Schrijfwijze aanpast/geabstraheerd | een geabstraheerde naam van hetzelfde product | — | regel 7 |
| Type | sturend of ondersteunend | soort product | regel 7, 229-230 |
| GEMMA domeinen | het GEMMA-domein van het product | — | regel 7, 229-235 |
| SCOPAFIJTH | het gebied van de bedrijfsvoering | — | regel 7, 229-240 |
| Generiek/Specifiek | voor alle gemeenten of voor één gemeente | — | regel 7, 229-230 |

## Relaties

Geen relatietabel: de lijst noemt producten en hun grondslag, geen verbanden tussen begrippen.

## Relevantie voor de architectuur

- **Diensten**: bij een onderwerp met sturende of ondersteunende taken (bestuur, bedrijfsvoering) is de lijst de referentie voor het interne aanbod, zoals de lijst extern dat is voor het aanbod aan burgers en bedrijven.
- **Indelingen**: het SCOPAFIJTH-gebied is een indeling van de bedrijfsvoering; of de wiki haar als overgenomen indeling gebruikt, komt aan de orde bij het eerste onderwerp dat de lijst gebruikt.

## Citaten

> Vastgesteld in expergroep GEMMA procesarchitectuur en 1.0 versie van gemaakt (regel 243)
