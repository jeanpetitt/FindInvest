# Generated by Django 4.1 on 2022-09-24 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_rooms_message_room_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='etudiant',
            new_name='etud',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='invest',
            new_name='inv',
        ),
    ]