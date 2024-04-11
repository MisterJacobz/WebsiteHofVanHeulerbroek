## Project info
This website is developed for the conference room and B&B rental organization Hof van Heulerbroek in Nieuw-Bergen.


# TODO 
Meerdere foto's op home pagina
kleinere foto bij over ons
misschien overleggen met elke voor toepasselijke kleur tekst bij achtergrond en logo
foto van parkeerplaats zettten bij route
reserveren toevoegen aan subnav
lettertype figcaption vergroten
reviews toevoegen aan subnav voor B&B en vergaderruimte
omgeving toevoegen aan navbar met meerdere foto's en beide videos
subnav voor omgeving: omgeving, route (x km)
B&B subnav activiteiten: padelbaan

# Developing details
`docker compose up --build` for running website
`python3 manage.py makemigrations` for making migrations
`python3 manage.py migrate` for applying migrations
`python3 manage.py sqlmigrate <name> <migration_number>` for seeing sql migration code. Example: `python3 manage.py sqlmigrate blog 0001`


8-17:00 hele dag
8-12:00
13:00-17:00

tweede email veld

group size maximum 12 (als dit groter is dan moeten ze eigenlijk overleggen)
optie om de site engels, duits en nederlands te maken

nieuw ding in navigatie

nieuw ding in navigatie "Training" tussen vergaderruimte en B&B  (mogelijk links tussen die 2)

Totaalprijs in form verwerken (reservering is x euro voor huur + x voor arrangement) (zie https://www.deschuurvanloenen.nl/offerte-aanvraag.html voor voorbeeld)

kleuren combi:
- rusty rebel
- mud soldier
- #585c64 (kleur van logo)
