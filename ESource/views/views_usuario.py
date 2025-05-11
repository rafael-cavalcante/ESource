from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
            return  redirect('ESource:artigos')
        else:
            messages.error(request, 'Conta não existe!')

    return render(request, 'conta/entrar.html')

@login_required
def sair(request):
    logout(request)
    return redirect('ESource:artigos')