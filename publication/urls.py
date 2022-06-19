from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('comment', commentPost, name='comments'),
]