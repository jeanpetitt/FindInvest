from django.contrib import admin
from .models import Etudiant, Investisseur

# Register your models here.

class AdminEtudiant(admin.ModelAdmin):

	list_display = ['user', 'universite', 'niveauEtude']
	list_filter    = ('universite','niveauEtude',)


class AdminInvestisseur(admin.ModelAdmin):
	list_display = ['user', 'profession', 'entreprise']
	list_filter = ['profession']


admin.site.register(Investisseur, AdminInvestisseur)
admin.site.register(Etudiant, AdminEtudiant)