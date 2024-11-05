FROM ubuntu:latest

# w ubuntu i tak nie ma inputow wiec mozna taki system wziac
ENV DEBIAN_FRONTEND=noninteractive

# dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# to jest po to zeby byly jakby dwa pythony, to co pan pokazywal u siebie
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN /opt/venv/bin/pip install --no-cache-dir flask uwsgi

# kopiowanie konfiguracji nginxa i uwsgi
COPY nginx.conf /etc/nginx/nginx.conf
COPY app/uwsgi.ini /app/uwsgi.ini

# to kopiuje pliki z folderu zeby byl ten kod z pythona
COPY app /app

# set working directory
WORKDIR /app

# ustaw port
# to CHYBA nie jest potrzebne, skoro dajemy porty jako input ale lepiej nie psuc
EXPOSE 5000

# odpala uwsgi i nginxa
CMD ["sh", "-c", "service nginx start && /opt/venv/bin/uwsgi --ini /app/uwsgi.ini"]
