from django.contrib import admin

# Register your models here.
from .models import *
class AdminComment(admin.ModelAdmin):
    list_display = ['user_comment', 'texte', 'projet', 'date_comment', 'time_com']
    list_filter = ['date_comment', 'user_comment']

class AdminReponse(admin.ModelAdmin):
    list_display = ['user_reponse', 'texte', 'title_com','time_rep']
    list_filter = ['date_reponse']


admin.site.register(Commentaire, AdminComment)
admin.site.register(Reponses, AdminReponse)