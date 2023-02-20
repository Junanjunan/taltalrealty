import os
import datetime
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import *
from django_apps.users.models import Realtor


def insert_all(request):
    project_path = '/home/taltal/git/taltalrealty'
    data_path = f'{project_path}/django_apps/books/data'
    filename = 'book_office.xlsx'
    file = os.path.join(data_path, filename)
    df_building = pd.read_excel(file, sheet_name='매매(건물)')
    df_apartment_sell = pd.read_excel(file, sheet_name='매매(아파트)')
    df_apartment_lease = pd.read_excel(file, sheet_name='임대(아파트)')
    df_villa_sell = pd.read_excel(file, sheet_name='매매(빌라)')
    df_villa_lease = pd.read_excel(file, sheet_name='임대(주택)')
    df_officetel_sell = pd.read_excel(file, sheet_name='매매(오피스텔)')
    df_officetel_lease = pd.read_excel(file, sheet_name='임대(오피스텔)')
    df_shop_sell = pd.read_excel(file, sheet_name='매매(상가)')
    df_shop_lease = pd.read_excel(file, sheet_name='임대(상가)')
    me = Realtor.objects.get(id=1)

    for index, row in df_building.iterrows():
        address = row.get('address')
        updated = row.get('updated') if isinstance(row.get('updated'), datetime.date) else None
        deal_type = 'sell'
        price = row.get('price') if type(row.get('price')) == int else 0
        deposit = row.get('deposit') if type(row.get('deposit')) == int else 0
        month_fee = row.get('month_fee') if type(row.get('month_fee')) == int  else 0
        management_fee = row.get('management_fee') if type(row.get('management_fee')) == int  else 0
        birth = row.get('birth') if isinstance(row.get('birth'), datetime.date)  else None
        total_floor = row.get('total_floor') if type(row.get('total_floor')) == int else 0
        under_floor = row.get('under_floor') if type(row.get('under_floor')) == int else 0
        land_type = row.get('land_type') if row.get('land_type') else ''
        area_land = row.get('area_m2') if type(row.get('area_m2')) == float else 0
        area_building = row.get('building_area_m2') if type(row.get('building_area_m2')) == float else 0
        area_total_floor = row.get('total_floor_area_m2') if type(row.get('total_floor_area_m2')) == float else 0
        area_total_floor_for_ratio = row.get('total_floor_area_m2_for_ratio') if type(row.get('total_floor_area_m2_for_ratio')) == float else 0
        building_coverage = row.get('building_coverage') if type(row.get('building_coverage')) == float else 0
        floor_area_ratio = row.get('floor_area_ratio') if type(row.get('floor_area_ratio')) == float else 0
        parking_number = row.get('parking_number') if type(row.get('parking_number')) == int else 0
        elevator = row.get('elevator') if row.get('elevator') == bool else False
        loanable = row.get('loan') if row.get('loan') == bool else True
        status = 'progress' if row.get('not_finished') == True else 'finished'
        realtor = me
        owner = row.get('owner_phone')
        description = row.get('description')

        Building.objects.create(
            address = address,
            updated = updated,
            deal_type = deal_type,
            price = price,
            deposit = deposit,
            month_fee = month_fee,
            management_fee = management_fee,
            birth = birth,
            total_floor = total_floor,
            under_floor = under_floor,
            land_type = land_type,
            area_land = area_land,
            area_building = area_building,
            area_total_floor = area_total_floor,
            area_total_floor_for_ratio = area_total_floor_for_ratio,
            building_coverage = building_coverage,
            floor_area_ratio = floor_area_ratio,
            parking_number = parking_number,
            elevator = elevator,
            loanable = loanable,
            status = status,
            realtor = realtor,
            owner = owner,
            description = description,
        )

    for index, row in df_villa_sell.iterrows():
        address = row.get('address')
        updated = row.get('updated') if isinstance(row.get('updated'), datetime.date) else None
        deal_type = 'sell'
        price = row.get('price') if type(row.get('price')) == int else 0
        deposit = row.get('deposit') if type(row.get('deposit')) == int else 0
        month_fee = row.get('month_fee') if type(row.get('month_fee')) == int  else 0
        management_fee = row.get('management_fee') if type(row.get('management_fee')) == int  else 0
        status = 'progress' if row.get('not_finished') == True else 'finished'
        realtor = me
        owner = row.get('owner_phone')
        area_ex = row.get('area_m2') if row.get('area_m2') else 0
        area_land = row.get('land_m2') if row.get('land_m2') else 0
        on_lease = True if deposit > 0 or month_fee > 0 else False
        birth = row.get('birth') if isinstance(row.get('birth'), datetime.date)  else None
        total_floor = row.get('total_floor') if type(row.get('total_floor')) == int else 0
        parking = row.get('parking') if row.get('parking_number') else True
        elevator = row.get('elevator') if row.get('elevator') == bool else False
        loanable = row.get('loan') if row.get('loan') == bool else True
        empty = row.get('empty') if row.get('empty') == bool else False
        description = row.get('description')

        Room.objects.create(
            address = address,
            updated = updated,
            deal_type = deal_type,
            price = price,
            deposit = deposit,
            month_fee = month_fee,
            management_fee = management_fee,
            status = status,
            realtor = realtor,
            owner = owner,
            area_ex = area_ex,
            area_land = area_land,
            on_lease = on_lease,
            birth = birth,
            total_floor = total_floor,
            parking = parking,
            elevator = elevator,
            loanable = loanable,
            empty = empty,
            description = description,
        )

    for index, row in df_villa_lease.iterrows():
        address = row.get('address')
        updated = row.get('updated') if isinstance(row.get('updated'), datetime.date) else None
        deal_type = 'lease'
        price = row.get('price') if type(row.get('price')) == int else 0
        deposit = row.get('deposit') if type(row.get('deposit')) == int else 0
        month_fee = row.get('month_fee') if type(row.get('month_fee')) == int  else 0
        management_fee = row.get('management_fee') if type(row.get('management_fee')) == int  else 0
        status = 'progress' if row.get('not_finished') == True else 'finished'
        realtor = me
        owner = row.get('owner_phone')
        area_ex = row.get('area_m2') if row.get('area_m2') else 0
        area_land = row.get('land_m2') if row.get('land_m2') else 0
        on_lease = True if deposit > 0 or month_fee > 0 else False
        birth = row.get('birth') if isinstance(row.get('birth'), datetime.date)  else None
        total_floor = row.get('total_floor') if type(row.get('total_floor')) == int else 0
        parking = row.get('parking') if row.get('parking_number') else True
        elevator = row.get('elevator') if row.get('elevator') == bool else False
        loanable = row.get('loan') if row.get('loan') == bool else True
        empty = row.get('empty') if row.get('empty') == bool else False
        description = row.get('description')

        Room.objects.create(
            address = address,
            updated = updated,
            deal_type = deal_type,
            price = price,
            deposit = deposit,
            month_fee = month_fee,
            management_fee = management_fee,
            status = status,
            realtor = realtor,
            owner = owner,
            area_ex = area_ex,
            area_land = area_land,
            on_lease = on_lease,
            birth = birth,
            total_floor = total_floor,
            parking = parking,
            elevator = elevator,
            loanable = loanable,
            empty = empty,
            description = description,
        )
        
    for index, row in df_shop_lease.iterrows():
        address = row.get('address')
        updated = row.get('updated') if isinstance(row.get('updated'), datetime.date) else None
        deal_type = 'lease'
        premium = row.get('right_deposit') if type(row.get('right_deposit')) == int else 0
        deposit = row.get('deposit') if type(row.get('deposit')) == int else 0
        month_fee = row.get('month_fee') if type(row.get('month_fee')) == int  else 0
        management_fee = row.get('management_fee') if type(row.get('management_fee')) == int  else 0
        status = 'progress' if row.get('not_finished') == True else 'finished'
        realtor = me
        owner = row.get('owner_phone')
        area_ex = row.get('area_m2') if type(row.get('area_m2')) == int else 0
        on_lease = True
        birth = row.get('birth') if isinstance(row.get('birth'), datetime.date)  else None
        parking = row.get('parking') if row.get('parking_number') else True
        elevator = row.get('elevator') if row.get('elevator') == bool else False
        empty = row.get('empty') if row.get('empty') == bool else False
        description = row.get('description')

        Shop.objects.create(
            address = address,
            updated = updated,
            deal_type = deal_type,
            premium = premium,
            deposit = deposit,
            month_fee = month_fee,
            management_fee = management_fee,
            status = status,
            realtor = realtor,
            owner = owner,
            area_ex = area_ex,
            on_lease = on_lease,
            birth = birth,
            parking = parking,
            elevator = elevator,
            empty = empty,
            description = description,
        )
    return JsonResponse({"response":"success"})