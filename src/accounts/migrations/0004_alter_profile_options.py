# Generated by Django 4.1.7 on 2023-04-09 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'プロフィール', 'verbose_name_plural': 'プロフィール'},
        ),
    ]
