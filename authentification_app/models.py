import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


def get_token():
    return str(uuid.uuid4())


class AllUsers (AbstractUser):
    note = models.CharField(max_length=300, blank=True)
    money = models.PositiveIntegerField(default=False)
    token = models.UUIDField(default=get_token, editable=False, unique=True)


class Basket (models.Model):
    user = models.OneToOneField(AllUsers, on_delete=models.CASCADE, related_name='userbasket',
                                to_field='id', primary_key=True)



