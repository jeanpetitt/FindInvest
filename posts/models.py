from PIL import Image
from django.db import models
from users.models import *
from django.utils import timezone

# creation de la classe Projet

class Comment(models.Model):
    
    title = models.CharField(max_length=600, blank=False)
    
    def __str__(self):
        return self.title
    

class Projet(models.Model):
    INVESTI = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    title = models.CharField('Titre du Projet', max_length=200)
    categorie = models.CharField('categorie projet', max_length=200)
    media = models.FileField(upload_to='documents/post_doc/', blank=True)
    image = models.ImageField(upload_to='image/post_image/', default='post.jpg', blank=True)
    investi = models.CharField(choices=INVESTI, default='Non', max_length=10, blank=True)

    description = models.TextField(max_length=500)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projet')
    date_post = models.DateTimeField('date_post',default=timezone.now, blank=True)


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
    
