---
id: proceshierarchie
type: doc
titel: 'Processen: niveaus, klant-tot-klant en ketensamenwerking'
bijgewerkt: '2026-10-08'
bronnen:
- 2026-vng-gemma-proceshierarchie
- 2026-vng-gemma-impact-ketensamenwerking
- 2026-vng-over-gemma
- 2026-vng-gemma-2026-10-02
- 2026-rijk-paspoortwet-bwbr0005212
---

# Processen: niveaus, klant-tot-klant en ketensamenwerking

Bronnen: [Proceshiërarchie](../bronanalyses/algemeen/overig/2026-vng-gemma-proceshierarchie.md) (PH) · [Impact van ketensamenwerking](../bronanalyses/algemeen/overig/2026-vng-gemma-impact-ketensamenwerking.md) (IK) · [Over GEMMA](../bronanalyses/algemeen/overig/2026-vng-over-gemma.md) (OG)

Welke procesniveaus kent het model, wanneer is iets een bedrijfsproces en geen deelproces, en hoe modelleren we een keten? Deze pagina legt de procesniveaus van de wiki naast de GEMMA-procesarchitectuur op GEMMA Online. Regelnummers met PH of IK verwijzen naar de tekst van die pagina's, regelnummers met OG naar Over GEMMA; wat de bronnen zeggen, staat in hun bronanalyse. Sinds 2026-10-08 staan hier ook de toets klant-tot-klant en de procesniveaus en processtructuur uit [Indelingen](indelingen.md). Het GEMMA-model is gelezen via `tools/gemma.py`. Aanleiding: de naam *taak* voor het bovenste procesniveau was onduidelijk en lag dicht bij het Iv3-taakveld (sessie redacteur 2026-10-07/08). Het besluit staat onderaan en in [Indelingen](indelingen.md); het is op 2026-10-08 uitgewerkt in de criteria, de scripts en de beoordelingen, met de besluiten per geval in [Besluiten van de redacteur](../besluiten/per-begrip.md) en de procesarchitectuur-terugmeldingen 4, 5 en 20.

## Wat de bronnen zeggen

De ladder van bedrijfsproces tot handeling, de clusters, de specialisatie en de ketensamenwerking staan in de bronanalyse van [Proceshiërarchie](../bronanalyses/algemeen/overig/2026-vng-gemma-proceshierarchie.md); de soorten ketens (orkestratie, estafette) in die van [Impact van ketensamenwerking](../bronanalyses/algemeen/overig/2026-vng-gemma-impact-ketensamenwerking.md). De tegenspraak met het kennismodel (OG 564, 590) gaat als procesarchitectuur-terugmelding naar GEMMA.

## Het processenlandschap van GEMMA

Elementen met GEMMA type *Bedrijfsproces (cluster)* in de map *Procesarchitectuur / Processenlandschap*. Uitvoerend: *Uitvoerende (primaire) processen* → soort werk (*Uitvoeren*, *Handhaven*, *Nazorgen*, *Ontwikkelen*, *Samenwerken in de keten*) → onder *Uitvoeren* en *Ontwikkelen* een fijnere soort werk (*Verstrekken producten en diensten*, *Informeren*, *Organiseren*, *Exploiteren*) → generiek bedrijfsproces (*Behandelen aanvraag vergunning of ontheffing*, *Behandelen aangifte of melding*). Ondersteunend: *Ondersteunende processen* → *Beheren en ontwikkelen* → clusters per thema die "corresponderen met de bedrijfsfunctie" (*Beheren personeel*, *Beheren financiën*), zonder bedrijfsprocessen eronder. Het landschap deelt in naar soort werk; ketenprocessen en een indeling naar thema of kernobject kent het voor de uitvoerende processen niet.

## Procesniveaus

De niveaus volgen sinds 2026-10-08 de ladder van GEMMA Online, Proceshiërarchie (PH); de afweging staat op deze pagina. Tot dan lagen de niveaus van de wiki één trede hoger: een taak boven de processen per kernobject, en wat nu bedrijfsproces heet, heette deelproces.

