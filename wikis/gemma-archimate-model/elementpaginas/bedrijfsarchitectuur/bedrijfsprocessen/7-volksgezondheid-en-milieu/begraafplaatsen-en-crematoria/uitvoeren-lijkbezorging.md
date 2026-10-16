---
id: uitvoeren-lijkbezorging
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Uitvoeren lijkbezorging
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het begraven, cremeren of op een andere wettelijke wijze bezorgen van een stoffelijk overschot.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
---

# Uitvoeren lijkbezorging

<!-- Gegenereerd door tools/render.py uit de beoordeling uitvoeren-lijkbezorging.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het begraven, cremeren of op een andere wettelijke wijze bezorgen van een stoffelijk overschot.

### Beschrijving

De lijkbezorging geschiedt door begraving, crematie of op een andere wettelijk voorziene wijze, en omvat ook het geven van een bestemming aan de as (art. 1, 18 lid 2). Ze vereist een verlof tot begraving of crematie (art. 11) en volgt, waar mogelijk, de wens van de overledene (art. 19). Op de gemeentelijke begraafplaats bepaalt de beheerder tijd en plaats in overleg met de uitvaartondernemer, na kennisgeving door wie de uitvaart regelt (Groningen art. 7). Begraving, crematie en ontleding zijn varianten zonder eigen pagina; het bijzetten of verstrooien van de as is een deelproces.

Na de crematie bewaart de houder van het crematorium de asbus minimaal een maand en zorgt hij daarna dat de asbus wordt bijgezet, de as wordt verstrooid, de asbus aan de nabestaande wordt meegegeven of naar het buitenland gaat (Wet op de lijkbezorging art. 59). Een asbus wordt bijgezet in een crematorium, in of op een graf of op een afzonderlijke plaats op een begraafplaats, of in een bewaarplaats; in een particulier graf alleen met toestemming van de rechthebbende (art. 62). De houder van de plaats van bijzetting houdt een register bij en kan de asbus op verzoek aan de nabestaande meegeven (art. 63, 65). Verstrooien door een houder mag alleen op een daartoe bestemd terrein of in open zee (art. 66a); op de gemeentelijke begraafplaats kan het college incidentele asverstrooiing op een aangewezen plek toestaan (Groningen art. 21).

### Deelprocessen

1. **Begraven of cremeren**: Na het verlof bepaalt de beheerder tijd en plaats in overleg met de uitvaartondernemer, binnen de termijn na het overlijden. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 11, 16; Groningen art. 7)
2. **Bijzetten of verstrooien van de as**: Na een crematie bewaart de houder van het crematorium de asbus minimaal een maand en zorgt hij daarna voor de bestemming: bijzetten, verstrooien, meegeven aan de nabestaande of naar het buitenland. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 59, 62)

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Begraven en cremeren stoffelijk overschot](begraven-en-cremeren-stoffelijk-overschot.md), [Uitbaten begraafplaatsen en crematoria](uitbaten-begraafplaatsen-en-crematoria.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Functie-indeling naar domein, bediend door**: [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md).
- **Gestart door gebeurtenis**: [Overlijden](../../../gebeurtenissen/overlijden.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Degene die in de lijkbezorging voorziet](../../../rollen/degene-die-in-de-lijkbezorging-voorziet.md), [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md), [Houder van een plaats van bijzetting](../../../rollen/houder-van-een-plaats-van-bijzetting.md), [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md), [Nabestaande](../../../rollen/nabestaande.md), [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Vergunning](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md), [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md), [Graf](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md), [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md), [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md), [Urn](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/urn.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Overlijden](../../../gebeurtenissen/overlijden.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, begraven of gecremeerd lijk, bijgezette of verstrooide as (art. 1, 59). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke uitvaart. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, art. 16 (termijn), 23 (graf), 49 (crematorium), 59 (bestemming as); Groningen art. 7–10 (tijden, stukken). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Begraven en cremeren stoffelijk overschot](begraven-en-cremeren-stoffelijk-overschot.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het overlijden en de kennisgeving tot de begraven of gecremeerde overledene en de bestemming van de as. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |

### Specialisaties

- **Begraving**: Begraven van een stoffelijk overschot op een begraafplaats, in een algemeen of particulier graf (art. 23). Geen eigen pagina.
- **Crematie**: Cremeren van een stoffelijk overschot in een crematorium (art. 49). Geen eigen pagina.
- **Ontleding**: Ontleden van een stoffelijk overschot in het belang van de wetenschap, met verlof van de burgemeester (art. 67, 68). Geen eigen pagina.
- **Bijzetting**: Bijzetten van een asbus in een crematorium, graf, urnennis of bewaarplaats (art. 62). Geen eigen pagina.
- **Verstrooiing**: Verstrooien van as op een daartoe bestemd terrein of in open zee (art. 66a). Geen eigen pagina.
- **Incidentele asverstrooiing**: Verstrooien van as op een aangewezen plek op of buiten de begraafplaats, met toestemming van het college (Groningen art. 1 m, 21). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitvoeren lijkbezorging | vereist *toegang (raadplegen)* | [Vergunning](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 11) |
| Uitvoeren lijkbezorging | bezorgt *toegang (bijwerken)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 1) |
| Uitvoeren lijkbezorging | begraaft in, zet bij in of op *toegang (bijwerken)* | [Graf](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/graf.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23 lid 2; art. 62 lid 1 b, 3) |
| Uitvoeren lijkbezorging | geschiedt op *toegang (raadplegen)* | [Begraafplaats](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23 lid 1) |
| Uitvoeren lijkbezorging | geschiedt in *toegang (raadplegen)* | [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 49) |
| Uitvoeren lijkbezorging | zet bij of verstrooit de as uit *toegang (bijwerken)* | [Urn](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/urn.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 59 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Begraven en cremeren stoffelijk overschot](begraven-en-cremeren-stoffelijk-overschot.md) | omvat *aggregatie* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 1, 16) |
| [Degene die in de lijkbezorging voorziet](../../../rollen/degene-die-in-de-lijkbezorging-voorziet.md) | voorziet in en vraagt het verlof aan voor *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (Wlb art. 18; Groningen art. 7 lid 2) |
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | bedient *bediening* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 23) |
| [Houder van de begraafplaats](../../../rollen/houder-van-de-begraafplaats.md) | stelt de identiteit vast bij *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 8 lid 2) |
| [Houder van een plaats van bijzetting](../../../rollen/houder-van-een-plaats-van-bijzetting.md) | houdt het register bij en stelt de asbus ter beschikking bij *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 63, 65) |
| [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md) | bergt de as bij, zorgt voor de bewaring en de bestemming van de as bij *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 58; art. 59) |
| [Nabestaande](../../../rollen/nabestaande.md) | geeft opdracht tot bijzetting bij *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 62 lid 2) |
| [Overlijden](../../../gebeurtenissen/overlijden.md) | leidt tot *triggering* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 16) |
| [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md) | machtigt tot begraving in het particulier graf *toewijzing* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) (Wlb art. 23 lid 2; Groningen art. 9 lid 2; VNG-modelverordening art. 9 lid 2) |
| [Uitbaten begraafplaatsen en crematoria](uitbaten-begraafplaatsen-en-crematoria.md) | omvat *aggregatie* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 23, 49; Groningen art. 7; art. 59, 62; Groningen art. 21) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Uitvoeren lijkbezorging | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 1, 23, 49; art. 59–66b) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
