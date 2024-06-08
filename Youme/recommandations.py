# import pickle
# from pprint import pprint
# import numpy as np
# import pandas as pd
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# from pandas.api.types import CategoricalDtype
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# from kneed import KneeLocator


# def load_and_preprocess_data(sample_path):
#     features = ['age', 'height', 'status', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'bio']
#     sample = pd.read_csv(sample_path)
#     sample = sample[features]
    
#     for y in features:
#         nan_indices = sample[y].isna()
#         if nan_indices.any():
#             sample.loc[nan_indices, y] = 0
    
#     return sample


# def preprocess_for_clustering(df, features):
#     X = df[features[0:2]].copy()
#     for feat in features[2:]:
#         X[feat] = df[feat]
        
#     X = pd.get_dummies(X, columns=['status', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'bio'])
    
#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)
    
#     return X_scaled


# def find_optimal_clusters(X_scaled, max_clusters=20):
#     num_clusters = list(np.arange(1, max_clusters + 1))
#     inertias = []

#     for k in num_clusters:
#         model = KMeans(n_clusters=k, n_init='auto', random_state=42)
#         model.fit(X_scaled)
#         inertias.append(model.inertia_)

#     kneedle = KneeLocator(num_clusters, inertias, curve='convex', direction='decreasing')
#     optimal_k = kneedle.elbow
#     return optimal_k


# def cluster_data(X_scaled, k):
#     model = KMeans(n_clusters=k, n_init='auto', random_state=42)
#     model.fit(X_scaled)
    
#     # Sauvegarder le modèle dans un fichier .pkl
#     with open("kmeans_model.pkl", "wb") as file:
#         pickle.dump(model, file)
    
#     return model.labels_


# def plot_clusters(df, k):
#     fig, ax = plt.subplots(figsize=(7, 5))
#     sns.countplot(data=df, x='membership', ax=ax, hue='sex')
#     ax.set(title='Users per cluster', ylabel='')
#     plt.show()


# def suggest_profiles(df, user_id):
#     user = df.loc[user_id]
#     user_sex = user['sex']
#     user_orientation = user['orientation']
#     user_membership = user['membership']
#     user_location = user['location']

#     if user_orientation == 'Hétérosexuel':
#         opposite_sex = 'f' if user_sex == 'm' else 'm'
#         suggested_users = df.loc[(df.sex == opposite_sex) & 
#                                  (df.membership == user_membership)].index
#     elif user_orientation == 'Homosexuel':
#         suggested_users = df.loc[(df.sex == user_sex) & 
#                                  (df.membership == user_membership)].index
#     elif user_orientation == 'Bisexuel':
#         suggested_users = df.loc[(df.membership == user_membership)].index

#     return suggested_users


# def main(sample_path, user_id):
#     df = load_and_preprocess_data(sample_path)
#     features = ['age', 'height', 'status', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'bio']
    
#     X_scaled = preprocess_for_clustering(df, features)
#     optimal_k = None
    
#     try:
#         # Tenter de charger le modèle à partir du fichier .pkl
#         with open("kmeans_model.pkl", "rb") as file:
#             model = pickle.load(file)
#         df['membership'] = model.predict(X_scaled)
#         print(df.membership.value_counts())
#         optimal_k = model.n_clusters
#     except FileNotFoundError:
#         # Si le fichier n'existe pas, trouver le nombre optimal de clusters et entraîner le modèle
#         optimal_k = find_optimal_clusters(X_scaled, max_clusters=20)
#         df['membership'] = cluster_data(X_scaled, optimal_k)
        
#     plot_clusters(df, optimal_k)
    
#     suggested_users = suggest_profiles(df, user_id)
    
#     print(f'So we have found {len(suggested_users)} users for the given preferences.\n')
#     return suggested_users


# if __name__ == "__main__":
#     sample_path = "C:\\Users\\perri\\Desktop\\WORKSPACE\\Django app\\PIL1_2324_2\\Youme\\data\\donnees.csv"
#     user_id = 6
#     suggested_users = main(sample_path, user_id)
#     pprint(suggested_users)
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PIL1_2324_2.settings')
# import django
# django.setup()

import pickle
from pprint import pprint
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
from django.db import connection
from django.apps import apps
from Youme.models import Profile
# from Youme import models
# from Youme.models import Utilisateur , Profile


