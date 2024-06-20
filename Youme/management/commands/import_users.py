import pandas as pd
from django.core.management.base import BaseCommand
from Youme.models import Utilisateur, Profile, Préférences
from django.core.files import File
from faker import Faker
import os

class Command(BaseCommand):
    help = 'Import users and profiles from CSV file'

    def handle(self, *args, **kwargs):
        sample_path = "PIL1_2324_2\\Youme\\data\\youme-cleaned.csv"
        
        features = ['age', 'height', 'status', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'bio']
        sample = pd.read_csv(sample_path)
        sample = sample[features]

        for y in features:
            nan_indices = sample[y].isna()
            if nan_indices.any():
                sample.loc[nan_indices, y] = 0

        # Initialiser Faker avec une locale française
        faker = Faker('fr_FR')

        # Générer des prénoms uniques
        male_names = [faker.first_name_male() for _ in range(int(0.6 * len(sample)))]
        female_names = [faker.first_name_female() for _ in range(int(0.4 * len(sample)))]
        used_names = set()
        used_emails = set()
        
        # Mot de passe par défaut
        default_password = 'defaultpassword'

        # Photo de profil par défaut
        default_photo_path = "C:\\Users\\perri\\Desktop\\WORKSPACE\\Django app\\PIL1_2324_2\\static\\images\\profile.png"  
        # Remplacez par le chemin de votre photo par défaut

        for index, row in sample.iterrows():
            sex = 'm' if row['sex'] == 'm' else 'f'
            if sex == 'm' and male_names:
                name = male_names.pop()
            elif sex == 'f' and female_names:
                name = female_names.pop()
            else:
                # Générer un nouveau prénom si les listes sont épuisées
                name = faker.first_name_male() if sex == 'm' else faker.first_name_female()
            i = 1
            # Assurez-vous que le prénom est unique
            while name in used_names:
                name = f"{faker.first_name_male()}{i}" if sex == 'm' else f"{faker.first_name_female()}{i}"
                i += 1
            
            used_names.add(name)

            email = f"{name.lower()}_youme@gmail.com"
            
            # Assurez-vous que l'email est unique
            j = 1
            unique_email = email
            while unique_email in used_emails or Utilisateur.objects.filter(email=unique_email).exists():
                unique_email = f"{name.lower()}{j}_youme@gmail.com"
                j += 1
            
            used_emails.add(unique_email)
            
            # Créer l'utilisateur
            utilisateur = Utilisateur.objects.create_user(email=unique_email, nom=name, password=default_password)
            
            # Créer le profil
            profile = Profile(
                utilisateur=utilisateur,
                age=row['age'] if row['age'] != 0 else faker.random_int(min=18, max=70),
                height=row['height'] if row['height'] != 0 else faker.random_int(min=150, max=200),
                sex=row['sex'],
                orientation=row['orientation'] if row['orientation'] != 0 else faker.random.choice(['Hétérosexuel', 'Homosexuel', 'Bisexuel']),
                body_type=faker.random.choice(['Athlétique', 'Moyen', 'En surpoids', 'Minces']),
                diet=faker.random.choice(['Végétalien', 'Végétarien', 'Omnivore']),
                drink=faker.random.choice(['Jamais', 'Socialement', 'Régulièrement']),
                drugs=faker.random.choice(['Jamais', 'Parfois', 'Souvent']),
                education=faker.random.choice(['École secondaire', 'Licence', 'Master', 'Doctorat']),
                location=faker.random.choice(['Abidjan', 'Dakar', 'Lomé', 'Bamako', 'Ouagadougou', 'Accra', 'Cotonou', 'Porto-Novo', 'Abomey-Calavi', 'Ouidah']),
                offspring=row['offspring'] if row['offspring'] != 0 else faker.random.choice(['Non', 'Oui, vivant avec moi', 'Oui, ne vivant pas avec moi']),
                smokes=faker.random.choice(['Non', 'Parfois', 'Tous les jours']),
                bio=faker.text(max_nb_chars=500),
                religion=faker.random.choice(['Chrétien', 'Musulman', 'Aucune', 'Autre']),
                origin=faker.random.choice(['Côte d\'Ivoire', 'Sénégal', 'Togo', 'Mali', 'Burkina Faso', 'Ghana', 'Bénin']),
                langue=faker.random.choice(['Français', 'Anglais']),
                enfant=faker.random.choice(['Oui', 'Non']),
            )
            
            # Ajouter la photo de profil par défaut
            with open(default_photo_path, 'rb') as photo_file:
                profile.photo.save(os.path.basename(default_photo_path), File(photo_file), save=True)
            
            profile.save()

            # Créer les préférences
            preferences = Préférences(
                user=utilisateur,
                location=faker.random.choice(['Abidjan', 'Dakar', 'Lomé', 'Bamako', 'Ouagadougou', 'Accra', 'Cotonou','Porto-Novo', 'Abomey-Calavi', 'Ouidah']),
                religion=faker.random.choice(['Chrétien', 'Musulman', 'Aucune', 'Autre']),
                origin=faker.random.choice(['Côte d\'Ivoire', 'Sénégal', 'Togo', 'Mali', 'Burkina Faso', 'Ghana', 'Bénin']),
                height=faker.random.uniform(150, 200),
                physique=faker.random.choice(['Athlétique', 'Moyen', 'En surpoids', 'Minces']),
                education=faker.random.choice(['École secondaire', 'Licence', 'Master', 'Doctorat']),
                lifestyle=faker.random.choice(['Actif', 'Sédentaire']),
            )
            preferences.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported users, profiles, and preferences'))
