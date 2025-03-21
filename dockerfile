# Utilisation de Python 3.9 basé sur Alpine
FROM python:3.12-alpine

# Définition du répertoire de travail
WORKDIR /app


# Installation des dépendances
COPY requirements.txt .
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN pip install --no-cache-dir -r requirements.txt

# Copie du projet Django
COPY . .

# Exposer le port Django
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
