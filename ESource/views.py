from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos' : eventos}

    return render(request, 'eventos.html', context)