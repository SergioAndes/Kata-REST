from django.test import TestCase, Client


# Create your tests here.

class KataTestCase(TestCase):

    def test_servicio_list_status(self):
        url = '/kata/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
