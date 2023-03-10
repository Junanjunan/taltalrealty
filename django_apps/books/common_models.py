from django.db import models
from django_apps.users.models import Realtor


class BooksCommon(models.Model):
    """
    area_ex: 전용면적
    area_su: 공급면적
    area_land: 토지면적(대지면적)
    """
    address = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=30, null=True, blank=True)
    deal_type = models.CharField(max_length=20, choices=(('sell', 'sell'), ('lease', 'lease')))
    price = models.IntegerField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    month_fee = models.FloatField(null=True, blank=True)
    management_fee = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('progress', 'progress'), ('finished', 'finished')), default='progress')
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100, null=True, blank=True)
    owner_phone = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank=True)
    on_lease = models.BooleanField(default=False)
    loanable = models.BooleanField(default=True)
    area_ex = models.FloatField(null=True, blank=True)
    area_su = models.FloatField(null=True, blank=True)
    area_land = models.FloatField(null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    total_floor = models.PositiveIntegerField(null=True, blank=True)
    elevator = models.BooleanField(default=False)
    parking = models.BooleanField(default=True)
    updated = models.DateField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.address

    class Meta:
        abstract = True


class HouseCommon(BooksCommon):
    room = models.IntegerField(null=True, blank=True)
    bath = models.IntegerField(null=True, blank=True)
    pet = models.BooleanField(default=False)

    class Meta:
        abstract = True


class NotBuildingCommon(models.Model):
    floor = models.PositiveIntegerField(null=True, blank=True)
    empty = models.BooleanField(default=False)
    tenant = models.CharField(max_length=100, null=True, blank=True)
    tenant_phone = models.DecimalField(max_digits=11, decimal_places=0,null=True, blank=True)
    
    class Meta:
        abstract = True