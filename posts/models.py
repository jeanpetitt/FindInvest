from django.db import models
from users.models import Etudiant
import os
from PIL import Image
from django.utils import timezone

# creation de la classe Projet

def load_media(instance, filename):
    upload_to = 'media/'
    external = filename.split('.')[-1]
    if instance.email:
        filename = "media_name/{}.{}".format(instance.email, external)
        return os.path.join(upload_to, filename)


class Projet(models.Model):
    INVESTI = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    title = models.CharField(max_length=200, null=True)
    categorie = models.CharField(max_length=200)
    media = models.FileField(upload_to='documents/post_doc/', blank=True)
    image1 = models.ImageField(upload_to='image/post_image/', blank=True)
    image2 = models.ImageField(upload_to='image/post_image/', blank=True)
    image3 = models.ImageField(upload_to='image/post_image/', blank=True)
    investi = models.CharField(choices=INVESTI, default='Non', max_length=10, blank=True)

    description = models.TextField(max_length=500, null=True)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projet')
    date_post = models.DateTimeField(default=timezone.now, blank=True)


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