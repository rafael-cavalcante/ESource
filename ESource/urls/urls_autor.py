from django.urls import path
from ESource.views import views_autor

urlpatterns = [
    path('autores', views_autor.autores, name='autores'),
    path('criar_autor', views_autor.criar_autor, name='criar_autor'), 
    path('editar_autor/<int:autor_id>/', views_autor.editar_autor, name='editar_autor'),
    path('excluir_autor/<int:autor_id>/', views_autor.excluir_autor, name='excluir_autor'),
]