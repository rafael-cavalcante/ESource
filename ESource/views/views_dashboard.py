import csv
import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required

from ESource.models import Artigo

def exibir_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gerar_csv_artigos(request):
    # Cria diretório "source" se não existir
    output_dir = os.path.join(settings.BASE_DIR, 'ESource','source')
    os.makedirs(output_dir, exist_ok=True)

    # Caminho completo do arquivo
    filepath = os.path.join(output_dir, 'dados_fontes.csv')

    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'titulo_artigo',
            'ano_publicacao',
            'nomes_autores',
            'instituicoes_autores',
            'unidades_federativas_autores',
            'sub_areas',
            'link'
        ])

        for artigo in Artigo.objects.filter(status='DISP'):
            autores = artigo.autores.all()

            nomes = ','.join(autor.nome or '' for autor in autores)
            instituicoes = ','.join(autor.instituicao or '' for autor in autores)
            ufs = ','.join(autor.unidade_federativa or '' for autor in autores)

            ano = artigo.dataPublicacao.year if artigo.dataPublicacao else ''

            writer.writerow([
                artigo.titulo or '',
                ano,
                nomes,
                instituicoes,
                ufs,
                artigo.subAreas or '',
                artigo.link or ''
            ])
            
    messages.success(request, f'Base de dados Dashboard Atualiza com Sucesso!')

    return redirect('ESource:artigos')