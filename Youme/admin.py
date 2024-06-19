from django.contrib import admin
from .models import *

admin.site.register(Utilisateur)
admin.site.register(Profile)
admin.site.register(Préférences)
admin.site.register(Discussion)
admin.site.register(Message)