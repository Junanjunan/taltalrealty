from django.db import models
from django_apps.users.models import User


class BooksCommon(models.Model):
    address = models.CharField(max_length=100)
    addres_detail = models.CharField(max_length=30, null=True, blank=True)
    deal_type = models.CharField(max_length=20, choices=(('sell', 'sell'), ('lease', 'lease')))
    price = models.IntegerField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    month_fee = models.IntegerField(null=True, blank=True)
    management_fee = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('progress', 'progress'), ('finished', 'finished')))
    realtor = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100, null=True, blank=True)
    owner_phone = models.CharField(max_length=50, null=True, blank=True)
    on_lease = models.BooleanField(default=False)
    loanable = models.BooleanField(default=True)
    area_ex = models.FloatField(null=True, blank=True)
    area_su = models.FloatField(null=True, blank=True)
    area_land = models.FloatField(null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    elevator = models.BooleanField(default=False)
    updated = models.DateField(auto_now=True)
    description = models.TextField()

    class Meta:
        abstract = True


class HouseCommon(BooksCommon):
    """
    area_ex: exclusive area
    area_su: supply area (area_ex + public_area + ...)
    """
    room = models.IntegerField(null=True, blank=True)
    bath = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Apartment(HouseCommon):
    empty = models.BooleanField(default=False)

