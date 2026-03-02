from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import re
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

def parseia_string(result):
    """
    - Recebe a string completa retornada pelo OCR e extrai: Nome, Data e Numero
    - Substitui todas as "/" por "."
    - Monta o nome do arquivo: "PGTO_N° <Numero> - [<Data>] - (<Nome>).pdf"
    """
    nome , data, numero = None, None, None
    linhas = []

    for linha in result.splitlines():
        if len(linhas) < 25:
            if linha.strip():
                linhas.append(linha.strip())

    for i, linha in enumerate(linhas):
        # Nome: Procura pelo antecessor das palavras-chave
        if nome is None and i > 0 and any(p in linhas[i - 2].upper() for p in PALAVRAS_CHAVE_NOME):
            nome = linha
            continue

        # Data
        if data is None and _data.search(linha):
            data = _data.search(linha).group()
            continue

        # Número: geralmente vem logo após o rótulo "NUMERO" ou após a data
        if numero is None and _numero.match(linha) and i > 0 and any(p in linhas[i - 2].upper() for p in PALAVRAS_CHAVE_NUMERO) or numero is None and _numero.match(linha) and i > 0 and any(p in linhas[i - 3].upper() for p in PALAVRAS_CHAVE_NUMERO):
            numero = linha
            continue
    
    nome = nome.replace("/", ".") if nome else "Nao_encontrado"
    data =  data.replace("/", ".") if data else "Nao_encontrado"
    numero = numero if numero else "Nao_encontrado"
    novo_nome=f"PGTO_N° {numero} - [{data}] - ({nome}).pdf"

    return novo_nome

# --- COMEÇO ---
print("Carregando modelo OCR...")
predictor = ocr_predictor(pretrained=True)

input_path = os.getenv("INPUT_PATH", "/app/input")
output_path = os.getenv("OUTPUT_PATH", "/app/output")
INPUT = Path(input_path)
OUTPUT = Path(output_path)

lista_arquivos = list(INPUT.glob("*.pdf"))

# --- Palavras de Busca ---
PALAVRAS_CHAVE_NUMERO = ["NUMERO", "NÚMERO"]
PALAVRAS_CHAVE_NOME = ["Razao Social/Forecedor","Razao Social.Forecedor","FORNECEDOR", "RAZAO SOCIAL"]

# --- Regex ---
_data = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
_numero = re.compile(r"^\d+$")

print("Processando arquivos... aguarde...")
for arq in lista_arquivos:
    nome_arquivo = arq.name
    doc = DocumentFile.from_pdf(arq)
    resul = predictor(doc[:1])
    string_result = resul.render()
    novo_nome = parseia_string(string_result)
    _arquivo = arq.with_name(novo_nome)
    arq.rename(_arquivo)
    print(f"{nome_arquivo}  -->  {novo_nome}")
    
    if "nao_encontrado" in _arquivo.name.lower():
        continue  
    # _arquivo.rename(OUTPUT / _arquivo.name)
    shutil.move(str(_arquivo), OUTPUT / _arquivo.name)