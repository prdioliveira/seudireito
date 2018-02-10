from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AdvogadoForm, EmpresaForm
from .models import Advogado, Empresa


def index(request):
    return render(request, 'index.html')


def advogado_cadastro(request):
    if request.method == 'POST':
        form = AdvogadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/advogado/')
    else:
        form = AdvogadoForm()
        advogados = Advogado.objects.all()
        return render(request, 'cad_advogado.html', {'form': form, 'advogados': advogados})


def empresa_cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/empresa/')
    else:
        form = EmpresaForm()
        empresas = Empresa.objects.all()
        return render(request, 'cad_empresa.html', {'form': form, 'empresas': empresas})