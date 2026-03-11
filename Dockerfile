FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-por \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# python3.10 \
# python3-pip \
# python3.10-venv \
# libbz2-dev \
# liblzma-dev \
# libreadline-dev \ 
# libsqlite3-dev \
# libffi-dev \
# libssl-dev \
# zlib1g-dev \
# libtk8.6 \
# && apt-get clean \
