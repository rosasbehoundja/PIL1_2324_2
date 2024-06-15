import os
import django
import random
from faker import Faker

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PIL1_2324_2.settings')
django.setup()

from Youme.models import Préférences, Profile

# Initialize Faker with French locale
fake = Faker('fr_FR')

# List of 20 hobbies in French
hobbies_list = [
    "Lecture", "Cinéma", "Voyages", "Cuisine", "Sport", "Randonnée",
    "Musique", "Photographie", "Dessin", "Écriture", "Jardinage", 
    "Pêche", "Chasse", "Collection", "Jeux vidéo", "Bricolage", 
    "Danse", "Théâtre", "Astronomie", "Yoga"
]

# Function to generate a random list of hobbies
def generate_random_hobbies():
    return ', '.join(random.sample(hobbies_list, 3))

# Update Préférences table
preferences = Préférences.objects.all()
for preference in preferences:
    preference.hobbies = generate_random_hobbies()
    preference.save()

# Update Profile table
profiles = Profile.objects.all()
for profile in profiles:
    profile.hobbies = generate_random_hobbies()
    profile.save()

print("Les colonnes 'hobbies' des tables 'Préférences' et 'Profile' ont été mises à jour avec succès.")
