# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herziening van de regels

De redacteur wil de regels van deze wiki herzien omdat ze te strak zijn (besloten 2026-09-30).

- **Statusregel [EL18].** `voorgestelde_status` in `tools/bepaal_type.py` zet een governance-object en een data-object zonder GGM-match altijd op `kandidaat`; een besluit van de redacteur kan dat niet opheffen, en `promote apply` weigert het goedkeuren van een kandidaat. Zulke elementen kunnen dus nooit worden goedgekeurd. Voorstel: een frontmatter-veld `besluit_redacteur` (datum, door, besluit) waarmee de status `review` wordt als dit het enige bezwaar is; een conflict of "voorleggen" uit de beslistabel blijft kandidaat. [EL18] krijgt daarvoor een UITZONDERING, en `tools/check_elementen.py` meldt een `besluit_redacteur` zonder datum of naam.
- **Daarna opnieuw voorleggen:** Regeling (governance-object), Graf en Grafrecht (data-object zonder GGM-entiteit, terugmeldingen 3 en 4). De redacteur heeft opname akkoord bevonden (run 2026-09-30T1144-3c57); ze staan nog op `kandidaat`.

## Herbeoordeling na de herziening van 2026-10-01

De criteria van 2026-10-01 zijn doorgevoerd in de beslistabel, de relatietool, de controle, de schema's, de paginatypen (dienst, gebeurtenis, bedrijfssamenwerking, kanaal, beleidskader) en de skills; de documentatie staat in `analyses/beslistabel.md`. De bestaande elementen voldoen nog aan de criteria van 2026-09-30; de controle meldt dat als waarschuwing.

- **Herbeoordeling per onderwerp.** Een run per onderwerp (lijkbezorging, participatie) die voor elk element de kenmerken opnieuw beantwoordt volgens de criteria van 2026-10-01, en de relaties omzet: actor via een rol (24 relaties), rol → object als verantwoordelijkheid of als handeling via een proces (21), functie bedient proces (8), toegang met een handeling (22), de dienstrelaties via het realiserende proces, `## Homoniemen` als tabel (Regeling, Rechthebbende op het graf), afwijkende GGM- en GEMMA-namen als synoniem. Elke wijziging van type, relatie of status apart voorleggen [EL9]; alleen een aangevuld kenmerk laat de status ongemoeid. Nieuwe beleidskaders (bijv. Wet op de lijkbezorging, participatie-modelverordening) en ontbrekende processen (verlenen verlof tot begraving of crematie, vervallen verklaren grafrecht) komen in dezelfde run als kandidaat.
- **Overgang opruimen.** Als alle elementen zijn herbeoordeeld: `SLEUTELS_2026_09_30` en `kenmerkwaarden_2026_09_30` uit `tools/bepaal_type.py`, `TOEGANG_OUD` en `toegestaan(oud=True)` uit `tools/relaties.py`, en de herbeoordelingswaarschuwingen uit `tools/check_elementen.py` verwijderen.
