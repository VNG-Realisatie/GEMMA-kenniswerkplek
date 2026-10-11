Gemeentelijk Vastgoed - Gemeentelijk Gegevensmodel (GGM)

Ga naar inhoud

# Gemeentelijk Vastgoed

Het vastgoed van de gemeente betreft kadastrale onroerende zaken. Dit objecttype is overgenomen uit de Kern:RSGB. Voor deze onroerende zaken is het objecttype ‘Object’ gedefinieerd. Deze objecten kunnen uit bouwdelen en bouwdeelelementen bestaan. Alle objecten en bijbehorende bouwdelen en bouwdeelelementen worden opgenomen in een MJOP (Meerjarig Onderhoudsplan). Koppeling in het gegevensmodel verloopt via de MJOP-Items. Bij het feitelijk uitvoeren van werkzaamheden wordt een ‘Werkbon’ aangemaakt die de wordt gebruikt als opdracht voor werkzaamheden door een ‘Leverancier’. Een ‘Leverancier’ kan een aanbesteding hebben gewonnen.
Huurcontracten en koopcontracten worden volgens Kern:RSGB gemodelleerd via het objecttype ‘Zakelijk Recht’. Hieraan is danwel een eigenaar danwel een huurder gekoppeld. Beiden zijn ‘RECHTSPERSOON’ uit de Kern: RSGB.
Het ‘Object’ is gekoppeld aan een ‘Kostenplaats’ uit het financiële model en de ‘Werkbon’ hoort bij een ‘Verplichting’ uit het financiële model. Zo is de koppeling met financiën verankerd.
Bovenstaande is weergegeven in onderstaande figuren.

De relatie met leveranciers is weergegeven in onderstaand figuur.

Het gemeentelijk vastgoed objecttype 'Vastgoedobject' is gekoppeld aan 'Kadastrale Onroerende Zaak'. Immers met het objecttype 'Vastgoedobject' wordt het bezit van een bepaald object weergegeven. Bezit van onroerende zaken is vastgelegd in de BRK, en beschikbaar via 'Kadastrale Onroerende Zaak'. Deze koppeling verloopt via een meer-op-meer-relatie, aangezien een bezit meerdere percelen kan beslaan, en er meerdere bezittingen op een perceel kunnen liggen (in het geval van appartementsrechten).
Aan een 'Kadastrale Onroerende Zaak' zijn 'Benoemde Objecten' gekoppeld, dit kunnen: 'Overig Gebouwd Object, Verblijfsobject', 'Standplaats', 'Ligplaats' of 'Overig Benoemd Terrein' zijn. Deze hebben op hun beurt een 'Nummeraanduiding', waarmee het adres kan worden bepaald.
De koppeling naar de eigenaar van een 'Kadastrale Onroerende Zaak' verloopt via het 'Zakelijk Recht' en de 'Tennaamstelling'. Er bestaan overigens ook andere soorten zakelijkrecht, zoals: recht van vruchtgebruik en recht van overpad.

De Kadastrale objecttypen zijn hier verder uitgewerkt, dus ik verwijs hier voor verdere informatie. Conform RSGB 3.0 ligt de 'Tennaamstelling' tussen 'Zakelijk Recht' en 'Rechtspersoon'. Ook is de relatie toegevoegd: 'Gesitueerd op' (varkensoortje) van 'Kadastrale Onroerende Zaak' met zichzelf. Dit om het gemakkelijk mogelijk te maken de bepalen op welk perceel een bepaald appartementsrecht ligt.
