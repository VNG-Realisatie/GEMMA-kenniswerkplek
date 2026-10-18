---
id: stempas
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Stempas
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Persoonlijk document waarmee een kiezer bij een verkiezing kan stemmen, toegezonden door de gemeente waar hij als kiezer is geregistreerd.
match:
  ggm: geen
  gemma: geen
data_objecten:
- Stempas-data
objectniveau: kernobject
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
---

# Stempas

<!-- Gegenereerd door tools/render.py uit de beoordeling stempas.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur. De beslistabel legt dit element voor (zie *Ter discussie*).

## Ter discussie

- data-object zonder sterke GGM-match

## Betekenis

### Definitie

Persoonlijk document waarmee een kiezer bij een verkiezing kan stemmen, toegezonden door de gemeente waar hij als kiezer is geregistreerd.

### Beschrijving

Daags na de kandidaatstelling stelt de burgemeester de gegevens vast van de kiezers die op die dag in de gemeente als kiezer zijn geregistreerd; ten minste veertien dagen voor de stemming ontvangt elke kiezer een stempas met een volgnummer, naar een model van de minister (Kieswet art. J 7). Wie zijn stempas kwijt is of niet heeft ontvangen, krijgt op een schriftelijk of mondeling verzoek met een kopie van een identiteitsbewijs een nieuwe (art. J 8).

Een stempas wordt ongeldig als er een kiezerspas, volmachtbewijs, vervangende stempas of briefstembewijs voor in de plaats komt, als de houder niet als kiezer behoort te zijn geregistreerd of is overleden, of als zij is ontvreemd; de burgemeester stelt de dag voor de stemming een uittreksel uit het register van ongeldige stempassen vast en vernietigt het register drie maanden na de toelating van de gekozenen (art. J 7a). Een kiezer kan een andere kiezer machtigen door zijn stempas om te zetten in een volmachtbewijs en over te dragen (art. L 14).

Het stemmen zelf, de stembureaus en de uitslag vallen buiten dit onderwerp (afbakening Burgerzaken).

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Stempas ontvangen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) (wiki, UPL nr. 397) | De dienst waarmee de kiezer de stempas krijgt, met de UPL-naam stempas als synoniem | Deze pagina heet Stempas, het document; de dienst heet Stempas ontvangen, met de UPL-naam stempas als synoniem (precedent Briefadres aanvragen). |

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Beheren stempassen](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md).
- **Mutaties door bedrijfsprocessen**: [Behandelen verzoek om kiezerspas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md), [Behandelen verzoek om volmacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md), [Verstrekken stempas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Behandelen verzoek om kiezerspas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md), [Behandelen verzoek om volmacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md), [Beheren stempassen](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md), [Verstrekken stempas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Specialisaties

- **Vervangende stempas**: Nieuwe stempas op verzoek als de stempas in het ongerede is of niet is ontvangen; de oude wordt ongeldig (Kieswet art. J 7a lid 2 onder b, J 8). Geen eigen pagina: dezelfde gegevens en hetzelfde bedrijfsproces.
- **Kiezerspas**: Verklaring op verzoek waarmee de kiezer in een stembureau naar keuze in het gebied van de verkiezing kan stemmen; ze komt in de plaats van de stempas, die ongeldig wordt, en wordt niet vervangen (Kieswet art. K 1, K 4, J 7a lid 2 onder a). Geen eigen pagina; de dienst Kiezerspas levert haar.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Stempas | is bestemd voor *associatie (gericht)* | [Ingeschreven persoon](ingeschreven-persoon.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 1-2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verzoek om kiezerspas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md) | reikt een kiezerspas uit in plaats van de stempas *toegang (registreren)* | Stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 4, J 7a lid 2 onder a) |
| [Behandelen verzoek om volmacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md) | maakt de stempas van de volmachtgever ongeldig *toegang (beëindigen)* | Stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7a lid 2 onder a, L 11) |
| [Beheren stempassen](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md) | verstrekt, vervangt en maakt ongeldig *toegang (registreren)* | Stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 7a, J 8) |
| [Kiezer](../../../rollen/kiezer.md) | ontvangt *toegang (houder)* | Stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |
| [Verstrekken stempas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md) | verstrekt en vervangt *toegang (registreren)* | Stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 8) |

### Data-objecten

- [Stempas-data](../../../../applicatiearchitectuur/data-objecten/stempas-data.md) *realisatie*: geen GGM-entiteit (GGM-terugmelding hiaat).

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen stempas en geen ander begrip voor de verkiezingen (GGM-terugmelding 17). Ontstaat in Beheren stempassen: de burgemeester verstrekt de stempas aan elke geregistreerde kiezer ([2026-rijk-kieswet-bwbr0004627](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), art. J 7).

GGM-terugmeldingen:

- [Nummer 17](../../../../../modellen/ggm/terugmeldingen.md) (hiaat, open): **GGM:** het GGM kent geen stempas en geen ander begrip voor de gemeentelijke taak bij verkiezingen. **Bevinding:** de burgemeester stelt bij elke verkiezing de gegevens van de geregistreerde kiezers vast, verstrekt elke kiezer een stempas met volgnummer, vervangt haar op verzoek en houdt een register van ongeldige stempassen bij ([2026-rijk-kieswet-bwbr0004627](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), art. J 7, J 7a, J 8). Relevante attributen: volgnummer; kiezer (ingeschreven persoon) en verkiezing; datum van verstrekking; soort (stempas, vervangende stempas, kiezerspas, omgezet in volmachtbewijs); ongeldig, met reden (art. J 7a lid 2). **Voorstel:** opnemen in RSGBPlus of een beleidsdomein Verkiezingen, met een relatie naar IngeschrevenPersoon.

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen bedrijfsobject voor de stempas; de functie Verkiezingen gerelateerde diensten noemt het verstrekken van stempassen als voorbeeld. Nieuw voor GEMMA.
