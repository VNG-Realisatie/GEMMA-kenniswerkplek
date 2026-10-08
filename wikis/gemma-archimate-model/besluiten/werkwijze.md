---
id: werkwijze
type: doc
titel: Besluiten over de werkwijze
bijgewerkt: '2026-10-08'
---

# Besluiten over de werkwijze

## Hoe dit register werkt

De besluiten van de redacteur over de werkwijze en de criteria, per thema en in volgorde van datum. Dit is geschiedenis: wat nu geldt, staat in de regels van [AGENTS.md](../AGENTS.md) en in de skills. De kolom Stand zegt waar een besluit nu staat, of door welk besluit het is herzien. Een besluit dat bij één document in `docs/` hoort, staat in de besluitentabel van dat document (genoemd onder elk thema); besluiten over één begrip staan in [Besluiten per begrip](per-begrip.md).

Een nieuw algemeen besluit verwerk je in de regel of de skill waar het hoort, en je zet het hier of bij het document in `docs/`, met de stand.

## 1 Criteria en naamgeving

Besluitentabellen in de docs: [Kenmerken per elementtype](../docs/kenmerken.md), [GEMMA-kennismodel](../docs/gemma-kennismodel.md), [Toegang tot een bedrijfsobject](../docs/gegevensrollen.md), [Synoniemen en homoniemen](../docs/synoniemen-en-homoniemen.md).

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-05 | Naam van een UPL-product | Een product of dienst uit de UPL krijgt de UPL-naam letterlijk, met een synoniem waar dat betekenis toevoegt (regel Naamvorm). Onderhoud van graven wordt Grafonderhoud. | regel Naamvorm |
| 2026-10-07 | Soort partij | Het criterium betekent: elke gemeente heeft met de partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt. Het sluit uit wat bij één of enkele gemeenten hoort (gemeente Utrecht, provincie Utrecht), niet een partij die landelijk maar één keer bestaat: Rijk, Provincie en Waterschap zijn een soort partij (de bestuurslaag als geheel). Aangepast in de beslistabel (`tools/bepaal_type.py`), de criteria-skill en [Indelingen](../docs/indelingen.md). | skill gemma-archimate-model-criteria (soort partij); tools/bepaal_type.py |

## 2 Procesniveaus en indelingen

