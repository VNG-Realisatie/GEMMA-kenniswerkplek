---
id: toestaan-lijkbezorging
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Toestaan lijkbezorging
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het schouwen van een stoffelijk overschot en het verlenen van verlof, vergunningen en toestemmingen voor de lijkbezorging, met zo nodig maatregelen.
match:
  gemma: geen
data_object: nee
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2025-groningen-algemene-plaatselijke-verordening
- 2026-rijk-besluit-op-de-lijkbezorging-wettekst
---

# Toestaan lijkbezorging

<!-- Gegenereerd door tools/render.py uit de beoordeling toestaan-lijkbezorging.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het schouwen van een stoffelijk overschot en het verlenen van verlof, vergunningen en toestemmingen voor de lijkbezorging, met zo nodig maatregelen.

### Beschrijving

Geen begraving, crematie of ontleding zonder schriftelijk verlof: de ambtenaar van de burgerlijke stand verleent verlof tot begraving of crematie als hij beschikt over een verklaring van overlijden van de behandelend arts of de gemeentelijke lijkschouwer, of over een verklaring van geen bezwaar van de officier van justitie; de burgemeester verleent verlof tot ontleding (Wet op de lijkbezorging art. 3, 4, 11, 12, 68). De burgemeester kan een andere termijn stellen, geeft het laissez-passer af voor vervoer naar het buitenland, treft maatregelen bij een besmet stoffelijk overschot en verleent vergunning tot opgraving; het college staat asverstrooiing toe (art. 17, 22a, 29; Besluit op de lijkbezorging art. 11; APV Groningen art. 5:27).

Het is het deel van de gemeente als overheid in de ketensamenwerking Bezorgen stoffelijk overschot; het begraven en cremeren zelf is het deel van de houder van de begraafplaats of het crematorium. De schouwing door de behandelend arts valt buiten het gemeentelijk perspectief.

### Naamkeuze

