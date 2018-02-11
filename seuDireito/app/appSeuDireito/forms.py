from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        advogado = self.cleaned_data['advogado']
        ordem_servico = self.cleaned_data['ordem_servico']

        id_advogado = Advogado.objects.filter(nome_advogado=advogado)
        id_os = OrdemServico.objects.filter(ordem_servico=ordem_servico)

        if id_advogado and id_os in Proposta.objects.all():
            raise forms.ValidationError('O advogado já fez uma proposta para esta OS')
        return 'Advogado: ' + advogado + ' - OS: ' + ordem_servico