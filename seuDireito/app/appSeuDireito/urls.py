from django.conf.urls import url
from . import views

app_name = 'appSeuDireito'

urlpatterns = [
    url(r'^advogado/$', views.advogado_cadastro, name='get_advogado'),
    url(r'^empresa/$', views.empresa_cadastro, name='get_empresa'),
    url(r'^$', views.index, name='index'),
]
