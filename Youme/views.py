from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import InscriptionForm, ConnexionForm
from .models import Utilisateur
# Create your views here.

def accueil(request):
    return render(request, 'registration/accueil.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            # prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            motdepasse = form.cleaned_data['motdepasse']
            utilisateur = Utilisateur(nom=nom, email=email, motdepasse=motdepasse)
            utilisateur.save()
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'registration/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            motdepasse = form.cleaned_data['motdepasse']
            try:
                utilisateur = Utilisateur.objects.get(email=email, motdepasse=motdepasse)
                return redirect('accueil')
            except Utilisateur.DoesNotExist:
                return render(request, 'registration/connexion.html', {'form': form, 'message': 'Utilisateur inconnu'})
    else:
        form = ConnexionForm()
    return render(request, 'registration/connexion.html', {'form': form})

