FROM ubuntu:latest

RUN apt update && apt install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html


CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80

# ustaw ubuntu jako system, pobierz nginxa, skopiuj pliki konfiguracyjne i index.html,
# uruchom nginx, otwórz port 80
# w tym przypadku plik index.html wygenerowany przez nginxa ZASTĘPUJEMY naszym index.html
# alternatywnie moglibyśmy wejść do kontenera i ręcznie zmienić plik index.html 
# docker build -t zad1 .
# docker run -d -it -p 80:80 zad1
# docker exec -it <nazwa od dockera / id> bash
# i tam sobie wejsc do /usr/share/nginx/html/ i zmienic index.html
# tylko wczesniej trzeba sudo apt install vim