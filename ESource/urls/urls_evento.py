from django.urls import path
from ESource.views import views_evento

urlpatterns = [
    path('eventos', views_evento.eventos, name='eventos'),
    path('criar_evento', views_evento.criar_evento, name='criar_evento'),
    path('editar_evento/<int:evento_id>/', views_evento.editar_evento, name='editar_evento'),
    path('excluir_evento/<int:evento_id>/', views_evento.excluir_evento, name='excluir_evento'),
    path('arquivar_evento/<int:evento_id>/', views_evento.arquivar_evento, name='arquivar_evento'),
    path('desarquivar_evento/<int:evento_id>/', views_evento.desarquivar_evento, name='desarquivar_evento'),
    path('listar_eventos_arquivados/', views_evento.listar_eventos_arquivados, name='listar_eventos_arquivados'),
]