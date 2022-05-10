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

def update_profile(request, id_util, objet, formulaire):
    err1 = ''
    err2 = ''
    registered = False
    list_util = objet.objects.all()

    # identifier un étudiant spécifique par son id
    util = objet.objects.get(id=id_util)
    
    # identifier le user associé à cet etudiant, par son id
    user = User.objects.get(id=util.user.id)
    
    # remplir le formulaire avec les info de l'etudiant
    form1 = formulaire(instance=util)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        form1 = formulaire(request.POST, request.FILES, instance=util)
        user_form = UserForm(data=request.POST, instance=user)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        if user_form.is_valid() and form1.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            util = form1.save(commit=False)
            util.user = user
            util.save()
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
            err2 = form1.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'form1':form1,
        'err1':err1,
        'err2':err2,
    }
    return context




# page modifier profil étudiant

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



# page modifier profil

def update_profile_investor(request, id_i):
    err1 = ''
    err2 = ''
    registered = False
    investList = Investisseur.objects.all()

    # identifier un étudiant spécifique par son id
    investisseur = Investisseur.objects.get(id=id_i)
    
    # identifier le user associé à cet investissuer, par son id
    user = User.objects.get(id=investisseur.user.id)
    
    # remplir le formulaire avec les info de l'etudiant
    invest_form = InvestForm(instance=investisseur)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        invest_form = InvestForm(request.POST, request.FILES, instance=investisseur)
        user_form = UserForm(data=request.POST, instance=user)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        if user_form.is_valid() and invest_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            investisseur = invest_form.save(commit=False)
            investisseur.user = user
            investisseur.save()
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
            err2 = invest_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'invest_form':invest_form,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/update_profile_investor.html', context)
