---
id: verkiezingen-gerelateerde-diensten
type: bedrijfsfunctie
archimate_type: business-function
status: goedgekeurd
naam: Verkiezingen gerelateerde diensten
onderwerpen:
- burgerzaken
definitie: Het lokaal organiseren van verkiezingen.
match:
  gemma: exact
domein: Publieksdiensten
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2026-rvig-hup-kiesrecht
- 2025-vng-upl-producten-en-diensten-extern
gemma_id: id-78bbc144-8a22-43a4-8233-c4cfaf7b73c2
gemma_naam: Verkiezingen gerelateerde diensten
gemma_type: business-function
gemma_definitie: Het lokaal organiseren van verkiezingen
gemma_map: Business / Bedrijfsfuncties / Sub(sub)bedrijfsfuncties
gemma_eigenschappen:
  Object ID: 78bbc144-8a22-43a4-8233-c4cfaf7b73c2
  Toelichting: Bijv. het inrichten van stemlokalen en verstrekken van stempassen
---

# Verkiezingen gerelateerde diensten

<!-- Gegenereerd door tools/render.py uit de beoordeling verkiezingen-gerelateerde-diensten.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het lokaal organiseren van verkiezingen.

### Beschrijving

GEMMA noemt als voorbeeld het inrichten van stemlokalen en het verstrekken van stempassen (GEMMA, toelichting bij de functie).

### Per onderwerp

#### [Burgerzaken](../../../../onderwerpen/burgerzaken/begrippen.md)

Van deze functie valt alleen de gemeentelijke taak voor de kiezer in dit onderwerp: ze bedient Beheren stempassen en Registreren kiesgerechtigdheid en omvat de diensten Stempas ontvangen, Kiezerspas, Volmachtbewijs verkiezingen en Stemrecht (UPL nr. 397, 208, 453, 398). De organisatie van de verkiezing zelf (kandidaatstelling, stembureaus, stemming, uitslag) valt erbuiten (afbakening Burgerzaken).

### Naamkeuze

De naam is de GEMMA-naam, met de GEMMA-definitie. Het signaal dat de naam een proces lijkt, is hier een vals alarm: Verkiezingen is een meervoudig zelfstandig naamwoord, geen werkwoord, en de naam is een zelfstandig naamwoord voor het gebied van gedrag.

## Plaats in het model

### Typering

Bedrijfsfunctie. Uitkomst van de beslistabel: Gedrag, *gegroepeerd gedrag* (4 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Producten- en dienstenrealisatie publieksdiensten* (geen element van de wiki; Publieksdiensten › Uitvoering Publieksdiensten › Producten- en dienstenrealisatie publieksdiensten), GEMMA-relatie `id-8fba2af8-119c-4bdd-b3eb-a0f18303b0ff`.
- **Functie-indeling naar domein, omvat**: [Kiezerspas](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md), [Stempas ontvangen](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md), [Stemrecht](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md), [Volmachtbewijs verkiezingen](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md).
- **Bedient**: [Beheren stempassen](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md), [Registreren kiesgerechtigdheid](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md).
- **Domein**: Publieksdiensten.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: gegroepeerd gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) |
| **bedient gedrag**: Ondersteunt de functie aanwijsbaar een proces? | Ja, met [Beheren stempassen](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md), [Registreren kiesgerechtigdheid](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md). [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, registreert en beëindigt de stempas en werkt de kiesrechtgegevens van de ingeschreven persoon bij (Kieswet art. J 7, J 7a; HUP Kiesrecht). [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) |
| **in functie-indeling**: Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of op domeinniveau onder het domein? | Ja, onder Producten- en dienstenrealisatie publieksdiensten (GEMMA). [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) (GEMMA id-8fba2af8-119c-4bdd-b3eb-a0f18303b0ff) |
| **stabiel over tijd**: Blijft het bestaan als de organisatie, de werkwijze of de systemen veranderen, en is het geen opgave met een einde? | Ja, standaard. [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verkiezingen gerelateerde diensten | bedient *bediening* | [Beheren stempassen](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (Kieswet art. J 7) |
| Verkiezingen gerelateerde diensten | bedient *bediening* | [Registreren kiesgerechtigdheid](../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (Kieswet art. D 1) |
| Verkiezingen gerelateerde diensten | omvat *aggregatie* | [Stempas ontvangen](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 397 (GEMMA-domein Publieksdiensten)) |
| Verkiezingen gerelateerde diensten | omvat *aggregatie* | [Kiezerspas](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 208 (GEMMA-domein Publieksdiensten)) |
| Verkiezingen gerelateerde diensten | omvat *aggregatie* | [Volmachtbewijs verkiezingen](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 453 (GEMMA-domein Publieksdiensten)) |
| Verkiezingen gerelateerde diensten | omvat *aggregatie* | [Stemrecht](../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 398 (GEMMA-domein Publieksdiensten)) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [HUP Kiesrecht](../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) | HUP BRP: Kiesrecht |
| [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Verkiezingen gerelateerde diensten* (business-function). Zelfde begrip en zelfde definitie: de GEMMA-bedrijfsfunctie Verkiezingen gerelateerde diensten. De wiki modelleert alleen het deel voor de kiezer; de functie zelf blijft ongewijzigd.

> Het lokaal organiseren van verkiezingen
