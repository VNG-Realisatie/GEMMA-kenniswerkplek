# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herbeoordeling met de nieuwe werkwijze

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-modelverordening art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-modelverordening toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).

## Wettelijke grondslag (ARCHITECTURE.md, secties 3.4 en 4.2)

- **Licentie VNG-modelverordeningen**: de Model-APV (2023-vng-model-apv) en de Model beheersverordening (2010) staan letterlijk in `sources/raw/` van een publieke repository, zonder licentie in de bron. Laat de VNG (juridische zaken of het team modelverordeningen) bevestigen dat hergebruik mag, of er een licentie op zetten. De VNG herziet de Model-APV volledig (gepland begin 2027): vervang dan de bron.

## Indelingen (ARCHITECTURE.md, sectie 4.4)

- **Functie-indeling naar domein: welke elementtypen en op welk niveau**: bepaal welke elementtypen volgens de Functie-indeling worden ingedeeld (nu functies, producten en diensten; een dienst hangt onder één bovenliggende functie), en op welk niveau van de functiehiërarchie: een duidelijk niveau, de bedrijfsfunctie of hoger, nooit een subfunctie. Indelen is alles of niks, maar de huidige plekken komen inhoudelijk willekeurig over: zo hangt Uitvaart vervroegen of uitstellen onder Vergunningbeheer publieksdiensten, een subfunctie van Producten- en dienstenrealisatie publieksdiensten. Tot dit is beslist, krijgt een nieuwe dienst geen functie als die niet eenduidig volgt, en blijft de waarschuwing "hangt onder geen functie" staan (Zienswijze, besluit 2026-10-11).
- **Definitie van Ketenpartner**: nu "verantwoordelijkheid van een andere organisatie", terwijl de rol wordt vervuld door personen (Arts als behandelende arts, Officier van justitie). Definitie verbreden naar een andere partij, of de organisatie (openbaar ministerie, zorgaanbieder) als actor nemen; meenemen in het voorstel aan het GEMMA-team over de definitie van de rol Ketenpartner.
- **Verlengen en overschrijven van het grafrecht**: nu onderdelen van Grafrecht (eigen identiteit nee). Mogelijk eigen bedrijfsprocessen onder het levensloopproces Beheren grafrechten (eigen besluit, Wlb art. 28 lid 1–3; Groningen art. 16–20). De UPL kent er geen eigen product voor (beoordeling UPL-producten).
- **Kennismodel-aanvullingen als GEMMA-terugmelding**: de wiki gebruikt elementen en relaties die Over GEMMA niet kent (`export/rapport.md`, Kennismodel-wiki): Afspraak met toegang door bedrijfsproces en rol, aggregatie van Dienst door Bedrijfsfunctie (76×), flow tussen bedrijfsprocessen (7×) en triggering tussen gebeurtenissen (5×). Bepaal of ze in het GEMMA-model zelf voorkomen en meld de ontbrekende bij de procesarchitectuur-terugmeldingen over het kennismodel (5 en 6).
- **Voorstellen aan het GEMMA-team** (de voorstellen over het GEMMA-model zelf staan in `modellen/gemma/terugmeldingen/gemma-team.yaml`):
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7, met de GEMMA-domeinen waaronder het valt (procesarchitectuur-terugmelding 1);
  - de procesarchitectuur-terugmeldingen over het kennismodel: de tegenspraak over het ketenproces tussen het kennismodel en de pagina Proceshiërarchie (5), structurele relaties tussen actoren (6), en het levensloopproces als cluster per thema met de themaclusters van de ondersteunende tak als groepering per beleidsdomein (20); 4 is opgelost door de procesniveaus van 2026-10-08.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein. Daarbij de referentiecomponenten: in GEMMA hangt geen van de 256 applicatiecomponenten direct aan een bedrijfsfunctie, 76 alleen aan een groepering. Beoordeel de koppeling (aggregatie door een hogere bedrijfsfunctie, als ArchiMate dat toestaat, of via de applicatieservice die de functie bedient) en maak dan een GEMMA-terugmelding.
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (nu geen views).

## Kennismodel

