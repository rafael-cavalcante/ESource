from . import views
from django.urls import path

app_name = "ESource"

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos', views.eventos, name='eventos'),
    path('artigo', views.artigo, name='artigo'),
    path('cadastrarEvento', views.cadastrarEvento, name='cadastrarEvento'),
    path('atualizarEvento/<int:eventoId>/', views.atualizarEvento, name='atualizarEvento'),
    path('deletarEvento/<int:eventoId>/', views.deletarEvento, name='deletarEvento'),
]