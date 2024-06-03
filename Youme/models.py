from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255 , unique=True)
    email = models.EmailField(unique=True)
    motdepasse = models.CharField(max_length=255)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    
    USERNAME_FIELD = "nom"
    REQUIRED_FIELDS = ["email"]

    REQUIRED_FIELDS = ["email"]

    # def is_anonymous(self):
    #     return False
    # def is_authenticated(self):
    # # Check if the user has a valid session or token
    #     if self.session_key and self.session_key == self.get_session_key():
    #         return True
    #     elif self.token and self.token == self.get_token():
    #         return True
    #     else:
    #         return False