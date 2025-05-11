from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ESource.models import Evento
from ESource.utils.context import get_context_data

def eventos(request):
    eventos = Evento.objects.filter(status='DISP')
    context = get_context_data({'eventos': eventos})

    return render(request, 'eventos.html', context)

@login_required
def criar_evento(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sigla = request.POST.get('sigla')
        data = request.POST.get('data')
        link = request.POST.get('link')

        try:
            data_evento = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            data_evento = None 

        evento = Evento.objects.create(
            nome=nome,
            sigla=sigla,
            data=data_evento,
            link=link
        )
        
        messages.success(request, f'Evento {evento.nome} Criado com Sucesso!')

        return redirect('ESource:eventos')  
    
    return render(request, 'evento/criar_evento.html')

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

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
        
        messages.success(request, f'Evento {evento.nome} Editado com Sucesso!')

        return redirect('ESource:eventos')

    context = {'evento': evento}

    return render(request, 'evento/criar_evento.html', context)

@login_required
def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    
    messages.success(request, f'Evento {evento.nome} Deletado com Sucesso!')

    return redirect('ESource:eventos')

@login_required
def arquivar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.status = 'ARQ'
    evento.save()

    messages.success(request, f'Evento {evento.nome} Arquivado com Sucesso!')

    return redirect('ESource:eventos')

@login_required
def desarquivar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.status = 'DISP'
    evento.save()

    messages.success(request, f'Evento {evento.nome} Desarquivado com Sucesso!')

    return redirect('ESource:listar_eventos_arquivados')

@login_required
def listar_eventos_arquivados(request):
    eventos_arquivados = Evento.objects.filter(status='ARQ')
        
    return render(request, 'evento/listar_eventos_arquivados.html', {'eventos_arquivados': eventos_arquivados})