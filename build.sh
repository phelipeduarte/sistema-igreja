#!/usr/bin/env bash
# Sair se der erro
set -o errexit

pip install -r requirements.txt

# Coletar os arquivos estáticos (CSS)
python manage.py collectstatic --no-input

# Criar as tabelas no banco de dados novo
python manage.py migrate