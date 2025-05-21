from django.urls import path
from . import views

urlpatterns = [
    path('chatia/', views.exibir_chatIA, name='chatia'),
]