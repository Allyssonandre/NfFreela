from django.urls import path
#    IMPORT DAS VIEWS
from . import views
from django.conf import settings

from django.conf.urls.static import static
# ================================================ URL´S DO SISTEMA ==================================================== #
urlpatterns = [
	path('', views.informacoes, name="informacoes"), # URL DA PÁGINA INICIAL DO NFREELA
    path('formulario/',views.formulario, name="formulario"), # URL DO FORMULÁRIO DO PROFISSIONAL GRÁTIS
    path('prepesquisa/',views.prepesquisa, name="prepesquisa"), # URL DE PESQUISA DE PROFISSIONAL GRÁTIS
    path('termos/',views.termos, name="termos"), # URL DE TERMO DE USO E POLÍTICA DE PRIVACIDADE
    path('bemvindo/',views.bemvindo, name="bemvindo"), # URL DA PÁGINA INICIAL DO PROFISSIONAL PREMIUM
    path('usuariopremium/<int:id>', views.usuariopremium, name="usuariopremium"), # URL DO PERFIL DO PROFISSIONAL PREMIUM
    path('meuperfil', views.meuperfil, name="meuperfil"), # URL DO PERFIL DO PROFIISSIONAL PREMIUM
    path('editarperfil/<int:id>', views.editarperfil, name="editarperfil"), # URL DE EDIÇAO DOS DADOS DO PROFISSIONAL PREMIUM
    path('dicasusuariofree',views.dicasusuariofree, name="dicasusuariofree"), # URL DE DICAS DO PROFISSIONAL FREE
    path('dicasusuariopremium',views.dicasusuariopremium, name="dicasusuariopremium"), # URL DE DICAS PROFISSIONAL PREMIUM
    path('verificacao',views.verificacao, name="verificacao"), # URL DE VERIFICAÇÃO DE FORMULÁRIO PREMIUM
    path('videospremium',views.videospremium, name="videospremium"),  # URL DE VÍDEOS PREMIUM
    path('somos',views.somos, name="somos"), # PÁGINA DE QUEM SOMOS
    path('vagas',views.vagas, name="vagas"), # URL DA PÁGINA DE VAGAS DE EMPREGOS
    path('participa/<int:id>',views.participa, name="participa"), # URL PARA INSCRIÇÃO EM PROCESSOS SELETIVOS
    path('inscricao/<int:id>', views.inscricao, name="inscricao"), # URL DAS INSCRIÇÕES
    path('faq/',views.pergunta,name="pergunta"), # URL DE PERGUNTAS FREQUENTES
    path('curriculos/',views.curriculos,name="curriculos"), # URL DOS CURRICULOS ENVIADOS
    path('enviarcurriculo/',views.enviarcurriculo,name='enviarcurriculo'),
    path('deletaPdf/<int:id>',views.deletaPdf,name='deletaPdf'),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # imagem de perfil