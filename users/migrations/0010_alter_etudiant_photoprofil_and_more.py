# Generated by Django 4.0.1 on 2022-05-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_etudiant_photoprofil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='photoProfil',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='image/profile_pics/'),
        ),
        migrations.AlterField(
            model_name='investisseur',
            name='photoProfil',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='image/profile_pics/'),
        ),
    ]