- **Consolidatie van indelingen** (als eigen klus met een plan; `plannen/2026-10-10-indelingen.md` is klaar): de ontstane indelingen (onderwerpen, Procesindeling naar kernobject, Grondslagindeling) naast de overgenomen (GEMMA, Iv3, GGM, UPL) leggen, overlap beoordelen en bepalen wat in de export meegaat (ARCHITECTURE.md, sectie 4.4).
- **Conflicten met GEMMA Online**: een momentopname van GEMMA Online in `sources/` (opgehaald met pywikibot, brontype `model`), en een vergelijking van de inhoud van de wiki daarmee; een conflict wordt een GEMMA-terugmelding (ARCHITECTURE.md, sectie 2).
- **Kwaliteitsdoelen per beleidskader beoordelen** (na fase 5 van het plan kennismodel, als eigen klus): het kennismodel, het veld `kwaliteitsdoelen`, de controle, de render en de export bestaan. Beoordeel per beleidskader aan welke kwaliteitsdoelen van GEMMA (`tools/gemma.py kwaliteitsdoelen`) het grondslag geeft en hoe sterk, met de bepalingen als onderbouwing; leg het voor en vraag AKKOORD.

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).

## Thematisch gedeelde onderwerpen: Besluitvorming, Bestuur en organisatie, Heffingen en betalingen

- **Besluitvorming, plak 2**: de overige UPL-diensten met de Awb als grondslag beoordelen: bezwaar (art. 7:1), beroep (art. 8:1), klacht (art. 9:1), bekendmaking (art. 3:40), dwangsom bij niet tijdig beslissen (art. 4:17), nadeelcompensatie (art. 4:126) en de UPL-dienst beschikking (art. 1:3, naast het bedrijfsobject Beschikking); bepalen waar subsidie (art. 4:21), bestuurlijke boete (art. 5:40), spoedeisende bestuursdwang (art. 5:31) en belastingaanslag bezwaar (art. 7:1) thuishoren. Lees daarvoor de hoofdstukken 3 (bekendmaking), 4 (dwangsom, nadeelcompensatie), 6 tot en met 9 van de Awb en vul de bronduiding aan. Plak 1 (Awb als beleidskader, Belanghebbende, Aanvraag, Uitvoeren uniforme openbare voorbereidingsprocedure met Zienswijze, Bestuursorgaan als synoniem van Beslisser, Beleidsnota, Beleidsregel) is afgerond.
- **Bestuur en organisatie**: de Gemeentewet (nu een verwijzing) als bron en mogelijk beleidskader.
- **Heffen van rechten** bij het onderwerp Heffingen en betalingen: het proces dat de heffingsverordening raadpleegt voor de tarieven bij uitgifte en onderhoud (Groningen art. 8, 23, 24). Dat lost de signalen *wordt bewerkt* zonder toegang bij Heffingsverordening en Regeling op, en geeft de relatie *regelt het recht voor* van Heffingsverordening naar Grafonderhoud (nu buiten het kennismodel) een plek via dat proces.
- **VNG Modelverordening lijkbezorgingsrechten** (ledenbrief 2011, met kostenonderbouwing) als bron en mogelijk beleidskader opnemen bij Heffingen en betalingen. De link op de VNG-pagina `https://vng.nl/artikelen/modelverordeningen-wet-op-de-lijkbezorging` geeft een 404; zoek een openbare kopie.

## Verwijzingen vanuit Burgerzaken (onderwerp afgerond op 2026-10-07)

Begrippen die thuishoren in een onderwerp dat nog niet bestaat; ze staan als verwijzing in de begrippenlijst van Burgerzaken.

- **Verkiezingen** (organisatie): Kandidaatstelling verkiezingen, Stembiljet, Stemmen identificatieplicht (UPL nr. 205, 395, 396; Kieswet).
- **Invordering**: Verzoeken om signalering (Paspoortwet art. 22).
- **Adressen en BAG**: Adres.
- **Openbare ruimte**: de vier meldingen openbare ruimte (UPL nr. 243 tot en met 246).
- **Sociaal domein**: Overlijdensuitkering (UPL nr. 317).
- **Dienstverlening aan inwoners en leefomgeving**: Contactgegevens aanpassing (UPL nr. 105), Reclamesticker (UPL nr. 348).
- **Overeenkomst van München**: of zij bron en beleidskader wordt, hangt af van de vraag bij Verklaring van huwelijksbevoegdheid. De Wet griffierechten burgerlijke zaken is geen grondslag voor Legalisatie handtekening, die zonder grondslag is (besluit 2026-10-11).
