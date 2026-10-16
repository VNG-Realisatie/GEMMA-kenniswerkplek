---
id: beheren-begraafplaatsen
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Beheren begraafplaatsen
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: 'Het beheer van een begraafplaats over de hele levensloop: aanleggen, in gebruik nemen, sluiten en opheffen.'
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Beheren begraafplaatsen

<!-- Gegenereerd door tools/render.py uit de beoordeling beheren-begraafplaatsen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beheer van een begraafplaats over de hele levensloop: aanleggen, in gebruik nemen, sluiten en opheffen.

### Beschrijving

Elke gemeente heeft ten minste één gemeentelijke begraafplaats, alleen of samen met andere gemeenten; voor aanleg op het grondgebied van een andere gemeente is toestemming van de raad van die gemeente nodig (Wet op de lijkbezorging art. 33, 36). Voor een bijzondere begraafplaats wijst de raad de grond aan en geeft het college toestemming voor de ingebruikneming (art. 40, 41). Het college kan een gemeentelijke begraafplaats sluiten, of gesloten verklaren als er tien jaar niet is begraven (art. 43, 44). Een begraafplaats houdt op te bestaan als de grond die bestemming verloor en er geen graf meer is (art. 47).

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Sluiten begraafplaats](sluiten-begraafplaats.md), [Verlenen toestemming bijzondere begraafplaats](verlenen-toestemming-bijzondere-begraafplaats.md).
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md).
- **Functie-indeling naar domein, bediend door**: [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het voornemen tot aanleg of uitbreiding, of een verzoek om toestemming (art. 36, 40, 41). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een begraafplaats die in gebruik is, en na sluiting en opheffing niet meer bestaat (art. 41, 43, 47). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke begraafplaats, gemeentelijk of bijzonder. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet op de lijkbezorging art. 33–47. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, houders van bijzondere begraafplaatsen, rechthebbenden en nabestaanden (art. 37, 45). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **omvat processen**: Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? | Ja, met [Verlenen toestemming bijzondere begraafplaats](verlenen-toestemming-bijzondere-begraafplaats.md), [Sluiten begraafplaats](sluiten-begraafplaats.md). |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat de levensloop van de begraafplaats: aanleg of uitbreiding, ingebruikneming, sluiting en opheffing (art. 36, 40, 41, 43, 44, 47). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Beheren begraafplaatsen | omvat *aggregatie* | [Verlenen toestemming bijzondere begraafplaats](verlenen-toestemming-bijzondere-begraafplaats.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 40, 41) |
| Beheren begraafplaatsen | omvat *aggregatie* | [Sluiten begraafplaats](sluiten-begraafplaats.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 43, 44) |
| Beheren begraafplaatsen | beheert *toegang (bijwerken)* | [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 33, 36, 43, 47) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | bedient *bediening* | Beheren begraafplaatsen | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 39 lid 2) |
| [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md) | houdt in stand *toewijzing* | Beheren begraafplaatsen | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 33, 37) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor het beheer van begraafplaatsen; nieuw voor GEMMA.
