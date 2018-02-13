from django.test import TestCase
from .models import Empresa, Advogado, OrdemServico
from django.core.management import call_command
from .models import Status


class ModelTest(TestCase):
    def setUp(self):
        call_command('loaddata', 'initial_data.json', verbosity=0)
        self.advogado = Advogado.objects.create(nome_advogado='Alan Delon',
                                                email='alan.delon@gmail.com',
                                                cpf='123.123.123-12')

        self.empresa = Empresa.objects.create(nome_empresa='Construshow LTDA',
                                              ramo_atuacao='Construção Civil')

        self.ordem_servico = OrdemServico.objects.create(empresa=self.empresa,
                                                         titulo='Processo XPTO',
                                                         descricao='Empresa X está sendo processada por seus clientes',
                                                         status_id=1)

    def test_advogado_model(self):
        self.assertEqual(str(self.advogado), self.advogado.nome_advogado)

    def test_empresa_model(self):
        self.assertEqual(str(self.empresa), self.empresa.nome_empresa)

    def test_ordem_servico_model(self):
        self.assertEqual(str(self.ordem_servico), self.ordem_servico.titulo)

    def test_fixtures_status(self):
        status = ['Criada', 'Delegada', 'Finalizada']

        for st in status:
            self.assertIn(st, str(Status.objects.all()))

