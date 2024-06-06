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
        fields = ['age', 'height', 'body_type','education', 'drink', 'drug', 'smokes', 'likes_drog', 'likes_cat', 'bio', 'photo']