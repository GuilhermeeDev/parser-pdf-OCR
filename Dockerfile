FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV INPUT_PATH=/app/input
ENV OUTPUT_PATH=/app/output

CMD ["python", "main.py"]