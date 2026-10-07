# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herbeoordeling met de nieuwe werkwijze (2026-10-01)

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar, besluit redacteur 2026-10-01): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-model art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-model toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).

## Indelingen (analyse 2026-10-04, `analyses/indelingen.md`)

- **Definitie van Ketenpartner**: nu "verantwoordelijkheid van een andere organisatie", terwijl de rol wordt vervuld door personen (Arts als behandelende arts, Officier van justitie; besluit redacteur 2026-10-04). Definitie verbreden naar een andere partij, of de organisatie (openbaar ministerie, zorgaanbieder) als actor nemen; meenemen in het voorstel aan het GEMMA-team over de definitie van de rol Ketenpartner.
- **Verlengen en overschrijven van het grafrecht**: nu onderdelen van Grafrecht (eigen identiteit nee). Met de criteria van 2026-10-04 mogelijk deelprocessen van Beheren grafrechten (eigen besluit, Wlb art. 28 lid 1–3; Groningen art. 16–20). De UPL kent er geen eigen product voor (beoordeling UPL-producten 2026-10-05).
- **Interne UPL-lijst**: staat in `sources/` en krijgt een bronanalyse bij het eerste onderwerp met sturende of ondersteunende producten.
- **Voorstellen aan het GEMMA-team**:
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7, met de GEMMA-domeinen waaronder het valt (procesarchitectuur-terugmelding 1);
  - generieke gebeurtenissen (aanvraag ontvangen, besluit bekendgemaakt);
  - de afwijkingen van het kennismodel procesarchitectuur: een deelproces levert een dienst, een ketenproces bevat deelprocessen, structurele relaties tussen actoren (procesarchitectuur-terugmeldingen 4–6);
  - het advies om referentiecomponenten te laten aggregeren door een hogere bedrijfsfunctie;
  - de definities van de GEMMA-rollen Ketenpartner, Adviseur en Beslisser, die in GEMMA leeg zijn en die de export met de definitie uit de wiki vult.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein.
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (herziening van het besluit van 2026-10-02: geen views).

## Ketenprocessen en bedrijfsprocessen (besluit 2026-10-07)

Drie ketenprocessen aggregeren deelprocessen rechtstreeks, wat het kennismodel niet kent (besluit in [besluiten](analyses/besluiten-redacteur.md)): Bezorgen stoffelijk overschot (10 deelprocessen), Beheren Nederlanderschap (4) en Afgeven verklaring omtrent het gedrag (1).

- **Bedrijfsprocessen ertussen**: per ketenproces bedrijfsprocessen die logische groepen deelprocessen aggregeren, liefst geen 1-op-1, bij voorkeur per uitvoerende partij. Voorstel: Behandelen aanvraag VOG wordt het bedrijfsproces van het gemeentelijke deel; Beheren Nederlanderschap krijgt één bedrijfsproces voor het gemeentelijke deel met alle vier de deelprocessen; bij Bezorgen eerst per deelproces uitzoeken wie het uitvoert. Verzorgen gemeentebegrafenis blijft direct onder het ketenproces.
- **Criteria en beslistabel**: leg de lezing van *omvat levensloop* vast (ketenproces over de partijen heen, bedrijfsproces het deel van één partij) in de skill gemma-archimate-model-criteria en in [Beslistabel](analyses/beslistabel.md), en een ketenproces aggregeert alleen bedrijfsprocessen.
- **Terugmeldingen**: procesarchitectuur-terugmelding 5 bijwerken (nog alleen een afwijking voor wat blijft) en als voorstel aan het GEMMA-team: bedrijfsproces is het deel van één partij binnen een ketenproces.
- **Daarna** nieuwe export.

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).

## Algemeen onderwerp besluitvorming en heffingen

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
