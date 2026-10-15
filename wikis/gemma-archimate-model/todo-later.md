# Todo later

Punten die nu niet aan de orde zijn. [todo.md](todo.md) heeft het actieve werk; haal een punt hierheen of daarvandaan met de tekst ongewijzigd. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Wettelijke grondslag (ARCHITECTURE.md, secties 3.4 en 4.2)

- **Licentie VNG-modelverordeningen**: de Model-APV (2023-vng-model-apv) en de Model beheersverordening (2010) staan letterlijk in `sources/raw/` van een publieke repository, zonder licentie in de bron. Laat de VNG (juridische zaken of het team modelverordeningen) bevestigen dat hergebruik mag, of er een licentie op zetten. De VNG herziet de Model-APV volledig (gepland begin 2027): vervang dan de bron.

## Indelingen (ARCHITECTURE.md, sectie 4.4)

- **Functie-indeling naar domein: welke elementtypen en op welk niveau**: bepaal welke elementtypen volgens de Functie-indeling worden ingedeeld (nu functies, producten en diensten; een dienst hangt onder één bovenliggende functie), en op welk niveau van de functiehiërarchie: een duidelijk niveau, de bedrijfsfunctie of hoger, nooit een subfunctie. Indelen is alles of niks, maar de huidige plekken komen inhoudelijk willekeurig over: zo hangt Uitvaart vervroegen of uitstellen onder Vergunningbeheer publieksdiensten, een subfunctie van Producten- en dienstenrealisatie publieksdiensten. Tot dit is beslist, krijgt een nieuwe dienst geen functie als die niet eenduidig volgt, en blijft de waarschuwing "hangt onder geen functie" staan (Zienswijze, besluit 2026-10-11; de diensten van Besluitvorming deel 2, besluiten 2026-10-12). GEMMA heeft voor bezwaar en klacht functies onder Ondersteuning (Juridische ondersteuning) én, voor klacht en schade, onder Publieksdiensten.
- **Definitie van Ketenpartner**: nu "verantwoordelijkheid van een andere organisatie", terwijl de rol wordt vervuld door personen (Arts als behandelende arts, Officier van justitie). Definitie verbreden naar een andere partij, of de organisatie (openbaar ministerie, zorgaanbieder) als actor nemen; meenemen in het voorstel aan het GEMMA-team over de definitie van de rol Ketenpartner.
- **Verlengen en overschrijven van het grafrecht**: nu onderdelen van Grafrecht (eigen identiteit nee). Mogelijk eigen bedrijfsprocessen onder het levensloopproces Beheren grafrechten (eigen besluit, Wlb art. 28 lid 1–3; Groningen art. 16–20). De UPL kent er geen eigen product voor (beoordeling UPL-producten).
- **Kennismodel-aanvullingen als GEMMA-terugmelding**: de wiki gebruikt elementen en relaties die Over GEMMA niet kent (`export/rapport.md`, Kennismodel-wiki): Afspraak met toegang door bedrijfsproces en rol, aggregatie van Dienst door Bedrijfsfunctie (76×), flow tussen bedrijfsprocessen (7×) en triggering tussen gebeurtenissen (5×). Bepaal of ze in het GEMMA-model zelf voorkomen en meld de ontbrekende bij de procesarchitectuur-terugmeldingen over het kennismodel (5 en 6).
- **Voorstellen aan het GEMMA-team** (de voorstellen over het GEMMA-model zelf staan in `modellen/gemma/terugmeldingen/gemma-team.yaml`):
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7, met de GEMMA-domeinen waaronder het valt (procesarchitectuur-terugmelding 1);
  - de procesarchitectuur-terugmeldingen over het kennismodel: de tegenspraak over het ketenproces tussen het kennismodel en de pagina Proceshiërarchie (5), structurele relaties tussen actoren (6), en het levensloopproces als cluster per thema met de themaclusters van de ondersteunende tak als groepering per beleidsdomein (20); 4 is opgelost door de procesniveaus van 2026-10-08.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein. Daarbij de referentiecomponenten: in GEMMA hangt geen van de 256 applicatiecomponenten direct aan een bedrijfsfunctie, 76 alleen aan een groepering. Beoordeel de koppeling (aggregatie door een hogere bedrijfsfunctie, als ArchiMate dat toestaat, of via de applicatieservice die de functie bedient) en maak dan een GEMMA-terugmelding.
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (nu geen views). Eerste kandidaat (vraag redacteur 2026-10-13): per levensloopproces een view met beleidsdomein, levensloopproces, de bedrijfsprocessen en gebeurtenissen die het aggregeert en het kernobject; het beleidsdomein is de ingang, niet het onderwerp, want de export gebruikt de onderwerpen niet (ARCHITECTURE.md, sectie 4.4). Sluit aan bij optie 1 van Overzicht bij veel toegangsrelaties.

