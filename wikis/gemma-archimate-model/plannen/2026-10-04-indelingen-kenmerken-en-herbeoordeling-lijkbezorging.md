# Plan: indelingen van de bedrijfsarchitectuur, complete kenmerken en beslistabel, herbeoordeling lijkbezorging

## Context

Lijkbezorging is nu plat en fijnmazig: één functie bedient negen processen, en vijftien bedrijfsobjecten staan naast elkaar (waaronder generieke objecten en invoerdocumenten). Doel is een kwalitatief en compleet GEMMA-model op het juiste abstractieniveau, met indelingen in de hele breedte van de bedrijfsarchitectuur:
- elk elementtype heeft een kernrelatie, een regel voor wel of geen eigen pagina, en een plaats in één of meer indelingen;
- de bestaande GEMMA-indelingen blijven ongewijzigd en worden gevolgd; nieuwe indelingen komen alleen waar GEMMA er geen heeft;
- bij voorkeur hiërarchisch; waar dat niet past, mag een element onder meer dan één groep hangen;
- alles is zichtbaar in Archi, met overzichten bovenaan en details per onderwerp;
- minder elementen door strakkere beslisregels. Detail dat geen element meer is, gaat naar de beschrijving van wat overblijft.

**Abstractieniveau voor GEMMA.** GEMMA is een referentiemodel voor alle gemeenten. Daarom:
- een element is een soort, geen exemplaar;
- het staat op het niveau waarop gemeenten beleid maken en uitvoeren;
- een variant wordt een specialisatie zonder pagina, een deel een onderdeel, een stap komt in de beschrijving;
- wat in veel onderwerpen terugkomt, is generiek.

De kenmerken hieronder moeten dat per elementtype afdwingen.

> **Wijziging 2026-10-04 (fase 1):** de processtructuur is herzien. Er komt één bedrijfsproces of ketenproces per kernobject (de deeltaak vervalt), met deelprocessen die de producten leveren, plus clusters naar soort werk binnen de taak als specialisatie van het generieke GEMMA-proces. De aparte indeling *Ketens* vervalt. Bindend is `wikis/gemma-archimate-model/analyses/indelingen.md`.

## Indelingen

GEMMA-stand uit het ingelezen model (`tools/gemma.py`) en de lijsten op GEMMA Online.

Een indeling is één criterium met benoemde niveaus. Gebruikt een tweede elementtype hetzelfde criterium, dan is dat **geen nieuwe indeling**: het type wordt ingedeeld in de bestaande indeling. Zo blijven er vier GEMMA-indelingen en twee nieuwe over.

| Indeling | Van | Deelt in | Naar | Niveaus | Relatie in Archi |
|---|---|---|---|---|---|
| **Procesindeling naar soort werk** (GEMMA-processenlandschap) | GEMMA | bedrijfsprocessen (via specialisatie), en via generieke GEMMA-elementen ook gebeurtenissen, diensten en rollen | soort proces | sturend, uitvoerend of ondersteunend → procescluster → generiek bedrijfsproces → deelproces → processtap | aggregatie (102×); domeinproces via specialisatie |
| **Functie-indeling naar domein** | GEMMA | bedrijfsfuncties; **producten en diensten** (domein → functie, interne producten op functieniveau) | soort sturing, domein, soort werk | soort sturing → domein → soort werk → onderwerp; onderaan 7 functies met meer ouders | aggregatie (302×) |
| **Beleidsdomeinindeling** | GEMMA (GGM) | bedrijfsobjecten, afspraken; **producten en diensten**; **beleidskaders** (regelgever als eigenschap) | taakveld Iv3, beleidsdomein | taakveld → beleidsdomein → element | groepering (507×) |
| **Doelgroepindeling** | GEMMA (4 rollen) | rollen, **actoren**, **bedrijfssamenwerkingen**, **kanalen** (fysiek of digitaal als eigenschap) | gemeente (bestuursorgaan, ambtelijk), inwoners en ondernemers, ketenpartners | doelgroep → element | groepering |
| **Procesindeling naar taak** | nieuw | bedrijfsprocessen, gebeurtenissen | gemeentelijke taak en kernobject | taak (*Verzorgen lijkbezorging*) → deeltaak per kernobject (*Beheren grafrechten*) → bedrijfsproces → deelproces | aggregatie; map `wiki-gemma-model / Procesindeling naar taak` |
| **Ketens** | nieuw, op basis van het GEMMA-kennismodel (ketenproces) | bedrijfsprocessen | samenwerking over organisaties | ketenproces → bedrijfsprocessen van meer organisaties, dwars door taken | aggregatie; het ketenproces realiseert een dienst |

