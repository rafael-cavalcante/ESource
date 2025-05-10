from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Artigo, Status

# Create your views here.
def home(request):
    artigos = Artigo.objects.all()
    totalArtigos = Artigo.objects.count()
    totalEventos = Evento.objects.count()
    statusEvento = Status.objects.filter(modelo='Evento').latest('atualizado')
    statusArtigo = Status.objects.filter(modelo='Artigo').latest('atualizado')
    context = {'artigos' : artigos, 'totalArtigos' : totalArtigos, 'totalEventos' : totalEventos, 'statusEvento' : statusEvento, 'statusArtigo' : statusArtigo}

    return render(request, 'home.html', context)

def entrar(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Por favor preencha username e password!')
            return render(request, 'conta/entrar.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return  redirect('ESource:home')
        else:
            messages.error(request, 'Usuario não existe!')

    return render(request, 'conta/entrar.html')

def sair(request):
    logout(request)
    return redirect('ESource:home')

def eventos(request):
    eventos = Evento.objects.all()
    totalArtigos = Artigo.objects.count()
    totalEventos = Evento.objects.count()
    statusEvento = Status.objects.filter(modelo='Evento').latest('atualizado')
    statusArtigo = Status.objects.filter(modelo='Artigo').latest('atualizado')
    context = {'eventos' : eventos, 'totalArtigos' : totalArtigos, 'totalEventos' : totalEventos, 'statusEvento' : statusEvento, 'statusArtigo' : statusArtigo}

    return render(request, 'eventos.html', context)

def visualizarArtigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)
    context = {'artigo' : artigo}

    return render(request, 'visualizarArtigo.html', context)

@login_required
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

        return redirect('ESource:home')

    eventos = Evento.objects.all()
    context = {'eventos' : eventos}

    return render(request, 'cadastrarArtigo.html', context)

@login_required
def atualizarArtigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)

    if request.method == "POST":
        artigo.titulo = request.POST.get('titulo')
        artigo.autor = request.POST.get('autor')
        artigo.subAreas = request.POST.get('subAreas')
        data = request.POST.get('dataPublicacao')
        artigo.link = request.POST.get('link')
        artigo.conteudo = request.POST.get('conteudo')

        # Converte a data
        try:
            data_publicacao = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_publicacao = None

        # Lida com a imagem (salvando só o nome ou caminho, simplificado)
        imagem_file = request.FILES.get('imagem')
        imagem_path = imagem_file.name if imagem_file else artigo.imagem

        artigo.dataPublicacao = data_publicacao
        artigo.imagem = imagem_path

        evento_id = request.POST.get('evento')
        evento = Evento.objects.get(id=evento_id) if evento_id else None
        artigo.evento = evento

        artigo.save()

        return redirect('ESource:home')

    eventos = Evento.objects.all()
    context = {'artigo' : artigo, 'eventos' : eventos}

    return render(request, 'cadastrarArtigo.html', context)

def deletarArtigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)
    artigo.delete()

    return redirect('ESource:home')

@login_required
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

@login_required
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

@login_required
def deletarEvento(request, eventoId):
    evento = get_object_or_404(Evento, id=eventoId)
    evento.delete()

    return redirect('ESource:eventos')