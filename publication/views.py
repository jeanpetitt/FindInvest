from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .form import *
from .models import Commentaire, Reponses

# Create your views here.
@login_required(login_url='connexion')
def commentPost(request):

    erro_comm = ''
    err_reponse = ""
    
    nb_commentaire = 0
    nb_reps = 0
    total_com = 0
    coms = Commentaire.objects.all()
    reps = Reponses.objects.all()
 
    comment_form = CommentForm()
    reponse_form = ReponseForm()
    
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
    if request.method == "POST":
        #poster un commentaire
        if 'user_comment' in request.POST:
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
        'err_com': erro_comm,
        'err_reponse':err_reponse,
        'nb_com': total_com,
        'list_com': list_comment,
        'list_rep': list_rep_com,
        'comment_form': comment_form,
        'reponse_form': reponse_form,
        'projet_com': list_projet_com,

    }
    return render(request, "posts/comment.html", context)