**Indeling en view.** Uit één indeling kunnen meer views worden gemaakt, elk voor één of meer elementtypen. Voorbeelden uit de Beleidsdomeinindeling: *Bedrijfsobjecten per beleidsdomein*, *Producten en diensten per beleidsdomein*, *Beleidskaders per beleidsdomein*. Besloten:
- de wiki genereert deze views nu als overzichten, per indeling en elementtype, in `overzicht.md` en per onderwerp;
- de export blijft zonder views (besluit 2026-10-02);
- Archi-views komen op de todo, na de eerste proefimport.

Voorgestelde views (definitief in fase 1):

| Indeling | Views |
|---|---|
| Procesindeling naar soort werk | Bedrijfsprocessen per generiek GEMMA-proces |
| Functie-indeling naar domein | Functies die processen bedienen; Producten en diensten per functie |
| Beleidsdomeinindeling | Bedrijfsobjecten per beleidsdomein (kernobjecten en subobjecten); Producten en diensten per beleidsdomein; Beleidskaders per beleidsdomein |
| Doelgroepindeling | Actoren en rollen per doelgroep; Kanalen per doelgroep |
| Procesindeling naar taak | Per taak: deeltaken, bedrijfsprocessen, gebeurtenissen en kernobjecten |
| Ketens | Per keten: bedrijfsprocessen in volgorde, met de gebeurtenissen en de organisaties |

**Hergebruik van bestaande indelingen, geanalyseerd:**
- *Product- en dienstindeling*: geen eigen indeling. Producten en diensten vallen in de Beleidsdomeinindeling (inhoud) en in de Functie-indeling naar domein (soort werk). Ze hebben dus twee ouders.
- *Beleidskaderindeling*: geen eigen indeling, maar de Beleidsdomeinindeling.
- *Kanaalindeling naar doelgroep*: geen eigen indeling, maar de Doelgroepindeling.
- *Applicatieservice-indeling naar domein* (GEMMA, alleen gedocumenteerd): ook geen eigen indeling, maar een combinatie van het domein uit de Functie-indeling en de doelgroep uit de Doelgroepindeling.
- *Afnemer extern of intern*: geen indeling, maar een eigenschap. Ze volgt de bovenste laag van de Procesindeling naar soort werk: uitvoerend tegenover sturend en ondersteunend.
- *Procesindeling naar taak*: in fase 1 toets ik of het taakniveau zelf een hergebruik is van het beleidsdomein (*Verzorgen lijkbezorging* ↔ *Begraafplaatsen en crematoria*). Is dat zo, dan voegt deze indeling alleen de deeltaak per kernobject toe onder het beleidsdomein. Dan staan processen, objecten, producten en beleidskaders van één taak bij elkaar.
- *Ketens*: geen hergebruik mogelijk. Het kennismodel kent het ketenproces, maar GEMMA heeft er nog geen indeling van.

## Taak, keten en intern of extern: advies

Er spelen drie assen, die elk een eigen plaats krijgen:

