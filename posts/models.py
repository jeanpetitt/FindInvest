from django.db import models
from users.models import Etudiant, Investisseur
from django.utils import timezone
from django.contrib.auth.models import User

# creation de la classe Projet
class Projet(models.Model):
    INVESTI = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]
    CATHEGORIES = [
        ('INFORMATIQUE','INFORMATIQUE'),
        ('AGRICULTURE','AGRICULTURE'),
        ('ELEVAGE','ELEVAGE'),
        ('SANTE','SANTE'),
        ('AUTRES','AUTRES')
    ]    
    
    title = models.CharField('Titre du Projet', max_length=200)
    categorie = models.CharField('categorie projet', max_length=200)
    media = models.FileField(upload_to='documents/post_doc/', blank=True)
    image = models.ImageField(upload_to='', default='post.jpg', blank=True)
    investi = models.CharField(choices=INVESTI, default='Non', max_length=10, blank=True)

    description = models.TextField(max_length=500)
    # un projet ne concerne qu'un etudiant
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projet')
    date_post = models.DateTimeField('date_post',default=timezone.now, blank=True)


    def __str__(self):
        return  f'{self.etudiant.user.last_name} Post- {self.title}'


# model pour le Chat
class Room(models.Model):
    name = models.CharField(max_length=100)
    # inv = models.CharField(max_length=100)
    # etu = models.CharField(max_length=1000)
    inv = models.ForeignKey(Investisseur, on_delete=models.CASCADE, related_name="room")
    etu = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='room')
    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    # room = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')

    def __str__(self):
        return f'Msg de {self.user} le {self.date}'


# models pour le syst??me de commentaires

class Commentaire(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f'Commentaire de {self.user.last_name} pour {self.projet.title}'
    

class ComMessage(models.Model):
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name="contenus")
    auteur = models.CharField(max_length=100)
    id_projet = models.CharField(max_length=100, null=True)
    corps = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contenue du {self.auteur} le {self.date_added}'
    class Meta:
        ordering = ['-date_added']


class Reponse(models.Model):
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='reponses')
    auteur = models.ForeignKey(User, models.CASCADE)
    corps = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reponse de {self.auteur} au commentaire de {self.commentaire.auteur}'
    class Meta:
        ordering = ['-date_added']




# models l'ajout d'un projet en favoris

class Favoris(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='favoris')
    user = models.ForeignKey(User, models.CASCADE)
    nomFav = models.CharField(max_length=100)
    id_proj = models.CharField(max_length=100, null=True)
    id_usr = models.CharField(max_length=100, null=True)

