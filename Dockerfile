FROM python:3.10.18-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt и устанавливаем зависимости
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

# Копируем остальной код
COPY . /app

CMD ["python3", "app_api.py"]