| As | Vraag | Waarden | Vorm in het model |
|---|---|---|---|
| **Inhoud** | Bij welke taak hoort het? | taak → deeltaak | **procescluster** (business-process met procesniveau *procescluster*, zoals GEMMA's clusters in het processenlandschap). Geen echt proces: het wordt niet per geval doorlopen |
| **Reikwijdte** | Wie voert het uit? | ketenproces (meer organisaties) → bedrijfsproces (één organisatie) → deelproces (één organisatorische eenheid) → processtap | echte processen, per geval doorlopen. **Ketenproces** volgens het kennismodel (regel 564, 590-591): aggregeert bedrijfsprocessen en realiseert een dienst |
| **Afnemer** | Voor wie? | extern (burger, bedrijf, ketenpartner) of intern (de eigen organisatie) | eigenschap `afnemer`. Sluit aan op de bovenste laag van het processenlandschap (uitvoerend tegenover sturend en ondersteunend), op *Klant (intern of extern)* en op de externe en interne UPL-lijst |

**Antwoord op "zijn taken ook bedrijfsprocessen?"**
- In ArchiMate krijgen taak en deeltaak het type business-process, zoals GEMMA dat bij procesclusters doet. Inhoudelijk zijn ze een groepering, geen bedrijfsproces.
- Een keten is wél een proces: per geval doorlopen, over organisaties heen.

**Wat dit in het model geeft:**
- Een keten staat naast de taken en kan bedrijfsprocessen uit meer taken en onderwerpen bevatten. Voorbeeld: overlijden → schouwen → aangifte → verlof → begraven of cremeren, met arts, burgerlijke stand, officier van justitie, uitvaartondernemer en houder van de begraafplaats.
- Een bedrijfsproces mag daardoor zowel onder een deeltaak als in een keten hangen.
- Intern of extern staat los van taak en keten: zowel een keten als een taak kan interne en externe processen bevatten.

**Nieuw kenmerk *meer organisaties*.**
- De vraag: voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol (niet de klant)?
- Samen met *per keer doorlopen* en *omvat bedrijfsprocessen* geeft het procesniveau ketenproces.
- Een ketenpartner die alleen adviseert, maakt van een bedrijfsproces geen keten.

## Toets aan het Kennismodel procesarchitectuur (Over GEMMA, work in progress)

| Kennismodel (regel) | Plan | Oordeel |
|---|---|---|
| Actor → toewijzing → Rol (602) | actor alleen via rol | volgt |
| Rol → toewijzing → Deelproces (599) | rol aan bedrijfsproces of deelproces (besluit 2026-10-01) | bewuste afwijking; met strakkere deelprocesregels blijft de toewijzing aan het bedrijfsproces nodig. Voorstel aan het kennismodel |
| Relaties tussen actoren: niet in het kennismodel; in het GEMMA-model aggregeert een samenwerking actoren | alleen structurele relaties | aanvulling; voorstel aan het kennismodel |
| Product → bediening → Klant (intern of extern) (596) | ontbrak | **toevoegen**: *afnemer* noemt een rol die een specialisatie van Klant is, en het product bedient die rol |
| Product → associatie → Beleidskader (595) | kernrelatie *is grondslag voor* naar proces, dienst of product | **besloten**: bij voorkeur naar een product; naar proces of dienst alleen tijdelijk zolang er geen product is (signaal). Na de UPL (todo) verhuizen de relaties naar de producten |
| Product → aggregatie → Dienst (593) | kernrelatie *omvat diensten en afspraken* | volgt (afspraak uit de definitie) |
| Bedrijfsfunctie ↔ bediening ↔ Bedrijfsproces (597, 604) | kernrelatie *bedient gedrag* | volgt |
| Ketenproces → aggregatie → Bedrijfsproces; Ketenproces → realisatie → Dienst (590-591) | ketens als eigen as | volgt |
| Bedrijfsproces → aggregatie → Deelproces → Processtap → Handeling (605, 601, 589) | procesniveaus; een processtap krijgt geen pagina | volgt |
| Bedrijfsproces → realisatie → Dienst (603) | een dienst wordt gerealiseerd door een bedrijfsproces, ketenproces of functie | functie volgt het uitgebreide kennismodel, niet deze view |
| Bedrijfsproces → toegang → Bedrijfsobject (606) | kernobject via toegang | volgt |
| Procescluster, taak, gebeurtenis: niet in deze view | procescluster als in het processenlandschap; gebeurtenis uit het uitgebreide kennismodel | aanvulling |

## Kenmerken per elementtype: validatie en voorstel

De huidige stand komt uit `tools/bepaal_type.py` (`TYPEN`). Een **vet** woord is nieuw of gewijzigd.

| Type | Bepaald door | Kernrelatie (moet ja) | Drempel | Eigen pagina (abstractie) | Indeling (verplicht) |
|---|---|---|---|---|---|
| Bedrijfsobject | geen aard | *wordt bewerkt* | *onderscheidbare exemplaren*, *levenscyclus* | **objectniveau**: generiek, kernobject, subobject; geen pagina bij onderdeel en invoer van een ander; *zelfstandige specialisatie* | Beleidsdomeinindeling |
| Afspraak | *afspraak* | *wordt bewerkt* | idem | idem | Beleidsdomeinindeling |
| Product | *aanbod als geheel* | *omvat diensten en afspraken* | *afnemer* (**noemt een klantrol, met bediening**), *benoembaar resultaat* | Gat: geen abstractieregel. → **zelfstandig aanbod**: eigen naam in een catalogus, geen variant of tarief | Beleidsdomeinindeling en Functie-indeling naar domein |
| Ketenproces | *per keer doorlopen* + **meer organisaties** | **omvat bedrijfsprocessen** (van minstens 2 organisaties) | *aanleiding*, *benoembaar resultaat* | procesniveau ketenproces | Ketens |
| Dienst | *aangeboden gedrag* | *gerealiseerd door* | *afnemer*, *benoembaar resultaat* | Gat: een dienst per stap is mogelijk. → **het realiserende element moet bedrijfsproces, taak of functie zijn**; *generiek* → specialisatie van een GEMMA-dienst | Beleidsdomeinindeling en Functie-indeling naar domein |
| Taak, deeltaak | **groepeert processen** | **omvat bedrijfsprocessen** (minstens 2) | *toegewezen partij* | deeltaak alleen met een `kernobject` | Procesindeling naar taak |
| Bedrijfsproces | *per keer doorlopen* | *toegewezen partij* | **vervangen door de niveauregel** (stap 7) | **procesniveau**: bedrijfsproces, deelproces; een processtap krijgt geen pagina | naar taak (aggregatie) en naar soort werk (specialisatie) |
| Bedrijfsfunctie | *gegroepeerd gedrag* | Gat: nu *toegewezen partij*, terwijl een functie in GEMMA bedient. → **bedient gedrag** | *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd* | → **in functie-indeling**: past als onderwerp onder een soort werk; bij voorkeur een exacte GEMMA-match, anders besluit | Functie-indeling naar domein |
| Gebeurtenis | *toestandsverandering* | *leidt tot gedrag* | *komt herhaald voor* | Gat: generieke ontvangstgebeurtenissen per proces. → pagina alleen als zij een bedrijfsproces start of twee verbindt; *generiek* → specialisatie | Procesindeling naar taak |
| Actor | partij, *los van verantwoordelijkheid* | *vervult een rol* | — | Gat: soort of exemplaar. → **soort partij**: komt bij elke gemeente voor, geen individuele organisatie. Raakt het besluit van 2026-09-30 (gemeenten Amsterdam en Utrecht als actor): opnieuw voorleggen | Doelgroepindeling |
| Rol | *hoedanigheid* | *voert gedrag uit* | — | *zelfstandige specialisatie*; *generiek* → specialisatie van een GEMMA-rol | Doelgroepindeling |
| Bedrijfssamenwerking | *samenwerkingsverband* | *voert gedrag uit* | — | **soort partij** | Doelgroepindeling |
| Kanaal | *toegangspunt* | *ontsluit een dienst* | — | centrale set (besluit) | Doelgroepindeling |
| Beleidskader | *regeling als geheel*, *landelijk* | *is grondslag voor* (**bij voorkeur van een product**; proces of dienst tijdelijk, met een signaal) | *in werking* | de regeling als geheel; een artikel valt buiten het model | Beleidsdomeinindeling |
| Interaction | *gezamenlijk gedrag* | — | — | herkend, voorleggen | als bedrijfsproces |
| Representatie, locatie | — | — | — | geen pagina | — |

**Nieuwe kenmerken** (definitief na fase 1):

| Groep | Kenmerk | Vraag (kort) |
|---|---|---|
| Soort gedrag | *groepeert processen* | Inhoudelijke groepering van processen rond een taak of kernobject, zonder eigen doorloop? |
| Gedrag | *omvat bedrijfsprocessen* | Groepeert het minstens 2 bedrijfsprocessen? Noem ze |
| Gedrag | *bedient gedrag* | Ondersteunt de functie aanwijsbaar een bedrijfsproces? Noem het |
| Gedrag | *in functie-indeling* | Past de functie als onderwerp onder een soort werk in de Functie-indeling naar domein? Noem de bovenliggende functie |
| Gedrag | *meerdere partijen* | Twee of meer rollen of eenheden betrokken? |
| Gedrag | *meer organisaties* | Voeren twee of meer organisaties het samen uit, elk vanuit een eigen rol (niet de klant)? |
| Gedrag | *eigen besluit* | Eindigt het in een besluit van een bevoegd orgaan? |
| Gedrag | *bepaalt levensloop* | Brengt het één object in een nieuwe toestand? Noem het; daarbij het veld `kernobject` |
| Gedrag | *leidt tot gebeurtenis* | Eindigt het in een benoemde toestandsverandering of een die een ander proces start? |
| Partij | *soort partij* | Komt deze partij bij elke gemeente voor, en is het geen individuele organisatie? |
| Passief | *deel van object* | Onderdeel van één ander object, dat ermee ontstaat en eindigt? |
| Passief | *invoer van een ander* | Gemaakt door een andere partij, door de gemeente alleen geraadpleegd? |
| Passief | *zelfstandig aanbod* | Wordt het onder eigen naam aangeboden, en niet als variant of tarief van een ander product? |
| Specialisatie | *generiek* | Komt het met dezelfde betekenis in veel onderwerpen voor (besluit, aanvraag ontvangen, klant)? |

Hergebruikt worden: *aanleiding*, *afnemer* (nu ook voor processen), *benoembaar resultaat*, *eigen normering*, *bijdrage aan groter proces*, *zelfstandige specialisatie*, *leidt tot gedrag*.

**Indelingsvelden** in de beoordeling (verplicht per type, gecontroleerd door `tools/afleiden.py`): `taakveld` en `beleidsdomein` (bestaan), **`domein`** (GEMMA-domein: functie, product, dienst), **`doelgroep`** (actor, rol, samenwerking, kanaal), **`regelgever`** (beleidskader), **`kernobject`** (deeltaak, bedrijfsproces), **`afnemer`** extern of intern (bedrijfsproces, ketenproces, product, dienst).

**Stap 7 Indeling** (na stap 6, met de context van alle uitkomsten):
- **Proces**:
  - procescluster (taak, of deeltaak met `kernobject`) bij *groepeert processen*;
  - ketenproces bij *per keer doorlopen*, *meer organisaties* en *omvat bedrijfsprocessen*;
  - bedrijfsproces bij *aanleiding*, *afnemer*, *benoembaar resultaat* en *bepaalt levensloop*, plus minstens 2 van *meerdere partijen*, *eigen besluit* en *eigen normering*;
  - deelproces bij *bijdrage aan groter proces* met *eigen besluit* of *eigen normering*;
  - anders processtap: geen pagina.
- **Object**: generiek → kernobject → subobject → onderdeel; invoer krijgt geen pagina; anders voorleggen.
- **Generiek** bij gebeurtenis, rol en dienst: specialisatie zonder eigen indeling, of een generiek GEMMA-element met exacte match.
- **Controles**:
  - een plaats in de indeling is verplicht, en meer ouders geeft een signaal;
  - specialisatie en bediening naar GEMMA alleen via een exacte match;
  - triggering bij *leidt tot gebeurtenis*;
  - `via` naar een specialisatie;
  - een actorrelatie met een werkwoord van gedrag geeft een signaal;
  - relatietabel: aggregatie proces → proces en proces → gebeurtenis, compositie object → object, specialisatie van gebeurtenis, dienst en rol.

## Begrippen

Vastgelegd in `analyses/indelingen.md` en `ARCHITECTURE.md`, samen met wat over indelingen geleerd is.

- **Indeling**: een ordening van elementtypen naar één criterium, met benoemde niveaus.
- **Taak** en **deeltaak**: de niveaus van de procesindeling naar taak. Het zijn procesclusters (een groepering), geen echte processen.
- **Ketenproces**: een echt proces over meer organisaties (kennismodel). Het staat naast de taken.
- **Afnemer extern of intern**: voor wie het proces, product of de dienst is; dit volgt de externe en interne UPL-lijst.
- **Procesniveau** en **objectniveau**: zie de tabel.
- **Kernobject**: het object waarvan de processen van een deeltaak de levensloop bepalen.
- **Generiek, verhuizen later**: een generiek object blijft voorlopig element in het onderwerp, zodat de relaties geldig blijven, en verhuist naar een algemeen onderwerp. Domeinspecialisaties krijgen geen pagina. Ze staan per onderwerp op de generieke pagina en worden in relaties genoemd via het veld **`via`**.
- **Specialisatie of aggregatie**: specialisatie koppelt aan een GEMMA-indeling (wat voor soort?), aggregatie aan een eigen indeling (waar hoort het bij?).
- **Actoren**: alleen via een rol aan gedrag en objecten. Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); handelingen lopen via rollen en processen of een gebeurtenis.
- **Denkniveau**: per stap laag, middel of hoog, zonder modelnaam (portabiliteit, `AGENTS.md`). Ik controleer dat elke stap in de betrokken skills er een heeft.

