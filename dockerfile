# Utilisation de Python 3.12 basé sur Alpine
FROM python:3.12-alpine

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances système
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Copier uniquement requirements.txt pour éviter de tout reconstruire à chaque changement de code
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Django
EXPOSE 8000

# Commande par défaut (remplacée par l'override de docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
