---
id: proceshierarchie
type: analyse
titel: Proceshiërarchie, levensloopprocessen en ketensamenwerking
bijgewerkt: '2026-10-08'
bronnen:
- 2026-vng-gemma-proceshierarchie
- 2026-vng-gemma-impact-ketensamenwerking
- 2026-vng-over-gemma
- 2026-vng-gemma-2026-10-02
bronanalyse_van:
- 2026-vng-gemma-proceshierarchie
- 2026-vng-gemma-impact-ketensamenwerking
---

# Proceshiërarchie, levensloopprocessen en ketensamenwerking

Bronnen: Proceshiërarchie (PH) [tekst](../../../sources/raw/2026-vng-gemma-proceshierarchie.md) · [origineel (html)](../../../sources/raw/2026-vng-gemma-proceshierarchie.html) · [online](https://www.gemmaonline.nl/wiki/Procesarchitectuur_Proceshi%C3%ABrarchie) · Impact van ketensamenwerking (IK) [tekst](../../../sources/raw/2026-vng-gemma-impact-ketensamenwerking.md) · [origineel (html)](../../../sources/raw/2026-vng-gemma-impact-ketensamenwerking.html) · [online](https://www.gemmaonline.nl/wiki/Procesarchitectuur_Impact_van_ketensamenwerking)

Deze analyse legt de procesniveaus van de wiki naast de GEMMA-procesarchitectuur op GEMMA Online, en is de bronanalyse van de pagina's Proceshiërarchie (PH) en Impact van ketensamenwerking (IK). Regelnummers met PH of IK verwijzen naar de tekst van die pagina's, regelnummers met OG naar Over GEMMA ([tekst](../../../sources/raw/2026-vng-over-gemma.md)). Het GEMMA-model is gelezen via `tools/gemma.py`. Aanleiding: de naam *taak* voor het bovenste procesniveau was onduidelijk en lag dicht bij het Iv3-taakveld (sessie redacteur 2026-10-07/08). Het besluit staat onderaan en in [Indelingen](indelingen.md); de uitwerking staat in `todo.md`.

## Wat de bronnen zeggen

- **Ladder**: bedrijfsproces → deelproces → processtap → handeling, als aggregatie; "het hoogste niveau dat we in deze hiërarchie onderkennen is het klant-tot-klant- ofwel bedrijfsproces" (PH 47). Een bedrijfsproces is "onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerd […] gericht op het leveren van een dienst aan die klant" (PH 81); een deelproces valt onder één bedrijfsfunctie en levert een deeldienst (PH 83). De ladder geldt voor sturende, uitvoerende en ondersteunende processen (PH 35-43, 89).
- **Clusters**: "clusters van bedrijfsprocessen […] die bij elkaar horen omdat ze op hetzelfde 'thema' betrekking hebben", bijvoorbeeld personeelszaken (PH 91). Het kennismodel kent het type Procescluster, dat bedrijfsprocessen en procesclusters aggregeert (OG 409, 419-420).
- **Specialisatie**: geen extra niveau in de ladder, maar gemeenschappelijkheid en verbijzondering (PH 95).
- **Ketensamenwerking**: twee bedrijfsprocessen van twee organisaties raken elkaar, zonder overkoepelende aansturing (PH 144). "Ketensamenwerking wordt soms aangeduid als 'ketenproces', een proces op een hoger niveau dan de eigen bedrijfsprocessen. […] vanuit de procesarchitectuur gezien niet correct"; ArchiMate: een bedrijfsinteractie waarin de bedrijfsprocessen van de partijen samenkomen (PH 146). Uitbesteding van een deelproces of processtap is een klant-leverancierrelatie (PH 148). In het GEMMA-model is *Ketensamenwerking* een business-interaction (map *Procesarchitectuur / Ketensamenwerking*) die *Bedrijfsproces 1* en *Bedrijfsproces 2* bedienen.
- **Soorten ketens**: orkestratiemodel (één partij verantwoordelijk, de andere voeren onder haar aansturing deelprocessen uit), estafettemodel (gerelateerde processen onder verantwoordelijkheid van elke schakel, afhankelijk zonder aansturing, zoals de VTH-keten) en de keten van gezamenlijke beleidsdoelen (IK 27-34).
- **Tegenspraak**: het kennismodel heeft wél *Ketenproces → aggregatie → Bedrijfsproces* (OG 564, 590). De pagina Proceshiërarchie werkt uit hoe GEMMA ketens modelleert en is specifieker; de tegenspraak gaat als procesarchitectuur-terugmelding naar GEMMA.

## Het processenlandschap van GEMMA

Elementen met GEMMA type *Bedrijfsproces (cluster)* in de map *Procesarchitectuur / Processenlandschap*. Uitvoerend: *Uitvoerende (primaire) processen* → soort werk (*Uitvoeren*, *Handhaven*, *Nazorgen*, *Ontwikkelen*, *Samenwerken in de keten*) → onder *Uitvoeren* en *Ontwikkelen* een fijnere soort werk (*Verstrekken producten en diensten*, *Informeren*, *Organiseren*, *Exploiteren*) → generiek bedrijfsproces (*Behandelen aanvraag vergunning of ontheffing*, *Behandelen aangifte of melding*). Ondersteunend: *Ondersteunende processen* → *Beheren en ontwikkelen* → clusters per thema die "corresponderen met de bedrijfsfunctie" (*Beheren personeel*, *Beheren financiën*), zonder bedrijfsprocessen eronder. Het landschap deelt in naar soort werk; ketenprocessen en een indeling naar thema of kernobject kent het voor de uitvoerende processen niet.

## Vergelijking met de wiki tot 2026-10-08

| Wiki | Voorbeeld | In GEMMA-termen |
|---|---|---|
| taak | Verzorgen burgerzaken | cluster per thema; valt samen met het beleidsdomein van zijn kernobjecten |
| ketenproces | Bezorgen stoffelijk overschot | ketensamenwerking (bedrijfsinteractie), geen niveau (PH 146) |
| bedrijfsproces (levensloop per kernobject) | Beheren grafrechten | cluster van bedrijfsprocessen over één kernobject (PH 91) |
| deelproces (levert product of dienst) | Behandelen aanvraag rijbewijs, specialisatie van *Behandelen aanvraag product* | bedrijfsproces: klant-tot-klant, levert een dienst (PH 81); een specialisatie houdt het niveau (PH 95) |
| cluster naar soort werk | Behandelen vergunningaanvragen lijkbezorging | blijft een eigen indeling naast de procesindeling naar kernobject |

De wiki-niveaus lagen dus één niveau hoger dan de GEMMA-ladder: wat de wiki deelproces noemde, is in GEMMA een bedrijfsproces. De afwijking "een deelproces levert een dienst" (procesarchitectuur-terugmelding 4) verdwijnt als de niveaus meeschuiven.

## Uitkomst: het landschap naar kernobject

```
Taakveld Iv3          groepering (GEMMA)                         0 Bestuur en ondersteuning
└ Beleidsdomein       groepering (GGM, of nieuw met terugmelding) Burgerzaken
  └ Levensloopproces  per kernobject; GEMMA type Bedrijfsproces (cluster)   Beheren reisdocumenten
    └ Bedrijfsproces  klant-tot-klant, levert product of dienst  Behandelen aanvraag reisdocument
      └ Deelproces    binnen één bedrijfsfunctie, levert deeldienst (meestal geen pagina)
        └ Processtap → Handeling (geen pagina)

Dwarsverbanden, geen niveau:
  Ketensamenwerking   bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen
  Specialisatie       bedrijfsproces → generiek GEMMA-bedrijfsproces
  Soort werk          de eigen procesindeling naar soort werk
```

- **Boven het levensloopproces** staan twee groeperingen die al bestaan, taakveld en beleidsdomein, en geen procesniveau: een domein is een groepering, geen proces. Het is dezelfde Beleidsdomeinindeling als voor objecten, producten en beleidskaders.
- **Strikt hiërarchisch**: een bedrijfsproces hoort bij het levensloopproces van het kernobject dat het maakt of wijzigt, het levensloopproces bij het beleidsdomein van zijn kernobject, het beleidsdomein bij zijn taakveld. Een bedrijfsobject heeft één beleidsdomein, dus de plaats is afgeleid en hoeft niet per cluster gekozen te worden. Een thema dat over beleidsdomeinen heen loopt (lijkbezorging) is geen knoop in de boom maar een keten.
- **Kruisingen die al een oplossing hebben**: een GGM-beleidsdomein dat technisch is of niet past (Ingeschreven persoon, Gemeentebegrafenis) wordt een gemeentelijk beleidsdomein met een GGM-terugmelding; een product dat de UPL onder een ander taakveld zet (verlof tot begraven onder 0.2) staat niet in de procesboom en heeft al een procesarchitectuur-terugmelding; een kernobject dat veel taken gebruiken (Persoon) heeft één thuis (regel Thuishoren).
- **Ketens**: een keten wordt een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen en uitgevoerd door een bedrijfssamenwerking. Het ketenproces erboven is impliciet en hoeft niet afgesproken te zijn of te bestaan; het staat alleen in de beschrijving van de interactie. Per keten blijkt bij de herbeoordeling of het ketensamenwerking is (estafette) of orkestratie, waarbij de gemeente een dienst aan derden levert (GEMMA *Leveren dienst aan derden*); VOG en Nederlanderschap lijken orkestratie.
- **Naam**: *levensloopproces*, het proces over de levensloop van één kernobject (*Beheren grafrechten*: van uitgifte tot verval). Afgewezen: *procescluster* (te vaag; GEMMA gebruikt het op drie niveaus), *themacluster* (niet duidelijk), *taak* (botst met taakveld), *kernobjectcluster* (technischer).
- **Aansluiting**: GEMMA's themaclusters in de ondersteunende tak (*Beheren personeel*) liggen op het niveau van een beleidsdomein (HR) maar zijn een proces; voorstel aan GEMMA via een terugmelding.

## Besluiten van de redacteur

| Datum | Besluit |
|---|---|
| 2026-10-08 | De procesniveaus volgen de GEMMA-ladder (PH 47, 81-83): wat de wiki deelproces noemde (levert een product of dienst, klant-tot-klant) wordt bedrijfsproces; wat de wiki bedrijfsproces noemde (levensloop van één kernobject) wordt **levensloopproces**, met GEMMA type *Bedrijfsproces (cluster)*; deelproces krijgt de GEMMA-betekenis (binnen één bedrijfsfunctie, levert een deeldienst). |
| 2026-10-08 | Het procesniveau taak vervalt. Boven het levensloopproces staan de groeperingen beleidsdomein en taakveld uit de Beleidsdomeinindeling; het beleidsdomein van een levensloopproces volgt uit zijn kernobject. Herziet de besluiten van 2026-10-04 over de taak (processtructuur, taak in de Beleidsdomeinindeling) in [Indelingen](indelingen.md). |
| 2026-10-08 | Ketensamenwerking wordt een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen (PH 146); het ketenproces is geen niveau en geen element, en staat alleen impliciet in de beschrijving van de interactie. Herziet de besluiten van 2026-10-07 over ketenproces, bedrijfsproces en deelproces in [Besluiten van de redacteur](besluiten-redacteur.md). De tegenspraak met het kennismodel (OG 590) wordt een procesarchitectuur-terugmelding. |
| 2026-10-08 | De procesindeling naar soort werk blijft naast de procesindeling naar kernobject bestaan, ongewijzigd. |
