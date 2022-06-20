from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('accueil', accueil, name="accueil"),

    #  crud post
    path('delete_post/<str:pk>', delete_post, name='delete_post'),
    path('update_post/<str:pk>', update_post, name='update_post'),
    path('create_post', create_post, name='create_post'),
    path('list_projects', list_projects, name='list_projects'),

    # chat 
    path('<str:room>/', room, name="romm"),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
    path('createRoom/<str:u1>/<str:u2>/<str:title>', createRoom, name='createRoom'),

    # comment post
    path('comment', commenterPublication, name='comments'),

]
