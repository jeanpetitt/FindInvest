from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, EtuForm, InvestForm
from .models import Etudiant, Investisseur
from django.contrib.auth.models import User

# Create your views here.


# page d'inscription des etudiants

def register_student(request):
    registered = False
    util = ""
    err1 = ""
    err2 = ""
    user_form = UserForm()
    etu_form = EtuForm()

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        etu_form = EtuForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if user_form.is_valid() and etu_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            etudiant = etu_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            registered = True
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('/')
        else:
            util = username
            err1 = user_form.errors
            err2 = etu_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'etu_form':etu_form,
        'util':util,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/register_student.html', context)



# page d'incrition des investisseurs

def register_investor(request):
    registered = False
    util = ""
    err1 = ""
    err2 = ""
    user_form = UserForm()
    invest_form = InvestForm()

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        invest_form = InvestForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if user_form.is_valid() and invest_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            etudiant = invest_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            registered = True
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('/')
        else:
            util = username
            err1 = user_form.errors
            err2 = invest_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'invest_form':invest_form,
        'util':util,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/register_investor.html', context)




# page modifier profil

def update_profile_student(request, id_e):
    err1 = ''
    err2 = ''
    registered = False
    etuList = Etudiant.objects.all()

    # identifier un étudiant spécifique par son id
    etudiant = Etudiant.objects.get(id=id_e)
    
    # identifier le user associé à cet etudiant, par son id
    user = User.objects.get(id=etudiant.user.id)
    
    # remplir le formulaire avec les info de l'etudiant
    etu_form = EtuForm(instance=etudiant)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        etu_form = EtuForm(request.POST, request.FILES, instance=etudiant)
        user_form = UserForm(data=request.POST, instance=user)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        if user_form.is_valid() and etu_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            etudiant = etu_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            registered = True
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('/')
        else:
            err1 = user_form.errors
            err2 = etu_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'etu_form':etu_form,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/update_profile_student.html', context)
