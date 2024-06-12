# from django.conf.urls import include
from .views import *
from django.urls import path, include

urlpatterns = [
    ##################### AUTHENTIFICATION #################################
    path('accounts', include("django.contrib.auth.urls")),
    path('', accueil, name= 'accueil'),
    path('inscription/', inscription, name= 'inscription'),
    path('connexion/', connexion, name= 'connexion'),
    path('deconnexion/', deconnexion, name= 'deconnexion'),
    ######################## SUGGESTIONS ET PROFILS #########################
    # path('view_profiles/', view_profiles, name='view_profiles'),
    path('maj_profile/', maj_profile, name='maj_profile'),
    path('suggestion_profiles/', suggestion_profiles, name='suggestion_profiles'),
    path('recherche_profiles/', recherche_profiles, name='recherche_profiles'),
    path('info_profil/', info_profil,name='info_profil'),
    path('personality_test/', personality_test_view, name='personality_test'),
]

