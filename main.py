from google import *
from dotenv import load_dotenv
import google.generativeai as genai
import time
import json
import os
import re
from pathlib import Path
load_dotenv()

# --- VARIAVEIS DE AMBIENTE ---
GOOGLE_API_KEY = os.getenv("API_GEMINI_KEY")
MODEL = os.getenv("MODEL")
INPUT = Path(os.getenv("INPUT_PATH"))
OUTPUT = Path(os.getenv("OUTPUT_PATH"))

genai.configure(api_key=GOOGLE_API_KEY)

def limpar_nome_arquivo(texto):
    """
    Remove caracteres que o Windows/Linux/macOS não permitem em nomes de arquivos.
    """
    nome = texto.strip().replace('\n', ' ').replace('\r', '')
    nome = re.sub(r'[\\/*?:"<>|]', '_', nome)
    return nome

def gemini_parse_pdf(file):
    print(f"Fazendo upload do arquivo: {file}...")
    sample_file = genai.upload_file(path=file, display_name="Documento pdf para OCR")

    # 3. Aguardar o processamento do arquivo pelo Google
    while sample_file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        sample_file = genai.get_file(sample_file.name)

    if sample_file.state.name == "FAILED":
        raise Exception("Falha no processamento do arquivo.")

    model = genai.GenerativeModel(model_name=MODEL)
    
    prompt = """
    Analise este documento PDF. 
    1. Realize o OCR de todo o texto visível.
    2. Extraia os dados principais (Razão social/Fornecedor, Data do cabeçalho, Número de documento).
    3. Se os itens do item 2. foram extraidos com sucesso, despreze o restante dos dados do documento.
    4. Formate a saida de dados para que seja respondido somente "PGTO_N° <Número de documento> - [<Data do cabeçalho>] - (<Razão social/Fornecedor>).pdf"
    5. Substitua todos os caracteres ("/, \, :, *, ?, ", <, >, |, \n") presentes na saida formata por "." (ponto).
    6. Responda somente a saida formatada
    """
    
    response = model.generate_content([sample_file, prompt])
    return response.text

# --- Execução ---
if __name__ == "__main__":
    
    # PASTA DE ENTRADA E SAIDA DE ARQUIVOS .pdf
    arquivos = list(INPUT.glob("*.pdf"))
    
    for arq in arquivos:
        try:
            nome_arquivo = arq.name
            result = gemini_parse_pdf(arq)
            novo_nome = limpar_nome_arquivo(result)
            _arquivo = arq.with_name(novo_nome)
            arq.rename(_arquivo)
            print(f"\n {nome_arquivo}  -->  {novo_nome}")
            _arquivo.rename(OUTPUT / _arquivo.name)
                
        except Exception as e:
            print(f"\nErro: {e}")