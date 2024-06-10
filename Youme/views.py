from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
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

def accueil(request):
    return render(request, 'registration/accueil.html')

################################################## AUTHENTIFICATION ########################################
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if Utilisateur.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà utilisé')
            else:
                utilisateur = Utilisateur.objects.create_user(email=email, nom=nom, password=password)
                messages.success(request, 'Votre compte a été créé avec succès!')
                # subject = "Bienvenue sur YOU & ME"
                # message = f"Bienvenue {utilisateur.nom} chez vous !"
                # you_mail = EMAIL_HOST_USER
                # send_mail(subject, message, you_mail , [email], fail_silently=False)
                return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'registration/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            utilisateur = authenticate(email=email, password=password)
            if utilisateur is not None:
                auth_login(request, utilisateur)
                return redirect('accueil')
            else:
                messages.error(request, "Votre compte n'existe pas ou les informations sont incorrectes")
    else:
        form = ConnexionForm()
    return render(request, 'registration/connexion.html', {'form': form})

def deconnexion(request):
    auth_logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('accueil')
# ########################################## PROFILS DES UTILISATEURS & SUGGESTIONS ###########################
@login_required
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

# @login_required
# def recherche_profils(request):
#     query = request.GET.get('query', '')
#     resultat = Utilisateur.objects.filter(profile__interests_icontains=query).exclude(id=request.user.id)
#     return render(request, 'profile/recherche_profils.html', {'utilisateurs': resultat}) 




# def generate_suggestions(user_profile):
#     # Utiliser le modèle chargé pour faire des prédictions
#     # Exemple: X est le vecteur de caractéristiques d'entrée pour la prédiction
#     X = [user_profile.age, user_profile.height, user_profile.body_type, user_profile.education, 
#          user_profile.orientation, user_profile.offspring, user_profile.smokes, user_profile.drugs, 
#          user_profile.location,user_profile.diet ]  # Ajoutez toutes les caractéristiques nécessaires
#     suggestions = model.predict([X])  # Exemple d'appel de prédiction, ajustez selon votre modèle
#     return suggestions


# Chemin du fichier modèle
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Youme/models/youme_cleaned_model.pkl')

# Charger le modèle
model = joblib.load(MODEL_PATH)

# # Initialise un encodeur one-hot
# encoder = OneHotEncoder()

# # Supposez que ces sont toutes les catégories possibles pour les caractéristiques textuelles
# categories = [
#     ['Athlétique', 'Mince', 'Arrondie'],  # 'body_type'
#     ['Baccalauréat ou moins', 'Licence', 'Master', 'Doctorat'],  # 'education'
#     ['Hétérosexuel', 'Homosexuel', 'Bisexuel'],  # 'orientation'
#     ["Je n'en ai pas, mais j'aimerais en avoir", "Je n'en veux pas",
#      "J'en ai déjà et souhaiterais en avoir plus", "J'en ai mais je n'en veux plus"],  # 'offspring'
#     ['Jamais', 'Souvent', 'Très souvent', "J'essaie d'abandonner"],  # 'smokes'
#     ['Jamais', 'Souvent', 'Très souvent'],  # 'drugs'
#     ["Je n'ai pas de préférence", 'Végétarien', 'Je suis un halal'],  # 'diet'
#     ['Cotonou', 'Porto-Novo', 'Abomey-Calavi', 'Natitingou', 'Lagos', 'Paris', 'Douala', 'Niamey', 'Ouidah',
#      'Abidjan', 'Accra', 'Genève', 'New-York']  # 'location'
# ]
# encoder = OneHotEncoder(categories=categories, handle_unknown='ignore')
# # Ajustez l'encodeur avec des données factices (un échantillon de chaque catégorie)
# dummy_data = np.array([category[0] for category in categories]).reshape(1, -1)
# encoder.fit(dummy_data)

# # Définir les noms des caractéristiques
# numerical_feature_names = ['age', 'height']
# categorical_feature_names = [
#     'body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location'
# ]

# def generate_suggestions(user_profile):
#     # Extraire les caractéristiques
#     numerical_features = [
#         user_profile.age,
#         user_profile.height
#     ]

#     categorical_features = [
#         user_profile.body_type,
#         user_profile.education,
#         user_profile.orientation,
#         user_profile.offspring,
#         user_profile.smokes,
#         user_profile.drugs,
#         user_profile.diet,
#         user_profile.location
#     ]

#     # Transformer les caractéristiques catégorielles en valeurs numériques
#     categorical_features = np.array(categorical_features).reshape(1, -1)
#     categorical_encoded = encoder.transform(categorical_features).toarray()

#     # Combiner les caractéristiques numériques et encodées
#     numerical_features = np.array(numerical_features).reshape(1, -1)
#     X = np.hstack((numerical_features, categorical_encoded))

