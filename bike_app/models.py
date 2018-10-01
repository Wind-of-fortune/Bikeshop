
from django.db import models
from django.utils import timezone

class Bikes(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    img_link = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=50)

    def to_dict(self):
        return {'id': self.pk,
                'name': self.name,
                'brand': self.brand,
                'price': self.price,
                'available': self.available,
                'img_link': self.img_link,
                'size': self.size
        }

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True


class MountBikes(Bikes):
    pass


class MountBikesDescription(models.Model):

    mountbikes = models.OneToOneField(MountBikes, on_delete=models.CASCADE, related_name='bikefirst',
                                to_field='name', primary_key=True)

    description = models.CharField(max_length=3000)
    sex = models.BooleanField(default=True)

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
                'sex': self.sex,
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
