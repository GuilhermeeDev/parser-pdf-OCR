FROM python:3.10.20-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]