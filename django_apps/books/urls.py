from django.urls import path
from . import insert_views, views

app_name = "books"

urlpatterns = [
    path("<str:model_name>", views.book_list),
    path("insert-all", insert_views.insert_all),
]