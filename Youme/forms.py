from django import forms
from .models import *

class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ['nom', 'email', 'password']

class ConnexionForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'age', 'bio', 'height', 'body_type', 'education', 'drink', 'drugs', 'smokes', 'likes_dogs', 'likes_cats']
