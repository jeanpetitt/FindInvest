# Generated by Django 4.1 on 2022-09-24 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_etu_room_etudiant_rename_inv_room_invest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='value',
            new_name='values',
        ),
    ]
