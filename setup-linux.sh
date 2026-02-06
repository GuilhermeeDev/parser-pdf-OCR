#!/usr/bin/env bash

# Esse Script precisa necessariamente dessas bibliotecas Python para rodar a biblioteca Doctr do projeto
sudo apt install -y libbz2-dev liblzma-dev libreadline-dev libsqlite3-dev libffi-dev libssl-dev zlib1g-dev libtk8.6 

rm -rf venv/ env/ .venv/ .env/
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt