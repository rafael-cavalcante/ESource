from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def exibir_chatIA(request):
    return HttpResponse('Carregado ChatIA com sucesso!')
