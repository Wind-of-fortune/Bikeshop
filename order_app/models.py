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
    mark = models.CharField(max_length=100, default='')


class Order(models.Model):
    username = models.CharField(max_length=100)
    order_item_name = models.CharField(max_length=1000)
    order_item_size = models.CharField(max_length=200)
    items_price = models.CharField(max_length=1000)
    sum_price = models.BigIntegerField()

    ship_country = models.CharField(max_length=100, default='Russia')
    ship_city = models.CharField(max_length=100, default='Irkutsk')
    ship_street = models.CharField(max_length=100)
    ship_house = models.CharField(max_length=100)
    ship_postalcode = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=30)

    date_created = models.DateTimeField(default=timezone.now)
    date_delivered = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    is_accept = models.BooleanField(default=False)

    add_information = models.CharField(max_length=1000, blank=True)
