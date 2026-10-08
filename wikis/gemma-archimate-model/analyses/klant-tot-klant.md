---
id: klant-tot-klant
type: analyse
titel: Bedrijfsproces of deelproces, de toets klant-tot-klant
bijgewerkt: '2026-10-08'
bronnen:
- 2026-vng-gemma-proceshierarchie
- 2026-rijk-paspoortwet-bwbr0005212
---

# Bedrijfsproces of deelproces, de toets klant-tot-klant

Aanleiding: een opmerking van de redacteur op 2026-10-08 over [Beheren reisdocumenten](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md). De deelprocessen daarin triggeren elkaar: Behandelen aanvraag reisdocument leidt tot Uitreiken reisdocument, en Inhouden reisdocument leidt tot Vervallen verklaren reisdocument. Dat zijn niet steeds aparte bedrijfsprocessen. Deze analyse zoekt uit hoe vaak dit voorkomt, hoe het is ontstaan en wat moet veranderen. Regelnummers met PH verwijzen naar de tekst van [Proceshiërarchie](proceshierarchie.md).

## Wat GEMMA zegt

- **Bedrijfsproces** (PH 81): "een onder verantwoordelijkheid van één organisatie (gemeente) uitgevoerde, geordende reeks deelprocessen, gerelateerd aan een interne of externe klant en gericht op het leveren van een dienst aan die klant", ook wel klant-tot-klantproces. Het hoogste niveau van de ladder (PH 47).
- **Deelproces** (PH 83): "een onder verantwoordelijkheid van één bedrijfsfunctie uitgevoerde, geordende reeks processtappen, gericht op het leveren van een deeldienst die een noodzakelijke of gewenste bijdrage levert aan een uiteindelijk aan de klant te leveren dienst".

Daaruit volgt de toets: een bedrijfsproces begint bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis, een termijn) en loopt door tot het resultaat voor die klant. Wat voor hetzelfde geval op een ander proces volgt en pas samen met dat proces de dienst levert, is een deelproces van één bedrijfsproces.

## Hoe het is ontstaan

Vóór 2026-10-08 had de wiki het niveau deelproces voor alles wat *bijdrage aan groter proces* had, en een pagina kreeg het bij *eigen besluit*, *eigen normering* of *levert aanbod*. De drempel was dus: verdient het een eigen pagina? Daaronder lag de processtap, zonder pagina.

Bij het besluit van 2026-10-08 (procesniveaus volgens de GEMMA-ladder) is die regel één niveau omhoog geschoven: wat deelproces heette werd bedrijfsproces, en de oude processtap werd deelproces of processtap zonder pagina. De drempel is niet aangepast. `tools/bepaal_type.py` (`_niveau_proces`) maakt nog steeds een bedrijfsproces van alles met *bijdrage aan groter proces* en één van de drie kenmerken. Maar *eigen normering* is geen toets op klant-tot-klant: Paspoortwet art. 42 regelt de uitreiking apart ("De uitreiking volgt … uiterlijk binnen twee weken … na de verstrekking", [Paspoortwet](../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md)), en daardoor werd Uitreiken reisdocument een bedrijfsproces.

Drie dingen vangen dit nu niet af:

1. **Geen kenmerk voor klant-tot-klant.** *Aanleiding* vraagt alleen óf er een gebeurtenis, verzoek of termijn is, niet of dat een aanleiding van buiten is of de afloop van een ander proces voor hetzelfde geval. Bij Uitreiken reisdocument is de aanleiding de verstrekking.
2. **Eigen besluit en eigen normering bepalen het niveau.** Ze zeggen iets over hoe belangrijk een stap is, niet over waar het klant-tot-klantproces begint en eindigt.
3. **Geen controle op triggering.** De hiërarchiecontrole kijkt naar aggregatie (één levensloopproces per bedrijfsproces), niet naar een bedrijfsproces dat een ander bedrijfsproces van hetzelfde levensloopproces triggert voor hetzelfde geval.

## Omvang

Er zijn 63 bedrijfsprocessen. Twee signalen wijzen op een deelproces dat als bedrijfsproces is opgenomen: (a) een ander bedrijfsproces triggert het voor hetzelfde geval, en (b) het realiseert geen dienst. Per geval is het oordeel van de AI gegeven; de redacteur beslist bij de herbeoordeling.

### Vervolg van een ander bedrijfsproces voor hetzelfde geval: deelproces

