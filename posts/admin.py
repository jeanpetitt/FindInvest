from django.contrib import admin
from .models import Projet, Comment


# Register your models here.

class AdminProjet(admin.ModelAdmin):
	list_display   = ('title', 'etudiant', 'date_post', 'categorie')
	list_filter    = ('title','categorie',)
	ordering       = ('date_post', )
	search_fields  = ('title', 'etudiant')

admin.site.register(Comment)

admin.site.register(Projet, AdminProjet)
