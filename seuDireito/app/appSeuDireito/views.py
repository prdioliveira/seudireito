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
            return redirect('appSeuDireito:get_advogado')
    else:
        form = AdvogadoForm()
        advogados = Advogado.objects.all()
        return render(request, 'cad_advogado.html', {'form': form, 'advogados': advogados})


def advogado_edit(request, pk):
    advogado = get_object_or_404(Advogado, pk=pk)
    if request.method == 'POST':
        form = AdvogadoForm(request.POST, instance=advogado)
        if form.is_valid():
            form.save()
        return redirect('appSeuDireito:get_advogado')
    else:
        form = AdvogadoForm(instance=advogado)
        return render(request, 'advogado_edit.html', {'form': form})


def advogado_delete(request, pk):
    advogado = Advogado.objects.get(pk=pk)
    advogado.delete()
    return redirect('appSeuDireito:get_advogado')


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


def empresa_edit(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('appSeuDireito:get_empresa')
    else:
        form = EmpresaForm(instance=empresa)
        return render(request, 'empresa_edit.html', {'form': form})


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


def ordem_servico_edit(request, pk):
    ordem_servico = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem_servico)
        if form.is_valid():
            form.save()
            return redirect('appSeuDireito:get_os')
    else:
        form = OrdemServicoForm(instance=ordem_servico)
        return render(request, 'ordem_servico_edit.html', {'form': form})


def os_list(request):
    ordem_servico = OrdemServico.objects.filter(status_id=1)
    return render(request, 'os_list.html', {'ordem_servico': ordem_servico})


def fazer_proposta_ordem_servico(request, ordem_servico_id):
    if request.method == 'POST':
        form = PropostaForm(request.POST)
        if form.is_valid():
            proposta = form.save(commit=False)
            proposta.ordem_servico_id = ordem_servico_id
            proposta.save()
            return redirect('appSeuDireito:os_list')
    else:
        form = PropostaForm()
        ordem = OrdemServico.objects.get(pk=ordem_servico_id)
        propostas = Proposta.objects.filter(ordem_servico_id=ordem_servico_id)
        return render(request, 'fazer_proposta.html', {'form': form, 'ordem': ordem, 'propostas': propostas})


def proposta_edit(request, pk, ordem_servico_id):
    proposta = get_object_or_404(Proposta, pk=pk)
    if request.method == 'POST':
        form = PropostaForm(request.POST, instance=proposta)
        if form.is_valid():
            form.save()
            return redirect('appSeuDireito:get_proposta', ordem_servico_id=ordem_servico_id)
    else:
        form = PropostaForm(instance=proposta)
        ordem = OrdemServico.objects.get(pk=ordem_servico_id)
        return render(request, 'proposta_edit.html', {'form': form, 'ordem': ordem})


def listar_propostas(request):
    # Retorna todas as OS com Status Criada
    os_ids = OrdemServico.objects.filter(status_id=1).values_list('id')
    propostas_criadas = Proposta.objects.filter(ordem_servico_id__in=os_ids, aceita=None).distinct('ordem_servico_id')

    # Retorna todas as OS com Status Delegada
    os_ids = OrdemServico.objects.filter(status_id=2).values_list('id')
    propostas_delegadas = Proposta.objects.filter(ordem_servico_id__in=os_ids, aceita=True)
    return render(request, 'listar_propostas.html', {'propostas_criadas': propostas_criadas,
                                                     'propostas_delegadas': propostas_delegadas})


def delegar_proposta(request, pk, ordem_servico_id):
    proposta = Proposta.objects.filter(ordem_servico_id=ordem_servico_id)
    if request.method == 'POST':
        # Retorna os ids das OS's da proposta
        os_ids = Proposta.objects.filter(pk=pk).values_list('ordem_servico_id')
        # Atualiza o status da Ordem de Servico para Delegada
        OrdemServico.objects.filter(pk=os_ids).update(status_id=2)

        # Seta o valor do campo como true para determinar a proposta que foi aceita
        Proposta.objects.filter(pk=pk).update(aceita=True)

        # Retorna as propostas nao aceitas para setar o valor false
        prop_na = Proposta.objects.exclude(pk=pk).values_list('id')
        os_id = Proposta.objects.filter(pk=pk).values_list('ordem_servico_id')
        Proposta.objects.filter(id__in=prop_na, ordem_servico_id=os_id).update(aceita=False)
        return redirect('appSeuDireito:listar_propostas')
    return render(request, 'proposta_detalhe.html', {'proposta': proposta})


def concluir_ordem_servico(request, pk):
    if request.method == 'POST':
        # Pega o id da ordem de servico
        os_id = Proposta.objects.filter(pk=pk).values_list('ordem_servico_id')
        # Atualiza o status da OS para Finalizada
        OrdemServico.objects.filter(pk=os_id).update(status_id=3)
        return redirect('appSeuDireito:listar_propostas')
    # Retorna o contexto para a página
    proposta = Proposta.objects.get(pk=pk)
    return render(request, 'finalizar_ordem_servico.html', {'proposta': proposta})