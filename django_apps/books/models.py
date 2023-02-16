from django_apps.books.common_models import *


class Apartment(HouseCommon):
    floor = models.PositiveIntegerField(null=True, blank=True)
    empty = models.BooleanField(default=False)


class Room(HouseCommon):
    floor = models.PositiveIntegerField(null=True, blank=True)
    empty = models.BooleanField(default=False)
    