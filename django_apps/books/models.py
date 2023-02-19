from django_apps.books.common_models import *


class Apartment(HouseCommon, NotBuildingCommon):
    pass


class Room(HouseCommon, NotBuildingCommon):
    pass


class Officetel(HouseCommon, NotBuildingCommon):
    pass


class Shop(BooksCommon, NotBuildingCommon):
    """
    premium: 권리금
    """
    premium = models.PositiveIntegerField(null=True, blank=True)


class Building(BooksCommon):
    """
    area_building: 건축면적
    area_total_floor_area: 연면적
    area_total_floor_area_for_ratio: 용적률용 연면적
    building_coverage: 건폐율
    floor_area_ratio: 용적률
    """
    under_floor = models.PositiveSmallIntegerField(null=True, blank=True)
    land_type = models.CharField(max_length=30, null=True, blank=True)
    area_building = models.FloatField(null=True, blank=True)
    area_total_floor_area = models.FloatField(null=True, blank=True)
    area_total_floor_area_for_ratio = models.FloatField(null=True, blank=True)
    building_coverage = models.FloatField(null=True, blank=True)
    floor_area_ratio = models.FloatField(null=True, blank=True)
    parking_number = models.PositiveIntegerField(null=True, blank=True)