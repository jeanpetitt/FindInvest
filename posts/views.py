from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import *
from .forms import ProjetForm, CommentForm, ReponseForm
from .models import Projet, Comment, Reponse

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
    err_post = ""
    erro_comm = ''
    err_reponse = ""
    
    nb_commentaire = 0
    nb_reps = 0
    total_com = 0
    coms = Comment.objects.all()
    reps = Reponse.objects.all()
    
    
    projet_form = ProjetForm()
    comment_form = CommentForm()
    reponse_form = ReponseForm()
    
    list_projet = []
    list_comment = []
    list_rep_com = []
    list_projet_com = []
    
    #obtenir la liste de les commentaire
    for com in coms:
        list_comment.append(com)
        list_projet_com.append(com)
    nb_commentaire = len(list_comment)
    for rep in reps:
        list_rep_com.append(rep)
        list_projet_com.append(rep.title_com.projet)
    nb_reps = len(list_rep_com)
    
    
    total_com = nb_reps + nb_commentaire    
    

    # obtenir la liste de tous les projets publiers
    projets = Projet.objects.all()
    for projet in projets:
        list_projet.append(projet)

    if request.method == "POST":
        
        #poster une publication
        if 'etudiant' in request.POST:
            
            projet_form = ProjetForm(request.POST, request.FILES)
            if projet_form.is_valid():

                # enregistrer dans la BD
                projet = projet_form.save()
                projet.save()
                
                publied = True
                context = {'title':projet.title, 'categorie':projet.categorie, 'description':projet.description, 'image':projet.image,'etudiant_img': projet.etudiant.photoProfil.url}
                return HttpResponseRedirect('../accueil')
            else:
                err_post = projet_form.errors
        #poster un commentaire
        elif 'user_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save()
                comment.save()
                context = {'comment_texte': comment.texte,'comment_user': comment.user_comment,'date_comment': comment.date_comment,'comment_time': comment.time_com,'comment_projet': comment.projet,'nb_com': total_com,}
                #return JsonResponse({'comment_texte': comment.texte,'comment_user': comment.user_comment,'date_comment': comment.date_comment,'comment_time': comment.time_com,'comment_projet': comment.projet})
                return HttpResponseRedirect('../accueil')
            else:
                erro_comm = comment_form.errors()
        #repondre a un commentaire
        elif 'title_com' in request.POST:
            reponse_form = ReponseForm(request.POST)
            
            if reponse_form.is_valid():
                
                reponse = reponse_form.save()
                reponse.save()
                context = {
                    'reponse_texte': reponse.texte,
                    'reponse_com': reponse.title_com,
                    'reponse_date': reponse.date_reponse,
                    'reponse_user': reponse.user_reponse,
                    'reponse_time': reponse.time_rep,
                    'nb_com': total_com,
                }
                #return JsonResponse(context)
                return HttpResponseRedirect('../accueil')
            else:
                err_reponse = reponse_form.errors()

    

    context = {
        'err': err_post,
        'err_com': erro_comm,
        'err_post': err_post,
        'err_reponse':err_reponse,
        'nb_com': total_com,
        
        'list_com': list_comment,
        'list_rep': list_rep_com,
        'comment_form': comment_form,
        'reponse_form': reponse_form,
        'projet_form': projet_form,
        'publied': publied,
        'list_projet': list_projet,
        'projet_com': list_projet_com,

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


# commenter un projet

@login_required(login_url='connexion')
def commenterPublication(request):
    comments = Comment.objects.all()
    list_comment = []
    
    for com in comments:
        list_comment.append(com)
    comment_form = CommentForm()
    error = ''
    if request.method == "POST":
        title = request.POST.get('title')
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid:
            comment = comment_form.save()
            comment.save()
            return JsonResponse({'new_comment':comment.title})
            
        else:
            error = comment_form.errors()
            comment_form = CommentForm()
            
    context = {
        'comment':comment_form,
        'error': error,
        'comments':list_comment,
    }
            
    return render(request, 'posts/comment.html', context)