from distutils.command.sdist import sdist
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, EtuForm, InvestForm, UserUpadateForm, PwdUpdateForm
from .models import Etudiant, Investisseur
from django.contrib.auth.models import User

# Create your views here.



# page de connexion

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if user.is_authenticated:
                    logout(request)
                login(request, user)
                return HttpResponseRedirect('../accueil')  
            else:
                return HttpResponse("L'utilisateur est désactivé")
        else:
            msg = messages.info(request, "votre Adresse mail ou votre Mot de passe est incorrect, veuillez réessayer !")
            context = {
                'msg':msg
            }
            return render(request, 'users/connexion.html', context)
    else:
        return render(request, 'users/connexion.html')



# reinitialiser mot de passe

def reset_pwd(request):
    err = ""
    question = ""
    rep = ""
    existe = False
    listEtu = []
    listInv = []
    for etu in Etudiant.objects.all():
        listEtu.append(etu.user.username)
    for inv in Investisseur.objects.all():
        listInv.append(inv.user.username)

    if request.method == 'POST':
        username = request.POST.get('username')
        methode = request.POST.get('methode')
        reponse = request.POST.get('reponse')

        # if methode == "1":
        
        for user in User.objects.all():
            if user.username == username:
                if username in listEtu:
                    question = user.etudiant.question
                    rep = user.etudiant.reponse
                elif username in listInv:
                    question = user.investisseur.question
                    rep = user.investisseur.reponse
                existe = True
                break

        if existe:
            if reponse == rep:
                return HttpResponseRedirect("new_password")
            else:
                err = messages.error(request, "Réponse incorrecte, Veuillez réessayer !")
            context = {
                'username':username,
                'question':question,
                'rep':rep,
                'existe':existe,
                'err':err
            }
            return render(request, 'users/reset_password.html', context)
        else:
            err = messages.error(request, "Il n'existe pas un utilisateur ayant cette adresse email. Veuillez réessayer !")
            context = {
                'err':err,
                'existe':existe
            }
            return render(request, 'users/reset_password.html', context)
    else:
        return render(request, 'users/reset_password.html')
       



# définir le nouveau mot de passe

def new_password(request):
    pwd_form = PwdUpdateForm()
    if request.method == 'POST':
        existe = False
        username = request.POST.get('username')
        for use in User.objects.all():
            if use.username == username:
                pwd_form = PwdUpdateForm(data=request.POST, instance=use)
                break

        # pwd_form = PwdUpdateForm(data=request.POST)
        
        if pwd_form.is_valid():

            # enregistrer dans la BD
            pwd = pwd_form.save()
            pwd.save()
            return HttpResponseRedirect("connexion")
            
    return render(request, 'users/new_password.html')





# se déconnecter
@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# page d'inscription des etudiants

def register_student(request):
    registered = False
    util = ""
    num_tel = ""
    err1 = ""
    err2 = ""
    user_form = UserForm()
    etu_form = EtuForm()

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        etu_form = EtuForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        telephone = request.POST.get('telephone')
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
            return HttpResponseRedirect('../accueil')
        else:
            util = username
            num_tel = telephone
            err1 = user_form.errors
            err2 = etu_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'etu_form':etu_form,
        'util':util,
        'num_tel':num_tel,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/register_student.html', context)



# page d'incrition des investisseurs

def register_investor(request):
    registered = False
    util = ""
    num_tel = ""
    err1 = ""
    err2 = ""
    user_form = UserForm()
    invest_form = InvestForm()

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        invest_form = InvestForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        telephone = request.POST.get('telephone')
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
            return HttpResponseRedirect('../accueil')
        else:
            util = username
            num_tel = telephone
            err1 = user_form.errors
            err2 = invest_form.errors

    context = {
        'registered':registered,
        'user_form':user_form,
        'invest_form':invest_form,
        'util':util,
        'num_tel':num_tel,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/register_investor.html', context)



# page modifier profil étudiant

@login_required(login_url='connexion')
def update_profile_student(request):
    err1 = ''
    err2 = ''
    etu_form = EtuForm(instance=request.user.etudiant)
    user_form = UserUpadateForm(instance=request.user)
    if request.method == "POST":
        etu_form = EtuForm(request.POST, request.FILES, instance=request.user.etudiant)
        user_form = UserUpadateForm(data=request.POST, instance=request.user)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        if user_form.is_valid() and etu_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            etudiant = etu_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('../../../accueil')
        else:
            err1 = user_form.errors
            err2 = etu_form.errors

    context = {
        'user_form':user_form,
        'etu_form':etu_form,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/update_profile_student.html', context)



# page modifier profil investisseur

@login_required(login_url='connexion')
def update_profile_investor(request):
    err1 = ''
    err2 = ''

    # identifier un étudiant spécifique par son id
    # investisseur = Investisseur.objects.get(id=id_i)
    
    # identifier le user associé à cet investissuer, par son id
    # user = User.objects.get(id=investisseur.user.id)
    
    # remplir le formulaire avec les info de l'etudiant
    invest_form = InvestForm(instance=request.user.investisseur)
    user_form = UserUpadateForm(instance=request.user)
    if request.method == "POST":
        invest_form = InvestForm(request.POST, request.FILES, instance=request.user.investisseur)
        user_form = UserUpadateForm(data=request.POST, instance=request.user)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        if user_form.is_valid() and invest_form.is_valid():

            # enregistrer dans la BD
            user = user_form.save()
            user.save()
            investisseur = invest_form.save(commit=False)
            investisseur.user = user
            investisseur.save()
            
            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('../../../accueil')
        else:
            err1 = user_form.errors
            err2 = invest_form.errors

    context = {
        'user_form':user_form,
        'invest_form':invest_form,
        'err1':err1,
        'err2':err2,
    }
    return render(request, 'users/update_profile_investor.html', context)




# Consulter profil etudiant

def profile_student(request, id_e):

    # identifier l'etudiant
    etudiant = Etudiant.objects.get(id=id_e)

    # identifier le user
    util = User.objects.get(id=etudiant.user.id)
    
    context = {
        'etudiant':etudiant,
        'util':util,
    }
    return render(request, 'users/profile_student.html', context)





#consulter profil investisseur

@login_required(login_url='connexion')
def profile_investor(request,id_i):
    investor=Investisseur.objects.get(id=id_i)
    util=User.objects.get(id=investor.user.id)
    context={
        'util':util,
        'investor':investor,
    }
    return render(request, 'users/profile_investor.html',context)


# inscription via les reseaux sociaux

def signup(request):
    context = {
    }

    return render(request, 'account/signup.html', context)


def student_signup(request, pk):
    registered = False
    util = ""
    err1 = ""
    err2 = ""
    user_id = User.objects.get(id=pk)
    for user in User.objects.all():
        if user_id == user.id:
            etudian = Etudiant.objects.create(id=request.user.id)
            etudian.user.id = user.id

    user_form = UserForm(instance=user_id)
    etu_form = EtuForm()
    if request.method == "POST":
        user_form = UserForm(data=request.POST, instance=user_id)
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
        if not etudiant.save():
            logout(request)

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
        'registered': registered,
        'user_form': user_form,
        'etu_form': etu_form,
        'util': util,
        'err1': err1,
        'err2': err2,
    }

    return render(request, 'users/register_student.html', context)


def investor_signup(request, pk):
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
        'registered': registered,
        'user_form': user_form,
        'invest_form': invest_form,
        'util': util,
        'err1': err1,
        'err2': err2,
    }
    return render(request, 'users/register_investor.html', context)


