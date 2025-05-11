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

def autores(request):
    autores = Autor.objects.all()
    context = get_context_data({'autores': autores})
    
    return render(request, 'autores.html', context)

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