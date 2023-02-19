import os
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


def insert_room(request):
    project_path = '/home/taltal/git/taltalrealty'
    data_path = f'{project_path}/django_apps/books/data'
    filename = 'room.xlsx'
    file = os.path.join(data_path, filename)
    df_room = pd.read_excel(file)
    dict_room = dict(df_room)
    print(dict_room.get('roomm'))
    return JsonResponse({"response":"success"})