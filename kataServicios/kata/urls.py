from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
  path('kata/portafolio', views.index, name="portafiolio"),
  path('kata/portafolioLista', views.portafolioLista, name="portafolioLista"),
  path('kata/crearUsuario', views.crearUsuario, name="crearUsuario")


]