from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Advogado, Empresa


class AdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ['nome_advogado', 'email', 'cpf']


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_empresa', 'ramo_atuacao']