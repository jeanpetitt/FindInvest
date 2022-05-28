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

    # obtenir la liste de tous les projets publiers
    projets = Projet.objects.all()
    for projet in projets:
        list_projet.append(projet)

    if request.method == "POST":
        projet_form = ProjetForm(request.POST, request.FILES)
        if projet_form.is_valid():

            # enregistrer dans la BD
            projet = projet_form.save()
            projet.save()
            
            publied = True
            return HttpResponseRedirect('../accueil')
        else:
            err = projet_form.errors

    

    context = {
        'err': err,
        'projet_form': projet_form,
        'publied': publied,
        'list_projet': list_projet,

    }
    return render(request, "posts/accueil.html", context)

# update de project
@login_required(login_url='connexion')
def update_post(request, pk):

    publied = False
    err = ""

    projet = Projet.objects.get(id=pk)

    projet_form = ProjetForm(instance=projet)

    if request.method == 'POST':

        projet_form = ProjetForm(request.POST, request.FILES, instance=projet)

        if projet_form.is_valid():
            projet_form.save()
            publied = True
            return HttpResponseRedirect('../accueil')

        else:
            err = projet_form.errors

    context = {
        'err': err,
        'projet':projet,
        'projet_form': projet_form,
        'publied': publied
    }

    return render(request, 'posts/update_post.html', context)

# delete de project
@login_required(login_url='connexion')
def delete_post(request, pk):
    
    projet_del = Projet.objects.get(id=pk)

    if request.method == 'POST':
        projet_del.delete()
        return HttpResponseRedirect('../accueil')

    context = {
        'projet_del': projet_del
    }

    return render(request, 'posts/delete_projet.html', context)
