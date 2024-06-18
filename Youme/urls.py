# from django.conf.urls import include
from .views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    ##################### AUTHENTIFICATION #################################
    path('accounts', include("django.contrib.auth.urls")),
    path('', accueil, name= 'accueil'),
    path('inscription/', inscription, name= 'inscription'),
    path('connexion/', connexion, name= 'connexion'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('deconnexion/', deconnexion, name= 'deconnexion'),
    ################ FORMULAIRES DE PROFILS ET PREFERENCES ###################
    path('profile_intro/', user_profile_intro, name='profile_intro'),
    path('personality_test/', personality_test, name='personality_test'),
    path('preferences_intro/', preferences_intro, name='preferences_intro'),
    path('preferences_form/', preferences_form, name='preferences_form'),
    ######################## SUGGESTIONS ET RECHERCHES #########################
    path('suggestion_profiles/', suggestion_profiles, name='suggestion_profiles'),
    path('recherche_profiles/', recherche_profiles, name='recherche_profiles'),
    ############## PAGES D'AFFICHAGE DE PROFIL DES UTILISATEURS ################
    path('profile/', profile ,name='profile'),
    path('profile_detail/<int:pk>/', profile_detail, name='profile_detail')
    ########################### MESSAGERIE INSTANTANEE & CHATBOT ################
]

