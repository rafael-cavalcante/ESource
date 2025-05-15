from django.shortcuts import render

def exibir_dashboard(request):
    return render(request, 'dashboard.html')