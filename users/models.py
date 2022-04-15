from django.db import models
from django.contrib.auth.models import User
import os


def load_image(instance, filename):
    upload_to = 'image/'
    external = filename.split('.')[-1]
    if instance.email:
        filename = "photo_profile/{}.{}".format(instance.email, external)
        return os.path.join(upload_to, filename)

# creation de la Classe Utilsteur
class Utilisateur(models.Model):
    Type_User = [
        ('Investisseur', 'Investisseur'),
        ('Etudiant', 'Etudiant'),

    ]

    ville = models.CharField(max_length=200, null=True)
    photo_profile = models.ImageField('Profile', upload_to=load_image ,blank=True)
    tel = models.IntegerField('telephone')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type_user = models.CharField('type user', max_length=20, choices=Type_User, null=True, default='Etudiant')

    # s'inscrire sur la platefoerme
    def register():
        pass
    
    # s'authentifier à son compte
    def login():
        pass
    #l'utilisateur peut modifier son profile
    def updateProfil():
        pass

    # consulter
    def consultProfil():
        pass

    #commenter une publication
    def commentPost():
        pass
    
    #liker un post
    def likerPost():
        pass

    # partager 
    def sharePost():
        pass

    # rechercher u
    def searchProjecet():
        pass

    # suivre un etudiant
    def followsStudent():
        pass

    # ajouter un projet comme favoris

    def appendFavoritProject():
        pass
    


    class Meta:
        abstract = True

# creation de la Classe Etudiant

class Etudiant(Utilisateur):
    niveau = [
        ('Licence 1', 'Licence 1'),
        ('Licence 2', 'Licence 2'),
        ('Licence 3', 'Licence 3'),
        ('Master I',  'Master I'),
        ('Master II', 'Master II'),
        ('Doctorant', 'Doctorant'),
    ]
    niveauEtude = models.CharField("Niveau D'Etude", choices=niveau, default='Licence 1', max_length=30)
    universite = models.CharField(max_length=100)
    fiche_inscription = models.FileField(upload_to=load_image)
    bio = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.user.username

    # l'etudiant redefini la methode register
    def register():
        pass

    # etudiant poste un projet
    def postProjet():
        pass

# creation de la classe Investisseur

class Investisseur(Utilisateur):
    profession = models.CharField(max_length=70)
    entreprise = models.CharField(max_length=100)
    objectif = models.CharField(max_length=500)

    # un etudiant peut avoir plusieurs relations avec un investisseur et vis-vers-sa
    etudiant = models.ManyToManyField(Etudiant, related_name='investisseurs', blank=True)

    def __str__(self):
        return self.user.username

    # l'investisseur redefini la methode register
    def register():
        pass

    # l'investisseur marque un projet investir
    def investProject():
        pass
