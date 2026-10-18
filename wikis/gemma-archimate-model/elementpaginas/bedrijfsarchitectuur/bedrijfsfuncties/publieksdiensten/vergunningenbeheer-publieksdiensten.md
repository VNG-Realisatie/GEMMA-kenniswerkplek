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

Bedrijfsfunctie. Uitkomst van de beslistabel: Gedrag, *gegroepeerd gedrag* (4 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Producten- en dienstenrealisatie publieksdiensten* (geen element van de wiki; Publieksdiensten › Uitvoering Publieksdiensten › Producten- en dienstenrealisatie publieksdiensten), GEMMA-relatie `id-e9c3ffeb-f96c-4bcd-8e74-cf5c866bb1cc`.
- **Functie-indeling naar domein, omvat**: [Bijzondere begraafplaats toestemming](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzondere-begraafplaats-toestemming.md), [Uitvaart vervroegen of uitstellen](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md).
- **Realiseert capability**: [Lijkbezorging waarborgen](../../../strategie/capabilities/niet-domeingebonden/lijkbezorging-waarborgen.md).
- **Bedient**: [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md).
- **Domein**: Publieksdiensten.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: gegroepeerd gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **bedient gedrag**: Ondersteunt de functie aanwijsbaar een proces? | Ja, met [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md). [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Vergunning](../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md): Legt de vergunning vast die nabestaanden aanvragen bij de gemeente waar de persoon is overleden (RVO, § Uitvaart vervroegen, § Uitvaart uitstellen). [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **in functie-indeling**: Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? | Ja, met Producten- en dienstenrealisatie publieksdiensten (bedrijfsfunctie, nog geen element): Onderwerp onder Producten- en dienstenrealisatie publieksdiensten (Uitvoering › Publieksdiensten) in de GEMMA-functie-indeling. [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (GEMMA id-e9c3ffeb-f96c-4bcd-8e74-cf5c866bb1cc) |
| **stabiel over tijd**: Blijft het bestaan als de organisatie, de werkwijze of de systemen veranderen, en is het geen opgave met een einde? | Ja, standaard. [Model-APV](../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md), [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vergunningenbeheer Publieksdiensten | omvat *aggregatie* | [Uitvaart vervroegen of uitstellen](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md) | [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (§ Uitvaart vervroegen, § Uitvaart uitstellen) |
| Vergunningenbeheer Publieksdiensten | bedient *bediening* | [Stellen andere termijn](../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| Vergunningenbeheer Publieksdiensten | omvat *aggregatie* | [Bijzondere begraafplaats toestemming](../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzondere-begraafplaats-toestemming.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 71 (GEMMA-domein Publieksdiensten)) |
| Vergunningenbeheer Publieksdiensten | realiseert *realisatie* | [Lijkbezorging waarborgen](../../../strategie/capabilities/niet-domeingebonden/lijkbezorging-waarborgen.md) | [Wet op de lijkbezorging](../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| Vergunningenbeheer Publieksdiensten | legt vast *toegang (registreren)* | [Vergunning](../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md) | [Ondernemersplein Aangifte overlijden](../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (§ Uitvaart vervroegen, § Uitvaart uitstellen) |

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
