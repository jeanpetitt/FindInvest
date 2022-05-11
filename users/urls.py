from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name="login"),
    path('register_student', register_student, name="register_student"),
    path('register_investor', register_investor, name="register_investor"),
    path('update_profile/<str:id_e>', update_profile_student, name="update_profile_student"),
    path('update_profile_i/<str:id_i>', update_profile_investor, name="update_profile_investor"),
]
