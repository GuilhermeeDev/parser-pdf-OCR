# parser-pdf-ocr no Notebook python

### Como rodar?

Ao abrir o projeto como pasta raiz no seu ambiente, execute o arquivo `setup-linux.sh` ou `setup-windows.bat`

Linux:
```
./setup-linux.sh
```

Windows:
```
.\setup-windows.bat
```

Adicione os arquivos .pdf na pasta input e em seguida ative o ambiente virtual python criado pelo script

Powershell
```
.\venv\Scripts\Activate.ps1
```
Ou
Terminal
```
venv\Scripts\activate.bat
```

Em seguida instale o jupyter notebook
```
pip install jupyterlab
```

Ative o ambiente com
```
jupyter lab
```

E acesse no seu navegador de preferencia
```
http://localhost:8888/lab
```