Besluitentabellen in de docs: [Indelingen](../docs/indelingen.md), [Processen](../docs/proceshierarchie.md).

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-07 | Ketenproces, bedrijfsproces, deelproces | Een ketenproces aggregeert alleen bedrijfsprocessen, nooit rechtstreeks deelprocessen (kennismodel: Ketenproces → Bedrijfsproces, regel 590; Bedrijfsproces → Deelproces, regel 605). Tussen een ketenproces en zijn deelprocessen komen bedrijfsprocessen die elk een logische groep deelprocessen aggregeren, liefst geen 1-op-1. Lezing van *omvat levensloop*: het ketenproces omvat de levensloop over de partijen heen, een bedrijfsproces binnen het ketenproces de levensloop van het deel van één partij (bijvoorbeeld de gemeente). Dit is een interpretatie van de definities (ketenproces: over afdelingen of organisaties; bedrijfsproces: reeks activiteiten voor één resultaat; deelproces: binnen één organisatorische eenheid); de GEMMA-definities noemen geen levensloop. Raakt Bezorgen stoffelijk overschot, Beheren Nederlanderschap en Afgeven verklaring omtrent het gedrag; uitwerking: zie de besluiten hieronder. | herzien door 2026-10-08 (Ketenproces, levensloopproces, taak) |
| 2026-10-07 | Kernobject van een bedrijfsproces binnen een ketenproces | Hetzelfde kernobject als het ketenproces. Per kernobject één bedrijfs- of ketenproces, plus de bedrijfsprocessen die het ketenproces met dat kernobject aggregeert; elk omvat het deel van één partij in die levensloop. Een eigen kernobject (Optieverklaring, Aanvraag VOG) zou kunstmatige objecten geven, geen kernobject zou de levensloop niet meer toetsen. `tools/bepaal_type.py` controleert het: een gedeeld kernobject mag alleen binnen het ketenproces, en een ketenproces dat een deelproces aggregeert is een fout. Formulering in [Beslistabel](../docs/beslistabel.md) (kenmerk *omvat levensloop*, regel 28 en 35), skill gemma-archimate-model-criteria en [Indelingen](../docs/indelingen.md). | herzien door 2026-10-08 (Ketenproces, levensloopproces, taak; Eén levensloopproces per kernobject) |
| 2026-10-08 | Ketenproces, levensloopproces, taak | De procesniveaus volgen de GEMMA-ladder (GEMMA Online, Proceshiërarchie): wat de wiki deelproces noemde wordt bedrijfsproces, wat de wiki bedrijfsproces noemde wordt levensloopproces; de taak vervalt (Verzorgen burgerzaken, Verzorgen lijkbezorging: per geval voorleggen bij de uitwerking); ketensamenwerking wordt een bedrijfsinteractie, bediend door de bedrijfsprocessen van de partijen, en het ketenproces is geen element meer (Bezorgen stoffelijk overschot, Beheren Nederlanderschap, Afgeven verklaring omtrent het gedrag: herbeoordelen). Herziet de besluiten van 2026-10-07 over ketenproces, bedrijfsproces en deelproces en over het kernobject binnen een ketenproces. Zie [Proceshiërarchie](../docs/proceshierarchie.md). | skill gemma-archimate-model-criteria (Procesniveau, Ketensamenwerking) |
| 2026-10-08 | Procesindeling naar kernobject | De *Procesindeling naar taak* heet *Procesindeling naar kernobject*; het niveau heet *levensloopproces*. Zie [Indelingen](../docs/indelingen.md). | skill gemma-archimate-model-criteria (stap 7); export |
| 2026-10-08 | Bedrijfsinteractie | Een bedrijfsinteractie (ketensamenwerking) krijgt een eigen paginatype met een kernobject, staat bij dat kernobject in de Procesindeling naar kernobject en via zijn beleidsdomein in de Beleidsdomeinindeling, en in Archi in de map *Ketensamenwerking*; elke nieuwe interactie wordt voorgelegd. Het kenmerk *meer organisaties* vervalt. Herziet het besluit van 2026-09-30 in [GEMMA-kennismodel](../docs/gemma-kennismodel.md). | skill gemma-archimate-model-criteria (Ketensamenwerking); paginatype bedrijfsinteractie in wiki.yaml |
| 2026-10-08 | Beleidsdomeinen | Een register `beoordelingen/beleidsdomeinen.yaml` met per beleidsdomein de beschrijving en de bronnen. De render toont de tekst in het overzicht bij het beleidsdomein; de export zet haar als documentatie op een nieuwe groepering en als wiki-eigenschap op een GEMMA-groepering (de GGM-documentatie blijft). Afgewezen: de tekst in de omschrijving van het onderwerp (een onderwerp is geen beleidsdomein) en niet bewaren (regel Letterlijk verplaatsen). | skill gemma-archimate-model-beoordelen §4 (aangevuld 2026-10-08); render en export |
| 2026-10-08 | Eén levensloopproces per kernobject | Meer levensloopprocessen met hetzelfde kernobject alleen als ze samen een bedrijfsinteractie met dat kernobject bedienen, elk het deel van één partij; anders een fout. Het kenmerk *omvat levensloop* noemt weer het deel van één partij binnen een ketensamenwerking. Afgewezen: altijd een signaal. | skill gemma-archimate-model-criteria (Procesniveau); tools/bepaal_type.py |
| 2026-10-08 | Bedrijfsproces, deelproces (klant tot klant) | Een bedrijfsproces is klant-tot-klant (GEMMA Online, Proceshiërarchie, PH 81, 83): nieuw kenmerk *klant tot klant* (begint bij een aanleiding van buiten het proces en loopt door tot het resultaat voor de klant, zonder de voortzetting te zijn van een ander proces voor hetzelfde geval). Alleen dat kenmerk maakt van *bijdrage aan groter proces* een bedrijfsproces; *eigen besluit* en *eigen normering* bepalen het procesniveau niet meer, *levert aanbod* zonder *klant tot klant* wordt voorgelegd. Herstelt de omzetting van 2026-10-08, die de drempel van het oude deelproces meenam. Zie [Klant tot klant](../docs/proceshierarchie.md#bedrijfsproces-of-deelproces-de-toets-klant-tot-klant). | skill gemma-archimate-model-criteria (Procesniveau, aangevuld 2026-10-08) en kenmerk klant tot klant |
| 2026-10-08 | Deelproces | Een deelproces krijgt geen pagina (bevestigt 2026-10-08). Het bedrijfsproces krijgt een compacte, goed leesbare toelichting voor procesontwerpers over zijn deelprocessen (veld `deelprocessen`), op de pagina en in Archi als eigen property *wiki-gemma-model deelprocessen*; de beschrijving blijft ongewijzigd. | skill gemma-archimate-model-criteria (Procesniveau); veld deelprocessen |
| 2026-10-08 | Controles op triggering | Een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert: voorleggen (mogelijk een deelproces). Een gebeurtenis die een deelproces triggert: fout (een gebeurtenis van buiten start altijd een bedrijfsproces). | skill gemma-archimate-model-criteria (Procesniveau, aangevuld 2026-10-08); tools/bepaal_type.py |

## 3 Eén model en thuishoren

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-06 | Eén element in het hele model | Geen dubbelingen tussen onderwerpen: een begrip is één element, geplaatst bij het onderwerp met de meeste samenhang (maximale samenhang, minimale koppeling), met relaties naar de andere onderwerpen; de onderwerpgrenzen volgen modulariteit. Vastgelegd in de regels Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen en Grenzen van een onderwerp. Het overlijden (aangifte, akte) hoort bij Burgerzaken, het verlof tot begraven en het laissez-passer bij Lijkbezorging. | regels Eén element in het hele model, Thuishoren en Relaties tussen onderwerpen; de maatstaf 'de meeste samenhang' herzien door 2026-10-06 (Criterium voor thuishoren) |
| 2026-10-06 | Thuisonderwerp | Het eerste onderwerp in `onderwerpen` is het thuisonderwerp: dat onderwerp beoordeelt het element, ook het kenmerk *betekenis in onderwerp*; de andere gebruiken het. De tools lazen de volgorde niet; nu wel (signalen, begrippenlijst, samenhang in de voortgang). | regel Thuishoren |
| 2026-10-06 | Criterium voor thuishoren | De inhoud beslist, niet het aantal relaties: de taak waarin het element ontstaat of verandert (proces dat het object maakt, kernobject, object waarvan de toestand verandert, meeste gedrag van een rol). Het aantal relaties is een signaal; bij twijfel voorleggen. Reden: tellen hangt af van de volgorde van werken en van het aantal bronnen (Gemeente en Burgemeester zouden naar Burgerzaken gaan). Vervangt in het besluit Eén element in het hele model de maatstaf "de meeste samenhang"; de regel Grenzen van een onderwerp gaat op in Thuishoren. | regel Thuishoren |
| 2026-10-06 | Signalen voor één model | Signalen in `tools/signalen.py`: dezelfde naam of hetzelfde synoniem zonder `synoniem_van` of `homoniemen`, dezelfde GEMMA- of GGM-match, kernobject met een ander thuisonderwerp, verwijzing naar een bestaand onderwerp, element zonder relatie of met meer relaties naar een ander onderwerp; samenhang per onderwerp in `voortgang.md`. | signalen bij de regels Eén element in het hele model, Thuishoren en Relaties tussen onderwerpen (tools/signalen.py) |
| 2026-10-07 | Thuisonderwerp en eerdere goedkeuring | Dat een element eerder in een ander onderwerp is beoordeeld of goedgekeurd, is geen argument voor zijn thuisonderwerp: dat komt door de volgorde van inlezen. Alleen de inhoud telt (regel Thuishoren). Volgt het thuisonderwerp eenduidig uit de inhoud, dan verplaatst de AI het element zonder voor te leggen en noemt het in de lijst ter bevestiging; alleen bij inhoudelijke twijfel voorleggen. | regel Thuishoren |

## 4 Bronnen en wettelijke grondslag

Besluitentabellen in de docs: [Wettelijke grondslag](../docs/wettelijke-grondslag.md).

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-06 | Tegenspraak tussen bronnen | Beide vastleggen en markeren; wat formeel geldt volgt de bronvoorrang (wet vóór praktijk). Voorbeeld: de bevestigingstermijn van de optie (wet 13 weken, Utrecht 13 tot 26 weken). | regel Tegenspraak |
| 2026-10-07 | Wet als grondslag van een UPL-product | Een wet die de UPL als grondslag van een product noemt, wordt als bron opgehaald; daarna wordt beoordeeld of ze een beleidskader wordt, alleen als ze de gemeente een taak of bevoegdheid geeft. Een wet met alleen een tarief of een regel buiten de gemeentelijke taak blijft bron. Een verdrag is bron en geen beleidskader zolang de criteria geen regelgever verdrag kennen. Geldt ook als regel in `wiki-curatie-update` en `gemma-archimate-model-beoordelen`. Eerste toepassingen: Wet griffierechten burgerlijke zaken (art. 23, alleen het tarief; de bevoegdheidsgrondslag van de legalisatie is niet gevonden, verificatie nodig) en de Overeenkomst van München 1980 (Trb. 1981, 71; uitvoering in BW boek 1 art. 49a). | skill gemma-archimate-model-beoordelen §2 (verdrag aangevuld 2026-10-08); skill wiki-curatie-update |
| 2026-10-08 | Wettelijke grondslag, groep A en D | Een element of relatie waarvan de landelijke wettelijke grondslag eenduidig in de wettekst staat (artikel nagelezen, geen twijfel over de taak), krijgt de bron en de relatie *is grondslag voor* zonder voorleggen; de AI noemt die gevallen in de samenvatting ter bevestiging. Alleen bij twijfel (geen passend artikel, een grondslag die de taak maar gedeeltelijk dekt, een element dat misschien niet blijft) voorleggen. | regel Wettelijke grondslag (aangevuld 2026-10-08) |
| 2026-10-08 | Relaties en wettelijke grondslag | Een relatie heeft geen eigen landelijke grondslag nodig (te gedetailleerd): elementen en structuur worden afgeleid uit wettelijke bronnen, maar per relatie volstaat een bron. Voor elementen blijft de regel Wettelijke grondslag gelden (besluit 16 in `docs/wettelijke-grondslag.md`). | regel Wettelijke grondslag |

## 5 Terugmeldingen

Besluitentabellen in de docs: [Wettelijke grondslag](../docs/wettelijke-grondslag.md) (besluit 4 en 15).

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-05 | Procesarchitectuur-terugmeldingen | Een register van terugmeldingen aan de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel), naast de GGM-terugmeldingen. Het model mag afwijken van de UPL-indeling, mits teruggemeld. Eerste meldingen: de domeinen van het beleidsdomein Begraafplaatsen en crematoria, en het taakveld van verlof tot begraven en van ontleding stoffelijk overschot toestemming. | skill gemma-archimate-model-beoordelen §7 |

