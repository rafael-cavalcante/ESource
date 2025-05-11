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
    path('cadastrarArtigo', views.cadastrarArtigo, name='cadastrarArtigo'),
    path('visualizarArtigo/<int:artigoId>', views.visualizarArtigo, name='visualizarArtigo'),
    path('deletarArtigo/<int:artigoId>/', views.deletarArtigo, name='deletarArtigo'),
    path('atualizarArtigo/<int:artigoId>/', views.atualizarArtigo, name='atualizarArtigo'),
    path('cadastrarAutor', views.cadastrarAutor, name='cadastrarAutor'),
    path('atualizarAutor/<int:autorId>/', views.atualizarAutor, name='atualizarAutor'),
    path('deletarAutor/<int:autorId>/', views.deletarAutor, name='deletarAutor'),
    path('entrar', views.entrar, name='entrar'),
    path('sair', views.sair, name='sair')
]