## Fasen

| Fase | Denkniveau | Wat |
|---|---|---|
| 1 Analyse | hoog | `analyses/indelingen.md`: indelingen met GEMMA-bewijs, de validatie per type, begrippen, regels en een inschatting voor lijkbezorging. **De UPL-lijsten tellen mee als analysemateriaal**, gelezen van GEMMA Online, zonder ingest (zie hieronder). Open keuzes één voor één voorleggen (regel Navragen), waaronder het besluit over actoren als exemplaar |
| 2 Criteria | middel: besluiten omzetten in code; is iets dubbelzinnig, dan terug naar fase 1 | `tools/bepaal_type.py`: kenmerken, kernrelaties, stap 7, indelingsvelden; documentatie en schema genereren; controles en signalen |
| 3 Render en export | middel | Frontmatter `procesniveau` en `objectniveau`, sectie *Plaats in de indelingen*, `overzicht.md` per onderwerp, export-eigenschappen (`procesniveau`, `objectniveau`, `indeling` op aggregaties, `specialisatie` uit `via`); aggregaties vanuit de bestaande GEMMA-groeperingen (beleidsdomein, domein of functie, doelgroep) en de nieuwe clusters en ketens |
| 4 Overgang | laag | Eenmalig script in de scratchpad: nieuwe kenmerken als "nee, niet van toepassing" waar de aard ze uitsluit |
| 5 Herbeoordeling lijkbezorging | hoog | Volgens `gemma-archimate-model-update`; elk verlies van een pagina en elke nieuwe GEMMA-koppeling apart voorleggen; AKKOORD, export, controle in Archi |

