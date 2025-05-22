import csv
import os

from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, StreamingHttpResponse

from django.contrib.auth.decorators import login_required

import google.generativeai as genai

from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

from ESource.models import Artigo 

genai.configure(api_key=settings.GEMINI_API_KEY)

# Create your views here.
def exibir_chatIA(request):
    return render(request, 'chat_ia.html')    

@login_required
def atualizar_csv_chatIA(request):
    # Cria diretório "source" se não existir
    output_dir = os.path.join(settings.BASE_DIR, 'ChatIA','source')
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
            
    messages.success(request, f'Base de dados ChatIA Atualiza com Sucesso!')

    return redirect('ESource:artigos')

# 🤖 Função que interage com o modelo Gemini
def chatia_response(request):
    user_message = request.GET.get("message", "")

    if not user_message:
        return JsonResponse({"error": "Nenhuma mensagem recebida."}, status=400)

    # 🔍 Busca no FAISS
    retrieved_docs = retriever.invoke(user_message) if retriever else []
    context = "\n".join([doc.page_content for doc in retrieved_docs]) if retrieved_docs else "Nenhuma informação encontrada."

    # 📝 Monta o prompt final para o modelo
    final_prompt = prompt.format(context=context, question=user_message)

    def stream_response():
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                final_prompt, stream=True
            )  # 🔹 Ativa streaming

            for chunk in response:
                content = chunk.text
                if content:
                    yield content  # 🔹 Retorna o texto diretamente

        except Exception as e:
            yield f"Erro: {str(e)}"

    return StreamingHttpResponse(stream_response(), content_type="text/plain")

# 🔍 Função para carregar e indexar o CSV no FAISS
def carregar_base():
    try:
        loader = CSVLoader(file_path=os.path.join(settings.BASE_DIR, 'ChatIA', 'source', 'dados_fontes.csv'))
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=settings.GEMINI_API_KEY)
        documents = loader.load()
        vectorstore = FAISS.from_documents(documents, embeddings)
        retriever_local = vectorstore.as_retriever()
        if not retriever_local:
            print("⚠️ O vetor de busca FAISS não foi carregado corretamente. Verifique o CSV ou as credenciais da API.")

        return retriever_local
    except Exception as e:
        print(f"Erro ao carregar FAISS: {e}")
        return None

retriever = carregar_base()

rag_template = """
Você é um gerente de um portal de Artefatos Engenharia de Software.
Seu trabalho é conversar com os usuarios, consultando a base de 
conhecimentos do portal, e dar 
uma resposta simples e precisa para ele, baseada na 
base de dados do portal fornecida como 
contexto.

📌 **Contexto disponível**:
{context}

💬 **Pergunta do cliente**:
{question}

Responda de forma clara e objetiva.
"""
prompt = ChatPromptTemplate.from_template(rag_template)