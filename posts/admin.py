from django.contrib import admin
from .models import *


# Register your models here.

class AdminProjet(admin.ModelAdmin):
	list_display   = ('title', 'etudiant', 'date_post', 'categorie')
	list_filter    = ('title','categorie',)
	ordering       = ('date_post', )
	search_fields  = ('title', 'etudiant')
"""
	fieldsets = (
    	# Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse',],
            'fields': ('title', 'categorie', 'media', 'image')
        }),
        # Fieldset 2 : description du projet
        (' contenu de la description', {
           'description': u'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('description', )
        }),
    )
"""
class AdminComment(admin.ModelAdmin):
    list_display = ['user_comment', 'texte', 'projet', 'date_comment', 'time_com']
    list_filter = ['date_comment', 'user_comment']

class AdminReponse(admin.ModelAdmin):
    list_display = ['user_reponse', 'texte', 'title','time_rep']
    list_filter = ['date_reponse']
    
admin.site.register(Comment, AdminComment)
admin.site.register(Reponse, AdminReponse)

admin.site.register(Projet, AdminProjet)
