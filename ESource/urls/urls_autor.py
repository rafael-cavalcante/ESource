from django.urls import path
from ESource.views import autores, cadastrarAutor, atualizarAutor, deletarAutor

urlpatterns = [
    path('autores', autores, name='autores'),
    path('cadastrarAutor', cadastrarAutor, name='cadastrarAutor'), 
    path('atualizarAutor/<int:autorId>/', atualizarAutor, name='atualizarAutor'),
    path('deletarAutor/<int:autorId>/', deletarAutor, name='deletarAutor'),
]