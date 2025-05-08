from . import views
from django.urls import path

app_name = "ESource"

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos', views.eventos, name='eventos'),
    path('artigo', views.artigo, name='artigo'),
]