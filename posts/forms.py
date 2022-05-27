from django import forms
from .models import Projet


class ProjetForm(forms.ModelForm):
	class Meta():
		
		model = Projet
		fields = '__all__'