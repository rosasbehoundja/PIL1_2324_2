from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, nom, password=None):
        if not email:
            raise ValueError('L\'adresse email doit être fournie')
        email = self.normalize_email(email)
        utilisateur = self.model(email=email, nom=nom)
        utilisateur.set_password(password)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, nom, password):
        utilisateur = self.create_user(email, nom, password)
        utilisateur.is_admin = True
        utilisateur.save(using=self._db)
        return utilisateur

class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(datetime.datetime.now(), null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    class OrientationChoices(models.TextChoices):
        Hétérosexuel = 'Hétérosexuel'
        Homosexuel = 'Homosexuel'
        Bisexuel = 'Bisexuel'
    
    class BodyTypeChoices(models.TextChoices):
        Mince = 'Minces'
        En_Surpoids = 'En surpoids'
        Moyen = 'Moyen'
        Athlétique = 'Athlétique'
    
    class SexeChoices(models.TextChoices):
        Homme = 'm'
        Femme = 'f'
  
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, default='f', choices=SexeChoices.choices)
    orientation = models.CharField(max_length=255, default='Hétérosexuel', choices=OrientationChoices.choices)
    body_type = models.CharField(max_length=255, unique=False, null=True, choices=BodyTypeChoices.choices)
    diet = models.CharField(max_length=255, unique=False, null=True)
    drink = models.CharField(max_length=255, null=True)
    drugs = models.CharField(max_length=50, null=True)
    education =  models.CharField(max_length=255, unique=False)
    location = models.CharField(max_length=255, unique=False, default='Cotonou')
    offspring = models.CharField(max_length=255, unique=False, default="Non")
    enfant = models.CharField(max_length=255, unique=False, default="Oui")
    smokes = models.CharField(max_length=50, null=True)
    religion = models.CharField(max_length=300, null=True)
    origin = models.CharField(max_length=255, null=True)
    langue = models.CharField(max_length=225, null=True)
    hobbies = models.CharField(max_length=225, null=True, default= 'Lecture, Voyage')
    bio = models.TextField(max_length= 1000, null=True)
    photo = models.ImageField(upload_to='profile_pictures', null=True, default='static/images/profile.png')

    def __str__(self):
        return self.utilisateur.nom

class Préférences(models.Model):

    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    origin = models.CharField(max_length=50, blank=True, null=True)
    physique = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    lifestyle = models.CharField(max_length=100, blank=True, null=True)
    hobbies = models.CharField(max_length=225, null=False, default= 'Lecture, Voyage')
    
