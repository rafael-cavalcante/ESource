from django.urls import path
from ESource.views import autores, criar_autor, editar_autor, excluir_autor

urlpatterns = [
    path('autores', autores, name='autores'),
    path('criar_autor',criar_autor, name='criar_autor'), 
    path('editar_autor/<int:autor_id>/',editar_autor, name='editar_autor'),
    path('excluir_autor/<int:autor_id>/', excluir_autor, name='excluir_autor'),
]