from . import views
from django.urls import path, include

app_name = "ESource"

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos', views.eventos, name='eventos'),
    path('visualizarArtigo/<int:artigoId>', views.visualizarArtigo, name='visualizarArtigo'),
    path('cadastrarEvento', views.cadastrarEvento, name='cadastrarEvento'),
    path('atualizarEvento/<int:eventoId>/', views.atualizarEvento, name='atualizarEvento'),
    path('deletarEvento/<int:eventoId>/', views.deletarEvento, name='deletarEvento'),
    path('cadastrarArtigo', views.cadastrarArtigo, name='cadastrarArtigo'),
    path('deletarArtigo/<int:artigoId>/', views.deletarArtigo, name='deletarArtigo'),
    path('atualizarArtigo/<int:artigoId>/', views.atualizarArtigo, name='atualizarArtigo'),
    path('entrar', views.entrar, name='entrar'),
    path('sair', views.sair, name='sair')
]