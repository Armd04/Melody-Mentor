# Generated by Django 4.2.3 on 2023-08-01 10:40

import karaoke.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KaraokeSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_code', models.CharField(max_length=8, default='', null=False)),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('lyrics', models.TextField()),
                ('mp3_file', models.FileField(null=True, upload_to='karaoke-songs/')),
            ],
        ),
    ]
