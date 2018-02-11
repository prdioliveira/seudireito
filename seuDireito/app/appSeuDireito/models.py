from django.db import models


class Advogado(models.Model):
    nome_advogado = models.CharField(max_length=80, null=False)
    email = models.EmailField(null=False)
    cpf = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.nome_advogado

    class Meta:
        db_table = 'advogado'


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100, null=False)
    ramo_atuacao = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.nome_empresa

    class Meta:
        db_table = 'empresa'


class Status(models.Model):
    status = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'status'


class OrdemServico(models.Model):
    empresa = models.ForeignKey(Empresa)
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.TextField(max_length=1024, null=False)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'ordem_servico'


class Proposta(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico)
    advogado = models.ForeignKey(Advogado)
    valor_proposta = models.CharField(max_length=10)

    def __str__(self):
        return self.valor_proposta

    class Meta:
        db_table = 'proposta'