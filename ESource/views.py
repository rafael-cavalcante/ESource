from django.shortcuts import render, get_object_or_404
from .models import Evento, Artigo

# Create your views here.

def index(request):
    artigos = Artigo.objects.all()
    totalArtigos = Artigo.objects.count()
    totalEventos = Evento.objects.count()
    context = {'artigos' : artigos, 'totalArtigos' : totalArtigos, 'totalEventos' : totalEventos}

    return render(request, 'index.html', context)

def eventos(request):
    eventos = Evento.objects.all()
    totalArtigos = Artigo.objects.count()
    totalEventos = Evento.objects.count()
    context = {'eventos' : eventos, 'totalArtigos' : totalArtigos, 'totalEventos' : totalEventos}

    return render(request, 'eventos.html', context)

def artigo(request):
    artigoId = request.GET.get('id')
    artigo = get_object_or_404(Artigo, id=artigoId)
    context = {'artigo' : artigo}

    return render(request, 'visualizarArtigo.html', context)