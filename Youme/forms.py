from django import forms
from .models import Utilisateur

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'email', 'motdepasse']

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['email', 'motdepasse']