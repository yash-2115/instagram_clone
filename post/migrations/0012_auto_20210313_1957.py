# Generated by Django 3.1.5 on 2021-03-13 14:27

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20210313_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilecontent',
            name='file',
            field=models.FileField(upload_to=post.models.user_directory_path),
        ),
    ]
