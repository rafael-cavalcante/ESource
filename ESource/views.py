'''from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Artigo, Status, Autor

# Create your views here.
def get_context_data(extra_context=None):
    context = {
        'totalArtigos': Artigo.objects.filter(status='DISP').count,
        'totalEventos': Evento.objects.filter(status='DISP').count,
        'totalAutores': Autor.objects.count(),
        'statusEvento': Status.objects.filter(modelo='Evento').order_by('-atualizado').first(),
        'statusArtigo': Status.objects.filter(modelo='Artigo').order_by('-atualizado').first(),
        'statusAutor': Status.objects.filter(modelo='Autor').order_by('-atualizado').first(),
    }
    if extra_context:
        context.update(extra_context)
    return context

# Artigo views
def artigos(request):
    artigos = Artigo.objects.filter(status='DISP')
    context = get_context_data({'artigos': artigos})
    
    return render(request, 'artigos.html', context)

def eventos(request):
    eventos = Evento.objects.filter(status='DISP')
    context = get_context_data({'eventos': eventos})

    return render(request, 'eventos.html', context)

def autores(request):
    autores = Autor.objects.all()
    context = get_context_data({'autores': autores})
    
    return render(request, 'autores.html', context)

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

        # Converte a data
        try:
            data_publicacao = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_publicacao = None

        evento = Evento.objects.get(id=evento_id) if evento_id else None

        Artigo.objects.create(
            titulo=titulo,
            autor=autor,
            subAreas=subAreas,
            dataPublicacao=data_publicacao,
            link=link,
            conteudo=conteudo,
            evento=evento
        )

        return redirect('ESource:home')

    eventos = Evento.objects.all()
    autores = Autor.objects.all()
    context = {'eventos' : eventos, 'autores' : autores}

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

        artigo.dataPublicacao = data_publicacao

        evento_id = request.POST.get('evento')
        evento = Evento.objects.get(id=evento_id) if evento_id else None
        artigo.evento = evento
        
        autores_ids = request.POST.getlist("autores")
        artigo.autores.set(autores_ids)

        artigo.save()

        return redirect('ESource:home')

    eventos = Evento.objects.all()
    autores = Autor.objects.all()
    context = {'artigo' : artigo, 'eventos' : eventos, 'autores' : autores}

    return render(request, 'cadastrarArtigo.html', context)

@login_required
def deletarArtigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)
    artigo.delete()
    
    messages.success(request, f'Artigo {artigo.titulo} Deletado com Sucesso!')

    return redirect('ESource:home')

#Modulo de Arquivamento Artigos
@login_required
def arquivar_artigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)
    artigo.status = 'ARQ'
    artigo.save()

    messages.success(request, f'Artigo {artigo.titulo} Arquivado com Sucesso!')

    return redirect('ESource:artigos')

@login_required
def desarquivar_artigo(request, artigoId):
    artigo = get_object_or_404(Artigo, id=artigoId)
    artigo.status = 'DISP'
    artigo.save()

    messages.success(request, f'Artigo {artigo.titulo} Desarquivado com Sucesso!')

    return redirect('ESource:listar_artigos_arquivados')

@login_required
def listar_artigos_arquivados(request):
    artigos_arquivados = Artigo.objects.filter(status='ARQ')
        
    return render(request, 'artigo/listar_artigos_arquivados.html', {'artigos_arquivados': artigos_arquivados})

#Modulo de Arquivamento Eventos
@login_required
def arquivar_evento(request, eventoId):
    evento = get_object_or_404(Evento, id=eventoId)
    evento.status = 'ARQ'
    evento.save()

    messages.success(request, f'Evento {evento.nome} Arquivado com Sucesso!')

    return redirect('ESource:eventos')

@login_required
def desarquivar_evento(request, eventoId):
    evento = get_object_or_404(Evento, id=eventoId)
    evento.status = 'DISP'
    evento.save()

    messages.success(request, f'Evento {evento.nome} Desarquivado com Sucesso!')

    return redirect('ESource:listar_eventos_arquivados')

@login_required
def listar_eventos_arquivados(request):
    eventos_arquivados = Evento.objects.filter(status='ARQ')
        
    return render(request, 'evento/listar_eventos_arquivados.html', {'eventos_arquivados': eventos_arquivados})

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
    
    messages.success(request, f'Evento {evento.nome} Deletado com Sucesso!')

    return redirect('ESource:eventos')

# CRUD DE AUTOR
# Cadastrar Autor
@login_required
def cadastrarAutor(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        citacao = request.POST.get('citacao')

        Autor.objects.create(
            nome=nome,
            citacao=citacao
        )

        messages.success(request, f'Autor {nome} Cadastrado com Sucesso!')
        
        return redirect('ESource:autores')

    return render(request, 'cadastrarAutor.html')

# Atualizar Autor
@login_required
def atualizarAutor(request, autorId):
    autor = get_object_or_404(Autor, id=autorId)

    if request.method == "POST":
        autor.nome = request.POST.get('nome')
        autor.citacao = request.POST.get('citacao')

        autor.save()

        messages.success(request, f'Autor {autor.nome} Atualizado com Sucesso!')

        return redirect('ESource:autores')

    return render(request, 'cadastrarAutor.html', {'autor': autor})

# Deletar Autor
@login_required
def deletarAutor(request, autorId):
    autor = get_object_or_404(Autor, id=autorId)
    autor.delete()

    messages.success(request, f'Autor {autor.nome} Deletado com Sucesso!')

    return redirect('ESource:autores')

# Login and Logout views
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
            messages.error(request, 'Conta não existe!')

    return render(request, 'conta/entrar.html')

def sair(request):
    logout(request)
    return redirect('ESource:home')
    
'''