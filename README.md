# Enoki
Test technique pour Enoki studio

## Ne pas oublier d'ajouter le fichier .env et le fichier users.csv
Ce dernier est à intégrer dans . /media/csv. Le "." représente la racine du projet.

## Initialisation de la base de données

> docker compose up -d db_postgresql

## Initialisation du projet

> docker compose up -d django

## Lancement des conteneurs une fois installée

Lors d'un - éventuel - rallumage des conteneurs, il n'est pas recommandé d'utiliser docker compose up. Le fichier start.sh permet d'allumer les conteneurs.

## Création des utilisateurs

> docker compose run django python manage.py create_user

L'api est accessible depuis localhost:8000/api

## Connexion à la partie admin

La partie admin est accessible depuis localhost:8000/admin. Le compte admin est Camomille / 123
