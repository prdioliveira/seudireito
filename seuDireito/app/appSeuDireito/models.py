from django.db import models


class Advogado(models.Model):
    nome_advogado = models.CharField(max_length=80, null=False)
    email = models.EmailField(null=False)
    cpf = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.nome_advogado


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100, null=False)
    ramo_atuacao = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.nome_empresa