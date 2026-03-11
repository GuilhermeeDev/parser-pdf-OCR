@echo off
setlocal

REM Diretório onde o .bat está localizado
set BASE_DIR=%~dp0

REM Remove barra invertida final (caso exista)
if "%BASE_DIR:~-1%"=="\" set BASE_DIR=%BASE_DIR:~0,-1%

REM Define caminhos absolutos
set INPUT_DIR=%BASE_DIR%\input
set OUTPUT_DIR=%BASE_DIR%\output
set VENV_DIR=%BASE_DIR%\venv

echo.
echo ===== Criando estrutura de pastas =====

REM Cria pastas se não existirem
if not exist "%INPUT_DIR%" (
    mkdir "%INPUT_DIR%"
    echo Pasta input criada.
)

if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
    echo Pasta output criada.
)

echo.
echo ===== Gerando arquivo .env =====

(
echo INPUT_PATH=%INPUT_DIR%
echo OUTPUT_PATH=%OUTPUT_DIR%
) > "%BASE_DIR%\.env"

echo Arquivo .env criado com sucesso.

echo.
echo ===== Criando ambiente virtual Python =====

REM Verifica se python está disponível
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python nao encontrado no PATH.
    echo Instale o Python e marque a opcao "Add Python to PATH".
    pause
    exit /b
)

REM Cria o venv se nao existir
if not exist "%VENV_DIR%" (
    python -m venv "%VENV_DIR%"
    echo Ambiente virtual criado.
) else (
    echo Ambiente virtual ja existe.
)

echo.
echo ===== Ativando ambiente virtual =====

echo.
echo Setup concluido com sucesso!

endlocal
pause