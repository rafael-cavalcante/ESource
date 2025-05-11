from django.urls import path
from ESource.views import artigos, criar_artigo, exibir_artigo, excluir_artigo, editar_artigo, listar_artigos_arquivados, arquivar_artigo, desarquivar_artigo

urlpatterns = [
    path('', artigos, name='artigos'),
    path('criar_artigo', criar_artigo, name='criar_artigo'),
    path('exibir_artigo/<int:artigo_id>', exibir_artigo, name='exibir_artigo'),
    path('editar_artigo/<int:artigo_id>/', editar_artigo, name='editar_artigo'),
    path('excluir_artigo/<int:artigo_id>/', excluir_artigo, name='excluir_artigo'),
    path('listar_artigos_arquivados/', listar_artigos_arquivados, name='listar_artigos_arquivados'),
    path('arquivar_artigo/<int:artigo_id>/', arquivar_artigo, name='arquivar_artigo'),
    path('desarquivar_artigo/<int:artigo_id>/', desarquivar_artigo, name='desarquivar_artigo'),
]