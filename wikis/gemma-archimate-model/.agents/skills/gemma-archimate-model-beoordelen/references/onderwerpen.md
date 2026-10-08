# Eén model over de onderwerpen heen

De uitwerking van de regels Eén element in het hele model, Thuishoren en Relaties tussen onderwerpen (`AGENTS.md`). De besluiten erachter staan in `besluiten/werkwijze.md`, thema 3.

## Eén element in het hele model

Eén betekenis is één element in het hele model, ook als meer onderwerpen het gebruiken; een gelijke naam met een andere betekenis is een homoniem (regel Match op betekenis). Zoek vóór je een begrip beoordeelt in alle beoordelingen, van alle onderwerpen, op naam en synoniemen. Bestaat het al, werk die beoordeling bij: voeg je onderwerp toe aan `onderwerpen` en zet wat alleen in jouw onderwerp geldt onder `per_onderwerp`. Hetzelfde begrip onder een andere naam krijgt `synoniem_van`, een gelijke naam met een andere betekenis staat onder `homoniemen`.

Controles: signaal: dezelfde naam of hetzelfde synoniem in twee beoordelingen zonder `synoniem_van` of `homoniemen`; dezelfde GEMMA- of GGM-match, exact of sterk, bij twee elementen.

## Thuishoren

Elk element heeft één thuisonderwerp, het eerste in `onderwerpen`: dat onderwerp beoordeelt het, ook het kenmerk *betekenis in onderwerp*; de andere onderwerpen gebruiken het met relaties en `per_onderwerp`. Een generiek element (kenmerk *generiek*) en een orgaan of de organisatie van de gemeente horen thuis in het onderwerp Algemeen. Anders beslist de inhoud: het thuisonderwerp is het onderwerp van de taak waarin het element ontstaat of verandert. Voor een bedrijfsobject is dat het onderwerp van het proces dat het maakt, voor een proces, dienst of product het onderwerp van zijn kernobject, voor een gebeurtenis het onderwerp van het object waarvan de toestand verandert, voor een rol of actor het onderwerp van het meeste gedrag dat hij uitvoert. Het aantal relaties is een aanwijzing, geen beslissing; dat een element eerder in een ander onderwerp is beoordeeld of goedgekeurd (de volgorde van inlezen) is geen argument. Volgt het thuisonderwerp eenduidig uit de inhoud, dan verplaatst de AI het zonder voorleggen en noemt het in de lijst ter bevestiging; alleen bij inhoudelijke twijfel voorleggen (besluit redacteur 2026-10-07). Hoort een begrip bij een onderwerp dat nog niet bestaat, dan is de uitkomst een verwijzing en beoordeelt dat onderwerp het later. Verplaatsen gaat per geval (regel Per geval) door de volgorde van `onderwerpen` te wijzigen; het object in Archi blijft, want de export gebruikt de onderwerpen niet. De omschrijving van een onderwerp noemt zijn kernobjecten en wat erbuiten valt, met het onderwerp waar dat thuishoort (besluit redacteur 2026-10-06).

Controles: signaal: kernobject met een ander thuisonderwerp; verwijzing naar een onderwerp dat nu bestaat; element met meer relaties naar één ander onderwerp dan naar het eigen, generieke elementen uitgezonderd.

## Relaties tussen onderwerpen

Een relatie tussen elementen van verschillende onderwerpen is een gewone relatie: leg haar vast waar de bronnen haar noemen, in de beoordeling van het bronelement (`tools/relaties.py voorstel` kijkt over alle onderwerpen). Een onderwerp verwijst zo naar de elementen van een ander onderwerp in plaats van ze te herhalen. Is het bronelement van een ander onderwerp en goedgekeurd, dan gaat het door de relatie opnieuw ter beoordeling. Elk element heeft minstens één relatie met een ander element; de samenhang per onderwerp staat in `voortgang.md`.

Controles: signaal: element zonder relatie.