**UPL-lijsten in deze analyse** (de externe lijst met 506 producten, de interne met 587):
- **Indelingen**: de kolommen (taakveld Iv3, GEMMA-domein, burger of bedrijf, generiek of specifiek, digitaal kanaal; intern ook sturend of ondersteunend en de functiecategorie) onderbouwen de indeling van producten en diensten in de Beleidsdomeinindeling en de Functie-indeling naar domein, de Doelgroepindeling (ook voor kanalen) en de eigenschap afnemer extern of intern.
- **Kenmerken ijken**: de 16 lijkbezorging-producten worden naast de processen gelegd (grafuitgifte – Verlenen grafrecht, herbegraven of alsnog cremeren – Opgraven lijk, grafonderhoud – Onderhouden graf …). Toets: geeft de niveauregel *bedrijfsproces* voor elk proces dat een UPL-product levert, en geven *zelfstandig aanbod* en *afnemer* de juiste producten? Afwijkingen leiden tot bijstelling in fase 1.
- **Abstractie**: de UPL laat zien op welk niveau gemeenten hun aanbod benoemen (één product per UPL-naam, geen varianten).
- **Grondslagen**: de grondslagkolommen wijzen bronnen aan voor beleidskaders.
- Deze analyse citeert de lijsten met hun vindplaats op GEMMA Online. In beoordelingen komen ze pas na de ingest.