#     # Vérification de la taille des caractéristiques combinées
#     expected_feature_count = 39  # Nombre total attendu de caractéristiques (2 numériques + 37 catégorielles encodées)
#     actual_feature_count = X.shape[1]

#     if actual_feature_count != expected_feature_count:
#         raise ValueError(f"Le nombre total de caractéristiques (numériques et encodées) est incorrect. Attendu: {expected_feature_count}, Obtenu: {actual_feature_count}")

#     # Convertir en DataFrame pandas avec les noms de caractéristiques appropriés
#     feature_names = numerical_feature_names + list(encoder.get_feature_names_out(categorical_feature_names))
#     X_df = pd.DataFrame(X, columns=feature_names)

#     # Faire des prédictions avec le modèle
#     suggestions = model.predict(X_df)
#     return suggestions

@login_required
def view_profiles(request):
    try:
        user_profile = Profile.objects.get(utilisateur=request.user)
    except Profile.DoesNotExist:
        # Gérer le cas où le profil n'existe pas
        messages.error(request, "Votre profil n'existe pas. Veuillez le créer.")
        return redirect('maj_profile')  # Rediriger vers la page de mise à jour du profil

    suggestions = generate_suggestions(user_profile)
    suggested_profiles = Profile.objects.filter(id__in=suggestions)
    return render(request, 'profile/view_profiles.html', {'suggested_profiles': suggested_profiles})


def suggestion_profiles(request):
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
        profile = None

    features = ['id','age', 'height','sex','body_type', 'education', 'orientation', 'offspring', 'smokes', 'drugs', 'diet', 'location']

    user_id = current_user.id
    user_name = current_user.nom
    user_age = profile.age	
    user_height = profile.height
    user_sex = profile.sex	
    user_orientation = profile.orientation	
    user_body_type =profile.body_type	
    user_diet = profile.diet	
    user_drink = profile.drink
    user_drugs = profile.drugs
    user_education = profile.education
    user_location = profile.location
    user_offspring = profile.offspring
    user_smokes = profile.smokes
    user_bio = profile.bio
    
     # Synchroniser les index avant la normalisation
    df.reset_index(drop=True, inplace=True)

    X = df[features].copy()
    
    # Convertir les colonnes en catégories et obtenir les codes numériques
    for feat in features[2:]:  # commence à partir de 'body_type'
        X[feat] = df[feat].astype('category').cat.codes
    
    # Vérifiez les dimensions avant la normalisation
    print(f"Length of X before scaling: {len(X)}")
    print(f"Columns in X before scaling: {X.columns}")

    scaler = StandardScaler()
    scaler.set_output(transform='pandas')
    X_scaled = scaler.fit_transform(X)

    # Vérifiez les dimensions après la normalisation
    print(f"Length of X_scaled: {len(X_scaled)}")
    print(f"Columns in X_scaled: {X_scaled.columns}")

    # Vérifiez la longueur des labels du modèle
    print(f"Length of model.labels_: {len(model.labels_)}")

    if len(X_scaled) != len(model.labels_):
        raise ValueError(f"Mismatch between DataFrame length ({len(X_scaled)}) and model labels length ({len(model.labels_)})")


    df['membership'] = model.labels_
    # df.membership.value_counts()

    id = user_id
    prof = df.loc[id:id, features]
    if 'm' == user_sex:
        sex = 'f'
    else:
        sex = 'm'
    users = df.loc[(df.sex == sex)&
        (df.membership == df.at[0, 'membership']) &
        (df.orientation == user_orientation)].index
    print(f'So we have found {len(users)} users in the same cluster.\n')

    def distance(row, user):
        result = 0
        for i, v in enumerate(row):
            result += (v - user[i])**2
        return result ** 0.5
    user = X_scaled.loc[user_id]
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
    # user_id = current_user.id
    # user_name = current_user.name
    # user_age = profile.age	
    # user_height = profile.height
    # user_sex = profile.sex	
    # user_orientation = profile.orientation	
    # user_body_type =profile.body_type	
    # user_diet = profile.diet	
    # user_drink = profile.drink
    # user_drugs = profile.drug
    # user_education = profile.education
    # user_location = profile.location
    # user_offspring = profile.offspring
    # user_smokes = profile.smokes
    # user_bio = profile.bio
    


    # context = {
    #     'current_user_id': current_user.email,
    #     'profile': profile,
    # }
    # return render(request, 'profile/suggestion_profiles.html', context)

    suggested_profiles = Profile.objects.filter(id__in=suggested_users.id)
    return render(request, 'profile/suggestion_profiles.html', {'suggested_profiles': suggested_profiles})
    