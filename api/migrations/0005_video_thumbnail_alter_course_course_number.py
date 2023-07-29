# Generated by Django 4.2.3 on 2023-07-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_course_course_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='video_thumbnails'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(default=1000),
        ),
    ]
