# Generated by Django 5.0.3 on 2024-05-09 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_genres_singer_remove_music_genres_alter_music_singer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='music.genres'),
        ),
        migrations.AlterField(
            model_name='music',
            name='singer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.singer'),
        ),
    ]
