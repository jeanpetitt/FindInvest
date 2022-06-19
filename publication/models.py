from django.db import models
from posts.models import Projet
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
   
class Commentaire(models.Model):
    
    texte = models.CharField(max_length=600)
    date_comment = models.DateTimeField(auto_now_add=timezone.now())
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="comment")
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    time_com = models.TimeField(auto_now_add=timezone.now())
 
    
    def __str__(self):
        return f'{self.user_comment} a commenter la publication {self.projet.title}'
   
    
        
class Reponses(models.Model):
    title_com = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name="reponse")
    texte = models.CharField(max_length=600)
    date_reponse = models.DateTimeField(auto_now_add=timezone.now())
    user_reponse = models.ForeignKey(User, on_delete=models.CASCADE)
    time_rep = models.TimeField(auto_now_add=timezone.now())
    
    def __str__(self):
        return f'{self.user_reponse} a repondu au commentaire de {self.title_com.user_comment.last_name} le {self.date_reponse}'
    
  
class LikePost(models.Model):
    
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likeUser')
    nb_like = models.BigIntegerField('nombre de like', default=0)
    Projet_like = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='liskeProjet')

  