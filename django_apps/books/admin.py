from django.contrib import admin
from django.apps import apps


model_list = apps.get_app_config('books').get_models()
for model in model_list:
    admin.site.register(model)