FROM python:3.13-slim

# Instala dependências do sistema necessárias para compilar pacotes Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libbz2-dev \
    libsqlite3-dev \
    libreadline-dev \
    libncursesw5-dev \
    curl \
    && apt-get clean

WORKDIR /app

# Copia dependências do projeto
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto
COPY ./src ./src
COPY ./main.py ./main.py
# COPY ./tests ./tests
COPY ./hypercorn.toml ./hypercorn.toml

# Expõe a porta usada pelo Hypercorn
EXPOSE 8000

# Usa Hypercorn como entrypoint
CMD ["hypercorn", "-c", "hypercorn.toml", "main:app"]