## Kennismodel

- **Consolidatie van indelingen** (als eigen klus met een plan; `plannen/2026-10-10-indelingen.md` is klaar): de ontstane indelingen (onderwerpen, Procesindeling naar kernobject, Grondslagindeling) naast de overgenomen (GEMMA, Iv3, GGM, UPL) leggen, overlap beoordelen en bepalen wat in de export meegaat (ARCHITECTURE.md, sectie 4.4).
- **Conflicten met GEMMA Online**: een momentopname van GEMMA Online in `sources/` (opgehaald met pywikibot, brontype `model`), en een vergelijking van de inhoud van de wiki daarmee; een conflict wordt een GEMMA-terugmelding (ARCHITECTURE.md, sectie 2).
- **Kwaliteitsdoelen per beleidskader beoordelen** (na fase 5 van het plan kennismodel, als eigen klus): het kennismodel, het veld `kwaliteitsdoelen`, de controle, de render en de export bestaan. Beoordeel per beleidskader aan welke kwaliteitsdoelen van GEMMA (`tools/gemma.py kwaliteitsdoelen`) het grondslag geeft en hoe sterk, met de bepalingen als onderbouwing; leg het voor en vraag AKKOORD.
- **Overzicht bij veel toegangsrelaties**: sommige bedrijfsobjecten krijgen zoveel toegangsrelaties dat het overzicht eronder lijdt (Ingeschreven persoon 27, waarvan 14 van een ander proces dan dat van het kernobject; Akte van de burgerlijke stand 14, Stoffelijk overschot 11). Het toegangstype volgt uit de handeling, niet uit eigenaarschap (ARCHITECTURE.md, sectie 6.5; besluit 2026-10-13). Overwegingen, in volgorde van voorkeur: (1) overzicht in views, niet in het model: de export maakt per levensloopproces of kernobject een view met de schrijvende relaties, eventueel een tweede met de lezende; (2) een drempel voor lezen: alleen als het object nodig is voor het resultaat van het proces, niet alleen om de klant te identificeren; (3) lezen via de verstrekking: een ander proces gebruikt het object via een dienst van het levensloopproces (bediening in plaats van toegang), past bij verstrekker en afnemer maar verplaatst het aantal relaties alleen; (4) lezen op het niveau van functie of levensloopproces leggen: verliest precisie, afgeraden. Beslissen welke, dan kennismodel, modelleerregels en export bijwerken.
- **Toegangstype Rol → Bedrijfsobject in Over GEMMA**: de relatie *heeft toegang tot* is schrijven (`accessType="Write"`, ook de standaard van Archi voor een nieuwe toegangsrelatie), terwijl Bedrijfsproces en Bedrijfsfunctie naar Bedrijfsobject lezen-schrijven zijn (*benadert*). Waarschijnlijk niet bedoeld; het kennismodel van de wiki neemt de relatie met haar id en toegangstype over. Nagaan en zo nodig een terugmelding over het kennismodel.

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).

## Thematisch gedeelde onderwerpen: Besluitvorming, Bestuur en organisatie, Heffingen en betalingen

