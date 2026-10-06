---
id: 2026-rvig-hup-bijzonder-nederlanderschap
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-bijzonder-nederlanderschap
relevant: ja
korte_titel: HUP Bijzonder Nederlanderschap
bijgewerkt: 2026-10-06
---

# HUP Bijzonder Nederlanderschap (RvIG)

Bron: [tekst](../../../../sources/raw/2026-rvig-hup-bijzonder-nederlanderschap.md) · [origineel (html)](../../../../sources/raw/2026-rvig-hup-bijzonder-nederlanderschap.html) · [online](https://www.rvig.nl/hup/bijzonder-nederlanderschap)

## Samenvatting

HUP-pagina over twee bijzondere vormen van Nederlanderschap in de BRP: Behandeld als Nederlander (code B) en vastgesteld niet-Nederlander (code V). Het bijzonder Nederlanderschap staat in dezelfde stapel als de Nederlandse nationaliteit en sluit andere actuele nationaliteiten uit: bij opname wordt de registratie van een vreemde of onbekende nationaliteit of van staatloosheid beëindigd. Voor een persoon die als Nederlander wordt behandeld vervallen een verblijfstitel, een reisdocument voor vreemdelingen of vluchtelingen en de aanduiding Europees kiesrecht; bij verlies vervalt een Nederlands reisdocument van rechtswege. Vastgesteld niet-Nederlander ontstaat uit een gerechtelijke procedure. De pagina geeft geen wettelijke grondslag en geen partij die het vaststelt; de registratiecodes en voorbeelden zijn uitvoeringsdetail en vallen buiten het model.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| bijzonder Nederlanderschap | gegevensgroep aanduiding bijzonder Nederlanderschap, in dezelfde stapel als de Nederlandse nationaliteit | — | kop Opnemen behandeld als Nederlander |
| behandeld als Nederlander | een persoon die als Nederlander wordt behandeld; registratie met aanduiding B | bijzonder Nederlanderschap (B) | kop Behandeld als Nederlander |
| vastgesteld niet-Nederlander | in een gerechtelijke procedure vastgesteld dat de persoon geen Nederlander is; aanduiding V | — | kop Opnemen vastgesteld niet-Nederlander |
| verlies bijzonder Nederlanderschap | beëindiging; vreemde of onbekende nationaliteit wordt weer opgenomen | verlies behandeld als Nederlander | kop Beëindiging behandeld als Nederlander |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| gemeente | beëindigt bij opname | registratie van vreemde nationaliteit, onbekende nationaliteit en staatloosheid | kop Behandeld als Nederlander en een andere vreemde nationaliteit |
| gemeente | beëindigt | verblijfstitel bij verkrijging van het bijzonder Nederlanderschap | kop Gevolgen voor andere categorieën |
| gemeente | beëindigt | aanduiding Europees kiesrecht | kop Gevolgen voor andere categorieën |
| verkrijging van bijzonder Nederlanderschap | laat vervallen van rechtswege | reisdocument voor vreemdelingen of vluchtelingen | kop Gevolgen voor andere categorieën |
| verlies van het bijzonder Nederlanderschap | laat vervallen van rechtswege | Nederlands reisdocument | kop Beëindiging behandeld als Nederlander |

## Relevantie voor de architectuur

- **Bedrijfsobject (applicatielaag):** bijzonder Nederlanderschap als specialisatie van nationaliteit (Behandeld als Nederlander, vastgesteld niet-Nederlander).
- **Gebeurtenis:** verkrijging en verlies van het bijzonder Nederlanderschap, met dezelfde gevolgen voor reisdocument en verblijfstitel als bij het Nederlanderschap.
- **Buiten scope:** de registratiecodes, correcties en voorbeelden.

## Citaten

> Als een persoon wordt 'Behandeld als Nederlander', dan wordt dit geregistreerd met behulp van de code 'B' in element 65.10 Aanduiding bijzonder Nederlanderschap. (kop Behandeld als Nederlander)
