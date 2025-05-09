# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo o restante da aplicação
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta usada pelo gunicorn
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "ESource.wsgi:application", "--bind", "0.0.0.0:8000"]