# parser-pdf-OCR

Script em Python para processar PDFs OCR em lote e renomear automaticamente os arquivos com base em informações extraídas do conteúdo do arquivo.
O projeto utiliza a biblioteca [DocTR](https://github.com/mindee/doctr "Repositório DocTR") para extrair texto de documentos PDF OCR e aplica regras de parsing para identificar campos relevantes e padronizar o nome final do arquivo.

---

### 📦 Dependências do projeto

- Python 3.12+ (buildado em asdf python 3.12.0)
- Google Gemini API key (Free or Not-Free)

---

### Como rodar o projeto

**Clone este repositório:**
```
git clone https://github.com/GuilhermeeDev/parser-pdf-OCR.git
cd parser-pdf-OCR
```
**Instale as dependências:**
- Linux:
```
source ./setup-linux.sh
```

- Linux com ASDF:
```
source ./setup-linux-asdf.sh
```

- Windows:
```
cmd
```

```
.\setup-windows.bat
```

**Rode o projeto:**
Ative o ambiente virtual python gerado
Linux: 
```
source venv/bin/activate
```

```
python src/main.py
```


Windows:
```
.\venv\Scripts\Activate.bat
```

```
python.exe -m pip install --upgrade pip
```

```
pip install --no-cache-dir -r requirements.txt
```

Rode o projeto:
```
python .\src\main.py
```
---