from django.test import TestCase
from .models import Empresa, Advogado, OrdemServico
from .models import Status


class ModelTest(TestCase):
    def setUp(self):
        self.advogado = Advogado.objects.create(nome_advogado='Alan Delon',
                                                email='alan.delon@gmail.com',
                                                cpf='123.123.123-12')

        self.empresa = Empresa.objects.create(nome_empresa='Construshow LTDA',
                                              ramo_atuacao='Construção Civil')

        self.status = Status.objects.create(status='Criada')

        self.ordem_servico = OrdemServico.objects.create(empresa=self.empresa,
                                                         titulo='Processo XPTO',
                                                         descricao='Empresa X está sendo processada por seus clientes',
                                                         status=self.status)

    def test_advogado_model(self):
        self.assertEqual(str(self.advogado), self.advogado.nome_advogado)

    def test_empresa_model(self):
        self.assertEqual(str(self.empresa), self.empresa.nome_empresa)

    def test_ordem_servico_model(self):
        self.assertEqual(str(self.ordem_servico), self.ordem_servico.titulo)