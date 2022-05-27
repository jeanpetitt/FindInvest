from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import *
from .forms import ProjetForm
from .models import Projet


# Create your views here.


# page d'accueil (1)


def index(request):
    return render(request, 'posts/index.html')


# page d'accueil (2) des publications
"""
@login_required(login_url='connexion')
def accueil(request):
    return render(request, 'posts/accueil.html')
"""

@login_required(login_url='connexion')
def accueil(request):
    publied = False
    err = ""
    projet_form = ProjetForm()
    list_projet = []

    projets = Projet.objects.all()
    etudiant = request.user.etudiant.id

    if request.method == "POST":
        projet_form = ProjetForm(data=request.POST)
        if projet_form.is_valid():
            
            projet = projet_form.save(commit=False)
            
            # enregistrer dans la BD
            projet.etudiant = etudiant
            projet.save()
            
            publied = True
            print('reussi')

            return HttpResponseRedirect('../accueil')
        else:
            print('echec')
            err = projet_form.errors

    for projet in projets:
        list_projet.append(projet)

    context = {
        'err': err,
        'projet_form': projet_form,
        'publied': publied,
        'list_projet': list_projet,

    }
    return render(request, "posts/accueil.html", context)
