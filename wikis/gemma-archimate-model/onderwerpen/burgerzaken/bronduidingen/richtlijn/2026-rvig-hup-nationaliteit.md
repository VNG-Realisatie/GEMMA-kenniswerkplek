---
id: 2026-rvig-hup-nationaliteit
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-nationaliteit
relevant: ja
korte_titel: HUP Nationaliteit
bijgewerkt: 2026-10-06
---

# HUP Nationaliteit (RvIG)

Bron: [tekst](../../../../../sources/raw/2026-rvig-hup-nationaliteit.md) · [origineel (html)](../../../../../sources/raw/2026-rvig-hup-nationaliteit.html) · [online](https://www.rvig.nl/hup/nationaliteit)

## Samenvatting

Overzichtspagina van de HUP over de gegevensgroep nationaliteit in de BRP. Als basisregel heeft elke nationaliteit een eigen stapel, ook staatloosheid en de onbekende nationaliteit; de Nederlandse nationaliteit en het bijzonder Nederlanderschap staan in dezelfde stapel. De pagina onderscheidt de soorten nationaliteit die de BRP kent: Nederlandse, bijzonder Nederlanderschap, vreemde, onbekende en staatloosheid (en geprivilegieerden, buiten deze analyse). De onbekende nationaliteit wordt opgenomen als een nationaliteit vermoed maar niet aangetoond kan worden, ook niet door een mededeling op grond van art. 2.17 Wet BRP. Staatloosheid moet de persoon zelf aantonen; de gemeente hoeft die niet zelf te onderzoeken. Het verlies van het Nederlanderschap laat een nog geldig Nederlands reisdocument van rechtswege vervallen. De stapelregels en codes zijn registratiedetail en vallen buiten het model.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| nationaliteit | gegevensgroep in de BRP; elke nationaliteit heeft een eigen stapel | — | kop Elke nationaliteit een eigen stapel |
| Nederlandse nationaliteit | wordt samen met bijzonder Nederlanderschap in dezelfde stapel opgenomen | Nederlanderschap | kop Elke nationaliteit een eigen stapel |
| bijzonder Nederlanderschap | in dezelfde stapel als de Nederlandse nationaliteit | behandeld als Nederlander | kop Elke nationaliteit een eigen stapel |
| vreemde nationaliteit | elke niet-Nederlandse nationaliteit | — | doorlinkpagina |
| onbekende nationaliteit | een nationaliteit wordt vermoed maar kan niet worden aangetoond of vastgesteld | nationaliteit onbekend of nog niet bekend | kop Nationaliteit onbekend of nog niet bekend |
| staatloosheid | situatie waarin het verkrijgen van een nationaliteit in beginsel niet mogelijk is | staatloos | kop Staatloosheid |
| van rechtswege vervallen reisdocument | een geldig Nederlands reisdocument vervalt als de houder het Nederlanderschap verliest | — | kop Van rechtswege vervallen van een reisdocument |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| persoon die beweert staatloos te zijn | moet aantonen | staatloosheid | kop Staatloosheid |
| gemeente | is niet verplicht te onderzoeken | staatloosheid | kop Staatloosheid |
| gemeente | neemt op | onbekende nationaliteit | kop Nationaliteit onbekend of nog niet bekend |
| reisdocument | vervalt van rechtswege bij | verlies van het Nederlanderschap | kop Van rechtswege vervallen van een reisdocument |

## Relevantie voor de architectuur

- **Bedrijfsobject (applicatielaag):** nationaliteit als gegevensgroep bij de persoon, met de soorten Nederlandse, bijzonder Nederlanderschap, vreemde, onbekende en staatloos. Het onderscheid is een kandidaat-specialisatie.
- **Gebeurtenis:** verlies van het Nederlanderschap, met gevolg voor het reisdocument (onderwerp Reisdocumenten).
- **Buiten scope:** stapels, codes, reden opnemen en beëindigen, correcties.

## Citaten

> Als basisregel geldt dat je bij het opnemen, actualiseren en corrigeren elke nationaliteit een eigen stapel hebt. (kop Elke nationaliteit een eigen stapel)

> Een persoon die beweert staatloos te zijn, moet dat normaal gesproken zelf aantonen door het tonen van brondocumenten. De gemeente is niet verplicht om zelfstandig de staatloosheid te onderzoeken of vast te stellen. (kop Staatloosheid)
