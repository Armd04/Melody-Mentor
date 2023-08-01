# Generated by Django 4.2.3 on 2023-08-01 11:17

from django.db import migrations, models
import karaoke.models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karaokesong',
            name='song_code',
            field=models.CharField(default=karaoke.models.generate_unique_song_code, max_length=8),
        ),
    ]
