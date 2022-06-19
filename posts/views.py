from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ProjetForm, CommentForm
from .models import Projet, Comment, Room, Message

# Create your views here.



# page d'accueil (1)

def index(request):
    return render(request, 'posts/index.html')



# page d'accueil (2) des publications

@login_required(login_url='connexion')
def accueil(request):
    # crer un projet
    err_create_post = ""
    create_post_form = ProjetForm()
    postList = Projet.objects.all()
    postListUnique = []
    pListCat = []
    for p in postList:
        if p.categorie not in pListCat:
            postListUnique.append(p)
            pListCat.append(p.categorie)

    # chat
    roomList = Room.objects.all()
    userList = User.objects.all()
    
    if request.method == 'POST':
        #poster une publication
        if 'etudiant' in request.POST:   
            create_post_form = ProjetForm(request.POST, request.FILES)
            if create_post_form.is_valid():

                # enregistrer dans la BD
                projet = create_post_form.save()
                projet.save()
                
                publied = True
                context = {'title':projet.title, 'categorie':projet.categorie, 'description':projet.description, 'image':projet.image,'etudiant_img': projet.etudiant.photoProfil.url}
                return HttpResponseRedirect('../accueil')
            else:
                err_create_post = create_post_form.errors
    
    context = {
        # creer un projet
        'create_post_form':create_post_form,
        'err_create_post':err_create_post,
        'postList':postList,
        'postListUnique':postListUnique,

        # chat
        'roomList':roomList,
        'userList':userList,
    }
    return render(request, 'posts/accueil.html', context)




# ==================== CRUD POST ======================


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
        'create_post_form': projet_form,
        'publied': publied
    }

    return render(request, 'posts/update_post.html', context)



# delete de project

@login_required(login_url='connexion')
def delete_post(request, pk):
    
    projet_del = Projet.objects.get(id=pk)

    # if request.method == 'POST':
    projet_del.delete()
    return HttpResponseRedirect('../accueil')

    # context = {
    #     'projet_del': projet_del
    # }

    # return render(request, 'posts/delete_projet.html', context)




# ======================== CHAT ==========================

# page de chat
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    roomList = Room.objects.all()
    userList = User.objects.all()
    context = {
        'username': username,
        'room': room,
        'room_details': room_details,
        'roomList':roomList,
        'userList':userList,
    }
    return render(request, 'posts/room.html', context)



# creer nouveau slaon de chat
def createRoom(request, u1, u2, title):
    user1 = User.objects.get(id=u1).last_name
    user2 = User.objects.get(id=u2).last_name
    room = title+'_'+u1+'_'+u2
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user1)
    else:
        new_room = Room.objects.create(name=room, user1=user1, user2=user2)
        new_room.save()
        return redirect('/'+room+'/?username='+user1)


# envoyer un message
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


# récupérer la liste des message d'un salon
def getMessages(request, room):
    inv = ""
    room_details = Room.objects.get(name=room)
    for u in User.objects.all():
        if room_details.user1 == u.last_name:
            inv = Investisseur.objects.get(id=u.investisseur.id)
    photo = inv.photoProfil.url
    messages = Message.objects.filter(room=room_details.id)
    context = {"messages":list(messages.values()), 'photo':photo}
    return JsonResponse(context)





# ========================== COMMENTS =====================


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
