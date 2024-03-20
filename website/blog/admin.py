from django.contrib import admin
from .models import ConferenceRoom, ConferenceRoomReservation, MenuItems

admin.site.register(ConferenceRoom)
admin.site.register(ConferenceRoomReservation)
admin.site.register(MenuItems)
