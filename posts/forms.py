from dataclasses import field
from pyexpat import model
from django import forms
from .models import *


class ProjetForm(forms.ModelForm):
	class Meta():
		
		model = Projet

		fields = [
			'title',
			'categorie',
			'media',
			'image',
			'investi',
			'description',
			'etudiant',

		]
  
class CommentForm(forms.ModelForm):
      class Meta():
          
          model = Comment
          
          fields = [
			'texte',
			'projet',
			'user_comment',

		  ]
          
class ReponseForm(forms.ModelForm):
      class Meta():
          
          model = Reponse
          
          fields = [
			'title_com',
			'texte',
			'user_reponse'

		  ]