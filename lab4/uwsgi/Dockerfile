# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to avoid interactive installation issues
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
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

# Set up a virtual environment for Python dependencies
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Flask and uWSGI in the virtual environment
RUN /opt/venv/bin/pip install --no-cache-dir flask uwsgi

# Copy Nginx and uWSGI configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY app/uwsgi.ini /app/uwsgi.ini

# Copy the app directory containing app2.py
COPY app /app

# Set the working directory to /app
WORKDIR /app

# Expose port 5000 for Nginx (or any other port you'd like to expose)
EXPOSE 5000

# Start Nginx and uWSGI using JSON notation
CMD ["sh", "-c", "service nginx start && /opt/venv/bin/uwsgi --ini /app/uwsgi.ini"]
