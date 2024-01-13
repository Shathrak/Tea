from django.contrib import admin
from django.urls import path, include
from Cadd import urls, views

urlpatterns = [
    path('index/', views.index, name="index" ),
]