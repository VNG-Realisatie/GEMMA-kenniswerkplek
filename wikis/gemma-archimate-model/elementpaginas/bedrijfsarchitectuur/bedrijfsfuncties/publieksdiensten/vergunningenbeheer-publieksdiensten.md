---
id: vergunningenbeheer-publieksdiensten
type: bedrijfsfunctie
archimate_type: business-function
status: goedgekeurd
naam: Vergunningenbeheer Publieksdiensten
onderwerpen:
- lijkbezorging
definitie: Het beheren en verlenen van vergunningen voor diverse soorten lokale activiteiten.
match:
  gemma: exact
domein: Publieksdiensten
bronnen:
- 2023-vng-model-apv
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2025-vng-upl-producten-en-diensten-extern
gemma_id: id-b7e4786e-cff2-40a8-ac4b-6c48a0abfbe0
gemma_naam: Vergunningenbeheer Publieksdiensten
gemma_type: business-function
gemma_definitie: Het beheren en verlenen van vergunningen voor diverse soorten lokale activiteiten.
gemma_map: Business / Bedrijfsfuncties / Sub(sub)bedrijfsfuncties
gemma_eigenschappen:
  Object ID: b7e4786e-cff2-40a8-ac4b-6c48a0abfbe0
  Toelichting: Bijv. vergunningen voor loterijen, rommelmarkten, collectes, luchtbalonnen, textielinzameling. Andere domeinen waar andere typen vergunningen worden beheerd zijn de domeinen 'Veiligheid' en 'Ruimte'.
---

# Vergunningenbeheer Publieksdiensten

<!-- Gegenereerd door tools/render.py uit de beoordeling vergunningenbeheer-publieksdiensten.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beheren en verlenen van vergunningen voor diverse soorten lokale activiteiten.

### Beschrijving

De gemeente beheert en verleent vergunningen voor lokale activiteiten die inwoners en ondernemers aanvragen, zoals vergunningen op grond van het Burgerlijk Wetboek en de APV.

### Per onderwerp

#### [Lijkbezorging](../../../../onderwerpen/lijkbezorging/begrippen.md)

Wie de uitvaart eerder dan 36 uur of later dan zes werkdagen na het overlijden wil laten plaatsvinden, heeft een vergunning nodig; de burgemeester geeft toestemming (RVO; Wet op de lijkbezorging art. 17).

## Plaats in het model

### Typering

Bedrijfsfunctie. Uitkomst van de beslistabel: Gedrag, *gegroepeerd gedrag* (kern ja, 4/4).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Producten- en dienstenrealisatie publieksdiensten* (geen element van de wiki; Publieksdiensten › Uitvoering Publieksdiensten › Producten- en dienstenrealisatie publieksdiensten), GEMMA-relatie `id-e9c3ffeb-f96c-4bcd-8e74-cf5c866bb1cc`.
- **Functie-indeling naar domein, omvat**: [Bijzondere begraafplaats toestemming](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzondere-begraafplaats-toestemming.md), [Uitvaart vervroegen of uitstellen](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md).
- **Bedient**: [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md).
- **Domein**: Publieksdiensten.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: gegroepeerd gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, de burgemeester beslist over een andere termijn voor begraving of crematie (art. 17). [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, legt de vergunning vast die nabestaanden aanvragen bij de gemeente waar de persoon is overleden (RVO, § Uitvaart vervroegen, § Uitvaart uitstellen). [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **stabiel over tijd**: Blijft deze groepering bestaan als de organisatie of de werkwijze verandert? | Ja, volgt uit wettelijke bevoegdheden zoals die van de burgemeester in art. 17, los van de organisatie. [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **bedient gedrag**: Ondersteunt de functie aanwijsbaar een proces? | Ja, met [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md). |
| **in functie-indeling**: Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? | Ja, onderwerp onder Producten- en dienstenrealisatie publieksdiensten (Uitvoering › Publieksdiensten) in de GEMMA-functie-indeling. (GEMMA id-e9c3ffeb-f96c-4bcd-8e74-cf5c866bb1cc) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. (GEMMA id-e9c3ffeb-f96c-4bcd-8e74-cf5c866bb1cc) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt met dezelfde betekenis voor bij elke vergunning voor een lokale activiteit. Zo in de Model-APV: evenementen (art. 2:25), inzameling van geld of goederen (art. 5:13) en standplaatsen (art. 5:18). [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vergunningenbeheer Publieksdiensten | omvat *aggregatie* | [Uitvaart vervroegen of uitstellen](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md) | [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (§ Uitvaart vervroegen, § Uitvaart uitstellen) |
| Vergunningenbeheer Publieksdiensten | bedient *bediening* | [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| Vergunningenbeheer Publieksdiensten | omvat *aggregatie* | [Bijzondere begraafplaats toestemming](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzondere-begraafplaats-toestemming.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 71 (GEMMA-domein Publieksdiensten)) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md) | Model Algemene plaatselijke verordening per 1 januari 2024 (VNG, november 2023) |
| [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Vergunningenbeheer Publieksdiensten* (business-function). Zelfde begrip en zelfde definitie: de GEMMA-bedrijfsfunctie Vergunningenbeheer Publieksdiensten.

> Het beheren en verlenen van vergunningen voor diverse soorten lokale activiteiten.
