# Site de rencontre avec Django, HTML, CSS et Javascript _____ PIL1_2324_2 

## Contexte
  Chaque année, l'Institut de Formation et de Recherche en Informatique (IFRI) de l'Université Publique d'Abomey-Calavi soumet soumet un défi aux étudiants de Licence 1 en fin d'anéee. Le projet de cette année consiste à réaliser un service de rencontres en ligne sous la forme d’une application web en 4 semaines.
Le développement de cette application nous a permis de mettre en oeuvre et d'étendre nos connaissances du framework Django et de sa logique. Le style de l'application a été fait à l'aide de Bootstrap5.
Afin de la rendre plus facilement testable, le repository contient la base de données, la Secret Key Django, ainsi que des informations de connexions. Les instructions de déploiement ont été rajoutées un peu plus bas sur le dépôt.

# You_Me App

![Logo du Projet](./You_Me.jpg)

## Fonctionnalités

- **Inscription et Connexion** : Les utilisateurs peuvent s'inscrire et se connecter pour accéder à la plateforme.
- **Récupération de mot de passe** : Les utilisateurs peuvent récuperer leurs mots de passe en cas d'oubli.
- **Profil Utilisateur** : Chaque utilisateur a un profil où il peut gérer ses informations personnelles.
- **Messagerie Instantanée** : Discutez avec d'autres utilisateurs en temps réel.
- **Liste des Discussions** : Visualisez et accédez rapidement à vos discussions récentes.
- **Suggestions de Profils** : Découvrez et connectez-vous avec de nouveaux utilisateurs grâce à un superbe algorithme de matchmaking.
- **Dashboard Administrateur** : Accédez à un interface administrateur si vous y êtes autorisés.

## Installation

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- Autres dépendances listées dans `requirements.txt`

  ### Installation
1. Créer un dossier puis y accéder dans l'éditeur de code : 

2. Créer et Activer un environnement virtuel : 
    - Sous Windows :
        ```sh
        python -m venv mon_env
        .\mon_env\Scripts\activate
        ```
    - Sous Linux :
        ```sh
        python3 -m venv mon_env
        source mon_env/bin/activate
        ```
3. Cloner le dépôt :
    ```bash
    (mon_env) git clone https://github.com/rosasbehoundja/PIL1_2324_2.git
    ```
4. Naviguer dans le répertoire du projet :
    ```bash
    (mon_env) cd PIL1_2324_2
    ```
5. Installer les dépendances :
    ```bash
    (mon_env) pip install -r requirements.txt
    ```
6. Configurer la base de données dans le fichier [settings.py](PIL1_2324_2/settings.py) :
    - Utilisation de SQLite :
      ```bash 
       DATABASES = {
          'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
      ```
  - Utilisation de MySQL : 
      ```bash
      DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'your_db_host',  # Set to 'localhost' or '127.0.0.1' for local development
          'PORT': '3306',          # Default port for MySQL
          }
    }
        ```
7. AppliqueR les migrations :
    ```bash
    (mon_env) python manage.py makemigrations
    (mon_env) python manage.py migrate
    ```
8. (Optionnel) ImporteR dans la base de données les infos de 2000 utilisateurs prédéfinis : 
    ```bash
    (mon_env) python manage.py import_users
    (mon_env) python manage.py import_hobbies
    ```
9. Créer un superutilisateur :
    ```bash
    (mon_env) python manage.py createsuperuser
    ```
10. Démarrer le serveur de développement :
    ```bash
    (mon_env) python manage.py runserver
    ```

## Utilisation

L'application est facile d'utilisation.

### Inscription et Connexion

Pour vous inscrire, cliquez sur le bouton "S'inscrire" sur la page d'accueil. Remplissez le formulaire et soumettez-le. Une fois inscrit, utilisez vos identifiants pour vous connecter.

### Profil Utilisateur

Accédez à votre profil en cliquant sur votre photo de profil en haut à droite. Ici, vous pouvez mettre à jour vos informations personnelles et changer votre photo de profil.

### Messagerie Instantanée

1. **Accéder à une discussion** : Cliquez sur une discussion dans la liste des discussions pour ouvrir la boîte de messagerie.
2. **Envoyer un message** : Tapez votre message dans le champ de saisie et cliquez sur "Envoyer".

### Liste des Discussions

Visualisez toutes vos discussions en cours dans la liste des discussions à gauche. Cliquez sur une discussion pour l'ouvrir.

### Suggestions de Profils

Découvrez de nouveaux utilisateurs en naviguant dans la section "Suggestions". Utilisez la barre de filtres pour trouver des utilisateurs spécifiques.

### Recherche de profils 

Recherchez et entamez des discussions en naviguant dans la section "Recherche". Servez vous du filtre pour affiner vos recherches.

### Récupération de mot de passe 

Cliquez sur le lien <Avez-vous oublié votre mot de passe> sur la page de connexion et recevez un mail de récupération.

## Interface

[Cliquez sur lien pour acceder aux photos de l'interface](./Interface/)

## Déploiement sur Heroku

[https://devcenter.heroku.com/articles/getting-started-with-python](https://devcenter.heroku.com/articles/getting-started-with-python)

[https://realpython.com/django-hosting-on-heroku](https://realpython.com/django-hosting-on-heroku/)
