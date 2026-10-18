---
id: behandelen-verklaring-van-afstand
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen verklaring van afstand
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het in ontvangst nemen en bevestigen van een verklaring waarmee een persoon afstand doet van het Nederlanderschap.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Afstand van het Nederlanderschap (wet)
bronnen:
- 2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
---

# Behandelen verklaring van afstand

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verklaring-van-afstand.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het in ontvangst nemen en bevestigen van een verklaring waarmee een persoon afstand doet van het Nederlanderschap.

### Beschrijving

Een meerderjarige met een andere nationaliteit legt de verklaring van afstand af voor de burgemeester; die stelt eerst de identiteit vast en bepaalt welke andere personen, zoals minderjarige kinderen, door de afstand het Nederlanderschap verliezen (Rijkswet op het Nederlanderschap art. 15, 16; Besluit verkrijging en verlies Nederlanderschap art. 63 lid 1-2). Kinderen van 12 tot 16 jaar mogen hun mening geven; vanaf 16 jaar legt een kind zelf een verklaring af (Utrecht).

De persoon ontvangt onverwijld een bevestiging (Besluit art. 63 lid 3). De burgemeester zendt de verklaring en een afschrift van de bevestiging aan de minister en aan de bijhoudingsgemeente, en bevordert dat de afstand in de basisregistratie personen wordt verwerkt en de Nederlandse reisdocumenten en identiteitskaarten worden ingenomen (art. 64). Weigert de gemeente het verlies te bevestigen, dan staat beroep open bij de rechtbank Den Haag en daarna cassatie bij de Hoge Raad (Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Afstand van het Nederlanderschap | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren Nederlanderschap](beheren-nederlanderschap.md).
- **Kernobject**: [Nederlanderschap](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/nederlanderschap.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een verklaring van een feit dat tot bijwerking van de basisregistratie personen leidt; de persoon krijgt een bevestiging.
- **Eindigt in gebeurtenis**: [Verlies van het Nederlanderschap](../../../gebeurtenissen/verlies-van-het-nederlanderschap.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **procesniveau**: bedrijfsproces, kernobject [Nederlanderschap](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/nederlanderschap.md) | Ja, van de verklaring van afstand tot de bevestiging. [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md). [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Verklaring van afstand ondertekend (gebeurtenis, nog geen element): De verklaring van afstand, door de meerderjarige zelf ondertekend, met inlevering van identiteitsbewijs en reisdocumenten (Besluit art. 62, 63; Utrecht). [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verklaring van afstand | beëindigt door afstand *toegang (beëindigen)* | [Nederlanderschap](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/nederlanderschap.md) | [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (Rijkswet art. 15 lid 1 onder b; Besluit art. 63) |
| Behandelen verklaring van afstand | realiseert *realisatie* | [Verklaring van afstand nederlandse nationaliteit](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-van-afstand-nederlandse-nationaliteit.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) (UPL nr. 436) |
| Behandelen verklaring van afstand | leidt tot *triggering* | [Verlies van het Nederlanderschap](../../../gebeurtenissen/verlies-van-het-nederlanderschap.md) | [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 15 lid 1 onder b) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren Nederlanderschap](beheren-nederlanderschap.md) | omvat *aggregatie* | Behandelen verklaring van afstand | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 62-64) |
| [Beslisser](../../../rollen/beslisser.md) | bevestigt de afstand *toewijzing* | Behandelen verklaring van afstand | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 63) |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-verkrijging-en-verlies-nederlanderschap.md) | is grondslag voor *associatie (gericht)* | Behandelen verklaring van afstand | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 62-64) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht nationaliteit opgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) | Gemeente Utrecht: Nederlandse nationaliteit opgeven of verliezen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
