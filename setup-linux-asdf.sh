#!/usr/bin/env bash

asdf uninstall python 3.10.0
# Esse Script precisa necessariamente dessas bibliotecas Python para rodar a biblioteca Doctr do projeto
sudo apt install -y libbz2-dev liblzma-dev libreadline-dev libsqlite3-dev libffi-dev libssl-dev zlib1g-dev libtk8.6 

asdf install python 3.10.0
asdf global python 3.10.0
rm -rf venv/ env/ .venv/ .env/
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt