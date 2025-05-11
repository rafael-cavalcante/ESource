from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ESource.models import Evento, Artigo, Autor

from ESource.utils.context import get_context_data

# Create your views here.
def artigos(request):
    artigos = Artigo.objects.filter(status='DISP')
    context = get_context_data({'artigos': artigos})
    
    return render(request, 'artigos.html', context)

def exibir_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    return render(request, 'artigo/exibir_artigo.html', {'artigo': artigo})

@login_required
def criar_artigo(request):
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

        artigo = Artigo.objects.create(
            titulo=titulo,
            autor=autor,
            subAreas=subAreas,
            dataPublicacao=data_publicacao,
            link=link,
            conteudo=conteudo,
            evento=evento
        )
        
        messages.success(request, f'Artigo {artigo.titulo} Criado com Sucesso!')

        return redirect('ESource:artigos')

    eventos = Evento.objects.filter(status='DISP')
    autores = Autor.objects.all()
    
    context = {'eventos' : eventos, 'autores' : autores}

    return render(request, 'artigo/criar_artigo.html', context)

@login_required
def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

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
        
        messages.success(request, f'Artigo {artigo.titulo} Editado com Sucesso!')

        return redirect('ESource:artigos')

    eventos = Evento.objects.filter(status='DISP')
    autores = Autor.objects.all()
    
    context = {'artigo' : artigo, 'eventos' : eventos, 'autores' : autores}

    return render(request, 'artigo/criar_artigo.html', context)

@login_required
def excluir_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    artigo.delete()
    
    messages.success(request, f'Artigo {artigo.titulo} Deletado com Sucesso!')

    return redirect('ESource:artigos')

@login_required
def arquivar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    artigo.status = 'ARQ'
    artigo.save()

    messages.success(request, f'Artigo {artigo.titulo} Arquivado com Sucesso!')

    return redirect('ESource:artigos')

@login_required
def desarquivar_artigo(request, artigo_id):
    '''artigo = get_object_or_404(Artigo, id=artigo_id)
    artigo.status = 'DISP'
    artigo.save()

    messages.success(request, f'Artigo {artigo.titulo} Desarquivado com Sucesso!')'''
    
    try:
        artigo = Artigo.objects.get(id=artigo_id)
        artigo.status = 'DISP'
        artigo.save()
        
        messages.success(request, f'Artigo {artigo.titulo} Desarquivado com Sucesso!')
    except Artigo.DoesNotExist:
        
        messages.error(request, 'Artigo não encontrado.')

    return redirect('ESource:listar_artigos_arquivados')

@login_required
def listar_artigos_arquivados(request):
    artigos_arquivados = Artigo.objects.filter(status='ARQ')
        
    return render(request, 'artigo/listar_artigos_arquivados.html', {'artigos_arquivados': artigos_arquivados})