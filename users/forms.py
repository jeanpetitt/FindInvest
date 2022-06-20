from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Etudiant, Investisseur


# formulaire pour DJANGO user
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
# formulaire pour modifier DJANGO user
class UserUpadateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            'last_name',
            'email',
        ]
#  formulaire pour définir le nouveau password
class PwdUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            # 'password1',
            # 'password2'
        ]

# formulaire pour Etudiant
class EtuForm(forms.ModelForm):
    # Pour tout les champs tu doit definir sa correspondance en formfields
    # exemple
    # bio = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = Etudiant
        fields = [
            'bio',
            'fiche_inscription',
            'universite',
            'niveauEtude',
            'reponse',
            'question',
            'photoProfil',
            'telephone',
            'ville'
        ]

    #  implemnter la methode save

    # def save(self, commit=True):
        

# formulaire pour Investisseur
class InvestForm(forms.ModelForm):
    class Meta():
        model = Investisseur
        fields = [
            'entreprise',
            'objectifs',
            'profession',
            'reponse',
            'question',
            'photoProfil',
            'telephone',
            'ville'
        ]