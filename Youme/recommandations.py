# recommandations.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from Youme.models import Profile, Préférences

def charger_donnees_profils():
    profiles = Profile.objects.all().select_related('utilisateur')
    data = [] 
    for profile in profiles:
        try:
            preferences = Préférences.objects.get(user=profile.utilisateur)
            data.append({
                'nom': profile.utilisateur.nom,
                'orientation' : profile.orientation,
                'interests': profile.hobbies,
                'education': preferences.education if preferences.education else '',
                'hobbies_pref': preferences.hobbies if preferences.hobbies else '',
                'lifestyle': preferences.lifestyle if preferences.lifestyle else '',
                'physique': preferences.physique if preferences.physique else '',
            })
        except Préférences.DoesNotExist:
            data.append({
                'nom': profile.utilisateur.nom,
                'orientation' : profile.orientation,
                'interests': profile.hobbies,
                'education': '',
                'hobbies_pref': '',
                'lifestyle': '',
                'physique': '',
            })
    return pd.DataFrame(data)

def calculer_similarites(df):
    tfidf = TfidfVectorizer(tokenizer=lambda x: x.split(', '), lowercase=True)
    orientation_tfidf = tfidf.fit_transform(df['orientation'])
    interests_tfidf = tfidf.fit_transform(df['interests'])
    education_tfidf = tfidf.fit_transform(df['education'])
    hobbies_pref_tfidf = tfidf.fit_transform(df['hobbies_pref'])
    lifestyle_tfidf = tfidf.fit_transform(df['lifestyle'])
    physique_tfidf = tfidf.fit_transform(df['physique'])
    
    orientation_similarity = linear_kernel(orientation_tfidf, orientation_tfidf)
    interests_similarity = linear_kernel(interests_tfidf, interests_tfidf)
    education_similarity = linear_kernel(education_tfidf, education_tfidf)
    hobbies_pref_similarity = linear_kernel(hobbies_pref_tfidf, hobbies_pref_tfidf)
    lifestyle_similarity = linear_kernel(lifestyle_tfidf, lifestyle_tfidf)
    physique_similarity = linear_kernel(physique_tfidf, physique_tfidf)
    
    combined_similarity = ( orientation_similarity +
        interests_similarity + education_similarity + 
        hobbies_pref_similarity + lifestyle_similarity +
        physique_similarity) / 6 
    return combined_similarity

def suggérer_matchs(nom, combined_similarity, df):
    user_index = df[df['nom'] == nom].index[0]
    similarity_scores = list(enumerate(combined_similarity[user_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_users_indices = [i[0] for i in similarity_scores[1:]]
    similar_users_noms = df.iloc[similar_users_indices]['nom'].values
    return similar_users_noms

def obtenir_recommandations(nom_nouvel_utilisateur):
    df = charger_donnees_profils()
    # Calculer les similarités
    combined_similarity = calculer_similarites(df)
    # Suggérer des matchs pour le nouvel utilisateur
    matchs = suggérer_matchs(nom_nouvel_utilisateur, combined_similarity, df)
    matchs = matchs[:100]
    return matchs

    
