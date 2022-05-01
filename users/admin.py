from django.contrib import admin
from .models import Etudiant, Investisseur

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Investisseur)