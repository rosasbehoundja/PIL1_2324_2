import pandas as pd
from django.core.management.base import BaseCommand
from Youme.models import Utilisateur, Profile  # Remplacez 'myapp' par le nom de votre application
from django.core.files import File
from faker import Faker
import os

class Command(BaseCommand):
    help = 'Import users and profiles from CSV file'

    def handle(self, *args, **kwargs):
        sample_path = "C:\\Users\\perri\\Desktop\\WORKSPACE\\Django app\\PIL1_2324_2\\Youme\\data\\donnees.csv"
        
        features = ['age', 'height', 'status', 'sex', 'orientation', 'body_type', 'diet', 'drink', 'drugs', 'education', 'location', 'offspring', 'smokes', 'bio']
        sample = pd.read_csv(sample_path)
        sample = sample[features]

        for y in features:
            nan_indices = sample[y].isna()
            if nan_indices.any():
                sample.loc[nan_indices, y] = 0

        # Initialiser Faker pour générer des prénoms et des emails uniques
        faker = Faker()

        # Générer des prénoms uniques
        male_names = [faker.first_name_male() for _ in range(int(0.6 * len(sample)))]
        female_names = [faker.first_name_female() for _ in range(int(0.4 * len(sample)))]
        used_names = set()
        
        # Mot de passe par défaut
        default_password = 'defaultpassword'

        # Photo de profil par défaut
        default_photo_path = "C:\\Users\\perri\\Desktop\\WORKSPACE\\Django app\\PIL1_2324_2\\static\\images\\default.jpeg"  
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
            
            # Assurez-vous que le prénom est unique
            while name in used_names:
                name = faker.first_name_male() if sex == 'm' else faker.first_name_female()
                
            used_names.add(name)

            email = f"{name.lower()}_youme@gmail.com"
            
            # Créer l'utilisateur
            utilisateur = Utilisateur.objects.create_user(email=email, nom=name, password=default_password)
            
            # Créer le profil
            profile = Profile(
                utilisateur=utilisateur,
                age=row['age'],
                height=row['height'],
                sex=row['sex'],
                orientation=row['orientation'],
                body_type=row['body_type'],
                drink=row['drink'],
                drugs=row['drugs'],
                education=row['education'],
                location=row['location'],
                offspring=row['offspring'],
                smokes=row['smokes'],
                bio=row['bio']
            )
            
            # Ajouter la photo de profil par défaut
            with open(default_photo_path, 'rb') as photo_file:
                profile.photo.save(os.path.basename(default_photo_path), File(photo_file), save=True)
            
            profile.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported users and profiles'))