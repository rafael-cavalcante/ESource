from django.urls import path, include

urlpatterns = [
    path('', include('ESource.urls.urls_artigo')),
    path('', include('ESource.urls.urls_evento')),
    path('', include('ESource.urls.urls_autor')),
    path('', include('ESource.urls.urls_usuario')),
]