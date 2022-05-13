from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, EtuForm, InvestForm, Investisseur, Etudiant
from django.contrib.auth.models import User

# Create your views here.


# page d'inscrition des etudiants

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

# inscription via les reseaux sociaux

def signup(request):
    context = {
    }
    
    return render(request, 'account/signup.html', context)



def student_signup(request):
    context = {}
    
    

    return render(request, 'account/signup_student.html', context)



def investor_signup(request,pk):
    
    registered = False
    util = ""
    err1 = ""
    err2 = ""
    user_id = User.objects.get(id=pk)
    for user in User.objects.all():
        if user_id == user.id:
            investisseur = Investisseur.objects.create(id=request.user.id)
            investisseur.user.id = user.id
        
    
    user_form = UserForm(instance=user_id)
    invest_form = InvestForm()
    if request.method == "POST":
        user_form = UserForm(data=request.POST, instance=user_id)
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
    return render(request, 'account/sinup_investor.html', context)