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
        fields = ['location', 'religion', 'origin', 'height', 'physique', 'education', 'lifestyle']

class PersonalityTestForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'religion', 'origin', 'langue', 'bio']

    age = forms.IntegerField(label='Entrez votre âge ', min_value=18, max_value=100)
    height = forms.IntegerField(label='Taille (en cm)', min_value=100, max_value=250)
    sex = forms.ChoiceField(label='Sexe', choices=[('m', 'Homme'), ('f', 'Femme')])
    orientation = forms.ChoiceField(label='Orientation sexuelle', choices=[('Hétérosexuel', 'Hétérosexuel'), ('Homosexuel', 'Homosexuel'), ('Bisexuel', 'Bisexuel')])
    body_type = forms.ChoiceField(label='Type de corps', choices=[('Athlétique', 'Athlétique'), ('Moyen', 'Moyen'), ('En surpoids', 'En surpoids'), ('Minces', 'Minces')])
    diet = forms.ChoiceField(label='Régime alimentaire', choices=[('Végétalien', 'Végétalien'), ('Végétarien', 'Végétarien'), ('Omnivore', 'Omnivore')])
    drink = forms.ChoiceField(label='Consommation d\'alcool', choices=[('Jamais', 'Jamais'), ('Socialement', 'Socialement'), ('Régulièrement', 'Régulièrement')])
    drugs = forms.ChoiceField(label='Consommation de drogues', choices=[('Jamais', 'Jamais'), ('Parfois', 'Parfois'), ('Souvent', 'Souvent')])
    education = forms.ChoiceField(label='Niveau d\'éducation', choices=['École secondaire', 'Licence', 'Master', 'Doctorat'])
    location = forms.ChoiceField(label='Localisation', choices=[('Abidjan', 'Abidjan'), ('Dakar', 'Dakar'), ('Lomé', 'Lomé'), ('Bamako', 'Bamako'), ('Ouagadougou', 'Ouagadougou'), ('Accra', 'Accra'), ('Cotonou', 'Cotonou')])
    offspring = forms.ChoiceField(label='Avez-vous des enfants?', choices=[('Non', 'Non'), ('Oui, vivant avec moi', 'Oui, vivant avec moi'), ('Oui, ne vivant pas avec moi', 'Oui, ne vivant pas avec moi')])
    smokes = forms.ChoiceField(label='Fumez-vous ?', choices=[('Non', 'Non'), ('Parfois', 'Parfois'), ('Tous les jours', 'Tous les jours')])
    religion = forms.ChoiceField(label='Religion', choices=[('Chrétien', 'Chrétien'), ('Musulman', 'Musulman'), ('Aucune', 'Aucune'), ('Autre', 'Autre')])
    origin = forms.ChoiceField(label='Pays d\'origine', choices=[('Côte d\'Ivoire', 'Côte d\'Ivoire'), ('Sénégal', 'Sénégal'), ('Togo', 'Togo'), ('Mali', 'Mali'), ('Burkina Faso', 'Burkina Faso'), ('Ghana', 'Ghana'), ('Bénin', 'Bénin')])
    langue = forms.ChoiceField(label='Langue parlée', choices=[('Français', 'Français'), ('Anglais', 'Anglais'), ('Portugais', 'Portugais')])
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'max_length': 1000}))

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Préférences
        fields = ['location', 'religion', 'origin', 'height', 'physique', 'education', 'lifestyle']

    location = forms.ChoiceField(label='Localisation souhaitée', choices=[('Abidjan', 'Abidjan'), ('Dakar', 'Dakar'), ('Lomé', 'Lomé'), ('Bamako', 'Bamako'), ('Ouagadougou', 'Ouagadougou'), ('Accra', 'Accra'), ('Cotonou', 'Cotonou')])
    religion = forms.ChoiceField(label='Religion souhaitée', choices=[('Chrétien', 'Chrétien'), ('Musulman', 'Musulman'), ('Aucune', 'Aucune'), ('Autre', 'Autre')])
    origin = forms.ChoiceField(label='Origine souhaitée', choices=[('Côte d\'Ivoire', 'Côte d\'Ivoire'), ('Sénégal', 'Sénégal'), ('Togo', 'Togo'), ('Mali', 'Mali'), ('Burkina Faso', 'Burkina Faso'), ('Ghana', 'Ghana'), ('Bénin', 'Bénin')])
    height = forms.FloatField(label='Taille souhaitée (en cm)', min_value=100, max_value=250)
    physique = forms.ChoiceField(label='Type de corps souhaité', choices=[('Athlétique', 'Athlétique'), ('Moyen', 'Moyen'), ('En surpoids', 'En surpoids'), ('Minces', 'Minces')])
    education = forms.ChoiceField(label='Niveau d\'éducation souhaité', choices=[('École secondaire', 'École secondaire'), ('Licence', 'Licence'), ('Master', 'Master'), ('Doctorat', 'Doctorat')])
    lifestyle = forms.ChoiceField(label='Mode de vie souhaité', choices=[('Actif', 'Actif'), ('Sédentaire', 'Sédentaire')])