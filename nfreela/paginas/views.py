from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User

# ************* IMPORTS MODELS E FORMS ************ #
# IMPORTANDO O MODEL E FORMS PROFISSIONAL #
from .models import Profissional
from .forms import Form
# --------------------------------------- #
# IMPORTANDO O MODEL E FORMS PROFISSIONAL PAGO
from .models import UsuarioPay
from .forms import UsuarioPago
# --------------------------------------- #
# IMPORTANDO O MODEL E FORMS DAS EMPRESAS
from .models import Processos
from .forms import Empresavaga
# --------------------------------------- #
# IMPORTANDO O MODEL E FORMS DOS PROCESSOS SELETIVOS #
from .models import Incricao
from .forms import Inscritos
# --------------------------------------- #
from .models import Pdfs
from .forms import Pdf 
# ************** FIM DOS IMPORTS ******************* #
# IMPORTA PAGINATOR
from django.core.paginator import Paginator
# -----------------------------------------
# LOGIN
from django.contrib.auth.decorators import login_required
# --------------------------------------------
from django.contrib import messages
import datetime
from django.db.models import Count

# =============================================== LÓGICA DO SISTEMA =========================================================== #

# PAGINÁ INICIAL DE INFORMAÇÕES, DE USUÁRIO NÃO LOGADO
def informacoes(request):
    busca = request.GET.get('busca')
    if busca:
        profissional = UsuarioPay.objects.filter(profissao__icontains=busca)
    else:
        usuario = UsuarioPay.objects.all().order_by('-updated_at')
        paginator = Paginator(usuario, 5)
        pagina = request.GET.get('page')
        profissional = paginator.get_page(pagina)
    return render(request , 'inicio/informacoes.html', {'profissional':profissional})
# -----------------------------------------------------
# PAGINÁ DICAS USUÁRIO FREE
def dicasusuariofree(request):
    return render(request, 'inicio/dicasusuariofree.html')
# -----------------------------------------------------
# PAGINÁ DICAS USUÁRIO PREMIUM
def dicasusuariopremium(request):
    return render(request, 'inicio/dicasusuariopremium.html')
# -----------------------------------------------------
# PÁGINA DE QUEM SOMOS
def somos(request):
    return render(request, 'inicio/somos.html')
# -----------------------------------------------------
# PÁGINA DE BOAS VINDAS
@login_required 
def bemvindo(request):
    return render(request, 'inicio/bemvindo.html')

# PÁGINA DE PESQUISA DE PROFISSIONAL   
def prepesquisa(request): 
    busca = request.GET.get('busca')
    if busca:
        profissional = Profissional.objects.filter(profissao__icontains=busca)
    else:
        usuario = Profissional.objects.all().order_by('-updated_at')
        paginator = Paginator(usuario, 2)
        pagina = request.GET.get('page')
        profissional = paginator.get_page(pagina)
    return render(request, 'inicio/prepesquisa.html',{'profissional': profissional})
# -----------
# FORMULÁRIO PROFISSIONAL GRÁTIS
def formulario(request):
    if request.method == 'POST':
        formulario = Form(request.POST, request.FILES or none)
        if formulario.is_valid():
            formulario.save()
            messages.info(request, 'Seu cadastro foi concluído com sucesso, você já faz parte da Família NFreela. Boa sorte !!!')
            return redirect('/formulario')
    else:
        formulario = Form()
        return render(request, 'inicio/formulario.html',{'formulario':formulario})
# ----------------------------------------------------------------------------------

# VIEW DE PROFISSIONAL PREMIUM
def usuariopremium(request, id):
    profissional = get_object_or_404(UsuarioPay, pk=id)
    profissional.views = profissional.views + 1
    profissional.save()
    return render(request, 'inicio/usuariopremium.html',{'profissional': profissional})

# PÁGINA DE TERMO E POLÍTICAs
def termos(request):
    return render(request, 'inicio/termos.html')
# ------------------------------------------------------------------------------   

# PÁGINA DE BOAS VINDAS (PROFISSIONAL PREMIUM), COM FORMULARIO PREMIUM

