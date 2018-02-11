from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AdvogadoForm, EmpresaForm
from .models import Advogado, Empresa, Status
from .models import OrdemServico, Proposta
from .forms import OrdemServicoForm, PropostaForm


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


def ordem_servico_cadastro(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            os = form.save(commit=False)
            os.status_id = Status.objects.get(pk=1).id
            os.save()
            return redirect('/ordem-servico/')
    else:
        form = OrdemServicoForm()
        ordem_servico = OrdemServico.objects.filter(status_id=1)
        return render(request, 'cad_os.html', {'form': form, 'ordem_servico': ordem_servico})


def os_list(request):
    ordem_servico = OrdemServico.objects.filter(status_id=1)
    return render(request, 'os_list.html', {'ordem_servico': ordem_servico})


def fazer_proposta_ordem_servico(request, pk):
    os = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = PropostaForm(request.POST)
        if form.is_valid():
            proposta = form.save(commit=False)
            proposta.ordem_servico_id = pk
            proposta.save()
            return redirect('appSeuDireito:os_list')
    else:
        form = PropostaForm()
        ordem = OrdemServico.objects.get(pk=pk)
        propostas = Proposta.objects.filter(ordem_servico_id=pk)
        print(propostas)
        return render(request, 'fazer_proposta.html', {'form': form, 'ordem': ordem, 'propostas': propostas})