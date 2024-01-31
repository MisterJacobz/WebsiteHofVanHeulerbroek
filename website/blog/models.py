from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ConferenceRoom(models.Model):
    name = models.CharField(max_length=100)
    daypart_1_price = models.DecimalField(max_digits=6, decimal_places=2, default=350)
    daypart_2_price = models.DecimalField(max_digits=6, decimal_places=2, default=500)
    lunch_price_per_person = models.DecimalField(max_digits=5, decimal_places=2, default=25)
    lunch_items = models.CharField(max_length=1000)

class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    creation_datetime = models.DateTimeField(default=timezone.now)
    reservation_datetime_start = models.DateTimeField(default=timezone.now)
    reservation_datetime_finish = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # account = models.ForeignKey(User, on_delete=models.CASCADE)

