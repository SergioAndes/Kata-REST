from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Portafiolio, Persona
import json


# Create your views here.
@csrf_exempt
def index(request):
    portafolios = []
    return HttpResponse(serializers.serialize("json", portafolios))


@csrf_exempt
def portafolioLista(request):
    portafolios = Portafiolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolios))


@csrf_exempt
def crearUsuario(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        nombre = json_user['nombre']
        apellido = json_user['apellido']
        foto = json_user['foto']
        perfilProfesional = json_user['perfilProfesional']
        password = json_user['password']

        usuario = Persona.objects.create()
        usuario.nombre = nombre
        usuario.foto = foto
        usuario.perfilProfesional = perfilProfesional
        usuario.password = password
        usuario.save()

        return HttpResponse(serializers.serialize("json", usuario))


@csrf_exempt
def getPortafoliosPersona(self, nombre):
    portafolios = Portafiolio.objects.all()
    user = Persona.objects.get(nombre=nombre)
    portafolios = Portafiolio.objects.filter(persona=user.id)
    return HttpResponse(serializers.serialize("json", portafolios))