**Naar `todo.md`**:
- de UPL-lijsten (extern en intern) opnemen als bron (`gemma-archimate-model-ingest`), met bronanalyse. Daarna de producten en diensten van lijkbezorging beoordelen, en via de grondslagkolommen bronnen zoeken;
- de applicatielaag in de wiki;
- generieke GEMMA-gebeurtenissen;
- het advies over referentiecomponenten;
- Archi-views per indeling en elementtype in de export, na de eerste proefimport (herziening van het besluit van 2026-10-02).

## Verwachte uitkomst lijkbezorging (ter toetsing)

- **Processen**: *Verzorgen lijkbezorging* (nu functie; de partiële match vervalt):
  - *Bezorgen lijken* (Lijk): Uitvoeren lijkbezorging, Opgraven lijk, Verzorgen gemeentebegrafenis, Treffen maatregel bij besmet lijk;
  - *Beheren grafrechten* (Grafrecht): Verlenen grafrecht, Vervallen verklaren grafrecht;
  - *Beheren graven* (Graf): Ruimen graf, Onderhouden graf (bedrijfsproces of stap);
  - Schouwen lijk wordt deelproces of stap.
- **Keten** (kandidaat, voorleggen): *Afhandelen overlijden* (naam volgens de regel Naamvorm). Overlijden → schouwen (arts of gemeentelijke lijkschouwer) → aangifte en verlof (burgerlijke stand, onderwerp Burgerzaken) → Uitvoeren lijkbezorging, met de officier van justitie bij een niet-natuurlijke dood. Realiseert een dienst aan nabestaanden; afnemer extern.
- **Functies**: *Exploiteren van begraafplaatsen*, *Burgerlijke stand diensten* en andere als element met exacte match, die bedienen.
- **Gebeurtenissen**: Overlijden (taak), Verval van het grafrecht (Beheren grafrechten), Besmet lijk gemeld (Bezorgen lijken).
- **Objecten**:
  - kernobject: Lijk, Graf, Grafrecht (of een specialisatie: voorleggen);
  - subobject of onderdeel: Grafbedekking, Plaats van bijzetting, Urn;
  - invoer: Verklaring van overlijden;
  - generiek: Besluit, Beschikking, Vergunning, Heffing, Heffingsverordening, Regeling.
