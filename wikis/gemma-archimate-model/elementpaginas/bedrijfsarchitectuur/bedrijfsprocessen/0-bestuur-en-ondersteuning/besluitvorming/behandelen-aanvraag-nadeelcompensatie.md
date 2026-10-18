---
id: behandelen-aanvraag-nadeelcompensatie
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen aanvraag nadeelcompensatie
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het beslissen op een aanvraag om vergoeding van onevenredige schade door rechtmatig handelen van de gemeente.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen aanvraag nadeelcompensatie

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-aanvraag-nadeelcompensatie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beslissen op een aanvraag om vergoeding van onevenredige schade door rechtmatig handelen van de gemeente.

### Beschrijving

De benadeelde dient een aanvraag in met de schadeveroorzakende gebeurtenis en de aard en zo mogelijk het bedrag van de schade; een verordening kan een recht van ten hoogste € 500 heffen voor de behandeling (Awb art. 4:127, 4:128). Het bestuursorgaan beoordeelt of de schade boven het normale maatschappelijke risico uitgaat en de benadeelde onevenredig treft, en wat voor rekening van de aanvrager blijft (art. 4:126). Het beslist binnen acht weken, of binnen zes maanden als een adviescommissie met een onafhankelijke voorzitter adviseert, en kan eenmaal verdagen of de beslissing aanhouden tot een schadeveroorzakend besluit onherroepelijk is (art. 4:130). Kent het een vergoeding toe, dan vergoedt het ook redelijke kosten, het betaalde recht en de wettelijke rente (art. 4:129); na vijf of twintig jaar kan het de aanvraag afwijzen (art. 4:131).

### Deelprocessen

1. **Ontvangen aanvraag nadeelcompensatie**: Het bestuursorgaan ontvangt de aanvraag met de gebeurtenis en de schade, en heft zo nodig een recht (art. 4:127, 4:128). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Beoordelen schade**: Het bestuursorgaan beoordeelt of de schade boven het normale maatschappelijke risico uitgaat en onevenredig is, eventueel met advies van een onafhankelijke adviescommissie (art. 4:126, 4:130). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
3. **Beslissen op aanvraag nadeelcompensatie**: Het bestuursorgaan kent de vergoeding toe, met kosten en rente, of wijst de aanvraag af (art. 4:126, 4:129–4:131). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md), [Aanvraag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/aanvraag.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Aanvraag nadeelcompensatie ingediend (gebeurtenis, nog geen element): Een aanvraag van de benadeelde, met de schadeveroorzakende gebeurtenis en de schade (art. 4:127). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een beschikking die de vergoeding toekent of de aanvraag afwijst (art. 4:126, 4:130, 4:131). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke aanvraag om nadeelcompensatie. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, titel 4.5 Awb: inhoud van de aanvraag, recht van ten hoogste € 500, beslistermijn van acht weken of zes maanden met een adviescommissie, verdaging, verjaring (art. 4:127–4:131). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met Beheren beschikkingen (bedrijfsproces, nog geen element): Eén mutatie in de levensloop van een beschikking: het besluit over de vergoeding (art. 4:126, 4:130). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van de aanvraag van de benadeelde tot de beschikking aan hem (art. 4:127, 4:130). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, eindigt in de beschikking van het bestuursorgaan over de vergoeding (art. 4:126, 4:130). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Nadeelcompensatie](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/nadeelcompensatie.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen aanvraag nadeelcompensatie | realiseert *realisatie* | [Nadeelcompensatie](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/nadeelcompensatie.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 4:126; UPL nr. 260) |
| Behandelen aanvraag nadeelcompensatie | kent de vergoeding toe of wijst af bij *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:126, 4:130) |
| Behandelen aanvraag nadeelcompensatie | neemt in behandeling *toegang (raadplegen)* | [Aanvraag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/aanvraag.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:127) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Belanghebbende](../../../rollen/belanghebbende.md) | vraagt als benadeelde de vergoeding aan *toewijzing* | Behandelen aanvraag nadeelcompensatie | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:126, 4:127) |
| [Beslisser](../../../rollen/beslisser.md) | beslist op de aanvraag en kent de vergoeding toe *toewijzing* | Behandelen aanvraag nadeelcompensatie | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:126, 4:130) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor nadeelcompensatie. Nieuw voor GEMMA.
