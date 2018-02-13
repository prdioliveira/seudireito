from django.contrib import admin
from .models import Advogado, Empresa, Status, OrdemServico, Proposta

# Register your models here.
admin.site.register(Advogado)
admin.site.register(Empresa)
admin.site.register(Status)
admin.site.register(OrdemServico)
admin.site.register(Proposta)
