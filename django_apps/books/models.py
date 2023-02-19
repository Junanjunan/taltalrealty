from django_apps.books.common_models import *


class Apartment(HouseCommon):
    floor = models.PositiveIntegerField(null=True, blank=True)
    empty = models.BooleanField(default=False)
    tenant = models.CharField(max_length=100, null=True, blank=True)
    tenant_phone = models.CharField(max_length=50, null=True, blank=True)


class Room(HouseCommon):
    floor = models.PositiveIntegerField(null=True, blank=True)
    empty = models.BooleanField(default=False)
    tenant = models.CharField(max_length=100, null=True, blank=True)
    tenant_phone = models.CharField(max_length=50, null=True, blank=True)