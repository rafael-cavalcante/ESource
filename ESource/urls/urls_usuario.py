from django.urls import path
from ESource.views import views_usuario

urlpatterns = [
    path('entrar', views_usuario.entrar, name='entrar'),
    path('sair', views_usuario.sair, name='sair'),
]