def load_and_preprocess_data():
    Utilisateur = apps.get_model('Youme', 'Profile')  
    queryset = Utilisateur.objects.all()
    data = list(queryset.values('age', 'height', 'sex', 'orientation', 'body_type', 'education', 'offspring'))
    df = pd.DataFrame(data)
    
    features = ['age', 'height', 'sex', 'orientation', 'body_type', 'education', 'offspring']
    
    for y in features:
        nan_indices = df[y].isna()
        if nan_indices.any():
            df.loc[nan_indices, y] = 0
    
    return df


def preprocess_for_clustering(df, features):
    X = df[features[0:2]].copy()
    for feat in features[2:]:
        X[feat] = df[feat]
        
    X = pd.get_dummies(X, columns=['sex', 'orientation', 'body_type', 'education', 'offspring'])
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled


def find_optimal_clusters(X_scaled, max_clusters=20):
    num_clusters = list(np.arange(1, max_clusters + 1))
    inertias = []

    for k in num_clusters:
        model = KMeans(n_clusters=k, n_init='auto', random_state=42)
        model.fit(X_scaled)
        inertias.append(model.inertia_)

    kneedle = KneeLocator(num_clusters, inertias, curve='convex', direction='decreasing')
    optimal_k = kneedle.elbow
    return optimal_k


def cluster_data(X_scaled, k):
    model = KMeans(n_clusters=k, n_init='auto', random_state=42)
    model.fit(X_scaled)
    
    # Sauvegarder le modèle dans un fichier .pkl
    with open("kmeans_model.pkl", "wb") as file:
        pickle.dump(model, file)
    
    return model.labels_


def plot_clusters(df, k):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.countplot(data=df, x='membership', ax=ax, hue='sex')
    ax.set(title='Users per cluster', ylabel='')
    plt.show()


def suggest_profiles(df, user_id):
    user = df.loc[user_id]
    user_sex = user['sex']
    user_orientation = user['orientation']
    user_membership = user['membership']
    user_offspring = user['offspring']
    user_body_type = user['body_type']
    user_education = user['education']

    if user_orientation == 'Hétérosexuel':
        opposite_sex = 'f' if user_sex == 'm' else 'm'
        suggested_users = df.loc[(df.sex == opposite_sex) & 
                                 (df.membership == user_membership) &
                                 (df.offspring == user_offspring) &
                                 (df.body_type == user_body_type) &
                                 (df.education == user_education)].index
    elif user_orientation == 'Homosexuel':
        suggested_users = df.loc[(df.sex == user_sex) & 
                                 (df.membership == user_membership) &
                                 (df.offspring == user_offspring) &
                                 (df.body_type == user_body_type) &
                                 (df.education == user_education)].index
    elif user_orientation == 'Bisexuel':
        suggested_users = df.loc[(df.membership == user_membership) &
                                 (df.offspring == user_offspring) &
                                 (df.body_type == user_body_type) &
                                 (df.education == user_education)].index

    return suggested_users


def main(user_id):
    df = load_and_preprocess_data()
    features = ['age', 'height', 'sex', 'orientation', 'body_type', 'education', 'offspring']
    
    X_scaled = preprocess_for_clustering(df, features)
    optimal_k = None
    
    try:
        # Tenter de charger le modèle à partir du fichier .pkl
        with open("kmeans_model.pkl", "rb") as file:
            model = pickle.load(file)
        df['membership'] = model.predict(X_scaled)
        print(df.membership.value_counts())
        optimal_k = model.n_clusters
    except FileNotFoundError:
        # Si le fichier n'existe pas, trouver le nombre optimal de clusters et entraîner le modèle
        optimal_k = find_optimal_clusters(X_scaled, max_clusters=20)
        df['membership'] = cluster_data(X_scaled, optimal_k)
        
    plot_clusters(df, optimal_k)
    
    suggested_users = suggest_profiles(df, user_id)
    
    print(f'So we have found {len(suggested_users)} users for the given preferences.\n')
    return suggested_users


if __name__ == "__main__":
    user_id = 422
    suggested_users = main(user_id)
    pprint(user_id['age'])
    pprint(suggested_users)
