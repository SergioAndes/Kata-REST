from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Portafiolio, Persona
import json


# Create your views here.
def index(request):
    portafolios = []
    return HttpResponse(serializers.serialize("json", portafolios))

def portafolioLista(request):
    portafolios = Portafiolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolios))