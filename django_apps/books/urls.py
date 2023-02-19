from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("insert-all", views.insert_all),
]