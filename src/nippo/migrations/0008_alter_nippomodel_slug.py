# Generated by Django 4.1.7 on 2023-04-21 09:19

from django.db import migrations, models
import nippo.models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0007_nippomodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippomodel',
            name='slug',
            field=models.SlugField(default=nippo.models.slug_maker, max_length=20, unique=True),
        ),
    ]