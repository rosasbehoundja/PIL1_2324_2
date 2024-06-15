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
    ######################## SUGGESTIONS ET PROFILS #########################
    path('profile_form/', profile_form_view, name='profile_form'),
    path('next_step/', next_step, name='next_step'),
    path('preferences_form/', preferences_form_view, name='preferences_form'),
    path('maj_profile/', maj_profile, name='maj_profile'),
    path('suggestion_profiles/', suggestion_profiles, name='suggestion_profiles'),
    #path('recherche_profiles/', recherche_profiles, name='recherche_profiles'),
    #path('info_profil/', info_profil,name='info_profil'),
    #path('personality_test/', personality_test_view, name='personality_test'),
    #path('view_profiles/', view_profiles, name='view_profiles'),
]

