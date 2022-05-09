from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/Home/
]
