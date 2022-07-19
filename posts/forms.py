from django import forms
from .models import Projet


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
"""
class RepForm(forms.ModelForm):
    class Meta():
        model = Reponse
        fields = ['corps',]
        label = {'corps': 'Reponses'}
        widgets = {
			'corps': forms.Textarea(attrs={
				'class':'form-control',
				'rows':2,
				'cols':10,
				'placeholder':'Votre réponse'
			})
		}
"""