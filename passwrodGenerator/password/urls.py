
from django.contrib import admin
from django.urls import path, include
from .views import about, home, password
urlpatterns = [
    path('', home, name='home'),
    path('password/', password, name='password'),
    path('about/', about, name='about'),
]
