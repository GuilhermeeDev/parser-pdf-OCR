#!/usr/bin/env bash

mkdir input/ output/
rm -rf venv/ env/ .venv/ .env/
python -m venv venv

source venv/bin/activate
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

cat > .env << EOF
API_GEMINI_KEY= # Acesse https://aistudio.google.com
MODEL=gemini-2.5-flash
INPUT_PATH=$(realpath ./input)
OUTPUT_PATH=$(realpath ./output)
EOF