- **Levensloopproces**: per kernobject het gedrag over de levensloop van één exemplaar, van begin tot eind (*Beheren grafrechten*: van uitgifte tot verval). In GEMMA een cluster van bedrijfsprocessen over één thema (PH 91), met GEMMA type *Bedrijfsproces (cluster)*; in ArchiMate een business-process. Per kernobject één; het taakveld en beleidsdomein zijn die van het kernobject. Binnen een ketensamenwerking mag een kernobject één levensloopproces per partij hebben, als die samen de bedrijfsinteractie met dat kernobject bedienen (besluit 2026-10-08).
- **Bedrijfsproces**: klant-tot-klant, onder verantwoordelijkheid van één organisatie, en het levert een product, dienst of besluit (PH 47, 81): één mutatie in de levensloop van een kernobject (*Verlenen grafrecht*). Vaak een specialisatie van een generiek GEMMA-bedrijfsproces (*Behandelen aanvraag product*); een specialisatie is geen niveau (PH 95). Bedrijfsprocessen leveren de producten en diensten.
- **Deelproces**: in de betekenis van GEMMA een deel van een bedrijfsproces binnen één bedrijfsfunctie, dat een deeldienst levert (PH 83). Meestal geen pagina; de tekst gaat naar het bedrijfsproces.
- **Cluster naar soort werk**: de bedrijfsprocessen van één soort, als specialisatie van een generiek GEMMA-bedrijfsproces. Alleen bij minstens twee bedrijfsprocessen; anders specialiseert het bedrijfsproces zelf.
- **Processtap**, **handeling**: geen pagina (regel 560, 563).

Geen procesniveau zijn:
- **Taak**: vervalt. Boven het levensloopproces staan de groeperingen beleidsdomein en taakveld uit de Beleidsdomeinindeling; het beleidsdomein volgt uit het kernobject, want een bedrijfsobject heeft één beleidsdomein.
- **Ketenproces**: waar de bedrijfsprocessen van meer partijen samenkomen, is dat een **ketensamenwerking**: een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen en uitgevoerd door een bedrijfssamenwerking of hun rollen (PH 146; GEMMA-element *Ketensamenwerking*). Het ketenproces erboven is impliciet: het hoeft niet afgesproken te zijn of te bestaan, en staat alleen in de beschrijving van de interactie. Een keten kan ook orkestratie zijn: één partij is verantwoordelijk en de andere voeren onder haar aansturing een deel uit (IK 27-34); de gemeente levert dan een dienst aan derden.

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
- **Ketens**: een keten wordt een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen en uitgevoerd door een bedrijfssamenwerking. Het ketenproces erboven is impliciet en hoeft niet afgesproken te zijn of te bestaan; het staat alleen in de beschrijving van de interactie. Per keten blijkt bij de herbeoordeling of het ketensamenwerking is (estafette) of orkestratie, waarbij de gemeente een dienst aan derden levert (GEMMA *Leveren dienst aan derden*); VOG en Nederlanderschap bleken orkestratie, Bezorgen stoffelijk overschot een estafette (besluiten 2026-10-08).
- **Naam**: *levensloopproces*, het proces over de levensloop van één kernobject (*Beheren grafrechten*: van uitgifte tot verval). Afgewezen: *procescluster* (te vaag; GEMMA gebruikt het op drie niveaus), *themacluster* (niet duidelijk), *taak* (botst met taakveld), *kernobjectcluster* (technischer).
- **Aansluiting**: GEMMA's themaclusters in de ondersteunende tak (*Beheren personeel*) liggen op het niveau van een beleidsdomein (HR) maar zijn een proces; voorstel aan GEMMA via een terugmelding.

## Eén levensloopproces per kernobject

Een gemeente levert 500 externe en 215 interne producten en diensten (UPL-lijsten); GEMMA dekt ze met zo'n 50 generieke bedrijfsprocessen. Eén bedrijfsproces per product of dienst volgt de definitie van GEMMA (klant-tot-klant, PH 81), maar zonder groepering wordt het model plat. Eén levensloopproces per kernobject groepeert ze: herkenbaar per beleidsdomein, en het aantal groeit met het aantal kernobjecten, niet met het aantal producten. Het cluster naar soort werk houdt de aansluiting op het processenlandschap. GEMMA kent ook processen die een levensloop omvatten (*Onderhouden*, *Heffen en innen*).

## Bedrijfsproces of deelproces: de toets klant-tot-klant

Aanleiding: een opmerking van de redacteur op 2026-10-08 over [Beheren reisdocumenten](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md). De deelprocessen daarin triggeren elkaar: Behandelen aanvraag reisdocument leidt tot Uitreiken reisdocument, en Inhouden reisdocument leidt tot Vervallen verklaren reisdocument. Dat zijn niet steeds aparte bedrijfsprocessen. Deze analyse zoekt uit hoe vaak dit voorkomt, hoe het is ontstaan en wat moet veranderen. Regelnummers met PH verwijzen naar de tekst van Proceshiërarchie ([bronanalyse](../bronanalyses/algemeen/overig/2026-vng-gemma-proceshierarchie.md)).

