import os
import django

# Set the environment variable to point to your Django project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Configure Django settings
django.setup()

from blog.models import ConferenceRoom, MenuItems, MenuItemsExtraInfo

def initialize_data():
    ConferenceRoom.objects.create(
        name="Vergaderruimte",
        daypart_1_price=350.00,
        daypart_2_price=500,
        lunch_price_per_person=25.00,
        lunch_items="Broodje met beleg"
    )

    MenuItems.objects.create(name="Cola", price=2.50)
    MenuItems.objects.create(name="Sinas", price=2.50)
    MenuItems.objects.create(name="Sprite", price=2.50)
    MenuItems.objects.create(name="Chips", price=3.50)
    MenuItems.objects.create(name="Nachos met gesmolten kaas en quacamole", price=4.95)
    MenuItems.objects.create(name="Smoothie", price=5.95)
    MenuItems.objects.create(name="Appeltaart", price=4.95)
    MenuItems.objects.create(name="Cake", price=3.50)
    MenuItems.objects.create(name="Verse fruitsalade met fruit uit het seizoen", price=4.95)
    MenuItems.objects.create(name="Uitgebreide borrelplank¹", price=12.50)
    MenuItemsExtraInfo.objects.create(reference="¹", info="Een rijk gevulde plank met oa verschillende soorten worst, ham, kazen, noten, rauwkost, diverse soorten dips, flatbread")
    MenuItems.objects.create(name="Borrelplank 'nog even bijpraten'²", price=7.75)
    MenuItemsExtraInfo.objects.create(reference="²", info="Deze borrelplank bevat groente chips, nootjes, kaaskrokantjes en olijven")

if __name__ == "__main__":
    initialize_data()