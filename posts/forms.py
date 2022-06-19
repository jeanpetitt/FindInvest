from django import forms
from .models import Comment, Projet


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
			  'title'
		  ]