### Wat GEMMA zegt

- **Bedrijfsproces** (PH 81): "een onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerde, geordende reeks deelprocessen, gerelateerd aan een interne of externe klant en gericht op het leveren van een dienst aan die klant", ook wel klant-tot-klantproces. Het hoogste niveau van de ladder (PH 47).
- **Deelproces** (PH 83): "een onder verantwoordelijkheid van één bedrijfsfunctie uitgevoerde, geordende reeks processtappen, gericht op het leveren van een deeldienst die een noodzakelijke of gewenste bijdrage levert aan een uiteindelijk aan de klant te leveren dienst".

Daaruit volgt de toets: een bedrijfsproces begint bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis, een termijn) en loopt door tot het resultaat voor die klant. Wat voor hetzelfde geval op een ander proces volgt en pas samen met dat proces de dienst levert, is een deelproces van één bedrijfsproces.

### Hoe het is ontstaan

Vóór 2026-10-08 had de wiki het niveau deelproces voor alles wat *bijdrage aan groter proces* had, en een pagina kreeg het bij *eigen besluit*, *eigen normering* of *levert aanbod*. De drempel was dus: verdient het een eigen pagina? Daaronder lag de processtap, zonder pagina.

Bij het besluit van 2026-10-08 (procesniveaus volgens de GEMMA-ladder) is die regel één niveau omhoog geschoven: wat deelproces heette werd bedrijfsproces, en de oude processtap werd deelproces of processtap zonder pagina. De drempel is niet aangepast. `tools/bepaal_type.py` (`_niveau_proces`) maakt nog steeds een bedrijfsproces van alles met *bijdrage aan groter proces* en één van de drie kenmerken. Maar *eigen normering* is geen toets op klant-tot-klant: Paspoortwet art. 42 regelt de uitreiking apart ("De uitreiking volgt … uiterlijk binnen twee weken … na de verstrekking", [Paspoortwet](../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md)), en daardoor werd Uitreiken reisdocument een bedrijfsproces.

Drie dingen vangen dit nu niet af:

1. **Geen kenmerk voor klant-tot-klant.** *Aanleiding* vraagt alleen óf er een gebeurtenis, verzoek of termijn is, niet of dat een aanleiding van buiten is of de afloop van een ander proces voor hetzelfde geval. Bij Uitreiken reisdocument is de aanleiding de verstrekking.
2. **Eigen besluit en eigen normering bepalen het niveau.** Ze zeggen iets over hoe belangrijk een stap is, niet over waar het klant-tot-klantproces begint en eindigt.
3. **Geen controle op triggering.** De hiërarchiecontrole kijkt naar aggregatie (één levensloopproces per bedrijfsproces), niet naar een bedrijfsproces dat een ander bedrijfsproces van hetzelfde levensloopproces triggert voor hetzelfde geval.

### Omvang

Er zijn 63 bedrijfsprocessen. Twee signalen wijzen op een deelproces dat als bedrijfsproces is opgenomen: (a) een ander bedrijfsproces triggert het voor hetzelfde geval, en (b) het realiseert geen dienst. Per geval is het oordeel van de AI gegeven; de redacteur beslist bij de herbeoordeling.

#### Vervolg van een ander bedrijfsproces voor hetzelfde geval: deelproces

| Proces | Getriggerd door | Dienst | Oordeel |
|---|---|---|---|
| [Uitreiken reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitreiken-reisdocument.md) | Behandelen aanvraag reisdocument, ook de variant voor niet-ingezetenen | geen | deelproces: de dienst Paspoort of Identiteitskaart is pas geleverd bij uitreiking (Paspoortwet art. 42 lid 2) |
| [Uitreiken rijbewijs](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitreiken-rijbewijs.md) | Behandelen aanvraag rijbewijs, Behandelen aanvraag omwisseling buitenlands rijbewijs | geen | deelproces, zoals bij het reisdocument |
| [Vervallen verklaren reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/vervallen-verklaren-reisdocument.md) | Inhouden reisdocument | geen | deelproces: na inhouding op een mededeling over een signalering gaat de burgemeester na of de gronden nog bestaan en beslist hij (Paspoortwet art. 44 lid 2 en 4, 53) |
| [Houden naturalisatieceremonie](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md) | Behandelen naturalisatieverzoek, Behandelen optieverklaring | één | deelproces van beide: de verkrijging gaat pas in na de ceremonie; de dienst hoort bij het verzoek of de optie |
| [Voltrekken huwelijk](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md), [Registreren partnerschap](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-partnerschap.md) | Behandelen melding voorgenomen huwelijk of partnerschap | drie en één | twijfel: de klant wil trouwen, de melding is de start; maar melding en voltrekking zijn aparte producten in de UPL, en de omzetting van een partnerschap begint met een eigen verzoek |

