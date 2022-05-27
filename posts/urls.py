from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('accueil', accueil, name="accueil"),
    #path('publier', publierProjet, name='publier')

    path('delete/<str:pk>', delete_post, name='delete'),
    path('update_post/<str:pk>', update_post, name='update'),
]
