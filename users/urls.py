from django.urls import path

from .views import *

urlpatterns = [
    path('register_student', register_student, name="register_student"),
    path('register_investor', register_investor, name="register_investor"),
    path('signup', signup, name='signup'),
    path('signup/student_investor',student_signup, name='student_signup'),
    path('signup/investor_registor/<str:pk>', investor_signup, name='investor_signup')
]
