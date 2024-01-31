from django.contrib import admin
from .models import ConferenceRoom, Reservation, MenuItems

admin.site.register(ConferenceRoom)
admin.site.register(Reservation)
admin.site.register(MenuItems)