@login_required
def bemvindo(request):
    formulario = UsuarioPago(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if formulario.is_valid():
            obj = formulario.save(commit = False)
            obj.user = request.user
            obj.save()
            messages.info(request, 'PARABÉNS')
            return redirect('/verificacao')
    else:
        formulario = UsuarioPago()
        return render(request, 'inicio/bemvindo.html',{'formulario':formulario})



# PÁGINA DE PERFIL DO PROFISSIONAL PREMIUM
@login_required
def meuperfil(request):
    formulario = UsuarioPay.objects.all().filter(user=request.user)
    file       = Pdfs.objects.all().filter(user=request.user)
    contexto   = {'formulario': formulario,'file': file}
    return render(request, 'inicio/meuperfil.html', contexto)

    

# EDITA PERFIL  DE USUÁRIO PREMIUM
@login_required
def editarperfil(request, id):
    formulario = get_object_or_404(UsuarioPay, pk=id)
    form = UsuarioPago(instance=formulario)
    if(request.method == 'POST'):
        form = UsuarioPago(request.POST, instance=formulario)
        if(form.is_valid()):
            formulario.save()
            return redirect('/meuperfil')
        else:
            return render(request, 'inicio/editausuer.html', {'form': form, 'formulario': formulario})

    else:
        return render(request, 'inicio/editausuer.html', {'form': form, 'formulario': formulario})

# CKECKOUT DE PAGAMENTO PAGSEGURO
@login_required
def verificacao(request):
    return render(request, 'inicio/verificacao.html')

# PÁGINA DE VIDEO CURRÍCULO

def videospremium(request):
    return render(request, 'inicio/videospremium.html')


# PÁGINA DA VAGAS EXISTENTES
@login_required
def vagas(request):
    busca = request.GET.get('busca')
    if busca:
        vagas = Processos.objects.filter(vaga__icontains=busca)
    else:
        vagas_s = Processos.objects.all().order_by('-criado_vaga')
        paginator = Paginator(vagas_s, 8)
        pagina = request.GET.get('page')
        vagas = paginator.get_page(pagina)
    return render(request, 'inicio/vagas.html',{'vagas': vagas})
 
# PÁGINA DE INSCRIÇÃO DA PARTICIPANTES EM PROCESSOS SELETIVOS
@login_required
def participa(request, id):
    participando = get_object_or_404(Processos, pk=id)
    return render(request, 'inicio/participa.html',{'participando': participando})



# PÁGINA DE INSCRIÇÃO REALIZADA COM SUCESSO
@login_required
def inscricao(request, id):
    inscrevendo = Inscritos(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        inscrevendo = Inscritos(request.POST)
        if inscrevendo.is_valid():
            usuario = inscrevendo.save(commit=False)
            usuario.user = request.user;
            usuario.save()
            messages.info(request, 'Obrigado por participa !!!, Se atente a data e hora do processo seletivo')
            return redirect('/vagas')
    else:
        inscrevendo = Inscritos()
        inscritos  = Incricao.objects.all().filter(user=request.user)
        c = {'inscrevendo':inscrevendo,'inscritos':inscritos}   
        return render(request, 'inicio/inscricao.html',c)


def pergunta(request):
    return render(request, 'inicio/faq.html')

def curriculos(request):
    busca = request.GET.get('busca')
    if busca:
        pdfs = Pdfs.objects.filter(profissao__icontains=busca)
    else:
        pdfs  =  Pdfs.objects.all().order_by('-criacao')
    return render(request, 'inicio/curriculos.html', {'pdfs':pdfs})

# VIEW DE ENVIO DE CURRICULO

@login_required
def enviarcurriculo(request):
    if request.method == 'POST':
        pdf = Pdf(request.POST, request.FILES)
        if pdf.is_valid():
            obj = pdf.save(commit = False)
            obj.user = request.user
            obj.save()
            messages.info(request, 'Seu currículo foi enviado com sucesso BOA SORTE !!!')
            return redirect('meuperfil')
    else:
        pdf = Pdf()
        return render(request, 'inicio/enviar_curriculo.html',{'pdf':pdf})




@login_required
def deletaPdf(request, id):
    deletando = get_object_or_404(Pdfs, pk=id)
    deletando.delete()
    messages.info(request, 'Currículo excluído!!')
    return redirect('meuperfil')




