from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login),
    
    path('login/github', views.github_login),
    path('login/github/callback', views.github_callback),
    
]