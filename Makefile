.PHONY: install format check-format lint check-all test cov requirements run

# Instala as dependências do projeto com Poetry
install:
	poetry install

# Formata todos os arquivos com Black
format:
	poetry run black .
	poetry run ruff check . --fix

# Verifica se o código está formatado corretamente
check-format:
	poetry run black --check .
	poetry run ruff check .

# Verifica problemas de lint (estilo, bugs, etc)
lint:
	poetry run ruff check .

# Realiza todas as verificações de estilo e formatação
check-all: check-format

# Executa os testes com detalhamento
test:
	poetry run pytest tests/ -v

# Executa os testes com relatório de cobertura
cov:
	poetry run pytest tests/ -v --cov=./src

# Exporta o requirements.txt para uso em produção (ex: Docker)
requirements:
	poetry export -f requirements.txt --without-hashes --output requirements.txt

# Executa a aplicação usando Hypercorn com configurações definidas no TOML
run:
	poetry run hypercorn -c hypercorn.toml main:server.app
