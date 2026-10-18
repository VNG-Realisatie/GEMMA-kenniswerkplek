---
id: begraven-en-cremeren-stoffelijk-overschot
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Begraven en cremeren stoffelijk overschot
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het begraven of cremeren van een stoffelijk overschot door de houder van een begraafplaats of crematorium, tot en met de bestemming van de as.
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
---

# Begraven en cremeren stoffelijk overschot

<!-- Gegenereerd door tools/render.py uit de beoordeling begraven-en-cremeren-stoffelijk-overschot.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het begraven of cremeren van een stoffelijk overschot door de houder van een begraafplaats of crematorium, tot en met de bestemming van de as.

### Beschrijving

Begraving geschiedt op een begraafplaats, crematie in een crematorium (Wet op de lijkbezorging art. 23, 49). Op de gemeentelijke begraafplaats bepaalt de beheerder tijd en plaats in overleg met de uitvaartondernemer, na kennisgeving door wie de uitvaart regelt (Groningen art. 7). De houder van een crematorium houdt een register bij, bewaart de asbus minimaal een maand en zorgt daarna voor de bestemming van de as: bijzetting, verstrooiing of meegeven aan de nabestaande (art. 50, 59, 62).

Het is het deel van de houder van de begraafplaats of het crematorium in de ketensamenwerking Bezorgen stoffelijk overschot. De gemeente voert het uit als houder van de gemeentelijke begraafplaats of van een gemeentelijk crematorium (art. 33); bij een bijzondere begraafplaats of een particulier crematorium doet de particuliere houder het.

### Naamkeuze

Infinitief met object in GEMMA-volgorde: begraven en cremeren zijn de wettelijke wijzen van lijkbezorging bij de houder, met de bestemming van de as als onderdeel (art. 1). Bezorgen en bestemmen is overwogen, maar valt bijna samen met de naam van de ketensamenwerking.

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Uitvoeren lijkbezorging](uitvoeren-lijkbezorging.md).
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Ketensamenwerking, bedient**: [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **procesniveau**: levensloopproces, kernobject [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | Omvat, binnen de ketensamenwerking Bezorgen stoffelijk overschot, het deel van de houder in de levensloop van het stoffelijk overschot: de begraving of crematie, het register, de bewaring van de asbus en de bestemming van de as (art. 23, 50, 59, 62–66a). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md), [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md), [Houder van een plaats van bijzetting](../../../rollen/houder-van-een-plaats-van-bijzetting.md): Houder van de begraafplaats, Beheerder van de begraafplaats, Houder van het crematorium en Houder van een plaats van bijzetting (art. 23, 50, 59, 62; Groningen art. 7). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Kennisgeving begraving of crematie gedaan (gebeurtenis, nog geen element): De kennisgeving door wie de uitvaart regelt, met het verlof tot begraving of crematie (art. 11; Groningen art. 7). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Begraven en cremeren stoffelijk overschot | omvat *aggregatie* | [Uitvoeren lijkbezorging](uitvoeren-lijkbezorging.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 1, 16) |
| Begraven en cremeren stoffelijk overschot | begraaft of cremeert *toegang (bijwerken)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23, 49) |
| Begraven en cremeren stoffelijk overschot | begraaft of cremeert in *bediening* | [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23, 49) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor begraven en cremeren; Uitbaten gemeentelijke voorzieningen is het generieke proces achter het cluster Uitbaten begraafplaatsen en crematoria, geen match voor dit deel van een ketensamenwerking. Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 5](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **Kennismodel:** een ketenproces is een samenhangend geheel van processen over afdelingen of organisaties heen, en aggregeert bedrijfsprocessen: Ketenproces → aggregatie → Bedrijfsproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 564, 590). **Bevinding:** de pagina Proceshiërarchie op GEMMA Online zegt het tegendeel: een ketenproces als proces boven de eigen bedrijfsprocessen is vanuit de procesarchitectuur gezien niet correct; ketensamenwerking is in ArchiMate een bedrijfsinteractie waarin de bedrijfsprocessen van de betrokken organisaties samenkomen ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 144, 146). Het GEMMA-model volgt die pagina: de bedrijfsinteractie Ketensamenwerking wordt bediend door de bedrijfsprocessen van de partijen. De pagina Impact van ketensamenwerking onderscheidt daarbij een estafette- en een orkestratiemodel ([2026-vng-gemma-impact-ketensamenwerking](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-impact-ketensamenwerking.md), regel 27-34). In het model: een estafette is een bedrijfsinteractie met een kernobject, bediend door de levensloopprocessen van de partijen. Voorbeeld: Bezorgen stoffelijk overschot, bediend door Toestaan lijkbezorging (de gemeente als overheid), Begraven en cremeren stoffelijk overschot (de houder van de begraafplaats of het crematorium) en Verzorgen gemeentebegrafenis, met de officier van justitie als ketenpartner ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), art. 10, 11, 12, 21, 23, 49). Bij orkestratie is er geen interactie: het deel dat de gemeente voor een andere partij uitvoert, is een specialisatie van Leveren dienst aan derden (bijvoorbeeld de verklaring omtrent het gedrag en de naturalisatie). **Voorstel:** haal Ketenproces → aggregatie → Bedrijfsproces uit het kennismodel en neem de bedrijfsinteractie op, bediend door bedrijfsprocessen en toegewezen aan een bedrijfssamenwerking of aan de rollen van de partijen.
