from django.contrib import admin
from django.urls import include, path
from .views import createPath

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('createpath',createPath, name='createPath'),
]