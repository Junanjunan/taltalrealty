from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("insert-room", views.insert_room),
]