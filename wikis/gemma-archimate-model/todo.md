# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herbeoordeling met de nieuwe werkwijze (2026-10-01)

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar, besluit redacteur 2026-10-01): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-model art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-model toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).

## Indelingen (analyse 2026-10-04, `analyses/indelingen.md`)

- **Lijkbezorging in Archi**: na het akkoord op de elementen in `ter-beoordeling.md` opnieuw exporteren, importeren in een GEMMA-kopie (*File › Import › Model into selected model…*, bestaande objecten bijwerken), jArchi-script draaien, controleren dat gekoppelde elementen in hun GEMMA-map blijven, geen dubbele mappen ontstaan, `Object ID` blijft staan. Het exportbestand in Archi nooit opslaan (Archi overschrijft het en maakt een `.bak`). Daarna `voortgang.md` bijwerken (was: 48 elementen).
- **Verlengen en overschrijven van het grafrecht**: nu onderdelen van Grafrecht (eigen identiteit nee). Met de criteria van 2026-10-04 mogelijk deelprocessen van Beheren grafrechten (eigen besluit, Wlb art. 28 lid 1–3; Groningen art. 16–20). Beoordelen samen met de UPL-producten.
- **UPL-lijsten als bron**: de externe en interne lijst van GEMMA Online (*Producten en diensten procesarchitectuur*) opnemen met `gemma-archimate-model-ingest`. Daarna de producten en diensten van lijkbezorging beoordelen (16 in de externe lijst). Via de grondslagkolommen bronnen zoeken voor de gaten: de model-APV (asverstrooiing) en het Besluit op de lijkbezorging (vervoersdocumenten).
- **Voorstellen aan het GEMMA-team**:
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7;
  - generieke gebeurtenissen (aanvraag ontvangen, besluit bekendgemaakt);
  - de afwijkingen van het kennismodel procesarchitectuur: een deelproces levert een dienst, een ketenproces bevat deelprocessen, structurele relaties tussen actoren;
  - het advies om referentiecomponenten te laten aggregeren door een hogere bedrijfsfunctie;
  - de definities van de GEMMA-rollen Ketenpartner, Adviseur en Beslisser, die in GEMMA leeg zijn en die de export met de definitie uit de wiki vult.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein.
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (herziening van het besluit van 2026-10-02: geen views).

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).
- **Eerste proefimport** op een kopie van het GEMMA-model: controleren dat gekoppelde elementen in hun GEMMA-map blijven, geen dubbele mappen ontstaan, `Object ID` blijft staan; de naam van de importoptie vastleggen in de skill `gemma-archimate-model-archimate-export`; het jArchi-script proberen met een tweede export.

## Algemeen onderwerp besluitvorming en heffingen

- **VNG Modelverordening lijkbezorgingsrechten** (ledenbrief 2011, met kostenonderbouwing) als bron en mogelijk beleidskader opnemen bij het algemene onderwerp voor Heffing en Heffingsverordening (besluit redacteur 2026-10-01). De link op de VNG-pagina `https://vng.nl/artikelen/modelverordeningen-wet-op-de-lijkbezorging` geeft een 404; zoek een openbare kopie.
