# from django.conf.urls import include
from .views import *
from django.urls import path, include

urlpatterns = [
    path('accounts', include("django.contrib.auth.urls")),
    path('', accueil, name= 'accueil'),
    path('inscription/', inscription, name= 'Inscription'),
]