- **Besluitvorming, specialisaties naar de generieke processen**: de diensten en beslisprocessen op aanvraag in de onderwerpen (zoals Verlof tot begraven en Behandelen aanvraag reisdocument) zijn gevallen van de generieke dienst Beschikking aanvragen en het generieke proces Behandelen aanvraag beschikking. Bepaal of en hoe ze die specialiseren, naast hun koppeling met de GEMMA-processen (`gemma_generiek`); per geval voorleggen, want het raakt goedgekeurde beoordelingen in andere onderwerpen.
- **Bestuur en organisatie**: de Gemeentewet (nu een verwijzing) als bron en mogelijk beleidskader.
- **Heffen van rechten** bij het onderwerp Heffingen en betalingen: het proces dat de heffingsverordening raadpleegt voor de tarieven bij uitgifte en onderhoud (Groningen art. 8, 23, 24). Dat lost de signalen *wordt bewerkt* zonder toegang bij Heffingsverordening en Regeling op, en geeft de relatie *regelt het recht voor* van Heffingsverordening naar Grafonderhoud (nu buiten het kennismodel) een plek via dat proces.
- **Belastingaanslag bezwaar** (UPL nr. 49) bij Heffingen en betalingen, bij het kernobject Belastingaanslag: met de Algemene wet inzake rijksbelastingen en Gemeentewet art. 231 als bronnen, als specialisatie van de dienst Bezwaar, gerealiseerd door Behandelen bezwaar (besluit 2026-10-12 bij het onderwerp).
- **VNG Modelverordening lijkbezorgingsrechten** (ledenbrief 2011, met kostenonderbouwing) als bron en mogelijk beleidskader opnemen bij Heffingen en betalingen. De link op de VNG-pagina `https://vng.nl/artikelen/modelverordeningen-wet-op-de-lijkbezorging` geeft een 404; zoek een openbare kopie.

## Nieuwe onderwerpen uit de Awb (besluiten 2026-10-12 bij Besluitvorming)

- **Subsidies** (eigen onderwerp): kernobject Subsidie, het GGM-domein Subsidies, het GEMMA-proces Verstrekken subsidie, de Awb titel 4.2 als grondslag en de VNG Model algemene subsidieverordening als bron; de dienst Subsidie (UPL nr. 402) en de specifieke subsidies uit de UPL.
- **Handhaving** (thematisch onderwerp, Awb hoofdstuk 5): overtreding, bestuurlijke sanctie, last onder bestuursdwang en last onder dwangsom, de GEMMA-processen Opleggen sanctie en Uitvoeren sanctie en het GGM-domein Normafwijking; de diensten Bestuurlijke boete (UPL nr. 59) en Spoedeisende bestuursdwang (UPL nr. 386).
- **Omgevingswet**: Omgevingswet nadeelcompensatie (UPL nr. 296, afdeling 15.1 Omgevingswet) staat als verwijzing in de begrippenlijst van Besluitvorming, mogelijk als specialisatie van Nadeelcompensatie.

## Verwijzingen vanuit Burgerzaken (onderwerp afgerond op 2026-10-07)

Begrippen die thuishoren in een onderwerp dat nog niet bestaat; ze staan als verwijzing in de begrippenlijst van Burgerzaken.

- **Verkiezingen** (organisatie): Kandidaatstelling verkiezingen, Stembiljet, Stemmen identificatieplicht (UPL nr. 205, 395, 396; Kieswet).
- **Invordering**: Verzoeken om signalering (Paspoortwet art. 22).
- **Adressen en BAG**: Adres.
- **Openbare ruimte**: de vier meldingen openbare ruimte (UPL nr. 243 tot en met 246).
- **Sociaal domein**: Overlijdensuitkering (UPL nr. 317).
- **Dienstverlening aan inwoners en leefomgeving**: Contactgegevens aanpassing (UPL nr. 105), Reclamesticker (UPL nr. 348).
- **Overeenkomst van München**: of zij bron en beleidskader wordt, hangt af van de vraag bij Verklaring van huwelijksbevoegdheid. De Wet griffierechten burgerlijke zaken is geen grondslag voor Legalisatie handtekening, die zonder grondslag is (besluit 2026-10-11).
