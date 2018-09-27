
from django.db import models
from django.utils import timezone

# Create your models here.


class MountBikes(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    img_link = models.CharField(max_length=150)
    model_link = models.CharField(max_length=150)
    available = models.BooleanField(default=True)

    # description = models.ForeignKey('MountBikesDescription', related_name='bikes' , on_delete=models.CASCADE)

    XS = ('XS', 'Super small')
    S = ('S', 'Small')
    M = ('M', 'Medium')
    L = ('L', 'Large')
    XL = ('XL', 'Extra large')
    __all = dict([XS, S, M, L, XL])
    size = models.CharField(max_length=2, choices=__all.items())

    def to_dict(self):
        return {'id': self.pk,
                'name': self.name,
                'brand': self.brand,
                'price': self.price,
                'available': self.available,
                'img_link': self.img_link,
                'model_link': self.model_link,
                'size': self.size
        }


    def __str__(self):
        return str(self.name)

# class MountBikesDescription(models.Model):
#     description = models.CharField(max_length=3000)
#     frame = models.CharField(max_length=200)
#     fork = models.CharField(max_length=200)
#     crank = models.CharField(max_length=200)
#     wheels_size = models.SmallIntegerField()
#     wheels = models.CharField(max_length=200)
#     front_shifter = models.CharField(max_length=200)
#     rear_shifter = models.CharField(max_length=200)
#     front_brake = models.CharField(max_length=200)
#     rear_brake = models.CharField(max_length=200)
#     handlebar = models.CharField(max_length=200)
#     seat = models.CharField(max_length=200)
#     warranty = models.SmallIntegerField()
#

# class MountBikesDetail(models.Model):
#     model = models.ForeignKey('MountBikes', related_name='bikes')
#     brand = models.CharField(max_length=50)
#     year = models.IntegerField()
#     price = models.IntegerField()
#
#     UNISEX = ('U', 'Unisex')
#     FEMALE = ('F', 'Femail')
#     __all = dict([UNISEX, FEMALE])
#     sex = models.CharField(max_length=1, choices=__all.items())
#
#     MOUNTBIKE = ('MB', 'Mountain Bikes')
#     ROAD = ('Road', 'Road Bikes')
#     BMX = ('BMX', 'BMX Bikes')
#     CITY = ('City', 'City Bikes')
#     KIDS = ('Kids', 'Kids Bikes')
#     __all_2 = dict([MOUNTBIKE, ROAD, BMX, CITY, KIDS])
#     type = models.CharField(max_length=4, choices=__all_2.items())
#

#
#     date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return str(self.name)
