## Project info
This website is developed for the conference room and B&B rental organization Hof van Heulerbroek in Nieuw-Bergen.


# TODO 
Meerdere foto's op home pagina
adres, mail naam en link naar insta onderaan de pagina's
kleinere foto bij over ons
misschien overleggen met elke voor toepasselijke kleur tekst bij achtergrond en logo
Logo bovenaan de home pagina, indien mogelijk een transperant logo van Elke krijgen
Navbar items centreren
foto van parkeerplaats zettten bij route
B&B toevoegen aan navbar, pagina vullen met comming soon
reserveren toevoegen aan subnav
lettertype figcaption vergroten
reviews toevoegen aan subnav voor B&B en vergaderruimte
omgeving toevoegen aan navbar met meerdere foto's en beide videos
subnav voor omgeving: omgeving, route (x km)
B&B subnav activiteiten: padelbaan

# Developing details
`docker-compose up --build` for running website
`python3 manage.py makemigrations` for making migrations
`python3 manage.py migrate` for applying migrations
`python3 manage.py sqlmigrate <name> <migration_number>` for seeing sql migration code. Example: `python3 manage.py sqlmigrate blog 0001`
