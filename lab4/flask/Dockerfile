# Używamy obrazu Ubuntu
FROM ubuntu:latest

# Aktualizacja i instalacja pakietów
RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

# Utworzenie i aktywacja wirtualnego środowiska oraz instalacja Flask
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install flask

# Konfiguracja Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Skopiuj aplikację Flask
COPY app /app

# Ustawienie katalogu roboczego
WORKDIR /app

# Uruchamiamy serwer Flask i Nginx
CMD ["sh", "-c", "service nginx start && python app.py"]
