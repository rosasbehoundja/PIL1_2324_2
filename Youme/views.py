from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
# from django.contrib.auth.models import User
from .forms import *
from .models import *
from PIL1_2324_2.settings import EMAIL_HOST_USER
import joblib
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
from django.apps import apps
import pickle
from django.shortcuts import get_object_or_404
from django.utils import timezone
import logging
from .recommandations import obtenir_recommandations


def accueil(request):
    return render(request, 'registration/accueil.html')

######################################################## AUTHENTIFICATION ##########################################################
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.nom = form.cleaned_data['nom']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user = form.save()
            login(request, user)
            if Utilisateur.objects.filter(email=user.email).exists():
                messages.error(request, 'Cet email est déjà utilisé')
            else:
                messages.success(request, 'Votre compte a été créé avec succès!')
            # return redirect('maj_profile')
            return redirect('maj_profile')
    else:
        form = InscriptionForm()
    return render(request, 'registration/inscription.html', {'form': form})

logger = logging.getLogger(__name__)
def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                user.last_login = timezone.now()
                user.save()
                return redirect('suggestion_profiles')
            else:
                logger.error(f"Échec de l'authentification pour l'email: {email}")
                messages.error(request, "Votre compte n'existe pas ou les informations sont incorrectes")
        else:
            logger.error("Formulaire invalide.")
            messages.error(request, "Formulaire invalide. Veuillez vérifier les informations saisies.")
    else:
        form = ConnexionForm()
    return render(request, 'registration/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('accueil')
######################################### PROFILS DES UTILISATEURS  - RECHERCHE & SUGGESTIONS ###########################################

# def info_profil(request):
#     user = request.user
#     return render(request, 'profile/info_profil.html', {'user': user})
def profile_form_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrer le formulaire dans la base de données
            profile = form.save(commit=False)
            # Si besoin, effectuer des manipulations supplémentaires avant l'enregistrement
            profile.user = request.user  # Exemple : lier le profil à l'utilisateur connecté
            # profile.age = form.cleaned_data['age']
            # profile.height = form.cleaned_data['height']
            # profile.sex = form.cleaned_data['sex']
            # profile.orientation = form.cleaned_data['orientation']
            # profile.body_type = form.cleaned_data['body_type']
            # profile.diet = form.cleaned_data['diet']
            # profile.drink = form.cleaned_data['drink']
            # profile.drugs = form.cleaned_data['drugs']
            # profile.education = form.cleaned_data['education']
            # profile.location = form.cleaned_data['location']
            # profile.offspring = form.cleaned_data['offspring']
            # profile.enfant = form.cleaned_data['enfant']
            # profile.smokes = form.cleaned_data['smokes']
            # profile.religion = form.cleaned_data['religion']
            # profile.origin= form.cleaned_data['origin']
            # profile.langue = form.cleaned_data['langue']
            # profile.bio = form.cleaned_data['bio']
            profile = form.save()
            return redirect('next_step')  # Redirection vers l'étape suivante après l'enregistrement
    else:
        form = ProfileForm()
    
    return render(request, 'profile/profile_form.html', {'form': form})

def next_step(request):
    return render(request, 'profile/next_step.html')

def preferences_form_view(request):
    if request.method == 'POST':
        form = PréférencesForm(request.POST)
        if form.is_valid():
            # Enregistrer le formulaire dans la base de données
            preferences = form.save(commit=False)
            # Si besoin, effectuer des manipulations supplémentaires avant l'enregistrement
            preferences.user = request.user  # Exemple : lier les préférences à l'utilisateur connecté
            preferences.save()
            return redirect('suggestion_profiles')  # Redirection vers l'étape finale après l'enregistrement
    else:
        form = PréférencesForm()
    
    return render(request, 'profile/preferences_form.html', {'form': form})



@login_required
def maj_profile(request):
    utilisateur = request.user
    try:
        profile, created = Profile.objects.get_or_create(utilisateur=utilisateur)
    except Exception as e:
        # Ajouter du logging ou imprimer l'erreur pour une meilleure compréhension
        print(f"Erreur lors de la récupération ou de la création du profil: {e}")
        # Vous pouvez également utiliser logging pour une meilleure pratique en production
        # import logging
        # logger = logging.getLogger(__name__)
        # logger.error(f"Erreur lors de la récupération ou de la création du profil: {e}")
        raise e
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès')
            return redirect('suggestion_profiles')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile/maj_profile.html', {'form': form})


# def views_profiles(request):
#     utilisateurs= Utilisateur.objects.exclude(id = request.user.id)
#     return render(request, 'profile/view_profiles.html', {'utilisateurs':utilisateurs})


@login_required
def suggestion_profiles(request):
    # Récupérer l'utilisateur connecté
    if not request.user.is_active:
        return redirect('connexion')

    current_user = request.user
    user_nom = current_user.nom
    user_id = current_user.id
    print(user_id)

    # Appeler la fonction pour obtenir les recommandations
    matchs = obtenir_recommandations(user_nom)

    # Initialiser une liste pour stocker les informations des profils recommandés
    recommended_profiles = []

    for match in matchs:
        utilisateurs = Utilisateur.objects.filter(nom=match)
        for utilisateur in utilisateurs:
            try:
                profil = Profile.objects.get(utilisateur=utilisateur)
                recommended_profiles.append({
                    'nom': utilisateur.nom,
                    #'email': utilisateur.email,
                    'hobbies': profil.hobbies,
                    'age': profil.age,
                    'location': profil.location,
                    'orientation': profil.orientation,
                    'body_type': profil.body_type,
                })
            except Profile.DoesNotExist:
                print(f"Profile for user {utilisateur.nom} does not exist")
            except Préférences.DoesNotExist:
                print(f"Preferences for user {utilisateur.nom} do not exist")
    ################ FILTRES ##################
    localisation = request.GET.get('Localisation')
    # Passer les recommandations au template
    context = {
        'form': SuggestionFilterForm(),
        'matchs': matchs,
        'recommended_profiles': recommended_profiles,
    }
    return render(request, 'profile/suggestion_profiles.html', context)


# @login_required
# def recherche_profiles(request):
#     # if not request.user.is_active:
#     #     return redirect('connexion')
#     # current_user = request.user
#     # profile = Profile.objects.get(utilisateur=current_user)
#     utilisateurs = Profile.objects.all()
#     data_u = list(utilisateurs.values('id','age', 'height','sex', 'body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location'))
#     context = {'form' : ProfileFilterForm(),
#                'profiles' : utilisateurs }
#     # query = request.GET.get('query', '')
#     # resultat = Utilisateur.objects.filter(profile__interests_icontains=query).exclude(id=request.user.id)
#     return render(request, 'profile/recherche_profiles.html', context) 