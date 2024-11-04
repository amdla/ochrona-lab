# Użyj oficjalnego obrazu Nginx
FROM nginx:latest

# Kopiuj konfigurację Nginx do obrazu
COPY nginx.conf /etc/nginx/nginx.conf

# Kopiuj statyczne pliki HTML do standardowego katalogu Nginx
COPY html /usr/share/nginx/html

# Nginx domyślnie nasłuchuje na porcie 80
EXPOSE 3000
