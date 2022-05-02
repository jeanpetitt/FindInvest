# Generated by Django 4.0.1 on 2022-05-01 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('photoProfil', models.ImageField(blank=True, upload_to=users.models.renommer_image)),
                ('question', models.CharField(max_length=100)),
                ('reponse', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('objectifs', models.CharField(max_length=500)),
                ('entreprise', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('photoProfil', models.ImageField(blank=True, upload_to=users.models.renommer_image)),
                ('question', models.CharField(max_length=100)),
                ('reponse', models.CharField(max_length=100)),
                ('niveauEtude', models.CharField(choices=[('BAC + 1', 'BAC + 1'), ('BAC + 2', 'BAC + 2'), ('BAC + 3', 'BAC + 3'), ('BAC + 4', 'BAC + 4'), ('BAC + 5', 'BAC + 5'), ('Doctorant', 'Doctorant')], default='BAC + 1', max_length=100)),
                ('universite', models.CharField(max_length=200)),
                ('fiche_inscription', models.FileField(blank=True, upload_to=users.models.renommer_fichier)),
                ('bio', models.TextField(max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
