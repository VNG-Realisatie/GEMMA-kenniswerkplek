---
id: uitvaart-vervroegen-of-uitstellen
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Uitvaart vervroegen of uitstellen
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Toestemming van de gemeente om een overledene eerder dan 36 uur of later dan zes werkdagen na het overlijden te begraven of te cremeren.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Andere termijn (wet)
bronnen:
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Uitvaart vervroegen of uitstellen

<!-- Gegenereerd door tools/render.py uit de beoordeling uitvaart-vervroegen-of-uitstellen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Toestemming van de gemeente om een overledene eerder dan 36 uur of later dan zes werkdagen na het overlijden te begraven of te cremeren.

### Beschrijving

Begraven of cremeren mag niet eerder dan 36 uur en uiterlijk op de zesde werkdag na het overlijden (art. 16). Na een arts te hebben gehoord kan de burgemeester een andere termijn stellen; eerder dan 36 uur alleen in overeenstemming met de officier van justitie (art. 17). De uitvaartondernemer vraagt de vergunning namens de nabestaanden aan bij de gemeente waar de persoon is overleden, bijvoorbeeld om religieuze redenen of omdat familie uit het buitenland moet komen (Ondernemersplein).

### Synoniemen

| Synoniem | Context |
|---|---|
| Andere termijn | wet |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Andere termijn (Specialisatie van Beschikking zonder eigen pagina in deze wiki) | Het besluit van de burgemeester waarmee een afwijkende termijn voor begraving of crematie wordt gesteld (Wet op de lijkbezorging art. 17) | Deze pagina heet Uitvaart vervroegen of uitstellen: de dienst voor de afnemer, met Andere termijn als synoniem (wet). Het besluit zelf is de specialisatie Andere termijn van Beschikking en krijgt geen pagina. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Vergunningenbeheer Publieksdiensten](../../../bedrijfsfuncties/publieksdiensten/vergunningenbeheer-publieksdiensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Stellen andere termijn](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md). [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitvaart vervroegen of uitstellen | bedient *bediening* | [Degene die in de lijkbezorging voorziet](../../../rollen/degene-die-in-de-lijkbezorging-voorziet.md) | [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (§ Uitvaart vervroegen, § Uitvaart uitstellen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Stellen andere termijn](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | realiseert *realisatie* | Uitvaart vervroegen of uitstellen | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (art. 17; § Uitvaart vervroegen, § Uitvaart uitstellen) |
| [Vergunningenbeheer Publieksdiensten](../../../bedrijfsfuncties/publieksdiensten/vergunningenbeheer-publieksdiensten.md) | omvat *aggregatie* | Uitvaart vervroegen of uitstellen | [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (§ Uitvaart vervroegen, § Uitvaart uitstellen) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Uitvaart vervroegen of uitstellen | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
