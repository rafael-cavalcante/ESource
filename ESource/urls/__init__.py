from django.urls import include, path
from . import urls_evento, urls_artigo, urls_autor, urls_usuario, urls_dashboard

app_name = "ESource"

urlpatterns = [
    path('', include(urls_evento)),
    path('', include(urls_artigo)),
    path('', include(urls_autor)),
    path('', include(urls_usuario)),
    path('', include(urls_dashboard)),
]