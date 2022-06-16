from cgitb import text
from turtle import title
from django.db import models
from users.models import Etudiant
import os
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

# creation de la classe Projet

 


def posts_image(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    listExt = ['png', 'jpg', 'tif', 'bmp', 'jpeg', 'gif']
    if instance.etudiant.user.username:
        noms = instance.etudiant.user.last_name.split(' ')
        idUser = instance.etudaint.id
        n = ""
        nom_image = ""
        for nom in noms:
            n += ("_"+nom)
        nom_image = (str(idUser)+n)
        filename = "post_image/{}.{}".format(nom_image, listExt)
        return os.path.join(upload_to, filename)


class Projet(models.Model):
    INVESTI = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    title = models.CharField('Titre du Projet', max_length=200, null=True)
    categorie = models.CharField('categorie projet', max_length=200)
    media = models.FileField(upload_to='documents/post_doc/', blank=True)
    image = models.ImageField(upload_to='images/post_image/', blank=True, default="default.jpeg")
    investi = models.CharField(choices=INVESTI, default='Non', max_length=10, blank=True)

    description = models.TextField(max_length=500, null=True)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projet')
    date_post = models.DateTimeField('date de publication',default=timezone.now, blank=True)


    def __str__(self):
        return  f'{self.etudiant.user.last_name} Post- {self.title}'
"""
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        path = 'image/post_image'
        img1 = Image.open(self.image1.path)
        img2 = Image.open(self.image2.path)
        img3 = Image.open(self.image3.path)
        if (img1.height > 400 or img1.width > 400) or (img2.height > 400 or img2.width > 400) or (img3.height > 400 or img3.width > 400):
            output_size = (300, 300)

            # enregistrement image1
            img1.thumbnail(output_size)
            img1.save(self.image1.path)
            # enregistrement image 2
            img2.thumbnail(output_size)
            img2.save(self.image2.path)
            #enregistrement image 3
            img3.thumbnail(output_size)
            img3.save(self.image3.path)

    """
    
class Comment(models.Model):
    
    texte = models.CharField(max_length=600)
    date_comment = models.DateTimeField(auto_now_add=timezone.now())
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="comments")
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    time_com = models.TimeField(auto_now_add=timezone.now())
 
    
    def __str__(self):
        return f'{self.user_comment} a commenter la publication {self.projet.title}'
   
    
        
class Reponse(models.Model):
    title_com = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reponses")
    texte = models.CharField(max_length=600)
    date_reponse = models.DateTimeField(auto_now_add=timezone.now())
    user_reponse = models.ForeignKey(User, on_delete=models.CASCADE)
    time_rep = models.TimeField(auto_now_add=timezone.now())
    
    def __str__(self):
        return f'{self.user_reponse} a repondu au commentaire de {self.title.user_comment.last_name} le {self.date_reponse}'