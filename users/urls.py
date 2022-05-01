from django.urls import path
from .views import *

urlpatterns = [
    path('register_student', register_student, name="register_student"),
    path('register_investor', register_investor, name="register_investor"),
]
