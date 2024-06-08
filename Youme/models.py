from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    nom = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
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
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pictures/', null=True )
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, default='unknown')
    orientation = models.CharField(max_length=255, default='unknown')
    body_type = models.CharField(max_length=255, unique=False)
    diet = models.CharField(max_length=255, unique=False, default= 'unknown')
    drink = models.CharField(max_length=255)
    drugs = models.CharField(max_length=50)
    education =  models.CharField(max_length=255, unique=False)
    location = models.CharField(max_length=255, unique=False, default='Cotonou')
    offspring = models.CharField(max_length=255, unique=False, default='unknown')
    smokes = models.CharField(max_length=50)
    bio = models.TextField(max_length= 1000)
        
    def __str__(self):
        return self.utilisateur.nom
