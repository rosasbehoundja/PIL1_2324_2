from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InscriptionForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ['nom', 'email', 'password']

    def save(self, commit=True):
        user = super(InscriptionForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hacher le mot de passe
        if commit:
            user.save()
        return user
    
class ConnexionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age','height', 'sex', 'orientation', 'body_type', 'diet' , 'drink', 'drugs','education','location','offspring','enfant', 'smokes', 'religion','origin', 'langue', 'bio', 'photo']


class PréférencesForm(forms.Form):
    class Meta:
        model = Préférences
        fields = ['location', 'religion', 'origin', 'physique', 'education', 'lifestyle']

class PersonalityTestForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age','height', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'religion', 'origin', 'langue', 'bio']

    age = forms.IntegerField(label='Entrez votre âge ', min_value=18, max_value=100)
    sex = forms.ChoiceField(label='Sexe', choices=[('m', 'Homme'), ('f', 'Femme')])
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'max_length': 1000}))

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Préférences
        fields = ['location', 'religion', 'origin', 'physique', 'education', 'lifestyle']

    location = forms.ChoiceField(label='Localisation souhaitée', choices=[('Abidjan', 'Abidjan'), ('Dakar', 'Dakar'), ('Lomé', 'Lomé'), ('Bamako', 'Bamako'), ('Ouagadougou', 'Ouagadougou'), ('Accra', 'Accra'), ('Cotonou', 'Cotonou')])
    religion = forms.ChoiceField(label='Religion souhaitée', choices=[('Chrétien', 'Chrétien'), ('Musulman', 'Musulman'), ('Aucune', 'Aucune'), ('Autre', 'Autre')])
    origin = forms.ChoiceField(label='Origine souhaitée', choices=[('Côte d\'Ivoire', 'Côte d\'Ivoire'), ('Sénégal', 'Sénégal'), ('Togo', 'Togo'), ('Mali', 'Mali'), ('Burkina Faso', 'Burkina Faso'), ('Ghana', 'Ghana'), ('Bénin', 'Bénin')])
    physique = forms.ChoiceField(label='Type de corps souhaité', choices=[('Athlétique', 'Athlétique'), ('Moyen', 'Moyen'), ('En surpoids', 'En surpoids'), ('Minces', 'Minces')])
    education = forms.ChoiceField(label='Niveau d\'éducation souhaité', choices=[('École secondaire', 'École secondaire'), ('Licence', 'Licence'), ('Master', 'Master'), ('Doctorat', 'Doctorat')])
    lifestyle = forms.ChoiceField(label='Mode de vie souhaité', choices=[('Actif', 'Actif'), ('Sédentaire', 'Sédentaire')])


class SuggestionFilterForm(forms.Form):
    Localisation = forms.CharField(required=False)
    age_min = forms.IntegerField(required=False)
    age_max = forms.IntegerField(required=False)
    