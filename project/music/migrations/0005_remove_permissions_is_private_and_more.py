# Generated by Django 4.2.1 on 2023-05-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_musics_music_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='permissions',
            name='is_protected',
        ),
        migrations.RemoveField(
            model_name='permissions',
            name='is_public',
        ),
        migrations.AddField(
            model_name='musics',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