## 6 Akkoord, export en objectbehoud

| Datum | Besluit | Inhoud | Stand |
|---|---|---|---|
| 2026-10-02 | Export naar Archi | Export in het opslagformaat van Archi (`.archimate`), niet AMEFF; GEMMA wordt native (`.archimate`) ingelezen. Een element met een GEMMA-match krijgt het GEMMA-id; naam en definitie uit de wiki overschrijven die van GEMMA, de oude gaan mee als eigenschap. Eigen eigenschappen en de eigen map heten `wiki-gemma-model`. Volledige sync via `wiki-gemma-model exportdatum` en een jArchi-script: alleen door de wiki gemaakte objecten worden verwijderd, bij een niet meer gekoppeld GEMMA-object alleen de wiki-eigenschappen. Alleen goedgekeurd; `--concept` alleen om te bekijken. Geen views. | skill gemma-archimate-model-archimate-export; 'geen views' wordt herzien na de eerste proefimport (todo.md) |
| 2026-10-02 | GEMMA-match | Elke match met id wordt in de export een koppeling, ook `zwak` en `partieel`. Zo'n match wordt daarom alleen gemaakt met akkoord van de redacteur; matchen is de verantwoordelijkheid van wiki en redacteur, de export en Archi vertrouwen haar. | regel Zwakke match voorleggen |
| 2026-10-05 | Export na akkoord | Elk AKKOORD levert meteen een nieuwe export naar Archi op: na `llmwiki promote apply` volgen `tools/archimate_export.py --check` en de export, en de export gaat mee in de commit (stap 9 van gemma-archimate-model-update). Importeren in GEMMA blijft aan de redacteur. | skill gemma-archimate-model-update, stap 9 |
| 2026-10-05 | Objectbehoud in Archi | Hernoemen, samenvoegen en splitsen leiden niet vanzelf tot nieuwe objecten in Archi: de redacteur gebruikt de objecten in views, die de export niet bijwerkt. Het register `beoordelingen/objecten.yaml` legt vast welk object een element voortzet. Bij samenvoegen kiest de redacteur of en welk object blijft, bij splitsen of er een blijft en welk deel het krijgt. De zeven hernoemingen van 2026-10-05 houden zo hun object (Lijk, Bezorgen lijken, Opgraven lijk, Schouwen lijk, Treffen maatregel bij besmet lijk, Besmet lijk gemeld, Onderhoud van graven). | regel Objectbehoud |

