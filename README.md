# Enoki
Test technique pour Enoki studio

## Installation du projet
Initialisation de la base de données

docker compose up -d db_postgresql

## Initialisation du projet

docker compose up -d django

## Création des utilisateurs

docker compose run django python manage.py create_user

L'api est accessible depuis localhost:8000/api

## Connexion à la partie admin

La partie admin est accessible depuis localhost:8000/admin. Le compte admin est Camomille / 123