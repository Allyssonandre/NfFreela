from django.contrib import admin   # IMPORTANDO O ADMIN DO DJANGO
from .models import Profissional   # MODEL DOS PROFISSIONAIS FREE
from .models import UsuarioPay     # MODEL DOS PROFISSIONAIS PAGOS
from .models import Empresa        # MODEL DAS EMPRESAS PARCEIRAS DO NFREELA
from .models import Processos      # MODEL DE PROCESSOS SELETIVOS OU VAGAS ABERTAS PELAS EMPRESAS PARCEIRAS
from .models import Incricao       # MODEL DAS INCRIÇÕES REALIZADAS, PARA PROCESSOS SELETIVOS
from .models import Vendedor       # MODEL DO VENDEDOR
from .models import Pdfs           # MODEL CURRICULO
from django.contrib.auth import get_permission_codename
# DISPLAY DOS PARCEIROS
class Parceiros(admin.ModelAdmin):
	list_display = ('empresa','cnpj','cidade_empresa','telefone_empresa','email_empresa','ramo_empresa','criado')
	search_fields = ('empresa',)
# ************************************************************************************************************************** #
# DISPLAY DAS INCRIÇÕES
class AdminIncricao(admin.ModelAdmin):
	list_display    = ('nome_candidato','telefone_candidato','empresa','inscricao_criada','user')
	search_fields   = ('nome_candidato','empresa')
# ************************************************************************************************************************** #
# DISPLAY DOS PROCESSOS SELETIVOS ABERTOS
class ProcessoSeletivo(admin.ModelAdmin):
	list_display    = ('empresa_vaga','vaga','cidade_vaga','telefone_vaga','email_vaga','criado_vaga')
	search_fields   = ('empresa_vaga',)
# ************************************************************************************************************************** #
# DISPLAY DOS PROFISSIONAIS FREE
class ProfissionalFree(admin.ModelAdmin):
	 list_display  = ('nome','contato','email','cidade','profissao','created_at')
	 search_fields = ('nome',)
# ************************************************************************************************************************** #
# DISPLAY DOS PROFISSIONAIS PAGOS
class ProfissionalPago(admin.ModelAdmin):
	list_display  = ('name','phone','email','cidade','profissao','created_at','user')
	search_fields = ('name','email')
# ************************************************************************************************************************** #
# DISPLAY DOS VENDEDORES
class Vendedores(admin.ModelAdmin):
	list_display  = ('Nome','Cidade_Vendedor','uf','Telefone','Email_vendedor','Conta_Bancaria','cpf','Codigo','Data_Inscricao')
	search_fields = ('Codigo',)
# ************************************************************************************************************************** #
# DISPLAY DOS CURRÍCULOS
class VerCurriculos(admin.ModelAdmin):
	list_display  = ('user','profissao','pdf','criacao')
	search_fields = ('profissao',)
# ************************************************************************************************************************** #
# ============================ INCLUSÃO DAS CLASSES NO ADMIN DO NFREELA ==================================================== #
admin.site.register(Profissional, ProfissionalFree)
admin.site.register(UsuarioPay, ProfissionalPago)
admin.site.register(Empresa,Parceiros)
admin.site.register(Processos, ProcessoSeletivo)
admin.site.register(Incricao, AdminIncricao)
admin.site.register(Vendedor,Vendedores)
admin.site.register(Pdfs,VerCurriculos)

class MyModelAdmin(admin.ModelAdmin):
   readonly_fields = ('field')
admin.site.site_header = "ADMINISTRAÇÃO NFREELA" 