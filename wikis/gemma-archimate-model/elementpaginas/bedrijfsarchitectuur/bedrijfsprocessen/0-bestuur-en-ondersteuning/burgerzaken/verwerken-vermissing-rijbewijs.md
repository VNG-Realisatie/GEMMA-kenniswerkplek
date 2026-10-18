---
id: verwerken-vermissing-rijbewijs
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken vermissing rijbewijs
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen en vastleggen van de verklaring dat een rijbewijs kwijt of gestolen is, waardoor het rijbewijs ongeldig wordt.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Melding van vermissing van het rijbewijs (wet)
bronnen:
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
---

# Verwerken vermissing rijbewijs

<!-- Gegenereerd door tools/render.py uit de beoordeling verwerken-vermissing-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ontvangen en vastleggen van de verklaring dat een rijbewijs kwijt of gestolen is, waardoor het rijbewijs ongeldig wordt.

### Beschrijving

De houder geeft de vermissing online door aan de RDW met DigiD, waar ze direct wordt geregistreerd, of aan de balie van de gemeente, waar hij de vermissingsverklaring invult bij een nieuwe aanvraag of in een eigen afspraak (Utrecht). Een rijbewijs verliest zijn geldigheid door aangifte van vermissing; wie het terugvindt, levert het in bij degene die het nieuwe rijbewijs afgaf (Wegenverkeerswet 1994 art. 123 lid 1 onder h, 119 lid 4, 120 lid 3).

Bij een vermoeden van misbruik na identiteitsfraude houdt de gemeente het rijbewijs in en vraagt direct een nieuw rijbewijs aan (Utrecht; Wegenverkeerswet 1994 art. 115). Het Reglement rijbewijzen vraagt bij een aanvraag na vermissing een proces-verbaal van een opsporingsambtenaar (art. 39 lid 1), terwijl Utrecht spreekt van een vermissingsverklaring die aan de balie wordt ingevuld; wat formeel geldt, volgt de wet en de verhouding is uit de bronnen niet te halen (verificatie nodig).

### Synoniemen

| Synoniem | Context |
|---|---|
| Melding van vermissing van het rijbewijs | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren rijbewijzen](beheren-rijbewijzen.md).
- **Kernobject**: [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een melding van een gebeurtenis waardoor het rijbewijs ongeldig wordt; de melder krijgt een afspraak voor een nieuw rijbewijs (Utrecht).
- **Gestart door gebeurtenis**: [Vermissing van het rijbewijs](../../../gebeurtenissen/vermissing-van-het-rijbewijs.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |
| **procesniveau**: bedrijfsproces, kernobject [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md) | Ja, van de melding van de vermissing tot de registratie. [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van het rijbewijs](../../../rollen/houder-van-het-rijbewijs.md). [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Vermissing van het rijbewijs](../../../gebeurtenissen/vermissing-van-het-rijbewijs.md). [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken vermissing rijbewijs | registreert vermissing van *toegang (bijwerken)* | [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md) | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |
| Verwerken vermissing rijbewijs | realiseert *realisatie* | [Vermissing of diefstal rijbewijs doorgeven](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/vermissing-of-diefstal-rijbewijs-doorgeven.md) | [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (Utrecht regel 134-140) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren rijbewijzen](beheren-rijbewijzen.md) | omvat *aggregatie* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Reglement art. 39; Utrecht regel 126-140) |
| [Houder van het rijbewijs](../../../rollen/houder-van-het-rijbewijs.md) | geeft vermissing door *toewijzing* | Verwerken vermissing rijbewijs | [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (Utrecht regel 126-140) |
| [Reglement rijbewijzen](../../../../motivatie/beleidskaders/rijksregelgeving/reglement-rijbewijzen.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing rijbewijs | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 39) |
| [Vermissing van het rijbewijs](../../../gebeurtenissen/vermissing-van-het-rijbewijs.md) | leidt tot *triggering* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |
| [Wegenverkeerswet 1994](../../../../motivatie/beleidskaders/rijksregelgeving/wegenverkeerswet-1994.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 123 lid 1 onder h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |
| [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) | Reglement rijbewijzen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA. Het specialiseert het generieke proces Behandelen aangifte of melding.