- **Doelgroepen**:
  - gemeente: Gemeenteraad, College van B&W, Burgemeester, Ambtenaar van de burgerlijke stand, Beheerder;
  - inwoners en ondernemers: Nabestaande, Rechthebbende op het graf, Uitvaartondernemer;
  - ketenpartners: GGD, Kerkgenootschap.
- **Actorrelaties**: Burgemeester als voorzitter blijft; *GGD geeft melding door* en *College benoemt lijkschouwer* gaan via rollen en processen of een gebeurtenis.

## Kritieke bestanden

- **Code**: `wikis/gemma-archimate-model/tools/` (`bepaal_type.py`, `afleiden.py`, `relaties.py`, `signalen.py`, `render.py`, `archimate_export.py`) en `tools/tests/test_gam_*.py`.
- **Documentatie**: `analyses/indelingen.md` (nieuw), `analyses/kenmerken.md`, `ARCHITECTURE.md`, `todo.md`.
- **Gegenereerd**: `analyses/beslistabel.md`, het blok in de criteria-skill, `schemas/beoordeling.schema.json`.
- **Skills**: denkniveau per stap in `gemma-archimate-model-update`, `-beoordelen` en `-archimate-export`.
- **Beoordelingen**: `beoordelingen/begrippen/*.yaml`.

## Verificatie

- **Tests**: `uv run pytest tools/tests`. Nieuwe tests dekken:
  - per type de kernrelatie en de regel voor een eigen pagina;
  - stap 7 en de verplichte indelingsvelden;
  - de controles op exacte match, triggering, `via` en actorrelaties;
  - de export-eigenschappen en het overzicht.
  - Daarnaast de bestaande gelijkheidstest van de gegenereerde documentatie en het schema.
- **IJking met de UPL**: in de analyse een tabel van de 16 lijkbezorging-producten met het proces dat ze levert en de uitkomst van de niveauregel. Elk proces met een UPL-product komt uit als bedrijfsproces of ketenproces.
- **Compleetheid**: een test dat elk type met een pagina een typebepalend kenmerk, een kernrelatie, een regel voor een eigen pagina en een verplichte indeling heeft.
- **Scripts**: `tools/afleiden.py` zonder fouten, `tools/render.py --check`, en `uv run python -m llmwiki lint`.
- **Export**: `tools/archimate_export.py --check` en de export. In Archi zijn de indelingen zichtbaar, de GEMMA-indelingen onaangeroerd, en de eigenschappen aanwezig.
- **Voortgang**: `voortgang.md` voor en na, met het aantal elementen per type.
