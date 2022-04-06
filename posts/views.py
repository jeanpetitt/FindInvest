from django.shortcuts import render

# Create your views here.



# page d'accueil

def accueil(request):
    return render(request, 'posts/accueil.html')
