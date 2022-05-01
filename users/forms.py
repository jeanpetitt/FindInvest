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


# formulaire pour Etudiant