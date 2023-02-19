from django_apps.books.common_models import *


class Apartment(HouseCommon, NotBuildingCommon):
    pass


class Room(HouseCommon, NotBuildingCommon):
    pass


class Officetel(HouseCommon, NotBuildingCommon):
    pass


class Shop(BooksCommon, NotBuildingCommon):
    premium = models.PositiveIntegerField(null=True, blank=True)


class Building(BooksCommon):
    under_floor = models.PositiveSmallIntegerField(null=True, blank=True)
    land_type = models.CharField(max_length=30, null=True, blank=True)
    area_building = models.FloatField(null=True, blank=True)
    area_total_floor_area = models.FloatField(null=True, blank=True)
    area_total_floor_area_for_ratio = models.FloatField(null=True, blank=True)
    building_coverage = models.FloatField(null=True, blank=True)
    floor_area_ratio = models.FloatField(null=True, blank=True)
    parking_number = models.PositiveIntegerField(null=True, blank=True)