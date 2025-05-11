from django.urls import path
from ESource.views import eventos, criar_evento, editar_evento, excluir_evento, listar_eventos_arquivados, arquivar_evento, desarquivar_evento

urlpatterns = [
    path('eventos', eventos, name='eventos'),
    path('criar_evento',criar_evento, name='criar_evento'),
    path('editar_evento/<int:evento_id>/',editar_evento, name='editar_evento'),
    path('excluir_evento/<int:evento_id>/',excluir_evento, name='excluir_evento'),
    path('arquivar_evento/<int:evento_id>/', arquivar_evento, name='arquivar_evento'),
    path('desarquivar_evento/<int:evento_id>/', desarquivar_evento, name='desarquivar_evento'),
    path('listar_eventos_arquivados/', listar_eventos_arquivados, name='listar_eventos_arquivados'),
]