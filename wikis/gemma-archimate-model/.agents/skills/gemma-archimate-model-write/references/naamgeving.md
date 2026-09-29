# Naamgeving

Elke elementnaam is op zichzelf ondubbelzinnig, ongeacht de grondslag.

## Gangbare term boven wetsterm

De bronvoorrang geldt voor welke begrippen er zijn en wat ze formeel betekenen, niet voor de naam.

- STANDAARD is de naam de term die beleids- en praktijkbronnen gebruiken. Toets: welke term gebruiken de beleids- en praktijkbronnen, en welke zou een medewerker aan de balie gebruiken?
- De wetsterm gaat naar `synoniemen` met context "wet"; de gangbare term eventueel ook met context "beleid" of "dagelijks gebruik" als er meer gangbare termen zijn.
- Vallen onder de gangbare en de wettelijke term niet precies dezelfde exemplaren, dan komt er een formele definitie met `## Definitie` (zie `definitie.md`).
- ALS er geen beleids- of praktijkbron is, of meer gangbare termen naast elkaar → voorleggen ([PR6]); niet terugvallen op de wetsterm zonder dat te melden.

Precedent: *Urn* (VNG-bron, praktijk), niet *Asbus* (Wet op de lijkbezorging); asbus is synoniem met context "wet".

## Naamconflict

- **Wiki-conflict**: de naam (of het id) wordt al door een ander element gebruikt. Geldt voor elke grondslag.
- **GGM-homoniem**: dezelfde GGM-entiteitnaam betekent in een ander beleidsdomein iets anders (`tools/ggm.py naamgenoten <naam>`). Alleen bij grondslag `ggm-entiteit`; meld ook terug als `homoniem`.

Bij een conflict: stel 2–3 namen voor en leg de keuze voor aan de redacteur:
- domeinprefix ("Onderwijsinschrijving"), samengesteld woord, of functionele naam ("Aanbestedingsinschrijving"). Geen haakjes in namen of bestandsnamen (niet "Inschrijving (Onderwijs)"). Leg de keuze vast in `## Naamkeuze` (overwogen namen met reden). Bij een GGM-homoniem blijft `ggm_entiteit` de GGM-naam; de GGM-naam mag als synoniem.

## Naam bij een bredere GGM-entiteit

Bij een match *sterk* of *partieel* op een bredere GGM-entiteit (generalisatie/specialisatie):
- STANDAARD blijft de naam het gemeentelijke, herkenbare begrip; NIET hernoemen naar de abstractere GGM-naam.
- De afwijking staat in `## GGM-bron` (bij de matchsterkte), NIET in `## Naamkeuze` (die is alleen voor naamconflicten).
- UITZONDERING (zeldzaam, per geval): hernoemen naar de GGM-naam ALLEEN als het begrip geen eigen identiteit heeft: de bronnen gebruiken de GGM-entiteit nergens anders voor, én het is geen zelfstandig gedragen begrip. Toets: zou een domeinexpert dit begrip ooit anders noemen of voor iets anders gebruiken? Ja → niet hernoemen.
- Bij hernoemen wordt de specifieke term een specialisatie: zonder pagina, of met pagina als die zelf een element is.
- NOOIT in bulk hernoemen op grond van één eerder akkoord ([EL9]); elk geval apart voorleggen.
- Na hernoemen: alle links naar het element bijwerken (relaties, begrippenlijsten, terugmeldingen).

Precedenten uit de vorige wiki: Woonboot → Vaartuig hernoemd (enige toepassing van de GGM-entiteit); Evenement, Woning en Rioolleiding niet (zelfstandige begrippen).

## Synoniemen

`synoniemen` in de frontmatter: andere namen voor hetzelfde begrip, elk met `context` ("GGM", "wet", "beleid", "dagelijks gebruik"). Een afwijkende GGM-naam of wetsterm hoort erin.
