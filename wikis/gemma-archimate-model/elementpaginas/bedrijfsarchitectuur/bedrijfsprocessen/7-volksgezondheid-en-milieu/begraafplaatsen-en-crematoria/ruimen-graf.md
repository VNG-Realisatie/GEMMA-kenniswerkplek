---
id: ruimen-graf
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Ruimen graf
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het leegmaken van een graf, waarbij de resten worden herbegraven en de as wordt verstrooid.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Ruiming (beleid)
- Ruimen van graven (wet)
bronnen:
- 2010-vng-model-beheersverordening-begraafplaatsen
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
---

# Ruimen graf

<!-- Gegenereerd door tools/render.py uit de beoordeling ruimen-graf.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het leegmaken van een graf, waarbij de resten worden herbegraven en de as wordt verstrooid.

### Beschrijving

Een graf wordt geruimd op last van de houder van de begraafplaats, na ten minste tien jaar na de laatste begraving en bij een particulier graf met toestemming van de rechthebbende (art. 31). Het college kondigt een ruiming ten minste een jaar vooraf aan, per brief of met een bordje bij het graf en op het mededelingenbord; de beheerder ziet toe op een respectvolle omgang met de resten, die worden herbegraven, terwijl de as wordt verstrooid (Groningen art. 27; VNG-modelverordening art. 24). Asbussen worden geruimd door verstrooiing van de as (art. 66).

### Synoniemen

| Synoniem | Context |
|---|---|
| Ruiming | beleid |
| Ruimen van graven | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren graven](beheren-graven.md), [Uitbaten begraafplaatsen en crematoria](uitbaten-begraafplaatsen-en-crematoria.md).
- **Kernobject**: [Graf](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md).
- **Gestart door gebeurtenis**: [Verval van het grafrecht](../../../gebeurtenissen/verval-van-het-grafrecht.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md), [Houder van een plaats van bijzetting](../../../rollen/houder-van-een-plaats-van-bijzetting.md), [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Graf](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md), [Urn](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/urn.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Verval van het grafrecht](../../../gebeurtenissen/verval-van-het-grafrecht.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een geruimd graf; resten herbegraven, as verstrooid (art. 31 lid 3; Groningen art. 27 lid 3). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, regelmatig, voor veel graven. [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, art. 31 (tien jaar grafrust, toestemming rechthebbende, melding graf van een onbekende); Groningen art. 27 (aankondiging een jaar vooraf). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Beheren graven](beheren-graven.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, ambtshalve, van het verval van het grafrecht of het einde van de termijn tot het geruimde graf. [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ruimen graf | ruimt *toegang (bijwerken)* | [Graf](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 31; Groningen art. 27) |
| Ruimen graf | ruimt door verstrooiing *toegang (bijwerken)* | [Urn](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/urn.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 66) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren graven](beheren-graven.md) | omvat *aggregatie* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 31; Groningen art. 27) |
| [Belanghebbende](../../../rollen/belanghebbende.md) | ontvangt bericht van de ruiming (bij een algemeen graf) *toewijzing* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) (Wlb art. 27a; VNG-modelverordening art. 24 lid 1) |
| [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md) | geeft last tot *toewijzing* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 31 lid 2) |
| [Houder van een plaats van bijzetting](../../../rollen/houder-van-een-plaats-van-bijzetting.md) | ruimt asbussen bij *toewijzing* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 66) |
| [Model-beheersverordening begraafplaatsen](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-beheersverordening-begraafplaatsen.md) | werkt uit voor *associatie (gericht)* | Ruimen graf | [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) (art. 24) |
| [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md) | geeft toestemming voor *toewijzing* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 31 lid 2) |
| [Uitbaten begraafplaatsen en crematoria](uitbaten-begraafplaatsen-en-crematoria.md) | omvat *aggregatie* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 31; Groningen art. 27) |
| [Verval van het grafrecht](../../../gebeurtenissen/verval-van-het-grafrecht.md) | leidt tot *triggering* | Ruimen graf | [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 20 lid 4, 26) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Ruimen graf | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 31) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) | Model-beheersverordening begraafplaatsen 2010 (VNG), met toelichting |
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
