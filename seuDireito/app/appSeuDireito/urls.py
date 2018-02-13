from django.conf.urls import url
from . import views

app_name = 'appSeuDireito'

urlpatterns = [
    url(r'^advogado/$', views.advogado_cadastro, name='get_advogado'),
    url(r'^advogado/(?P<pk>[0-9]+)/editar/$', views.advogado_edit, name='advogado_editar'),
    url(r'^advogado/(?P<pk>[0-9]+)/deletar/$', views.advogado_delete, name='advogado_deletar'),
    url(r'^empresa/$', views.empresa_cadastro, name='get_empresa'),
    url(r'^empresa/(?P<pk>[0-9]+)/editar/$', views.empresa_edit, name='empresa_editar'),
    url(r'^ordem-servico/$', views.ordem_servico_cadastro, name='get_os'),
    url(r'^ordem-servico/visualizar-ordem-servico/$', views.visualizar_ordem_seervico, name='visualizar_ordem_seervico'),
    url(r'^ordem-servico/visualizar-ordem-servico/(?P<ordem_servico_id>[0-9]+)/$', views.proposta_ordem_servico, name='propostas_all_os'),
    url(r'^ordem-servico/(?P<pk>[0-9]+)/editar/$', views.ordem_servico_edit, name='ordem_servico_editar'),
    url(r'^ordem-servico/ver/$', views.os_list, name='os_list'),
    url(r'^ordem-servico/(?P<ordem_servico_id>[0-9]+)/proposta/$', views.fazer_proposta_ordem_servico, name='get_proposta'),
    url(r'^ordem-servico/(?P<ordem_servico_id>[0-9]+)/proposta/(?P<pk>[0-9]+)/editar/$', views.proposta_edit, name='proposta_editar'),
    url(r'^ordem-servico/delegar-ordem-servico/$', views.listar_propostas, name='listar_propostas'),
    url(r'^ordem-servico/delegar-ordem-servico/(?P<pk>[0-9]+)/proposta/(?P<ordem_servico_id>[0-9]+)/$', views.delegar_proposta, name='delegar_proposta'),
    url(r'^ordem-servico/finalizar-ordem-servico/(?P<pk>[0-9]+)/proposta/$', views.concluir_ordem_servico, name='finalizar_os'),
    url(r'^$', views.index, name='index'),
]