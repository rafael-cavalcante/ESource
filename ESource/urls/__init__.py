from django.urls import include, path
from . import urls_evento, urls_artigo, urls_autor, urls_usuario

app_name = "ESource"

urlpatterns = [
    path('', include(urls_evento)),
    path('', include(urls_artigo)),
    path('', include(urls_autor)),
    path('', include(urls_usuario)),
]
