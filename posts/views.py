from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import *

# Create your views here.



# page d'accueil (1)

def index(request):
    return render(request, 'posts/index.html')



# page d'accueil (2) des publications

@login_required(login_url='connexion')
def accueil(request):
    return render(request, 'posts/accueil.html')
