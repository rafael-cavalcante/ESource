from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ESource.models import Evento, Artigo, Status, Autor
from ESource.utils.context import get_context_data

def autores(request):
    autores = Autor.objects.all()
    context = get_context_data({'autores': autores})
    
    return render(request, 'autores.html', context)

@login_required
def criar_autor(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        citacao = request.POST.get('citacao')

        Autor.objects.create(
            nome=nome,
            citacao=citacao
        )

        messages.success(request, f'Autor {nome} Cadastrado com Sucesso!')
        
        return redirect('ESource:autores')

    return render(request, 'autor/criar_autor.html')

@login_required
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)

    if request.method == "POST":
        autor.nome = request.POST.get('nome')
        autor.citacao = request.POST.get('citacao')

        autor.save()

        messages.success(request, f'Autor {autor.nome} Atualizado com Sucesso!')

        return redirect('ESource:autores')

    return render(request, 'autor/criar_autor.html', {'autor': autor})

@login_required
def excluir_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()

    messages.success(request, f'Autor {autor.nome} Deletado com Sucesso!')

    return redirect('ESource:autores')