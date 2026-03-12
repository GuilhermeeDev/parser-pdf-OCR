#!/usr/bin/env bash

mkdir input/ output/

asdf install python 3.12.0
asdf local python 3.12.0

rm -rf venv/ env/ .venv/ .env/
python -m venv venv

source venv/bin/activate
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

cat > .env << EOF
API_GEMINI_KEY=
MODEL=gemini-2.5-flash
INPUT_PATH=$(realpath ./input)
OUTPUT_PATH=$(realpath ./output)
EOF