from django import forms
from .models import *
from .models import Profissional  # MODEL DOS PROFISSIONAIS FREE
from .models import UsuarioPay    # MODEL DOS PROFISSIONAIS PAGOS
from .models import Empresa       # MODEL DAS EMPRESAS PARCEIRAS DO NFREELA
from .models import Processos     # MODEL DE PROCESSOS SELETIVOS OU VAGAS ABERTAS PELAS EMPRESAS PARCEIRAS
from .models import Incricao      # MODEL DAS INCRIÇÕES REALIZADAS, PARA PROCESSOS SELETIVOS
from .models import Vendedor      # MODEL DA INCRIÇÃO DO VENDEDOR
from .models import Pdfs          # MODEL DO CURRICULO    
#======= MODEL DO FORMULARIO PROFISSIONAL FREE =======#
class Form(forms.ModelForm):
  class Meta:
    model = Profissional
    fields = ('nome','contato','email','rua','bairro',
      'cidade','estado','numero'
      ,'profissao','image',
      'Descricao','termo')
      # =====================================================#

# ======== MODEL DO FORMULARIO DO PROFISSIONAL PREMIUM ====== #
class UsuarioPago(forms.ModelForm):

	class Meta:
		model = UsuarioPay
		fields = 'name','phone','email','rua','bairro','cidade','estado','numero','profissao','image','premium','Descricao',
    
# =====================================================#

# ======== MODEL DO FORMULARIO DA EMPRESA PARCEIRA ====== #
class Empresaparceira(forms.ModelForm):
  class Meta:
    model = Empresa
    fields = '__all__'

# =====================================================#

# ======== MODEL DO PROCESSO SELETIVO ====== #
class Empresavaga(forms.ModelForm):
  class Meta:
    model = Processos
    fields = '__all__'

# =====================================================#

# ============= MODEL DA INCRIÇÃO ======================#
class Inscritos(forms.ModelForm):
  class Meta:
    model = Incricao
    fields = 'nome_candidato','telefone_candidato','empresa'
# =====================================================#

# ============== CLASSE DO VENDEDOR ===================#

class Vendendo(forms.ModelForm):
  class Meta:
    model  = Vendedor
    fields = '__all__'


# ====================================================== 

class Pdf(forms.ModelForm):
  class Meta:
    model = Pdfs
    fields = 'profissao','pdf' 
  

