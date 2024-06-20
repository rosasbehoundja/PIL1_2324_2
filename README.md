# Site de rencontre avec Django, HTML, CSS et Javascript _____ PIL1_2324_2 

## Contexte
  Chaque année, l'Institut de Formation et de Recherche en Informatique (IFRI) de l'Université Publique d'Abomey-Calavi soumet soumet un défi aux étudiants de Licence 1 en fin d'anéee. Le projet de cette année consiste à réaliser un service de rencontres en ligne sous la forme d’une application web en 4 semaines.
Le développement de cette application nous a permis de mettre en oeuvre et d'étendre nos connaissances du framework Django et de sa logique. Le style de l'application a été fait à l'aide de Bootstrap5.
Afin de la rendre plus facilement testable, le repository contient la base de données, la Secret Key Django, ainsi que des informations de connexions. Les instructions de déploiement ont été rajoutées un peu plus bas sur le dépôt.

# You_Me App

![Logo du Projet](./You_Me.jpg)

## Fonctionnalités

- **Inscription et Connexion** : Les utilisateurs peuvent s'inscrire et se connecter pour accéder à la plateforme.
- **Profil Utilisateur** : Chaque utilisateur a un profil où il peut gérer ses informations personnelles.
- **Messagerie Instantanée** : Discutez avec d'autres utilisateurs en temps réel.
- **Liste des Discussions** : Visualisez et accédez rapidement à vos discussions récentes.
- **Suggestions de Profils** : Découvrez et connectez-vous avec de nouveaux utilisateurs.
- **Dashboard Administrateur** : Accédez à un interface administrateur si vous y êtes autorisés.

## Installation

- [Python 3.9](https://www.python.org/downloads/)
- [Django 4.2.13](https://www.djangoproject.com/)
- Autres dépendances listées dans `requirements.txt`

  ### Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/rosasbehoundja/PIL1_2324_2.git
    ```
2. Naviguez dans le répertoire du projet :
    ```bash
    cd PIL1_2324_2
    ```
3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
4. Appliquez les migrations :
    ```bash
    python manage.py migrate
    ```
5. Démarrez le serveur de développement :
    ```bash
    python manage.py runserver
    ```
