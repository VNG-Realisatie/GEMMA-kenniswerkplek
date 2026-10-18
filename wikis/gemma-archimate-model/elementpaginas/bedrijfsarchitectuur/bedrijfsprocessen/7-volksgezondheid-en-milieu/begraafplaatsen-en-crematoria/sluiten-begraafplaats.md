---
id: sluiten-begraafplaats
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Sluiten begraafplaats
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het besluit dat op een begraafplaats niet meer wordt begraven, of de geslotenverklaring na tien jaar zonder begraving.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Sluiten begraafplaats

<!-- Gegenereerd door tools/render.py uit de beoordeling sluiten-begraafplaats.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het besluit dat op een begraafplaats niet meer wordt begraven, of de geslotenverklaring na tien jaar zonder begraving.

### Beschrijving

Een begraafplaats kan worden gesloten; voor een gemeentelijke begraafplaats neemt het college het besluit, en van de sluiting van een andere begraafplaats wordt het college direct op de hoogte gesteld (Wet op de lijkbezorging art. 43). Is er tien jaar niet begraven, dan kan het college de begraafplaats gesloten verklaren (art. 44). Belanghebbenden kunnen in beroep bij gedeputeerde staten, die de rechthebbende op een particulier graf een schadeloosstelling ten laste van de gemeente kunnen toekennen (art. 45).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren begraafplaatsen](beheren-begraafplaatsen.md).
- **Kernobject**: [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | Ja, ambtshalve, van het voornemen of de termijn tot het besluit. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Voornemen tot sluiting begraafplaats gemeld (gebeurtenis, nog geen element), Termijn van tien jaar zonder begraving verstreken (gebeurtenis, nog geen element): Een voornemen van het college, of een termijn: tien jaar zonder begraving (art. 43, 44). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Sluiten begraafplaats | besluit tot *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43 lid 2, 44) |
| Sluiten begraafplaats | sluit *toegang (beëindigen)* | [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43, 44) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren begraafplaatsen](beheren-begraafplaatsen.md) | omvat *aggregatie* | Sluiten begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43, 44) |
| [Beslisser](../../../rollen/beslisser.md) | besluit tot *toewijzing* | Sluiten begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43 lid 2, 44) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Sluiten begraafplaats | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43, 44) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
