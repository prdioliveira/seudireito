from django import forms
from .models import Advogado, Empresa, OrdemServico
from .models import Proposta


class AdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ['nome_advogado', 'email', 'cpf']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        obj_adv = Advogado.objects.filter(cpf=cpf).count()
        if obj_adv > 0:
            raise forms.ValidationError(u'CPF já cadastrado!')
        return self.cleaned_data['cpf']


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
        valor_proposta = forms.DecimalField(max_digits=8, decimal_places=2, localize=True)
        model = Proposta
        fields = ['ordem_servico', 'advogado', 'valor_proposta']

        exclude = ['ordem_servico']