# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herziening van de regels

De redacteur wil de regels van deze wiki herzien omdat ze te strak zijn (besloten 2026-09-30).

- **Statusregel [EL18].** `voorgestelde_status` in `tools/bepaal_type.py` zet een governance-object en een data-object zonder GGM-match altijd op `kandidaat`; een besluit van de redacteur kan dat niet opheffen, en `promote apply` weigert het goedkeuren van een kandidaat. Zulke elementen kunnen dus nooit worden goedgekeurd. Voorstel: een frontmatter-veld `besluit_redacteur` (datum, door, besluit) waarmee de status `review` wordt als dit het enige bezwaar is; een conflict of "voorleggen" uit de beslistabel blijft kandidaat. [EL18] krijgt daarvoor een UITZONDERING, en `tools/check_elementen.py` meldt een `besluit_redacteur` zonder datum of naam.
- **Daarna opnieuw voorleggen:** Regeling (governance-object), Graf en Grafrecht (data-object zonder GGM-entiteit, terugmeldingen 3 en 4). De redacteur heeft opname akkoord bevonden (run 2026-09-30T1144-3c57); ze staan nog op `kandidaat`.

## Herziening van kenmerken en beslistabel

Analyse van de kenmerken per elementtype; besluiten van de redacteur van 2026-09-30. Nog door te voeren in `tools/bepaal_type.py` (KENMERKEN, REGELS, DREMPELS, NAREGELS), daarna skill `gemma-archimate-model-criteria` en `schemas/beoordeling.schema.json` opnieuw genereren, schema's voor de nieuwe paginatypen toevoegen en de tests bijwerken.

- **Drempel met kernrelatie.** Elk type krijgt één kernrelatie die ja moet zijn; van de overige drempelcriteria mag hoogstens één nee zijn. Kernrelaties: bedrijfsobject en contract *wordt bewerkt*; product *omvat aanbod*; dienst *gerealiseerd door*; proces en functie *toegewezen partij*; gebeurtenis *leidt tot gedrag*; actor, rol, samenwerkingsverband en kanaal *voert gedrag uit*. Reden: nu tellen dienst, gebeurtenis en actor twee criteria waarvan één nee mag, een proces zeven.
- **Nieuwe kenmerken.** *voert gedrag uit* (partij toegewezen aan aanwijsbaar gemeentelijk gedrag, of kanaal dat een aanwijsbare dienst ontsluit); *afnemer* (afnemer buiten de uitvoerder aanwijsbaar; drempel dienst en product); *gerealiseerd door* (proces of functie dat de dienst uitvoert); *leidt tot gedrag* (gebeurtenis start, onderbreekt of beëindigt aanwijsbaar gedrag); *omvat aanbod* (product bestaat uit aanwijsbare diensten of objecten met voorwaarden).
- **Vervallen kenmerken.** *relaties* (dubbeltelling met *wordt bewerkt* en *toegewezen partij*/*gebruikt objecten*; vervangen door de kernrelaties) en *meerdere vervullers* (onderscheidt niet; *los van verantwoordelijkheid* maakt het onderscheid actor/rol al).
- **Gewijzigde kenmerken.** *per keer doorlopen* zonder de deelvraag naar een resultaat (telt apart als *benoembaar resultaat*); *herhaald uitgevoerd* wordt *komt herhaald voor* en telt ook bij gebeurtenis; *toegewezen partij* en *benoembaar resultaat* tellen ook bij dienst.
- **Betekenis in onderwerp wordt poort.** Nee in stap 2: het begrip hoort bij een ander onderwerp, krijgt hier een verwijzing in de begrippenlijst en wordt in dat onderwerp beoordeeld.
- **Consistentieregels vóór de aard.** Conflict als gedragskenmerken ja zijn zonder *gedrag* (vervangt regel 15), als partijkenmerken ja zijn zonder partij, hoedanigheid of samenwerkingsverband, en als *afspraak* of *waarneembare vorm* ja is naast een aard. Nu wordt bijvoorbeeld een gedragsbegrip met *afspraak* ja stil een proces.
- **Nieuwe paginatypen.** Samenwerkingsverband (Business Collaboration): alleen een verband zonder eigen rechtspersoon; met eigen rechtspersoon blijft het actor (precedent GGD). Kanaal (Business Interface): één centrale set generieke kanalen; een onderwerp koppelt alleen een dienst aan een bestaand kanaal, een nieuw kanaal alleen na besluit van de redacteur.
- **Ongewijzigd.** Product blijft paginatype (met *omvat aanbod* en *afnemer*). Business Interaction blijft herkend en wordt voorgelegd; *gezamenlijk gedrag* blijft.
- **Vaste uitkomst zonder pagina.** *waarneembare vorm* (Representation): vermelden bij het genoemde object, niet meer voorleggen (volgt het besluit over Register van begraven lijken). *plaats* (Location): fysieke plaats, geen pagina; een gebiedsindeling blijft een bedrijfsobject.
- **Samenhangsignalen.** Een dienst waarvan het realiserende proces nog geen pagina heeft, en een gebeurtenis waarvan het gestarte gedrag nog geen pagina heeft: proces als kandidaat voorleggen.
- **Open:** worden de bestaande elementen na de wijziging opnieuw door de beslistabel gehaald, of alleen nieuwe begrippen? Vragen aan de redacteur vóór het doorvoeren.
