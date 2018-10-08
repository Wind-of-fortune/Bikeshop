
from django.db import models
from django.utils import timezone


class MountBikes(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    fake_price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveIntegerField(default=fake_price)
    img_link = models.CharField(max_length=150)

    mount_bike = ('mountain_bike', 'mountain_bike')
    road_bike = ('road_bike', 'road_bike')
    city_bike = ('city_bike', 'city_bike')
    bmx_bike = ('BMX_bike', 'BMX_bike')
    child_bike = ('child_bike', 'child_bike')
    __all = dict([mount_bike, road_bike, city_bike, bmx_bike, child_bike])
    bike_type = models.CharField(max_length=20, choices=__all.items())

    available_XS = models.PositiveSmallIntegerField(default=0)
    available_S = models.PositiveSmallIntegerField(default=0)
    available_M = models.PositiveSmallIntegerField(default=0)
    available_L = models.PositiveSmallIntegerField(default=0)
    available_XL = models.PositiveSmallIntegerField(default=0)


    def to_dict(self):
        return {'id': self.pk,
                'name': self.name,
                'brand': self.brand,
                'price': self.price,
                'discount': self.discount,
                'img_link': self.img_link,
                'bike_type': self.bike_type,
                'available_XS': self.available_XS,
                'available_S': self.available_S,
                'available_M': self.available_M,
                'available_L': self.available_L,
                'available_XL': self.available_XL,
        }

    def __str__(self):
        return str(self.name)


class MountBikesDescription(models.Model):

    mountbikes = models.OneToOneField(MountBikes, on_delete=models.CASCADE, related_name='bikefirst',
                                to_field='name', primary_key=True)

    description = models.CharField(max_length=3000)
    unisex = models.BooleanField(default=True)

    frame = models.CharField(max_length=200)
    fork = models.CharField(max_length=200)
    crank = models.CharField(max_length=200)
    wheels = models.CharField(max_length=200)
    front_shifter = models.CharField(max_length=200)
    rear_shifter = models.CharField(max_length=200)
    front_brake = models.CharField(max_length=200)
    rear_brake = models.CharField(max_length=200)
    handlebar = models.CharField(max_length=200)
    seat = models.CharField(max_length=200)
    warranty = models.PositiveSmallIntegerField(default=5)

    def to_dict(self):
        return {'description': self.description,
                'sex': self.unisex,
                'frame': self.frame,
                'fork': self.fork,
                'crank': self.crank,
                'wheels': self.wheels,
                'front_shifter': self.front_shifter,
                'rear_shifter': self.rear_shifter,
                'front_brake': self.front_brake,
                'rear_brake': self.rear_brake,
                'handlebar': self.handlebar,
                'warranty': self.warranty,
        }


    def __str__(self):
        return str(self.mountbikes.name)
