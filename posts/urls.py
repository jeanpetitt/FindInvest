from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('accueil', accueil, name="accueil"),

    path('delete_post/<str:pk>', delete_post, name='delete_post'),

    path('update_post/<str:pk>', update_post, name='update_post'),
    path('comment', commenterPublication, name='comments'),

    path('create_post', create_post, name='create_post'),
    path('list_projects', list_projects, name='list_projects'),
]
