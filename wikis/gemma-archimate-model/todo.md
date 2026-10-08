# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herbeoordeling met de nieuwe werkwijze (2026-10-01)

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar, besluit redacteur 2026-10-01): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-model art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-model toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).

## Wettelijke grondslag (analyse 2026-10-08, `analyses/wettelijke-grondslag.md`)

- **Richtlijnen als beleidskader** (besluit 9): per onderwerp beoordelen welke landelijke richtlijnen als geheel een beleidskader worden, met relatie *geeft richtlijn voor*. Kandidaten in burgerzaken: de HUP van RvIG (per hoofdstuk of als geheel, voorleggen), de Circulaire adresonderzoek BRP, de NVVB-handreikingen adresonderzoek en gezag.
- **Licentie VNG-modellen**: de Model-APV (2023-vng-model-apv) en de Model beheersverordening (2010) staan letterlijk in `sources/raw/` van een publieke repository, zonder licentie in de bron. Laat de VNG (juridische zaken of het team modelverordeningen) bevestigen dat hergebruik mag, of er een licentie op zetten. De VNG herziet de Model-APV volledig (gepland begin 2027): vervang dan de bron.

## Indelingen (analyse 2026-10-04, `analyses/indelingen.md`)

- **Definitie van Ketenpartner**: nu "verantwoordelijkheid van een andere organisatie", terwijl de rol wordt vervuld door personen (Arts als behandelende arts, Officier van justitie; besluit redacteur 2026-10-04). Definitie verbreden naar een andere partij, of de organisatie (openbaar ministerie, zorgaanbieder) als actor nemen; meenemen in het voorstel aan het GEMMA-team over de definitie van de rol Ketenpartner.
- **Verlengen en overschrijven van het grafrecht**: nu onderdelen van Grafrecht (eigen identiteit nee). Mogelijk eigen bedrijfsprocessen onder het levensloopproces Beheren grafrechten (eigen besluit, Wlb art. 28 lid 1–3; Groningen art. 16–20). De UPL kent er geen eigen product voor (beoordeling UPL-producten 2026-10-05).
- **Interne UPL-lijst**: staat in `sources/` en krijgt een bronanalyse bij het eerste onderwerp met sturende of ondersteunende producten.
- **Kennismodel-aanvullingen als GEMMA-terugmelding**: de wiki gebruikt elementen en relaties die Over GEMMA niet kent (`export/rapport.md`, Kennismodel-wiki): Afspraak met toegang door bedrijfsproces en rol, aggregatie van Dienst door Bedrijfsfunctie (76×), flow tussen bedrijfsprocessen (7×) en triggering tussen gebeurtenissen (5×). Bepaal of ze in het GEMMA-model zelf voorkomen en meld de ontbrekende bij de procesarchitectuur-terugmeldingen over het kennismodel (5 en 6).
- **Voorstellen aan het GEMMA-team** (de voorstellen over het GEMMA-model zelf staan in `beoordelingen/terugmeldingen/gemma.yaml`):
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7, met de GEMMA-domeinen waaronder het valt (procesarchitectuur-terugmelding 1);
  - de procesarchitectuur-terugmeldingen over het kennismodel: de tegenspraak over het ketenproces tussen het kennismodel en de pagina Proceshiërarchie (5), structurele relaties tussen actoren (6), en het levensloopproces als cluster per thema met de themaclusters van de ondersteunende tak als groepering per beleidsdomein (20); 4 is opgelost door de procesniveaus van 2026-10-08.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein. Daarbij de referentiecomponenten: in GEMMA hangt geen van de 256 applicatiecomponenten direct aan een bedrijfsfunctie, 76 alleen aan een groepering. Beoordeel de koppeling (aggregatie door een hogere bedrijfsfunctie, als ArchiMate dat toestaat, of via de applicatieservice die de functie bedient) en maak dan een GEMMA-terugmelding (besluit redacteur 2026-10-08).
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (herziening van het besluit van 2026-10-02: geen views).

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).

## Algemeen onderwerp besluitvorming en heffingen

- **Algemeen onderwerp besluitvorming** voor de generieke elementen Besluit, Beschikking, Vergunning, Heffing, Heffingsverordening en Regeling, en voor Uniforme openbare voorbereidingsprocedure, Bestuursorgaan en Beleidsnota. Het onderwerp Algemeen bestaat sinds 2026-10-06 (licht ingericht); de elementen verhuizen per geval.
- **Bestuursorgaan**: zolang het geen element is, staat de toewijzing van inspraak aan het college en de gemeenteraad niet in het model.
- **VNG Modelverordening lijkbezorgingsrechten** (ledenbrief 2011, met kostenonderbouwing) als bron en mogelijk beleidskader opnemen bij het algemene onderwerp voor Heffing en Heffingsverordening (besluit redacteur 2026-10-01). De link op de VNG-pagina `https://vng.nl/artikelen/modelverordeningen-wet-op-de-lijkbezorging` geeft een 404; zoek een openbare kopie.

## Onderwerpen als één model (besluit 2026-10-06)

- **Belanghebbende** beoordelen in Algemeen (Awb art. 1:2; besluit 2026-10-06: generiek, hoort bij Algemeen). Nu nog een verwijzing in Lijkbezorging; vraagt een volledige beoordeling met bron en GGM-terugmelding 9.
- **Bronanalyse per onderwerp in de render**: een bron met een bronanalyse in meer onderwerpen (UPL extern: lijkbezorging en burgerzaken) krijgt op elke pagina een link naar de alfabetisch eerste lens; sinds Burgerzaken linken lijkbezorgingspagina's naar de lens van Burgerzaken. Kies de lens van het thuisonderwerp van de pagina.

## Verwijzingen vanuit Burgerzaken (onderwerp afgerond op 2026-10-07)

Begrippen die thuishoren in een onderwerp dat nog niet bestaat; ze staan als verwijzing in de begrippenlijst van Burgerzaken.

- **Verkiezingen** (organisatie): Kandidaatstelling verkiezingen, Stembiljet, Stemmen identificatieplicht (UPL nr. 205, 395, 396; Kieswet).
- **Invordering**: Verzoeken om signalering (Paspoortwet art. 22).
- **Adressen en BAG**: Adres.
- **Openbare ruimte**: de vier meldingen openbare ruimte (UPL nr. 243 tot en met 246).
- **Sociaal domein**: Overlijdensuitkering (UPL nr. 317).
- **Dienstverlening aan inwoners en leefomgeving**: Contactgegevens aanpassing (UPL nr. 105), Reclamesticker (UPL nr. 348).
- **Wet griffierechten burgerlijke zaken en Overeenkomst van München**: of ze bron en beleidskader worden, hangt af van de vragen bij Legalisatie handtekening en Verklaring van huwelijksbevoegdheid.
