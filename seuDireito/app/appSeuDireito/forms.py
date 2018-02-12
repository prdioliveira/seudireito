from django import forms
from .models import Advogado, Empresa, OrdemServico
from .models import Proposta


class AdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ['nome_advogado', 'email', 'cpf']


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_empresa', 'ramo_atuacao']


class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['empresa', 'titulo', 'descricao', 'status']

        exclude = ['status']


class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = ['ordem_servico', 'advogado', 'valor_proposta']

        exclude = ['ordem_servico']