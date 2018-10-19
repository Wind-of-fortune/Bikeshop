
from django.db import models


class MountBikes(models.Model): # FOR MOUNTBIKES, ROADBIKES
    name = models.CharField(max_length=200, unique=True)
    brand = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    fake_price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveIntegerField(default=fake_price)
    img_link = models.CharField(max_length=300)

    mount_bike = ('mountbike', 'горные велосипеды')
    road_bike = ('roadbike', 'шоссейные велосипеды')
    bmx = ('bmx', 'BMX')
    city_bike = ('city_bike', 'городские велосипеды')
    child_bike = ('child_bike', 'детские велосипеды')
    wheels = ('wheels', 'колеса')
    frame = ('frame', 'рамы')
    shifter = ('shifter', 'переключатели')
    brake = ('brake', 'тормоза')
    shirts = ('shirts', 'футболки')
    shorts = ('shorts','шорты')
    gloves = ('gloves','перчатки')
    glases = ('glases', 'очки')
    tool = ('tool', 'инструменты')
    pump = ('pump', 'насосы')
    backpack = ('backpack', 'рюкзаки')
    lamp = ('lamp', 'фонари')
    fruit = ('fruit', 'фрукты')
    water = ('water', 'вода')
    nutrition = ('nutrition', 'питание')
    __all = dict([mount_bike, road_bike, bmx, city_bike, child_bike, wheels, frame, shifter, brake, shirts, shorts,
                  gloves, glases, tool, pump, backpack, lamp, fruit, water, nutrition
                  ])
    bike_type = models.CharField(max_length=40, choices=__all.items())

    available_XS = models.PositiveSmallIntegerField(default=0)
    available_S = models.PositiveSmallIntegerField(default=0)
    available_M = models.PositiveSmallIntegerField(default=0)
    available_L = models.PositiveSmallIntegerField(default=0)
    available_XL = models.PositiveSmallIntegerField(default=0)

    available_no_size = models.PositiveSmallIntegerField(default=0) # for items that doesn't have size

    available_gramms = models.PositiveSmallIntegerField(default=0)

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
                'available_no_size': self.available_no_size,
                'available_gramms': self.available_gramms,
                }

    def __str__(self):
        return str(self.name)

class MountBikesDescription(models.Model): # FOR MOUNTBIKES, ROADBIKES
    mountbikes = models.OneToOneField(MountBikes, on_delete=models.CASCADE, related_name='bikefirst',
                                      to_field='name', primary_key=True)

    description = models.CharField(max_length=5000)

    frame = models.CharField(max_length=800)
    fork = models.CharField(max_length=800)
    ammort = models.CharField(max_length=800) # new
    crank = models.CharField(max_length=800)
    pedal = models.CharField(max_length=800)#new
    front_shifter = models.CharField(max_length=800)
    rear_shifter = models.CharField(max_length=800)
    lever = models.CharField(max_length=800) #new
    cassete = models.CharField(max_length=800)  # new
    chain = models.CharField(max_length=800)  # new
    rims = models.CharField(max_length=800) # new
    tyres = models.CharField(max_length=800)  # new
    front_hub = models.CharField(max_length=800)  # new
    rear_hub = models.CharField(max_length=800)  # new
    front_brake = models.CharField(max_length=800)
    rear_brake = models.CharField(max_length=800)
    handlebar = models.CharField(max_length=800)
    stem = models.CharField(max_length=800)# new
    grips = models.CharField(max_length=800)# new
    headset = models.CharField(max_length=800)  # new
    saddle = models.CharField(max_length=800)
    seatpost = models.CharField(max_length=800)  # new
    warranty = models.PositiveSmallIntegerField(default=5)
    unisex = models.BooleanField(default=True)

    def __str__(self):
        return str(self.mountbikes.name)







