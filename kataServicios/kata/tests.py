import requests
from django.test import TestCase, Client
from .models import Portafiolio, Persona, Imagen
import json


# Create your tests here.

class KataTestCase(TestCase):

    def test_servicio_list_status(self):
        url = '/kata/portafolio'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_elementos_especificos(self):
        persona = Persona.objects.create(nombre='hola', apellido='apellido', usuario='user', foto='foto',
                                         perfilProfesional='test', password='noPass')
        portafolios = Portafiolio.objects.create(nombrePortafolio='porta', esPublico=True, persona=persona)
        response = self.client.get('/kata/portafolioLista')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)

    def test_elementosPersona(self):
        persona = Persona.objects.create(nombre='hola', apellido='apellido', usuario='user', foto='foto',
                                         perfilProfesional='test', password='noPass')
        portafolios = Portafiolio.objects.create(nombrePortafolio='porta', esPublico=True, persona=persona)
        imagen = Imagen.objects.create(titulo='porta', enlace='True', descripcion='persona', esPublica=True,
                                       portafolio=portafolios, tipoDeArchivo='test')
        response = self.client.get('/kata/elemntosPersona')
        current_data = json.loads(response.content)
        self.assertEqual(current_data, imagen)
