from django.urls import path
from .views import *

urlpatterns = [
    # connexion et déconnexion
    path('connexion', connexion, name="connexion"),
    path('déconnexion', user_logout, name="user_logout"),

    # réinitaliser mdp par question/reponse (non terminée)
    path('reset_password', reset_pwd, name="reset_pwd"),
    path('new_password', new_password, name="new_password"),

    # s'enregister et modfier son profil (étudiant et investisseur)
    path('register_student', register_student, name="register_student"),
    path('register_investor', register_investor, name="register_investor"),
    # path('update_profile/<str:id_e>', update_profile_student, name="update_profile_student"),
    path('update_profile', update_profile_student, name="update_profile_student"),
    path('profile_student/<str:id_e>', profile_student, name="profile_student"),
    # path('update_profile_i/<str:id_i>', update_profile_investor, name="update_profile_investor"),
    path('update_profile_i', update_profile_investor, name="update_profile_investor"),
    path('profile_investor/<str:id_i>', profile_investor, name="profile_investor"),

    # inscrition via github et google
    path('signup', signup, name='signup'),
    path('signup/student_register/<str:pk>',student_signup, name='student_signup'),
    path('signup/investor_register/<str:pk>', investor_signup, name='investor_signup'),
]
