from . import views
from django.urls import path, include

app_name = "ESource"

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos', views.eventos, name='eventos'),
    path('autores', views.autores, name='autores'),
    path('cadastrarEvento', views.cadastrarEvento, name='cadastrarEvento'),
    path('atualizarEvento/<int:eventoId>/', views.atualizarEvento, name='atualizarEvento'),
    path('deletarEvento/<int:eventoId>/', views.deletarEvento, name='deletarEvento'),
    path('arquivar_evento/<int:eventoId>/', views.arquivar_evento, name='arquivar_evento'),
    path('desarquivar_evento/<int:eventoId>/', views.desarquivar_evento, name='desarquivar_evento'),
    path('listar_eventos_arquivados/', views.listar_eventos_arquivados, name='listar_eventos_arquivados'),
    path('cadastrarArtigo', views.cadastrarArtigo, name='cadastrarArtigo'),
    path('visualizarArtigo/<int:artigoId>', views.visualizarArtigo, name='visualizarArtigo'),
    path('deletarArtigo/<int:artigoId>/', views.deletarArtigo, name='deletarArtigo'),
    path('atualizarArtigo/<int:artigoId>/', views.atualizarArtigo, name='atualizarArtigo'),
    path('arquivar_artigo/<int:artigoId>/', views.arquivar_artigo, name='arquivar_artigo'),
    path('desarquivar_artigo/<int:artigoId>/', views.desarquivar_artigo, name='desarquivar_artigo'),
    path('listar_artigos_arquivados/', views.listar_artigos_arquivados, name='listar_artigos_arquivados'),
    path('cadastrarAutor', views.cadastrarAutor, name='cadastrarAutor'),
    path('atualizarAutor/<int:autorId>/', views.atualizarAutor, name='atualizarAutor'),
    path('deletarAutor/<int:autorId>/', views.deletarAutor, name='deletarAutor'),
    path('entrar', views.entrar, name='entrar'),
    path('sair', views.sair, name='sair')
]