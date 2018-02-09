from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AdvogadoForm, EmpresaForm


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
        return render(request, 'cad_advogado.html', {'form': form})


def empresa_cadastro(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/empresa/')
    else:
        form = EmpresaForm()
        return render(request, 'cad_empresa.html', {'form': form})