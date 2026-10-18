---
id: beheren-stempassen
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Beheren stempassen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verstrekken, vervangen en ongeldig maken van stempassen, kiezerspassen en volmachtbewijzen voor een verkiezing.
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
---

# Beheren stempassen

<!-- Gegenereerd door tools/render.py uit de beoordeling beheren-stempassen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verstrekken, vervangen en ongeldig maken van stempassen, kiezerspassen en volmachtbewijzen voor een verkiezing.

### Beschrijving

Bij elke verkiezing stelt de burgemeester daags na de kandidaatstelling de gegevens vast van de kiezers die op die dag in de gemeente als kiezer zijn geregistreerd en verstrekt hij hun ten minste veertien dagen voor de stemming een stempas (Kieswet art. J 7). Op verzoek reikt hij een vervangende stempas of een kiezerspas uit of verleent hij een volmacht; de stempas waarvoor iets anders in de plaats komt, wordt ongeldig en komt in het register van ongeldige stempassen (art. J 7a, J 8, K 3, K 4, L 8, L 11).

De organisatie van de verkiezing zelf, met de stembureaus, de stemming en de uitslag, valt buiten dit onderwerp (afbakening Burgerzaken). De minister van Binnenlandse Zaken en Koninkrijksrelaties stelt de modellen vast en levert de informatie voor de productie van stempas en kiezerspas (art. J 7 lid 3-4, K 4 lid 4).

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Behandelen verzoek om kiezerspas](behandelen-verzoek-om-kiezerspas.md), [Behandelen verzoek om volmacht](behandelen-verzoek-om-volmacht.md), [Verstrekken stempas](verstrekken-stempas.md).
- **Beleidsdomeinindeling**: beleidsdomein Burgerzaken, taakveld 0 Bestuur en Ondersteuning (van het kernobject).
- **Kernobject**: [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md).
- **Functie-indeling naar domein, bediend door**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **procesniveau**: levensloopproces, kernobject [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | Omvat de levensloop van de stempas: vaststelling, verstrekking, vervanging, omzetting in kiezerspas of volmachtbewijs, ongeldigheid en vernietiging van het register (Kieswet art. J 7, J 7a, J 8, K 4, L 14). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Kiezer](../../../rollen/kiezer.md): Beslisser: de burgemeester beslist op het verzoek om volmacht (Kieswet art. L 11); Kiezer: ontvangt de stempas en doet verzoeken (art. J 8, K 3, L 8). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Kandidaatstelling voor verkiezing (gebeurtenis, nog geen element): De dag van de kandidaatstelling voor een verkiezing (Kieswet art. J 7 lid 1). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Beheren stempassen | verstrekt, vervangt en maakt ongeldig *toegang (registreren)* | [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 7a, J 8) |
| Beheren stempassen | omvat *aggregatie* | [Verstrekken stempas](verstrekken-stempas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 8) |
| Beheren stempassen | omvat *aggregatie* | [Behandelen verzoek om kiezerspas](behandelen-verzoek-om-kiezerspas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 1-K 6) |
| Beheren stempassen | omvat *aggregatie* | [Behandelen verzoek om volmacht](behandelen-verzoek-om-volmacht.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 1-L 15) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Kieswet](../../../../motivatie/beleidskaders/rijksregelgeving/kieswet.md) | is grondslag voor *associatie (gericht)* | Beheren stempassen | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (hoofdstuk J, K, L) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | bedient *bediening* | Beheren stempassen | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (Kieswet art. J 7) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-07: Procesindeling kiesrecht: Stempas is kernobject van Beheren stempassen, met de deelprocessen Verstrekken stempas, Behandelen verzoek om kiezerspas en Behandelen verzoek om volmacht; de registratie van de kiesgerechtigdheid is een deelproces van Bijhouden persoonsgegevens. Geen kunstmatig object Kiezersregistratie. *Zekerheid: logica.*
