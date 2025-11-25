# Utiliser Python slim pour ARM64
FROM python:3.11-slim

# Installer dépendances système + Tesseract avec langue française
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-fra \
    poppler-utils \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Définir la variable TESSDATA_PREFIX pour Tesseract
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le projet dans le container
COPY . /app

# Installer les packages Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5001

# Lancer Flask en utilisant le package app pour que les imports relatifs fonctionnent
CMD ["python", "-m", "app.main"]
