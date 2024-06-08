from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *
from .models import *
from PIL1_2324_2.settings import EMAIL_HOST_USER

def accueil(request):
    return render(request, 'registration/accueil.html')

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

@login_required
def maj_profile(request):
    utilisateur = request.user
    profile , created = Profile.objects.get_or_create(utilisateur= utilisateur)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance= profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès')
            return redirect('profile')
        else: 
            form = ProfileForm(instance=profile)
    return render(request, 'profile/maj_profile.html', {'form': form})

@login_required
def views_profiles(request):
    utilisateurs= Utilisateur.objects.exclude(id = request.user.id)
    return render(request, 'profile/view_profiles.html', {'utilisateurs':utilisateurs})

# @login_required
# def recherche_profils(request):
#     query = request.GET.get('query', '')
#     resultat = Utilisateur.objects.filter(profile__interests_icontains=query).exclude(id=request.user.id)
#     return render(request, 'profile/recherche_profils.html', {'utilisateurs': resultat}) 