---
id: beheren-reisdocumenten
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Beheren reisdocumenten
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het behandelen van aanvragen, verstrekken en uitreiken van reisdocumenten en het verwerken van vermissing, inhouding en verval ervan.
match:
  gemma: geen
data_object: nee
procesniveau: levensloopproces
afnemer: extern
synoniemen:
- Reisdocumenten (dagelijks gebruik)
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-paspoortbesluit-bwbr0044308
- 2026-rvig-hup-inhouding-inlevering-vermissing
---

# Beheren reisdocumenten

<!-- Gegenereerd door tools/render.py uit de beoordeling beheren-reisdocumenten.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van aanvragen, verstrekken en uitreiken van reisdocumenten en het verwerken van vermissing, inhouding en verval ervan.

### Beschrijving

De burgemeester neemt de aanvraag in ontvangst, verstrekt het reisdocument binnen vier weken en reikt het binnen twee weken daarna uit, voor wie als ingezetene met een adres in zijn gemeente in de basisregistratie personen staat (Paspoortwet art. 26, 40, 41, 42). Een aangewezen gemeente behandelt ook aanvragen van niet-ingezetenen (Paspoortbesluit art. 3.2, 4.2). De Nederlandse identiteitskaart heeft een eigen wet, maar valt voor vermissing, signalering en inhouding ook onder de Paspoortwet (art. 1 onder u, 25, 50b).

Het reisdocument eindigt door verval van rechtswege, bijvoorbeeld na vermissing, wijziging van de naam of overlijden, of door vervallenverklaring op verzoek van een tot signalering bevoegd orgaan; de burgemeester houdt het in en onttrekt het definitief aan het verkeer (Paspoortwet art. 44, 47, 54). Het blijft rijkseigendom; de minister laat het maken en houdt het register vermiste of vervallen reisdocumenten, het basisregister reisdocumenten en het register paspoortsignaleringen bij (art. 2, 4a, 4c, 25).

De bedrijfsprocessen leveren de diensten van de UPL voor reisdocumenten (paspoort, identiteitskaart, vluchtelingen- en vreemdelingenpaspoort) en de melding van vermissing. De gemeente legt de uitgereikte Nederlandse reisdocumenten en de signalering vast in categorie 12 van de persoonslijst (HUP Reisdocument).

### Synoniemen

| Synoniem | Context |
|---|---|
| Reisdocumenten | dagelijks gebruik |

### Naamkeuze

