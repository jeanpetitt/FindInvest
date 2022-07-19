from django.contrib import admin
from .models import Projet, Room, Message


# Register your models here.

class AdminProjet(admin.ModelAdmin):
	list_display   = ('title', 'etudiant', 'date_post', 'categorie')
	list_filter    = ('title','categorie',)
	#ordering       = ('date_post', )
	search_fields  = ('title', 'etudiant')
 

admin.site.register(Projet, AdminProjet)

admin.site.register(Room)
admin.site.register(Message)
"""
class AdminCom(admin.ModelAdmin):
    	list_display   = ('user', 'projet')
admin.site.register(Commentaire, AdminCom)

class AdminComMessage(admin.ModelAdmin):
	list_display   = ('commentaire', 'auteur', 'date_added')
admin.site.register(ComMessage, AdminComMessage)

admin.site.register(Reponse)


class AdminFavoris(admin.ModelAdmin):
	list_display   = ('projet', 'user')
admin.site.register(Favoris, AdminFavoris)
"""