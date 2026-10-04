# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herbeoordeling met de nieuwe werkwijze (2026-10-01)

De werkwijze is omgezet naar beoordelingen (oordeel van de AI) en gegenereerde pagina's; de elementpagina's van vóór de herziening staan in Git onder tag `voor-herbeoordeling`.

- **Lijkbezorging** opnieuw beoordelen met `gemma-archimate-model-update`, als proef van de nieuwe werkwijze. Graf, Grafrecht en Regeling krijgen hun besluit van 2026-09-30 uit `analyses/besluiten-redacteur.md`. Relaties volgens de criteria van 2026-10-01: actor via een rol, rol → object als verantwoordelijkheid of als handeling via een proces, functie bedient proces, toegang met een handeling, dienstrelaties via het realiserende proces. Nieuwe beleidskaders (bijv. Wet op de lijkbezorging) en ontbrekende processen (verlenen verlof tot begraving of crematie, vervallen verklaren grafrecht) komen mee als kandidaat.
- **Participatie** daarna, met de participatie-modelverordening als mogelijk beleidskader.
- **Kanalen** als één centrale set. Input uit lijkbezorging (geen element daar, besluit redacteur 2026-10-01): de elektronische weg (Wlb art. 7, Awb art. 2:13–2:15), het mededelingenbord en bordje bij het graf (Groningen art. 27, VNG-model art. 24), de beheerder als aanspreekpunt voor aanvragen (VNG-model toelichting 2), en digitaal aangifte doen met eHerkenning (RVO, burgerlijke stand).
- **GGM-terugmeldingen 1–9** bij de herbeoordeling koppelen aan de nieuwe beoordelingen; een melding die niet meer van toepassing is, voorleggen.
- **Links in de analyses** (`analyses/gegevensrollen.md`, `analyses/gemma-kennismodel.md`) naar de oude elementpagina's bijwerken zodra de elementen opnieuw bestaan.

## Indelingen (analyse 2026-10-04, `analyses/indelingen.md`)

- **Lijkbezorging opnieuw beoordelen met de criteria van 2026-10-04** (denkniveau hoog; nieuwe conversatie met een sterker model aanbevolen). Gedaan: de beslistabel, stap 7, controles en signalen, render (*Plaats in de indelingen*, `overzichten/<onderwerp>.md`) en export, en alle 139 beoordelingen hebben de nieuwe kenmerken met waarde `nee` ("nog niet beoordeeld"). Nu is het oordeel van de AI aan de beurt; de uitkomst staat in `analyses/indelingen.md` (*Inschatting voor lijkbezorging*), de besluiten in `analyses/besluiten-redacteur.md`. Werkwijze: skill `gemma-archimate-model-update`, stap 3 tot en met 8; start met `uv run python tools/afleiden.py` en lees de waarschuwingen.
  1. De taak *Verzorgen lijkbezorging*: de functie Lijkbezorging wordt een procescluster (`groepeert_processen`, `omvat_processen`); `bedient_gedrag` staat nu tijdelijk op ja. De partiële GEMMA-match met *Exploiteren van begraafplaatsen* vervalt.
  2. Per kernobject één bedrijfs- of ketenproces (`omvat_levensloop`, `kernobject`): *Bezorgen lijken* (ketenproces), *Beheren grafrechten*, *Beheren graven*; de huidige negen processen worden deelprocessen (`bijdrage_aan_groter_proces`, `eigen_besluit`, `eigen_normering` of `levert_aanbod`) met aggregaties vanaf de bedrijfsprocessen; *Verlenen verlof tot begraving of crematie* wordt een deelproces.
  3. Gebeurtenissen met triggering (*Overlijden*, *Verval van het grafrecht*, *Besmet lijk gemeld*).
  4. Objecten: `objectniveau` via `kernobject` en `deel_van_object`; Besluit, Beschikking, Vergunning, Heffing, Heffingsverordening en Regeling `generiek`; Verklaring van overlijden `invoer_van_een_ander`; specialisaties genoemd met `via`.
  5. Actoren: `soort_partij`; Gemeente wordt een actor met de rollen Houder van de begraafplaats, Houder van het crematorium, Houder van een plaats van bijzetting en Kostendrager; de officier van justitie wordt actor als ketenpartner. De zes actoren zijn nu geen element tot dit is beoordeeld.
  6. Indelingsvelden (`domein`, `doelgroep`, `regelgever`, `afnemer`): elk ontbrekend veld is een reden om voor te leggen. Waarden en GEMMA-functies met exacte match (*Exploiteren van begraafplaatsen*, *Burgerlijke stand diensten*) per geval aan de redacteur voorleggen (regel Navragen en regel Zwakke match voorleggen).
  7. Daarna AKKOORD, export en controle in Archi; `voortgang.md` voor en na vergelijken (nu 48 elementen, allemaal kandidaat behalve 3 gebeurtenissen op review).
- **UPL-lijsten als bron**: de externe en interne lijst van GEMMA Online (*Producten en diensten procesarchitectuur*) opnemen met `gemma-archimate-model-ingest`. Daarna de producten en diensten van lijkbezorging beoordelen (16 in de externe lijst). Via de grondslagkolommen bronnen zoeken voor de gaten: de model-APV (asverstrooiing) en het Besluit op de lijkbezorging (vervoersdocumenten).
- **Voorstellen aan het GEMMA-team**:
  - het beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7;
  - generieke gebeurtenissen (aanvraag ontvangen, besluit bekendgemaakt);
  - de afwijkingen van het kennismodel procesarchitectuur: een deelproces levert een dienst, een ketenproces bevat deelprocessen, structurele relaties tussen actoren;
  - het advies om referentiecomponenten te laten aggregeren door een hogere bedrijfsfunctie.
- **Applicatielaag** in de wiki opnemen, met de Applicatieservice-indeling naar domein.
- **Archi-views** per indeling en elementtype in de export, na de eerste proefimport (herziening van het besluit van 2026-10-02: geen views).

## Export naar Archi

- **Verzoek aan het GEMMA-team**: zet bij elke release naast `export/GEMMA release.xml` (AMEFF) ook `export/GEMMA release.archimate` in de GEMMA-Archi-repository (opslagformaat van Archi, met map-id's en profielen). Daarna `wiki.yaml` → `gemma.herkomst.pad` daarop zetten; na de overgang naar coArchi 2 op `model.archimate`. Tot dan neemt de redacteur een lokaal opgeslagen `.archimate` op (skill `gemma-archimate-model-gemma-release`).
- **Eerste proefimport** op een kopie van het GEMMA-model: controleren dat gekoppelde elementen in hun GEMMA-map blijven, geen dubbele mappen ontstaan, `Object ID` blijft staan; de naam van de importoptie vastleggen in de skill `gemma-archimate-model-archimate-export`; het jArchi-script proberen met een tweede export.
- **Zwakke en partiële matches** van vóór 2026-10-02 (Beheerder, Gemeente, Lijkbezorging) opnieuw voorleggen: de export overschrijft het GEMMA-element (regel Zwakke match voorleggen).

## Algemeen onderwerp besluitvorming en heffingen

- **VNG Modelverordening lijkbezorgingsrechten** (ledenbrief 2011, met kostenonderbouwing) als bron en mogelijk beleidskader opnemen bij het algemene onderwerp voor Heffing en Heffingsverordening (besluit redacteur 2026-10-01). De link op de VNG-pagina `https://vng.nl/artikelen/modelverordeningen-wet-op-de-lijkbezorging` geeft een 404; zoek een openbare kopie.
