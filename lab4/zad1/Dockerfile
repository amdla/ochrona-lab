FROM ubuntu:latest

RUN apt update && apt install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html


CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80
