# Generated by Django 4.0.1 on 2022-04-15 23:09

from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('categorie', models.CharField(max_length=200)),
                ('media', models.FileField(upload_to=posts.models.load_media)),
                ('description', models.TextField(max_length=500, null=True)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.etudiant')),
                ('investisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.investisseur')),
            ],
        ),
    ]
