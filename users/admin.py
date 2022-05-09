from django.contrib import admin
from .models import Etudiant, Investisseur, Profile

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Investisseur)
admin.site.register(Profile)