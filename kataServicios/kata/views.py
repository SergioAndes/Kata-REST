from django.db import models
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

# Create your views here.
class Pregunta(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    perfilProfesional = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre