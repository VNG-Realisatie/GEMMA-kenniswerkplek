---
id: rijk
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Rijk
onderwerpen:
- bestuur-en-organisatie
- burgerzaken
definitie: De Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft.
match:
  gemma: exact
doelgroep: ketenpartners
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rijk-wet-brp-bwbr0033715
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-rijk-bw2-rechtspersonen
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
gemma_id: id-9f6a80ba-b7fb-4a58-b599-b5f2b33b840e
gemma_naam: Rijk
gemma_type: business-actor
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: 9f6a80ba-b7fb-4a58-b599-b5f2b33b840e
---

# Rijk

<!-- Gegenereerd door tools/render.py uit de beoordeling rijk.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

De Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft.

### Beschrijving

Het Rijk handelt via zijn ministers, die elk een deel van de rijkstaken dragen, en hun diensten. Voor de gemeente gaat het om taken die in de wet naast de gemeentelijke taak staan: de minister van Binnenlandse Zaken en Koninkrijksrelaties (uitgevoerd door de Rijksdienst voor Identiteitsgegevens, RvIG) houdt de niet-ingezetenen bij in de BRP en de voorzieningen daarvoor in stand (Wet BRP art. 1.4 lid 2, 2.64), laat de reisdocumenten maken en houdt de registers van reisdocumenten bij (Paspoortwet art. 2 lid 3–4); de minister van Justitie en Veiligheid (uitgevoerd door de Immigratie- en Naturalisatiedienst, IND) beslist over de naturalisatie (Besluit verkrijging en verlies Nederlanderschap art. 37, 38) en, in de praktijk via Justis, over de afgifte van de verklaring omtrent het gedrag (Wet justitiële en strafvorderlijke gegevens art. 30, 37).

Het model kent het Rijk als één actor, de bestuurslaag als geheel, zoals Gemeente, Provincie en Waterschap; de afzonderlijke ministeries en rijksdiensten staan in de beschrijving en zijn geen eigen element. Waar de gemeente gegevens of registers van het Rijk gebruikt, zijn die invoer. De RDW en het CBR zijn zelfstandige bestuursorganen met een eigen rechtspersoonlijkheid; ze zijn geen eigen element en staan in de beschrijving van Beheren rijbewijzen (Wegenverkeerswet 1994 art. 4a, 4z).

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: handelende partij.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [BW Boek 2](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, de bestuurslaag als geheel, waarmee elke gemeente in dezelfde rol te maken heeft; zo ook Provincie en Waterschap. Afzonderlijke ministeries en rijksdiensten zijn geen eigen actor. [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Ketenpartner](../rollen/ketenpartner.md). [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [BW Boek 2](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Rijk | vervult *toewijzing* | [Ketenpartner](../rollen/ketenpartner.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 37, 38; Wjsg art. 30, 37) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [BW Boek 2](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-bw2-rechtspersonen.md) | Burgerlijk Wetboek Boek 2 Rechtspersonen (BWBR0003045) |
| [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Rijk* (business-actor). GEMMA-actor Rijk (procesarchitectuur, actoren en rollen); zelfde begrip, in GEMMA zonder definitie en zonder relaties. Nieuw: een definitie.

GEMMA-terugmeldingen:

- [Nummer 2](../../../modellen/gemma/terugmeldingen/gemma-team.md) (definitie, open): **GEMMA:** de rol Kiezer en de actoren Gemeenteraad, College en Rijk hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). Rijk heeft ook geen relaties. **Bevinding:** de wiki heeft deze vier elementen aan GEMMA gekoppeld. De import vult dus de definities in en hernoemt College naar College van B&W, want "College" kan meerdere organen bedoelen. **Voorstel:** controleer de definities en de nieuwe naam bij de import: Kiezer: wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen; Gemeenteraad: het bestuursorgaan dat de bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt; College van B&W: het dagelijks bestuur, de burgemeester en de wethouders; Rijk: de Staat der Nederlanden als bestuurslaag, met zijn ministers en rijksdiensten, en de relaties daarvan.
