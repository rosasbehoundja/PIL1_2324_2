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
            return redirect('profile_form')
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
            profile.age = form.cleaned_data['age']
            profile.height = form.cleaned_data['height']
            profile.sex = form.cleaned_data['sex']
            profile.orientation = form.cleaned_data['orientation']
            profile.body_type = form.cleaned_data['body_type']
            profile.diet = form.cleaned_data['diet']
            profile.drink = form.cleaned_data['drink']
            profile.drugs = form.cleaned_data['drugs']
            profile.education = form.cleaned_data['education']
            profile.location = form.cleaned_data['location']
            profile.offspring = form.cleaned_data['offspring']
            profile.enfant = form.cleaned_data['enfant']
            profile.smokes = form.cleaned_data['smokes']
            profile.religion = form.cleaned_data['religion']
            profile.origin= form.cleaned_data['origin']
            profile.langue = form.cleaned_data['langue']
            profile.bio = form.cleaned_data['bio']
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
    profile, created = Profile.objects.get_or_create(utilisateur=utilisateur)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès')
            return redirect('view_profiles')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile/maj_profile.html', {'form': form})


# def views_profiles(request):
#     utilisateurs= Utilisateur.objects.exclude(id = request.user.id)
#     return render(request, 'profile/view_profiles.html', {'utilisateurs':utilisateurs})


# Chemin du fichier modèle
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Youme/models/youme_cleaned_model.pkl')

# Charger le modèle
model = joblib.load(MODEL_PATH)

@login_required
def suggestion_profiles(request):
    suggested_profiles = []
    if not request.user.is_active:
        return redirect('connexion')

    current_user = request.user
    try:
        profile = Profile.objects.get(utilisateur=current_user)
        utilisateurs = Profile.objects.all()
        data_u = list(utilisateurs.values('id','age', 'height','sex', 'body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location'))
        data = data_u[:-1]
        df = pd.DataFrame(data)
    except Profile.DoesNotExist:
        messages.error(request, "Votre profil n'existe pas. Veuillez le créer.")
        return redirect('maj_profile')  # Rediriger vers la page de mise à jour du profil


  
    features = ['id','age', 'height','sex','body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location']

    user_id = current_user.id
    user_name = current_user.nom
    user_sex = profile.sex	
    user_orientation = profile.orientation	
    
     # Synchroniser les index avant la normalisation
    df.reset_index(drop=True, inplace=True)

    X = df[features].copy()
    
    # Convertir les colonnes en catégories et obtenir les codes numériques
    for feat in features[2:]:  # commence à partir de 'height'
        X[feat] = df[feat].astype('category').cat.codes

    scaler = StandardScaler()
    scaler.set_output(transform='pandas')
    X_scaled = scaler.fit_transform(X)

    if len(X_scaled) != len(model.labels_):
        raise ValueError(f"Mismatch between DataFrame length ({len(X_scaled)}) and model labels length ({len(model.labels_)})")
        

    df['membership'] = model.labels_
    # df.membership.value_counts()

    # Ensure that the user's index is properly identified
    user_index_list = df.index[df['id'] == user_id].tolist()
    # print(user_index_list)
    if not user_index_list:
        raise ValueError(f"User name {user_name} not found in the DataFrame.")
    user_index = user_index_list[0]

    id = user_id
    info = df.loc[id:id, features]
    print(info)
    if user_orientation == 'Hétérosexuel' and user_sex == 'f': 
        opposite_sex = 'm'
        users = df.loc[(df.sex == opposite_sex) & (df.orientation == 'Hétérosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Homosexuel' and user_sex == 'f':
        users = df.loc[(df.sex == user_sex) & (df.orientation == 'Homosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Hétérosexuel' and user_sex == 'm': 
        opposite_sex = 'f'
        users = df.loc[(df.sex == opposite_sex) & (df.orientation == 'Hétérosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Homosexuel' and user_sex == 'm':
        users = df.loc[(df.sex == user_sex) & (df.orientation == 'Homosexuel') & (df.membership == df.at[0, 'membership'])].index
    elif user_orientation == 'Bisexuel':
        users = df.loc[(df.membership ==df.at[0, 'membership']) & ((df.sex == user_sex) | (df.sex!= user_sex))].index
    else:
        users = df.loc[(df.membership == df.at[0, 'membership'])].index
    print(f'So we have found {len(users)} users in the same cluster.\n')

    def distance(row, user):
        result = 0
        for i, v in enumerate(row):
            result += (v - user[i])**2
        return result ** 0.5
    
    user = X_scaled.loc[user_index]
    distances = X_scaled.loc[users].apply(distance, axis=1, args=(user,)).sort_values()
    
    for y in X:
        nan_indices = df[y].isna()
        if nan_indices.any():
            if pd.api.types.is_categorical_dtype(df[y]):
            # Add 0 to the categories if it's a categorical column
                df[y] = df[y].cat.add_categories([0])
            df.loc[nan_indices, y] = 0

    gamma = 1 / (len(features))
    suggested_users = df.loc[distances.index, features]
    S = pd.DataFrame(distances.apply(lambda x: round(np.exp(-x * gamma)*100, 1)).rename('affinity'))

    suggested_profiles = Profile.objects.filter(id__in=suggested_users.id)
    return render(request, 'profile/suggestion_profiles.html', {'suggested_profiles': suggested_profiles})
    


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