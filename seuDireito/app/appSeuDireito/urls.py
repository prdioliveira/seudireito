from django.conf.urls import url
from . import views

app_name = 'appSeuDireito'

urlpatterns = [
    url(r'^advogado/$', views.advogado_cadastro, name='get_advogado'),
    url(r'^empresa/$', views.empresa_cadastro, name='get_empresa'),
    url(r'^ordem-servico/$', views.ordem_servico_cadastro, name='get_os'),
    url(r'^ordem-servico/ver/$', views.os_list, name='os_list'),
    url(r'^ordem-servico/(?P<pk>[0-9]+)/proposta/$', views.fazer_proposta_ordem_servico, name='get_proposta'),
    url(r'^$', views.index, name='index'),
]