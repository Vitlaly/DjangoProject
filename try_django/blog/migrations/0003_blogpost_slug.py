# Generated by Django 3.0.8 on 2020-08-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-wold'),
            preserve_default=False,
        ),
    ]
