from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ESource.models import Evento, Artigo, Status, Autor

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

def eventos(request):
    eventos = Evento.objects.filter(status='DISP')
    context = get_context_data({'eventos': eventos})

    return render(request, 'eventos.html', context)

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