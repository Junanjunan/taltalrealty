from django_apps.books.common_models import *


class Apartment(HouseCommon):
    empty = models.BooleanField(default=False)


class Room(HouseCommon):
    empty = models.BooleanField(default=False)
    