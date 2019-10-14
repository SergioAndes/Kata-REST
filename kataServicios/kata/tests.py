import requests
from django.test import TestCase, Client
from .models import Portafiolio, Persona
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

    def test_registro(self):
        headerInfo = {'content-type': 'application/json'}
        payload = {"nombre": "hola", "apellido": "apellido", "usuario": "user", "foto": "foto", "perfilProfesional": "test",
             "password": "noPass"}
        jLoad = json.dumps(payload)
        fd = self.client.post('/kata/crearUsuario', headers=headerInfo, data=jLoad)
        self.assertEqual(fd[0]['fields']['nombre'], 'hola')
