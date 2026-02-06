# parser-pdf-OCR

Script em Python para processar PDFs OCR em lote e renomear automaticamente os arquivos com base em informações extraídas do conteúdo do arquivo.
O projeto utiliza a biblioteca [DocTR](https://github.com/mindee/doctr "Repositório DocTR") para extrair texto de documentos PDF OCR e aplica regras de parsing para identificar campos relevantes e padronizar o nome final do arquivo.

# 📦 Dependências do projeto

- Python 3.10+ (buildado em asdf python 3.10.0)
- doctr[viz] (CPU)

# Como rodar o projeto

#### 1️⃣ Rodando em Linux sem ASDF:
```
git clone https://github.com/GuilhermeeDev/parser-pdf-OCR.git
cd parser-pdf-OCR
```
**Instale as dependências:**
- Ubuntu sem ASDF:
```
source ./setup-linux.sh
```

- Ubuntu com ASDF:
```
source ./setup-linux-asdf.sh
```
**Rode o projeto:**
```
python3 main.py
```

