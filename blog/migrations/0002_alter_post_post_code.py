# Generated by Django 4.2.3 on 2023-08-07 13:21

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_code',
            field=models.CharField(default=blog.models.generate_unique_post_code, max_length=8),
        ),
    ]