## Uit besluiten per element

Besluiten over één element die een algemene regel bevatten, nagelopen op 2026-10-08. Het besluit zelf staat in [Besluiten per begrip](per-begrip.md).

| Datum | Element | Regel (kort) | Stand |
|---|---|---|---|
| 2026-10-05 | Grafuitgifte | Het product bedient de rol van de afnemer (kennismodel regel 596: Product → bediening → Klant). | skill gemma-archimate-model-beoordelen, references/relaties.md (aangevuld 2026-10-08) |
| 2026-10-08 | Model beheersverordening begraafplaatsen | Is grondslag voor alleen bij UPL-producten zonder landelijke wettelijke grondslag; anders werkt uit voor. | regel Wettelijke grondslag; references/relaties.md (aangevuld 2026-10-08) |
| 2026-10-07 | Verklaring van huwelijksbevoegdheid | Een verdrag is bron en geen beleidskader. | skill gemma-archimate-model-beoordelen §2 (aangevuld 2026-10-08) |
| 2026-10-05 | UPL-producten van lijkbezorging | Een product bij een dienst met een afspraak, anders een dienst; de UPL-naam letterlijk. | beslistabel (product); regel Naamvorm |
| 2026-10-05 | Begraafplaatsregister, Crematoriumregister, Bijzettingenregister | Een product of dienst uit de UPL valt niet weg. | regel Wettelijke grondslag; skill gemma-archimate-model-criteria (Procesniveau) |
| 2026-10-04 | Gedeputeerde staten; 2026-10-07 Rechtbank Den Haag, Koning | Wie per geval en op verzoek beslist (beroep, ontheffing), valt buiten het model en staat in de beschrijving. | regel Gemeentelijk perspectief |
| 2026-10-04 | Adviescommissie begraafplaatsen, Gemeenschappelijke regeling begraafplaats | Wat de bron alleen als mogelijkheid noemt, is geen soort partij bij elke gemeente. | skill gemma-archimate-model-criteria (soort partij) |
| 2026-10-01 | Elektronische weg, Mededelingenbord | Geen element: input voor de centrale kanalenset. | skill gemma-archimate-model-criteria (kanaal: één centrale set); todo.md (Kanalen) |
| 2026-10-04 | Verlenen grafrecht, Treffen maatregel bij besmet stoffelijk overschot | Het enige proces van zijn soort specialiseert zelf het GEMMA-proces; een cluster naar soort werk vraagt minstens twee. | beslistabel (kenmerk omvat processen) |
| 2026-10-08 | Behandelen naturalisatieverzoek, Houden naturalisatieceremonie, Behandelen aanvraag verklaring omtrent het gedrag | Orkestratie: het deel dat de gemeente voor een ander uitvoert, specialiseert Leveren dienst aan derden. | skill gemma-archimate-model-criteria (Ketensamenwerking) |
| 2026-10-01 | Burgerlijk Wetboek Boek 2 | Een regeling die alleen definities levert, is geen beleidskader. | skill gemma-archimate-model-criteria (regeling) |
| 2026-10-08 | Beheerder van de begraafplaats | Een rol zonder landelijke wettelijke bron vervalt en wordt een synoniem van de rol uit de wet. | regel Wettelijke grondslag |
