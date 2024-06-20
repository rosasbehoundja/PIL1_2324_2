from django.contrib import admin
from .models import *

class ProfileAdminInline(admin.TabularInline): 
    model = Profile

class PreferencesAdminInline(admin.TabularInline):
    model = Préférences

class UtilisateurAdmin(admin.ModelAdmin):
    inlines = [ProfileAdminInline, PreferencesAdminInline]
    list_display = ('nom', 'get_sexe', 'get_age', 'get_orientation', 'last_login', 'is_active', 'is_admin')
    list_filter = ('nom', 'is_active')
    search_fields = ('nom', 'is_active')

    def get_sexe(self, obj):
        return obj.profile.sex if hasattr(obj, 'profile') else 'N/A'
    get_sexe.short_description = 'Sexe'

    def get_age(self, obj):
        return obj.profile.age if hasattr(obj, 'profile') else 'N/A'
    get_age.short_description = 'Age'

    def get_orientation(self, obj):
        return obj.profile.orientation if hasattr(obj, 'profile') else 'N/A'
    get_orientation.short_description = 'Orientation'

admin.site.register(Utilisateur, UtilisateurAdmin)      

admin.site.register(Préférences)
admin.site.register(Discussion)
admin.site.register(Message)