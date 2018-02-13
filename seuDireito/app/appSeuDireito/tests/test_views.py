from django.test import Client, TestCase


class AdvogadoTest(TestCase):
    def test_cadastro_advogado_get(self):
        client = Client()
        response = client.get('/advogado/')
        self.assertEqual(response.status_code, 200)