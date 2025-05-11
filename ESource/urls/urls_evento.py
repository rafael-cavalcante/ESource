from django.urls import path
from ESource.views import eventos, cadastrarEvento, atualizarEvento, deletarEvento, listar_eventos_arquivados, arquivar_evento, desarquivar_evento

urlpatterns = [
    path('eventos', eventos, name='eventos'),
    path('cadastrarEvento', cadastrarEvento, name='cadastrarEvento'),
    path('atualizarEvento/<int:eventoId>/', atualizarEvento, name='atualizarEvento'),
    path('deletarEvento/<int:eventoId>/', deletarEvento, name='deletarEvento'),
    path('arquivar_evento/<int:eventoId>/', arquivar_evento, name='arquivar_evento'),
    path('listar_eventos_arquivados/', listar_eventos_arquivados, name='listar_eventos_arquivados'),
    path('desarquivar_evento/<int:eventoId>/', desarquivar_evento, name='desarquivar_evento'),
]