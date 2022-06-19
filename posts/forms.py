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
  