| Proces | Getriggerd door | Dienst | Oordeel |
|---|---|---|---|
| [Uitreiken reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitreiken-reisdocument.md) | Behandelen aanvraag reisdocument, ook de variant voor niet-ingezetenen | geen | deelproces: de dienst Paspoort of Identiteitskaart is pas geleverd bij uitreiking (Paspoortwet art. 42 lid 2) |
| [Uitreiken rijbewijs](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitreiken-rijbewijs.md) | Behandelen aanvraag rijbewijs, Behandelen aanvraag omwisseling buitenlands rijbewijs | geen | deelproces, zoals bij het reisdocument |
| [Vervallen verklaren reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/vervallen-verklaren-reisdocument.md) | Inhouden reisdocument | geen | deelproces: na inhouding op een mededeling over een signalering gaat de burgemeester na of de gronden nog bestaan en beslist hij (Paspoortwet art. 44 lid 2 en 4, 53) |
| [Houden naturalisatieceremonie](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md) | Behandelen naturalisatieverzoek, Behandelen optieverklaring | één | deelproces van beide: de verkrijging gaat pas in na de ceremonie; de dienst hoort bij het verzoek of de optie |
| [Voltrekken huwelijk](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md), [Registreren partnerschap](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-partnerschap.md) | Behandelen melding voorgenomen huwelijk of partnerschap | drie en één | twijfel: de klant wil trouwen, de melding is de start; maar melding en voltrekking zijn aparte producten in de UPL, en de omzetting van een partnerschap begint met een eigen verzoek |

### Eigen aanleiding, maar mogelijk deel van een ander geval

