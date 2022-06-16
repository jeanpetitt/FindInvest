# Generated by Django 4.0.1 on 2022-05-09 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_alter_etudiant_photoprofil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investisseur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='envestisseur', to=settings.AUTH_USER_MODEL),
        ),
    ]