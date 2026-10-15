---
id: verzorgen-gemeentebegrafenis
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Verzorgen gemeentebegrafenis
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het regelen en betalen van de lijkbezorging door de gemeente als niemand anders daarin voorziet.
match:
  gemma: geen
data_object: nee
procesniveau: levensloopproces
afnemer: extern
synoniemen:
- Lijkbezorging door de burgemeester (wet)
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Verzorgen gemeentebegrafenis

<!-- Gegenereerd door tools/render.py uit de beoordeling verzorgen-gemeentebegrafenis.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het regelen en betalen van de lijkbezorging door de gemeente als niemand anders daarin voorziet.

### Beschrijving

Als niemand voorziet in de lijkschouwing en lijkbezorging, waarschuwt degene die het stoffelijk overschot onder zich heeft de burgemeester, die daarvoor zorg draagt (art. 20, 21 lid 1). Beslisser is de burgemeester. De kosten komen ten laste van de gemeente, die ze kan verhalen op de nalatenschap, onderhoudsplichtige verwanten of de werkgever (art. 22); dat kostenverhaal is een stap in dit proces. Een stoffelijk overschot waarvan de identiteit niet kan worden vastgesteld, wordt begraven (art. 21 lid 6). Het resultaat is een gemeentebegrafenis.

### Synoniemen

| Synoniem | Context |
|---|---|
| Lijkbezorging door de burgemeester | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Gemeentebegrafenis](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md).
- **Ketensamenwerking, bedient**: [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Kostendrager](../../../rollen/kostendrager.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md), [Gemeentebegrafenis](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, melding dat niemand in de lijkbezorging voorziet, uiterlijk de derde dag na het overlijden (art. 20). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een gemeentebegrafenis, met kostenverhaal (art. 21, 22). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk overlijden waarbij niemand in de lijkbezorging voorziet. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, art. 20–22: melding, zorgplicht, kostenverhaal; art. 21 lid 3–6 bij onbekende identiteit. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat de levensloop van de gemeentebegrafenis: de melding dat niemand in de lijkbezorging voorziet (art. 20), de zorg door de burgemeester (art. 21), het kostenverhaal (art. 22) en de afdoening (GGM-attributen datumGemeld, datumBegrafenis, verhaaldBedrag, datumAfgedaan). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verzorgen gemeentebegrafenis | betreft *toegang (raadplegen)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21) |
| Verzorgen gemeentebegrafenis | legt vast en handelt af *toegang (bijwerken)* | [Gemeentebegrafenis](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/gemeentebegrafenis.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21, 22) |
| Verzorgen gemeentebegrafenis | zorgt voor de bezorging in *bediening* | [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | draagt zorg voor *toewijzing* | Verzorgen gemeentebegrafenis | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21 lid 1) |
| [Kostendrager](../../../rollen/kostendrager.md) | draagt de kosten van *toewijzing* | Verzorgen gemeentebegrafenis | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Verzorgen gemeentebegrafenis | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 21, 22) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 5](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **Kennismodel:** een ketenproces is een samenhangend geheel van processen over afdelingen of organisaties heen, en aggregeert bedrijfsprocessen: Ketenproces → aggregatie → Bedrijfsproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 564, 590). **Bevinding:** de pagina Proceshiërarchie op GEMMA Online zegt het tegendeel: een ketenproces als proces boven de eigen bedrijfsprocessen is vanuit de procesarchitectuur gezien niet correct; ketensamenwerking is in ArchiMate een bedrijfsinteractie waarin de bedrijfsprocessen van de betrokken organisaties samenkomen ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 144, 146). Het GEMMA-model volgt die pagina: de bedrijfsinteractie Ketensamenwerking wordt bediend door de bedrijfsprocessen van de partijen. De pagina Impact van ketensamenwerking onderscheidt daarbij een estafette- en een orkestratiemodel ([2026-vng-gemma-impact-ketensamenwerking](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-impact-ketensamenwerking.md), regel 27-34). In het model: een estafette is een bedrijfsinteractie met een kernobject, bediend door de levensloopprocessen van de partijen. Voorbeeld: Bezorgen stoffelijk overschot, bediend door Toestaan lijkbezorging (de gemeente als overheid), Begraven en cremeren stoffelijk overschot (de houder van de begraafplaats of het crematorium) en Verzorgen gemeentebegrafenis, met de officier van justitie als ketenpartner ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), art. 10, 11, 12, 21, 23, 49). Bij orkestratie is er geen interactie: het deel dat de gemeente voor een andere partij uitvoert, is een specialisatie van Leveren dienst aan derden (bijvoorbeeld de verklaring omtrent het gedrag en de naturalisatie). **Voorstel:** haal Ketenproces → aggregatie → Bedrijfsproces uit het kennismodel en neem de bedrijfsinteractie op, bediend door bedrijfsprocessen en toegewezen aan een bedrijfssamenwerking of aan de rollen van de partijen.