Infinitief met object in GEMMA-volgorde: de kern zijn de verloven, vergunningen en toestemmingen; de schouwing is de voorwaarde voor het verlof (art. 12) en de maatregel stuurt de bezorging bij (art. 22a). Toezien op lijkbezorging is overwogen, maar kan verward worden met toezicht en handhaving.

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Afgeven laissez-passer](afgeven-laissez-passer.md), [Opgraven stoffelijk overschot](opgraven-stoffelijk-overschot.md), [Schouwen stoffelijk overschot](schouwen-stoffelijk-overschot.md), [Stellen andere termijn](stellen-andere-termijn.md), [Treffen maatregel bij besmet stoffelijk overschot](treffen-maatregel-bij-besmet-stoffelijk-overschot.md), [Verlenen verlof tot begraving of crematie](verlenen-verlof-tot-begraving-of-crematie.md), [Verlenen verlof tot ontleding](verlenen-verlof-tot-ontleding.md).
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Ketensamenwerking, bedient**: [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, gemeentelijke lijkschouwer (art. 3, 4), Ambtenaar van de burgerlijke stand (art. 11) en Beslisser: de burgemeester of het college (art. 17, 22a, 29, 68; APV Groningen art. 5:27). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het overlijden en de aanvraag van het verlof door wie in de lijkbezorging voorziet (art. 3, 11, 18). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een stoffelijk overschot dat mag worden begraven, gecremeerd of ontleed: het verlof, met zo nodig een andere termijn, een laissez-passer of een maatregel (art. 11, 17, 22a, 68; Besluit op de lijkbezorging art. 11). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk overlijden. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet op de lijkbezorging art. 3–17, 22a, 29, 67–68; Besluit op de lijkbezorging art. 11. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **omvat processen**: Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? | Ja, met [Schouwen stoffelijk overschot](schouwen-stoffelijk-overschot.md), [Verlenen verlof tot begraving of crematie](verlenen-verlof-tot-begraving-of-crematie.md), [Stellen andere termijn](stellen-andere-termijn.md), [Verlenen verlof tot ontleding](verlenen-verlof-tot-ontleding.md), [Afgeven laissez-passer](afgeven-laissez-passer.md), [Opgraven stoffelijk overschot](opgraven-stoffelijk-overschot.md), [Treffen maatregel bij besmet stoffelijk overschot](treffen-maatregel-bij-besmet-stoffelijk-overschot.md). |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat, binnen de ketensamenwerking Bezorgen stoffelijk overschot, het deel van de gemeente als overheid in de levensloop van het stoffelijk overschot: de schouwing door de gemeentelijke lijkschouwer, het verlof tot begraving, crematie of ontleding, een andere termijn, het laissez-passer, een maatregel bij besmetting, de toestemming voor asverstrooiing en later de vergunning tot opgraving (art. 3, 11, 17, 22a, 29, 68; Besluit op de lijkbezorging art. 11; APV Groningen art. 5:27). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md), [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Toestaan lijkbezorging | omvat *aggregatie* | [Schouwen stoffelijk overschot](schouwen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Verlenen verlof tot begraving of crematie](verlenen-verlof-tot-begraving-of-crematie.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 11, 12) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Stellen andere termijn](stellen-andere-termijn.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Verlenen verlof tot ontleding](verlenen-verlof-tot-ontleding.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 67, 68) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Afgeven laissez-passer](afgeven-laissez-passer.md) | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (Besluit op de lijkbezorging art. 11) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Opgraven stoffelijk overschot](opgraven-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Treffen maatregel bij besmet stoffelijk overschot](treffen-maatregel-bij-besmet-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| Toestaan lijkbezorging | schouwt en geeft verlof voor *toegang (raadplegen)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 11) |
| Toestaan lijkbezorging | verleent verlof voor *bediening* | [Bezorgen stoffelijk overschot](../../../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 10, 11, 12) |
| Toestaan lijkbezorging | omvat *aggregatie* | [Besmet stoffelijk overschot gemeld](../../../gebeurtenissen/besmet-stoffelijk-overschot-gemeld.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a; Wpg art. 27 lid 3) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [APV Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2025-groningen-algemene-plaatselijke-verordening.md) | Algemene Plaatselijke Verordening Groningen 2021 |
| [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) | Besluit op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor de lijkbezorging; Behandelen aanvraag vergunning of ontheffing is het generieke proces achter het cluster Behandelen vergunningaanvragen lijkbezorging, geen match voor dit deel van een ketensamenwerking. Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 5](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **Kennismodel:** een ketenproces is een samenhangend geheel van processen over afdelingen of organisaties heen, en aggregeert bedrijfsprocessen: Ketenproces → aggregatie → Bedrijfsproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 564, 590). **Bevinding:** de pagina Proceshiërarchie op GEMMA Online zegt het tegendeel: een ketenproces als proces boven de eigen bedrijfsprocessen is vanuit de procesarchitectuur gezien niet correct; ketensamenwerking is in ArchiMate een bedrijfsinteractie waarin de bedrijfsprocessen van de betrokken organisaties samenkomen ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 144, 146). Het GEMMA-model volgt die pagina: de bedrijfsinteractie Ketensamenwerking wordt bediend door de bedrijfsprocessen van de partijen. De pagina Impact van ketensamenwerking onderscheidt daarbij een estafette- en een orkestratiemodel ([2026-vng-gemma-impact-ketensamenwerking](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-impact-ketensamenwerking.md), regel 27-34). In het model: een estafette is een bedrijfsinteractie met een kernobject, bediend door de levensloopprocessen van de partijen. Voorbeeld: Bezorgen stoffelijk overschot, bediend door Toestaan lijkbezorging (de gemeente als overheid), Begraven en cremeren stoffelijk overschot (de houder van de begraafplaats of het crematorium) en Verzorgen gemeentebegrafenis, met de officier van justitie als ketenpartner ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), art. 10, 11, 12, 21, 23, 49). Bij orkestratie is er geen interactie: het deel dat de gemeente voor een andere partij uitvoert, is een specialisatie van Leveren dienst aan derden (bijvoorbeeld de verklaring omtrent het gedrag en de naturalisatie). **Voorstel:** haal Ketenproces → aggregatie → Bedrijfsproces uit het kennismodel en neem de bedrijfsinteractie op, bediend door bedrijfsprocessen en toegewezen aan een bedrijfssamenwerking of aan de rollen van de partijen.

### Besluiten redacteur

- 2026-10-07: Afgewezen: één gemeentelijk deel met alle tien bedrijfsprocessen (bijna gelijk aan de ketensamenwerking, mengt overheid en houder) en groepen per fase (volgen de fase, niet de partij). Een groep arts vervalt: in het model schouwt alleen de gemeentelijke lijkschouwer, die de gemeente benoemt (Wlb art. 3, 4). Namen afgewezen: Toezien op lijkbezorging (homoniem met toezicht), Bezorgen en bestemmen (bijna de naam van de ketensamenwerking). *Zekerheid: logica.*