Infinitief met object in GEMMA-volgorde, zoals Beheren grafrechten: het proces omvat de hele levensloop van het reisdocument, ook vermissing, inhouding en verval. Verstrekken reisdocumenten is overwogen, maar verstrekking is in de Paspoortwet alleen de beslissing tot uitreiking (art. 1 onder d) en wordt een deel van Behandelen aanvraag reisdocument.

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Behandelen aanvraag reisdocument](behandelen-aanvraag-reisdocument.md), [Behandelen aanvraag reisdocument niet-ingezetene](behandelen-aanvraag-reisdocument-niet-ingezetene.md), [Inhouden reisdocument](inhouden-reisdocument.md), [Verwerken vermissing reisdocument](verwerken-vermissing-reisdocument.md).
- **Beleidsdomeinindeling**: beleidsdomein Burgerzaken, taakveld 0 Bestuur en Ondersteuning (van het kernobject).
- **Kernobject**: [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md).
- **Functie-indeling naar domein, bediend door**: [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, beslisser: de burgemeester is bevoegd tot verstrekking, uitreiking, weigering, vervallenverklaring en inhouding (Paspoortwet art. 40, 42, 44, 50b); de Houder van het reisdocument vraagt aan en levert in (art. 1, 28, 32). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de aanvraag van een reisdocument (Paspoortwet art. 27). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een uitgereikt reisdocument, en aan het eind een vervallen, ingehouden of aan het verkeer onttrokken reisdocument (Paspoortwet art. 42, 47, 54). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk reisdocument dat wordt aangevraagd. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, paspoortwet hoofdstuk IV tot en met VIII; Paspoortbesluit hoofdstuk 2 tot en met 7. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat de levensloop van het reisdocument: aanvraag, verstrekking, uitreiking, wijziging, vermissing, inhouding, vervallenverklaring, verval en definitieve onttrekking aan het verkeer (Paspoortwet art. 1). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Beheren reisdocumenten | verstrekt, reikt uit en onttrekt aan het verkeer *toegang (registreren)* | [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1, 40, 42, 54) |
| Beheren reisdocumenten | omvat *aggregatie* | [Behandelen aanvraag reisdocument](behandelen-aanvraag-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 26-41) |
| Beheren reisdocumenten | omvat *aggregatie* | [Verwerken vermissing reisdocument](verwerken-vermissing-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 5a; HUP Inhouding) |
| Beheren reisdocumenten | omvat *aggregatie* | [Vermissing van het reisdocument](../../../gebeurtenissen/vermissing-van-het-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder k) |
| Beheren reisdocumenten | omvat *aggregatie* | [Inhouden reisdocument](inhouden-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 50b-57) |
| Beheren reisdocumenten | omvat *aggregatie* | [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 47) |
| Beheren reisdocumenten | omvat *aggregatie* | [Behandelen aanvraag reisdocument niet-ingezetene](behandelen-aanvraag-reisdocument-niet-ingezetene.md) | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2) |
| Beheren reisdocumenten | omvat *aggregatie* | [Inlevering van het reisdocument](../../../gebeurtenissen/inlevering-van-het-reisdocument.md) | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 56) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | bedient *bediening* | Beheren reisdocumenten | [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (Paspoortwet art. 40, 42) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) | Paspoortbesluit |
| [HUP Inhouding, inlevering of vermissing](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor reisdocumenten; de functie Officiële documenten verstrekking bedient het, en het generieke proces Behandelen aanvraag product noemt het paspoort als voorbeeld.

Procesarchitectuur-terugmeldingen:

- [Nummer 20](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, open): **GEMMA Online, Proceshiërarchie:** het hoogste niveau van de hiërarchie is het klant-tot-klant- of bedrijfsproces; daarboven spreekt GEMMA van clusters van bedrijfsprocessen: een groepering van bedrijfsprocessen die bij elkaar horen omdat ze op hetzelfde thema betrekking hebben, bijvoorbeeld personeelszaken ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 91). **Bevinding:** het processenlandschap van het GEMMA-model deelt de uitvoerende processen alleen in naar soort werk (Uitvoeren, Handhaven, Nazorgen, Ontwikkelen; GEMMA type Bedrijfsproces (cluster)). Alleen de ondersteunende tak heeft clusters per thema, zoals Beheren personeel, zonder bedrijfsprocessen eronder. Het model groepeert de bedrijfsprocessen per kernobject in een levensloopproces: het gedrag over de levensloop van één kernobject van begin tot eind (Beheren grafrechten, Beheren graven, Bijhouden persoonsgegevens, Beheren reisdocumenten), met GEMMA type Bedrijfsproces (cluster). Daarboven staan het beleidsdomein en het taakveld, afgeleid uit het kernobject. **Voorstel:** neem het levensloopproces op als cluster per thema voor de uitvoerende processen, naast de indeling naar soort werk, die blijft; zie de themaclusters van de ondersteunende tak (Beheren personeel, Beheren financiën) als groepering per beleidsdomein, met levensloopprocessen per kernobject eronder, zoals in de uitvoerende tak.

### Besluiten redacteur

- 2026-10-07: Geen ketenproces: de minister voert tegenover de houder geen eigen deel uit. De documentsoorten zijn specialisaties zonder pagina met de wetsterm; de diensten houden de UPL-naam. *Zekerheid: logica.*
