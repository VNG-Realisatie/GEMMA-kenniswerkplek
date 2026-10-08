---
id: 2026-vng-gemma-proceshierarchie
type: bronanalyse
onderwerp: algemeen
bronnen:
- 2026-vng-gemma-proceshierarchie
relevant: ja
bijgewerkt: '2026-10-08'
---

# GEMMA Procesarchitectuur Proceshiërarchie

Bron: [tekst](../../../../../sources/raw/2026-vng-gemma-proceshierarchie.md) · [origineel (html)](../../../../../sources/raw/2026-vng-gemma-proceshierarchie.html) · [online](https://www.gemmaonline.nl/wiki/Procesarchitectuur_Proceshi%C3%ABrarchie)

## Samenvatting

Regelnummers met PH verwijzen naar de tekst van deze pagina, regelnummers met OG naar Over GEMMA. Verplaatst uit de analyse Proceshiërarchie (2026-10-08).

- **Ladder**: bedrijfsproces → deelproces → processtap → handeling, als aggregatie; "het hoogste niveau dat we in deze hiërarchie onderkennen is het klant-tot-klant- ofwel bedrijfsproces" (PH 47). Een bedrijfsproces is "onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerd […] gericht op het leveren van een dienst aan die klant" (PH 81); een deelproces valt onder één bedrijfsfunctie en levert een deeldienst (PH 83). De ladder geldt voor sturende, uitvoerende en ondersteunende processen (PH 35-43, 89).
- **Clusters**: "clusters van bedrijfsprocessen […] die bij elkaar horen omdat ze op hetzelfde 'thema' betrekking hebben", bijvoorbeeld personeelszaken (PH 91). Het kennismodel kent het type Procescluster, dat bedrijfsprocessen en procesclusters aggregeert (OG 409, 419-420).
- **Specialisatie**: geen extra niveau in de ladder, maar gemeenschappelijkheid en verbijzondering (PH 95).
- **Ketensamenwerking**: twee bedrijfsprocessen van twee organisaties raken elkaar, zonder overkoepelende aansturing (PH 144). "Ketensamenwerking wordt soms aangeduid als 'ketenproces', een proces op een hoger niveau dan de eigen bedrijfsprocessen. […] vanuit de procesarchitectuur gezien niet correct"; ArchiMate: een bedrijfsinteractie waarin de bedrijfsprocessen van de partijen samenkomen (PH 146). Uitbesteding van een deelproces of processtap is een klant-leverancierrelatie (PH 148). In het GEMMA-model is *Ketensamenwerking* een business-interaction (map *Procesarchitectuur / Ketensamenwerking*) die *Bedrijfsproces 1* en *Bedrijfsproces 2* bedienen.
- **Tegenspraak**: het kennismodel heeft wél *Ketenproces → aggregatie → Bedrijfsproces* (OG 564, 590). De pagina Proceshiërarchie werkt uit hoe GEMMA ketens modelleert en is specifieker; de tegenspraak gaat als procesarchitectuur-terugmelding naar GEMMA.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| Bedrijfsproces | onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerd, gericht op het leveren van een dienst aan die klant | klant-tot-klantproces | PH 47, 81 |
| Deelproces | valt onder één bedrijfsfunctie en levert een deeldienst | — | PH 83 |
| Cluster van bedrijfsprocessen | bedrijfsprocessen die bij elkaar horen omdat ze op hetzelfde thema betrekking hebben | Procescluster (Over GEMMA) | PH 91 |
| Ketensamenwerking | twee bedrijfsprocessen van twee organisaties raken elkaar, zonder overkoepelende aansturing | ketenproces (volgens de bron niet correct) | PH 144, 146 |

## Relaties

Geen relatietabel: de bron beschrijft typen van elementen en relaties, geen begrippen van gemeenten.

## Relevantie voor de architectuur

De procesniveaus van de wiki (levensloopproces, bedrijfsproces, deelproces) en de ketensamenwerking als bedrijfsinteractie volgen deze pagina. De afweging staat in [Processen: niveaus, klant-tot-klant en ketensamenwerking](../../../docs/proceshierarchie.md).

## Citaten

> het hoogste niveau dat we in deze hiërarchie onderkennen is het klant-tot-klant- ofwel bedrijfsproces (PH 47)

> Ketensamenwerking wordt soms aangeduid als 'ketenproces', een proces op een hoger niveau dan de eigen bedrijfsprocessen. […] vanuit de procesarchitectuur gezien niet correct (PH 146)