#### Eigen aanleiding, maar mogelijk deel van een ander geval

| Proces | Oordeel |
|---|---|
| [Schouwen stoffelijk overschot](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | twijfel: de verklaring is een voorwaarde voor het verlof, maar een andere partij (de gemeentelijk lijkschouwer) voert het uit bij elk overlijden |
| [Bijzetten of verstrooien van de as](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzetten-of-verstrooien-van-de-as.md) | twijfel: dezelfde houder, hetzelfde stoffelijk overschot, minstens een maand na de crematie; mogelijk deelproces van Uitvoeren lijkbezorging |
| [Inhouden reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | blijft bedrijfsproces bij inlevering of het aantreffen van een vervallen document; bij een signalering is het het begin van het bedrijfsproces dat eindigt in de vervallenverklaring |

#### Ambtshalve, met een eigen aanleiding: bedrijfsproces blijft

Ruimen graf, Vervallen verklaren grafrecht, Sluiten begraafplaats, Treffen maatregel bij besmet stoffelijk overschot, Wijzigen identificatienummers en Verlenen vergunning bijzonder crematorium realiseren geen dienst, maar beginnen bij een eigen gebeurtenis, termijn of aanvraag en lopen door tot het resultaat. GEMMA laat de klant ook intern zijn (PH 81). Verlenen verlof tot begraving of crematie volgt op Opmaken akte van overlijden, maar hoort bij een ander kernobject en begint met een eigen aanvraag (Wlb art. 18): ook bedrijfsproces.

### Gebeurtenis en deelproces

Vraag van de redacteur: betekent de keten bij vermissing dat een gebeurtenis een deelproces triggert? De keten is nu: gebeurtenis Vermissing van het reisdocument → Verwerken vermissing reisdocument → gebeurtenis Verval van het reisdocument → Inhouden reisdocument → Vervallen verklaren reisdocument.

Een gebeurtenis heeft in het model twee plaatsen:

- **Aanleiding van buiten**: de klant, een derde, het recht of een termijn (Vermissing, Overlijden, Verhuizing). Zo'n gebeurtenis start een bedrijfsproces. Triggert ze iets wat een deelproces lijkt, dan is dat in feite het begin van een eigen bedrijfsproces, of het is geen deelproces van dat ene geval.
- **Resultaat van een bedrijfsproces**: een rechtsgevolg dat het proces teweegbrengt (Verval van het reisdocument, Verkrijging van het Nederlanderschap). Zo'n gebeurtenis kan elders een bedrijfsproces starten. Een tussentoestand binnen één bedrijfsproces (verstrekt, ingehouden) is geen element: deelprocessen hebben meestal geen pagina, en de volgorde staat in de beschrijving van het bedrijfsproces.

Een gebeurtenis triggert dus altijd een bedrijfsproces, nooit een deelproces. Voor de vermissing betekent dat:

- Vermissing triggert één bedrijfsproces, Verwerken vermissing reisdocument; dat eindigt met het verval van rechtswege (Paspoortwet art. 47 lid 1 onder j).
- De triggering Verval van het reisdocument → Inhouden reisdocument klopt niet. Het verval zelf start geen gemeentelijk gedrag; de inhouding volgt pas als het vervallen document wordt ingeleverd of aangetroffen, soms nooit. Het verval is dan een voorwaarde (associatie), en de aanleiding is de inlevering.
- Inhouden op een signalering (art. 53) en Vervallen verklaren (art. 44) vormen één bedrijfsproces, gestart door de mededeling van de minister (art. 25 lid 4), met de vervallenverklaring of de teruggave als resultaat.

### Wat moet veranderen

Repareren en voorkomen, in deze volgorde. De besluiten van de redacteur en de uitwerking staan in de laatste sectie.

1. **Kenmerk *klant tot klant*** in de criteria (`tools/bepaal_type.py`, criteria-skill, `docs/kenmerken.md`): "Begint het bij een aanleiding van buiten het proces (verzoek of melding van een klant, gebeurtenis, termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? Noem begin en eind." Bron: PH 81, 83.
2. **Beslisregel stap 7** (`_niveau_proces`, `naslag/beslistabel.md`): *bijdrage aan groter proces* met *klant tot klant* ja wordt bedrijfsproces; zonder wordt het deelproces of processtap. *Eigen besluit* en *eigen normering* bepalen het niveau niet meer. *Levert aanbod* zonder *klant tot klant* wordt voorgelegd: de dienst hoort bij het bedrijfsproces.
3. **Pagina voor een deelproces?** Nu krijgt een deelproces geen pagina en gaan tekst en relaties naar het bedrijfsproces. Alternatief: een deelproces met eigen normering krijgt een pagina, met procesniveau deelproces, geaggregeerd door zijn bedrijfsproces; dan blijven de Archi-objecten (Uitreiken reisdocument) bestaan.
4. **Controles** (hiërarchiecontrole in `tools/bepaal_type.py`): een fout of voorleggen bij (a) een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert, en (b) een gebeurtenis die een deelproces triggert.
5. **Herbeoordelen** de processen uit de tabellen hierboven, en de triggering Verval van het reisdocument → Inhouden reisdocument; de definities van de bedrijfsprocessen die een deelproces opnemen lopen dan tot het eindresultaat (Behandelen aanvraag reisdocument: tot uitreiking of weigering).

### Uitwerking (besluiten redacteur 2026-10-08)

Stand: het kenmerk *klant tot klant* en de controles op triggering staan in skill gemma-archimate-model-criteria (Procesniveau) en `tools/bepaal_type.py`; het besluit staat in [Besluiten over de werkwijze](../besluiten/werkwijze.md), thema 2.

- **Kenmerk en beslisregel**: *klant tot klant* is een nieuw kenmerk; alleen dat maakt van *bijdrage aan groter proces* een bedrijfsproces. Een deelproces dat een dienst levert, wordt voorgelegd. Alle 432 beoordelingen hebben het kenmerk: 58 processen zijn klant-tot-klant, 9 zijn deelproces of processtap, de rest is niet van toepassing.
- **Geen pagina voor een deelproces**: het bedrijfsproces beschrijft zijn deelprocessen in het veld `deelprocessen`, in volgorde en met bron, op de pagina (sectie Deelprocessen) en in Archi als property *wiki-gemma-model deelprocessen*. De beoordeling van het deelproces blijft, als onderdeel zonder pagina; beschrijving en relaties zijn letterlijk naar het bedrijfsproces verplaatst.
- **Controles**: een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert, wordt voorgelegd; een gebeurtenis die een deelproces triggert, is een fout.
- **Deelproces geworden**: Uitreiken reisdocument (in Behandelen aanvraag reisdocument en de variant voor niet-ingezetenen), Uitreiken rijbewijs (in Behandelen aanvraag rijbewijs en de omwisseling), Vervallen verklaren reisdocument (in Inhouden reisdocument), Houden naturalisatieceremonie (in Behandelen naturalisatieverzoek en Behandelen optieverklaring), Behandelen melding voorgenomen huwelijk of partnerschap (in Voltrekken huwelijk en Registreren partnerschap), Bijzetten of verstrooien van de as (in Uitvoeren lijkbezorging). Hun objecten in Archi vervallen.
- **Vermissing en inlevering**: Verwerken vermissing reisdocument eindigt bij de registratie en het verval. De processtap Inlevering reisdocument is de gebeurtenis Inlevering van het reisdocument geworden (Paspoortwet art. 56); die triggert Inhouden reisdocument, het bedrijfsproces voor elke inlevering. Verval van het reisdocument verplicht de houder tot inlevering en triggert de inhouding niet meer zelf.
- **Overlijden**: Schouwen stoffelijk overschot blijft een bedrijfsproces en geeft de verklaring van overlijden door aan Verlenen verlof tot begraving of crematie (Wlb art. 7, 12).
- **Gevolgen om te volgen**: het levensloopproces Begraven en cremeren stoffelijk overschot omvat nu één bedrijfsproces, Uitvoeren lijkbezorging (een 1-op-1-aggregatie); procesarchitectuur-terugmelding 4 (opgelost) noemt nog Behandelen melding voorgenomen huwelijk of partnerschap en Houden naturalisatieceremonie als element.

## Toets aan het Kennismodel procesarchitectuur

Het kennismodel (regel 544-606) is work in progress.

| Kennismodel (regel) | Wiki | Oordeel |
|---|---|---|
| Actor → toewijzing → Rol (602) | actor alleen via een rol | volgt |
| Rol → toewijzing → Deelproces (599) | rol aan bedrijfsproces (het deelproces heeft meestal geen pagina) | volgt |
| Product → bediening → Klant (596) | *afnemer* noemt een specialisatie van Klant; het product bedient die rol | volgt (toegevoegd) |
| Product → associatie → Beleidskader (595) | *is grondslag voor* bij voorkeur van een product, tijdelijk van proces of dienst | volgt, met overgang |
| Product → aggregatie → Dienst (593) | *omvat diensten en afspraken* | volgt |
| Bedrijfsfunctie ↔ bediening ↔ Bedrijfsproces (597, 604) | *bedient gedrag* | volgt |
| Bedrijfsproces → aggregatie → Deelproces → Processtap → Handeling (605, 601, 589) | procesniveaus; deelproces, processtap en handeling meestal zonder pagina | volgt |
| Bedrijfsproces → toegang → Bedrijfsobject (606) | kernobject via toegang | volgt |
| Procescluster → aggregatie → Bedrijfsproces, Procescluster (419-420) | levensloopproces en cluster naar soort werk | volgt |
| Deelproces → realisatie → Deelservice (398) | een bedrijfsproces levert een dienst | volgt (tot 2026-10-08 een afwijking: het deelproces van de wiki leverde een dienst) |
| Ketenproces → aggregatie → Bedrijfsproces (590) | ketensamenwerking als bedrijfsinteractie, bediend door de bedrijfsprocessen (PH 146) | afwijking van het kennismodel, in lijn met de pagina Proceshiërarchie; terugmelding |
| Relaties tussen actoren: niet in het kennismodel | alleen structurele relaties | aanvulling |
| Gebeurtenis: niet in deze view | uit het uitgebreide kennismodel (regel 915, 924) | aanvulling |

De afwijkingen en aanvullingen gaan als voorstel naar het GEMMA-team (todo).

## Besluiten van de redacteur

| Datum | Besluit | Stand |
|---|---|---|
| 2026-10-08 | De procesniveaus volgen de GEMMA-ladder (PH 47, 81-83): wat de wiki deelproces noemde (levert een product of dienst, klant-tot-klant) wordt bedrijfsproces; wat de wiki bedrijfsproces noemde (levensloop van één kernobject) wordt **levensloopproces**, met GEMMA type *Bedrijfsproces (cluster)*; deelproces krijgt de GEMMA-betekenis (binnen één bedrijfsfunctie, levert een deeldienst). | skill criteria (Procesniveau) |
| 2026-10-08 | Het procesniveau taak vervalt. Boven het levensloopproces staan de groeperingen beleidsdomein en taakveld uit de Beleidsdomeinindeling; het beleidsdomein van een levensloopproces volgt uit zijn kernobject. Herziet de besluiten van 2026-10-04 over de taak (processtructuur, taak in de Beleidsdomeinindeling) in [Indelingen](indelingen.md). | skill criteria (Procesniveau) |
| 2026-10-08 | Ketensamenwerking wordt een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen (PH 146); het ketenproces is geen niveau en geen element, en staat alleen impliciet in de beschrijving van de interactie. Herziet de besluiten van 2026-10-07 over ketenproces, bedrijfsproces en deelproces in [Besluiten van de redacteur](../besluiten/per-begrip.md). De tegenspraak met het kennismodel (OG 590) wordt een procesarchitectuur-terugmelding. | skill criteria (Ketensamenwerking); procesarchitectuur-terugmelding 5 |
| 2026-10-08 | De procesindeling naar soort werk blijft naast de procesindeling naar kernobject bestaan, ongewijzigd. | skill criteria (Procesniveau: cluster naar soort werk) |
| 2026-10-08 | Per kernobject één levensloopproces, of één per partij als ze samen een bedrijfsinteractie met dat kernobject bedienen (Toestaan lijkbezorging en Begraven en cremeren stoffelijk overschot in de ketensamenwerking Bezorgen stoffelijk overschot). Een estafette wordt een bedrijfsinteractie; bij orkestratie is er geen interactie, en het deel dat de gemeente voor een ander uitvoert, specialiseert *Leveren dienst aan derden* (VOG, naturalisatie). Een beleidsdomein krijgt zijn beschrijving in het register `beoordelingen/beleidsdomeinen.yaml`. Zie [Besluiten van de redacteur](../besluiten/per-begrip.md). | skill criteria (Procesniveau, Ketensamenwerking); tools/bepaal_type.py |
