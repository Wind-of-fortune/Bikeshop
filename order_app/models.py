from django.db import models
from bike_app.models import MountBikes
from authentification_app.models import AllUsers
from django.utils import timezone

class Basket (models.Model):
    #user = models.ForeignKey(AllUsers, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    item_name = models.CharField(max_length=100)
    item_code = models.PositiveIntegerField(null=True)
    item_size = models.CharField(max_length=2)
    item_price = models.PositiveIntegerField()

    date_created = models.DateTimeField(default=timezone.now)
    add_information = models.CharField(max_length=1000, blank=True)

    ship_country = models.CharField(max_length=100, default='Russia')
    ship_city = models.CharField(max_length=100, default='Irkutsk')
    ship_street = models.CharField(max_length=100, blank=True)
    ship_house = models.CharField(max_length=100, blank=True)
    ship_postalcode = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=30, default='', blank=True)

