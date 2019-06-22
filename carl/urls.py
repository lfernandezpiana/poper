# Son las vistas que tiene la aplicacion carl

from django.urls import path, include
from . import views
from django.views import generic
from django.views.generic import ListView
from carl.views import ComedianteList

urlpatterns = [
    path('', views.index, name='index'),
    path('template/integrantes/', views.ComedianteList.as_view(), name='comediante_list')
]
