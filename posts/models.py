from django.db import models
from users.models import Etudiant, Investisseur
import os




# creation de la classe Projet

def load_media(instance, filename):
    upload_to = 'media/'
    external = filename.split('.')[-1]
    if instance.email:
        filename = "media_name/{}.{}".format(instance.email, external)
        return os.path.join(upload_to, filename)

class Projet(models.Model):
    title = models.CharField(max_length=200, null=True)
    categorie = models.CharField(max_length=200)
    media = models.FileField(upload_to=load_media)
    description = models.TextField(max_length=500, null=True)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    # un projet est investi par un seul investisseur
    investisseur = models.ForeignKey(Investisseur, on_delete=models.CASCADE)
