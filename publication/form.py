from django import forms
from .models import *

  
class CommentForm(forms.ModelForm):
      class Meta():
          
          model = Commentaire
          
          fields = [
			'texte',
			'projet',
			'user_comment',

		  ]
          
class ReponseForm(forms.ModelForm):
      class Meta():
          
          model = Reponses
          
          fields = [
			'title_com',
			'texte',
			'user_reponse'

		  ]