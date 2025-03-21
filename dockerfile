# Utilisation de Python 3.9 basé sur Alpine
FROM python:3.9-alpine

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du projet Django
COPY . .

# Exposer le port Django
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
