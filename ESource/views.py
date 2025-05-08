from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
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

def cadastrarArtigo(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        subAreas = request.POST.get('subAreas')
        data = request.POST.get('dataPublicacao')
        link = request.POST.get('link')
        conteudo = request.POST.get('conteudo')
        evento_id = request.POST.get('evento')
        imagem_file = request.FILES.get('imagem')

        # Converte a data
        try:
            data_publicacao = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_publicacao = None

        # Lida com a imagem (salvando só o nome ou caminho, simplificado)
        imagem_path = imagem_file.name if imagem_file else ''

        evento = Evento.objects.get(id=evento_id) if evento_id else None

        Artigo.objects.create(
            titulo=titulo,
            autor=autor,
            subAreas=subAreas,
            dataPublicacao=data_publicacao,
            link=link,
            imagem=imagem_path,
            conteudo=conteudo,
            evento=evento
        )

        return redirect('ESource:index')

    eventos = Evento.objects.all()
    context = {'eventos' : eventos}

    return render(request, 'cadastrarArtigo.html', context)

def cadastrarEvento(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sigla = request.POST.get('sigla')
        data = request.POST.get('data')
        link = request.POST.get('link')

        try:
            data_evento = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_evento = None  # ou lidar com erro

        Evento.objects.create(
            nome=nome,
            sigla=sigla,
            data=data_evento,
            link=link
        )

        return redirect('ESource:eventos')  # ou outra view de sucesso

    return render(request, 'cadastrarEvento.html')

def atualizarEvento(request, eventoId):
    evento = get_object_or_404(Evento, id=eventoId)

    if request.method == "POST":
        evento.nome = request.POST.get('nome')
        evento.sigla = request.POST.get('sigla')
        data = request.POST.get('data')
        evento.link = request.POST.get('link')

        try:
            data_evento = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_evento = None  # ou lidar com erro

        evento.data = data_evento

        evento.save()

        return redirect('ESource:eventos')

    context = {'evento': evento}

    return render(request, 'cadastrarEvento.html', context)

def deletarEvento(request, eventoId):
    evento = get_object_or_404(Evento, id=eventoId)
    evento.delete()

    return redirect('ESource:eventos')