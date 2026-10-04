---
id: besluiten-redacteur
type: analyse
titel: Besluiten van de redacteur
bijgewerkt: '2026-10-04'
---

# Besluiten van de redacteur

Besluiten van de redacteur over afzonderlijke begrippen, verzameld bij de start van de herbeoordeling (2026-10-01) uit de elementpagina's, de begrippenlijsten en de commitberichten. De AI leest deze lijst bij het beoordelen en legt een besluit dat hier staat niet opnieuw voor. Een besluit dat niet meer past bij de criteria van 2026-10-01, legt de AI wel opnieuw voor, met de reden.

Besluiten over de werkwijze en de criteria staan bij de analyse waar ze bij horen: [Kenmerken per elementtype](kenmerken.md), [Beslistabel](beslistabel.md), [GEMMA-kennismodel](gemma-kennismodel.md), [Toegang tot een bedrijfsobject](gegevensrollen.md), [Synoniemen en homoniemen](synoniemen-en-homoniemen.md) en [Indelingen](indelingen.md).

## Per begrip

| Datum | Begrip | Onderwerp | Besluit |
|---|---|---|---|
| 2026-09-30 | GGD | lijkbezorging | Actor, ook al ontbreekt *betekenis in onderwerp* (alleen advies bij een besmet lijk): precedent GGD, mede-eigenaar en opdrachtgever via de gemeenschappelijke regeling. |
| 2026-09-30 | Gemeente | lijkbezorging | *Herzien op 2026-10-04.* Rol, geen actor. Gemeente is de hoedanigheid; de afzonderlijke gemeenten (Amsterdam, Utrecht) zijn de actoren, als rechtspersoon met een raad, een college en een burgemeester. |
| 2026-09-30 | College van B&W | lijkbezorging | Naam *College van B&W*, de gangbare naam; de wetsterm *burgemeester en wethouders* en Groningen *college* zijn synoniemen. |
| 2026-09-30 | Rechthebbende op het graf | lijkbezorging | Naam *Rechthebbende op het graf* (wet, art. 23, 28), niet *Rechthebbende* of *Rechthebbende grafrecht*, omdat GGM en GEMMA al een ander begrip *Rechthebbende* kennen (Archief). |
| 2026-09-30 | Urn | lijkbezorging | Naam *Urn* volgens het gangbare gebruik; *asbus* (wet, beheersverordening) is een synoniem. Een sierurn met meer asbussen is één urn. |
| 2026-09-30 | Besluit | lijkbezorging | Element als breder begrip boven Beschikking; generiek en domeinoverstijgend. |
| 2026-09-30 | Beschikking | lijkbezorging | Generiek en domeinoverstijgend, hoort niet bij één beleidsdomein. Geen van de twee GGM-GUID's is primair; de GUID van Generiek Jeugd en Wmo blijft de koppeling zolang het GGM geen domeinoverstijgende entiteit kent. |
| 2026-09-30 | Vergunning | lijkbezorging | Het gekozen niveau voor de vergunningen en verloven in de lijkbezorging (geen element per soort vergunning of verlof). |
| 2026-09-30 | Heffing | lijkbezorging | Het hoogste herkenbare niveau voor lijkbezorgingsrechten en retributie. |
| 2026-09-30 | Heffingsverordening | lijkbezorging | Het hoogste herkenbare niveau voor de verordening lijkbezorgingsrechten. |
| 2026-09-30 | Regeling | lijkbezorging | Element op het hoogste herkenbare niveau voor de beheersverordening begraafplaatsen; het generieke element is bevestigd. De gemeentelijke verordening is een specialisatie op grond van de Gemeentewet (art. 147). Opname akkoord (run 2026-09-30T1144-3c57). |
| 2026-09-30 | Begraafplaats, Crematorium, Plaats van bijzetting | lijkbezorging | Kenmerk *plaats* is nee: beoordeeld als gemeentelijke voorziening die wordt aangelegd, beheerd, in gebruik genomen en gesloten, niet als fysieke plaats. |
| 2026-09-30 | Graf | lijkbezorging | Opname akkoord als gegevensobject zonder GGM-entiteit (GGM-terugmelding 3). |
| 2026-09-30 | Grafrecht | lijkbezorging | Contract: kenmerk *afspraak* is ja, een tweezijdige afspraak tussen houder en rechthebbende met rechten en plichten, ook als de gemeente het als besluit op aanvraag verleent. Opname akkoord als gegevensobject zonder GGM-entiteit (GGM-terugmelding 4). |
| 2026-09-30 | Register van begraven lijken | lijkbezorging | Geen pagina: de vorm (representation) van de gegevens van graven, toegelicht bij Graf. |
| 2026-09-30 | Lijkbezorging (functie) | lijkbezorging | *Herzien op 2026-10-04.* Overkoepelende bedrijfsfunctie voor de gemeentelijke taken rond de lijkbezorging. |
| 2026-10-01 | Burgemeester, College van B&W, Gemeenteraad, Beslisser | lijkbezorging | De bestuursorganen hangen via de rol Beslisser (GEMMA, procesbouwstenen) aan gedrag; welk orgaan bij welk proces beslist, staat met het wetsartikel in de beschrijving van het proces. |
| 2026-10-01 | Model-beheersverordening begraafplaatsen | lijkbezorging | Opnemen als bron (openbare versie 2010, kopie Eerste Kamer); kandidaat-beleidskader. De Modelverordening lijkbezorgingsrechten volgt bij het algemene onderwerp heffingen. |
| 2026-09-30 | Uitdaagrecht | participatie | Geen eigen pagina: dezelfde procedure van verzoek, beoordeling, afspraken en evaluatie als overheidsparticipatie. |
| 2026-09-30 | Uniforme openbare voorbereidingsprocedure | participatie | Verhuist naar een algemeen onderwerp besluitvorming. |
| 2026-09-30 | Bestuursorgaan | participatie | Verhuist naar een algemeen onderwerp besluitvorming. |
| 2026-09-30 | Participatiebeleid | participatie | Variant van Beleidsnota; oppakken in een algemeen onderwerp. Tot dan vervallen de relaties van Gemeenteraad en Plan voor inwonersparticipatie naar het participatiebeleid. |
| 2026-10-02 | Export naar Archi | (alle) | Export in het opslagformaat van Archi (`.archimate`), niet AMEFF; GEMMA wordt native (`.archimate`) ingelezen. Een element met een GEMMA-match krijgt het GEMMA-id; naam en definitie uit de wiki overschrijven die van GEMMA, de oude gaan mee als eigenschap. Eigen eigenschappen en de eigen map heten `wiki-gemma-model`. Volledige sync via `wiki-gemma-model exportdatum` en een jArchi-script: alleen door de wiki gemaakte objecten worden verwijderd, bij een niet meer gekoppeld GEMMA-object alleen de wiki-eigenschappen. Alleen goedgekeurd; `--concept` alleen om te bekijken. Geen views. |
| 2026-10-02 | GEMMA-match | (alle) | Elke match met id wordt in de export een koppeling, ook `zwak` en `partieel`. Zo'n match wordt daarom alleen gemaakt met akkoord van de redacteur; matchen is de verantwoordelijkheid van wiki en redacteur, de export en Archi vertrouwen haar. |
| 2026-10-03 | Verklaring van geen bezwaar | lijkbezorging | Afgewezen: geen kernrelatie. De enige relatie stond bij het (toen) afgewezen proces Verlenen verlof tot begraving of crematie. De verklaring blijft genoemd in de beschrijving van Vergunning en Verklaring van overlijden. |
| 2026-10-04 | Gemeente | lijkbezorging | Actor als soort partij (elke gemeente), geen rol meer. Vervult Houder van de begraafplaats, Houder van het crematorium, Houder van een plaats van bijzetting en Kostendrager; omvat Gemeenteraad, College van B&W en Burgemeester. Herziet het besluit van 2026-09-30. Zie [Indelingen](indelingen.md). |
| 2026-10-04 | Verlenen verlof tot begraving of crematie | lijkbezorging | Deelproces van het ketenproces Bezorgen lijken; levert het UPL-product verlof tot begraven. Herziet het besluit van 2026-10-01 (geen eigen proces). Zie [Indelingen](indelingen.md). |
| 2026-10-04 | Verzorgen lijkbezorging (was: functie Lijkbezorging) | lijkbezorging | De functie wordt de taak *Verzorgen lijkbezorging*, een procescluster boven de processen per kernobject (Bezorgen lijken, Beheren grafrechten, Beheren graven). De partiële GEMMA-match met *Exploiteren van begraafplaatsen* vervalt; die GEMMA-functie wordt een eigen element dat de processen bedient. Herziet het besluit van 2026-09-30. Zie [Indelingen](indelingen.md). |
| 2026-10-04 | Beleidsdomein Begraafplaatsen en crematoria | lijkbezorging | Voorstel aan GEMMA en GGM: een beleidsdomein *Begraafplaatsen en crematoria* onder taakveld 7 (Iv3 7.5). De export maakt de groepering in de wiki-map voor de objecten, producten en beleidskaders van lijkbezorging. Gemeentebegrafenis blijft daarnaast in het GGM-beleidsdomein Gemeentebegrafenissen. |
| 2026-10-04 | Officier van justitie | lijkbezorging | Actor als ketenpartner in het ketenproces Bezorgen lijken (Wlb art. 10, 12), zonder eigen deelproces. Herziet de uitkomst buiten scope. Zie [Indelingen](indelingen.md). |

## Open punten uit eerdere besluiten

- Een algemeen onderwerp (besluitvorming) voor de generieke elementen Besluit, Beschikking, Vergunning, Heffing, Heffingsverordening en Regeling, en voor Uniforme openbare voorbereidingsprocedure, Bestuursorgaan en Beleidsnota.
- Zolang Bestuursorgaan geen element is, staat de toewijzing van inspraak aan het college en de gemeenteraad niet in het model.
