from django.contrib import admin
from .models import Projet, Comment, Room, Message


# Register your models here.

class AdminProjet(admin.ModelAdmin):
	list_display   = ('title', 'etudiant', 'date_post', 'categorie')
	list_filter    = ('title','categorie',)
	ordering       = ('date_post', )
	search_fields  = ('title', 'etudiant')

admin.site.register(Comment)

admin.site.register(Projet, AdminProjet)

admin.site.register(Room)
admin.site.register(Message)