from django.urls import path
from ESource.views import views_artigo

urlpatterns = [
    path('', views_artigo.artigos, name='artigos'),
    path('criar_artigo', views_artigo.criar_artigo, name='criar_artigo'),
    path('exibir_artigo/<int:artigo_id>', views_artigo.exibir_artigo, name='exibir_artigo'),
    path('editar_artigo/<int:artigo_id>/', views_artigo.editar_artigo, name='editar_artigo'),
    path('excluir_artigo/<int:artigo_id>/', views_artigo.excluir_artigo, name='excluir_artigo'),
    path('listar_artigos_arquivados/', views_artigo.listar_artigos_arquivados, name='listar_artigos_arquivados'),
    path('arquivar_artigo/<int:artigo_id>/', views_artigo.arquivar_artigo, name='arquivar_artigo'),
    path('desarquivar_artigo/<int:artigo_id>/', views_artigo.desarquivar_artigo, name='desarquivar_artigo'),
]