| Proces | Oordeel |
|---|---|
| [Schouwen stoffelijk overschot](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | twijfel: de verklaring is een voorwaarde voor het verlof, maar een andere partij (de gemeentelijk lijkschouwer) voert het uit bij elk overlijden |
| [Bijzetten of verstrooien van de as](../bedrijfsarchitectuur/bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bijzetten-of-verstrooien-van-de-as.md) | twijfel: dezelfde houder, hetzelfde stoffelijk overschot, minstens een maand na de crematie; mogelijk deelproces van Uitvoeren lijkbezorging |
| [Inhouden reisdocument](../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | blijft bedrijfsproces bij inlevering of het aantreffen van een vervallen document; bij een signalering is het het begin van het bedrijfsproces dat eindigt in de vervallenverklaring |

### Ambtshalve, met een eigen aanleiding: bedrijfsproces blijft

Ruimen graf, Vervallen verklaren grafrecht, Sluiten begraafplaats, Treffen maatregel bij besmet stoffelijk overschot, Wijzigen identificatienummers en Verlenen vergunning bijzonder crematorium realiseren geen dienst, maar beginnen bij een eigen gebeurtenis, termijn of aanvraag en lopen door tot het resultaat. GEMMA laat de klant ook intern zijn (PH 81). Verlenen verlof tot begraving of crematie volgt op Opmaken akte van overlijden, maar hoort bij een ander kernobject en begint met een eigen aanvraag (Wlb art. 18): ook bedrijfsproces.

## Gebeurtenis en deelproces

Vraag van de redacteur: betekent de keten bij vermissing dat een gebeurtenis een deelproces triggert? De keten is nu: gebeurtenis Vermissing van het reisdocument → Verwerken vermissing reisdocument → gebeurtenis Verval van het reisdocument → Inhouden reisdocument → Vervallen verklaren reisdocument.

Een gebeurtenis heeft in het model twee plaatsen:

- **Aanleiding van buiten**: de klant, een derde, het recht of een termijn (Vermissing, Overlijden, Verhuizing). Zo'n gebeurtenis start een bedrijfsproces. Triggert ze iets wat een deelproces lijkt, dan is dat in feite het begin van een eigen bedrijfsproces, of het is geen deelproces van dat ene geval.
- **Resultaat van een bedrijfsproces**: een rechtsgevolg dat het proces teweegbrengt (Verval van het reisdocument, Verkrijging van het Nederlanderschap). Zo'n gebeurtenis kan elders een bedrijfsproces starten. Een tussentoestand binnen één bedrijfsproces (verstrekt, ingehouden) is geen element: deelprocessen hebben meestal geen pagina, en de volgorde staat in de beschrijving van het bedrijfsproces.

Een gebeurtenis triggert dus altijd een bedrijfsproces, nooit een deelproces. Voor de vermissing betekent dat:

- Vermissing triggert één bedrijfsproces, Verwerken vermissing reisdocument; dat eindigt met het verval van rechtswege (Paspoortwet art. 47 lid 1 onder j).
- De triggering Verval van het reisdocument → Inhouden reisdocument klopt niet. Het verval zelf start geen gemeentelijk gedrag; de inhouding volgt pas als het vervallen document wordt ingeleverd of aangetroffen, soms nooit. Het verval is dan een voorwaarde (associatie), en de aanleiding is de inlevering.
- Inhouden op een signalering (art. 53) en Vervallen verklaren (art. 44) vormen één bedrijfsproces, gestart door de mededeling van de minister (art. 25 lid 4), met de vervallenverklaring of de teruggave als resultaat.

## Wat moet veranderen

Repareren en voorkomen, in deze volgorde. De besluiten van de redacteur en de uitwerking staan in de laatste sectie.

1. **Kenmerk *klant tot klant*** in de criteria (`tools/bepaal_type.py`, criteria-skill, `analyses/kenmerken.md`): "Begint het bij een aanleiding van buiten het proces (verzoek of melding van een klant, gebeurtenis, termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? Noem begin en eind." Bron: PH 81, 83.
2. **Beslisregel stap 7** (`_niveau_proces`, `analyses/beslistabel.md`): *bijdrage aan groter proces* met *klant tot klant* ja wordt bedrijfsproces; zonder wordt het deelproces of processtap. *Eigen besluit* en *eigen normering* bepalen het niveau niet meer. *Levert aanbod* zonder *klant tot klant* wordt voorgelegd: de dienst hoort bij het bedrijfsproces.
3. **Pagina voor een deelproces?** Nu krijgt een deelproces geen pagina en gaan tekst en relaties naar het bedrijfsproces. Alternatief: een deelproces met eigen normering krijgt een pagina, met procesniveau deelproces, geaggregeerd door zijn bedrijfsproces; dan blijven de Archi-objecten (Uitreiken reisdocument) bestaan.
4. **Controles** (hiërarchiecontrole in `tools/bepaal_type.py`): een fout of voorleggen bij (a) een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert, en (b) een gebeurtenis die een deelproces triggert.
5. **Herbeoordelen** de processen uit de tabellen hierboven, en de triggering Verval van het reisdocument → Inhouden reisdocument; de definities van de bedrijfsprocessen die een deelproces opnemen lopen dan tot het eindresultaat (Behandelen aanvraag reisdocument: tot uitreiking of weigering).

## Uitwerking (besluiten redacteur 2026-10-08)

- **Kenmerk en beslisregel**: *klant tot klant* is een nieuw kenmerk; alleen dat maakt van *bijdrage aan groter proces* een bedrijfsproces. Een deelproces dat een dienst levert, wordt voorgelegd. Alle 432 beoordelingen hebben het kenmerk: 58 processen zijn klant-tot-klant, 9 zijn deelproces of processtap, de rest is niet van toepassing.
- **Geen pagina voor een deelproces**: het bedrijfsproces beschrijft zijn deelprocessen in het veld `deelprocessen`, in volgorde en met bron, op de pagina (sectie Deelprocessen) en in Archi als property *wiki-gemma-model deelprocessen*. De beoordeling van het deelproces blijft, als onderdeel zonder pagina; beschrijving en relaties zijn letterlijk naar het bedrijfsproces verplaatst.
- **Controles**: een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert, wordt voorgelegd; een gebeurtenis die een deelproces triggert, is een fout.
- **Deelproces geworden**: Uitreiken reisdocument (in Behandelen aanvraag reisdocument en de variant voor niet-ingezetenen), Uitreiken rijbewijs (in Behandelen aanvraag rijbewijs en de omwisseling), Vervallen verklaren reisdocument (in Inhouden reisdocument), Houden naturalisatieceremonie (in Behandelen naturalisatieverzoek en Behandelen optieverklaring), Behandelen melding voorgenomen huwelijk of partnerschap (in Voltrekken huwelijk en Registreren partnerschap), Bijzetten of verstrooien van de as (in Uitvoeren lijkbezorging). Hun objecten in Archi vervallen.
- **Vermissing en inlevering**: Verwerken vermissing reisdocument eindigt bij de registratie en het verval. De processtap Inlevering reisdocument is de gebeurtenis Inlevering van het reisdocument geworden (Paspoortwet art. 56); die triggert Inhouden reisdocument, het bedrijfsproces voor elke inlevering. Verval van het reisdocument verplicht de houder tot inlevering en triggert de inhouding niet meer zelf.
- **Overlijden**: Schouwen stoffelijk overschot blijft een bedrijfsproces en geeft de verklaring van overlijden door aan Verlenen verlof tot begraving of crematie (Wlb art. 7, 12).
- **Gevolgen om te volgen**: het levensloopproces Begraven en cremeren stoffelijk overschot omvat nu één bedrijfsproces, Uitvoeren lijkbezorging (een 1-op-1-aggregatie); procesarchitectuur-terugmelding 4 (opgelost) noemt nog Behandelen melding voorgenomen huwelijk of partnerschap en Houden naturalisatieceremonie als element.
