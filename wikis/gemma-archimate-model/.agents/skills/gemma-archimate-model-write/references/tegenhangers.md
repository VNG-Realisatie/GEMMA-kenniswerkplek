# Tegenhanger

Een actor of rol waarvan de exemplaren ook als ding worden behandeld (kenmerken *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*) krijgt daarnaast een bedrijfsobjectpagina: de beslistabel noemt dan een tegenhanger. Bij gedrag (proces, functie) nooit: het resultaat is dan een apart begrip (bijv. het object "Aanvraag" naast het proces "Aanvraag behandelen").

- Twee pagina's, elk met een eigen definitie vanuit het eigen perspectief: wie handelt (actor/rol) tegenover het ding waarmee gewerkt wordt (bedrijfsobject).
- Beide pagina's hebben een sectie `## Tegenhanger` met een link naar de andere en één zin over de verhouding. `tools/check_elementen.py` controleert dat de verwijzing wederzijds is.
- Beide mogen dezelfde `ggm_guid` dragen.
- De bedrijfsobjectpagina neemt de kenmerken van het begrip over; de check accepteert haar als tegenhanger.
