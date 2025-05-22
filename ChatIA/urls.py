from django.urls import path
from . import views

app_name = "ChatIA"

urlpatterns = [
    path('chatia/', views.exibir_chatIA, name='chatia'),
    path('atualizar_csv_chatIA/', views.atualizar_csv_chatIA, name='atualizar_csv_chatIA'),
    path('chatia_response/', views.chatia_response, name='chatia_response'),
]