from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ProjetForm, CommentForm
from .models import Projet, Comment

# Create your views here.



# page d'accueil (1)

def index(request):
    return render(request, 'posts/index.html')



# page d'accueil (2) des publications

@login_required(login_url='connexion')
def accueil(request):
    err_create_post =""
    create_post_form = ProjetForm()
    postList = Projet.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('form_type') == 'create_form':
            # projet_form = ProjetForm(request.POST, request.FILES)
            # if projet_form.is_valid():
            #     projet = projet_form.save()
            #     projet.save()
            #     return HttpResponseRedirect('accueil')
            # else:
            #     err_create_post = projet.errors
            test = request.POST.get('test')
            success = 'Massage '+test+' reçu'
            return HttpResponse(success)
    
    context = {
        'create_post_form':create_post_form,
        'err_create_post':err_create_post,
        'postList':postList,
    }
    return render(request, 'posts/accueil.html', context)


# create a post

def create_post(request):
    err =""
    projet_form = ProjetForm()
    if request.method == 'POST':
        projet_form = ProjetForm(request.POST, request.FILES)
        if projet_form.is_valid():
            projet = projet_form.save()
            projet.save()
            return HttpResponseRedirect('list_projects')
        else:
            err = projet.errors
    context = {'projet_form':projet_form, 'err':err,}
    return render(request, 'posts/create_post.html', context)


# list of posts

def list_projects(request):
    postList = Projet.objects.all()
    
    context = {'postList':postList}
    return render(request, 'posts/list_projects.html', context)




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
